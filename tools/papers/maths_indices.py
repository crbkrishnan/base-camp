#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)

EYEBROW = 'Base Camp · IGCSE Mathematics · Grade 7 · Number'
TOPIC   = 'Laws of Indices'

INSTR_MED = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Every number on this paper is small enough to handle on paper.',
    'The laws you need: <b>a<sup>m</sup> &times; a<sup>n</sup> = a<sup>m+n</sup></b> &nbsp; '
    '<b>a<sup>m</sup> &divide; a<sup>n</sup> = a<sup>m&minus;n</sup></b> &nbsp; '
    '<b>(a<sup>m</sup>)<sup>n</sup> = a<sup>m&times;n</sup></b> &nbsp; <b>a<sup>0</sup> = 1</b>',
    'The multiplication and division laws only work when the <b>bases are the same</b>.',
    'Where a question says &ldquo;as a single power&rdquo;, leave your answer in index form. Where it asks for a value, work it out.',
    'The mark for each question is shown in square brackets on the right.',
]
INSTR_HARD = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Every number on this paper is small enough to handle on paper, and every fraction comes out simple.',
    'The laws are not printed on this paper. You are expected to know them.',
    'The mark for each question is shown in square brackets on the right.',
    'Several questions describe steps you may not have seen before — apply the ideas you already have. If two bases do not match, ask whether one of them can be rewritten in terms of the other.',
    'If a question stops you, leave it and come back — do not spend more than five minutes stuck.',
]

# ----------------------------------------------------------------- PAPER A
A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — what the index is saying',
   'text':'Complete the table. Each empty box is worth one mark.', 'marks':6,
   'grid':[['Power','Written out in full','Value'],
           ['2<sup>5</sup>','',''],
           ['3<sup>3</sup>','',''],
           ['10<sup>4</sup>','','']],
   'grid_widths':[AVAIL*0.18, AVAIL*0.52, AVAIL*0.30],
   'tip':'The middle column is the whole topic in one box: the index counts how many of the base are multiplied together.'},

  {'text':'Write each of these in index form.', 'marks':2,
   'parts':[{'label':'(a)','text':'3 &times; 3 &times; 3 &times; 3 &times; 3','marks':1,'space':16},
            {'label':'(b)','text':'2 &times; 2 &times; 2 &times; 7 &times; 7','marks':1,'space':18}]},

  {'text':'Work out the value of each power.', 'marks':2,
   'parts':[{'label':'(a)','text':'5<sup>3</sup>','marks':1,'space':16},
            {'label':'(b)','text':'2<sup>7</sup>','marks':1,'space':16}]},

  {'section':'Section 2 — multiplying and dividing',
   'text':'Write each answer as a single power.', 'marks':2,
   'parts':[{'label':'(a)','text':'2<sup>4</sup> &times; 2<sup>3</sup>','marks':1,'space':16},
            {'label':'(b)','text':'7<sup>2</sup> &times; 7<sup>5</sup>','marks':1,'space':16}]},

  {'text':'Write each answer as a single power.', 'marks':2,
   'parts':[{'label':'(a)','text':'6<sup>8</sup> &divide; 6<sup>5</sup>','marks':1,'space':16},
            {'label':'(b)','text':'10<sup>7</sup> &divide; 10<sup>4</sup>','marks':1,'space':16}]},

  {'text':'Simplify, leaving each answer as a single power.', 'marks':2,
   'parts':[{'label':'(a)','text':'a<sup>6</sup> &times; a<sup>2</sup>','marks':1,'space':16},
            {'label':'(b)','text':'b<sup>7</sup> &divide; b<sup>3</sup>','marks':1,'space':16}],
   'tip':'You are never told what a and b stand for, and you never need to know.'},

  {'text':'Simplify, leaving each answer as a single power.', 'marks':3,
   'parts':[{'label':'(a)','text':'c<sup>4</sup> &times; c<sup>5</sup>','marks':1,'space':16},
            {'label':'(b)','text':'d<sup>10</sup> &divide; d<sup>4</sup>','marks':1,'space':16},
            {'label':'(c)','text':'e<sup>3</sup> &times; e &times; e<sup>2</sup>','marks':1,'space':18}]},

  {'section':'Section 3 — thinking about the laws',
   'text':'Explain why 2<sup>3</sup> &times; 5<sup>2</sup> <b>cannot</b> be written as a single power, '
          'and work out its value.', 'marks':2, 'space':32},

  {'text':'Which is larger, 3<sup>4</sup> or 4<sup>3</sup>? Show your working.', 'marks':2, 'space':30,
   'tip':'Swapping the base and the index changes the answer. That is worth seeing once, in numbers.'},

  {'text':'Simplify 2<sup>3</sup> &times; 2<sup>4</sup> &divide; 2<sup>5</sup>.', 'marks':3,
   'parts':[{'label':'(a)','text':'Deal with the multiplication first, and write the result as a single power.','marks':1,'space':20},
            {'label':'(b)','text':'Now apply the division law.','marks':1,'space':20},
            {'label':'(c)','text':'Write your final answer as an ordinary number.','marks':1,'space':18}]},

  {'text':'A student writes &ldquo;2<sup>3</sup> &times; 2<sup>5</sup> = 4<sup>8</sup>&rdquo;. '
          'Explain the mistake, and give the correct answer as a single power.', 'marks':2, 'space':32},

  {'text':'Write 64 as a power of 2, and then as a power of 4.', 'marks':2, 'space':30,
   'tip':'The same number can be written as a power in more than one way. Both answers here are correct.'},
 ]}

