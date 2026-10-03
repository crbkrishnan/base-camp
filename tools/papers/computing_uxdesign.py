#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Four test papers + mark-scheme booklet for uxdesign.html (Computing, Unit 4a: design).

Papers have no computer beside them, so every screen is drawn here with reportlab graphics.
paper_lib.build_paper has no hook for drawings, so this file carries its own build_paper()
(a copy of the library's layout plus a `flow` key on questions and parts) and does NOT edit
paper_lib.py.

Every number printed on a paper or in the scheme comes from CALC, computed below with exact
Fractions. _verify() re-derives them a second way and asserts marks, parts, [1] tags and
colour luminances. Run it:  python3 tools/papers/computing_uxdesign.py
"""
import os, sys
from fractions import Fraction as F

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import (build_scheme, AVAIL, INK, SOFT, LINE, RULE, PAPERBG, MARGIN_L, MARGIN_R,
                       MARGIN_T, MARGIN_B, S_Q, S_NOTE, S_SEC, Ruled, Rule, NumberedCanvas,
                       _header, _qrow, _tickboxes)
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, Flowable, KeepTogether)

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Computing · Grade 7 · Unit 4 · Design'
TOPIC = 'Design Before You Build'
HEX = colors.HexColor

# =====================================================================================
#  1. NUMBERS — all computed, none typed
# =====================================================================================

def lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4          # same as the page

def lum(h):
    r, g, b = [int(h[i:i + 2], 16) for i in (1, 3, 5)]
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)

def ratio_exact(l1, l2):
    """WCAG: (lighter + 0.05) / (darker + 0.05), with exact Fractions."""
    l1, l2 = F(l1), F(l2)
    return (max(l1, l2) + F(5, 100)) / (min(l1, l2) + F(5, 100))

def fr(x):
    """7 -> '7.0', 5.25 -> '5.25', 3.5 -> '3.5' (hand-friendly, two places at most)."""
    s = '%.2f' % float(x)
    return s[:-1] if s.endswith('0') else s

class Sw:
    """A printed colour sample. L values are nominal (to 2 dp) so the sum works by hand; the hex
    codes are chosen so the real WCAG luminance agrees with the nominal one."""
    def __init__(self, tag, fg, bg, lf, lb, text, px, bold=False):
        self.tag, self.fg, self.bg, self.text, self.px, self.bold = tag, fg, bg, text, px, bold
        self.lf, self.lb = F(lf), F(lb)
        self.hand = ratio_exact(self.lf, self.lb)                                 # what the student computes
        self.true = (max(lum(fg), lum(bg)) + 0.05) / (min(lum(fg), lum(bg)) + 0.05)   # what the hex codes really give
        assert abs(lum(fg) - float(self.lf)) < 0.0007 and abs(lum(bg) - float(self.lb)) < 0.0007, tag
        assert abs(float(self.hand) - self.true) < 0.005, (tag, float(self.hand), self.true)
        assert abs(float(self.hand) - 4.5) > 0.2 and abs(float(self.hand) - 3) > 0.2, tag   # no knife-edge verdicts
        self.pass_ord = self.hand >= F(9, 2)
        self.pass_large = self.hand >= 3

def lstr(x):           # '0.10', '1.00'
    return '%.2f' % float(x)

WHITE = '#FFFFFF'
# Paper A — dark text on white
A_S1 = Sw('A', '#1B6360', WHITE, '0.10', '1.00', 'Return by Friday', 16)
A_S2 = Sw('B', '#CC7224', WHITE, '0.25', '1.00', 'Return by Friday', 16)
# Paper B — two button labels
B_S1 = Sw('1', '#153696', '#C09C09', '0.05', '0.35', 'Book ticket', 16)
B_S2 = Sw('2', WHITE, '#097E09', '1.00', '0.15', 'Book ticket', 16)
# Paper C — three samples (hard: only L is printed)
C_S1 = Sw('i', '#81B7F3', '#153696', '0.45', '0.05', 'Order lunch', 16)
C_S2 = Sw('ii', '#153696', '#D28151', '0.05', '0.30', 'Order lunch', 16)
C_S3 = Sw('iii', '#960FB1', '#F3EDE1', '0.10', '0.85', 'Order lunch', 16)
# Paper D — white label on green
D_S1 = Sw('', WHITE, '#309C51', '1.00', '0.25', 'Book now', 16)

CALC = {}
c = CALC
# ---- A
c['A_r1'], c['A_r2'] = A_S1.hand, A_S2.hand
c['A_pad_w'], c['A_pad_h'] = F(48 - 32, 2), F(48 - 28, 2)
c['A_new_w'], c['A_new_h'] = 32 + 2 * 4, 28 + 2 * 4
c['A_X'] = F(390 - 342, 2)
c['A_step'] = 96 + 24
c['A_Y3'] = 88 + 2 * c['A_step']
c['A_bot3'] = c['A_Y3'] + 96
c['A_below'] = 844 - c['A_bot3']
c['A_w_forgot_gaps'], c['A_w_three_steps'], c['A_w_from_top'] = 88 + 2 * 96, 88 + 3 * c['A_step'], 844 - c['A_Y3']
# ---- B
c['B_r1'], c['B_r2'] = B_S1.hand, B_S2.hand
c['B_no_plus'] = F(35, 100) / F(5, 100)                                          # forgot the +0.05
c['B_six'] = 6 * 44 + 5 * 12
c['B_six_wrong'] = 6 * 44 + 6 * 12
c['B_seven'] = 7 * 44 + 6 * 12
c['B_Y5'] = 72 + 4 * 56
c['B_Y5_wrong'] = 72 + 5 * 56
c['B_fit_exact'] = F(844 - 72, 56)
c['B_fit'] = (844 - 72) // 56
c['B_scores'] = [5, 4, 2, 1, 4, 5]
c['B_avg'] = F(sum(c['B_scores']), 6)
c['B_avg_wrong'] = F(sum(c['B_scores']), 5)
# ---- C
c['C_r1'], c['C_r2'], c['C_r3'] = C_S1.hand, C_S2.hand, C_S3.hand
c['C_usable'] = 360 - 2 * 16
c['C_col'] = F(c['C_usable'] - 3 * 8, 4)
c['C_span2'] = 2 * c['C_col'] + 8
c['C_X3'] = 16 + 2 * (c['C_col'] + 8)
c['C_col_wrong'], c['C_span_wrong'], c['C_X3_wrong'] = F(c['C_usable'], 4), 2 * c['C_col'], 16 + 2 * c['C_col']
c['C_pct'] = F(27, 36) * 100
# ---- D
c['D_links3'], c['D_links4'] = 3 * 2, 4 * 3
c['D_links_wrong'] = 4 * 4
c['D_added'] = c['D_links4'] - c['D_links3']
c['D_r'] = D_S1.hand
c['D_tab_Y'] = 844 - 72
c['D_area'] = c['D_tab_Y'] - 96
c['D_rows'] = c['D_area'] // 64
c['D_rows_exact'] = F(c['D_area'], 64)
c['D_left'] = c['D_area'] - 64 * c['D_rows']
c['D_rows72'] = c['D_area'] // 72
c['D_rows72_exact'] = F(c['D_area'], 72)
c['D_rows_forgot_tab'] = (844 - 96) // 64
c['D_before'], c['D_fixA'], c['D_fixB'] = [4, 3, 1, 3, 5], [5, 5, 1, 4, 5], [4, 3, 3, 3, 5]
c['D_avg_before'] = F(sum(c['D_before']), 5)
c['D_avg_A'] = F(sum(c['D_fixA']), 5)
c['D_avg_B'] = F(sum(c['D_fixB']), 5)

def n(x):
    """Format an int/Fraction for print: integers plain, others via fr()."""
    x = F(x)
    return str(int(x)) if x.denominator == 1 else fr(x)

# =====================================================================================
#  2. DRAWING TOOLKIT (reportlab graphics, drawn straight onto the paper canvas)
# =====================================================================================

DARK = HEX('#4A4650'); MID = HEX('#9C8F92'); FILL = HEX('#F6F2F0'); BLOCK = HEX('#E6DFDC')
FOOT = HEX('#D9D0CD'); RASP = HEX('#A8325E'); TEAL = HEX('#1D6A6A')
RASP_T = HEX('#F6E4EB'); TEAL_T = HEX('#DDEEED'); BLUE = HEX('#1D4ED8'); GREEN = HEX('#2E7D32')
RED = HEX('#C62828'); GRID = HEX('#E3DED6')


class Art(Flowable):
    """A drawing: fn(canvas, width, height) paints with (0,0) at bottom-left."""
    def __init__(self, h_mm, fn, w=AVAIL):
        Flowable.__init__(self)
        self.width, self.height, self.fn = w, h_mm * mm, fn
    def wrap(self, aw, ah):
        return self.width, self.height
    def draw(self):
        self.canv.saveState()
        self.fn(self.canv, self.width, self.height)
        self.canv.restoreState()


def T(cv, s, x, y, font='UI', size=8, col=INK, anchor='l'):
    cv.setFont(font, size); cv.setFillColor(col)
    {'l': cv.drawString, 'c': cv.drawCentredString, 'r': cv.drawRightString}[anchor](x, y, s)

def R(cv, x, y, w, h, fill=None, stroke=DARK, lw=1.0, r=0, dash=None):
    cv.setLineWidth(lw)
    cv.setDash(*dash) if dash else cv.setDash()
    if fill is not None: cv.setFillColor(fill)
    if stroke is not None: cv.setStrokeColor(stroke)
    if r: cv.roundRect(x, y, w, h, r, stroke=1 if stroke is not None else 0, fill=1 if fill is not None else 0)
    else: cv.rect(x, y, w, h, stroke=1 if stroke is not None else 0, fill=1 if fill is not None else 0)
    cv.setDash()

def L_(cv, x1, y1, x2, y2, col=DARK, lw=1.0, dash=None):
    cv.setStrokeColor(col); cv.setLineWidth(lw)
    cv.setDash(*dash) if dash else cv.setDash()
    cv.line(x1, y1, x2, y2); cv.setDash()

def arrow(cv, x1, y1, x2, y2, col=DARK, lw=1.2, head=4.5, both=False):
    import math
    L_(cv, x1, y1, x2, y2, col, lw)
    def tip(xa, ya, xb, yb):
        a = math.atan2(yb - ya, xb - xa)
        p = cv.beginPath()
        p.moveTo(xb, yb)
        p.lineTo(xb - head * math.cos(a - 0.45), yb - head * math.sin(a - 0.45))
        p.lineTo(xb - head * math.cos(a + 0.45), yb - head * math.sin(a + 0.45))
        p.close(); cv.setFillColor(col); cv.drawPath(p, stroke=0, fill=1)
    tip(x1, y1, x2, y2)
    if both: tip(x2, y2, x1, y1)


# ---------------- the double diamond, boxes blank ----------------
def diamond_fn(h_mm=50):
    def fn(cv, w, h):
        sx, sy = w / 760.0, h / 250.0
        P = lambda x, y: (x * sx, h - y * sy)
        tris = [((30, 120), (205, 30), (205, 210), RASP_T, RASP),
                ((205, 30), (380, 120), (205, 210), TEAL_T, TEAL),
                ((380, 120), (555, 30), (555, 210), RASP_T, RASP),
                ((555, 30), (730, 120), (555, 210), TEAL_T, TEAL)]
        for a, b, d, fill, st in tris:
            p = cv.beginPath(); p.moveTo(*P(*a)); p.lineTo(*P(*b)); p.lineTo(*P(*d)); p.close()
            cv.setFillColor(fill); cv.setStrokeColor(st); cv.setLineWidth(1.8); cv.drawPath(p, stroke=1, fill=1)
        cx = [132, 268, 482, 618]
        for x in cx:                                   # phase-name boxes (inside)
            bx, by = P(x - 58, 120 + 20)
            R(cv, bx, by, 116 * sx, 40 * sy, fill=colors.white, stroke=DARK, lw=0.9, r=3)
            T(cv, 'phase name', bx + 58 * sx, by + 13 * sy, 'UI', 6.2, MID, 'c')
        for x in cx:                                   # direction boxes (above)
            bx, by = P(x - 64, 22)
            R(cv, bx, by, 128 * sx, 20 * sy, fill=colors.white, stroke=DARK, lw=0.9, r=3, dash=(2.5, 2))
            T(cv, 'diverge or converge?', bx + 64 * sx, by + 6.5 * sy, 'UI', 6.2, MID, 'c')
        T(cv, 'DIAMOND 1', 205 * sx, 6, 'Mono-Bold', 7.5, SOFT, 'c')
        T(cv, 'DIAMOND 2', 555 * sx, 6, 'Mono-Bold', 7.5, SOFT, 'c')
    return fn


# ---------------- a "diamond" drawn as a straight line (paper B) ----------------
def straight_fn():
    def fn(cv, w, h):
        T(cv, "Ishaan's drawing", 0, h - 9, 'Mono-Bold', 7.6, SOFT)
        bw, bh, gap = 82, 32, 18
        x = 4
        y = h / 2 - bh / 2 - 6
        names = ['Discover', 'Define', 'Develop', 'Deliver']
        for i, nm in enumerate(names):
            R(cv, x, y, bw, bh, fill=colors.white, stroke=DARK, lw=1.4, r=4)
            T(cv, nm, x + bw / 2, y + bh / 2 - 3.6, 'UI-Bold', 10.5, INK, 'c')
            arrow(cv, x + bw + 1, y + bh / 2, x + bw + gap - 1, y + bh / 2, DARK, 1.3)
            x += bw + gap
        R(cv, x, y, w - x - 2, bh, fill=BLOCK, stroke=DARK, lw=1.4, r=4)
        T(cv, 'FINISHED', x + (w - x - 2) / 2, y + bh / 2 - 3.6, 'UI-Bold', 9.5, INK, 'c')
    return fn


# ---------------- login screen with inconsistent buttons (paper A) ----------------
def login_fn():
    def fn(cv, w, h):
        pw, ph = 168, h - 6
        px0, py0 = 6, 3
        R(cv, px0, py0, pw, ph, fill=colors.white, stroke=DARK, lw=1.8, r=14)
        T(cv, 'Shelf · school library', px0 + 14, py0 + ph - 22, 'UI-Bold', 10.5, INK)
        T(cv, 'Sign in', px0 + 14, py0 + ph - 38, 'UI', 8.5, SOFT)
        # email field: red border only
        T(cv, 'Email', px0 + 14, py0 + ph - 54, 'UI', 7.5, SOFT)
        R(cv, px0 + 14, py0 + ph - 74, pw - 28, 17, fill=colors.white, stroke=RED, lw=2.0, r=2)
        T(cv, 'ananya.school.com', px0 + 19, py0 + ph - 69.5, 'UI', 7.8, INK)
        T(cv, 'Password', px0 + 14, py0 + ph - 90, 'UI', 7.5, SOFT)
        R(cv, px0 + 14, py0 + ph - 110, pw - 28, 17, fill=colors.white, stroke=MID, lw=0.9, r=2)
        T(cv, '••••••••', px0 + 19, py0 + ph - 105, 'UI', 8, INK)
        # three buttons, deliberately inconsistent
        bx = px0 + 14; bw = pw - 28
        R(cv, bx, py0 + ph - 144, bw, 25, fill=BLUE, stroke=None, r=12.5)
        T(cv, 'Log in', bx + bw / 2, py0 + ph - 135.5, 'UI-Bold', 9.5, colors.white, 'c')
        R(cv, bx, py0 + ph - 172, bw * 0.78, 17, fill=GREEN, stroke=None, r=0)
        T(cv, 'Sign up', bx + bw * 0.39, py0 + ph - 166.5, 'UI-Bold', 8, colors.white, 'c')
        R(cv, bx, py0 + ph - 200, bw, 20, fill=HEX('#9E9E9E'), stroke=None, r=4)
        T(cv, 'CONTINUE AS GUEST', bx + bw / 2, py0 + ph - 193.5, 'UI', 7.6, colors.white, 'c')
        # callouts on the right
        cx = px0 + pw + 22
        T(cv, 'Figure 1', cx, h - 14, 'Mono-Bold', 7.6, SOFT)
        T(cv, 'The sign-in screen of the school library app.', cx, h - 28, 'Body', 9.2, INK)
        T(cv, 'Ananya tapped Log in. The email she typed has no @.', cx, h - 41, 'Body', 9.2, INK)
        arrow(cv, cx - 2, h - 75, px0 + pw - 16, py0 + ph - 66, SOFT, 0.8, 3.2)
        T(cv, 'This is the only sign that', cx, h - 72, 'Body-Italic', 8.8, SOFT)
        T(cv, 'something is wrong.', cx, h - 83, 'Body-Italic', 8.8, SOFT)
        T(cv, 'Three buttons, three jobs, one screen.', cx, py0 + ph - 150, 'Body-Italic', 8.8, SOFT)
    return fn


# ---------------- colour samples ----------------
def swatch_fn(sws, show_hex=True, h_mm=33, label_style='A'):
    def fn(cv, w, h):
        k = len(sws)
        gap = 14
        sw = (w - gap * (k - 1)) / k
        for i, s in enumerate(sws):
            x = i * (sw + gap)
            sh = 50
            by = h - 14 - sh
            if s.tag:
                T(cv, ('Sample ' if label_style == 'A' else ('Button ' if label_style == 'B' else 'Sample ')) + s.tag,
                  x, h - 8, 'Mono-Bold', 7.6, SOFT)
            R(cv, x, by, sw, sh, fill=HEX(s.bg), stroke=DARK, lw=1.0, r=3)
            size = s.px * 0.75
            T(cv, s.text, x + 12, by + sh / 2 - size * 0.33, 'UI-Bold' if s.bold else 'UI', size, HEX(s.fg))
            T(cv, 'text  ' + s.fg + '   L = ' + lstr(s.lf), x, by - 11, 'Mono', 7.5, INK)
            T(cv, 'back  ' + s.bg + '   L = ' + lstr(s.lb), x, by - 21, 'Mono', 7.5, INK)
    return fn


def sizes_fn(sw):
    specs = [('16 px regular', 16, False), ('20 px bold', 20, True), ('24 px regular', 24, False)]
    def fn(cv, w, h):
        gap = 14
        bw = (w - 2 * gap) / 3.0
        for i, (cap, px, bold) in enumerate(specs):
            x = i * (bw + gap)
            by = h - 14 - 42
            R(cv, x, by, bw, 42, fill=HEX(sw.bg), stroke=DARK, lw=1.0, r=6)
            T(cv, sw.text, x + bw / 2, by + 21 - px * 0.75 * 0.33, 'UI-Bold' if bold else 'UI', px * 0.75, HEX(sw.fg), 'c')
            T(cv, cap, x, h - 8, 'Mono-Bold', 7.6, SOFT)
            T(cv, 'text  ' + sw.fg + '   L = ' + lstr(sw.lf), x, by - 11, 'Mono', 7.5, INK)
            T(cv, 'back  ' + sw.bg + '   L = ' + lstr(sw.lb), x, by - 21, 'Mono', 7.5, INK)
    return fn


# ---------------- Figma-style frames (all drawn at 0.2 pt per px) ----------------
K = 0.165
def phone(cv, x0, y0, W=390, H=844, k=K, r=4):
    R(cv, x0, y0, W * k, H * k, fill=colors.white, stroke=DARK, lw=1.6, r=r)

def dimv(cv, x, ytop, ybot, label, col=RASP, side='l', size=7.2):
    arrow(cv, x, ytop, x, ybot, col, 0.9, 3, both=True)
    T(cv, label, x - 3 if side == 'l' else x + 3, (ytop + ybot) / 2 - 2.5, 'Mono-Bold', size, col,
      'r' if side == 'l' else 'l')

def figma_cards_fn():
    def fn(cv, w, h):
        x0, y0 = 54, (h - 844 * K) / 2
        top = y0 + 844 * K
        phone(cv, x0, y0)
        Y = lambda y: top - y * K
        for i in range(3):
            yy = 88 + i * 120
            R(cv, x0 + 24 * K, Y(yy + 96), 342 * K, 96 * K, fill=FILL, stroke=DARK, lw=1.0, r=2)
            T(cv, 'card %d' % (i + 1), x0 + 24 * K + 5, Y(yy + 96) + 96 * K / 2 - 2.5, 'UI', 6.8, INK)
        # dimension marks (unknowns are '?')
        dimv(cv, x0 - 8, Y(0), Y(88), '88', col=DARK)
        dimv(cv, x0 - 8, Y(88 + 3 * 96 + 2 * 24 - 0), Y(844), '?', col=RASP)
        arrow(cv, x0 + 1, Y(60), x0 + 24 * K - 1, Y(60), RASP, 0.9, 2.6, both=False)
        T(cv, 'X = ?', x0 + 24 * K + 3, Y(60) - 2, 'Mono-Bold', 6.6, RASP)
        yy3 = 88 + 2 * 120
        T(cv, 'Y = ?', x0 + 390 * K + 5, Y(yy3 + 96) + 96 * K / 2 - 2.5, 'Mono-Bold', 7.2, RASP)
        dimv(cv, x0 + 390 * K + 10, Y(88 + 96), Y(88 + 120), '24', col=DARK, side='r')
        T(cv, 'gap', x0 + 390 * K + 30, Y(88 + 108) - 2.5, 'UI', 6.6, SOFT)
        # notes
        tx = x0 + 390 * K + 62
        T(cv, 'FIGMA PANEL', tx, h - 14, 'Mono-Bold', 7.6, SOFT)
        lines = ['Frame:  W 390   H 844', 'All three cards:  W 342   H 96', 'Gap between neighbouring cards:  24',
                 'Card 1:  top edge at  Y = 88', 'Cards are centred, left to right', '',
                 'X and Y are measured from the top-left', 'corner of the frame. The ? marks are yours to find.']
        for i, ln in enumerate(lines):
            T(cv, ln, tx, h - 30 - i * 13, 'Mono', 8, INK if i < 5 else SOFT)
    return fn

def figma_rows_fn():
    def fn(cv, w, h):
        x0, y0 = 54, (h - 844 * K) / 2
        top = y0 + 844 * K
        phone(cv, x0, y0)
        Y = lambda y: top - y * K
        R(cv, x0, Y(72), 390 * K, 72 * K, fill=BLOCK, stroke=DARK, lw=1.0, r=0)
        T(cv, 'header', x0 + 5, Y(72) + 72 * K / 2 - 2.5, 'UI', 6.8, INK)
        for i in range(6):
            yy = 72 + i * 56
            R(cv, x0, Y(yy + 56), 390 * K, 56 * K, fill=FILL if i % 2 == 0 else colors.white, stroke=DARK, lw=0.8, r=0)
            T(cv, 'row %d' % (i + 1), x0 + 5, Y(yy + 56) + 56 * K / 2 - 2.5, 'UI', 6.8, INK)
        yy = 72 + 6 * 56
        for j in range(3):
            L_(cv, x0 + 6, Y(yy + 24 + j * 24), x0 + 390 * K - 6, Y(yy + 24 + j * 24), MID, 0.7, (1.5, 2.5))
        dimv(cv, x0 - 8, Y(0), Y(72), '72', col=DARK)
        dimv(cv, x0 - 8, Y(72 + 4 * 56), Y(72 + 5 * 56), '56', col=DARK)
        T(cv, 'row 5', x0 - 22, Y(72 + 4 * 56) + 1, 'UI', 6.2, SOFT, 'r')
        T(cv, 'Y of row 5 = ?', x0 + 390 * K + 8, Y(72 + 4 * 56) - 2, 'Mono-Bold', 7.2, RASP)
        L_(cv, x0 + 390 * K, Y(72 + 4 * 56), x0 + 390 * K + 6, Y(72 + 4 * 56), RASP, 0.9)
        tx = x0 + 390 * K + 62
        T(cv, 'FIGMA PANEL', tx + 70, h - 14, 'Mono-Bold', 7.6, SOFT)
        lines = ['Frame:  W 390   H 844', 'Header:  H 72, at Y = 0', 'Every row:  H 56, no gaps',
                 'Row 1:  top edge at  Y = 72', '', 'Rows run down to the bottom', 'edge of the frame (Y = 844).']
        for i, ln in enumerate(lines):
            T(cv, ln, tx + 70, h - 30 - i * 13, 'Mono', 8, INK if i < 4 else SOFT)
    return fn

def figma_grid_fn():
    def fn(cv, w, h):
        k = 0.8
        W = 360
        x0 = 34
        y0 = 16
        fh = h - 16 - 44
        R(cv, x0, y0, W * k, fh, fill=colors.white, stroke=DARK, lw=1.6, r=0)
        cols = [16 + i * 84 for i in range(4)]
        for i, cxp in enumerate(cols):
            R(cv, x0 + cxp * k, y0 + 1, 76 * k, fh - 2, fill=HEX('#F9E1E3'), stroke=None)
            T(cv, 'col %d' % (i + 1), x0 + (cxp + 38) * k, y0 + fh - 13, 'Mono-Bold', 7, RASP, 'c')
        R(cv, x0 + 16 * k, y0 + 30, (2 * 76 + 8) * k, 42, fill=colors.white, stroke=DARK, lw=1.2, r=2)
        T(cv, 'card across columns 1 and 2', x0 + 16 * k + 6, y0 + 48, 'UI', 7.6, INK)
        top = y0 + fh
        # margin / gutter / column labels above the frame, with leader lines
        T(cv, 'margin 16', x0 + 8 * k, top + 30, 'Mono', 6.8, DARK, 'c')
        L_(cv, x0 + 8 * k, top + 27, x0 + 8 * k, top + 3, DARK, 0.6)
        T(cv, 'gutter 8', x0 + 92 * k + 2, top + 30, 'Mono', 6.8, DARK, 'c')
        L_(cv, x0 + 92 * k + 2, top + 27, x0 + 92 * k + 2, top + 3, DARK, 0.6)
        T(cv, 'column width = ?', x0 + (16 + 38) * k + 40, top + 14, 'Mono-Bold', 6.8, RASP, 'c')
        arrow(cv, x0 + 16 * k, top + 6, x0 + 92 * k, top + 6, RASP, 0.8, 2.4, both=True)
        xm = x0 + cols[2] * k
        L_(cv, xm, y0 - 8, xm, y0 + 30, RASP, 1.0)
        T(cv, 'column 3 starts at X = ?', xm + 4, y0 - 8, 'Mono-Bold', 7.2, RASP)
        tx = x0 + W * k + 30
        T(cv, 'FIGMA PANEL', tx, h - 14, 'Mono-Bold', 7.6, SOFT)
        lines = ['Frame:  W 360', 'Layout grid:  4 columns', 'Margin:  16 each side', 'Gutter:  8 between columns', '',
                 'Figma divides the space that is', 'left equally between the four', 'columns.']
        for i, ln in enumerate(lines):
            T(cv, ln, tx, h - 30 - i * 13, 'Mono', 8, INK if i < 4 else SOFT)
    return fn

def figma_tab_fn():
    def fn(cv, w, h):
        x0, y0 = 54, (h - 844 * K) / 2
        top = y0 + 844 * K
        phone(cv, x0, y0)
        Y = lambda y: top - y * K
        R(cv, x0, Y(96), 390 * K, 96 * K, fill=BLOCK, stroke=DARK, lw=1.0)
        T(cv, 'header', x0 + 5, Y(96) + 96 * K / 2 - 2.5, 'UI', 6.8, INK)
        for i in range(5):
            yy = 96 + i * 64
            R(cv, x0, Y(yy + 64), 390 * K, 64 * K, fill=FILL if i % 2 == 0 else colors.white, stroke=DARK, lw=0.8)
            T(cv, 'row %d' % (i + 1), x0 + 5, Y(yy + 64) + 64 * K / 2 - 2.5, 'UI', 6.8, INK)
        R(cv, x0, y0, 390 * K, 72 * K, fill=HEX('#CFC8C4'), stroke=DARK, lw=1.2)
        T(cv, 'tab bar', x0 + 5, y0 + 72 * K / 2 - 2.5, 'UI-Bold', 6.8, INK)
        yy = 96 + 5 * 64
        for j in range(2):
            L_(cv, x0 + 6, Y(yy + 28 + j * 28), x0 + 390 * K - 6, Y(yy + 28 + j * 28), MID, 0.7, (1.5, 2.5))
        dimv(cv, x0 - 8, Y(0), Y(96), '96', col=DARK)
        dimv(cv, x0 - 8, Y(844 - 72), Y(844), '72', col=DARK)
        L_(cv, x0 + 390 * K, Y(844 - 72), x0 + 390 * K + 8, Y(844 - 72), RASP, 0.9)
        T(cv, 'tab bar top: Y = ?', x0 + 390 * K + 10, Y(844 - 72) - 2.5, 'Mono-Bold', 7.2, RASP)
        tx = x0 + 390 * K + 62
        T(cv, 'FIGMA PANEL', tx + 70, h - 14, 'Mono-Bold', 7.6, SOFT)
        lines = ['Frame:  W 390   H 844', 'Header:  Y = 0 to Y = 96', 'Tab bar:  H 72, flush with the', 'bottom edge of the frame',
                 'List rows:  H 64 each, no gaps,', 'row 1 starts at  Y = 96', 'Rows fill the space between the', 'header and the tab bar.']
        for i, ln in enumerate(lines):
            T(cv, ln, tx + 70, h - 30 - i * 13, 'Mono', 8, INK)
    return fn


# ---------------- wireframes ----------------
HT = {'toprow': 17, 'logo': 17, 'head': 17, 'image': 40, 'para': 24, 'button': 16, 'field': 15, 'footer': 19}

def wf_page(cv, x, y, w, h, items, label):
    T(cv, label, x, y + h + 4, 'Mono-Bold', 7.8, SOFT)
    R(cv, x, y, w, h, fill=colors.white, stroke=DARK, lw=1.6, r=5)
    cur = y + h - 6
    ix, iw = x + 6, w - 12
    for kind, lab in items:
        hh = HT[kind]
        by = cur - hh
        if kind == 'toprow':
            R(cv, ix, by, iw * 0.28, hh, fill=FILL, stroke=DARK, lw=1.0, dash=(3, 2))
            T(cv, 'LOGO', ix + 4, by + 5.5, 'Mono', 6.6, INK)
            R(cv, ix + iw * 0.32, by, iw * 0.68, hh, fill=FILL, stroke=DARK, lw=1.0)
            T(cv, 'Home  About  Contact', ix + iw * 0.32 + 4, by + 5.5, 'Mono', 6.4, INK)
        elif kind == 'logo':
            R(cv, ix, by, iw * 0.28, hh, fill=FILL, stroke=DARK, lw=1.0, dash=(3, 2))
            T(cv, 'LOGO', ix + 4, by + 5.5, 'Mono', 6.6, INK)
        elif kind == 'head':
            R(cv, ix, by, iw, hh, fill=BLOCK, stroke=DARK, lw=1.0)
            T(cv, lab or 'HEADING', ix + 4, by + 5.5, 'Mono-Bold', 6.8, INK)
        elif kind == 'image':
            R(cv, ix, by, iw, hh, fill=FILL, stroke=DARK, lw=1.0)
            L_(cv, ix, by, ix + iw, by + hh, MID, 0.7); L_(cv, ix, by + hh, ix + iw, by, MID, 0.7)
            R(cv, ix + iw / 2 - 17, by + hh / 2 - 6, 34, 12, fill=FILL, stroke=None)
            T(cv, 'IMAGE', ix + iw / 2, by + hh / 2 - 2.4, 'Mono', 6.8, INK, 'c')
        elif kind == 'para':
            for j, f in enumerate([1, 1, 0.62]):
                R(cv, ix, by + hh - 6 - j * 8, iw * f, 4, fill=MID, stroke=None)
        elif kind == 'button':
            R(cv, ix, by, iw * 0.55, hh, fill=BLOCK, stroke=DARK, lw=1.0, r=hh / 2)
            T(cv, lab or 'BUTTON', ix + iw * 0.275, by + hh / 2 - 2.4, 'Mono', 6.6, INK, 'c')
        elif kind == 'field':
            R(cv, ix, by, iw, hh, fill=colors.white, stroke=DARK, lw=1.0)
            T(cv, lab or 'field', ix + 4, by + 4.6, 'Mono', 6.6, SOFT)
        elif kind == 'footer':
            R(cv, ix, by, iw, hh, fill=FOOT, stroke=DARK, lw=1.0)
            T(cv, 'FOOTER', ix + 4, by + 6.6, 'Mono', 6.6, INK)
        cur = by - 5

def flawed_wf_fn(h_mm=70):
    def fn(cv, w, h):
        fw = (w - 2 * 14) / 3.0
        fh = h - 14
        pages = [
            ('HOME', [('toprow', ''), ('head', 'HEADING: Welcome'), ('image', ''), ('para', ''), ('footer', '')]),
            ('ABOUT', [('logo', ''), ('head', 'HEADING: About us'), ('para', ''), ('head', 'HEADING: Our menu'),
                       ('image', ''), ('footer', '')]),
            ('CONTACT', [('toprow', ''), ('head', 'HEADING: Contact'), ('field', 'Name _______'),
                         ('field', 'Message _______'), ('button', 'Send'), ('footer', ''), ('para', '')]),
        ]
        for i, (lab, items) in enumerate(pages):
            wf_page(cv, i * (fw + 14), 0, fw, fh, items, lab)
    return fn

def blank_frames_fn(labels, h_mm, notes=3, side_notes=False, note_label='NOTES'):
    def fn(cv, w, h):
        k = len(labels)
        gap = 14
        if side_notes:
            fw = 150
        else:
            fw = (w - gap * (k - 1)) / k
        note_h = 0 if side_notes else (notes * 17 + 14)
        fh = h - 16 - note_h
        for i, lab in enumerate(labels):
            x = i * (fw + gap)
            T(cv, lab, x, h - 11, 'Mono-Bold', 7.8, SOFT)
            T(cv, '390 × 844 frame', x + fw, h - 11, 'Mono', 6.8, MID, 'r')
            R(cv, x, note_h, fw, fh, fill=colors.white, stroke=DARK, lw=1.6, r=6)
            gx = 12
            c2 = cv
            c2.setStrokeColor(GRID); c2.setLineWidth(0.4)
            xx = x + gx
            while xx < x + fw - 2:
                c2.line(xx, note_h + 3, xx, note_h + fh - 3); xx += gx
            yy = note_h + gx
            while yy < note_h + fh - 2:
                c2.line(x + 3, yy, x + fw - 3, yy); yy += gx
            R(cv, x, note_h, fw, fh, fill=None, stroke=DARK, lw=1.6, r=6)
            if not side_notes:
                T(cv, note_label, x, note_h - 10, 'Mono-Bold', 6.8, SOFT)
                for j in range(notes):
                    yy = note_h - 10 - (j + 1) * 15.5 + 4
                    L_(cv, x, yy, x + fw, yy, RULE, 0.6)
        if side_notes:
            nx = fw + 26
            T(cv, note_label, nx, h - 11, 'Mono-Bold', 7.8, SOFT)
            yy = h - 28
            while yy > 6:
                L_(cv, nx, yy, w, yy, RULE, 0.6); yy -= 17
    return fn

def box_fn(label, h_mm):
    def fn(cv, w, h):
        R(cv, 0, 0, w, h, fill=colors.white, stroke=DARK, lw=1.0, r=4, dash=(4, 3))
        T(cv, label, 8, h - 11, 'Mono-Bold', 7, MID)
    return fn


# ---------------- another student's notebook (paper D) ----------------
def notebook_fn(h_mm, owner, statements):
    from reportlab.lib.utils import simpleSplit
    PEN = HEX('#1F3A93')
    def fn(cv, w, h):
        R(cv, 0, 0, w, h, fill=HEX('#FBF9F1'), stroke=LINE, lw=0.8, r=3)
        step = 22
        rules = []
        yy = h - 42
        while yy > 6:
            L_(cv, 0, yy, w, yy, HEX('#CFE0EE'), 0.6); rules.append(yy); yy -= step
        L_(cv, 38, 0, 38, h, HEX('#E9A0A0'), 0.8)
        T(cv, owner, 48, h - 16, 'Mono-Bold', 7.6, SOFT)
        k = 0
        for lab, txt in statements:
            lines = simpleSplit(txt, 'Body-Italic', 11.6, w - 48 - 14 - 22)
            T(cv, lab, 48, rules[k] + 4, 'Body-Italic', 11.6, PEN)
            for ln in lines:
                T(cv, ln, 48 + 22, rules[k] + 4, 'Body-Italic', 11.6, PEN)
                k += 1
            k += 1
    return fn


# =====================================================================================
#  3. TABLES
# =====================================================================================
def grid2(rows, widths, blank_h=10 * mm, fs=10, hfs=8.8, center_from=None):
    body = ParagraphStyle('gb', parent=S_Q, fontSize=fs, leading=fs + 3)
    head = ParagraphStyle('gh', fontName='UI-Bold', fontSize=hfs, leading=hfs + 2.4, textColor=INK)
    ctr = ParagraphStyle('gc', parent=body, alignment=1, fontName='Mono', fontSize=fs + 0.6)
    data = []
    for i, row in enumerate(rows):
        r = []
        for j, cell in enumerate(row):
            if i == 0:
                r.append(Paragraph(cell, head))
            elif cell == '':
                r.append([Spacer(1, blank_h)])
            else:
                r.append(Paragraph(cell, ctr if (center_from is not None and j >= center_from) else body))
        data.append(r)
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.6, LINE), ('BACKGROUND', (0, 0), (-1, 0), PAPERBG),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5), ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    return t


def hang(rows, label_w=26, fs=10.2):
    """A borderless two-column block: a bold label and text that wraps under itself."""
    sty = ParagraphStyle('hg', parent=S_Q, fontSize=fs, leading=fs + 3.4)
    lab = ParagraphStyle('hl', fontName='UI-Bold', fontSize=fs, leading=fs + 3.4, textColor=INK)
    t = Table([[Paragraph(a, lab), Paragraph(b, sty)] for a, b in rows],
              colWidths=[label_w, AVAIL - 24 - 24 - label_w - 8])
    t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 1),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
    outer = Table([[t]], colWidths=[AVAIL])
    outer.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 24 + 4), ('RIGHTPADDING', (0, 0), (-1, -1), 24),
                               ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return outer


# =====================================================================================
#  4. LOCAL build_paper: the library's layout + a `flow` key
# =====================================================================================
def _flows(x):
    if x is None: return []
    return list(x) if isinstance(x, (list, tuple)) else [x]

def build_paper(spec, path):
    story = _header(spec)
    for i, q in enumerate(spec['questions'], 1):
        head = []
        if q.get('section'):
            head.append(Paragraph(q['section'].upper(), S_SEC))
        top_marks = q.get('marks', 0) if not q.get('parts') else 0
        head.append(_qrow('%d.' % i, q['text'], top_marks))
        for fl in _flows(q.get('flow')):
            head.append(Spacer(1, 5)); head.append(fl)
        if q.get('flow') is not None and q.get('parts'):
            head.append(Spacer(1, 4))
        if q.get('tick'):
            head.append(Spacer(1, 3)); head.append(_tickboxes(q['tick'])); head.append(Spacer(1, 2))
        if q.get('space'):
            head.append(Ruled(q['space']))
        if q.get('tip') and not q.get('parts'):
            head.append(Spacer(1, 2)); head.append(Paragraph(q['tip'], S_NOTE))
        blocks = [head]
        for p in q.get('parts', []):
            sub = [Spacer(1, 3), _qrow(p['label'], p['text'], p.get('marks', 0), indent=16, numw=26)]
            for fl in _flows(p.get('flow')):
                sub.append(Spacer(1, 4)); sub.append(fl)
            if p.get('space'):
                sub.append(Ruled(p['space'], width=AVAIL, indent=16))
            blocks.append(sub)
        if q.get('tip') and q.get('parts'):
            blocks.append([Spacer(1, 2), Paragraph(q['tip'], S_NOTE)])
        if q.get('keep'):
            story.append(KeepTogether([x for b in blocks for x in b]))
        else:
            for b in blocks:
                story.append(KeepTogether(b))
        story.append(Spacer(1, 11))
    story.append(Spacer(1, 4)); story.append(Rule(thickness=0.6, colour=LINE)); story.append(Spacer(1, 4))
    story.append(Paragraph(spec.get('endnote', 'End of paper.'), S_NOTE))

    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                          topMargin=MARGIN_T, bottomMargin=MARGIN_B, title=spec['title'].replace('&mdash;', '-'),
                          author='Base Camp')
    frame = Frame(MARGIN_L, MARGIN_B, AVAIL, A4[1] - MARGIN_T - MARGIN_B, id='f',
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame])])
    footer = spec['footer']

    class Cv(NumberedCanvas):
        def __init__(self, *a, **k):
            k['footer'] = footer
            NumberedCanvas.__init__(self, *a, **k)
    doc.build(story, canvasmaker=Cv)
    return path


# =====================================================================================
#  5. THE PAPERS
# =====================================================================================
ENDNOTE = ('End of paper. Check that every screen measurement carries px, and that every UI or UX '
           'answer says why, not just which.')

BASE = [
 'Answer <b>every</b> question in the space provided. Show your working: method marks are awarded even when the final answer is wrong.',
 'No calculator and no computer. Every number on this paper works by hand.',
 'Where a question says <b>sketch</b>, draw plain boxes and labels only. Colour, real pictures and decoration earn nothing on a wireframe.',
 'Write <b>px</b> on every screen measurement. Give a contrast ratio as a number.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + [
 'Reminder: <b>contrast ratio = (L&#8321; + 0.05) &divide; (L&#8322; + 0.05)</b>, where L is relative luminance and L&#8321; belongs to the <b>lighter</b> colour. '
 'Ordinary text needs a ratio of at least <b>4.5</b>. Large text (24 px or bigger, or 18.66 px bold) needs at least <b>3</b>.']
INSTR_HARD = BASE + [
 'No formula and no pass mark is given on this paper. If you cannot remember them, write down what you do know and work from there. Relative luminance L is printed wherever you need it.',
 'Several questions describe products and situations you may not have seen before. Apply the ideas you already have.']

_ = lambda s: s  # readability

# ------------------------------------------------------------------ Paper A (library)
A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC, 'endnote': ENDNOTE,
 'questions': [
  {'section': 'Section 1 — the process and the words',
   'text': 'A school library is redesigning its book-renewal app and follows the double diamond. The diagram below has blank boxes.',
   'marks': 4, 'flow': Art(44, diamond_fn()),
   'parts': [{'label': '(a)', 'text': 'Write the name of each phase in its box, in order, from left to right.', 'marks': 2},
             {'label': '(b)', 'text': 'In each dashed box above the diagram, write <b>diverge</b> or <b>converge</b>.', 'marks': 1},
             {'label': '(c)', 'text': 'State what the team is holding at the end of the first diamond.', 'marks': 1, 'space': 15}]},
  {'text': 'Each activity below comes from one phase of the library project. Write the phase in the right-hand box. Use each phase once.',
   'marks': 4,
   'flow': grid2([['Activity', 'Phase'],
                  ['Watch six students try to renew a book at the desk', ''],
                  ['Write one sentence: &ldquo;Students return books late because they cannot see due dates&rdquo;', ''],
                  ['Sketch eight different ways to show a due date on the screen', ''],
                  ['Release it to every student, then track late returns', '']],
                 [AVAIL * 0.72, AVAIL * 0.28], blank_h=6.5 * mm),
   'tip': 'Two of these sound alike. Ask whether each one is about the problem or about the answer.'},
  {'text': 'Each change below is made to the library app. Write <b>UI</b> or <b>UX</b>, and give a reason in one short sentence.',
   'marks': 3,
   'parts': [{'label': '(a)', 'text': 'Darken the pale grey due-date text so it can be read in sunlight.', 'marks': 1, 'space': 12},
             {'label': '(b)', 'text': 'Cut renewing a book from five taps to two.', 'marks': 1, 'space': 12},
             {'label': '(c)', 'text': 'Show &ldquo;Renewed&rdquo; for a moment after the tap.', 'marks': 1, 'space': 12}],
   'tip': 'Did the screen change how it looks, or did the task change how it goes?'},

  {'section': 'Section 2 — numbers on a screen',
   'text': 'Two text colours are being tested on a white background for the due dates. L is relative luminance; white has L = 1.00.',
   'marks': 4, 'flow': Art(33, swatch_fn([A_S1, A_S2], label_style='A')),
   'parts': [{'label': '(a)', 'text': 'Calculate the contrast ratio for sample A.', 'marks': 1, 'space': 15},
             {'label': '(b)', 'text': 'Calculate the contrast ratio for sample B.', 'marks': 1, 'space': 15},
             {'label': '(c)', 'text': 'State which sample may be used for the ordinary 16 px due dates, and why.', 'marks': 1, 'space': 14},
             {'label': '(d)', 'text': 'The designer wants to use the other sample for a 28 px heading. State whether that is allowed, using a number from your answers.', 'marks': 1, 'space': 15}]},
  {'text': 'The Renew button is drawn <b>32 px wide and 28 px high</b>. A tap target should be at least <b>48 &times; 48 px</b>. '
           'Invisible padding, the same on every side, is added around the button.', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'Calculate the padding needed on each side to reach 48 px wide.', 'marks': 1, 'space': 14},
             {'label': '(b)', 'text': 'Calculate the padding needed on each side to reach 48 px high.', 'marks': 1, 'space': 14},
             {'label': '(c)', 'text': 'A designer adds only 4 px on every side. Calculate the new width and height, and state whether the button now meets 48 &times; 48.', 'marks': 1, 'space': 15}],
   'tip': 'Padding goes on <b>both</b> sides of the button.'},
  {'text': 'In Figma a designer makes a frame <b>390 px wide and 844 px high</b>. She places three cards in a column, each <b>342 px wide and 96 px high</b>. '
           'The top of card 1 is at <b>Y = 88</b>, there is a <b>24 px gap</b> between neighbouring cards, and the cards are centred from left to right.',
   'marks': 4, 'flow': Art(52, figma_cards_fn()),
   'parts': [{'label': '(a)', 'text': 'State the X position of each card.', 'marks': 1, 'space': 12},
             {'label': '(b)', 'text': 'Calculate the Y position of card 3.', 'marks': 2, 'space': 20},
             {'label': '(c)', 'text': 'Calculate the distance from the bottom of card 3 to the bottom of the frame.', 'marks': 1, 'space': 12}]},

  {'section': 'Section 3 — judging and drawing',
   'text': 'Look at the sign-in screen in Figure 1.', 'marks': 4, 'flow': Art(80, login_fn()),
   'parts': [{'label': '(a)', 'text': 'Describe two different ways in which the buttons are inconsistent.', 'marks': 2, 'space': 22},
             {'label': '(b)', 'text': 'The only sign that Ananya&rsquo;s email is wrong is the red border. Give one reason this fails for some users, and one addition that fixes it.', 'marks': 2, 'space': 26}]},
  {'text': 'The library also needs a Home screen. In the frame below, sketch a <b>low-fidelity wireframe</b> for it with: navigation, one heading, '
           'one button and a footer, in a sensible order. You may add an image box. Label every box, and use the notes lines to say what the button says.',
   'marks': 4, 'flow': Art(100, blank_frames_fn(['HOME'], 100, side_notes=True, note_label='NOTES')),
   'tip': 'Plain boxes and labels. Colour on a first wireframe is the mistake.'},
 ]}

# ------------------------------------------------------------------ Paper B (train tickets)
B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC, 'endnote': ENDNOTE,
 'questions': [
  {'section': 'Section 1 — process and vocabulary',
   'text': 'A team is designing a train-ticket app. Ishaan draws the design process like this and says: &ldquo;That is the double diamond.&rdquo;',
   'marks': 4, 'flow': Art(30, straight_fn()),
   'parts': [{'label': '(a)', 'text': 'Give two things his drawing leaves out that the real double diamond shows.', 'marks': 2, 'space': 28},
             {'label': '(b)', 'text': 'In the box, sketch the real double diamond. Name the four phases, and draw an arrow to show where a failed test can send the team.',
              'marks': 2, 'flow': Art(38, box_fn('SKETCH HERE', 38), w=AVAIL - 16)}]},
  {'text': 'Three lines from the train-ticket team&rsquo;s notebook. Write <b>Define</b> or <b>Develop</b> beside each.', 'marks': 3,
   'flow': grid2([['Line from the notebook', 'Define or Develop?'],
                  ['Sketch six different ways to show a platform change', ''],
                  ['Write: &ldquo;Commuters miss trains because platform changes appear only on a distant board&rdquo;', ''],
                  ['Group forty interview notes into three themes, then pick one', '']],
                 [AVAIL * 0.70, AVAIL * 0.30], blank_h=8 * mm),
   'tip': 'Which lines are about the problem, and which are about the answer?'},
  {'text': 'A student says: <i>&ldquo;All three of these fixes are UI, because you can see all of them on the screen.&rdquo;</i>', 'marks': 3,
   'flow': hang([('(i)', 'Replace the three-screen seat choice with one seat-map screen.'),
                 ('(ii)', 'Change the Book button to the same blue as the other buttons.'),
                 ('(iii)', 'Show a spinner and &ldquo;Booking your seat&rdquo; after the tap.')], label_w=30),
   'parts': [{'label': '(a)', 'text': 'State which one fix is truly a UI fix.', 'marks': 1, 'space': 12},
             {'label': '(b)', 'text': 'Explain why each of the other two is a UX fix.', 'marks': 2, 'space': 32}]},

  {'section': 'Section 2 — measuring screens',
   'text': 'Two button labels from the app, both 16 px and regular weight. L is relative luminance.',
   'marks': 5, 'flow': Art(33, swatch_fn([B_S1, B_S2], label_style='B')),
   'parts': [{'label': '(a)', 'text': 'Calculate the contrast ratio for button 1.', 'marks': 1, 'space': 20},
             {'label': '(b)', 'text': 'Calculate the contrast ratio for button 2.', 'marks': 1, 'space': 20},
             {'label': '(c)', 'text': 'State which button passes and which fails for these labels, and give the number each ratio is compared with.', 'marks': 2, 'space': 22},
             {'label': '(d)', 'text': 'The designer says: &ldquo;Button 1 is near enough to 4.5.&rdquo; Explain why that is not good enough.', 'marks': 1, 'space': 22}]},
  {'text': 'A toolbar has <b>328 px</b> of usable width. Every button is <b>44 px</b> wide, and the gap between neighbouring buttons is <b>12 px</b>.', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'Calculate the total width taken by 6 buttons and the gaps between them.', 'marks': 2, 'space': 26},
             {'label': '(b)', 'text': 'Can a seventh button fit? Show the width it would need.', 'marks': 1, 'space': 22}],
   'tip': 'n buttons have n &minus; 1 gaps between them.'},
  {'text': 'A frame is <b>390 px wide and 844 px high</b>. A header <b>72 px</b> high sits at the top, at Y = 0. Below it are list rows, each <b>56 px</b> high, '
           'with no gaps. Row 1 starts at <b>Y = 72</b>.', 'marks': 3, 'flow': Art(52, figma_rows_fn()),
   'parts': [{'label': '(a)', 'text': 'Calculate the Y position of row 5.', 'marks': 2, 'space': 22},
             {'label': '(b)', 'text': 'How many whole rows fit between the header and the bottom of the frame?', 'marks': 1, 'space': 24}]},

  {'section': 'Section 3 — users and wireframes',
   'text': 'Meet the persona. <b>Mrs Savitri Rao, 66,</b> books train tickets for her family. She uses her son&rsquo;s old phone with a cracked screen, '
           'her mobile data is slow, and she types with one finger. Her favourite colour is yellow. Her journey booking a ticket is scored from 1 (miserable) to 5 (delighted).',
   'marks': 4,
   'flow': grid2([['Step', '1 Open the app', '2 Search trains', '3 Choose a seat', '4 Passenger details', '5 Pay by UPI', '6 Get the ticket'],
                  ['Feeling'] + [str(v) for v in CALC['B_scores']]],
                 [AVAIL * 0.13] + [AVAIL * 0.145] * 6, blank_h=6 * mm, fs=10, hfs=7.6, center_from=1),
   'parts': [{'label': '(a)', 'text': 'State which step is the lowest point.', 'marks': 1, 'space': 12},
             {'label': '(b)', 'text': 'Calculate the average feeling score across the six steps.', 'marks': 1, 'space': 18},
             {'label': '(c)', 'text': 'Give one UX fix aimed at the lowest point.', 'marks': 1, 'space': 16},
             {'label': '(d)', 'text': 'Copy one detail from Savitri&rsquo;s card that earns its place on a persona, and say what design decision it changes.', 'marks': 1, 'space': 20}]},
  {'text': 'The Railway Club needs a three-page website: <b>Home, About and Contact</b>. In the frames below, sketch a low-fidelity wireframe for all three pages. '
           'It must show: the <b>same navigation in the same place</b> on every page; exactly <b>one heading</b> per page, before the content; a <b>button</b> on Home after its heading; '
           'a form with <b>two fields and a button</b> on Contact only; and a <b>footer</b> that is the last thing on every page. Use the notes lines for anything a box cannot say.',
   'marks': 5, 'flow': Art(104, blank_frames_fn(['HOME', 'ABOUT', 'CONTACT'], 104, notes=3)),
   'tip': 'Grey boxes and labels. If you reach for a coloured pencil, put it down.'},
 ]}

# ------------------------------------------------------------------ Paper C (canteen + bus)
C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC, 'endnote': ENDNOTE,
 'questions': [
  {'section': 'Section 1 — know the ideas',
   'text': 'A school canteen team is following the double diamond to design a pre-order app. The diagram is blank. After launch, a survey shows that students skip lunch because the '
           'break is too short, a cause nobody had researched.',
   'marks': 4, 'flow': Art(50, diamond_fn()),
   'parts': [{'label': '(a)', 'text': 'Write the four phases in the boxes, in order.', 'marks': 2},
             {'label': '(b)', 'text': 'In each dashed box, write <b>diverge</b> or <b>converge</b>.', 'marks': 1},
             {'label': '(c)', 'text': 'Draw an arrow on the diagram from the end of the process back to the phase the team should return to, and name that phase.', 'marks': 1, 'space': 14}]},
  {'keep': True, 'text': 'A temple trust wants to reduce crowding at its free-meal counter. After watching the counter for a week, the team writes thirty different ideas on sticky notes '
           '(a token system, two counters, a one-way queue&hellip;) and announces: <i>&ldquo;Define is done.&rdquo;</i>', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'Name the phase the team is really in, and say whether it is diverging or converging.', 'marks': 1, 'space': 14},
             {'label': '(b)', 'text': 'Explain what Define should have ended with, and why the team needs it before listing ideas.', 'marks': 2, 'space': 30}]},
  {'keep': True, 'text': 'For each fix to the canteen order form, write <b>UI</b> or <b>UX</b> and give a reason of no more than ten words.', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'Add &ldquo;Step 2 of 4&rdquo; and a progress bar to the form.', 'marks': 1, 'space': 14},
             {'label': '(b)', 'text': 'Change the form text from 12 px to 16 px.', 'marks': 1, 'space': 14},
             {'label': '(c)', 'text': 'Let a student repeat last week&rsquo;s lunch order with one tap.', 'marks': 1, 'space': 14}]},

  {'section': 'Section 2 — work it out',
   'text': 'Three colour samples for the canteen app. L is relative luminance; the text colour and the background colour are printed with their L values.',
   'marks': 5, 'flow': Art(33, swatch_fn([C_S1, C_S2, C_S3], label_style='C')),
   'parts': [{'label': '(a)', 'text': 'Calculate the contrast ratio for each of the three samples.', 'marks': 3, 'space': 40},
             {'label': '(b)', 'text': 'State which sample fails for 16 px body text but would be allowed for a 32 px heading.', 'marks': 1, 'space': 16},
             {'label': '(c)', 'text': 'A student says: &ldquo;Sample ii looks perfectly clear on my phone, so it passes.&rdquo; Give a one-sentence reply.', 'marks': 1, 'space': 20}]},
  {'text': 'A designer sets up a <b>4-column</b> layout grid on a phone frame <b>360 px</b> wide, with a margin of <b>16 px</b> at each side and a gutter of <b>8 px</b> '
           'between neighbouring columns. Figma shares the space that is left equally between the four columns.', 'marks': 5,
   'flow': Art(64, figma_grid_fn()),
   'parts': [{'label': '(a)', 'text': 'Calculate the width of one column.', 'marks': 2, 'space': 26},
             {'label': '(b)', 'text': 'A card spans columns 1 and 2. Calculate its width.', 'marks': 1, 'space': 20},
             {'label': '(c)', 'text': 'Calculate the X position where column 3 starts.', 'marks': 2, 'space': 24}]},

  {'section': 'Section 3 — judge the design',
   'text': 'Tanvi draws first wireframes for the canteen&rsquo;s website. Her brief: the same navigation at the top of every page; exactly one heading per page, before the content; '
           'a form on Contact only; a button on Home after its heading; every page ends with its footer. Her drawings contain <b>four</b> mistakes against that brief. '
           'For each, name the page and say which part of the brief is broken.',
   'marks': 4, 'flow': Art(70, flawed_wf_fn()), 'space': 46},
  {'text': 'Before the first meeting, Farhan spends a week turning his wireframe into a finished-looking design with the canteen&rsquo;s orange, real photographs of dosa and a custom font. '
           'The principal spends the whole meeting arguing about the shade of orange and never notices that the Home page has no way to reach the menu.', 'marks': 3,
   'parts': [{'label': '(a)', 'text': 'Name the mistake in Farhan&rsquo;s approach.', 'marks': 1, 'space': 14},
             {'label': '(b)', 'text': 'Explain how it caused what happened in the meeting.', 'marks': 1, 'space': 22},
             {'label': '(c)', 'text': 'State what he should have shown instead.', 'marks': 1, 'space': 16}]},
  {'text': 'A school runs a bus for <b>36 families</b>. In a survey, <b>27</b> parents said they wait at the gate for the bus, that the wait averages <b>18 minutes</b>, '
           'and that the bus is anything from <b>10 to 25 minutes</b> late. Write <b>one sentence</b>, a problem statement for the Define phase. It must say who is affected, '
           'what goes wrong and why it matters, use one figure from the research, and suggest no solution.', 'marks': 3, 'space': 42},
 ]}

# ------------------------------------------------------------------ Paper D (railway club / canteen journeys)
D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC, 'endnote': ENDNOTE,
 'questions': [
  {'section': 'Section 1 — structure and process',
   'text': 'The Railway Club website has three pages: Home, About and Contact. The navigation on every page links to every other page. The club now adds a fourth page, <b>Gallery</b>.',
   'marks': 4,
   'parts': [{'label': '(a)', 'text': 'In the box, sketch a sitemap for the four-page site, with Home at the top. Show how the pages connect.', 'marks': 2,
              'flow': Art(40, box_fn('SITEMAP', 40), w=AVAIL - 16)},
             {'label': '(b)', 'text': 'Calculate the total number of navigation links between pages before Gallery was added, and after.', 'marks': 2, 'space': 26}]},
  {'text': 'Three entries from a design team&rsquo;s diary.', 'marks': 3,
   'flow': hang([('P', 'Week 2. The team groups fifty interview notes into four themes and finds one pain that keeps repeating.'),
                 ('Q', 'Week 4. The team draws three different layouts and tests each with five users.'),
                 ('R', 'Week 7. Testing shows the chosen design works well, but users say it solves a problem they never had: the team had misread its own notes. They rewrite the problem statement.')], label_w=18),
   'parts': [{'label': '(a)', 'text': 'Name the phase of the double diamond that entry <b>P</b> belongs to.', 'marks': 1, 'space': 12},
             {'label': '(b)', 'text': 'Name the phase that entry <b>Q</b> belongs to.', 'marks': 1, 'space': 12},
             {'label': '(c)', 'text': 'In entry <b>R</b> the team goes back. Name the phase they return to.', 'marks': 1, 'space': 12}]},
  {'text': 'A booking app has a white label on a green button. The green has relative luminance <b>L = 0.25</b>; white has L = 1.00.', 'marks': 3,
   'flow': Art(30, sizes_fn(D_S1)),
   'parts': [{'label': '(a)', 'text': 'Calculate the contrast ratio of the label.', 'marks': 1, 'space': 20},
             {'label': '(b)', 'text': 'The designer tries three labels: <b>16 px regular</b>, <b>20 px bold</b> and <b>24 px regular</b>. State which of them pass, and why.', 'marks': 2, 'space': 32}]},

  {'section': 'Section 2 — numbers and users',
   'text': 'A frame is <b>390 px wide and 844 px high</b>. A header occupies Y = 0 to Y = 96. A bottom tab bar is <b>72 px</b> high and sits flush with the bottom edge. '
           'Between them is a list of rows, each <b>64 px</b> high with no gaps, starting at <b>Y = 96</b>.', 'marks': 5, 'flow': Art(52, figma_tab_fn()),
   'parts': [{'label': '(a)', 'text': 'Calculate the Y position of the top edge of the tab bar.', 'marks': 1, 'space': 16},
             {'label': '(b)', 'text': 'Calculate how many whole rows fit between the header and the tab bar, and how many px are left over.', 'marks': 2, 'space': 30},
             {'label': '(c)', 'text': 'Each row is a component instance. The designer edits the main component so each row is <b>72 px</b> high. State how many whole rows now fit, and which instances change.', 'marks': 2, 'space': 30}]},
  {'text': 'Diya orders lunch on her family&rsquo;s shared tablet, and the canteen app logs her out every time. Her journey is scored from 1 (miserable) to 5 (delighted). '
           'Two teams each make one change. Team A polishes the screens. Team B changes how signing in works.', 'marks': 5,
   'flow': grid2([['', '1 Welcome', '2 Choose food', '3 Sign in', '4 Pay', '5 Order number'],
                  ['Before'] + [str(v) for v in CALC['D_before']],
                  ['Fix A'] + [str(v) for v in CALC['D_fixA']],
                  ['Fix B'] + [str(v) for v in CALC['D_fixB']]],
                 [AVAIL * 0.14] + [AVAIL * 0.172] * 5, blank_h=6 * mm, fs=10, hfs=8, center_from=1),
   'parts': [{'label': '(a)', 'text': 'Calculate the average score before, after Fix A and after Fix B.', 'marks': 2, 'space': 28},
             {'label': '(b)', 'text': 'State the lowest point before either fix, and whether Fix A changes it.', 'marks': 1, 'space': 18},
             {'label': '(c)', 'text': 'Fix A has the higher average. Explain why Fix B is still the better fix.', 'marks': 2, 'space': 30}]},

  {'section': 'Section 3 — handover and diagnosis',
   'text': 'Farhan has finished the Railway Club wireframes. He emails the three images to his friend Kabir, who will build the site, and sends nothing else. '
           'List <b>four</b> things Kabir cannot guess from the images alone and would have to ask about.', 'marks': 4, 'space': 46},
  {'text': 'Another student, Rohan, has answered two questions on this topic. Both answers are wrong. For each one, state the mistake and write out a correct version, '
           'giving a reason or example that would convince him.', 'marks': 6,
   'flow': Art(58, notebook_fn(58, "ROHAN'S ANSWERS", [
       ('(i)', '\u201cUX is how the app looks and UI is how it works. So changing the Pay button from grey to green is a UX fix.\u201d'),
       ('(ii)', '\u201cOur form shows a mistake by turning the box red, so every user can see which box to fix.\u201d')])),
   'parts': [{'label': '(i)', 'text': 'Diagnose and correct the first answer.', 'marks': 3, 'space': 40},
             {'label': '(ii)', 'text': 'Diagnose and correct the second answer.', 'marks': 3, 'space': 40}],
   'tip': 'Each answer has more than one thing wrong with it. Deal with them separately.'},
 ]}

PAPERS = [('a', A), ('b', B), ('c', C), ('d', D)]

# =====================================================================================
#  6. MARK SCHEMES — one `lines` entry per mark, each carrying exactly one [1]
# =====================================================================================
M = ' <b>[1]</b>'
SCHEMES = [
 {'title': 'Paper A — Medium', 'meta': '30 marks', 'questions': [
  {'n': '1', 'marks': 4, 'lines': [
     '(a) <b>Discover</b>, then <b>Define</b>, in the first diamond' + M,
     '(a) <b>Develop</b>, then <b>Deliver</b>, in the second diamond' + M,
     '(b) <b>diverge, converge, diverge, converge</b>, left to right' + M,
     '(c) <b>one clearly defined problem</b> (a problem statement)' + M],
   'note': 'The usual slip is Define and Develop swapped, because both sound like making things. Award the two phase-name marks only if the order is right from left to right. '
           'A student who writes &ldquo;the answer&rdquo; or &ldquo;a solution&rdquo; for (c) has described the end of the second diamond; no mark.'},
  {'n': '2', 'marks': 4, 'lines': [
     'Watch six students&hellip; = <b>Discover</b>' + M, 'One sentence about late returns = <b>Define</b>' + M,
     'Sketch eight different ways = <b>Develop</b>' + M, 'Release and track for a month = <b>Deliver</b>' + M],
   'note': 'The trap pair is Define and Develop. A sentence that names the problem is Define; sketching eight options is Develop. If a student writes Develop for the one-sentence card, '
           'give nothing for either of those two rows: they have not separated the problem from the answer.'},
  {'n': '3', 'marks': 3, 'lines': [
     '(a) <b>UI</b>: darker text changes how the screen looks (colour and contrast)' + M,
     '(b) <b>UX</b>: fewer taps changes how the task goes' + M,
     '(c) <b>UX</b>: it is feedback, telling the user the tap worked' + M],
   'note': 'Part (c) catches &ldquo;I can see it, so it is UI&rdquo;. A message is something you see, but its job is to say the tap worked, which is UX. '
           'Each mark needs the label <i>and</i> a reason; a bare label scores nothing.'},
  {'n': '4', 'marks': 4, 'lines': [
     '(a) (1 + 0.05) &divide; (0.10 + 0.05) = 1.05 &divide; 0.15 = <b>%s</b>' % fr(CALC['A_r1']) + M,
     '(b) 1.05 &divide; (0.25 + 0.05) = 1.05 &divide; 0.30 = <b>%s</b>' % fr(CALC['A_r2']) + M,
     '(c) <b>Sample A</b>: %s is at least 4.5; sample B at %s is below it' % (fr(CALC['A_r1']), fr(CALC['A_r2'])) + M,
     '(d) <b>Yes</b>: 28 px is large text, and %s is at least 3' % fr(CALC['A_r2']) + M],
   'note': 'Leaving out the + 0.05 on both parts gives 1 &divide; 0.10 = 10 and 1 &divide; 0.25 = 4, and 4 looks like &ldquo;nearly passes&rdquo;. '
           'Give no mark for (a) or (b) without the 0.05s, then mark (c) and (d) as follow-through on the student&rsquo;s own figures.'},
  {'n': '5', 'marks': 3, 'lines': [
     '(a) (48 &minus; 32) &divide; 2 = <b>%s px</b> each side' % n(CALC['A_pad_w']) + M,
     '(b) (48 &minus; 28) &divide; 2 = <b>%s px</b> each side' % n(CALC['A_pad_h']) + M,
     '(c) <b>%d wide and %d high</b>: it does <b>not</b> meet 48 &times; 48' % (CALC['A_new_w'], CALC['A_new_h']) + M],
   'note': 'Answers of 16 and 20 mean the extra was not halved: padding goes on two sides. In (c) 4 px on each side adds 8 to each measurement, not 4; '
           'a student who writes 36 and 32 has added 4 once.'},
  {'n': '6', 'marks': 4, 'lines': [
     '(a) X = (390 &minus; 342) &divide; 2 = <b>%s</b>' % n(CALC['A_X']) + M,
     '(b) Each step down is 96 + 24 = %d' % CALC['A_step'] + M,
     '(b) Y = 88 + 2 &times; %d = <b>%d</b>' % (CALC['A_step'], CALC['A_Y3']) + M,
     '(c) Bottom of card 3 = %d + 96 = %d; 844 &minus; %d = <b>%d px</b>' % (CALC['A_Y3'], CALC['A_bot3'], CALC['A_bot3'], CALC['A_below']) + M],
   'note': 'Three wrong methods, each visibly wrong against the diagram: 88 + 2 &times; 96 = %d (forgot the gaps), 88 + 3 &times; %d = %d (three steps down, but card 3 is only two steps below card 1), '
           'and 844 &minus; %d = %d (measured from the top of card 3, not its bottom).' % (CALC['A_w_forgot_gaps'], CALC['A_step'], CALC['A_w_three_steps'], CALC['A_Y3'], CALC['A_w_from_top'])},
  {'n': '7', 'marks': 4, 'lines': [
     '(a) First inconsistency, read from the picture (see note)' + M,
     '(a) A second, <b>different</b> inconsistency' + M,
     '(b) Red alone fails for users who cannot tell red from other colours, in bright sunlight, or on a screen reader' + M,
     '(b) Fix: an <b>icon and a message</b> under the box saying what to fix' + M],
   'note': 'Real differences in Figure 1: shape (Log in is a pill, Sign up is square, Guest is slightly rounded); colour (blue, green, grey); height (the three buttons are three different heights); '
           'capitals (CONTINUE AS GUEST). Two answers about the same property, such as blue and green, are one answer. &ldquo;Make the red darker&rdquo; is still colour alone: no mark for the fix.'},
  {'n': '8', 'marks': 4, 'lines': [
     'A <b>navigation bar</b> across the top of the frame' + M,
     'Exactly <b>one heading</b>, placed before the content' + M,
     'One <b>button</b> with a verb label (Renew, Search), not &ldquo;Click here&rdquo; or &ldquo;Submit&rdquo;' + M,
     'A <b>footer</b> as the last box on the page' + M],
   'note': 'Any colour fill, shading, real picture or drawn-in artwork caps the question at 3: this is the over-polished-wireframe trap, and the question tells him so twice. '
           'Unlabelled boxes cannot be marked; a box has to say what it is.'},
 ]},

 {'title': 'Paper B — Medium', 'meta': '30 marks', 'questions': [
  {'n': '1', 'marks': 4, 'lines': [
     '(a) <b>No opening up and narrowing</b>: every phase is drawn the same, as one run, with no diamond shape' + M,
     '(a) <b>No way back</b>: arrows only go forwards, but a test result can send the team to an earlier phase' + M,
     '(b) <b>Two diamonds</b> side by side, each opening up then narrowing, with the four phases named in order' + M,
     '(b) A <b>backward arrow</b> from a late phase to an earlier one' + M],
   'note': 'The straight line is the commonest wrong picture of the double diamond. Credit (a) only for the two ideas, shape and loop-back; &ldquo;it is too simple&rdquo; or '
           '&ldquo;it has no colours&rdquo; earns nothing. Both parts (b) marks can be earned even if (a) was weak.'},
  {'n': '2', 'marks': 3, 'lines': [
     'Sketch six different ways = <b>Develop</b>' + M,
     'The &ldquo;Commuters miss trains because&hellip;&rdquo; sentence = <b>Define</b>' + M,
     'Group forty notes into three themes, then pick one = <b>Define</b>' + M],
   'note': 'Rows 1 and 2 are the classic swap. The sentence names a problem; sketching six ways is a solution. Row 3 narrows towards a problem, which is why a student who '
           'thinks &ldquo;Define is about ideas&rdquo; gets it wrong too.'},
  {'n': '3', 'marks': 3, 'lines': [
     '(a) <b>(ii)</b>, the blue Book button: it changes how the screen looks' + M,
     '(b) (i) is UX: one screen instead of three changes how the task <b>goes</b>' + M,
     '(b) (iii) is UX: the spinner is <b>feedback</b>, telling the user the tap worked; it is seen, but its job is the experience' + M],
   'note': 'The student in the question uses &ldquo;you can see it&rdquo; as the test, which is the wrong test: judge a change by what it is <i>for</i>. The spinner is the case that exposes it. '
           'Do not accept &ldquo;(iii) is UI because it is a picture&rdquo;.'},
  {'n': '4', 'marks': 5, 'lines': [
     '(a) (0.35 + 0.05) &divide; (0.05 + 0.05) = 0.40 &divide; 0.10 = <b>%s</b>' % fr(CALC['B_r1']) + M,
     '(b) (1 + 0.05) &divide; (0.15 + 0.05) = 1.05 &divide; 0.20 = <b>%s</b>' % fr(CALC['B_r2']) + M,
     '(c) Button 1 <b>fails</b> and button 2 <b>passes</b>' + M,
     '(c) Both are compared with <b>4.5</b>, because 16 px regular is not large text' + M,
     '(d) %s is below 4.5, so it fails: a minimum is a minimum, and text just under it is hard to read for people with weaker sight' % fr(CALC['B_r1']) + M],
   'note': 'Leaving out the + 0.05 gives 0.35 &divide; 0.05 = %s for button 1, which would <i>pass</i>: the wrong method turns a fail into a pass, so check the working before the verdict. '
           'Mark (c) as follow-through if a ratio was wrong, but only with the 4.5 stated.' % n(CALC['B_no_plus'])},
  {'n': '5', 'marks': 3, 'lines': [
     '(a) 6 &times; 44 = %d' % (6 * 44) + M,
     '(a) 5 gaps &times; 12 = %d, so the total is <b>%d px</b> (fits in 328)' % (5 * 12, CALC['B_six']) + M,
     '(b) 7 &times; 44 + 6 &times; 12 = <b>%d px</b>, which is more than 328: no' % CALC['B_seven'] + M],
   'note': 'Six gaps instead of five gives %d, more than 328, and wrongly says six buttons do not fit. n buttons have n &minus; 1 gaps; a student who draws six buttons will see it.' % CALC['B_six_wrong']},
  {'n': '6', 'marks': 3, 'lines': [
     '(a) Row 5 is four rows below row 1' + M,
     '(a) Y = 72 + 4 &times; 56 = <b>%d</b>' % CALC['B_Y5'] + M,
     '(b) (844 &minus; 72) &divide; 56 = 772 &divide; 56 = %s, so <b>%d whole rows</b>' % (fr(CALC['B_fit_exact']), CALC['B_fit']) + M],
   'note': '72 + 5 &times; 56 = %d is the Y of row 6. Rounding 13.8 up to 14 counts a row that is cut off by the bottom of the frame; the question says <i>whole</i> rows.' % CALC['B_Y5_wrong']},
  {'n': '7', 'marks': 4, 'lines': [
     '(a) <b>Step 4, Passenger details</b> (score 1)' + M,
     '(b) (5 + 4 + 2 + 1 + 4 + 5) &divide; 6 = %d &divide; 6 = <b>%s</b>' % (sum(CALC['B_scores']), fr(CALC['B_avg'])) + M,
     '(c) A UX fix that changes the task, e.g. save family members so their details fill in automatically' + M,
     '(d) A detail <i>with the decision it changes</i>: slow data (light pages, save progress), or cracked screen and one finger (big targets, few fields)' + M],
   'note': 'Yellow is the decoy: a detail belongs on a persona only if it changes a decision, and nothing depends on a favourite colour. A student who divides %d by 5 steps and gets %s '
           'has miscounted: the table has six. A UI fix in (c), such as a bigger font, does not score.' % (sum(CALC['B_scores']), fr(CALC['B_avg_wrong']))},
  {'n': '8', 'marks': 5, 'lines': [
     '<b>Same navigation, same place</b>, on all three pages' + M,
     'Exactly <b>one heading</b> per page, before the content' + M,
     '<b>Home</b> has a button after its heading' + M,
     '<b>Contact</b> has a form with two fields and a button, and no other page has a form' + M,
     'A <b>footer</b> that is the last box on every page' + M],
   'note': 'These are the five rules of the page&rsquo;s wireframe studio; mark them rule by rule from the frames. A nav bar that moves between pages fails mark 1 even if it is at the top '
           'on two of them. Any colour, shading or real picture caps the question at 4: that is the polished-too-early trap.'},
 ]},

 {'title': 'Paper C — Hard', 'meta': '30 marks', 'questions': [
  {'n': '1', 'marks': 4, 'lines': [
     '(a) <b>Discover</b>, then <b>Define</b>, in the first diamond' + M,
     '(a) <b>Develop</b>, then <b>Deliver</b>, in the second diamond' + M,
     '(b) <b>diverge, converge, diverge, converge</b>, left to right' + M,
     '(c) An arrow from the end back to <b>Discover</b>: the cause is new evidence nobody had gathered' + M],
   'note': '&ldquo;Define&rdquo; alone earns no mark in (c): a team cannot rewrite a problem it has not yet researched, and the question says the cause was never researched. '
           'Accept Define only if the student draws the arrow to Discover first. A straight arrow forward is the straight-line trap in another form.'},
  {'n': '2', 'marks': 3, 'lines': [
     '(a) <b>Develop</b>, and <b>diverging</b> (many ideas for a solution)' + M,
     '(b) Define should have ended with <b>one clear problem statement</b>' + M,
     '(b) Without it there is no way to choose among the thirty ideas, or they may all solve the wrong problem' + M],
   'note': 'The trap is that both phases start with D and both feel like making things. Thirty ideas open the options up, so it cannot be Define, which narrows. '
           '&ldquo;They are in Define because they are choosing&rdquo; gets nothing for (a). Reasons about time or tidiness in (b) do not score.'},
  {'n': '3', 'marks': 3, 'lines': [
     '(a) <b>UX</b>: it shows how far and how much is left, which changes whether people finish' + M,
     '(b) <b>UI</b>: text size is typography, a change to how it looks' + M,
     '(c) <b>UX</b>: one tap instead of a whole order changes how the task goes' + M],
   'note': 'A progress bar looks like decoration, so students write UI. Each mark needs the label and a reason that names the task; &ldquo;UX because it helps people&rdquo; is too vague. '
           'Part (b) is the control: a bigger font is genuinely UI, so a student who writes UX for everything has not learnt the test.'},
  {'n': '4', 'marks': 5, 'lines': [
     '(a) (0.45 + 0.05) &divide; (0.05 + 0.05) = 0.50 &divide; 0.10 = <b>%s</b>' % fr(CALC['C_r1']) + M,
     '(a) (0.30 + 0.05) &divide; (0.05 + 0.05) = 0.35 &divide; 0.10 = <b>%s</b>' % fr(CALC['C_r2']) + M,
     '(a) (0.85 + 0.05) &divide; (0.10 + 0.05) = 0.90 &divide; 0.15 = <b>%s</b>' % fr(CALC['C_r3']) + M,
     '(b) <b>Sample ii</b>: %s is below 4.5 but at least 3' % fr(CALC['C_r2']) + M,
     '(c) Looking clear is not a measurement: screens, sunlight and eyes differ, so the ratio decides' + M],
   'note': 'The lighter colour goes on top. In sample i the <i>text</i> is the lighter colour; a student who always puts the background on top gets 0.10 &divide; 0.50 = 0.2, '
           'an impossible ratio (a ratio is never below 1), so point that out rather than only marking it wrong. Samples i and iii pass; only ii sits between 3 and 4.5.'},
  {'n': '5', 'marks': 5, 'lines': [
     '(a) Usable width = 360 &minus; 2 &times; 16 = %d' % CALC['C_usable'] + M,
     '(a) 3 gutters &times; 8 = 24; (%d &minus; 24) &divide; 4 = <b>%s px</b>' % (CALC['C_usable'], n(CALC['C_col'])) + M,
     '(b) 2 &times; %s + 8 = <b>%s px</b>' % (n(CALC['C_col']), n(CALC['C_span2'])) + M,
     '(c) Column 3 starts after two columns and two gutters: 16 + 2 &times; (%s + 8)' % n(CALC['C_col']) + M,
     '(c) = <b>%s px</b>' % n(CALC['C_X3']) + M],
   'note': 'Three visible slips: %d &divide; 4 = %s (ignores the gutters), 2 &times; %s = %s (a two-column card spans one gutter), and 16 + 2 &times; %s = %s (forgets the two gutters before column 3). '
           'Check: two 2-column cards, %s + 8 + %s = %d, fill the usable width exactly.' % (
               CALC['C_usable'], n(CALC['C_col_wrong']), n(CALC['C_col']), n(CALC['C_span_wrong']), n(CALC['C_col']), n(CALC['C_X3_wrong']),
               n(CALC['C_span2']), n(CALC['C_span2']), CALC['C_usable'])},
  {'n': '6', 'marks': 4, 'lines': [
     '<b>Home</b>: no button after the heading (Home must have a call to action)' + M,
     '<b>About</b>: no navigation (same navigation at the top of every page)' + M,
     '<b>About</b>: two headings (exactly one per page)' + M,
     '<b>Contact</b>: a paragraph after the footer, so the footer is not last' + M],
   'note': 'Each flag needs the page <i>and</i> the rule. Home&rsquo;s navigation and heading are fine, and Contact is where the form belongs: a student who flags the form or the image box has flagged '
           'correct things, and earns nothing for them. About&rsquo;s two faults are separate marks.'},
  {'n': '7', 'marks': 3, 'lines': [
     '(a) <b>Polishing the wireframe too early</b>' + M,
     '(b) Colour and photographs pulled attention to decoration, so people argued about the shade and missed the missing structure' + M,
     '(c) A <b>low-fidelity wireframe</b>: grey boxes and labels, so feedback is about layout and flow' + M],
   'note': 'The effort is not the mistake; the timing and the fidelity are. &ldquo;He should have worked less&rdquo; or &ldquo;he should have asked first&rdquo; earns nothing. '
           'The missing route to the menu is the proof for (b): a plain wireframe would have made the gap the only thing to look at.'},
  {'n': '8', 'marks': 3, 'lines': [
     '<b>Who</b> is affected (the parents of the bus families, not &ldquo;everyone&rdquo;) and <b>what goes wrong</b> in plain words' + M,
     'Uses a figure from the research <b>correctly</b>: 27 of 36 (%s%%), 18 minutes, or 10 to 25 minutes late' % n(CALC['C_pct']) + M,
     'Says <b>why it matters</b>, and contains <b>no solution</b>' + M],
   'note': 'Model: <i>&ldquo;Parents of the bus families, 27 of 36 of them, wait about 18 minutes at the gate because the bus is 10 to 25 minutes late, so they lose working time and children wait outside.&rdquo;</i> '
           'Any solution word (app, tracker, SMS, GPS, &ldquo;should build&rdquo;) loses the third mark whatever else the sentence says. 27 &divide; 36 = 0.75, so 75%; 27% or 36% means the two figures were swapped.'},
 ]},

 {'title': 'Paper D — Hard', 'meta': '30 marks', 'questions': [
  {'n': '1', 'marks': 4, 'lines': [
     '(a) A box for <b>each of the four pages</b>, Home at the top, joined to the others' + M,
     '(a) The links or a note showing the navigation connects <b>every page to every other page</b>' + M,
     '(b) Before: 3 pages &times; 2 other pages = <b>%d links</b>' % CALC['D_links3'] + M,
     '(b) After: 4 pages &times; 3 other pages = <b>%d links</b>' % CALC['D_links4'] + M],
   'note': '4 &times; 4 = %d counts every page linking to itself, which nobody needs. Notice that one new page adds %d links, not one: every old page needs a link to it, and it needs links to all three. '
           'A sitemap drawn as a tree with Home above three boxes earns the first mark; the second needs the all-to-all idea shown somewhere.' % (CALC['D_links_wrong'], CALC['D_added'])},
  {'n': '2', 'marks': 3, 'lines': [
     '(a) <b>Define</b>: grouping the notes to find the pattern narrows' + M,
     '(b) <b>Develop</b>: drawing and testing different layouts keeps the options open' + M,
     '(c) <b>Define</b>: the problem statement has to be rewritten' + M],
   'note': 'Part (c) is the loop-back. The team has the facts and has a design that works; what is wrong is the problem statement, so they go back to Define. Discover is wrong because they already '
           'have the evidence, and Develop is wrong because they have a good design for the wrong problem.'},
  {'n': '3', 'marks': 3, 'lines': [
     '(a) (1 + 0.05) &divide; (0.25 + 0.05) = 1.05 &divide; 0.30 = <b>%s</b>' % fr(CALC['D_r']) + M,
     '(b) <b>16 px regular fails</b>: %s is below 4.5 and 16 px is not large text' % fr(CALC['D_r']) + M,
     '(b) <b>20 px bold and 24 px regular both pass</b>: bold from 18.66 px, or any text from 24 px, counts as large, and %s is at least 3' % fr(CALC['D_r']) + M],
   'note': 'The hard paper gives no thresholds, so this tests recall. Students who remember 24 px but not 18.66 px bold will say 20 px bold fails: award the third mark only if both passes are named.'},
  {'n': '4', 'marks': 5, 'lines': [
     '(a) 844 &minus; 72 = <b>Y = %d</b>' % CALC['D_tab_Y'] + M,
     '(b) Rows fill Y = 96 to Y = %d: %d px; %d &divide; 64 = %s, so <b>%d whole rows</b>' % (CALC['D_tab_Y'], CALC['D_area'], CALC['D_area'], fr(CALC['D_rows_exact']), CALC['D_rows']) + M,
     '(b) Left over: %d &minus; %d &times; 64 = <b>%d px</b>' % (CALC['D_area'], CALC['D_rows'], CALC['D_left']) + M,
     '(c) %d &divide; 72 = %s, so <b>%d whole rows</b> now fit' % (CALC['D_area'], fr(CALC['D_rows72_exact']), CALC['D_rows72']) + M,
     '(c) <b>All of the instances</b> change, because editing the main component updates every instance' + M],
   'note': 'Dividing (844 &minus; 96) &divide; 64 gives %d rows: the tab bar was forgotten, and the last row would sit underneath it. Rounding %s up to %d keeps a row that is cut off. '
           'In (c) a student who says only one instance changes has copied rectangles; that is the exact mistake components exist to prevent.' % (
               CALC['D_rows_forgot_tab'], fr(CALC['D_rows72_exact']), CALC['D_rows72'] + 1)},
  {'n': '5', 'marks': 5, 'lines': [
     '(a) Before: %d &divide; 5 = <b>%s</b>' % (sum(CALC['D_before']), fr(CALC['D_avg_before'])) + M,
     '(a) Fix A: %d &divide; 5 = <b>%s</b>; Fix B: %d &divide; 5 = <b>%s</b>' % (sum(CALC['D_fixA']), fr(CALC['D_avg_A']), sum(CALC['D_fixB']), fr(CALC['D_avg_B'])) + M,
     '(b) <b>Step 3, Sign in</b>, scoring 1; Fix A <b>leaves it at 1</b>' + M,
     '(c) Fix B lifts the lowest point from 1 to 3' + M,
     '(c) An average can rise while the one step that makes people quit stays broken: anyone who stalls at sign-in never reaches the steps Fix A improved' + M],
   'note': 'The question is built so the higher average (%s against %s) points at the worse fix. The lowest point is where you fix first; the average hides it. '
           'A student who picks A because %s is bigger than %s has used the average and should see the sign-in score of 1 before the explanation.' % (
               fr(CALC['D_avg_A']), fr(CALC['D_avg_B']), fr(CALC['D_avg_A']), fr(CALC['D_avg_B']))},
  {'n': '6', 'marks': 4, 'lines': [
     'The <b>page list and file names</b> (index.html, about.html, contact.html)' + M,
     'Where <b>each navigation link</b> goes' + M,
     'The <b>frame size</b> the pages were designed at, e.g. 390 &times; 844' + M,
     'Which text is <b>placeholder</b> and which is final, <b>or</b> what each image should show, <b>or</b> the order of blocks on each page' + M],
   'note': 'Accept any four <i>different</i> items from: page list and file names; where each link goes; the frame size; the order of blocks on each page; which text is placeholder; what each image '
           'should show. Not accepted: colours and fonts (a low-fidelity wireframe has none, deliberately) or &ldquo;how to code it&rdquo;, which is Kabir&rsquo;s job.'},
  {'n': '7', 'marks': 6, 'lines': [
     '(i) The mistake: <b>UI and UX are swapped</b>' + M,
     '(i) Correct: <b>UI is what you see and touch; UX is how the whole thing works and feels</b>' + M,
     '(i) Applied: changing a button&rsquo;s colour changes how the screen looks, so it is a <b>UI</b> fix' + M,
     '(ii) The mistake: <b>colour is the only signal</b>' + M,
     '(ii) Correct: show it in red <b>and</b> with an icon and a message saying what to fix' + M,
     '(ii) A reason: some users cannot tell red from other colours (about 1 in 12 men), screens wash out in sunlight, screen readers do not see colour' + M],
   'note': 'Both statements are the page&rsquo;s named traps, so the diagnosis has to be specific. In (i) the conclusion is also wrong, and a student who corrects the definition but keeps '
           '&ldquo;UX fix&rdquo; has not finished: give the third mark only for applying the corrected idea. In (ii) &ldquo;use a brighter red&rdquo; is still colour alone, so no mark for the correction. '
           'Marking rubric for each: names the error [1], writes a correct version [1], gives a reason or test that would convince Rohan [1].'},
 ]},
]


# =====================================================================================
#  7. VERIFY — marks, parts, [1] tags, and a second derivation of every number
# =====================================================================================
def _verify():
    # --- marks and parts
    for code, spec in PAPERS:
        tot = 0
        for i, q in enumerate(spec['questions'], 1):
            assert q.get('marks'), (code, i)
            if q.get('parts'):
                ps = sum(p['marks'] for p in q['parts'])
                assert ps == q['marks'], (code, i, ps, q['marks'])
            tot += q['marks']
        assert tot == 30, (code, tot)
        assert len(spec['questions']) == len(SCHEMES[ord(code) - 97]['questions']), code
        # three named sections, in order
        secs = [q['section'] for q in spec['questions'] if q.get('section')]
        assert len(secs) == 3, (code, secs)
    # --- schemes: marks match the paper, one [1] per line, one line per mark, a note on every question
    for (code, spec), sc in zip(PAPERS, SCHEMES):
        tot = 0
        for q, sq in zip(spec['questions'], sc['questions']):
            assert sq['marks'] == q['marks'], (code, sq['n'])
            assert len(sq['lines']) == sq['marks'], (code, sq['n'], len(sq['lines']))
            for ln in sq['lines']:
                assert ln.count('[1]') == 1, (code, sq['n'], ln)
            assert sq.get('note'), (code, sq['n'])
            tot += sq['marks']
        assert tot == 30, code
    # --- second derivation of every number (floats / different arithmetic), compared to CALC
    close = lambda a, b: abs(float(a) - float(b)) < 1e-9
    assert close(CALC['A_r1'], 1.05 / 0.15) and close(CALC['A_r2'], 1.05 / 0.30)
    assert (48 - 32) / 2 == CALC['A_pad_w'] == 8 and (48 - 28) / 2 == CALC['A_pad_h'] == 10
    assert (CALC['A_new_w'], CALC['A_new_h']) == (40, 36) and not (40 >= 48 and 36 >= 48)
    assert CALC['A_X'] == 24 and 24 + 342 + 24 == 390                      # centred: equal margins
    assert [88 + i * 120 for i in range(3)] == [88, 208, 328] and CALC['A_Y3'] == 328
    assert CALC['A_bot3'] == 424 and CALC['A_below'] == 420
    assert len({CALC['A_Y3'], CALC['A_w_forgot_gaps'], CALC['A_w_three_steps']}) == 3          # wrong methods all differ
    assert 328 + 2 * 24 + 0 > 0
    assert close(CALC['B_r1'], 0.40 / 0.10) and close(CALC['B_r2'], 1.05 / 0.20)
    assert B_S1.pass_ord is False and B_S2.pass_ord is True
    assert CALC['B_six'] == 324 <= 328 < CALC['B_six_wrong'] == 336 and CALC['B_seven'] == 380 > 328
    assert [72 + 56 * i for i in range(5)][-1] == CALC['B_Y5'] == 296 and CALC['B_Y5_wrong'] == 352
    assert CALC['B_fit'] == 13 and 13 * 56 + 72 <= 844 < 14 * 56 + 72
    assert sum(CALC['B_scores']) == 21 and close(CALC['B_avg'], 3.5) and min(CALC['B_scores']) == 1
    assert CALC['B_scores'].count(1) == 1                                        # a single lowest point, no tie
    assert close(CALC['B_no_plus'], 7.0)
    assert (CALC['C_r1'], CALC['C_r2'], CALC['C_r3']) == (5, F(7, 2), 6)
    assert len({CALC['C_r1'], CALC['C_r2'], CALC['C_r3']}) == 3                 # no ties
    assert [s.pass_ord for s in (C_S1, C_S2, C_S3)] == [True, False, True]
    assert [s.pass_large for s in (C_S1, C_S2, C_S3)] == [True, True, True]
    assert CALC['C_col'] == 76 and 16 + 4 * 76 + 3 * 8 + 16 == 360               # the grid fills the frame exactly
    assert CALC['C_span2'] == 160 and 16 + 160 + 8 + 160 + 16 == 360
    assert CALC['C_X3'] == 184 and 16 + 76 + 8 + 76 + 8 == 184
    assert len({CALC['C_col'], CALC['C_col_wrong']}) == 2 and len({CALC['C_X3'], CALC['C_X3_wrong']}) == 2
    assert CALC['C_pct'] == 75
    assert (CALC['D_links3'], CALC['D_links4'], CALC['D_added']) == (6, 12, 6) and CALC['D_links_wrong'] == 16
    assert close(CALC['D_r'], 1.05 / 0.30) and 3 <= float(CALC['D_r']) < 4.5      # large passes, ordinary fails
    assert 18.66 <= 20 and CALC['D_tab_Y'] == 772 and CALC['D_area'] == 676
    assert (CALC['D_rows'], CALC['D_left']) == (10, 36) and 10 * 64 + 36 == 676
    assert CALC['D_rows72'] == 9 and 9 * 72 <= 676 < 10 * 72
    assert CALC['D_rows_forgot_tab'] == 11 != CALC['D_rows']
    assert (CALC['D_avg_before'], CALC['D_avg_A'], CALC['D_avg_B']) == (F(16, 5), 4, F(18, 5))
    assert len({CALC['D_avg_before'], CALC['D_avg_A'], CALC['D_avg_B']}) == 3
    assert CALC['D_avg_A'] > CALC['D_avg_B'] > CALC['D_avg_before']             # the average points the wrong way
    assert min(CALC['D_fixA']) == 1 and min(CALC['D_fixB']) == 3 and min(CALC['D_before']) == 1
    # luminance of every hex vs its printed L (done in Sw), and printed text never contradicts a verdict
    for s in (A_S1, A_S2, B_S1, B_S2, C_S1, C_S2, C_S3, D_S1):
        assert (s.pass_ord is True) == (s.true >= 4.5), s.tag
    return True


def main():
    _verify()
    files = []
    for code, spec in PAPERS:
        p = os.path.join(OUT, 'computing-uxdesign-paper-%s.pdf' % code)
        build_paper(spec, p)
        files.append(p)
    p = os.path.join(OUT, 'computing-uxdesign-answers.pdf')
    build_scheme(SCHEMES, p, {
        'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
        'meta': 'Papers A to D · 30 marks each · tutor copy',
        'intro': 'Each line is one mark, tagged [1]. On the calculation questions award method marks for the right formula and the right substitution even when the arithmetic fails. '
                 'On UI and UX questions a bare label never scores: the reason is the mark. The two mistakes this unit produces most are putting ideas in Define, and judging a fix by what '
                 'can be seen on the screen. Every note names the specific error its question was built to catch. On the sketch questions, any colour, shading or real picture caps the mark: '
                 'that is the polished-too-early trap.',
        'footer': 'Mark schemes · ' + TOPIC})
    files.append(p)
    print('\n'.join(files))


if __name__ == '__main__':
    main()
