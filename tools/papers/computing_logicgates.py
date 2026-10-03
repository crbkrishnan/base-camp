#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Computing, Unit 3: Logic gates. Papers A to D and the mark-scheme booklet.

Everything that is a number in this file is computed, not typed:

  * every truth table printed on a paper or in the scheme comes from `col()`, which enumerates all
    input combinations through a gate evaluator (`ev`);
  * every circuit that is drawn is stored as a data structure (`Circ`) and drawn FROM that structure,
    so the picture, the expression and the table cannot disagree;
  * every scenario is also written once as a plain Python lambda (BEHAVIOUR), which knows nothing about
    gates. `_verify()` checks that the drawn circuit, the typed answer expressions (run through a port of
    the page's own expression parser) and the lambda all give the same column, and that every "decoy"
    differs from the right answer exactly as the mark scheme says.

paper_lib.py is not edited. It cannot embed a drawing, so build_paper2 / build_scheme2 below follow
the same layout code and add `fig`, `box`, `quote` and a reminder box.
"""
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, Flowable, KeepTogether)
from paper_lib import (AVAIL, INK, SOFT, LINE, PAPERBG, S_Q, S_NOTE, S_SEC, S_ANS, S_ANSN, S_MARKS,
                       S_META, S_EYEBROW, S_TITLE, Ruled, Rule, NumberedCanvas, _header, _qrow,
                       _tickboxes, MARGIN_L, MARGIN_R, MARGIN_T, MARGIN_B)

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Computer Science · Grade 7 · Unit 3 · Logic gates'
TOPIC = 'Logic Gates'

# =====================================================================================================
# 1. The evaluator. Rows are always in binary counting order, first input changing slowest.
# =====================================================================================================
def _gate(g, v):
    if g == 'AND':  return int(all(v))
    if g == 'OR':   return int(any(v))
    if g == 'NAND': return int(not all(v))
    if g == 'NOR':  return int(not any(v))
    if g == 'NOT':
        assert len(v) == 1, 'NOT has exactly one input'
        return int(not v[0])
    raise ValueError(g)

def V(name):            return ('v', name)
def G(g, *ins):         return ('g', g, tuple(ins))

def ev(node, env):
    if node[0] == 'v':
        return env[node[1]]
    return _gate(node[1], [ev(x, env) for x in node[2]])

def rows(n):
    return [tuple((i >> (n - 1 - k)) & 1 for k in range(n)) for i in range(2 ** n)]

def col(node, vars):
    return [ev(node, dict(zip(vars, r))) for r in rows(len(vars))]

def fcol(f, n):
    """Column of a plain Python function: the independent route, no gates involved."""
    return [int(f(*r)) for r in rows(n)]

def expr_str(node):
    """The page's own astStr: brackets everywhere except round a variable or a NOT of a variable."""
    def wrap(x):
        if x[0] == 'v' or (x[1] == 'NOT' and x[2][0][0] == 'v'):
            return expr_str(x)
        return '(' + expr_str(x) + ')'
    if node[0] == 'v':
        return node[1]
    if node[1] == 'NOT':
        return 'NOT ' + wrap(node[2][0])
    return (' ' + node[1] + ' ').join(wrap(x) for x in node[2])

def parse(src, vars):
    """Port of the page's parseExpr. NOT binds to the thing straight after it; two different gates at
    the same level need brackets; NAND and NOR take exactly two inputs. Raises ValueError otherwise."""
    toks = src.replace('(', ' ( ').replace(')', ' ) ').upper().split()
    OPS = ('AND', 'OR', 'NAND', 'NOR')
    pos = [0]
    def operand():
        t = toks[pos[0]] if pos[0] < len(toks) else None
        if t is None: raise ValueError('stops early: ' + src)
        if t == 'NOT':
            pos[0] += 1
            return G('NOT', operand())
        if t == '(':
            pos[0] += 1
            e = chain()
            if pos[0] >= len(toks) or toks[pos[0]] != ')': raise ValueError('bracket not closed: ' + src)
            pos[0] += 1
            return e
        if t in vars:
            pos[0] += 1
            return V(t)
        raise ValueError('unexpected %r in %r' % (t, src))
    def chain():
        items = [operand()]
        op = None
        while pos[0] < len(toks) and toks[pos[0]] in OPS:
            o = toks[pos[0]]
            if op and o != op: raise ValueError('brackets needed: ' + src)
            op = o
            pos[0] += 1
            items.append(operand())
        if op is None: return items[0]
        if op in ('NAND', 'NOR') and len(items) > 2: raise ValueError(op + ' takes two inputs: ' + src)
        return G(op, *items)
    ast = chain()
    if pos[0] != len(toks): raise ValueError('trailing tokens: ' + src)
    return ast

def cs(c):
    """A column as text: 0, 1, 1, 1"""
    return ', '.join(str(x) for x in c)

def rowlabels(n, idx):
    return ' and '.join(''.join(map(str, rows(n)[i])) for i in idx)

def ones_at(c, n):
    return [''.join(map(str, rows(n)[i])) for i, x in enumerate(c) if x == 1]

# =====================================================================================================
# 2. Circuits: stored as data, drawn from the data.
# =====================================================================================================
OUTW = {'AND': 52, 'OR': 52, 'NOT': 48, 'NAND': 60, 'NOR': 60}

class Circ(object):
    """gates: list of (id, type, [inputs], col, row). An input is a variable name or a gate id.
    An input of '_' is an unconnected stub (used to show a symbol on its own)."""
    def __init__(self, vars, var_rows, gates, out, out_name='Q', labels=None,
                 S=0.74, colw=98, rowh=44, x0=66):
        self.vars, self.var_rows, self.gates = vars, var_rows, gates
        self.out, self.out_name, self.labels = out, out_name, labels or {}
        self.S, self.colw, self.rowh, self.x0 = S, colw, rowh, x0
        self.byid = {g[0]: g for g in gates}

    def ast(self, ref=None):
        ref = ref or self.out
        if ref in self.vars:
            return V(ref)
        _, t, ins, _, _ = self.byid[ref]
        return G(t, *[self.ast(i) for i in ins])

    def gate_col(self, gid, vars=None):
        """Output column of one named gate: used for the intermediate columns of trace tables."""
        return col(self.ast(gid), vars or self.vars)

    def expr(self):
        return expr_str(self.ast())


class CircuitFig(Flowable):
    def __init__(self, circ, scale=0.88, show_labels=True):
        Flowable.__init__(self)
        self.circ, self.k, self.show_labels = circ, scale, show_labels
        c = circ
        allrows = list(c.var_rows.values()) + [g[4] for g in c.gates]
        self.rmin, self.rmax = min(allrows), max(allrows)
        self.pad = 22 * c.S + 3
        self.W0 = (c.x0 + max(g[3] for g in c.gates) * c.colw
                   + OUTW[[g for g in c.gates if g[0] == c.out][0][1]] * c.S + 28 + (16 if c.out_name else 0))
        self.H0 = (self.rmax - self.rmin) * c.rowh + 2 * self.pad
        self.width, self.height = self.W0 * scale, self.H0 * scale

    # ---- geometry
    def Y(self, row):
        return self.pad + (self.rmax - row) * self.circ.rowh
    def GX(self, colno):
        return self.circ.x0 + colno * self.circ.colw
    def pin_y(self, g, k):
        _, t, ins, cn, rw = g
        y = self.Y(rw)
        if len(ins) == 1:
            return y
        return y + (11 if k == 0 else -11) * self.circ.S
    def pin_x(self, g):
        return self.GX(g[3]) + (5 * self.circ.S if g[1] in ('OR', 'NOR') else 0)
    def out_x(self, g):
        return self.GX(g[3]) + OUTW[g[1]] * self.circ.S

    def _body(self, c, t, x, y):
        s = self.circ.S
        c.saveState()
        c.translate(x, y - 22 * s)
        c.scale(s, s)
        c.setLineWidth(1.5 / s)
        c.setStrokeColor(INK)
        c.setFillColor(colors.white)
        p = c.beginPath()
        if t in ('AND', 'NAND'):
            p.moveTo(0, 0); p.lineTo(26, 0); p.arcTo(0, 0, 52, 44, -90, 180); p.lineTo(0, 44); p.close()
        elif t in ('OR', 'NOR'):
            p.moveTo(0, 0); p.curveTo(16, 0, 38, 8, 52, 22); p.curveTo(38, 36, 16, 44, 0, 44)
            p.curveTo(9, 34, 9, 10, 0, 0); p.close()
        else:
            p.moveTo(0, 0); p.lineTo(40, 22); p.lineTo(0, 44); p.close()
        c.drawPath(p, fill=1, stroke=1)
        if t in ('NAND', 'NOR'):
            c.circle(56, 22, 4, stroke=1, fill=1)
        if t == 'NOT':
            c.circle(44, 22, 4, stroke=1, fill=1)
        c.restoreState()

    def draw(self):
        cv, circ = self.canv, self.circ
        cv.saveState()
        cv.scale(self.k, self.k)
        cv.setStrokeColor(INK); cv.setLineWidth(1.15); cv.setLineCap(0); cv.setLineJoin(0)

        # sources and their sinks
        def src_xy(s):
            if s in circ.vars:
                return 24, self.Y(circ.var_rows[s])
            g = circ.byid[s]
            return self.out_x(g), self.Y(g[4])
        sinks = {}
        for g in circ.gates:
            for k, s in enumerate(g[2]):
                if s == '_':
                    y = self.pin_y(g, k)
                    cv.line(self.pin_x(g) - 16, y, self.pin_x(g), y)
                    continue
                sinks.setdefault(s, []).append((self.pin_x(g), self.pin_y(g, k), g[3]))
        # one vertical channel per source, in the gap just left of the first column it feeds
        bycol = {}
        for s, sk in sinks.items():
            bycol.setdefault(min(x[2] for x in sk), []).append(s)
        chan = {}
        for cn, srcs in bycol.items():
            srcs.sort(key=lambda s: -src_xy(s)[1])
            for i, s in enumerate(srcs):
                chan[s] = self.GX(cn) - 10 - 5.5 * i
        for s, sk in sinks.items():
            sx, sy = src_xy(s)
            chx = chan[s]
            ys = [sy] + [p[1] for p in sk]
            cv.line(sx, sy, chx, sy)
            if max(ys) - min(ys) > 0.01:
                cv.line(chx, min(ys), chx, max(ys))
            for px, py, _ in sk:
                cv.line(chx, py, px, py)
            lo, hi = min(ys), max(ys)
            cv.setFillColor(INK)
            for y in set(round(v, 3) for v in ys):
                if lo + 0.05 < y < hi - 0.05:
                    cv.circle(chx, y, 1.9, stroke=0, fill=1)
        # variable terminals
        cv.setFillColor(INK)
        for v in circ.vars:
            y = self.Y(circ.var_rows[v])
            cv.setFont('Mono-Bold', 10.5)
            cv.drawRightString(14, y - 3.6, v)
        # final output
        og = circ.byid[circ.out]
        ox, oy = self.out_x(og), self.Y(og[4])
        cv.line(ox, oy, ox + 28, oy)
        if circ.out_name:
            cv.setFont('Mono-Bold', 10.5)
            cv.drawString(ox + 33, oy - 3.6, circ.out_name)
        # gates on top of the wires
        for g in circ.gates:
            self._body(cv, g[1], self.GX(g[3]), self.Y(g[4]))
            if g[2] == ['_', '_'] or g[2] == ['_']:
                ex = self.out_x(g)
                cv.line(ex, self.Y(g[4]), ex + 16, self.Y(g[4]))
        if self.show_labels:
            cv.setFillColor(SOFT)
            cv.setFont('Mono-Bold', 8.6)
            for gid, lab in circ.labels.items():
                g = circ.byid[gid]
                cv.drawString(self.out_x(g) + 3, self.Y(g[4]) + 4, lab)
        cv.restoreState()


class BlankBox(Flowable):
    """A dashed box for a hand-drawn circuit, with the inputs and output printed on its edges."""
    def __init__(self, vars, out='Q', h_mm=40, w=395, inner_note=None):
        Flowable.__init__(self)
        self.vars, self.out, self.w, self.h = vars, out, w, h_mm * mm
        self.width, self.height = w, self.h
        self.note = inner_note

    def draw(self):
        c = self.canv
        bx0, bx1 = 40, self.w - 40
        c.setStrokeColor(LINE); c.setLineWidth(0.9); c.setDash(3, 3)
        c.rect(bx0, 0, bx1 - bx0, self.h, stroke=1, fill=0)
        c.setDash()
        c.setStrokeColor(INK); c.setLineWidth(1.1); c.setFillColor(INK)
        n = len(self.vars)
        for i, v in enumerate(self.vars):
            y = self.h * (n - i) / (n + 1.0) if n > 0 else 0
            c.setFont('Mono-Bold', 10.5)
            c.drawRightString(14, y - 3.6, v)
            c.line(20, y, bx0, y)
        if self.out:
            y = self.h / 2.0
            c.line(bx1, y, bx1 + 22, y)
            c.setFont('Mono-Bold', 10.5)
            c.drawString(bx1 + 27, y - 3.6, self.out)
        if self.note:
            c.setFont('Body-Italic', 8.2); c.setFillColor(SOFT)
            c.drawCentredString((bx0 + bx1) / 2.0, 4, self.note)


S_CAPC = ParagraphStyle('capc', fontName='UI-Bold', fontSize=9.5, leading=12, alignment=1, textColor=INK)

def gate_only(t, S=0.9):
    return CircuitFig(Circ([], {}, [('g', t, ['_', '_'] if t != 'NOT' else ['_'], 0, 0)], 'g',
                           out_name=None, S=S, x0=22), scale=1.0)

def symbol_row(types, captions):
    figs = [gate_only(t) for t in types]
    cw = [AVAIL / len(types)] * len(types)
    cap = [Paragraph('<font name="UI-Bold" size="9.5">%s</font>' % c, S_CAPC) for c in captions]
    t = Table([figs, cap], colWidths=cw, rowHeights=[None, 14])
    t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
    return t

def panels(circs, captions, scale, cols=None):
    figs = [CircuitFig(c, scale=scale) for c in circs]
    n = len(figs)
    cols = cols or n
    cw = [AVAIL / cols] * cols
    cells_f, cells_c = [], []
    data, heights = [], []
    for r0 in range(0, n, cols):
        chunk = list(range(r0, min(n, r0 + cols)))
        data.append([Paragraph('<font name="UI-Bold" size="10">%s</font>' % captions[i], S_Q) for i in chunk]
                    + [''] * (cols - len(chunk)))
        data.append([figs[i] for i in chunk] + [''] * (cols - len(chunk)))
    t = Table(data, colWidths=cw)
    t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 1), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
    return t

