#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)

EYEBROW = 'Base Camp · IGCSE Mathematics · Grade 7 · Number'
TOPIC   = 'Integers, Primes and Roots'

INSTR_MED = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Every number on this paper is small enough to handle on paper.',
    'A <b>prime</b> has exactly two factors. <b>1 is not prime.</b>',
    'For <b>HCF</b> take the primes in both lists at the lower power; for <b>LCM</b> take every prime at the higher power. '
    'As a check, HCF &times; LCM equals the product of the two numbers.',
    'Where a question says &ldquo;in index form&rdquo;, write 2<sup>3</sup> &times; 3<sup>2</sup>, not 2 &times; 2 &times; 2 &times; 3 &times; 3.',
    'The mark for each question is shown in square brackets on the right.',
]
INSTR_HARD = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Every number on this paper is designed to come out exactly.',
    'The rules for HCF, LCM and signs are not printed on this paper. You are expected to know them.',
    'You are expected to know the squares up to 15<sup>2</sup> and the cubes up to 10<sup>3</sup> by heart.',
    'Several questions describe steps you may not have seen before — apply the ideas you already have. '
    'If a number will not factorise neatly, ask whether its prime factorisation is telling you something about squares or cubes.',
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
  {'section':'Section 1 — factors, multiples and primes',
   'text':'Complete the table. Each empty box is worth one mark.', 'marks':6,
   'grid':[['Number','All of its factors','How many factors'],
           ['18','',''],
           ['28','',''],
           ['36','','']],
   'grid_widths':[AVAIL*0.16, AVAIL*0.58, AVAIL*0.26],
   'tip':'Work in pairs from 1 upwards and stop when the pair meets itself. One of these three rows has an odd number of factors — that is not an accident.'},

  {'text':'Write down:', 'marks':2,
   'parts':[{'label':'(a)','text':'the first four multiples of 7 that are greater than 20','marks':1,'space':18},
            {'label':'(b)','text':'all the prime numbers between 20 and 30','marks':1,'space':18}]},

  {'text':'Write each number as a product of its prime factors, in index form.', 'marks':3,
   'parts':[{'label':'(a)','text':'60','marks':1,'space':22},
            {'label':'(b)','text':'84','marks':1,'space':22},
            {'label':'(c)','text':'200','marks':1,'space':22}]},

  {'section':'Section 2 — HCF, LCM, negatives and roots',
   'text':'Find the HCF and the LCM of each pair. Show the prime factorisations you used.', 'marks':4,
   'parts':[{'label':'(a)','text':'12 and 18','marks':2,'space':30},
            {'label':'(b)','text':'20 and 30','marks':2,'space':30}]},

  {'text':'Work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'&minus;6 &times; 7','marks':1,'space':16},
            {'label':'(b)','text':'&minus;48 &divide; &minus;6','marks':1,'space':16},
            {'label':'(c)','text':'&minus;5 &times; &minus;3 &times; &minus;2','marks':1,'space':18},
            {'label':'(d)','text':'(&minus;4)<sup>2</sup>','marks':1,'space':16}]},

  {'text':'Work out:', 'marks':3,
   'parts':[{'label':'(a)','text':'&radic;144','marks':1,'space':16},
            {'label':'(b)','text':'the cube root of 64','marks':1,'space':16},
            {'label':'(c)','text':'11<sup>2</sup>','marks':1,'space':16}]},

  {'section':'Section 3 — using it',
   'text':'Two bells ring at a school. One rings every 8 minutes and the other every 12 minutes. '
          'They both ring at 9:00 am. At what time do they next ring together?', 'marks':3, 'space':34,
   'tip':'Two things repeating and you want them to coincide.'},

  {'text':'Priya has 24 pencils and 36 erasers. She wants to make identical gift packs, using every '
          'pencil and every eraser, with as many packs as possible.<br/>'
          'How many packs can she make, and what does each pack contain?', 'marks':3, 'space':38},

  {'text':'At midnight the temperature is &minus;4 &deg;C. It then falls by 3 &deg;C every hour '
          'for the next 5 hours. What is the temperature at 5 am?', 'marks':2, 'space':28},
 ]}

