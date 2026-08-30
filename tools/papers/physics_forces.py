#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Physics · Grade 7 · Forces'
TOPIC = 'Characteristics of Forces'

BASE = [
 'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
 'A calculator is allowed, but every number on this paper is designed to work without one.',
 'Every answer must carry a <b>unit</b>, and every resultant force must carry a <b>direction</b>. An answer with no unit does not score the final mark.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + ['Reminder: <b>weight = mass &times; gravitational field strength</b> (W = mg), and on Earth <b>g = 10 N/kg</b>.']
INSTR_HARD = BASE + ['No formula is given on this paper. Values of <i>g</i> are given only where they are not Earth&rsquo;s.',
                     'Several questions describe situations you may not have seen before — apply the ideas you already have.']

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — naming forces',
   'text':'State what is meant by a <b>force</b>, and give the unit in which force is measured.','marks':2,'space':24},
  {'text':'Name the force being described in each case.','marks':3,
   'parts':[{'label':'(a)','text':'The force that opposes a car as it moves through the air.','marks':1,'space':16},
            {'label':'(b)','text':'The force that pulls a hanging mass downwards.','marks':1,'space':16},
            {'label':'(c)','text':'The force in a rope that is being pulled tight.','marks':1,'space':16}]},
  {'text':'State whether each force below is a <b>contact</b> force or a <b>non-contact</b> force.','marks':3,
   'parts':[{'label':'(a)','text':'Friction','marks':1,'space':14},
            {'label':'(b)','text':'Magnetic attraction','marks':1,'space':14},
            {'label':'(c)','text':'Upthrust','marks':1,'space':14}]},
  {'text':'State the <b>three</b> things a force can change about an object.','marks':3,'space':28},
  {'section':'Section 2 — mass and weight',
   'text':'Calculate the weight of each object on Earth. Take g = 10 N/kg.','marks':4,
   'parts':[{'label':'(a)','text':'A bag of mass 5 kg.','marks':1,'space':18},
            {'label':'(b)','text':'A child of mass 12 kg.','marks':1,'space':18},
            {'label':'(c)','text':'A phone of mass 0.5 kg.','marks':2,'space':22}]},
  {'text':'Calculate the mass of each object. Take g = 10 N/kg.','marks':3,
   'parts':[{'label':'(a)','text':'A crate that weighs 300 N.','marks':1,'space':18},
            {'label':'(b)','text':'A tin that weighs 45 N.','marks':1,'space':18},
            {'label':'(c)','text':'An apple that weighs 7 N.','marks':1,'space':18}]},
  {'text':'Explain the difference between <b>mass</b> and <b>weight</b>. Your answer must include the unit of each.',
   'marks':3,'space':36},
  {'section':'Section 3 — adding forces up',
   'text':'For each pair of horizontal forces, calculate the resultant force. Give a direction as well as a size.','marks':4,
   'parts':[{'label':'(a)','text':'30 N to the right and 20 N to the left.','marks':1,'space':18},
            {'label':'(b)','text':'45 N to the right and 45 N to the left.','marks':1,'space':18},
            {'label':'(c)','text':'12 N to the left and 30 N to the left.','marks':2,'space':22}]},
  {'text':'A book rests on a table. Its weight is 60 N downwards and the table pushes up on it with 60 N.','marks':3,
   'parts':[{'label':'(a)','text':'State the resultant vertical force on the book.','marks':1,'space':16},
            {'label':'(b)','text':'Describe the motion of the book.','marks':1,'space':16},
            {'label':'(c)','text':'State the word used to describe forces that add up to zero.','marks':1,'space':16}]},
  {'text':'A car engine pushes the car forwards with 2400 N. Friction and air resistance together push backwards '
          'with 2400 N. Describe the motion of the car and explain your answer.','marks':2,'space':30},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — drawing and measuring forces',
   'text':'A crate rests on the floor. In the space below, draw the crate and label the <b>two</b> vertical forces '
          'acting on it, using arrows. Then state what you notice about the lengths of your two arrows, and why.',
   'marks':4,'space':66},
  {'text':'Explain why a force is drawn as an <b>arrow</b> on a diagram, rather than written as a number on its own.',
   'marks':3,'space':34},
  {'text':'A newtonmeter is used to measure a force.','marks':3,
   'parts':[{'label':'(a)','text':'State the unit that a newtonmeter reads in.','marks':1,'space':14},
            {'label':'(b)','text':'Name the part inside a newtonmeter that stretches.','marks':1,'space':14},
            {'label':'(c)','text':'State what happens to the stretch when the force pulling on it is doubled.','marks':1,'space':18}]},
  {'section':'Section 2 — resultants and motion',
   'text':'Calculate the resultant force in each case. Give a direction as well as a size.','marks':5,
   'parts':[{'label':'(a)','text':'80 N to the right and 50 N to the right.','marks':1,'space':18},
            {'label':'(b)','text':'90 N to the left and 35 N to the right.','marks':1,'space':18},
            {'label':'(c)','text':'120 N to the right and 120 N to the left.','marks':1,'space':18},
            {'label':'(d)','text':'6 N to the right, 14 N to the left and 4 N to the right.','marks':2,'space':24}]},
  {'text':'A lorry drives along a straight motorway at a steady 25 m/s. The driving force from its engine is 4500 N.','marks':4,
   'parts':[{'label':'(a)','text':'State the size of the total backward force acting on the lorry.','marks':1,'space':16},
            {'label':'(b)','text':'Explain how you know.','marks':1,'space':20},
            {'label':'(c)','text':'The driver presses the accelerator and the driving force rises to 5200 N. '
                                 'Calculate the new resultant force and describe what happens to the lorry.','marks':2,'space':28}]},
  {'text':'Explain the difference between <b>balanced</b> and <b>unbalanced</b> forces, and state what each does '
          'to an object that is already moving.','marks':3,'space':36},
  {'section':'Section 3 — friction',
   'text':'Friction acts on a moving object.','marks':4,
   'parts':[{'label':'(a)','text':'State the direction in which friction acts.','marks':1,'space':16},
            {'label':'(b)','text':'Give two everyday situations in which friction is useful.','marks':2,'space':24},
            {'label':'(c)','text':'Give one situation in which friction is a nuisance.','marks':1,'space':18}]},
  {'text':'A cyclist stops pedalling on a flat road and gradually comes to a stop.','marks':4,
   'parts':[{'label':'(a)','text':'Name the two forces that slow her down.','marks':2,'space':20},
            {'label':'(b)','text':'Explain, in terms of the resultant force on her, why she slows down.','marks':2,'space':28}]},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — the same object, different gravity',
   'text':'The gravitational field strength on the Moon is 1.6 N/kg and on Mars it is 3.7 N/kg.','marks':5,
   'parts':[{'label':'(a)','text':'A rover has a mass of 250 kg. Calculate its weight on Mars.','marks':2,'space':28},
            {'label':'(b)','text':'An instrument weighs 32 N on the Moon. Calculate its mass.','marks':2,'space':28},
            {'label':'(c)','text':'State the weight of that same instrument on Earth.','marks':1,'space':20}]},
  {'text':'A student writes: &ldquo;My mass is 45 kg, so my weight is 45 kg.&rdquo; '
          'Identify <b>two</b> separate errors in that sentence, and calculate the student&rsquo;s correct weight on Earth.',
   'marks':4,'space':44},
  {'section':'Section 2 — forces in more than one direction',
   'text':'A hot-air balloon is held by a rope. Its weight is 12 000 N downwards and the upthrust on it is 15 000 N upwards. '
          'A wind pushes it east with 900 N while the rope pulls it west with 900 N.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the resultant vertical force, and give its direction.','marks':2,'space':28},
            {'label':'(b)','text':'Calculate the resultant horizontal force.','marks':1,'space':20},
            {'label':'(c)','text':'Describe the motion of the balloon, in both directions.','marks':2,'space':28}]},
  {'text':'A box is dragged across a rough floor by a rope.','marks':4,
   'parts':[{'label':'(a)','text':'The rope pulls with 85 N and the box moves at a steady speed. '
                                 'State the size of the friction force and explain how you know.','marks':2,'space':28},
            {'label':'(b)','text':'The pull is increased to 130 N while friction stays at 85 N. '
                                 'Calculate the resultant force and describe its effect on the box.','marks':2,'space':28}]},
  {'section':'Section 3 — judgement',
   'text':'Three forces act on a trolley along one straight line: 26 N to the right, 9 N to the left and 12 N to the left.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the resultant force on the trolley.','marks':2,'space':26},
            {'label':'(b)','text':'A fourth force is now applied so that the trolley moves at a constant velocity. '
                                 'State the size and direction of that fourth force.','marks':2,'space':26}]},
  {'text':'A skydiver of mass 80 kg jumps from a plane.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate her weight.','marks':1,'space':20},
            {'label':'(b)','text':'Just after she jumps, the air resistance acting on her is 150 N. '
                                 'Calculate the resultant force and state its direction.','marks':2,'space':26},
            {'label':'(c)','text':'Later she falls at a constant speed. State the air resistance at that moment.','marks':1,'space':20}]},
  {'text':'A spacecraft far from any planet switches its engine off. It carries on at a steady speed in a straight line '
          'with nothing pushing it. Explain why.','marks':4,'space':46},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — several forces at once',
   'text':'A crate of mass 40 kg is pulled along a rough floor by a horizontal rope. The rope pulls with 260 N and '
          'friction between the crate and the floor is 100 N.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the weight of the crate.','marks':1,'space':20},
            {'label':'(b)','text':'State the size and direction of the force the floor exerts on the crate, '
                                 'and explain how you know.','marks':2,'space':28},
            {'label':'(c)','text':'Calculate the horizontal resultant force and describe the motion of the crate.','marks':2,'space':28}]},
  {'text':'Two children pull a sledge along the ice in opposite directions. Priya pulls east with 145 N and '
          'Kabir pulls west with 190 N. Friction between the sledge and the ice is 15 N.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the resultant of the two pulls, with its direction.','marks':2,'space':26},
            {'label':'(b)','text':'State the direction of the friction force, and calculate the overall resultant '
                                 'force on the sledge.','marks':2,'space':28},
            {'label':'(c)','text':'Describe the motion of the sledge.','marks':1,'space':18}]},
  {'section':'Section 2 — reasoning about motion',
   'text':'A lift carrying a passenger of mass 60 kg is moving upwards at a constant speed.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the weight of the passenger.','marks':1,'space':20},
            {'label':'(b)','text':'State the size of the upward force that the floor of the lift exerts on the passenger, '
                                 'and explain your answer fully.','marks':3,'space':36}]},
  {'text':'A parachutist has a weight of 750 N. The moment her parachute opens, the air resistance acting on her '
          'rises to 1100 N.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the resultant force on her and give its direction.','marks':2,'space':26},
            {'label':'(b)','text':'She is still moving downwards at that moment. Explain how she can be moving '
                                 'downwards while the resultant force on her acts upwards.','marks':2,'space':32}]},
  {'section':'Section 3 — working backwards, and diagnosis',
   'text':'On the planet Zeta, an object of mass 60 kg has a weight of 138 N.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the gravitational field strength on Zeta.','marks':2,'space':28},
            {'label':'(b)','text':'State what the same object would weigh on Earth.','marks':1,'space':20},
            {'label':'(c)','text':'State the mass of the object on Zeta.','marks':1,'space':18}]},
  {'text':'A student draws a force diagram for a car driving along a straight, flat road at a steady 20 m/s. '
          'He draws one arrow only: a long arrow pointing forwards, labelled &ldquo;driving force&rdquo;.','marks':4,
   'parts':[{'label':'(a)','text':'Name two forces he has left out, and state the direction of each.','marks':2,'space':26},
            {'label':'(b)','text':'Explain what is wrong with drawing the forward arrow longer than any backward arrow '
                                 'for this particular car.','marks':2,'space':30}]},
  {'text':'A student has written two answers, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;The box has a mass of 20 kg, so its weight is 20 kg.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;The trolley is moving at a steady speed, so there must be a resultant force '
          'pushing it forwards.&rdquo;<br/>'
          'For each one, explain the mistake and give the correct statement.','marks':4,'space':52},
 ]}

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':2,'lines':['A force is a push or a pull on an object (from an interaction with another object) <b>[1]</b>',
    'Force is measured in <b>newtons (N)</b> <b>[1]</b>'],
   'note':'Reject "energy" and "power" outright. They are different quantities with different units, and this is the one place on the paper where the definition alone is worth a mark.'},
  {'n':'2','marks':3,'lines':['(a) <b>air resistance</b> (accept drag)','(b) <b>weight</b> (accept gravity / gravitational force)',
    '(c) <b>tension</b>'],
   'note':'In (b), "gravity" alone is acceptable at this level, but "weight" is the term the syllabus uses and the one to encourage.'},
  {'n':'3','marks':3,'lines':['(a) <b>contact</b>','(b) <b>non-contact</b>','(c) <b>contact</b>'],
   'note':'Upthrust is the one that gets guessed wrong. The liquid or gas is touching the object, so it is a contact force.'},
  {'n':'4','marks':3,'lines':['Change its <b>speed</b> (speed it up or slow it down) <b>[1]</b>',
    'Change its <b>direction</b> <b>[1]</b>','Change its <b>shape</b> <b>[1]</b>'],
   'note':'"Make it move" and "make it stop" are the same mark, both being a change of speed. Award one for that pair, not two.'},
  {'n':'5','marks':4,'lines':['(a) 5 &times; 10 = <b>50 N</b>','(b) 12 &times; 10 = <b>120 N</b>',
    '(c) W = m &times; g = 0.5 &times; 10 <b>[1]</b> = <b>5 N</b> <b>[1]</b>'],
   'note':'Any answer given in kilograms scores zero for that part, however good the arithmetic. The unit is the whole point of the section.'},
  {'n':'6','marks':3,'lines':['(a) 300 &divide; 10 = <b>30 kg</b>','(b) 45 &divide; 10 = <b>4.5 kg</b>',
    '(c) 7 &divide; 10 = <b>0.7 kg</b>'],
   'note':'Multiplying instead of dividing gives 3000 kg, 450 kg and 70 kg. If all three are ten times too big it is one error repeated, not three — award the method once if it is shown.'},
  {'n':'7','marks':3,'lines':['Mass is the amount of matter in an object, measured in <b>kilograms (kg)</b> <b>[1]</b>',
    'Weight is the force of gravity acting on that object, measured in <b>newtons (N)</b> <b>[1]</b>',
    'Mass is the same everywhere; weight depends on the gravitational field strength where the object is <b>[1]</b>'],
   'note':'The third mark is the one usually missing. A comparison of the two units alone is worth two, not three.'},
  {'n':'8','marks':4,'lines':['(a) 30 &minus; 20 = <b>10 N to the right</b>','(b) 45 &minus; 45 = <b>0 N</b>',
    '(c) Same direction, so add: 12 + 30 <b>[1]</b> = <b>42 N to the left</b> <b>[1]</b>'],
   'note':'(c) is the trap: two forces, so the instinct is to subtract. They point the same way, so they add. Withhold the final mark from any answer with no direction on it.'},
  {'n':'9','marks':3,'lines':['(a) <b>0 N</b> <b>[1]</b>','(b) It stays <b>stationary</b> (it does not move) <b>[1]</b>',
    '(c) <b>Balanced</b> forces <b>[1]</b>']},
  {'n':'10','marks':2,'lines':['It carries on at a <b>constant speed in a straight line</b> <b>[1]</b>',
    'because the forces are balanced, so the resultant force is zero and nothing about its motion changes <b>[1]</b>'],
   'note':'"It stops" is the commonest wrong answer and scores nothing. A zero resultant maintains the motion; it does not remove it.'},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':4,'lines':['Arrow pointing <b>down</b>, labelled weight (accept a value in N) <b>[1]</b>',
    'Arrow pointing <b>up</b>, labelled normal contact force / reaction / push from the floor <b>[1]</b>',
    'The two arrows drawn the <b>same length</b> <b>[1]</b>',
    'because the crate is stationary, so the forces are balanced and the resultant is zero <b>[1]</b>'],
   'note':'Arrows drawn as plain lines with no arrowhead lose the first two marks. Worth saying out loud once, because it repeats on every forces paper.'},
  {'n':'2','marks':3,'lines':['A force has a <b>size</b> (magnitude) <b>[1]</b>','and a <b>direction</b> <b>[1]</b>',
    'The length of the arrow shows the size and the arrowhead shows the direction <b>[1]</b>'],
   'note':'"So you can see it" and "to make the diagram clear" score nothing. The mark scheme wants the word direction.'},
  {'n':'3','marks':3,'lines':['(a) <b>newtons (N)</b>','(b) the <b>spring</b>','(c) The stretch (extension) also <b>doubles</b>'],
   'note':'(c) is a reasoning mark, not a recall one. Accept "the extension doubles"; do not accept "the whole spring doubles in length".'},
  {'n':'4','marks':5,'lines':['(a) Same direction, so add: 80 + 50 = <b>130 N to the right</b>',
    '(b) 90 &minus; 35 = <b>55 N to the left</b>','(c) <b>0 N</b> (balanced)',
    '(d) Right: 6 + 4 = 10 N. Left: 14 N <b>[1]</b>. 14 &minus; 10 = <b>4 N to the left</b> <b>[1]</b>'],
   'note':'(d) is the question of the paper. Two arrows point right and only one points left, and the single one still wins. Counting arrows is the error it is built to catch.'},
  {'n':'5','marks':4,'lines':['(a) <b>4500 N</b> <b>[1]</b>',
    '(b) The speed is steady, so the resultant force is zero and the backward force must equal the driving force <b>[1]</b>',
    '(c) 5200 &minus; 4500 = <b>700 N forwards</b> <b>[1]</b>; the forces are now unbalanced, so the lorry <b>speeds up</b> <b>[1]</b>'],
   'note':'In (a) any answer other than 4500 N means the student has not accepted that steady speed implies balance. Read (b) before deciding how much of the topic has landed.'},
  {'n':'6','marks':3,'lines':['Balanced forces have a resultant of zero; unbalanced forces have a resultant that is not zero <b>[1]</b>',
    'Balanced: the object keeps moving at the <b>same steady speed in a straight line</b> <b>[1]</b>',
    'Unbalanced: the object changes speed or changes direction <b>[1]</b>'],
   'note':'An answer saying balanced forces make a moving object stop is worth one mark at most. This is the single most valuable correction on the paper.'},
  {'n':'7','marks':4,'lines':['(a) <b>Opposite to the direction of motion</b> <b>[1]</b>',
    '(b) Any two: walking without slipping, brakes on a car or bicycle, tyres gripping the road, holding a pen, '
    'a nail staying in a wall, striking a match <b>[1] [1]</b>',
    '(c) Any one: it wears moving parts down, it wastes energy as heat, it slows machinery, it makes engines need oil <b>[1]</b>']},
  {'n':'8','marks':4,'lines':['(a) <b>Friction</b> (between tyres and road, or in the bearings) <b>[1]</b>; <b>air resistance</b> (drag) <b>[1]</b>',
    '(b) With no forward force from pedalling, only the backward forces are left <b>[1]</b>',
    'so the resultant force acts backwards, opposite to her motion, which is unbalanced and slows her down <b>[1]</b>'],
   'note':'"She runs out of energy" is common and scores nothing here. The question asks for a force explanation and the mark scheme wants the word resultant.'},
 ]},

 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) W = 250 &times; 3.7 <b>[1]</b> = <b>925 N</b> <b>[1]</b>',
    '(b) m = 32 &divide; 1.6 <b>[1]</b> = <b>20 kg</b> <b>[1]</b>','(c) 20 &times; 10 = <b>200 N</b> <b>[1]</b>'],
   'note':'(b) has to be done by dividing. Multiplying gives 51.2 kg, which would make the object heavier on the Moon than it started — an absurdity the student can spot without knowing the answer.'},
  {'n':'2','marks':4,'lines':['Error 1: weight is a <b>force</b>, not a mass — they are different quantities <b>[1]</b>',
    'Error 2: the unit should be <b>newtons</b>, not kilograms <b>[1]</b>',
    'W = 45 &times; 10 <b>[1]</b>','= <b>450 N</b> <b>[1]</b>'],
   'note':'The two error marks must be genuinely separate points. "It should be in newtons" written twice in different words is one mark.'},
  {'n':'3','marks':5,'lines':['(a) 15 000 &minus; 12 000 <b>[1]</b> = <b>3000 N upwards</b> <b>[1]</b>',
    '(b) 900 &minus; 900 = <b>0 N</b> <b>[1]</b>',
    '(c) Vertically the forces are unbalanced, so the balloon <b>rises, speeding up</b> <b>[1]</b>; '
    'horizontally the forces are balanced, so it does not speed up or slow down sideways <b>[1]</b>'],
   'note':'The point of this question is that vertical and horizontal are settled separately. Any answer that adds all four numbers into one sum has missed it entirely.'},
  {'n':'4','marks':4,'lines':['(a) <b>85 N</b> <b>[1]</b>, because the box moves at a steady speed, so the resultant is zero '
    'and friction must equal the pull <b>[1]</b>',
    '(b) 130 &minus; 85 <b>[1]</b> = <b>45 N in the direction of the pull</b>, so the box <b>speeds up</b> <b>[1]</b>'],
   'note':'In (b) a common answer is 130 N, from assuming friction disappeared when the pull increased. Friction was never removed — only outmatched.'},
  {'n':'5','marks':4,'lines':['(a) Left total = 9 + 12 = 21 N <b>[1]</b>; 26 &minus; 21 = <b>5 N to the right</b> <b>[1]</b>',
    '(b) <b>5 N to the left</b> <b>[1] [1]</b>'],
   'note':'"Constant velocity" is doing the work in (b): it means the resultant must be zero, so the new force cancels the 5 N exactly. A student answering 26 N has cancelled the wrong thing.'},
  {'n':'6','marks':4,'lines':['(a) W = 80 &times; 10 = <b>800 N</b> <b>[1]</b>',
    '(b) 800 &minus; 150 <b>[1]</b> = <b>650 N downwards</b> <b>[1]</b>',
    '(c) <b>800 N</b> <b>[1]</b>'],
   'note':'(c) needs no arithmetic at all: constant speed means zero resultant, so air resistance equals weight. If a student calculates here, the idea has not landed.'},
  {'n':'7','marks':4,'lines':['There is no air in space, so no air resistance, and nothing is touching it, so no friction <b>[1]</b>',
    'With no opposing forces there is no resultant force acting on it <b>[1]</b>',
    'A zero resultant force means nothing about its motion changes <b>[1]</b>',
    'A force is needed to <b>change</b> motion, not to maintain it, so it keeps moving at the same steady speed <b>[1]</b>'],
   'note':'This is the whole topic in one question. Any answer containing "it needs a force to keep going" has the physics backwards, whatever else it says.'},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) W = 40 &times; 10 = <b>400 N</b> <b>[1]</b>',
    '(b) <b>400 N upwards</b> <b>[1]</b>, because the crate does not move vertically, so the vertical forces must be balanced <b>[1]</b>',
    '(c) 260 &minus; 100 <b>[1]</b> = <b>160 N in the direction of the pull</b>, so the crate <b>speeds up</b> <b>[1]</b>'],
   'note':'The 400 N must not appear anywhere in (c). Dragging the weight into the horizontal sum is the standard error in four-force questions and is worth marking explicitly.'},
  {'n':'2','marks':5,'lines':['(a) 190 &minus; 145 <b>[1]</b> = <b>45 N to the west</b> <b>[1]</b>',
    '(b) The sledge would move west, so friction acts <b>east</b> <b>[1]</b>; 45 &minus; 15 = <b>30 N to the west</b> <b>[1]</b>',
    '(c) The forces are unbalanced, so the sledge <b>speeds up towards the west</b> <b>[1]</b>'],
   'note':'Friction is set by the direction of motion, not by the stronger child. An answer putting friction west has stopped thinking about what friction is for.'},
  {'n':'3','marks':4,'lines':['(a) W = 60 &times; 10 = <b>600 N</b> <b>[1]</b>',
    '(b) <b>600 N</b> <b>[1]</b>; the lift moves at a constant speed, so the resultant force on the passenger is zero <b>[1]</b>; '
    'so the upward push from the floor must exactly equal the 600 N weight <b>[1]</b>'],
   'note':'Moving upwards tempts students into making the upward force bigger. Constant speed rules that out — the direction of travel is irrelevant to the balance.'},
  {'n':'4','marks':4,'lines':['(a) 1100 &minus; 750 <b>[1]</b> = <b>350 N upwards</b> <b>[1]</b>',
    '(b) A resultant force changes motion rather than causing it <b>[1]</b>; the upward resultant is slowing her down, '
    'but she was already moving downwards and carries on doing so, just more slowly <b>[1]</b>'],
   'note':'This separates students who have accepted that force and direction of travel are independent from those who have not. Expect it to be the least-answered question on the paper.'},
  {'n':'5','marks':4,'lines':['(a) g = W &divide; m = 138 &divide; 60 <b>[1]</b> = <b>2.3 N/kg</b> <b>[1]</b>',
    '(b) 60 &times; 10 = <b>600 N</b> <b>[1]</b>','(c) <b>60 kg</b> <b>[1]</b>'],
   'note':'(c) is a one-word answer that a surprising number of students calculate. Mass does not change with location, which is the whole reason the part is there.'},
  {'n':'6','marks':4,'lines':['(a) Any two, with directions: <b>air resistance / friction backwards</b>, '
    '<b>weight downwards</b>, <b>normal contact force upwards</b> <b>[1] [1]</b>',
    '(b) The car travels at a steady speed, so the forces must be balanced <b>[1]</b>; '
    'the forward and backward arrows must therefore be drawn the <b>same length</b> <b>[1]</b>'],
   'note':'Award (a) only where a direction is given. A named force with no direction is half a force arrow and is worth nothing on a diagram question.'},
  {'n':'7','marks':4,'lines':[
    '(i) The mistake: weight is a force, so it cannot be measured in kilograms <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;W = 20 &times; 10 = <b>200 N</b> <b>[1]</b>',
    '(ii) The mistake: a steady speed means the forces are <b>balanced</b> and the resultant force is <b>zero</b> <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;A resultant force is needed to <b>change</b> motion, not to maintain it, '
    'so no forward resultant is required <b>[1]</b>'],
   'note':'These are the two most common wrong sentences in the whole topic. If a student can correct both here but not on Paper A question 10, the problem is confidence rather than knowledge.'},
 ]},
]

