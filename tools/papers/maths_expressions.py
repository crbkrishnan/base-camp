#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)

EYEBROW = 'Base Camp · IGCSE Mathematics · Grade 7 · Algebra'
TOPIC   = 'Expressions, Formulae and Brackets'

INSTR_MED = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Every number on this paper is small enough to handle on paper.',
    'When you substitute a value, <b>write it in brackets</b>: 3(&minus;2), not 3&minus;2. Most lost marks on this paper are dropped signs.',
    'Only <b>like terms</b> can be added — terms with exactly the same letter part. 3x + 2 is already simplified.',
    '&ldquo;Factorise completely&rdquo; means take out the <b>highest</b> common factor. Check by looking inside your bracket: if the numbers there still share a factor, you stopped early.',
    'The mark for each question is shown in square brackets on the right.',
]
INSTR_HARD = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Every number on this paper is designed to come out exactly.',
    'The rules for expanding, factorising and signs are not printed on this paper. You are expected to know them.',
    'When a bracket is <b>subtracted</b>, the minus sign multiplies <b>every</b> term inside it. This is the single largest source of lost marks in this topic.',
    'Several questions ask you to explain or to prove something is always true. A calculation on its own is not an explanation — say what the algebra shows.',
    'The mark for each question is shown in square brackets on the right.',
    'If a question stops you, leave it and come back — do not spend more than five minutes stuck.',
]

# ----------------------------------------------------------------- PAPER A
A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — simplifying and writing expressions',
   'text':'Complete the table. Each empty box is worth one mark.', 'marks':6,
   'grid':[['Expression','Simplified','Its value when x = 2'],
           ['5x + 3 &minus; 2x + 7','',''],
           ['8x &minus; 3 &minus; 5x + 9','',''],
           ['4x + 2x &minus; 7 + 1','','']],
   'grid_widths':[AVAIL*0.36, AVAIL*0.32, AVAIL*0.32],
   'tip':'Underline each term together with the sign in front of it before you start. The sign always travels with its term.'},

  {'text':'Simplify:', 'marks':3,
   'parts':[{'label':'(a)','text':'9p + 4q &minus; 5p + 2q','marks':1,'space':18},
            {'label':'(b)','text':'6m &times; 4n','marks':1,'space':18},
            {'label':'(c)','text':'3c &times; 5c','marks':1,'space':18}]},

  {'text':'Using <i>n</i> for the number, write an expression for each of these.', 'marks':3,
   'parts':[{'label':'(a)','text':'five more than three times the number','marks':1,'space':18},
            {'label':'(b)','text':'the number decreased by seven','marks':1,'space':18},
            {'label':'(c)','text':'double the sum of the number and four','marks':1,'space':20}]},

  {'section':'Section 2 — substituting, expanding, factorising',
   'text':'Given that <i>a</i> = 5 and <i>b</i> = &minus;3, work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'2a + b','marks':1,'space':18},
            {'label':'(b)','text':'3b &minus; a','marks':1,'space':18},
            {'label':'(c)','text':'ab','marks':1,'space':18},
            {'label':'(d)','text':'a &minus; b','marks':1,'space':18}]},

  {'text':'Expand:', 'marks':4,
   'parts':[{'label':'(a)','text':'3(x + 4)','marks':1,'space':18},
            {'label':'(b)','text':'5(2x &minus; 3)','marks':1,'space':18},
            {'label':'(c)','text':'4(3x + 2)','marks':1,'space':18},
            {'label':'(d)','text':'2(5 &minus; x)','marks':1,'space':18}]},

  {'text':'Factorise completely:', 'marks':4,
   'parts':[{'label':'(a)','text':'6x + 9','marks':1,'space':18},
            {'label':'(b)','text':'10x &minus; 15','marks':1,'space':18},
            {'label':'(c)','text':'8x + 20','marks':1,'space':18},
            {'label':'(d)','text':'14x + 21','marks':1,'space':18}]},

  {'section':'Section 3 — using it',
   'text':'A taxi charges a fixed 40 rupees, plus 12 rupees for every kilometre travelled.', 'marks':3,
   'parts':[{'label':'(a)','text':'Write an expression for the cost of a journey of <i>d</i> kilometres.','marks':1,'space':20},
            {'label':'(b)','text':'Find the cost of a journey of 8 km.','marks':1,'space':20},
            {'label':'(c)','text':'Find the cost of a journey of 15 km.','marks':1,'space':20}]},

  {'text':'A rectangle has width <i>w</i> cm and length (<i>w</i> + 6) cm.', 'marks':3,
   'parts':[{'label':'(a)','text':'Write an expression for the perimeter, fully simplified.','marks':1,'space':24},
            {'label':'(b)','text':'Find the perimeter when w = 5.','marks':1,'space':20},
            {'label':'(c)','text':'Write an expression for the area, with the bracket expanded.','marks':1,'space':22}]},
 ]}

