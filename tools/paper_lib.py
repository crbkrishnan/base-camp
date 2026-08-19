#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates printed test papers and mark schemes in the Base Camp house style."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Flowable, KeepTogether)
from reportlab.pdfgen import canvas as pdfcanvas

FDIR = '/usr/share/fonts/truetype/dejavu/'
for name, fn in [('Body', 'DejaVuSerif.ttf'), ('Body-Bold', 'DejaVuSerif-Bold.ttf'),
                 ('Body-Italic', 'DejaVuSerif-Italic.ttf'),
                 ('UI', 'DejaVuSans.ttf'), ('UI-Bold', 'DejaVuSans-Bold.ttf'),
                 ('Mono', 'DejaVuSansMono.ttf'), ('Mono-Bold', 'DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, FDIR + fn))

INK      = colors.HexColor('#1A1A22')
SOFT     = colors.HexColor('#5A5A66')
LINE     = colors.HexColor('#C9C4BA')
RULE     = colors.HexColor('#D8D4CC')
PAPERBG  = colors.HexColor('#F2F0EB')
OK       = colors.HexColor('#1B7F4B')

MARGIN_L = 18*mm
MARGIN_R = 18*mm
MARGIN_T = 15*mm
MARGIN_B = 17*mm
AVAIL    = A4[0] - MARGIN_L - MARGIN_R

S_EYEBROW = ParagraphStyle('eyebrow', fontName='Mono', fontSize=7.6, leading=10,
                           textColor=SOFT, spaceAfter=3)
S_TITLE   = ParagraphStyle('title', fontName='UI-Bold', fontSize=16.5, leading=19,
                           textColor=INK, spaceAfter=3)
S_META    = ParagraphStyle('meta', fontName='Mono', fontSize=8, leading=11, textColor=SOFT)
S_Q       = ParagraphStyle('q', fontName='Body', fontSize=10.6, leading=15.4, textColor=INK)
S_QB      = ParagraphStyle('qb', parent=S_Q, fontName='Body-Bold')
S_NUM     = ParagraphStyle('num', fontName='UI-Bold', fontSize=10.6, leading=15.4, textColor=INK)
S_MARKS   = ParagraphStyle('marks', fontName='Mono', fontSize=8.6, leading=15.4,
                           textColor=SOFT, alignment=2)
S_NOTE    = ParagraphStyle('note', fontName='Body-Italic', fontSize=9.2, leading=13, textColor=SOFT)
S_INSTR   = ParagraphStyle('instr', fontName='Body', fontSize=9.4, leading=13.6, textColor=INK)
S_SEC     = ParagraphStyle('sec', fontName='Mono', fontSize=8, leading=11, textColor=SOFT,
                           spaceBefore=6, spaceAfter=4)
S_ANS     = ParagraphStyle('ans', fontName='Body', fontSize=9.8, leading=13.6, textColor=INK)
S_ANSN    = ParagraphStyle('ansn', fontName='UI-Bold', fontSize=9.8, leading=13.6, textColor=INK)


class Ruled(Flowable):
    """Ruled working space."""
    def __init__(self, height_mm, width=AVAIL, gap=8.2*mm, indent=0):
        Flowable.__init__(self)
        self.height = height_mm*mm
        self.width = width
        self.gap = gap
        self.indent = indent

    def draw(self):
        c = self.canv
        c.setStrokeColor(RULE)
        c.setLineWidth(0.5)
        y = self.height - self.gap
        while y > 0:
            c.line(self.indent, y, self.width, y)
            y -= self.gap


class Rule(Flowable):
    def __init__(self, width=AVAIL, thickness=1.1, colour=INK, space=3):
        Flowable.__init__(self)
        self.width = width; self.height = space; self.t = thickness; self.c = colour
    def draw(self):
        self.canv.setStrokeColor(self.c)
        self.canv.setLineWidth(self.t)
        self.canv.line(0, self.height-1, self.width, self.height-1)


class NumberedCanvas(pdfcanvas.Canvas):
    """Two-pass canvas so the footer can say 'page 2 of 4'."""
    def __init__(self, *args, **kw):
        self._footer = kw.pop('footer', '')
        pdfcanvas.Canvas.__init__(self, *args, **kw)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for state in self._saved:
            self.__dict__.update(state)
            self._draw_footer(total)
            pdfcanvas.Canvas.showPage(self)
        pdfcanvas.Canvas.save(self)

    def _draw_footer(self, total):
        self.setStrokeColor(LINE); self.setLineWidth(0.5)
        self.line(MARGIN_L, MARGIN_B - 5*mm, A4[0]-MARGIN_R, MARGIN_B - 5*mm)
        self.setFont('Mono', 7.4)
        self.setFillColor(SOFT)
        self.drawString(MARGIN_L, MARGIN_B - 9.5*mm, self._footer)
        self.drawRightString(A4[0]-MARGIN_R, MARGIN_B - 9.5*mm,
                             'page %d of %d' % (self._pageNumber, total))


def _header(spec):
    out = []
    out.append(Paragraph(spec['eyebrow'].upper(), S_EYEBROW))
    out.append(Paragraph(spec['title'], S_TITLE))
    out.append(Paragraph(spec['meta'].upper(), S_META))
    out.append(Spacer(1, 5))
    out.append(Rule())
    out.append(Spacer(1, 7))

    w = (AVAIL - 12) / 3.0
    cells = []
    for lab in ('Name', 'Date', 'Score        / %d' % spec['marks']):
        cells.append(Paragraph('<font name="Mono" size="7.6" color="#5A5A66">%s</font>'
                               % lab.upper(), S_META))
    t = Table([cells], colWidths=[w, w, w], rowHeights=[20*mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LINEBELOW', (0,0), (-1,0), 0.8, LINE),
    ]))
    out.append(t)
    out.append(Spacer(1, 8))

    if spec.get('instructions'):
        body = '<br/>'.join('&bull;&nbsp; ' + i for i in spec['instructions'])
        box = Table([[Paragraph(body, S_INSTR)]], colWidths=[AVAIL])
        box.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), PAPERBG),
            ('BOX', (0,0), (-1,-1), 0.6, LINE),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('RIGHTPADDING', (0,0), (-1,-1), 10),
            ('TOPPADDING', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ]))
        out.append(box)
        out.append(Spacer(1, 10))
    return out