files = []
for spec, code in [(A,'a'), (B,'b'), (C,'c'), (D,'d')]:
    t = sum(q.get('marks',0) for q in spec['questions'])
    assert t == 30, (spec['title'], t)
    for q in spec['questions']:
        if 'parts' in q:
            pt = sum(p['marks'] for p in q['parts'])
            assert pt == q['marks'], (spec['title'], q['text'][:40], pt, q['marks'])
    p = os.path.join(OUT, 'physics-forces-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)
for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)
for spec, sc in [(A,SCHEMES[0]), (B,SCHEMES[1]), (C,SCHEMES[2]), (D,SCHEMES[3])]:
    assert len(spec['questions']) == len(sc['questions']), (spec['title'], len(spec['questions']), len(sc['questions']))
    for i,(q,s) in enumerate(zip(spec['questions'], sc['questions'])):
        assert q['marks'] == s['marks'], (spec['title'], i+1, q['marks'], s['marks'])
p = os.path.join(OUT, 'physics-forces-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Award method marks for a correct formula and a '
             'correct substitution even when the arithmetic fails. Almost every mark lost on this topic goes one of '
             'four ways: a weight written in kilograms, a resultant given with no direction, opposing forces added '
             'instead of subtracted, and a steady speed treated as evidence of a forward resultant. The notes under '
             'each answer flag the specific mistake that question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