# ----------------------------------------------------------------- PAPER B
B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — substituting and simplifying',
   'text':'Complete the table. Each empty box is worth one mark. Write the number in brackets as you substitute it.', 'marks':6,
   'grid':[['Expression','Value when x = 3','Value when x = &minus;2'],
           ['2x + 5','',''],
           ['x<sup>2</sup>','',''],
           ['3x &minus; 4','','']],
   'grid_widths':[AVAIL*0.30, AVAIL*0.35, AVAIL*0.35],
   'tip':'The middle row is the one that catches people: squaring a negative gives a positive.'},

  {'text':'Simplify:', 'marks':2,
   'parts':[{'label':'(a)','text':'6y + 3 &minus; 2y &minus; 8','marks':1,'space':18},
            {'label':'(b)','text':'7ab &minus; 3ab','marks':1,'space':18}]},

  {'text':'Using <i>n</i> for the number, write an expression for each of these.', 'marks':2,
   'parts':[{'label':'(a)','text':'three times the sum of the number and five','marks':1,'space':20},
            {'label':'(b)','text':'the number squared, then doubled','marks':1,'space':20}]},

  {'section':'Section 2 — brackets, both directions',
   'text':'Expand and simplify:', 'marks':4,
   'parts':[{'label':'(a)','text':'2(x + 3) + 3(x + 1)','marks':2,'space':28},
            {'label':'(b)','text':'4(2x &minus; 1) + 3(x + 5)','marks':2,'space':28}]},

  {'text':'Factorise completely:', 'marks':4,
   'parts':[{'label':'(a)','text':'12x + 8','marks':1,'space':18},
            {'label':'(b)','text':'5y<sup>2</sup> + 10y','marks':1,'space':18},
            {'label':'(c)','text':'9x &minus; 12','marks':1,'space':18},
            {'label':'(d)','text':'4a<sup>2</sup> + 6a','marks':1,'space':18}]},

  {'text':'Expand:', 'marks':4,
   'parts':[{'label':'(a)','text':'x(x + 7)','marks':1,'space':18},
            {'label':'(b)','text':'2x(3x &minus; 1)','marks':1,'space':18},
            {'label':'(c)','text':'(x + 2)(x + 5)','marks':1,'space':22},
            {'label':'(d)','text':'3(2x + 1)','marks':1,'space':18}]},

  {'section':'Section 3 — using it',
   'text':'A triangle has sides of length <i>x</i> cm, (<i>x</i> + 3) cm and (2<i>x</i> &minus; 1) cm.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write an expression for the perimeter, fully simplified.','marks':2,'space':28},
            {'label':'(b)','text':'Find the perimeter when x = 5, then check your answer by working out the three '
                                  'side lengths separately and adding them.','marks':2,'space':34}]},

  {'text':'A pen costs <i>p</i> rupees and a notebook costs <i>n</i> rupees.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write an expression for the cost of 4 pens and 3 notebooks.','marks':1,'space':20},
            {'label':'(b)','text':'Each of 5 students buys 4 pens and 3 notebooks. Write an expression for the '
                                  'total cost, with the bracket expanded.','marks':1,'space':26},
            {'label':'(c)','text':'Find that total when p = 12 and n = 45.','marks':2,'space':30}]},
 ]}

