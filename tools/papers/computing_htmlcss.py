#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Computing — HTML and CSS: four papers (A-D) and a mark-scheme booklet.

Every code listing printed in a question is run through a real checker (html.parser for the
HTML, a small CSS reader for the CSS) and every number is computed, not typed. _verify() runs
before any PDF is written; if it fails, nothing is built.
"""
import os, re, sys
from html.parser import HTMLParser
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import paper_lib as pl
from paper_lib import build_paper, build_scheme, AVAIL
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import Flowable, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfbase import pdfmetrics

OUT = os.path.join(ROOT, 'sheets')
EYEBROW = 'Base Camp · IGCSE Computing · Grade 7 · Unit 4 · Building a web page'
TOPIC = 'HTML and CSS'

# ======================================================================
#  1. CHECKERS
# ======================================================================
VOID = {'br', 'img', 'hr', 'meta', 'link', 'input'}
BLOCKS = {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'div', 'pre', 'table'}
BADALT = {'image', 'picture', 'photo', 'img', 'pic'}


class Lint(HTMLParser):
    """Counts the faults the papers are allowed to contain. One fault code per real fault."""
    def __init__(self):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.stack, self.faults, self.last_h = [], [], 0
        self.tree = []                                  # (tag, attrs) in document order
    def _start(self, tag, attrs):
        d = dict(attrs)
        raw = self.get_starttag_text() or ''
        if re.search(r'=\s*[^"\'\s>]', raw):
            self.faults.append('unquoted_attr:' + tag)
        top = self.stack[-1] if self.stack else None
        if tag in BLOCKS and 'p' in self.stack and top == 'p':
            self.faults.append('unclosed:p'); self.stack.pop(); top = self.stack[-1] if self.stack else None
        if tag == 'li':
            if top == 'li':
                self.faults.append('unclosed:li'); self.stack.pop(); top = self.stack[-1] if self.stack else None
            if top not in ('ul', 'ol'):
                self.faults.append('li_outside_list')
        elif top in ('ul', 'ol'):
            self.faults.append('non_li_in_list:' + tag)
        if re.fullmatch(r'h[1-6]', tag):
            lvl = int(tag[1])
            if lvl - self.last_h > 1:
                self.faults.append('heading_skip:' + tag)
            self.last_h = lvl
        if tag == 'a' and 'href' not in d:
            self.faults.append('a_src_not_href' if 'src' in d else 'a_no_href')
        if tag == 'img':
            if 'src' not in d:
                self.faults.append('img_href_not_src' if 'href' in d else 'img_no_src')
            if 'alt' not in d:
                self.faults.append('img_no_alt')
            else:
                v = (d['alt'] or '').strip().lower()
                if not v or v in BADALT or re.search(r'\.(jpe?g|png|gif|svg|webp)$', v):
                    self.faults.append('img_bad_alt')
        self.tree.append((tag, d))
        if tag not in VOID:
            self.stack.append(tag)
    def handle_starttag(self, tag, attrs):
        self._start(tag, attrs)
    def handle_startendtag(self, tag, attrs):
        self._start(tag, attrs)
        if tag not in VOID and self.stack and self.stack[-1] == tag:
            self.stack.pop()
    def handle_endtag(self, tag):
        if tag in VOID:
            self.faults.append('void_closed:' + tag); return
        if tag in self.stack:
            while self.stack[-1] != tag:
                self.faults.append('unclosed:' + self.stack.pop())
            self.stack.pop()
        else:
            self.faults.append('stray_end:' + tag)
    def finish(self):
        self.close()
        while self.stack:
            self.faults.append('unclosed:' + self.stack.pop())
        return self.faults


def lint(src):
    p = Lint(); p.feed(src)
    return sorted(p.finish())


def tree_of(src):
    """Nested structure [(tag, attrs, children|text)] for assertions about model answers."""
    class T(HTMLParser):
        def __init__(s):
            HTMLParser.__init__(s, convert_charrefs=True); s.root = ['#root', {}, []]; s.st = [s.root]
        def handle_starttag(s, tag, attrs):
            n = [tag, dict(attrs), []]; s.st[-1][2].append(n)
            if tag not in VOID: s.st.append(n)
        def handle_startendtag(s, tag, attrs):
            s.st[-1][2].append([tag, dict(attrs), []])
        def handle_endtag(s, tag):
            if tag in VOID: return
            for i in range(len(s.st) - 1, 0, -1):
                if s.st[i][0] == tag:
                    del s.st[i:]; break
        def handle_data(s, data):
            if data.strip(): s.st[-1][2].append(data.strip())
    t = T(); t.feed(src); return t.root


def find_all(node, tag):
    out = []
    for c in node[2]:
        if isinstance(c, list):
            if c[0] == tag: out.append(c)
            out.extend(find_all(c, tag))
    return out


def text_of(node):
    return ' '.join(c if isinstance(c, str) else text_of(c) for c in node[2]).strip()


def render(src):
    """What a browser would print, line by line: headings, paragraphs, <br>, bullet and numbered lists."""
    lines, cur, lists = [], [], []
    def flush():
        s = ''.join(cur).strip()
        if s: lines.append(s)
        cur[:] = []
    class R(HTMLParser):
        def handle_starttag(s, tag, attrs):
            if tag in ('p', 'h1', 'h2', 'h3', 'ul', 'ol'): flush()
            if tag in ('ul', 'ol'): lists.append([tag, 0])
            if tag == 'li':
                flush(); lists[-1][1] += 1
                cur.append('• ' if lists[-1][0] == 'ul' else '%d. ' % lists[-1][1])
            if tag == 'br': flush()
        def handle_endtag(s, tag):
            if tag in ('p', 'h1', 'h2', 'h3', 'li'): flush()
            if tag in ('ul', 'ol'): lists.pop()
        def handle_data(s, d):
            cur.append(re.sub(r'\s+', ' ', d))
    r = R(convert_charrefs=True); r.feed(src); r.close(); flush()
    return lines


# ---------------------------------------------------------------- CSS
NAMED = {'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'lime': (0, 255, 0),
         'green': (0, 128, 0), 'blue': (0, 0, 255), 'yellow': (255, 255, 0), 'maroon': (128, 0, 0),
         'navy': (0, 0, 128), 'darkblue': (0, 0, 139), 'darkred': (139, 0, 0), 'grey': (128, 128, 128),
         'silver': (192, 192, 192), 'orange': (255, 165, 0)}


def color_rgb(v):
    v = v.strip().lower()
    if v in NAMED: return NAMED[v]
    m = re.fullmatch(r'#([0-9a-f]{6})', v)
    if m: return tuple(int(m.group(1)[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r'#([0-9a-f]{3})', v)
    if m: return tuple(int(ch * 2, 16) for ch in m.group(1))
    m = re.fullmatch(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', v)
    if m and all(0 <= int(x) <= 255 for x in m.groups()): return tuple(int(x) for x in m.groups())
    return None


KNOWN_PROPS = {'color', 'background-color', 'text-align', 'font-family', 'width', 'height',
               'padding', 'margin', 'border'}


def parse_css(text):
    """-> (rules, faults). rules = [(selector, {prop: value})], invalid declarations dropped like a browser."""
    rules, faults = [], []
    for sel, body in re.findall(r'([^{}]+)\{([^{}]*)\}', text):
        decls = {}
        for d in body.split(';'):
            if not d.strip(): continue
            if ':' not in d:
                faults.append('no_colon'); continue
            prop, val = d.split(':', 1)
            prop, val = prop.strip().lower(), val.strip()
            ok = True
            if prop in ('colour', 'background-colour'):
                faults.append('prop_spelt:' + prop); ok = False
            elif prop not in KNOWN_PROPS:
                faults.append('unknown_prop:' + prop); ok = False
            elif ':' in val:
                faults.append('missing_semicolon'); ok = False
            elif prop in ('color', 'background-color'):
                if color_rgb(val) is None:
                    faults.append('bad_hex' if val.startswith('#') else 'bad_color:' + val); ok = False
            elif prop == 'text-align':
                if val not in ('left', 'right', 'center', 'justify'):
                    faults.append('value_spelt:' + val); ok = False
            if ok: decls[prop] = val
        rules.append((sel.strip(), decls))
    return rules, sorted(faults)


def computed(html, css):
    """Tag selectors only. Returns {tag: {'color':(r,g,b), 'text-align':...}} for every tag in the html."""
    rules, _ = parse_css(css)
    out = {}
    for tag in sorted({t for t, _ in Lint_tags(html)}):
        st = {'color': (0, 0, 0), 'text-align': 'left'}
        for sel, d in rules:
            if sel == tag:
                if 'color' in d: st['color'] = color_rgb(d['color'])
                if 'text-align' in d: st['text-align'] = d['text-align']
        out[tag] = st
    return out


def Lint_tags(html):
    p = Lint(); p.feed(html); p.close(); return p.tree


def expand4(val):
    v = [int(x.replace('px', '')) for x in val.split()]
    if len(v) == 1: return (v[0],) * 4
    if len(v) == 2: return (v[0], v[1], v[0], v[1])
    assert len(v) == 4, 'only 1, 2 or 4 values are taught'
    return tuple(v)


def box_of(css):
    """Parse one rule's box declarations -> dict of numbers (px). A border with no style draws nothing."""
    (sel, d), = parse_css(css)[0]
    px = lambda s: int(s.replace('px', ''))
    pad = expand4(d['padding']) if 'padding' in d else (0, 0, 0, 0)
    mar = expand4(d['margin']) if 'margin' in d else (0, 0, 0, 0)
    bw = 0
    if 'border' in d:
        parts = d['border'].split()
        if any(p in ('solid', 'dashed', 'dotted', 'double') for p in parts):
            bw = px(parts[0])
    return dict(w=px(d['width']) if 'width' in d else None, h=px(d['height']) if 'height' in d else None,
                pad=pad, bw=bw, mar=mar)


def total_w(b, w=None):
    w = b['w'] if w is None else w
    return w + b['pad'][1] + b['pad'][3] + 2 * b['bw'] + b['mar'][1] + b['mar'][3]


def total_h(b, h=None):
    h = b['h'] if h is None else h
    return h + b['pad'][0] + b['pad'][2] + 2 * b['bw'] + b['mar'][0] + b['mar'][2]


def visible_w(b, w=None):
    w = b['w'] if w is None else w
    return w + b['pad'][1] + b['pad'][3] + 2 * b['bw']