# ----------------------------------------------------------------- PAPER B
B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — a power of a power',
   'text':'Write each answer as a single power.', 'marks':3,
   'parts':[{'label':'(a)','text':'(2<sup>3</sup>)<sup>2</sup>','marks':1,'space':16},
            {'label':'(b)','text':'(5<sup>4</sup>)<sup>3</sup>','marks':1,'space':16},
            {'label':'(c)','text':'(x<sup>2</sup>)<sup>5</sup>','marks':1,'space':16}]},

  {'text':'Simplify fully. Everything inside the bracket takes the outer power.', 'marks':3,
   'parts':[{'label':'(a)','text':'(3x<sup>2</sup>)<sup>2</sup>','marks':1,'space':18},
            {'label':'(b)','text':'(2y<sup>3</sup>)<sup>4</sup>','marks':1,'space':18},
            {'label':'(c)','text':'(5a)<sup>3</sup>','marks':1,'space':18}],
   'tip':'If your answer still has the same number in front of the letter as the question did, you have left the coefficient behind.'},

  {'text':'Simplify, leaving each answer as a single power.', 'marks':2,
   'parts':[{'label':'(a)','text':'(a<sup>3</sup>)<sup>4</sup> &divide; a<sup>5</sup>','marks':1,'space':20},
            {'label':'(b)','text':'(b<sup>2</sup>)<sup>3</sup> &times; b<sup>4</sup>','marks':1,'space':20}]},

  {'text':'Work out the value of each of these as an ordinary number.', 'marks':2,
   'parts':[{'label':'(a)','text':'(2<sup>2</sup>)<sup>3</sup>','marks':1,'space':18},
            {'label':'(b)','text':'(10<sup>2</sup>)<sup>3</sup>','marks':1,'space':18}]},

  {'section':'Section 2 — the zero index',
   'text':'Complete the table. Each empty box is worth one mark.', 'marks':4,
   'grid':[['Power','Value'],
           ['2<sup>5</sup>',''],
           ['5<sup>3</sup>',''],
           ['7<sup>0</sup>',''],
           ['10<sup>4</sup>','']],
   'grid_widths':[AVAIL*0.35, AVAIL*0.65]},

  {'text':'Explain why 5<sup>0</sup> = 1. You must use the division law in your answer.',
   'marks':2, 'space':34,
   'tip':'Two marks means two statements: what the law gives you, and what the arithmetic gives you.'},

  {'text':'Work out the value of each of these.', 'marks':3,
   'parts':[{'label':'(a)','text':'2<sup>0</sup> + 3<sup>0</sup>','marks':1,'space':18},
            {'label':'(b)','text':'4<sup>0</sup> &times; 4<sup>3</sup>','marks':1,'space':18},
            {'label':'(c)','text':'(6<sup>3</sup>)<sup>0</sup>','marks':1,'space':18}]},

  {'section':'Section 3 — putting the laws together',
   'text':'Work out the value of each of these without a calculator.', 'marks':3,
   'parts':[{'label':'(a)','text':'2<sup>4</sup> &times; 2<sup>3</sup> &divide; 2<sup>5</sup>','marks':1,'space':22},
            {'label':'(b)','text':'3<sup>5</sup> &divide; 3<sup>3</sup>','marks':1,'space':22},
            {'label':'(c)','text':'(10<sup>3</sup>)<sup>2</sup> &divide; 10<sup>4</sup>','marks':1,'space':22}],
   'tip':'Simplify to a single power first. Working out 3<sup>5</sup> = 243 before you divide is doing the hard version on purpose.'},

  {'text':'Simplify fully.', 'marks':3,
   'parts':[{'label':'(a)','text':'3a<sup>2</sup> &times; 4a<sup>5</sup>','marks':1,'space':20},
            {'label':'(b)','text':'(2p<sup>3</sup>)<sup>2</sup> &times; p','marks':1,'space':20},
            {'label':'(c)','text':'20b<sup>8</sup> &divide; 5b<sup>2</sup>','marks':1,'space':20}]},

  {'text':'Two calculations use the same three numbers.', 'marks':3,
   'parts':[{'label':'(a)','text':'Work out (2<sup>3</sup>)<sup>2</sup>.','marks':1,'space':18},
            {'label':'(b)','text':'Work out 2<sup>3</sup> &times; 2<sup>2</sup>.','marks':1,'space':18},
            {'label':'(c)','text':'Explain why the two answers are different.','marks':1,'space':22}]},

  {'text':'Which is larger, 2<sup>10</sup> or 10<sup>3</sup>? Show your working.', 'marks':2, 'space':30},
 ]}