# ----------------------------------------------------------------- PAPER C
C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — brackets that are taken away',
   'text':'Expand and simplify:', 'marks':4,
   'parts':[{'label':'(a)','text':'5(2x + 3) &minus; 2(x + 4)','marks':2,'space':30},
            {'label':'(b)','text':'4(3x &minus; 2) &minus; 3(2x &minus; 5)','marks':2,'space':30}]},

  {'text':'Expand and simplify:', 'marks':4,
   'parts':[{'label':'(a)','text':'3(2x &minus; 5) &minus; (x &minus; 4)','marks':2,'space':30},
            {'label':'(b)','text':'2(4x + 1) &minus; 5(x &minus; 3)','marks':2,'space':30}]},

  {'text':'Given that <i>a</i> = &minus;3 and <i>b</i> = 4, work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'a<sup>2</sup>','marks':1,'space':18},
            {'label':'(b)','text':'2a<sup>2</sup>','marks':1,'space':18},
            {'label':'(c)','text':'(a + b)<sup>2</sup>','marks':1,'space':20},
            {'label':'(d)','text':'a<sup>2</sup> + b<sup>2</sup>','marks':1,'space':20}]},

  {'section':'Section 2 — factorising completely',
   'text':'Factorise completely. One of these cannot be factorised — say so and explain why.', 'marks':4,
   'parts':[{'label':'(a)','text':'18x + 24','marks':1,'space':18},
            {'label':'(b)','text':'15y<sup>2</sup> &minus; 20y','marks':1,'space':18},
            {'label':'(c)','text':'12a<sup>2</sup> + 18a','marks':1,'space':18},
            {'label':'(d)','text':'8x + 3y','marks':1,'space':22}]},

  {'text':'A rectangular garden has an area of (20<i>x</i> + 45) m<sup>2</sup>. One of its sides is 5 m long.', 'marks':4,
   'parts':[{'label':'(a)','text':'Factorise 20x + 45 completely.','marks':2,'space':26},
            {'label':'(b)','text':'Hence write down an expression for the other side.','marks':1,'space':20},
            {'label':'(c)','text':'Write an expression for the perimeter, fully simplified.','marks':1,'space':26}]},

  {'section':'Section 3 — showing something is always true',
   'text':'Two consecutive whole numbers can be written as <i>n</i> and <i>n</i> + 1.', 'marks':5,
   'parts':[{'label':'(a)','text':'Write an expression for their sum, fully simplified.','marks':1,'space':20},
            {'label':'(b)','text':'Use your answer to explain why the sum of two consecutive whole numbers is '
                                  '<b>always odd</b>.','marks':2,'space':32},
            {'label':'(c)','text':'Write a simplified expression for the sum of <b>three</b> consecutive whole '
                                  'numbers, and use it to explain why that sum is always a multiple of 3.','marks':2,'space':38}]},

  {'text':'The cost <i>C</i> rupees of hiring a hall for <i>h</i> hours is given by the formula '
          '<b>C = 150 + 25h</b>.', 'marks':5,
   'parts':[{'label':'(a)','text':'Find the cost of hiring the hall for 6 hours.','marks':1,'space':22},
            {'label':'(b)','text':'A booking cost 425 rupees. For how many hours was the hall hired?','marks':2,'space':30},
            {'label':'(c)','text':'Explain why a booking can never cost exactly 210 rupees if the hall is only '
                                  'hired for a whole number of hours.','marks':2,'space':34}]},
 ]}

