#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)

EYEBROW = 'Base Camp · IGCSE Mathematics · Grade 7 · Number'
TOPIC   = 'Ratio and Proportion'

INSTR_MED = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Anything you cannot do in your head, do on paper.',
    'To share a total: <b>add the parts, divide the total by that sum, then multiply back up.</b>',
    'For proportion questions, <b>find one first, then scale.</b>',
    'Give every ratio in its simplest form, and convert to a common unit before simplifying.',
    'The mark for each question is shown in square brackets on the right.',
]
INSTR_HARD = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Anything you cannot do in your head, do on paper.',
    'Give every ratio in its simplest form, and convert to a common unit before simplifying.',
    'The mark for each question is shown in square brackets on the right.',
    'Several questions do not give you the total. Work out what <b>one part</b> is worth first — everything else follows from it.',
    'Two questions on this paper have no obvious first step. If one stops you, leave it and come back — do not spend more than five minutes stuck.',
]

# ----------------------------------------------------------------- PAPER A
A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — writing and simplifying ratios',
   'text':'Complete the table. Each empty box is worth one mark.', 'marks':6,
   'grid':[['Ratio','Simplest form','First share as a fraction of the total'],
           ['18 : 24','',''],
           ['20 : 50','',''],
           ['45 : 27','','']],
   'grid_widths':[AVAIL*0.24, AVAIL*0.28, AVAIL*0.48],
   'tip':'The last column is where the marks are lost. Add both numbers of the ratio to get the total number of parts first.'},

  {'text':'Write each ratio in its simplest form.', 'marks':2,
   'parts':[{'label':'(a)','text':'24 : 36','marks':1,'space':16},
            {'label':'(b)','text':'5 : 15 : 20','marks':1,'space':16}]},

  {'text':'Write each of these as a ratio in its simplest form. Convert the units first.', 'marks':2,
   'parts':[{'label':'(a)','text':'30 cm : 1 m','marks':1,'space':18},
            {'label':'(b)','text':'45 minutes : 2 hours','marks':1,'space':18}]},

  {'section':'Section 2 — sharing a quantity',
   'text':'Share 350 in the ratio 2 : 5.', 'marks':2, 'space':28},

  {'text':'Share 720 in the ratio 4 : 5.', 'marks':2, 'space':28},

  {'text':'Share &#8377;960 among three people in the ratio 1 : 2 : 5.', 'marks':3, 'space':34,
   'tip':'Check your three answers add back up to 960 before you move on.'},

  {'text':'In a class the ratio of boys to girls is 3 : 4. There are 28 students in the class.', 'marks':2,
   'parts':[{'label':'(a)','text':'How many boys are there?','marks':1,'space':18},
            {'label':'(b)','text':'How many girls are there?','marks':1,'space':18}]},

  {'section':'Section 3 — word problems',
   'text':'A recipe for 4 people uses 300 g of rice. How much rice is needed for 10 people?',
   'marks':2, 'space':30},

  {'text':'5 pens cost &#8377;60. Find the cost of 8 pens.', 'marks':2, 'space':30},

  {'text':'Concrete is made by mixing cement and sand in the ratio 1 : 4. '
          'A builder uses 60 kg of cement.', 'marks':2,
   'parts':[{'label':'(a)','text':'What mass of sand does he use?','marks':1,'space':18},
            {'label':'(b)','text':'What is the total mass of the concrete he makes?','marks':1,'space':18}]},

  {'text':'The ratio of red to blue counters in a bag is 2 : 3. There are 18 red counters.', 'marks':2,
   'parts':[{'label':'(a)','text':'How many blue counters are there?','marks':1,'space':18},
            {'label':'(b)','text':'How many counters are there altogether?','marks':1,'space':18}]},

  {'text':'Two shops sell the same rice.<br/>'
          '<b>Shop A:</b> 2 kg for &#8377;150. &nbsp; <b>Shop B:</b> 5 kg for &#8377;365.<br/>'
          'Work out the price per kilogram at each shop, and state which is better value.',
   'marks':3, 'space':38,
   'tip':'Two correct prices and no sentence saying which shop wins scores 2 out of 3.'},
 ]}