# =====================================================================================================
# 3. Tables, boxes and the two build functions
# =====================================================================================================
S_CELL = ParagraphStyle('cell', fontName='Mono', fontSize=11, leading=13, alignment=1, textColor=INK)
S_HEAD = ParagraphStyle('head', fontName='UI-Bold', fontSize=9, leading=11, alignment=1, textColor=INK)
S_QUOTE = ParagraphStyle('quote', fontName='Body-Italic', fontSize=11, leading=16, textColor=colors.HexColor('#1F3A93'))
S_WHO = ParagraphStyle('who', fontName='Mono', fontSize=7.6, leading=10, textColor=SOFT)

def tt(vars, heads, prefill=None, blank_inputs=False, widths_mm=None, hdr_h=None, rowh=7.4,
       extra_rows=(), last_h=None):
    """Truth-table grid spec: inputs in counting order, answer columns blank unless prefilled."""
    n = len(vars)
    body = []
    for i, r in enumerate(rows(n)):
        left = ['' if blank_inputs else str(b) for b in r]
        right = []
        for j in range(len(heads)):
            if prefill and prefill[j] is not None:
                right.append(str(prefill[j][i]))
            else:
                right.append('')
        body.append(left + right)
    body += [list(x) for x in extra_rows]
    return {'rows': [list(vars) + list(heads)] + body, 'nin': n, 'widths_mm': widths_mm,
            'hdr_h': hdr_h, 'rowh': rowh, 'last_h': last_h}

def grid2(spec):
    rws = spec['rows']
    n = len(rws[0])
    wm = spec.get('widths_mm')
    widths = [w * mm for w in wm] if wm else [min(AVAIL / n, 19 * mm)] * n
    data = [[Paragraph(str(c), S_HEAD if i == 0 else S_CELL) for c in r] for i, r in enumerate(rws)]
    rh = spec.get('rowh', 7.4) * mm
    heights = [(spec['hdr_h'] * mm) if spec.get('hdr_h') else rh] + [rh] * (len(rws) - 1)
    if spec.get('last_h'):
        heights[-1] = spec['last_h'] * mm
    t = Table(data, colWidths=widths, rowHeights=heights, hAlign='LEFT')
    st = [('GRID', (0, 0), (-1, -1), 0.6, LINE), ('BACKGROUND', (0, 0), (-1, 0), PAPERBG),
          ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 2),
          ('RIGHTPADDING', (0, 0), (-1, -1), 2), ('TOPPADDING', (0, 0), (-1, -1), 2),
          ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]
    if 0 < spec.get('nin', 0) < n:
        st.append(('LINEAFTER', (spec['nin'] - 1, 0), (spec['nin'] - 1, -1), 1.4, INK))
    t.setStyle(TableStyle(st))
    return t

def quote_box(items, who):
    paras = [Paragraph('<font name="UI-Bold" color="#1F3A93">%s</font>&nbsp;&nbsp;%s' % (lab, txt), S_QUOTE)
             for lab, txt in items]
    data = [[Paragraph(who.upper(), S_WHO)]] + [[p] for p in paras]
    t = Table(data, colWidths=[AVAIL - 30], hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F6F4EC')),
                           ('LINEBEFORE', (0, 0), (0, -1), 2.2, colors.HexColor('#1F3A93')),
                           ('BOX', (0, 0), (-1, -1), 0.5, LINE),
                           ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                           ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    return t

def reminder_box(items):
    data = [[Paragraph('<font name="UI-Bold" size="9">%s</font>' % n, S_Q),
             Paragraph('<font name="Body" size="9.4">%s</font>' % r, S_Q)] for n, r in items]
    head = Table([[Paragraph('<font name="Mono" size="7.8" color="#5A5A66">REMINDER &middot; THE FIVE GATES '
                             '&middot; YOU MAY USE THIS ON EVERY QUESTION</font>', S_META)]], colWidths=[AVAIL])
    body = Table(data, colWidths=[18 * mm, AVAIL - 18 * mm - 20])
    body.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('TOPPADDING', (0, 0), (-1, -1), 1.5),
                              ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5), ('LEFTPADDING', (0, 0), (-1, -1), 0)]))
    outer = Table([[head], [body]], colWidths=[AVAIL])
    outer.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.8, INK), ('BACKGROUND', (0, 0), (-1, 0), PAPERBG),
                               ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                               ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
    return outer

def tick_row(labels):
    cells, cw = [], []
    for lab in labels:
        cells += [Paragraph('<font name="Body" size="10.4">%s</font>' % lab, S_Q), '']
        cw += [30 * mm, 8 * mm]
    t = Table([cells], colWidths=cw, rowHeights=[8 * mm], hAlign='LEFT')
    st = [('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 0)]
    for i in range(len(labels)):
        st.append(('BOX', (2 * i + 1, 0), (2 * i + 1, 0), 0.8, LINE))
    t.setStyle(TableStyle(st))
    return t

def _ind(fl, indent):
    if not indent:
        return fl
    t = Table([[fl]], colWidths=[AVAIL], hAlign='LEFT')
    t.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), indent), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return t

def _extras(o, indent=0):
    out = []
    if o.get('fig') is not None:
        out += [Spacer(1, 4), _ind(o['fig'], indent), Spacer(1, 3)]
    if o.get('grid'):
        out += [Spacer(1, 4), _ind(grid2(o['grid']), indent), Spacer(1, 3)]
    if o.get('quote'):
        out += [Spacer(1, 4), _ind(quote_box(*o['quote']), indent), Spacer(1, 3)]
    if o.get('tickrow'):
        out += [Spacer(1, 3), _ind(tick_row(o['tickrow']), indent), Spacer(1, 2)]
    if o.get('box'):
        out += [Spacer(1, 3), _ind(BlankBox([], None, o['box'], inner_note=o.get('box_note')), indent), Spacer(1, 3)]
    if o.get('space'):
        out.append(Ruled(o['space'], width=AVAIL, indent=indent))
    return out

def _doc(path, title, story, footer):
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                          topMargin=MARGIN_T, bottomMargin=MARGIN_B, title=title, author='Base Camp')
    frame = Frame(MARGIN_L, MARGIN_B, AVAIL, A4[1] - MARGIN_T - MARGIN_B, id='f',
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame])])

    class C(NumberedCanvas):
        def __init__(self, *a, **k):
            k['footer'] = footer
            NumberedCanvas.__init__(self, *a, **k)
    doc.build(story, canvasmaker=C)

def build_paper2(spec, path):
    story = _header(spec)
    if spec.get('reminder'):
        story += [reminder_box(spec['reminder']), Spacer(1, 10)]
    for i, q in enumerate(spec['questions'], 1):
        head = []
        if q.get('section'):
            head.append(Paragraph(q['section'].upper(), S_SEC))
        head.append(_qrow('%d.' % i, q['text'], q.get('marks', 0) if not q.get('parts') else 0))
        head += _extras(q)
        if q.get('tip') and not q.get('parts'):
            head += [Spacer(1, 2), Paragraph(q['tip'], S_NOTE)]
        blocks = []
        for p in q.get('parts', []):
            sub = [Spacer(1, 3), _qrow(p['label'], p['text'], p.get('marks', 0), indent=16, numw=26)]
            sub += _extras(p, indent=16)
            blocks.append(sub)
        if blocks:                       # never strand a question's text at the foot of a page
            head += blocks[0]
            blocks = blocks[1:]
        story.append(KeepTogether(head))
        for blk in blocks:
            story.append(KeepTogether(blk))
        if q.get('tip') and q.get('parts'):
            story += [Spacer(1, 2), Paragraph(q['tip'], S_NOTE)]
        story.append(Spacer(1, 10))
    story += [Spacer(1, 4), Rule(thickness=0.6, colour=LINE), Spacer(1, 4),
              Paragraph(spec['endnote'], S_NOTE)]
    _doc(path, spec['title'], story, spec['footer'])
    return path

def ans_tbl(vars, cols):
    """A small answer table for the mark scheme. cols: list of (header, column)."""
    heads = list(vars) + [h for h, _ in cols]
    body = []
    for i, r in enumerate(rows(len(vars))):
        body.append([str(b) for b in r] + [str(c[i]) for _, c in cols])
    st_c = ParagraphStyle('sc', fontName='Mono', fontSize=8.4, leading=9.6, alignment=1, textColor=INK)
    st_h = ParagraphStyle('sh', fontName='UI-Bold', fontSize=7.8, leading=9, alignment=1, textColor=INK)
    data = [[Paragraph(h, st_h) for h in heads]] + [[Paragraph(c, st_c) for c in r] for r in body]
    cw = [11 * mm] * len(vars) + [15 * mm] * len(cols)
    t = Table(data, colWidths=cw, rowHeights=[4.9 * mm] * len(data), hAlign='LEFT')
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.4, LINE), ('BACKGROUND', (0, 0), (-1, 0), PAPERBG),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('TOPPADDING', (0, 0), (-1, -1), 1),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 1), ('LEFTPADDING', (0, 0), (-1, -1), 1),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 1),
                           ('LINEAFTER', (len(vars) - 1, 0), (len(vars) - 1, -1), 1.0, INK)]))
    return t

