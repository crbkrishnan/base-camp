#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cumulative Paper 1 — one hour, 80 marks, medium to hard.

Spans Units 1, 2, 3, 4, 7, 10 and 12 of the Grade 7 maths syllabus. Unlike the
per-topic papers this one is 80 marks, not 30: it is an end-of-term paper, not a
topic drill, so the 30-mark assert does not apply here — _verify() asserts 80.
Every number was computed by _verify() before it was typeset.
"""
import os, sys
from math import gcd
from fractions import Fraction as F
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)

EYEBROW = 'Base Camp · IGCSE Mathematics · Grade 7 · Cumulative'
TOPIC   = 'Cumulative Paper 1'
RS      = '&#8377;'

INSTR = [
 'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
 'No calculator. Anything you cannot do in your head, do on paper.',
 'The mark for each question is shown in square brackets on the right. There are <b>80 marks</b> in <b>60 minutes</b> — about <b>45 seconds a mark</b>, so do not sit on one question.',
 'Give every fraction and every ratio in its simplest form, and convert to a common unit before simplifying.',
 'Section 1 is recall, Section 2 is method, Section 3 is problems with no obvious first step. Work in order and do not spend more than five minutes stuck.',
 'Several questions are built so that a wrong method produces an answer that <i>looks</i> reasonable. Checking is part of the work.',
]

QUESTIONS = [
 # ---------------------------------------------------- Section 1 — 22 marks
 {'section':'Section 1 — the mechanics',
  'text':'Write <b>504</b> as a product of its prime factors. Give your answer in index notation.',
  'marks':2, 'space':30},

 {'text':'Two numbers are 84 and 126.', 'marks':2,
  'parts':[{'label':'(a)','text':'Find the highest common factor (HCF) of 84 and 126.','marks':1,'space':20},
           {'label':'(b)','text':'Find the lowest common multiple (LCM) of 84 and 126.','marks':1,'space':20}],
  'tip':'One factor tree for each number serves both parts. Do not build it twice.'},

 {'text':'Work out:', 'marks':2,
  'parts':[{'label':'(a)','text':'&minus;12 &times; 5 &divide; (&minus;4)','marks':1,'space':18},
           {'label':'(b)','text':'(&minus;2)<super>3</super> &times; (&minus;3)<super>2</super>','marks':1,'space':18}]},

 {'text':'Work out &nbsp;<super>3</super>&radic;(&minus;216) &nbsp;+&nbsp; &radic;196.', 'marks':2, 'space':26},

 {'text':'Simplify. Leave each answer in index form.', 'marks':2,
  'parts':[{'label':'(a)','text':'(3<super>5</super> &times; 3<super>4</super>) &divide; 3<super>6</super>','marks':1,'space':18},
           {'label':'(b)','text':'(4<super>3</super>)<super>2</super> &times; 4 &divide; 4<super>5</super>','marks':1,'space':18}]},

 {'text':'Work out:', 'marks':2,
  'parts':[{'label':'(a)','text':'7.2 &divide; 0.1','marks':1,'space':18},
           {'label':'(b)','text':'0.6 &times; 0.01 &divide; 0.1','marks':1,'space':18}],
  'tip':'Dividing by 0.1 makes a number <i>larger</i>. If your answer to (b) is smaller than 0.006 you have gone the wrong way.'},

 {'text':'Round <b>0.0498317</b>', 'marks':2,
  'parts':[{'label':'(a)','text':'to 3 decimal places,','marks':1,'space':18},
           {'label':'(b)','text':'to 3 significant figures.','marks':1,'space':18}]},

 {'text':'Write these decimals in <b>ascending</b> order.<br/>'
         '<b>0.505 &nbsp;&nbsp; 0.55 &nbsp;&nbsp; 0.05 &nbsp;&nbsp; 0.5 &nbsp;&nbsp; 0.055</b>',
  'marks':2, 'space':26},

 {'text':'Write <super>7</super>&frasl;<sub>12</sub> as a decimal. Use dot notation to show which digit recurs.',
  'marks':2, 'space':28},

 {'text':'Write down the single decimal multiplier for:', 'marks':2,
  'parts':[{'label':'(a)','text':'an increase of 17%','marks':1,'space':18},
           {'label':'(b)','text':'a decrease of 6.5%','marks':1,'space':18}]},

 {'text':'Write the ratio &nbsp;<b>0.75 : 1.8 : 2.25</b>&nbsp; in its simplest whole-number form.',
  'marks':2, 'space':30},

 # ---------------------------------------------------- Section 2 — 33 marks
 {'section':'Section 2 — method',
  'text':'A taxi charges a fixed fee of ' + RS + '<i>c</i> plus ' + RS + '<i>m</i> for every kilometre travelled.',
  'marks':3,
  'parts':[{'label':'(a)','text':'Write a formula for the total cost, ' + RS + '<i>T</i>, of a journey of <i>k</i> kilometres.','marks':1,'space':20},
           {'label':'(b)','text':'The fixed fee is ' + RS + '43. A journey of 12 km costs ' + RS + '235. Work out the value of <i>m</i>.','marks':2,'space':32}]},

 {'text':'Expand and simplify:', 'marks':3,
  'parts':[{'label':'(a)','text':'5(3<i>y</i> &minus; 2) &minus; 2(4<i>y</i> &minus; 7)','marks':2,'space':28},
           {'label':'(b)','text':'<i>x</i>(<i>x</i> &minus; 6)','marks':1,'space':18}],
  'tip':'In (a), &minus;2 &times; &minus;7 is <i>plus</i> 14. That one sign is where this question is usually lost.'},

 {'text':'Factorise fully:', 'marks':3,
  'parts':[{'label':'(a)','text':'12<i>a</i> + 18','marks':1,'space':18},
           {'label':'(b)','text':'15<i>x</i><super>2</super><i>y</i> &minus; 25<i>xy</i><super>2</super>','marks':2,'space':28}],
  'tip':'&ldquo;Fully&rdquo; means nothing is left inside the bracket that both terms still share.'},

 {'text':'Solve &nbsp;<super>(5<i>x</i> &minus; 3)</super>&frasl;<sub>4</sub> = <i>x</i> + 2. &nbsp;Show every step, then check your answer.',
  'marks':3, 'space':44},

 {'text':'<i>N</i> = 2<super>4</super> &times; 3<super>5</super> &times; 5<super>2</super>', 'marks':3,
  'parts':[{'label':'(a)','text':'Explain how you can tell, <b>without</b> working out <i>N</i>, that <i>N</i> is not a square number.','marks':1,'space':24},
           {'label':'(b)','text':'Find the smallest positive integer <i>k</i> for which <i>Nk</i> <b>is</b> a square number.','marks':2,'space':32}],
  'tip':'Write a square number in prime factors and look at the indices. What do they all have in common?'},

 {'text':'Work out, showing your method:', 'marks':3,
  'parts':[{'label':'(a)','text':'3.6 &times; 0.45','marks':2,'space':30},
           {'label':'(b)','text':'0.126 &divide; 0.03','marks':1,'space':22}]},

 {'text':'Work out &nbsp;5<super>1</super>&frasl;<sub>6</sub> &minus; 2<super>3</super>&frasl;<sub>4</sub>. '
         'Give your answer as a mixed number in its simplest form.', 'marks':3, 'space':40,
  'tip':'One sixth minus three quarters is negative. Either borrow, or turn both into improper fractions first.'},

 {'text':'Work out, giving each answer in its simplest form:', 'marks':3,
  'parts':[{'label':'(a)','text':'6 &times; 2<super>5</super>&frasl;<sub>8</sub>','marks':2,'space':30},
           {'label':'(b)','text':'8 &divide; <super>2</super>&frasl;<sub>5</sub>','marks':1,'space':22}],
  'tip':'In (b): dividing by a fraction smaller than 1 gives an answer <i>bigger</i> than 8.'},

 {'text':'Write these fractions in <b>descending</b> order. You must show your working.<br/>'
         '<b><super>5</super>&frasl;<sub>8</sub> &nbsp;&nbsp; <super>7</super>&frasl;<sub>12</sub> '
         '&nbsp;&nbsp; <super>11</super>&frasl;<sub>18</sub> &nbsp;&nbsp; <super>3</super>&frasl;<sub>5</sub></b>',
  'marks':3, 'space':44,
  'tip':'Two of these four are very close together. Eyeballing them will not separate them.'},

 {'text':'Amir, Bina and Cara share ' + RS + '9300. Amir&rsquo;s share : Bina&rsquo;s share = 3 : 4, and '
         'Bina&rsquo;s share : Cara&rsquo;s share = 6 : 5. Work out how much each person receives.',
  'marks':3, 'space':46,
  'tip':'The two ratios disagree about Bina. Scale them until they agree, then you have a three-part ratio.'},

 {'text':'A laptop costs ' + RS + '8400. In a sale the price is reduced by 15%. Two months later the '
         'sale price is increased by 15%.', 'marks':3,
  'parts':[{'label':'(a)','text':'Work out the final price of the laptop.','marks':2,'space':32},
           {'label':'(b)','text':'Find the overall percentage change from the original price.','marks':1,'space':24}]},

 # ---------------------------------------------------- Section 3 — 25 marks
 {'section':'Section 3 — problems',
  'text':'A machine fills 1250 bottles in 25 minutes, working at a constant rate.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out how many bottles it fills in 1 hour 12 minutes.','marks':2,'space':32},
           {'label':'(b)','text':'A second machine fills bottles at <super>3</super>&frasl;<sub>5</sub> of the rate of the first. '
                                 'Both machines run together. Find how many minutes they take to fill 6400 bottles.','marks':3,'space':46}],
  'tip':'Find what <i>one minute</i> is worth first. Everything else in this question comes off that number.'},

 {'text':'A rectangle has length (3<i>x</i> + 2) cm and width (<i>x</i> &minus; 1) cm. Its perimeter is 58 cm.',
  'marks':5,
  'parts':[{'label':'(a)','text':'Form an equation in <i>x</i> and solve it.','marks':3,'space':44},
           {'label':'(b)','text':'Hence find the area of the rectangle.','marks':2,'space':32}],
  'tip':'Check your value of <i>x</i> by putting the length and width back into the perimeter before you do (b).'},

 {'text':'A sports club has 448 members. This is after a 12% increase on last year&rsquo;s membership.',
  'marks':5,
  'parts':[{'label':'(a)','text':'Work out the number of members last year.','marks':2,'space':32},
           {'label':'(b)','text':'The 448 members are junior : senior in the ratio 5 : 3. Next year the number of '
                                 'juniors increases by 20% and the number of seniors decreases by 25%. Find the new '
                                 'ratio of juniors to seniors in its simplest form.','marks':3,'space':50}],
  'tip':'In (a) the 448 is the <i>new</i> figure. Taking 12% off 448 is not the reverse of adding 12% to something else.'},

 {'text':'A sheet of card is 0.08 cm thick and has a mass of 4.6 g.', 'marks':5,
  'parts':[{'label':'(a)','text':'Work out how many sheets are in a stack 2.4 cm tall.','marks':2,'space':30},
           {'label':'(b)','text':'Find the total mass of this stack in <b>kilograms</b>, correct to 2 significant figures.','marks':3,'space':44}]},

 {'text':'Rahul has handed in this homework. All three answers are wrong. For each one, say what he did '
         'wrong and write the correct answer.', 'marks':5,
  'parts':[{'label':'(a)','text':'&ldquo;4.8 &divide; 0.1 = 0.48&rdquo;','marks':2,'space':30},
           {'label':'(b)','text':'&ldquo;12 : 18 : 30 in its simplest form is 6 : 9 : 15&rdquo;','marks':2,'space':30},
           {'label':'(c)','text':'&ldquo;0.7 &times; 0.4 = 2.8&rdquo;','marks':1,'space':22}],
  'tip':'A mark for spotting the mistake, a mark for fixing it. Naming the rule he broke is worth more than just writing the right number.'},
]

SPEC = {
 'eyebrow': EYEBROW,
 'title': TOPIC + ' &mdash; Number, Algebra, Ratio and Proportion',
 'meta': 'MtoH · Non-calculator · 60 minutes · 80 marks',
 'marks': 80, 'instructions': INSTR,
 'footer': 'Cumulative Paper 1 · MtoH · Units 1, 2, 3, 4, 7, 10, 12',
 'endnote': 'End of paper. Go back to any answer that came out as a round, comfortable number — '
            'those are the ones a wrong method produces most often.',
 'questions': QUESTIONS,
}

# ----------------------------------------------------------------- mark scheme
def B(n):
    return ' <b>[%d]</b>' % n

SCHEME = [{
 'title': TOPIC + ' — mark scheme',
 'meta': 'Medium to hard · 80 marks · tutor copy',
 'questions': [
  {'n':'1','marks':2,
   'lines':['504 = 2 × 252 = 2 × 2 × 126 = 2 × 2 × 2 × 63 = 2 × 2 × 2 × 7 × 9' + B(1),
            '= <b>2<super>3</super> × 3<super>2</super> × 7</b>' + B(1)],
   'note':'A complete tree with the answer left as 2×2×2×3×3×7 scores 1 of 2 — the question asked for index notation.'},
  {'n':'2','marks':2,
   'lines':['84 = 2<super>2</super>×3×7 &nbsp;&nbsp; 126 = 2×3<super>2</super>×7',
            '(a) HCF = 2×3×7 = <b>42</b>' + B(1),
            '(b) LCM = 2<super>2</super>×3<super>2</super>×7 = <b>252</b>' + B(1)],
   'note':'The classic swap is 252 for the HCF and 42 for the LCM. An HCF can never be larger than the smaller number — say that out loud when marking it.'},
  {'n':'3','marks':2,
   'lines':['(a) &minus;60 &divide; (&minus;4) = <b>15</b>' + B(1),
            '(b) (&minus;8) × 9 = <b>&minus;72</b>' + B(1)],
   'note':'(b) catches the student who makes (&minus;2)<super>3</super> positive because &ldquo;two negatives make a positive&rdquo;. An odd power keeps the sign; an even power loses it.'},
  {'n':'4','marks':2,
   'lines':['<super>3</super>&radic;(&minus;216) = &minus;6 &nbsp;and&nbsp; &radic;196 = 14' + B(1),
            '&minus;6 + 14 = <b>8</b>' + B(1)],
   'note':'An answer of 20 means both roots were taken positive. A cube root of a negative number is negative — that is the whole distinction being tested here.'},
  {'n':'5','marks':2,
   'lines':['(a) 3<super>9</super> &divide; 3<super>6</super> = <b>3<super>3</super></b>' + B(1),
            '(b) 4<super>6</super> × 4<super>1</super> &divide; 4<super>5</super> = 4<super>7</super> &divide; 4<super>5</super> = <b>4<super>2</super></b>' + B(1)],
   'note':'Watch for (4<super>3</super>)<super>2</super> being read as 4<super>5</super> — a power of a power multiplies. Bare 27 or 16 without index form scores 0; the question asked for index form.'},
  {'n':'6','marks':2,
   'lines':['(a) <b>72</b>' + B(1),
            '(b) 0.6 × 0.01 = 0.006, then 0.006 &divide; 0.1 = <b>0.06</b>' + B(1)],
   'note':'0.0006 in (b) means they divided by 10 instead of by 0.1. This is the most common place-value error in the unit: dividing by a number smaller than 1 makes the result bigger.'},
  {'n':'7','marks':2,
   'lines':['(a) <b>0.050</b>' + B(1), '(b) <b>0.0498</b>' + B(1)],
   'note':'0.05 in (a) scores 0 — 3 d.p. requires the trailing zero. In (b), counting the leading zeros as significant gives 0.05, which is the error to look for.'},
  {'n':'8','marks':2,
   'lines':['all to 3 d.p.: 0.505, 0.550, 0.050, 0.500, 0.055' + B(1),
            '<b>0.05, &nbsp;0.055, &nbsp;0.5, &nbsp;0.505, &nbsp;0.55</b>' + B(1)],
   'note':'Ordering by how long the number looks rather than by value gives 0.5, 0.05, 0.55, 0.055, 0.505. Padding to a common number of decimal places is the fix — insist on seeing it written down.'},
  {'n':'9','marks':2,
   'lines':['7 &divide; 12 = 0.58333…' + B(1),
            '= <b>0.583</b> with a dot written above the final 3 only' + B(1)],
   'note':'A dot over the 8, or over both 8 and 3, is the error — only the 3 repeats. Terminating the decimal at 0.58 also scores 1 at most.'},
  {'n':'10','marks':2,
   'lines':['(a) <b>1.17</b>' + B(1), '(b) <b>0.935</b>' + B(1)],
   'note':'1.065 in (b) is the sign error; 0.94 is a rounding habit that will wreck later multi-step work. Neither scores.'},
  {'n':'11','marks':2,
   'lines':['×100 gives 75 : 180 : 225' + B(1),
            '&divide; HCF 15 gives <b>5 : 12 : 15</b>' + B(1)],
   'note':'Stopping at 15 : 36 : 45 (divided by 5 only) scores 1. A ratio is simplest only when the three numbers share no factor at all.'},

  {'n':'12','marks':3,
   'lines':['(a) <b>T = c + mk</b>' + B(1) + ' &nbsp;(accept T = mk + c)',
            '(b) 235 &minus; 43 = 192' + B(1),
            '192 &divide; 12 = <b>16</b>, so m = ' + RS + '16 per km' + B(1)],
   'note':'Dividing 235 by 12 straight away gives 19.58 — a plausible-looking number, which is why it was chosen. The fixed fee must come off first.'},
  {'n':'13','marks':3,
   'lines':['(a) 15y &minus; 10 &minus; 8y + 14' + B(1) + ' = <b>7y + 4</b>' + B(1),
            '(b) <b>x<super>2</super> &minus; 6x</b>' + B(1)],
   'note':'7y &minus; 24 is what you get when &minus;2 × &minus;7 is taken as &minus;14. Award the first mark only. This single sign is worth a whiteboard minute.'},
  {'n':'14','marks':3,
   'lines':['(a) <b>6(2a + 3)</b>' + B(1),
            '(b) partial factorisation, e.g. 5x(3xy &minus; 5y<super>2</super>)' + B(1),
            'fully: <b>5xy(3x &minus; 5y)</b>' + B(1)],
   'note':'2(6a + 9) and 5(3x<super>2</super>y &minus; 5xy<super>2</super>) are factorised but not fully. (a) is all-or-nothing; (b) gives 1 for a partial. The test: is anything left inside that both terms still share?'},
  {'n':'15','marks':3,
   'lines':['× 4 on both sides: 5x &minus; 3 = 4(x + 2)' + B(1),
            '5x &minus; 3 = 4x + 8' + B(1),
            '<b>x = 11</b>' + B(1) + ' &nbsp;check: (55 &minus; 3) &divide; 4 = 13 and 11 + 2 = 13 <font name="UI">&#10003;</font>'],
   'note':'Multiplying only the x term by 4, or writing 5x &minus; 3 = x + 8, are the two failures. A non-integer answer here is the signal that a whole side was not multiplied.'},
  {'n':'16','marks':3,
   'lines':['(a) a square number has every prime index <b>even</b>; 3<super>5</super> has an odd index, so N is not square' + B(1),
            '(b) one more factor of 3 makes that index even' + B(1),
            '<b>k = 3</b>' + B(1) + ' &nbsp;(Nk = 2<super>4</super>×3<super>6</super>×5<super>2</super> = 540<super>2</super>)'],
   'note':'The discriminating question of Section 2. &ldquo;It is too big&rdquo; or &ldquo;it ends in 0&rdquo; scores nothing — the reason has to be about the indices. k = 9 or k = 15 means the rule is half-remembered.'},
  {'n':'17','marks':3,
   'lines':['(a) 36 × 45 = 1620' + B(1) + '; two decimal places altogether, so <b>1.62</b>' + B(1),
            '(b) ×100 on both: 12.6 &divide; 3 = <b>4.2</b>' + B(1)],
   'note':'16.2 or 0.162 in (a) is a place-count error, not a multiplication error — award the method mark and mark the placement wrong. In (b), 0.042 means only the divisor was scaled up.'},
  {'n':'18','marks':3,
   'lines':['31/6 &minus; 11/4' + B(1),
            'common denominator 12: 62/12 &minus; 33/12 = 29/12' + B(1),
            '= <b>25/12</b>' + B(1)],
   'note':'37/12 appears when the whole numbers are subtracted separately and the negative fraction is flipped to keep it positive. Award 1. The improper-fraction route avoids it entirely — push it.'},
  {'n':'19','marks':3,
   'lines':['(a) 6 × 21/8 = 126/8' + B(1) + ' = <b>153/4</b>' + B(1),
            '(b) 8 × 5/2 = <b>20</b>' + B(1)],
   'note':'125/8 in (a) is multiplying the whole number only and copying the fraction across — scores 0. In (b) an answer of 3.2 means they multiplied by 2/5 instead of dividing.'},
  {'n':'20','marks':3,
   'lines':['common denominator 360' + B(1),
            '5/8 = 225/360, &nbsp;7/12 = 210/360, '
            '&nbsp;11/18 = 220/360, &nbsp;3/5 = 216/360' + B(1),
            '<b>5/8, &nbsp;11/18, &nbsp;3/5, &nbsp;7/12</b>' + B(1)],
   'note':'11/18 (0.611) and 3/5 (0.600) are deliberately close — swapping only those two scores 2 and is the near-miss to look for. Ordering by numerator or by denominator are the two wholesale errors.'},
  {'n':'21','marks':3,
   'lines':['A : B = 9 : 12 &nbsp;and&nbsp; B : C = 12 : 10, so A : B : C = 9 : 12 : 10' + B(1),
            '31 parts; 9300 &divide; 31 = ' + RS + '300 per part' + B(1),
            '<b>Amir ' + RS + '2700, &nbsp;Bina ' + RS + '3600, &nbsp;Cara ' + RS + '3000</b>' + B(1) + ' &nbsp;(sum 9300 <font name="UI">&#10003;</font>)'],
   'note':'Jamming the ratios together as 3 : 4 : 5 without scaling B gives 2325 : 3100 : 3875 — which still adds to 9300, so it survives the obvious check. That is exactly why the question is built this way: the shared number must match in both ratios.'},
  {'n':'22','marks':3,
   'lines':['(a) 8400 × 0.85 = 7140' + B(1) + '; &nbsp;7140 × 1.15 = <b>' + RS + '8211</b>' + B(1),
            '(b) 0.85 × 1.15 = 0.9775, so a <b>2.25% decrease</b>' + B(1)],
   'note':'&ldquo;Back to ' + RS + '8400, no change&rdquo; is the error this question exists to catch — the 15% rise acts on 7140, not on 8400. Do not accept &ldquo;2.25%&rdquo; without the word decrease.'},

  {'n':'23','marks':5,
   'lines':['(a) 1250 &divide; 25 = 50 bottles per minute' + B(1) + '; &nbsp;50 × 72 = <b>3600 bottles</b>' + B(1),
            '(b) second machine: 50 × 3/5 = 30 per minute' + B(1),
            'together: 50 + 30 = 80 per minute' + B(1),
            '6400 &divide; 80 = <b>80 minutes</b>' + B(1)],
   'note':'Two traps. Using 1 hour instead of 72 minutes in (a) gives 3000. In (b), averaging the rates to 40 instead of adding them to 80 gives 160 minutes — rates add, they never average.'},
  {'n':'24','marks':5,
   'lines':['(a) 2[(3x + 2) + (x &minus; 1)] = 58' + B(1),
            '8x + 2 = 58' + B(1) + ', &nbsp;so <b>x = 7</b>' + B(1),
            '(b) length 23 cm, width 6 cm' + B(1),
            'area = 23 × 6 = <b>138 cm<super>2</super></b>' + B(1)],
   'note':'Adding the two expressions and forgetting to double gives x = 14.25. A non-integer x in a question with tidy whole-number lengths is itself a warning sign — teach that as the check. Missing cm<super>2</super> in (b) loses the last mark.'},
  {'n':'25','marks':5,
   'lines':['(a) 448 &divide; 1.12' + B(1) + ' = <b>400 members</b>' + B(1),
            '(b) juniors = 448 × 5/8 = 280, seniors = 168' + B(1),
            '280 × 1.2 = 336 &nbsp;and&nbsp; 168 × 0.75 = 126' + B(1),
            '336 : 126 = <b>8 : 3</b> &nbsp;(&divide; 42)' + B(1)],
   'note':'448 × 0.88 = 394.24 is the reverse-percentage error and scores 0 in (a): a 12% rise is undone by dividing by 1.12, not by taking 12% off. In (b), leaving 336 : 126 unsimplified scores 2 of 3.'},
  {'n':'26','marks':5,
   'lines':['(a) 2.4 &divide; 0.08 = 240 &divide; 8' + B(1) + ' = <b>30 sheets</b>' + B(1),
            '(b) 30 × 4.6 = 138 g' + B(1),
            '138 &divide; 1000 = 0.138 kg' + B(1),
            '= <b>0.14 kg</b> (2 s.f.)' + B(1)],
   'note':'0.3 or 3 sheets in (a) is a place-value slip in the division, and it is one the student can catch himself — a stack cannot hold a fraction of a sheet. Leaving 0.138 unrounded in (b) loses only the final mark.'},
  {'n':'27','marks':5,
   'lines':['(a) dividing by 0.1 <b>multiplies by 10</b>; he divided by 10 instead' + B(1) + '; correct answer <b>48</b>' + B(1),
            '(b) he divided by 2 only, but 6, 9 and 15 still share a factor of 3' + B(1) + '; correct answer <b>2 : 3 : 5</b>' + B(1),
            '(c) <b>0.28</b>' + B(1) + ' &nbsp;(7 × 4 = 28, and two decimal places in the question means two in the answer)'],
   'note':'The point here is naming the rule, not producing the number. A correct answer with no explanation scores 1 of 2 in (a) and (b). If he can say &ldquo;dividing by something less than one makes it bigger&rdquo; in his own words, that is the whole place-value unit landing.'},
 ]}]

SCHEME_HEADER = {
 'eyebrow': EYEBROW,
 'title': TOPIC + ' — mark scheme',
 'meta': 'Tutor copy · 80 marks · not linked from the hub',
 'intro': 'Marks in brackets are awarded line by line: a line of correct method scores even when the '
          'arithmetic after it goes wrong. Follow through an earlier wrong answer wherever the later method is '
          'sound. The note under each question names the specific mistake that question was built to catch — '
          'that is what this booklet is for.',
 'footer': 'Cumulative Paper 1 · mark scheme · tutor copy',
}

# ----------------------------------------------------------------- verification
def _verify():
    # Q1 504
    n, f = 504, {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    assert f == {2: 3, 3: 2, 7: 1}, f
    # Q2
    assert gcd(84, 126) == 42 and 84 * 126 // 42 == 252
    # Q3
    assert -12 * 5 // -4 == 15 and (-2) ** 3 * (-3) ** 2 == -72
    # Q4
    assert -6 + 14 == 8 and (-6) ** 3 == -216 and 14 ** 2 == 196
    # Q5
    assert 5 + 4 - 6 == 3 and 3 * 2 + 1 - 5 == 2
    # Q6
    assert F(72, 10) / F(1, 10) == 72 and F(6, 10) * F(1, 100) / F(1, 10) == F(6, 100)
    # Q7
    assert '%.3f' % 0.0498317 == '0.050' and float('%.3g' % 0.0498317) == 0.0498
    # Q8
    assert sorted([0.505, 0.55, 0.05, 0.5, 0.055]) == [0.05, 0.055, 0.5, 0.505, 0.55]
    # Q9
    assert F(7, 12) == F(7, 12) and str(F(7, 12)) == '7/12' and 7 * 10 ** 6 // 12 == 583333
    # Q11
    assert F(75, 15) == 5 and F(180, 15) == 12 and F(225, 15) == 15 and gcd(gcd(75, 180), 225) == 15
    # Q12
    assert F(235 - 43, 12) == 16
    # Q18 / Q19
    assert F(31, 6) - F(11, 4) == F(29, 12) == 2 + F(5, 12)
    assert 6 * F(21, 8) == F(63, 4) == 15 + F(3, 4)
    assert 8 / F(2, 5) == 20
    # Q20 — and no accidental ties
    vals = [('5/8', F(5, 8)), ('7/12', F(7, 12)), ('11/18', F(11, 18)), ('3/5', F(3, 5))]
    assert len({v for _, v in vals}) == 4, 'two fractions are equal'
    assert [k for k, _ in sorted(vals, key=lambda t: -t[1])] == ['5/8', '11/18', '3/5', '7/12']
    # Q21
    assert 9 + 12 + 10 == 31 and 9300 % 31 == 0 and 9300 // 31 == 300
    assert (2700, 3600, 3000) == (9 * 300, 12 * 300, 10 * 300)
    # Q22
    assert F(8400) * F(85, 100) == 7140 and F(7140) * F(115, 100) == 8211
    assert (F(8211) - 8400) / 8400 * 100 == F(-9, 4)
    # Q23
    assert 1250 // 25 == 50 and 50 * 72 == 3600
    assert 50 * F(3, 5) == 30 and 6400 // (50 + 30) == 80
    # Q24
    assert 2 * ((3 * 7 + 2) + (7 - 1)) == 58 and (3 * 7 + 2) * (7 - 1) == 138
    # Q25
    assert F(448) / F(112, 100) == 400
    assert F(448) * F(5, 8) == 280 and F(448) * F(3, 8) == 168
    assert 280 * F(6, 5) == 336 and 168 * F(3, 4) == 126 and gcd(336, 126) == 42
    assert (336 // 42, 126 // 42) == (8, 3)
    # Q26
    assert F(24, 10) / F(8, 100) == 30 and 30 * F(46, 10) == 138 and float('%.2g' % 0.138) == 0.14
    # Q27
    assert F(48, 10) / F(1, 10) == 48
    assert gcd(gcd(12, 18), 30) == 6 and (12 // 6, 18 // 6, 30 // 6) == (2, 3, 5)
    assert F(7, 10) * F(4, 10) == F(28, 100)
    # structure
    total = sum(q['marks'] for q in QUESTIONS)
    assert total == 80, 'paper totals %d marks, expected 80' % total
    for q in QUESTIONS:
        if q.get('parts'):
            s = sum(p['marks'] for p in q['parts'])
            assert s == q['marks'], 'part marks %d != %d in %r' % (s, q['marks'], q['text'][:44])
    assert sum(q['marks'] for q in SCHEME[0]['questions']) == 80
    assert len(SCHEME[0]['questions']) == len(QUESTIONS)
    tally = {}
    for q in QUESTIONS:
        tally[q['marks']] = tally.get(q['marks'], 0) + 1
    print('verified: %d questions, %d marks, spread %s'
          % (len(QUESTIONS), total, sorted(tally.items())))


if __name__ == '__main__':
    _verify()
    print(build_paper(SPEC, os.path.join(OUT, 'maths-cumulative-1-paper.pdf')))
    print(build_scheme(SCHEME, os.path.join(OUT, 'maths-cumulative-1-answers.pdf'), SCHEME_HEADER))