# ======================================================================
#  2. TYPESETTING HELPERS
# ======================================================================
def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def m(s, size=9.2):
    """Inline monospace for one short piece of code inside prose or a mark scheme."""
    return '<font name="Mono" size="%s">%s</font>' % (size, esc(s).replace(' ', '&nbsp;'))


def mc(src, size=8.6):
    """A multi-line code answer inside a mark-scheme entry."""
    rows = []
    for ln in src.strip('\n').split('\n'):
        lead = len(ln) - len(ln.lstrip(' '))
        rows.append('&nbsp;' * lead + esc(ln.lstrip(' ')).replace(' ', '&nbsp;'))
    return '<font name="Mono" size="%s">%s</font>' % (size, '<br/>'.join(rows))


MONO_CMAP = pdfmetrics.getFont('Mono').face.charToGlyph
PRINTED_CODE = []          # every listing, so _verify can check the font covers every character


class Code(Flowable):
    """A shaded, line-numbered code listing. Draws from the canvas, so nothing needs escaping."""
    SIZE, LEAD, PAD, GUT = 8.8, 12.6, 6, 20

    def __init__(self, src, start=1, numbers=True, hilite=()):
        Flowable.__init__(self)
        self.lines = src.strip('\n').split('\n')
        self.start, self.numbers = start, numbers
        PRINTED_CODE.append(src)
        self.gut = self.GUT if numbers else 0
        self.need = max(pdfmetrics.stringWidth(l, 'Mono', self.SIZE) for l in self.lines) + self.gut + 2 * self.PAD
        assert self.need < 395, ('code line too wide for the answer column', self.need, self.lines)
        self.height = len(self.lines) * self.LEAD + 2 * self.PAD - 3
    def wrap(self, aw, ah):
        self.w = min(aw, max(self.need + 10, 150))
        return self.w, self.height
    def draw(self):
        c = self.canv
        c.setFillColor(colors.HexColor('#F4F2F8')); c.setStrokeColor(pl.LINE); c.setLineWidth(0.6)
        c.roundRect(0, 0, self.w, self.height, 3, stroke=1, fill=1)
        if self.numbers:
            c.setStrokeColor(pl.RULE); c.line(self.GUT + 1, 3, self.GUT + 1, self.height - 3)
        y = self.height - self.PAD - self.SIZE + 1.5
        for i, ln in enumerate(self.lines):
            if self.numbers:
                c.setFont('Mono', 7); c.setFillColor(pl.SOFT)
                c.drawRightString(self.GUT - 5, y + 0.6, str(self.start + i))
            c.setFont('Mono', self.SIZE); c.setFillColor(pl.INK)
            c.drawString(self.gut + self.PAD - (0 if self.numbers else 0), y, ln)
            y -= self.LEAD


def code(src, **kw):
    return Code(src, **kw)


def hand(text, who):
    """Another student's handwriting: blue ink, italic, on a ruled card."""
    p = Paragraph('<font name="Body-Italic" size="10.2" color="#2B4C9E">%s</font>' % text, pl.S_Q)
    lab = Paragraph('<font name="Mono" size="7.4" color="#5A5A66">%s</font>' % who.upper(), pl.S_META)
    t = Table([[lab], [p]], colWidths=[395])
    t.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.6, pl.LINE), ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FBFAF4')),
                           ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                           ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 6)]))
    t.hAlign = 'LEFT'
    return t


class BoxDiagram(Flowable):
    """One element drawn as nested rectangles.
    mode 'label': four arrows (A-D), each ending in a blank for the student to name the layer.
    mode 'dims' : numbers printed on each layer, plus two dimension arrows (a) and (b) to be measured."""
    def __init__(self, mode, arrows=None, dims=None, h=60 * mm):
        Flowable.__init__(self)
        self.mode, self.arrows, self.dims, self.h = mode, arrows or [], dims or {}, h
    def wrap(self, aw, ah):
        self.w = min(aw, 400); return self.w, self.h
    def draw(self):
        c, W, H = self.canv, self.w, self.h
        dims = self.mode == 'dims'
        bw_ = W * (0.50 if dims else 0.52)
        x0, y0 = 6, (38 if dims else 8)
        ow, oh = bw_ - 12, H - y0 - 8
        MG, BD, PD = 13, 7, 15                               # drawn thickness of each layer (not to scale)
        INK, AMB, VIO = pl.INK, colors.HexColor('#A15208'), colors.HexColor('#4A3FB0')
        # margin
        c.setFillColor(colors.HexColor('#FBF0E1')); c.setStrokeColor(AMB); c.setLineWidth(0.9); c.setDash(3, 2)
        c.rect(x0, y0, ow, oh, fill=1, stroke=1); c.setDash()
        # border
        bx, by, bw, bh = x0 + MG, y0 + MG, ow - 2 * MG, oh - 2 * MG
        c.setFillColor(INK); c.setStrokeColor(INK); c.rect(bx, by, bw, bh, fill=1, stroke=0)
        # padding
        px, py, pw, ph = bx + BD, by + BD, bw - 2 * BD, bh - 2 * BD
        c.setFillColor(colors.HexColor('#E3DFF7')); c.rect(px, py, pw, ph, fill=1, stroke=0)
        # content
        cx, cy, cw, ch = px + PD, py + PD, pw - 2 * PD, ph - 2 * PD
        c.setFillColor(colors.white); c.setStrokeColor(pl.SOFT); c.setLineWidth(0.6); c.rect(cx, cy, cw, ch, fill=1, stroke=1)
        c.setStrokeColor(pl.LINE); c.setLineWidth(1.6)
        for k in range(3):
            yy = cy + ch - 9 - k * 8
            if yy > cy + 3: c.line(cx + 6, yy, cx + cw - 6 - (14 if k == 2 else 0), yy)
        # anchor points: the middle of each band, right-hand side
        anchor = {'margin': x0 + ow - MG / 2.0, 'border': bx + bw - BD / 2.0,
                  'padding': px + pw - PD / 2.0, 'content': cx + cw - 22}
        ranges = {'margin': (y0, y0 + oh), 'border': (by, by + bh), 'padding': (py, py + ph), 'content': (cy, cy + ch)}
        def dot(ax, y, col):
            c.setFillColor(colors.white); c.setStrokeColor(col); c.setLineWidth(1.1); c.circle(ax, y, 2.6, fill=1, stroke=1)
        if self.mode == 'label':
            ys = [H * 0.84, H * 0.64, H * 0.46, H * 0.30]
            lx = x0 + ow + 12
            for (letter, layer), y in zip(self.arrows, ys):
                lo, hi = ranges[layer]
                assert lo + 6 < y < hi - 6, ('arrow %s does not land inside the %s layer' % (letter, layer), y, lo, hi)
                ax = anchor[layer]
                c.setStrokeColor(INK); c.setLineWidth(0.8); c.line(ax, y, lx, y)
                dot(ax, y, INK)
                c.setFont('UI-Bold', 10); c.setFillColor(INK); c.drawString(lx + 4, y - 3.5, letter)
                c.setStrokeColor(pl.SOFT); c.setLineWidth(0.7); c.line(lx + 20, y - 4, W - 4, y - 4)
        else:
            d = self.dims
            names = [('margin', '%d px' % d['margin'], AMB), ('border', '%d px' % d['border'], INK),
                     ('padding', '%d px' % d['padding'], VIO), ('content', '%d px wide' % d['content'], pl.SOFT)]
            ys = [y0 + oh * 0.92, y0 + oh * 0.78, y0 + oh * 0.60, cy + ch * 0.45]
            lx = x0 + ow + 12
            for (nm, val, col), y in zip(names, ys):
                lo, hi = ranges[nm]
                assert lo + 6 < y < hi - 6, (nm, y, lo, hi)
                ax = anchor[nm]
                c.setStrokeColor(col); c.setLineWidth(0.8); c.line(ax, y, lx, y)
                dot(ax, y, col)
                c.setFont('UI-Bold', 9.4); c.setFillColor(pl.INK); c.drawString(lx + 4, y - 3.3, nm)
                c.setFont('Mono', 9.4); c.drawString(lx + 58, y - 3.3, val)
            # dimension arrows, with light extension lines so each one is clearly attached to its rectangle
            def dim(xa, xb, y, tag, ext_from):
                c.setStrokeColor(pl.LINE); c.setLineWidth(0.5); c.setDash(1.5, 1.5)
                for xx in (xa, xb): c.line(xx, ext_from, xx, y)
                c.setDash()
                c.setStrokeColor(pl.INK); c.setLineWidth(0.8); c.line(xa, y, xb, y)
                c.line(xa, y, xa + 4, y + 2.5); c.line(xa, y, xa + 4, y - 2.5)
                c.line(xb, y, xb - 4, y + 2.5); c.line(xb, y, xb - 4, y - 2.5)
                c.setFillColor(colors.white); c.setStrokeColor(pl.INK)
                mid = (xa + xb) / 2.0
                c.circle(mid, y, 6.5, fill=1, stroke=1)
                c.setFillColor(pl.INK); c.setFont('UI-Bold', 9); c.drawCentredString(mid, y - 3.2, tag)
            dim(x0, x0 + ow, 24, 'a', y0)
            dim(bx, bx + bw, 9, 'b', by)
            c.setFont('Body-Italic', 8); c.setFillColor(pl.SOFT)
            c.drawString(lx, 8, 'Not drawn to scale.')


# ---- let a question's text be a LIST of paragraphs and flowables (code, diagrams, handwriting)
_orig_qrow = pl._qrow


def _qrow2(num, text, marks, style=pl.S_Q, indent=0, numw=24):
    if not isinstance(text, (list, tuple)):
        return _orig_qrow(num, text, marks, style, indent, numw)
    mkw = 24
    cell = []
    for it in text:
        cell.append(Paragraph(it, style) if isinstance(it, str) else it)
        cell.append(Spacer(1, 4))
    cells = [Paragraph(num, pl.S_NUM) if num else '', cell,
             Paragraph('[%d]' % marks if marks else '', pl.S_MARKS)]
    t = Table([cells], colWidths=[numw, AVAIL - numw - mkw - indent, mkw])
    t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (0, 0), 5),
                           ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
    if indent:
        outer = Table([[t]], colWidths=[AVAIL])
        outer.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), indent), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                                   ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
        return outer
    return t


pl._qrow = _qrow2