def build_scheme2(schemes, path, header):
    story = [Paragraph(header['eyebrow'].upper(), S_EYEBROW), Paragraph(header['title'], S_TITLE),
             Paragraph(header['meta'].upper(), S_META), Spacer(1, 5), Rule(), Spacer(1, 8),
             Paragraph(header['intro'], S_NOTE), Spacer(1, 12)]
    for si, sc in enumerate(schemes):
        if si:
            story.append(Spacer(1, 6))
        head = Table([[Paragraph('<font name="UI-Bold" size="12">%s</font>' % sc['title'], S_ANS),
                       Paragraph('<font name="Mono" size="8" color="#5A5A66">%s</font>' % sc['meta'].upper(), S_MARKS)]],
                     colWidths=[AVAIL * 0.62, AVAIL * 0.38])
        head.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), PAPERBG), ('BOX', (0, 0), (-1, -1), 0.6, LINE),
                                  ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 9),
                                  ('RIGHTPADDING', (0, 0), (-1, -1), 9), ('TOPPADDING', (0, 0), (-1, -1), 6),
                                  ('BOTTOMPADDING', (0, 0), (-1, -1), 6)]))
        story += [head, Spacer(1, 7)]
        for q in sc['questions']:
            block = []
            row = Table([[Paragraph('%s' % q['n'], S_ANSN), Paragraph('<br/>'.join(q['lines']), S_ANS),
                          Paragraph('[%d]' % q['marks'], S_MARKS)]], colWidths=[32, AVAIL - 32 - 26, 26])
            row.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                                     ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0),
                                     ('BOTTOMPADDING', (0, 0), (-1, -1), 1)]))
            block.append(row)
            for f in q.get('figs', []):
                block += [Spacer(1, 3), _ind(f, 32)]
            if q.get('note'):
                block.append(Table([[Paragraph(q['note'], S_NOTE)]], colWidths=[AVAIL - 32],
                                   style=TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 32), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                                                     ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)])))
            block.append(Spacer(1, 8))
            story.append(KeepTogether(block))
    _doc(path, header['title'], story, header['footer'])
    return path

# =====================================================================================================
# 4. Behaviours: each scenario written once as a plain function that knows nothing about gates.
#    These are the independent source of truth for every answer column in the booklet.
# =====================================================================================================
B = {
 'A5':  lambda a, b, c: (a or b) and not c,
 'A5_nobracket': lambda a, b, c: a or (b and not c),
 'A5_nonot':     lambda a, b, c: (a or b) and c,
 'A6X': lambda a, b: (not a) or b,
 'A6Y': lambda a, b: not (a or b),
 'A7':  lambda a, b: (not a) and b,
 'A7_wrong': lambda a, b: not (a and b),
 'A8':  lambda m, p: (not m) and (not p),
 'A9':  lambda a: not (a and a),
 'B1_and': lambda a, b, c: a and b and c,
 'B1_or':  lambda a, b, c: a or b or c,
 'B1_exactly_one': lambda a, b, c: (a + b + c) == 1,
 'B5':  lambda a, b, c: not ((a or b) and c),
 'B6X': lambda a, b: not (a and b),
 'B6Y': lambda a, b: a and not b,
 'B7':  lambda a, b, c: (a and not b) or c,
 'B7_nonot': lambda a, b, c: (a and b) or c,
 'B7_and':   lambda a, b, c: (a and not b) and c,
 'B8':  lambda a, b, c: a or (b and c),
 'B8_wrong': lambda a, b, c: (a or b) and c,
 'C3X': lambda a, b, c: (not a) and b and c,
 'C3Y': lambda a, b, c: not (a and b and c),
 'C4':  lambda a, b, c: (a and b) or (not (b or c)),
 'C4_wrong': lambda a, b, c: (a and b) or (b or c),
 'C5_ok':  lambda a, b, c: not ((a and b) or (not c)),
 'C5_or':  lambda a, b, c: not ((a or b) or (not c)),
 'C5_nor': lambda a, b, c: not ((not (a or b)) or (not c)),
 'C6':  lambda a, b, c: not ((a or b) and (not c)),
 'C7':  lambda a, b, c, d: ((a and not b) or c) and d,
 'C7_nod': lambda a, b, c, d: (a and not b) or c,
 'C7_bracket': lambda a, b, c, d: (a and not b) or (c and d),
 'C8':  lambda a, b: not ((not (a and a)) and (not (b and b))),
 'D1':  lambda a, b, c: not ((not (a or b)) or (not c)),
 'D1_nonot': lambda a, b, c: not ((not (a or b)) or c),
 'D4':  lambda a, b, c: not ((not (a and b)) and (not (b and c))),
 'D4_asand': lambda a, b, c: (a and b) and (b and c),
 'D5X': lambda a, b: not (a and b),
 'D5Y': lambda a, b: (not a) or (not b),
 'D5Z': lambda a, b: (not a) and (not b),
 'D6':  lambda a, b, c: a and not (b and c),
 'D6_wrong': lambda a, b, c: a and not (b or c),
 'D7':  lambda a, b: a and b,
}
NIN = {'A5': 3, 'A5_nobracket': 3, 'A5_nonot': 3, 'A6X': 2, 'A6Y': 2, 'A7': 2, 'A7_wrong': 2, 'A8': 2, 'A9': 1,
       'B1_and': 3, 'B1_or': 3, 'B1_exactly_one': 3, 'B5': 3, 'B6X': 2, 'B6Y': 2, 'B7': 3, 'B7_nonot': 3,
       'B7_and': 3, 'B8': 3, 'B8_wrong': 3, 'C3X': 3, 'C3Y': 3, 'C4': 3, 'C4_wrong': 3, 'C5_ok': 3,
       'C5_or': 3, 'C5_nor': 3, 'C6': 3, 'C7': 4, 'C7_nod': 4, 'C7_bracket': 4, 'C8': 2, 'D1': 3,
       'D1_nonot': 3, 'D4': 3, 'D4_asand': 3, 'D5X': 2, 'D5Y': 2, 'D5Z': 2, 'D6': 3, 'D6_wrong': 3, 'D7': 2}
K = {k: fcol(f, NIN[k]) for k, f in B.items()}          # K['A7'] is the column for A7

# plain gate columns, for the questions that use bare gates
GATE_F = {'AND': lambda a, b: a and b, 'OR': lambda a, b: a or b, 'NAND': lambda a, b: not (a and b),
          'NOR': lambda a, b: not (a or b)}
GC = {g: fcol(f, 2) for g, f in GATE_F.items()}
GATE3 = {'AND': lambda a, b, c: a and b and c, 'OR': lambda a, b, c: a or b or c,
         'NAND': lambda a, b, c: not (a and b and c), 'NOR': lambda a, b, c: not (a or b or c)}
GC3 = {g: fcol(f, 3) for g, f in GATE3.items()}

# ---- the drawn circuits -------------------------------------------------------------------------
V3 = ['A', 'B', 'C']

def circ_s2(g1, g2, not_on_c, out='Q', labels=None, **kw):
    """g2( g1(A,B), C or NOT C ). The standard three-input, two-gate shape."""
    gates = [('g1', g1, ['A', 'B'], 0, 0.5)]
    if not_on_c:
        gates += [('n1', 'NOT', ['C'], 0, 2.2), ('g2', g2, ['g1', 'n1'], 1, 1.35)]
    else:
        gates += [('g2', g2, ['g1', 'C'], 1, 1.35)]
    return Circ(V3, {'A': 0, 'B': 1, 'C': 2.2}, gates, 'g2', out_name=out, labels=labels, **kw)

def circ_s1(g1, g2, g3, out='Q', labels=None, **kw):
    """g3( g1(A,B), g2(B,C) ): B is shared, so it is drawn with a junction dot."""
    gates = [('g1', g1, ['A', 'B'], 0, 0.55), ('g2', g2, ['B', 'C'], 0, 2.05),
             ('g3', g3, ['g1', 'g2'], 1, 1.3)]
    return Circ(V3, {'A': 0, 'B': 1.3, 'C': 2.6}, gates, 'g3', out_name=out, labels=labels, **kw)

CIRC = {}
CIRC['A5'] = circ_s2('OR', 'AND', True, out='X', labels={'g1': 'P', 'n1': 'R'})
CIRC['A9'] = Circ(['A'], {'A': 0.95}, [('g1', 'NAND', ['A', 'A'], 0, 0.95)], 'g1', out_name='Z')
CIRC['A7'] = Circ(['A', 'B'], {'A': 0, 'B': 1.4}, [('n1', 'NOT', ['A'], 0, 0), ('g1', 'AND', ['n1', 'B'], 1, 0.7)],
                  'g1', out_name='Q')
CIRC['B5'] = circ_s2('OR', 'NAND', False, labels={'g1': 'P'})
CIRC['B6X'] = Circ(['A', 'B'], {'A': 0.45, 'B': 1.45}, [('g1', 'AND', ['A', 'B'], 0, 0.95), ('n1', 'NOT', ['g1'], 1, 0.95)],
                   'n1', out_name='X', S=0.7, colw=88, x0=62)
CIRC['B6Y'] = Circ(['A', 'B'], {'A': 0.45, 'B': 1.45}, [('n1', 'NOT', ['B'], 0, 1.45), ('g1', 'AND', ['A', 'n1'], 1, 0.95)],
                   'g1', out_name='Y', S=0.7, colw=88, x0=62)
CIRC['B8'] = Circ(['A', 'B', 'C'], {'A': 0, 'B': 1.3, 'C': 2.2},
                  [('g1', 'AND', ['B', 'C'], 0, 1.75), ('g2', 'OR', ['A', 'g1'], 1, 0.9)], 'g2', out_name='Q')
CIRC['C4'] = circ_s1('AND', 'NOR', 'OR', labels={'g1': 'P', 'g2': 'R'})
_c5 = dict(S=0.7, colw=84, rowh=40, x0=56)
CIRC['C5_i'] = circ_s2('OR', 'NOR', True, out='X', **_c5)
CIRC['C5_ii'] = circ_s2('AND', 'NOR', True, out='X', **_c5)
CIRC['C5_iii'] = circ_s2('NOR', 'NOR', True, out='X', **_c5)
CIRC['C6'] = circ_s2('OR', 'NAND', True, labels={'g1': 'P', 'n1': 'R'})
CIRC['C8'] = Circ(['A', 'B'], {'A': 0.2, 'B': 1.7},
                  [('g1', 'NAND', ['A', 'A'], 0, 0.2), ('g2', 'NAND', ['B', 'B'], 0, 1.7),
                   ('g3', 'NAND', ['g1', 'g2'], 1, 0.95)], 'g3', out_name='Q', labels={'g1': 'P', 'g2': 'R'})
CIRC['C8_not'] = Circ(['A'], {'A': 0.95}, [('g1', 'NAND', ['A', 'A'], 0, 0.95)], 'g1', out_name='Q')
CIRC['D4'] = circ_s1('NAND', 'NAND', 'NAND', labels={'g1': 'P', 'g2': 'R'})
CIRC['D6'] = Circ(['A', 'B', 'C'], {'A': 0, 'B': 1.5, 'C': 2.2},
                  [('g1', 'NAND', ['B', 'C'], 0, 1.85), ('g2', 'AND', ['A', 'g1'], 1, 0.95)], 'g2', out_name='Q')
CIRC['D7'] = Circ(['A', 'B'], {'A': 0.45, 'B': 1.45},
                  [('g1', 'NAND', ['A', 'B'], 0, 0.95), ('g2', 'NAND', ['g1', 'g1'], 1, 0.95)], 'g2', out_name='Q',
                  labels={'g1': 'P'})

# =====================================================================================================
# 5. Paper content
# =====================================================================================================
BASE = [
 'Answer <b>every</b> question in the space provided. The mark for each question is in square brackets on the right.',
 'No calculator is needed anywhere on this paper.',
 'Truth-table rows go in <b>binary counting order</b>: 00, 01, 10, 11, and for three inputs 000, 001, 010, 011, 100, 101, 110, 111.',
 'Write expressions with AND, OR, NOT, NAND and NOR, and put <b>brackets wherever two different gates meet</b>. '
 'NOT applies only to the thing straight after it, so NOT A AND B means (NOT A) AND B.',
]
INSTR_MED = BASE + ['A reminder of the five gates is printed below. You may use it on every question.']
INSTR_HARD = BASE + ['Several questions describe machines you may not have seen before. You are not expected to recognise them: '
                     'apply the gate rules and the one-gate-at-a-time method you already have.',
                     'No reminder of the gates is printed on this paper.']
REMINDER = [('AND', '1 only when <b>every</b> input is 1.'),
            ('OR', '1 when <b>at least one</b> input is 1. Both inputs being 1 still gives 1.'),
            ('NOT', 'One input. The output is the opposite of it.'),
            ('NAND', 'AND, then flip. 0 only when every input is 1; 1 on every other row.'),
            ('NOR', 'OR, then flip. 1 only when every input is 0; 0 on every other row.')]
END = ('End of paper. Check every truth table has all its rows in counting order, and that every expression '
       'has brackets wherever two different gates meet.')

def name_row(labels, w=30):
    return {'rows': [list(labels), [''] * len(labels)], 'nin': 0, 'widths_mm': [w] * len(labels), 'rowh': 10}