def _qrow(num, text, marks, style=S_Q, indent=0, numw=18):
    mkw = 24
    cells = [Paragraph(num, S_NUM) if num else '',
             Paragraph(text, style),
             Paragraph('[%d]' % marks if marks else '', S_MARKS)]
    t = Table([cells], colWidths=[numw, AVAIL-numw-mkw-indent, mkw])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (0,0), 5),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    if indent:
        outer = Table([[t]], colWidths=[AVAIL])
        outer.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), indent),
                                   ('RIGHTPADDING', (0,0), (-1,-1), 0),
                                   ('TOPPADDING', (0,0), (-1,-1), 0),
                                   ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
        return outer
    return t


def _grid(rows, col_widths=None):
    n = len(rows[0])
    cw = col_widths or [AVAIL/float(n)]*n
    data = [[Paragraph('<font name="UI-Bold" size="9.4">%s</font>' % c, S_Q) if i == 0
             else Paragraph('<font name="Body" size="10.4">%s</font>' % c, S_Q)
             for c in row] for i, row in enumerate(rows)]
    t = Table(data, colWidths=cw, rowHeights=[9*mm]*len(rows))
    t.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.6, LINE),
        ('BACKGROUND', (0,0), (-1,0), PAPERBG),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    return t


def build_paper(spec, path):
    story = _header(spec)
    for i, q in enumerate(spec['questions'], 1):
        head = []
        if q.get('section'):
            head.append(Paragraph(q['section'].upper(), S_SEC))
        top_marks = q.get('marks', 0) if not q.get('parts') else 0
        head.append(_qrow('%d.' % i, q['text'], top_marks))
        if q.get('grid'):
            head.append(Spacer(1, 4))
            head.append(_grid(q['grid'], q.get('grid_widths')))
            head.append(Spacer(1, 2))
        if q.get('space'):
            head.append(Ruled(q['space']))
        if q.get('tip') and not q.get('parts'):
            head.append(Spacer(1, 2))
            head.append(Paragraph(q['tip'], S_NOTE))
        story.append(KeepTogether(head))

        for p in q.get('parts', []):
            sub = [Spacer(1, 3),
                   _qrow(p['label'], p['text'], p.get('marks', 0), indent=16, numw=26)]
            if p.get('space'):
                sub.append(Ruled(p['space'], width=AVAIL, indent=16))
            story.append(KeepTogether(sub))
        if q.get('tip') and q.get('parts'):
            story.append(Spacer(1, 2))
            story.append(Paragraph(q['tip'], S_NOTE))
        story.append(Spacer(1, 11))

    story.append(Spacer(1, 4))
    story.append(Rule(thickness=0.6, colour=LINE))
    story.append(Spacer(1, 4))
    story.append(Paragraph(spec.get('endnote', 'End of paper. Check every answer has a unit '
                                                'or a form the question actually asked for.'), S_NOTE))

    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                          topMargin=MARGIN_T, bottomMargin=MARGIN_B,
                          title=spec['title'], author='Base Camp')
    frame = Frame(MARGIN_L, MARGIN_B, AVAIL, A4[1]-MARGIN_T-MARGIN_B, id='f',
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame])])
    footer = spec['footer']

    class C(NumberedCanvas):
        def __init__(self, *a, **k):
            k['footer'] = footer
            NumberedCanvas.__init__(self, *a, **k)

    doc.build(story, canvasmaker=C)
    return path