def tick(opts):
    """Option strings that are code: monospace, escaped."""
    return [m(o, 9.6) for o in opts]

# ======================================================================
#  3. EVERY LISTING THAT APPEARS IN A QUESTION, AND EVERY MODEL ANSWER
# ======================================================================
# ---------------- Paper A
A_LINK = '<a href="about.html">About us</a>'
A_SKEL = """<!DOCTYPE html>
<html>
<head>
  <title>Meera's Bakery</title>
</head>
<body>
  <h1>Meera's Bakery</h1>
</body>
</html>"""
_sk = A_SKEL.split('\n')
A_SKEL_ANS = {3: _sk[2].strip(), 4: '<title>', 5: _sk[4].strip(), 6: _sk[5].strip()}
_sk[2] = '<______>'
_sk[3] = '  <______>Meera\'s Bakery</title>'
_sk[4] = '</______>'
_sk[5] = '<______>'
A_SKEL_BLANK = '\n'.join(_sk)

A_H = ("<h1>Meera's Bakery</h1>\n<h2>Opening hours</h2>\n<p>Open 7 am to 9 pm every day.</p>")
A_OL = "<ol>\n  <li>Boil water</li>\n  <li>Add tea</li>\n  <li>Pour</li>\n</ol>"
A_IMG = '<img src="kulfi.jpg" alt="Vendor selling pink kulfi from a steel cart">'
A_PREDICT = """<p>Doors open at 9.<br>Match starts at 10.</p>
<ol>
  <li>Toss</li>
  <li>Batting</li>
  <li>Tea</li>
</ol>"""
A_PREDICT_OUT = ['Doors open at 9.', 'Match starts at 10.', '1. Toss', '2. Batting', '3. Tea']
A_CSS = "h2 {\n  color: darkblue;\n  background-color: yellow;\n  text-align: center;\n}"
A_BOX = ".tag {\n  width: 100px;\n  padding: 10px;\n  border: 2px solid black;\n  margin: 8px;\n}"

# ---------------- Paper B
B_FIX = """<h1>Hampi Heritage Tours</h1>
<p>Visit the <a src="ruins.html">ruins</a>
<img src="temple.jpg">"""
B_FIX_FAULTS = ['a_src_not_href', 'img_no_alt', 'unclosed:p']
B_FIX_OK = ("<h1>Hampi Heritage Tours</h1>\n<p>Visit the <a href=\"ruins.html\">ruins</a></p>\n"
            "<img src=\"temple.jpg\" alt=\"Virupaksha Temple tower against a blue sky\">")
B_NAV = ("<ul>\n  <li><a href=\"index.html\">Home</a></li>\n  <li><a href=\"menu.html\">Menu</a></li>\n"
         "  <li><a href=\"contact.html\">Contact</a></li>\n</ul>")
B_PRED_HTML = "<h1>Chai Stop</h1>\n<p>Open till 10 pm</p>"
B_PRED_CSS = "h1 { color: green; text-align: right; }\np  { colour: blue; text-align: centre; }"
B_MARGIN = 'margin: 5px 10px 15px 20px;'
B_BOX = dict(content=120, padding=20, border=5, margin=10)
B_TICK_COLOR = ['colour: red;', 'color: red;', 'color = red;', 'text-color: red;']
B_TICK_LINK = ['<a src="menu.html">Menu</a>', '<a href="menu.html">Menu</a>',
               '<img href="menu.html">Menu</img>', '<a href="menu.html">Menu</link>']

# ---------------- Paper C
C_HTML = """<!DOCTYPE html>
<html>
<head>
  <title>Lalbagh Flower Show</title>
<body>
  <h1>Lalbagh Flower Show</h1>
  <h4>Dates</h4>
  <p>12 to 26 January.
  <ul>
    <li>Roses</li>
    <li>Orchids</li>
  </ul>
  <img href="tulip.jpg" alt="image">
</body>
</html>"""
C_HTML_FAULTS = ['heading_skip:h4', 'img_bad_alt', 'img_href_not_src', 'unclosed:head', 'unclosed:p']
C_HTML_FIX = C_HTML.replace('<body>', '</head>\n<body>').replace('<h4>Dates</h4>', '<h2>Dates</h2>') \
    .replace('January.\n', 'January.</p>\n').replace('<img href="tulip.jpg" alt="image">',
                                                     '<img src="tulip.jpg" alt="Red tulips in the Glass House">')
C_CSS = """h1 {
  colour: white;
  background-color: #00800;
  text-align: centre;
}
p {
  font-family: Georgia
  color: darkred;
}"""
C_CSS_FAULTS = ['bad_hex', 'missing_semicolon', 'prop_spelt:colour', 'value_spelt:centre']
C_CSS_FIX = """h1 {
  color: white;
  background-color: #008000;
  text-align: center;
}
p {
  font-family: Georgia, serif;
  color: darkred;
}"""
C_BOX = ".card {\n  width: 150px;\n  height: 60px;\n  padding: 10px 25px;\n  border: 4px solid black;\n  margin: 8px 0 8px 12px;\n}"
C_LOGO = '<a href="home.html"><img src="logo.png" alt="Green kite on a white circle"></a>'
C_RECIPE = """<h1>Masala Dosa</h1>
<img src="dosa.jpg" alt="Golden folded dosa with potato filling">
<h2>Ingredients</h2>
<ul>
  <li>Rice</li>
  <li>Urad dal</li>
  <li>Potato</li>
</ul>
<h2>Method</h2>
<ol>
  <li>Soak</li>
  <li>Grind</li>
  <li>Cook</li>
</ol>"""

# ---------------- Paper D
D_SKEL = """<!DOCTYPE html>
<html>
<head>
  <title>Jaipur Kites</title>
</head>
<body>
  <h1>Jaipur Kites</h1>
  <p>Festival on 14 January.</p>
</body>
</html>"""
D_COL = ".box {\n  width: ____px;\n  padding: 15px;\n  border: 5px solid black;\n  margin: 10px;\n}"
D_NOBORDER = 'border: 5px red;'
D_CSS = "p { font-family: Verdana, sans-serif; color: #008000; text-align: right; }"
D_PAGES = ['index.html', 'shop.html', 'contact.html']
D_NAV = ("<ul>\n  <li><a href=\"index.html\">Home</a></li>\n  <li><a href=\"shop.html\">Shop</a></li>\n"
         "  <li><a href=\"contact.html\">Contact</a></li>\n</ul>")
D_TRIPLE = dict(w=80, pad=10, bw=2, mar=6, col=360, mar2=10)
D_FIX = """<h1>Hampi Heritage Tours</h1>
<h2>Places to visit</h2>
<ul>
  <li><a src="virupaksha.html">Virupaksha Temple</a></li>
  <p>Vittala Temple</p>
</ul>
<img src="stone-chariot.jpg" alt="stone-chariot.jpg">"""
D_FIX_FAULTS = ['a_src_not_href', 'img_bad_alt', 'non_li_in_list:p']
D_FIX_OK = D_FIX.replace('src="virupaksha', 'href="virupaksha').replace(
    '<p>Vittala Temple</p>', '<li>Vittala Temple</li>').replace(
    'alt="stone-chariot.jpg"', 'alt="Stone chariot at Vittala Temple"')


