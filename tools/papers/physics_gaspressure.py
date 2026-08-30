#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Physics · Grade 7 · Gases'
TOPIC = 'Gas Pressure, the Particle Model and Diffusion'

BASE = [
 'Answer <b>every</b> question in the space provided. Show your working &mdash; method marks are awarded even when the final answer is wrong.',
 'A calculator is allowed, but every number on this paper is designed to work without one.',
 'Every numerical answer must carry a <b>unit</b>. An answer with no unit does not score the final mark.',
 'Explanations must be written <b>in terms of particles</b>. &ldquo;The particles get bigger&rdquo;, &ldquo;the particles expand&rdquo; and &ldquo;the particles push harder because they are squashed&rdquo; score nothing.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + ['Reminder: <b>pressure = force &divide; area</b>, measured in pascals (Pa), where 1 Pa = 1 N/m<super>2</super>. '
                    'Atmospheric pressure at sea level is about 100 000 Pa.']
INSTR_HARD = BASE + ['No formula is given on this paper, and no value for atmospheric pressure.',
                     'Several questions describe apparatus you may not have seen before &mdash; apply the ideas you already have.',
                     'Where an explanation is worth three marks or more, the mark scheme is looking for <b>collisions per unit area per second</b>, '
                     'and, wherever the temperature changes, for the force of each collision as well.']

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — pressure, force and area',
   'text':'State what is meant by <b>pressure</b>, write down the equation linking pressure, force and area, '
          'and give the unit of pressure.','marks':2,'space':28},
  {'text':'Calculate the pressure in each case.','marks':4,
   'parts':[{'label':'(a)','text':'A force of 240 N acting evenly over an area of 0.4 m<super>2</super>.','marks':1,'space':18},
            {'label':'(b)','text':'A force of 60 N acting evenly over an area of 0.02 m<super>2</super>.','marks':1,'space':18},
            {'label':'(c)','text':'A force of 1500 N acting evenly over an area of 0.05 m<super>2</super>.','marks':2,'space':24}]},
  {'text':'Calculate the force in each case.','marks':3,
   'parts':[{'label':'(a)','text':'A pressure of 200 Pa acting on an area of 3 m<super>2</super>.','marks':1,'space':18},
            {'label':'(b)','text':'A pressure of 100 000 Pa acting on an area of 0.02 m<super>2</super>.','marks':1,'space':18},
            {'label':'(c)','text':'A pressure of 50 000 Pa acting on an area of 0.4 m<super>2</super>.','marks':1,'space':18}]},
  {'text':'Describe, in terms of particles, what causes a gas to exert a pressure on the walls '
          'of its container.','marks':2,'space':30},
  {'section':'Section 2 — changing the pressure',
   'text':'A sealed gas syringe is pushed in until the volume of the trapped gas is halved. '
          'The temperature does not change. State what happens to the pressure, and explain why '
          'in terms of particles.','marks':3,'space':38},
  {'text':'A sealed metal tin of gas is heated. The tin does not change shape, so the volume stays the same. '
          'State what happens to the pressure and give the <b>two</b> separate reasons for it, '
          'in terms of particles.','marks':3,'space':38},
  {'text':'A gas is sealed in a cube-shaped box. Explain why the pressure on the lid, the base and '
          'all four sides is the same.','marks':2,'space':28},
  {'text':'More air is pumped into a bicycle tyre, which does not get any bigger and does not get warmer. '
          'Explain why the pressure inside rises.','marks':2,'space':28},
  {'section':'Section 3 — saying it correctly',
   'text':'A student writes: <i>&ldquo;When you squash a gas the particles are pushed closer together, '
          'so they push harder on the walls.&rdquo;</i> State what is wrong with this and write a '
          'correct explanation.','marks':3,'space':40},
  {'text':'A gas is heated from 27 &#176;C to 327 &#176;C inside a sealed container of fixed volume.','marks':2,
   'parts':[{'label':'(a)','text':'Convert both temperatures into kelvin.','marks':1,'space':16},
            {'label':'(b)','text':'State, with a reason, what happens to the pressure.','marks':1,'space':20}]},
  {'text':'State what is meant by <b>diffusion</b>.','marks':2,'space':28},
  {'text':'State two changes that would make a gas diffuse faster, and explain one of them '
          'in terms of particles.','marks':2,'space':30},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — the atmosphere',
   'text':'Explain why the atmosphere exerts a pressure on everything at the Earth&rsquo;s surface, '
          'and state its approximate value at sea level.','marks':3,'space':36},
  {'text':'Atmospheric pressure is 100 000 Pa.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the force the atmosphere exerts on the palm of a hand of area 0.01 m<super>2</super>.','marks':2,'space':24},
            {'label':'(b)','text':'A desk top measures 1.2 m by 0.6 m. Calculate the force of the atmosphere on it.','marks':1,'space':22},
            {'label':'(c)','text':'Explain why the desk is not crushed.','marks':1,'space':20}]},
  {'text':'A little water is boiled inside an empty drinks can until steam pours out of the opening. '
          'The can is then turned upside down and pushed into cold water. It is crushed almost at once.','marks':4,
   'parts':[{'label':'(a)','text':'State what happens to the steam inside the can when it meets the cold water.','marks':1,'space':18},
            {'label':'(b)','text':'State what happens to the pressure inside the can, and why.','marks':1,'space':22},
            {'label':'(c)','text':'Explain why the can is crushed. Your answer must use the word &ldquo;atmospheric&rdquo;.','marks':2,'space':28}]},
  {'text':'Explain what makes a drink rise up a straw when you drink through it. Your answer must not '
          'use the word &ldquo;suck&rdquo;.','marks':3,'space':36},
  {'section':'Section 2 — diffusion',
   'text':'State what is meant by diffusion, and explain why it happens even when nothing stirs '
          'or blows the gas.','marks':3,'space':36},
  {'text':'A bottle of nail varnish remover is opened at one end of a still, closed room. Two minutes later '
          'the smell can be detected six metres away.','marks':4,
   'parts':[{'label':'(a)','text':'Name the process that carried the smell across the room.','marks':1,'space':16},
            {'label':'(b)','text':'The particles move at hundreds of metres per second. Explain why the smell took two minutes and not a fraction of a second.','marks':2,'space':28},
            {'label':'(c)','text':'State one change that would make the smell arrive sooner, and give a reason.','marks':1,'space':22}]},
  {'text':'Explain why diffusion is much faster in a gas than in a liquid, and why it does not happen '
          'in a solid.','marks':3,'space':36},
  {'text':'A gas jar of dense orange bromine vapour is placed under a gas jar of colourless air, with a '
          'glass lid between them. The lid is removed. State what is seen over the next few minutes, '
          'and explain it in terms of particles.','marks':3,'space':38},
  {'text':'A window pane measures 1.5 m by 0.8 m. Atmospheric pressure is 100 000 Pa.','marks':3,
   'parts':[{'label':'(a)','text':'Calculate the area of the pane.','marks':1,'space':16},
            {'label':'(b)','text':'Calculate the force of the atmosphere on one side of it.','marks':1,'space':20},
            {'label':'(c)','text':'Explain why the pane does not break.','marks':1,'space':20}]},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — two changes, one after the other',
   'text':'A sealed gas syringe holds 60 cm<super>3</super> of air at a pressure of 100 kPa and a '
          'temperature of 300 K.','marks':5,
   'parts':[{'label':'(a)','text':'The plunger is pushed in until the volume is 20 cm<super>3</super>, at constant temperature. '
                                  'Calculate the new pressure and explain the result in terms of particles.','marks':3,'space':38},
            {'label':'(b)','text':'The syringe is then locked at that volume and heated to 600 K. Calculate the pressure now.','marks':1,'space':22},
            {'label':'(c)','text':'State one assumption about the syringe that must be true for your answer to (b).','marks':1,'space':20}]},
  {'text':'A sealed glass flask of gas is at a pressure of 100 kPa and a temperature of 300 K. '
          'It is cooled to 150 K. The flask does not change size.','marks':5,
   'parts':[{'label':'(a)','text':'State and explain what happens to the pressure, in terms of particles.','marks':2,'space':30},
            {'label':'(b)','text':'Calculate the new pressure.','marks':1,'space':20},
            {'label':'(c)','text':'A student says the pressure falls &ldquo;because cooling makes the particles smaller, so there is more space&rdquo;. '
                                  'Explain what is wrong with this and give the correct reason.','marks':2,'space':32}]},
  {'section':'Section 2 — the diffusion tube',
   'text':'A 60 cm glass tube has a cotton wool plug soaked in ammonia solution at the left-hand end and one '
          'soaked in concentrated hydrochloric acid at the right-hand end. Both are put in at the same moment. '
          'After several minutes a white ring of solid forms 36 cm from the ammonia end.<br/><br/>'
          '<font name="Mono" size="10">M<sub>r</sub>(NH<sub>3</sub>) = 17 &nbsp; &nbsp; M<sub>r</sub>(HCl) = 36.5</font>','marks':6,
   'parts':[{'label':'(a)','text':'Explain why a ring forms at all, and name the solid that forms it.','marks':2,'space':30},
            {'label':'(b)','text':'Calculate how far the hydrogen chloride travelled, and the ratio of the two distances.','marks':2,'space':26},
            {'label':'(c)','text':'Explain the ratio you calculated, in terms of the particles of the two gases.','marks':2,'space':30}]},
  {'text':'The same experiment is repeated with the whole tube warmed from 20 &#176;C to 60 &#176;C.','marks':4,
   'parts':[{'label':'(a)','text':'State and explain the effect on the time the ring takes to appear.','marks':2,'space':28},
            {'label':'(b)','text':'State and explain the effect on the position of the ring.','marks':2,'space':28}]},
  {'section':'Section 3 — the long explanation',
   'text':'A sealed metal can of air is left near a fire. Its volume cannot change. After a while the can bursts.<br/>'
          'Explain fully, in terms of particles, why the pressure inside rises as the can gets hotter, and why it '
          'eventually bursts. Write in continuous prose.','marks':6,'space':78},
  {'text':'A gas at a pressure of 250 000 Pa acts on one face of a piston of area 0.008 m<super>2</super>. '
          'The atmosphere, at 100 000 Pa, acts on the other face.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the force the trapped gas exerts on the piston.','marks':1,'space':20},
            {'label':'(b)','text':'Calculate the force the atmosphere exerts on the piston.','marks':1,'space':20},
            {'label':'(c)','text':'Calculate the resultant force on the piston and state its direction.','marks':1,'space':20},
            {'label':'(d)','text':'The piston is held still. State the size and direction of the force holding it.','marks':1,'space':20}]},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — apparatus you may not have met',
   'text':'A pressure cooker is a sealed pot with a locking lid and a valve in the top. Water is boiled inside it '
          'and the volume of the pot cannot change.','marks':5,
   'parts':[{'label':'(a)','text':'Explain, in terms of particles, why the pressure inside rises as the pot is heated.','marks':2,'space':30},
            {'label':'(b)','text':'The valve opens and lets steam escape when the pressure reaches 200 kPa. Explain, in terms of particles, why this lowers the pressure inside.','marks':2,'space':30},
            {'label':'(c)','text':'Explain why the lid must be locked shut.','marks':1,'space':20}]},
  {'text':'A weather balloon is released at ground level, where atmospheric pressure is 100 kPa. '
          'It rises until the atmospheric pressure around it is only 25 kPa. Assume the temperature does not change.','marks':5,
   'parts':[{'label':'(a)','text':'Explain, in terms of particles, why atmospheric pressure falls as you go higher.','marks':2,'space':30},
            {'label':'(b)','text':'At ground level the balloon has a volume of 2.0 m<super>3</super>. Calculate its volume at 25 kPa.','marks':2,'space':28},
            {'label':'(c)','text':'Suggest what eventually happens to the balloon, and why.','marks':1,'space':22}]},
  {'section':'Section 2 — reasoning it out',
   'text':'Two identical sealed containers are kept at the same temperature. Container X holds twice as many '
          'gas particles as container Y.','marks':4,
   'parts':[{'label':'(a)','text':'State which container has the greater pressure, and by what factor.','marks':1,'space':18},
            {'label':'(b)','text':'Explain your answer in terms of particles.','marks':2,'space':28},
            {'label':'(c)','text':'Y is at 300 K. Calculate the temperature Y must be heated to for its pressure to match X.','marks':1,'space':20}]},
  {'text':'A diffusion tube like the ammonia and hydrogen chloride one is set up, but this time the two gases '
          'have the same relative molecular mass, and the tube is kept at a steady temperature.','marks':4,
   'parts':[{'label':'(a)','text':'Predict where the ring will form, and explain your prediction.','marks':2,'space':28},
            {'label':'(b)','text':'The tube is now stood vertically, with the denser gas at the top. Suggest one reason the result may no longer be a fair test of diffusion.','marks':2,'space':30}]},
  {'text':'A diver&rsquo;s air cylinder holds gas at a pressure of 20 000 000 Pa. The valve at the top has an '
          'area of 0.0004 m<super>2</super>, and atmospheric pressure outside it is 100 000 Pa.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the force the compressed gas exerts on the inside of the valve.','marks':2,'space':24},
            {'label':'(b)','text':'Calculate the force the atmosphere exerts on the outside of the valve, and hence the resultant force.','marks':2,'space':28}]},
  {'section':'Section 3 — judgement',
   'text':'A bag of crisps is sealed in a factory at sea level and driven up a mountain road. At the top it has '
          'swollen up tightly, although nobody has opened it and it has not been warmed. Explain what has '
          'happened, in terms of particles and pressure.','marks':4,'space':52},
  {'text':'A student has written two answers, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;When you squash a gas, the particles are pushed closer together so they push harder '
          'on the walls. That is why the pressure goes up.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;The can was crushed because the vacuum inside sucked the sides in.&rdquo;<br/>'
          'For each one, explain the mistake and write the correct version.','marks':4,'space':56},
 ]}

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':2,'lines':[
    'Pressure is the force acting perpendicular to a surface, per unit area of that surface; pressure = force &divide; area <b>[1]</b>',
    'Unit: the <b>pascal (Pa)</b>, equal to 1 N/m<super>2</super> <b>[1]</b>'],
   'note':'&ldquo;Newtons&rdquo; alone is not a unit of pressure and scores nothing. Accept N/m<super>2</super> in place of Pa.'},
  {'n':'2','marks':4,'lines':['(a) 240 &divide; 0.4 = <b>600 Pa</b> <b>[1]</b>','(b) 60 &divide; 0.02 = <b>3000 Pa</b> <b>[1]</b>',
    '(c) 1500 &divide; 0.05 <b>[1]</b> = <b>30 000 Pa</b> <b>[1]</b>'],
   'note':'Dividing area by force gives 0.0017, 0.00033 and 0.000033. If all three answers come out tiny, the whole question has been done upside down &mdash; award the method mark in (c) only.'},
  {'n':'3','marks':3,'lines':['(a) 200 &times; 3 = <b>600 N</b> <b>[1]</b>','(b) 100 000 &times; 0.02 = <b>2000 N</b> <b>[1]</b>',
    '(c) 50 000 &times; 0.4 = <b>20 000 N</b> <b>[1]</b>']},
  {'n':'4','marks':2,'lines':[
    'The gas particles are in constant random motion and collide with the walls of the container <b>[1]</b>',
    'Each collision exerts a small force on the wall; the total force from all the collisions, divided by the area, is the pressure <b>[1]</b>'],
   'note':'&ldquo;The gas pushes on the walls&rdquo; restates the question and scores nothing. The word <b>collide</b> (or &ldquo;collisions&rdquo;) is required for the first mark.'},
  {'n':'5','marks':3,'lines':['The pressure <b>increases</b>, roughly doubling <b>[1]</b>',
    'The particles have a shorter distance to travel between the walls, so they hit the walls more often <b>[1]</b>',
    'giving more <b>collisions per unit area per second</b> <b>[1]</b>'],
   'note':'&ldquo;The particles are squashed so they push harder&rdquo; scores <b>zero</b> for the explanation. Nothing has speeded the particles up, so no collision is harder than before. This is the single most common wrong answer in the topic.'},
  {'n':'6','marks':3,'lines':['The pressure <b>increases</b> <b>[1]</b>',
    'The particles gain kinetic energy and move faster, so they hit the walls <b>more often</b> per second <b>[1]</b>',
    'and each collision transfers more momentum, so <b>each hit is harder</b> <b>[1]</b>'],
   'note':'Two separate reasons are asked for and most students give only the first. Do not award the third mark for a rewording of the second.'},
  {'n':'7','marks':2,'lines':['The particles move <b>randomly in all directions</b>, so no direction is favoured <b>[1]</b>',
    'Every wall therefore receives the same number of collisions per unit area per second <b>[1]</b>'],
   'note':'Answers that say the pressure is greatest at the bottom have imported the behaviour of a liquid. The weight of the gas is negligible here.'},
  {'n':'8','marks':2,'lines':['There are now more particles in the same volume <b>[1]</b>',
    'so more collisions with the walls each second, and therefore more collisions per unit area per second <b>[1]</b>'],
   'note':'Award nothing for &ldquo;there is more air in it so the pressure is higher&rdquo; &mdash; that is the question restated.'},
  {'n':'9','marks':3,'lines':[
    'The mistake: squashing a gas does not make the particles move any faster, so no collision is harder than before; only temperature changes how hard a particle hits <b>[1]</b>',
    'Correct explanation: the particles have less distance to travel between the walls, so they collide with the walls more often <b>[1]</b>',
    'giving more collisions per unit area per second, which is a higher pressure <b>[1]</b>'],
   'note':'The first mark is for identifying <i>why</i> &ldquo;push harder&rdquo; is wrong, not just for saying that it is.'},
  {'n':'10','marks':2,'lines':['(a) 27 &#176;C = <b>300 K</b> and 327 &#176;C = <b>600 K</b> (add 273) <b>[1]</b>',
    '(b) The kelvin temperature has doubled at constant volume, so the pressure <b>doubles</b> <b>[1]</b>'],
   'note':'A student who reasons from Celsius sees 27 going to 327 and concludes the pressure rises twelvefold. Kelvin is not optional here.'},
  {'n':'11','marks':2,'lines':[
    'Diffusion is the <b>net</b> movement of particles from a region of higher concentration to a region of lower concentration <b>[1]</b>',
    'caused by the <b>random</b> motion of the particles <b>[1]</b>'],
   'note':'Both <b>net</b> and <b>random</b> are required, one for each mark. &ldquo;Particles spreading out&rdquo; describes the result, not the process.'},
  {'n':'12','marks':2,'lines':['Any two of: a higher temperature; lighter particles (smaller M<sub>r</sub>); a greater difference in concentration <b>[1]</b>',
    'Explanation, e.g. a higher temperature gives the particles more kinetic energy so they move faster on average, and cover ground more quickly <b>[1]</b>'],
   'note':'&ldquo;Stir it&rdquo; and &ldquo;use a fan&rdquo; are not accepted. Those replace diffusion with bulk movement of the gas, which is a different process.'},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':3,'lines':['The atmosphere is a gas, and its particles are in constant random motion <b>[1]</b>',
    'They collide with every surface, and the total force of those collisions divided by the area is the pressure <b>[1]</b>',
    'At sea level it is about <b>100 000 Pa</b> (accept 100 kPa, or 1 &times; 10<super>5</super> Pa) <b>[1]</b>']},
  {'n':'2','marks':4,'lines':['(a) force = pressure &times; area = 100 000 &times; 0.01 <b>[1]</b> = <b>1000 N</b> <b>[1]</b>',
    '(b) area = 1.2 &times; 0.6 = 0.72 m<super>2</super>, force = 100 000 &times; 0.72 = <b>72 000 N</b> <b>[1]</b>',
    '(c) The same atmospheric pressure acts on the underside of the desk, so the forces balance and there is no resultant force <b>[1]</b>'],
   'note':'1000 N is the weight of a 100 kg person. Worth pointing out to a student who has written it down without reacting to it.'},
  {'n':'3','marks':4,'lines':['(a) The steam <b>condenses</b> back to liquid water <b>[1]</b>',
    '(b) The number of gas particles inside collapses, so there are almost no collisions on the inside wall and the pressure inside falls close to zero <b>[1]</b>',
    '(c) <b>Atmospheric</b> pressure outside is unchanged at about 100 000 Pa <b>[1]</b>; with nothing pushing back from inside, the atmosphere pushes the walls inwards and crushes the can <b>[1]</b>'],
   'note':'Deduct the final mark from any answer containing &ldquo;the vacuum sucked it in&rdquo;. A low pressure does not pull; it simply pushes back far more weakly, so the atmospheric push that was there all along is no longer balanced.'},
  {'n':'4','marks':3,'lines':['Expanding your chest lowers the pressure of the air inside the straw <b>[1]</b>',
    'Atmospheric pressure still acts on the surface of the drink in the glass <b>[1]</b>',
    'so the atmosphere pushes the liquid up the straw into the region of lower pressure <b>[1]</b>'],
   'note':'The question forbids the word &ldquo;suck&rdquo; on purpose. A student who cannot write the answer without it has not understood that nothing pulls.'},
  {'n':'5','marks':3,'lines':['The net movement of particles from a region of higher concentration to a region of lower concentration <b>[1]</b>',
    'The particles are in constant random motion and never stop moving <b>[1]</b>',
    'Where they are crowded, more happen to wander outwards than wander back, so the movements do not cancel <b>[1]</b>'],
   'note':'The third mark is the one that separates a description from an explanation. It is rarely written and always available.'},
  {'n':'6','marks':4,'lines':['(a) <b>Diffusion</b> <b>[1]</b>',
    '(b) The room is already full of air particles <b>[1]</b>; each vapour particle collides with them constantly and changes direction, so it follows a long random zigzag path and its progress across the room is far slower than its actual speed <b>[1]</b>',
    '(c) Warming the room (or a greater concentration of vapour); the particles gain kinetic energy and move faster on average <b>[1]</b>'],
   'note':'&ldquo;Open a window&rdquo; or &ldquo;turn on a fan&rdquo; scores nothing in (c) &mdash; both replace diffusion with a draught.'},
  {'n':'7','marks':3,'lines':['In a gas the particles are much further apart and moving much faster <b>[1]</b>',
    'so they travel further between collisions and spread more quickly; in a liquid the particles are touching, slower, and constantly obstruct one another <b>[1]</b>',
    'In a solid the particles only vibrate about fixed positions and cannot move past each other at all <b>[1]</b>']},
  {'n':'8','marks':3,'lines':['The orange colour spreads <b>upwards</b> into the top jar until both jars are evenly pale orange <b>[1]</b>',
    'The bromine and air particles are in constant random motion, so they mix by diffusion <b>[1]</b>',
    'It happens even though bromine is much denser than air, because diffusion is driven by random particle motion and not by weight; it is slow because bromine particles are heavy (M<sub>r</sub> 160 against about 29 for air) <b>[1]</b>'],
   'note':'The direction is the whole point of this classic. An answer predicting that the bromine stays at the bottom because it is heavier has missed it.'},
  {'n':'9','marks':3,'lines':['(a) 1.5 &times; 0.8 = <b>1.2 m<super>2</super></b> <b>[1]</b>',
    '(b) 100 000 &times; 1.2 = <b>120 000 N</b> <b>[1]</b>',
    '(c) The same atmospheric pressure acts on the other side, so the two forces balance <b>[1]</b>'],
   'note':'120 000 N is about the weight of twelve tonnes on one window. The balance in (c) is the only reason glazing survives at all, and stating it is worth the mark.'},
 ]},

 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':[
    '(a) The volume is divided by 3, so the pressure is multiplied by 3: <b>300 kPa</b> <b>[1]</b>; the particles travel a third of the distance between the walls, so they collide with the walls three times as often <b>[1]</b>, giving three times as many <b>collisions per unit area per second</b> <b>[1]</b>',
    '(b) The kelvin temperature doubles at constant volume, so the pressure doubles: 300 &times; 2 = <b>600 kPa</b> <b>[1]</b>',
    '(c) The syringe stays sealed and rigid &mdash; no gas escapes and the volume does not change <b>[1]</b>'],
   'note':'In (b), starting again from 100 kPa gives 200 kPa. The two changes happen one after the other, so the second acts on the answer to the first. This is the most common way to lose a mark on Paper C.'},
  {'n':'2','marks':5,'lines':[
    '(a) The pressure <b>falls</b> <b>[1]</b>; the particles lose kinetic energy and move more slowly, so they hit the walls less often and each collision is gentler <b>[1]</b>',
    '(b) The kelvin temperature has halved at constant volume, so the pressure halves: <b>50 kPa</b> <b>[1]</b>',
    '(c) The mistake: particles never change size &mdash; a particle is identical at 300 K and at 150 K <b>[1]</b>; what changes is their average speed, which lowers both the number of collisions per unit area per second and the force of each one <b>[1]</b>'],
   'note':'Award the first mark in (a) even if the reason is wrong, but only if the direction is right. Any mention of the particles shrinking, expanding or changing in (c) other than in speed cancels the second mark there.'},
  {'n':'3','marks':6,'lines':[
    '(a) Both gases spread along the tube by <b>diffusion</b> &mdash; net movement from the plug, where they are concentrated, towards the middle, because of their random motion <b>[1]</b>; where they meet they react to form solid <b>ammonium chloride, NH<sub>4</sub>Cl</b> <b>[1]</b>',
    '(b) 60 &minus; 36 = <b>24 cm</b> <b>[1]</b>; ratio 36 : 24 = <b>1.5</b> (accept 3 : 2) <b>[1]</b>',
    '(c) Both gases travelled for the same time, so ammonia must have moved faster on average <b>[1]</b>; ammonia particles have a smaller mass (17 against 36.5), and at the same temperature lighter particles move faster, so they diffuse further <b>[1]</b>'],
   'note':'&#8730;(36.5 &divide; 17) = 1.47, which is why the ring lands where it does. That calculation is beyond this syllabus and must not be required, but a student who produces it deserves to be told they are right.'},
  {'n':'4','marks':4,'lines':[
    '(a) The ring appears <b>sooner</b> <b>[1]</b>; both gases have more kinetic energy and so move faster on average, so both fronts advance more quickly <b>[1]</b>',
    '(b) The position is <b>unchanged</b> <b>[1]</b>; both gases are speeded up by the same factor, so the ratio of the two distances, and therefore the meeting point, is the same <b>[1]</b>'],
   'note':'Part (b) is the discriminator. Most students assume that anything which changes the timing must also move the ring. The reason it does not is that the change applies equally to both gases.'},
  {'n':'5','marks':6,'lines':[
    'The air in the can is made of particles in constant random motion, colliding with the walls; the total effect of those collisions, per unit area, is the pressure <b>[1]</b>',
    'Heating gives the particles more kinetic energy, so their average speed increases <b>[1]</b>',
    'They therefore reach the walls more often &mdash; more <b>collisions per unit area per second</b> <b>[1]</b>',
    'and each collision transfers more momentum, so each one exerts a greater force on the wall <b>[1]</b>',
    'The volume cannot change, so neither effect is relieved and the pressure keeps rising <b>[1]</b>',
    'When the outward force on the wall exceeds what the metal can withstand, the can bursts <b>[1]</b>'],
   'note':'Six marks, six separate ideas. Mark strictly: this question exists to reward a student who writes the mechanism out in order rather than asserting that &ldquo;heat makes pressure&rdquo;. Award no mark anywhere in this answer for &ldquo;the particles expand&rdquo;.'},
  {'n':'6','marks':4,'lines':['(a) 250 000 &times; 0.008 = <b>2000 N</b> <b>[1]</b>',
    '(b) 100 000 &times; 0.008 = <b>800 N</b> <b>[1]</b>',
    '(c) 2000 &minus; 800 = <b>1200 N</b>, acting <b>outwards</b> <b>[1]</b>',
    '(d) <b>1200 N inwards</b> <b>[1]</b>'],
   'note':'Ignoring the atmosphere altogether and answering 2000 N in (c) is the standard error. Atmospheric pressure acts on the other side of everything and is never decoration in a piston question.'},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':[
    '(a) The particles gain kinetic energy and move faster, so they hit the walls more often <b>[1]</b> and each collision is harder, giving a greater force on the same area <b>[1]</b>',
    '(b) Steam escaping removes particles from the pot <b>[1]</b>, so there are fewer particles left to collide with the walls and therefore fewer collisions per unit area per second <b>[1]</b>',
    '(c) The pressure inside is far above atmospheric, so there is a large resultant outward force on the lid, which would otherwise be blown off <b>[1]</b>'],
   'note':'Part (b) is the unfamiliar one. Students who have learnt &ldquo;pressure goes up when you heat&rdquo; as a rule rather than a mechanism have nothing to say here.'},
  {'n':'2','marks':5,'lines':[
    '(a) The higher you go, the less air there is above you <b>[1]</b>, so there are fewer particles per unit volume and therefore fewer collisions per unit area per second <b>[1]</b>',
    '(b) Pressure &times; volume stays constant, so 100 &times; 2.0 = 25 &times; V <b>[1]</b>, giving V = <b>8.0 m<super>3</super></b> <b>[1]</b>',
    '(c) It keeps expanding as it rises and eventually bursts, because the rubber can only stretch so far <b>[1]</b>'],
   'note':'Accept any correct route in (b), including &ldquo;the pressure is a quarter, so the volume is four times as big&rdquo;. A student who multiplies instead of dividing gets 0.5 m<super>3</super> &mdash; a balloon that shrinks as it rises, which should have been rejected on sight.'},
  {'n':'3','marks':4,'lines':['(a) <b>X</b>, with <b>twice</b> the pressure of Y <b>[1]</b>',
    '(b) Twice as many particles in the same volume, all moving at the same average speed since the temperature is the same <b>[1]</b>, so twice as many collisions per unit area per second <b>[1]</b>',
    '(c) The kelvin temperature must double: <b>600 K</b> <b>[1]</b>'],
   'note':'The trap in (c) is answering 600 &#176;C, or doubling 27 &#176;C. The question gives the temperature in kelvin precisely so that a student who converts unnecessarily exposes the habit.'},
  {'n':'4','marks':4,'lines':[
    '(a) In the <b>middle</b> of the tube <b>[1]</b>; equal relative molecular masses at the same temperature means equal average speeds, so both gases travel the same distance in the same time <b>[1]</b>',
    '(b) Any sensible reason, e.g. the denser gas would sink through the lighter one under gravity <b>[1]</b>, so the gases would be mixed by bulk movement (convection) as well as by diffusion, and the result would no longer be caused by diffusion alone <b>[1]</b>'],
   'note':'Part (b) is deliberately open. Award both marks for any answer that identifies bulk movement of the gas as a competing process and says why that spoils the test.'},
  {'n':'5','marks':4,'lines':['(a) 20 000 000 &times; 0.0004 <b>[1]</b> = <b>8000 N</b> <b>[1]</b>',
    '(b) 100 000 &times; 0.0004 = <b>40 N</b> <b>[1]</b>; resultant = 8000 &minus; 40 = <b>7960 N outwards</b> <b>[1]</b>'],
   'note':'Here the atmospheric contribution is only half a per cent, which is worth saying out loud: knowing when a term matters is as useful as knowing it exists.'},
  {'n':'6','marks':4,'lines':[
    'The air sealed in the bag is at about 100 000 Pa, the pressure at sea level <b>[1]</b>',
    'Higher up there is less air above, so atmospheric pressure outside the bag is lower <b>[1]</b>',
    'The pressure inside is now greater than the pressure outside, so there is a resultant outward force on the bag <b>[1]</b>',
    'The bag expands until the pressures balance, or until it bursts <b>[1]</b>'],
   'note':'A student who says &ldquo;the air inside expands because there is less pressure&rdquo; has the right idea and one mark. Insist on the comparison between inside and outside for the rest.'},
  {'n':'7','marks':4,'lines':[
    '(i) The mistake: squashing a gas does not speed the particles up, so no collision is harder than before &mdash; only a change in temperature does that <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct: the particles have a shorter distance to travel between the walls, so they collide with them more often, giving more collisions per unit area per second <b>[1]</b>',
    '(ii) The mistake: a vacuum cannot pull. A region of low pressure still pushes outwards, just far more weakly &mdash; it never draws anything towards it <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct: atmospheric pressure outside pushes the can inwards, and with the steam condensed there is nothing left inside to push back <b>[1]</b>']},
 ]},
]

