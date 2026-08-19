#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Physics · Grade 7 · Forces'
TOPIC = 'The Turning Effect'

BASE = [
 'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
 'A calculator is allowed, but every number on this paper is designed to work without one.',
 'Always convert centimetres to metres <b>before</b> you multiply, and give every moment the unit <b>N m</b>.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + ['Reminder: <b>moment = force &times; perpendicular distance from the pivot</b>.']
INSTR_HARD = BASE + ['No formula is given on this paper. If you cannot remember it, write down what you do know and work from there.',
                     'Where a beam has its own weight, that weight acts at its centre.']

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — the idea','text':'Answer these three parts about the moment of a force.','marks':3,
   'parts':[{'label':'(a)','text':'State what is meant by the <b>moment of a force</b>.','marks':1,'space':18},
            {'label':'(b)','text':'Write down the formula for a moment.','marks':1,'space':16},
            {'label':'(c)','text':'State the unit of a moment.','marks':1,'space':14}]},
  {'text':'Calculate the moment in each case.','marks':4,
   'parts':[{'label':'(a)','text':'A force of 20 N acting 0.5 m from the pivot.','marks':1,'space':18},
            {'label':'(b)','text':'A force of 40 N acting 25 cm from the pivot.','marks':2,'space':24},
            {'label':'(c)','text':'A force of 12 N acting 1.5 m from the pivot.','marks':1,'space':18}]},
  {'text':'A mechanic uses a spanner with a long handle rather than a short one. '
          'Explain why this makes the nut easier to undo.','marks':2,'space':28},
  {'text':'A beam is free to turn about a pivot at its centre.','marks':2,
   'parts':[{'label':'(a)','text':'A force pushes down on the right-hand end. State the direction of the turning effect.','marks':1,'space':14},
            {'label':'(b)','text':'A force pushes down on the left-hand end. State the direction of the turning effect.','marks':1,'space':14}]},
  {'section':'Section 2 — calculation','text':'Convert each distance into metres, ready for the moment formula.','marks':2,
   'parts':[{'label':'(a)','text':'60 cm','marks':1,'space':14},
            {'label':'(b)','text':'250 cm','marks':1,'space':14}]},
  {'text':'A force of 25 N acts at a perpendicular distance of 40 cm from a pivot, turning the object clockwise. '
          'Calculate the moment and state its direction.','marks':3,'space':32},
  {'text':'The handle of a door is fitted as far as possible from the hinges. Explain why.','marks':2,'space':26},
  {'text':'A child of weight 300 N sits 2 m from the pivot of a see-saw. Calculate the moment of his weight about the pivot.',
   'marks':2,'space':28},
  {'section':'Section 3 — balance','text':'State the <b>principle of moments</b>.','marks':2,'space':26},
  {'text':'State where the pivot is in each case.','marks':2,
   'parts':[{'label':'(a)','text':'A door being pushed open.','marks':1,'space':14},
            {'label':'(b)','text':'A spanner turning a nut.','marks':1,'space':14}]},
  {'text':'A force of 15 N acts 0.8 m to the left of a pivot. A force of 24 N acts 0.5 m to the right of the same pivot.',
   'marks':4,
   'parts':[{'label':'(a)','text':'Calculate the anticlockwise moment.','marks':1,'space':18},
            {'label':'(b)','text':'Calculate the clockwise moment.','marks':1,'space':18},
            {'label':'(c)','text':'State, with a reason, whether the beam balances.','marks':2,'space':22}]},
  {'text':'Explain why the distance in the moment formula must be the <b>perpendicular</b> distance from the pivot.',
   'marks':2,'space':26},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — balancing','text':'State the principle of moments.','marks':2,'space':26},
  {'text':'Ravi, whose weight is 320 N, sits 1.6 m from the pivot of a see-saw. Meera weighs 400 N. '
          'How far from the pivot must she sit to balance it?','marks':3,'space':36},
  {'text':'A metre rule is pivoted at its 50 cm mark. A weight of 2 N hangs at the 20 cm mark.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the anticlockwise moment about the pivot.','marks':2,'space':26},
            {'label':'(b)','text':'A 4 N weight is used to balance the rule. At which mark must it hang?','marks':2,'space':30}]},
  {'text':'A crowbar is used to lift a heavy stone. An effort of 200 N is applied 1.2 m from the pivot, '
          'and the stone sits 0.2 m from the pivot on the other side. Calculate the largest weight of stone that can be lifted.',
   'marks':3,'space':36},
  {'section':'Section 2 — more than two forces',
   'text':'On the left of a see-saw pivot, a 250 N child sits 1.2 m away and a 150 N child sits 2.0 m away. '
          'A single child of weight 400 N sits on the right.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the total anticlockwise moment.','marks':2,'space':26},
            {'label':'(b)','text':'How far from the pivot must the 400 N child sit to balance the see-saw?','marks':2,'space':26}]},
  {'text':'Explain each of these using the idea of moments.','marks':4,
   'parts':[{'label':'(a)','text':'A door is harder to push open near its hinges than at its handle.','marks':2,'space':26},
            {'label':'(b)','text':'A loaded wheelbarrow is easier to lift when the load is placed close to the wheel.','marks':2,'space':26}]},
  {'text':'A see-saw is balanced. One child then slides closer to the pivot. '
          'State and explain what happens next.','marks':3,'space':32},
  {'text':'Calculate the moment of a force of 18 N acting 45 cm from a pivot.','marks':2,'space':26},
  {'section':'Section 3 — using the idea',
   'text':'Give two situations in everyday life where a large moment is useful, and explain one of them.',
   'marks':3,'space':34},
  {'text':'A student writes: <i>&ldquo;The moment of the force is 30 N.&rdquo;</i> '
          'Explain what is wrong with this statement.','marks':2,'space':26},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — beams with weight',
   'text':'A uniform plank is 4 m long and has a weight of 200 N. It is pivoted 1 m from its left-hand end.','marks':4,
   'parts':[{'label':'(a)','text':'State where the weight of the plank acts, and how far this is from the pivot.','marks':2,'space':26},
            {'label':'(b)','text':'Calculate the moment of the plank&rsquo;s weight about the pivot, and state its direction.','marks':2,'space':28}]},
  {'text':'A uniform beam 3 m long is pivoted exactly at its centre. A 20 N weight hangs 1.2 m to the left of the pivot.',
   'marks':4,
   'parts':[{'label':'(a)','text':'Explain why the weight of the beam itself has no turning effect about this pivot.','marks':2,'space':26},
            {'label':'(b)','text':'A 30 N weight is hung on the right to balance the beam. Calculate its distance from the pivot.','marks':2,'space':30}]},
  {'text':'Two forces act anticlockwise about a pivot: 5 N at 0.4 m, and 3 N at 0.9 m. '
          'A single force is applied 0.5 m from the pivot on the other side to balance them. Calculate its size.',
   'marks':4,'space':40},
  {'section':'Section 2 — thinking about the model',
   'text':'A force is applied to the end of a spanner at an angle, rather than at right angles to the handle. '
          'Explain why the moment produced is smaller than force &times; length of handle.','marks':2,'space':28},
  {'text':'A uniform beam 6 m long and of weight 300 N rests on a support at each end. '
          'State the upward force provided by each support, and explain your reasoning.','marks':3,'space':34},
  {'text':'A plank 2 m long is found to balance on a pivot placed 0.8 m from its left-hand end. '
          'State what this tells you about the plank, and explain how you know.','marks':3,'space':34},
  {'section':'Section 3 — putting it together',
   'text':'A metre rule of weight 1 N is pivoted at its 40 cm mark. A 2 N weight hangs at the 10 cm mark. '
          'The weight of the rule acts at its 50 cm mark.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the anticlockwise moment produced by the 2 N weight.','marks':1,'space':20},
            {'label':'(b)','text':'Calculate the clockwise moment produced by the weight of the rule itself.','marks':2,'space':24},
            {'label':'(c)','text':'A weight is hung at the 90 cm mark to balance the rule. Calculate its size.','marks':2,'space':30}]},
  {'text':'Explain how two children of very different weights can still balance a see-saw.','marks':2,'space':26},
  {'text':'A nut requires a moment of 30 N m to loosen it.','marks':3,
   'parts':[{'label':'(a)','text':'Calculate the force needed on a spanner of length 25 cm.','marks':1,'space':22},
            {'label':'(b)','text':'Calculate the force needed on a spanner of length 40 cm.','marks':1,'space':22},
            {'label':'(c)','text':'Comment on what your two answers show.','marks':1,'space':18}]},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — several forces at once',
   'text':'Four children sit on a see-saw. On the left: 250 N at 1.6 m from the pivot, and 200 N at 0.8 m. '
          'On the right: 300 N at 1.2 m, and a fourth child sitting 2.0 m from the pivot. The see-saw balances.',
   'marks':5,
   'parts':[{'label':'(a)','text':'Calculate the total anticlockwise moment.','marks':2,'space':26},
            {'label':'(b)','text':'Calculate the moment produced by the 300 N child.','marks':1,'space':20},
            {'label':'(c)','text':'Calculate the weight of the fourth child.','marks':2,'space':30}]},
  {'text':'A uniform beam is 4 m long and has a weight of 400 N. It is pivoted 1.5 m from its left-hand end. '
          'A load of 600 N hangs from the left-hand end.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the moment of the 600 N load about the pivot.','marks':1,'space':22},
            {'label':'(b)','text':'Calculate the moment of the beam&rsquo;s own weight about the pivot, and state its direction.','marks':2,'space':28},
            {'label':'(c)','text':'A downward force is applied at the right-hand end to balance the beam. Calculate its size.','marks':2,'space':32}]},
  {'section':'Section 2 — designing and judging',
   'text':'A worker can push down with a maximum force of 250 N. She needs to produce a moment of 400 N m '
          'to shift a paving slab with a crowbar.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the shortest crowbar that would do the job.','marks':2,'space':28},
            {'label':'(b)','text':'Explain one practical problem with using a crowbar much longer than this.','marks':2,'space':26}]},
  {'text':'A student says: <i>&ldquo;The distance in the moment formula is just the distance from the pivot to '
          'where you push.&rdquo;</i> Explain what is missing from this statement, and when it matters.',
   'marks':3,'space':34},
  {'text':'A tall bus travelling round a bend begins to tip. Explain, using moments and the idea of a pivot, '
          'why a bus with passengers on the upper deck tips more easily than an empty one.','marks':4,'space':44},
  {'text':'A wheelbarrow carries a load of 500 N whose weight acts 0.4 m from the wheel. '
          'The handles are 1.2 m from the wheel.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the upward force needed at the handles to lift the barrow.','marks':3,'space':32},
            {'label':'(b)','text':'Explain why moving the load closer to the wheel reduces the force needed.','marks':2,'space':26}]},
  {'text':'A student claims: <i>&ldquo;Doubling the force always doubles the moment.&rdquo;</i> '
          'State whether this is true, and describe a situation in which doubling the force does '
          '<b>not</b> double the moment.','marks':4,'space':44},
 ]}

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':3,'lines':['(a) The turning effect of a force about a pivot.',
    '(b) moment = force &times; perpendicular distance from the pivot.','(c) <b>N m</b> (newton metre).'],
   'note':'The word "perpendicular" is required in (b). Without it, do not award the mark.'},
  {'n':'2','marks':4,'lines':['(a) 20 &times; 0.5 = <b>10 N m</b>',
    '(b) 25 cm = 0.25 m <b>[1]</b>; 40 &times; 0.25 = <b>10 N m</b> <b>[1]</b>','(c) 12 &times; 1.5 = <b>18 N m</b>'],
   'note':'In (b), 40 &times; 25 = 1000 scores zero. The conversion is the whole point of the question.'},
  {'n':'3','marks':2,'lines':['A longer handle gives a larger distance <i>d</i> from the pivot <b>[1]</b>',
    'Since moment = F &times; d, the same force produces a larger moment, so the nut turns more easily <b>[1]</b>']},
  {'n':'4','marks':2,'lines':['(a) <b>Clockwise</b>','(b) <b>Anticlockwise</b>']},
  {'n':'5','marks':2,'lines':['(a) <b>0.6 m</b>','(b) <b>2.5 m</b>']},
  {'n':'6','marks':3,'lines':['40 cm = 0.40 m <b>[1]</b>','25 &times; 0.40 = <b>10 N m</b> <b>[1]</b>','<b>Clockwise</b> <b>[1]</b>'],
   'note':'Omitting the direction costs a mark for a word the student already knew.'},
  {'n':'7','marks':2,'lines':['The handle is far from the hinges, which are the pivot, so <i>d</i> is large <b>[1]</b>',
    'A larger distance gives a larger moment for the same push, so the door opens more easily <b>[1]</b>']},
  {'n':'8','marks':2,'lines':['300 &times; 2 <b>[1]</b>','= <b>600 N m</b> <b>[1]</b>']},
  {'n':'9','marks':2,'lines':['When an object is balanced, the total clockwise moment about a pivot <b>[1]</b>',
    'equals the total anticlockwise moment about the same pivot <b>[1]</b>'],
   'note':'"About the same pivot" is worth insisting on — it becomes essential on Papers C and D.'},
  {'n':'10','marks':2,'lines':['(a) The <b>hinges</b>','(b) The <b>nut</b> (the centre of the nut)']},
  {'n':'11','marks':4,'lines':['(a) 15 &times; 0.8 = <b>12 N m</b> anticlockwise',
    '(b) 24 &times; 0.5 = <b>12 N m</b> clockwise',
    '(c) The two moments are equal <b>[1]</b>, so the beam <b>balances</b> <b>[1]</b>']},
  {'n':'12','marks':2,'lines':['The distance must be measured at right angles to the line of action of the force <b>[1]</b>',
    'If the force is at an angle, only the perpendicular part of the distance produces turning, so using the full distance overestimates the moment <b>[1]</b>']},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':2,'lines':['Total clockwise moment = total anticlockwise moment <b>[1]</b>',
    'about the same pivot, when the object is balanced <b>[1]</b>']},
  {'n':'2','marks':3,'lines':['Ravi&rsquo;s moment = 320 &times; 1.6 = 512 N m <b>[1]</b>',
    '400 &times; d = 512 <b>[1]</b>','d = <b>1.28 m</b> <b>[1]</b>'],
   'note':'Heavier child, shorter distance. If the answer comes out bigger than 1.6 m, it is wrong before it is checked.'},
  {'n':'3','marks':4,'lines':['(a) Distance = 50 &minus; 20 = 30 cm = 0.30 m <b>[1]</b>; 2 &times; 0.30 = <b>0.6 N m</b> <b>[1]</b>',
    '(b) 4 &times; d = 0.6, so d = 0.15 m = 15 cm <b>[1]</b>; on the other side of the pivot, so at the <b>65 cm mark</b> <b>[1]</b>'],
   'note':'Using 20 cm as the distance instead of 30 cm is the standard error. Distances are measured from the pivot, not from the end of the rule.'},
  {'n':'4','marks':3,'lines':['Effort moment = 200 &times; 1.2 = 240 N m <b>[1]</b>','W &times; 0.2 = 240 <b>[1]</b>','W = <b>1200 N</b> <b>[1]</b>']},
  {'n':'5','marks':4,'lines':['(a) 250 &times; 1.2 = 300, and 150 &times; 2.0 = 300 <b>[1]</b>; total = <b>600 N m</b> <b>[1]</b>',
    '(b) 400 &times; d = 600 <b>[1]</b>, so d = <b>1.5 m</b> <b>[1]</b>']},
  {'n':'6','marks':4,'lines':[
    '(a) Near the hinges the distance from the pivot is small <b>[1]</b>, so the same force gives a much smaller moment and the door resists opening <b>[1]</b>',
    '(b) The load&rsquo;s distance from the wheel (the pivot) is smaller <b>[1]</b>, so the load&rsquo;s moment is smaller and less force is needed at the handles to balance it <b>[1]</b>']},
  {'n':'7','marks':3,'lines':['That child&rsquo;s distance from the pivot decreases <b>[1]</b>',
    'so their moment decreases and the moments are no longer equal <b>[1]</b>',
    'The see-saw tips down on the <b>other</b> side <b>[1]</b>']},
  {'n':'8','marks':2,'lines':['45 cm = 0.45 m <b>[1]</b>','18 &times; 0.45 = <b>8.1 N m</b> <b>[1]</b>']},
  {'n':'9','marks':3,'lines':['Any two sensible examples <b>[2]</b> — spanner, door handle, crowbar, wheelbarrow, scissors, bicycle pedal',
    'One explained using a large distance from the pivot producing a large moment for a small force <b>[1]</b>']},
  {'n':'10','marks':2,'lines':['N is a unit of force, not of moment <b>[1]</b>',
    'A moment must be given in <b>N m</b>, because it is a force multiplied by a distance <b>[1]</b>']},
 ]},

 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':4,'lines':['(a) The weight of a uniform plank acts at its <b>centre</b>, 2 m from the left end <b>[1]</b>; '
    'that is 2 &minus; 1 = <b>1 m</b> from the pivot <b>[1]</b>',
    '(b) 200 &times; 1 = <b>200 N m</b> <b>[1]</b>, acting <b>clockwise</b> (the centre lies to the right of the pivot) <b>[1]</b>']},
  {'n':'2','marks':4,'lines':[
    '(a) The beam is uniform, so its weight acts at its centre, which is exactly where the pivot is <b>[1]</b>. '
    'The distance from the pivot is zero, so the moment is zero <b>[1]</b>',
    '(b) 20 &times; 1.2 = 24 N m; 30 &times; d = 24 <b>[1]</b>, so d = <b>0.8 m</b> <b>[1]</b>']},
  {'n':'3','marks':4,'lines':['5 &times; 0.4 = 2 N m <b>[1]</b>','3 &times; 0.9 = 2.7 N m <b>[1]</b>',
    'Total anticlockwise = 4.7 N m <b>[1]</b>','F &times; 0.5 = 4.7, so F = <b>9.4 N</b> <b>[1]</b>'],
   'note':'Moments on the same side add. Students who subtract them have confused "same side" with "opposite side".'},
  {'n':'4','marks':2,'lines':['At an angle, the perpendicular distance from the pivot to the line of action is shorter than the handle itself <b>[1]</b>',
    'Since the moment uses that shorter perpendicular distance, the moment is smaller <b>[1]</b>']},
  {'n':'5','marks':3,'lines':['<b>150 N</b> at each support <b>[1]</b>',
    'The beam is uniform, so its weight acts at the centre, which is the same distance from each support <b>[1]</b>',
    'By symmetry the two supports share the 300 N equally <b>[1]</b>']},
  {'n':'6','marks':3,'lines':['The plank is <b>not uniform</b> <b>[1]</b>',
    'Its weight acts at the balance point, 0.8 m from the left end <b>[1]</b>',
    'A uniform plank would have balanced at its centre, 1.0 m from the end, so more of its mass lies towards the left <b>[1]</b>']},
  {'n':'7','marks':5,'lines':['(a) Distance = 40 &minus; 10 = 30 cm = 0.30 m; 2 &times; 0.30 = <b>0.6 N m</b> <b>[1]</b>',
    '(b) The rule&rsquo;s weight acts at 50 cm, which is 0.10 m to the right of the pivot <b>[1]</b>; 1 &times; 0.10 = <b>0.1 N m</b> clockwise <b>[1]</b>',
    '(c) Clockwise needed = 0.6 &minus; 0.1 = 0.5 N m <b>[1]</b>; the 90 cm mark is 0.5 m from the pivot, so W &times; 0.5 = 0.5 and W = <b>1 N</b> <b>[1]</b>'],
   'note':'Forgetting the rule&rsquo;s own weight in (c) gives 1.2 N. That omission is what this question exists to catch.'},
  {'n':'8','marks':2,'lines':['The lighter child sits further from the pivot <b>[1]</b>',
    'so that weight &times; distance is the same on both sides, even though the weights differ <b>[1]</b>']},
  {'n':'9','marks':3,'lines':['(a) 30 &divide; 0.25 = <b>120 N</b>','(b) 30 &divide; 0.40 = <b>75 N</b>',
    '(c) A longer spanner needs a smaller force for the same moment <b>[1]</b>'],
   'note':'The moment required is fixed by the nut, not by the person. Only the trade between force and distance changes.'},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) 250 &times; 1.6 = 400 and 200 &times; 0.8 = 160 <b>[1]</b>; total = <b>560 N m</b> <b>[1]</b>',
    '(b) 300 &times; 1.2 = <b>360 N m</b> <b>[1]</b>',
    '(c) The fourth child must supply 560 &minus; 360 = 200 N m <b>[1]</b>; W &times; 2.0 = 200, so W = <b>100 N</b> <b>[1]</b>']},
  {'n':'2','marks':5,'lines':['(a) 600 &times; 1.5 = <b>900 N m</b> anticlockwise <b>[1]</b>',
    '(b) The weight acts at the centre, 2 m from the left end, which is 0.5 m to the right of the pivot <b>[1]</b>; '
    '400 &times; 0.5 = <b>200 N m</b> clockwise <b>[1]</b>',
    '(c) Clockwise still needed = 900 &minus; 200 = 700 N m <b>[1]</b>; the right end is 2.5 m from the pivot, so F = 700 &divide; 2.5 = <b>280 N</b> <b>[1]</b>'],
   'note':'Two common failures: forgetting the beam&rsquo;s weight entirely (giving 360 N), and using 4 m instead of 2.5 m as the distance to the right-hand end.'},
  {'n':'3','marks':4,'lines':['(a) 250 &times; L = 400 <b>[1]</b>, so L = <b>1.6 m</b> <b>[1]</b>',
    '(b) Any sensible problem, explained <b>[2]</b> — it becomes unwieldy or too heavy to handle; '
    'she may not be able to reach the far end while keeping the pivot in place; the bar may bend or snap.']},
  {'n':'4','marks':3,'lines':['It must be the <b>perpendicular</b> distance <b>[1]</b>',
    'measured from the pivot to the <b>line of action</b> of the force <b>[1]</b>',
    'It matters whenever the force is not at right angles to the arm — then the perpendicular distance is shorter than the distance to your hand, and the student&rsquo;s version overestimates the moment <b>[1]</b>'],
   'note':'When the force <i>is</i> perpendicular, the student&rsquo;s statement happens to give the right answer, which is why the misunderstanding survives so long.'},
  {'n':'5','marks':4,'lines':['The bus pivots about the outer wheels on the bend <b>[1]</b>',
    'Passengers upstairs have their weight acting higher up and further out as the bus leans <b>[1]</b>',
    'This gives a larger perpendicular distance from the pivot, so a larger overturning moment <b>[1]</b>',
    'When the overturning moment exceeds the restoring moment of the bus&rsquo;s own weight, it tips <b>[1]</b>']},
  {'n':'6','marks':5,'lines':['(a) Load moment = 500 &times; 0.4 = 200 N m <b>[1]</b>; F &times; 1.2 = 200 <b>[1]</b>; F = <b>167 N</b> (166.7 N) <b>[1]</b>',
    '(b) Moving the load closer reduces its distance from the wheel <b>[1]</b>, so its moment falls and a smaller force at the handles balances it <b>[1]</b>'],
   'note':'Accept 166.7 N or 167 N. The wheel is the pivot — students who use the far end of the barrow lose the first mark.'},
  {'n':'7','marks':4,'lines':['<b>True, but only if the distance stays the same</b> <b>[1]</b>',
    'Moment = F &times; d, so doubling F doubles the moment when d is unchanged <b>[1]</b>',
    'If the distance changes at the same time, it does not: for example, doubling the force while halving the distance leaves the moment unchanged, since 2F &times; d/2 = Fd <b>[2]</b>'],
   'note':'A worked numerical example is fully acceptable in place of the algebra.'},
 ]},
]

files = []
for spec, code in [(A,'a'), (B,'b'), (C,'c'), (D,'d')]:
    t = sum(q.get('marks',0) for q in spec['questions'])
    assert t == 30, (spec['title'], t)
    p = os.path.join(OUT, 'physics-moments-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)
for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)
p = os.path.join(OUT, 'physics-moments-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Award method marks for a correct '
             'formula and a correct substitution even when the arithmetic fails. Two marks are lost more '
             'often than any others on this topic: the missing unit conversion from centimetres to metres, '
             'and the missing direction on an answer. The notes under each answer flag the specific mistake '
             'that question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