# ======================================================================
#  4. VERIFICATION  (runs before any PDF is written)
# ======================================================================
def _verify():
    V = {}
    # ---------------- Paper A
    assert lint(A_LINK) == []
    t = find_all(tree_of(A_LINK), 'a')[0]
    assert t[1] == {'href': 'about.html'} and text_of(t) == 'About us'
    assert lint(A_SKEL) == [], lint(A_SKEL)
    sl = A_SKEL.split('\n'); bl = A_SKEL_BLANK.split('\n')
    assert [i + 1 for i in range(len(sl)) if sl[i] != bl[i]] == [3, 4, 5, 6]
    for ln, ans in A_SKEL_ANS.items():
        assert sl[ln - 1].strip().startswith(ans), (ln, ans)
    assert lint(A_SKEL_BLANK) != []                         # the blanked page really is broken
    assert lint(A_H) == [] and [n[0] for n in tree_of(A_H)[2]] == ['h1', 'h2', 'p']
    assert lint(A_OL) == [] and [text_of(n) for n in find_all(tree_of(A_OL), 'li')] == ['Boil water', 'Add tea', 'Pour']
    assert lint(A_IMG) == [] and 'kulfi.jpg' == tree_of(A_IMG)[2][0][1]['src']
    assert render(A_PREDICT) == A_PREDICT_OUT, render(A_PREDICT)
    assert lint(A_PREDICT) == []
    r, f = parse_css(A_CSS); assert f == [] and r[0][1] == {'color': 'darkblue', 'background-color': 'yellow', 'text-align': 'center'}
    b = box_of(A_BOX); V['A_total'] = total_w(b); V['A_vis'] = visible_w(b)
    V['A_wrong'] = b['w'] + 2 * b['pad'][1] + 2 * b['mar'][1]                # border left out
    V['A_once'] = b['w'] + b['pad'][1] + b['bw'] + b['mar'][1]               # each layer counted once
    assert (V['A_total'], V['A_vis'], V['A_wrong'], V['A_once']) == (140, 124, 136, 120)
    assert V['A_wrong'] != V['A_total'] and V['A_wrong'] not in (V['A_once'],)
    # ---------------- Paper B
    V['B_hex'] = {h: color_rgb(h) for h in ('#0000FF', '#800000', '#FFFF00')}
    assert V['B_hex'] == {'#0000FF': (0, 0, 255), '#800000': (128, 0, 0), '#FFFF00': (255, 255, 0)}
    assert '#%02X%02X%02X' % (0, 255, 0) == '#00FF00'
    assert expand4('5px 10px 15px 20px') == (5, 10, 15, 20)
    def works(decl): return bool(parse_css('p { %s }' % decl)[0][0][1])
    assert [works(x) for x in B_TICK_COLOR] == [False, True, False, False]
    assert [lint(x) == [] for x in B_TICK_LINK] == [False, True, False, False]
    assert lint(B_FIX) == B_FIX_FAULTS, lint(B_FIX)
    assert lint(B_FIX_OK) == []
    assert lint(B_NAV) == []
    nav = tree_of(B_NAV); lis = find_all(nav, 'li'); asx = find_all(nav, 'a')
    assert len(lis) == 3 and [a[1]['href'] for a in asx] == ['index.html', 'menu.html', 'contact.html']
    assert all(any(isinstance(ch, list) and ch[0] == 'a' for ch in li[2]) for li in lis)
    ev = computed(B_PRED_HTML, B_PRED_CSS)
    assert ev['h1'] == {'color': (0, 128, 0), 'text-align': 'right'}
    assert ev['p'] == {'color': (0, 0, 0), 'text-align': 'left'}                  # both p lines silently ignored
    assert parse_css(B_PRED_CSS)[1] == ['prop_spelt:colour', 'value_spelt:centre']
    d = B_BOX
    V['B_total'] = d['content'] + 2 * d['padding'] + 2 * d['border'] + 2 * d['margin']
    V['B_vis'] = d['content'] + 2 * d['padding'] + 2 * d['border']
    V['B_m200'] = (200 - V['B_vis']) // 2
    assert (V['B_total'], V['B_vis'], V['B_m200']) == (190, 170, 15) and (200 - V['B_vis']) % 2 == 0
    assert V['B_vis'] + 2 * V['B_m200'] == 200
    V['B_once'] = d['content'] + d['padding'] + d['border'] + d['margin']
    assert V['B_once'] == 155 and V['B_once'] != V['B_total']
    # ---------------- Paper C
    assert lint(C_HTML) == C_HTML_FAULTS, lint(C_HTML)
    assert lint(C_HTML_FIX) == [], lint(C_HTML_FIX)
    ln = C_HTML.split('\n')
    assert ln[4].strip() == '<body>' and ln[6].strip().startswith('<h4>') and ln[7].strip().startswith('<p>') \
        and ln[12].strip().startswith('<img'), 'fault line numbers moved'
    assert parse_css(C_CSS)[1] == C_CSS_FAULTS, parse_css(C_CSS)[1]
    assert parse_css(C_CSS_FIX)[1] == []
    cl = C_CSS.split('\n')
    assert cl[1].strip().startswith('colour') and '#00800;' in cl[2] and 'centre' in cl[3] and cl[6].strip() == 'font-family: Georgia'
    ev = computed('<h1>x</h1><p>y</p>', C_CSS)
    assert ev['p']['color'] == (0, 0, 0)                      # line 8 is spelt right but is swallowed
    assert computed('<h1>x</h1><p>y</p>', C_CSS_FIX)['p']['color'] == NAMED['darkred']
    assert color_rgb('#00800') is None and color_rgb('#008000') == (0, 128, 0)
    V['C_hex'] = (color_rgb('#FF8000'), '#%02X%02X%02X' % (0, 0, 128), color_rgb('#C0C0C0'))
    assert V['C_hex'] == ((255, 128, 0), '#000080', (192, 192, 192))
    b = box_of(C_BOX)
    V['C_tw'] = total_w(b); V['C_maxw'] = 300 - (total_w(b) - b['w']); V['C_th'] = total_h(b)
    assert (V['C_tw'], V['C_maxw'], V['C_th']) == (220, 230, 104)
    assert total_w(b, V['C_maxw']) == 300
    V['C_w_wrong1'] = b['w'] + 20 + 2 * 4 + 12                 # padding read as 10 left and right
    V['C_w_wrong2'] = b['w'] + 50 + 8 + 24                     # margin 12 both sides
    assert V['C_w_wrong1'] == 190 and V['C_w_wrong2'] == 232 and V['C_tw'] not in (190, 232)
    assert lint(C_LOGO) == []
    a = find_all(tree_of(C_LOGO), 'a')[0]; assert a[1]['href'] == 'home.html' and a[2][0][0] == 'img'
    assert lint(C_RECIPE) == []
    rt = tree_of(C_RECIPE)
    assert [n[0] for n in rt[2]] == ['h1', 'img', 'h2', 'ul', 'h2', 'ol'] and len(find_all(rt, 'li')) == 6
    assert [text_of(x) for x in find_all(find_all(rt, 'ol')[0], 'li')] == ['Soak', 'Grind', 'Cook']
    # ---------------- Paper D
    assert lint(D_SKEL) == []
    dt = tree_of(D_SKEL)
    assert find_all(dt, 'title')[0][2] == ['Jaipur Kites'] and len(find_all(find_all(dt, 'head')[0], 'title')) == 1
    bd = find_all(dt, 'body')[0]; assert [n[0] for n in bd[2]] == ['h1', 'p']
    b = box_of(D_COL.replace('____px', '0px'))
    V['D_w'] = 400 - (total_w(b) - b['w'])
    assert V['D_w'] == 340 and total_w(b, V['D_w']) == 400
    assert box_of('x { width: 10px; ' + D_NOBORDER + ' }')['bw'] == 0       # a border with no style draws nothing
    assert box_of('x { width: 10px; border: 5px solid red; }')['bw'] == 5
    r, f = parse_css(D_CSS); assert f == [] and color_rgb(r[0][1]['color']) == (0, 128, 0)
    assert r[0][1]['font-family'].split(',')[-1].strip() == 'sans-serif'
    V['D_links'] = len(D_PAGES) ** 2
    assert V['D_links'] == 9 and lint(D_NAV) == []
    assert [a[1]['href'] for a in find_all(tree_of(D_NAV), 'a')] == D_PAGES
    t = D_TRIPLE
    one = lambda mar: t['w'] + 2 * t['pad'] + 2 * t['bw'] + 2 * mar
    V['D_one'], V['D_three'], V['D_one2'], V['D_three2'] = one(t['mar']), 3 * one(t['mar']), one(t['mar2']), 3 * one(t['mar2'])
    assert (V['D_one'], V['D_three'], V['D_one2'], V['D_three2']) == (116, 348, 124, 372)
    assert V['D_three'] <= t['col'] < V['D_three2'] and V['D_three2'] - t['col'] == 12 and 3 * t['w'] == 240
    assert lint(D_FIX) == D_FIX_FAULTS, lint(D_FIX)
    assert lint(D_FIX_OK) == []
    V['D_neel'] = 120 + 2 * 10; V['D_right'] = 120 + 2 * 10 + 2 * 4
    assert (V['D_neel'], V['D_right']) == (140, 148) and V['D_neel'] != V['D_right']
    return V


def _check_fonts():
    assert PRINTED_CODE, 'no code listings were registered'
    for src in PRINTED_CODE:
        bad = sorted({ch for ch in src if ch != '\n' and ord(ch) not in MONO_CMAP})
        assert not bad, ('DejaVu Sans Mono cannot draw', bad)


V = _verify()

# ======================================================================
#  5. THE PAPERS
# ======================================================================
BASE = [
    'Answer <b>every</b> question in the space provided.',
    'This is a paper exam: <b>no computer and no calculator</b>. Write code by hand, exactly as you would type it. '
    'Every bracket, slash, colon and quote mark counts, and so does spelling.',
    'Unless a question says otherwise, use the <b>default box model</b>: ' + m('width') + ' sets the content only.',
    'The mark for each question is shown in square brackets on the right.',
]
REMINDER = ('<b>Reminder box</b><br/>'
            + '<font name="Mono" size="8.2">'
            + 'Tags:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;html head title body h1&ndash;h6 p br ul ol li a img<br/>'
            + 'Attributes:&nbsp;&nbsp;href (on a) &nbsp;src and alt (on img) &nbsp;style<br/>'
            + 'Properties:&nbsp;&nbsp;color background-color text-align font-family<br/>'
            + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;width height padding border margin<br/>'
            + 'Box layers, inside to outside: content, padding, border, margin<br/>'
            + 'Default box model: total width = content + 2&times;padding + 2&times;border + 2&times;margin'
            + '</font>')
INSTR_MED = BASE + [REMINDER]
INSTR_HARD = BASE + [
    'Several questions describe pages or situations you may not have seen before. You are not expected to recognise '
    'them: apply the ideas you already have.',
    'Nothing is printed here to remind you of tag names, attributes, properties or the box-model formula. '
    'That is deliberate: recalling them is part of what this paper tests.']


def P(label, text, marks, space=0, **kw):
    d = {'label': label, 'text': text, 'marks': marks}
    if space: d['space'] = space
    d.update(kw)
    return d


# ---------------------------------------------------------------- PAPER A
A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · No computer · No calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section': 'Section 1 — name the parts',
   'text': ["This is one link from the website of Meera's Bakery in Mysuru.", code(A_LINK),
            'Write down exactly which part of the code each of these is.'], 'marks': 4,
   'parts': [P('(a)', 'The opening tag', 1, 11),
             P('(b)', 'The attribute (its name only)', 1, 11),
             P('(c)', 'The value of that attribute', 1, 11),
             P('(d)', 'The word for the whole piece of code, from the opening tag to the closing tag', 1, 11)]},
  {'text': ["Here is the skeleton of the bakery's home page. Four tags have been left out: each one is a blank "
            + m('<______>') + '.', code(A_SKEL_BLANK),
            'Write the missing tag for each of lines 3, 4, 5 and 6.'], 'marks': 4,
   'grid': [['Line', 'The tag that belongs there'], ['3', ''], ['4', ''], ['5', ''], ['6', '']],
   'grid_widths': [AVAIL * 0.16, AVAIL * 0.5]},

  {'section': 'Section 2 — write it, read it',
   'text': "Write the HTML for the top of Meera's page. It needs, in this order:<br/>"
           "&bull;&nbsp; the main heading <b>Meera's Bakery</b><br/>&bull;&nbsp; a section heading <b>Opening hours</b><br/>"
           "&bull;&nbsp; a paragraph: <b>Open 7 am to 9 pm every day.</b>",
   'marks': 3, 'space': 36,
   'tip': 'Choose a heading level by where it sits in the outline of the page, not by how big you want the text.'},
  {'text': 'Write the HTML for a <b>numbered</b> list of the three steps for making chai, in this order: '
           '<b>Boil water</b>, <b>Add tea</b>, <b>Pour</b>.', 'marks': 3, 'space': 44},
  {'text': 'The bakery has a photo called <b>kulfi.jpg</b>. It shows a vendor on Brigade Road selling pink kulfi from a '
           'steel cart. Write the tag that puts the photo on the page, with both attributes every image needs.',
   'marks': 3, 'space': 26},
  {'text': ['A browser reads this code.', code(A_PREDICT),
            'Write out what appears on the screen, line by line, exactly as the browser would show it.'],
   'marks': 3, 'space': 46,
   'tip': 'Tags are instructions to the browser. They do not appear on the screen.'},

  {'section': 'Section 3 — the box and the skin',
   'text': ['The diagram shows one HTML element drawn as a box. Write the name of the layer that each arrow points to.',
            BoxDiagram('label', arrows=[('A', 'border'), ('B', 'content'), ('C', 'margin'), ('D', 'padding')])],
   'marks': 4},
  {'text': 'Write one CSS rule that makes the text of every <b>h2</b> dark blue, on a yellow background, and centred.',
   'marks': 3, 'space': 38, 'tip': 'Spell every word the way CSS spells it.'},
  {'text': ['Meera styles a price tag with this rule.', code(A_BOX, numbers=False)], 'marks': 3,
   'parts': [P('(a)', 'Work out the total width the tag takes up across the page.', 2, 28),
             P('(b)', 'Rahul works out the total as <b>136 px</b>. Which layer has he left out?', 1, 14)]},
 ]}

