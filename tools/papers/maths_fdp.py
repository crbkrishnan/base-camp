#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)

EYEBROW = 'Base Camp · IGCSE Mathematics · Grade 7 · Number'
TOPIC   = 'Fractions, Decimals and Percentages'

INSTR_MED = [
    'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
    'No calculator. Anything you cannot do in your head, do on paper.',
    'Give fractions in their simplest form unless the question says otherwise.',
    'The mark for each question is shown in square brackets on the right.',
]
INSTR_HARD = INSTR_MED + [
    'Two questions on this paper have no obvious first step. If one stops you, leave it and come back — do not spend more than five minutes stuck.',
]

# ----------------------------------------------------------------- PAPER A
A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — conversions',
   'text':'Complete the table. Each empty box is worth one mark.', 'marks':6,
   'grid':[['Fraction','Decimal','Percentage'],
           ['3/4','',''],
           ['','0.35',''],
           ['','','60%']],
   'grid_widths':[AVAIL/3.0]*3},

  {'text':'Write each of these as a fraction in its simplest form.', 'marks':2,
   'parts':[{'label':'(a)','text':'0.45','marks':1,'space':16},
            {'label':'(b)','text':'24%','marks':1,'space':16}]},

  {'text':'Change each fraction to a decimal.', 'marks':2,
   'parts':[{'label':'(a)','text':'7/8','marks':1,'space':20},
            {'label':'(b)','text':'5/16','marks':1,'space':20}]},

  {'section':'Section 2 — calculation',
   'text':'Work out, giving each answer in its simplest form.', 'marks':4,
   'parts':[{'label':'(a)','text':'3/5 + 1/4','marks':1,'space':18},
            {'label':'(b)','text':'5/6 &minus; 1/3','marks':1,'space':18},
            {'label':'(c)','text':'2/3 &times; 9/10','marks':1,'space':18},
            {'label':'(d)','text':'3/4 &divide; 2/5','marks':1,'space':18}]},

  {'text':'Work out each of these without a calculator.', 'marks':3,
   'parts':[{'label':'(a)','text':'25% of 480','marks':1,'space':16},
            {'label':'(b)','text':'15% of 60','marks':1,'space':16},
            {'label':'(c)','text':'12.5% of 240','marks':1,'space':16}]},

  {'text':'Put these four numbers in order, smallest first. Write your final answer using the '
          'forms given in the question.<br/><br/>'
          '<font name="Mono" size="10.5">0.7 &nbsp; &nbsp; 3/5 &nbsp; &nbsp; 65% &nbsp; &nbsp; 2/3</font>',
   'marks':2, 'space':28,
   'tip':'Turning everything into decimals first is almost always the fastest route.'},

  {'section':'Section 3 — word problems',
   'text':'A jacket costs 1200 rupees. In a sale, the price is reduced by 20%. '
          'Find the sale price.', 'marks':2, 'space':30},

  {'text':'There are 30 students in a class, and 40% of them wear glasses. '
          'How many students do <b>not</b> wear glasses?', 'marks':2, 'space':30},

  {'text':'A recipe uses 3/4 of a 500 g bag of flour.', 'marks':3,
   'parts':[{'label':'(a)','text':'How many grams of flour are used?','marks':2,'space':26},
            {'label':'(b)','text':'How many grams are left in the bag?','marks':1,'space':18}]},

  {'text':'Ravi scores 18 out of 24 in a test.', 'marks':2,
   'parts':[{'label':'(a)','text':'Write his score as a fraction in its simplest form.','marks':1,'space':18},
            {'label':'(b)','text':'Write his score as a percentage.','marks':1,'space':18}]},

  {'text':'A phone costs 8000 rupees. The price is increased by 5%. Find the new price.',
   'marks':2, 'space':30},
 ]}