# ----------------------------------------------------------------- PAPER B
B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — units, the 1 : n form and scale',
   'text':'Write each ratio in its simplest form.', 'marks':3,
   'parts':[{'label':'(a)','text':'250 g : 1 kg','marks':1,'space':16},
            {'label':'(b)','text':'40 cm : 1.5 m','marks':1,'space':16},
            {'label':'(c)','text':'20 minutes : 1 hour','marks':1,'space':16}]},

  {'text':'Write each ratio in the form 1 : n. The value of n may be a decimal.', 'marks':2,
   'parts':[{'label':'(a)','text':'4 : 10','marks':1,'space':16},
            {'label':'(b)','text':'5 : 12','marks':1,'space':16}]},

  {'text':'A map is drawn to a scale of 1 : 50 000.', 'marks':3,
   'parts':[{'label':'(a)','text':'Two towns are 6 cm apart on the map. Find the real distance '
                                  'between them, in kilometres.','marks':2,'space':30},
            {'label':'(b)','text':'A straight road is 8 km long. How long is it on the map, in centimetres?',
             'marks':1,'space':22}],
   'tip':'The multiplication is the easy mark. Converting centimetres to kilometres is the one that goes missing.'},

  {'section':'Section 2 — direct proportion',
   'text':'7 identical books have a total mass of 2.1 kg. Find the mass of 12 of these books.',
   'marks':2, 'space':30},

  {'text':'A car uses 6 litres of fuel to travel 90 km. How far can it travel on 15 litres?',
   'marks':2, 'space':30},

  {'text':'One pound sterling is worth &#8377;105.', 'marks':2,
   'parts':[{'label':'(a)','text':'Convert &#8377;840 into pounds.','marks':1,'space':18},
            {'label':'(b)','text':'Convert &pound;15 into rupees.','marks':1,'space':18}]},

  {'text':'Washing powder is sold in two sizes.<br/>'
          '<b>Pack A:</b> 900 g for &#8377;135. &nbsp; <b>Pack B:</b> 1.2 kg for &#8377;174.<br/>'
          'Work out the price per 100 g of each pack, and state which is better value.',
   'marks':3, 'space':38},

  {'section':'Section 3 — word problems',
   'text':'Share 4500 in the ratio 2 : 3 : 4.', 'marks':3, 'space':32},

  {'text':'A fruit drink is made by mixing orange juice and water in the ratio 2 : 7. '
          'A jug holds 1800 ml of the drink. How much orange juice does it contain?',
   'marks':2, 'space':30},

  {'text':'In a car park the ratio of cars to motorbikes is 5 : 2. There are 24 more cars than '
          'motorbikes. How many motorbikes are in the car park?', 'marks':3, 'space':36,
   'tip':'You have not been given the total. Work out how many parts the 24 represents.'},

  {'text':'A recipe for 8 biscuits uses 120 g of butter and 180 g of flour.', 'marks':3,
   'parts':[{'label':'(a)','text':'How much butter is needed for 20 biscuits?','marks':2,'space':28},
            {'label':'(b)','text':'Amit has 270 g of flour and plenty of butter. '
                                  'How many biscuits can he make?','marks':1,'space':22}]},

  {'text':'The ratio of Meera&rsquo;s age to Nikhil&rsquo;s age is 4 : 7. Nikhil is 21 years old. '
          'How old is Meera?', 'marks':2, 'space':28},
 ]}