def build_scheme(schemes, path, header):
    """schemes: list of dicts {title, meta, questions:[{n, marks, lines:[...], note}]}"""
    story = [Paragraph(header['eyebrow'].upper(), S_EYEBROW),
             Paragraph(header['title'], S_TITLE),
             Paragraph(header['meta'].upper(), S_META),
             Spacer(1, 5), Rule(), Spacer(1, 8),
             Paragraph(header['intro'], S_NOTE), Spacer(1, 12)]

    for si, sc in enumerate(schemes):
        if si:
            story.append(Spacer(1, 6))
        head = Table([[Paragraph('<font name="UI-Bold" size="12">%s</font>' % sc['title'], S_ANS),
                       Paragraph('<font name="Mono" size="8" color="#5A5A66">%s</font>'
                                 % sc['meta'].upper(), S_MARKS)]],
                     colWidths=[AVAIL*0.62, AVAIL*0.38])
        head.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), PAPERBG),
            ('BOX', (0,0), (-1,-1), 0.6, LINE),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 9), ('RIGHTPADDING', (0,0), (-1,-1), 9),
            ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ]))
        story.append(head)
        story.append(Spacer(1, 7))

        for q in sc['questions']:
            block = []
            body = '<br/>'.join(q['lines'])
            row = Table([[Paragraph('%s' % q['n'], S_ANSN),
                          Paragraph(body, S_ANS),
                          Paragraph('[%d]' % q['marks'], S_MARKS)]],
                        colWidths=[21, AVAIL-21-26, 26])
            row.setStyle(TableStyle([
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ]))
            block.append(row)
            if q.get('note'):
                block.append(Table([[Paragraph(q['note'], S_NOTE)]], colWidths=[AVAIL-21],
                                   style=TableStyle([('LEFTPADDING', (0,0), (-1,-1), 21),
                                                     ('RIGHTPADDING', (0,0), (-1,-1), 0),
                                                     ('TOPPADDING', (0,0), (-1,-1), 1),
                                                     ('BOTTOMPADDING', (0,0), (-1,-1), 0)])))
            block.append(Spacer(1, 7))
            story.append(KeepTogether(block))

    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                          topMargin=MARGIN_T, bottomMargin=MARGIN_B,
                          title=header['title'], author='Base Camp')
    frame = Frame(MARGIN_L, MARGIN_B, AVAIL, A4[1]-MARGIN_T-MARGIN_B, id='f',
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame])])
    footer = header['footer']

    class C(NumberedCanvas):
        def __init__(self, *a, **k):
            k['footer'] = footer
            NumberedCanvas.__init__(self, *a, **k)

    doc.build(story, canvasmaker=C)
    return path
