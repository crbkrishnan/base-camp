#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)

EYEBROW = 'Base Camp · IGCSE Mathematics · Grade 7 · Number'
TOPIC   = 'Place Value, Rounding and Estimating'

INSTR_MED = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Every number on this paper is designed to be handled on paper.',
    'The decimal point does not move. The <b>digits</b> move: one column left for each &times; 10, one column right for each &divide; 10.',
    '<b>&times; 0.1 is the same as &divide; 10</b>, and <b>&divide; 0.1 is the same as &times; 10</b>. Rewrite the question that way before you calculate.',
    'Read every rounding instruction twice: <b>decimal places</b> and <b>significant figures</b> give different answers on the same number.',
    'Write a zero before the decimal point (0.47, never .47), and keep placeholder zeros (38 000, never 38).',
    'The mark for each question is shown in square brackets on the right.',
]
INSTR_HARD = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Every number on this paper is designed to come out exactly, or to be estimated.',
    'The rules for powers of ten, rounding and significant figures are not printed on this paper. You are expected to know them.',
    'When you estimate, round every number to <b>1 significant figure</b> and show what you rounded each one to — that is usually the first mark.',
    'Several questions ask whether an estimate is too big or too small. Track what each rounding did to the answer; if the two roundings pull in opposite directions, saying so is a correct answer.',
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
  {'section':'Section 1 — powers of ten, and 0.1',
   'text':'Complete the table. Each empty box is worth one mark.', 'marks':6,
   'grid':[['Number','&times; 100','&divide; 100'],
           ['5.3','',''],
           ['47','',''],
           ['0.6','','']],
   'grid_widths':[AVAIL*0.28, AVAIL*0.36, AVAIL*0.36],
   'tip':'Count the zeros to count the columns. The point stays put; the digits travel.'},

  {'text':'Work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'8.2 &times; 10','marks':1,'space':18},
            {'label':'(b)','text':'3.5 &divide; 100','marks':1,'space':18},
            {'label':'(c)','text':'0.09 &times; 1000','marks':1,'space':18},
            {'label':'(d)','text':'620 &divide; 10 000','marks':1,'space':18}]},

  {'text':'Work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'7.4 &times; 0.1','marks':1,'space':18},
            {'label':'(b)','text':'5 &divide; 0.1','marks':1,'space':18},
            {'label':'(c)','text':'3.8 &times; 0.01','marks':1,'space':18},
            {'label':'(d)','text':'6 &divide; 0.01','marks':1,'space':18}]},

  {'section':'Section 2 — rounding',
   'text':'Round <b>4736</b> to:', 'marks':4,
   'parts':[{'label':'(a)','text':'the nearest 10','marks':1,'space':18},
            {'label':'(b)','text':'the nearest 100','marks':1,'space':18},
            {'label':'(c)','text':'the nearest 1000','marks':1,'space':18},
            {'label':'(d)','text':'1 significant figure','marks':1,'space':18}]},

  {'text':'Round <b>12.3648</b> to:', 'marks':4,
   'parts':[{'label':'(a)','text':'1 decimal place','marks':1,'space':18},
            {'label':'(b)','text':'2 decimal places','marks':1,'space':18},
            {'label':'(c)','text':'3 decimal places','marks':1,'space':18},
            {'label':'(d)','text':'2 significant figures','marks':1,'space':18}]},

  {'text':'Round each of these to <b>2 significant figures</b>.', 'marks':4,
   'parts':[{'label':'(a)','text':'0.06382','marks':1,'space':18},
            {'label':'(b)','text':'5471','marks':1,'space':18},
            {'label':'(c)','text':'0.9047','marks':1,'space':18},
            {'label':'(d)','text':'38.72','marks':1,'space':18}]},

  {'section':'Section 3 — estimating',
   'text':'Estimate 61.4 &times; 4.8 by rounding each number to 1 significant figure. '
          'Show what you rounded each number to.', 'marks':2, 'space':30},

  {'text':'Estimate 3891 &divide; 19 by rounding each number to 1 significant figure. '
          'Show what you rounded each number to.', 'marks':2, 'space':30},
 ]}