# ----------------------------------------------------------------- PAPER C
C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — negative indices',
   'text':'Write each of these as an ordinary fraction.', 'marks':3,
   'parts':[{'label':'(a)','text':'2<sup>&minus;4</sup>','marks':1,'space':16},
            {'label':'(b)','text':'5<sup>&minus;2</sup>','marks':1,'space':16},
            {'label':'(c)','text':'10<sup>&minus;3</sup>','marks':1,'space':16}],
   'tip':'Every answer here is a small positive number. A negative index is an instruction to flip, not a sign.'},

  {'text':'Write each of these as a power with a negative index.', 'marks':3,
   'parts':[{'label':'(a)','text':'1/9, as a power of 3','marks':1,'space':18},
            {'label':'(b)','text':'1/32, as a power of 2','marks':1,'space':18},
            {'label':'(c)','text':'1/100, as a power of 10','marks':1,'space':18}]},

  {'text':'Consider 2<sup>3</sup> &divide; 2<sup>7</sup>.', 'marks':3,
   'parts':[{'label':'(a)','text':'Use the division law to write it as a single power of 2, and then as a fraction.',
             'marks':2,'space':28},
            {'label':'(b)','text':'Write both powers out in full and cancel, to show that your answer is right.',
             'marks':1,'space':26}]},

  {'section':'Section 2 — when the bases do not match',
   'text':'Powers of 2 are hiding inside other numbers.', 'marks':3,
   'parts':[{'label':'(a)','text':'Write 4 as a power of 2.','marks':1,'space':16},
            {'label':'(b)','text':'Write 8 as a power of 2.','marks':1,'space':16},
            {'label':'(c)','text':'Hence write 2<sup>5</sup> &times; 4<sup>2</sup> as a single power of 2.',
             'marks':1,'space':24}]},

  {'text':'Now the same idea with base 3.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write 9<sup>3</sup> as a power of 3.','marks':1,'space':20},
            {'label':'(b)','text':'Hence write 9<sup>3</sup> &times; 3<sup>2</sup> as a single power of 3.',
             'marks':1,'space':22},
            {'label':'(c)','text':'Write 27 &times; 9<sup>2</sup> &divide; 3<sup>5</sup> as a single power of 3, '
                                  'and work out its value.','marks':2,'space':30}],
   'tip':'Convert every term to the same base before you reach for a law. Look for this whenever you see 4, 8, 9, 16, 25 or 27.'},

  {'text':'Simplify fully.', 'marks':4,
   'parts':[{'label':'(a)','text':'(2a<sup>3</sup>)<sup>2</sup> &times; 3a<sup>4</sup>','marks':2,'space':28},
            {'label':'(b)','text':'24x<sup>7</sup> &divide; (2x<sup>2</sup>)<sup>3</sup>','marks':2,'space':30}]},

  {'section':'Section 3 — multi-step',
   'text':'Write 16<sup>2</sup> &divide; 2<sup>5</sup> as a single power of 2, and work out its value.',
   'marks':3, 'space':36},

  {'text':'Work out the value of each of these, giving your answer as a whole number or a fraction.', 'marks':4,
   'parts':[{'label':'(a)','text':'2<sup>&minus;3</sup> &times; 2<sup>5</sup>','marks':2,'space':28},
            {'label':'(b)','text':'3<sup>4</sup> &times; 3<sup>&minus;6</sup>','marks':2,'space':28}],
   'tip':'The laws work exactly the same way when an index is negative. Add the indices first, then decide what the result means.'},

  {'text':'Write these four values in order, smallest first. Show the value of each one.<br/>'
          '2<sup>&minus;1</sup> &nbsp; &nbsp; 3<sup>0</sup> &nbsp; &nbsp; 2<sup>&minus;3</sup> &nbsp; &nbsp; 3<sup>1</sup>',
   'marks':3, 'space':40},
 ]}

# ----------------------------------------------------------------- PAPER D
D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — powers of ten and place value',
   'text':'Complete the table. Each empty box is worth one mark.', 'marks':4,
   'grid':[['Number','As a power of 10'],
           ['1000',''],
           ['1 000 000',''],
           ['0.01',''],
           ['0.0001','']],
   'grid_widths':[AVAIL*0.45, AVAIL*0.55],
   'tip':'For the last two, write the number as a fraction first. One over a power of ten is a negative index.'},

  {'text':'Work with base 10 throughout.', 'marks':3,
   'parts':[{'label':'(a)','text':'Write 10<sup>4</sup> &times; 10<sup>3</sup> as a single power of 10.','marks':1,'space':18},
            {'label':'(b)','text':'Write 10<sup>5</sup> &divide; 10<sup>8</sup> as a single power of 10.','marks':1,'space':18},
            {'label':'(c)','text':'Write your answer to part (b) as a decimal.','marks':1,'space':18}]},

  {'text':'A sheet of paper is about 10<sup>&minus;4</sup> m thick. A stack contains 10<sup>3</sup> sheets.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write the thickness of the stack as a single power of 10, in metres.',
             'marks':2,'space':26},
            {'label':'(b)','text':'Write that thickness as an ordinary number, in metres and in centimetres.',
             'marks':1,'space':22},
            {'label':'(c)','text':'A student writes &ldquo;10<sup>&minus;4</sup> &times; 10<sup>3</sup> = 10<sup>&minus;12</sup>&rdquo;. '
                                  'Explain the mistake in one sentence.','marks':1,'space':24}]},

  {'section':'Section 2 — why the laws have to be true',
   'text':'This question is about the zero index.', 'marks':4,
   'parts':[{'label':'(a)','text':'Use 6<sup>4</sup> &divide; 6<sup>4</sup> and the division law to show that 6<sup>0</sup> = 1.',
             'marks':2,'space':30},
            {'label':'(b)','text':'Explain why the same argument works whatever base you choose.','marks':1,'space':24},
            {'label':'(c)','text':'Explain what goes wrong with the argument when the base is 0.','marks':1,'space':24}]},

  {'text':'This question is about negative indices.', 'marks':4,
   'parts':[{'label':'(a)','text':'Use the division law to write 5<sup>2</sup> &divide; 5<sup>5</sup> as a single power of 5.',
             'marks':1,'space':20},
            {'label':'(b)','text':'Write both powers out in full and cancel, to find the value as a fraction.',
             'marks':2,'space':30},
            {'label':'(c)','text':'Use your two answers to explain what a negative index means.','marks':1,'space':24}]},

  {'text':'Write these four values in order, smallest first. Show the value of each one as a fraction.<br/>'
          '10<sup>&minus;2</sup> &nbsp; &nbsp; 2<sup>&minus;3</sup> &nbsp; &nbsp; 5<sup>&minus;1</sup> &nbsp; &nbsp; 3<sup>&minus;2</sup>',
   'marks':3, 'space':40,
   'tip':'All four are one over something. The bigger the bottom, the smaller the fraction.'},

  {'section':'Section 3 — corrections',
   'text':'Simplify fully.', 'marks':4,
   'parts':[{'label':'(a)','text':'(3x<sup>2</sup>)<sup>3</sup> &divide; 9x<sup>4</sup>','marks':2,'space':30},
            {'label':'(b)','text':'(a<sup>5</sup> &times; a<sup>&minus;2</sup>)<sup>2</sup>','marks':2,'space':28}]},

  {'text':'A student has written two lines in her book, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;(x<sup>3</sup>)<sup>2</sup> = x<sup>5</sup>&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;10<sup>&minus;2</sup> = &minus;100&rdquo;<br/>'
          'For each one, explain the mistake and give the correct answer.', 'marks':4, 'space':48},
 ]}