# ---- columns used in several places (all from the evaluator) ------------------------------------
NAND_JOINED = col(CIRC['A9'].ast(), ['A'])
HIS_P = [int(r[0] != r[1]) for r in rows(3)]                       # Tom: "OR gives 0 when both are 1"
HIS_R = [_gate('NOT', [r[2]]) for r in rows(3)]
HIS_Q = [_gate('NAND', [p, r]) for p, r in zip(HIS_P, HIS_R)]
TRUE_P = CIRC['C6'].gate_col('g1')
TRUE_R = CIRC['C6'].gate_col('n1')
TRUE_Q = col(CIRC['C6'].ast(), V3)

# =====================================================================================================
# PAPER A
# =====================================================================================================
A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A', 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED, 'reminder': REMINDER, 'footer': 'Paper A · Medium · ' + TOPIC, 'endnote': END,
 'questions': [
  {'section': 'Section 1 — gates and tables',
   'text': 'A circuit has <b>three</b> inputs, A, B and C.', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'How many rows does its truth table need?', 'marks': 1, 'space': 10},
             {'label': '(b)', 'text': 'Write out every row of the table below, in counting order, starting at 000. '
                                      '(There is no output column yet.)', 'marks': 2,
              'grid': tt(V3, [], blank_inputs=True, widths_mm=[16, 16, 16], rowh=5.9)}]},
  {'text': 'Complete the truth table for an <b>AND</b> gate and for an <b>OR</b> gate with the same two inputs.', 'marks': 2,
   'grid': tt(['A', 'B'], ['AND', 'OR'], widths_mm=[16, 16, 24, 24])},
  {'text': 'Complete the truth table for a <b>NAND</b> gate and for a <b>NOR</b> gate with the same two inputs.', 'marks': 2,
   'grid': tt(['A', 'B'], ['NAND', 'NOR'], widths_mm=[16, 16, 24, 24]),
   'tip': 'Do the plain gate first in your head, then flip every output.'},
  {'text': 'Name each of these four gate symbols. Write the name in the box under its number.', 'marks': 4,
   'fig': symbol_row(['NOR', 'NOT', 'AND', 'NAND'], ['(i)', '(ii)', '(iii)', '(iv)']),
   'grid': name_row(['(i)', '(ii)', '(iii)', '(iv)']),
   'tip': 'Look for a small circle first, then at the shape of the body. A circle on its own means &ldquo;flip&rdquo;.'},

  {'section': 'Section 2 — reading circuits',
   'text': 'Study the circuit. The first two gates give the outputs P and R, and the last gate gives X.', 'marks': 4,
   'fig': CircuitFig(CIRC['A5']),
   'parts': [{'label': '(a)', 'text': 'Write the expression for X.', 'marks': 1, 'space': 11},
             {'label': '(b)', 'text': 'Complete the trace table. Fill in one whole column at a time, from left to right.', 'marks': 3,
              'grid': tt(V3, ['P', 'R', 'X'], widths_mm=[14, 14, 14, 18, 18, 18], rowh=5.9)}]},
  {'text': 'NOT applies only to the thing straight after it. Complete the table for these two expressions, which look alike:<br/>'
           '<font name="Mono" size="10.4">X = NOT A OR B &nbsp;&nbsp;&nbsp;&nbsp; Y = NOT (A OR B)</font>', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'Complete the table.', 'marks': 2,
              'grid': tt(['A', 'B'], ['X', 'Y'], widths_mm=[16, 16, 22, 22])},
             {'label': '(b)', 'text': 'One of X and Y gives exactly the same output column as a single gate. Name the gate, and say whether it is X or Y.',
              'marks': 1, 'space': 11}]},

  {'section': 'Section 3 — from words to circuits',
   'text': 'A pump fills the overhead tank of an apartment block in Bengaluru. The pump motor, Q, must run only when the tank is '
           '<b>not</b> full <b>and</b> the sump (the underground tank) has water in it. '
           '<b>A = 1</b> when the overhead tank is full. <b>B = 1</b> when the sump has water.', 'marks': 5,
   'parts': [{'label': '(a)', 'text': 'Write an expression for Q.', 'marks': 1, 'space': 11},
             {'label': '(b)', 'text': 'Complete the truth table for Q.', 'marks': 2,
              'grid': tt(['A', 'B'], ['Q'], widths_mm=[16, 16, 22])},
             {'label': '(c)', 'text': 'Draw the circuit in the box, using the standard gate symbols.', 'marks': 2,
              'fig': BlankBox(['A', 'B'], 'Q', 33)}]},
  {'text': 'An auto-rickshaw has a &ldquo;FOR HIRE&rdquo; lamp, H. <b>M = 1</b> when the fare meter is running. <b>P = 1</b> when a passenger '
           'is seated. The lamp must be on only when the meter is off <b>and</b> nobody is seated.', 'marks': 4,
   'parts': [{'label': '(a)', 'text': 'Write an expression for H.', 'marks': 1, 'space': 11},
             {'label': '(b)', 'text': 'Complete the truth table for H.', 'marks': 2,
              'grid': tt(['M', 'P'], ['H'], widths_mm=[16, 16, 22])},
             {'label': '(c)', 'text': 'Which single gate gives this same table?', 'marks': 1, 'space': 10}]},
  {'text': 'In this circuit the two inputs of one <b>NAND</b> gate are joined together, so both receive the same input A.', 'marks': 3,
   'fig': CircuitFig(CIRC['A9']),
   'parts': [{'label': '(a)', 'text': 'Complete the truth table for Z.', 'marks': 2,
              'grid': tt(['A'], ['Z'], widths_mm=[16, 22])},
             {'label': '(b)', 'text': 'Which single gate does this circuit behave as?', 'marks': 1, 'space': 10}]},
 ]}

# =====================================================================================================
# PAPER B
# =====================================================================================================
B_COLS = [GC['NAND'], GC['AND'], GC['NOR'], GC['OR']]          # printed as (i) (ii) (iii) (iv)
B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B', 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED, 'reminder': REMINDER, 'footer': 'Paper B · Medium · ' + TOPIC, 'endnote': END,
 'questions': [
  {'section': 'Section 1 — gates and tables',
   'text': 'Complete the truth table for a <b>three-input</b> AND gate and for a <b>three-input</b> OR gate.', 'marks': 2,
   'grid': tt(V3, ['AND', 'OR'], widths_mm=[14, 14, 14, 24, 24], rowh=5.9)},
  {'text': 'Answer these without drawing the tables.', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'A circuit has <b>4</b> inputs. How many rows does its truth table need?', 'marks': 1, 'space': 10},
             {'label': '(b)', 'text': 'A circuit has <b>6</b> inputs. How many rows does its truth table need?', 'marks': 1, 'space': 10},
             {'label': '(c)', 'text': 'A truth table has <b>32</b> rows. How many inputs does the circuit have?', 'marks': 1, 'space': 10}]},
  {'text': 'Each output column below belongs to one of AND, OR, NAND or NOR, and each gate is used once. '
           'Write the name of the gate in the bottom row of its column.', 'marks': 4,
   'grid': tt(['A', 'B'], ['(i)', '(ii)', '(iii)', '(iv)'], prefill=B_COLS, extra_rows=[['Gate', '', '', '', '', '']],
              widths_mm=[16, 16, 26, 26, 26, 26], last_h=10),
   'tip': 'Count the 1s in each column, then find where the odd one out sits.'},
  {'text': 'In the box, draw the standard symbol for (a) a NOT gate, (b) a NAND gate and (c) a NOR gate. '
           'Label each one, and show every input and output wire.', 'marks': 3, 'box': 46},

  {'section': 'Section 2 — reading circuits',
   'text': 'Study the circuit. The first gate gives the output P. Fill in the whole of column P before you start column Q.', 'marks': 5, 'fig': CircuitFig(CIRC['B5']),
   'parts': [{'label': '(a)', 'text': 'Write the expression for Q.', 'marks': 1, 'space': 11},
             {'label': '(b)', 'text': 'Complete the trace table.', 'marks': 3,
              'grid': tt(V3, ['P', 'Q'], widths_mm=[14, 14, 14, 20, 20], rowh=5.9)},
             {'label': '(c)', 'text': 'How many of the 8 rows have Q = 1?', 'marks': 1, 'space': 10}]},
  {'text': 'Look at these two small circuits.', 'marks': 3,
   'fig': panels([CIRC['B6X'], CIRC['B6Y']], ['(i)', '(ii)'], 1.0),
   'parts': [{'label': '(a)', 'text': 'Write the expression for X in circuit (i).', 'marks': 1, 'space': 10},
             {'label': '(b)', 'text': 'Which single gate does circuit (i) behave as?', 'marks': 1, 'space': 10},
             {'label': '(c)', 'text': 'Write the expression for Y in circuit (ii).', 'marks': 1, 'space': 10}]},

  {'section': 'Section 3 — from words to circuits',
   'text': 'A railway crossing near Tumakuru has a warning bell, Q. <b>A = 1</b> when a train is approaching. '
           '<b>B = 1</b> when the barrier is fully down. <b>C = 1</b> when the engineer presses the test switch. '
           'The bell rings when a train is approaching and the barrier is <b>not</b> fully down, <b>or</b> when the test switch is pressed.', 'marks': 5,
   'parts': [{'label': '(a)', 'text': 'Write an expression for Q.', 'marks': 2, 'space': 13},
             {'label': '(b)', 'text': 'Complete the truth table for Q.', 'marks': 3,
              'grid': tt(V3, ['Q'], widths_mm=[14, 14, 14, 22], rowh=5.9)}]},
  {'text': 'An ATM kiosk in Chennai has an alarm, Q. <b>A = 1</b> when the door is forced open. <b>B = 1</b> when the card slot is blocked. '
           '<b>C = 1</b> when the camera is covered. The alarm sounds when the door is forced, <b>or</b> when the card slot is blocked '
           '<b>and</b> the camera is covered.', 'marks': 5,
   'parts': [{'label': '(a)', 'text': 'Write an expression for Q.', 'marks': 2, 'space': 13},
             {'label': '(b)', 'text': 'Draw the circuit in the box, using the standard gate symbols.', 'marks': 3,
              'fig': BlankBox(V3, 'Q', 44)}]},
 ]}