# ----------------------------------------------------------------- PAPER B
B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — multiplying and dividing by 0.1',
   'text':'Complete the table. Each empty box is worth one mark. One of these columns makes the '
          'numbers smaller and the other makes them bigger — decide which before you start.', 'marks':6,
   'grid':[['Number','&times; 0.1','&divide; 0.1'],
           ['4.7','',''],
           ['82','',''],
           ['0.5','','']],
   'grid_widths':[AVAIL*0.28, AVAIL*0.36, AVAIL*0.36],
   'tip':'Rewrite each one first: &times; 0.1 is &divide; 10, and &divide; 0.1 is &times; 10.'},

  {'text':'Work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'6.9 &times; 0.01','marks':1,'space':18},
            {'label':'(b)','text':'0.4 &divide; 0.01','marks':1,'space':18},
            {'label':'(c)','text':'250 &times; 0.1','marks':1,'space':18},
            {'label':'(d)','text':'7.3 &divide; 0.1','marks':1,'space':18}]},

  {'text':'Fill in the missing number in each.', 'marks':2,
   'parts':[{'label':'(a)','text':'8.4 &times; ______ = 0.084','marks':1,'space':20},
            {'label':'(b)','text':'5 &divide; ______ = 500','marks':1,'space':20}]},

  {'section':'Section 2 — decimal places and significant figures',
   'text':'Round <b>0.083529</b> to:', 'marks':4,
   'parts':[{'label':'(a)','text':'2 decimal places','marks':1,'space':18},
            {'label':'(b)','text':'3 decimal places','marks':1,'space':18},
            {'label':'(c)','text':'2 significant figures','marks':1,'space':18},
            {'label':'(d)','text':'3 significant figures','marks':1,'space':18}]},

  {'text':'Round <b>74 851</b> to:', 'marks':4,
   'parts':[{'label':'(a)','text':'the nearest 100','marks':1,'space':18},
            {'label':'(b)','text':'the nearest 1000','marks':1,'space':18},
            {'label':'(c)','text':'2 significant figures','marks':1,'space':18},
            {'label':'(d)','text':'3 significant figures','marks':1,'space':18}]},

  {'text':'Write down <b>any</b> number that rounds to:', 'marks':4,
   'parts':[{'label':'(a)','text':'60, to the nearest 10','marks':1,'space':18},
            {'label':'(b)','text':'4.7, to 1 decimal place','marks':1,'space':18},
            {'label':'(c)','text':'0.03, to 2 decimal places','marks':1,'space':18},
            {'label':'(d)','text':'200, to 1 significant figure','marks':1,'space':18}]},

  {'section':'Section 3 — estimating',
   'text':'A customer buys 4 shirts at 18.90 rupees each, 3 notebooks at 6.20 rupees each, '
          'and 2 bags at 44.50 rupees each.', 'marks':3,
   'parts':[{'label':'(a)','text':'Estimate the total bill by rounding each price to 1 significant figure.','marks':2,'space':34},
            {'label':'(b)','text':'The till prints a total of 1782.20 rupees. Explain how your estimate shows '
                                  'this must be wrong.','marks':1,'space':26}]},

  {'text':'This question is about 46 &times; 78.', 'marks':3,
   'parts':[{'label':'(a)','text':'Estimate the answer by rounding each number to 1 significant figure.','marks':1,'space':22},
            {'label':'(b)','text':'Work out the exact answer.','marks':1,'space':26},
            {'label':'(c)','text':'State whether your estimate is bigger or smaller than the exact answer, '
                                  'and explain why.','marks':1,'space':26}]},
 ]}