# ----------------------------------------------------------------- PAPER D
D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — expanding and substituting',
   'text':'Expand and simplify:', 'marks':4,
   'parts':[{'label':'(a)','text':'6(2x &minus; 3) &minus; 4(x &minus; 5)','marks':2,'space':30},
            {'label':'(b)','text':'3(4x + 2) &minus; 2(3x &minus; 7)','marks':2,'space':30}]},

  {'text':'Given that <i>p</i> = &minus;2 and <i>q</i> = 5, work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'3p<sup>2</sup>','marks':1,'space':18},
            {'label':'(b)','text':'(3p)<sup>2</sup>','marks':1,'space':18},
            {'label':'(c)','text':'q &minus; p','marks':1,'space':18},
            {'label':'(d)','text':'p<sup>3</sup> + q','marks':1,'space':20}]},

  {'section':'Section 2 — factorising and rearranging',
   'text':'Factorise completely:', 'marks':4,
   'parts':[{'label':'(a)','text':'24x + 36','marks':1,'space':18},
            {'label':'(b)','text':'14y<sup>2</sup> &minus; 21y','marks':1,'space':18},
            {'label':'(c)','text':'30a + 45b','marks':1,'space':18},
            {'label':'(d)','text':'6x<sup>2</sup> + 9x + 12','marks':1,'space':20}]},

  {'text':'A rectangle has a perimeter of (14<i>x</i> + 6) cm. One of its sides is (2<i>x</i> + 5) cm long.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write a simplified expression for the sum of two adjacent sides.','marks':1,'space':22},
            {'label':'(b)','text':'Hence find a simplified expression for the other side.','marks':2,'space':30},
            {'label':'(c)','text':'Check your answer by finding both sides and the perimeter when x = 3.','marks':1,'space':28}]},

  {'text':'Three consecutive even numbers can be written as 2<i>n</i>, 2<i>n</i> + 2 and 2<i>n</i> + 4.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write down the next even number after 2n + 4.','marks':1,'space':18},
            {'label':'(b)','text':'Write a simplified expression for the sum of the three numbers given above.','marks':1,'space':24},
            {'label':'(c)','text':'By factorising your answer, show that the sum of three consecutive even numbers '
                                  'is always a multiple of 6.','marks':2,'space':32}]},

  {'section':'Section 3 — marking somebody else',
   'text':'Two students were each asked to expand and simplify 5(2x &minus; 3) &minus; 2(x &minus; 4).<br/>'
          '<b>Student R wrote:</b> &ldquo;10x &minus; 15 &minus; 2x &minus; 8 = 8x &minus; 23&rdquo;<br/>'
          '<b>Student S wrote:</b> &ldquo;10x &minus; 3 &minus; 2x + 4 = 8x + 1&rdquo;<br/>'
          'For each student, describe exactly what they did wrong. Then give the correct answer.', 'marks':5, 'space':58},

  {'text':'A student has written two answers in his book, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;3x + 2 = 5x, because 3 + 2 = 5.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;12x + 18 factorises completely to 2(6x + 9).&rdquo;<br/>'
          'For each one, explain the mistake and give the correct answer. For (ii), also state the '
          'one-line check that would have caught the error.', 'marks':5, 'space':60},
 ]}

