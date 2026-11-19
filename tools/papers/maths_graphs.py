#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maths, Graphs: functions, plotting, gradient and intercept, interpreting graphs.
Papers A to D and the mark-scheme booklet.

Every number that reaches a PDF is computed here first (section 1, `N`), and every printed graph is drawn
FROM the same data the answers are computed from (`G`), so a drawn line and its mark-scheme gradient cannot
disagree. `_verify()` recomputes the answers independently with Fractions, checks every drawn line really
passes through the points the questions name, checks that each blank grid is big enough for the line the
student is asked to draw, and asserts the marks.

paper_lib.py is not edited. It cannot embed a drawing, so build_paper2 / build_scheme2 below follow its
layout code and add `fig` (a drawn graph or blank grid) to questions and parts — the same approach as
computing_logicgates.py.
"""
import os, sys
from fractions import Fraction as Fr
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, Flowable, KeepTogether)
from paper_lib import (AVAIL, INK, SOFT, LINE, PAPERBG, S_Q, S_NOTE, S_SEC, S_ANS, S_ANSN, S_MARKS,
                       S_META, S_EYEBROW, S_TITLE, Ruled, Rule, NumberedCanvas, _header, _qrow, _grid,
                       MARGIN_L, MARGIN_R, MARGIN_T, MARGIN_B)

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Mathematics · Grade 7 · Graphs'
TOPIC = 'Functions and Graphs'
GRIDC = colors.HexColor('#D9D5CC')
LINEC = colors.HexColor('#2B5797')

# =====================================================================================================
# 1. Arithmetic. Everything here is exact.
# =====================================================================================================
def grad(p, q):
    return Fr(q[1] - p[1], q[0] - p[0])
def through(p, q):
    m = grad(p, q); return m, p[1] - m * p[0]
def meet(m1, c1, m2, c2):
    x = Fr(c2 - c1, 1) / (m1 - m2); return x, m1 * x + c1
def xint(m, c):
    return Fr(-c, 1) / m
def f(v):
    """A Fraction for print: whole numbers plain, halves and quarters as decimals, else a/b."""
    v = Fr(v)
    if v.denominator == 1:
        s = str(v.numerator)
    elif v.denominator in (2, 4, 5, 10, 20, 25):
        s = ('%.3f' % float(v)).rstrip('0').rstrip('.')
    else:
        s = '%d/%d' % (v.numerator, v.denominator)
    return s.replace('-', '&minus;')
def eq(m, c, v='x', lhs='y'):
    m, c = Fr(m), Fr(c)
    t = '' if m == 1 else ('&minus;' if m == -1 else f(m))
    s = '%s = %s%s' % (lhs, t, v) if m != 0 else '%s = ' % lhs
    if m == 0: return s + f(c)
    if c > 0: s += ' + ' + f(c)
    if c < 0: s += ' &minus; ' + f(-c)
    return s

N = {}
# ---- Paper A
mach = lambda x: 4 * x - 3
N['A1'] = (mach(5), mach(-2), Fr(25 + 3, 4))
N['A2'] = [3 * x - 2 for x in range(-2, 4)]
N['A3'] = through((0, -1), (3, 5))
N['A4'] = (grad((2, 3), (6, 11)), grad((-1, 4), (3, -8)))
N['A5c'] = (Fr(8, 2), Fr(6, 2))
N['A6'] = (4 * 3 - 2 == 10)
N['A7'] = dict(m=grad((0, 40), (8, 160)), c=40)
N['A7'].update(at6=N['A7']['m'] * 6 + 40, at20=N['A7']['m'] * 20 + 40)
N['A8'] = through((1, 5), (4, 14))
# ---- Paper B
fb = lambda x: 2 * x + 5
N['B1'] = (fb(3), fb(-4), Fr(19 - 5, 2), Fr(-5, 2))
N['B2'] = [Fr(10 - x, 2) for x in (-2, 0, 2, 4, 6)]
N['B3'] = through((0, 4), (2, 0))
N['B4b'] = 9 - 3 * 2
N['B5'] = (grad((0, -3), (4, 5)), grad((-2, 6), (2, -2)))
N['B6c'] = (Fr(12, 3), Fr(-9, 3))
N['B7'] = dict(m=grad((0, 0), (50, 80)))
N['B7'].update(km30=N['B7']['m'] * 30, mi64=Fr(64) / N['B7']['m'], km200=N['B7']['m'] * 200)
N['B8'] = dict(c3=250 * 3 + 300, h=Fr(1300 - 300, 250))
# ---- Paper C
mc = lambda x: Fr(x + 3, 2) - 1
N['C1'] = (mc(-7), (4 + 1) * 2 - 3)
N['C2'] = ((Fr(-4, 2), Fr(10, 2)), (Fr(6, 3), Fr(12, 3)), (Fr(1, 2), Fr(8, 2)))
N['C3'] = through((-3, 8), (5, -8)); N['C3x'] = xint(*N['C3'])
N['C4'] = through((0, 10), (20, 70)); N['C4wrong'] = Fr(6, 4)
N['C5'] = (grad((-1, 1), (2, 7)), grad((2, 7), (5, 13)))
m5, c5 = through((-1, 1), (2, 7)); N['C5k'] = (21 - c5) / m5
N['C6'] = dict(fill=Fr(240, 8), drain=Fr(240, 28 - 12))
N['C6'].update(up120=Fr(120) / N['C6']['fill'], down120=12 + Fr(120) / N['C6']['drain'],
               early=8 + Fr(240) / N['C6']['drain'])
N['C7'] = dict(u=Fr(150 - 30, 8 - 6))
N['C7'].update(cost=150 + 6 * N['C7']['u'], X100=150 + 6 * 100, Y100=30 + 8 * 100)
# ---- Paper D
a = Fr(22 - 10, 7 - 3); b = 10 - a * 3
N['D1'] = (a, b, (49 - b) / a)
N['D2'] = (Fr(-2, 4), Fr(16, 4)); N['D2x'] = xint(*N['D2']); N['D2c'] = 7 - N['D2'][0] * (-2)
N['D3'] = meet(3, -5, -1, 7); N['D3m'] = (N['D3'][1] - 1) / N['D3'][0]
N['D4'] = meet(2, 4, -1, 7); N['D4x'] = (xint(2, 4), xint(-1, 7))
N['D4area'] = Fr(1, 2) * (N['D4x'][1] - N['D4x'][0]) * N['D4'][1]
N['D5'] = meet(2, -1, -1, 5)
N['D6'] = dict(m=grad((0, 50), (375, 20)))
N['D6'].update(per100=-N['D6']['m'] * 100, empty=Fr(50) / -N['D6']['m'])
N['D7'] = (Fr(6, 3), Fr(12, 3), grad((-3, 5), (1, -3)), Fr(-3 - 5, 1 - 3))

# =====================================================================================================
# 2. The graph flowable: a grid drawn to scale, optionally with lines, points and labels.
# =====================================================================================================
class Graph(Flowable):
    def __init__(self, x0, x1, xs, y0, y1, ys, w_mm=None, h_mm=None, sq_mm=None, xl=1, yl=1,
                 lines=(), pts=(), xt='x', yt='y', labels=()):
        Flowable.__init__(self)
        self.x0, self.x1, self.xs, self.y0, self.y1, self.ys = x0, x1, xs, y0, y1, ys
        self.nx, self.ny = round((x1 - x0) / xs), round((y1 - y0) / ys)
        if sq_mm:
            self.gw, self.gh = self.nx * sq_mm * mm, self.ny * sq_mm * mm
        else:
            self.gw, self.gh = w_mm * mm, h_mm * mm
        self.L, self.B = 13 * mm, 12 * mm
        self.width, self.height = self.gw + self.L + 8 * mm, self.gh + self.B + 6 * mm
        self.xl, self.yl, self.lines, self.pts, self.xt, self.yt, self.labels = xl, yl, lines, pts, xt, yt, labels

    def X(self, x): return self.L + (x - self.x0) / (self.x1 - self.x0) * self.gw
    def Y(self, y): return self.B + (y - self.y0) / (self.y1 - self.y0) * self.gh

    def draw(self):
        c = self.canv
        c.setLineWidth(0.35); c.setStrokeColor(GRIDC)
        for i in range(self.nx + 1):
            x = self.X(self.x0 + i * self.xs); c.line(x, self.B, x, self.B + self.gh)
        for j in range(self.ny + 1):
            y = self.Y(self.y0 + j * self.ys); c.line(self.L, y, self.L + self.gw, y)
        ax = self.X(0) if self.x0 <= 0 <= self.x1 else self.L
        ay = self.Y(0) if self.y0 <= 0 <= self.y1 else self.B
        c.setStrokeColor(INK); c.setLineWidth(0.9)
        c.line(self.L, ay, self.L + self.gw, ay); c.line(ax, self.B, ax, self.B + self.gh)
        c.setFont('Mono', 6.6); c.setFillColor(SOFT)
        for i in range(0, self.nx + 1, self.xl):
            v = self.x0 + i * self.xs
            if v == 0 and self.x0 < 0: continue
            c.drawCentredString(self.X(v), ay - 7.5, f(v).replace('&minus;', '−'))
        for j in range(0, self.ny + 1, self.yl):
            v = self.y0 + j * self.ys
            if v == 0 and self.y0 < 0: continue
            c.drawRightString(ax - 2.5, self.Y(v) - 2.2, f(v).replace('&minus;', '−'))
        if self.x0 < 0 and self.y0 < 0:
            c.drawRightString(ax - 2.5, ay - 7.5, '0')
        c.setFont('UI-Bold', 7.8); c.setFillColor(INK)
        if ay == self.B:
            c.drawRightString(self.L + self.gw, self.B - 17, self.xt)
        else:
            c.drawRightString(self.L + self.gw, ay + 3, self.xt)
        c.drawString(ax + 3, self.B + self.gh + 2.5, self.yt)
        # lines, clipped to the grid
        p = c.beginPath(); p.rect(self.L, self.B, self.gw, self.gh)
        c.saveState(); c.clipPath(p, stroke=0, fill=0)
        c.setStrokeColor(LINEC); c.setLineWidth(1.5)
        for ln in self.lines:
            for (u, v), (s, t) in zip(ln[:-1], ln[1:]):
                c.line(self.X(u), self.Y(v), self.X(s), self.Y(t))
        c.restoreState()
        c.setFillColor(INK)
        for (u, v, lab) in self.pts:
            c.circle(self.X(u), self.Y(v), 1.5, stroke=0, fill=1)
            if lab:
                c.setFont('UI-Bold', 7.6); c.drawString(self.X(u) + 3, self.Y(v) + 3, lab)
        c.setFont('Body-Italic', 7.4)
        for (u, v, t) in self.labels:
            c.drawString(self.X(u), self.Y(v), t)

def on_line(m, c, pts):
    return all(Fr(y) == m * Fr(x) + c for x, y in pts)

# The printed graphs. Each is (flowable, the polyline it shows) so _verify can test the line.
G = {
 'A2': Graph(-2, 3, 1, -8, 8, 1, w_mm=72, h_mm=96, yl=2),
 'A3': Graph(-1, 4, 1, -3, 8, 1, sq_mm=5.2, lines=[[(-1, -3), (4, 7)]]),
 'A7': Graph(0, 8, 1, 0, 200, 10, w_mm=104, h_mm=76, yl=2, lines=[[(0, 40), (8, 160)]],
             xt='distance (km)', yt='fare (₹)'),
 'B2': Graph(-2, 6, 1, -1, 7, 1, sq_mm=5.6),
 'B3': Graph(-1, 4, 1, -4, 6, 1, sq_mm=5.2, lines=[[(-1, 6), (4, -4)]], pts=[]),
 'B7': Graph(0, 50, 5, 0, 80, 8, w_mm=110, h_mm=80, yl=2, lines=[[(0, 0), (50, 80)]],
             xt='miles', yt='kilometres'),
 'C4': Graph(0, 30, 5, 0, 100, 10, w_mm=90, h_mm=84, lines=[[(0, 10), (30, 100)]],
             pts=[(0, 10, 'P'), (20, 70, 'Q')]),
 'C6': Graph(0, 30, 2, 0, 280, 20, w_mm=120, h_mm=74, xl=1, yl=2,
             lines=[[(0, 0), (8, 240), (12, 240), (28, 0), (30, 0)]], xt='time (minutes)', yt='volume (litres)'),
 'D5': Graph(-1, 4, 1, -3, 7, 1, w_mm=80, h_mm=100),
 'D6': Graph(0, 500, 25, 0, 60, 5, w_mm=120, h_mm=66, xl=4, yl=2,
             lines=[[(0, 50), (500, 10)]], pts=[(0, 50, '(0, 50)'), (375, 20, '(375, 20)')],
             xt='distance driven (km)', yt='fuel in tank (litres)'),
}

# =====================================================================================================
# 3. Layout (same as paper_lib, plus figures)
# =====================================================================================================
def _ind(fl, indent):
    if not indent: return fl
    t = Table([[fl]], colWidths=[AVAIL], hAlign='LEFT')
    t.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), indent), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return t

def _extras(o, indent=0):
    out = []
    if o.get('fig') is not None:
        out += [Spacer(1, 4), _ind(o['fig'], indent + 14), Spacer(1, 3)]
    if o.get('grid'):
        out += [Spacer(1, 4), _ind(_grid(o['grid'], o.get('grid_widths')), indent), Spacer(1, 3)]
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
        if blocks:
            head += blocks[0]; blocks = blocks[1:]
        story.append(KeepTogether(head))
        for blk in blocks:
            story.append(KeepTogether(blk))
        if q.get('tip') and q.get('parts'):
            story += [Spacer(1, 2), Paragraph(q['tip'], S_NOTE)]
        story.append(Spacer(1, 10))
    story += [Spacer(1, 4), Rule(thickness=0.6, colour=LINE), Spacer(1, 4), Paragraph(spec['endnote'], S_NOTE)]
    _doc(path, spec['title'], story, spec['footer'])
    return path

def build_scheme2(schemes, path, header):
    story = [Paragraph(header['eyebrow'].upper(), S_EYEBROW), Paragraph(header['title'], S_TITLE),
             Paragraph(header['meta'].upper(), S_META), Spacer(1, 5), Rule(), Spacer(1, 8),
             Paragraph(header['intro'], S_NOTE), Spacer(1, 12)]
    for si, sc in enumerate(schemes):
        if si: story.append(Spacer(1, 6))
        head = Table([[Paragraph('<font name="UI-Bold" size="12">%s</font>' % sc['title'], S_ANS),
                       Paragraph('<font name="Mono" size="8" color="#5A5A66">%s</font>' % sc['meta'].upper(), S_MARKS)]],
                     colWidths=[AVAIL * 0.62, AVAIL * 0.38])
        head.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), PAPERBG), ('BOX', (0, 0), (-1, -1), 0.6, LINE),
                                  ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 9),
                                  ('RIGHTPADDING', (0, 0), (-1, -1), 9), ('TOPPADDING', (0, 0), (-1, -1), 6),
                                  ('BOTTOMPADDING', (0, 0), (-1, -1), 6)]))
        story += [head, Spacer(1, 7)]
        for q in sc['questions']:
            row = Table([[Paragraph(q['n'], S_ANSN), Paragraph('<br/>'.join(q['lines']), S_ANS),
                          Paragraph('[%d]' % q['marks'], S_MARKS)]], colWidths=[32, AVAIL - 32 - 26, 26])
            row.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                                     ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0),
                                     ('BOTTOMPADDING', (0, 0), (-1, -1), 1)]))
            block = [row]
            if q.get('note'):
                block.append(Table([[Paragraph(q['note'], S_NOTE)]], colWidths=[AVAIL - 32],
                                   style=TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 32), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                                                     ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)])))
            block.append(Spacer(1, 8))
            story.append(KeepTogether(block))
    _doc(path, header['title'], story, header['footer'])
    return path

# =====================================================================================================
# 4. The papers
# =====================================================================================================
INSTR_MED = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are given even when the final answer is wrong.',
    'No calculator. You need a sharp pencil and a <b>ruler</b>: a line drawn freehand does not score.',
    'Gradient = <b>change in y &divide; change in x</b>. A straight line is <b>y = mx + c</b>, where m is the gradient and c is where it crosses the y-axis.',
    'Read the numbers on the axes. One square is not always one unit.',
    'When a question is about a real situation, give gradients as a rate with units, such as &ldquo;₹ per km&rdquo;.',
    'The mark for each question is shown in square brackets on the right.',
]
INSTR_HARD = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are given even when the final answer is wrong.',
    'No calculator. You need a sharp pencil and a <b>ruler</b>.',
    'No formulas are printed on this paper. You are expected to know them.',
    'Several questions describe situations you may not have seen before — apply the ideas you already have.',
    'Where a question asks you to explain, a correct number on its own is not an explanation: say what it shows.',
    'The mark for each question is shown in square brackets on the right.',
    'If a question stops you, leave it and come back — do not spend more than five minutes stuck.',
]
END = 'End of paper. Check that every gradient in context has units, every point has two coordinates, and every line was drawn with a ruler.'
def P(label, text, marks, space=None, **kw):
    d = {'label': label, 'text': text, 'marks': marks}
    if space: d['space'] = space
    d.update(kw); return d

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A', 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED, 'footer': 'Paper A · Medium · ' + TOPIC, 'endnote': END,
 'questions': [
  {'section': 'Section 1 — functions and tables',
   'text': 'Here is a function machine: &nbsp; <b>input &rarr; [ &times; 4 ] &rarr; [ &minus; 3 ] &rarr; output</b>', 'marks': 4,
   'parts': [P('(a)', 'Find the output when the input is 5.', 1, 14),
             P('(b)', 'Find the output when the input is &minus;2.', 1, 14),
             P('(c)', 'Find the input when the output is 25.', 1, 18),
             P('(d)', 'Draw or describe the <b>inverse</b> machine.', 1, 16)]},
  {'text': 'This question is about the function y = 3x &minus; 2.', 'marks': 4,
   'parts': [P('(a)', 'Complete the table of values.', 2,
               grid=[['x', '&minus;2', '&minus;1', '0', '1', '2', '3'], ['y', '', '&minus;5', '', '1', '', '']]),
             P('(b)', 'On the grid, draw the graph of y = 3x &minus; 2 for values of x from &minus;2 to 3.', 2, fig=G['A2'])]},
  {'section': 'Section 2 — gradient and y = mx + c',
   'text': 'A straight line is drawn on the grid.', 'marks': 3, 'fig': G['A3'],
   'parts': [P('(a)', 'Work out the gradient of the line.', 1, 16),
             P('(b)', 'Write down the coordinates of the point where it crosses the y-axis.', 1, 12),
             P('(c)', 'Write down the equation of the line.', 1, 12)]},
  {'text': 'Work out the gradient of the straight line through each pair of points.', 'marks': 3,
   'parts': [P('(a)', '(2, 3) and (6, 11)', 1, 18), P('(b)', '(&minus;1, 4) and (3, &minus;8)', 2, 22)]},
  {'text': 'Write down the gradient and the y-intercept of each line.', 'marks': 4,
   'parts': [P('(a)', 'y = 5x + 2', 1, 12), P('(b)', 'y = 7 &minus; 4x', 1, 12), P('(c)', '2y = 8x + 6', 2, 20)]},
  {'text': 'This question is about the line y = 4x &minus; 2.', 'marks': 2,
   'parts': [P('(a)', 'Does the point (3, 10) lie on the line? Show how you decide.', 1, 16),
             P('(b)', 'Write down the equation of the line parallel to y = 4x &minus; 2 that crosses the y-axis at (0, 5).', 1, 12)]},
  {'section': 'Section 3 — graphs that mean something',
   'text': 'The graph shows the fare, in rupees, for a taxi journey of up to 8 km.', 'marks': 6, 'fig': G['A7'],
   'parts': [P('(a)', 'Use the graph to find the fare for a 6 km journey.', 1, 12),
             P('(b)', 'Work out the gradient of the line. What does it represent?', 2, 22),
             P('(c)', 'What does the point where the line meets the fare axis represent?', 1, 14),
             P('(d)', 'Write a formula for the fare F rupees for a journey of d km.', 1, 12),
             P('(e)', 'The same rule is used for longer journeys. Work out the fare for 20 km.', 1, 16)]},
  {'text': 'A straight line passes through (1, 5) and (4, 14).', 'marks': 4,
   'parts': [P('(a)', 'Work out its gradient.', 1, 16), P('(b)', 'Find the equation of the line.', 2, 22),
             P('(c)', 'Does the point (&minus;2, &minus;4) lie on the line? Show how you decide.', 1, 16)]},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B', 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED, 'footer': 'Paper B · Medium · ' + TOPIC, 'endnote': END,
 'questions': [
  {'section': 'Section 1 — functions and tables',
   'text': 'The function y = 2x + 5 is written as a set of mappings. Complete each one. Each box is worth one mark.', 'marks': 4,
   'grid': [['Mapping', 'Your answer'], ['3 &rarr; ?', ''], ['&minus;4 &rarr; ?', ''], ['? &rarr; 19', ''], ['? &rarr; 0', '']],
   'grid_widths': [AVAIL * 0.35, AVAIL * 0.65],
   'tip': 'For the last two you are running the function backwards. Undo the last operation first.'},
  {'text': 'This question is about the line x + 2y = 10.', 'marks': 4,
   'parts': [P('(a)', 'Complete the table of values.', 2, grid=[['x', '&minus;2', '0', '2', '4', '6'], ['y', '', '5', '', '', '']]),
             P('(b)', 'On the grid, draw the line x + 2y = 10 for values of x from &minus;2 to 6.', 2, fig=G['B2'])]},
  {'section': 'Section 2 — gradient and y = mx + c',
   'text': 'The line L is drawn on the grid.', 'marks': 3, 'fig': G['B3'],
   'parts': [P('(a)', 'Work out the gradient of L.', 1, 16), P('(b)', 'Find the equation of L.', 2, 16)]},
  {'text': 'Here are five lines. &nbsp; <b>A</b>: y = 3x + 2 &nbsp; <b>B</b>: y = 5x &minus; 3 &nbsp; <b>C</b>: y = 3 &minus; x &nbsp; '
           '<b>D</b>: 2y = 6x + 1 &nbsp; <b>E</b>: y = &minus;3x + 4', 'marks': 4,
   'parts': [P('(a)', 'Which <b>two</b> lines are parallel to y = 3x &minus; 5? Give a reason.', 2, 20),
             P('(b)', 'Find the equation of the line parallel to y = 3x &minus; 5 that passes through (2, 9).', 2, 22)]},
  {'text': 'Work out the gradient of the straight line through each pair of points.', 'marks': 2,
   'parts': [P('(a)', '(0, &minus;3) and (4, 5)', 1, 18), P('(b)', '(&minus;2, 6) and (2, &minus;2)', 1, 18)]},
  {'text': 'Write down the gradient and the y-intercept of each line.', 'marks': 4,
   'parts': [P('(a)', 'y = 6 &minus; 3x', 1, 12), P('(b)', 'y = &frac12;x &minus; 2', 1, 12), P('(c)', '3y = 12x &minus; 9', 2, 20)]},
  {'section': 'Section 3 — graphs that mean something',
   'text': 'The graph converts between miles and kilometres.', 'marks': 6, 'fig': G['B7'],
   'parts': [P('(a)', 'Use the graph to convert 30 miles to kilometres.', 1, 12),
             P('(b)', 'Use the graph to convert 64 km to miles.', 1, 12),
             P('(c)', 'Work out the gradient of the line and say what it represents.', 2, 22),
             P('(d)', 'Explain why the line passes through (0, 0).', 1, 14),
             P('(e)', 'Convert 200 miles to kilometres. The graph does not go that far.', 1, 16)]},
  {'text': 'A plumber charges a call-out fee of ₹300, plus ₹250 for each hour of work.', 'marks': 3,
   'parts': [P('(a)', 'Write a formula for the total charge C rupees for h hours of work.', 1, 12),
             P('(b)', 'A bill comes to ₹1300. How many hours did the plumber work?', 1, 18),
             P('(c)', 'On a graph of C against h, what would the gradient and the C-intercept be?', 1, 14)]},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C', 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD, 'footer': 'Paper C · Hard · ' + TOPIC, 'endnote': END,
 'questions': [
  {'section': 'Section 1 — functions and the algebra of lines',
   'text': 'A three-stage function machine: &nbsp; <b>x &rarr; [ + 3 ] &rarr; [ &divide; 2 ] &rarr; [ &minus; 1 ] &rarr; y</b>', 'marks': 4,
   'parts': [P('(a)', 'Find y when x = &minus;7.', 1, 14), P('(b)', 'Find x when y = 4.', 1, 18),
             P('(c)', 'Write the inverse function as a formula for x in terms of y. Simplify it.', 2, 24)]},
  {'text': 'Find the gradient and the y-intercept of each line.', 'marks': 4,
   'parts': [P('(a)', '4x + 2y = 10', 1, 18), P('(b)', '3y &minus; 6x = 12', 1, 18), P('(c)', 'x = 2y &minus; 8', 2, 22)]},
  {'text': 'A straight line passes through (&minus;3, 8) and (5, &minus;8).', 'marks': 4,
   'parts': [P('(a)', 'Work out its gradient.', 1, 16), P('(b)', 'Find its equation in the form y = mx + c.', 2, 22),
             P('(c)', 'Find the coordinates of the point where it crosses the x-axis.', 1, 16)]},
  {'section': 'Section 2 — reading graphs carefully',
   'text': 'P and Q lie on the line drawn below. Look carefully at the scales on both axes.', 'marks': 3, 'fig': G['C4'],
   'parts': [P('(a)', 'Work out the gradient of the line.', 2, 22), P('(b)', 'Write down the equation of the line.', 1, 12)]},
  {'text': 'The points A(&minus;1, 1), B(2, 7) and C(5, 13) are given.', 'marks': 4,
   'parts': [P('(a)', 'Show that A, B and C lie on one straight line.', 2, 26),
             P('(b)', 'The point D(k, 21) lies on the same line. Find k.', 2, 22)]},
  {'section': 'Section 3 — graphs that mean something',
   'text': 'The graph shows the volume of water in a tank over 30 minutes.', 'marks': 6, 'fig': G['C6'],
   'parts': [P('(a)', 'Find the rate at which the tank fills in the first 8 minutes.', 1, 14),
             P('(b)', 'Describe what happens between 8 and 12 minutes.', 1, 14),
             P('(c)', 'Find the rate at which the tank drains.', 1, 14),
             P('(d)', 'The tank holds 120 litres at two different times. Find both.', 2, 22),
             P('(e)', 'If the drain had been opened at 8 minutes instead, at the same rate, when would the tank have been empty?', 1, 16)]},
  {'text': 'Two electricity tariffs. &nbsp; <b>Tariff X</b>: ₹150 a month plus ₹6 per unit. &nbsp; <b>Tariff Y</b>: ₹30 a month plus ₹8 per unit.', 'marks': 5,
   'parts': [P('(a)', 'Write an equation for the monthly cost C of each tariff for u units.', 1, 14),
             P('(b)', 'Find the number of units for which the two tariffs cost the same, and that cost.', 2, 24),
             P('(c)', 'A family uses 100 units a month. Which tariff is cheaper, and by how much?', 1, 16),
             P('(d)', 'Explain, using the gradients of the two graphs, why one tariff is always cheaper for large amounts of use.', 1, 18)]},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D', 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD, 'footer': 'Paper D · Hard · ' + TOPIC, 'endnote': END,
 'questions': [
  {'section': 'Section 1 — functions and the algebra of lines',
   'text': 'A function machine does <b>&times; a</b> then <b>+ b</b>. It maps 3 &rarr; 10 and 7 &rarr; 22.', 'marks': 4,
   'parts': [P('(a)', 'Find a.', 1, 16), P('(b)', 'Find b.', 1, 12),
             P('(c)', 'Write the function as an equation, y = &hellip;', 1, 10), P('(d)', 'Which input gives an output of 49?', 1, 14)]},
  {'text': 'The line M has equation 2x + 4y = 16.', 'marks': 4,
   'parts': [P('(a)', 'Write the equation of M in the form y = mx + c.', 1, 16), P('(b)', 'Find where M crosses the x-axis.', 1, 12),
             P('(c)', 'Find the equation of the line parallel to M that passes through (&minus;2, 7).', 2, 20)]},
  {'section': 'Section 2 — two lines at once',
   'text': 'The lines y = 3x &minus; 5 and y = &minus;x + 7 meet at the point P.', 'marks': 4,
   'parts': [P('(a)', 'Find the coordinates of P by calculation.', 2, 24), P('(b)', 'Show that your answer fits both equations.', 1, 12),
             P('(c)', 'The line y = mx + 1 also passes through P. Find m.', 1, 14)]},
  {'text': 'The lines y = 2x + 4 and y = &minus;x + 7 and the x-axis enclose a triangle. Work out its area. '
           'Show the coordinates of all three corners.', 'marks': 4, 'space': 46,
   'tip': 'A sketch is not required, but it is the quickest way to see which three points are the corners.'},
  {'text': 'This question is answered on the grid.', 'marks': 4,
   'parts': [P('(a)', 'On the grid, draw y = 2x &minus; 1 for x from &minus;1 to 4.', 1, fig=G['D5']),
             P('(b)', 'On the same grid, draw x + y = 5.', 1),
             P('(c)', 'Write down the coordinates of the point where the lines cross.', 1, 10),
             P('(d)', 'Hence write down the solution of the equation 2x &minus; 1 = 5 &minus; x.', 1, 10)]},
  {'section': 'Section 3 — graphs that mean something',
   'text': 'A car starts with 50 litres of fuel. The graph shows the fuel left as it is driven. It uses fuel at a steady rate.', 'marks': 5, 'fig': G['D6'],
   'parts': [P('(a)', 'Work out the gradient of the line, with its units.', 1, 18), P('(b)', 'How many litres does the car use per 100 km?', 1, 12),
             P('(c)', 'Write an equation for the fuel F litres left after d km.', 1, 12), P('(d)', 'How far can the car go on a full 50 litres?', 1, 14),
             P('(e)', 'The driver says: &ldquo;I can do a 700 km trip without stopping for fuel.&rdquo; Is she right? Explain.', 1, 14)]},
  {'text': 'Two students have made mistakes. For each one, say what is wrong and give the correct answer.', 'marks': 5,
   'parts': [P('(a)', '<b>Kabir</b> writes: <i>&ldquo;The line 3y = 6x + 12 has gradient 6 and crosses the y-axis at (0, 12).&rdquo;</i>', 2, 22),
             P('(b)', '<b>Anaya</b> writes: <i>&ldquo;The gradient of the line through (&minus;3, 5) and (1, &minus;3) is (&minus;3 &minus; 5) &divide; (1 &minus; 3) = &minus;8 &divide; &minus;2 = 4.&rdquo;</i>', 2, 22),
             P('(c)', 'Without calculating anything, how could Anaya have known her answer was wrong?', 1, 16)]},
 ]}
SPECS = [('a', A), ('b', B), ('c', C), ('d', D)]

# =====================================================================================================
# 5. Mark schemes. Every number is formatted from N.
# =====================================================================================================
def T(n): return '<b>[%d]</b>' % n
def b(x): return '<b>%s</b>' % x
def pt(x, y): return '(%s, %s)' % (f(x), f(y))

n = N
SA = [
 {'n': '1', 'marks': 4, 'lines': ['(a) 5 &times; 4 &minus; 3 = ' + b(f(n['A1'][0])) + ' ' + T(1),
                                  '(b) &minus;2 &times; 4 &minus; 3 = ' + b(f(n['A1'][1])) + ' ' + T(1),
                                  '(c) (25 + 3) &divide; 4 = ' + b(f(n['A1'][2])) + ' ' + T(1),
                                  '(d) ' + b('+ 3, then &divide; 4') + ' (both operations, in that order) ' + T(1)],
  'note': 'In (c) and (d) the error to look for is &divide; 4 then + 3, which gives 9.25 from 25. Order wrong = 0 for (d), even with the right two operations.'},
 {'n': '2', 'marks': 4, 'lines': ['(a) ' + b(', '.join(f(n['A2'][i]) for i in (0, 2, 4, 5))) + ' for x = &minus;2, 0, 2, 3. All four ' + T(2) + '; two or three correct [1]',
                                  '(b) Points plotted correctly ' + T(1) + '; single ruled line from x = &minus;2 to x = 3 ' + T(1)],
  'note': 'x = &minus;2 giving &minus;4 or &minus;1 is the usual slip. The y row must go up in equal steps of 3 — if it does not, the line cannot be straight and the plot mark is lost too.'},
 {'n': '3', 'marks': 3, 'lines': ['(a) e.g. from (0, &minus;1) to (3, 5): 6 &divide; 3 = ' + b(f(n['A3'][0])) + ' ' + T(1),
                                  '(b) ' + b(pt(0, n['A3'][1])) + ' ' + T(1), '(c) ' + b(eq(*n['A3'])) + ' ' + T(1)],
  'note': 'Follow-through in (c) from their (a) and (b). Watch for the intercept written as (&minus;1, 0) — x and y swapped.'},
 {'n': '4', 'marks': 3, 'lines': ['(a) 8 &divide; 4 = ' + b(f(n['A4'][0])) + ' ' + T(1),
                                  '(b) (&minus;8 &minus; 4) &divide; (3 &minus; (&minus;1)) ' + T(1) + ' = &minus;12 &divide; 4 = ' + b(f(n['A4'][1])) + ' ' + T(1)],
  'note': '+3 in (b) means the sign was lost; &minus;6 means 3 + (&minus;1) on the bottom. The line falls, so a positive answer should have been self-checked away.'},
 {'n': '5', 'marks': 4, 'lines': ['(a) gradient ' + b('5') + ', intercept ' + b('2') + ' ' + T(1),
                                  '(b) gradient ' + b('&minus;4') + ', intercept ' + b('7') + ' ' + T(1),
                                  '(c) y = 4x + 3 ' + T(1) + ': gradient ' + b(f(n['A5c'][0])) + ', intercept ' + b(f(n['A5c'][1])) + ' ' + T(1)],
  'note': '(b) answered as gradient 7 is the &ldquo;first number&rdquo; reflex. (c) answered as 8 and 6 means the equation was read before it was rearranged — the single most common error on this topic.'},
 {'n': '6', 'marks': 2, 'lines': ['(a) 4(3) &minus; 2 = 10, so ' + b('yes') + ' ' + T(1), '(b) ' + b('y = 4x + 5') + ' ' + T(1)],
  'note': '&ldquo;Yes&rdquo; without the substitution scores 0. In (b), y = 5x &minus; 2 swaps the roles of m and c.'},
 {'n': '7', 'marks': 6, 'lines': ['(a) ' + b('₹' + f(n['A7']['at6'])) + ' (accept 128&ndash;132) ' + T(1),
                                  '(b) (160 &minus; 40) &divide; 8 = ' + f(n['A7']['m']) + ' ' + T(1) + '; ' + b('the fare rises ₹' + f(n['A7']['m']) + ' per km') + ' ' + T(1),
                                  '(c) ' + b('a fixed charge of ₹40') + ' before any distance ' + T(1),
                                  '(d) ' + b(eq(n['A7']['m'], 40, 'd', 'F')) + ' ' + T(1),
                                  '(e) 15 &times; 20 + 40 = ' + b('₹' + f(n['A7']['at20'])) + ' ' + T(1)],
  'note': '(b): 160 &divide; 8 = 20 ignores the starting value. (e): scaling up the 8 km fare (₹160 &times; 2.5 = ₹400) multiplies the fixed charge too — this is the question built to show why the formula beats the graph.'},
 {'n': '8', 'marks': 4, 'lines': ['(a) 9 &divide; 3 = ' + b(f(n['A8'][0])) + ' ' + T(1),
                                  '(b) 5 = 3(1) + c ' + T(1) + ', ' + b(eq(*n['A8'])) + ' ' + T(1),
                                  '(c) 3(&minus;2) + 2 = &minus;4, so ' + b('yes') + ' ' + T(1)],
  'note': 'In (b), c = 5 (forgetting to subtract 3) is the slip. A student who checks with (4, 14) catches it alone.'},
]

SB = [
 {'n': '1', 'marks': 4, 'lines': ['3 &rarr; ' + b(f(n['B1'][0])) + ' ' + T(1) + ' &nbsp; &minus;4 &rarr; ' + b(f(n['B1'][1])) + ' ' + T(1),
                                  b(f(n['B1'][2])) + ' &rarr; 19 ' + T(1) + ' &nbsp; ' + b(f(n['B1'][3])) + ' &rarr; 0 ' + T(1)],
  'note': '&minus;4 &rarr; &minus;13 means 2(&minus;4) &minus; 5. The last box needs a negative non-integer; a student who writes &ldquo;none&rdquo; has assumed outputs are whole numbers.'},
 {'n': '2', 'marks': 4, 'lines': ['(a) ' + b(', '.join(f(n['B2'][i]) for i in (0, 2, 3, 4))) + ' for x = &minus;2, 2, 4, 6. All four ' + T(2) + '; two or three [1]',
                                  '(b) Points plotted ' + T(1) + '; ruled line from x = &minus;2 to 6 ' + T(1)],
  'note': 'At x = &minus;2: &minus;2 + 2y = 10 gives 2y = 12, y = 6. Students who get 4 have done 10 &minus; 2 instead of 10 + 2.'},
 {'n': '3', 'marks': 3, 'lines': ['(a) down 4 for across 2: ' + b(f(n['B3'][0])) + ' ' + T(1),
                                  '(b) c = ' + f(n['B3'][1]) + ' ' + T(1) + '; ' + b(eq(*n['B3'])) + ' ' + T(1)],
  'note': 'Gradient +2 is the classic sign loss on a falling line. y = 4x &minus; 2 swaps m and c.'},
 {'n': '4', 'marks': 4, 'lines': ['(a) ' + b('A and D') + ' ' + T(1) + '; both have gradient 3 (D is y = 3x + &frac12;) ' + T(1),
                                  '(b) 9 = 3(2) + c, c = ' + f(n['B4b']) + ' ' + T(1) + '; ' + b(eq(3, n['B4b'])) + ' ' + T(1)],
  'note': 'Missing D is the target error: 2y = 6x + 1 looks like gradient 6 until it is divided by 2. E (gradient &minus;3) catches students who think parallel means &ldquo;same number, any sign&rdquo;.'},
 {'n': '5', 'marks': 2, 'lines': ['(a) 8 &divide; 4 = ' + b(f(n['B5'][0])) + ' ' + T(1), '(b) &minus;8 &divide; 4 = ' + b(f(n['B5'][1])) + ' ' + T(1)],
  'note': 'In (b) a denominator of 0 (2 + (&minus;2)) is the subtraction error; it should alarm the student, because division by zero means a vertical line, and this one plainly is not.'},
 {'n': '6', 'marks': 4, 'lines': ['(a) ' + b('&minus;3, 6') + ' ' + T(1), '(b) ' + b('&frac12;, &minus;2') + ' ' + T(1),
                                  '(c) y = 4x &minus; 3 ' + T(1) + '; ' + b(f(n['B6c'][0]) + ', ' + f(n['B6c'][1])) + ' ' + T(1)],
  'note': '(a) answered 6, &minus;3: reading order instead of the coefficient of x.'},
 {'n': '7', 'marks': 6, 'lines': ['(a) ' + b(f(n['B7']['km30']) + ' km') + ' ' + T(1), '(b) ' + b(f(n['B7']['mi64']) + ' miles') + ' ' + T(1),
                                  '(c) 80 &divide; 50 = ' + f(n['B7']['m']) + ' ' + T(1) + '; ' + b(f(n['B7']['m']) + ' km per mile') + ' ' + T(1),
                                  '(d) ' + b('0 miles is 0 km') + ' (no fixed amount) ' + T(1),
                                  '(e) 200 &times; 1.6 = ' + b(f(n['B7']['km200']) + ' km') + ' ' + T(1)],
  'note': 'Gradient 0.625 is km &divide; miles upside down; accept it only if described as &ldquo;miles per km&rdquo;. In (e), any correct scaling (e.g. 5 &times; 64 km for 5 &times; 40 miles) earns the mark.'},
 {'n': '8', 'marks': 3, 'lines': ['(a) ' + b('C = 250h + 300') + ' ' + T(1), '(b) (1300 &minus; 300) &divide; 250 = ' + b(f(n['B8']['h']) + ' hours') + ' ' + T(1),
                                  '(c) gradient ' + b('250') + ', intercept ' + b('300') + ' ' + T(1)],
  'note': '1300 &divide; 250 = 5.2 forgets the call-out fee. C = 300h + 250 swaps the rate and the fixed charge — the same swap as m and c.'},
]

SC = [
 {'n': '1', 'marks': 4, 'lines': ['(a) (&minus;7 + 3) &divide; 2 &minus; 1 = ' + b(f(n['C1'][0])) + ' ' + T(1),
                                  '(b) (4 + 1) &times; 2 &minus; 3 = ' + b(f(n['C1'][1])) + ' ' + T(1),
                                  '(c) x = 2(y + 1) &minus; 3 ' + T(1) + ' = ' + b('2y &minus; 1') + ' ' + T(1)],
  'note': 'x = (y + 1) &times; 2 &minus; 3 left unsimplified gets the first mark only. x = (y &minus; 1) &times; 2 + 3 reverses the operations but not the order.'},
 {'n': '2', 'marks': 4, 'lines': ['(a) y = &minus;2x + 5: ' + b(f(n['C2'][0][0]) + ', ' + f(n['C2'][0][1])) + ' ' + T(1),
                                  '(b) y = 2x + 4: ' + b(f(n['C2'][1][0]) + ', ' + f(n['C2'][1][1])) + ' ' + T(1),
                                  '(c) 2y = x + 8 ' + T(1) + '; y = &frac12;x + 4: ' + b('&frac12;, 4') + ' ' + T(1)],
  'note': '(c) is the hardest form on the paper because y is on the &ldquo;wrong&rdquo; side. Gradient 2 means the student treated x = 2y &minus; 8 as if it were y = 2x &minus; 8.'},
 {'n': '3', 'marks': 4, 'lines': ['(a) &minus;16 &divide; 8 = ' + b(f(n['C3'][0])) + ' ' + T(1),
                                  '(b) 8 = &minus;2(&minus;3) + c ' + T(1) + ', c = 2: ' + b(eq(*n['C3'])) + ' ' + T(1),
                                  '(c) ' + b(pt(n['C3x'], 0)) + ' ' + T(1)],
  'note': 'c = 14 comes from 8 = &minus;6 + c, i.e. &minus;2 &times; &minus;3 taken as &minus;6. Check with (5, &minus;8): &minus;10 + 2 = &minus;8.'},
 {'n': '4', 'marks': 3, 'lines': ['(a) P(0, 10), Q(20, 70): rise 60, run 20 ' + T(1) + '; gradient ' + b(f(n['C4'][0])) + ' ' + T(1),
                                  '(b) ' + b(eq(*n['C4'])) + ' ' + T(1)],
  'note': 'The question exists for the answer ' + f(n['C4wrong']) + ' (counting 6 squares up and 4 across). Award 0 for 1.5 with no working; the axes go up in 10s and 5s.'},
 {'n': '5', 'marks': 4, 'lines': ['(a) gradient AB = 6 &divide; 3 = 2, gradient BC = 6 &divide; 3 = 2 ' + T(1) + '; equal gradients ' + b('and a shared point B') + ' ' + T(1),
                                  '(b) line is y = 2x + 3 ' + T(1) + '; 21 = 2k + 3, ' + b('k = ' + f(n['C5k'])) + ' ' + T(1)],
  'note': 'Equal gradients alone show AB is parallel to BC; the second mark needs the shared point. In (b), stepping along (+3 across, +6 up) from C to D is an equally good method.'},
 {'n': '6', 'marks': 6, 'lines': ['(a) 240 &divide; 8 = ' + b(f(n['C6']['fill']) + ' litres per minute') + ' ' + T(1),
                                  '(b) ' + b('volume constant at 240 litres') + ': nothing in or out ' + T(1),
                                  '(c) 240 &divide; 16 = ' + b(f(n['C6']['drain']) + ' litres per minute') + ' ' + T(1),
                                  '(d) filling: ' + b(f(n['C6']['up120']) + ' minutes') + ' ' + T(1) + '; draining: 12 + 8 = ' + b(f(n['C6']['down120']) + ' minutes') + ' ' + T(1),
                                  '(e) 8 + 16 = ' + b(f(n['C6']['early']) + ' minutes') + ' ' + T(1)],
  'note': '(c) 240 &divide; 28 uses the whole clock instead of the draining interval. (d) &ldquo;8 minutes&rdquo; for the second time forgets the clock had reached 12. (e) checks they understand the drain time does not depend on when it starts.'},
 {'n': '7', 'marks': 5, 'lines': ['(a) ' + b('X: C = 6u + 150; Y: C = 8u + 30') + ' ' + T(1),
                                  '(b) 6u + 150 = 8u + 30 ' + T(1) + '; ' + b('u = ' + f(n['C7']['u']) + ', cost ₹' + f(n['C7']['cost'])) + ' ' + T(1),
                                  '(c) X ₹' + f(n['C7']['X100']) + ', Y ₹' + f(n['C7']['Y100']) + ': ' + b('X, by ₹' + f(n['C7']['Y100'] - n['C7']['X100'])) + ' ' + T(1),
                                  '(d) ' + b('X has the smaller gradient') + ' (₹6 per unit against ₹8), so above 60 units its line stays below Y&rsquo;s ' + T(1)],
  'note': '(d) needs the word gradient (or rate per unit) and the comparison. &ldquo;X is cheaper&rdquo; repeats (c) and scores 0.'},
]

SD = [
 {'n': '1', 'marks': 4, 'lines': ['(a) outputs rise 12 for inputs rising 4: ' + b('a = ' + f(n['D1'][0])) + ' ' + T(1),
                                  '(b) 10 = 3(3) + b: ' + b('b = ' + f(n['D1'][1])) + ' ' + T(1),
                                  '(c) ' + b(eq(n['D1'][0], n['D1'][1])) + ' ' + T(1),
                                  '(d) (49 &minus; 1) &divide; 3 = ' + b(f(n['D1'][2])) + ' ' + T(1)],
  'note': 'a = 22 &divide; 7 or 10 &divide; 3 means the student divided an output by an input. The method is gradient-then-intercept; that is the point of the question.'},
 {'n': '2', 'marks': 4, 'lines': ['(a) 4y = &minus;2x + 16, ' + b(eq(*n['D2'])) + ' ' + T(1),
                                  '(b) ' + b(pt(n['D2x'], 0)) + ' ' + T(1),
                                  '(c) 7 = &minus;&frac12;(&minus;2) + c ' + T(1) + ', c = 6: ' + b(eq(n['D2'][0], n['D2c'])) + ' ' + T(1)],
  'note': 'Gradient &minus;2 in (a) is dividing the wrong way (4 &divide; 2). In (c), c = 8 comes from &minus;&frac12; &times; &minus;2 = &minus;1.'},
 {'n': '3', 'marks': 4, 'lines': ['(a) 3x &minus; 5 = &minus;x + 7, 4x = 12 ' + T(1) + '; ' + b('P' + pt(*n['D3'])) + ' ' + T(1),
                                  '(b) 3(3) &minus; 5 = 4 and &minus;3 + 7 = 4 ' + T(1),
                                  '(c) 4 = 3m + 1, ' + b('m = ' + f(n['D3m'])) + ' ' + T(1)],
  'note': 'x = 3 with no y is half of (a). 2x = 12 (forgetting &minus;x becomes +x when moved) gives x = 6 — then (b) fails, which is the point of (b).'},
 {'n': '4', 'marks': 4, 'lines': ['Top corner: 2x + 4 = &minus;x + 7, ' + b(pt(*n['D4'])) + ' ' + T(1),
                                  'x-intercepts ' + b(pt(n['D4x'][0], 0)) + ' and ' + b(pt(n['D4x'][1], 0)) + ' ' + T(1),
                                  'base = 7 &minus; (&minus;2) = 9 ' + T(1) + '; area = &frac12; &times; 9 &times; 6 = ' + b(f(n['D4area']) + ' square units') + ' ' + T(1)],
  'note': 'Base 5 (7 &minus; 2) is the error this was built for. Height 1 (using the x-coordinate of the top corner) is the second-commonest.'},
 {'n': '5', 'marks': 4, 'lines': ['(a) ruled line through e.g. (&minus;1, &minus;3), (0, &minus;1), (4, 7) ' + T(1),
                                  '(b) ruled line through e.g. (0, 5), (4, 1) ' + T(1),
                                  '(c) ' + b(pt(*n['D5'])) + ' ' + T(1), '(d) ' + b('x = ' + f(n['D5'][0])) + ' ' + T(1)],
  'note': '(d) is the link the whole topic is building to: the x-coordinate where two graphs cross solves the equation formed by setting them equal. Accept (d) only as x = 2, not (2, 3).'},
 {'n': '6', 'marks': 5, 'lines': ['(a) (20 &minus; 50) &divide; 375 = ' + b(f(n['D6']['m']) + ' litres per km') + ' ' + T(1),
                                  '(b) ' + b(f(n['D6']['per100']) + ' litres') + ' ' + T(1),
                                  '(c) ' + b('F = 50 &minus; 0.08d') + ' ' + T(1),
                                  '(d) 50 &divide; 0.08 = ' + b(f(n['D6']['empty']) + ' km') + ' ' + T(1),
                                  '(e) ' + b('No') + ': a full tank lasts only ' + f(n['D6']['empty']) + ' km, less than 700 ' + T(1)],
  'note': 'Gradient +0.08 with &ldquo;fuel used per km&rdquo; is acceptable in (a) if the student says so; a bare +0.08 is not. (e) needs the comparison with 625.'},
 {'n': '7', 'marks': 5, 'lines': ['(a) Kabir did not divide by 3 first ' + T(1) + '; y = 2x + 4, so ' + b('gradient ' + f(n['D7'][0]) + ', crosses at (0, ' + f(n['D7'][1]) + ')') + ' ' + T(1),
                                  '(b) the bottom should be 1 &minus; (&minus;3) = 4, not 1 &minus; 3 ' + T(1) + '; gradient = &minus;8 &divide; 4 = ' + b(f(n['D7'][2])) + ' ' + T(1),
                                  '(c) y ' + b('falls') + ' from 5 to &minus;3 as x increases, so the gradient must be ' + b('negative') + ' ' + T(1)],
  'note': 'Students who can explain someone else&rsquo;s error rarely repeat it. If (c) is blank, they have not yet got the habit of sense-checking the sign — that is worth a conversation, not just a mark.'},
]
SCHEMES = [('Paper A &mdash; Medium', SA), ('Paper B &mdash; Medium', SB), ('Paper C &mdash; Hard', SC), ('Paper D &mdash; Hard', SD)]

# =====================================================================================================
# 6. Verification — runs on every build
# =====================================================================================================
import re
def _verify():
    F_ = Fr
    # -- 1. answers, re-derived by a second route and compared with hand-expected values
    exp = {
      'A1': (17, -11, 7), 'A2': [-8, -5, -2, 1, 4, 7], 'A3': (2, -1), 'A4': (2, -3), 'A5c': (4, 3), 'A8': (3, 2),
      'B1': (11, -3, 7, F_(-5, 2)), 'B2': [6, 5, 4, 3, 2], 'B3': (-2, 4), 'B4b': 3, 'B5': (2, -2), 'B6c': (4, -3),
      'C1': (-3, 7), 'C3': (-2, 2), 'C3x': 1, 'C4': (3, 10), 'C5': (2, 2), 'C5k': 9,
      'D1': (3, 1, 16), 'D2': (F_(-1, 2), 4), 'D2x': 8, 'D2c': 6, 'D3': (3, 4), 'D3m': 1, 'D4': (1, 6), 'D4x': (-2, 7),
      'D4area': 27, 'D5': (2, 3),
    }
    for k, v in exp.items():
        got = N[k]
        got = list(got) if isinstance(v, list) else got
        assert (tuple(got) if isinstance(got, (tuple, list)) and not isinstance(v, list) else got) == v, (k, got, v)
    assert (N['A7']['m'], N['A7']['at6'], N['A7']['at20']) == (15, 130, 340)
    assert (N['B7']['m'], N['B7']['km30'], N['B7']['mi64'], N['B7']['km200']) == (F_(8, 5), 48, 40, 320)
    assert (N['B8']['h'], N['B8']['c3']) == (4, 1050)
    assert (N['C6']['fill'], N['C6']['drain'], N['C6']['up120'], N['C6']['down120'], N['C6']['early']) == (30, 15, 4, 20, 24)
    assert (N['C7']['u'], N['C7']['cost'], N['C7']['X100'], N['C7']['Y100']) == (60, 510, 750, 830)
    assert (N['D6']['m'], N['D6']['per100'], N['D6']['empty']) == (F_(-2, 25), 8, 625) and N['D6']['empty'] < 700
    assert N['D7'] == (2, 4, -2, 4)                       # Kabir right values, Anaya right (-2) and her wrong (4)
    assert N['C4wrong'] != N['C4'][0]                       # the square-counting answer really is different
    assert F_(25 - 3, 4) != N['A1'][2] and F_(25, 4) + 3 != N['A1'][2]   # wrong-order inverse differs
    # substitutions in the mark scheme text
    assert 160 * F_(5, 2) == 400 != N['A7']['at20']
    assert 4 * 3 - 2 == 10 and 3 * -2 + 2 == -4 and 2 * (-4) + 5 == -3
    assert 3 * 3 - 5 == 4 == -3 + 7
    # -- 2. drawn lines pass through what the questions and schemes say
    assert on_line(2, -1, G['A3'].lines[0]) and on_line(2, -1, [(0, -1), (3, 5)])
    assert on_line(15, 40, G['A7'].lines[0])
    assert on_line(-2, 4, G['B3'].lines[0]) and on_line(-2, 4, [(0, 4), (2, 0)])
    assert on_line(F_(8, 5), 0, G['B7'].lines[0])
    assert on_line(3, 10, G['C4'].lines[0]) and on_line(3, 10, [(0, 10), (20, 70)])
    assert on_line(F_(-2, 25), 50, G['D6'].lines[0]) and on_line(F_(-2, 25), 50, [(375, 20)])
    tank = G['C6'].lines[0]
    assert tank[1] == (8, 240) and tank[2] == (12, 240) and tank[3] == (28, 0)
    # -- 3. readings land on grid lines, and blank grids hold the lines asked for
    def on_grid(g, x=None, y=None):
        ok = True
        if x is not None: ok &= F_(x - g.x0) / g.xs == int(F_(x - g.x0) / g.xs)
        if y is not None: ok &= F_(y - g.y0) / g.ys == int(F_(y - g.y0) / g.ys)
        return ok
    assert on_grid(G['A7'], 6, 130) and on_grid(G['B7'], 30, 48) and on_grid(G['B7'], 50 * 64 // 80, 64)
    assert on_grid(G['C6'], 4, 120) and on_grid(G['C6'], 20, 120) and on_grid(G['D6'], 375, 20)
    assert on_grid(G['C4'], 0, 10) and on_grid(G['C4'], 20, 70)
    def fits(g, fn, xa, xb):
        return all(g.y0 <= fn(x) <= g.y1 for x in (xa, xb)) and g.x0 <= xa and xb <= g.x1
    assert fits(G['A2'], lambda x: 3 * x - 2, -2, 3)
    assert fits(G['B2'], lambda x: F_(10 - x, 2), -2, 6)
    assert fits(G['D5'], lambda x: 2 * x - 1, -1, 4) and fits(G['D5'], lambda x: 5 - x, -1, 4)
    # -- 4. marks
    for code, spec in SPECS:
        qs = spec['questions']
        assert sum(q['marks'] for q in qs) == spec['marks'] == 30, (code, sum(q['marks'] for q in qs))
        assert sum(1 for q in qs if q.get('section')) == 3, code
        for i, q in enumerate(qs, 1):
            if q.get('parts'):
                assert sum(p['marks'] for p in q['parts']) == q['marks'], (code, i)
    for (title, sc), (code, spec) in zip(SCHEMES, SPECS):
        assert len(sc) == len(spec['questions']), code
        for s, q in zip(sc, spec['questions']):
            assert s['marks'] == q['marks'], (code, s['n'])
            tags = sum(int(t) for line in s['lines'] for t in re.findall(r'<b>\[(\d)\]</b>', line))
            assert tags == s['marks'], (code, s['n'], tags)
            assert s.get('note'), (code, s['n'])
    # -- 5. house conventions
    assert 'y = mx + c' in ' '.join(INSTR_MED) and 'y = mx + c' not in ' '.join(INSTR_HARD)
    assert any('may not have seen before' in i for i in INSTR_HARD)
    last = D['questions'][-1]
    assert 'Two students' in last['text'] and 'Kabir' in last['parts'][0]['text'] and 'Anaya' in last['parts'][1]['text']

def main():
    _verify()
    files = []
    for code, spec in SPECS:
        p = os.path.join(OUT, 'maths-graphs-paper-%s.pdf' % code)
        build_paper2(spec, p); files.append(p)
    p = os.path.join(OUT, 'maths-graphs-answers.pdf')
    build_scheme2([{'title': t, 'meta': '30 marks', 'questions': sc} for t, sc in SCHEMES], p, {
        'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes', 'meta': 'Papers A to D · 30 marks each · tutor copy',
        'intro': 'Marks in square brackets show how each total is split. Marks on this topic go to a short list of habits: reading m and c '
                 'before the equation is in y = mx + c form, counting squares instead of reading the scales, losing the sign of a gradient, '
                 'undoing a function machine in the wrong order, giving a bare number where an interpretation with units was asked for, and '
                 'stopping at x when a point was wanted. Each note names the error that question was built to catch. Every number here was '
                 'computed by tools/papers/maths_graphs.py, and every drawn line was checked against the equation in this booklet.',
        'footer': 'Mark schemes · ' + TOPIC})
    files.append(p)
    print('verify ok'); print('\n'.join(files))

if __name__ == '__main__':
    main()