# =====================================================================================================
# PAPER C
# =====================================================================================================
C_COLS = [GC3['NAND'], GC3['AND'], GC3['NOR'], GC3['OR']]       # printed as (i) (ii) (iii) (iv)
C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C', 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD, 'footer': 'Paper C · Hard · ' + TOPIC, 'endnote': END,
 'questions': [
  {'section': 'Section 1 — quick and exact',
   'text': 'Each output column below belongs to a <b>three-input</b> AND, OR, NAND or NOR gate, and each gate is used once. '
           'Write the name of the gate in the bottom row. One mark for each correct pair.', 'marks': 2,
   'grid': tt(V3, ['(i)', '(ii)', '(iii)', '(iv)'], prefill=C_COLS, extra_rows=[['Gate', '', '', '', '', '', '']],
              widths_mm=[13, 13, 13, 24, 24, 24, 24], rowh=5.8, last_h=9)},
  {'text': 'Answer these without drawing the tables.', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'A truth table has <b>64</b> rows. How many inputs does the circuit have?', 'marks': 1, 'space': 10},
             {'label': '(b)', 'text': 'A circuit has four inputs, A, B, C and D. How many of its rows have A = 1?', 'marks': 1, 'space': 10},
             {'label': '(c)', 'text': 'A <b>four-input NAND</b> gate has 16 rows. On how many of them is the output 1?', 'marks': 1, 'space': 10}]},
  {'text': 'In the first expression NOT applies only to A. Complete the table for both:<br/>'
           '<font name="Mono" size="10.4">X = NOT A AND B AND C &nbsp;&nbsp;&nbsp;&nbsp; Y = NOT (A AND B AND C)</font>', 'marks': 4,
   'parts': [{'label': '(a)', 'text': 'Complete the table.', 'marks': 2,
              'grid': tt(V3, ['X', 'Y'], widths_mm=[14, 14, 14, 22, 22], rowh=5.8)},
             {'label': '(b)', 'text': 'On how many of the 8 rows do X and Y give different outputs?', 'marks': 1, 'space': 10},
             {'label': '(c)', 'text': 'Y gives the same table as one single three-input gate. Name it.', 'marks': 1, 'space': 10}]},

  {'section': 'Section 2 — circuits and tables',
   'text': 'Study the circuit. P and R are the outputs of the first two gates.', 'marks': 5, 'fig': CircuitFig(CIRC['C4']),
   'parts': [{'label': '(a)', 'text': 'Write the expression for Q.', 'marks': 2, 'space': 12},
             {'label': '(b)', 'text': 'Complete the trace table.', 'marks': 3,
              'grid': tt(V3, ['P', 'R', 'Q'], widths_mm=[14, 14, 14, 18, 18, 18], rowh=5.9)}]},
  {'text': 'The table gives the output X of exactly one of the three circuits below. The circuits are identical except for one gate, '
           'so they agree on most rows. Do not complete all three tables.', 'marks': 3,
   'fig': panels([CIRC['C5_i'], CIRC['C5_ii'], CIRC['C5_iii']], ['(i)', '(ii)', '(iii)'], 0.72),
   'grid': tt(V3, ['X'], prefill=[K['C5_ok']], widths_mm=[14, 14, 14, 20], rowh=5.8),
   'parts': [{'label': '(a)', 'text': 'Tick the circuit that produces X.', 'marks': 1,
              'tickrow': ['Circuit (i)', 'Circuit (ii)', 'Circuit (iii)']},
             {'label': '(b)', 'text': 'Write down one row (as three digits, ABC) that rules out circuit (i), and one row that rules out circuit (iii). '
                                      'Say what each wrong circuit outputs on its row.', 'marks': 2, 'space': 24}]},
  {'text': 'Tom filled in the trace table for the circuit below. He made one mistake, in column P, and carried it forward.', 'marks': 3,
   'fig': CircuitFig(CIRC['C6']),
   'grid': {'rows': [V3 + ['P', 'R', 'Q']] + [[str(b) for b in r] + [str(HIS_P[i]), str(HIS_R[i]), str(HIS_Q[i])] for i, r in enumerate(rows(3))],
            'nin': 3, 'widths_mm': [14, 14, 14, 18, 18, 18], 'rowh': 6.2},
   'parts': [{'label': '(a)', 'text': 'Write down the rows (ABC) where column P is wrong.', 'marks': 1, 'space': 10},
             {'label': '(b)', 'text': 'Describe the rule Tom used for gate P that is not the rule for that gate.', 'marks': 1, 'space': 12},
             {'label': '(c)', 'text': 'How many cells in column Q are wrong?', 'marks': 1, 'space': 10}]},

  {'section': 'Section 3 — machines and design',
   'text': 'A greenhouse in Nashik has a misting valve, Q. <b>A = 1</b> when the air is too hot. <b>B = 1</b> when the soil is wet. '
           '<b>C = 1</b> when the gardener presses the manual button. <b>D = 1</b> when the water pump is running. '
           'The valve opens when (the air is too hot and the soil is <b>not</b> wet, or the manual button is pressed) <b>and</b> the pump is running. '
           'With the pump off, the valve must stay shut whatever else is happening.', 'marks': 5,
   'parts': [{'label': '(a)', 'text': 'Write an expression for Q.', 'marks': 2, 'space': 14},
             {'label': '(b)', 'text': 'The full table has 16 rows. Without writing it out, work out how many of them give Q = 1. Show your reasoning.',
              'marks': 2, 'space': 28},
             {'label': '(c)', 'text': 'State Q when A = 1, B = 1, C = 0 and D = 1, and give the reason in a few words.', 'marks': 1, 'space': 13}]},
  {'text': 'A workshop has only <b>NAND</b> gates in stock. A technician builds the circuit below, in which P and R are the outputs of the first two gates.', 'marks': 5, 'fig': CircuitFig(CIRC['C8']),
   'parts': [{'label': '(a)', 'text': 'Complete the trace table.', 'marks': 2,
              'grid': tt(['A', 'B'], ['P', 'R', 'Q'], widths_mm=[14, 14, 18, 18, 18], rowh=5.9)},
             {'label': '(b)', 'text': 'Explain why the first two gates act as NOT gates, even though they are NAND gates.', 'marks': 1, 'space': 20},
             {'label': '(c)', 'text': 'Draw one NAND gate, wired to behave as a NOT gate, in the box.', 'marks': 1,
              'fig': BlankBox(['A'], 'Q', 24)},
             {'label': '(d)', 'text': 'State the single gate that the circuit above is equivalent to.', 'marks': 1, 'space': 10}]},
 ]}

# =====================================================================================================
# PAPER D
# =====================================================================================================
D_P = CIRC['D4'].gate_col('g1'); D_R = CIRC['D4'].gate_col('g2')
D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D', 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD, 'footer': 'Paper D · Hard · ' + TOPIC, 'endnote': END,
 'questions': [
  {'section': 'Section 1 — quick and exact',
   'text': 'Complete the trace table for <font name="Mono" size="10.2">Q = (A NOR B) NOR (NOT C)</font>. '
           'P is the output of the first gate and R is the output of the NOT.', 'marks': 3,
   'grid': tt(V3, ['P<br/>A NOR B', 'R<br/>NOT C', 'Q<br/>P NOR R'], widths_mm=[14, 14, 14, 24, 24, 24], hdr_h=10, rowh=5.9)},
  {'text': 'Answer these without writing out the tables. Rows are numbered from the first row, so the first row of a three-input table is row 1 (000).', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'In a three-input table (A, B, C), write the <b>sixth</b> row.', 'marks': 1, 'space': 10},
             {'label': '(b)', 'text': 'In the same table, which row number is ABC = 110?', 'marks': 1, 'space': 10},
             {'label': '(c)', 'text': 'In a four-input table (A, B, C, D), write the <b>tenth</b> row.', 'marks': 1, 'space': 10}]},
  {'text': 'A gate has two inputs, and its output column contains exactly <b>three</b> 1s.', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'Name the two gates this could be.', 'marks': 2, 'space': 11},
             {'label': '(b)', 'text': 'Write down one input row (AB) that would tell you which of the two it is.', 'marks': 1, 'space': 11}]},

  {'section': 'Section 2 — circuits and tables',
   'text': 'Study the circuit, which is built only from NAND gates. P and R are the outputs of the first two gates.', 'marks': 5,
   'fig': CircuitFig(CIRC['D4']),
   'parts': [{'label': '(a)', 'text': 'Write the expression for Q.', 'marks': 2, 'space': 12},
             {'label': '(b)', 'text': 'Complete the trace table.', 'marks': 3,
              'grid': tt(V3, ['P', 'R', 'Q'], widths_mm=[14, 14, 14, 18, 18, 18], rowh=5.9)}]},
  {'text': 'Complete the table for these three expressions, which are easy to confuse:<br/>'
           '<font name="Mono" size="10">X = NOT (A AND B) &nbsp;&nbsp;&nbsp; Y = (NOT A) OR (NOT B) &nbsp;&nbsp;&nbsp; Z = (NOT A) AND (NOT B)</font>', 'marks': 4,
   'parts': [{'label': '(a)', 'text': 'Complete the table.', 'marks': 3,
              'grid': tt(['A', 'B'], ['X', 'Y', 'Z'], widths_mm=[16, 16, 22, 22, 22])},
             {'label': '(b)', 'text': 'Two of the three columns are identical. Say which two, and name the single gate they equal.', 'marks': 1, 'space': 13}]},

  {'section': 'Section 3 — machines and diagnosis',
   'text': 'At a school in Pune the period bell, Q, rings when the timer fires, <b>unless both</b> the exam-hall switch and the silent-mode switch are on. '
           '<b>A = 1</b> when the timer fires. <b>B = 1</b> when the exam-hall switch is on. <b>C = 1</b> when the silent-mode switch is on. '
           'If B and C are both on, the bell must stay silent. If only one of them is on, it must still ring.', 'marks': 4,
   'parts': [{'label': '(a)', 'text': 'Write an expression for Q.', 'marks': 2, 'space': 13},
             {'label': '(b)', 'text': 'Draw the circuit in the box, using the standard gate symbols.', 'marks': 2,
              'fig': BlankBox(V3, 'Q', 42)}]},
  {'text': 'The store only has <b>NAND</b> gates. Draw an <b>AND</b> gate made from NAND gates only, then check it.', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'Draw the circuit in the box. Label the output of the first gate P.', 'marks': 2,
              'fig': BlankBox(['A', 'B'], 'Q', 34)},
             {'label': '(b)', 'text': 'Complete the trace table for your circuit.', 'marks': 1,
              'grid': tt(['A', 'B'], ['P', 'Q'], widths_mm=[16, 16, 20, 20])}]},
  {'text': 'Rohan has written two statements in his notebook, and <b>both are wrong</b>. For each one, explain the mistake and write a correct version.', 'marks': 5,
   'quote': ([('(i)', '&ldquo;A NAND gate is an AND gate with a circle added, so it gives 1 when both inputs are 1.&rdquo;'),
              ('(ii)', '&ldquo;NOT A AND B means the same as NOT (A AND B), because the NOT comes first.&rdquo;')],
             "Rohan's notebook"),
   'space': 64},
 ]}
SPECS = [('a', A), ('b', B), ('c', C), ('d', D)]

# =====================================================================================================
# 6. Mark schemes. One `lines` entry per mark, tagged [1]. Every column below comes from K / CIRC.
# =====================================================================================================
T = '<b>[1]</b>'
def b(x): return '<b>%s</b>' % x
def rl(n, i): return ''.join(map(str, rows(n)[i]))
def nrows(c, n): return ', '.join(ones_at(c, n))
def diffrows(c1, c2, n): return [rl(n, i) for i in range(2 ** n) if c1[i] != c2[i]]
def colx(circ, gid): return circ.gate_col(gid)
def fig(c, s=0.9): return CircuitFig(c, scale=s)

# some columns used in more than one place
A5P, A5R, A5X = colx(CIRC['A5'], 'g1'), colx(CIRC['A5'], 'n1'), col(CIRC['A5'].ast(), V3)
XOR2 = fcol(lambda a, b_: a != b_, 2)
C4P, C4R, C4Q = colx(CIRC['C4'], 'g1'), colx(CIRC['C4'], 'g2'), col(CIRC['C4'].ast(), V3)
C8P, C8R, C8Q = colx(CIRC['C8'], 'g1'), colx(CIRC['C8'], 'g2'), col(CIRC['C8'].ast(), ['A', 'B'])
D4P, D4R, D4Q = colx(CIRC['D4'], 'g1'), colx(CIRC['D4'], 'g2'), col(CIRC['D4'].ast(), V3)
D1P = fcol(lambda a, b_, c_: not (a or b_), 3)
D1R = fcol(lambda a, b_, c_: not c_, 3)
D1Q = K['D1']
D7P, D7Q = colx(CIRC['D7'], 'g1'), col(CIRC['D7'].ast(), ['A', 'B'])
B5P, B5Q = colx(CIRC['B5'], 'g1'), col(CIRC['B5'].ast(), V3)
B5_asand = fcol(lambda a, b_, c_: (a or b_) and c_, 3)
C5_agree = [rl(3, i) for i in range(8) if K['C5_ok'][i] == K['C5_or'][i] == K['C5_nor'][i]]
wrong_order = [''.join(map(str, r)) for r in sorted(rows(3), key=sum)]
C3_diff = diffrows(K['C3X'], K['C3Y'], 3)
D2_a, D2_a_wrong = rl(3, 5), rl(3, 6)
D2_b = [i for i, r in enumerate(rows(3)) if r == (1, 1, 0)][0] + 1
D2_c = ''.join(map(str, rows(4)[9]))