# ----------------------------------------------------------------- PAPER B
B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 40 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — mixed numbers and order',
   'text':'Convert each number.', 'marks':2,
   'parts':[{'label':'(a)','text':'Write 2 3/5 as an improper fraction.','marks':1,'space':16},
            {'label':'(b)','text':'Write 17/4 as a mixed number.','marks':1,'space':16}]},

  {'text':'Work out, giving each answer as a mixed number or whole number where possible.', 'marks':4,
   'parts':[{'label':'(a)','text':'1 1/2 + 2 3/4','marks':1,'space':22},
            {'label':'(b)','text':'3 1/3 &minus; 1 5/6','marks':1,'space':22},
            {'label':'(c)','text':'1 1/4 &times; 2 2/5','marks':2,'space':26}]},

  {'text':'Put these four numbers in order, smallest first.<br/><br/>'
          '<font name="Mono" size="10.5">0.46 &nbsp; &nbsp; 4/9 &nbsp; &nbsp; 43% &nbsp; &nbsp; 9/20</font>',
   'marks':2, 'space':28},

  {'section':'Section 2 — percentage change',
   'text':'Increase 250 by 12%.', 'marks':2, 'space':26},

  {'text':'Decrease 640 by 15%.', 'marks':2, 'space':26},

  {'text':'A shirt cost 800 rupees. It is now sold for 680 rupees. '
          'Calculate the percentage decrease in price.', 'marks':3, 'space':32},

  {'text':'The population of a town rises from 4000 to 4600. '
          'Calculate the percentage increase.', 'marks':3, 'space':32},

  {'section':'Section 3 — word problems',
   'text':'Work out 3/8 of 320.', 'marks':2, 'space':24},

  {'text':'Which is larger: 5/8 of 400, or 60% of 420? You must show your working '
          'and state which one is larger.', 'marks':3, 'space':36},

  {'text':'A car park has 250 spaces and is 68% full. How many spaces are empty?',
   'marks':2, 'space':28},

  {'text':'Write 0.375 as a fraction in its simplest form and as a percentage.',
   'marks':2, 'space':26},

  {'text':'In a class of 40 students, 24 are girls. What percentage of the class are boys?',
   'marks':3, 'space':32,
   'tip':'Two steps. Find the number of boys first — the question is not asking about girls.'},
 ]}

# ----------------------------------------------------------------- PAPER C
C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — decimals and reverse percentages',
   'text':'For each fraction, state whether its decimal <b>terminates</b> or <b>recurs</b>, '
          'and write the decimal.', 'marks':3,
   'parts':[{'label':'(a)','text':'3/16','marks':1,'space':18},
            {'label':'(b)','text':'5/12','marks':1,'space':18},
            {'label':'(c)','text':'7/25','marks':1,'space':18}],
   'tip':'You can tell before dividing. Look at the prime factors of the denominator.'},

  {'text':'After a 20% increase, the price of a book is 96 rupees. '
          'Find the price before the increase.', 'marks':3, 'space':34},

  {'text':'A price is reduced by 25% to 180 rupees. Find the original price.',
   'marks':3, 'space':34},

  {'section':'Section 2 — successive change',
   'text':'A sum of money is increased by 10%, and the result is then decreased by 10%.', 'marks':3,
   'parts':[{'label':'(a)','text':'Show, using a starting value of your choice, that the final amount '
                                  'is not the same as the original.','marks':2,'space':30},
            {'label':'(b)','text':'State the overall percentage change.','marks':1,'space':16}]},

  {'text':'Work out 2/3 of 3/5 of 450.', 'marks':3, 'space':30},

  {'text':'A jacket has a marked price of 2400 rupees. Two shops sell it.<br/>'
          '<b>Shop A:</b> a straight 30% off.<br/>'
          '<b>Shop B:</b> 1/4 off the marked price, then a further 10% off that reduced price.', 'marks':4,
   'parts':[{'label':'(a)','text':'Find the price at each shop.','marks':2,'space':32},
            {'label':'(b)','text':'State which shop is cheaper, and by how much.','marks':2,'space':22}]},

  {'section':'Section 3 — multi-step',
   'text':'A number is 5/8 of 640. Find 15% of that number.', 'marks':3, 'space':32},

  {'text':'A bag of rice loses 12% of its mass. It now has a mass of 4.4 kg. '
          'Find the original mass of the bag.', 'marks':3, 'space':32},

  {'text':'Write the recurring decimal 0.4444&hellip; as a fraction in its simplest form.',
   'marks':2, 'space':26,
   'tip':'The recurring block is one digit long. Ninths are worth knowing by heart.'},

  {'text':'In a sale a coat is reduced by 35%, and then a further 10% is taken off at the till. '
          'A sign says <b>&ldquo;45% off everything&rdquo;</b>. Explain why the sign is wrong, '
          'and give the correct single percentage discount.', 'marks':3, 'space':38},
 ]}