# ---------------------------------------------------------------- PAPER B
B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · No computer · No calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section': 'Section 1 — colours, spelling and the four sides',
   'text': 'Complete the table. Each empty box is worth one mark.', 'marks': 4,
   'grid': [['Colour', 'Hex', 'rgb'], ['blue', '#0000FF', ''], ['maroon', '#800000', ''],
            ['lime', '', 'rgb(0, 255, 0)'], ['yellow', '#FFFF00', '']],
   'grid_widths': [AVAIL * 0.2, AVAIL * 0.3, AVAIL * 0.4],
   'tip': 'Each pair of hex digits is one number. FF is 255, 80 is 128 and 00 is 0.'},
  {'text': 'Tick the <b>one</b> line that makes the text of a paragraph red.', 'marks': 1, 'tick': tick(B_TICK_COLOR)},
  {'text': 'Tick the <b>one</b> line that is a correct link to a page called menu.html.', 'marks': 1,
   'tick': tick(B_TICK_LINK)},
  {'text': ['This declaration sets the margin of a box.', code(B_MARGIN, numbers=False),
            'Write the size of each side of the margin in the table.'], 'marks': 4,
   'grid': [['Side', 'Margin (px)'], ['top', ''], ['right', ''], ['bottom', ''], ['left', '']],
   'grid_widths': [AVAIL * 0.2, AVAIL * 0.3],
   'tip': 'Four values go round the box clockwise, starting at the top.'},

  {'section': 'Section 2 — links, faults and predictions',
   'text': "Meera's Bakery has three pages: index.html, menu.html and contact.html. Write the HTML for a navigation list: "
           "an <b>unordered</b> list with three items, where each item is a link to one of the pages. "
           "Use the link texts Home, Menu and Contact.", 'marks': 4, 'space': 42},
  {'text': ['This part of a page for Hampi Heritage Tours has <b>three</b> faults.', code(B_FIX),
            'For each fault, write the line number and the corrected line.'], 'marks': 3, 'space': 25},
  {'text': ['A page contains this HTML and this CSS.', code(B_PRED_HTML, numbers=False), code(B_PRED_CSS, numbers=False),
            'In the table, write what the browser shows. Text colour: black, blue or green. '
            'Alignment: left, in the middle, or right.'], 'marks': 4,
   'grid': [['Element', 'Text colour', 'Alignment'], ['h1', '', ''], ['p', '', '']],
   'grid_widths': [AVAIL * 0.2, AVAIL * 0.3, AVAIL * 0.3]},

  {'section': 'Section 3 — measure the box',
   'text': ['Here is a box in the page, drawn from the middle outwards. Each layer is the same on all four sides.',
            BoxDiagram('dims', dims=B_BOX, h=64 * mm)], 'marks': 4,
   'parts': [P('(a)', 'Work out the total width the box takes up across the page (arrow <b>a</b>).', 2, 26),
             P('(b)', 'Work out the width of the visible box, to the outer edge of the border (arrow <b>b</b>).', 1, 18),
             P('(c)', 'Changing <b>only the margin</b>, what margin makes the total width exactly 200 px?', 1, 22)]},
  {'text': 'Priya makes price tags for her stall in Pune.', 'marks': 3,
   'parts': [P('(a)', 'The text touches the edge of the coloured tag. She wants a gap between the text and the edge, '
                       'with the colour filling the gap. Which layer should she increase? Give a reason.', 2, 28),
             P('(b)', 'Two tags touch each other. She wants an uncoloured gap between them. Which layer should she increase?',
               1, 16)]},
  {'text': 'Write the one CSS declaration that asks for the font Georgia, and says what the browser should use '
           'if the visitor does not have Georgia.', 'marks': 2, 'space': 22},
 ]}

# ---------------------------------------------------------------- PAPER C
C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · No computer · No calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section': 'Section 1 — from memory',
   'text': ['The diagram shows one element drawn as a box. Write the name of the layer that each arrow points to.',
            BoxDiagram('label', arrows=[('A', 'margin'), ('B', 'padding'), ('C', 'content'), ('D', 'border')])],
   'marks': 4},
  {'text': 'Convert these colours. Each answer is worth one mark.', 'marks': 3,
   'parts': [P('(a)', 'Write <b>#FF8000</b> as an rgb value.', 1, 12),
             P('(b)', 'Write <b>rgb(0, 0, 128)</b> as a hex code.', 1, 12),
             P('(c)', 'Write <b>#C0C0C0</b> as an rgb value.', 1, 12)]},
  {'text': 'The Chennai Chess Club website has a picture called <b>logo.png</b> showing a green kite on a white circle. '
           'Write the HTML that makes the <b>picture itself</b> the clickable link to a page called <b>home.html</b>. '
           'There must be no separate text link.', 'marks': 3, 'space': 30},

  {'section': 'Section 2 — find the faults',
   'text': ['This page for the Lalbagh Flower Show has <b>five</b> faults. Not all of them would make the browser complain.',
            code(C_HTML),
            'For each fault, write the line number, say what is wrong, and write the corrected line.'],
   'marks': 5, 'space': 80},
  {'text': ['Isha wrote this CSS. She wants the <b>h1</b> to have white text on a green background, centred, and the '
            '<b>p</b> to use Georgia with dark red text. Neither rule does anything at all.', code(C_CSS)],
   'marks': 5,
   'parts': [P('(a)', 'Find four faults. For each, write the line number and the corrected line.', 4, 46),
             P('(b)', 'Line 8 is spelt correctly, yet the paragraph text does not turn dark red. Explain why.', 1, 26)]},

  {'section': 'Section 3 — apply it to something new',
   'text': 'Write the HTML for the <b>body</b> of a recipe page, in this order:<br/>'
           '&bull;&nbsp; the main heading <b>Masala Dosa</b><br/>'
           '&bull;&nbsp; the picture <b>dosa.jpg</b>, which shows a golden folded dosa with potato filling<br/>'
           '&bull;&nbsp; a section heading <b>Ingredients</b>, then a <b>bulleted</b> list: Rice, Urad dal, Potato<br/>'
           '&bull;&nbsp; a section heading <b>Method</b>, then a <b>numbered</b> list of three steps: Soak, Grind, Cook<br/>'
           'You do not need the doctype, html, head or body tags.', 'marks': 5, 'space': 70},
  {'text': ['Kavya styles a card for a stall at Chickpet market.', code(C_BOX, numbers=False)], 'marks': 5,
   'parts': [P('(a)', 'Calculate the total <b>horizontal</b> space the card takes up.', 2, 24),
             P('(b)', 'The card sits in a column exactly 300 px wide. Changing only the width, what value makes the card '
                      'fill the column exactly?', 1, 14),
             P('(c)', 'Calculate the total <b>vertical</b> space the card takes up.', 2, 24)]},
 ]}

# ---------------------------------------------------------------- PAPER D
D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · No computer · No calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section': 'Section 1 — recall',
   'text': 'Write the complete HTML for a page with the title <b>Jaipur Kites</b> on the browser tab, a main heading '
           '<b>Jaipur Kites</b>, and one paragraph: <b>Festival on 14 January.</b> Include the line every page begins with.',
   'marks': 3, 'space': 64},
  {'text': 'Write one CSS rule for every <b>p</b>. It must use the font Verdana (with a safety net if the visitor does not '
           'have it), make the text the colour <b>rgb(0, 128, 0)</b> written as a <b>hex code</b>, and align the text '
           'to the right.', 'marks': 3, 'space': 40},

  {'text': ['A box in a page has this rule. The column it sits in is exactly 400 px wide.', code(D_COL, numbers=False)],
   'marks': 3,
   'parts': [P('(a)', 'Changing only the width, what value makes the box fill the column exactly?', 2, 30),
             P('(b)', ['Anil changes the border line to ' + m(D_NOBORDER) + ' and no border appears. Explain why not.'], 1, 22)]},

  {'section': 'Section 2 — build and calculate',
   'text': 'Jaipur Kites has three pages: index.html, shop.html and contact.html. Every page carries the same navigation '
           'list, with a link to each of the three pages, including itself.', 'marks': 5,
   'parts': [P('(a)', 'Write the navigation list that sits on shop.html. Use the link texts Home, Shop and Contact.', 3, 52),
             P('(b)', 'How many links are there in the whole site?', 1, 14),
             P('(c)', 'The shop page is renamed <b>store.html</b>. How many files must be edited so that every link still '
                      'works? Explain your answer.', 1, 22)]},
  {'text': 'Three identical boxes sit side by side in a container exactly 360 px wide. The only gaps between them are '
           'their own margins. Each box has ' + m('width: 80px;') + ' ' + m('padding: 10px;') + ' '
           + m('border: 2px solid black;') + ' and ' + m('margin: 6px;') + '.', 'marks': 6,
   'parts': [P('(a)', 'Calculate the total width one box takes up.', 2, 28),
             P('(b)', 'Calculate the total width of all three boxes. Do they fit in the container?', 2, 28),
             P('(c)', 'The margin is changed to <b>10px</b>; nothing else changes. Do the three boxes still fit? '
                      'Show how you know.', 2, 32)]},

  {'section': 'Section 3 — diagnose',
   'text': ['Arjun is building a page for Hampi Heritage Tours.', code(D_FIX)], 'marks': 4,
   'parts': [P('(a)', 'Find three faults. For each, write the line number and the corrected line.', 3, 38),
             P('(b)', 'Explain why the alt text on line 7 is no help to a visitor who cannot see the picture.', 1, 20)]},
  {'text': 'Two students have written these notes. <b>Both are wrong.</b> For each one, say what the mistake is and '
           'write the correct version.', 'marks': 6,
   'parts': [P('(i)', [hand('Padding and margin are the same thing, just two names. I put padding: 20px on my box to push '
                            'it away from the box next to it. Now there is a 20 px gap between the two boxes.',
                            "Divya's notebook")], 3, 40),
             P('(ii)', [hand('A border is only a line, so it adds nothing to the size. My box has width: 120px; '
                             'padding: 10px; border: 4px solid black. The visible box is 120 + 10 + 10 = 140 px wide.',
                             "Neel's notebook")], 3, 40)]},
 ]}

