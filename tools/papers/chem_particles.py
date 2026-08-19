#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Chemistry · Grade 7 · States of matter'
TOPIC = 'The Particle Model'

BASE = [
 'Answer <b>every</b> question in the space provided.',
 'No calculator is needed anywhere on this paper.',
 'Where a question says <b>explain</b>, your answer must talk about <b>particles</b> — their arrangement, their movement, the spaces between them, or the forces between them.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE
INSTR_HARD = BASE + ['Several questions here describe experiments you may not have seen before. '
                     'You are not expected to recognise them — apply the particle ideas you already have.',
                     'Never write that particles melt, expand, or get bigger. Only their arrangement, spacing and energy change.']

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — the three states',
   'text':'Complete the table. Each empty box is worth one mark.','marks':6,
   'grid':[['','Solid','Liquid','Gas'],
           ['Arrangement','regular pattern','',''],
           ['Movement','','slide past each other',''],
           ['Spacing','very close','','']],
   'grid_widths':[AVAIL*0.22, AVAIL*0.26, AVAIL*0.26, AVAIL*0.26]},
  {'text':'Name the change of state in each case.','marks':4,
   'parts':[{'label':'(a)','text':'Solid to liquid','marks':1,'space':13},
            {'label':'(b)','text':'Gas to liquid','marks':1,'space':13},
            {'label':'(c)','text':'Liquid to gas','marks':1,'space':13},
            {'label':'(d)','text':'Solid straight to gas','marks':1,'space':13}]},
  {'text':'Answer these two questions about the properties of the states.','marks':2,
   'parts':[{'label':'(a)','text':'Which state has a fixed volume but no fixed shape?','marks':1,'space':13},
            {'label':'(b)','text':'Which state has neither a fixed volume nor a fixed shape?','marks':1,'space':13}]},
  {'section':'Section 2 — diagrams and explanations',
   'text':'In the space below, draw a particle diagram for a solid, a liquid and a gas. '
          'Label each one.','marks':3,'space':56},
  {'text':'Explain why a gas can easily be compressed, but a liquid can hardly be compressed at all.',
   'marks':3,'space':34},
  {'text':'State the melting point and the boiling point of water in degrees Celsius.','marks':2,'space':22},
  {'text':'Explain, in terms of particles, why a solid keeps its shape.','marks':2,'space':28},
  {'section':'Section 3 — what changes and what does not',
   'text':'Changes of state are described as <b>physical</b> changes rather than chemical changes. '
          'State what this means, and give one piece of evidence for it.','marks':3,'space':34},
  {'text':'20 g of ice is left in a sealed container until it has all melted. '
          'State the mass of water produced, and explain your answer.','marks':2,'space':28},
  {'text':'Give three properties of a gas.','marks':3,'space':34},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — heating and cooling',
   'text':'A solid is heated steadily and its temperature recorded every two minutes.<br/><br/>'
          '<font name="Mono" size="10">Time (min): &nbsp;0 &nbsp; &nbsp;2 &nbsp; &nbsp;4 &nbsp; &nbsp;6 &nbsp; &nbsp;8 &nbsp; &nbsp;10 &nbsp; &nbsp;12<br/>'
          'Temp (°C): &nbsp; 30 &nbsp; 54 &nbsp; 80 &nbsp; 80 &nbsp; 80 &nbsp; 96 &nbsp; 118</font>','marks':5,
   'parts':[{'label':'(a)','text':'State the melting point of the substance, and how you can tell.','marks':2,'space':22},
            {'label':'(b)','text':'State how long the substance took to melt.','marks':1,'space':16},
            {'label':'(c)','text':'Describe what is happening to the particles between 4 and 8 minutes.','marks':2,'space':26}]},
  {'text':'A different substance boils at 78 °C and melts at &minus;114 °C. '
          'State what state it is in at room temperature (20 °C), and explain how you know.','marks':3,'space':30},
  {'text':'Explain why the temperature of a pure substance does not rise while it is melting, '
          'even though the heater is still switched on.','marks':3,'space':34},
  {'section':'Section 2 — mass and movement',
   'text':'A sealed flask containing water is weighed. It is then warmed until all the water has turned to steam, '
          'and weighed again.','marks':4,
   'parts':[{'label':'(a)','text':'State what happens to the reading on the balance.','marks':1,'space':16},
            {'label':'(b)','text':'Explain your answer in terms of particles.','marks':2,'space':26},
            {'label':'(c)','text':'State what would be different if the flask had been left open.','marks':1,'space':20}]},
  {'text':'A drop of ink is placed at the bottom of a tall glass of still water. Two days later the whole glass '
          'is evenly coloured, although nobody stirred it.','marks':4,
   'parts':[{'label':'(a)','text':'Name the process.','marks':1,'space':13},
            {'label':'(b)','text':'Explain how the ink reached the top.','marks':2,'space':26},
            {'label':'(c)','text':'State one change that would make it happen faster.','marks':1,'space':16}]},
  {'text':'Smoke is viewed in a small glass cell under a microscope, and the specks are seen to jiggle '
          'about in random directions.','marks':3,
   'parts':[{'label':'(a)','text':'Name what is being observed.','marks':1,'space':13},
            {'label':'(b)','text':'Explain what is causing the specks to move.','marks':2,'space':26}]},
  {'section':'Section 3 — speed and pressure',
   'text':'Explain why a smell spreads across a warm room faster than across a cold one.','marks':3,'space':32},
  {'text':'Name the change of state in which a solid turns directly into a gas, and give one example.',
   'marks':2,'space':24},
  {'text':'A sealed balloon is put into a fridge and is found to shrink slightly. '
          'Explain this in terms of particles.','marks':3,'space':34},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — evaporation against boiling',
   'text':'Give <b>four</b> differences between evaporation and boiling. '
          'Each difference must say something about both processes.','marks':4,'space':48},
  {'text':'Water boils at 100 °C. Explain how a puddle can still disappear completely on a day '
          'when the temperature never rises above 9 °C.','marks':3,'space':36},
  {'text':'A wet cloth wrapped around a bottle keeps the bottle cool. '
          'Explain why evaporation cools the liquid that is left behind.','marks':3,'space':36},
  {'text':'State three things that would make water evaporate faster, and explain <b>one</b> of them '
          'in terms of particles.','marks':4,'space':44},
  {'section':'Section 2 — gas pressure',
   'text':'A sealed metal tin containing air is placed in a hot oven. '
          'Explain, in terms of particles, why the pressure inside the tin increases.','marks':3,'space':34},
  {'text':'A gas in a sealed syringe is pushed into half its original volume, at the same temperature. '
          'Explain what happens to the pressure, and why.','marks':3,'space':34},
  {'section':'Section 3 — unfamiliar experiments',
   'text':'A drop of liquid bromine is released at the bottom of a tall sealed jar. In one experiment the jar '
          'contains air; in another the air has been pumped out first. The brown bromine vapour fills the '
          'empty jar almost instantly, but takes several minutes to fill the jar containing air.','marks':4,
   'parts':[{'label':'(a)','text':'Name the process by which the bromine spreads.','marks':1,'space':14},
            {'label':'(b)','text':'Explain why it is so much slower in the jar containing air.','marks':3,'space':34}]},
  {'text':'Washing dries faster on a windy day than on a still day of the same temperature. '
          'Explain why.','marks':3,'space':34},
  {'text':'A burn from steam at 100 °C is far more serious than a burn from boiling water at 100 °C, '
          'even though both are at the same temperature. Explain why.','marks':3,'space':36},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — reading a cooling curve',
   'text':'A liquid is allowed to cool and its temperature is recorded every minute.<br/><br/>'
          '<font name="Mono" size="10">Time (min): &nbsp;0 &nbsp; &nbsp;2 &nbsp; &nbsp;4 &nbsp; &nbsp;6 &nbsp; &nbsp;8 &nbsp; &nbsp;10 &nbsp; &nbsp;12 &nbsp; &nbsp;14<br/>'
          'Temp (°C): &nbsp; 90 &nbsp; 72 &nbsp; 55 &nbsp; 55 &nbsp; 55 &nbsp; 55 &nbsp; 41 &nbsp; 30</font>','marks':6,
   'parts':[{'label':'(a)','text':'State the freezing point of the substance.','marks':1,'space':14},
            {'label':'(b)','text':'State the state of the substance at 2 minutes and at 14 minutes.','marks':2,'space':20},
            {'label':'(c)','text':'Explain why the temperature stays constant between 4 and 10 minutes, '
                                  'even though the substance is still losing energy to the room.','marks':3,'space':36}]},
  {'section':'Section 2 — the diffusion tube',
   'text':'A long glass tube has cotton wool soaked in <b>ammonia</b> pushed into one end and cotton wool soaked '
          'in <b>hydrogen chloride</b> pushed into the other, at the same moment. Both give off gases. '
          'After a few minutes a white ring of solid forms inside the tube, closer to the hydrogen chloride end.',
   'marks':5,
   'parts':[{'label':'(a)','text':'Explain how the two gases travelled along the tube.','marks':2,'space':26},
            {'label':'(b)','text':'Explain why the ring does not form in the middle.','marks':2,'space':28},
            {'label':'(c)','text':'Predict, with a reason, what would happen to the position of the ring if the '
                                  'experiment were repeated in a warmer room.','marks':1,'space':24}]},
  {'section':'Section 3 — the long explanation',
   'text':'A block of ice at &minus;20 °C is heated steadily until it has all become steam at 120 °C. '
          'Describe and explain the whole journey in terms of particles and energy. '
          'Your answer should refer to both flat sections of the heating curve, and to what the energy '
          'is doing at each stage.','marks':6,'space':84},
  {'text':'A substance melts at &minus;7 °C and boils at 58 °C.','marks':4,
   'parts':[{'label':'(a)','text':'State its state at 20 °C, and explain how you know.','marks':2,'space':26},
            {'label':'(b)','text':'State its state at 80 °C, and explain how you know.','marks':2,'space':26}]},
  {'text':'Water is boiled in an open pan on a stove. After ten minutes the pan and its contents have '
          'a smaller mass than before.','marks':4,
   'parts':[{'label':'(a)','text':'Explain where the missing mass has gone.','marks':2,'space':26},
            {'label':'(b)','text':'Explain why this does <b>not</b> break the rule that mass is conserved.','marks':2,'space':28}]},
  {'text':'A student has written two statements in her book, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;When a solid is heated, the particles get bigger, so the solid expands.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;The flat part of the heating curve shows that nothing is happening.&rdquo;<br/>'
          'For each one, explain the mistake and write a correct version.','marks':5,'space':60},
 ]}

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':6,'lines':[
    'Arrangement — liquid: <b>touching but jumbled, no pattern</b>; gas: <b>far apart, random</b>',
    'Movement — solid: <b>vibrate about fixed positions</b>; gas: <b>fast and random, in all directions</b>',
    'Spacing — liquid: <b>close, still touching</b>; gas: <b>far apart, large spaces</b>'],
   'note':'One mark per box. "Do not move" for a solid is wrong — solid particles vibrate.'},
  {'n':'2','marks':4,'lines':['(a) <b>Melting</b>','(b) <b>Condensing</b>','(c) <b>Boiling</b> (or evaporating)','(d) <b>Sublimation</b>']},
  {'n':'3','marks':2,'lines':['(a) <b>Liquid</b>','(b) <b>Gas</b>']},
  {'n':'4','marks':3,'lines':['Solid: circles touching in a regular pattern <b>[1]</b>',
    'Liquid: circles touching but jumbled, no pattern <b>[1]</b>',
    'Gas: circles well spread out with clear space between them <b>[1]</b>'],
   'note':'Drawing gaps between the particles of a solid or liquid loses that mark. Only gases have real space.'},
  {'n':'5','marks':3,'lines':['In a gas the particles are far apart with large spaces between them <b>[1]</b>',
    'so they can be pushed closer together <b>[1]</b>',
    'In a liquid the particles are already touching, so there is almost no space left to remove <b>[1]</b>']},
  {'n':'6','marks':2,'lines':['Melting point <b>0 °C</b> <b>[1]</b>','Boiling point <b>100 °C</b> <b>[1]</b>']},
  {'n':'7','marks':2,'lines':['The particles are held in fixed positions by strong forces between them <b>[1]</b>',
    'so they cannot move past one another and the shape cannot change <b>[1]</b>']},
  {'n':'8','marks':3,'lines':['A physical change means no new substance is made <b>[1]</b>, and the change can be reversed <b>[1]</b>',
    'Evidence: steam can be condensed straight back into water, and the mass is unchanged <b>[1]</b>']},
  {'n':'9','marks':2,'lines':['<b>20 g</b> <b>[1]</b>',
    'The same particles are still present, just arranged differently, and none can leave a sealed container <b>[1]</b>']},
  {'n':'10','marks':3,'lines':['Any three, one mark each: no fixed shape; no fixed volume / fills its container; '
    'can be compressed; much less dense than the solid or liquid; particles move fast and randomly; exerts pressure on the container walls.']},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) <b>80 °C</b> <b>[1]</b>; the temperature stops rising and stays at that value while the substance melts <b>[1]</b>',
    '(b) From 4 min to 8 min, so <b>4 minutes</b> <b>[1]</b>',
    '(c) The energy going in is breaking the forces holding the particles in their fixed pattern <b>[1]</b>, '
    'so the particles become free to slide past each other rather than speeding up <b>[1]</b>'],
   'note':'Notice the readings rise 24 °C in the first two minutes and 22 °C in the last two — the heater was working just as hard during the flat section.'},
  {'n':'2','marks':3,'lines':['<b>Liquid</b> <b>[1]</b>',
    '20 °C is above its melting point of &minus;114 °C, so it is not solid <b>[1]</b>',
    'and below its boiling point of 78 °C, so it is not a gas <b>[1]</b>'],
   'note':'Both comparisons are needed. One of them alone narrows it to two states, not one.'},
  {'n':'3','marks':3,'lines':['All the energy going in is used to break or weaken the forces between the particles <b>[1]</b>',
    'None of it is left over to make the particles move faster <b>[1]</b>',
    'Temperature is a measure of how fast the particles move, so it does not rise <b>[1]</b>']},
  {'n':'4','marks':4,'lines':['(a) The reading <b>does not change</b> <b>[1]</b>',
    '(b) The same particles are still inside; boiling only spreads them out and speeds them up <b>[1]</b>, '
    'and nothing can enter or leave a sealed flask <b>[1]</b>',
    '(c) The reading would <b>fall</b>, because steam would escape from the flask <b>[1]</b>']},
  {'n':'5','marks':4,'lines':['(a) <b>Diffusion</b> <b>[1]</b>',
    '(b) The particles of ink and water are in constant random motion and collide with each other <b>[1]</b>; '
    'because the ink starts crowded in one place, random movement carries more particles outwards than back, until they are evenly spread <b>[1]</b>',
    '(c) Warming the water (accept: a shallower container, or gentle warming) <b>[1]</b>'],
   'note':'"It just spread out" describes the result rather than explaining it, and scores nothing in (b).'},
  {'n':'6','marks':3,'lines':['(a) <b>Brownian motion</b> <b>[1]</b>',
    '(b) Air particles, too small to see, are moving fast and randomly <b>[1]</b> and colliding unevenly with the much larger smoke specks, knocking them about <b>[1]</b>']},
  {'n':'7','marks':3,'lines':['In a warm room the particles have more energy <b>[1]</b>',
    'so they move faster <b>[1]</b>','and diffuse across the room more quickly <b>[1]</b>']},
  {'n':'8','marks':2,'lines':['<b>Sublimation</b> <b>[1]</b>','Example: solid carbon dioxide (dry ice), or iodine when warmed <b>[1]</b>']},
  {'n':'9','marks':3,'lines':['In the fridge the air particles inside lose energy and move more slowly <b>[1]</b>',
    'so they hit the walls of the balloon less often and less hard <b>[1]</b>',
    'The pressure inside falls, so the outside air pressure squeezes the balloon smaller <b>[1]</b>']},
 ]},

 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':4,'lines':['One mark for each genuine comparison:',
    'Boiling happens only at the boiling point; evaporation happens at any temperature.',
    'Boiling happens throughout the liquid; evaporation happens only at the surface.',
    'Boiling is fast; evaporation is slow.','Boiling produces bubbles; evaporation does not.'],
   'note':'Each mark needs both halves. "Evaporation is at the surface" on its own is half an answer.'},
  {'n':'2','marks':3,'lines':['The particles in the puddle have a range of speeds, not all the same <b>[1]</b>',
    'The fastest ones at the surface have enough energy to overcome the forces holding them in the liquid <b>[1]</b>',
    'so they escape as a gas, and this can happen at any temperature <b>[1]</b>']},
  {'n':'3','marks':3,'lines':['Only the fastest particles have enough energy to escape <b>[1]</b>',
    'so the average speed of the particles left behind falls <b>[1]</b>',
    'Temperature is a measure of average particle speed, so the remaining liquid cools <b>[1]</b>']},
  {'n':'4','marks':4,'lines':['Any three, one mark each: higher temperature; larger surface area; wind or a draught. <b>[3]</b>',
    'One explained <b>[1]</b> — e.g. a higher temperature means more particles have enough energy to escape from the surface.']},
  {'n':'5','marks':3,'lines':['The particles gain energy and move faster <b>[1]</b>',
    'so they hit the walls of the tin harder <b>[1]</b> and more frequently <b>[1]</b>'],
   'note':'Harder <i>and</i> more often. Only one of the two is the most commonly dropped mark in the whole topic.'},
  {'n':'6','marks':3,'lines':['The pressure <b>doubles</b>, or increases <b>[1]</b>',
    'The same number of particles now occupies half the space, so they hit the walls more often <b>[1]</b>',
    'More frequent collisions in the same area means a greater pressure <b>[1]</b>'],
   'note':'The particles are not moving faster — the temperature is unchanged. Only the frequency of collisions has changed.'},
  {'n':'7','marks':4,'lines':['(a) <b>Diffusion</b> <b>[1]</b>',
    '(b) In the empty jar the bromine particles travel freely in straight lines with nothing in the way <b>[1]</b>; '
    'in air they collide constantly with air particles <b>[1]</b>, so they are knocked in random directions and take a '
    'long, zig-zagging path to cross the jar <b>[1]</b>'],
   'note':'The bromine particles are moving just as fast in both jars. It is the path length, not the speed, that differs.'},
  {'n':'8','marks':3,'lines':['Water particles escape from the surface of the wet clothes by evaporation <b>[1]</b>',
    'Wind carries those escaped particles away from just above the surface <b>[1]</b>',
    'so fewer are recaptured by the cloth, and the washing loses particles faster overall <b>[1]</b>']},
  {'n':'9','marks':3,'lines':['When steam touches the skin it condenses back into liquid water <b>[1]</b>',
    'Condensing releases the large amount of energy that was needed to separate the particles when it boiled <b>[1]</b>',
    'That extra energy is transferred to the skin on top of the energy from the water cooling, so the burn is worse <b>[1]</b>'],
   'note':'This is the same 2260 kJ per kilogram that made the boiling plateau so long on the study page.'},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':6,'lines':['(a) <b>55 °C</b> <b>[1]</b>',
    '(b) At 2 minutes it is a <b>liquid</b> (72 °C, above the freezing point) <b>[1]</b>; at 14 minutes it is a <b>solid</b> (30 °C, below it) <b>[1]</b>',
    '(c) The particles are settling into fixed positions in a regular pattern <b>[1]</b>; as they do so, energy is '
    '<b>released</b> <b>[1]</b>, and this released energy replaces the energy lost to the room, so the temperature holds steady until all of it has frozen <b>[1]</b>'],
   'note':'Freezing releases energy — the mirror image of melting absorbing it. Students who describe freezing as "losing energy so it cools" have missed the point of the flat section.'},
  {'n':'2','marks':5,'lines':['(a) By <b>diffusion</b> <b>[1]</b>; the gas particles are in constant random motion and spread out from where they are concentrated towards the empty space in the tube <b>[1]</b>',
    '(b) The ring forms where the two gases meet. Ammonia particles are lighter, so at the same temperature they travel faster <b>[1]</b> and cover more of the tube before the two meet, putting the meeting point nearer the hydrogen chloride end <b>[1]</b>',
    '(c) The ring would form in <b>about the same place, but sooner</b> — both gases speed up, so the race is still won by the same margin <b>[1]</b>'],
   'note':'Part (c) is the discriminator. The instinct is to say the ring moves, because "faster" feels as though it should change the position.'},
  {'n':'3','marks':6,'lines':['Award one mark for each of these, up to six:',
    'Below 0 °C the energy makes the particles vibrate faster and the temperature rises.',
    'At 0 °C the temperature stops rising; the energy breaks the forces holding particles in the lattice.',
    'The particles become free to slide past each other — the ice melts.',
    'From 0 to 100 °C the energy again goes into speed, and the temperature rises.',
    'At 100 °C the temperature stops again; the energy separates the particles completely.',
    'Above 100 °C the energy goes back into speed and the steam heats up; throughout, the particles themselves never change.'],
   'note':'For full marks the answer must say what the energy is doing at each stage, not just what state the substance is in. Award at most four if both flat sections are described without explaining where the energy goes.'},
  {'n':'4','marks':4,'lines':['(a) <b>Liquid</b> <b>[1]</b>; 20 °C is above the melting point of &minus;7 °C and below the boiling point of 58 °C <b>[1]</b>',
    '(b) <b>Gas</b> <b>[1]</b>; 80 °C is above the boiling point of 58 °C <b>[1]</b>']},
  {'n':'5','marks':4,'lines':['(a) The water has turned to steam and escaped into the room as a gas <b>[1]</b>; '
    'the particles have left the pan, taking their mass with them <b>[1]</b>',
    '(b) No particles have been destroyed — they have only moved somewhere else <b>[1]</b>; '
    'if the steam were collected and weighed, the total would be unchanged, so mass is still conserved <b>[1]</b>'],
   'note':'The pan is an open system. Conservation of mass only looks broken when you weigh part of it.'},
  {'n':'6','marks':5,'lines':[
    '(i) The mistake: particles do not change size, whatever the temperature <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: the particles vibrate faster and further apart, so the <b>spaces</b> between them increase and the solid expands <b>[2]</b>',
    '(ii) The mistake: the energy is still going in at the same rate, so a great deal is happening <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: the energy is breaking the forces between the particles rather than speeding them up, so the state changes while the temperature stays constant <b>[1]</b>'],
   'note':'These are the two most common wrong sentences in the whole topic. If he can mark them in someone else&rsquo;s work, he is unlikely to write them in his own.'},
 ]},
]

files = []
for spec, code in [(A,'a'), (B,'b'), (C,'c'), (D,'d')]:
    t = sum(q.get('marks',0) for q in spec['questions'])
    assert t == 30, (spec['title'], t)
    p = os.path.join(OUT, 'chemistry-particles-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)
for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)
p = os.path.join(OUT, 'chemistry-particles-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Most marks on this topic are won or lost '
             'on language rather than knowledge: an answer that describes how something feels or looks scores '
             'nothing, while the same idea expressed in terms of arrangement, movement, spacing or forces '
             'scores in full. Two phrases are worth insisting on — "the forces between the particles", and '
             '"harder and more frequently". The notes under each answer flag the specific mistake that '
             'question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