# ----------------------------------------------------------------- PAPER C
C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — when the total is not given',
   'text':'Red and blue beads are threaded in the ratio 3 : 8. There are 96 blue beads.', 'marks':3,
   'parts':[{'label':'(a)','text':'How many red beads are there?','marks':2,'space':28},
            {'label':'(b)','text':'How many beads are there altogether?','marks':1,'space':20}]},

  {'text':'Two numbers are in the ratio 5 : 9. The difference between them is 36. '
          'Find both numbers.', 'marks':3, 'space':34,
   'tip':'The difference is measured in parts too. How many parts is it?'},

  {'text':'An amount of money is shared in the ratio 3 : 5 : 7. The largest share is &#8377;840. '
          'Find the total amount that was shared.', 'marks':3, 'space':34},

  {'section':'Section 2 — combining two ratios',
   'text':'For three quantities A, B and C you are told that A : B = 2 : 3 and B : C = 4 : 5.', 'marks':4,
   'parts':[{'label':'(a)','text':'Write the ratio A : B : C in its simplest form.','marks':2,'space':30},
            {'label':'(b)','text':'105 marbles are shared in the ratio A : B : C. Find each share.',
             'marks':2,'space':28}],
   'tip':'B is 3 parts in one ratio and 4 in the other. Scale both until the two figures for B agree.'},

  {'text':'In a school the ratio of teachers to students is 1 : 18, and the ratio of students to '
          'computers is 3 : 1. Find the ratio of teachers to computers, in its simplest form.',
   'marks':3, 'space':36},

  {'section':'Section 3 — multi-step',
   'text':'6 workers can build a wall in 10 days. All the workers work at the same rate.', 'marks':3,
   'parts':[{'label':'(a)','text':'How long would 4 workers take to build the same wall?','marks':2,'space':30},
            {'label':'(b)','text':'How many workers would be needed to build it in 5 days?','marks':1,'space':22}],
   'tip':'Check the direction of your answer to (a) before you write it down. Fewer workers cannot be faster.'},

  {'text':'A sum of money is shared between Anil and Bina in the ratio 5 : 3. Anil then gives '
          '&#8377;120 of his share to Bina, and they now have equal amounts. '
          'How much money was shared altogether?', 'marks':4, 'space':46},

  {'text':'4 pipes fill a tank in 9 hours. All the pipes deliver water at the same rate.', 'marks':3,
   'parts':[{'label':'(a)','text':'How long would 6 pipes take to fill the tank?','marks':2,'space':28},
            {'label':'(b)','text':'A student writes &ldquo;6 pipes, so 9 &times; 6 &divide; 4 = 13.5 hours.&rdquo; '
                                  'Explain the mistake in one sentence.','marks':1,'space':22}]},

  {'text':'Rice and lentils are mixed in the ratio 5 : 2 by mass. A shop makes 21 kg of the mixture. '
          'Rice costs &#8377;60 per kg and lentils cost &#8377;95 per kg. '
          'Find the total cost of the ingredients in the 21 kg of mixture.', 'marks':4, 'space':46},
 ]}

# ----------------------------------------------------------------- PAPER D
D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — ratios that change',
   'text':'The ratio of boys to girls in a club is 7 : 5. Six more girls join the club, and the '
          'ratio becomes 7 : 6. How many boys are in the club?', 'marks':4, 'space':48,
   'tip':'Call one part k. The number of boys never changes, so write both ratios using the same k.'},

  {'text':'Two numbers are in the ratio 3 : 5. When 4 is added to each of them, the ratio becomes '
          '2 : 3. Find the two numbers.', 'marks':4, 'space':48},

  {'section':'Section 2 — inverse proportion',
   'text':'12 machines can complete an order in 15 days. All the machines work at the same rate.', 'marks':4,
   'parts':[{'label':'(a)','text':'How long would 9 machines take to complete the same order?','marks':2,'space':28},
            {'label':'(b)','text':'The order must be finished in 10 days. How many machines are needed?',
             'marks':1,'space':22},
            {'label':'(c)','text':'Explain in one sentence why your answers move in the opposite '
                                  'direction to the number of machines.','marks':1,'space':22}]},

  {'text':'A car travelling at 60 km/h completes a journey in 5 hours.', 'marks':3,
   'parts':[{'label':'(a)','text':'How long would the same journey take at 75 km/h?','marks':2,'space':28},
            {'label':'(b)','text':'What speed would be needed to complete it in 3 hours?','marks':1,'space':22}]},

  {'section':'Section 3 — comparisons and corrections',
   'text':'Three friends share the profit from a stall in the ratio of the hours they each worked. '
          'Asha worked 6 hours, Bhavna worked 9 hours and Chetan worked 12 hours. '
          'The profit was &#8377;4500.', 'marks':4,
   'parts':[{'label':'(a)','text':'Work out how much each friend receives.','marks':3,'space':36},
            {'label':'(b)','text':'Chetan says he should get half the profit because he worked the '
                                  'longest. Show by calculation that he is wrong.','marks':1,'space':24}]},

  {'text':'Two shops sell the same juice.<br/>'
          '<b>Shop A:</b> 1.5 litres for &#8377;99. &nbsp; <b>Shop B:</b> 2 litres for &#8377;126.', 'marks':4,
   'parts':[{'label':'(a)','text':'Work out the price per litre at each shop, and state which is better value.',
             'marks':2,'space':30},
            {'label':'(b)','text':'Shop A then offers &ldquo;buy 2, get the third free&rdquo;. '
                                  'Find Shop A&rsquo;s new price per litre under this offer, and state '
                                  'which shop is now better value.','marks':2,'space':32}]},

  {'text':'A recipe for 12 pancakes uses 200 g of flour, 300 ml of milk and 2 eggs. '
          'Ravi has 500 g of flour, 700 ml of milk and 6 eggs. '
          'What is the greatest number of pancakes he can make, and which ingredient runs out first?',
   'marks':3, 'space':44,
   'tip':'Work out how many pancakes each ingredient on its own would allow, then take the smallest.'},

  {'text':'A student has written two answers in her book, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;The ratio of red to blue is 3 : 5, so 3/5 of the counters are red.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;A : B = 2 : 3 and B : C = 4 : 5, so A : B : C = 2 : 3 : 5.&rdquo;<br/>'
          'For each one, explain the mistake and give the correct answer.', 'marks':4, 'space':48},
 ]}