# ======================================================================
#  6. MARK SCHEMES   (one tagged line per mark)
# ======================================================================
T1 = ' <b>[1]</b>'
bA = box_of(A_BOX)
bB = B_BOX
bC = box_of(C_BOX)

SCHEMES = [
 {'title': 'Paper A — Medium', 'meta': '30 marks · 35 minutes', 'questions': [
  {'n': '1', 'marks': 4, 'lines': [
     '(a) ' + m(A_LINK[:21]) + ' &nbsp;(the whole opening tag, attribute included)' + T1,
     '(b) <b>href</b>' + T1,
     '(c) <b>about.html</b>, with or without the quote marks' + T1,
     '(d) <b>element</b>' + T1],
   'note': 'Tag, attribute, element: three words, and the exam uses all three. The usual slip is (d): answering "tag" for the '
           'whole piece. A tag is one half; an element is opening tag, content and closing tag together. For (a), "a" or '
           + m('<a>') + ' alone loses the mark, because the attribute is part of the opening tag.'},
  {'n': '2', 'marks': 4, 'lines': [
     'Line 3: ' + m('<head>') + T1, 'Line 4: ' + m('<title>') + T1,
     'Line 5: ' + m('</head>') + T1, 'Line 6: ' + m('<body>') + T1],
   'note': 'Line 5 is the one that catches people: the missing tag is a <i>closing</i> tag, and without the slash it is a '
           'different tag. On line 5, "head" or ' + m('<head>') + ' scores nothing. On lines 3, 4 and 6 accept the bare word '
           '(head, title, body) if it is clear which tag is meant. Capital letters are fine.'},
  {'n': '3', 'marks': 3, 'lines': [
     'Model answer:<br/>' + mc(A_H),
     m("<h1>Meera's Bakery</h1>") + T1,
     m('<h2>Opening hours</h2>') + ' &nbsp;(h2: a section sitting directly under the h1)' + T1,
     m('<p>Open 7 am to 9 pm every day.</p>') + T1],
   'note': 'The mistake this was built to catch is choosing a heading by its size. An h3 or h4 for "Opening hours" loses the '
           'second mark, however sensible it looks on screen: it skips the outline. Mark the tags, not the spelling of the words '
           'between them. A tag opened and never closed loses that line\'s mark. One line or three, any indentation, capitals: all fine.'},
  {'n': '4', 'marks': 3, 'lines': [
     'Model answer:<br/>' + mc(A_OL),
     '<b>ol</b> opening and closing tags (not ul)' + T1,
     'three <b>li</b> elements, each opened and closed, holding Boil water, Add tea and Pour in that order' + T1,
     'only li directly inside the list, and no typed numbers' + T1],
   'note': 'Typed numbers ("1. Boil water") lose the third mark: the browser counts for you, which is the whole point of an '
           'ordered list. A student who uses ul has built a bulleted list; take the first mark only and give the other two '
           'if the li structure is right. Items in the wrong order lose the second mark.'},
  {'n': '5', 'marks': 3, 'lines': [
     'Model answer: ' + m(A_IMG),
     'an <b>img</b> tag with <b>no closing tag</b> (' + m('<img … />') + ' is also accepted)' + T1,
     m('src="kulfi.jpg"') + ' &nbsp;(src, not href)' + T1,
     'an <b>alt</b> that describes the picture: pink kulfi, a vendor, a steel cart' + T1],
   'note': 'Three separate traps. ' + m('</img>') + ' or ' + m('<img>…</img>') + ' loses the first mark. ' + m('href') +
           ' for ' + m('src') + ' loses the second. For the third, "image", "photo", "kulfi" and "kulfi.jpg" all score nothing: '
           'they say nothing the visitor could not guess. Missing alt is the same. Attribute order does not matter; single '
           'or double quotes are both fine; no quotes at all loses the mark for that attribute.'},
  {'n': '6', 'marks': 3, 'lines': [
     'The browser shows: ' + ' &nbsp;/&nbsp; '.join(A_PREDICT_OUT),
     'the paragraph is on <b>two lines</b>, broken after "9." by the br' + T1,
     'the list is <b>numbered</b> 1, 2, 3 (not bullets)' + T1,
     'the items read Toss, Batting, Tea in order, with no tag visible anywhere on the screen' + T1],
   'note': 'Every wrong answer here comes from reading the code as typed instead of as drawn: ' + m('<br>') +
           ' printed on the screen, bullets for an ol, or the whole paragraph run onto one line. A student who ignores the br '
           'still gets the other two marks. Accept written lines or a drawn picture.'},
  {'n': '7', 'marks': 4, 'lines': [
     'A: <b>border</b>' + T1, 'B: <b>content</b> (accept "text")' + T1,
     'C: <b>margin</b>' + T1, 'D: <b>padding</b>' + T1],
   'note': 'The arrows are not in nesting order on purpose, so the answers cannot be guessed from the order they are printed in. '
           'The common slip is margin and padding swapped (C and D): withhold both and keep A and B. The reminder box gives the '
           'order of the layers, so none of this should be a guess.'},
  {'n': '8', 'marks': 3, 'lines': [
     'Model answer:<br/>' + mc(A_CSS),
     'selector <b>h2</b>, curly braces, and each declaration written as property, colon, value, semicolon' + T1,
     '<b>color</b> for the text and <b>background-color</b> for the yellow (any dark blue: darkblue, navy, #00008B, '
     'rgb(0, 0, 139); plain blue is also accepted)' + T1,
     m('text-align: center;') + T1],
   'note': 'British spelling is the target. ' + m('colour') + ' and ' + m('centre') + ' each lose their mark: CSS ignores both without a word '
           'of complaint, which is why the mistake survives. Swapping the two colours (color for the yellow) loses the second mark. '
           'A missing semicolon after the <i>last</i> declaration is legal CSS and is not penalised; a missing semicolon between two '
           'declarations loses the first mark. One line or several, any order, capitals in property names: all fine.'},
  {'n': '9', 'marks': 3, 'lines': [
     '(a) %d + 2×%d + 2×%d + 2×%d' % (bA['w'], bA['pad'][1], bA['bw'], bA['mar'][1]) + T1,
     '= %d + %d + %d + %d = <b>%d px</b>' % (bA['w'], 2 * bA['pad'][1], 2 * bA['bw'], 2 * bA['mar'][1], V['A_total']) + T1,
     '(b) the <b>border</b>' + T1 + ' &nbsp;(%d + %d + %d = %d)' % (bA['w'], 2 * bA['pad'][1], 2 * bA['mar'][1], V['A_wrong'])],
   'note': 'Forgetting the border is the commonest slip in this topic, which is why 136 is the printed wrong answer. The other '
           'wrong method to watch for is counting each layer once: %d + %d + %d + %d = %d. Award nothing for (a) and say why: every '
           'layer has two sides. Give the method mark for a correct sum with one slip in the addition. "px" need not be written.'
           % (bA['w'], bA['pad'][1], bA['bw'], bA['mar'][1], V['A_once'])},
 ]},

 {'title': 'Paper B — Medium', 'meta': '30 marks · 35 minutes', 'questions': [
  {'n': '1', 'marks': 4, 'lines': [
     'blue: <b>rgb(0, 0, 255)</b>' + T1, 'maroon: <b>rgb(128, 0, 0)</b>' + T1,
     'lime: <b>#00FF00</b>' + T1, 'yellow: <b>rgb(255, 255, 0)</b>' + T1],
   'note': 'The 80 = 128 conversion separates a student who understands base 16 from one who guesses. rgb(80, 0, 0) for maroon is '
           'the tell-tale wrong answer: each pair read as ordinary decimal. Accept rgb written without spaces and lower-case hex. '
           'A hex code without the # loses the mark: the # is part of the code.'},
  {'n': '2', 'marks': 1, 'lines': ['The second option, ' + m('color: red;') + T1],
   'note': 'The silent-failure trap. ' + m('colour: red;') + ' is the tempting one: the browser ignores it and the text stays black, '
           'with no error message. ' + m('color = red;') + ' has no colon; ' + m('text-color') + ' is not a property.'},
  {'n': '3', 'marks': 1, 'lines': ['The second option, ' + m('<a href="menu.html">Menu</a>') + T1],
   'note': 'Option 1 is href and src swapped; option 3 is an img with an href and a closing tag it must not have; option 4 opens '
           'with a and closes with link. One mark, no half marks.'},
  {'n': '4', 'marks': 4, 'lines': [
     'top: <b>5</b>' + T1, 'right: <b>10</b>' + T1, 'bottom: <b>15</b>' + T1, 'left: <b>20</b>' + T1],
   'note': 'Four values go clockwise from the top: 12, 3, 6, 9 o\'clock. The usual wrong answer reads them left to right as '
           'top, left, bottom, right (left 10, right 20). That still gets top and bottom right, so award those two marks only.'},
  {'n': '5', 'marks': 4, 'lines': [
     'Model answer:<br/>' + mc(B_NAV),
     '<b>ul</b> opening and closing tags (an ol is a numbered list, and the question said unordered)' + T1,
     'three <b>li</b> elements, each opened and closed' + T1,
     'each li holds an <b>a</b> with <b>href</b> set to exactly index.html, menu.html and contact.html' + T1,
     'link texts Home, Menu, Contact between the opening and closing a tags' + T1],
   'note': 'This is the navigation bar of nearly every website, and the mark scheme is about nesting: ul, then li, then a. '
           'A link placed beside the li instead of inside it loses the second mark. A wrong file name loses the third. All three on '
           'one line, capitals, single quotes, any indentation: all fine.'},
  {'n': '6', 'marks': 3, 'lines': [
     'Line 2: ' + m('<a src="ruins.html">') + ' should be ' + m('<a href="ruins.html">') + T1,
     'Line 2: the <b>p</b> is never closed: add ' + m('</p>') + ' after the link' + T1,
     'Line 3: the img has no alt: add ' + m('alt="…"') + ' describing the picture' + T1],
   'note': 'One mark per fault, and the fault must be both found and corrected. The line number or a quotation of the line are both '
           'accepted. The missing ' + m('</p>') + ' is the one students miss, because the browser forgives it; the exam does not. '
           'An alt of "image", "photo" or "temple.jpg" is not a correction.'},
  {'n': '7', 'marks': 4, 'lines': [
     'h1 text colour: <b>green</b>' + T1, 'h1 alignment: <b>right</b>' + T1,
     'p text colour: <b>black</b>' + T1, 'p alignment: <b>left</b>' + T1],
   'note': 'Built around silent failure. ' + m('colour') + ' and ' + m('centre') + ' are British spellings, so the browser threw the whole p rule '
           'away: the paragraph stays black and left-aligned. A student who answers "blue, middle" has read what the CSS <i>meant</i>; '
           'the browser reads what it <i>says</i>. Mark the h1 pair independently of the p pair. The h1\'s right alignment does not '
           'reach the p.'},
  {'n': '8', 'marks': 4, 'lines': [
     '(a) %d + 2×%d + 2×%d + 2×%d' % (bB['content'], bB['padding'], bB['border'], bB['margin']) + T1,
     '= %d + %d + %d + %d = <b>%d px</b>' % (bB['content'], 2 * bB['padding'], 2 * bB['border'], 2 * bB['margin'], V['B_total']) + T1,
     '(b) %d + %d + %d = <b>%d px</b> (margin left out)' % (bB['content'], 2 * bB['padding'], 2 * bB['border'], V['B_vis']) + T1,
     '(c) (200 &minus; %d) &divide; 2 = <b>%d px</b>' % (V['B_vis'], V['B_m200']) + T1],
   'note': 'Counting each layer once gives %d for (a): no marks, because every layer has two sides. In (b), %d means the margin was '
           'included in the visible box. In (c), an answer of %d means the margin was treated as one-sided; the working 200 &minus; %d '
           '= %d is worth nothing without the halving.' % (V['B_once'], V['B_total'], 200 - V['B_vis'], V['B_vis'], 200 - V['B_vis'])},
  {'n': '9', 'marks': 3, 'lines': [
     '(a) <b>padding</b>' + T1,
     'it is the space <i>inside</i> the border, and the background colour fills it' + T1,
     '(b) <b>margin</b>: it is outside the border, so it pushes the neighbour away and is never coloured' + T1],
   'note': 'The two words are swapped in most wrong scripts. Award (b) independently of (a). A student who says "border" for (a) '
           'has noticed the gap but not the layer: no mark. For (a) the reason must say <i>inside</i> or mention the background colour.'},
  {'n': '10', 'marks': 2, 'lines': [
     'Model answer: ' + m('font-family: Georgia, serif;'),
     'the property <b>font-family</b> with Georgia as the first choice' + T1,
     'a <b>generic family</b> as the safety net: serif (sans-serif or monospace are also accepted)' + T1],
   'note': 'The generic family is the mark most students drop: if the visitor does not have Georgia, the browser needs something to '
           'fall back on. Accept quote marks round Georgia, and "Georgia, \'Times New Roman\', serif". ' + m('font:') + ' on its own is a '
           'different property and earns nothing. A missing semicolon on its own is not penalised here: it is the last thing written.'},
 ]},
]