SA = [
 {'n': '1', 'marks': 3, 'lines': [
   '(a) ' + b('8') + ' rows (2 &times; 2 &times; 2) ' + T,
   '(b) Eight different rows, none missing and none repeated ' + T,
   'In counting order: ' + ', '.join(''.join(map(str, r)) for r in rows(3)) + ' ' + T],
  'note': 'The addition slip gives 2 + 2 + 2 = 6 rows; multiplying gives 8. Writing the rows in the order a person happens to think of them '
          '(for example by how many 1s each has: %s) often keeps all eight but loses the order mark: award the first mark of (b) only.'
          % ', '.join(wrong_order)},
 {'n': '2', 'marks': 2, 'lines': ['AND column: ' + b(cs(GC['AND'])) + ' ' + T, 'OR column: ' + b(cs(GC['OR'])) + ' ' + T],
  'note': 'The OR trap: reading OR as &ldquo;one or the other&rdquo; writes 0 on the 1 1 row and gives %s. That is XOR, which this topic does not examine. '
          'Award the AND mark and withhold the OR mark.' % cs(XOR2)},
 {'n': '3', 'marks': 2, 'lines': ['NAND column: ' + b(cs(GC['NAND'])) + ' ' + T, 'NOR column: ' + b(cs(GC['NOR'])) + ' ' + T],
  'note': 'Ignoring the circle copies the plain gate: NAND written as %s (AND\'s column) and NOR written as %s (OR\'s column). '
          'Each mark is independent.' % (cs(GC['AND']), cs(GC['OR']))},
 {'n': '4', 'marks': 4, 'lines': ['(i) ' + b('NOR') + ' ' + T, '(ii) ' + b('NOT') + ' ' + T, '(iii) ' + b('AND') + ' ' + T,
                                  '(iv) ' + b('NAND') + ' ' + T],
  'note': 'Only one of the four symbols has a single input: the NOT. A circle on its own is not a gate, so calling (ii) NAND or NOR is the '
          '&ldquo;circle means NAND&rdquo; trap. For the other three, a curved back is the OR family (NOR) and a flat back is the AND family (AND, NAND); '
          'then the circle decides between AND and NAND.'},
 {'n': '5', 'marks': 4, 'lines': [
   '(a) ' + b('X = (A OR B) AND (NOT C)') + ' ' + T + ' (accept P AND R; brackets round NOT C are optional)',
   '(b) P = A OR B: ' + b(cs(A5P)) + ' ' + T,
   'R = NOT C: ' + b(cs(A5R)) + ' ' + T,
   'X = P AND R: ' + b(cs(A5X)) + ' ' + T + ' (award if consistent with their own P and R)'],
  'figs': [ans_tbl(V3, [('P', A5P), ('R', A5R), ('X', A5X)])],
  'note': 'Reading the circuit without its brackets, as A OR (B AND NOT C), gives %s. Dropping the NOT on C (X = P AND C) gives %s. '
          'Both are wrong in several rows against the correct %s, which has %d ones. The method on trial is filling one column at a time.' % (cs(K['A5_nobracket']), cs(K['A5_nonot']), cs(A5X), sum(A5X))},
 {'n': '6', 'marks': 3, 'lines': [
   '(a) X = (NOT A) OR B: ' + b(cs(K['A6X'])) + ' ' + T,
   'Y = NOT (A OR B): ' + b(cs(K['A6Y'])) + ' ' + T,
   '(b) ' + b('NOR') + ', and it is ' + b('Y') + ' ' + T],
  'note': 'Reading X as NOT (A OR B) gives Y\'s column %s: the NOT was applied to the whole expression instead of to A alone. X matches no single gate: '
          'it has three 1s like OR and NAND, but its 0 is on the row %s, whereas OR\'s is on 00 and NAND\'s on 11.'
          % (cs(K['A6Y']), rl(2, K['A6X'].index(0)))},
 {'n': '7', 'marks': 5, 'lines': [
   '(a) ' + b('Q = (NOT A) AND B') + ' ' + T + ' (NOT A AND B is accepted under this course\'s rule)',
   '(b) Q = ' + b(cs(K['A7'])) + ': the row A = 0, B = 1 gives 1 ' + T,
   'the other three rows give 0 ' + T,
   '(c) A NOT gate on A ' + T,
   'An AND gate taking NOT A and B, with its output labelled Q ' + T],
  'figs': [fig(CIRC['A7'])],
  'note': 'Reading the sentence as NOT (A AND B) gives %s: three 1s instead of one. A drawing that uses a NAND or a NOR scores nothing in (c), and a NOT '
          'drawn with two inputs loses the first mark. Mark the structure; do not penalise untidy symbols.' % cs(K['A7_wrong'])},
 {'n': '8', 'marks': 4, 'lines': [
   '(a) ' + b('H = (NOT M) AND (NOT P)') + ' ' + T,
   '(b) The row M = 0, P = 0 gives 1 ' + T,
   'The other three rows give 0, so H = ' + b(cs(K['A8'])) + ' ' + T,
   '(c) ' + b('NOR') + ' ' + T],
  'note': 'NOT (M AND P) and (NOT M) OR (NOT P) both give %s, which is NAND\'s column: they say &ldquo;at least one is off&rdquo;, but the lamp needs '
          '<i>both</i> off. The sentence has &ldquo;and&rdquo; in it, and each condition needs its own NOT.' % cs(GC['NAND'])},
 {'n': '9', 'marks': 3, 'lines': [
   '(a) A = 0 gives ' + b('1') + ' ' + T, 'A = 1 gives ' + b('0') + ' ' + T, '(b) ' + b('NOT') + ' ' + T],
  'note': 'Forgetting the circle writes Z = %s: AND of A with itself is just A. The joined inputs make NOT (A AND A), and A AND A is A, so the circle leaves '
          'the opposite of A.' % cs([0, 1])},
]

SB = [
 {'n': '1', 'marks': 2, 'lines': ['AND: ' + b(cs(GC3['AND'])) + ' ' + T, 'OR: ' + b(cs(GC3['OR'])) + ' ' + T],
  'note': 'Reading OR as &ldquo;exactly one input is 1&rdquo; gives %s: it drops the rows with two or three 1s, which OR counts too. '
          'Award the AND mark only.' % cs(K['B1_exactly_one'])},
 {'n': '2', 'marks': 3, 'lines': ['(a) ' + b('16') + ' ' + T, '(b) ' + b('64') + ' ' + T, '(c) ' + b('5') + ' (2<super>5</super> = 32) ' + T],
  'note': 'Rows double with every extra input: 2, 4, 8, 16, 32, 64. The slip is to add: 4 inputs by addition is 2 + 2 + 2 + 2 = 8, or 4 &times; 2 = 8, '
          'and 6 inputs by the same habit gives 12. (c) works backwards: 32 is five doublings.'},
 {'n': '3', 'marks': 4, 'lines': [
   '(i) ' + b('NAND') + ' (0 only on the 1 1 row) ' + T, '(ii) ' + b('AND') + ' (1 only on the 1 1 row) ' + T,
   '(iii) ' + b('NOR') + ' (1 only on the 0 0 row) ' + T, '(iv) ' + b('OR') + ' (0 only on the 0 0 row) ' + T],
  'note': 'There are two confusable pairs. NAND (%s) and OR (%s) each have three 1s, but NAND\'s 0 is on row 11 and OR\'s on row 00. '
          'AND (%s) and NOR (%s) each have a single 1, on row 11 and row 00. A student who counts the 1s and stops cannot separate either pair.'
          % (cs(GC['NAND']), cs(GC['OR']), cs(GC['AND']), cs(GC['NOR']))},
 {'n': '4', 'marks': 3, 'lines': [
   '(a) ' + b('NOT') + ': a triangle with a small circle on its point; <b>one</b> input and one output ' + T,
   '(b) ' + b('NAND') + ': the flat-backed D-shape of AND with a small circle on the output; two inputs ' + T,
   '(c) ' + b('NOR') + ': the curved-backed OR shape with a small circle on the output; two inputs ' + T],
  'figs': [symbol_row(['NOT', 'NAND', 'NOR'], ['(a)', '(b)', '(c)'])],
  'note': 'Withhold the mark if the circle is missing (that draws AND, OR or half a NOT) or if the NOT has two inputs. Do not penalise a wobbly curve: '
          'look for three features only, which are the body shape, the circle and the number of inputs.'},
 {'n': '5', 'marks': 5, 'lines': [
   '(a) ' + b('Q = (A OR B) NAND C') + ' ' + T + ' (accept P NAND C)',
   '(b) P = A OR B: ' + b(cs(B5P)) + ' ' + T,
   'Q is 0 only where P = 1 and C = 1, which is rows ' + nrows([1 - x for x in B5Q], 3) + ' ' + T,
   'every other row gives 1, so Q = ' + b(cs(B5Q)) + ' ' + T,
   '(c) ' + b(str(sum(B5Q))) + ' rows ' + T],
  'figs': [ans_tbl(V3, [('P', B5P), ('Q', B5Q)])],
  'note': 'Treating the NAND as an AND gives %s, which is the exact opposite of the correct column in every row: the circle was ignored. '
          '(c) is follow-through: accept the number of 1s in the student\'s own Q column if it is the right count for that column.' % cs(B5_asand)},
 {'n': '6', 'marks': 3, 'lines': [
   '(a) ' + b('X = NOT (A AND B)') + ' ' + T + ' (the brackets are essential)',
   '(b) ' + b('NAND') + ' ' + T,
   '(c) ' + b('Y = A AND (NOT B)') + ' ' + T + ' (accept A AND NOT B)'],
  'note': 'In circuit (i) the NOT comes <i>after</i> the AND, so the brackets must go round the AND. Writing it as NOT A AND B means (NOT A) AND B, '
          'whose column is %s against NAND\'s %s. In circuit (ii) the NOT sits on B alone, so brackets round the whole AND would be wrong there.'
          % (cs(K['A7']), cs(K['B6X']))},
 {'n': '7', 'marks': 5, 'lines': [
   '(a) &ldquo;Train approaching and barrier not down&rdquo; is ' + b('A AND (NOT B)') + ' ' + T,
   'Joined to the test switch by OR, with brackets round the AND part: ' + b('Q = (A AND (NOT B)) OR C') + ' ' + T,
   '(b) The rows with C = 1 (' + ', '.join(r for r in ones_at(K['B7'], 3) if r[2] == '1') + ') all give 1 ' + T,
   'Row 100 gives 1 (train approaching, barrier up, test switch off) ' + T,
   'Rows 000, 010 and 110 give 0, so Q = ' + b(cs(K['B7'])) + ' ' + T],
  'figs': [ans_tbl(V3, [('Q', K['B7'])])],
  'note': 'Dropping the NOT (reading &ldquo;not fully down&rdquo; as plain B) gives %s: row 100 turns to 0 and row 110 turns to 1. Joining with AND instead of OR '
          'gives %s. Follow-through is allowed in (b) if the table matches the student\'s own expression.' % (cs(K['B7_nonot']), cs(K['B7_and']))},
 {'n': '8', 'marks': 5, 'lines': [
   '(a) &ldquo;Card slot blocked and camera covered&rdquo; is ' + b('B AND C') + ' ' + T,
   'Joined to A by OR, brackets round the AND: ' + b('Q = A OR (B AND C)') + ' ' + T,
   '(b) An AND gate with inputs B and C ' + T,
   'An OR gate taking A and the output of the AND ' + T,
   'Every input labelled, output labelled Q, wires joined correctly ' + T],
  'figs': [fig(CIRC['B8'])],
  'note': 'The common bracket slip is (A OR B) AND C, whose column is %s against the correct %s: they differ on rows %s. A drawing with the AND as the last '
          'gate is the wrong circuit even if each symbol is perfect. If the expression in (a) is wrong but the drawing in (b) matches it, award (b) in full.'
          % (cs(K['B8_wrong']), cs(K['B8']), ' and '.join(diffrows(K['B8'], K['B8_wrong'], 3)))},
]

