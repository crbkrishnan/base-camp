#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)

EYEBROW = 'Base Camp · IGCSE Mathematics · Grade 7 · Algebra'
TOPIC   = 'Constructing and Solving Equations'

INSTR_MED = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Every equation on this paper has a whole-number solution unless it says otherwise.',
    'Whatever you do to one side, <b>do to the other</b>. Write the operation beside each line, like &ldquo;&minus;4&rdquo; or &ldquo;&divide;3&rdquo;.',
    'Strip the numbers off the x first and <b>divide last</b>. Dividing early makes you divide every term.',
    'Every answer can be checked by putting it back into the <b>original</b> equation. Do it every time — it costs ten seconds and it catches nearly every error.',
    'The mark for each question is shown in square brackets on the right.',
]
INSTR_HARD = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Every equation on this paper is designed to come out exactly.',
    'The method is not printed on this paper. You are expected to know it.',
    'When a bracket is <b>subtracted</b>, the minus sign multiplies every term inside it. When a fraction wraps a whole side, multiplying by the denominator undoes it in one move.',
    'Several questions ask you to explain, prove or diagnose. A correct calculation is not by itself an explanation — say what the algebra shows.',
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
  {'section':'Section 1 — one step, then two',
   'text':'Complete the table. Each empty box is worth one mark. In the last column, show the '
          'substitution that proves your answer is right.', 'marks':6,
   'grid':[['Equation','Solution','Check (substitute back)'],
           ['x + 9 = 17','',''],
           ['5x = 45','',''],
           ['3x + 2 = 20','','']],
   'grid_widths':[AVAIL*0.28, AVAIL*0.24, AVAIL*0.48],
   'tip':'The check column is not decoration — it is where you find out whether you were right before the marker does.'},

  {'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'x &minus; 6 = 11','marks':1,'space':18},
            {'label':'(b)','text':'7x = 56','marks':1,'space':18},
            {'label':'(c)','text':'x &divide; 4 = 6','marks':1,'space':18},
            {'label':'(d)','text':'x + 13 = 5','marks':1,'space':18}]},

  {'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'2x + 5 = 17','marks':1,'space':22},
            {'label':'(b)','text':'4x &minus; 3 = 25','marks':1,'space':22},
            {'label':'(c)','text':'5x + 8 = 8','marks':1,'space':22},
            {'label':'(d)','text':'3x &minus; 11 = 4','marks':1,'space':22}]},

  {'section':'Section 2 — both sides, and brackets',
   'text':'Solve, showing each step:', 'marks':4,
   'parts':[{'label':'(a)','text':'5x = 2x + 18','marks':2,'space':30},
            {'label':'(b)','text':'7x &minus; 4 = 3x + 12','marks':2,'space':30}]},

  {'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'2(x + 5) = 16','marks':2,'space':28},
            {'label':'(b)','text':'3(x &minus; 4) = 21','marks':2,'space':28}]},

  {'section':'Section 3 — building the equation yourself',
   'text':'I think of a number, multiply it by 5, then subtract 3. The result is 32.', 'marks':3,
   'parts':[{'label':'(a)','text':'Using <i>n</i> for the number, form an equation.','marks':1,'space':20},
            {'label':'(b)','text':'Solve it.','marks':1,'space':24},
            {'label':'(c)','text':'Check your answer against the original instructions.','marks':1,'space':22}]},

  {'text':'A rectangle has width <i>x</i> cm and length (<i>x</i> + 3) cm. Its perimeter is 26 cm.', 'marks':3,
   'parts':[{'label':'(a)','text':'Form an equation in x.','marks':1,'space':22},
            {'label':'(b)','text':'Solve it.','marks':1,'space':24},
            {'label':'(c)','text':'Write down the width and the length, and check the perimeter.','marks':1,'space':24}]},

  {'text':'Ali has <i>n</i> marbles. Ben has 7 more than Ali. Together they have 41 marbles.', 'marks':2,
   'parts':[{'label':'(a)','text':'Form an equation in n.','marks':1,'space':20},
            {'label':'(b)','text':'Solve it, and state how many marbles each boy has.','marks':1,'space':26}]},
 ]}