# ----------------------------------------------------------------- PAPER B
B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — taking numbers apart',
   'text':'Complete the table. Each empty box is worth one mark. For the last column write YES or NO, '
          'and you should be able to decide it from the index form alone.', 'marks':6,
   'grid':[['Number','As a product of primes, in index form','A square number?'],
           ['72','',''],
           ['100','',''],
           ['96','','']],
   'grid_widths':[AVAIL*0.16, AVAIL*0.56, AVAIL*0.28],
   'tip':'A number is a perfect square exactly when every index in its prime factorisation is even.'},

  {'text':'Answer both parts.', 'marks':2,
   'parts':[{'label':'(a)','text':'List all the factors of 40.','marks':1,'space':20},
            {'label':'(b)','text':'Exactly one of 39, 41, 49 and 51 is prime. Which one, and why are the other three not prime?','marks':1,'space':26}]},

  {'text':'Write each number as a product of its prime factors, in index form.', 'marks':2,
   'parts':[{'label':'(a)','text':'126','marks':1,'space':24},
            {'label':'(b)','text':'189','marks':1,'space':24}]},

  {'section':'Section 2 — negatives, powers and roots',
   'text':'Work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'&minus;9 &times; 6','marks':1,'space':16},
            {'label':'(b)','text':'&minus;72 &divide; 8','marks':1,'space':16},
            {'label':'(c)','text':'&minus;2 &times; &minus;5 &times; &minus;4','marks':1,'space':18},
            {'label':'(d)','text':'(&minus;6)<sup>2</sup>','marks':1,'space':16}]},

  {'text':'Work out:', 'marks':2,
   'parts':[{'label':'(a)','text':'(&minus;2)<sup>4</sup>','marks':1,'space':16},
            {'label':'(b)','text':'(&minus;2)<sup>5</sup>','marks':1,'space':16}]},

  {'text':'Work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'&radic;225','marks':1,'space':16},
            {'label':'(b)','text':'the cube root of 343','marks':1,'space':16},
            {'label':'(c)','text':'14<sup>2</sup>','marks':1,'space':16},
            {'label':'(d)','text':'4<sup>3</sup>','marks':1,'space':16}]},

  {'section':'Section 3 — using it',
   'text':'A tailor has two rolls of ribbon, one 45 cm long and one 60 cm long. She cuts them into '
          'equal pieces, as long as possible, with nothing left over from either roll.<br/>'
          'Find the length of each piece and the total number of pieces.', 'marks':3, 'space':38},

  {'text':'Two cyclists start together at the same point on a circular track. One completes a lap '
          'every 40 seconds, the other every 60 seconds.<br/>'
          'After how many seconds are they next together at the starting point, and how many laps '
          'has each completed by then?', 'marks':3, 'space':38},

  {'text':'Without using a calculator, state which two consecutive whole numbers each of these lies between. '
          'You must show the two square or cube numbers you used.', 'marks':4,
   'parts':[{'label':'(a)','text':'&radic;40','marks':1,'space':18},
            {'label':'(b)','text':'&radic;150','marks':1,'space':18},
            {'label':'(c)','text':'the cube root of 30','marks':1,'space':18},
            {'label':'(d)','text':'the cube root of 200','marks':1,'space':18}]},
 ]}