SCHEMES += [
 {'title': 'Paper C — Hard', 'meta': '30 marks · 45 minutes', 'questions': [
  {'n': '1', 'marks': 4, 'lines': [
     'A: <b>margin</b>' + T1, 'B: <b>padding</b>' + T1, 'C: <b>content</b> (accept "text")' + T1, 'D: <b>border</b>' + T1],
   'note': 'No reminder box on this paper, so this is pure recall of the four layers. Same diagram as Paper A with the arrows '
           'pointing at different layers, so a student who memorised A\'s answers by position scores nothing. Margin and padding '
           'swapped is the usual error: withhold both marks.'},
  {'n': '2', 'marks': 3, 'lines': [
     '(a) <b>rgb(255, 128, 0)</b> &nbsp;(FF = 255, 80 = 8×16 = 128, 00 = 0)' + T1,
     '(b) <b>#000080</b> &nbsp;(128 = 8×16, so 80)' + T1,
     '(c) <b>rgb(192, 192, 192)</b> &nbsp;(C0 = 12×16 = 192)' + T1],
   'note': 'Two wrong methods to look for. Reading a pair as ordinary decimal gives rgb(255, 80, 0) for (a). Pasting decimal into hex gives '
           '#0000128 for (b), seven digits. Accept lower-case hex; the # is required. No calculator is needed: C is twelve, '
           'and 12×16 is the only multiplication in the question.'},
  {'n': '3', 'marks': 3, 'lines': [
     'Model answer: ' + m(C_LOGO, 8.2),
     'the <b>img</b> sits <i>inside</i> the <b>a</b>, between its opening and closing tags' + T1,
     '<b>href</b> on the a (home.html) and <b>src</b> on the img (logo.png), not swapped' + T1,
     'an <b>alt</b> that describes the picture: a green kite on a white circle' + T1],
   'note': 'Targets href/src and alt. alt="logo" or alt="logo.png" scores nothing: it names the file, it does not describe what is in it. '
           'An img placed beside the a (not inside it) loses the first mark only. A separate text link instead of the picture '
           'contradicts the question: first mark withheld. Single quotes, capitals, ' + m('/>') + ' on the img: all accepted.'},
  {'n': '4', 'marks': 5, 'lines': [
     'Line 5: the head is never closed: add ' + m('</head>') + ' before ' + m('<body>') + T1,
     'Line 7: ' + m('<h4>') + ' straight after the h1 skips levels: it should be ' + m('<h2>') + ' (structure, not size)' + T1,
     'Line 8: the <b>p</b> is never closed: add ' + m('</p>') + ' after "January." (anywhere before the ul)' + T1,
     'Line 13: <b>href</b> on an image: it must be ' + m('src="tulip.jpg"') + T1,
     'Line 13: ' + m('alt="image"') + ' describes nothing: needs a real description, e.g. "Red tulips in the Glass House"' + T1],
   'note': 'One mark per fault, found (line number or a quotation of the line) <i>and</i> corrected. Two of the five, the h4 and the alt, '
           'would never make a browser complain, so a student who tests by "does it show?" finds three. An h3 for line 7 is not '
           'accepted: it still skips h2. A student who spots "two faults on line 13" but fixes one earns one mark. The page '
           'was checked with a real parser: these five are the only faults it has.'},
  {'n': '5', 'marks': 5, 'lines': [
     'Fixed CSS:<br/>' + mc(C_CSS_FIX),
     '(a) Line 2: <b>colour</b> should be ' + m('color: white;') + T1,
     'Line 3: ' + m('#00800') + ' has five digits and a hex colour needs six: ' + m('#008000') + ' (any valid green)' + T1,
     'Line 4: ' + m('centre') + ' should be ' + m('text-align: center;') + T1,
     'Line 7: the semicolon after Georgia is missing: ' + m('font-family: Georgia;') + ' (or ' + m('Georgia, serif;') + ')' + T1,
     '(b) The missing semicolon makes the browser read lines 7 and 8 as <b>one</b> declaration it cannot understand, so it throws away '
     'both, including the correct ' + m('color: darkred;') + T1],
   'note': 'Both parts are one idea: CSS ignores whatever it cannot read and says nothing. In (a), the colour for line 3 may be any '
           'valid colour that is green: ' + m('#080') + ' or ' + m('lime') + ' are acceptable; seven digits are not. For (b), "because there is no '
           'semicolon" alone scores nothing: the mark is for saying that line 8 was swallowed along with line 7.'},
  {'n': '6', 'marks': 5, 'lines': [
     'Model answer:<br/>' + mc(C_RECIPE),
     '<b>h1</b> then two <b>h2</b>, so the outline has no skipped level' + T1,
     '<b>img</b> with src="dosa.jpg" and an alt that describes the dosa (not "image", "photo" or "dosa.jpg")' + T1,
     'Ingredients: a <b>ul</b> holding three li (Rice, Urad dal, Potato)' + T1,
     'Method: an <b>ol</b> holding three li in the order Soak, Grind, Cook' + T1,
     'every tag opened is closed and nested correctly, only li inside the lists, no typed numbers, and no closing tag on the img' + T1],
   'note': 'Almost all of these marks are for structure, not wording. A heading level other than h2 for the two sections is fine only if '
           'the outline stays unbroken (h1, h2, h2 is the only sensible answer). The last mark is the one most often lost: a forgotten '
           + m('</li>') + ' or ' + m('</ol>') + '. Extra doctype, html, head and body tags are harmless if they are correct. If the picture is placed elsewhere in the '
           'body, still award the list and structure marks.'},
  {'n': '7', 'marks': 5, 'lines': [
     '(a) padding left and right: 25 + 25 = 50' + T1,
     '%d + %d + %d + %d = <b>%d px</b> &nbsp;(width, padding, border 4 + 4, margin 12 + 0)' % (bC['w'], 50, 8, 12, V['C_tw']) + T1,
     '(b) 300 &minus; (50 + 8 + 12) = 300 &minus; 70 = <b>%d px</b>' % V['C_maxw'] + T1,
     '(c) vertical pairs: padding 10 + 10 = 20, border 4 + 4 = 8, margin 8 + 8 = 16' + T1,
     '%d + 20 + 8 + 16 = <b>%d px</b>' % (bC['h'], V['C_th']) + T1],
   'note': 'Two shorthands, two directions. ' + m('padding: 10px 25px') + ' is vertical first, so left and right are 25; reading it the other way '
           'gives %d for (a). ' % V['C_w_wrong1'] + m('margin: 8px 0 8px 12px') + ' runs top, right, bottom, left, so the right margin is 0; '
           'giving it 12 on both sides gives %d. Neither is close to %d, so the wrong methods show themselves. In (c) the left and '
           'right values are irrelevant: a student who adds 25 or 12 has not understood which direction is being measured. '
           'Give method marks for correct pairs even if the final addition slips.' % (V['C_w_wrong2'], V['C_tw'])},
 ]},
]

