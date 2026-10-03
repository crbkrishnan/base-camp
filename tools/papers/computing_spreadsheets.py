#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Computing, Unit 2 - Data handling in Google Sheets: four papers + one mark-scheme booklet.

Every printed sheet extract is real data, and every answer in the papers and the mark
schemes is computed here by a small independent Google-Sheets-style evaluator (class
Sheet below), never typed in from memory. Each `check(...)` compares the evaluator with
the hand-worked value the paper was designed around; a mismatch stops the build.
Ordering and filtering questions assert that no two values tie.
"""
import os, sys, re
from xml.sax.saxutils import escape
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import paper_lib as PL
from paper_lib import build_scheme, AVAIL
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether)

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Computer Science · Grade 7 · Unit 2 · Data handling in Google Sheets'
TOPIC = 'Let the Sheet Do the Work'
FOOT = 'Data handling in Google Sheets'


# =====================================================================================
#  The evaluator: a small Google-Sheets-style formula engine, independent of the page's JS
# =====================================================================================
class Err(object):
    def __init__(self, code): self.code = code
    def __repr__(self): return self.code
    def __eq__(self, o): return isinstance(o, Err) and o.code == self.code
    def __ne__(self, o): return not self.__eq__(o)
    def __hash__(self): return hash(self.code)


class ParseError(Exception):
    pass


class Rng(object):
    def __init__(self, vals): self.vals = vals


def col2n(s):
    n = 0
    for ch in s.upper():
        n = n * 26 + ord(ch) - 64
    return n


def n2col(n):
    s = ''
    while n > 0:
        n, m = divmod(n - 1, 26)
        s = chr(65 + m) + s
    return s


TOKEN_RE = re.compile(r'''\s*(?:
  (?P<num>\d+\.\d*|\.\d+|\d+) |
  (?P<str>"(?:[^"]|"")*") |
  (?P<range>\$?[A-Za-z]{1,2}\$?\d+:\$?[A-Za-z]{1,2}\$?\d+) |
  (?P<func>[A-Za-z][A-Za-z0-9_.]*(?=\s*\()) |
  (?P<cell>\$?[A-Za-z]{1,2}\$?\d+(?![A-Za-z0-9_.])) |
  (?P<name>[A-Za-z_][A-Za-z0-9_.]*) |
  (?P<op><=|>=|<>|[-+*/^&=<>(),%])
)''', re.X)


def tokenize(src):
    out, pos = [], 0
    src = src.rstrip()
    while pos < len(src):
        m = TOKEN_RE.match(src, pos)
        if not m:
            raise ParseError(src[pos:])
        pos = m.end()
        k = m.lastgroup
        out.append((k, m.group(k)))
    return out


class Parser(object):
    def __init__(self, toks): self.t = toks; self.i = 0
    def peek(self): return self.t[self.i] if self.i < len(self.t) else (None, None)
    def take(self):
        tok = self.peek(); self.i += 1; return tok
    def is_op(self, *ops):
        k, v = self.peek(); return k == 'op' and v in ops
    def parse(self):
        n = self.cmp()
        if self.i != len(self.t):
            raise ParseError('trailing')
        return n
    def cmp(self):
        n = self.cat()
        while self.is_op('=', '<>', '<', '>', '<=', '>='):
            op = self.take()[1]; n = ('bin', op, n, self.cat())
        return n
    def cat(self):
        n = self.add()
        while self.is_op('&'):
            self.take(); n = ('bin', '&', n, self.add())
        return n
    def add(self):
        n = self.mul()
        while self.is_op('+', '-'):
            op = self.take()[1]; n = ('bin', op, n, self.mul())
        return n
    def mul(self):
        n = self.pow()
        while self.is_op('*', '/'):
            op = self.take()[1]; n = ('bin', op, n, self.pow())
        return n
    def pow(self):
        n = self.unary()
        while self.is_op('^'):
            self.take(); n = ('bin', '^', n, self.unary())
        return n
    def unary(self):
        if self.is_op('-', '+'):
            op = self.take()[1]; return ('un', op, self.unary())
        n = self.prim()
        while self.is_op('%'):
            self.take(); n = ('pct', n)
        return n
    def prim(self):
        k, v = self.take()
        if k == 'num': return ('num', float(v) if '.' in v else int(v))
        if k == 'str': return ('str', v[1:-1].replace('""', '"'))
        if k == 'range':
            a, b = v.replace('$', '').split(':')
            ma = re.match(r'([A-Za-z]+)(\d+)', a); mb = re.match(r'([A-Za-z]+)(\d+)', b)
            return ('range', col2n(ma.group(1)), int(ma.group(2)), col2n(mb.group(1)), int(mb.group(2)))
        if k == 'cell':
            m = re.match(r'([A-Za-z]+)(\d+)', v.replace('$', ''))
            return ('cell', col2n(m.group(1)), int(m.group(2)))
        if k == 'name': return ('name', v)
        if k == 'func':
            if self.take() != ('op', '('): raise ParseError('(')
            args = []
            if self.is_op(')'):
                self.take(); return ('call', v.upper(), args)
            while True:
                args.append(self.cmp())
                if self.is_op(','): self.take(); continue
                if self.is_op(')'): self.take(); break
                raise ParseError('arg')
            return ('call', v.upper(), args)
        if k == 'op' and v == '(':
            n = self.cmp()
            if self.take() != ('op', ')'): raise ParseError(')')
            return n
        raise ParseError('unexpected')


def is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


class Sheet(object):
    """rows[0] is spreadsheet row 1. A str starting with '=' is a formula. None is an empty cell."""
    def __init__(self, rows, over=None):
        self.rows = [list(r) for r in rows]
        self.over = dict(over or {})
        self.cache = {}

    def with_cell(self, ref, value):
        d = dict(self.over)
        m = re.match(r'([A-Z]+)(\d+)', ref)
        d[(col2n(m.group(1)), int(m.group(2)))] = value
        return Sheet(self.rows, d)

    def raw(self, c, r):
        if (c, r) in self.over:
            return self.over[(c, r)]
        if 1 <= r <= len(self.rows) and 1 <= c <= len(self.rows[r - 1]):
            v = self.rows[r - 1][c - 1]
            return None if v == '' else v
        return None

    def cell(self, c, r):
        v = self.raw(c, r)
        if isinstance(v, str) and v.startswith('='):
            if (c, r) not in self.cache:
                self.cache[(c, r)] = self.f(v)
            return self.cache[(c, r)]
        return v

    def f(self, formula):
        try:
            src = formula[1:] if formula.startswith('=') else formula
            return self.ev(Parser(tokenize(src)).parse())
        except ParseError:
            return Err('#ERROR!')

    def a(self, ref):
        m = re.match(r'([A-Z]+)(\d+)$', ref)
        return self.cell(col2n(m.group(1)), int(m.group(2)))

    def num(self, v):
        if isinstance(v, Rng): return Err('#VALUE!')
        if isinstance(v, Err): return v
        if v is None: return 0
        if isinstance(v, bool): return int(v)
        if is_num(v): return v
        try:
            return float(str(v).strip())
        except ValueError:
            return Err('#VALUE!')

    def ev(self, n):
        t = n[0]
        if t in ('num', 'str'): return n[1]
        if t == 'name':
            u = n[1].upper()
            return True if u == 'TRUE' else False if u == 'FALSE' else Err('#NAME?')
        if t == 'cell': return self.cell(n[1], n[2])
        if t == 'range':
            _, c1, r1, c2, r2 = n
            return Rng([self.cell(c, r) for r in range(min(r1, r2), max(r1, r2) + 1)
                        for c in range(min(c1, c2), max(c1, c2) + 1)])
        if t == 'un':
            v = self.num(self.ev(n[2]))
            return v if isinstance(v, Err) else (-v if n[1] == '-' else v)
        if t == 'pct':
            v = self.num(self.ev(n[1]))
            return v if isinstance(v, Err) else v / 100.0
        if t == 'bin': return self.binop(n[1], self.ev(n[2]), self.ev(n[3]))
        if t == 'call': return self.call(n[1], n[2])
        raise ParseError('node')

    def binop(self, op, a, b):
        if op in ('+', '-', '*', '/', '^'):
            x, y = self.num(a), self.num(b)
            if isinstance(x, Err): return x
            if isinstance(y, Err): return y
            if op == '+': return x + y
            if op == '-': return x - y
            if op == '*': return x * y
            if op == '^': return x ** y
            return Err('#DIV/0!') if y == 0 else x / float(y)
        for v in (a, b):
            if isinstance(v, Err): return v
        if op == '&':
            return ('' if a is None else fmt(a)) + ('' if b is None else fmt(b))
        if a is None: a = '' if isinstance(b, str) else 0
        if b is None: b = '' if isinstance(a, str) else 0

        def rank(v): return 2 if isinstance(v, bool) else 1 if isinstance(v, str) else 0
        ka = (rank(a), a.lower() if isinstance(a, str) else a)
        kb = (rank(b), b.lower() if isinstance(b, str) else b)
        return {'=': ka == kb, '<>': ka != kb, '<': ka < kb, '>': ka > kb,
                '<=': ka <= kb, '>=': ka >= kb}[op]

    def collect(self, args):
        """Numbers only: text and blanks inside a range are skipped, errors propagate."""
        out = []
        for node in args:
            v = self.ev(node)
            if isinstance(v, Rng):
                for x in v.vals:
                    if isinstance(x, Err): return x
                    if is_num(x): out.append(x)
            else:
                if isinstance(v, Err): return v
                x = self.num(v)
                if isinstance(x, Err): return x
                out.append(x)
        return out

    def criterion(self, c):
        if is_num(c): return lambda v: is_num(v) and v == c
        s = '' if c is None else str(c)
        m = re.match(r'^(<=|>=|<>|<|>|=)?(.*)$', s, re.S)
        op, rest = m.group(1) or '=', m.group(2)
        try:
            x = float(rest); numeric = True
        except ValueError:
            numeric = False
        if numeric:
            def p(v):
                if op == '<>': return not (is_num(v) and v == x)
                if not is_num(v): return False
                return {'=': v == x, '<': v < x, '>': v > x, '<=': v <= x, '>=': v >= x}[op]
            return p
        t = rest.lower()

        def q(v):
            same = isinstance(v, str) and v.lower() == t
            if op == '=': return same
            if op == '<>': return not same
            if not isinstance(v, str): return False
            return {'<': v.lower() < t, '>': v.lower() > t, '<=': v.lower() <= t, '>=': v.lower() >= t}[op]
        return q

    def call(self, name, args):
        n = len(args)
        if name == 'IF':
            if n < 2 or n > 3: return Err('#N/A')
            test = self.ev(args[0])
            if isinstance(test, Err): return test
            if isinstance(test, (str, Rng)): return Err('#VALUE!')
            if test: return self.ev(args[1])
            return self.ev(args[2]) if n == 3 else False
        if name in ('SUM', 'AVERAGE', 'MIN', 'MAX', 'PRODUCT'):
            xs = self.collect(args)
            if isinstance(xs, Err): return xs
            if name == 'SUM': return sum(xs)
            if name == 'AVERAGE': return Err('#DIV/0!') if not xs else sum(xs) / float(len(xs))
            if name == 'MIN': return min(xs) if xs else 0
            if name == 'MAX': return max(xs) if xs else 0
            p = 1
            for x in xs: p *= x
            return p
        if name in ('COUNT', 'COUNTA'):
            c = 0
            for node in args:
                v = self.ev(node)
                for x in (v.vals if isinstance(v, Rng) else [v]):
                    if name == 'COUNT': c += 1 if is_num(x) else 0
                    else: c += 0 if x is None else 1
            return c
        if name in ('MINUS', 'DIVIDE', 'MULTIPLY', 'ADD'):
            if n != 2: return Err('#N/A')
            a, b = self.ev(args[0]), self.ev(args[1])
            if isinstance(a, Rng) or isinstance(b, Rng): return Err('#VALUE!')
            return self.binop({'MINUS': '-', 'DIVIDE': '/', 'MULTIPLY': '*', 'ADD': '+'}[name], a, b)
        if name in ('COUNTIF', 'SUMIF'):
            if (name == 'COUNTIF' and n != 2) or (name == 'SUMIF' and n not in (2, 3)): return Err('#N/A')
            rng = self.ev(args[0]); crit = self.ev(args[1])
            if not isinstance(rng, Rng): return Err('#VALUE!')
            if isinstance(crit, Err): return crit
            pred = self.criterion(crit)
            tot = self.ev(args[2]) if n == 3 else rng
            if not isinstance(tot, Rng): return Err('#VALUE!')
            c = s = 0
            for i, v in enumerate(rng.vals):
                if pred(v):
                    c += 1
                    if i < len(tot.vals) and is_num(tot.vals[i]): s += tot.vals[i]
            return c if name == 'COUNTIF' else s
        return Err('#NAME?')


def fmt(v, dp=None):
    if isinstance(v, Err): return v.code
    if isinstance(v, bool): return 'TRUE' if v else 'FALSE'
    if v is None: return ''
    if is_num(v):
        if dp is not None: return ('%.' + str(dp) + 'f') % v
        if abs(v - round(v)) < 1e-9: return str(int(round(v)))
        return ('%.6f' % v).rstrip('0').rstrip('.')
    return str(v)


def check(actual, expected, what=''):
    """The evaluator against the hand-worked answer. A mismatch means the paper, not the assert, is wrong."""
    if isinstance(expected, str): ok = fmt(actual) == expected
    else: ok = is_num(actual) and abs(actual - expected) < 1e-9
    assert ok, 'MISMATCH %s: evaluator says %r, hand value %r' % (what, actual, expected)
    return actual


def no_ties(vals, what):
    assert len(set(vals)) == len(vals), 'tie in ' + what


def sort_whole(sh, col, desc=False):
    """Sort the data rows (row 2 down) as whole rows by column `col` (1-based)."""
    data = sh.rows[1:]
    no_ties([r[col - 1] for r in data], 'sort column %d' % col)
    return sorted(data, key=lambda r: r[col - 1], reverse=desc)


def sort_one_column(sh, col, desc=False):
    """The trap: only one column is selected, so only its cells move."""
    data = sh.rows[1:]
    no_ties([r[col - 1] for r in data], 'sort column %d' % col)
    vals = sorted([r[col - 1] for r in data], reverse=desc)
    out = [list(r) for r in data]
    for r, v in zip(out, vals): r[col - 1] = v
    return out


def visible_rows(sh, test):
    """Row numbers (spreadsheet numbering) that satisfy test(row). Hidden rows are still in the sheet."""
    return [i for i, r in enumerate(sh.rows, 1) if i > 1 and test(r)]


def between(lo, hi): return lambda x: is_num(x) and lo <= x <= hi
def greater_than(k): return lambda x: is_num(x) and x > k
def in_list(items): return lambda x: x in items


# =====================================================================================
#  Print helpers
# =====================================================================================
def F(s): return '<font name="Mono" size="9.4">%s</font>' % escape(s)


def cellhtml(v):
    if v is None or v == '': return ''
    s = escape(fmt(v) if not isinstance(v, str) else v)
    if s.endswith(' '): s = s[:-1] + '␣'      # a typed trailing space is shown as an open box
    return '<font name="Mono" size="9.2">%s</font>' % s


def rownum(i): return '<font name="UI-Bold" size="8.6" color="#5A5A66">%d</font>' % i


def widths_for(ncols, ratios=None, frac=1.0):
    total = AVAIL * frac
    ratios = ratios or [1] * ncols
    rest = total - 24
    return [24] + [rest * r / float(sum(ratios)) for r in ratios]


def sheet_grid(sh, fx='text', ratios=None, frac=1.0, blanks=()):
    """The printed extract: column letters on top, row numbers down the side.
    fx='text' prints a formula as typed; fx='value' prints what it would show.
    `blanks` is a set of (col, row) cells left empty for the student to fill."""
    ncols = max(len(r) for r in sh.rows)
    rows = [[''] + [n2col(i + 1) for i in range(ncols)]]
    for i, r in enumerate(sh.rows, 1):
        line = [rownum(i)]
        for c in range(1, ncols + 1):
            if (c, i) in blanks:
                line.append('')
                continue
            raw = sh.raw(c, i)
            shown = sh.cell(c, i) if (isinstance(raw, str) and raw.startswith('=') and fx == 'value') else raw
            line.append(cellhtml(shown))
        rows.append(line)
    return rows, widths_for(ncols, ratios, frac)


def table_grid(data, ratios=None, frac=1.0):
    """A grid from explicit rows (row 1 = headings) for a student to fill; same look as a sheet extract."""
    return sheet_grid(Sheet(data), ratios=ratios, frac=frac)


def Q(text, marks=0, grid=None, fill=False, **kw):
    d = {'text': text, 'marks': marks}
    if grid:
        d['grid'], d['grid_widths'] = grid
        if fill: d['grid_h'] = 9
    d.update(kw)
    return d


def part(label, text, marks, space=0, grid=None, fill=False, **kw):
    d = {'label': label, 'text': text, 'marks': marks}
    if space: d['space'] = space
    if grid:
        d['grid'], d['grid_widths'] = grid
        if fill: d['grid_h'] = 9
    d.update(kw)
    return d


def M(s): return s + ' <b>[1]</b>'


def _sgrid(rows, col_widths, row_h_mm):
    data = [[Paragraph('<font name="UI-Bold" size="9.4">%s</font>' % c, PL.S_Q) if i == 0
             else Paragraph('<font name="Body" size="10.4">%s</font>' % c, PL.S_Q)
             for c in row] for i, row in enumerate(rows)]
    t = Table(data, colWidths=col_widths, rowHeights=[row_h_mm * mm] * len(rows))
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.6, PL.LINE), ('BACKGROUND', (0, 0), (-1, 0), PL.PAPERBG),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
    return t


def build_paper2(spec, path):
    """paper_lib.build_paper, plus the two layout differences above. Same fonts, header, rules, footer."""
    story = PL._header(spec)
    for qi, q in enumerate(spec['questions'], 1):
        head = []
        if q.get('section'):
            head.append(Paragraph(q['section'].upper(), PL.S_SEC))
        head.append(PL._qrow('%d.' % qi, q['text'], q.get('marks', 0) if not q.get('parts') else 0))
        if q.get('grid'):
            head.append(Spacer(1, 4)); head.append(_sgrid(q['grid'], q.get('grid_widths'), q.get('grid_h', 7.4))); head.append(Spacer(1, 2))
        if q.get('space'):
            head.append(PL.Ruled(q['space']))
        if q.get('tip') and not q.get('parts'):
            head.append(Spacer(1, 2)); head.append(Paragraph(q['tip'], PL.S_NOTE))
        parts = q.get('parts', [])
        blocks = []
        for p in parts:
            sub = [Spacer(1, 3), PL._qrow(p['label'], p['text'], p.get('marks', 0), indent=16, numw=26)]
            if p.get('grid'):
                sub.append(Spacer(1, 4)); sub.append(_sgrid(p['grid'], p.get('grid_widths'), p.get('grid_h', 7.4))); sub.append(Spacer(1, 2))
            if p.get('space'):
                sub.append(PL.Ruled(p['space'], width=AVAIL, indent=16))
            blocks.append(sub)
        if blocks:
            head.extend(blocks[0])            # the stem travels with its first part
            blocks = blocks[1:]
        if q.get('tip') and parts and not blocks:
            head.append(Spacer(1, 2)); head.append(Paragraph(q['tip'], PL.S_NOTE))
        story.append(KeepTogether(head))
        for bi, sub in enumerate(blocks):
            if q.get('tip') and bi == len(blocks) - 1:
                sub = sub + [Spacer(1, 2), Paragraph(q['tip'], PL.S_NOTE)]
            story.append(KeepTogether(sub))
        story.append(Spacer(1, 9))
    story.extend([Spacer(1, 4), PL.Rule(thickness=0.6, colour=PL.LINE), Spacer(1, 4), Paragraph(spec['endnote'], PL.S_NOTE)])
    doc = BaseDocTemplate(path, pagesize=PL.A4, leftMargin=PL.MARGIN_L, rightMargin=PL.MARGIN_R,
                          topMargin=PL.MARGIN_T, bottomMargin=PL.MARGIN_B, title=spec['title'], author='Base Camp')
    frame = Frame(PL.MARGIN_L, PL.MARGIN_B, AVAIL, PL.A4[1] - PL.MARGIN_T - PL.MARGIN_B, id='f',
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame])])
    footer = spec['footer']

    class C(PL.NumberedCanvas):
        def __init__(self, *a, **k):
            k['footer'] = footer
            PL.NumberedCanvas.__init__(self, *a, **k)
    doc.build(story, canvasmaker=C)
    return path


# =====================================================================================
#  Instructions
# =====================================================================================
BASE = [
    'Answer <b>every</b> question in the space provided. There is no computer and no calculator: every number is designed to work by hand.',
    'This paper is about <b>Google Sheets</b>. Every formula starts with <b>=</b>, arguments are separated by <b>commas</b>, and text goes in <b>quotation marks</b>.',
    'Where a question asks for a <b>value</b>, write what the cell would show. Where it asks for a <b>formula</b>, write it exactly, brackets and commas included.',
    'The mark for each question is shown in square brackets on the right.',
]
REMINDER = ('<b>Reminder (medium papers only).</b> &nbsp;' + ' &nbsp; '.join(F(x) for x in [
    'SUM(range)', 'AVERAGE(range)', 'MIN(range)', 'MAX(range)', 'COUNT(range)', 'COUNTA(range)',
    'MINUS(a, b)', 'DIVIDE(a, b)', 'PRODUCT(a, b)', 'IF(test, if_true, if_false)',
    'SUMIF(range, criterion, sum_range)', 'COUNTIF(range, criterion)']))
INSTR_MED = BASE + [REMINDER]
INSTR_HARD = BASE + [
    'No list of functions is printed on this paper. You are expected to remember the syntax, including the order of the arguments.',
    'Several questions describe sheets you may not have seen before. You are not expected to recognise them: apply the ideas you already have.',
    'A correct value with a wrong formula, or the other way round, earns one mark and not two.']


# =====================================================================================
#  PAPER A  (medium) -- every number below is computed, then asserted against the design
# =====================================================================================
SA1 = Sheet([['Item', 'Price (₹)', 'Sold', 'Revenue (₹)'],
             ['Samosa', 15, 12, '=B2*C2'], ['Vada Pav', 20, 11, '=B3*C3'], ['Poha', 30, 8, '=B4*C4'],
             ['Chai', 10, 15, '=B5*C5'], ['Lassi', 25, 9, '=B6*C6']])
A1_rev = [SA1.cell(4, r) for r in range(2, 7)]
no_ties(A1_rev, 'A1 revenues')
A1_d5 = check(SA1.a('D5'), 150, 'A1 D5')
A1_sum = check(SA1.f('=SUM(D2:D6)'), 1015, 'A1 sum')
A1_max = check(SA1.f('=MAX(D2:D6)'), 240, 'A1 max')
A1_avg = check(SA1.f('=AVERAGE(C2:C6)'), 11, 'A1 avg')
A1_short = check(SA1.f('=SUM(D2:D5)'), 790, 'A1 short range')
A1_price = check(SA1.f('=MAX(B2:B6)'), 30, 'A1 max price')
A1_avg_rev = check(SA1.f('=AVERAGE(D2:D6)'), 203, 'A1 average of the wrong column')

SA2 = Sheet([['Student', 'Test mark (out of 50)'],
             ['Aditi', 34], ['Bhavna', 41], ['Chetan', 'absent'], ['Deepa', 28], ['Eshan', None],
             ['Farah', 45], ['Girish', 'absent'], ['Hema', 32]])
A2_count = check(SA2.f('=COUNT(B2:B9)'), 5, 'A2 count')
A2_counta = check(SA2.f('=COUNTA(B2:B9)'), 7, 'A2 counta')
A2_avg = check(SA2.f('=AVERAGE(B2:B9)'), 36, 'A2 average')
A2_sum = check(SA2.f('=SUM(B2:B9)'), 180, 'A2 sum')
A2_div7 = SA2.f('=SUM(B2:B9)/COUNTA(B2:B9)')
A2_div8 = SA2.f('=SUM(B2:B9)/8')
assert fmt(A2_div7, 1) == '25.7' and fmt(A2_div8) == '22.5'

SA3 = Sheet([['Student', 'Score', 'Result'], ['Anil', 47, '=IF(B2>=40,"Pass","Fail")'],
             ['Bina', 40, '=IF(B3>=40,"Pass","Fail")'], ['Charu', 39, '=IF(B4>=40,"Pass","Fail")'],
             ['Dev', 12, '=IF(B5>=40,"Pass","Fail")']])
A3 = [check(SA3.a('C%d' % r), x, 'A3 C%d' % r) for r, x in [(2, 'Pass'), (3, 'Pass'), (4, 'Fail'), (5, 'Fail')]]
A3_strict = check(SA3.f('=IF(B3>40,"Pass","Fail")'), 'Fail', 'A3 > for >=')
A3_noquote = SA3.f('=IF(B3>=40,Pass,Fail)')
assert A3_noquote == Err('#NAME?')

SA4 = Sheet([['Name', 'Class', 'Marks'], ['Farhan', 'A', 44], ['Gauri', 'B', 31], ['Harini', 'A', 29],
             ['Imran', 'B', 37], ['Jatin', 'A', 38], ['Kavya', 'B', 46], ['Lakshman', 'A', 22]])
A4_max = check(SA4.f('=MAX(C2:C8)'), 46, 'A4 max')
A4_cnt = check(SA4.f('=COUNTIF(B2:B8,"A")'), 4, 'A4 countif')
A4_sumif = check(SA4.f('=SUMIF(B2:B8,"B",C2:C8)'), 114, 'A4 sumif')
A4_noq = check(SA4.f('=COUNTIF(B2:B8,A)'), '#NAME?', 'A4 no quotes')
A4_no3rd = check(SA4.f('=SUMIF(B2:B8,"B")'), 0, 'A4 no third argument')
A4_sumall = check(SA4.f('=SUM(C2:C8)'), 247, 'A4 sum of everyone')

A5_model = '=IF(C2>=30,"High",IF(C2>=20,"Medium","Low"))'
A5_wrong = '=IF(C2>=20,"Medium",IF(C2>=30,"High","Low"))'
base5 = Sheet([[None, None, None], [None, None, 0]])
for v, exp in [(45, 'High'), (30, 'High'), (29, 'Medium'), (20, 'Medium'), (19, 'Low')]:
    check(base5.with_cell('C2', v).f(A5_model), exp, 'A5 model %d' % v)
A5_wrong_45 = check(base5.with_cell('C2', 45).f(A5_wrong), 'Medium', 'A5 wrong order, 45')
A5_strict20 = check(base5.with_cell('C2', 20).f('=IF(C2>30,"High",IF(C2>20,"Medium","Low"))'), 'Low', 'A5 > for >=')

SA6 = Sheet([['Bus (₹)', 'Students', 'Collected (₹)'], [2400, 30, 1800]])
A6_div = check(SA6.f('=DIVIDE(A2,B2)'), 80, 'A6 divide')
A6_min = check(SA6.f('=MINUS(A2,C2)'), 600, 'A6 minus')
A6_div_sw = check(SA6.f('=DIVIDE(B2,A2)'), 0.0125, 'A6 swapped divide')
A6_min_sw = check(SA6.f('=MINUS(C2,A2)'), -600, 'A6 swapped minus')

SA7 = Sheet([['Name', 'Score'], ['Dev', 14], ['Esha', 22], ['Fatima', 9], ['Gopal', 31], ['Hari', 18]])
A7_bad = sort_one_column(SA7, 2)
A7_good = sort_whole(SA7, 2)
assert [r[1] for r in A7_bad] == [9, 14, 18, 22, 31]
assert [r[0] for r in A7_bad] == ['Dev', 'Esha', 'Fatima', 'Gopal', 'Hari']
assert [r[0] for r in A7_good] == ['Fatima', 'Dev', 'Hari', 'Esha', 'Gopal']
A7_dev_now = A7_bad[0][1]
assert A7_dev_now == 9

SA8 = Sheet([['Subject', 'Marks'], ['Maths', 42], ['Science', 28], ['English', 36], ['Maths', 31],
             ['Science', 35], ['English', 19]])
A8_rows = visible_rows(SA8, lambda r: r[1] >= 35)
assert A8_rows == [2, 4, 6]
A8_strict = visible_rows(SA8, lambda r: r[1] > 35)
assert A8_strict == [2, 4]
A8_total_after = check(SA8.f('=SUM(B2:B7)'), 191, 'A8 SUM still reads hidden rows')

A9_right = between(0, 50)
assert [A9_right(x) for x in (0, 23, 50, 51, -4, 300, 'absent')] == [True, True, True, False, False, False, False]
A9_gt0 = greater_than(0)
assert A9_gt0(0) is False and A9_gt0(300) is True    # the wrong rule refuses a valid 0 and lets 300 in

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · No computer · No calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + FOOT,
 'questions': [
  Q('The tuck-shop sheet below is open in Google Sheets. Column D holds a formula in every row; the extract shows each one as typed. '
    'Write the value each of these would show.', 0, sheet_grid(SA1, ratios=[3, 2, 1.4, 2.4], frac=0.82),
    section='Section 1 — Read the sheet',
    parts=[part('(a)', 'The cell ' + F('D5'), 1, 11), part('(b)', F('=SUM(D2:D6)'), 1, 11),
           part('(c)', F('=MAX(D2:D6)'), 1, 11), part('(d)', F('=AVERAGE(C2:C6)'), 1, 11)]),
  Q('Eight students sat a test out of 50. Two were absent, so the teacher typed the word <b>absent</b>, and one cell was left empty. '
    'Write the value of each.', 0, sheet_grid(SA2, ratios=[2, 2.4], frac=0.6),
    parts=[part('(a)', F('=COUNT(B2:B9)'), 1, 11), part('(b)', F('=COUNTA(B2:B9)'), 1, 11),
           part('(c)', F('=AVERAGE(B2:B9)'), 1, 11),
           part('(d)', 'Mr Rao wants to know how many students actually sat the test. Say which of COUNT and COUNTA he should use, and why.', 1, 19)]),
  Q('Column C holds this formula in C2, filled down: &nbsp;' + F('=IF(B2>=40,"Pass","Fail")') + '<br/>Write what each of C2, C3, C4 and C5 shows.', 4,
    sheet_grid(SA3, ratios=[2, 1.2, 1.8], frac=0.6, blanks={(3, 2), (3, 3), (3, 4), (3, 5)}), fill=True),
  Q('A class sheet has Class in column B and Marks in column C, rows 2 to 8.', 0, sheet_grid(SA4, ratios=[2, 1.2, 1.4], frac=0.6),
    section='Section 2 — Write the formula',
    parts=[part('(a)', 'Write a formula that shows the highest mark.', 1, 13),
           part('(b)', 'Write a formula that counts the students in Class A.', 1, 13),
           part('(c)', 'Write a formula that adds up the marks of the Class B students only, and state the value it shows.', 2, 22)],
    tip='Write the formula, then the value. A value with no formula next to it will not earn the formula mark.'),
  Q('A mark out of 50 is typed in cell C2. Column D should show <b>High</b> for 30 or more, <b>Medium</b> for 20 to 29, and <b>Low</b> for below 20.', 0,
    parts=[part('(a)', 'Write the formula for D2, using a nested IF.', 3, 26),
           part('(b)', 'State what your formula shows when C2 is exactly 20.', 1, 11)]),
  Q('A school trip sheet holds the cost of the bus in A2, the number of students in B2, and the money collected so far in C2.', 0,
    sheet_grid(SA6, ratios=[1.6, 1.4, 1.8], frac=0.6),
    parts=[part('(a)', 'Using DIVIDE, write the formula for the cost per student, and state its value.', 1, 15),
           part('(b)', 'Using MINUS, write the formula for the money still needed, and state its value.', 1, 15)]),
  Q('A student wants to put this table in order of score, smallest first. She selects <b>only</b> the Score cells, B2 to B6, and uses '
    'Data &gt; Sort range, A to Z. She does not select column A.', 0, sheet_grid(SA7, ratios=[2, 1], frac=0.5),
    section='Section 3 — Sort, filter and protect',
    parts=[part('(a)', 'Write what the table holds after her sort.', 2, 0,
                grid=table_grid([['Name', 'Score'], [None, None], [None, None], [None, None], [None, None], [None, None]], ratios=[2, 1], frac=0.5), fill=True),
           part('(b)', 'Dev really scored 14. What does the sheet now say Dev scored?', 1, 11),
           part('(c)', 'Write the names in the order they should appear after a <b>correct</b> sort, smallest score first.', 1, 14)]),
  Q('A filter is applied to this table with the condition <b>Marks is greater than or equal to 35</b>.', 0,
    sheet_grid(SA8, ratios=[2, 1.2], frac=0.5),
    parts=[part('(a)', 'Write the row numbers that are still showing.', 1, 11),
           part('(b)', 'Row 3 is no longer on the screen. Say exactly what has happened to it.', 1, 15)]),
  Q('A column holds marks out of 50. Design a data validation rule that stops anyone entering a mark above 50 or below 0.', 0,
    parts=[part('(a)', 'State the criteria, with the numbers.', 1, 13),
           part('(b)', 'State the setting for invalid data, and why you chose it.', 1, 17)]),
 ]}

# =====================================================================================
#  PAPER B  (medium)
# =====================================================================================
STEPS_ORDER = [('Collect', 1), ('Clean', 2), ('Organise', 3), ('Process', 4), ('Analyse', 5), ('Present', 6)]
STEP_TEXT = {
 'Present': 'Present &mdash; a chart or a sentence someone can act on',
 'Clean': 'Clean &mdash; fix the typo, the blank, the wrong spelling',
 'Collect': 'Collect &mdash; gather till slips, a survey, sensor readings',
 'Analyse': 'Analyse &mdash; compare groups, find the odd one out',
 'Process': 'Process &mdash; run formulas for totals, averages, counts',
 'Organise': 'Organise &mdash; one row per thing, one column per fact, a header row',
}
STEP_SHOWN = ['Process', 'Present', 'Collect', 'Organise', 'Analyse', 'Clean']
assert sorted(STEP_SHOWN) == sorted(k for k, _ in STEPS_ORDER) and STEP_SHOWN != [k for k, _ in STEPS_ORDER]
STEP_POS = dict(STEPS_ORDER)
assert sorted(STEP_POS.values()) == [1, 2, 3, 4, 5, 6]
B1_rows = ([['', 'Step of data analytics', 'Write 1 to 6']] +
           [['', STEP_TEXT[s], ''] for s in STEP_SHOWN])
B1_grid = (B1_rows, [24, (AVAIL - 24) * 0.78, (AVAIL - 24) * 0.22])

SB3 = Sheet([['City', 'Jun', 'Jul', 'Aug'], ['Mumbai', 540, 840, 590], ['Pune', 130, 180, 150], ['Chennai', 60, 90, 120]])
B3 = [('=SUM(B2:D2)', 1970), ('=MAX(B2:B4)', 540), ('=AVERAGE(C2:C4)', 370), ('=MINUS(D2,D4)', 470), ('=MIN(B2:D4)', 60)]
B3_vals = [check(SB3.f(f), x, 'B3 ' + f) for f, x in B3]
B3_col_sum = check(SB3.f('=SUM(B2:B4)'), 730, 'B3 sum down the column')
B3_swap = check(SB3.f('=MINUS(D4,D2)'), -470, 'B3 swapped MINUS')
B3_min_aug = check(SB3.f('=MIN(D2:D4)'), 120, 'B3 MIN of one column')
B3_avg_all = check(SB3.f('=AVERAGE(B2:D4)'), 2700 / 9.0, 'B3 average of everything')

SB4 = Sheet([['Item', 'Category', 'Units'], ['Samosa', 'Snack', 24], ['Idli', 'Meal', 17], ['Chai', 'Drink', 30],
             ['Poha', 'Meal', 12], ['Lassi', 'Drink', 18], ['Puff', 'Snack', 16], ['Biryani', 'Meal', 9]])
B4_meals = check(SB4.f('=COUNTIF(B2:B8,"Meal")'), 3, 'B4 meals')
B4_snack = check(SB4.f('=SUMIF(B2:B8,"Snack",C2:C8)'), 40, 'B4 snack units')
B4_noq = check(SB4.f('=COUNTIF(B2:B8,Meal)'), '#NAME?', 'B4 no quotes')
B4_no3rd = check(SB4.f('=SUMIF(B2:B8,"Snack")'), 0, 'B4 no third argument')
B4_all = check(SB4.f('=SUM(C2:C8)'), 126, 'B4 SUM of every row')
B4_cnt_all = check(SB4.f('=COUNTA(B2:B8)'), 7, 'B4 COUNTA of every row')

B5_model = '=IF(B2>=34,"Gold",IF(B2>=26,"Silver",IF(B2>=16,"Bronze","None")))'
base_b = Sheet([[None, None], [None, 0]])
for v, exp in [(40, 'Gold'), (34, 'Gold'), (33, 'Silver'), (26, 'Silver'), (25, 'Bronze'), (16, 'Bronze'), (15, 'None')]:
    check(base_b.with_cell('B2', v).f(B5_model), exp, 'B5 model %d' % v)
B5_noq = check(base_b.with_cell('B2', 10).f('=IF(B2>=34,"Gold",IF(B2>=26,"Silver",IF(B2>=16,"Bronze",None)))'), '#NAME?', 'B5 unquoted None')
B5_swap = check(base_b.with_cell('B2', 20).f('=IF(B2>=34,"Gold",IF(B2>=16,"Silver",IF(B2>=26,"Bronze","None")))'), 'Silver', 'B5 swapped thresholds')

B6_wrong = '=IF(B2>=20,"Pass",IF(B2>=35,"Merit",IF(B2>=42,"Distinction","Fail")))'
B6_right = '=IF(B2>=42,"Distinction",IF(B2>=35,"Merit",IF(B2>=20,"Pass","Fail")))'
B6_marks = [47, 36, 25, 12]
B6_shows = [base_b.with_cell('B2', m).f(B6_wrong) for m in B6_marks]
B6_should = [base_b.with_cell('B2', m).f(B6_right) for m in B6_marks]
assert B6_shows == ['Pass', 'Pass', 'Pass', 'Fail'] and B6_should == ['Distinction', 'Merit', 'Pass', 'Fail']

SB7 = Sheet([['Student', 'Subject', 'Marks'], ['Anaya', 'Science', 33], ['Bilal', 'SCIENCE', 41], ['Chitra', 'Sci', 28],
             ['Deven', 'English', 36], ['Esha', 'Science ', 45], ['Farid', 'Science', 38], ['Gita', 'English', 30]])
B7_count = check(SB7.f('=COUNTIF(B2:B8,"Science")'), 3, 'B7 countif')
B7_missed = [i for i in range(2, 9) if str(SB7.raw(2, i)).strip().lower().startswith('sci') and
             not str(SB7.raw(2, i)) == 'Science' and str(SB7.raw(2, i)).lower() != 'science']
assert B7_missed == [4, 6]
SB7_fixed = SB7.with_cell('B4', 'Science').with_cell('B6', 'Science')
B7_fixed = check(SB7_fixed.f('=COUNTIF(B2:B8,"Science")'), 5, 'B7 after correcting rows 4 and 6')
B7_rule = in_list(['Maths', 'Science', 'English'])
assert not B7_rule('Sci') and not B7_rule('Science ') and B7_rule('Science')

SB8 = Sheet([['Branch', 'Zone', 'Takings (₹)'], ['Hebbal', 'North', 400], ['Jayanagar', 'South', 300], ['Yelahanka', 'North', 500],
             ['Banashankari', 'South', 200], ['Koramangala', 'South', 250], ['Malleshwaram', 'North', 450]])
B8_sum = check(SB8.f('=SUMIF(B2:B7,"North",C2:C7)'), 1350, 'B8 north')
B8_avg = check(SB8.f('=SUMIF(B2:B7,"North",C2:C7)/COUNTIF(B2:B7,"North")'), 450, 'B8 north average')
B8_all = check(SB8.f('=AVERAGE(C2:C7)'), 350, 'B8 average of every branch')
B8_div6 = check(SB8.f('=SUMIF(B2:B7,"North",C2:C7)/6'), 225, 'B8 divided by every row')

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · No computer · No calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + FOOT,
 'questions': [
  Q('The six steps of data analytics are listed below out of order. In the right-hand column, write 1 to 6 to show the order in which they happen.', 3,
    B1_grid, fill=True, section='Section 1 — Data, steps and functions'),
  Q('A canteen sheet has one row that reads <b>Masala Chai, 150</b>.', 0,
    parts=[part('(a)', 'Which of these is <b>data</b> and which is <b>information</b>? &nbsp;(i) &ldquo;Masala Chai, 150&rdquo; &nbsp;(ii) &ldquo;Masala Chai sold more units than any other item.&rdquo;', 1, 17),
           part('(b)', 'State what has to be done to data to turn it into information.', 1, 15)]),
  Q('Rainfall in millimetres is held in this sheet. Write the value each formula would show.', 0,
    sheet_grid(SB3, ratios=[2.2, 1, 1, 1], frac=0.66),
    parts=[part('(a)', F('=SUM(B2:D2)'), 1, 10), part('(b)', F('=MAX(B2:B4)'), 1, 10), part('(c)', F('=AVERAGE(C2:C4)'), 1, 10),
           part('(d)', F('=MINUS(D2,D4)'), 1, 10), part('(e)', F('=MIN(B2:D4)'), 1, 10)]),
  Q('The canteen sheet below has the Category in column B and the units sold in column C, rows 2 to 8.', 0,
    sheet_grid(SB4, ratios=[2, 1.6, 1], frac=0.66), section='Section 2 — Conditions',
    parts=[part('(a)', 'Write a formula that counts the items in the <b>Meal</b> category, and state its value.', 2, 20),
           part('(b)', 'Write a formula that adds up the units sold in the <b>Snack</b> category, and state its value.', 2, 20)]),
  Q('Marks out of 40 are in column B. Column C should show <b>Gold</b> for 34 or more, <b>Silver</b> for 26 to 33, <b>Bronze</b> for 16 to 25, and <b>None</b> below 16. '
    'Fill the three gaps in the formula for C2.<br/><br/>' + F('=IF(B2>=34,"Gold",IF(B2>=____,"Silver",IF(B2>=____,"Bronze","____")))'), 3, space=16),
  Q('Another tutor writes this formula in C2 for marks out of 50, intending 42+ Distinction, 35 to 41 Merit, 20 to 34 Pass, and below 20 Fail:<br/>'
    + F(B6_wrong), 0,
    parts=[part('(a)', 'Write what the formula shows for each mark.', 2, 0,
                grid=table_grid([['Mark in B2', 'The formula shows'], [47, None], [36, None], [25, None], [12, None]], ratios=[1, 2], frac=0.6), fill=True),
           part('(b)', 'Explain what is wrong with the formula.', 1, 22)]),
  Q('A Subject column was typed by hand. The extract is below; the space typed after the word in row 6 is shown as <font name="Mono">\u2423</font>.', 0,
    sheet_grid(SB7, ratios=[2, 1.8, 1], frac=0.72), section='Section 3 — Check, clean and conclude',
    parts=[part('(a)', 'State the value of ' + F('=COUNTIF(B2:B8,"Science")') + '.', 1, 11),
           part('(b)', 'Rows 4 and 6 are both meant to be Science. Say why COUNTIF does not count either of them.', 1, 20),
           part('(c)', 'Design a data validation rule for column B that would have stopped both. State the criteria and the setting for invalid data.', 1, 20),
           part('(d)', 'The rule is now added. State what the formula in (a) shows, and what must be done to make it show 5.', 1, 20)]),
  Q('Six branches of a shop record their takings in rupees. Zone is in column B and Takings in column C, rows 2 to 7.', 0,
    sheet_grid(SB8, ratios=[2.4, 1.2, 1.4], frac=0.7),
    parts=[part('(a)', 'Write a formula that adds up the takings of the North zone.', 1, 15),
           part('(b)', 'Using SUMIF and COUNTIF, write one formula for the <b>average</b> takings of a North branch, and state its value.', 2, 22)]),
  Q('Choose a chart type for each, and give a reason.', 0,
    parts=[part('(a)', 'The total takings of the North zone and of the South zone, side by side.', 1, 17),
           part('(b)', 'Mumbai\'s rainfall in June, July, August and September.', 1, 17),
           part('(c)', 'A chart has been drawn with neither a title nor axis labels. Say what must be added.', 1, 15)]),
 ]}

# =====================================================================================
#  PAPER C  (hard)
# =====================================================================================
SC1 = Sheet([['Student', 'Days late', 'Fine (₹)'], ['Akash', 3, '=B2*2'], ['Bhumi', 7, '=B3*2'], ['Chirag', 'lost', '=B4*2'],
             ['Disha', None, '=B5*2'], ['Eklavya', 5, '=B6*2'], ['Fiza', 9, '=B7*2']])
C1_c4 = check(SC1.a('C4'), '#VALUE!', 'C1 C4')
C1_count = check(SC1.f('=COUNT(B2:B7)'), 4, 'C1 count')
C1_counta = check(SC1.f('=COUNTA(B2:B7)'), 5, 'C1 counta')
C1_sum = check(SC1.f('=SUM(B2:B7)'), 24, 'C1 sum')
C1_avg = check(SC1.f('=AVERAGE(B2:B7)'), 6, 'C1 average')
C1_div6 = check(SC1.f('=SUM(B2:B7)/6'), 4, 'C1 average over every row')
C1_div5 = check(SC1.f('=SUM(B2:B7)/COUNTA(B2:B7)'), 4.8, 'C1 average over COUNTA')
C1_plus = check(SC1.f('=B2+B3+B4'), '#VALUE!', 'C1 plus chokes on text')
C1_sum3 = check(SC1.f('=SUM(B2:B4)'), 10, 'C1 SUM skips text')

SC2 = Sheet([['Player', 'Team', 'Runs'], ['Aryan', 'Nilgiri', 62], ['Vivaan', 'Nilgiri', 45], ['Krish', 'Nilgiri', 78],
             ['Dhruv', 'Aravalli', 91], ['Atharv', 'Aravalli', 33], ['Yuvraj', 'Aravalli', 50], ['Rudra', 'Sahyadri', 24],
             ['Shaurya', 'Sahyadri', 70]])
C2_rows = visible_rows(SC2, lambda r: r[1] == 'Aravalli' and r[2] >= 50)
assert C2_rows == [5, 7]
C2_strict = visible_rows(SC2, lambda r: r[1] == 'Aravalli' and r[2] > 50)
assert C2_strict == [5]
C2_order = [r[0] for r in sort_whole(SC2, 3, desc=True)]
assert C2_order == ['Dhruv', 'Krish', 'Shaurya', 'Aryan', 'Yuvraj', 'Vivaan', 'Atharv', 'Rudra']
C2_asc = [r[0] for r in sort_whole(SC2, 3, desc=False)]
C2_total = check(SC2.f('=SUM(C2:C9)'), 453, 'C2 SUM with the filter on')
C2_visible_only = SC2.cell(3, 5) + SC2.cell(3, 7)
assert C2_visible_only == 141

SC3 = Sheet([['Player', 'Team', 'Runs', 'Balls', 'Strike rate'], ['Aryan', 'Nilgiri', 80, 50, None], ['Vivaan', 'Nilgiri', 55, 50, None],
             ['Krish', 'Nilgiri', 75, 50, None], ['Dhruv', 'Aravalli', 40, 50, None], ['Atharv', 'Aravalli', 50, 40, None],
             ['Rudra', 'Sahyadri', 24, 30, None], ['Shaurya', 'Sahyadri', 30, 20, None]])
C3_sr = check(SC3.f('=C2/D2*100'), 160, 'C3 strike rate')
C3_sr_plain = check(SC3.f('=C2/D2'), 1.6, 'C3 forgot the 100')
C3_sr_brk = check(SC3.f('=C2/(D2*100)'), 0.016, 'C3 bracket in the wrong place')
C3_cnt = check(SC3.f('=COUNTIF(C2:C8,">=50")'), 4, 'C3 count >= 50')
C3_cnt_strict = check(SC3.f('=COUNTIF(C2:C8,">50")'), 3, 'C3 count > 50')
C3_cnt_noq = check(SC3.f('=COUNTIF(C2:C8,>=50)'), '#ERROR!', 'C3 unquoted criterion')
C3_cnt_str = check(SC3.f('=COUNTIF(C2:C8,"50")'), 1, 'C3 "50" means exactly 50')
C3_avg = check(SC3.f('=SUMIF(B2:B8,"Nilgiri",C2:C8)/COUNTIF(B2:B8,"Nilgiri")'), 70, 'C3 Nilgiri average')
C3_avg_all = check(SC3.f('=AVERAGE(C2:C8)'), 354 / 7.0, 'C3 average of everyone')
C3_sumif_only = check(SC3.f('=SUMIF(B2:B8,"Nilgiri",C2:C8)'), 210, 'C3 SUMIF without the division')

C4_model = '=IF(A2>=12,"Danger",IF(A2>=9,"Alert",IF(A2>=5,"Watch","Normal")))'
C4_wrong = '=IF(A2>=5,"Watch",IF(A2>=9,"Alert",IF(A2>=12,"Danger","Normal")))'
base_c = Sheet([[None], [0]])
for v, exp in [(14, 'Danger'), (12, 'Danger'), (11, 'Alert'), (9, 'Alert'), (8, 'Watch'), (5, 'Watch'), (4, 'Normal')]:
    check(base_c.with_cell('A2', v).f(C4_model), exp, 'C4 model %d' % v)
C4_wrong_14 = check(base_c.with_cell('A2', 14).f(C4_wrong), 'Watch', 'C4 wrong order, 14')
C4_wrong_set = [base_c.with_cell('A2', v).f(C4_wrong) for v in (12, 9, 8, 4)]
C4_strict9 = check(base_c.with_cell('A2', 9).f('=IF(A2>12,"Danger",IF(A2>9,"Alert",IF(A2>5,"Watch","Normal")))'), 'Watch', 'C4 > for >=')

C5_rule = between(1, 5)
C5_entries = [0, 5, 6, 'five']
C5_ok = [x for x in C5_entries if C5_rule(x)]
assert C5_ok == [5]
C5_gt1 = greater_than(1); assert [x for x in C5_entries if C5_gt1(x)] == [5, 6]    # 'greater than 1' lets 6 in

SC6 = Sheet([['Item', 'Price (₹)', 'Sold', 'Revenue (₹)'], ['Chai', 10, 90, '=B2*C2'], ['Samosa', 15, 70, '=B3*C3'],
             ['Poha', 30, 45, '=B4*C4'], ['Thali', 80, 20, '=B5*C5']])
C6_units = [SC6.cell(3, r) for r in range(2, 6)]
C6_rev = [SC6.cell(4, r) for r in range(2, 6)]
no_ties(C6_units, 'C6 units'); no_ties(C6_rev, 'C6 revenues')
assert C6_rev == [900, 1050, 1350, 1600]
C6_top_units = SC6.cell(1, 2 + C6_units.index(max(C6_units)))
C6_top_rev = SC6.cell(1, 2 + C6_rev.index(max(C6_rev)))
assert (C6_top_units, C6_top_rev) == ('Chai', 'Thali')
C6_total = check(SC6.f('=SUM(D2:D5)'), 4900, 'C6 total revenue')
C6_by_rev = [SC6.cell(1, 2 + i) for i in sorted(range(4), key=lambda i: -C6_rev[i])[:2]]
C6_by_units = [SC6.cell(1, 2 + i) for i in sorted(range(4), key=lambda i: -C6_units[i])[:2]]
assert C6_by_rev == ['Thali', 'Poha'] and C6_by_units == ['Chai', 'Samosa']
C6_sum_units = check(SC6.f('=SUM(C2:C5)'), 225, 'C6 total units (the wrong column)')

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · No computer · No calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + FOOT,
 'questions': [
  Q('A school library records how many days late each book came back. Column C works out the fine at \u20b92 a day. '
    'Chirag\'s book was lost, so the librarian typed the word <b>lost</b>; Disha\'s cell was left empty. The extract shows column C as typed.', 0,
    sheet_grid(SC1, ratios=[2, 1.4, 1.6], frac=0.7), section='Section 1 — Read the sheet',
    parts=[part('(a)', 'What does cell C4 show?', 1, 10),
           part('(b)', 'State the values of ' + F('=COUNT(B2:B7)') + ' and of ' + F('=COUNTA(B2:B7)') + '.', 1, 11),
           part('(c)', 'State the value of ' + F('=SUM(B2:B7)') + '.', 1, 10),
           part('(d)', 'State the value of ' + F('=AVERAGE(B2:B7)') + '.', 1, 10),
           part('(e)', 'State the value of ' + F('=SUM(B2:B4)') + ', and explain why it is not an error although C4 is.', 1, 20)]),
  Q('A cricket sheet lists eight players, with Team in column B and Runs in column C.', 0,
    sheet_grid(SC2, ratios=[2, 2, 1], frac=0.66),
    parts=[part('(a)', 'A filter is applied: <b>Team is exactly &ldquo;Aravalli&rdquo;</b> and <b>Runs is greater than or equal to 50</b>. Write the row numbers that remain visible.', 2, 13),
           part('(b)', 'The filter is removed. The <b>whole table</b> is sorted by Runs, largest first. Write all eight names in order, top to bottom.', 2, 20),
           part('(c)', 'The sort is undone and the filter from (a) is switched back on. A student types ' + F('=SUM(C2:C9)') + ' in an empty cell below the table. State the value it shows.', 1, 13)]),
  Q('A coach adds a Strike rate column: the runs a batter scores per 100 balls. Runs are in column C and balls faced in column D, rows 2 to 8. '
    'The Team is in column B.', 0, sheet_grid(SC3, ratios=[2, 2, 1.1, 1.1, 1.6], frac=0.9),
    section='Section 2 — Build it',
    parts=[part('(a)', 'Write the formula for E2, so that it can be filled down.', 1, 13),
           part('(b)', 'Write one formula that counts the players who scored <b>50 or more</b>.', 1, 13),
           part('(c)', 'Write one formula that gives the average runs of the <b>Nilgiri</b> players only, and state its value.', 2, 22)]),
  Q('A river-gauge sheet records the level of a river in whole metres. The level is typed in A2. Column B should flag it:<br/>'
    '<b>12 m or more: Danger &nbsp;·&nbsp; 9 to 11 m: Alert &nbsp;·&nbsp; 5 to 8 m: Watch &nbsp;·&nbsp; below 5 m: Normal</b>', 0,
    parts=[part('(a)', 'Write the formula for B2 using nested IF.', 3, 28),
           part('(b)', 'State what your formula shows for a level of 12, 9, 8 and 4.', 2, 15),
           part('(c)', 'A different formula in B2 begins ' + F('=IF(A2>=5,"Watch",IF(A2>=9,"Alert",IF(A2>=12,"Danger","Normal")))') +
                       '. State what it shows for a level of 14 m, and say why.', 1, 22)]),
  Q('A feedback form records a star rating from 1 to 5 in column B.', 0, section='Section 3 — Diagnose and design',
    parts=[part('(a)', 'Design a data validation rule for column B. State the criteria with the numbers, and the setting for invalid data.', 2, 22),
           part('(b)', 'With your rule in place, someone types each of these in turn: 0, 5, 6 and the word five. State which are accepted.', 1, 14),
           part('(c)', 'Last week, before the rule existed, the cells B9 and B10 were filled with 9 and with five. State what happens to those two cells when the rule is added, and what the owner must do.', 1, 22)]),
  Q('A tuck shop wants to decide what to stock. Part of its sheet is shown. Column D is meant to hold the revenue: price times number sold.', 0,
    sheet_grid(SC6, ratios=[2, 1.4, 1.2, 1.8], frac=0.8, blanks={(4, 2), (4, 3), (4, 4), (4, 5)}), fill=True,
    parts=[part('(a)', 'Write the revenue of each item in column D. Then say which item sold the most <b>units</b> and which item earned the most <b>money</b>.', 2, 13),
           part('(b)', 'Write the formula that gives the total revenue of the four items, and state its value.', 1, 14),
           part('(c)', 'The shop can stock only two of the four items. Which two would you choose if the aim is to earn the most money? Which two if the aim is to serve the most children?', 2, 18),
           part('(d)', 'Use the words <b>data</b> and <b>information</b> to explain, in one sentence, why one sheet has given two different answers.', 1, 18)]),
 ]}

# =====================================================================================
#  PAPER D  (hard)
# =====================================================================================
SD1 = Sheet([['City', 'Region', 'Jul', 'Aug'], ['Mumbai', 'West', 840, 590], ['Pune', 'West', 180, 150], ['Chennai', 'South', 90, 115],
             ['Kochi', 'South', 700, 430], ['Kolkata', 'East', 370, 340], ['Delhi', 'North', 210, 245], ['Jaipur', 'North', 200, 230]])
D1_rows = visible_rows(SD1, lambda r: r[2] >= 200 and r[3] < 300)
assert D1_rows == [7, 8]
D1_strict = visible_rows(SD1, lambda r: r[2] > 200 and r[3] < 300)
assert D1_strict == [7]
D1_order = [r[0] for r in sort_whole(SD1, 4, desc=True)]
assert D1_order == ['Mumbai', 'Kochi', 'Kolkata', 'Delhi', 'Jaipur', 'Pune', 'Chennai']
D1_bad = sort_one_column(SD1, 4, desc=True)
D1_kochi_now = [r for r in D1_bad if r[0] == 'Kochi'][0][3]
assert D1_kochi_now == 245 and SD1.rows[4][3] == 430

SD2 = Sheet([['Item', 'Category', 'Units'], ['Chai', 'Drink', 30], ['Samosa', 'Snack', 24], ['Lassi', 'Drink', 18],
             ['Poha', 'Meal', 12], ['Puff', 'Snack', 16]])
D2_a_bad = check(SD2.f('=COUNTIF(B2:B6,Drink)'), '#NAME?', 'D2 unquoted')
D2_a_ok = check(SD2.f('=COUNTIF(B2:B6,"Drink")'), 2, 'D2 corrected')
D2_b_bad = check(SD2.f('=SUMIF(B2:B6,"Drink")'), 0, 'D2 no sum range')
D2_b_ok = check(SD2.f('=SUMIF(B2:B6,"Drink",C2:C6)'), 48, 'D2 SUMIF corrected')
D2_c = check(SD2.f('=COUNTIF(C2:C6,">=18")'), 3, 'D2 >=18')
D2_c_strict = check(SD2.f('=COUNTIF(C2:C6,">18")'), 2, 'D2 >18')

D3_wrong = '=IF(B2>=60,"B",IF(B2>=80,"A",IF(B2>=40,"C","D")))'
D3_right = '=IF(B2>=80,"A",IF(B2>=60,"B",IF(B2>=40,"C","D")))'
D3_marks = [85, 72, 45, 30]
D3_shows = [base_b.with_cell('B2', m).f(D3_wrong) for m in D3_marks]
D3_should = [base_b.with_cell('B2', m).f(D3_right) for m in D3_marks]
assert D3_shows == ['B', 'B', 'C', 'D'] and D3_should == ['A', 'B', 'C', 'D']
D3_boundary = [base_b.with_cell('B2', m).f(D3_right) for m in (80, 79, 60, 59, 40, 39)]
assert D3_boundary == ['A', 'B', 'B', 'C', 'C', 'D']

SD4 = Sheet([['Pupil', 'Height (cm)'], ['Ira', 152], ['Jai', 148], ['Kiran', 15], ['Lata', 160], ['Mohan', 'not measured'],
             ['Nisha', 155], ['Omkar', None], ['Pooja', 150]])
D4_min = check(SD4.f('=MIN(B2:B9)'), 15, 'D4 min')
D4_count = check(SD4.f('=COUNT(B2:B9)'), 6, 'D4 count')
D4_counta = check(SD4.f('=COUNTA(B2:B9)'), 7, 'D4 counta')
D4_avg = check(SD4.f('=AVERAGE(B2:B9)'), 130, 'D4 average')
D4_ok = check(SD4.f('=SUMIF(B2:B9,">=100")/COUNTIF(B2:B9,">=100")'), 153, 'D4 average of valid heights')
D4_div7 = SD4.f('=SUMIF(B2:B9,">=100")/COUNTA(B2:B9)')
assert fmt(D4_div7, 1) == '109.3'
D4_sumvalid = check(SD4.f('=SUMIF(B2:B9,">=100")'), 765, 'D4 sum of valid heights')

D5_house = in_list(['Red', 'Blue', 'Green', 'Yellow'])
assert D5_house('Red') and not D5_house('Reds') and not D5_house('red ')
D5_age = between(11, 14)
assert [D5_age(x) for x in (10, 11, 14, 15)] == [False, True, True, False]

SD6 = Sheet([['Subject', 'Marks'], ['Maths', 42], ['Science', 29], ['Maths', 38], ['Science', 31], [None, None], ['Total', '=SUM(B2:B5)']])
D6_total = check(SD6.a('B7'), 140, 'D6 SUM still reads every row')
D6_maths = check(SD6.f('=SUMIF(A2:A5,"Maths",B2:B5)'), 80, 'D6 Maths only')
D6_in_filter = visible_rows(Sheet(SD6.rows[:5]), lambda r: r[0] == 'Maths')
assert D6_in_filter == [2, 4]
D6_science = check(SD6.f('=SUM(B3,B5)'), 60, 'D6 the hidden Science rows')

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · No computer · No calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + FOOT,
 'questions': [
  Q('A weather sheet holds July and August rainfall in millimetres for seven cities, with Region in column B.', 0,
    sheet_grid(SD1, ratios=[2.2, 1.6, 1, 1], frac=0.74), section='Section 1 — Read the data',
    parts=[part('(a)', 'A filter is applied: <b>Jul is greater than or equal to 200</b> and <b>Aug is less than 300</b>. Write the row numbers that remain visible.', 2, 13),
           part('(b)', 'The filter is removed. The <b>whole table</b> is sorted by Aug, largest first. Write all seven city names in order, top to bottom.', 2, 20),
           part('(c)', 'Instead, only the Aug cells (D2 to D8) are selected and sorted largest first. State the Aug value that now sits in the row of Kochi.', 1, 13)]),
  Q('A canteen sheet has the Category in column B and the units sold in column C, rows 2 to 6.', 0,
    sheet_grid(SD2, ratios=[2, 1.6, 1], frac=0.66),
    parts=[part('(a)', 'A student types ' + F('=COUNTIF(B2:B6,Drink)') + '. State what it shows, and write the corrected formula.', 2, 17),
           part('(b)', 'Another student types ' + F('=SUMIF(B2:B6,"Drink")') + ', hoping for the units of drinks sold. State what it shows, and explain why.', 2, 22),
           part('(c)', 'State the value of ' + F('=COUNTIF(C2:C6,">=18")') + '.', 1, 11)]),
  Q('A teacher\'s grade formula in C2 is meant to show <b>A</b> for 80 or more, <b>B</b> for 60 to 79, <b>C</b> for 40 to 59 and <b>D</b> for below 40. The mark is in B2. '
    'The formula she typed is:<br/>' + F(D3_wrong), 0, section='Section 2 — Write and repair formulas',
    parts=[part('(a)', 'State what her formula shows for marks of 85, 72, 45 and 30.', 2, 14),
           part('(b)', 'Write the corrected formula.', 3, 26)]),
  Q('A class sheet has the heights of eight pupils in centimetres in B2 to B9. The column was typed by hand.', 0, sheet_grid(SD4, ratios=[2, 2.2], frac=0.6),
    parts=[part('(a)', 'State the value of ' + F('=MIN(B2:B9)') + ', and say what it tells you about the data.', 1, 17),
           part('(b)', 'State the values of ' + F('=COUNT(B2:B9)') + ' and of ' + F('=COUNTA(B2:B9)') + '.', 1, 12),
           part('(c)', 'State the value of ' + F('=AVERAGE(B2:B9)') + '.', 1, 11),
           part('(d)', 'Write one formula that gives the average of only the valid heights, those of 100 cm or more, and state its value.', 2, 22)]),
  Q('A sign-up sheet for a school trip has the pupil\'s House in column B (Red, Blue, Green or Yellow) and Age in column C, for pupils aged 11 to 14.', 0,
    section='Section 3 — Design and diagnose',
    parts=[part('(a)', 'Design a data validation rule for column B so that nobody can type a spelling that is not a house. State the criteria and the setting for invalid data.', 2, 22),
           part('(b)', 'Design a rule for column C. State the criteria with the numbers.', 1, 13),
           part('(c)', 'Another student sets the invalid-data option to <b>Show a warning</b> instead. State what happens when someone types <b>Reds</b>.', 1, 17)]),
  Q('Two students wrote the following. Neither statement is correct. The extract shows the sheet they were looking at.', 0,
    sheet_grid(SD6, ratios=[1.4, 1], frac=0.5),
    parts=[part('(i)', '<i>&ldquo;I added the rule <b>Number between 0 and 50, Reject the input</b> to a Marks column that already had a 300 typed in it. So the 300 has now been corrected.&rdquo;</i><br/>'
                       'Explain the mistake, then write a correct version.', 3, 36),
           part('(ii)', '<i>&ldquo;I filtered the table to show only Maths. All the Science rows were deleted, so the formula in B7 now shows 80.&rdquo;</i><br/>'
                        'Explain the mistake, then write a correct version.', 3, 36)]),
 ]}

# =====================================================================================
#  MARK SCHEMES
# =====================================================================================
def ff(v, dp=None): return fmt(v, dp)


SCHEMES = [
 {'title': 'Paper A — Medium', 'meta': '30 marks', 'questions': [
  {'n': '1', 'marks': 4, 'lines': [
     M('(a) D5 shows <b>%s</b> (=B5*C5, 10 &times; 15)' % ff(A1_d5)),
     M('(b) <b>%s</b> (%s)' % (ff(A1_sum), ' + '.join(ff(x) for x in A1_rev))),
     M('(c) <b>%s</b> &mdash; the largest <i>revenue</i>, which is the Poha row' % ff(A1_max)),
     M('(d) <b>%s</b> &mdash; the five numbers in Sold add to 55, and 55 &divide; 5' % ff(A1_avg))],
   'note': 'Four independent marks. Three slips to look for: a range that stops a row short, =SUM(D2:D5), shows %s and loses the Lassi; in (c) %s is the largest <i>price</i> (MAX of column B), '
           'so the candidate has read the wrong column; in (d) the question asks for the average of Sold, and answering %s (the average of Revenue) means the same wrong-column slip.'
           % (ff(A1_short), ff(A1_price), ff(A1_avg_rev))},
  {'n': '2', 'marks': 4, 'lines': [
     M('(a) <b>%s</b> &mdash; only the numbers' % ff(A2_count)),
     M('(b) <b>%s</b> &mdash; everything except the one empty cell, so both words count' % ff(A2_counta)),
     M('(c) <b>%s</b> &mdash; %s &divide; %s numbers' % (ff(A2_avg), ff(A2_sum), ff(A2_count))),
     M('(d) <b>COUNT</b>, because it counts only cells that hold a number, so &ldquo;absent&rdquo; and the empty cell are not counted as sitting the test')],
   'note': 'The COUNT/COUNTA trap in its plainest form. If (a) is 8, the candidate counted rows; %s means COUNTA was used. For (c), %s means they divided by COUNTA (the 7 non-empty cells), '
           'and %s means they divided by all 8 cells; AVERAGE never does either. Award (d) only if the reason mentions numbers.'
           % (ff(A2_counta), ff(A2_div7, 1), ff(A2_div8))},
  {'n': '3', 'marks': 4, 'lines': [
     M('C2 (47): <b>%s</b>' % A3[0]), M('C3 (40): <b>%s</b> &mdash; 40 is exactly the pass mark and &gt;= includes it' % A3[1]),
     M('C4 (39): <b>%s</b>' % A3[2]), M('C5 (12): <b>%s</b>' % A3[3])],
   'note': 'The boundary is the point of C3. A candidate who reads &gt;= as &gt; writes %s for C3, and that is the only mark lost. '
           'Pass and Fail must be the words, not 1 and 0. Do not penalise missing quotation marks here: the formula is given, not written.' % A3_strict},
  {'n': '4', 'marks': 4, 'lines': [
     M('(a) <b>=MAX(C2:C8)</b>'),
     M('(b) <b>=COUNTIF(B2:B8,"A")</b> &mdash; range first, criterion second, quotation marks round the A'),
     M('(c) formula <b>=SUMIF(B2:B8,"B",C2:C8)</b> &mdash; test range, criterion, then the range to add'),
     M('(c) value <b>%s</b> (31 + 37 + 46)' % ff(A4_sumif))],
   'note': 'Three traps live here. Quotation marks left off, =COUNTIF(B2:B8,A), give %s. The third argument left out, =SUMIF(B2:B8,"B"), gives %s, because Sheets adds the range it tested, '
           'which is words. =SUM(C2:C8) adds both classes and gives %s. A candidate who types =C3+C5+C7 and gets %s has not used the Class column: award the value mark only.'
           % (ff(A4_noq), ff(A4_no3rd), ff(A4_sumall), ff(A4_sumif))},
  {'n': '5', 'marks': 4, 'lines': [
     M('(a) highest band tested first, with its answer in quotation marks: <b>=IF(C2&gt;=30,"High",</b>'),
     M('second IF placed in the <b>false</b> slot, testing <b>C2&gt;=20</b> with <b>"Medium"</b>'),
     M('<b>"Low"</b> as the last false answer, with commas and <b>two</b> closing brackets: <b>=IF(C2&gt;=30,"High",IF(C2&gt;=20,"Medium","Low"))</b>'),
     M('(b) <b>%s</b>' % check(base5.with_cell('C2', 20).f(A5_model), 'Medium'))],
   'note': 'The order trap. =IF(C2&gt;=20,"Medium",IF(C2&gt;=30,"High","Low")) shows %s for a mark of 45, and High can never appear. Award the first mark only to a formula that tests 30 before 20. '
           'In (b), %s means the candidate used &gt; where &gt;= was needed (a mark of exactly 20 is Medium).' % (A5_wrong_45, A5_strict20)},
  {'n': '6', 'marks': 2, 'lines': [
     M('(a) <b>=DIVIDE(A2,B2)</b> shows <b>%s</b> (accept =A2/B2)' % ff(A6_div)),
     M('(b) <b>=MINUS(A2,C2)</b> shows <b>%s</b> (accept =A2-C2)' % ff(A6_min))],
   'note': 'The arguments go in the order of the sentence. =DIVIDE(B2,A2) shows %s, and =MINUS(C2,A2) shows %s: the second is a negative amount of money still needed, '
           'which is visibly wrong. Either swapped version scores zero for that part.' % (ff(A6_div_sw), ff(A6_min_sw))},
  {'n': '7', 'marks': 4, 'lines': [
     M('(a) the Score column in order: <b>%s</b>' % ', '.join(ff(r[1]) for r in A7_bad)),
     M('(a) the Name column <b>unchanged</b>: %s' % ', '.join(r[0] for r in A7_bad)),
     M('(b) <b>%s</b> &mdash; Dev is now beside the smallest score' % ff(A7_dev_now)),
     M('(c) <b>%s</b>' % ', '.join(r[0] for r in A7_good))],
   'note': 'Sorting one column on its own. The scores move and the names do not, so every student now owns someone else\'s score: Dev (really 14) shows %s. '
           'Candidates who move names and scores together in (a) have done the correct sort, not the one described, and score 0 for (a). Part (c) is marked on its own.' % ff(A7_dev_now)},
  {'n': '8', 'marks': 2, 'lines': [
     M('(a) rows <b>%s</b> &mdash; 35 is included by &gt;=' % ', '.join(str(r) for r in A8_rows)),
     M('(b) it is <b>hidden</b>, not deleted: it is still in the sheet and Data &gt; Remove filter brings it back')],
   'note': 'Filter hides, it does not delete. A candidate who writes &ldquo;deleted&rdquo; or &ldquo;moved&rdquo; loses (b). The strict reading of the condition gives rows %s and loses (a); '
           'it drops the 35 in row 6. Row numbers must be given, not names. A SUM over B2:B7 still shows %s with the filter on, because it reads the hidden rows too.' % (', '.join(str(r) for r in A8_strict), ff(A8_total_after))},
  {'n': '9', 'marks': 2, 'lines': [
     M('(a) <b>Number between 0 and 50</b>'),
     M('(b) <b>Reject the input</b> &mdash; a warning lets the bad entry in; only Reject keeps it out')],
   'note': 'Computed against the rules: &ldquo;Number between 0 and 50&rdquo; accepts 0, 23 and 50 and refuses 51, -4 and 300. &ldquo;Number greater than 0&rdquo; refuses the valid mark 0 and accepts 300, '
           'so it scores nothing. Show a warning in (b) scores nothing, whatever the reason given.'},
 ]},

 {'title': 'Paper B — Medium', 'meta': '30 marks', 'questions': [
  {'n': '1', 'marks': 3, 'lines': [
     M('<b>Collect 1</b> and <b>Present 6</b>'),
     M('<b>Clean 2</b> and <b>Organise 3</b>'),
     M('<b>Process 4</b> and <b>Analyse 5</b>')],
   'note': 'The order that matters is Clean before Organise and Process before Analyse. The usual slip is to put Clean after Process, which is the garbage-in, garbage-out mistake: '
           'a formula run on uncleaned data gives a confident wrong number. Award each mark only if both steps in the pair are numbered correctly.'},
  {'n': '2', 'marks': 2, 'lines': [
     M('(a) (i) is <b>data</b>; (ii) is <b>information</b>'),
     M('(b) the data has to be <b>processed or analysed to answer a question</b>')],
   'note': 'Look for the word &ldquo;question&rdquo; or &ldquo;process/analyse&rdquo;. &ldquo;Put it in a table&rdquo; describes Organise, not information. '
           'A candidate who calls both statements data, or treats the two words as synonyms, loses (a): the syllabus wants them kept apart.'},
  {'n': '3', 'marks': 5, 'lines': [
     M('(a) <b>%s</b> (540 + 840 + 590, across the row)' % ff(B3_vals[0])),
     M('(b) <b>%s</b>' % ff(B3_vals[1])),
     M('(c) <b>%s</b> (840 + 180 + 90 = 1110, &divide; 3)' % ff(B3_vals[2])),
     M('(d) <b>%s</b> (590 &minus; 120)' % ff(B3_vals[3])),
     M('(e) <b>%s</b> &mdash; the smallest of all nine numbers' % ff(B3_vals[4]))],
   'note': 'Direction and order. In (a) %s is the sum down the June column (B2:B4), not across row 2. In (d), swapping the cells gives %s. '
           'In (e), %s means the candidate looked at the Aug column only (MIN of D2:D4); MIN reads all nine cells as one list. Averaging all nine instead would give %s.'
           % (ff(B3_col_sum), ff(B3_swap), ff(B3_min_aug), ff(B3_avg_all))},
  {'n': '4', 'marks': 4, 'lines': [
     M('(a) formula <b>=COUNTIF(B2:B8,"Meal")</b>'),
     M('(a) value <b>%s</b> (Idli, Poha, Biryani)' % ff(B4_meals)),
     M('(b) formula <b>=SUMIF(B2:B8,"Snack",C2:C8)</b>'),
     M('(b) value <b>%s</b> (24 + 16)' % ff(B4_snack))],
   'note': 'Quotation marks and the third argument. =COUNTIF(B2:B8,Meal) shows %s. =SUMIF(B2:B8,"Snack") shows %s: it adds the Category column, which is words. '
           '=SUM(C2:C8) shows %s and ignores the category completely. Accept a formula with the correct logic and a different range only if it still covers rows 2 to 8.'
           % (ff(B4_noq), ff(B4_no3rd), ff(B4_all))},
  {'n': '5', 'marks': 3, 'lines': [
     M('first gap <b>26</b>'), M('second gap <b>16</b>'), M('third gap <b>"None"</b>, with the quotation marks')],
   'note': 'The gaps run from high to low, so the thresholds must be 26 then 16. Swapping them, =IF(B2&gt;=34,"Gold",IF(B2&gt;=16,"Silver",IF(B2&gt;=26,"Bronze","None"))), shows %s for a mark of 20 '
           'where Bronze is correct. Writing None without quotation marks makes the formula show %s for any mark under 16. Mark each gap on its own.' % (B5_swap, B5_noq)},
  {'n': '6', 'marks': 3, 'lines': [
     M('(a) 47 and 36: <b>Pass</b> and <b>Pass</b>'),
     M('(a) 25 and 12: <b>Pass</b> and <b>Fail</b>'),
     M('(b) it tests the <b>lowest</b> band first, so every mark of 20 or more is caught by the first test and Merit and Distinction can never appear; the highest band must be tested first')],
   'note': 'The nested-IF order trap, to be traced rather than described. The correct formula would show %s for the same four marks. A candidate who writes Distinction and Merit for 47 and 36 '
           'has traced the formula they meant, not the one printed. In (b), &ldquo;the brackets are wrong&rdquo; or &ldquo;the numbers are wrong&rdquo; earns nothing: the order is the fault.'
           % ', '.join(B6_should)},
  {'n': '7', 'marks': 4, 'lines': [
     M('(a) <b>%s</b> &mdash; rows 2, 3 and 7; capital letters do not matter, so row 3 counts' % ff(B7_count)),
     M('(b) row 4 is <b>Sci</b>, a different word; row 6 has an <b>extra space</b> after Science, which makes it different text'),
     M('(c) criteria <b>Dropdown</b> (Maths, Science, English); setting <b>Reject the input</b>'),
     M('(d) it still shows <b>%s</b>; the rule only checks new entries, so rows 4 and 6 must be <b>corrected by hand</b>, after which it shows <b>%s</b>' % (ff(B7_count), ff(B7_fixed)))],
   'note': 'Validation does not clean existing data. A candidate who writes that the count is now %s has assumed the rule fixed the old cells. Row 3 (SCIENCE) is not an error and is counted; '
           'a candidate who says row 3 is missed has not learnt that COUNTIF ignores capitals. Award (b) only if both rows are named with a reason.' % ff(B7_fixed)},
  {'n': '8', 'marks': 3, 'lines': [
     M('(a) <b>=SUMIF(B2:B7,"North",C2:C7)</b>'),
     M('(b) formula <b>=SUMIF(B2:B7,"North",C2:C7)/COUNTIF(B2:B7,"North")</b>'),
     M('(b) value <b>%s</b> (%s &divide; 3)' % (ff(B8_avg), ff(B8_sum)))],
   'note': 'The average of a group is SUMIF divided by COUNTIF. =AVERAGE(C2:C7) averages every branch and shows %s, so the zone has been ignored; dividing the North total by 6 (every row) shows %s. '
           'Both are visibly wrong against %s. Quotation marks round North are needed in both functions.' % (ff(B8_all), ff(B8_div6), ff(B8_avg))},
  {'n': '9', 'marks': 3, 'lines': [
     M('(a) a <b>column (or bar) chart</b>, because it compares categories'),
     M('(b) a <b>line chart</b>, because it shows change over time'),
     M('(c) a <b>title</b> and <b>labels on both axes</b>')],
   'note': 'Chart type follows the question: categories against each other get columns, change over time gets a line. A pie chart or a line chart for (a) earns nothing. '
           'For (c) both a title and axis labels are needed for the mark; &ldquo;a key&rdquo; alone does not earn it.'},
 ]},

 {'title': 'Paper C — Hard', 'meta': '30 marks', 'questions': [
  {'n': '1', 'marks': 5, 'lines': [
     M('(a) <b>%s</b>' % ff(C1_c4)),
     M('(b) <b>%s</b> and <b>%s</b>' % (ff(C1_count), ff(C1_counta))),
     M('(c) <b>%s</b> (3 + 7 + 5 + 9)' % ff(C1_sum)),
     M('(d) <b>%s</b> (%s &divide; 4 numbers)' % (ff(C1_avg), ff(C1_sum))),
     M('(e) <b>%s</b>; SUM skips the text &ldquo;lost&rdquo;, whereas the * in C4 tries to multiply it' % ff(C1_sum3))],
   'note': 'Functions skip text; symbols choke on it. C4 is =B4*2, and B4 is the word lost, so it shows %s; =B2+B3+B4 would show the same %s. =SUM(B2:B4) gives %s because it ignores the word. '
           'In (d), %s means the candidate divided by all six cells, and %s means they divided by COUNTA; AVERAGE divides by the 4 numbers only. In (b) the two values are %s and %s: '
           'if the candidate swaps them, award nothing.' % (ff(C1_c4), ff(C1_plus), ff(C1_sum3), ff(C1_div6), ff(C1_div5), ff(C1_count), ff(C1_counta))},
  {'n': '2', 'marks': 5, 'lines': [
     M('(a) rows <b>%s</b>' % ' and '.join(str(r) for r in C2_rows)),
     M('(a) no other rows (both conditions must hold, and 50 is included)'),
     M('(b) the first four: <b>%s</b>' % ', '.join(C2_order[:4])),
     M('(b) the last four: <b>%s</b>' % ', '.join(C2_order[4:])),
     M('(c) <b>%s</b> &mdash; a filter hides rows but SUM still adds them' % ff(C2_total))],
   'note': 'Filter hides, SUM does not care. The 141 a candidate would get by adding only the two visible rows (91 + 50) is wrong: the formula still reads all eight rows and shows %s. '
           'Yuvraj has exactly 50, so he is on the boundary: reading &ldquo;50 or more&rdquo; as &ldquo;more than 50&rdquo; leaves only row %s. '
           'Part (b) is a whole-table sort; no two runs tie, so the order is unique. Ascending order, which is %s, scores nothing.'
           % (ff(C2_total), ', '.join(str(r) for r in C2_strict), ', '.join(C2_asc[:3]) + ' &hellip;')},
  {'n': '3', 'marks': 4, 'lines': [
     M('(a) <b>=C2/D2*100</b> (or =DIVIDE(C2,D2)*100), which shows %s for Aryan' % ff(C3_sr)),
     M('(b) <b>=COUNTIF(C2:C8,"&gt;=50")</b> &mdash; the operator and the number together, inside quotation marks'),
     M('(c) <b>=SUMIF(B2:B8,"Nilgiri",C2:C8)</b> as the top of the fraction'),
     M('(c) divided by <b>COUNTIF(B2:B8,"Nilgiri")</b>, giving <b>%s</b> (%s &divide; 3)' % (ff(C3_avg), ff(C3_sumif_only)))],
   'note': 'Three precise slips. In (a) =C2/D2 shows %s (the 100 is forgotten) and =C2/(D2*100) shows %s; both are visibly wrong beside a strike rate of %s. '
           'In (b), =COUNTIF(C2:C8,&gt;=50) with no quotation marks shows %s, ">50" gives %s and loses the player on exactly 50, and "50" alone counts only that one player (%s). '
           'In (c), =AVERAGE(C2:C8) averages every player and shows %s, ignoring the team.'
           % (ff(C3_sr_plain), ff(C3_sr_brk), ff(C3_sr), ff(C3_cnt_noq), ff(C3_cnt_strict), ff(C3_cnt_str), ff(C3_avg_all, 1))},
  {'n': '4', 'marks': 6, 'lines': [
     M('(a) highest band first: <b>=IF(A2&gt;=12,"Danger",</b>'),
     M('(a) the next two IFs in the false slots, with thresholds <b>9 "Alert"</b> and <b>5 "Watch"</b>'),
     M('(a) <b>"Normal"</b> as the last false answer, all words in quotation marks, <b>three</b> closing brackets'),
     M('(b) 12 is <b>Danger</b> and 9 is <b>Alert</b>'),
     M('(b) 8 is <b>Watch</b> and 4 is <b>Normal</b>'),
     M('(c) <b>%s</b>, because it tests 5 first and every level of 5 or more is caught by that test, so Alert and Danger can never appear' % C4_wrong_14)],
   'note': 'Three tests need three IFs and three closing brackets. The formula printed in (c) shows %s for levels of 12, 9, 8 and 4, so only the level of 4 comes out right. '
           'A candidate who writes &gt; instead of &gt;= shows %s for a level of 9 where Alert is correct: mark (b) for what their formula would show. '
           'In (c), &ldquo;the answer is wrong&rdquo; with no reason about order earns nothing.' % (', '.join(C4_wrong_set), C4_strict9)},
  {'n': '5', 'marks': 4, 'lines': [
     M('(a) criteria <b>Number between 1 and 5</b>'),
     M('(a) setting <b>Reject the input</b>'),
     M('(b) only <b>5</b> is accepted (0 and 6 are outside the range; the word five is not a number)'),
     M('(c) both cells stay exactly as they are, because validation checks only new entries; the owner must <b>correct them by hand</b>')],
   'note': 'Validation does not clean what is already there. A candidate who says 9 and five are &ldquo;rejected&rdquo; or &ldquo;removed&rdquo; loses (c). '
           'A rule of &ldquo;greater than 1&rdquo; accepts %s, so it fails (a): the upper limit is missing. Show a warning in (a) scores nothing for the setting.'
           % ' and '.join(str(x) for x in [x for x in C5_entries if C5_gt1(x)])},
  {'n': '6', 'marks': 6, 'lines': [
     M('(a) revenues <b>%s</b>' % ', '.join(ff(x) for x in C6_rev)),
     M('(a) most units: <b>%s</b>; most money: <b>%s</b>' % (C6_top_units, C6_top_rev)),
     M('(b) <b>=SUM(D2:D5)</b>, value <b>%s</b>' % ff(C6_total)),
     M('(c) for money: <b>%s</b> and <b>%s</b>' % tuple(C6_by_rev)),
     M('(c) for children served: <b>%s</b> and <b>%s</b>' % tuple(C6_by_units)),
     M('(d) the <b>same data</b> (price and units) answers different <b>questions</b>; analysing it for money or for units gives different <b>information</b>, and so a different decision')],
   'note': 'The question you ask decides the answer you get. The 225 a candidate gets from =SUM(C2:C5) is the total <i>units</i>, the wrong column for revenue (the right total is %s). '
           'Neither the units ranking nor the revenue ranking has a tie, so both answers are unique. In (d) the two words must be used the right way round: data is the raw price and units, '
           'information is the answer to a question. A candidate who writes only &ldquo;price is different&rdquo; has the cause but not the idea: award nothing.' % ff(C6_total)},
 ]},

 {'title': 'Paper D — Hard', 'meta': '30 marks', 'questions': [
  {'n': '1', 'marks': 5, 'lines': [
     M('(a) row <b>%s</b>' % str(D1_rows[0])),
     M('(a) and row <b>%s</b> (Jaipur has exactly 200 in July, which &gt;= includes)' % str(D1_rows[1])),
     M('(b) the first three: <b>%s</b>' % ', '.join(D1_order[:3])),
     M('(b) the last four: <b>%s</b>' % ', '.join(D1_order[3:])),
     M('(c) <b>%s</b>' % ff(D1_kochi_now))],
   'note': 'Whole-row sorting against one-column sorting, plus a boundary. In (c) the Aug cells alone move and the names stay: Kochi is in row 5, which now holds the fourth-largest Aug value, %s, '
           'and not its own %s. A candidate who answers %s has sorted the whole table, which is (b) not (c). In (a), reading &gt;= as &gt; drops Jaipur and leaves only row %s. '
           'All seven Aug values are different, so the order is unique.' % (ff(D1_kochi_now), ff(SD1.rows[4][3]), ff(SD1.rows[4][3]), str(D1_strict[0]))},
  {'n': '2', 'marks': 5, 'lines': [
     M('(a) it shows <b>%s</b>' % ff(D2_a_bad)),
     M('(a) corrected: <b>=COUNTIF(B2:B6,"Drink")</b>'),
     M('(b) it shows <b>%s</b>' % ff(D2_b_bad)),
     M('(b) with no third argument SUMIF adds the range it tested, column B, which is words, so there is nothing to add'),
     M('(c) <b>%s</b> (Chai 30, Samosa 24, Lassi 18)' % ff(D2_c))],
   'note': 'Quotation marks, the third argument, and a boundary. =COUNTIF(B2:B6,"Drink") shows %s; the corrected SUMIF, =SUMIF(B2:B6,"Drink",C2:C6), shows %s, which is what the student wanted. '
           'In (c), &ldquo;&gt;18&rdquo; would show %s and lose Lassi, who sold exactly 18. A candidate who explains (b) as &ldquo;it should be a number&rdquo; has missed that the range being added is the text column.'
           % (ff(D2_a_ok), ff(D2_b_ok), ff(D2_c_strict))},
  {'n': '3', 'marks': 5, 'lines': [
     M('(a) 85 and 72 both show <b>%s</b>' % D3_shows[0]),
     M('(a) 45 shows <b>%s</b> and 30 shows <b>%s</b>' % (D3_shows[2], D3_shows[3])),
     M('(b) <b>=IF(B2&gt;=80,"A",</b> the highest band tested first'),
     M('(b) <b>IF(B2&gt;=60,"B",IF(B2&gt;=40,"C","D"))</b> in the false slot, thresholds 60 and 40'),
     M('(b) every grade in quotation marks and <b>three</b> closing brackets: %s' % escape(D3_right))],
   'note': 'The nested-IF order trap, repaired not just spotted. The printed formula tests 60 before 80, so 85 shows %s where %s is correct; the lower marks come out right because no earlier test catches them. '
           'The correct formula gives %s for 80, 79, 60, 59, 40 and 39: a marker can test a candidate\'s formula against those six. A candidate who only swaps the letters has not repaired the order.'
           % (D3_shows[0], D3_should[0], ', '.join(D3_boundary))},
  {'n': '4', 'marks': 5, 'lines': [
     M('(a) <b>%s</b>, a height of 15 cm is impossible: it is a typing slip for 150' % ff(D4_min)),
     M('(b) <b>%s</b> and <b>%s</b>' % (ff(D4_count), ff(D4_counta))),
     M('(c) <b>%s</b> (780 &divide; 6)' % ff(D4_avg)),
     M('(d) <b>=SUMIF(B2:B9,"&gt;=100")/COUNTIF(B2:B9,"&gt;=100")</b>, with the operator and number inside quotation marks'),
     M('(d) value <b>%s</b> (%s &divide; 5)' % (ff(D4_ok), ff(D4_sumvalid)))],
   'note': 'Analysis starts with distrust. The average of %s looks plausible for a class of Grade 7 pupils, which is exactly why it is dangerous: only MIN reveals the slip. '
           'In (d), dividing the valid total by COUNTA shows %s, and the word and the empty cell are the reason COUNT and COUNTA disagree (%s against %s). '
           'Without quotation marks round &gt;=100 the formula shows an error.' % (ff(D4_avg), ff(D4_div7, 1), ff(D4_count), ff(D4_counta))},
  {'n': '5', 'marks': 4, 'lines': [
     M('(a) criteria <b>Dropdown</b> with the four items Red, Blue, Green, Yellow'),
     M('(a) setting <b>Reject the input</b>'),
     M('(b) <b>Number between 11 and 14</b>'),
     M('(c) <b>Reds</b> goes into the cell anyway, with a warning flag; a warning is advice, not a barrier')],
   'note': 'A dropdown is the cure for spelling, because nobody can type a spelling that is not on the list. Reds is not in the list, so only Reject keeps it out. '
           'A rule of &ldquo;greater than 11&rdquo; with no upper limit does not earn (b). In (c) a candidate who says &ldquo;it is rejected&rdquo; has described the other setting.'},
  {'n': '6', 'marks': 6, 'lines': [
     M('(i) the mistake: validation does not change cells that are already filled'),
     M('(i) correct version: the rule only checks entries made from now on, so the 300 is still in its cell until someone changes it by hand'),
     M('(i) and the cell must be corrected, for example to a valid mark, before any total or average is trusted'),
     M('(ii) the mistake: a filter hides rows, it does not delete them'),
     M('(ii) correct version: the Science rows are still in the sheet, hidden, and SUM still adds every row, hidden or not'),
     M('(ii) so B7 still shows <b>%s</b>, not <b>%s</b>; the Maths-only total would need SUMIF' % (ff(D6_total), ff(D6_maths)))],
   'note': 'The standing Paper D question: two wrong statements to diagnose and mend. (i) is the validation trap, the one most students believe, and (ii) is the filter trap plus the SUM-reads-hidden-rows catch. '
           'The figures are computed: =SUM(B2:B5) shows %s with the filter on or off; the 80 comes only from the two Maths rows. The hidden Science rows hold %s between them. '
           'Award the mistake mark only for naming what the statement gets wrong, not for restating the statement.' % (ff(D6_total), ff(D6_science))},
 ]},
]

# =====================================================================================
#  Verification, then build
# =====================================================================================
def count_marks_in_lines(lines):
    return sum(l.count('<b>[1]</b>') for l in lines)


def _verify():
    papers = [A, B, C, D]
    for spec in papers:
        spec.setdefault('endnote', 'End of paper. Check that every formula starts with = and that every word inside a formula is in quotation marks.')
    for spec, sc in zip(papers, SCHEMES):
        total = 0
        for q in spec['questions']:
            if q.get('parts'):
                assert sum(p['marks'] for p in q['parts']) == q['marks'] or q['marks'] == 0, (spec['title'], q['text'][:40])
                q['marks'] = sum(p['marks'] for p in q['parts'])
            total += q['marks']
        assert total == 30, (spec['title'], total)
        # the scheme matches the paper question for question, and every mark has its own tagged line
        assert len(sc['questions']) == len(spec['questions']), spec['title']
        schemetotal = 0
        for pq, sq in zip(spec['questions'], sc['questions']):
            assert pq['marks'] == sq['marks'], (spec['title'], sq['n'], pq['marks'], sq['marks'])
            assert count_marks_in_lines(sq['lines']) == sq['marks'], (spec['title'], sq['n'], count_marks_in_lines(sq['lines']))
            assert sq.get('note'), (spec['title'], sq['n'], 'every question needs a note')
            schemetotal += sq['marks']
        assert schemetotal == 30, (sc['title'], schemetotal)
        assert len(spec['questions']) >= 6
        sections = [q['section'] for q in spec['questions'] if q.get('section')]
        assert len(sections) == 3, (spec['title'], sections)
    # medium papers print the reminder, hard papers do not
    assert any('Reminder' in i for i in A['instructions']) and any('Reminder' in i for i in B['instructions'])
    assert not any('Reminder' in i or 'SUMIF(range' in i for i in C['instructions'] + D['instructions'])
    assert any('unfamiliar' in i or 'may not have seen' in i for i in C['instructions']) and any('may not have seen' in i for i in D['instructions'])
    # Paper D ends with the standing question: two wrong statements
    last = D['questions'][-1]
    assert [p['label'] for p in last['parts']] == ['(i)', '(ii)'] and 'Neither statement is correct' in last['text']


def coverage_check():
    """Every lesson and every named trap appears somewhere across A to D."""
    blob = ' '.join(str(q) for spec in (A, B, C, D) for q in spec['questions'])
    must = ['COUNTA', 'COUNTIF', 'SUMIF', 'DIVIDE', 'MINUS', 'MIN(', 'MAX(', 'AVERAGE', 'IF(',
            'Data &gt; Sort range', 'filter', 'validation', 'information', 'chart']
    for m in must:
        assert m in blob, 'coverage: ' + m
    # traps, found by the evaluator values in the schemes
    notes = ' '.join(sq['note'] for sc in SCHEMES for sq in sc['questions'])
    for m in ['COUNT/COUNTA', 'quotation marks', 'order', 'Sorting one column', 'hides', 'does not clean']:
        assert m.lower() in notes.lower() or m.lower().replace('does not clean', 'validation does not') in notes.lower(), 'trap: ' + m


_verify()
coverage_check()

files = []
for spec, code in [(A, 'a'), (B, 'b'), (C, 'c'), (D, 'd')]:
    p = os.path.join(OUT, 'computing-spreadsheets-paper-%s.pdf' % code)
    build_paper2(spec, p)
    files.append(p)
p = os.path.join(OUT, 'computing-spreadsheets-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how each total is split, one line per mark. Every sheet extract on these papers is real data, and every value in this booklet, '
             'including each wrong value quoted in the notes, is computed by an independent Google Sheets evaluator in the generator and asserted against the hand-worked answer before typesetting. '
             'The notes under each question name the specific mistake it was built to catch. The six recurring ones on this topic: COUNT against COUNTA; quotation marks left off a criterion; '
             'a nested IF tested lowest band first; sorting one column on its own; believing a filter deletes; and believing validation cleans old data.',
    'footer': 'Mark schemes · ' + FOOT})
files.append(p)
print('\n'.join(files))