# ----------------------------------------------------------------- PAPER C
C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — what the prime factorisation tells you',
   'text':'Consider the number 1176.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write 1176 as a product of its prime factors, in index form.','marks':2,'space':34},
            {'label':'(b)','text':'Hence state, with a reason, whether 1176 is a perfect square. '
                                  'Your reason must refer to the indices.','marks':2,'space':30}]},

  {'text':'Consider the number 1080.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write 1080 as a product of its prime factors, in index form.','marks':1,'space':26},
            {'label':'(b)','text':'Find the smallest positive whole number <i>k</i> such that 1080<i>k</i> is a perfect square.','marks':2,'space':34},
            {'label':'(c)','text':'Hence write down the value of &radic;(1080<i>k</i>). You should not need to work out 1080<i>k</i> first.','marks':1,'space':22}]},

  {'text':'Using your prime factorisation of 1080 again:', 'marks':3,
   'parts':[{'label':'(a)','text':'find the smallest positive whole number <i>m</i> such that 1080<i>m</i> is a perfect <b>cube</b>','marks':2,'space':34},
            {'label':'(b)','text':'write down the cube root of 1080<i>m</i>','marks':1,'space':20}]},

  {'section':'Section 2 — working backwards',
   'text':'Two whole numbers have an HCF of 8 and an LCM of 96.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write down the product of the two numbers.','marks':1,'space':18},
            {'label':'(b)','text':'One of the numbers is 24. Find the other, and verify your answer by finding the HCF and LCM of your pair.','marks':2,'space':38},
            {'label':'(c)','text':'There is one other pair of whole numbers with this HCF and this LCM. Write it down.','marks':1,'space':20}]},

  {'text':'The HCF of 12 and <i>n</i> is 4, and the LCM of 12 and <i>n</i> is 60. Find <i>n</i>, '
          'and verify your answer using prime factorisations.', 'marks':3, 'space':40},

  {'text':'Work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'(&minus;3)<sup>2</sup> &times; (&minus;2)<sup>3</sup>','marks':1,'space':20},
            {'label':'(b)','text':'&minus;60 &divide; &minus;4 &divide; &minus;5','marks':1,'space':20},
            {'label':'(c)','text':'(&minus;2)<sup>6</sup>','marks':1,'space':18},
            {'label':'(d)','text':'&minus;4<sup>2</sup> + (&minus;4)<sup>2</sup>','marks':1,'space':20}]},

  {'section':'Section 3 — reasoning it out',
   'text':'Three lights on a tower flash at intervals of 6, 10 and 15 seconds. They all flash together '
          'at exactly 12:00:00.', 'marks':4,
   'parts':[{'label':'(a)','text':'After how many seconds do all three next flash together?','marks':1,'space':22},
            {'label':'(b)','text':'How many more times do all three flash together during the next 5 minutes?','marks':1,'space':22},
            {'label':'(c)','text':'A fourth light, flashing every 8 seconds, also flashed at 12:00:00. '
                                  'How long until all four flash together? Give your answer in minutes.','marks':2,'space':34}]},

  {'text':'This question is about &radic;300, and no calculator may be used.', 'marks':4,
   'parts':[{'label':'(a)','text':'Show that &radic;300 lies between 17 and 18.','marks':1,'space':22},
            {'label':'(b)','text':'State which of 17 and 18 it is nearer to, and justify your answer with a calculation.','marks':1,'space':26},
            {'label':'(c)','text':'Estimate &radic;300 to one decimal place. You must justify your estimate by squaring.','marks':2,'space':38}]},
 ]}

# ----------------------------------------------------------------- PAPER D
D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — building and breaking',
   'text':'Consider the number 2520.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write 2520 as a product of its prime factors, in index form.','marks':2,'space':34},
            {'label':'(b)','text':'Hence write down the largest square number that is a factor of 2520, '
                                  'and state what 2520 divided by it comes to.','marks':2,'space':32}]},

  {'text':'Still using 2520:', 'marks':4,
   'parts':[{'label':'(a)','text':'find the smallest positive whole number <i>k</i> such that 2520<i>k</i> is a perfect square','marks':3,'space':40},
            {'label':'(b)','text':'hence write down &radic;(2520<i>k</i>)','marks':1,'space':20}]},

  {'section':'Section 2 — HCF, LCM and signs',
   'text':'Two whole numbers have an HCF of 15 and an LCM of 90.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write down the product of the two numbers.','marks':1,'space':18},
            {'label':'(b)','text':'One of the numbers is 45. Find the other, and verify it using prime factorisations.','marks':2,'space':36},
            {'label':'(c)','text':'Explain why neither of the two numbers could possibly be 20.','marks':1,'space':24}]},

  {'text':'Work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'(&minus;2)<sup>5</sup>','marks':1,'space':18},
            {'label':'(b)','text':'(&minus;5)<sup>2</sup> &minus; 5<sup>2</sup>','marks':1,'space':20},
            {'label':'(c)','text':'&minus;3<sup>3</sup>','marks':1,'space':18},
            {'label':'(d)','text':'&minus;120 &divide; &minus;6 &times; &minus;2','marks':1,'space':20}]},

  {'text':'At 06:00 the temperature on a mountain is 5 &deg;C. It then falls by 4 &deg;C every hour.', 'marks':4,
   'parts':[{'label':'(a)','text':'What is the temperature at 11:00?','marks':1,'space':22},
            {'label':'(b)','text':'At what time does the temperature reach &minus;27 &deg;C?','marks':2,'space':32},
            {'label':'(c)','text':'Your working for (b) divided a negative by a negative and gave a positive answer. '
                                  'Explain, in terms of the situation, why a positive answer is the right kind of answer.','marks':1,'space':28}]},

  {'section':'Section 3 — marking somebody else',
   'text':'Two students were each asked to find the LCM of 18 and 24.<br/>'
          '<b>Student P wrote:</b> &ldquo;18 &times; 24 = 432, so the LCM is 432.&rdquo;<br/>'
          '<b>Student Q wrote:</b> &ldquo;18 = 2 &times; 3<sup>2</sup> and 24 = 2<sup>3</sup> &times; 3, '
          'so the LCM is 2 &times; 3 = 6.&rdquo;<br/>'
          'For each student, explain what they have actually calculated and why it is not the LCM. '
          'Then give the correct LCM of 18 and 24.', 'marks':5, 'space':58},

  {'text':'A student has written two answers in his book, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;&radic;81 = 40.5, because half of 81 is 40.5.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;&minus;4 + &minus;6 = 10, because two negatives make a positive.&rdquo;<br/>'
          'For each one, explain the mistake and give the correct answer. Then state exactly which '
          'operations the &ldquo;two negatives make a positive&rdquo; rule does apply to.', 'marks':5, 'space':60},
 ]}