# ----------------------------------------------------------------- mark schemes
SCHEMES = [
 {'title':'Paper A — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     'Row 1 &nbsp;2<sup>5</sup> &rarr; 2 &times; 2 &times; 2 &times; 2 &times; 2 &nbsp;and&nbsp; <b>32</b>',
     'Row 2 &nbsp;3<sup>3</sup> &rarr; 3 &times; 3 &times; 3 &nbsp;and&nbsp; <b>27</b>',
     'Row 3 &nbsp;10<sup>4</sup> &rarr; 10 &times; 10 &times; 10 &times; 10 &nbsp;and&nbsp; <b>10 000</b>'],
    'note':'One mark per correct box. Watch for the base multiplied by the index in the value column: '
           '2 &times; 5 = 10, 3 &times; 3 = 9 (right for the wrong reason) and 10 &times; 4 = 40. '
           'A student who writes 10 for 2<sup>5</sup> has the misconception the whole topic is built to remove.'},
   {'n':'2', 'marks':2, 'lines':['(a) <b>3<sup>5</sup></b>', '(b) <b>2<sup>3</sup> &times; 7<sup>2</sup></b>'],
    'note':'In (b) the two bases are different, so they stay separate. Any attempt to combine them into a single '
           'power scores zero — there is nothing to count once the factors stop being identical.'},
   {'n':'3', 'marks':2, 'lines':['(a) 5 &times; 5 &times; 5 = <b>125</b>', '(b) <b>128</b>'],
    'note':'The pair is deliberate: 125 and 128 sit next to each other, so a student who has memorised '
           '&ldquo;2<sup>7</sup> is about 125&rdquo; rather than counted it will not survive the comparison.'},
   {'n':'4', 'marks':2, 'lines':['(a) 4 + 3 = 7, so <b>2<sup>7</sup></b>', '(b) 2 + 5 = 7, so <b>7<sup>7</sup></b>'],
    'note':'Answers of 2<sup>12</sup> and 7<sup>10</sup> mean the indices were multiplied. That is the next law, '
           'not this one.'},
   {'n':'5', 'marks':2, 'lines':['(a) 8 &minus; 5 = 3, so <b>6<sup>3</sup></b>', '(b) 7 &minus; 4 = 3, so <b>10<sup>3</sup></b>']},
   {'n':'6', 'marks':2, 'lines':['(a) <b>a<sup>8</sup></b>', '(b) <b>b<sup>4</sup></b>']},
   {'n':'7', 'marks':3, 'lines':['(a) <b>c<sup>9</sup></b>', '(b) <b>d<sup>6</sup></b>',
                                 '(c) e is e<sup>1</sup>, so 3 + 1 + 2 = 6, giving <b>e<sup>6</sup></b>'],
    'note':'Part (c) is the whole question. A letter written with no index has an index of 1, and students who '
           'read it as 0 give e<sup>5</sup>. Ask what e on its own is worth before correcting the arithmetic.'},
   {'n':'8', 'marks':2, 'lines':[
     'The bases are different, so there is nothing to count &mdash; the laws only apply when the base is the same <b>[1]</b>',
     '8 &times; 25 = <b>200</b> <b>[1]</b>'],
    'note':'Accept any wording that names the mismatched bases. An answer of 10<sup>5</sup> (bases multiplied, '
           'indices added) is the failure this question exists to catch — it gives 100 000 instead of 200.'},
   {'n':'9', 'marks':2, 'lines':['3<sup>4</sup> = 81 and 4<sup>3</sup> = 64 <b>[1]</b>',
                                 '<b>3<sup>4</sup> is larger</b> <b>[1]</b>'],
    'note':'Both values must be shown for the first mark. The point is that swapping the base and the index is '
           'not a harmless move — worth saying out loud, because 2<sup>4</sup> and 4<sup>2</sup> are equal and '
           'students generalise from that one accident.'},
   {'n':'10', 'marks':3, 'lines':['(a) 2<sup>3</sup> &times; 2<sup>4</sup> = <b>2<sup>7</sup></b> <b>[1]</b>',
                                  '(b) 2<sup>7</sup> &divide; 2<sup>5</sup> = <b>2<sup>2</sup></b> <b>[1]</b>',
                                  '(c) <b>4</b> <b>[1]</b>'],
    'note':'The long way is 8 &times; 16 = 128, then 128 &divide; 32 = 4 — same answer, three-figure numbers. '
           'Award full marks for it, but point out what the laws saved.'},
   {'n':'11', 'marks':2, 'lines':[
     'The base was multiplied as well as the indices being added; only the indices are added, and the base stays as it is <b>[1]</b>',
     'Correct answer: <b>2<sup>8</sup></b> (= 256) <b>[1]</b>'],
    'note':'4<sup>8</sup> is 65 536 against a true answer of 256 — a factor of 256 out. A student who checks the '
           'size of an answer catches this without knowing any law.'},
   {'n':'12', 'marks':2, 'lines':['64 = <b>2<sup>6</sup></b> <b>[1]</b>', '64 = <b>4<sup>3</sup></b> <b>[1]</b>'],
    'note':'Both are correct and both are wanted. This is the first hint of Paper C: a number can be rewritten '
           'in whichever base makes the question work.'},
  ]},

 {'title':'Paper B — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':3, 'lines':['(a) 3 &times; 2 = 6, so <b>2<sup>6</sup></b>', '(b) <b>5<sup>12</sup></b>',
                                 '(c) <b>x<sup>10</sup></b>'],
    'note':'2<sup>5</sup>, 5<sup>7</sup> and x<sup>7</sup> are the added-instead-of-multiplied answers. '
           'The fix is to read the outer index as &ldquo;how many copies of the bracket&rdquo;.'},
   {'n':'2', 'marks':3, 'lines':['(a) 3<sup>2</sup> = 9 and (x<sup>2</sup>)<sup>2</sup> = x<sup>4</sup>, so <b>9x<sup>4</sup></b>',
                                 '(b) 2<sup>4</sup> = 16 and (y<sup>3</sup>)<sup>4</sup> = y<sup>12</sup>, so <b>16y<sup>12</sup></b>',
                                 '(c) <b>125a<sup>3</sup></b>'],
    'note':'3x<sup>4</sup>, 2y<sup>12</sup> and 5a<sup>3</sup> are the standard errors: the law was applied to the '
           'letter and the coefficient was left sitting there. The bracket does not care which parts are numbers.'},
   {'n':'3', 'marks':2, 'lines':['(a) a<sup>12</sup> &divide; a<sup>5</sup> = <b>a<sup>7</sup></b>',
                                 '(b) b<sup>6</sup> &times; b<sup>4</sup> = <b>b<sup>10</sup></b>'],
    'note':'Two laws in one line. Marking is all-or-nothing per part, but note which of the two steps failed — '
           'it is almost always the bracket.'},
   {'n':'4', 'marks':2, 'lines':['(a) 2<sup>6</sup> = <b>64</b>', '(b) 10<sup>6</sup> = <b>1 000 000</b>']},
   {'n':'5', 'marks':4, 'lines':['2<sup>5</sup> = <b>32</b>', '5<sup>3</sup> = <b>125</b>', '7<sup>0</sup> = <b>1</b>',
                                 '10<sup>4</sup> = <b>10 000</b>'],
    'note':'One mark per box. 7<sup>0</sup> = 0 is the answer to watch for, and it is worth stopping on: it is not '
           'a slip, it is a belief, and question 6 is the argument that dislodges it.'},
   {'n':'6', 'marks':2, 'lines':[
     '5<sup>n</sup> &divide; 5<sup>n</sup> = 5<sup>n&minus;n</sup> = 5<sup>0</sup> by the division law '
     '(any example such as 5<sup>4</sup> &divide; 5<sup>4</sup> is fine) <b>[1]</b>',
     'But any number divided by itself is 1, so 5<sup>0</sup> = <b>1</b> <b>[1]</b>'],
    'note':'&ldquo;Because that is the rule&rdquo; scores nothing. The mark is for the two statements being about '
           'the same calculation — that is what makes the answer forced rather than arbitrary.'},
   {'n':'7', 'marks':3, 'lines':['(a) 1 + 1 = <b>2</b>', '(b) 1 &times; 4<sup>3</sup> = <b>64</b>', '(c) <b>1</b>'],
    'note':'(a) catches the student who thinks a<sup>0</sup> = 0 and answers 0. (c) catches the one who reads the '
           'outer zero as belonging to the 3 — anything to the power zero is 1, however complicated the base looks.'},
   {'n':'8', 'marks':3, 'lines':['(a) 2<sup>4+3&minus;5</sup> = 2<sup>2</sup> = <b>4</b>',
                                 '(b) 3<sup>5&minus;3</sup> = 3<sup>2</sup> = <b>9</b>',
                                 '(c) 10<sup>6</sup> &divide; 10<sup>4</sup> = 10<sup>2</sup> = <b>100</b>'],
    'note':'Full marks for a correct value however it was reached, but a student who evaluates 3<sup>5</sup> = 243 '
           'and then divides has not understood what the laws are for. Say so.'},
   {'n':'9', 'marks':3, 'lines':['(a) 3 &times; 4 = 12 and a<sup>2+5</sup>, so <b>12a<sup>7</sup></b>',
                                 '(b) (2p<sup>3</sup>)<sup>2</sup> = 4p<sup>6</sup>, times p gives <b>4p<sup>7</sup></b>',
                                 '(c) 20 &divide; 5 = 4 and b<sup>8&minus;2</sup>, so <b>4b<sup>6</sup></b>'],
    'note':'Coefficients multiply and divide as ordinary numbers while the indices add and subtract. Students who '
           'add the coefficients in (a) give 7a<sup>7</sup>; that is the tell that the two halves of the term are '
           'being treated the same way.'},
   {'n':'10', 'marks':3, 'lines':['(a) <b>64</b>', '(b) <b>32</b>',
     '(c) In (a) the outer index says two copies of 2<sup>3</sup>, so the indices multiply to give 2<sup>6</sup>; '
     'in (b) two powers are joined, so the indices add to give 2<sup>5</sup> <b>[1]</b>'],
    'note':'The two answers differ by a factor of 2, which is small enough that a student who muddles the laws '
           'will not notice from the size alone. The explanation in (c) is the mark that matters.'},
   {'n':'11', 'marks':2, 'lines':['2<sup>10</sup> = 1024 and 10<sup>3</sup> = 1000 <b>[1]</b>',
                                  '<b>2<sup>10</sup> is larger</b> <b>[1]</b>'],
    'note':'They are within 24 of each other, so guessing is no help — the working has to happen. Doubling ten '
           'times is also worth practising in its own right; 2<sup>10</sup> = 1024 turns up everywhere later.'},
  ]},

 {'title':'Paper C — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':3, 'lines':['(a) 1/2<sup>4</sup> = <b>1/16</b>', '(b) 1/5<sup>2</sup> = <b>1/25</b>',
                                 '(c) 1/10<sup>3</sup> = <b>1/1000</b>'],
    'note':'&minus;16, &minus;25 and &minus;1000 are the answers to watch for. The minus sign is an instruction '
           'to flip the power over, not a sign attached to the answer. Every value here is positive and less than 1.'},
   {'n':'2', 'marks':3, 'lines':['(a) 9 = 3<sup>2</sup>, so 1/9 = <b>3<sup>&minus;2</sup></b>',
                                 '(b) 32 = 2<sup>5</sup>, so 1/32 = <b>2<sup>&minus;5</sup></b>',
                                 '(c) 100 = 10<sup>2</sup>, so 1/100 = <b>10<sup>&minus;2</sup></b>'],
    'note':'This is question 1 run backwards, which is the harder direction. A student who can do 1 but not 2 has '
           'learned a procedure rather than the meaning.'},
   {'n':'3', 'marks':3, 'lines':['(a) 3 &minus; 7 = &minus;4, so <b>2<sup>&minus;4</sup></b> <b>[1]</b>, '
                                 'which is <b>1/16</b> <b>[1]</b>',
                                 '(b) 8/128, and cancelling gives <b>1/16</b> &mdash; the two routes agree <b>[1]</b>'],
    'note':'Part (b) is the proof that the negative index is not a convention someone invented. Both routes have '
           'to agree, and seeing them agree once is what makes the rule usable.'},
   {'n':'4', 'marks':3, 'lines':['(a) <b>2<sup>2</sup></b>', '(b) <b>2<sup>3</sup></b>',
                                 '(c) 4<sup>2</sup> = (2<sup>2</sup>)<sup>2</sup> = 2<sup>4</sup>, so '
                                 '2<sup>5</sup> &times; 2<sup>4</sup> = <b>2<sup>9</sup></b>'],
    'note':'Check: 32 &times; 16 = 512 = 2<sup>9</sup>. Writing 8<sup>7</sup> in (c) — bases multiplied, indices '
           'added — is the usual wrong route. Parts (a) and (b) are there to make the conversion obvious; a '
           'student who does them and then ignores them has not seen why they were asked.'},
   {'n':'5', 'marks':4, 'lines':['(a) 9 = 3<sup>2</sup>, so 9<sup>3</sup> = (3<sup>2</sup>)<sup>3</sup> = <b>3<sup>6</sup></b> <b>[1]</b>',
                                 '(b) 3<sup>6</sup> &times; 3<sup>2</sup> = <b>3<sup>8</sup></b> <b>[1]</b>',
                                 '(c) 27 = 3<sup>3</sup> and 9<sup>2</sup> = 3<sup>4</sup>, so 3<sup>3+4&minus;5</sup> = <b>3<sup>2</sup></b> <b>[1]</b>',
                                 '&nbsp; &nbsp; &nbsp;= <b>9</b> <b>[1]</b>'],
    'note':'Every term must be converted to base 3 before any law is used. In (c), a student who converts 27 but '
           'forgets 9<sup>2</sup> gets 3<sup>3</sup> &times; 9<sup>2</sup> &divide; 3<sup>5</sup> and stalls — award '
           'the conversion mark and point at the term still in the wrong base.'},
   {'n':'6', 'marks':4, 'lines':['(a) (2a<sup>3</sup>)<sup>2</sup> = 4a<sup>6</sup> <b>[1]</b>, '
                                 'times 3a<sup>4</sup> gives <b>12a<sup>10</sup></b> <b>[1]</b>',
                                 '(b) (2x<sup>2</sup>)<sup>3</sup> = 8x<sup>6</sup> <b>[1]</b>, '
                                 'so 24x<sup>7</sup> &divide; 8x<sup>6</sup> = <b>3x</b> <b>[1]</b>'],
    'note':'The first mark in each part is the bracket, and it is where both go wrong: 2a<sup>6</sup> in (a) and '
           '2x<sup>6</sup> or 6x<sup>6</sup> in (b). Award the bracket mark separately so the pattern shows. '
           'In (b), 3x<sup>1</sup> is written 3x — do not penalise either form.'},
   {'n':'7', 'marks':3, 'lines':['16 = 2<sup>4</sup>, so 16<sup>2</sup> = 2<sup>8</sup> <b>[1]</b>',
                                 '2<sup>8</sup> &divide; 2<sup>5</sup> = <b>2<sup>3</sup></b> <b>[1]</b>',
                                 '= <b>8</b> <b>[1]</b>'],
    'note':'Check the long way: 256 &divide; 32 = 8. Doing it that way is correct and scores full marks, but it is '
           'the version that stops working the moment the numbers grow.'},
   {'n':'8', 'marks':4, 'lines':['(a) &minus;3 + 5 = 2, so 2<sup>2</sup> = <b>4</b> <b>[1]</b> <b>[1]</b>',
                                 '(b) 4 + (&minus;6) = &minus;2, so 3<sup>&minus;2</sup> = <b>1/9</b> <b>[1]</b> <b>[1]</b>'],
    'note':'One mark for the combined index, one for the value. The laws behave identically with negative indices '
           '— the arithmetic on the indices is just ordinary directed number. A student who is fine here but not on '
           'question 1 has an index problem, not a negative-number problem.'},
   {'n':'9', 'marks':3, 'lines':['2<sup>&minus;1</sup> = 1/2, &nbsp;3<sup>0</sup> = 1, &nbsp;'
                                 '2<sup>&minus;3</sup> = 1/8, &nbsp;3<sup>1</sup> = 3 <b>[1]</b> <b>[1]</b>',
                                 'Order: <b>2<sup>&minus;3</sup>, 2<sup>&minus;1</sup>, 3<sup>0</sup>, 3<sup>1</sup></b> <b>[1]</b>'],
    'note':'Two marks for the four values (one if two or three are right), one for the order. A student who ranks '
           'by the index alone puts 2<sup>&minus;3</sup> and 2<sup>&minus;1</sup> the wrong way round only if they '
           'also forget the flip; the flip reverses the order of the negatives, which is the point of including two.'},
  ]},

 {'title':'Paper D — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':4, 'lines':['1000 = <b>10<sup>3</sup></b>', '1 000 000 = <b>10<sup>6</sup></b>',
                                 '0.01 = 1/100 = <b>10<sup>&minus;2</sup></b>',
                                 '0.0001 = 1/10 000 = <b>10<sup>&minus;4</sup></b>'],
    'note':'One mark per box. The two decimals are where it goes wrong, and almost always by one: 0.01 read as '
           '10<sup>&minus;1</sup> because it has one zero after the point. Count the places, or write the fraction '
           'down first.'},
   {'n':'2', 'marks':3, 'lines':['(a) <b>10<sup>7</sup></b>', '(b) 5 &minus; 8 = &minus;3, so <b>10<sup>&minus;3</sup></b>',
                                 '(c) <b>0.001</b>'],
    'note':'In (b) the top index is smaller than the bottom one, which is exactly the case students avoid by '
           'silently swapping them to get 10<sup>3</sup>. The decimal in (c) catches it: 1000 is not a small number.'},
   {'n':'3', 'marks':4, 'lines':['(a) 10<sup>&minus;4</sup> &times; 10<sup>3</sup> = 10<sup>&minus;4+3</sup> <b>[1]</b> '
                                 '= <b>10<sup>&minus;1</sup> m</b> <b>[1]</b>',
                                 '(b) <b>0.1 m</b>, which is <b>10 cm</b> <b>[1]</b>',
                                 '(c) The indices were multiplied instead of added &mdash; this is a multiplication '
                                 'of two powers, so the law is add <b>[1]</b>'],
    'note':'10<sup>&minus;12</sup> m is about a hundredth of an atom, for a stack of a thousand sheets of paper. '
           'The sanity check is free and nobody does it: a thousand sheets is roughly a ream, which is about 10 cm high.'},
   {'n':'4', 'marks':4, 'lines':[
     '(a) 6<sup>4</sup> &divide; 6<sup>4</sup> = 6<sup>4&minus;4</sup> = 6<sup>0</sup> by the division law <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;But 1296 &divide; 1296 = 1, and both describe the same calculation, so 6<sup>0</sup> = <b>1</b> <b>[1]</b>',
     '(b) Nothing in the argument used the 6 &mdash; a<sup>n</sup> &divide; a<sup>n</sup> is 1 for any base a <b>[1]</b>',
     '(c) With base 0 the calculation is 0 &divide; 0, which has no value, so the argument gives nothing &mdash; '
     'this is why 0<sup>0</sup> is excluded <b>[1]</b>'],
    'note':'Part (c) separates the student who has followed the argument from the one who has memorised its '
           'conclusion. Accept any answer identifying the division by zero. Do not require the phrase &ldquo;undefined&rdquo;.'},
   {'n':'5', 'marks':4, 'lines':['(a) 2 &minus; 5 = &minus;3, so <b>5<sup>&minus;3</sup></b> <b>[1]</b>',
     '(b) 25/3125 <b>[1]</b>, and cancelling 25 from both gives <b>1/125</b> <b>[1]</b>',
     '(c) The two answers describe the same calculation, so 5<sup>&minus;3</sup> = 1/5<sup>3</sup> &mdash; '
     'a negative index means the <b>reciprocal</b> <b>[1]</b>'],
    'note':'This is the negative-index rule being derived rather than quoted, and it is the same shape of argument '
           'as question 4. A student who can produce both has understood that the two odd-looking rules are '
           'consequences of the division law, not extra rules bolted on.'},
   {'n':'6', 'marks':3, 'lines':['10<sup>&minus;2</sup> = 1/100, &nbsp;2<sup>&minus;3</sup> = 1/8, &nbsp;'
                                 '5<sup>&minus;1</sup> = 1/5, &nbsp;3<sup>&minus;2</sup> = 1/9 <b>[1]</b> <b>[1]</b>',
                                 'Order: <b>10<sup>&minus;2</sup>, 3<sup>&minus;2</sup>, 2<sup>&minus;3</sup>, '
                                 '5<sup>&minus;1</sup></b> <b>[1]</b>'],
    'note':'1/9 and 1/8 are close (0.111 and 0.125) and are the pair that gets swapped. Comparing denominators is '
           'enough — the bigger the bottom, the smaller the fraction — and no decimals are needed. A student who '
           'orders by the index gives 5<sup>&minus;1</sup> first, which is the largest.'},
   {'n':'7', 'marks':4, 'lines':['(a) (3x<sup>2</sup>)<sup>3</sup> = 27x<sup>6</sup> <b>[1]</b>, '
                                 'so 27x<sup>6</sup> &divide; 9x<sup>4</sup> = <b>3x<sup>2</sup></b> <b>[1]</b>',
                                 '(b) Inside first: a<sup>5</sup> &times; a<sup>&minus;2</sup> = a<sup>3</sup> <b>[1]</b>, '
                                 'then (a<sup>3</sup>)<sup>2</sup> = <b>a<sup>6</sup></b> <b>[1]</b>'],
    'note':'In (a) the cube of the 3 is the mark that goes missing — 3x<sup>6</sup> &divide; 9x<sup>4</sup> gives a '
           'fraction and the student usually assumes they have gone wrong somewhere else. In (b), 5 + (&minus;2) = 3 '
           'is directed number, not an index rule.'},
   {'n':'8', 'marks':4, 'lines':[
     '(i) The mistake: the indices were added. A power of a power multiplies them <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;Correct answer: <b>x<sup>6</sup></b> <b>[1]</b>',
     '(ii) The mistake: a negative index means the reciprocal, not a negative answer <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;Correct answer: 1/10<sup>2</sup> = <b>1/100</b>, or 0.01 <b>[1]</b>'],
    'note':'These are the two errors the topic is built around, which is why they close the paper. Marking someone '
           'else&rsquo;s working is identical cognitive work to checking your own and far easier to face — a student '
           'who can diagnose both here will hesitate before writing either.'},
  ]},
]