# ----------------------------------------------------------------- mark schemes
SCHEMES = [
 {'title':'Paper A — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     'Row 1 &nbsp;18 : 24 &rarr; <b>3 : 4</b> &nbsp;and&nbsp; <b>3/7</b>',
     'Row 2 &nbsp;20 : 50 &rarr; <b>2 : 5</b> &nbsp;and&nbsp; <b>2/7</b>',
     'Row 3 &nbsp;45 : 27 &rarr; <b>5 : 3</b> &nbsp;and&nbsp; <b>5/8</b>'],
    'note':'One mark per correct box. In the last column, 3/4, 2/5 and 5/3 are the ratio copied out again rather '
           'than a fraction of the total — this is the single most common error in the topic. Award nothing for those. '
           'The denominator must be the sum of both parts.'},
   {'n':'2', 'marks':2, 'lines':['(a) Both divide by 12: <b>2 : 3</b>', '(b) All divide by 5: <b>1 : 3 : 4</b>']},
   {'n':'3', 'marks':2, 'lines':['(a) 30 cm : 100 cm = <b>3 : 10</b>', '(b) 45 min : 120 min = <b>3 : 8</b>'],
    'note':'Answers of 30 : 1 and 45 : 2 score zero — the units were not converted first. This is worth pointing out '
           'every time it appears, because the student who does it once does it every time.'},
   {'n':'4', 'marks':2, 'lines':['2 + 5 = 7 parts, one part = 350 &divide; 7 = 50 <b>[1]</b>',
                                 '<b>100 and 250</b> <b>[1]</b>']},
   {'n':'5', 'marks':2, 'lines':['4 + 5 = 9 parts, one part = 720 &divide; 9 = 80 <b>[1]</b>',
                                 '<b>320 and 400</b> <b>[1]</b>']},
   {'n':'6', 'marks':3, 'lines':['1 + 2 + 5 = 8 parts <b>[1]</b>', 'One part = 960 &divide; 8 = 120 <b>[1]</b>',
                                 '<b>&#8377;120, &#8377;240 and &#8377;600</b> <b>[1]</b>'],
    'note':'Dividing 960 by 3 because there are three people gives 320 each and scores nothing. The tell is that the '
           'three shares come out equal from an unequal ratio.'},
   {'n':'7', 'marks':2, 'lines':['7 parts, one part = 28 &divide; 7 = 4', '(a) <b>12 boys</b> &nbsp; (b) <b>16 girls</b>'],
    'note':'Answers reversed (16 boys, 12 girls) score zero for both. The order in the question is boys to girls.'},
   {'n':'8', 'marks':2, 'lines':['300 &divide; 4 = 75 g per person <b>[1]</b>', '75 &times; 10 = <b>750 g</b> <b>[1]</b>']},
   {'n':'9', 'marks':2, 'lines':['60 &divide; 5 = &#8377;12 per pen <b>[1]</b>', '12 &times; 8 = <b>&#8377;96</b> <b>[1]</b>']},
   {'n':'10', 'marks':2, 'lines':['(a) 60 &times; 4 = <b>240 kg of sand</b>', '(b) 60 + 240 = <b>300 kg</b>'],
    'note':'In (b), answering 240 means the student gave the sand again rather than the total. Award (a) only.'},
   {'n':'11', 'marks':2, 'lines':['One part = 18 &divide; 2 = 9', '(a) 3 &times; 9 = <b>27 blue</b> &nbsp; (b) <b>45 altogether</b>'],
    'note':'The 18 is two parts, not one and not the total. Students who treat it as the total get 2 : 3 of 18 and lose both marks.'},
   {'n':'12', 'marks':3, 'lines':['Shop A: 150 &divide; 2 = <b>&#8377;75 per kg</b> <b>[1]</b>',
                                  'Shop B: 365 &divide; 5 = <b>&#8377;73 per kg</b> <b>[1]</b>',
                                  '<b>Shop B is better value</b> <b>[1]</b>'],
    'note':'The third mark is the conclusion in words. Two correct unit prices and no statement scores 2 — this is the '
           'easiest mark on the paper to leave behind, and it is left behind constantly.'},
  ]},

 {'title':'Paper B — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':3, 'lines':['(a) 250 g : 1000 g = <b>1 : 4</b>', '(b) 40 cm : 150 cm = <b>4 : 15</b>',
                                 '(c) 20 min : 60 min = <b>1 : 3</b>'],
    'note':'Each mark requires the conversion. 250 : 1, 40 : 1.5 and 20 : 1 all score zero.'},
   {'n':'2', 'marks':2, 'lines':['(a) Divide both by 4: <b>1 : 2.5</b>', '(b) Divide both by 5: <b>1 : 2.4</b>'],
    'note':'A decimal on the right is correct and expected here. Students who insist on whole numbers often give '
           '2 : 5 for (a), which is a valid equivalent ratio but is not in the form 1 : n that was asked for.'},
   {'n':'3', 'marks':3, 'lines':['(a) 6 &times; 50 000 = 300 000 cm <b>[1]</b>',
                                 '&nbsp; &nbsp; &nbsp;300 000 cm = 3000 m = <b>3 km</b> <b>[1]</b>',
                                 '(b) 8 km = 800 000 cm, and 800 000 &divide; 50 000 = <b>16 cm</b> <b>[1]</b>'],
    'note':'In (a) the multiplication is routinely correct and the conversion routinely is not. 300 000 left in '
           'centimetres, or divided only once to give 3000, scores the first mark only.'},
   {'n':'4', 'marks':2, 'lines':['2.1 &divide; 7 = 0.3 kg per book <b>[1]</b>', '0.3 &times; 12 = <b>3.6 kg</b> <b>[1]</b>']},
   {'n':'5', 'marks':2, 'lines':['90 &divide; 6 = 15 km per litre <b>[1]</b>', '15 &times; 15 = <b>225 km</b> <b>[1]</b>']},
   {'n':'6', 'marks':2, 'lines':['(a) 840 &divide; 105 = <b>&pound;8</b>', '(b) 15 &times; 105 = <b>&#8377;1575</b>'],
    'note':'Multiplying in (a) or dividing in (b) means the direction was not thought about. A quick sense-check: '
           'rupees are the smaller unit, so a rupee figure is always the bigger number.'},
   {'n':'7', 'marks':3, 'lines':['Pack A: 135 &divide; 900 &times; 100 = <b>&#8377;15.00 per 100 g</b> <b>[1]</b>',
                                 'Pack B: 1.2 kg = 1200 g, 174 &divide; 1200 &times; 100 = <b>&#8377;14.50 per 100 g</b> <b>[1]</b>',
                                 '<b>Pack B is better value</b> <b>[1]</b>'],
    'note':'Pack B costs more in total and is still the better buy — that is the whole design of the question. '
           'A student who answers &ldquo;A, because it is cheaper&rdquo; has compared the two prices instead of the two rates.'},
   {'n':'8', 'marks':3, 'lines':['2 + 3 + 4 = 9 parts <b>[1]</b>', 'One part = 4500 &divide; 9 = 500 <b>[1]</b>',
                                 '<b>1000, 1500 and 2000</b> <b>[1]</b>']},
   {'n':'9', 'marks':2, 'lines':['9 parts, one part = 1800 &divide; 9 = 200 <b>[1]</b>',
                                 'Juice = 2 &times; 200 = <b>400 ml</b> <b>[1]</b>'],
    'note':'1400 is the water. Award the first mark only — the question named the juice.'},
   {'n':'10', 'marks':3, 'lines':['The difference is 5 &minus; 2 = 3 parts <b>[1]</b>',
                                  'One part = 24 &divide; 3 = 8 <b>[1]</b>',
                                  'Motorbikes = 2 &times; 8 = <b>16</b> <b>[1]</b>'],
    'note':'Treating 24 as the total gives 7 parts and nothing works out whole. The key realisation is that a '
           'difference is measured in parts just as a total is.'},
   {'n':'11', 'marks':3, 'lines':['(a) 120 &divide; 8 = 15 g per biscuit <b>[1]</b>, so 15 &times; 20 = <b>300 g</b> <b>[1]</b>',
                                  '(b) 180 &divide; 8 = 22.5 g of flour each, and 270 &divide; 22.5 = <b>12 biscuits</b> <b>[1]</b>'],
    'note':'Part (b) runs the unitary method backwards, which is the harder direction. A student who can do (a) but '
           'not (b) has learned a procedure rather than the idea.'},
   {'n':'12', 'marks':2, 'lines':['One part = 21 &divide; 7 = 3 <b>[1]</b>', 'Meera = 4 &times; 3 = <b>12 years old</b> <b>[1]</b>'],
    'note':'Answering 36 means the student added 4 parts to Nikhil rather than reading 21 as seven parts.'},
  ]},

 {'title':'Paper C — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':3, 'lines':['The 96 blue beads are 8 parts, so one part = 96 &divide; 8 = 12 <b>[1]</b>',
                                 '(a) Red = 3 &times; 12 = <b>36</b> <b>[1]</b>',
                                 '(b) Total = 11 &times; 12 = <b>132</b> <b>[1]</b>'],
    'note':'Dividing 96 by 11, or treating 96 as the total, are the two failure modes. Ask: how many parts is the '
           'number I have been given?'},
   {'n':'2', 'marks':3, 'lines':['The difference is 9 &minus; 5 = 4 parts <b>[1]</b>',
                                 'One part = 36 &divide; 4 = 9 <b>[1]</b>',
                                 '<b>45 and 81</b> <b>[1]</b>'],
    'note':'Check: 81 &minus; 45 = 36. Dividing 36 by 14 (the sum) is the standard wrong move — that would be right '
           'only if 36 were the total.'},
   {'n':'3', 'marks':3, 'lines':['The largest share is 7 parts, so one part = 840 &divide; 7 = 120 <b>[1]</b>',
                                 'Total = 15 parts <b>[1]</b>',
                                 '15 &times; 120 = <b>&#8377;1800</b> <b>[1]</b>']},
   {'n':'4', 'marks':4, 'lines':[
     '(a) Make B match at 12: A : B = 2 : 3 becomes 8 : 12 (&times;4), and B : C = 4 : 5 becomes 12 : 15 (&times;3) <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;So A : B : C = <b>8 : 12 : 15</b> <b>[1]</b>',
     '(b) 8 + 12 + 15 = 35 parts, one part = 105 &divide; 35 = 3 <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;<b>24, 36 and 45</b> <b>[1]</b>'],
    'note':'Answering 2 : 3 : 5 in (a) scores zero and usually costs (b) as well. It is worth showing the student that '
           '2 : 3 : 5 on 105 gives 21, 31.5 and 52.5 — half a marble twice over, so the method refutes itself.'},
   {'n':'5', 'marks':3, 'lines':['Students appear as 18 in one ratio and 3 in the other; scale S : C by 6 <b>[1]</b>',
                                 'S : C = 3 : 1 becomes 18 : 6, so T : S : C = 1 : 18 : 6 <b>[1]</b>',
                                 'T : C = <b>1 : 6</b> <b>[1]</b>'],
    'note':'The same joining move as question 4, but the shared quantity sits in the middle of one ratio and the '
           'start of the other. Award full marks for any correct scaling route.'},
   {'n':'6', 'marks':3, 'lines':['The job is 6 &times; 10 = 60 worker-days <b>[1]</b>',
                                 '(a) 60 &divide; 4 = <b>15 days</b> <b>[1]</b>',
                                 '(b) 60 &divide; 5 = <b>12 workers</b> <b>[1]</b>'],
    'note':'The direct-proportion answer to (a) is 4/6 &times; 10 = 6.67 days, and it should be rejected on sight: '
           'fewer workers cannot finish sooner. Award nothing for it, but do point at the direction rather than the arithmetic.'},
   {'n':'7', 'marks':4, 'lines':['Let one part be k, so Anil has 5k and Bina has 3k <b>[1]</b>',
                                 'After the transfer: 5k &minus; 120 = 3k + 120 <b>[1]</b>',
                                 '2k = 240, so k = 120 <b>[1]</b>',
                                 'Total = 8k = <b>&#8377;960</b> <b>[1]</b>'],
    'note':'Check: Anil 600, Bina 360, and after the transfer both hold 480. A common wrong route is to treat the '
           '&#8377;120 as one part, which gives 960 by accident on this question — ask to see the equation before '
           'awarding full marks.'},
   {'n':'8', 'marks':3, 'lines':['The job is 4 &times; 9 = 36 pipe-hours <b>[1]</b>',
                                 '(a) 36 &divide; 6 = <b>6 hours</b> <b>[1]</b>',
                                 '(b) More pipes must mean less time, but the student&rsquo;s method makes the time '
                                 '<b>longer</b> — he has used direct proportion where the quantities are inversely '
                                 'proportional <b>[1]</b>'],
    'note':'Accept any answer in (b) that identifies the direction as wrong. Naming it &ldquo;inverse proportion&rdquo; '
           'is not required, but describing the multiplication as constant is a sign the idea has landed.'},
   {'n':'9', 'marks':4, 'lines':['5 + 2 = 7 parts, one part = 21 &divide; 7 = 3 kg <b>[1]</b>',
                                 'Rice 15 kg and lentils 6 kg <b>[1]</b>',
                                 '15 &times; 60 = 900 and 6 &times; 95 = 570 <b>[1]</b>',
                                 'Total = <b>&#8377;1470</b> <b>[1]</b>'],
    'note':'Two ideas stacked: share in a ratio, then cost each part separately. Averaging the two prices to '
           '&#8377;77.50 per kg and multiplying by 21 gives &#8377;1627.50 and scores nothing — the two quantities '
           'are not equal, so their prices cannot be averaged.'},
  ]},

 {'title':'Paper D — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':4, 'lines':['Let one part be k: boys = 7k, girls = 5k <b>[1]</b>',
                                 'After six more girls: 7k : (5k + 6) = 7 : 6, so 6 &times; 7k = 7(5k + 6) <b>[1]</b>',
                                 '42k = 35k + 42, so 7k = 42 and k = 6 <b>[1]</b>',
                                 'Boys = 7 &times; 6 = <b>42</b> <b>[1]</b>'],
    'note':'Check: girls go from 30 to 36, and 42 : 36 = 7 : 6. The number of boys is unchanged throughout, which is '
           'why the same k can be used in both ratios — that is the whole idea of the question.'},
   {'n':'2', 'marks':4, 'lines':['Let the numbers be 3k and 5k <b>[1]</b>',
                                 '(3k + 4) : (5k + 4) = 2 : 3, so 3(3k + 4) = 2(5k + 4) <b>[1]</b>',
                                 '9k + 12 = 10k + 8, so k = 4 <b>[1]</b>',
                                 'The numbers are <b>12 and 20</b> <b>[1]</b>'],
    'note':'Check: 16 : 24 = 2 : 3. Adding 4 to each side of the ratio itself, giving 7 : 9, is the trap — you add to '
           'the numbers, never to the parts.'},
   {'n':'3', 'marks':4, 'lines':['The order is 12 &times; 15 = 180 machine-days <b>[1]</b>',
                                 '(a) 180 &divide; 9 = <b>20 days</b> <b>[1]</b>',
                                 '(b) 180 &divide; 10 = <b>18 machines</b> <b>[1]</b>',
                                 '(c) The total work is fixed, so the machines and the days multiply to a constant — '
                                 'increasing one must decrease the other <b>[1]</b>'],
    'note':'For (c), accept any answer identifying the product as constant. &ldquo;Because it is inverse proportion&rdquo; '
           'on its own is naming rather than explaining; push for the sentence about the fixed amount of work.'},
   {'n':'4', 'marks':3, 'lines':['Distance = 60 &times; 5 = 300 km <b>[1]</b>',
                                 '(a) 300 &divide; 75 = <b>4 hours</b> <b>[1]</b>',
                                 '(b) 300 &divide; 3 = <b>100 km/h</b> <b>[1]</b>'],
    'note':'The constant here has a physical name the student already knows — the distance. Pointing that out links '
           'this straight back to the speed topic.'},
   {'n':'5', 'marks':4, 'lines':['(a) 6 : 9 : 12 simplifies to 2 : 3 : 4 <b>[1]</b>',
                                 '&nbsp; &nbsp; &nbsp;9 parts, one part = 4500 &divide; 9 = 500 <b>[1]</b>',
                                 '&nbsp; &nbsp; &nbsp;Asha <b>&#8377;1000</b>, Bhavna <b>&#8377;1500</b>, Chetan <b>&#8377;2000</b> <b>[1]</b>',
                                 '(b) Chetan is entitled to 4/9 of the profit, not 1/2. Half would be &#8377;2250, '
                                 'so he is claiming <b>&#8377;250 too much</b> <b>[1]</b>'],
    'note':'Working directly with 6 : 9 : 12 without simplifying is perfectly valid and reaches the same shares — do '
           'not penalise it. In (b), 4/9 &lt; 1/2 is enough on its own; the money comparison is the fuller answer.'},
   {'n':'6', 'marks':4, 'lines':['(a) Shop A: 99 &divide; 1.5 = <b>&#8377;66 per litre</b> <b>[1]</b>',
                                 '&nbsp; &nbsp; &nbsp;Shop B: 126 &divide; 2 = &#8377;63 per litre, so <b>Shop B is better value</b> <b>[1]</b>',
                                 '(b) Three bottles cost 2 &times; 99 = &#8377;198 and give 4.5 litres <b>[1]</b>',
                                 '&nbsp; &nbsp; &nbsp;198 &divide; 4.5 = &#8377;44 per litre, so <b>Shop A is now better value</b> <b>[1]</b>'],
    'note':'The offer changes the answer completely, which is the point. The frequent error in (b) is dividing the '
           'price of three bottles by three bottles&rsquo; worth of litres while forgetting that only two were paid for.'},
   {'n':'7', 'marks':3, 'lines':['Flour: 500 &divide; 200 &times; 12 = 30 pancakes <b>[1]</b>',
                                 'Milk: 700 &divide; 300 &times; 12 = 28 pancakes &nbsp;·&nbsp; Eggs: 6 &divide; 2 &times; 12 = 36 pancakes <b>[1]</b>',
                                 'The smallest wins: <b>28 pancakes, limited by the milk</b> <b>[1]</b>'],
    'note':'The third mark needs both the number and the ingredient. Adding or averaging the three figures scores '
           'nothing — you cannot make a pancake out of the ingredient you have run out of.'},
   {'n':'8', 'marks':4, 'lines':[
     '(i) The mistake: reading the colon as a fraction bar. There are 3 + 5 = 8 parts, not 5 <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;The correct fraction is <b>3/8</b> <b>[1]</b>',
     '(ii) The mistake: B is 3 parts in one ratio and 4 in the other, so the two cannot be written side by side <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;Scaling both until B is 12 gives <b>A : B : C = 8 : 12 : 15</b> <b>[1]</b>'],
    'note':'These are the two errors the whole topic is built around, which is why they close the paper. A student who '
           'can diagnose both in someone else&rsquo;s handwriting will not make them in their own — that is the entire '
           'reason this question type exists.'},
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
    p = os.path.join(OUT, 'maths-ratio-paper-%s.pdf' % code)
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

p = os.path.join(OUT, 'maths-ratio-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW,
    'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Where a question is worth more '
             'than one mark, award method marks even when the final answer is wrong. Almost every '
             'note below comes back to one of two errors: reading a : b as the fraction a/b, or '
             'dividing a total by the number of people instead of the number of parts. Watch for '
             'which of the two a given student favours — they rarely make both.',
    'footer': 'Mark schemes · ' + TOPIC,
})
files.append(p)
print('\n'.join(files))