SC = [
 {'n': '1', 'marks': 2, 'lines': [
   '(i) ' + b('NAND') + ' and (iv) ' + b('OR') + ': both have seven 1s; the 0 of NAND is on 111, the 0 of OR on 000 ' + T,
   '(ii) ' + b('AND') + ' and (iii) ' + b('NOR') + ': both have a single 1; the 1 of AND is on 111, the 1 of NOR on 000 ' + T],
  'note': 'Award a pair only if both names in it are right. The pairs are the confusable ones: the gates are told apart by <i>where</i> the odd digit sits, '
          'not by how many 1s there are. Naming (i) as OR and (iv) as NAND swaps the pair and scores nothing for it.'},
 {'n': '2', 'marks': 3, 'lines': [
   '(a) ' + b('6') + ' inputs (2<super>6</super> = 64) ' + T,
   '(b) ' + b('8') + ' rows (half of the 16) ' + T,
   '(c) ' + b('15') + ' ' + T],
  'note': '(b) Four is the tempting wrong answer: the number of inputs rather than the number of rows. (c) A NAND is 0 only on the row where AND is 1, '
          'which is 1111, so 15 of the 16 rows are 1. The answer 1 comes from copying AND\'s single 1 and ignoring the circle.'},
 {'n': '3', 'marks': 4, 'lines': [
   '(a) X = ' + b(cs(K['C3X'])) + ' ' + T, 'Y = ' + b(cs(K['C3Y'])) + ' ' + T,
   '(b) ' + b('6') + ' rows (' + ', '.join(C3_diff) + '): X is 0 and Y is 1 on each; on 011 and 111 they agree ' + T,
   '(c) ' + b('NAND') + ' (three-input) ' + T],
  'figs': [ans_tbl(V3, [('X', K['C3X']), ('Y', K['C3Y'])])],
  'note': 'Reading X as NOT (A AND B AND C) makes it identical to Y, %s: seven 1s instead of one. NOT sticks to the thing straight after it, so in X the NOT '
          'belongs to A alone and the three conditions are &ldquo;A off, B on, C on&rdquo;. A student who has X wrong will get (b) wrong as well, '
          'and (b) should be marked as follow-through: 0 differences if X = Y.' % cs(K['C3Y'])},
 {'n': '4', 'marks': 5, 'lines': [
   '(a) ' + b('Q = (A AND B) OR (B NOR C)') + ': the two bracketed gates ' + T,
   'joined by an OR, with brackets round each (accept P OR R) ' + T,
   '(b) P = A AND B: ' + b(cs(C4P)) + ' ' + T,
   'R = B NOR C: ' + b(cs(C4R)) + ' ' + T,
   'Q = P OR R: ' + b(cs(C4Q)) + ' ' + T],
  'figs': [ans_tbl(V3, [('P', C4P), ('R', C4R), ('Q', C4Q)])],
  'note': 'Treating the NOR as an OR (R = B OR C) gives Q = %s: the circle was ignored. B feeds both first-level gates, so a student who draws only one '
          'B wire into the picture in their head reads the circuit wrongly. Sanity check: the correct Q has %d ones.'
          % (cs(K['C4_wrong']), sum(C4Q))},
 {'n': '5', 'marks': 3, 'lines': [
   '(a) Circuit ' + b('(ii)') + ' ' + T,
   '(b) Rules out (i): row ' + b(' or '.join(diffrows(K['C5_ok'], K['C5_or'], 3))) + ', where (i) gives 0 and the table says 1 ' + T,
   'Rules out (iii): row ' + b(' or '.join(diffrows(K['C5_ok'], K['C5_nor'], 3))) + ' (on ' + diffrows(K['C5_ok'], K['C5_nor'], 3)[0] + ' (iii) gives '
   + str(K['C5_nor'][int(diffrows(K['C5_ok'], K['C5_nor'], 3)[0], 2)]) + ' against the table\'s ' + str(K['C5_ok'][int(diffrows(K['C5_ok'], K['C5_nor'], 3)[0], 2)])
   + '; on ' + diffrows(K['C5_ok'], K['C5_nor'], 3)[1] + ' it gives ' + str(K['C5_nor'][int(diffrows(K['C5_ok'], K['C5_nor'], 3)[1], 2)]) + ' against '
   + str(K['C5_ok'][int(diffrows(K['C5_ok'], K['C5_nor'], 3)[1], 2)]) + ') ' + T],
  'figs': [ans_tbl(V3, [('X', K['C5_ok']), ('(i)', K['C5_or']), ('(ii)', K['C5_ok']), ('(iii)', K['C5_nor'])])],
  'note': 'The decoys were built to agree with the table on six of the eight rows, so most rows prove nothing: all three circuits give the same answer on rows %s. '
          'A student who checks those rows first can tick any circuit. The method is to test a row where the candidates disagree. A row quoted '
          'without the circuit\'s output on it is half an answer: award (b)\'s marks only if the wrong output is stated.' % ', '.join(C5_agree)},
 {'n': '6', 'marks': 3, 'lines': [
   '(a) Rows ' + b(' and '.join(diffrows(HIS_P, TRUE_P, 3))) + ' ' + T,
   '(b) For 1 1 he gave 0: he treated OR as &ldquo;one or the other but not both&rdquo;, when OR gives 1 if at least one input is 1 ' + T,
   '(c) ' + b(str(len(diffrows(HIS_Q, TRUE_Q, 3)))) + ' cell (the Q in row ' + diffrows(HIS_Q, TRUE_Q, 3)[0] + ') ' + T],
  'figs': [ans_tbl(V3, [('P', TRUE_P), ('R', TRUE_R), ('Q', TRUE_Q)])],
  'note': 'His P column %s is XOR\'s, not OR\'s %s. Two wrong cells in P produce only one wrong cell in Q: on row 111 the NOT gives R = 0, and a NAND with a 0 on '
          'either input outputs 1 whatever P is, so the error is hidden there. Accept 1 only for (c); the answer 2 counts the P cells.'
          % (cs(HIS_P), cs(TRUE_P))},
 {'n': '7', 'marks': 5, 'lines': [
   '(a) ' + b('A AND (NOT B)') + ' for &ldquo;too hot and the soil is not wet&rdquo; ' + T,
   'OR with C, then AND with D, brackets showing the order: ' + b('Q = ((A AND (NOT B)) OR C) AND D') + ' ' + T,
   '(b) ' + b(str(sum(K['C7']))) + ' rows ' + T,
   'D = 0 gives 0 on all 8 of its rows. With D = 1 the inner part is 1 when C = 1 (4 rows) or when A = 1, B = 0, C = 0 (1 row): 4 + 1 = %d ' % sum(K['C7']) + T,
   '(c) Q = ' + b('0') + ': with A = 1 and B = 1 the first part is 0 (the soil is wet), and C = 0, so the OR is 0 and the AND with D is 0 ' + T],
  'note': 'Forgetting the pump (ignoring D) gives %d rows: the inner part is 1 on 5 of its 8 rows, and doubling over both values of D gives 10. '
          'Breaking the bracket, (A AND NOT B) OR (C AND D), gives %d rows. Neither is the sentence in the question, whose last clause makes D a veto.'
          % (sum(K['C7_nod']), sum(K['C7_bracket']))},
 {'n': '8', 'marks': 5, 'lines': [
   '(a) P = ' + b(cs(C8P)) + ' and R = ' + b(cs(C8R)) + ' ' + T,
   'Q = ' + b(cs(C8Q)) + ' ' + T,
   '(b) A NAND with both inputs joined gives NOT (A AND A), and A AND A is just A, so the output is NOT A: 0 gives 1 and 1 gives 0 ' + T,
   '(c) One NAND with both inputs wired to A and its output labelled Q ' + T,
   '(d) ' + b('OR') + ' ' + T],
  'figs': [ans_tbl(['A', 'B'], [('P', C8P), ('R', C8R), ('Q', C8Q)]), fig(CIRC['C8_not'])],
  'note': 'A student who thinks a joined NAND &ldquo;copies&rdquo; its input writes P = 0, 0, 1, 1 and R = 0, 1, 0, 1, and then Q (a NAND of those) = %s: '
          'that is NAND\'s own column, not OR\'s. If Q comes out as 1, 1, 1, 0 the flip in the first two gates was missed.'
          % cs(fcol(lambda a, b_: not (a and b_), 2))},
]

SD = [
 {'n': '1', 'marks': 3, 'lines': [
   'P = A NOR B: ' + b(cs(D1P)) + ' ' + T, 'R = NOT C: ' + b(cs(D1R)) + ' ' + T, 'Q = P NOR R: ' + b(cs(D1Q)) + ' ' + T],
  'figs': [ans_tbl(V3, [('P', D1P), ('R', D1R), ('Q', D1Q)])],
  'note': 'Q is 1 only when P = 0 and R = 0: that is when A or B is 1 and C is 1, rows %s. Using C instead of NOT C in the last gate gives %s. '
          'If P and R are right but Q is wrong, the final NOR was applied as an OR: award the marks for P and R.'
          % (nrows(D1Q, 3), cs(K['D1_nonot']))},
 {'n': '2', 'marks': 3, 'lines': ['(a) ' + b(D2_a) + ' ' + T, '(b) ' + b('Row %d' % D2_b) + ' ' + T, '(c) ' + b(D2_c) + ' ' + T],
  'note': 'Counting from 0 instead of 1 gives %s for (a) (that is the seventh row), 6 for (b), and %s for (c). The first row is 000 (or 0000), so row <i>n</i> is the '
          'binary number for <i>n</i> &minus; 1. The question states that rows are numbered from 1, so the off-by-one answers are marked wrong.'
          % (D2_a_wrong, ''.join(map(str, rows(4)[10])))},
 {'n': '3', 'marks': 3, 'lines': [
   '(a) ' + b('OR') + ' ' + T, ' ' + b('NAND') + ' ' + T,
   '(b) ' + b(' or '.join(diffrows(GC['OR'], GC['NAND'], 2))) + ': OR and NAND disagree on this row (on 00 OR gives 0 and NAND gives 1; on 11 OR gives 1 and NAND gives 0) ' + T],
  'note': 'Rows %s give the same answer for both gates, so they tell you nothing: a student who offers one of them has not understood what &ldquo;tell apart&rdquo; asks. '
          'If a student names AND or NOR they have counted the 1s as one rather than three.'
          % ' and '.join(r for r in [rl(2, i) for i in range(4)] if r not in diffrows(GC['OR'], GC['NAND'], 2))},
 {'n': '4', 'marks': 5, 'lines': [
   '(a) ' + b('Q = (A NAND B) NAND (B NAND C)') + ': the two inner NANDs ' + T,
   'joined by a third NAND, with brackets round each inner gate (accept P NAND R) ' + T,
   '(b) P = A NAND B: ' + b(cs(D4P)) + ' ' + T, 'R = B NAND C: ' + b(cs(D4R)) + ' ' + T, 'Q = P NAND R: ' + b(cs(D4Q)) + ' ' + T],
  'figs': [ans_tbl(V3, [('P', D4P), ('R', D4R), ('Q', D4Q)])],
  'note': 'Reading the NANDs as ANDs gives Q = %s. In fact Q is 1 where B = 1 and at least one of A, C is 1 (rows %s). The last gate is the one to watch: '
          'P and R are both 1 on most rows, and a NAND of two 1s is 0.' % (cs(K['D4_asand']), nrows(D4Q, 3))},
 {'n': '5', 'marks': 4, 'lines': [
   '(a) X = ' + b(cs(K['D5X'])) + ' ' + T, 'Y = ' + b(cs(K['D5Y'])) + ' ' + T, 'Z = ' + b(cs(K['D5Z'])) + ' ' + T,
   '(b) ' + b('X and Y') + ' are identical, and both equal ' + b('NAND') + ' ' + T],
  'figs': [ans_tbl(['A', 'B'], [('X', K['D5X']), ('Y', K['D5Y']), ('Z', K['D5Z'])])],
  'note': 'Z is NOR\'s column. A student who believes NOT (A AND B) is the same as (NOT A) AND (NOT B), with the NOT simply going inside, pairs X with Z. '
          'It does not: the NOT also changes the AND into an OR. That belief gives %s for X, against the true %s.' % (cs(K['D5Z']), cs(K['D5X']))},
 {'n': '6', 'marks': 4, 'lines': [
   '(a) &ldquo;Unless both are on&rdquo; is NOT (B AND C), which is ' + b('B NAND C') + ' ' + T,
   'ANDed with the timer: ' + b('Q = A AND (B NAND C)') + ' (accept A AND (NOT (B AND C))) ' + T,
   '(b) A NAND gate taking B and C ' + T,
   'Its output and A going into an AND gate, with the output labelled Q (accept an AND, then a NOT, then an AND as the equivalent circuit) ' + T],
  'figs': [fig(CIRC['D6'])],
  'note': 'Reading &ldquo;unless both&rdquo; as &ldquo;unless either&rdquo; gives A AND (B NOR C) = %s: the bell then falls silent whenever one switch is on. The question supplies '
          'the test row: only B on, timer firing must ring, which is row 110, where the right expression gives %d and the wrong one gives %d.'
          % (cs(K['D6_wrong']), K['D6'][6], K['D6_wrong'][6])},
 {'n': '7', 'marks': 3, 'lines': [
   '(a) A first NAND taking A and B, its output labelled P ' + T,
   'A second NAND with both its inputs joined to P, output Q ' + T,
   '(b) P = ' + b(cs(D7P)) + ' and Q = ' + b(cs(D7Q)) + ' (the table for the drawn circuit; Q must equal A AND B) ' + T],
  'figs': [fig(CIRC['D7']), ans_tbl(['A', 'B'], [('P', D7P), ('Q', D7Q)])],
  'note': 'If the second gate is read as passing P straight through, Q = P = %s, which is NAND\'s column: the student has rebuilt NAND, not AND. The second gate '
          'is the joined-inputs NOT, so Q = NOT P = %s.' % (cs(D7P), cs(D7Q))},
 {'n': '8', 'marks': 5, 'lines': [
   '(i) The mistake: the circle on the output <b>flips</b> the answer of the AND; it does not leave it unchanged ' + T,
   '&nbsp; &nbsp; &nbsp;Correct version: NAND gives <b>0 only when both inputs are 1</b>, and 1 on the other three rows ' + T,
   '&nbsp; &nbsp; &nbsp;Evidence: on the row A = 1, B = 1, AND gives 1, so NAND gives 0 ' + T,
   '(ii) The mistake: NOT applies only to the thing straight after it, so NOT A AND B means (NOT A) AND B, not NOT (A AND B) ' + T,
   '&nbsp; &nbsp; &nbsp;Correct version, shown with a row: with A = 1 and B = 0, (NOT A) AND B gives 0 but NOT (A AND B) gives 1, so they differ ' + T],
  'note': 'Accept any reasonable wording, and give credit for a correct version that is stated without a separate mistake sentence if the correction is explicit. '
          '&ldquo;NAND is the opposite of AND&rdquo; with no row earns the first two marks of (i) at most. The page\'s trap list names both of these wrong sentences. Marking them in Rohan\'s notebook is far easier to face than being told you made them, and it is the same thinking.'},
]
SCHEMES = [('Paper A — Medium', SA), ('Paper B — Medium', SB), ('Paper C — Hard', SC), ('Paper D — Hard', SD)]