# ----------------------------------------------------------------- PAPER C
C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — chains and missing multipliers',
   'text':'Work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'5 &times; 0.1 &times; 0.1','marks':1,'space':20},
            {'label':'(b)','text':'3 &divide; 0.1 &divide; 0.1','marks':1,'space':20},
            {'label':'(c)','text':'8 &times; 0.1 &divide; 0.01','marks':1,'space':20},
            {'label':'(d)','text':'0.6 &divide; 0.1 &times; 0.01','marks':1,'space':20}]},

  {'text':'Fill in the missing number in each.', 'marks':4,
   'parts':[{'label':'(a)','text':'7.2 &times; ______ = 0.072','marks':1,'space':20},
            {'label':'(b)','text':'0.9 &divide; ______ = 90','marks':1,'space':20},
            {'label':'(c)','text':'45 &times; ______ = 4.5','marks':1,'space':20},
            {'label':'(d)','text':'0.03 &divide; ______ = 3','marks':1,'space':20}]},

  {'text':'Round <b>0.0049682</b> to:', 'marks':4,
   'parts':[{'label':'(a)','text':'2 decimal places','marks':1,'space':18},
            {'label':'(b)','text':'3 decimal places','marks':1,'space':18},
            {'label':'(c)','text':'2 significant figures','marks':1,'space':20},
            {'label':'(d)','text':'3 significant figures','marks':1,'space':20}]},

  {'section':'Section 2 — why the two kinds of rounding differ',
   'text':'This question is about the number 0.04728.', 'marks':4,
   'parts':[{'label':'(a)','text':'Round it to 2 decimal places and to 2 significant figures, then explain '
                                  'carefully why the two answers are different.','marks':2,'space':36},
            {'label':'(b)','text':'Write down a number for which rounding to 2 decimal places and rounding to '
                                  '2 significant figures give the <b>same</b> answer, and explain why it does.','marks':2,'space':36}]},

  {'text':'This question is about 8237 &divide; 38.', 'marks':4,
   'parts':[{'label':'(a)','text':'Estimate the answer by rounding each number to 1 significant figure.','marks':1,'space':22},
            {'label':'(b)','text':'The exact answer, to 1 decimal place, is 216.8. State whether your estimate '
                                  'is bigger or smaller than this.','marks':1,'space':20},
            {'label':'(c)','text':'Explain why your estimate came out on that side, referring to what <b>each</b> '
                                  'rounding did to the answer.','marks':2,'space':36}]},

  {'section':'Section 3 — what a rounded number really tells you',
   'text':'A length is measured as 8.4 cm, correct to 1 decimal place.', 'marks':5,
   'parts':[{'label':'(a)','text':'Write down the smallest value the true length could be.','marks':1,'space':20},
            {'label':'(b)','text':'Describe carefully the largest value the true length could be.','marks':2,'space':30},
            {'label':'(c)','text':'A second length is 12 cm, correct to the nearest whole number. Between what '
                                  'two values does this length lie?','marks':2,'space':30}]},

  {'text':'A student uses a calculator to work out 48.6 &times; 0.37 and writes down 179.82.', 'marks':5,
   'parts':[{'label':'(a)','text':'Estimate 48.6 &times; 0.37 by rounding each number to 1 significant figure.','marks':2,'space':28},
            {'label':'(b)','text':'Use your estimate to show that 179.82 must be wrong, and suggest what the '
                                  'student probably typed in.','marks':2,'space':34},
            {'label':'(c)','text':'Write down the correct answer.','marks':1,'space':20}]},
 ]}