# ----------------------------------------------------------------- build
def total(spec):
    return sum(q.get('marks', 0) for q in spec['questions'])

def parts_total(spec):
    """Every question with parts must have parts whose marks sum to the question's marks."""
    for i, q in enumerate(spec['questions'], 1):
        if q.get('parts'):
            got = sum(p.get('marks', 0) for p in q['parts'])
            assert got == q['marks'], (spec['title'], 'Q%d' % i, got, q['marks'])

files = []
for spec, code in [(A, 'a'), (B, 'b'), (C, 'c'), (D, 'd')]:
    t = total(spec)
    assert t == 30, (spec['title'], t)
    parts_total(spec)
    p = os.path.join(OUT, 'maths-indices-paper-%s.pdf' % code)
    build_paper(spec, p)
    files.append(p)

for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)

# the scheme must agree with the paper, question by question
for spec, sc in zip([A, B, C, D], SCHEMES):
    assert len(sc['questions']) == len(spec['questions']), (sc['title'], 'question count')
    for i, (q, sq) in enumerate(zip(spec['questions'], sc['questions']), 1):
        assert sq['n'] == str(i), (sc['title'], 'numbering', sq['n'], i)
        assert sq['marks'] == q['marks'], (sc['title'], 'Q%d marks' % i, sq['marks'], q['marks'])

p = os.path.join(OUT, 'maths-indices-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW,
    'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Where a question is worth more '
             'than one mark, award method marks even when the final answer is wrong. Almost every '
             'note below comes back to one of three errors: multiplying the base as well as combining '
             'the indices, applying a law where the bases do not match, or reading a negative index as '
             'a negative answer. Watch which of the three a given student favours &mdash; they rarely '
             'make all of them, and the one they make is the one to drill.',
    'footer': 'Mark schemes · ' + TOPIC,
})
files.append(p)
print('\n'.join(files))