# ----------------------------------------------------------------- PAPER B
B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — one step, then two',
   'text':'Complete the table. Each empty box is worth one mark. In the last column, show the '
          'substitution that proves your answer is right.', 'marks':6,
   'grid':[['Equation','Solution','Check (substitute back)'],
           ['x &minus; 12 = 5','',''],
           ['8x = 72','',''],
           ['2x + 7 = 19','','']],
   'grid_widths':[AVAIL*0.28, AVAIL*0.24, AVAIL*0.48],
   'tip':'Write the operation beside every line you produce. Seeing it written twice is what stops one-sided working.'},

  {'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'x + 14 = 9','marks':1,'space':18},
            {'label':'(b)','text':'6x = 54','marks':1,'space':18},
            {'label':'(c)','text':'x &divide; 3 = 12','marks':1,'space':18},
            {'label':'(d)','text':'9 &minus; x = 4','marks':1,'space':20}]},

  {'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'3x + 11 = 26','marks':1,'space':22},
            {'label':'(b)','text':'5x &minus; 7 = 33','marks':1,'space':22},
            {'label':'(c)','text':'2x + 15 = 7','marks':1,'space':22},
            {'label':'(d)','text':'4x &minus; 5 = 23','marks':1,'space':22}]},

  {'section':'Section 2 — both sides, and brackets',
   'text':'Solve, showing each step:', 'marks':4,
   'parts':[{'label':'(a)','text':'6x &minus; 5 = 2x + 15','marks':2,'space':30},
            {'label':'(b)','text':'8x + 3 = 5x + 21','marks':2,'space':30}]},

  {'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'4(x + 2) = 28','marks':2,'space':28},
            {'label':'(b)','text':'2(3x &minus; 1) = 22','marks':2,'space':28}]},

  {'section':'Section 3 — building the equation yourself',
   'text':'I think of a number, multiply it by 6, then add 5. The result is 41.', 'marks':3,
   'parts':[{'label':'(a)','text':'Using <i>n</i> for the number, form an equation.','marks':1,'space':20},
            {'label':'(b)','text':'Solve it.','marks':1,'space':24},
            {'label':'(c)','text':'Check your answer against the original instructions.','marks':1,'space':22}]},

  {'text':'A triangle has sides of length <i>x</i> cm, (<i>x</i> + 2) cm and (<i>x</i> + 4) cm. '
          'Its perimeter is 30 cm.', 'marks':3,
   'parts':[{'label':'(a)','text':'Form an equation in x.','marks':1,'space':22},
            {'label':'(b)','text':'Solve it.','marks':1,'space':24},
            {'label':'(c)','text':'Write down the three side lengths and check they add to 30.','marks':1,'space':24}]},

  {'text':'A father is 4 times as old as his son. Together their ages total 45.', 'marks':2,
   'parts':[{'label':'(a)','text':'Using <i>s</i> for the son&rsquo;s age, form an equation.','marks':1,'space':20},
            {'label':'(b)','text':'Solve it, and state both ages.','marks':1,'space':26}]},
 ]}

