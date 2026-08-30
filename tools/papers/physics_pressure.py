#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Physics · Grade 7 · Pressure'
TOPIC = 'Pressure in Solids and Liquids'

BASE = [
 'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
 'A calculator is allowed, but every number on this paper is designed to work without one.',
 'Every answer must carry a <b>unit</b>. An answer with no unit does not score the final mark.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + [
 'Reminder: <b>pressure = force &divide; area</b>, and in a liquid <b>pressure = density &times; g &times; depth</b>.',
 'Take <b>g = 10 N/kg</b>, and remember that <b>1 m&#178; = 10 000 cm&#178;</b>.']
INSTR_HARD = BASE + [
 'No formulae and no conversion factors are given on this paper.',
 'Several questions describe situations you may not have seen before — apply the ideas you already have.',
 'Take <b>g = 10 N/kg</b> throughout, and give pressures in pascals unless told otherwise.']

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — the equation',
   'text':'Write down the equation linking pressure, force and area, and state the unit of pressure.',
   'marks':2,'space':24},
  {'text':'Calculate the pressure in each case.','marks':4,
   'parts':[{'label':'(a)','text':'A force of 200 N acting on an area of 4 m&#178;.','marks':1,'space':18},
            {'label':'(b)','text':'A force of 60 N acting on an area of 0.2 m&#178;.','marks':1,'space':18},
            {'label':'(c)','text':'A force of 750 N acting on an area of 0.05 m&#178;.','marks':2,'space':24}]},
  {'text':'Calculate the force.','marks':2,
   'parts':[{'label':'(a)','text':'A pressure of 500 Pa acting on an area of 6 m&#178;.','marks':1,'space':18},
            {'label':'(b)','text':'A pressure of 20 000 Pa acting on an area of 0.02 m&#178;.','marks':1,'space':18}]},
  {'text':'Calculate the area.','marks':2,
   'parts':[{'label':'(a)','text':'A force of 600 N producing a pressure of 300 Pa.','marks':1,'space':18},
            {'label':'(b)','text':'A force of 1500 N producing a pressure of 30 000 Pa.','marks':1,'space':18}]},
  {'section':'Section 2 — square centimetres',
   'text':'Convert each area into square metres.','marks':3,
   'parts':[{'label':'(a)','text':'20 cm&#178;','marks':1,'space':14},
            {'label':'(b)','text':'400 cm&#178;','marks':1,'space':14},
            {'label':'(c)','text':'2.5 cm&#178;','marks':1,'space':14}]},
  {'text':'A force of 60 N acts on an area of 20 cm&#178;. Calculate the pressure, in pascals.',
   'marks':3,'space':32},
  {'text':'A box of weight 480 N rests on the floor. Its base measures 0.4 m by 0.5 m. '
          'Calculate the pressure it exerts on the floor.','marks':3,'space':34},
  {'section':'Section 3 — spreading and concentrating',
   'text':'Explain why a tractor is fitted with very wide tyres.','marks':2,'space':26},
  {'text':'A drawing pin has a sharp point at one end and a wide flat disc at the other. '
          'Explain why each end is that shape, referring to force and area.','marks':3,'space':36},
  {'text':'Calculate the pressure due to the water at a depth of 8 m in a lake. '
          'The density of the water is 1000 kg/m&#179;.','marks':3,'space':32},
  {'text':'State <b>two</b> quantities that the pressure at a point in a liquid depends on, '
          'and <b>one</b> quantity that it does not depend on.','marks':3,'space':32},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — real contact areas',
   'text':'Aarav weighs 600 N. Standing on both feet, his shoes touch the floor over a total area of 0.03 m&#178;.',
   'marks':5,
   'parts':[{'label':'(a)','text':'Calculate the pressure he exerts on the floor.','marks':2,'space':26},
            {'label':'(b)','text':'He lifts one foot. Calculate the new pressure on the floor.','marks':2,'space':26},
            {'label':'(c)','text':'State what happened to the force he exerts on the floor.','marks':1,'space':18}]},
  {'text':'A metal crate of weight 900 N stands on four small feet. Each foot has an area of 25 cm&#178;.',
   'marks':5,
   'parts':[{'label':'(a)','text':'Calculate the total contact area, in m&#178;.','marks':2,'space':26},
            {'label':'(b)','text':'Calculate the pressure on the floor.','marks':2,'space':26},
            {'label':'(c)','text':'A board of area 0.3 m&#178; is slid underneath. Calculate the new pressure.','marks':1,'space':22}]},
  {'section':'Section 2 — pressure in liquids',
   'text':'Calculate the pressure due to the liquid in each case.','marks':4,
   'parts':[{'label':'(a)','text':'Water of density 1000 kg/m&#179; at a depth of 3 m.','marks':2,'space':26},
            {'label':'(b)','text':'Seawater of density 1030 kg/m&#179; at a depth of 20 m.','marks':2,'space':26}]},
  {'text':'A tall narrow jar and a wide tank are both filled with water to a depth of 0.5 m. '
          'A student says the pressure at the bottom of the wide tank must be greater, because it holds '
          'more water. Explain why he is wrong, and calculate the pressure at the bottom of each.',
   'marks':4,'space':44},
  {'text':'Explain why a dam is built much thicker at the bottom than at the top.','marks':3,'space':34},
  {'section':'Section 3 — in every direction',
   'text':'A sealed can is filled with water. Three small holes are made in its side, at different heights. '
          'Describe what you would see, and explain both features of what you have described.',
   'marks':4,'space':46},
  {'text':'State what is meant by <b>atmospheric pressure</b>, and explain why you do not normally notice it.',
   'marks':3,'space':34},
  {'text':'A diver is 12 m below the surface of a freshwater lake. Taking atmospheric pressure as '
          '100 000 Pa, calculate the total pressure acting on her.','marks':2,'space':28},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — the same weight, a different face',
   'text':'A rectangular concrete block has a weight of 2400 N.','marks':5,
   'parts':[{'label':'(a)','text':'It rests on a face measuring 1.5 m by 0.8 m. Calculate the pressure on the ground.','marks':2,'space':28},
            {'label':'(b)','text':'It is stood on a face measuring 0.8 m by 0.5 m instead. Calculate the new pressure.','marks':2,'space':28},
            {'label':'(c)','text':'State the factor by which the pressure changed, and say why.','marks':1,'space':22}]},
  {'text':'A kitchen knife is pressed onto a vegetable with a force of 45 N. '
          'The sharpened edge touches an area of 0.15 cm&#178;.','marks':5,
   'parts':[{'label':'(a)','text':'Convert the contact area into square metres.','marks':2,'space':24},
            {'label':'(b)','text':'Calculate the pressure under the edge.','marks':2,'space':26},
            {'label':'(c)','text':'The knife goes blunt and now touches 1.5 cm&#178;. State the new pressure.','marks':1,'space':22}]},
  {'section':'Section 2 — under the sea',
   'text':'A submarine has a window of area 0.05 m&#178;. It dives to a depth of 60 m in seawater of '
          'density 1030 kg/m&#179;. Atmospheric pressure is 100 000 Pa.','marks':6,
   'parts':[{'label':'(a)','text':'Calculate the pressure due to the seawater alone.','marks':2,'space':26},
            {'label':'(b)','text':'Calculate the total pressure on the outside of the window.','marks':2,'space':24},
            {'label':'(c)','text':'Calculate the force the sea exerts on the window.','marks':2,'space':28}]},
  {'text':'Point X is 4 m below the surface of a freshwater lake and point Y is 12 m below it. '
          'The density of the water is 1000 kg/m&#179;.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the pressure due to the water at X and at Y.','marks':2,'space':28},
            {'label':'(b)','text':'Calculate the difference in pressure between the two points.','marks':1,'space':20},
            {'label':'(c)','text':'The lake is drained and replaced by a swimming pool with the same two depths '
                                 'but one tenth of the surface area. State and explain what happens to your answers.',
             'marks':2,'space':30}]},
  {'section':'Section 3 — machines that multiply force',
   'text':'A hydraulic jack has a small piston of area 0.0004 m&#178; and a large piston of area 0.03 m&#178;. '
          'A force of 20 N is applied to the small piston.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the pressure produced in the oil.','marks':2,'space':26},
            {'label':'(b)','text':'Calculate the force produced at the large piston.','marks':2,'space':26},
            {'label':'(c)','text':'State the factor by which the force has been multiplied.','marks':1,'space':18}]},
  {'text':'Explain why the fluid inside a hydraulic system must be a liquid and not a gas.',
   'marks':4,'space':42},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — designing for pressure',
   'text':'An elephant of weight 40 000 N stands on four feet, each of area 0.1 m&#178;. '
          'A woman of weight 500 N stands on a single stiletto heel of area 0.0001 m&#178;.','marks':6,
   'parts':[{'label':'(a)','text':'Calculate the pressure the elephant exerts on the ground.','marks':2,'space':28},
            {'label':'(b)','text':'Calculate the pressure under the heel.','marks':2,'space':26},
            {'label':'(c)','text':'Explain how the far lighter woman can exert the far greater pressure.','marks':2,'space':30}]},
  {'text':'A sledge is to carry a load of 1800 N across snow. The snow gives way if the pressure on it '
          'exceeds 4000 Pa.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the smallest total runner area that will keep the sledge on top of the snow.',
             'marks':3,'space':32},
            {'label':'(b)','text':'The sledge has two runners of equal area. State the area of each.','marks':1,'space':18},
            {'label':'(c)','text':'The load is increased to 2250 N with the same runners. Show that the sledge now sinks.',
             'marks':1,'space':24}]},
  {'section':'Section 2 — liquids that ignore the container',
   'text':'A tank is narrow at the top and much wider at the bottom. It is filled with water of density '
          '1000 kg/m&#179; to a depth of 2.5 m.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the pressure due to the water at the bottom of the tank.','marks':2,'space':26},
            {'label':'(b)','text':'The tank is replaced by a straight-sided tank half as wide, filled to the same depth. '
                                 'State the pressure at the bottom now, and justify your answer.','marks':2,'space':30},
            {'label':'(c)','text':'State the directions in which this pressure acts.','marks':1,'space':18}]},
  {'text':'A glass tube is filled with mercury, of density 13 600 kg/m&#179;.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the pressure produced by a column of mercury 0.75 m tall.','marks':2,'space':26},
            {'label':'(b)','text':'Atmospheric pressure is about 100 000 Pa. Explain why a mercury column of roughly '
                                 'this height is used to measure it.','marks':2,'space':30}]},
  {'section':'Section 3 — judgement',
   'text':'Two identical tanks are filled to a depth of 5 m, one with water (1000 kg/m&#179;) and one with '
          'cooking oil (800 kg/m&#179;).','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the pressure at the bottom of each tank.','marks':2,'space':28},
            {'label':'(b)','text':'Calculate the depth of oil that would give the same pressure as 5 m of water.',
             'marks':2,'space':28}]},
  {'text':'A student has written two answers, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;A force of 60 N on an area of 20 cm&#178; gives a pressure of 3 Pa.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;Two tanks are both filled with water to a depth of 2 m. The pressure at the bottom of '
          'the wide tank is greater than at the bottom of the narrow one, because the wide tank holds more water.&rdquo;<br/>'
          'For each one, explain the mistake and give the correct answer.','marks':6,'space':60},
 ]}

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':2,'lines':['pressure = force &divide; area <b>[1]</b>',
    'Unit: the <b>pascal (Pa)</b>, which is the same as N/m&#178; <b>[1]</b>'],
   'note':'N/m without the square is not the unit of pressure and scores nothing here.'},
  {'n':'2','marks':4,'lines':['(a) 200 &divide; 4 = <b>50 Pa</b>','(b) 60 &divide; 0.2 = <b>300 Pa</b>',
    '(c) 750 &divide; 0.05 <b>[1]</b> = <b>15 000 Pa</b> <b>[1]</b>'],
   'note':'Multiplying instead of dividing gives 800 in (a). Check the direction of the formula before the arithmetic.'},
  {'n':'3','marks':2,'lines':['(a) F = p &times; A = 500 &times; 6 = <b>3000 N</b>',
    '(b) 20 000 &times; 0.02 = <b>400 N</b>']},
  {'n':'4','marks':2,'lines':['(a) A = F &divide; p = 600 &divide; 300 = <b>2 m&#178;</b>',
    '(b) 1500 &divide; 30 000 = <b>0.05 m&#178;</b>'],
   'note':'The unit here is m&#178;, not Pa. Carrying the wrong unit across from the previous question is common.'},
  {'n':'5','marks':3,'lines':['(a) 20 &divide; 10 000 = <b>0.002 m&#178;</b>','(b) 400 &divide; 10 000 = <b>0.04 m&#178;</b>',
    '(c) 2.5 &divide; 10 000 = <b>0.00025 m&#178;</b>'],
   'note':'Dividing by 100 instead of 10 000 is the error to look for. It gives answers a hundred times too big every time.'},
  {'n':'6','marks':3,'lines':['20 cm&#178; = 0.002 m&#178; <b>[1]</b>','60 &divide; 0.002 <b>[1]</b>',
    '= <b>30 000 Pa</b> <b>[1]</b>'],
   'note':'60 &divide; 20 = 3 scores nothing beyond the substitution mark. That answer is newtons per square centimetre, and it is the single most common error in this topic.'},
  {'n':'7','marks':3,'lines':['Area = 0.4 &times; 0.5 = 0.2 m&#178; <b>[1]</b>','480 &divide; 0.2 <b>[1]</b>',
    '= <b>2400 Pa</b> <b>[1]</b>'],
   'note':'The area line is worth a mark on its own. A candidate who writes only the final number risks two of the three marks.'},
  {'n':'8','marks':2,'lines':['Wide tyres give a larger contact area with the ground <b>[1]</b>',
    'Pressure = force &divide; area, so for the same weight a larger area gives a smaller pressure and the tractor does not sink into soft soil <b>[1]</b>'],
   'note':'&ldquo;So it does not sink&rdquo; alone is one mark. The second needs area and pressure named and linked.'},
  {'n':'9','marks':3,'lines':['The point has a very small area, so the same force gives a very large pressure and the pin goes into the board <b>[1]</b> <b>[1]</b>',
    'The disc has a large area, so the pressure on the thumb is small and it does not hurt <b>[1]</b>'],
   'note':'One force, two areas, two very different pressures. A candidate who says the point is &ldquo;sharper so stronger&rdquo; has not used the physics.'},
  {'n':'10','marks':3,'lines':['p = &rho; &times; g &times; h <b>[1]</b>','= 1000 &times; 10 &times; 8 <b>[1]</b>',
    '= <b>80 000 Pa</b> (80 kPa) <b>[1]</b>']},
  {'n':'11','marks':3,'lines':['Depends on: the <b>depth</b> below the surface <b>[1]</b>',
    'Depends on: the <b>density</b> of the liquid (accept g) <b>[1]</b>',
    'Does not depend on: the volume, the width, the shape of the container or the total amount of liquid <b>[1]</b>'],
   'note':'This question is the written form of the trap tested in Papers B and D. Anything naming volume or shape as a factor loses the third mark.'},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) 600 &divide; 0.03 <b>[1]</b> = <b>20 000 Pa</b> <b>[1]</b>',
    '(b) One foot is 0.015 m&#178;, so 600 &divide; 0.015 <b>[1]</b> = <b>40 000 Pa</b> <b>[1]</b>',
    '(c) The force is <b>unchanged</b> at 600 N — it is still his whole weight <b>[1]</b>'],
   'note':'The commonest error in (b) is halving the force as well as the area, giving 20 000 Pa again. Lifting a foot does not make him lighter.'},
  {'n':'2','marks':5,'lines':['(a) 4 &times; 25 = 100 cm&#178; <b>[1]</b>; 100 &divide; 10 000 = <b>0.01 m&#178;</b> <b>[1]</b>',
    '(b) 900 &divide; 0.01 <b>[1]</b> = <b>90 000 Pa</b> <b>[1]</b>',
    '(c) 900 &divide; 0.3 = <b>3000 Pa</b> <b>[1]</b>'],
   'note':'Using one foot instead of four gives 360 000 Pa. The board reduces the pressure by a factor of 30 while removing no force at all — worth pointing out when marking.'},
  {'n':'3','marks':4,'lines':['(a) 1000 &times; 10 &times; 3 <b>[1]</b> = <b>30 000 Pa</b> <b>[1]</b>',
    '(b) 1030 &times; 10 &times; 20 <b>[1]</b> = <b>206 000 Pa</b> <b>[1]</b>'],
   'note':'Rounding 1030 to 1000 gives 200 000 and loses the accuracy mark. The question supplied the exact density deliberately.'},
  {'n':'4','marks':4,'lines':['Pressure in a liquid depends only on depth, density and g <b>[1]</b>',
    'p = &rho;gh contains no volume, width or shape, so the amount of water is irrelevant <b>[1]</b>',
    '1000 &times; 10 &times; 0.5 <b>[1]</b>','= <b>5000 Pa</b> in <b>both</b> containers <b>[1]</b>'],
   'note':'The fourth mark requires the word &ldquo;both&rdquo;, or two identical answers. Calculating one pressure and stopping scores three.'},
  {'n':'5','marks':3,'lines':['Pressure in a liquid increases with depth <b>[1]</b>',
    'so the water pushes hardest at the base of the dam and hardly at all at the top <b>[1]</b>',
    'The wall is made thicker there so it is strong enough to withstand the greater pressure <b>[1]</b>'],
   'note':'Describing the shape is not explaining it. Without the words &ldquo;increases with depth&rdquo; this caps at one mark.'},
  {'n':'6','marks':4,'lines':['Water squirts out <b>sideways</b> from all three holes <b>[1]</b>',
    'because pressure in a liquid acts equally in all directions, not only downwards <b>[1]</b>',
    'The <b>lowest</b> jet travels furthest <b>[1]</b>','because the pressure is greater at greater depth <b>[1]</b>'],
   'note':'Two separate ideas, two marks each. Candidates usually get the depth half and miss the all-directions half entirely.'},
  {'n':'7','marks':3,'lines':['Atmospheric pressure is the pressure exerted by the weight of the air above a surface <b>[1]</b>',
    'It is about 100 000 Pa (100 kPa) at sea level <b>[1]</b>',
    'It is not noticed because it acts equally in all directions and the pressure inside the body pushes back equally hard <b>[1]</b>']},
  {'n':'8','marks':2,'lines':['Water pressure = 1000 &times; 10 &times; 12 = 120 000 Pa <b>[1]</b>',
    'Total = 120 000 + 100 000 = <b>220 000 Pa</b> <b>[1]</b>'],
   'note':'Omitting the atmosphere is the error the question is built to catch. The word &ldquo;total&rdquo; is the signal to add it.'},
 ]},

 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) Area = 1.5 &times; 0.8 = 1.2 m&#178;; 2400 &divide; 1.2 <b>[1]</b> = <b>2000 Pa</b> <b>[1]</b>',
    '(b) Area = 0.8 &times; 0.5 = 0.4 m&#178;; 2400 &divide; 0.4 <b>[1]</b> = <b>6000 Pa</b> <b>[1]</b>',
    '(c) The pressure is <b>three times</b> greater, because the area is three times smaller while the weight is unchanged <b>[1]</b>'],
   'note':'The block did not get heavier. Any answer in (c) that refers to a change in force is wrong even if the factor of 3 is stated.'},
  {'n':'2','marks':5,'lines':['(a) 0.15 &divide; 10 000 <b>[1]</b> = <b>0.000015 m&#178;</b> <b>[1]</b>',
    '(b) 45 &divide; 0.000015 <b>[1]</b> = <b>3 000 000 Pa</b> (3 MPa) <b>[1]</b>',
    '(c) Ten times the area, so a tenth of the pressure: <b>300 000 Pa</b> <b>[1]</b>'],
   'note':'A sharp knife is not a stronger knife. If a candidate says the blunt knife needs more force, they have inverted the whole idea — award (c) only for 300 000 Pa.'},
  {'n':'3','marks':6,'lines':['(a) 1030 &times; 10 &times; 60 <b>[1]</b> = <b>618 000 Pa</b> <b>[1]</b>',
    '(b) 618 000 + 100 000 <b>[1]</b> = <b>718 000 Pa</b> <b>[1]</b>',
    '(c) F = p &times; A = 718 000 &times; 0.05 <b>[1]</b> = <b>35 900 N</b> <b>[1]</b>'],
   'note':'Using 618 000 in (c) gives 30 900 N and scores the method mark only. Follow-through applies if (b) itself was wrong.'},
  {'n':'4','marks':5,'lines':['(a) X: 1000 &times; 10 &times; 4 = <b>40 000 Pa</b> <b>[1]</b>; Y: 1000 &times; 10 &times; 12 = <b>120 000 Pa</b> <b>[1]</b>',
    '(b) 120 000 &minus; 40 000 = <b>80 000 Pa</b> <b>[1]</b>',
    '(c) <b>Nothing changes</b> <b>[1]</b> — pressure depends on depth and density only, and neither has changed; the surface area of the water does not appear in p = &rho;gh <b>[1]</b>'],
   'note':'Part (c) is the discriminator on this paper. Three times the depth gives three times the pressure, and a tenth of the area gives exactly the same pressure.'},
  {'n':'5','marks':5,'lines':['(a) 20 &divide; 0.0004 <b>[1]</b> = <b>50 000 Pa</b> <b>[1]</b>',
    '(b) The liquid transmits the same pressure to the large piston; F = 50 000 &times; 0.03 <b>[1]</b> = <b>1500 N</b> <b>[1]</b>',
    '(c) <b>&times; 75</b>, which is the ratio of the two areas <b>[1]</b>'],
   'note':'The idea being tested is that the pressure is the same at both pistons. A candidate who recalculates a different pressure for the large piston has missed the point of hydraulics.'},
  {'n':'6','marks':4,'lines':['A liquid is (almost) incompressible <b>[1]</b>',
    'so pressure applied at one piston is transmitted undiminished to the other <b>[1]</b>',
    'A gas would be compressed by the applied force <b>[1]</b>',
    'so the small piston would move without the large piston moving, and the force transmitted would be reduced <b>[1]</b>'],
   'note':'&ldquo;Gases are squashy&rdquo; earns the third mark only. The fourth needs the consequence for the machine.'},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':6,'lines':['(a) Total area = 4 &times; 0.1 = 0.4 m&#178; <b>[1]</b>; 40 000 &divide; 0.4 = <b>100 000 Pa</b> <b>[1]</b>',
    '(b) 500 &divide; 0.0001 <b>[1]</b> = <b>5 000 000 Pa</b> <b>[1]</b>',
    '(c) Pressure is force divided by area, not force alone <b>[1]</b>; she is 80 times lighter (500 N against 40 000 N), but her heel spreads that weight over 0.0001 m&#178; against the elephant&rsquo;s <b>total</b> 0.4 m&#178; — an area 4000 times smaller. 4000 &divide; 80 = 50, which is exactly the ratio of the two pressures <b>[1]</b>'],
   'note':'Using one foot rather than four in (a) gives 400 000 Pa. This question exists to break the belief that a bigger force always means a bigger pressure.'},
  {'n':'2','marks':5,'lines':['(a) A = F &divide; p <b>[1]</b> = 1800 &divide; 4000 <b>[1]</b> = <b>0.45 m&#178;</b> <b>[1]</b>',
    '(b) 0.45 &divide; 2 = <b>0.225 m&#178;</b> each <b>[1]</b>',
    '(c) 2250 &divide; 0.45 = 5000 Pa, which is above the 4000 Pa limit, so it sinks <b>[1]</b>'],
   'note':'Multiplying instead of dividing in (a) gives 7 200 000 m&#178;, an area larger than a football pitch. Any candidate who writes that without noticing has stopped checking whether answers are sensible.'},
  {'n':'3','marks':5,'lines':['(a) 1000 &times; 10 &times; 2.5 <b>[1]</b> = <b>25 000 Pa</b> <b>[1]</b>',
    '(b) Still <b>25 000 Pa</b> <b>[1]</b>; the depth and the density are unchanged, and p = &rho;gh contains no width, shape or volume term <b>[1]</b>',
    '(c) Equally in <b>all directions</b> — downwards, sideways and upwards <b>[1]</b>'],
   'note':'Halving the width halves the amount of water and changes nothing at all. If a candidate halves the pressure in (b), they are using volume as a factor.'},
  {'n':'4','marks':4,'lines':['(a) 13 600 &times; 10 &times; 0.75 <b>[1]</b> = <b>102 000 Pa</b> <b>[1]</b>',
    '(b) That is almost exactly atmospheric pressure <b>[1]</b>, so the air pressure will support a mercury column about this tall, and the height of the column can be read directly as a measure of the pressure <b>[1]</b>'],
   'note':'Mercury is used because it is dense: the same pressure would need about 10 m of water, which is why barometers are not made of water.'},
  {'n':'5','marks':4,'lines':['(a) Water: 1000 &times; 10 &times; 5 = <b>50 000 Pa</b> <b>[1]</b>; oil: 800 &times; 10 &times; 5 = <b>40 000 Pa</b> <b>[1]</b>',
    '(b) h = p &divide; (&rho;g) = 50 000 &divide; (800 &times; 10) <b>[1]</b> = <b>6.25 m</b> <b>[1]</b>'],
   'note':'The oil is 80% as dense, so it needs 1/0.8 = 1.25 times the depth. A candidate who answers 4 m has used the ratio upside down.'},
  {'n':'6','marks':6,'lines':[
    '(i) The mistake: dividing by an area in cm&#178; and calling the answer pascals <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;20 cm&#178; = 20 &divide; 10 000 = 0.002 m&#178; <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;p = 60 &divide; 0.002 = <b>30 000 Pa</b> <b>[1]</b>',
    '(ii) The mistake: pressure in a liquid does not depend on the amount of liquid <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;p = &rho;gh depends only on depth, density and g, and both tanks are 2 m deep <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Both are <b>20 000 Pa</b> <b>[1]</b>'],
   'note':'These are the two errors this whole topic is built around. A candidate who can diagnose both here will not make them under exam pressure — that is the purpose of the question.'},
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
    p = os.path.join(OUT, 'physics-pressure-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)
for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)
for spec, sc in zip([A,B,C,D], SCHEMES):
    assert len(spec['questions']) == len(sc['questions']), (sc['title'], len(spec['questions']), len(sc['questions']))
    for q, a in zip(spec['questions'], sc['questions']):
        assert q['marks'] == a['marks'], (sc['title'], a['n'], q['marks'], a['marks'])
p = os.path.join(OUT, 'physics-pressure-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Award method marks for a correct '
             'formula and a correct substitution even when the arithmetic fails. Almost every mark lost on '
             'this topic goes one of three ways: an area left in square centimetres and the answer still '
             'called pascals, the belief that a larger force must always mean a larger pressure, or the '
             'belief that pressure in a liquid depends on how much liquid there is. The notes under each '
             'answer flag the specific mistake that question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