# ----------------------------------------------------------------- PAPER D
D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 50 minutes · 30 marks',
 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — profit and loss',
   'text':'A trader buys an item for 480 rupees and sells it for 600 rupees. '
          'Calculate the percentage profit.', 'marks':3, 'space':32},

  {'text':'A shopkeeper sells a bicycle at a 20% loss, receiving 640 rupees for it. '
          'Find the price he originally paid.', 'marks':3, 'space':32,
   'tip':'A 20% loss means he received 80% of what he paid. That is the same shape of problem as a reverse percentage.'},

  {'section':'Section 2 — fractions of what is left',
   'text':'Anil spends 1/3 of his money on books, and then 1/4 of what remains on food. '
          'He is left with 900 rupees.', 'marks':4,
   'parts':[{'label':'(a)','text':'What fraction of his original money does he have left?','marks':2,'space':30},
            {'label':'(b)','text':'How much money did he start with?','marks':2,'space':24}]},

  {'text':'A tank is 3/5 full. After 240 litres are removed, it is 1/3 full. '
          'Find the total capacity of the tank.', 'marks':4, 'space':40},

  {'section':'Section 3 — comparisons and traps',
   'text':'A shop offers two deals on an item priced at 600 rupees.<br/>'
          '<b>Deal 1:</b> 20% off, then a further 10% off.<br/>'
          '<b>Deal 2:</b> 25% off, then a further 5% off.<br/>'
          'Work out the final price under each deal, and state which is better and by how much.',
   'marks':4, 'space':44},

  {'text':'The price of an item rises by 25%. By what percentage must the new price now fall '
          'to bring it back to exactly the original price?', 'marks':4, 'space':40,
   'tip':'The answer is not 25%. Work with a starting value of 100 if that helps you see it.'},

  {'text':'In a school of 500 students, 3/5 are girls. 25% of the girls and 40% of the boys '
          'walk to school. How many students walk to school in total?', 'marks':4, 'space':44},

  {'text':'A student has written two answers in her book, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;0.9 is smaller than 0.15, because 15 is bigger than 9.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;1/2 + 1/3 = 2/5&rdquo;<br/>'
          'For each one, explain the mistake and give the correct answer.', 'marks':4, 'space':46},
 ]}