# ----------------------------------------------------------------- PAPER D
D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — chains, and which numbers round where',
   'text':'Work out:', 'marks':4,
   'parts':[{'label':'(a)','text':'0.8 &times; 0.1 &times; 0.01','marks':1,'space':20},
            {'label':'(b)','text':'4 &divide; 0.01 &divide; 0.1','marks':1,'space':20},
            {'label':'(c)','text':'25 &times; 0.01 &divide; 0.1','marks':1,'space':20},
            {'label':'(d)','text':'0.06 &divide; 0.1 &times; 0.1','marks':1,'space':20}]},

  {'text':'A whole number is rounded to the nearest 100 and the answer is 500.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write down the smallest whole number this could have been.','marks':1,'space':20},
            {'label':'(b)','text':'Write down the largest whole number this could have been.','marks':1,'space':20},
            {'label':'(c)','text':'How many whole numbers round to 500 to the nearest 100? Show how you counted them.','marks':2,'space':30}]},

  {'section':'Section 2 — accuracy, and what it hides',
   'text':'Round <b>0.0298471</b> to:', 'marks':4,
   'parts':[{'label':'(a)','text':'2 decimal places','marks':1,'space':18},
            {'label':'(b)','text':'4 decimal places','marks':1,'space':18},
            {'label':'(c)','text':'2 significant figures','marks':1,'space':20},
            {'label':'(d)','text':'3 significant figures','marks':1,'space':20}]},

  {'text':'A machine produces 0.68 kg of powder every minute. It runs for 4950 minutes.', 'marks':4,
   'parts':[{'label':'(a)','text':'Estimate the total mass produced, by rounding each number to 1 significant figure.','marks':2,'space':28},
            {'label':'(b)','text':'Work out the exact total mass.','marks':1,'space':28},
            {'label':'(c)','text':'State whether your estimate is bigger or smaller than the exact answer, and '
                                  'explain why.','marks':1,'space':26}]},

  {'text':'A mass is recorded as 3.60 kg, correct to 2 decimal places.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write down the smallest value the true mass could be.','marks':1,'space':20},
            {'label':'(b)','text':'Describe carefully the largest value the true mass could be.','marks':1,'space':22},
            {'label':'(c)','text':'Explain why writing 3.6 kg instead of 3.60 kg would give the reader different '
                                  'information.','marks':2,'space':32}]},

  {'section':'Section 3 — marking somebody else',
   'text':'Two students were each asked to round 5.7449 to 2 decimal places.<br/>'
          '<b>Student V wrote:</b> &ldquo;5.7449 &rarr; 5.745 &rarr; 5.75&rdquo;<br/>'
          '<b>Student W wrote:</b> &ldquo;the 9 on the end makes it round up, so 5.75&rdquo;<br/>'
          'For each student, describe exactly what they did wrong. Then give the correct answer.', 'marks':5, 'space':58},

  {'text':'A student has written two answers in his book, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;6.2 &divide; 0.01 = 0.062, because dividing makes numbers smaller.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;0.04728 to 2 significant figures is 0.05.&rdquo;<br/>'
          'For each one, explain the mistake and give the correct answer. Then state, for each, the '
          'general rule the student has missed.', 'marks':5, 'space':60},
 ]}