# ----------------------------------------------------------------- mark scheme
SCHEMES = [
 {'title':'Paper A — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     '5x + 3 &minus; 2x + 7 &rarr; <b>3x + 10</b> &nbsp;and&nbsp; <b>16</b>',
     '8x &minus; 3 &minus; 5x + 9 &rarr; <b>3x + 6</b> &nbsp;and&nbsp; <b>12</b>',
     '4x + 2x &minus; 7 + 1 &rarr; <b>6x &minus; 6</b> &nbsp;and&nbsp; <b>6</b>'],
    'note':'One mark per box. Award the value box on a correct follow-through from a wrong simplification — the student is being tested on two separate skills and should not lose both for one error.'},
   {'n':'2', 'marks':3, 'lines':['(a) <b>4p + 6q</b>', '(b) <b>24mn</b>', '(c) <b>15c<sup>2</sup></b>'],
    'note':'(a) stops there; 10pq scores nothing. (b) and (c) make the contrast that matters — you may always multiply unlike terms, you may only add like ones. In (c), c &times; c is c<sup>2</sup>, not 2c.'},
   {'n':'3', 'marks':3, 'lines':['(a) <b>3n + 5</b>', '(b) <b>n &minus; 7</b>', '(c) <b>2(n + 4)</b> or 2n + 8'],
    'note':'(b) must be n &minus; 7, not 7 &minus; n — &ldquo;decreased by&rdquo; keeps the number first. In (c) the word &ldquo;sum&rdquo; forces the bracket; 2n + 4 is a different expression and scores nothing.'},
   {'n':'4', 'marks':4, 'lines':['(a) 10 + (&minus;3) = <b>7</b>', '(b) &minus;9 &minus; 5 = <b>&minus;14</b>',
     '(c) 5 &times; (&minus;3) = <b>&minus;15</b>', '(d) 5 &minus; (&minus;3) = <b>8</b>'],
    'note':'(d) is the one to watch — subtracting a negative adds, so the answer is larger than a. A student answering 2 has treated &minus;(&minus;3) as &minus;3.'},
   {'n':'5', 'marks':4, 'lines':['(a) <b>3x + 12</b>', '(b) <b>10x &minus; 15</b>', '(c) <b>12x + 8</b>', '(d) <b>10 &minus; 2x</b>'],
    'note':'Watch for the second term being left unmultiplied — 3x + 4 in (a) or 10x &minus; 3 in (b). In (d) the terms are the other way round, which catches students who multiply by position rather than by meaning.'},
   {'n':'6', 'marks':4, 'lines':['(a) <b>3(2x + 3)</b>', '(b) <b>5(2x &minus; 3)</b>', '(c) <b>4(2x + 5)</b>', '(d) <b>7(2x + 3)</b>'],
    'note':'Every one must be the highest common factor. 2(4x + 10) in (c) is not completely factorised and scores nothing. Get the student to expand each answer back — it takes seconds and settles every dispute.'},
   {'n':'7', 'marks':3, 'lines':['(a) <b>40 + 12d</b> rupees <b>[1]</b>', '(b) 40 + 12(8) = <b>136 rupees</b> <b>[1]</b>',
     '(c) 40 + 12(15) = <b>220 rupees</b> <b>[1]</b>'],
    'note':'In (a), 52d is the error to look for — it adds the fixed charge to the per-kilometre charge as though the 40 were also charged every kilometre.'},
   {'n':'8', 'marks':3, 'lines':['(a) 2(w + w + 6) = 2(2w + 6) = <b>4w + 12</b> cm <b>[1]</b>',
     '(b) 4(5) + 12 = <b>32 cm</b> <b>[1]</b>', '(c) w(w + 6) = <b>w<sup>2</sup> + 6w</b> cm<sup>2</sup> <b>[1]</b>'],
    'note':'Check (b) without algebra: at w = 5 the rectangle is 5 by 11, so the perimeter is 32. In (c), w &times; w must become w<sup>2</sup>; 2w is the error.'},
  ]},

 {'title':'Paper B — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     '2x + 5 &rarr; <b>11</b> and <b>1</b>',
     'x<sup>2</sup> &rarr; <b>9</b> and <b>4</b>',
     '3x &minus; 4 &rarr; <b>5</b> and <b>&minus;10</b>'],
    'note':'One mark per box. The x<sup>2</sup> row at x = &minus;2 is the whole point: (&minus;2)<sup>2</sup> = 4, and a student answering &minus;4 has squared the 2 and kept the sign outside.'},
   {'n':'2', 'marks':2, 'lines':['(a) <b>4y &minus; 5</b>', '(b) <b>4ab</b>'],
    'note':'In (a) the constant terms are +3 and &minus;8, giving &minus;5. In (b), ab is a single letter part, so those two terms really are alike — some students refuse to join them because there are two letters.'},
   {'n':'3', 'marks':2, 'lines':['(a) <b>3(n + 5)</b> or 3n + 15', '(b) <b>2n<sup>2</sup></b>'],
    'note':'(b) must be 2n<sup>2</sup>, not (2n)<sup>2</sup> = 4n<sup>2</sup>. The order in the sentence is squared first, doubled second, and the notation follows it exactly.'},
   {'n':'4', 'marks':4, 'lines':['(a) 2x + 6 + 3x + 3 <b>[1]</b> = <b>5x + 9</b> <b>[1]</b>',
     '(b) 8x &minus; 4 + 3x + 15 <b>[1]</b> = <b>11x + 11</b> <b>[1]</b>'],
    'note':'The first mark is for expanding both brackets correctly, the second for collecting. A student who expands right and collects wrong still earns half — make sure both lines are written out.'},
   {'n':'5', 'marks':4, 'lines':['(a) <b>4(3x + 2)</b>', '(b) <b>5y(y + 2)</b>', '(c) <b>3(3x &minus; 4)</b>', '(d) <b>2a(2a + 3)</b>'],
    'note':'(b) and (d) need the letter taken out as well as the number. 5(y<sup>2</sup> + 2y) is the standard half-answer and is not completely factorised.'},
   {'n':'6', 'marks':4, 'lines':['(a) <b>x<sup>2</sup> + 7x</b>', '(b) <b>6x<sup>2</sup> &minus; 2x</b>',
     '(c) x<sup>2</sup> + 5x + 2x + 10 = <b>x<sup>2</sup> + 7x + 10</b>', '(d) <b>6x + 3</b>'],
    'note':'(c) has four products, not two — every term in the first bracket meets every term in the second. Note that (a) and (c) both give 7x, which is a coincidence worth pointing out so it is not mistaken for a rule.'},
   {'n':'7', 'marks':4, 'lines':['(a) x + (x + 3) + (2x &minus; 1) <b>[1]</b> = <b>4x + 2</b> cm <b>[1]</b>',
     '(b) 4(5) + 2 = <b>22 cm</b> <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;Check: sides are 5, 8 and 9, and 5 + 8 + 9 = 22 ✓ <b>[1]</b>'],
    'note':'The check is a mark in its own right and the question asked for it. It is also the habit worth building — every algebra-in-shapes answer can be tested against real numbers in about fifteen seconds.'},
   {'n':'8', 'marks':4, 'lines':['(a) <b>4p + 3n</b> <b>[1]</b>', '(b) 5(4p + 3n) = <b>20p + 15n</b> <b>[1]</b>',
     '(c) 20(12) + 15(45) = 240 + 675 <b>[1]</b> = <b>915 rupees</b> <b>[1]</b>'],
    'note':'In (b) the whole bracket is multiplied by 5, not just the first term — 20p + 3n is the error. Accept either form in (b), but (c) is far easier from the expanded one.'},
  ]},

 {'title':'Paper C — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':4, 'lines':['(a) 10x + 15 &minus; 2x &minus; 8 <b>[1]</b> = <b>8x + 7</b> <b>[1]</b>',
     '(b) 12x &minus; 8 &minus; 6x + 15 <b>[1]</b> = <b>6x + 7</b> <b>[1]</b>'],
    'note':'(b) is the sign test: &minus;3 &times; &minus;5 = +15. A student answering 6x &minus; 23 has written &minus;15, and that single sign is worth checking on every question of this shape.'},
   {'n':'2', 'marks':4, 'lines':['(a) 6x &minus; 15 &minus; x + 4 <b>[1]</b> = <b>5x &minus; 11</b> <b>[1]</b>',
     '(b) 8x + 2 &minus; 5x + 15 <b>[1]</b> = <b>3x + 17</b> <b>[1]</b>'],
    'note':'In (a) the bare minus in front of (x &minus; 4) means &minus;1, so both terms flip: &minus;x and +4. Students who ignore an invisible 1 tend to write &minus;x &minus; 4.'},
   {'n':'3', 'marks':4, 'lines':['(a) (&minus;3)<sup>2</sup> = <b>9</b>', '(b) 2 &times; 9 = <b>18</b>',
     '(c) (&minus;3 + 4)<sup>2</sup> = 1<sup>2</sup> = <b>1</b>', '(d) 9 + 16 = <b>25</b>'],
    'note':'(c) and (d) are the same two letters and differ only by a bracket, giving 1 against 25. Any student who thinks (a + b)<sup>2</sup> and a<sup>2</sup> + b<sup>2</sup> are the same thing has just been shown otherwise in one line.'},
   {'n':'4', 'marks':4, 'lines':['(a) <b>6(3x + 4)</b>', '(b) <b>5y(3y &minus; 4)</b>', '(c) <b>6a(2a + 3)</b>',
     '(d) <b>It cannot be factorised.</b> 8 and 3 share no common factor, and x and y are different letters, so there is nothing common to every term.'],
    'note':'(d) is a real answer, not a trick. Students who cannot bear to leave a question &ldquo;undone&rdquo; will invent something like x(8 + 3y/x) — the reason matters more than the answer here.'},
   {'n':'5', 'marks':4, 'lines':['(a) HCF of 20 and 45 is 5 <b>[1]</b>, so <b>5(4x + 9)</b> <b>[1]</b>',
     '(b) The area is 5 &times; (4x + 9), and one side is 5, so the other is <b>(4x + 9) m</b> <b>[1]</b>',
     '(c) Perimeter = 2(5 + 4x + 9) = 2(4x + 14) = <b>8x + 28</b> m <b>[1]</b>'],
    'note':'Factorising is doing real work here — it is the only way to find the missing side. Worth saying out loud, because students often see factorising as a pointless rearrangement.'},
   {'n':'6', 'marks':5, 'lines':['(a) n + (n + 1) = <b>2n + 1</b> <b>[1]</b>',
     '(b) 2n is a multiple of 2 and so is always even <b>[1]</b>; one more than an even number is always odd, so the sum is always odd <b>[1]</b>',
     '(c) n + (n + 1) + (n + 2) = <b>3n + 3</b>, which factorises to <b>3(n + 1)</b> <b>[1]</b>; '
     'that is 3 times a whole number, so it is always a multiple of 3 <b>[1]</b>'],
    'note':'The explanation carries the marks, not the algebra. &ldquo;I tried 4 and 5 and got 9, which is odd&rdquo; is a check, not a proof, and earns nothing in (b) — the argument must be about 2n being even for <i>every</i> n.'},
   {'n':'7', 'marks':5, 'lines':['(a) 150 + 25(6) = <b>300 rupees</b> <b>[1]</b>',
     '(b) 425 &minus; 150 = 275 <b>[1]</b>; 275 &divide; 25 = <b>11 hours</b> <b>[1]</b>',
     '(c) 210 &minus; 150 = 60 <b>[1]</b>; 60 &divide; 25 = 2.4, which is not a whole number of hours, so the cost 210 is impossible <b>[1]</b>'],
    'note':'(c) is the question that separates understanding from procedure. The point is that every possible cost is 150 plus a multiple of 25, and 210 is not — accept that argument as an alternative to the division.'},
  ]},

 {'title':'Paper D — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':4, 'lines':['(a) 12x &minus; 18 &minus; 4x + 20 <b>[1]</b> = <b>8x + 2</b> <b>[1]</b>',
     '(b) 12x + 6 &minus; 6x + 14 <b>[1]</b> = <b>6x + 20</b> <b>[1]</b>'],
    'note':'Both hinge on a negative times a negative. In (b), &minus;2 &times; &minus;7 = +14; a student writing &minus;14 gets 6x &minus; 8 and will make the same error again next week unless it is named.'},
   {'n':'2', 'marks':4, 'lines':['(a) 3 &times; 4 = <b>12</b>', '(b) (&minus;6)<sup>2</sup> = <b>36</b>',
     '(c) 5 &minus; (&minus;2) = <b>7</b>', '(d) &minus;8 + 5 = <b>&minus;3</b>'],
    'note':'(a) against (b) is the bracket trap in its cleanest form: square then multiply gives 12, multiply then square gives 36. (d) tests that an odd power of a negative stays negative.'},
   {'n':'3', 'marks':4, 'lines':['(a) <b>12(2x + 3)</b>', '(b) <b>7y(2y &minus; 3)</b>', '(c) <b>15(2a + 3b)</b>',
     '(d) <b>3(2x<sup>2</sup> + 3x + 4)</b>'],
    'note':'(d) has three terms, and the common factor must divide all three — 3 does, but no letter does, because the last term has none. Students often try to take out an x and are stopped by the 12.'},
   {'n':'4', 'marks':4, 'lines':['(a) Perimeter is twice the sum of two adjacent sides, so that sum is '
     '(14x + 6) &divide; 2 = <b>7x + 3</b> cm <b>[1]</b>',
     '(b) (7x + 3) &minus; (2x + 5) <b>[1]</b> = 7x + 3 &minus; 2x &minus; 5 = <b>5x &minus; 2</b> cm <b>[1]</b>',
     '(c) At x = 3 the sides are 11 cm and 13 cm, so the perimeter is 2(11 + 13) = 48 cm, and 14(3) + 6 = 48 ✓ <b>[1]</b>'],
    'note':'In (b) the whole second bracket is subtracted, so both of its terms change sign. A student writing 5x + 8 has subtracted only the 2x. The check in (c) would have caught it, which is exactly why it is asked for.'},
   {'n':'5', 'marks':4, 'lines':['(a) <b>2n + 6</b> <b>[1]</b>',
     '(b) 2n + (2n + 2) + (2n + 4) = <b>6n + 6</b> <b>[1]</b>',
     '(c) 6n + 6 = <b>6(n + 1)</b> <b>[1]</b>; that is 6 times a whole number, so the sum is always a multiple of 6 <b>[1]</b>'],
    'note':'The final mark needs the sentence, not just the factorisation. Note the result is stronger than students expect — not merely even, but always divisible by 6.'},
   {'n':'6', 'marks':5, 'lines':[
     'Student R expanded the first bracket correctly but multiplied &minus;2 by &minus;4 and wrote &minus;8 <b>[1]</b>. '
     'Two negatives multiply to a positive, so that term should be +8 <b>[1]</b>',
     'Student S multiplied only the <b>first</b> term inside each bracket, leaving the 3 and the 4 untouched <b>[1]</b>. '
     'The number outside multiplies <b>every</b> term inside <b>[1]</b>',
     'Correct: 10x &minus; 15 &minus; 2x + 8 = <b>8x &minus; 7</b> <b>[1]</b>'],
    'note':'These are the two failure modes of expanding, and it is worth showing they are independent: R multiplied everything but got one sign wrong, S got every sign right but did not multiply everything. Different fixes.'},
   {'n':'7', 'marks':5, 'lines':[
     '(i) The mistake: 3x and 2 are <b>not like terms</b> and cannot be added <b>[1]</b>. '
     'Correct: <b>3x + 2 is already fully simplified</b> — some expressions simply stop <b>[1]</b>',
     '(ii) The mistake: 2 is a common factor but not the <b>highest</b> one — 6 and 9 inside the bracket still share a 3 <b>[1]</b>. '
     'Correct: <b>6(2x + 3)</b> <b>[1]</b>',
     'The check: look inside the finished bracket. If those numbers still share a factor, the factorisation is incomplete <b>[1]</b>'],
    'note':'The last mark is the transferable one. A student who can state that check will never hand in a partly factorised answer again — and it is the single most commonly repeated error in this topic.'},
  ]},
]

# ----------------------------------------------------------------- build
def total(spec):
    return sum(q.get('marks', 0) for q in spec['questions'])

files = []
for spec, code in [(A, 'a'), (B, 'b'), (C, 'c'), (D, 'd')]:
    t = total(spec)
    assert t == 30, (spec['title'], t)
    for q in spec['questions']:
        if 'parts' in q:
            pt = sum(p['marks'] for p in q['parts'])
            assert pt == q['marks'], (spec['title'], q['text'][:40], pt, q['marks'])
    p = os.path.join(OUT, 'maths-expressions-paper-%s.pdf' % code)
    build_paper(spec, p)
    files.append(p)

for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)

p = os.path.join(OUT, 'maths-expressions-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW,
    'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Where a question is worth more '
             'than one mark, award method marks even when the final answer is wrong — and take them '
             'away for a correct answer with no working only if the question said "show your working". '
             'The notes under each answer flag the specific mistake that question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC,
})
files.append(p)
print('\n'.join(files))