# ----------------------------------------------------------------- mark scheme
SCHEMES = [
 {'title':'Paper A — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     '18: <b>1, 2, 3, 6, 9, 18</b> &nbsp;and&nbsp; <b>6</b> factors',
     '28: <b>1, 2, 4, 7, 14, 28</b> &nbsp;and&nbsp; <b>6</b> factors',
     '36: <b>1, 2, 3, 4, 6, 9, 12, 18, 36</b> &nbsp;and&nbsp; <b>9</b> factors'],
    'note':'One mark per box. A missing factor loses that box only. 36 is the square, which is why it alone has an odd count — 6 &times; 6 contributes one factor rather than two. Students who list 36 as having 10 factors have written 6 twice.'},
   {'n':'2', 'marks':2, 'lines':['(a) <b>21, 28, 35, 42</b>', '(b) <b>23 and 29</b>'],
    'note':'In (a), 14 and 21 are both multiples of 7 but only 21 is greater than 20 — starting the list at 14 or at 7 loses the mark. In (b), watch for 21 (3 &times; 7), 25 (5<sup>2</sup>) and 27 (3<sup>3</sup>) being offered as primes.'},
   {'n':'3', 'marks':3, 'lines':[
     '(a) 60 = <b>2<sup>2</sup> &times; 3 &times; 5</b>',
     '(b) 84 = <b>2<sup>2</sup> &times; 3 &times; 7</b>',
     '(c) 200 = <b>2<sup>3</sup> &times; 5<sup>2</sup></b>'],
    'note':'Accept a correct factor tree with the primes ringed. Do <b>not</b> accept an answer containing a 1, or one that leaves a composite unsplit (60 = 2<sup>2</sup> &times; 15 scores nothing).'},
   {'n':'4', 'marks':4, 'lines':[
     '(a) 12 = 2<sup>2</sup> &times; 3, 18 = 2 &times; 3<sup>2</sup> <b>[1]</b> &nbsp; HCF = <b>6</b>, LCM = <b>36</b> <b>[1]</b>',
     '(b) 20 = 2<sup>2</sup> &times; 5, 30 = 2 &times; 3 &times; 5 <b>[1]</b> &nbsp; HCF = <b>10</b>, LCM = <b>60</b> <b>[1]</b>'],
    'note':'The check HCF &times; LCM = product catches everything here: 6 &times; 36 = 216 = 12 &times; 18, and 10 &times; 60 = 600 = 20 &times; 30. If a student has swapped the two answers, this is the fastest way to show them.'},
   {'n':'5', 'marks':4, 'lines':[
     '(a) <b>&minus;42</b>', '(b) <b>8</b>', '(c) <b>&minus;30</b>', '(d) <b>16</b>'],
    'note':'(c) is the one that separates them: three minus signs is an odd count, so the answer is negative. Award nothing for +30. In (d), the bracket means the whole of &minus;4 is squared, so the answer is positive.'},
   {'n':'6', 'marks':3, 'lines':['(a) <b>12</b>', '(b) <b>4</b>', '(c) <b>121</b>'],
    'note':'A wrong answer of 72 in (a) is 144 &divide; 2 — halving instead of rooting. Get the student to square their answer back; it is a ten-second check that catches this every time.'},
   {'n':'7', 'marks':3, 'lines':[
     '8 = 2<sup>3</sup>, 12 = 2<sup>2</sup> &times; 3 <b>[1]</b>',
     'LCM = 2<sup>3</sup> &times; 3 = 24 minutes <b>[1]</b>',
     'So they next ring together at <b>9:24 am</b> <b>[1]</b>'],
    'note':'The third mark is the time, not the interval. Answering &ldquo;24 minutes&rdquo; and stopping is the commonest way to drop a mark here — the question asked at what time.'},
   {'n':'8', 'marks':3, 'lines':[
     'HCF of 24 and 36 <b>[1]</b>',
     '24 = 2<sup>3</sup> &times; 3, 36 = 2<sup>2</sup> &times; 3<sup>2</sup>, so HCF = 2<sup>2</sup> &times; 3 = <b>12 packs</b> <b>[1]</b>',
     'Each pack: 24 &divide; 12 = <b>2 pencils</b> and 36 &divide; 12 = <b>3 erasers</b> <b>[1]</b>'],
    'note':'Sharing into equal groups with nothing left over is always HCF. A student answering 72 has found the LCM — point out that you cannot make more packs than you have pencils.'},
   {'n':'9', 'marks':2, 'lines':[
     '5 &times; &minus;3 = &minus;15 <b>[1]</b>',
     '&minus;4 + &minus;15 = <b>&minus;19 &deg;C</b> <b>[1]</b>'],
    'note':'Answering &minus;7 means the student subtracted 3 once instead of five times. Answering +11 means they added the fall instead of subtracting it — worth naming out loud, since a falling temperature must give a lower number.'},
  ]},

 {'title':'Paper B — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     '72 = <b>2<sup>3</sup> &times; 3<sup>2</sup></b> &nbsp;— <b>NO</b> (the index 3 is odd)',
     '100 = <b>2<sup>2</sup> &times; 5<sup>2</sup></b> &nbsp;— <b>YES</b> (both indices even; 100 = 10<sup>2</sup>)',
     '96 = <b>2<sup>5</sup> &times; 3</b> &nbsp;— <b>NO</b> (indices 5 and 1 are both odd)'],
    'note':'One mark per box. The whole point is the last column: a student who answers it by trying to remember a list of squares rather than by reading the indices has missed what the question was testing, even if all three answers are right.'},
   {'n':'2', 'marks':2, 'lines':[
     '(a) <b>1, 2, 4, 5, 8, 10, 20, 40</b> — eight factors',
     '(b) <b>41</b> is prime. 39 = 3 &times; 13, 49 = 7<sup>2</sup>, 51 = 3 &times; 17'],
    'note':'In (b) the reason is required for the mark. 39 and 51 both have digit sums divisible by 3, which is the fastest way to kill them; 49 is on the squares list and so can never be prime.'},
   {'n':'3', 'marks':2, 'lines':[
     '(a) 126 = <b>2 &times; 3<sup>2</sup> &times; 7</b>',
     '(b) 189 = <b>3<sup>3</sup> &times; 7</b>'],
    'note':'Both check quickly by multiplying back: 2 &times; 9 &times; 7 = 126 and 27 &times; 7 = 189. A student who cannot start (b) has usually not tried dividing by 3 — 189 is odd, so 2 is never going to work.'},
   {'n':'4', 'marks':4, 'lines':[
     '(a) <b>&minus;54</b>', '(b) <b>&minus;9</b>', '(c) <b>&minus;40</b>', '(d) <b>36</b>'],
    'note':'(c) has three minus signs — odd, so negative. Award nothing for +40. Note that (b) and (d) between them test both halves of the rule: one sign gives a negative, two give a positive.'},
   {'n':'5', 'marks':2, 'lines':['(a) <b>16</b>', '(b) <b>&minus;32</b>'],
    'note':'This pair is the rule in miniature: an even power of a negative is positive, an odd power keeps the minus. If a student gets these two right they can do any power of a negative without thinking.'},
   {'n':'6', 'marks':4, 'lines':['(a) <b>15</b>', '(b) <b>7</b>', '(c) <b>196</b>', '(d) <b>64</b>'],
    'note':'(a) and (c) are the same fact in both directions, and it is worth saying so: if you know 14<sup>2</sup> = 196 you already knew &radic;196 = 14. The squares list is not extra work, it is half the marks on this section.'},
   {'n':'7', 'marks':3, 'lines':[
     'Longest equal pieces with nothing left over means HCF <b>[1]</b>',
     '45 = 3<sup>2</sup> &times; 5, 60 = 2<sup>2</sup> &times; 3 &times; 5, so HCF = 3 &times; 5 = <b>15 cm</b> <b>[1]</b>',
     'Pieces: 45 &divide; 15 = 3 and 60 &divide; 15 = 4, so <b>7 pieces</b> <b>[1]</b>'],
    'note':'The third mark needs both rolls added together. Answering &ldquo;3 and 4&rdquo; without totalling, or giving only one of them, loses it.'},
   {'n':'8', 'marks':3, 'lines':[
     'Repeating and coinciding means LCM <b>[1]</b>',
     '40 = 2<sup>3</sup> &times; 5, 60 = 2<sup>2</sup> &times; 3 &times; 5, so LCM = 2<sup>3</sup> &times; 3 &times; 5 = <b>120 seconds</b> <b>[1]</b>',
     '120 &divide; 40 = <b>3 laps</b> and 120 &divide; 60 = <b>2 laps</b> <b>[1]</b>'],
    'note':'The lap counts are a free check on the LCM: if either division does not come out whole, the LCM is wrong. Worth teaching as a habit.'},
   {'n':'9', 'marks':4, 'lines':[
     '(a) 36 &lt; 40 &lt; 49, so between <b>6 and 7</b>',
     '(b) 144 &lt; 150 &lt; 169, so between <b>12 and 13</b>',
     '(c) 27 &lt; 30 &lt; 64, so between <b>3 and 4</b>',
     '(d) 125 &lt; 200 &lt; 216, so between <b>5 and 6</b>'],
    'note':'The two squares or cubes must be shown — the question says so, and a bare pair of numbers scores nothing. (d) is the one that catches people: 200 feels like it should be much further from 216 than it is, because cubes are so far apart by then.'},
  ]},

 {'title':'Paper C — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':4, 'lines':[
     '(a) 1176 = 2 &times; 588 = 4 &times; 294 = 8 &times; 147 = 8 &times; 3 &times; 49 <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;= <b>2<sup>3</sup> &times; 3 &times; 7<sup>2</sup></b> <b>[1]</b>',
     '(b) The indices are 3, 1 and 2 <b>[1]</b>. Two of them are odd, so 1176 is <b>not</b> a perfect square <b>[1]</b>'],
    'note':'In (b) the reason carries the second mark and it must be about the indices. &ldquo;It is not on the list of squares&rdquo; is not a reason and scores one mark at most. A student who says &ldquo;the 7<sup>2</sup> makes it a square&rdquo; has spotted a real thing — 49 is a square factor — but has not answered the question asked.'},
   {'n':'2', 'marks':4, 'lines':[
     '(a) 1080 = <b>2<sup>3</sup> &times; 3<sup>3</sup> &times; 5</b> <b>[1]</b>',
     '(b) Indices are 3, 3 and 1 — all odd, so one more of each prime is needed <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;<i>k</i> = 2 &times; 3 &times; 5 = <b>30</b> <b>[1]</b>',
     '(c) 1080 &times; 30 = 2<sup>4</sup> &times; 3<sup>4</sup> &times; 5<sup>2</sup>, halve the indices: 2<sup>2</sup> &times; 3<sup>2</sup> &times; 5 = <b>180</b> <b>[1]</b>'],
    'note':'This is the central technique of the paper: a number is a square exactly when every index is even, and its root is found by halving every index. In (c), a student who works out 32400 and then hunts for its root has done far more work than the question intended — give the mark, but show them the short route.'},
   {'n':'3', 'marks':3, 'lines':[
     '(a) For a cube every index must be a multiple of 3. In 2<sup>3</sup> &times; 3<sup>3</sup> &times; 5 the first two already are; the 5 needs two more <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;<i>m</i> = 5<sup>2</sup> = <b>25</b> <b>[1]</b>',
     '(b) 1080 &times; 25 = 2<sup>3</sup> &times; 3<sup>3</sup> &times; 5<sup>3</sup> = 27000, and dividing the indices by 3 gives 2 &times; 3 &times; 5 = <b>30</b> <b>[1]</b>'],
    'note':'Run this straight after question 2 in any review: same number, same method, one word changed. Halve the indices for a square root, divide them by 3 for a cube root. Students who see those as two rules have not seen the pattern.'},
   {'n':'4', 'marks':4, 'lines':[
     '(a) HCF &times; LCM = product, so 8 &times; 96 = <b>768</b> <b>[1]</b>',
     '(b) 768 &divide; 24 = <b>32</b> <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;Verify: 24 = 2<sup>3</sup> &times; 3 and 32 = 2<sup>5</sup>, so HCF = 2<sup>3</sup> = 8 ✓ and LCM = 2<sup>5</sup> &times; 3 = 96 ✓ <b>[1]</b>',
     '(c) <b>8 and 96</b> <b>[1]</b>'],
    'note':'The verification in (b) is the mark, not the arithmetic — the product rule alone does not prove a pair is correct. See Paper D question 3 for the same point made from the other side.'},
   {'n':'5', 'marks':3, 'lines':[
     'Product = 4 &times; 60 = 240 <b>[1]</b>',
     '<i>n</i> = 240 &divide; 12 = <b>20</b> <b>[1]</b>',
     'Verify: 12 = 2<sup>2</sup> &times; 3 and 20 = 2<sup>2</sup> &times; 5, so HCF = 2<sup>2</sup> = 4 ✓ and LCM = 2<sup>2</sup> &times; 3 &times; 5 = 60 ✓ <b>[1]</b>'],
    'note':'Some students will find <i>n</i> = 20 by listing instead, which is fine and gets both marks — but the verification mark still has to be earned with prime factorisations, because the question said so.'},
   {'n':'6', 'marks':4, 'lines':[
     '(a) 9 &times; &minus;8 = <b>&minus;72</b>', '(b) 15 &divide; &minus;5 = <b>&minus;3</b>',
     '(c) <b>64</b>', '(d) &minus;16 + 16 = <b>0</b>'],
    'note':'(d) is the whole bracket trap in one line, and a student who answers 32 has treated the two terms as identical. Make them read it aloud: &ldquo;minus four squared&rdquo; and &ldquo;bracket minus four bracket squared&rdquo; are different instructions.'},
   {'n':'7', 'marks':4, 'lines':[
     '(a) 6 = 2 &times; 3, 10 = 2 &times; 5, 15 = 3 &times; 5, so LCM = 2 &times; 3 &times; 5 = <b>30 seconds</b> <b>[1]</b>',
     '(b) 5 minutes = 300 seconds, and 300 &divide; 30 = <b>10 times</b> <b>[1]</b>',
     '(c) 8 = 2<sup>3</sup>, so the LCM of all four is 2<sup>3</sup> &times; 3 &times; 5 = 120 seconds <b>[1]</b> = <b>2 minutes</b> <b>[1]</b>'],
    'note':'Note what the fourth light does: none of 6, 10 or 15 has more than one factor of 2, so adding 2<sup>3</sup> multiplies the answer by four. Students often expect adding a shorter interval to bring the meeting point sooner.'},
   {'n':'8', 'marks':4, 'lines':[
     '(a) 17<sup>2</sup> = 289 and 18<sup>2</sup> = 324, and 289 &lt; 300 &lt; 324 <b>[1]</b>',
     '(b) 300 &minus; 289 = 11 but 324 &minus; 300 = 24, so it is nearer <b>17</b> <b>[1]</b>',
     '(c) <b>17.3</b> <b>[1]</b>, justified by 17.3<sup>2</sup> = 299.29 (just under 300) and 17.4<sup>2</sup> = 302.76 (over) <b>[1]</b>'],
    'note':'In (c) accept 17.3 only with a squaring shown — the question demands the justification. A student who writes 17.5 has split the difference between 17 and 18 without noticing that 300 is much closer to 289 than to 324, which is exactly the reasoning (b) was setting up.'},
  ]},

 {'title':'Paper D — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':4, 'lines':[
     '(a) 2520 = 8 &times; 315 = 8 &times; 9 &times; 35 <b>[1]</b> = <b>2<sup>3</sup> &times; 3<sup>2</sup> &times; 5 &times; 7</b> <b>[1]</b>',
     '(b) Take each prime to the largest even index available: 2<sup>2</sup> &times; 3<sup>2</sup> = <b>36</b> <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;2520 &divide; 36 = <b>70</b> <b>[1]</b>'],
    'note':'In (b) the answer 9 shows a student who found <i>a</i> square factor rather than the largest — award one mark. Answer 4 likewise. The method is to sweep every prime at once, not to spot one.'},
   {'n':'2', 'marks':4, 'lines':[
     '(a) Indices are 3, 2, 1, 1 <b>[1]</b>. The 3, the 5 and the 7 sit at odd indices, so one more of each is needed <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;<i>k</i> = 2 &times; 5 &times; 7 = <b>70</b> <b>[1]</b>',
     '(b) 2520 &times; 70 = 2<sup>4</sup> &times; 3<sup>2</sup> &times; 5<sup>2</sup> &times; 7<sup>2</sup>, halve the indices: 2<sup>2</sup> &times; 3 &times; 5 &times; 7 = <b>420</b> <b>[1]</b>'],
    'note':'Notice that <i>k</i> = 70 is also the answer to question 1(b) — because 2520 &divide; (largest square factor) is exactly what must be multiplied back in. Worth pointing out; it is not a coincidence and it makes the pair of questions one idea.'},
   {'n':'3', 'marks':4, 'lines':[
     '(a) 15 &times; 90 = <b>1350</b> <b>[1]</b>',
     '(b) 1350 &divide; 45 = <b>30</b> <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;Verify: 45 = 3<sup>2</sup> &times; 5 and 30 = 2 &times; 3 &times; 5, so HCF = 3 &times; 5 = 15 ✓ and LCM = 2 &times; 3<sup>2</sup> &times; 5 = 90 ✓ <b>[1]</b>',
     '(c) Both numbers must be <b>multiples of the HCF</b>, and 20 is not a multiple of 15 <b>[1]</b>'],
    'note':'(c) accepts the equivalent reason from the other side — both numbers must also be factors of the LCM, and 20 is not a factor of 90. Either argument earns the mark; a student who only says &ldquo;20 does not work&rdquo; without a reason earns nothing.'},
   {'n':'4', 'marks':4, 'lines':[
     '(a) <b>&minus;32</b>', '(b) 25 &minus; 25 = <b>0</b>', '(c) <b>&minus;27</b>', '(d) 20 &times; &minus;2 = <b>&minus;40</b>'],
    'note':'(b) and (c) are the bracket trap twice over. In (d), working left to right matters: &minus;120 &divide; &minus;6 = 20 first, then &times; &minus;2. A student who counts signs instead gets the sign right by luck here, which is worth knowing about when you mark it.'},
   {'n':'5', 'marks':4, 'lines':[
     '(a) 5 hours at &minus;4 &deg;C per hour: 5 + (5 &times; &minus;4) = <b>&minus;15 &deg;C</b> <b>[1]</b>',
     '(b) Total change needed = &minus;27 &minus; 5 = &minus;32 <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;&minus;32 &divide; &minus;4 = 8 hours, so <b>14:00</b> <b>[1]</b>',
     '(c) The answer counts <b>hours</b>, not degrees. Both the total drop and the hourly drop point the same way, so asking how many of one fit into the other has an ordinary positive answer — a negative number of hours would be meaningless <b>[1]</b>'],
    'note':'(c) is the mark that tells you whether the sign rule is understood or recited. Accept any answer making the point that the quotient is a count, not a temperature. &ldquo;Because two negatives make a positive&rdquo; is a restatement of the rule, not an explanation, and scores nothing.'},
   {'n':'6', 'marks':5, 'lines':[
     'Student P: 432 <b>is</b> a common multiple of 18 and 24, but it is not the <b>lowest</b> one <b>[1]</b>. '
     'Multiplying two numbers always gives a common multiple; it only gives the LCM when the HCF is 1 <b>[1]</b>',
     'Student Q: taking the <b>lower</b> power of only the <b>shared</b> primes is the recipe for the HCF, so 6 is the HCF of 18 and 24, not the LCM <b>[1]</b>. '
     'For the LCM every prime is taken at its higher power <b>[1]</b>',
     'Correct: LCM = 2<sup>3</sup> &times; 3<sup>2</sup> = <b>72</b> <b>[1]</b>'],
    'note':'These are the two errors that account for nearly every lost LCM mark, and it is worth showing that they are related: 432 &divide; 72 = 6, which is exactly Student Q&rsquo;s answer. Student P overshot by precisely the factor Student Q returned, because HCF &times; LCM = the product.'},
   {'n':'7', 'marks':5, 'lines':[
     '(i) The mistake: halving instead of rooting. A square root asks what number multiplied by <b>itself</b> gives 81 <b>[1]</b>. '
     'Correct: <b>&radic;81 = 9</b>, since 9 &times; 9 = 81 <b>[1]</b>',
     '(ii) The mistake: the sign rule has been applied to an <b>addition</b> <b>[1]</b>. '
     'Correct: &minus;4 + &minus;6 = <b>&minus;10</b> — owing 4 and then owing 6 more leaves you owing 10 <b>[1]</b>',
     'The rule applies only to <b>multiplication and division</b>, never to addition or subtraction <b>[1]</b>'],
    'note':'The final mark is the one that matters most on this paper. A student can correct both lines and still not be able to say when the rule applies — and that student will make error (ii) again next week. Make them write the sentence out.'},
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
    p = os.path.join(OUT, 'maths-integers-paper-%s.pdf' % code)
    build_paper(spec, p)
    files.append(p)

for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)

p = os.path.join(OUT, 'maths-integers-answers.pdf')
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