# ----------------------------------------------------------------- PAPER C
C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — brackets, and fractions',
   'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'3(2x + 1) = 4x + 15','marks':2,'space':32},
            {'label':'(b)','text':'5(x &minus; 2) = 3(x + 2)','marks':2,'space':32}]},

  {'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'4(2x &minus; 3) &minus; 2(x &minus; 5) = 22','marks':2,'space':34},
            {'label':'(b)','text':'3(x + 4) &minus; 2(x &minus; 1) = 20','marks':2,'space':34}]},

  {'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'x &divide; 4 + 3 = 8','marks':1,'space':22},
            {'label':'(b)','text':'(x &minus; 3) &divide; 5 = 4','marks':1,'space':22},
            {'label':'(c)','text':'2x &divide; 3 = 8','marks':1,'space':22},
            {'label':'(d)','text':'(2x + 1) &divide; 3 = 5','marks':1,'space':24}]},

  {'section':'Section 2 — negatives, and comparisons',
   'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'7 &minus; 2x = 1','marks':2,'space':28},
            {'label':'(b)','text':'10 &minus; 3x = 4x &minus; 4','marks':2,'space':32}]},

  {'text':'Two gyms charge differently.<br/>'
          '<b>Gym A:</b> a 300 rupee joining fee, then 40 rupees a month.<br/>'
          '<b>Gym B:</b> a 100 rupee joining fee, then 60 rupees a month.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write an expression for the total cost at each gym after <i>m</i> months.','marks':1,'space':22},
            {'label':'(b)','text':'Form and solve an equation to find after how many months the two totals are equal.','marks':2,'space':34},
            {'label':'(c)','text':'Which gym is cheaper over 15 months, and by how much?','marks':1,'space':24}]},

  {'section':'Section 3 — reasoning it out',
   'text':'Three angles lie on a straight line. They measure (2<i>x</i> + 10)&deg;, (3<i>x</i> &minus; 5)&deg; '
          'and (<i>x</i> + 25)&deg;.', 'marks':5,
   'parts':[{'label':'(a)','text':'Form an equation in x. State the angle fact you have used.','marks':1,'space':24},
            {'label':'(b)','text':'Solve it.','marks':2,'space':28},
            {'label':'(c)','text':'Work out the three angles, and check that they are consistent with your '
                                  'angle fact.','marks':2,'space':32}]},

  {'text':'Three consecutive whole numbers add up to 72.', 'marks':5,
   'parts':[{'label':'(a)','text':'Using <i>n</i> for the smallest, form an equation.','marks':1,'space':22},
            {'label':'(b)','text':'Solve it and write down the three numbers.','marks':2,'space':28},
            {'label':'(c)','text':'Explain why three consecutive whole numbers can <b>never</b> add up to 70.','marks':2,'space':34}]},
 ]}

# ----------------------------------------------------------------- PAPER D
D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — brackets and fractions',
   'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'6(x &minus; 2) = 4(x + 1)','marks':2,'space':32},
            {'label':'(b)','text':'3(2x + 5) &minus; 4(x &minus; 1) = 27','marks':2,'space':34}]},

  {'text':'Solve:', 'marks':4,
   'parts':[{'label':'(a)','text':'(3x &minus; 2) &divide; 4 = 4','marks':2,'space':30},
            {'label':'(b)','text':'x &divide; 2 + x &divide; 3 = 10','marks':2,'space':34}]},

  {'section':'Section 2 — equations that describe something',
   'text':'A rectangle has length (3<i>x</i> &minus; 1) cm and width (<i>x</i> + 2) cm. '
          'Its perimeter is 42 cm.', 'marks':4,
   'parts':[{'label':'(a)','text':'Form an equation in x and simplify it.','marks':2,'space':30},
            {'label':'(b)','text':'Solve it, then write down the length and the width and check the perimeter.','marks':2,'space':34}]},

  {'text':'Two plumbers quote for a job.<br/>'
          '<b>Plumber A:</b> a 250 rupee call-out fee, then 180 rupees an hour.<br/>'
          '<b>Plumber B:</b> no call-out fee, but 230 rupees an hour.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write an expression for each plumber&rsquo;s charge for a job lasting <i>h</i> hours.','marks':1,'space':22},
            {'label':'(b)','text':'Form and solve an equation to find the length of job for which they charge the same.','marks':2,'space':32},
            {'label':'(c)','text':'Who is cheaper for a 3-hour job, and by how much?','marks':1,'space':24}]},

  {'text':'Four consecutive whole numbers add up to 90.', 'marks':4,
   'parts':[{'label':'(a)','text':'Using <i>n</i> for the smallest, form and solve an equation, and write down '
                                  'the four numbers.','marks':2,'space':32},
            {'label':'(b)','text':'By factorising the expression for the sum, show that the sum of four '
                                  'consecutive whole numbers is <b>always even</b>.','marks':2,'space':32}]},

  {'section':'Section 3 — marking somebody else',
   'text':'Two students were each asked to solve 5x &minus; 3 = 2x + 12.<br/>'
          '<b>Student T wrote:</b> &ldquo;5x + 2x = 12 + 3, so 7x = 15, so x = 15/7&rdquo;<br/>'
          '<b>Student U wrote:</b> &ldquo;3x = 9, so x = 3&rdquo;<br/>'
          'For each student, describe exactly what they did wrong. Then give the correct solution.', 'marks':5, 'space':58},

  {'text':'A student has written two solutions in his book, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;3x + 6 = 18, so dividing by 3 gives x + 6 = 6, so x = 0.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;4(x + 3) = 20, so 4x + 3 = 20, so 4x = 17, so x = 4.25.&rdquo;<br/>'
          'For each one, explain the mistake and give the correct answer. Then state the single '
          'check that would have caught both of them.', 'marks':5, 'space':60},
 ]}