# =====================================================================================================
# 7. Verification. Runs on every build. Any assertion firing means the content is wrong, not the check.
# =====================================================================================================
VARS = {'A8': ['M', 'P']}
EXPR = {
 'A5': ['(A OR B) AND (NOT C)', '(A OR B) AND NOT C'], 'A6X': ['NOT A OR B'], 'A6Y': ['NOT (A OR B)'],
 'A7': ['(NOT A) AND B', 'NOT A AND B'], 'A8': ['(NOT M) AND (NOT P)', 'NOT M AND NOT P'], 'A9': ['A NAND A', 'NOT A'],
 'B1_and': ['A AND B AND C'], 'B1_or': ['A OR B OR C'],
 'B5': ['(A OR B) NAND C'], 'B6X': ['NOT (A AND B)', 'A NAND B'], 'B6Y': ['A AND (NOT B)', 'A AND NOT B'],
 'B7': ['(A AND (NOT B)) OR C', '(A AND NOT B) OR C'], 'B8': ['A OR (B AND C)'],
 'C3X': ['NOT A AND B AND C'], 'C3Y': ['NOT (A AND B AND C)'],
 'C4': ['(A AND B) OR (B NOR C)'], 'C6': ['(A OR B) NAND (NOT C)'],
 'C7': ['((A AND (NOT B)) OR C) AND D', '((A AND NOT B) OR C) AND D'],
 'C8': ['(A NAND A) NAND (B NAND B)', 'A OR B'],
 'D1': ['(A NOR B) NOR (NOT C)'], 'D4': ['(A NAND B) NAND (B NAND C)'],
 'D5X': ['NOT (A AND B)'], 'D5Y': ['(NOT A) OR (NOT B)'], 'D5Z': ['(NOT A) AND (NOT B)'],
 'D6': ['A AND (B NAND C)', 'A AND (NOT (B AND C))'], 'D7': ['(A NAND B) NAND (A NAND B)', 'A AND B'],
}
DRAWN = {'A5': 'A5', 'A9': 'A9', 'A7': 'A7', 'B5': 'B5', 'B6X': 'B6X', 'B6Y': 'B6Y', 'B8': 'B8', 'C4': 'C4',
         'C5_ii': 'C5_ok', 'C5_i': 'C5_or', 'C5_iii': 'C5_nor', 'C6': 'C6', 'C8': 'C8', 'D4': 'D4', 'D6': 'D6', 'D7': 'D7'}

def _verify():
    # -- 1. every drawn circuit, and every typed answer, agrees with the plain-Python behaviour
    for ck, kk in DRAWN.items():
        c = CIRC[ck]
        got = col(c.ast(), c.vars)
        assert got == K[kk], (ck, got, K[kk])
        assert len(got) == 2 ** len(c.vars)
        for gid, g in c.byid.items():
            if g[1] == 'NOT':
                assert len(g[2]) == 1, 'a NOT must have one input'
            else:
                assert len(g[2]) == 2, 'every other gate here has two inputs'
    for kk, strs in EXPR.items():
        vs = VARS.get(kk, ['A', 'B', 'C', 'D'][:NIN[kk]])
        for s in strs:
            assert col(parse(s, vs), vs) == K[kk], (kk, s, col(parse(s, vs), vs), K[kk])
    # the circuits' own printed expressions parse back to the same column
    for ck, kk in DRAWN.items():
        c = CIRC[ck]
        assert col(parse(c.expr(), c.vars), c.vars) == K[kk], (ck, c.expr())
    # the wrong-method expressions must also be what the notes claim they are
    for s in ('A OR B AND NOT C', 'A AND B OR C', 'NOT A AND B OR C'):
        try:
            parse(s, V3); raise AssertionError('should need brackets: ' + s)
        except ValueError:
            pass
    assert col(parse('NOT A AND B', ['A', 'B']), ['A', 'B']) == K['A7'] != K['B6X']
    assert col(parse('(A OR B) AND C', V3), V3) == K['B8_wrong']
    assert col(parse('A OR (B AND C)', V3), V3) == K['B8']
    assert col(parse('A AND (B NOR C)', V3), V3) == K['D6_wrong']
    assert col(parse('(A AND B) OR (B OR C)', V3), V3) == K['C4_wrong']
    assert col(parse('(A AND B) AND (B AND C)', V3), V3) == K['D4_asand']
    # -- 2. gate-level facts the notes rely on
    assert B5_asand == [1 - x for x in B5Q]
    assert K['A8'] == GC['NOR'] and K['A9'] == [1, 0] and K['A6Y'] == GC['NOR'] and K['B6X'] == GC['NAND']
    assert K['D5X'] == K['D5Y'] == GC['NAND'] and K['D5Z'] == GC['NOR'] and K['D5X'] != K['D5Z']
    assert C8Q == GC['OR'] and D7Q == GC['AND'] and K['D7'] == D7Q
    assert [g for g, c in GC.items() if sum(c) == 3] == ['OR', 'NAND'], 'D3: exactly OR and NAND have three 1s'
    assert sum(GC['AND']) == 1 and sum(GC['NOR']) == 1
    assert diffrows(GC['OR'], GC['NAND'], 2) == ['00', '11']
    assert K['A6X'] not in GC.values(), 'A6: X must not equal any single gate'
    # distinct answers where the question needs them
    for cols_ in (B_COLS, C_COLS):
        assert len(set(map(tuple, cols_))) == 4, 'gate-identification columns must all differ'
    assert len(set(['NOR', 'NOT', 'AND', 'NAND'])) == 4
    assert [sum(c) for c in C_COLS] == [7, 1, 1, 7]
    # every three-input circuit column printed in the papers is different from every other
    three = [K[k] for k in ('A5', 'B5', 'B7', 'B8', 'C4', 'C5_ok', 'C6', 'D1', 'D4', 'D6')]
    assert len(set(map(tuple, three))) == len(three), 'two papers share an output column'
    for c_ in three:
        assert 2 <= sum(c_) <= 6, 'avoid near-constant columns'
    # -- 3. decoys differ from the right answer exactly as the scheme says
    for dk in ('C5_or', 'C5_nor'):
        assert len(diffrows(K['C5_ok'], K[dk], 3)) == 2, dk
    assert len(set(map(tuple, (K['C5_ok'], K['C5_or'], K['C5_nor'])))) == 3
    assert diffrows(K['C5_ok'], K['C5_or'], 3) == ['011', '101'] and diffrows(K['C5_ok'], K['C5_nor'], 3) == ['001', '111']
    assert C5_agree == ['000', '010', '100', '110']
    # Tom's table: P wrong on 110 and 111 only; Q wrong on one row; the other error is hidden
    assert diffrows(HIS_P, TRUE_P, 3) == ['110', '111']
    assert diffrows(HIS_Q, TRUE_Q, 3) == ['110']
    assert HIS_P == fcol(lambda a, b_, c_: a != b_, 3)
    # -- 4. counting facts
    assert K['C7'].count(1) == 5 and K['C7_nod'].count(1) == 10 and K['C7_bracket'].count(1) == sum(K['C7_bracket'])
    assert len(K['C7']) == 16
    assert C3_diff == ['000', '001', '010', '100', '101', '110']
    assert sum(fcol(lambda a, b_, c_, d_: not (a and b_ and c_ and d_), 4)) == 15
    assert sum(1 for r in rows(4) if r[0] == 1) == 8
    assert D4Q == fcol(lambda a, b_, c_: b_ and (a or c_), 3)
    assert K['D6'][6] == 1 and K['D6_wrong'][6] == 0
    assert (D2_a, D2_a_wrong, D2_b, D2_c) == ('101', '110', 7, '1001') and 2 ** 5 == 32 and 2 ** 6 == 64 and 2 ** 4 == 16
    # -- 5. marks: every paper is 30, parts sum, three sections, schemes match the papers
    for code, spec in SPECS:
        qs = spec['questions']
        assert sum(q['marks'] for q in qs) == spec['marks'] == 30, (code, sum(q['marks'] for q in qs))
        assert sum(1 for q in qs if q.get('section')) == 3, code + ': three named sections'
        for i, q in enumerate(qs, 1):
            if q.get('parts'):
                assert sum(p['marks'] for p in q['parts']) == q['marks'], (code, i)
            else:
                assert q['marks'] > 0, (code, i)
        assert qs[0].get('section') and qs[-1].get('section') is None
    # paper D ends with the standing diagnosis question
    qd = D['questions'][-1]
    assert qd.get('quote') and len(qd['quote'][0]) == 2 and qd['marks'] == 5
    for (title, sc), (code, spec) in zip(SCHEMES, SPECS):
        assert len(sc) == len(spec['questions']), code
        for s, q in zip(sc, spec['questions']):
            assert s['marks'] == q['marks'], (code, s['n'])
            tags = sum(line.count(T) for line in s['lines'])
            assert tags == s['marks'], (code, s['n'], tags, s['marks'])
            assert s.get('note'), (code, s['n'], 'every question needs a note')
        assert sum(s['marks'] for s in sc) == 30
    # medium papers print the reminder, hard papers do not and carry the unfamiliar-scenario sentence
    assert A.get('reminder') and B.get('reminder') and not C.get('reminder') and not D.get('reminder')
    for spec in (C, D):
        assert any('machines you may not have seen' in i for i in spec['instructions'])
    assert 'calculator' in A['instructions'][1]

# =====================================================================================================
# 8. Build
# =====================================================================================================
def main():
    _verify()
    files = []
    for code, spec in SPECS:
        p = os.path.join(OUT, 'computing-logicgates-paper-%s.pdf' % code)
        build_paper2(spec, p)
        files.append(p)
    p = os.path.join(OUT, 'computing-logicgates-answers.pdf')
    build_scheme2([{'title': t, 'meta': '30 marks', 'questions': sc} for t, sc in SCHEMES], p, {
        'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes', 'meta': 'Papers A to D · 30 marks each · tutor copy',
        'intro': 'Marks in square brackets show how the total is split, one per line. Marks on this topic are lost to a short list of habits: '
                 'ignoring the small circle on NAND and NOR, reading OR as &ldquo;one or the other&rdquo;, attaching NOT to the wrong thing '
                 '(NOT A AND B against NOT (A AND B)), missing a row in a truth table, and testing rows that cannot tell two circuits apart. '
                 'Every note below names the mistake that question was built to catch and shows the wrong column it produces, so that you can recognise '
                 'the pattern when it turns up in a different paper. Every table here was computed by enumerating all the input combinations.',
        'footer': 'Mark schemes · ' + TOPIC})
    files.append(p)
    print('verify ok')
    print('\n'.join(files))

if __name__ == '__main__':
    main()