SCHEMES += [
 {'title': 'Paper D — Hard', 'meta': '30 marks · 45 minutes', 'questions': [
  {'n': '1', 'marks': 3, 'lines': [
     'Model answer:<br/>' + mc(D_SKEL),
     '<b>' + esc('<!DOCTYPE html>') + '</b> and the <b>html</b> element wrapped round everything' + T1,
     '<b>head</b> containing the <b>title</b> Jaipur Kites' + T1,
     '<b>body</b> containing the h1 and the p, correctly nested and closed' + T1],
   'note': 'The most reliable three marks on the paper and the most often thrown away. Usual losses: the title written in the body (so it '
           'never appears on the tab), the heading inside the head, or no closing html. The doctype may be in any case, but if it is '
           'missing, withhold the first mark.'},
  {'n': '2', 'marks': 3, 'lines': [
     'Model answer: ' + m(D_CSS, 8.2),
     'a rule of the right shape: selector p, curly braces, property, colon, value, semicolon' + T1,
     '<b>font-family</b> with Verdana first and a generic family last (sans-serif)' + T1,
     '<b>color: #008000;</b> (0, 128, 0 is 00, 80, 00) and <b>text-align: right;</b>' + T1],
   'note': 'The conversion is the point: 128 is 8×16 = 80 in hex. #00FF00 is lime (255); #00128 and #0012800 are decimal pasted into hex. '
           'The question demands a hex code, so "green" scores nothing for the colour. Accept lower-case hex. ' + m('colour') +
           ' and ' + m('right-align') + ' lose the third mark.'},
  {'n': '3', 'marks': 3, 'lines': [
     '(a) everything except the width: 2×15 + 2×5 + 2×10 = 30 + 10 + 20 = 60' + T1,
     '400 &minus; 60 = <b>%d px</b>' % V['D_w'] + T1,
     '(b) a border needs a <b>style</b> as well as a width: ' + m('5px red') + ' has none, so no border is drawn (' + m('border: 5px solid red;') + ' fixes it)' + T1],
   'note': 'The question asks the box to fit, not to be built. A student who ADDS the 60 and answers 460 has built the box: tell them to add '
           '340 + 60 and see. Subtracting only one layer gives 385 (padding once) or 395 (border once). In (b) "it needs a colour" is wrong: '
           'the colour is there. The word the mark scheme wants is style (or solid).'},
  {'n': '4', 'marks': 5, 'lines': [
     '(a) Model answer:<br/>' + mc(D_NAV),
     '<b>ul</b> with three <b>li</b>, each opened and closed' + T1,
     'each li holds an <b>a</b> with href exactly index.html, shop.html and contact.html' + T1,
     'link texts Home, Shop, Contact between the a tags' + T1,
     '(b) 3 pages × 3 links = <b>%d</b>' % V['D_links'] + T1,
     '(c) <b>3</b> files: all three pages carry a link to shop.html, the shop page itself included' + T1],
   'note': 'Part (b) is the answer to the cliffhanger at the end of lesson 6: how many links does a three-page site really need? Nine, and '
           'every one is typed by hand, which is why renaming one page means editing every page. In (c), 2 means the page forgot it links to itself; '
           '1 means the other two pages were forgotten. The number needs the reason to score.'},
  {'n': '5', 'marks': 6, 'lines': [
     '(a) 80 + 2×10 + 2×2 + 2×6 = 80 + 20 + 4 + 12' + T1,
     '= <b>%d px</b>' % V['D_one'] + T1,
     '(b) 3 × %d = <b>%d px</b>' % (V['D_one'], V['D_three']) + T1,
     '%d is less than 360, so they <b>do fit</b> (12 px to spare)' % V['D_three'] + T1,
     '(c) 80 + 20 + 4 + 20 = %d, and 3 × %d = <b>%d px</b>' % (V['D_one2'], V['D_one2'], V['D_three2']) + T1,
     '%d is more than 360, so they <b>do not fit</b>: 12 px too wide' % V['D_three2'] + T1],
   'note': 'The wrong method prints itself: 3 × 80 = 240 looks like 120 px to spare, when the real figure is 12. The question is also built so '
           'that forgetting the border flips part (c): without it each box is 80 + 20 + 20 = 120, three make exactly 360, and the student '
           'answers "fits". Award (b) and (c) independently and allow follow-through from a wrong (a), as long as the comparison with 360 is made.'},
  {'n': '6', 'marks': 4, 'lines': [
     '(a) Line 4: ' + m('<a src="virupaksha.html">') + ' should be ' + m('<a href="virupaksha.html">') + T1,
     'Line 5: a ' + m('<p>') + ' sits directly inside the ul: it must be ' + m('<li>Vittala Temple</li>') + T1,
     'Line 7: ' + m('alt="stone-chariot.jpg"') + ' is the file name: describe the picture, e.g. "Stone chariot at Vittala Temple"' + T1,
     '(b) a visitor who cannot see the picture would hear the file name, which says nothing about what is in it' + T1],
   'note': 'Three different slips from three lessons: href/src, a list with something other than li in it, and alt text that is only the '
           'file name. The page checks out clean once these are fixed. A student who deletes line 5 instead of changing it has lost content: no mark. '
           'For (b), "for search engines" on its own is not the reason; it has to be about the visitor who cannot see.'},
  {'n': '7', 'marks': 6, 'lines': [
     '(i) Padding is the space <b>inside</b> the border (the background fills it); margin is the space <b>outside</b>. They are different layers' + T1,
     'Padding only makes the coloured box bigger: the gap between the two boxes\' edges has not changed' + T1,
     'The correct property is <b>margin: 20px;</b>' + T1,
     '(ii) A border has thickness, so it <b>adds</b> to the size' + T1,
     'It adds on <b>both</b> sides: 2 × 4 = 8' + T1,
     '120 + 20 + 8 = <b>%d px</b> (not %d)' % (V['D_right'], V['D_neel']) + T1],
   'note': 'The standing question type: two wrong statements in another student\'s handwriting. Marking someone else\'s error is far easier to '
           'face than being told you made it, and it is the same thinking. Both statements are the topic\'s two big traps in confident prose. '
           'If he can name the mistake in Divya\'s and Neel\'s notes, he is unlikely to write them in his own. For (ii), 148 with no reason '
           'scores one mark; the reasoning is what is being tested.'},
 ]},
]


# ======================================================================
#  7. FINAL CHECKS ON THE SPECS, THEN BUILD
# ======================================================================
def _verify_specs():
    # CSS in Paper C: neither rule does anything, exactly as the question says
    assert all(not d for _, d in parse_css(C_CSS)[0]), 'C Q5 says neither rule does anything'
    # D Q5: forgetting the border flips part (c), as the mark scheme note claims
    t = D_TRIPLE
    assert 3 * (t['w'] + 2 * t['pad'] + 2 * t['mar2']) == t['col']
    assert 3 * (t['w'] + 2 * t['pad'] + 2 * t['bw'] + 2 * t['mar2']) > t['col']
    markup = re.compile(r'</?(b|i|font)\b[^>]*>|<br/>')
    for spec, sch in zip((A, B, C, D), SCHEMES):
        tot, sections = 0, 0
        for i, (q, sq) in enumerate(zip(spec['questions'], sch['questions']), 1):
            sections += 1 if q.get('section') else 0
            if q.get('parts'):
                assert sum(p['marks'] for p in q['parts']) == q['marks'], (spec['title'], i, 'parts')
            tot += q['marks']
            assert sq['n'] == str(i) and sq['marks'] == q['marks'], (spec['title'], i, 'scheme/paper mismatch')
            tagged = sum(int(x) for x in re.findall(r'<b>\[(\d+)\]</b>', ' '.join(sq['lines'])))
            assert tagged == sq['marks'], (spec['title'], i, 'tagged', tagged, sq['marks'])
            assert sq.get('note'), (spec['title'], i, 'every question needs a note')
            for s in sq['lines'] + [sq['note']]:                      # no raw angle bracket may reach the Paragraph parser
                left = markup.sub('', s)
                assert '<' not in left and '>' not in left.replace('&gt;', ''), (spec['title'], i, left[:80])
        assert tot == spec['marks'] == 30, (spec['title'], tot)
        assert sections == 3, (spec['title'], 'three named sections')
        assert sum(q['marks'] for q in sch['questions']) == 30
    assert 'both are wrong' in D['questions'][-1]['text'].lower()
    assert all('Reminder box' in ' '.join(s['instructions']) for s in (A, B))
    assert all('Reminder box' not in ' '.join(s['instructions']) for s in (C, D))
    assert all('may not have seen before' in ' '.join(s['instructions']) for s in (C, D))


def build():
    _verify_specs()
    _check_fonts()
    os.makedirs(OUT, exist_ok=True)
    files = []
    for spec, k in ((A, 'a'), (B, 'b'), (C, 'c'), (D, 'd')):
        p = os.path.join(OUT, 'computing-htmlcss-paper-%s.pdf' % k)
        build_paper(spec, p); files.append(p)
    p = os.path.join(OUT, 'computing-htmlcss-answers.pdf')
    build_scheme(SCHEMES, p, {
        'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
        'meta': 'Papers A to D · 30 marks each · tutor copy',
        'intro': 'Marks in square brackets show how the total is split: one tagged line per mark. Code is marked on what it does, not on '
                 'how it is laid out. <b>Always accept</b>: single or double quote marks round an attribute value; capitals in tag and property '
                 'names; any indentation, or the whole thing on one line; attributes in any order; ' + m('<br>') + ' or ' + m('<br/>') + ', and '
                 + m('<img … />') + ' as well as ' + m('<img …>') + '. <b>Never accept</b>: a missing quote mark (withhold the mark for that attribute), '
                 'a closing tag on img or br, ' + m('colour') + ' or ' + m('centre') + ' in CSS, or a hex code without the #. A missing semicolon '
                 'after the <i>last</i> declaration is legal CSS and is not penalised; a missing semicolon between two declarations is. '
                 'Mark the tags and properties, not the spelling of the words between them. Every code listing printed in these papers was run '
                 'through a parser when the papers were built, so each fault listed here is a real fault and the only one. The notes under each '
                 'answer name the mistake that question was built to catch.',
        'footer': 'Mark schemes · ' + TOPIC})
    files.append(p)
    return files


if __name__ == '__main__':
    print('\n'.join(build()))
