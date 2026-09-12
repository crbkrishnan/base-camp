#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 7 maths mock exams — four cross-topic papers, 80 marks each, 75 minutes.

Spans Units 1, 2, 3, 4, 7, 10 and 12. These are NOT topic papers, so the 30-mark
rule in CLAUDE.md does not apply: a mock is a different artefact and _verify()
asserts 80. A and B are medium, C and D are hard.

No paper prints a formula or a method reminder, on any tier. WRITING-PAPERS.md
says medium papers give the formula; that is deliberately overridden here on the
tutor's instruction, because recall is part of what a mock is for. Difficulty
separates A/B from C/D through the questions, not through scaffolding.

Every number below was computed and read before it was typeset — see _verify(),
which recomputes the lot on every build.
"""
import os, sys
from fractions import Fraction as F
from math import gcd
from decimal import Decimal as D
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)

EYEBROW = 'Base Camp · IGCSE Mathematics · Grade 7 · Mock exam'
TOPIC   = 'Grade 7 Mathematics &mdash; Mock Exam'
RS      = '&#8377;'

def fr(n, d):
    """A fraction, e.g. fr(3, 8) -> three eighths."""
    return '<super>%s</super>&frasl;<sub>%s</sub>' % (n, d)

def mx(w, n, d):
    """A mixed number, e.g. mx(4, 1, 4) -> four and a quarter."""
    return '%s<super>%s</super>&frasl;<sub>%s</sub>' % (w, n, d)

def B(n):
    return ' <b>[%d]</b>' % n

SEC1 = 'Section 1 — quick fire'
SEC2 = 'Section 2 — short answers'
SEC3 = 'Section 3 — multi-step'
SEC4 = 'Section 4 — problems'

INSTR = [
 'Answer <b>every</b> question in the space provided. Show your working — method marks are '
 'awarded even when the final answer is wrong.',
 'No calculator. Every number on this paper is designed to work without one.',
 '<b>75 minutes for 80 marks</b> — about a minute a mark. If a 3-mark question has taken you '
 'five minutes, leave it and come back to it.',
 'No formulas and no methods are given anywhere on this paper — not one. Remembering the right '
 'one is part of what is being tested.',
 'Give every fraction and every ratio in its simplest form, and convert to a common unit before '
 'you simplify.',
 'The mark for each question is shown in square brackets on the right.',
]

INSTR_HARD = INSTR + [
 'Nothing tells you which topic a question belongs to, and several need two topics at once. '
 'Work out what you are being asked before you start writing.',
]

END_MED  = ('End of paper. Before you hand it in, check every answer that came out as a round, '
            'comfortable number — those are the ones a wrong method produces most often.')
END_HARD = ('End of paper. Go back to the two questions you were least sure of. On a mock, the '
            'marks you find in the last five minutes are the cheapest ones on the paper.')


# ================================================================= PAPER A
A_Q = [
 {'section':SEC1, 'text':'Write down the answer to each of these.', 'marks':5,
  'parts':[{'label':'(a)','text':'Write <b>84</b> as a product of its prime factors, in index form.','marks':1,'space':20},
           {'label':'(b)','text':'&minus;7 &times; &minus;6','marks':1,'space':18},
           {'label':'(c)','text':'<super>3</super>&radic;216','marks':1,'space':18},
           {'label':'(d)','text':'Write 3<super>4</super> as an ordinary number.','marks':1,'space':18},
           {'label':'(e)','text':'45 &times; 0.1','marks':1,'space':18}]},

 {'text':'Write down the answer to each of these.', 'marks':5,
  'parts':[{'label':'(a)','text':'Round <b>6.472</b> to 1 decimal place.','marks':1,'space':18},
           {'label':'(b)','text':'0.3 &times; 0.4','marks':1,'space':18},
           {'label':'(c)','text':'Write ' + fr(3, 8) + ' as a decimal.','marks':1,'space':18},
           {'label':'(d)','text':'Write the ratio 18 : 24 in its simplest form.','marks':1,'space':18},
           {'label':'(e)','text':'Expand 3(<i>x</i> + 5).','marks':1,'space':18}]},

 {'section':SEC2, 'text':'Two numbers are 12 and 18.', 'marks':2,
  'parts':[{'label':'(a)','text':'Find the highest common factor (HCF) of 12 and 18.','marks':1,'space':20},
           {'label':'(b)','text':'Find the lowest common multiple (LCM) of 12 and 18.','marks':1,'space':20}],
  'tip':'One factor tree for each number answers both parts. Do not build them twice.'},

 {'text':'Simplify &nbsp;(2<super>5</super> &times; 2<super>3</super>) &divide; 2<super>6</super>. '
         'Give your answer as an ordinary number.', 'marks':2, 'space':28},

 {'text':'Work out:', 'marks':2,
  'parts':[{'label':'(a)','text':'6.2 &divide; 0.1','marks':1,'space':18},
           {'label':'(b)','text':'6.2 &times; 0.01','marks':1,'space':18}],
  'tip':'One of these answers is bigger than 6.2 and one is smaller. Decide which before you write anything.'},

 {'text':'Write these decimals in ascending order &mdash; smallest first.<br/>'
         '<b>0.7 &nbsp;&nbsp; 0.68 &nbsp;&nbsp; 0.702 &nbsp;&nbsp; 0.71</b>', 'marks':2, 'space':28},

 {'text':'Write these fractions in ascending order &mdash; smallest first. You must show your working.<br/>'
         '<b>' + fr(2,3) + ' &nbsp;&nbsp; ' + fr(5,8) + ' &nbsp;&nbsp; ' + fr(7,12) +
         ' &nbsp;&nbsp; ' + fr(3,4) + '</b>', 'marks':2, 'space':32,
  'tip':'Two of these four are close together. Looking at them will not separate them.'},

 {'text':'Work out &nbsp;' + mx(4,1,4) + ' &minus; ' + mx(1,5,6) +
         '. Give your answer as a mixed number in its simplest form.', 'marks':2, 'space':34},

 {'text':'A pencil costs ' + RS + '<i>p</i>. A pen costs ' + RS + '3 more than a pencil. '
         'Write an expression, in its simplest form, for the total cost of 4 pencils and 2 pens.',
  'marks':2, 'space':32},

 {'text':'Factorise fully:', 'marks':2,
  'parts':[{'label':'(a)','text':'6<i>x</i> + 15','marks':1,'space':18},
           {'label':'(b)','text':'8<i>y</i><super>2</super> &minus; 12<i>y</i>','marks':1,'space':20}],
  'tip':'&ldquo;Fully&rdquo; means nothing is left inside the bracket that both terms still share.'},

 {'section':SEC3, 'text':'Work out:', 'marks':3,
  'parts':[{'label':'(a)','text':'&minus;6 &times; &minus;4','marks':1,'space':18},
           {'label':'(b)','text':'&minus;6 &minus; 4','marks':1,'space':18},
           {'label':'(c)','text':'&minus;48 &divide; 8','marks':1,'space':18}],
  'tip':'(a) and (b) look almost the same and are not. Two minus signs multiplied make a plus; two minus signs added do not.'},

 {'text':'Work out &nbsp;4.68 &divide; 0.12, showing your method.', 'marks':3, 'space':36},

 {'text':'Work out &nbsp;6 &times; ' + mx(2,3,4) + '. Give your answer as a mixed number.',
  'marks':3, 'space':36},

 {'text':'Work out &nbsp;8 &divide; ' + fr(2,5) + '.', 'marks':3, 'space':36,
  'tip':'Dividing by a fraction smaller than 1 gives an answer <i>bigger</i> than 8.'},

 {'text':'The cost, ' + RS + '<i>C</i>, of hiring a hall for <i>n</i> hours is given by '
         '<i>C</i> = 40<i>n</i> + 250.', 'marks':3,
  'parts':[{'label':'(a)','text':'Find <i>C</i> when <i>n</i> = 12.','marks':2,'space':28},
           {'label':'(b)','text':'Find <i>n</i> when <i>C</i> = 1050.','marks':1,'space':24}]},

 {'text':'Expand and simplify &nbsp;5(2<i>x</i> &minus; 3) &minus; 2(<i>x</i> &minus; 4).',
  'marks':3, 'space':36,
  'tip':'&minus;2 &times; &minus;4 is <i>plus</i> 8. That one sign is where this question is usually lost.'},

 {'text':'Solve &nbsp;5<i>x</i> + 7 = 3<i>x</i> + 19. &nbsp;Show every step.', 'marks':3, 'space':40},

 {'text':'A jacket costs ' + RS + '840. Its price is increased by 15%. Work out the new price.',
  'marks':3, 'space':36},

 {'section':SEC4, 'text':RS + '3600 is shared between Asha and Bela in the ratio 3 : 5.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out how much each of them receives.','marks':2,'space':32},
           {'label':'(b)','text':'Bela&rsquo;s share is then increased by 20%. Work out her new amount.','marks':2,'space':30},
           {'label':'(c)','text':'How much more than Asha&rsquo;s share is Bela&rsquo;s new amount?','marks':1,'space':22}],
  'tip':'Check your two answers to (a) add back up to 3600 before you go on.'},

 {'text':'Ravi thinks of a number, <i>n</i>. He multiplies it by 4 and then subtracts 7. '
         'His answer is the same as adding 11 to the number he first thought of.', 'marks':5,
  'parts':[{'label':'(a)','text':'Form an equation in <i>n</i>.','marks':2,'space':28},
           {'label':'(b)','text':'Solve your equation, and check your answer works.','marks':3,'space':42}]},

 {'text':'Two shops sell the same rice.<br/><b>Shop A:</b> 1.5 kg for ' + RS + '96. &nbsp;&nbsp; '
         '<b>Shop B:</b> 2.5 kg for ' + RS + '155.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out the price per kilogram at each shop.','marks':3,'space':40},
           {'label':'(b)','text':'Write down which shop is better value.','marks':1,'space':20},
           {'label':'(c)','text':'Work out the cost of 6 kg at the better-value shop.','marks':1,'space':22}]},

 {'text':'Two lights are switched on together at 9:00:00. One flashes every 12 seconds and the '
         'other flashes every 18 seconds.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out how many seconds pass before they next flash together.','marks':3,'space':38},
           {'label':'(b)','text':'Write down the time at which they next flash together.','marks':1,'space':20},
           {'label':'(c)','text':'How many times do they flash together in the 6 minutes after 9:00:00?','marks':1,'space':24}]},

 {'text':'A shirt costs ' + RS + '800. In one week its price is increased by 25%. The following '
         'week the new price is reduced by 20%.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out the price after the increase.','marks':2,'space':28},
           {'label':'(b)','text':'Work out the price after the reduction.','marks':2,'space':28},
           {'label':'(c)','text':'Write down the overall percentage change from ' + RS + '800.','marks':1,'space':22}]},

 {'text':'A rectangle has length (<i>x</i> + 4) cm and width 3 cm.', 'marks':5,
  'parts':[{'label':'(a)','text':'Write an expression for its area. Expand your answer.','marks':2,'space':24},
           {'label':'(b)','text':'Write an expression for its perimeter, in its simplest form.','marks':2,'space':24},
           {'label':'(c)','text':'Factorise your expression for the perimeter.','marks':1,'space':18}]},
]

A = {'eyebrow':EYEBROW, 'title':TOPIC + ' &mdash; Paper A',
     'meta':'Medium · Non-calculator · 75 minutes · 80 marks', 'marks':80,
     'instructions':INSTR, 'footer':'Paper A · Medium · Units 1, 2, 3, 4, 7, 10, 12',
     'endnote':END_MED, 'questions':A_Q}


# ================================================================= PAPER B
B_Q = [
 {'section':SEC1, 'text':'Write down the answer to each of these.', 'marks':5,
  'parts':[{'label':'(a)','text':'Write <b>90</b> as a product of its prime factors, in index form.','marks':1,'space':20},
           {'label':'(b)','text':'&minus;8 &times; &minus;5','marks':1,'space':18},
           {'label':'(c)','text':'&radic;196','marks':1,'space':18},
           {'label':'(d)','text':'Write 5<super>6</super> &divide; 5<super>4</super> as a single power of 5.','marks':1,'space':18},
           {'label':'(e)','text':'7.3 &divide; 0.1','marks':1,'space':18}]},

 {'text':'Write down the answer to each of these.', 'marks':5,
  'parts':[{'label':'(a)','text':'Round <b>34 682</b> to the nearest thousand.','marks':1,'space':18},
           {'label':'(b)','text':'0.6 &times; 0.05','marks':1,'space':18},
           {'label':'(c)','text':'Write ' + fr(5, 9) + ' as a decimal. Use dot notation.','marks':1,'space':20},
           {'label':'(d)','text':'Write the ratio 35 : 49 in its simplest form.','marks':1,'space':18},
           {'label':'(e)','text':'Factorise 7<i>x</i> &minus; 21.','marks':1,'space':18}]},

 {'section':SEC2, 'text':'Two numbers are 20 and 30.', 'marks':2,
  'parts':[{'label':'(a)','text':'Find the highest common factor (HCF) of 20 and 30.','marks':1,'space':20},
           {'label':'(b)','text':'Find the lowest common multiple (LCM) of 20 and 30.','marks':1,'space':20}]},

 {'text':'Simplify &nbsp;(3<super>2</super>)<super>3</super> &divide; 3<super>4</super>. '
         'Give your answer as an ordinary number.', 'marks':2, 'space':28,
  'tip':'Deal with the outside power first. A power raised to a power multiplies the indices.'},

 {'text':'Work out:', 'marks':2,
  'parts':[{'label':'(a)','text':'0.48 &divide; 0.01','marks':1,'space':18},
           {'label':'(b)','text':'350 &times; 0.01','marks':1,'space':18}]},

 {'text':'Write these decimals in ascending order &mdash; smallest first.<br/>'
         '<b>0.505 &nbsp;&nbsp; 0.55 &nbsp;&nbsp; 0.5 &nbsp;&nbsp; 0.5005</b>', 'marks':2, 'space':28,
  'tip':'Give them all the same number of decimal places first. 0.5 is 0.5000.'},

 {'text':'Write these fractions in ascending order &mdash; smallest first. You must show your working.<br/>'
         '<b>' + fr(3,5) + ' &nbsp;&nbsp; ' + fr(7,10) + ' &nbsp;&nbsp; ' + fr(11,20) +
         ' &nbsp;&nbsp; ' + fr(13,20) + '</b>', 'marks':2, 'space':32},

 {'text':'Work out &nbsp;' + mx(5,1,3) + ' &minus; ' + mx(2,3,4) +
         '. Give your answer as a mixed number in its simplest form.', 'marks':2, 'space':34,
  'tip':'A third minus three quarters is negative. Either borrow, or use improper fractions.'},

 {'text':'A notebook costs ' + RS + '<i>n</i>. A ruler costs ' + RS + '5 less than a notebook. '
         'Write an expression, in its simplest form, for the total cost of 3 notebooks and 4 rulers.',
  'marks':2, 'space':32},

 {'text':'Expand and simplify &nbsp;4(2<i>x</i> + 3) + 3(<i>x</i> &minus; 5).', 'marks':2, 'space':30},

 {'section':SEC3, 'text':'Work out:', 'marks':3,
  'parts':[{'label':'(a)','text':'&minus;5 &times; &minus;9','marks':1,'space':18},
           {'label':'(b)','text':'&minus;5 &minus; 9','marks':1,'space':18},
           {'label':'(c)','text':'72 &divide; &minus;9','marks':1,'space':18}],
  'tip':'(a) and (b) start with the same two numbers and end a long way apart.'},

 {'text':'Work out &nbsp;5.76 &divide; 0.24, showing your method.', 'marks':3, 'space':36},

 {'text':'Work out &nbsp;8 &times; ' + mx(3,2,5) + '. Give your answer as a mixed number.',
  'marks':3, 'space':36},

 {'text':'Work out &nbsp;12 &divide; ' + fr(3,4) + '.', 'marks':3, 'space':36},

 {'text':'<i>T</i> = 3<i>a</i> + 2<i>b</i>', 'marks':3,
  'parts':[{'label':'(a)','text':'Find <i>T</i> when <i>a</i> = 7 and <i>b</i> = &minus;4.','marks':2,'space':28},
           {'label':'(b)','text':'Find <i>a</i> when <i>T</i> = 26 and <i>b</i> = 4.','marks':1,'space':26}]},

 {'text':'Expand and simplify &nbsp;6(<i>x</i> &minus; 2) &minus; 3(2<i>x</i> &minus; 5).',
  'marks':3, 'space':36,
  'tip':'If your answer still has an <i>x</i> in it, check the signs again.'},

 {'text':'Solve &nbsp;3(<i>x</i> + 4) = 5<i>x</i> &minus; 2. &nbsp;Show every step.', 'marks':3, 'space':40},

 {'text':'A bicycle costs ' + RS + '640. Its price is reduced by 35%. Work out the new price.',
  'marks':3, 'space':36},

 {'section':SEC4, 'text':RS + '4200 is shared between Kiran and Leela in the ratio 2 : 5.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out how much each of them receives.','marks':2,'space':32},
           {'label':'(b)','text':'Kiran&rsquo;s share is then decreased by 25%. Work out his new amount.','marks':2,'space':30},
           {'label':'(c)','text':'How much more than Kiran&rsquo;s new amount is Leela&rsquo;s share?','marks':1,'space':22}]},

 {'text':'Meera has <i>x</i> stickers. Her brother has 8 fewer than three times as many as Meera. '
         'Together they have 64 stickers.', 'marks':5,
  'parts':[{'label':'(a)','text':'Form an equation in <i>x</i>.','marks':2,'space':28},
           {'label':'(b)','text':'Solve your equation to find how many stickers Meera has.','marks':2,'space':32},
           {'label':'(c)','text':'Write down how many stickers her brother has.','marks':1,'space':22}]},

 {'text':'Two shops sell the same petrol.<br/><b>Shop A:</b> 2.5 litres for ' + RS + '245. '
         '&nbsp;&nbsp; <b>Shop B:</b> 4 litres for ' + RS + '380.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out the price per litre at each shop.','marks':3,'space':40},
           {'label':'(b)','text':'Write down which shop is better value.','marks':1,'space':20},
           {'label':'(c)','text':'Work out the cost of 10 litres at the better-value shop.','marks':1,'space':22}]},

 {'text':'A rectangular floor measures 60 cm by 84 cm. It is to be covered completely by identical '
         'square tiles, with no tile cut and no gaps.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out the largest possible side length of a tile.','marks':3,'space':38},
           {'label':'(b)','text':'Work out how many of these tiles are needed.','marks':2,'space':30}],
  'tip':'The tile has to fit a whole number of times along <i>both</i> sides.'},

 {'text':'A phone costs ' + RS + '1500. In one week its price is increased by 20%. The following '
         'week the new price is reduced by 20%.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out the price after the increase.','marks':1,'space':24},
           {'label':'(b)','text':'Work out the price after the reduction.','marks':2,'space':28},
           {'label':'(c)','text':'Work out the overall percentage change from ' + RS + '1500.','marks':2,'space':30}],
  'tip':'The answer to (b) is not 1500. If you think a 20% rise and a 20% fall cancel, this question is here to argue with you.'},

 {'text':'A rectangle has length (2<i>x</i> &minus; 1) cm and width 5 cm.', 'marks':5,
  'parts':[{'label':'(a)','text':'Write an expression for its area. Expand your answer.','marks':2,'space':28},
           {'label':'(b)','text':'Write an expression for its perimeter, in its simplest form.','marks':2,'space':28},
           {'label':'(c)','text':'Factorise your expression for the perimeter.','marks':1,'space':22}]},
]

BP = {'eyebrow':EYEBROW, 'title':TOPIC + ' &mdash; Paper B',
      'meta':'Medium · Non-calculator · 75 minutes · 80 marks', 'marks':80,
      'instructions':INSTR, 'footer':'Paper B · Medium · Units 1, 2, 3, 4, 7, 10, 12',
      'endnote':END_MED, 'questions':B_Q}


# ================================================================= PAPER C
C_Q = [
 {'section':SEC1, 'text':'Write down the answer to each of these.', 'marks':5,
  'parts':[{'label':'(a)','text':'Write down the largest prime number that is less than 40.','marks':1,'space':18},
           {'label':'(b)','text':'&minus;3 &times; &minus;4 &times; &minus;2','marks':1,'space':18},
           {'label':'(c)','text':'&radic;81 &nbsp;+&nbsp; <super>3</super>&radic;8','marks':1,'space':18},
           {'label':'(d)','text':'Write 4<super>3</super> as a power of 2.','marks':1,'space':18},
           {'label':'(e)','text':'0.06 &divide; 0.01','marks':1,'space':18}]},

 {'text':'Write down the answer to each of these.', 'marks':5,
  'parts':[{'label':'(a)','text':'Round <b>0.0498</b> to 2 decimal places.','marks':1,'space':18},
           {'label':'(b)','text':'0.04 &times; 0.05','marks':1,'space':18},
           {'label':'(c)','text':'Write ' + fr(7, 11) + ' as a decimal. Use dot notation.','marks':1,'space':20},
           {'label':'(d)','text':'Write the ratio 750 g : 1.5 kg in its simplest form.','marks':1,'space':20},
           {'label':'(e)','text':'Factorise fully 12<i>x</i><super>2</super> &minus; 18<i>x</i>.','marks':1,'space':20}]},

 {'section':SEC2, 'text':'Two numbers are 24 and 36.', 'marks':2,
  'parts':[{'label':'(a)','text':'Find the highest common factor (HCF) of 24 and 36.','marks':1,'space':20},
           {'label':'(b)','text':'Find the lowest common multiple (LCM) of 24 and 36.','marks':1,'space':20}]},

 {'text':'Simplify &nbsp;(2<super>3</super> &times; 2<super>5</super>) &divide; '
         '(2<super>2</super> &times; 2<super>4</super>). Give your answer as an ordinary number.',
  'marks':2, 'space':30},

 {'text':'Work out:', 'marks':2,
  'parts':[{'label':'(a)','text':'3.6 &divide; 0.01','marks':1,'space':18},
           {'label':'(b)','text':'0.07 &times; 0.1','marks':1,'space':18}]},

 {'text':'Write these decimals in descending order &mdash; largest first.<br/>'
         '<b>0.4 &nbsp;&nbsp; 0.401 &nbsp;&nbsp; 0.41 &nbsp;&nbsp; 0.0409</b>', 'marks':2, 'space':28},

 {'text':'Write these fractions in ascending order &mdash; smallest first. You must show your working.<br/>'
         '<b>' + fr(5,6) + ' &nbsp;&nbsp; ' + fr(7,9) + ' &nbsp;&nbsp; ' + fr(11,12) +
         ' &nbsp;&nbsp; ' + fr(13,18) + '</b>', 'marks':2, 'space':32},

 {'text':'Work out &nbsp;' + mx(6,1,6) + ' &minus; ' + mx(2,7,8) +
         '. Give your answer as a mixed number in its simplest form.', 'marks':2, 'space':34},

 {'text':'A rectangle is 3 cm longer than it is wide. Its width is <i>w</i> cm. Write an expression, '
         'in terms of <i>w</i> and in its simplest form, for the perimeter of the rectangle.',
  'marks':2, 'space':32},

 {'text':'Expand and simplify &nbsp;3(2<i>x</i> &minus; 5) &minus; 4(3 &minus; <i>x</i>).',
  'marks':2, 'space':30},

 {'section':SEC3, 'text':'Work out:', 'marks':3,
  'parts':[{'label':'(a)','text':'&minus;7 &times; &minus;3','marks':1,'space':18},
           {'label':'(b)','text':'&minus;7 &minus; (&minus;3)','marks':1,'space':18},
           {'label':'(c)','text':'&minus;60 &divide; &minus;4','marks':1,'space':18}]},

 {'text':'Work out &nbsp;0.918 &divide; 0.027, showing your method.', 'marks':3, 'space':36},

 {'text':'Work out &nbsp;15 &times; ' + mx(2,4,5) + '.', 'marks':3, 'space':36},

 {'text':'Work out &nbsp;9 &divide; ' + fr(3,8) + '.', 'marks':3, 'space':36},

 {'text':'The perimeter <i>P</i> of a rectangle of length <i>l</i> and width <i>w</i> is given by '
         '<i>P</i> = 2(<i>l</i> + <i>w</i>).', 'marks':3,
  'parts':[{'label':'(a)','text':'Find <i>P</i> when <i>l</i> = 9 and <i>w</i> = 6.5.','marks':1,'space':24},
           {'label':'(b)','text':'Find <i>w</i> when <i>P</i> = 46 and <i>l</i> = 13.','marks':2,'space':32}]},

 {'text':'Expand and simplify &nbsp;4(3<i>x</i> + 5) &minus; 2(2<i>x</i> &minus; 5), then factorise '
         'your answer fully.', 'marks':3, 'space':42},

 {'text':'Solve &nbsp;2(3<i>x</i> &minus; 1) = 4(<i>x</i> + 3). &nbsp;Show every step.',
  'marks':3, 'space':40},

 {'text':'A television costs ' + RS + '1250. Its price is reduced by 18%. Work out the new price.',
  'marks':3, 'space':36},

 {'section':SEC4, 'text':RS + '9450 is shared between three charities in the ratio 2 : 3 : 4.',
  'marks':5,
  'parts':[{'label':'(a)','text':'Work out how much each charity receives.','marks':3,'space':38},
           {'label':'(b)','text':'The largest share is then increased by 12%. Work out its new value.','marks':1,'space':24},
           {'label':'(c)','text':'Work out the new total amount shared between the three charities.','marks':1,'space':24}]},

 {'text':'The three angles of a triangle are <i>x</i>&deg;, (3<i>x</i> &minus; 20)&deg; and '
         '(<i>x</i> + 40)&deg;.', 'marks':5,
  'parts':[{'label':'(a)','text':'Form an equation in <i>x</i> and solve it.','marks':3,'space':42},
           {'label':'(b)','text':'Hence write down the size of the largest angle.','marks':2,'space':30}]},

 {'text':'A shop sells juice in three sizes.<br/><b>0.75 litres for ' + RS + '57 &nbsp;&nbsp; '
         '1.25 litres for ' + RS + '90 &nbsp;&nbsp; 2.5 litres for ' + RS + '185</b>', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out the price per litre of each size.','marks':3,'space':42},
           {'label':'(b)','text':'Write down which size is the best value.','marks':1,'space':20},
           {'label':'(c)','text':'How much is saved by buying 5 litres in the best-value size rather '
                                 'than in the worst-value size?','marks':1,'space':24}]},

 {'text':'Machine A is serviced every 15 days. Machine B is serviced every 24 days. Both machines '
         'are serviced on 1 March.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out how many days pass before both machines are next serviced '
                                 'on the same day.','marks':3,'space':38},
           {'label':'(b)','text':'How many times in the 365 days after 1 March are both machines '
                                 'serviced on the same day?','marks':2,'space':30}]},

 {'text':'A share is worth ' + RS + '2000. In week 1 its value rises by 30%. In week 2 its new '
         'value falls by 30%.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out its value at the end of week 1.','marks':1,'space':24},
           {'label':'(b)','text':'Work out its value at the end of week 2.','marks':2,'space':28},
           {'label':'(c)','text':'Work out the overall percentage change over the two weeks.','marks':2,'space':30}]},

 {'text':'A rectangle has length (3<i>x</i> + 2) cm and width 4 cm.', 'marks':5,
  'parts':[{'label':'(a)','text':'Write an expression for its area. Expand your answer.','marks':2,'space':28},
           {'label':'(b)','text':'Write an expression for its perimeter, in its simplest form.','marks':2,'space':28},
           {'label':'(c)','text':'Factorise your expression for the perimeter fully.','marks':1,'space':22}]},
]

C = {'eyebrow':EYEBROW, 'title':TOPIC + ' &mdash; Paper C',
     'meta':'Hard · Non-calculator · 75 minutes · 80 marks', 'marks':80,
     'instructions':INSTR_HARD, 'footer':'Paper C · Hard · Units 1, 2, 3, 4, 7, 10, 12',
     'endnote':END_HARD, 'questions':C_Q}


# ================================================================= PAPER D
D_Q = [
 {'section':SEC1, 'text':'Write down the answer to each of these.', 'marks':5,
  'parts':[{'label':'(a)','text':'How many prime numbers are there between 20 and 30?','marks':1,'space':18},
           {'label':'(b)','text':'&minus;56 &divide; &minus;7','marks':1,'space':18},
           {'label':'(c)','text':'<super>3</super>&radic;343','marks':1,'space':18},
           {'label':'(d)','text':'Write 9<super>2</super> &times; 9<super>5</super> as a single power of 9.','marks':1,'space':18},
           {'label':'(e)','text':'0.5 &divide; 0.01','marks':1,'space':18}]},

 {'text':'Write down the answer to each of these.', 'marks':5,
  'parts':[{'label':'(a)','text':'Round <b>7.0962</b> to 2 decimal places.','marks':1,'space':18},
           {'label':'(b)','text':'1.2 &times; 0.03','marks':1,'space':18},
           {'label':'(c)','text':'Write ' + fr(4, 15) + ' as a decimal. Use dot notation.','marks':1,'space':20},
           {'label':'(d)','text':'Write the ratio 40 minutes : 2 hours in its simplest form.','marks':1,'space':20},
           {'label':'(e)','text':'Factorise fully 20<i>a</i><super>2</super> + 15<i>a</i>.','marks':1,'space':20}]},

 {'section':SEC2, 'text':'Two numbers are 18 and 45.', 'marks':2,
  'parts':[{'label':'(a)','text':'Find the highest common factor (HCF) of 18 and 45.','marks':1,'space':20},
           {'label':'(b)','text':'Find the lowest common multiple (LCM) of 18 and 45.','marks':1,'space':20}]},

 {'text':'Simplify &nbsp;(5<super>4</super> &times; 5<super>3</super>) &divide; 5<super>5</super>. '
         'Give your answer as an ordinary number.', 'marks':2, 'space':28},

 {'text':'Work out:', 'marks':2,
  'parts':[{'label':'(a)','text':'62 &times; 0.01','marks':1,'space':18},
           {'label':'(b)','text':'0.062 &divide; 0.01','marks':1,'space':18}]},

 {'text':'Write these decimals in ascending order &mdash; smallest first.<br/>'
         '<b>0.303 &nbsp;&nbsp; 0.033 &nbsp;&nbsp; 0.33 &nbsp;&nbsp; 0.3003</b>', 'marks':2, 'space':28},

 {'text':'Write these fractions in descending order &mdash; largest first. You must show your working.<br/>'
         '<b>' + fr(7,8) + ' &nbsp;&nbsp; ' + fr(5,6) + ' &nbsp;&nbsp; ' + fr(11,12) +
         ' &nbsp;&nbsp; ' + fr(17,24) + '</b>', 'marks':2, 'space':32},

 {'text':'Work out &nbsp;' + mx(7,2,5) + ' &minus; ' + mx(3,5,8) +
         '. Give your answer as a mixed number in its simplest form.', 'marks':2, 'space':34},

 {'text':'A taxi charges a fixed fee of ' + RS + '50 plus ' + RS + '18 for each kilometre travelled.',
  'marks':2,
  'parts':[{'label':'(a)','text':'Write an expression for the cost of a journey of <i>k</i> kilometres.','marks':1,'space':20},
           {'label':'(b)','text':'Write an expression, in its simplest form, for the cost of two such journeys.','marks':1,'space':22}]},

 {'text':'Expand and simplify &nbsp;2(5<i>x</i> &minus; 3) &minus; 5(<i>x</i> &minus; 2).',
  'marks':2, 'space':30},

 {'section':SEC3, 'text':'Work out:', 'marks':3,
  'parts':[{'label':'(a)','text':'&minus;9 &times; &minus;6','marks':1,'space':18},
           {'label':'(b)','text':'&minus;9 &minus; 6','marks':1,'space':18},
           {'label':'(c)','text':'&minus;144 &divide; 12','marks':1,'space':18}]},

 {'text':'Work out &nbsp;2.622 &divide; 0.038, showing your method.', 'marks':3, 'space':36},

 {'text':'Work out &nbsp;14 &times; ' + mx(1,5,7) + '.', 'marks':3, 'space':36},

 {'text':'Work out &nbsp;10 &divide; ' + fr(2,7) + '.', 'marks':3, 'space':36},

 {'text':'Temperatures in degrees Celsius (<i>C</i>) and degrees Fahrenheit (<i>F</i>) are '
         'connected by <i>F</i> = 1.8<i>C</i> + 32.', 'marks':3,
  'parts':[{'label':'(a)','text':'Find <i>F</i> when <i>C</i> = 25.','marks':1,'space':24},
           {'label':'(b)','text':'Find <i>C</i> when <i>F</i> = 5.','marks':2,'space':32}]},

 {'text':'Expand and simplify &nbsp;7(2<i>x</i> &minus; 3) &minus; 4(2<i>x</i> &minus; 6).',
  'marks':3, 'space':36},

 {'text':'Solve &nbsp;4(2<i>x</i> &minus; 3) = 3(<i>x</i> + 6). &nbsp;Show every step.',
  'marks':3, 'space':40},

 {'text':'A car is bought for ' + RS + '640 000. One year later it is worth ' + RS + '544 000. '
         'Work out the percentage decrease in its value.', 'marks':3, 'space':38},

 {'section':SEC4, 'text':RS + '7200 is shared between Asha and Bina in the ratio 5 : 4.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out how much each of them receives.','marks':2,'space':32},
           {'label':'(b)','text':'Asha then gives 15% of her share to Bina. Work out how much she gives.','marks':1,'space':24},
           {'label':'(c)','text':'Work out how much each of them has now.','marks':2,'space':30}],
  'tip':'Your answer to (c) should still add up to 7200. If it does not, one of the two amounts is wrong.'},

 {'text':'A rectangle has a perimeter of 58 cm. Its length is 5 cm more than twice its width. '
         'The width is <i>w</i> cm.', 'marks':5,
  'parts':[{'label':'(a)','text':'Form an equation in <i>w</i>.','marks':2,'space':30},
           {'label':'(b)','text':'Solve your equation to find the width.','marks':2,'space':32},
           {'label':'(c)','text':'Write down the length of the rectangle.','marks':1,'space':22}]},

 {'text':'A machine fills bottles that each hold 0.35 litres. In one run it uses 91 litres of juice.',
  'marks':5,
  'parts':[{'label':'(a)','text':'Work out how many bottles it fills in one run.','marks':3,'space':38},
           {'label':'(b)','text':'The juice costs ' + RS + '8 per litre. Work out the cost of the '
                                 'juice in one bottle.','marks':2,'space':30}]},

 {'text':'<i>n</i> = 2<super>2</super> &times; 3 &times; 5<super>2</super> &nbsp;&nbsp;&nbsp; '
         '<i>m</i> = 2<super>3</super> &times; 3<super>2</super> &times; 5', 'marks':5,
  'parts':[{'label':'(a)','text':'Find the highest common factor (HCF) of <i>n</i> and <i>m</i>.','marks':2,'space':28},
           {'label':'(b)','text':'Find the lowest common multiple (LCM) of <i>n</i> and <i>m</i>.','marks':2,'space':28},
           {'label':'(c)','text':'Write <i>n</i> as an ordinary number.','marks':1,'space':18}],
  'tip':'You do not need to work out <i>n</i> and <i>m</i> first. Compare the indices.'},

 {'text':'A laptop costs ' + RS + '45 000. In a sale its price is reduced by 20%. After the sale '
         'the reduced price is increased by 25%.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out the sale price.','marks':2,'space':26},
           {'label':'(b)','text':'Work out the price after the increase.','marks':2,'space':26},
           {'label':'(c)','text':'Write down the overall percentage change from ' + RS + '45 000.','marks':1,'space':18}]},

 {'text':'Rahul has handed in this homework. Both answers are wrong. For each one, say what he did '
         'wrong and then write the correct answer.', 'marks':5,
  'parts':[{'label':'(a)','text':'&ldquo;The counters are red : blue = 3 : 5, so ' + fr(3,5) +
                                 ' of the counters are red.&rdquo;','marks':2,'space':30},
           {'label':'(b)','text':'&ldquo;4 &minus; 2(<i>x</i> &minus; 5) = 4 &minus; 2<i>x</i> '
                                 '&minus; 10 = &minus;2<i>x</i> &minus; 6&rdquo;','marks':3,'space':36}],
  'tip':'A mark for spotting the mistake, a mark for fixing it. Naming the rule he broke is worth more than writing the right number.'},
]

DP = {'eyebrow':EYEBROW, 'title':TOPIC + ' &mdash; Paper D',
      'meta':'Hard · Non-calculator · 75 minutes · 80 marks', 'marks':80,
      'instructions':INSTR_HARD, 'footer':'Paper D · Hard · Units 1, 2, 3, 4, 7, 10, 12',
      'endnote':END_HARD, 'questions':D_Q}


# ============================================================ MARK SCHEMES
SCHEME_A = {'title':'Paper A &mdash; Medium', 'meta':'80 marks · 75 minutes', 'questions':[
 {'n':'1', 'marks':5, 'lines':[
   '(a) 2<super>2</super> &times; 3 &times; 7' + B(1),
   '(b) 42' + B(1) + ' &nbsp;·&nbsp; (c) 6' + B(1) + ' &nbsp;·&nbsp; (d) 81' + B(1) +
   ' &nbsp;·&nbsp; (e) 4.5' + B(1)],
  'note':'(a) without index form (2 &times; 2 &times; 3 &times; 7) is still worth the mark here — the '
         'question asks for index form, but Unit 1.1 is the skill being tested. In (d), 12 means he has '
         'multiplied 3 by 4 instead of raising it; that is a 1.4 failure, not an arithmetic slip.'},
 {'n':'2', 'marks':5, 'lines':[
   '(a) 6.5' + B(1) + ' &nbsp;·&nbsp; (b) 0.12' + B(1) + ' &nbsp;·&nbsp; (c) 0.375' + B(1),
   '(d) 3 : 4' + B(1) + ' &nbsp;·&nbsp; (e) 3<i>x</i> + 15' + B(1)],
  'note':'1.2 in (b) is the standard error — counting one decimal place instead of two. 3<i>x</i> + 5 in '
         '(e) means he multiplied only the first term; that same error reappears in Q16 and Q24, so check '
         'whether it is consistent before calling it careless.'},
 {'n':'3', 'marks':2, 'lines':['(a) HCF = 6' + B(1), '(b) LCM = 36' + B(1)],
  'note':'Swapping the two is the whole error in 1.1. If HCF = 36 and LCM = 6 he knows both methods and '
         'has attached the wrong name to each — one mark, and a five-minute conversation, not a re-teach.'},
 {'n':'4', 'marks':2, 'lines':['2<super>5+3&minus;6</super> = 2<super>2</super>' + B(1), '= <b>4</b>' + B(1)],
  'note':'2<super>2</super> left as the final answer still earns both marks only if the question asked for '
         'index form — it did not, so the second mark needs the 4. Getting 2<super>15</super> means he '
         'multiplied the indices instead of adding them.'},
 {'n':'5', 'marks':2, 'lines':['(a) 62' + B(1), '(b) 0.062' + B(1)],
  'note':'This is 3.1 in one line: dividing by 0.1 makes a number ten times <i>bigger</i>. If (a) is 0.62 '
         'he has treated &divide; 0.1 as &divide; 10, which is the single most common error in Unit 3.'},
 {'n':'6', 'marks':2, 'lines':['Writing all four to 3 d.p.: 0.680, 0.700, 0.702, 0.710' + B(1),
                               '<b>0.68, 0.7, 0.702, 0.71</b>' + B(1)],
  'note':'Putting 0.68 last means he is reading longer as larger. Award the first mark if the digits are '
         'lined up correctly even when the final order is wrong.'},
 {'n':'7', 'marks':2, 'lines':['Common denominator 24: ' + fr(16,24) + ', ' + fr(15,24) + ', ' +
                               fr(14,24) + ', ' + fr(18,24) + B(1),
                               '<b>' + fr(7,12) + ', ' + fr(5,8) + ', ' + fr(2,3) + ', ' + fr(3,4) +
                               '</b>' + B(1)],
  'note':'The answer must be given in the original fractions, not the twenty-fourths. ' + fr(5,8) +
         ' and ' + fr(7,12) + ' are the close pair; getting those two the wrong way round is a 7.2 error, '
         'while a wrong common denominator is a 1.1 error. They need different fixes.'},
 {'n':'8', 'marks':2, 'lines':[fr(17,4) + ' &minus; ' + fr(11,6) + ' = ' + fr(51,12) + ' &minus; ' +
                               fr(22,12) + B(1), '= ' + fr(29,12) + ' = <b>' + mx(2,5,12) + '</b>' + B(1)],
  'note':'A quarter minus five sixths is negative, so this needs a borrow. An answer of ' + mx(3,7,12) +
         ' means he subtracted the smaller fraction from the larger regardless of which was on top — the '
         'defining 7.3 error.'},
 {'n':'9', 'marks':2, 'lines':['4<i>p</i> + 2(<i>p</i> + 3)' + B(1),
                               '= <b>6<i>p</i> + 6</b>' + B(1)],
  'note':'The unsimplified form earns the first mark on its own. 4<i>p</i> + 2<i>p</i> + 3 means he '
         'multiplied only the <i>p</i> inside the bracket — the same 2.3 error as Q2(e).'},
 {'n':'10', 'marks':2, 'lines':['(a) 3(2<i>x</i> + 5)' + B(1),
                                '(b) 4<i>y</i>(2<i>y</i> &minus; 3)' + B(1)],
  'note':'In (b), 4(2<i>y</i><super>2</super> &minus; 3<i>y</i>) is not fully factorised — no mark. '
         'Taking out only <i>y</i> or only 4 is the 2.4 error worth naming out loud.'},
 {'n':'11', 'marks':3, 'lines':['(a) 24' + B(1), '(b) &minus;10' + B(1), '(c) &minus;6' + B(1)],
  'note':'These three sit together on purpose. If (a) is &minus;24 and (b) is &minus;10 he is applying the '
         'multiplication rule to a subtraction, or has not learned it at all. Two right and one wrong is '
         'carelessness; (a) wrong is a 1.2 gap.'},
 {'n':'12', 'marks':3, 'lines':['Multiply both by 100: 468 &divide; 12' + B(1),
                                '468 &divide; 12 = 39' + B(1), '= <b>39</b>' + B(1)],
  'note':'Any correct equivalent-fraction method earns the first mark. An answer near 0.39 means he moved '
         'the point in only one of the two numbers, which is the 4.3 error.'},
 {'n':'13', 'marks':3, 'lines':['6 &times; ' + fr(11,4) + B(1), '= ' + fr(66,4) + ' = ' + fr(33,2) + B(1),
                                '= <b>' + mx(16,1,2) + '</b>' + B(1)],
  'note':'Partitioning (6 &times; 2) + (6 &times; ' + fr(3,4) + ') = 12 + ' + mx(4,1,2) +
         ' is equally valid and reaches the same place. An answer of ' + mx(12,3,4) +
         ' means he multiplied the whole number and left the fraction alone — the 7.4 error.'},
 {'n':'14', 'marks':3, 'lines':['8 &divide; ' + fr(2,5) + ' = 8 &times; ' + fr(5,2) + B(1),
                                '= ' + fr(40,2) + B(1), '= <b>20</b>' + B(1)],
  'note':'An answer of ' + fr(16,5) + ' means he multiplied by ' + fr(2,5) + ' instead of inverting. '
         'The sanity check — dividing by something smaller than 1 must give an answer bigger than 8 — is '
         'worth more to him than the rule itself.'},
 {'n':'15', 'marks':3, 'lines':['(a) <i>C</i> = 40 &times; 12 + 250' + B(1), '&nbsp; &nbsp; &nbsp;= <b>730</b>' + B(1),
                                '(b) 40<i>n</i> = 800, so <i>n</i> = <b>20</b>' + B(1)],
  'note':'(b) is 2.2 run backwards and is where the marks go. Dividing 1050 by 40 without subtracting the '
         '250 first gives 26.25 — a non-integer answer he should have questioned.'},
 {'n':'16', 'marks':3, 'lines':['10<i>x</i> &minus; 15' + B(1), '&minus;2<i>x</i> + 8' + B(1),
                                '= <b>8<i>x</i> &minus; 7</b>' + B(1)],
  'note':'&minus;2 &times; &minus;4 is <b>+8</b>. An answer of 8<i>x</i> &minus; 23 is the sign error and '
         'is worth two of the three marks. This is the single most repeated 2.3 error across all four papers.'},
 {'n':'17', 'marks':3, 'lines':['5<i>x</i> &minus; 3<i>x</i> = 19 &minus; 7' + B(1), '2<i>x</i> = 12' + B(1),
                                '<i>x</i> = <b>6</b>' + B(1)],
  'note':'Any correct route earns the marks. Moving a term without changing its sign gives <i>x</i> = 13 '
         'or <i>x</i> = 3.25; both are 2.5 errors, and the check (both sides equal 37) would have caught them.'},
 {'n':'18', 'marks':3, 'lines':['15% of 840 = 126' + B(1), '840 + 126' + B(1), '= <b>' + RS + '966</b>' + B(1)],
  'note':'840 &times; 1.15 in one line earns all three. An answer of 126 is the 10.1 error — he has found '
         'the increase and stopped, which the word &ldquo;new price&rdquo; asked him not to.'},
 {'n':'19', 'marks':5, 'lines':[
   '(a) 3 + 5 = 8 parts, 3600 &divide; 8 = 450' + B(1),
   '&nbsp; &nbsp; &nbsp;Asha <b>' + RS + '1350</b>, Bela <b>' + RS + '2250</b>' + B(1),
   '(b) 2250 &times; 1.2' + B(1) + ' = <b>' + RS + '2700</b>' + B(1),
   '(c) 2700 &minus; 1350 = <b>' + RS + '1350</b>' + B(1)],
  'note':'Dividing 3600 by 2 instead of by 8 is the 12.2 error. Note that (c) comes out at exactly 1350, '
         'the same as Asha&rsquo;s share — a coincidence, not a method. Do not let him treat it as a check.'},
 {'n':'20', 'marks':5, 'lines':[
   '(a) 4<i>n</i> &minus; 7 = <i>n</i> + 11' + B(2),
   '(b) 3<i>n</i> = 18' + B(1) + ' &nbsp;·&nbsp; <i>n</i> = <b>6</b>' + B(1),
   '&nbsp; &nbsp; &nbsp;Check: 4 &times; 6 &minus; 7 = 17 and 6 + 11 = 17' + B(1)],
  'note':'The check is a mark in its own right and he will skip it. In (a), 4<i>n</i> &minus; 7 = 11 '
         'misses the phrase &ldquo;the number he first thought of&rdquo; — a 2.1 reading error, not algebra. '
         'Award one of the two marks.'},
 {'n':'21', 'marks':5, 'lines':[
   '(a) Shop A: 96 &divide; 1.5 = <b>' + RS + '64 per kg</b>' + B(2),
   '&nbsp; &nbsp; &nbsp;Shop B: 155 &divide; 2.5 = <b>' + RS + '62 per kg</b>' + B(1),
   '(b) <b>Shop B</b>' + B(1), '(c) 6 &times; 62 = <b>' + RS + '372</b>' + B(1)],
  'note':'Comparing kilograms per rupee instead is valid and reaches the same answer — do not penalise it. '
         'Two correct prices with no sentence naming the shop drops the (b) mark, which is the 12.3 habit '
         'worth drilling.'},
 {'n':'22', 'marks':5, 'lines':[
   '(a) Multiples of 12: 12, 24, 36 &nbsp;·&nbsp; of 18: 18, 36' + B(2),
   '&nbsp; &nbsp; &nbsp;LCM = <b>36 seconds</b>' + B(1),
   '(b) <b>9:00:36</b>' + B(1),
   '(c) 360 &divide; 36 = <b>10 times</b>' + B(1)],
  'note':'This is Q3 wearing a costume — the same LCM, now without the word. If he found 36 in Q3 and not '
         'here, the gap is 12.3 comprehension, not 1.1. Using 12 &times; 18 = 216 gives a time that is '
         'technically a common multiple but not the lowest; one mark.'},
 {'n':'23', 'marks':5, 'lines':[
   '(a) 800 &times; 1.25' + B(1) + ' = <b>' + RS + '1000</b>' + B(1),
   '(b) 1000 &times; 0.8' + B(1) + ' = <b>' + RS + '800</b>' + B(1),
   '(c) <b>No change (0%)</b>' + B(1)],
  'note':'The point of the question is that it lands exactly back on 800 — a 25% rise is undone by a 20% '
         'fall, not a 25% one. If he answers 5% decrease in (c) he has subtracted the percentages, which '
         'is the 10.2 error. Make him check (b) against his own answer.'},
 {'n':'24', 'marks':5, 'lines':[
   '(a) 3(<i>x</i> + 4)' + B(1) + ' = <b>3<i>x</i> + 12</b> cm<super>2</super>' + B(1),
   '(b) 2(<i>x</i> + 4) + 2(3)' + B(1) + ' = <b>2<i>x</i> + 14</b> cm' + B(1),
   '(c) <b>2(<i>x</i> + 7)</b>' + B(1)],
  'note':'Three units in one question: 2.2 to build it, 2.3 to expand it, 2.4 to put the bracket back. '
         'Forgetting that a perimeter has two lengths <i>and</i> two widths gives <i>x</i> + 7, which '
         'still factorises to nothing — if (c) is blank, check (b) first.'},
]}

SCHEME_B = {'title':'Paper B &mdash; Medium', 'meta':'80 marks · 75 minutes', 'questions':[
 {'n':'1', 'marks':5, 'lines':[
   '(a) 2 &times; 3<super>2</super> &times; 5' + B(1),
   '(b) 40' + B(1) + ' &nbsp;·&nbsp; (c) 14' + B(1) + ' &nbsp;·&nbsp; (d) 5<super>2</super>' + B(1) +
   ' &nbsp;·&nbsp; (e) 73' + B(1)],
  'note':'(d) asks for a single power, so 25 alone does not earn it — the 1.4 skill is subtracting the '
         'indices, not evaluating. (e) is the same &divide; 0.1 test as Paper A Q5; compare the two scripts.'},
 {'n':'2', 'marks':5, 'lines':[
   '(a) 35 000' + B(1) + ' &nbsp;·&nbsp; (b) 0.03' + B(1) + ' &nbsp;·&nbsp; (c) 0.5&#775;' + B(1),
   '(d) 5 : 7' + B(1) + ' &nbsp;·&nbsp; (e) 7(<i>x</i> &minus; 3)' + B(1)],
  'note':'(a) 34 000 means he rounded on the wrong digit. In (c) the dot must sit over the 5; 0.56 or 0.6 '
         'is a 7.1 error. (d) needs 7 spotted as the common factor — 35 : 49 resists the obvious 5 and 2.'},
 {'n':'3', 'marks':2, 'lines':['(a) HCF = 10' + B(1), '(b) LCM = 60' + B(1)],
  'note':'20 and 30 both being multiples of 10 makes this the easy case. If he misses it here he will miss '
         'Q22 as well, where the same 1.1 idea is buried in a floor-tiling problem.'},
 {'n':'4', 'marks':2, 'lines':['(3<super>2</super>)<super>3</super> = 3<super>6</super>, so '
                               '3<super>6</super> &divide; 3<super>4</super> = 3<super>2</super>' + B(1),
                               '= <b>9</b>' + B(1)],
  'note':'3<super>5</super> means he added the indices instead of multiplying them for the outer power — '
         'the 1.4 error that separates a power of a power from a product of powers.'},
 {'n':'5', 'marks':2, 'lines':['(a) 48' + B(1), '(b) 3.5' + B(1)],
  'note':'Dividing by 0.01 multiplies by 100; multiplying by 0.01 divides by 100. If both answers move the '
         'point the same way he has the direction rule, not the operation rule.'},
 {'n':'6', 'marks':2, 'lines':['All to 4 d.p.: 0.5000, 0.5005, 0.5050, 0.5500' + B(1),
                               '<b>0.5, 0.5005, 0.505, 0.55</b>' + B(1)],
  'note':'0.5005 and 0.505 are the trap. Ranking by how many digits each has puts them in exactly the '
         'wrong order, which is the 4.1 error this set of numbers was chosen to catch.'},
 {'n':'7', 'marks':2, 'lines':['Common denominator 20: ' + fr(12,20) + ', ' + fr(14,20) + ', ' +
                               fr(11,20) + ', ' + fr(13,20) + B(1),
                               '<b>' + fr(11,20) + ', ' + fr(3,5) + ', ' + fr(13,20) + ', ' + fr(7,10) +
                               '</b>' + B(1)],
  'note':'Two of the four are already in twentieths, so this is a gentler 7.2 than Paper A Q7. Answering in '
         'twentieths instead of the original fractions costs the second mark.'},
 {'n':'8', 'marks':2, 'lines':[fr(16,3) + ' &minus; ' + fr(11,4) + ' = ' + fr(64,12) + ' &minus; ' +
                               fr(33,12) + B(1), '= ' + fr(31,12) + ' = <b>' + mx(2,7,12) + '</b>' + B(1)],
  'note':'Needs a borrow, like Paper A Q8. ' + mx(3,5,12) + ' is the flipped-subtraction answer. If he gets '
         'one of the two papers right and not the other, it is confidence, not method.'},
 {'n':'9', 'marks':2, 'lines':['3<i>n</i> + 4(<i>n</i> &minus; 5)' + B(1),
                               '= <b>7<i>n</i> &minus; 20</b>' + B(1)],
  'note':'&ldquo;5 less than&rdquo; is <i>n</i> &minus; 5, not 5 &minus; <i>n</i>. Reversing it gives '
         '20 &minus; <i>n</i> and is a 2.1 reading error — mark it as comprehension, not algebra.'},
 {'n':'10', 'marks':2, 'lines':['8<i>x</i> + 12 + 3<i>x</i> &minus; 15' + B(1),
                                '= <b>11<i>x</i> &minus; 3</b>' + B(1)],
  'note':'Both brackets are added here, so there is no sign trap — this is the control question for Q16 on '
         'the same paper, which does have one. Getting this right and Q16 wrong isolates the sign rule.'},
 {'n':'11', 'marks':3, 'lines':['(a) 45' + B(1), '(b) &minus;14' + B(1), '(c) &minus;8' + B(1)],
  'note':'Same trio as Paper A Q11 with different numbers. (c) has one negative, so the answer is negative; '
         'if he writes 8 he has applied &ldquo;two negatives make a positive&rdquo; to a single one.'},
 {'n':'12', 'marks':3, 'lines':['Multiply both by 100: 576 &divide; 24' + B(1),
                                '576 &divide; 24 = 24' + B(1), '= <b>24</b>' + B(1)],
  'note':'The answer happening to equal the 24 in the divisor is a coincidence worth pointing out before he '
         'decides it is a pattern.'},
 {'n':'13', 'marks':3, 'lines':['8 &times; ' + fr(17,5) + B(1), '= ' + fr(136,5) + B(1),
                                '= <b>' + mx(27,1,5) + '</b>' + B(1)],
  'note':'Partitioning to 24 + ' + mx(3,1,5) + ' is equally valid. Leaving ' + fr(136,5) +
         ' as the final answer costs the last mark only because the question asked for a mixed number.'},
 {'n':'14', 'marks':3, 'lines':['12 &divide; ' + fr(3,4) + ' = 12 &times; ' + fr(4,3) + B(1),
                                '= ' + fr(48,3) + B(1), '= <b>16</b>' + B(1)],
  'note':'An answer of 9 means he multiplied by ' + fr(3,4) + '. The 7.5 check is that the answer must be '
         'bigger than 12, and it takes two seconds.'},
 {'n':'15', 'marks':3, 'lines':['(a) 3(7) + 2(&minus;4) = 21 &minus; 8' + B(1), '&nbsp; &nbsp; &nbsp;= <b>13</b>' + B(1),
                                '(b) 3<i>a</i> + 8 = 26, so <i>a</i> = <b>6</b>' + B(1)],
  'note':'(a) crosses 2.2 with 1.2 — 2 &times; &minus;4 is &minus;8, so the terms subtract. An answer of 29 '
         'means he added. (b) is the formula run backwards and is the harder mark.'},
 {'n':'16', 'marks':3, 'lines':['6<i>x</i> &minus; 12' + B(1), '&minus;6<i>x</i> + 15' + B(1),
                                '= <b>3</b>' + B(1)],
  'note':'The <i>x</i> terms cancel completely and the answer is a number. He will distrust that and go '
         'looking for a mistake. An answer of 3 &minus; 12<i>x</i> means &minus;3 &times; &minus;5 was '
         'taken as &minus;15 — the 2.3 sign error again.'},
 {'n':'17', 'marks':3, 'lines':['3<i>x</i> + 12 = 5<i>x</i> &minus; 2' + B(1), '14 = 2<i>x</i>' + B(1),
                                '<i>x</i> = <b>7</b>' + B(1)],
  'note':'Expanding the bracket first is the only reliable route. Collecting <i>x</i> on the right avoids '
         'a negative coefficient — worth showing him, because he will otherwise fight &minus;2<i>x</i> = &minus;14.'},
 {'n':'18', 'marks':3, 'lines':['35% of 640 = 224' + B(1), '640 &minus; 224' + B(1),
                                '= <b>' + RS + '416</b>' + B(1)],
  'note':'640 &times; 0.65 in one line earns all three and is the 10.2 method. An answer of 224 is the '
         'decrease, not the new price — the same stop-too-early error as Paper A Q18.'},
 {'n':'19', 'marks':5, 'lines':[
   '(a) 2 + 5 = 7 parts, 4200 &divide; 7 = 600' + B(1),
   '&nbsp; &nbsp; &nbsp;Kiran <b>' + RS + '1200</b>, Leela <b>' + RS + '3000</b>' + B(1),
   '(b) 1200 &times; 0.75' + B(1) + ' = <b>' + RS + '900</b>' + B(1),
   '(c) 3000 &minus; 900 = <b>' + RS + '2100</b>' + B(1)],
  'note':'Reading 2 : 5 as &ldquo;two fifths to Kiran&rdquo; gives 1680 and is the defining 12.1 error. '
         'It reappears in Paper D Q24(a) as a statement to diagnose.'},
 {'n':'20', 'marks':5, 'lines':[
   '(a) <i>x</i> + (3<i>x</i> &minus; 8) = 64' + B(2),
   '(b) 4<i>x</i> = 72' + B(1) + ' &nbsp;·&nbsp; <i>x</i> = <b>18</b>' + B(1),
   '(c) 3(18) &minus; 8 = <b>46</b>' + B(1)],
  'note':'&ldquo;8 fewer than three times&rdquo; is 3<i>x</i> &minus; 8, not 3(<i>x</i> &minus; 8). The '
         'second form gives <i>x</i> = 22 and a brother with 42 — which still sums to 64, so the check does '
         'not catch it. That is why (a) carries two marks.'},
 {'n':'21', 'marks':5, 'lines':[
   '(a) Shop A: 245 &divide; 2.5 = <b>' + RS + '98 per litre</b>' + B(2),
   '&nbsp; &nbsp; &nbsp;Shop B: 380 &divide; 4 = <b>' + RS + '95 per litre</b>' + B(1),
   '(b) <b>Shop B</b>' + B(1), '(c) 10 &times; 95 = <b>' + RS + '950</b>' + B(1)],
  'note':'Shop A looks cheaper because the price is smaller. That is the trap and it is 12.3, not arithmetic. '
         'Dividing 245 by 2.5 also tests 4.3 — if that division is where it broke, the ratio work is fine.'},
 {'n':'22', 'marks':5, 'lines':[
   '(a) The tile must divide both 60 and 84, so find the HCF' + B(1),
   '&nbsp; &nbsp; &nbsp;60 = 2<super>2</super> &times; 3 &times; 5, 84 = 2<super>2</super> &times; 3 &times; 7' + B(1),
   '&nbsp; &nbsp; &nbsp;HCF = <b>12 cm</b>' + B(1),
   '(b) (60 &divide; 12) &times; (84 &divide; 12) = 5 &times; 7' + B(1) + ' = <b>35 tiles</b>' + B(1)],
  'note':'The word HCF never appears, which is the whole test. Using the LCM gives 420 cm — a tile larger '
         'than the floor, and he should notice. In (b), 5 + 7 = 12 instead of 5 &times; 7 is an area-versus-'
         'perimeter confusion worth naming.'},
 {'n':'23', 'marks':5, 'lines':[
   '(a) 1500 &times; 1.2 = <b>' + RS + '1800</b>' + B(1),
   '(b) 1800 &times; 0.8' + B(1) + ' = <b>' + RS + '1440</b>' + B(1),
   '(c) 1500 &minus; 1440 = 60, and 60 &divide; 1500' + B(1) + ' = <b>4% decrease</b>' + B(1)],
  'note':'A 20% rise followed by a 20% fall loses 4%, because the fall is taken off a bigger number. '
         'Answering &ldquo;no change&rdquo; in (c) is the 10.2 error, and it is the exact opposite of the '
         'trap in Paper A Q23 — where it genuinely was no change. Check he has a reason, not a habit.'},
 {'n':'24', 'marks':5, 'lines':[
   '(a) 5(2<i>x</i> &minus; 1)' + B(1) + ' = <b>10<i>x</i> &minus; 5</b> cm<super>2</super>' + B(1),
   '(b) 2(2<i>x</i> &minus; 1) + 2(5)' + B(1) + ' = <b>4<i>x</i> + 8</b> cm' + B(1),
   '(c) <b>4(<i>x</i> + 2)</b>' + B(1)],
  'note':'&minus;1 &times; 2 = &minus;2, then +10 gives +8. An answer of 4<i>x</i> + 12 means he forgot to '
         'double the &minus;1. In (c), 2(2<i>x</i> + 4) is not fully factorised — the 2.4 error.'},
]}

SCHEME_C = {'title':'Paper C &mdash; Hard', 'meta':'80 marks · 75 minutes', 'questions':[
 {'n':'1', 'marks':5, 'lines':[
   '(a) 37' + B(1) + ' &nbsp;·&nbsp; (b) &minus;24' + B(1) + ' &nbsp;·&nbsp; (c) 11' + B(1),
   '(d) 2<super>6</super>' + B(1) + ' &nbsp;·&nbsp; (e) 6' + B(1)],
  'note':'(a) 39 is not prime (3 &times; 13) and is the answer he will reach by looking for &ldquo;odd and '
         'near 40&rdquo;. (b) has three negatives, so the answer is negative — two negatives cancelling and '
         'one being left over is the 1.2 idea. (d) needs 4 = 2<super>2</super> spotted first.'},
 {'n':'2', 'marks':5, 'lines':[
   '(a) 0.05' + B(1) + ' &nbsp;·&nbsp; (b) 0.002' + B(1) + ' &nbsp;·&nbsp; (c) 0.6&#775;3&#775;' + B(1),
   '(d) 1 : 2' + B(1) + ' &nbsp;·&nbsp; (e) 6<i>x</i>(2<i>x</i> &minus; 3)' + B(1)],
  'note':'(a) 0.04 means he truncated instead of rounding, and 0.0498 was chosen because it rounds up '
         'twice over. In (c) both digits recur, so two dots. (d) needs the units converted first — 750 : 1.5 '
         'is the 12.1 error and gives 500 : 1.'},
 {'n':'3', 'marks':2, 'lines':['(a) HCF = 12' + B(1), '(b) LCM = 72' + B(1)],
  'note':'24 and 36 share 12, and 72 is only twice 36 — both answers are close enough to the inputs that a '
         'guess looks plausible. Insist on the prime factorisation being visible.'},
 {'n':'4', 'marks':2, 'lines':['2<super>8</super> &divide; 2<super>6</super> = 2<super>2</super>' + B(1),
                               '= <b>4</b>' + B(1)],
  'note':'Two indices to add on top and two on the bottom before anything is subtracted. Working the '
         'brackets out as numbers (256 &divide; 64) is valid and earns both marks, but he should be nudged '
         'to the 1.4 route.'},
 {'n':'5', 'marks':2, 'lines':['(a) 360' + B(1), '(b) 0.007' + B(1)],
  'note':'(b) multiplying by 0.1 makes it smaller, and 0.07 is already small — an answer of 0.7 is the '
         'direction error. Together these two are the whole of 3.1.'},
 {'n':'6', 'marks':2, 'lines':['All to 4 d.p.: 0.4100, 0.4010, 0.4000, 0.0409' + B(1),
                               '<b>0.41, 0.401, 0.4, 0.0409</b>' + B(1)],
  'note':'Descending, not ascending — he will answer the question he expected. 0.0409 has the most digits '
         'and is the smallest by a long way; if he puts it first he has not looked at the leading zero.'},
 {'n':'7', 'marks':2, 'lines':['Common denominator 36: ' + fr(30,36) + ', ' + fr(28,36) + ', ' +
                               fr(33,36) + ', ' + fr(26,36) + B(1),
                               '<b>' + fr(13,18) + ', ' + fr(7,9) + ', ' + fr(5,6) + ', ' + fr(11,12) +
                               '</b>' + B(1)],
  'note':'All four are close, and 36 is the only denominator that works for all of them. Using 216 (the '
         'product) is slower but correct — full marks, and a word about it afterwards.'},
 {'n':'8', 'marks':2, 'lines':[fr(37,6) + ' &minus; ' + fr(23,8) + ' = ' + fr(148,24) + ' &minus; ' +
                               fr(69,24) + B(1), '= ' + fr(79,24) + ' = <b>' + mx(3,7,24) + '</b>' + B(1)],
  'note':'Denominators 6 and 8 need 24, not 48 — using 48 still works and costs nothing but time. The 7.3 '
         'borrow is unavoidable here because ' + fr(1,6) + ' &lt; ' + fr(7,8) + '.'},
 {'n':'9', 'marks':2, 'lines':['Length = <i>w</i> + 3, so perimeter = 2<i>w</i> + 2(<i>w</i> + 3)' + B(1),
                               '= <b>4<i>w</i> + 6</b>' + B(1)],
  'note':'No diagram is given, which is the difficulty. An answer of 2<i>w</i> + 3 means he added a length '
         'and a width and stopped. 4<i>w</i> + 3 means he doubled the bracket but not the 3.'},
 {'n':'10', 'marks':2, 'lines':['6<i>x</i> &minus; 15 &minus; 12 + 4<i>x</i>' + B(1),
                                '= <b>10<i>x</i> &minus; 27</b>' + B(1)],
  'note':'&minus;4(3 &minus; <i>x</i>) = &minus;12 <b>+</b> 4<i>x</i>. The <i>x</i> is second inside the '
         'bracket and its sign flips, which is the hardest form of the 2.3 error. 2<i>x</i> &minus; 27 is '
         'the expected wrong answer.'},
 {'n':'11', 'marks':3, 'lines':['(a) 21' + B(1), '(b) &minus;4' + B(1), '(c) 15' + B(1)],
  'note':'(b) subtracting a negative adds. &minus;10 means he treated &minus;(&minus;3) as &minus;3. '
         'This is the 1.2 case the other three papers do not test.'},
 {'n':'12', 'marks':3, 'lines':['Multiply both by 1000: 918 &divide; 27' + B(1),
                                '918 &divide; 27 = 34' + B(1), '= <b>34</b>' + B(1)],
  'note':'Three decimal places to shift in both numbers. Shifting by different amounts is the 4.3 error and '
         'gives 3.4 or 340 — both look plausible, which is the point of choosing these numbers.'},
 {'n':'13', 'marks':3, 'lines':['15 &times; ' + fr(14,5) + B(1), '= ' + fr(210,5) + B(1), '= <b>42</b>' + B(1)],
  'note':'Cancelling the 15 against the 5 first gives 3 &times; 14 = 42 in one step. The answer is a whole '
         'number, which he will not expect from a mixed number and may talk himself out of.'},
 {'n':'14', 'marks':3, 'lines':['9 &divide; ' + fr(3,8) + ' = 9 &times; ' + fr(8,3) + B(1),
                                '= ' + fr(72,3) + B(1), '= <b>24</b>' + B(1)],
  'note':'Another whole-number answer. If he gets Q13 and Q14 right on this paper but not the equivalents '
         'on Paper A, it is because these cancel cleanly — not because 7.4 and 7.5 are secure.'},
 {'n':'15', 'marks':3, 'lines':['(a) 2(9 + 6.5) = 2(15.5) = <b>31</b>' + B(1),
                                '(b) 2(13 + <i>w</i>) = 46, so 13 + <i>w</i> = 23' + B(1),
                                '&nbsp; &nbsp; &nbsp;<i>w</i> = <b>10</b>' + B(1)],
  'note':'(b) is 2.2 backwards. Dividing 46 by 2 first is the clean route; expanding to 26 + 2<i>w</i> = 46 '
         'is equally fine. Subtracting 13 from 46 before halving gives 16.5 and is the error to watch for.'},
 {'n':'16', 'marks':3, 'lines':['12<i>x</i> + 20 &minus; 4<i>x</i> + 10' + B(1),
                                '= 8<i>x</i> + 30' + B(1), '= <b>2(4<i>x</i> + 15)</b>' + B(1)],
  'note':'Two units in one question: expand, then factorise what comes out. &minus;2 &times; &minus;5 = '
         '<b>+10</b>. If he reaches 8<i>x</i> + 10 he will factorise to 2(4<i>x</i> + 5) and lose only the '
         'middle mark — award the third for a correct factorisation of his own wrong expression.'},
 {'n':'17', 'marks':3, 'lines':['6<i>x</i> &minus; 2 = 4<i>x</i> + 12' + B(1), '2<i>x</i> = 14' + B(1),
                                '<i>x</i> = <b>7</b>' + B(1)],
  'note':'Brackets on both sides. Dividing through by 2 at the start gives 3<i>x</i> &minus; 1 = 2(<i>x</i> '
         '+ 3) and is quicker — worth showing him, but not required.'},
 {'n':'18', 'marks':3, 'lines':['18% of 1250 = 225' + B(1), '1250 &minus; 225' + B(1),
                                '= <b>' + RS + '1025</b>' + B(1)],
  'note':'1250 &times; 0.82 earns all three. 18% is awkward without a calculator: 10% = 125, 8% = 100. If he '
         'reaches for long multiplication instead of partitioning, that is the 10.2 habit to fix.'},
 {'n':'19', 'marks':5, 'lines':[
   '(a) 2 + 3 + 4 = 9 parts, 9450 &divide; 9 = 1050' + B(1),
   '&nbsp; &nbsp; &nbsp;' + RS + '2100, ' + RS + '3150' + B(1) + ' and <b>' + RS + '4200</b>' + B(1),
   '(b) 4200 &times; 1.12 = <b>' + RS + '4704</b>' + B(1),
   '(c) 2100 + 3150 + 4704 = <b>' + RS + '9954</b>' + B(1)],
  'note':'(c) is where it goes wrong: the other two shares are unchanged, so only the largest is increased. '
         'Adding 12% to the whole 9450 gives 10 584 and is the error. Check the three shares in (a) sum to '
         '9450 before anything else.'},
 {'n':'20', 'marks':5, 'lines':[
   '(a) <i>x</i> + (3<i>x</i> &minus; 20) + (<i>x</i> + 40) = 180' + B(1),
   '&nbsp; &nbsp; &nbsp;5<i>x</i> + 20 = 180' + B(1) + ' &nbsp;·&nbsp; <i>x</i> = <b>32</b>' + B(1),
   '(b) Angles are 32&deg;, 76&deg; and 72&deg;' + B(1) + ' &nbsp;·&nbsp; largest = <b>76&deg;</b>' + B(1)],
  'note':'The 180 is not given and must be recalled — that is deliberate. In (b) the largest angle is '
         '3<i>x</i> &minus; 20, not <i>x</i> + 40, so he has to evaluate all three rather than guess from '
         'the expressions. Answering 32&deg; means he stopped at <i>x</i>.'},
 {'n':'21', 'marks':5, 'lines':[
   '(a) 57 &divide; 0.75 = <b>' + RS + '76</b>' + B(1) + ' &nbsp;·&nbsp; 90 &divide; 1.25 = <b>' + RS + '72</b>' + B(1),
   '&nbsp; &nbsp; &nbsp;185 &divide; 2.5 = <b>' + RS + '74</b>' + B(1),
   '(b) <b>1.25 litres</b>' + B(1),
   '(c) 5(76 &minus; 72) = <b>' + RS + '20</b>' + B(1)],
  'note':'The biggest bottle is <i>not</i> the best value, which is the whole design. Three divisions by '
         'decimals makes this 4.3 as much as 12.3. In (c) the worst value is the smallest bottle at 76 — '
         'using 74 gives ' + RS + '10 and means he compared against the wrong size.'},
 {'n':'22', 'marks':5, 'lines':[
   '(a) 15 = 3 &times; 5, 24 = 2<super>3</super> &times; 3' + B(1),
   '&nbsp; &nbsp; &nbsp;LCM = 2<super>3</super> &times; 3 &times; 5' + B(1) + ' = <b>120 days</b>' + B(1),
   '(b) 120, 240 and 360 all fall within 365' + B(1) + ' = <b>3 times</b>' + B(1)],
  'note':'15 &times; 24 = 360 is a common multiple but not the lowest, and it gives a believable 1 time in '
         '(b) — the 1.1 error this question was built around. In (b), 365 &divide; 120 = 3.04, and rounding '
         'that to 3 is right for the wrong reason; ask him to name the three dates.'},
 {'n':'23', 'marks':5, 'lines':[
   '(a) 2000 &times; 1.3 = <b>' + RS + '2600</b>' + B(1),
   '(b) 2600 &times; 0.7' + B(1) + ' = <b>' + RS + '1820</b>' + B(1),
   '(c) Loss = 2000 &minus; 1820 = 180, and 180 &divide; 2000' + B(1) + ' = <b>9% decrease</b>' + B(1)],
  'note':'1.3 &times; 0.7 = 0.91, so a 30% rise and a 30% fall lose 9%. Dividing the 180 by 1820 instead of '
         '2000 gives 9.9% and is the classic percentage-change error — the base is always the <i>original</i>. '
         'Award the first three marks only.'},
 {'n':'24', 'marks':5, 'lines':[
   '(a) 4(3<i>x</i> + 2)' + B(1) + ' = <b>12<i>x</i> + 8</b> cm<super>2</super>' + B(1),
   '(b) 2(3<i>x</i> + 2) + 2(4)' + B(1) + ' = <b>6<i>x</i> + 12</b> cm' + B(1),
   '(c) <b>6(<i>x</i> + 2)</b>' + B(1)],
  'note':'In (c), 2(3<i>x</i> + 6) and 3(2<i>x</i> + 4) are both incomplete — &ldquo;fully&rdquo; means the '
         'HCF of 6 and 12, which is 6. That is 1.1 doing the work inside a 2.4 question, and it is the mark '
         'most often dropped on this paper.'},
]}

SCHEME_D = {'title':'Paper D &mdash; Hard', 'meta':'80 marks · 75 minutes', 'questions':[
 {'n':'1', 'marks':5, 'lines':[
   '(a) 2 (they are 23 and 29)' + B(1),
   '(b) 8' + B(1) + ' &nbsp;·&nbsp; (c) 7' + B(1) + ' &nbsp;·&nbsp; (d) 9<super>7</super>' + B(1) +
   ' &nbsp;·&nbsp; (e) 50' + B(1)],
  'note':'(a) asks how many, not which — answering &ldquo;23 and 29&rdquo; is still the mark. Counting 21 '
         '(3 &times; 7) or 27 (3<super>3</super>) as prime is the 1.1 error. (d) 9<super>10</super> means '
         'he multiplied the indices.'},
 {'n':'2', 'marks':5, 'lines':[
   '(a) 7.10' + B(1) + ' &nbsp;·&nbsp; (b) 0.036' + B(1) + ' &nbsp;·&nbsp; (c) 0.26&#775;' + B(1),
   '(d) 1 : 3' + B(1) + ' &nbsp;·&nbsp; (e) 5<i>a</i>(4<i>a</i> + 3)' + B(1)],
  'note':'(a) must keep the trailing zero — 7.1 is not 2 decimal places. In (c) only the 6 recurs, so the '
         'dot goes on the 6 alone; a dot over the 2 as well is the 7.1 error. (d) needs hours converted to '
         'minutes before simplifying.'},
 {'n':'3', 'marks':2, 'lines':['(a) HCF = 9' + B(1), '(b) LCM = 90' + B(1)],
  'note':'18 and 45 share 9, not 3 — stopping at 3 is the usual 1.1 slip. Neither number divides the other, '
         'which rules out the shortcut that works on Paper B Q3.'},
 {'n':'4', 'marks':2, 'lines':['5<super>4+3&minus;5</super> = 5<super>2</super>' + B(1), '= <b>25</b>' + B(1)],
  'note':'Add the two on top, then subtract the bottom. The question asks for an ordinary number, so '
         '5<super>2</super> alone is one mark.'},
 {'n':'5', 'marks':2, 'lines':['(a) 0.62' + B(1), '(b) 6.2' + B(1)],
  'note':'The same digits appear in both answers, one hundred times apart. If he gives 0.62 twice he has '
         'read both operations as the same one — the core 3.1 confusion.'},
 {'n':'6', 'marks':2, 'lines':['All to 4 d.p.: 0.0330, 0.3003, 0.3030, 0.3300' + B(1),
                               '<b>0.033, 0.3003, 0.303, 0.33</b>' + B(1)],
  'note':'Three of the four start 0.3 and are separated only in the third and fourth places. Lining up the '
         'decimal points on paper is the method; comparing them in his head is the 4.1 error.'},
 {'n':'7', 'marks':2, 'lines':['Common denominator 24: ' + fr(21,24) + ', ' + fr(20,24) + ', ' +
                               fr(22,24) + ', ' + fr(17,24) + B(1),
                               '<b>' + fr(11,12) + ', ' + fr(7,8) + ', ' + fr(5,6) + ', ' + fr(17,24) +
                               '</b>' + B(1)],
  'note':'Descending. ' + fr(11,12) + ' and ' + fr(7,8) + ' are one twenty-fourth apart, which no amount of '
         'looking will separate. Answering in ascending order costs the second mark only.'},
 {'n':'8', 'marks':2, 'lines':[fr(37,5) + ' &minus; ' + fr(29,8) + ' = ' + fr(296,40) + ' &minus; ' +
                               fr(145,40) + B(1), '= ' + fr(151,40) + ' = <b>' + mx(3,31,40) + '</b>' + B(1)],
  'note':'Denominator 40 and an awkward numerator — the hardest 7.3 of the four papers. A whole-number part '
         'of 4 means he did 7 &minus; 3 and then took the fractions the easy way round.'},
 {'n':'9', 'marks':2, 'lines':['(a) 50 + 18<i>k</i>' + B(1), '(b) 2(50 + 18<i>k</i>) = <b>100 + 36<i>k</i></b>' + B(1)],
  'note':'(b) 100 + 18<i>k</i> means he doubled only the fixed fee. Either the bracketed or the expanded '
         'form earns the mark in (b), but the doubling must reach both terms — 2.1 into 2.3.'},
 {'n':'10', 'marks':2, 'lines':['10<i>x</i> &minus; 6 &minus; 5<i>x</i> + 10' + B(1),
                                '= <b>5<i>x</i> + 4</b>' + B(1)],
  'note':'&minus;5 &times; &minus;2 = <b>+10</b>. An answer of 5<i>x</i> &minus; 16 is the sign error, and '
         'it is the fourth appearance of that same 2.3 mistake across the set. If he has made it on all '
         'four papers it is a rule he does not have, not a slip.'},
 {'n':'11', 'marks':3, 'lines':['(a) 54' + B(1), '(b) &minus;15' + B(1), '(c) &minus;12' + B(1)],
  'note':'Same trio, fourth paper. By now the pattern across the four scripts is the useful thing: if (a) is '
         'always right and (b) sometimes wrong, the gap is in adding negatives, not multiplying them.'},
 {'n':'12', 'marks':3, 'lines':['Multiply both by 1000: 2622 &divide; 38' + B(1),
                                '2622 &divide; 38 = 69' + B(1), '= <b>69</b>' + B(1)],
  'note':'The hardest division on the four papers, and the only one where the long division itself is real '
         'work. Award the first two marks for a correct set-up even if the arithmetic then fails — that '
         'separates 4.3 from plain calculation.'},
 {'n':'13', 'marks':3, 'lines':['14 &times; ' + fr(12,7) + B(1), '= ' + fr(168,7) + B(1), '= <b>24</b>' + B(1)],
  'note':'Cancelling 14 against 7 gives 2 &times; 12 straight away. An answer of ' + mx(14,5,7) +
         ' means he multiplied the whole number and copied the fraction across — the 7.4 error.'},
 {'n':'14', 'marks':3, 'lines':['10 &divide; ' + fr(2,7) + ' = 10 &times; ' + fr(7,2) + B(1),
                                '= ' + fr(70,2) + B(1), '= <b>35</b>' + B(1)],
  'note':'Dividing by ' + fr(2,7) + ' more than triples the 10. If his answer is under 10 he has inverted '
         'the wrong number or not inverted at all — 7.5, and the estimate would have caught it.'},
 {'n':'15', 'marks':3, 'lines':['(a) 1.8(25) + 32 = 45 + 32 = <b>77</b>' + B(1),
                                '(b) 1.8<i>C</i> = 5 &minus; 32 = &minus;27' + B(1),
                                '&nbsp; &nbsp; &nbsp;<i>C</i> = &minus;27 &divide; 1.8 = <b>&minus;15</b>' + B(1)],
  'note':'(b) crosses three units: 2.2 to rearrange, 1.2 for the negative, 4.3 to divide by 1.8. A positive '
         'answer means he subtracted the wrong way round. 15 instead of &minus;15 earns the first mark only.'},
 {'n':'16', 'marks':3, 'lines':['14<i>x</i> &minus; 21' + B(1), '&minus;8<i>x</i> + 24' + B(1),
                                '= <b>6<i>x</i> + 3</b>' + B(1)],
  'note':'&minus;4 &times; &minus;6 = <b>+24</b>, so the constant is positive. 6<i>x</i> &minus; 45 is the '
         'sign error. Unlike Paper B Q16 the <i>x</i> terms do not cancel, so a bare number here is wrong.'},
 {'n':'17', 'marks':3, 'lines':['8<i>x</i> &minus; 12 = 3<i>x</i> + 18' + B(1), '5<i>x</i> = 30' + B(1),
                                '<i>x</i> = <b>6</b>' + B(1)],
  'note':'Both sides bracketed. Check: 4(12 &minus; 3) = 36 and 3(6 + 6) = 36. He will not check unless told '
         'to, and this is the paper where it matters most.'},
 {'n':'18', 'marks':3, 'lines':['Decrease = 640 000 &minus; 544 000 = 96 000' + B(1),
                                '96 000 &divide; 640 000' + B(1), '= <b>15% decrease</b>' + B(1)],
  'note':'Dividing by 544 000 instead of 640 000 gives 17.6% — the most common error in Unit 10, and the '
         'reason these numbers were chosen. The base is the <i>original</i> value. Award the first mark only.'},
 {'n':'19', 'marks':5, 'lines':[
   '(a) 5 + 4 = 9 parts, 7200 &divide; 9 = 800' + B(1),
   '&nbsp; &nbsp; &nbsp;Asha <b>' + RS + '4000</b>, Bina <b>' + RS + '3200</b>' + B(1),
   '(b) 15% of 4000 = <b>' + RS + '600</b>' + B(1),
   '(c) Asha <b>' + RS + '3400</b>' + B(1) + ', Bina <b>' + RS + '3800</b>' + B(1)],
  'note':'Bina ends up with more than Asha, which he will read as a mistake and may &ldquo;correct&rdquo;. '
         'The total is still 7200 — that is the check. Taking 15% of Bina&rsquo;s share instead of '
         'Asha&rsquo;s gives 480 and breaks the total.'},
 {'n':'20', 'marks':5, 'lines':[
   '(a) Length = 2<i>w</i> + 5, so 2(<i>w</i> + 2<i>w</i> + 5) = 58' + B(2),
   '(b) 3<i>w</i> + 5 = 29' + B(1) + ' &nbsp;·&nbsp; <i>w</i> = <b>8 cm</b>' + B(1),
   '(c) Length = 2(8) + 5 = <b>21 cm</b>' + B(1)],
  'note':'Halving the 58 first is the clean route. &ldquo;5 more than twice&rdquo; is 2<i>w</i> + 5, not '
         '2(<i>w</i> + 5) — the second form gives <i>w</i> = 6 and a 17 cm length, and 2(6 + 17) = 46, not '
         '58, so the check catches it. Make him do the check.'},
 {'n':'21', 'marks':5, 'lines':[
   '(a) 91 &divide; 0.35, multiply both by 100: 9100 &divide; 35' + B(1),
   '&nbsp; &nbsp; &nbsp;9100 &divide; 35' + B(1) + ' = <b>260 bottles</b>' + B(1),
   '(b) 8 &times; 0.35' + B(1) + ' = <b>' + RS + '2.80</b>' + B(1)],
  'note':'(a) is 4.3 with a real division behind it. An answer near 31.85 means he multiplied instead of '
         'dividing — and 31 bottles from 91 litres should have looked wrong. In (b), ' + RS +
         '2.8 is fine; ' + RS + '28 is a 4.2 place-value error.'},
 {'n':'22', 'marks':5, 'lines':[
   '(a) Lowest power of each shared prime: 2<super>2</super> &times; 3 &times; 5' + B(1) +
   ' = <b>60</b>' + B(1),
   '(b) Highest power of each prime: 2<super>3</super> &times; 3<super>2</super> &times; '
   '5<super>2</super>' + B(1) + ' = <b>1800</b>' + B(1),
   '(c) <i>n</i> = 4 &times; 3 &times; 25 = <b>300</b>' + B(1)],
  'note':'The numbers are never given, only their factorisations — that is the point, and it is the hardest '
         '1.1 question on the four papers. Swapping the rules gives HCF = 1800 and LCM = 60, which is the '
         'same name-confusion as Paper A Q3 but much harder to spot. Full working is the only way to tell.'},
 {'n':'23', 'marks':5, 'lines':[
   '(a) 45 000 &times; 0.8' + B(1) + ' = <b>' + RS + '36 000</b>' + B(1),
   '(b) 36 000 &times; 1.25' + B(1) + ' = <b>' + RS + '45 000</b>' + B(1),
   '(c) <b>No change (0%)</b>' + B(1)],
  'note':'0.8 &times; 1.25 = 1 exactly, so it lands back on the original price. He will assume he has made '
         'an error in (b) and go looking for it. A 20% fall is undone by a 25% rise — the mirror of Paper A '
         'Q23, and worth marking the two side by side.'},
 {'n':'24', 'marks':5, 'lines':[
   '(a) The mistake: reading the colon as a fraction bar. There are 3 + 5 = <b>8</b> parts, not 5' + B(1),
   '&nbsp; &nbsp; &nbsp;The correct fraction is <b>' + fr(3,8) + '</b>' + B(1),
   '(b) The mistake: &minus;2 &times; &minus;5 is <b>+10</b>, not &minus;10' + B(1),
   '&nbsp; &nbsp; &nbsp;4 &minus; 2<i>x</i> + 10' + B(1) + ' = <b>14 &minus; 2<i>x</i></b>' + B(1)],
  'note':'These are the two errors the whole set is built around, one from Unit 12 and one from Unit 2, '
         'which is why they close the last paper. Naming the rule is worth more than writing the right '
         'answer — a student who can diagnose both in someone else&rsquo;s handwriting will not make them '
         'in his own, and that is the entire reason this question type exists.'},
]}

SCHEMES = [SCHEME_A, SCHEME_B, SCHEME_C, SCHEME_D]


# ================================================================== VERIFY
def _lcm(a, b):
    return a * b // gcd(a, b)


def _verify():
    """Recomputes every answer on all four papers. Read the numbers, not the prose."""
    # ---- Paper A
    assert [2, 2, 3, 7] == _primes(84)
    assert -7 * -6 == 42 and round(216 ** (1 / 3)) == 6 and 3 ** 4 == 81
    assert D('45') * D('0.1') == D('4.5') and round(6.472, 1) == 6.5
    assert D('0.3') * D('0.4') == D('0.12') and F(3, 8) == F(375, 1000) and F(18, 24) == F(3, 4)
    assert gcd(12, 18) == 6 and _lcm(12, 18) == 36 and 2 ** (5 + 3 - 6) == 4
    assert D('6.2') / D('0.1') == 62 and D('6.2') * D('0.01') == D('0.062')
    _order([('0.68', D('0.68')), ('0.7', D('0.7')), ('0.702', D('0.702')), ('0.71', D('0.71'))])
    _order([('7/12', F(7, 12)), ('5/8', F(5, 8)), ('2/3', F(2, 3)), ('3/4', F(3, 4))])
    assert F(17, 4) - F(11, 6) == F(29, 12) == 2 + F(5, 12)
    assert -6 * -4 == 24 and -6 - 4 == -10 and -48 // 8 == -6
    assert D('4.68') / D('0.12') == 39
    assert 6 * F(11, 4) == F(33, 2) == 16 + F(1, 2) and 8 / F(2, 5) == 20
    assert 40 * 12 + 250 == 730 and (1050 - 250) / 40 == 20
    assert (19 - 7) / (5 - 3) == 6 and D('840') * D('1.15') == 966
    assert 3600 // 8 == 450 and (450 * 3, 450 * 5) == (1350, 2250)
    assert D(2250) * D('1.2') == 2700 and 2700 - 1350 == 1350
    assert (11 + 7) / (4 - 1) == 6                      # 4n - 7 = n + 11
    assert D('96') / D('1.5') == 64 and D('155') / D('2.5') == 62 and 6 * 62 == 372
    assert _lcm(12, 18) == 36 and 360 // 36 == 10
    assert D('800') * D('1.25') == 1000 and D(1000) * D('0.8') == 800
    assert D('1.25') * D('0.8') == 1                    # a 25% rise is undone by a 20% fall

    # ---- Paper B
    assert [2, 3, 3, 5] == _primes(90)
    assert -8 * -5 == 40 and round(196 ** 0.5) == 14 and 5 ** (6 - 4) == 25
    assert D('7.3') / D('0.1') == 73 and round(34682, -3) == 35000
    assert D('0.6') * D('0.05') == D('0.03') and F(5, 9) == F(5, 9) and F(35, 49) == F(5, 7)
    assert gcd(20, 30) == 10 and _lcm(20, 30) == 60 and 3 ** (2 * 3 - 4) == 9
    assert D('0.48') / D('0.01') == 48 and D('350') * D('0.01') == D('3.5')
    _order([('0.5', D('0.5')), ('0.5005', D('0.5005')), ('0.505', D('0.505')), ('0.55', D('0.55'))])
    _order([('11/20', F(11, 20)), ('3/5', F(3, 5)), ('13/20', F(13, 20)), ('7/10', F(7, 10))])
    assert F(16, 3) - F(11, 4) == F(31, 12) == 2 + F(7, 12)
    assert -5 * -9 == 45 and -5 - 9 == -14 and 72 // -9 == -8
    assert D('5.76') / D('0.24') == 24
    assert 8 * F(17, 5) == F(136, 5) == 27 + F(1, 5) and 12 / F(3, 4) == 16
    assert 3 * 7 + 2 * -4 == 13 and (26 - 2 * 4) / 3 == 6
    assert 6 * -2 - 3 * -5 == 3                         # the x terms cancel
    assert (12 + 2) / (5 - 3) == 7 and D('640') * D('0.65') == 416
    assert 4200 // 7 == 600 and (600 * 2, 600 * 5) == (1200, 3000)
    assert D(1200) * D('0.75') == 900 and 3000 - 900 == 2100
    assert (64 + 8) / 4 == 18 and 3 * 18 - 8 == 46 and 18 + 46 == 64
    assert D('245') / D('2.5') == 98 and D('380') / D('4') == 95 and 10 * 95 == 950
    assert gcd(60, 84) == 12 and (60 // 12) * (84 // 12) == 35
    assert D('1500') * D('1.2') == 1800 and D(1800) * D('0.8') == 1440
    assert D('1.2') * D('0.8') == D('0.96') and (1500 - 1440) / 1500 == 0.04

    # ---- Paper C
    assert _primes_between(30, 40) == [31, 37]          # largest below 40 is 37
    assert -3 * -4 * -2 == -24 and round(81 ** 0.5) + round(8 ** (1 / 3)) == 11 and 4 ** 3 == 2 ** 6
    assert D('0.06') / D('0.01') == 6 and round(0.0498, 2) == 0.05
    assert D('0.04') * D('0.05') == D('0.002') and F(750, 1500) == F(1, 2)
    assert gcd(24, 36) == 12 and _lcm(24, 36) == 72 and 2 ** ((3 + 5) - (2 + 4)) == 4
    assert D('3.6') / D('0.01') == 360 and D('0.07') * D('0.1') == D('0.007')
    _order([('0.41', D('0.41')), ('0.401', D('0.401')), ('0.4', D('0.4')), ('0.0409', D('0.0409'))],
           rev=True)
    _order([('13/18', F(13, 18)), ('7/9', F(7, 9)), ('5/6', F(5, 6)), ('11/12', F(11, 12))])
    assert F(37, 6) - F(23, 8) == F(79, 24) == 3 + F(7, 24)
    assert -7 * -3 == 21 and -7 - (-3) == -4 and -60 // -4 == 15
    assert D('0.918') / D('0.027') == 34
    assert 15 * F(14, 5) == 42 and 9 / F(3, 8) == 24
    assert 2 * (9 + F(13, 2)) == 31 and (46 - 2 * 13) / 2 == 10
    assert 4 * 5 - 2 * -5 == 30 and gcd(8, 30) == 2     # 8x + 30 = 2(4x + 15)
    assert (12 + 2) / (6 - 4) == 7 and D('1250') * D('0.82') == 1025
    assert 9450 // 9 == 1050 and [1050 * k for k in (2, 3, 4)] == [2100, 3150, 4200]
    assert D(4200) * D('1.12') == 4704 and 2100 + 3150 + 4704 == 9954
    x = (180 - 20) / 5                                  # x + (3x - 20) + (x + 40) = 180
    assert x == 32 and sorted([32, 3 * 32 - 20, 32 + 40]) == [32, 72, 76]
    assert D('57') / D('0.75') == 76 and D('90') / D('1.25') == 72 and D('185') / D('2.5') == 74
    assert 5 * (76 - 72) == 20
    assert _lcm(15, 24) == 120 and len([k for k in range(120, 366, 120)]) == 3
    assert D('2000') * D('1.3') == 2600 and D(2600) * D('0.7') == 1820
    assert D('1.3') * D('0.7') == D('0.91') and (2000 - 1820) / 2000 == 0.09
    assert gcd(6, 12) == 6                              # 6x + 12 = 6(x + 2), fully

    # ---- Paper D
    assert _primes_between(20, 30) == [23, 29] and len(_primes_between(20, 30)) == 2
    assert -56 // -7 == 8 and round(343 ** (1 / 3)) == 7 and 9 ** (2 + 5) == 9 ** 7
    assert D('0.5') / D('0.01') == 50 and round(7.0962, 2) == 7.1
    assert D('1.2') * D('0.03') == D('0.036') and F(4, 15) == F(4, 15) and F(40, 120) == F(1, 3)
    assert gcd(18, 45) == 9 and _lcm(18, 45) == 90 and 5 ** ((4 + 3) - 5) == 25
    assert D('62') * D('0.01') == D('0.62') and D('0.062') / D('0.01') == D('6.2')
    _order([('0.033', D('0.033')), ('0.3003', D('0.3003')), ('0.303', D('0.303')), ('0.33', D('0.33'))])
    _order([('11/12', F(11, 12)), ('7/8', F(7, 8)), ('5/6', F(5, 6)), ('17/24', F(17, 24))], rev=True)
    assert F(37, 5) - F(29, 8) == F(151, 40) == 3 + F(31, 40)
    assert -9 * -6 == 54 and -9 - 6 == -15 and -144 // 12 == -12
    assert D('2.622') / D('0.038') == 69
    assert 14 * F(12, 7) == 24 and 10 / F(2, 7) == 35
    assert D('1.8') * 25 + 32 == 77 and (D('5') - 32) / D('1.8') == -15
    assert 7 * -3 - 4 * -6 == 3                         # constant of 6x + 3
    assert (18 + 12) / (8 - 3) == 6
    assert 640000 - 544000 == 96000 and F(96000, 640000) == F(3, 20)
    assert 7200 // 9 == 800 and (800 * 5, 800 * 4) == (4000, 3200)
    assert D(4000) * D('0.15') == 600 and (4000 - 600, 3200 + 600) == (3400, 3800)
    assert 3400 + 3800 == 7200                          # the total survives the transfer
    w = (58 / 2 - 5) / 3                                # 2(w + 2w + 5) = 58
    assert w == 8 and 2 * 8 + 5 == 21 and 2 * (8 + 21) == 58
    assert D('91') / D('0.35') == 260 and D('8') * D('0.35') == D('2.80')
    n, m = 2 ** 2 * 3 * 5 ** 2, 2 ** 3 * 3 ** 2 * 5
    assert (n, m) == (300, 360) and gcd(n, m) == 60 and _lcm(n, m) == 1800
    assert D('45000') * D('0.8') == 36000 and D(36000) * D('1.25') == 45000
    assert D('0.8') * D('1.25') == 1                    # a 20% fall is undone by a 25% rise
    assert F(3, 3 + 5) == F(3, 8)                       # Q24(a): 3 : 5 is three eighths, not three fifths
    assert 4 - 2 * -5 == 14                             # Q24(b): 4 - 2(x - 5) = 14 - 2x

    print('verified: every answer on all four papers recomputed')


def _primes(n):
    f, d = [], 2
    while d * d <= n:
        while n % d == 0:
            f.append(d); n //= d
        d += 1
    if n > 1:
        f.append(n)
    return f


def _primes_between(lo, hi):
    return [n for n in range(lo + 1, hi) if n > 1 and all(n % d for d in range(2, n))]


def _order(pairs, rev=False):
    """Asserts no two values tie, and that the list is already in the intended order."""
    assert len({v for _, v in pairs}) == len(pairs), 'two values are equal: %r' % (pairs,)
    want = [k for k, _ in sorted(pairs, key=lambda t: t[1], reverse=rev)]
    assert want == [k for k, _ in pairs], 'order is %r, scheme claims %r' % (want, [k for k, _ in pairs])


# ================================================================ COVERAGE
# Every subtopic the tutor asked for, and which question on each paper tests it.
# One entry per numbered question, in order. The assert below is the point: a
# later edit that drops a subtopic fails the build instead of quietly shipping.
SYLLABUS = ['1.1', '1.2', '1.3', '1.4',
            '2.1', '2.2', '2.3', '2.4', '2.5',
            '3.1', '3.2',
            '4.1', '4.2', '4.3',
            '7.1', '7.2', '7.3', '7.4', '7.5',
            '10.1', '10.2',
            '12.1', '12.2', '12.3']

# Q1 and Q2 are the five-part quick-fire questions, so they carry five codes each.
_QUICKFIRE_1 = ['1.1', '1.2', '1.3', '1.4', '3.1']
_COMMON = {
 3:['1.1'], 4:['1.4'], 5:['3.1'], 6:['4.1'], 7:['7.2'], 8:['7.3'],
 11:['1.2'], 12:['4.3'], 13:['7.4'], 14:['7.5'], 15:['2.2'], 17:['2.5'], 18:['10.1'],
 19:['12.2', '10.1'], 20:['2.1', '2.5'], 22:['1.1'], 23:['10.2'],
}

def _cover(q2e, extra):
    """Builds a 24-question coverage list from the shared spine plus per-paper parts."""
    cov = dict(_COMMON)
    cov[1] = list(_QUICKFIRE_1)
    cov[2] = ['3.2', '4.2', '7.1', '12.1', q2e]
    cov.update(extra)
    assert sorted(cov) == list(range(1, 25)), sorted(cov)
    return [cov[i] for i in range(1, 25)]

COVERAGE = {
 'a': _cover('2.3', {9:['2.1'], 10:['2.4'], 16:['2.3'], 21:['12.3', '4.3'],
                     24:['2.2', '2.3', '2.4']}),
 'b': _cover('2.4', {9:['2.1'], 10:['2.3'], 16:['2.3'], 21:['12.3', '4.3'],
                     24:['2.2', '2.3', '2.4']}),
 'c': _cover('2.4', {9:['2.1'], 10:['2.3'], 16:['2.3', '2.4'], 21:['12.3', '4.3'],
                     24:['2.2', '2.3', '2.4']}),
 'd': _cover('2.4', {9:['2.1'], 10:['2.3'], 16:['2.3'], 21:['4.3', '12.3', '4.2'],
                     24:['12.1', '2.3']}),
}


def coverage_check(code, spec):
    cov = COVERAGE[code]
    assert len(cov) == len(spec['questions']), (spec['title'], 'coverage length', len(cov))
    seen = sorted({s for q in cov for s in q}, key=SYLLABUS.index)
    missing = [s for s in SYLLABUS if s not in seen]
    assert not missing, (spec['title'], 'subtopics never examined: %s' % ', '.join(missing))
    return seen


# =================================================================== BUILD
SECTIONS = (SEC1, SEC2, SEC3, SEC4)
SECTION_MARKS = {SEC1: 10, SEC2: 16, SEC3: 24, SEC4: 30}


def total(spec):
    return sum(q.get('marks', 0) for q in spec['questions'])


def parts_total(spec):
    for i, q in enumerate(spec['questions'], 1):
        if q.get('parts'):
            got = sum(p.get('marks', 0) for p in q['parts'])
            assert got == q['marks'], (spec['title'], 'Q%d' % i, got, q['marks'])


def section_totals(spec):
    """A later edit must not be able to unbalance the paper while still summing to 80."""
    tally, cur = {}, None
    for q in spec['questions']:
        if q.get('section'):
            cur = q['section']
        assert cur is not None, (spec['title'], 'question before the first section heading')
        tally[cur] = tally.get(cur, 0) + q['marks']
    assert tally == SECTION_MARKS, (spec['title'], tally, SECTION_MARKS)


_verify()

files = []
for spec, code in [(A, 'a'), (BP, 'b'), (C, 'c'), (DP, 'd')]:
    t = total(spec)
    assert t == 80, (spec['title'], t)
    parts_total(spec)
    section_totals(spec)
    seen = coverage_check(code, spec)
    print('paper %s: %d marks, %d questions, all %d subtopics examined'
          % (code, t, len(spec['questions']), len(seen)))
    p = os.path.join(OUT, 'maths-mock-paper-%s.pdf' % code)
    build_paper(spec, p)
    files.append(p)

for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 80, (sc['title'], t)

for spec, sc in zip([A, BP, C, DP], SCHEMES):
    assert len(sc['questions']) == len(spec['questions']), (sc['title'], 'question count')
    for i, (q, sq) in enumerate(zip(spec['questions'], sc['questions']), 1):
        assert sq['n'] == str(i), (sc['title'], 'numbering', sq['n'], i)
        assert sq['marks'] == q['marks'], (sc['title'], 'Q%d marks' % i, sq['marks'], q['marks'])

p = os.path.join(OUT, 'maths-mock-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW,
    'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 80 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Award method marks even when the '
             'final answer is wrong. These are cross-topic papers, so each note names the <i>unit</i> '
             'the mark was lost in, not just the mistake — on an 80-mark script that is the thing worth '
             'reading off. Four patterns recur and are worth tracking across all four papers: dropping '
             'the sign when a negative multiplies into a bracket (2.3), reading a : b as the fraction '
             'a/b (12.1), dividing a percentage change by the new value instead of the original (10.1), '
             'and treating &divide; 0.1 as &divide; 10 (3.1). He rarely makes all four; find which two '
             'are his.',
    'footer': 'Mark schemes · Grade 7 maths mock exam',
})
files.append(p)
print('\n'.join(files))