# ----------------------------------------------------------------- mark scheme
SCHEMES = [
 {'title':'Paper A — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':6, 'lines':[
     'Row 1: <b>0.75</b> and <b>75%</b>. &nbsp; Row 2: <b>7/20</b> and <b>35%</b>. &nbsp; Row 3: <b>3/5</b> and <b>0.6</b>.'],
    'note':'One mark per correct box. 35/100 not simplified to 7/20 loses that one box only.'},
   {'n':'2', 'marks':2, 'lines':['(a) 45/100 = <b>9/20</b>', '(b) 24/100 = <b>6/25</b>']},
   {'n':'3', 'marks':2, 'lines':['(a) 7 &divide; 8 = <b>0.875</b>', '(b) 5 &divide; 16 = <b>0.3125</b>']},
   {'n':'4', 'marks':4, 'lines':[
     '(a) 12/20 + 5/20 = <b>17/20</b>', '(b) 5/6 &minus; 2/6 = 3/6 = <b>1/2</b>',
     '(c) 18/30 = <b>3/5</b>', '(d) 3/4 &times; 5/2 = 15/8 = <b>1 7/8</b>'],
    'note':'Award the mark for a correct unsimplified answer only if the question did not ask for simplest form — here it did.'},
   {'n':'5', 'marks':3, 'lines':['(a) <b>120</b>', '(b) <b>9</b>', '(c) <b>30</b>'],
    'note':'(c) is 1/8 of 240. Halving three times is quicker than any other route.'},
   {'n':'6', 'marks':2, 'lines':[
     'Converting all four to decimals: 0.7, 0.6, 0.65, 0.667 <b>[1]</b>',
     'Order: <b>3/5, 65%, 2/3, 0.7</b> <b>[1]</b>'],
    'note':'The second mark requires the original forms. Answering 0.6, 0.65, 0.667, 0.7 loses it.'},
   {'n':'7', 'marks':2, 'lines':['1200 &times; 0.8 <b>[1]</b>', '= <b>960 rupees</b> <b>[1]</b>'],
    'note':'Finding 240 and stopping scores 1 — that is the discount, not the sale price.'},
   {'n':'8', 'marks':2, 'lines':['40% of 30 = 12 wear glasses <b>[1]</b>', '30 &minus; 12 = <b>18</b> <b>[1]</b>'],
    'note':'Or 60% of 30 directly. Answering 12 scores 1: the question asked who does not.'},
   {'n':'9', 'marks':3, 'lines':['(a) 500 &divide; 4 = 125, so 3 &times; 125 = <b>375 g</b> <b>[2]</b>',
                                 '(b) 500 &minus; 375 = <b>125 g</b> <b>[1]</b>']},
   {'n':'10', 'marks':2, 'lines':['(a) 18/24 = <b>3/4</b>', '(b) <b>75%</b>']},
   {'n':'11', 'marks':2, 'lines':['8000 &times; 1.05 <b>[1]</b>', '= <b>8400 rupees</b> <b>[1]</b>']},
  ]},

 {'title':'Paper B — Medium', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':2, 'lines':['(a) <b>13/5</b>', '(b) <b>4 1/4</b>']},
   {'n':'2', 'marks':4, 'lines':[
     '(a) 3/2 + 11/4 = 6/4 + 11/4 = 17/4 = <b>4 1/4</b>',
     '(b) 10/3 &minus; 11/6 = 20/6 &minus; 11/6 = 9/6 = <b>1 1/2</b>',
     '(c) 5/4 &times; 12/5 = 60/20 = <b>3</b> <b>[2]</b>'],
    'note':'In (c), one mark for converting both mixed numbers to improper fractions, one for the answer.'},
   {'n':'3', 'marks':2, 'lines':['Decimals: 0.46, 0.444, 0.43, 0.45 <b>[1]</b>',
                                 'Order: <b>43%, 4/9, 9/20, 0.46</b> <b>[1]</b>']},
   {'n':'4', 'marks':2, 'lines':['250 &times; 1.12 <b>[1]</b>', '= <b>280</b> <b>[1]</b>']},
   {'n':'5', 'marks':2, 'lines':['640 &times; 0.85 <b>[1]</b>', '= <b>544</b> <b>[1]</b>']},
   {'n':'6', 'marks':3, 'lines':['Change = 800 &minus; 680 = 120 <b>[1]</b>',
                                 '120 &divide; 800 <b>[1]</b>', '= <b>15% decrease</b> <b>[1]</b>'],
    'note':'Dividing by 680 instead of 800 gives 17.6% — the single most common error in this topic. Award the first mark only.'},
   {'n':'7', 'marks':3, 'lines':['Change = 4600 &minus; 4000 = 600 <b>[1]</b>',
                                 '600 &divide; 4000 <b>[1]</b>', '= <b>15% increase</b> <b>[1]</b>']},
   {'n':'8', 'marks':2, 'lines':['320 &divide; 8 = 40, so 3 &times; 40 <b>[1]</b>', '= <b>120</b> <b>[1]</b>']},
   {'n':'9', 'marks':3, 'lines':['5/8 of 400 = <b>250</b> <b>[1]</b>', '60% of 420 = <b>252</b> <b>[1]</b>',
                                 '<b>60% of 420 is larger</b> (by 2) <b>[1]</b>'],
    'note':'The third mark is for the conclusion in words. Two correct numbers with no statement scores 2.'},
   {'n':'10', 'marks':2, 'lines':['68% of 250 = 170 full <b>[1]</b>', '250 &minus; 170 = <b>80 empty</b> <b>[1]</b>'],
    'note':'Or 32% of 250 directly.'},
   {'n':'11', 'marks':2, 'lines':['375/1000 = <b>3/8</b> <b>[1]</b>', '<b>37.5%</b> <b>[1]</b>']},
   {'n':'12', 'marks':3, 'lines':['Boys = 40 &minus; 24 = 16 <b>[1]</b>', '16/40 <b>[1]</b>', '= <b>40%</b> <b>[1]</b>'],
    'note':'Answering 60% means the student found the girls. That scores nothing beyond the method mark.'},
  ]},

 {'title':'Paper C — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':3, 'lines':[
     '(a) <b>Terminates</b>, 0.1875 &nbsp;(16 = 2&times;2&times;2&times;2)',
     '(b) <b>Recurs</b>, 0.41666&hellip; &nbsp;(12 has a factor of 3)',
     '(c) <b>Terminates</b>, 0.28 &nbsp;(25 = 5&times;5)'],
    'note':'Both halves needed for each mark. A fraction terminates only when the denominator, in simplest form, has no prime factors other than 2 and 5.'},
   {'n':'2', 'marks':3, 'lines':['The multiplier for a 20% increase is 1.2 <b>[1]</b>',
                                 'Original = 96 &divide; 1.2 <b>[1]</b>', '= <b>80 rupees</b> <b>[1]</b>'],
    'note':'Taking 20% off 96 gives 76.80 and scores zero. You must divide, not subtract.'},
   {'n':'3', 'marks':3, 'lines':['The multiplier for a 25% decrease is 0.75 <b>[1]</b>',
                                 'Original = 180 &divide; 0.75 <b>[1]</b>', '= <b>240 rupees</b> <b>[1]</b>']},
   {'n':'4', 'marks':3, 'lines':[
     '(a) Starting from 100: 100 &times; 1.1 = 110, then 110 &times; 0.9 = <b>99</b>, which is not 100 <b>[2]</b>',
     '(b) 1.1 &times; 0.9 = 0.99, so an overall <b>1% decrease</b> <b>[1]</b>'],
    'note':'Any starting value is acceptable in (a). The second 10% is taken off a larger number than the first was added to, so the two never cancel.'},
   {'n':'5', 'marks':3, 'lines':['3/5 of 450 = 270 <b>[1]</b>', '2/3 of 270 <b>[1]</b>', '= <b>180</b> <b>[1]</b>'],
    'note':'Also acceptable: 2/3 &times; 3/5 = 2/5, then 2/5 of 450 = 180. Full marks for either route.'},
   {'n':'6', 'marks':4, 'lines':[
     '(a) Shop A: 2400 &times; 0.7 = <b>1680</b> <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;Shop B: 2400 &times; 0.75 = 1800, then 1800 &times; 0.9 = <b>1620</b> <b>[1]</b>',
     '(b) <b>Shop B is cheaper</b> <b>[1]</b>, by 1680 &minus; 1620 = <b>60 rupees</b> <b>[1]</b>'],
    'note':'Adding 25% and 10% to get 35% off is the trap. Successive percentage changes multiply.'},
   {'n':'7', 'marks':3, 'lines':['5/8 of 640 = 400 <b>[1]</b>', '15% of 400 <b>[1]</b>', '= <b>60</b> <b>[1]</b>']},
   {'n':'8', 'marks':3, 'lines':['Losing 12% leaves 88%, so the multiplier is 0.88 <b>[1]</b>',
                                 '4.4 &divide; 0.88 <b>[1]</b>', '= <b>5 kg</b> <b>[1]</b>'],
    'note':'Adding 12% to 4.4 gives 4.93 and scores at most the first mark.'},
   {'n':'9', 'marks':2, 'lines':['Recognising a single recurring digit gives ninths <b>[1]</b>', '= <b>4/9</b> <b>[1]</b>'],
    'note':'Worth memorising: 0.111&hellip; = 1/9, so 0.444&hellip; = 4/9 and 0.777&hellip; = 7/9.'},
   {'n':'10', 'marks':3, 'lines':[
     'Overall multiplier = 0.65 &times; 0.9 = 0.585 <b>[1]</b>',
     'So the customer pays 58.5% of the original, a discount of <b>41.5%</b> <b>[1]</b>',
     'The sign is wrong because the two discounts have been <b>added</b>; the second 10% is taken off an already reduced price, so it is worth less than 10% of the original <b>[1]</b>'],
   },
  ]},

 {'title':'Paper D — Hard', 'meta':'30 marks · non-calculator',
  'questions':[
   {'n':'1', 'marks':3, 'lines':['Profit = 600 &minus; 480 = 120 <b>[1]</b>',
                                 '120 &divide; 480 <b>[1]</b>', '= <b>25% profit</b> <b>[1]</b>'],
    'note':'Percentage profit is always measured against the <i>cost</i> price, never the selling price.'},
   {'n':'2', 'marks':3, 'lines':['A 20% loss means he received 80%, so the multiplier is 0.8 <b>[1]</b>',
                                 '640 &divide; 0.8 <b>[1]</b>', '= <b>800 rupees</b> <b>[1]</b>']},
   {'n':'3', 'marks':4, 'lines':[
     '(a) After books he has 2/3 left. He then spends 1/4 of that, so he keeps 3/4 of 2/3 <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;3/4 &times; 2/3 = <b>1/2</b> <b>[1]</b>',
     '(b) 1/2 of the original = 900 <b>[1]</b>, so he started with <b>1800 rupees</b> <b>[1]</b>'],
    'note':'The trap is adding 1/3 and 1/4 to get 7/12 spent. The second fraction is of the remainder, not of the original.'},
   {'n':'4', 'marks':4, 'lines':[
     'Fraction removed = 3/5 &minus; 1/3 <b>[1]</b>',
     '= 9/15 &minus; 5/15 = 4/15 <b>[1]</b>',
     '4/15 of the capacity = 240, so 1/15 = 60 <b>[1]</b>',
     'Capacity = 60 &times; 15 = <b>900 litres</b> <b>[1]</b>']},
   {'n':'5', 'marks':4, 'lines':[
     'Deal 1: 600 &times; 0.8 &times; 0.9 = <b>432</b> <b>[2]</b>',
     'Deal 2: 600 &times; 0.75 &times; 0.95 = <b>427.50</b> <b>[1]</b>',
     '<b>Deal 2 is better, by 4.50 rupees</b> <b>[1]</b>'],
    'note':'Both deals total 30% if you add them, which is exactly why they look identical and are not.'},
   {'n':'6', 'marks':4, 'lines':[
     'Take the original as 100; after a 25% rise it is 125 <b>[1]</b>',
     'The fall needed is 25 out of 125 <b>[1]</b>',
     '25 &divide; 125 = 0.2 <b>[1]</b>',
     'So the price must fall by <b>20%</b> <b>[1]</b>'],
    'note':'Answering 25% scores at most one mark. The fall is measured against the new, larger price — this is the same idea as the 10% up-and-down question on Paper C.'},
   {'n':'7', 'marks':4, 'lines':[
     'Girls = 3/5 of 500 = 300, so boys = 200 <b>[1]</b>',
     '25% of 300 = 75 girls walk <b>[1]</b>',
     '40% of 200 = 80 boys walk <b>[1]</b>',
     'Total = 75 + 80 = <b>155 students</b> <b>[1]</b>'],
    'note':'Averaging 25% and 40% to get 32.5% of 500 gives 162.5 and scores nothing. The two groups are different sizes.'},
   {'n':'8', 'marks':4, 'lines':[
     '(i) The mistake: comparing decimals by the size of the digits after the point instead of by place value <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;Padding with a zero gives 0.90 against 0.15, so <b>0.9 is larger</b> <b>[1]</b>',
     '(ii) The mistake: adding the numerators and the denominators separately <b>[1]</b>',
     '&nbsp; &nbsp; &nbsp;Using a common denominator: 3/6 + 2/6 = <b>5/6</b> <b>[1]</b>'],
    'note':'A useful check for (ii): the answer must be bigger than 1/2, and 2/5 is smaller — so it is wrong before you calculate anything.'},
  ]},
]

# ----------------------------------------------------------------- build
def total(spec):
    return sum(q.get('marks', 0) for q in spec['questions'])

files = []
for spec, code in [(A, 'a'), (B, 'b'), (C, 'c'), (D, 'd')]:
    t = total(spec)
    assert t == 30, (spec['title'], t)
    p = os.path.join(OUT, 'maths-fdp-paper-%s.pdf' % code)
    build_paper(spec, p)
    files.append(p)

for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)

p = os.path.join(OUT, 'maths-fdp-answers.pdf')
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