files = []
for spec, code in [(A,'a'), (B,'b'), (C,'c'), (D,'d')]:
    t = sum(q.get('marks',0) for q in spec['questions'])
    assert t == 30, (spec['title'], t)
    for q in spec['questions']:
        if q.get('parts'):
            pt = sum(p.get('marks',0) for p in q['parts'])
            assert pt == q['marks'], (spec['title'], q['text'][:40], pt, q['marks'])
    p = os.path.join(OUT, 'physics-gaspressure-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)
for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)
for spec, sc in zip([A,B,C,D], SCHEMES):
    assert len(spec['questions']) == len(sc['questions']), (sc['title'], len(spec['questions']), len(sc['questions']))
    for q, a in zip(spec['questions'], sc['questions']):
        assert q['marks'] == a['marks'], (sc['title'], a['n'], q['marks'], a['marks'])
p = os.path.join(OUT, 'physics-gaspressure-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. This topic is marked on wording far more than on '
             'arithmetic, so the schemes below quote the phrases that earn each mark and name the ones that do not. '
             'Almost every explanation mark lost on these four papers goes one of four ways: writing that the particles '
             '&ldquo;push harder&rdquo; when a gas is squashed, writing that the particles expand when heated, saying that '
             'a vacuum sucks, or giving only one of the two reasons why heating a fixed volume raises the pressure. '
             'The note under each answer names the specific mistake that question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