# ----------------------------------------------------------------- mark scheme
SCHEMES = [
 {'title':'Paper A — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     '5.3 &rarr; <b>530</b> and <b>0.053</b>',
     '47 &rarr; <b>4700</b> and <b>0.47</b>',
     '0.6 &rarr; <b>60</b> and <b>0.006</b>'],
    'note':'One mark per box. Watch for the placeholder zeros: 0.6 &divide; 100 is 0.006, and a student who writes 0.06 has moved the digits only one column. Accept 530 or 530.0 in the first box.'},
   {'n':'2', 'marks':4, 'lines':['(a) <b>82</b>', '(b) <b>0.035</b>', '(c) <b>90</b>', '(d) <b>0.062</b>'],
    'note':'(c) is the one that defeats the &ldquo;move the point&rdquo; rule — there is nothing to move past. Moving the digits three columns left puts the 9 in the tens column and the empty columns fill themselves. (d) needs four columns right.'},
   {'n':'3', 'marks':4, 'lines':['(a) <b>0.74</b>', '(b) <b>50</b>', '(c) <b>0.038</b>', '(d) <b>600</b>'],
    'note':'Rewrite before calculating: (a) is 7.4 &divide; 10, (b) is 5 &times; 10, (c) is 3.8 &divide; 100, (d) is 6 &times; 100. A student who answers 0.5 to (b) and 0.06 to (d) has assumed dividing always makes things smaller — the central misconception of the topic.'},
   {'n':'4', 'marks':4, 'lines':['(a) <b>4740</b>', '(b) <b>4700</b>', '(c) <b>5000</b>', '(d) <b>5000</b>'],
    'note':'All four are the same number and all four answers are correct. (c) and (d) agree because 1 significant figure and the nearest 1000 happen to be the same accuracy here — worth pointing out, because they usually are not.'},
   {'n':'5', 'marks':4, 'lines':['(a) <b>12.4</b>', '(b) <b>12.36</b>', '(c) <b>12.365</b>', '(d) <b>12</b>'],
    'note':'Each part looks at exactly one digit — the one immediately after the place being kept. In (b) that digit is 4, so it rounds down even though an 8 follows it. A student answering 12.37 has rounded twice.'},
   {'n':'6', 'marks':4, 'lines':['(a) <b>0.064</b>', '(b) <b>5500</b>', '(c) <b>0.90</b>', '(d) <b>39</b>'],
    'note':'(c) must keep the trailing zero — 0.9 shows only one significant figure, and the zero is what says the answer is accurate to two. (b) must keep the placeholder zeros; answering 55 changes the number by a factor of 100.'},
   {'n':'7', 'marks':2, 'lines':['61.4 &asymp; 60 and 4.8 &asymp; 5 <b>[1]</b>', '60 &times; 5 = <b>300</b> <b>[1]</b>'],
    'note':'The first mark is for showing both rounded values. The true answer is 294.72, so the estimate is close enough to have caught any misplaced decimal point.'},
   {'n':'8', 'marks':2, 'lines':['3891 &asymp; 4000 and 19 &asymp; 20 <b>[1]</b>', '4000 &divide; 20 = <b>200</b> <b>[1]</b>'],
    'note':'The true answer is about 204.8. Estimating a division works exactly like a multiplication — round both, then use a division you can do in your head.'},
  ]},

 {'title':'Paper B — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     '4.7 &rarr; <b>0.47</b> and <b>47</b>',
     '82 &rarr; <b>8.2</b> and <b>820</b>',
     '0.5 &rarr; <b>0.05</b> and <b>5</b>'],
    'note':'One mark per box. The whole table exists to make one point visible: the &times; column always shrinks and the &divide; column always grows. A student whose two columns have gone the other way has the central rule of this unit backwards, and no amount of practice on individual questions will fix it until that is named.'},
   {'n':'2', 'marks':4, 'lines':['(a) <b>0.069</b>', '(b) <b>40</b>', '(c) <b>25</b>', '(d) <b>73</b>'],
    'note':'(b) is the marker question: 0.4 &divide; 0.01 asks how many hundredths fit into 0.4, and the answer is 40. Anyone answering 0.004 should be sent back to the place-value board.'},
   {'n':'3', 'marks':2, 'lines':['(a) <b>0.01</b>', '(b) <b>0.01</b>'],
    'note':'Same answer both times, arrived at from opposite directions: in (a) the number shrank under a multiplication, in (b) it grew under a division. Both can only happen with a multiplier below 1.'},
   {'n':'4', 'marks':4, 'lines':['(a) <b>0.08</b>', '(b) <b>0.084</b>', '(c) <b>0.084</b>', '(d) <b>0.0835</b>'],
    'note':'(b) and (c) agree here and (a) does not, which is exactly the point: 3 decimal places and 2 significant figures land on the same column for this number, but 2 decimal places does not. The agreement is a coincidence of the number, not a rule.'},
   {'n':'5', 'marks':4, 'lines':['(a) <b>74 900</b>', '(b) <b>75 000</b>', '(c) <b>75 000</b>', '(d) <b>74 900</b>'],
    'note':'Note the pairing: (a) matches (d) and (b) matches (c). For a five-digit number, 3 significant figures <i>is</i> the nearest 100 and 2 significant figures <i>is</i> the nearest 1000. Seeing that connection is what stops the two ideas feeling like separate topics.'},
   {'n':'6', 'marks':4, 'lines':[
     '(a) any number from <b>55</b> up to but not including 65 — e.g. 58',
     '(b) any number from <b>4.65</b> up to but not including 4.75 — e.g. 4.72',
     '(c) any number from <b>0.025</b> up to but not including 0.035 — e.g. 0.031',
     '(d) any number from <b>150</b> up to but not including 250 — e.g. 210'],
    'note':'Award each mark for any value in range. This question is rounding run backwards, and students who can do it forwards but not backwards have memorised a procedure rather than understood the interval. If a student offers the upper bound itself (65, 4.75, 0.035, 250), it rounds the other way — a useful mistake to talk about.'},
   {'n':'7', 'marks':3, 'lines':[
     '(a) 18.90 &asymp; 20, 6.20 &asymp; 6, 44.50 &asymp; 40 <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;(4 &times; 20) + (3 &times; 6) + (2 &times; 40) = 80 + 18 + 80 = <b>178 rupees</b> <b>[1]</b>',
     '(b) 1782.20 is about <b>ten times</b> the estimate, so a decimal point has been misplaced somewhere. The true total is 183.20 <b>[1]</b>'],
    'note':'The exact bill is 183.20, so the estimate of 178 was within 3%. This is the single most useful thing on the paper: a ten-second check that catches an error of a factor of ten, which is by far the most common kind.'},
   {'n':'8', 'marks':3, 'lines':['(a) 46 &asymp; 50 and 78 &asymp; 80, so 50 &times; 80 = <b>4000</b> <b>[1]</b>',
     '(b) 46 &times; 78 = <b>3588</b> <b>[1]</b>',
     '(c) <b>Bigger.</b> Both numbers were rounded up, and multiplying two larger numbers gives a larger product <b>[1]</b>'],
    'note':'(c) needs the reason, not just the direction. &ldquo;Bigger because 4000 &gt; 3588&rdquo; is a comparison, not an explanation, and earns nothing — the student must refer to what the rounding did.'},
  ]},

 {'title':'Paper C — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':4, 'lines':['(a) <b>0.05</b>', '(b) <b>300</b>', '(c) <b>80</b>', '(d) <b>0.06</b>'],
    'note':'Work left to right and track the columns. (c) and (d) each move the digits one way and then the other: in (c) one right then two left, a net one left; in (d) one left then two right, a net one right. Students who try to shortcut by counting decimals usually lose the direction.'},
   {'n':'2', 'marks':4, 'lines':['(a) <b>0.01</b>', '(b) <b>0.01</b>', '(c) <b>0.1</b>', '(d) <b>0.01</b>'],
    'note':'Ask two questions each time: did the number get bigger or smaller, and by how many columns? In (b) and (d) the number grew under a division, which is only possible with a divisor below 1.'},
   {'n':'3', 'marks':4, 'lines':['(a) <b>0.00</b>', '(b) <b>0.005</b>', '(c) <b>0.0050</b>', '(d) <b>0.00497</b>'],
    'note':'(a) really is 0.00 — the number is smaller than half a hundredth, so to that accuracy it rounds away to nothing, and that is a correct answer rather than a failure. (c) must keep its trailing zero, or it shows one significant figure instead of two.'},
   {'n':'4', 'marks':4, 'lines':[
     '(a) 2 d.p. gives <b>0.05</b>; 2 s.f. gives <b>0.047</b> <b>[1]</b>. Decimal places are counted from the '
     'point, so only two digits survive; significant figures are counted from the first non-zero digit, so the '
     'two leading zeros are placeholders and do not count <b>[1]</b>',
     '(b) Any number between 0.1 and 1 written to two decimal places, such as <b>0.25</b> or <b>0.36</b> <b>[1]</b>. '
     'For such a number the first significant figure is the tenths digit, so the second significant figure is '
     'the hundredths digit — which is exactly where two decimal places stops <b>[1]</b>'],
    'note':'Accept other valid examples in (b), but the explanation mark requires the student to say <i>why</i> the two counts coincide, not merely that they do. A student offering 12.34 has also found a case where the answers agree in value, and the same reasoning applies — award it.'},
   {'n':'5', 'marks':4, 'lines':['(a) 8237 &asymp; 8000 and 38 &asymp; 40, so 8000 &divide; 40 = <b>200</b> <b>[1]</b>',
     '(b) <b>Smaller</b> than 216.8 <b>[1]</b>',
     '(c) The top was rounded <b>down</b> (8237 to 8000), and sharing out less gives less each <b>[1]</b>. '
     'The bottom was rounded <b>up</b> (38 to 40), and sharing between more also gives less each. Both changes '
     'push the answer down, so the estimate had to be too low <b>[1]</b>'],
    'note':'Both marks in (c) require the two roundings to be handled separately. This is the question that distinguishes a student who estimates from one who merely rounds — and it is the reasoning that lets you say confidently which side of the truth you are on.'},
   {'n':'6', 'marks':5, 'lines':['(a) <b>8.35 cm</b> <b>[1]</b>',
     '(b) The true length can be anything <b>up to but not including 8.45 cm</b> <b>[1]</b>. '
     '8.45 itself would round up to 8.5, so it is excluded <b>[1]</b>',
     '(c) The true length lies between <b>11.5 cm and 12.5 cm</b> <b>[1]</b>, including 11.5 but not '
     'including 12.5 <b>[1]</b>'],
    'note':'The second mark in (b) and in (c) is for the care about the upper end. &ldquo;Between 8.35 and 8.45&rdquo; earns the first mark only; the point of the question is that one end is included and the other is not.'},
   {'n':'7', 'marks':5, 'lines':['(a) 48.6 &asymp; 50 and 0.37 &asymp; 0.4 <b>[1]</b>, so 50 &times; 0.4 = <b>20</b> <b>[1]</b>',
     '(b) 179.82 is about <b>ten times</b> the estimate of 20, so it cannot be right <b>[1]</b>. '
     'The student probably typed <b>3.7</b> instead of 0.37 — that gives exactly 179.82 <b>[1]</b>',
     '(c) 48.6 &times; 0.37 = <b>17.982</b> <b>[1]</b>'],
    'note':'The estimate mark in (a) requires 0.37 to be rounded to 0.4, not to 0 — rounding to 1 significant figure means one <i>significant</i> figure, and the 3 is the first one. A student who rounds 0.37 to 0 gets an estimate of 0 and learns nothing.'},
  ]},

 {'title':'Paper D — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':4, 'lines':['(a) <b>0.0008</b>', '(b) <b>4000</b>', '(c) <b>2.5</b>', '(d) <b>0.06</b>'],
    'note':'(d) returns to where it started, because &divide; 0.1 and &times; 0.1 undo one another exactly. A student who does not spot that has not connected the two operations, and it is worth showing them the pair before moving on.'},
   {'n':'2', 'marks':4, 'lines':['(a) <b>450</b> <b>[1]</b>', '(b) <b>549</b> <b>[1]</b>',
     '(c) From 450 to 549 inclusive <b>[1]</b>, which is 549 &minus; 450 + 1 = <b>100 whole numbers</b> <b>[1]</b>'],
    'note':'The &ldquo;+ 1&rdquo; in (c) is where the mark is won or lost — 549 &minus; 450 = 99 counts the gaps, not the numbers. Note that 550 rounds to 600, which is why the top of the range is 549 and not 550.'},
   {'n':'3', 'marks':4, 'lines':['(a) <b>0.03</b>', '(b) <b>0.0298</b>', '(c) <b>0.030</b>', '(d) <b>0.0298</b>'],
    'note':'(c) is the difficult one: the first two significant figures are 2 and 9, and the next digit is 8, so 29 rounds up to 30, giving 0.030. The trailing zero must be written, both because it is the second significant figure and because dropping it gives 0.03, which shows only one.'},
   {'n':'4', 'marks':4, 'lines':['(a) 0.68 &asymp; 0.7 and 4950 &asymp; 5000 <b>[1]</b>, so 0.7 &times; 5000 = <b>3500 kg</b> <b>[1]</b>',
     '(b) 0.68 &times; 4950 = <b>3366 kg</b> <b>[1]</b>',
     '(c) <b>Bigger.</b> Both numbers were rounded up, so the product must be too large <b>[1]</b>'],
    'note':'The estimate is out by 134 on 3366, which is about 4%. Worth noting that multiplying by 0.7 gives a smaller answer than 5000 — the estimate is still a multiplication that shrinks, which some students find hard to accept even after the earlier questions.'},
   {'n':'5', 'marks':4, 'lines':['(a) <b>3.595 kg</b> <b>[1]</b>',
     '(b) Up to but <b>not including 3.605 kg</b> <b>[1]</b>',
     '(c) 3.60 says the measurement is accurate to 2 decimal places, so the true mass lies between 3.595 and '
     '3.605 <b>[1]</b>. 3.6 would say it is accurate only to 1 decimal place, giving a range from 3.55 to 3.65 — '
     'ten times wider. The trailing zero is information, not decoration <b>[1]</b>'],
    'note':'(c) is the idea the whole question exists for, and it is the reason mark schemes insist on trailing zeros elsewhere on this paper. A student who thinks 3.6 and 3.60 are &ldquo;the same number&rdquo; is right about the value and wrong about the claim.'},
   {'n':'6', 'marks':5, 'lines':[
     'Student V <b>rounded twice</b>, going first to 3 decimal places and then rounding that result <b>[1]</b>. '
     'The 9 pushed the 4 up to 5, and that 5 then wrongly pushed the second 4 up — but the 9 was never entitled '
     'to affect the second decimal place at all <b>[1]</b>',
     'Student W looked at the <b>wrong digit</b> — the last one — instead of the digit immediately after the '
     'place being kept <b>[1]</b>. For 2 decimal places the only digit that matters is the third one, which is a 4 <b>[1]</b>',
     'Correct: keep 5.74, the next digit is 4, so round down: <b>5.74</b> <b>[1]</b>'],
    'note':'Both students reached the same wrong answer by different routes, which is why they need separate diagnoses. The shared cure is one sentence: round the original number once, looking at exactly one digit.'},
   {'n':'7', 'marks':5, 'lines':[
     '(i) The mistake: dividing only makes a number smaller when you divide by something <b>bigger than 1</b> <b>[1]</b>. '
     'Correct: &divide; 0.01 is the same as &times; 100, so 6.2 &divide; 0.01 = <b>620</b> <b>[1]</b>',
     '(ii) The mistake: the student counted <b>decimal places</b>, not significant figures — the two leading zeros '
     'are placeholders and are not significant <b>[1]</b>. '
     'Correct: the first two significant figures are 4 and 7, and the next digit is 2, so the answer is <b>0.047</b> <b>[1]</b>',
     'The rules missed: (i) multiplying or dividing by a number between 0 and 1 reverses the direction you expect; '
     '(ii) significant figures are counted from the first non-zero digit, decimal places from the point <b>[1]</b>'],
    'note':'Worth noting to the student that 0.05 is not a random error — it is 0.04728 correct to 2 decimal places, and also to 1 significant figure. The answer was right for two other questions, which is exactly why the instruction has to be read before the number is touched.'},
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
    p = os.path.join(OUT, 'maths-placevalue-paper-%s.pdf' % code)
    build_paper(spec, p)
    files.append(p)

for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)

p = os.path.join(OUT, 'maths-placevalue-answers.pdf')
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