# ----------------------------------------------------------------- mark scheme
SCHEMES = [
 {'title':'Paper A — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     'x + 9 = 17 &rarr; <b>x = 8</b>, check 8 + 9 = 17 ✓',
     '5x = 45 &rarr; <b>x = 9</b>, check 5 &times; 9 = 45 ✓',
     '3x + 2 = 20 &rarr; <b>x = 6</b>, check 3(6) + 2 = 20 ✓'],
    'note':'One mark per box. Award the check box only if the substitution is actually shown — writing &ldquo;correct&rdquo; is not a check. This column exists to build the habit that makes the rest of the paper self-marking.'},
   {'n':'2', 'marks':4, 'lines':['(a) <b>x = 17</b>', '(b) <b>x = 8</b>', '(c) <b>x = 24</b>', '(d) <b>x = &minus;8</b>'],
    'note':'(c) is the one students reverse — x was divided by 4, so multiply by 4. Answering 1.5 means they divided again. (d) has a negative solution, which is an ordinary answer and not a warning sign.'},
   {'n':'3', 'marks':4, 'lines':['(a) 2x = 12, <b>x = 6</b>', '(b) 4x = 28, <b>x = 7</b>',
     '(c) 5x = 0, <b>x = 0</b>', '(d) 3x = 15, <b>x = 5</b>'],
    'note':'(c) surprises people: x = 0 is a perfectly good solution, and 5(0) + 8 = 8 checks out. Students who assume they have gone wrong and start again lose time they did not need to lose.'},
   {'n':'4', 'marks':4, 'lines':['(a) Subtract 2x: 3x = 18 <b>[1]</b>, so <b>x = 6</b> <b>[1]</b>',
     '(b) Subtract 3x: 4x &minus; 4 = 12, then add 4: 4x = 16 <b>[1]</b>, so <b>x = 4</b> <b>[1]</b>'],
    'note':'Move the smaller x term, so that what is left stays positive. Both are checkable in seconds: 5(6) = 30 = 2(6) + 18 ✓ and 7(4) &minus; 4 = 24 = 3(4) + 12 ✓'},
   {'n':'5', 'marks':4, 'lines':['(a) Divide by 2: x + 5 = 8 <b>[1]</b>, so <b>x = 3</b> <b>[1]</b>',
     '(b) Divide by 3: x &minus; 4 = 7 <b>[1]</b>, so <b>x = 11</b> <b>[1]</b>'],
    'note':'Accept expanding instead: 2x + 10 = 16 and 3x &minus; 12 = 21 reach the same answers. What earns nothing is half-expanding to 2x + 5 = 16, which is the error to watch for.'},
   {'n':'6', 'marks':3, 'lines':['(a) <b>5n &minus; 3 = 32</b> <b>[1]</b>', '(b) 5n = 35, so <b>n = 7</b> <b>[1]</b>',
     '(c) 7 &times; 5 = 35, and 35 &minus; 3 = 32 ✓ <b>[1]</b>'],
    'note':'The check in (c) must go back to the <i>words</i>, not to the student&rsquo;s own equation — otherwise a wrongly formed equation checks out perfectly and the error survives.'},
   {'n':'7', 'marks':3, 'lines':['(a) 2(x + x + 3) = 26, that is <b>4x + 6 = 26</b> <b>[1]</b>',
     '(b) 4x = 20, so <b>x = 5</b> <b>[1]</b>',
     '(c) Width <b>5 cm</b>, length <b>8 cm</b>; check 2(5 + 8) = 26 ✓ <b>[1]</b>'],
    'note':'Stopping at x = 5 loses the third mark. The question asked about the rectangle; x was only the route there.'},
   {'n':'8', 'marks':2, 'lines':['(a) <b>n + (n + 7) = 41</b>, that is 2n + 7 = 41 <b>[1]</b>',
     '(b) 2n = 34, n = 17, so Ali has <b>17</b> and Ben has <b>24</b> <b>[1]</b>'],
    'note':'Check both facts, not one: 24 is 7 more than 17 ✓ and 17 + 24 = 41 ✓. A student who answers &ldquo;17&rdquo; alone has not answered the question asked.'},
  ]},

 {'title':'Paper B — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     'x &minus; 12 = 5 &rarr; <b>x = 17</b>, check 17 &minus; 12 = 5 ✓',
     '8x = 72 &rarr; <b>x = 9</b>, check 8 &times; 9 = 72 ✓',
     '2x + 7 = 19 &rarr; <b>x = 6</b>, check 2(6) + 7 = 19 ✓'],
    'note':'One mark per box, and the check must be shown. The first row is the one where students subtract when they should add — the 12 was taken away from x, so it goes back on.'},
   {'n':'2', 'marks':4, 'lines':['(a) <b>x = &minus;5</b>', '(b) <b>x = 9</b>', '(c) <b>x = 36</b>', '(d) <b>x = 5</b>'],
    'note':'(d) has the x being subtracted. Add x to both sides to get 9 = 4 + x. Answering &minus;5 means the student subtracted 9 from 4 without dealing with the sign of the x first.'},
   {'n':'3', 'marks':4, 'lines':['(a) 3x = 15, <b>x = 5</b>', '(b) 5x = 40, <b>x = 8</b>',
     '(c) 2x = &minus;8, <b>x = &minus;4</b>', '(d) 4x = 28, <b>x = 7</b>'],
    'note':'(c) goes negative in the middle and stays there. Check it: 2(&minus;4) + 15 = &minus;8 + 15 = 7 ✓. Students who reject a negative answer on sight will lose this mark every time it appears.'},
   {'n':'4', 'marks':4, 'lines':['(a) Subtract 2x: 4x &minus; 5 = 15, then add 5: 4x = 20 <b>[1]</b>, so <b>x = 5</b> <b>[1]</b>',
     '(b) Subtract 5x: 3x + 3 = 21, then subtract 3: 3x = 18 <b>[1]</b>, so <b>x = 6</b> <b>[1]</b>'],
    'note':'Checks: 6(5) &minus; 5 = 25 = 2(5) + 15 ✓ and 8(6) + 3 = 51 = 5(6) + 21 ✓. Both sides coming out to the same number is the only confirmation anybody needs.'},
   {'n':'5', 'marks':4, 'lines':['(a) Divide by 4: x + 2 = 7 <b>[1]</b>, so <b>x = 5</b> <b>[1]</b>',
     '(b) Expand: 6x &minus; 2 = 22, so 6x = 24 <b>[1]</b>, and <b>x = 4</b> <b>[1]</b>'],
    'note':'In (b) dividing by 2 first also works and gives 3x &minus; 1 = 11 — accept either route. What does not work is 6x &minus; 1 = 22, where only the first term was multiplied.'},
   {'n':'6', 'marks':3, 'lines':['(a) <b>6n + 5 = 41</b> <b>[1]</b>', '(b) 6n = 36, so <b>n = 6</b> <b>[1]</b>',
     '(c) 6 &times; 6 = 36, and 36 + 5 = 41 ✓ <b>[1]</b>'],
    'note':'Follow the sentence in order. A student who writes 6(n + 5) = 41 has added before multiplying and will get a fraction — which is itself a signal that the equation was formed wrongly.'},
   {'n':'7', 'marks':3, 'lines':['(a) x + (x + 2) + (x + 4) = 30, that is <b>3x + 6 = 30</b> <b>[1]</b>',
     '(b) 3x = 24, so <b>x = 8</b> <b>[1]</b>',
     '(c) Sides <b>8 cm, 10 cm and 12 cm</b>; check 8 + 10 + 12 = 30 ✓ <b>[1]</b>'],
    'note':'The perimeter of a triangle is just the three sides added — there is no doubling here, unlike the rectangle questions. Students who write 2(3x + 6) = 30 have imported the wrong formula.'},
   {'n':'8', 'marks':2, 'lines':['(a) <b>s + 4s = 45</b>, that is 5s = 45 <b>[1]</b>',
     '(b) s = 9, so the son is <b>9</b> and the father is <b>36</b> <b>[1]</b>'],
    'note':'Letting s be the <i>younger</i> age keeps the algebra whole-numbered. Starting from the father gives f + f/4 = 45, which is correct but drags a fraction through the question for no reason.'},
  ]},

 {'title':'Paper C — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':4, 'lines':['(a) 6x + 3 = 4x + 15 <b>[1]</b>, so 2x = 12 and <b>x = 6</b> <b>[1]</b>',
     '(b) 5x &minus; 10 = 3x + 6 <b>[1]</b>, so 2x = 16 and <b>x = 8</b> <b>[1]</b>'],
    'note':'The first mark is for expanding correctly; the second for finishing. Checks: 3(13) = 39 = 4(6) + 15 ✓ and 5(6) = 30 = 3(10) ✓'},
   {'n':'2', 'marks':4, 'lines':['(a) 8x &minus; 12 &minus; 2x + 10 = 22, so 6x &minus; 2 = 22 <b>[1]</b>, giving <b>x = 4</b> <b>[1]</b>',
     '(b) 3x + 12 &minus; 2x + 2 = 20, so x + 14 = 20 <b>[1]</b>, giving <b>x = 6</b> <b>[1]</b>'],
    'note':'Both hinge on the subtracted bracket: &minus;2 &times; &minus;5 = +10 in (a) and &minus;2 &times; &minus;1 = +2 in (b). A student who writes &minus;10 and &minus;2 gets 5 and 5, which look plausible and are both wrong.'},
   {'n':'3', 'marks':4, 'lines':['(a) x &divide; 4 = 5, so <b>x = 20</b>', '(b) x &minus; 3 = 20, so <b>x = 23</b>',
     '(c) 2x = 24, so <b>x = 12</b>', '(d) 2x + 1 = 15, so <b>x = 7</b>'],
    'note':'(a) against (b) is the whole point: in (a) only the x is divided, so the +3 comes off first; in (b) the entire (x &minus; 3) is divided, so multiplying by 5 undoes it in one move. Reading (b) as x &divide; 5 &minus; 3 gives 35 and is the standard error.'},
   {'n':'4', 'marks':4, 'lines':['(a) &minus;2x = &minus;6 <b>[1]</b>, so <b>x = 3</b> <b>[1]</b>',
     '(b) Add 3x to both sides: 10 = 7x &minus; 4, so 14 = 7x <b>[1]</b>, giving <b>x = 2</b> <b>[1]</b>'],
    'note':'In (b), adding 3x rather than subtracting 4x is what keeps every coefficient positive. Accept the other route, but it produces &minus;7x = &minus;14 and one more chance to drop a sign.'},
   {'n':'5', 'marks':4, 'lines':['(a) Gym A: <b>300 + 40m</b>. Gym B: <b>100 + 60m</b> <b>[1]</b>',
     '(b) 300 + 40m = 100 + 60m, so 200 = 20m <b>[1]</b>, giving <b>m = 10 months</b> <b>[1]</b>',
     '(c) At 15 months A costs 900 and B costs 1000, so <b>Gym A is cheaper by 100 rupees</b> <b>[1]</b>'],
    'note':'The equation in (b) locates the crossover: below 10 months B&rsquo;s smaller joining fee wins, above 10 months A&rsquo;s cheaper rate wins. Students who answer (c) by guessing rather than substituting often pick the wrong side of the crossover.'},
   {'n':'6', 'marks':5, 'lines':['(a) Angles on a straight line add to 180&deg;, so (2x + 10) + (3x &minus; 5) + (x + 25) = 180, '
     'that is <b>6x + 30 = 180</b> <b>[1]</b>',
     '(b) 6x = 150 <b>[1]</b>, so <b>x = 25</b> <b>[1]</b>',
     '(c) The angles are <b>60&deg;, 70&deg; and 50&deg;</b> <b>[1]</b>; 60 + 70 + 50 = 180 ✓ <b>[1]</b>'],
    'note':'The angle fact is required in (a) and is a mark in itself. In (c) the final check is not optional — it is the only thing that distinguishes a correct answer from a plausible one, and it catches an arithmetic slip in the substitution.'},
   {'n':'7', 'marks':5, 'lines':['(a) n + (n + 1) + (n + 2) = 72, that is <b>3n + 3 = 72</b> <b>[1]</b>',
     '(b) 3n = 69, n = 23 <b>[1]</b>, so the numbers are <b>23, 24 and 25</b> <b>[1]</b>',
     '(c) The sum is always 3n + 3 = 3(n + 1) <b>[1]</b>, which is 3 times a whole number and therefore always '
     'a multiple of 3. 70 is not a multiple of 3, so it is impossible <b>[1]</b>'],
    'note':'In (c), &ldquo;I tried some numbers and none worked&rdquo; earns nothing — the argument must cover every case. The factorised form 3(n + 1) is what makes the claim provable rather than merely likely.'},
  ]},

 {'title':'Paper D — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':4, 'lines':['(a) 6x &minus; 12 = 4x + 4 <b>[1]</b>, so 2x = 16 and <b>x = 8</b> <b>[1]</b>',
     '(b) 6x + 15 &minus; 4x + 4 = 27, so 2x + 19 = 27 <b>[1]</b>, giving <b>x = 4</b> <b>[1]</b>'],
    'note':'(b) is the subtracted bracket again: &minus;4 &times; &minus;1 = +4. Check: 3(13) &minus; 4(3) = 39 &minus; 12 = 27 ✓'},
   {'n':'2', 'marks':4, 'lines':['(a) Multiply both sides by 4: 3x &minus; 2 = 16 <b>[1]</b>, so 3x = 18 and <b>x = 6</b> <b>[1]</b>',
     '(b) Multiply every term by 6: 3x + 2x = 60 <b>[1]</b>, so 5x = 60 and <b>x = 12</b> <b>[1]</b>'],
    'note':'(b) is the one worth teaching from. Multiplying by 6 — the lowest common denominator of 2 and 3 — clears both fractions at once, and it must hit the 10 as well. Check: 6 + 4 = 10 ✓'},
   {'n':'3', 'marks':4, 'lines':['(a) 2((3x &minus; 1) + (x + 2)) = 42, so 2(4x + 1) = 42, that is <b>8x + 2 = 42</b> <b>[2]</b>',
     '(b) 8x = 40, so x = 5. Length <b>14 cm</b>, width <b>7 cm</b> <b>[1]</b>; check 2(14 + 7) = 42 ✓ <b>[1]</b>'],
    'note':'Simplify inside the bracket before doubling — students who double each side separately and then add usually lose a term. The check in (b) is worth a mark and catches a wrong x immediately.'},
   {'n':'4', 'marks':4, 'lines':['(a) Plumber A: <b>250 + 180h</b>. Plumber B: <b>230h</b> <b>[1]</b>',
     '(b) 250 + 180h = 230h, so 250 = 50h <b>[1]</b>, giving <b>h = 5 hours</b> <b>[1]</b>',
     '(c) At 3 hours A charges 790 and B charges 690, so <b>Plumber B is cheaper by 100 rupees</b> <b>[1]</b>'],
    'note':'Plumber B has no fixed term at all, which students often mishandle by inventing one. Below 5 hours B wins; above 5 hours A&rsquo;s lower hourly rate overtakes the call-out fee.'},
   {'n':'5', 'marks':4, 'lines':['(a) n + (n+1) + (n+2) + (n+3) = 90, so 4n + 6 = 90, giving n = 21 <b>[1]</b>; '
     'the numbers are <b>21, 22, 23 and 24</b> <b>[1]</b>',
     '(b) The sum is always 4n + 6 = <b>2(2n + 3)</b> <b>[1]</b>, which is 2 times a whole number and therefore '
     'always even <b>[1]</b>'],
    'note':'Note what (b) does <i>not</i> claim: the sum is even but not necessarily a multiple of 4, since 2n + 3 is always odd. A student who claims divisibility by 4 has over-read their own factorisation.'},
   {'n':'6', 'marks':5, 'lines':[
     'Student T moved the 2x across <b>without changing its sign</b>, adding 2x instead of subtracting it <b>[1]</b>. '
     'Subtracting 2x from both sides gives 3x &minus; 3 = 12, not 7x = 15 <b>[1]</b>',
     'Student U moved the &minus;3 across <b>without changing its sign</b>, computing 12 &minus; 3 = 9 instead of 12 + 3 = 15 <b>[1]</b>. '
     'Adding 3 to both sides gives 3x = 15 <b>[1]</b>',
     'Correct: 3x = 15, so <b>x = 5</b> <b>[1]</b>'],
    'note':'Both students made the <i>same</i> error — moving a term across without flipping its sign — one on an x term and one on a constant. Naming it once covers both, and it is the error that &ldquo;doing it to both sides&rdquo; is designed to make impossible.'},
   {'n':'7', 'marks':5, 'lines':[
     '(i) The mistake: dividing by 3 must divide <b>every</b> term, so the 6 becomes 2, not 6 <b>[1]</b>. '
     'Correctly: x + 2 = 6, so <b>x = 4</b> (or subtract 6 first: 3x = 12) <b>[1]</b>',
     '(ii) The mistake: the 4 multiplies <b>both</b> terms in the bracket, so the 3 becomes 12, not 3 <b>[1]</b>. '
     'Correctly: 4x + 12 = 20, so 4x = 8 and <b>x = 2</b> <b>[1]</b>',
     'The check: substitute the answer back into the <b>original</b> equation. 3(0) + 6 = 6, not 18; and 4(4.25 + 3) = 29, not 20 <b>[1]</b>'],
    'note':'The final mark is the transferable one, and it is worth labouring: both students would have caught themselves in ten seconds. Note also that both errors are the same shape — a number applied to one term instead of all of them.'},
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
    p = os.path.join(OUT, 'maths-equations-paper-%s.pdf' % code)
    build_paper(spec, p)
    files.append(p)

for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)

p = os.path.join(OUT, 'maths-equations-answers.pdf')
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
