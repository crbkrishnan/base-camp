#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Physics · Grade 7 · Motion'
TOPIC = 'Speed, Distance and Time'

BASE = [
 'Answer <b>every</b> question in the space provided. Show your working — method marks are awarded even when the final answer is wrong.',
 'A calculator is allowed, but every number on this paper is designed to work without one.',
 'Every answer must carry a <b>unit</b>. An answer with no unit does not score the final mark.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + ['Reminder: <b>speed = distance &divide; time</b>, and to convert m/s to km/h multiply by 3.6.']
INSTR_HARD = BASE + ['No formula and no conversion factor are given on this paper.',
                     'Where a question asks for an average speed, it means total distance divided by total time.']

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — the formula',
   'text':'Write down the formula for speed, and state the SI unit of speed.','marks':2,'space':24},
  {'text':'Calculate the speed in each case.','marks':4,
   'parts':[{'label':'(a)','text':'100 m travelled in 20 s.','marks':1,'space':18},
            {'label':'(b)','text':'240 km travelled in 3 hours.','marks':1,'space':18},
            {'label':'(c)','text':'45 m travelled in 6 s.','marks':2,'space':22}]},
  {'text':'Calculate the distance travelled.','marks':2,
   'parts':[{'label':'(a)','text':'12 m/s for 30 s.','marks':1,'space':18},
            {'label':'(b)','text':'60 km/h for 2 hours.','marks':1,'space':18}]},
  {'text':'Calculate the time taken.','marks':2,
   'parts':[{'label':'(a)','text':'400 m at 8 m/s.','marks':1,'space':18},
            {'label':'(b)','text':'150 km at 50 km/h.','marks':1,'space':18}]},
  {'section':'Section 2 — units','text':'Convert each speed.','marks':3,
   'parts':[{'label':'(a)','text':'20 m/s into km/h','marks':1,'space':16},
            {'label':'(b)','text':'90 km/h into m/s','marks':1,'space':16},
            {'label':'(c)','text':'5 m/s into km/h','marks':1,'space':16}]},
  {'text':'Convert each time.','marks':3,
   'parts':[{'label':'(a)','text':'30 minutes into hours','marks':1,'space':14},
            {'label':'(b)','text':'2 hours 15 minutes into hours','marks':1,'space':14},
            {'label':'(c)','text':'3 minutes into seconds','marks':1,'space':14}]},
  {'section':'Section 3 — journeys',
   'text':'A walker&rsquo;s journey is recorded below.<br/><br/>'
          '<font name="Mono" size="10">Time (s): &nbsp; &nbsp; &nbsp;0 &nbsp; &nbsp;10 &nbsp; &nbsp;20 &nbsp; &nbsp;30<br/>'
          'Distance (m): &nbsp;0 &nbsp; &nbsp;15 &nbsp; &nbsp;30 &nbsp; &nbsp;45</font><br/><br/>'
          'Calculate the walker&rsquo;s speed, and state how you can tell it is constant.','marks':3,'space':34},
  {'text':'State what a <b>horizontal line</b> on a distance&ndash;time graph tells you about the object, '
          'and explain why.','marks':2,'space':26},
  {'text':'A cyclist travels 6 km in 15 minutes. Calculate her speed in km/h.','marks':3,'space':32},
  {'text':'A student calculates that his walking speed is 50 m/s. '
          'Explain why this answer must be wrong.','marks':2,'space':26},
  {'text':'A car travels at 15 m/s for 40 s. Calculate how far it goes, giving your answer '
          'in metres and in kilometres.','marks':2,'space':28},
  {'text':'State the difference between <b>average speed</b> and <b>instantaneous speed</b>.','marks':2,'space':26},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — reading a journey',
   'text':'A runner&rsquo;s journey is recorded below.<br/><br/>'
          '<font name="Mono" size="10">Time (s): &nbsp; &nbsp; &nbsp;0 &nbsp; &nbsp;20 &nbsp; &nbsp;40 &nbsp; &nbsp;60 &nbsp; &nbsp;80<br/>'
          'Distance (m): &nbsp;0 &nbsp; &nbsp;40 &nbsp; &nbsp;80 &nbsp; &nbsp;80 &nbsp; &nbsp;30</font>','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the speed during the first 40 seconds.','marks':2,'space':24},
            {'label':'(b)','text':'Describe what happens between 40 s and 60 s, and state how you know.','marks':1,'space':20},
            {'label':'(c)','text':'Describe what happens between 60 s and 80 s, and calculate the speed during it.','marks':2,'space':28}]},
  {'text':'Sketch a distance&ndash;time graph for this journey, labelling both axes with units:<br/>'
          '<i>A car travels 300 m in 30 s at a steady speed, stops for 20 s, then travels a further 100 m in 20 s.</i>',
   'marks':4,'space':70},
  {'text':'Using the journey in question 2, describe it in three sentences. '
          'Every sentence must contain a number.','marks':4,'space':44},
  {'section':'Section 2 — average speed',
   'text':'A car travels 20 km in 30 minutes, then a further 30 km in 1 hour. '
          'Calculate the average speed for the whole journey in km/h.','marks':4,'space':40},
  {'text':'A cyclist rides 15 km in 30 minutes, rests for 15 minutes, then rides 10 km in 15 minutes. '
          'Calculate the average speed for the whole journey in km/h.','marks':4,'space':40},
  {'text':'Explain why stopping for a rest lowers the average speed of a journey, '
          'even though the cyclist does not travel any slower when moving.','marks':3,'space':32},
  {'section':'Section 3 — comparing',
   'text':'Which is faster: 12 m/s, or 40 km/h? Show your working and state which one.','marks':3,'space':34},
  {'text':'Explain what the <b>gradient</b> of a distance&ndash;time graph represents, and describe how you '
          'would calculate it from a graph.','marks':3,'space':34},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — journeys in parts',
   'text':'A car travels 60 km at 60 km/h, then a further 60 km at 120 km/h.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the time taken for each part of the journey.','marks':2,'space':26},
            {'label':'(b)','text':'Calculate the average speed for the whole journey.','marks':2,'space':26},
            {'label':'(c)','text':'Explain why the answer is not 90 km/h.','marks':1,'space':22}]},
  {'text':'An athlete runs 500 m in 50 s, then walks a further 500 m in 200 s.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the total distance and the total time.','marks':2,'space':24},
            {'label':'(b)','text':'Calculate the average speed for the whole 1000 m, in m/s.','marks':2,'space':26},
            {'label':'(c)','text':'State why the answer is not the average of 10 m/s and 2.5 m/s.','marks':1,'space':20}]},
  {'section':'Section 2 — using speed in the real world',
   'text':'During a storm a student sees a flash of lightning and hears the thunder 6 seconds later. '
          'Sound travels at 330 m/s.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate how far away the lightning was, in metres.','marks':2,'space':26},
            {'label':'(b)','text':'Give your answer in kilometres.','marks':1,'space':18},
            {'label':'(c)','text':'Explain why it is reasonable to assume the light arrived instantly.','marks':1,'space':22}]},
  {'text':'Put these three speeds in order, slowest first. You must show your working.<br/><br/>'
          '<font name="Mono" size="10.5">15 m/s &nbsp; &nbsp; 50 km/h &nbsp; &nbsp; 840 m/min</font>',
   'marks':4,'space':44},
  {'section':'Section 3 — working backwards',
   'text':'A train must cover 300 km in 4 hours. It travels the first 100 km at an average speed of 50 km/h.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the total time allowed for the journey, and the time used so far.','marks':2,'space':26},
            {'label':'(b)','text':'Calculate the distance still to travel and the time remaining.','marks':1,'space':22},
            {'label':'(c)','text':'Calculate the average speed needed for the rest of the journey.','marks':2,'space':26}]},
  {'text':'Explain, in terms of time, why you can never find an average speed by averaging '
          'the two speeds of a two-part journey.','marks':3,'space':34},
  {'text':'A journey is recorded below.<br/><br/>'
          '<font name="Mono" size="10">Time (min): &nbsp; &nbsp;0 &nbsp; &nbsp; 5 &nbsp; &nbsp;10 &nbsp; &nbsp;15 &nbsp; &nbsp;20<br/>'
          'Distance (km): &nbsp;0 &nbsp; &nbsp; 3 &nbsp; &nbsp; 6 &nbsp; &nbsp; 6 &nbsp; &nbsp;12</font><br/><br/>'
          'Calculate the speed of the fastest section of this journey, in km/h.','marks':4,'space':40},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — hitting a target average',
   'text':'A runner wants to average 5 m/s over a 1000 m race. She covers the first 400 m at 4 m/s.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the total time she is allowed for the whole race.','marks':1,'space':22},
            {'label':'(b)','text':'Calculate the time she has used, and the time remaining.','marks':2,'space':26},
            {'label':'(c)','text':'Calculate the speed she must run for the rest of the race.','marks':2,'space':26}]},
  {'text':'Two drivers make different journeys.<br/>'
          '<b>Driver A</b> drives for 1 hour at 40 km/h, then for 1 hour at 80 km/h.<br/>'
          '<b>Driver B</b> drives 40 km at 40 km/h, then 40 km at 80 km/h.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate Driver A&rsquo;s average speed.','marks':2,'space':26},
            {'label':'(b)','text':'Calculate Driver B&rsquo;s average speed.','marks':2,'space':28},
            {'label':'(c)','text':'Explain why the two answers are different.','marks':1,'space':22}]},
  {'section':'Section 2 — two objects at once',
   'text':'A car travelling at 25 m/s draws level with a lorry travelling at 20 m/s in the next lane. '
          'Calculate how long it takes the car to be 100 m ahead of the lorry.','marks':4,'space':42},
  {'text':'A student shouts towards a cliff and hears the echo 3 seconds later. Sound travels at 340 m/s. '
          'Calculate the distance from the student to the cliff.','marks':4,'space':42},
  {'section':'Section 3 — traps and judgement',
   'text':'A car travels at 72 km/h for 90 seconds. Calculate the distance it covers, in metres.',
   'marks':4,'space':40},
  {'text':'On a distance&ndash;time graph, one object&rsquo;s line is straight and another&rsquo;s curves upwards more '
          'and more steeply.','marks':4,
   'parts':[{'label':'(a)','text':'State what each line tells you about that object&rsquo;s motion.','marks':2,'space':24},
            {'label':'(b)','text':'Explain how you can tell which object is moving faster at the very end of the journey.','marks':2,'space':26}]},
  {'text':'A student has written two answers, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;The train went 30 km in 20 minutes, so its speed is 1.5 km/h.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;The flat part of the graph shows the car moving at a constant speed.&rdquo;<br/>'
          'For each one, explain the mistake and give the correct answer or description.','marks':4,'space':48},
 ]}

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':2,'lines':['speed = distance &divide; time <b>[1]</b>','SI unit: <b>m/s</b> (metres per second) <b>[1]</b>']},
  {'n':'2','marks':4,'lines':['(a) 100 &divide; 20 = <b>5 m/s</b>','(b) 240 &divide; 3 = <b>80 km/h</b>',
    '(c) 45 &divide; 6 <b>[1]</b> = <b>7.5 m/s</b> <b>[1]</b>'],
   'note':'In (b) the answer is in km/h because the data was in km and hours. No conversion was asked for.'},
  {'n':'3','marks':2,'lines':['(a) 12 &times; 30 = <b>360 m</b>','(b) 60 &times; 2 = <b>120 km</b>']},
  {'n':'4','marks':2,'lines':['(a) 400 &divide; 8 = <b>50 s</b>','(b) 150 &divide; 50 = <b>3 hours</b>']},
  {'n':'5','marks':3,'lines':['(a) 20 &times; 3.6 = <b>72 km/h</b>','(b) 90 &divide; 3.6 = <b>25 m/s</b>',
    '(c) 5 &times; 3.6 = <b>18 km/h</b>'],
   'note':'A quick check: 72 km/h is a believable road speed. Answers like 7200 or 5.6 signal the wrong direction.'},
  {'n':'6','marks':3,'lines':['(a) <b>0.5 h</b>','(b) <b>2.25 h</b>','(c) <b>180 s</b>'],
   'note':'(b) is the standard trap. 2 h 15 min is 2.25 h, never 2.15 h.'},
  {'n':'7','marks':3,'lines':['45 &divide; 30 <b>[1]</b> = <b>1.5 m/s</b> <b>[1]</b>',
    'It is constant because the distance increases by the same amount (15 m) in each equal 10 s interval <b>[1]</b>']},
  {'n':'8','marks':2,'lines':['The object is <b>stationary</b> <b>[1]</b>',
    'because its distance from the start is not changing as time passes <b>[1]</b>'],
   'note':'"Constant speed" is the wrong answer here and is chosen more often than the right one.'},
  {'n':'9','marks':3,'lines':['15 minutes = 0.25 h <b>[1]</b>','6 &divide; 0.25 <b>[1]</b>','= <b>24 km/h</b> <b>[1]</b>'],
   'note':'6 &divide; 15 = 0.4 scores the method mark only. That answer is in km per minute.'},
  {'n':'10','marks':2,'lines':['50 m/s is about 180 km/h <b>[1]</b>',
    'That is far faster than any person can walk — a walking speed is closer to 1.5 m/s, so he has probably divided the wrong way round <b>[1]</b>']},
  {'n':'11','marks':2,'lines':['15 &times; 40 = <b>600 m</b> <b>[1]</b>','= <b>0.6 km</b> <b>[1]</b>']},
  {'n':'12','marks':2,'lines':['Average speed is the total distance divided by the total time for a whole journey <b>[1]</b>',
    'Instantaneous speed is the speed at one particular moment, such as the reading on a speedometer <b>[1]</b>']},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) 80 &divide; 40 <b>[1]</b> = <b>2 m/s</b> <b>[1]</b>',
    '(b) The runner is <b>stationary</b> — the distance stays at 80 m <b>[1]</b>',
    '(c) She is <b>returning towards the start</b> <b>[1]</b>; 50 m in 20 s, so the speed is <b>2.5 m/s</b> <b>[1]</b>'],
   'note':'In (c) she returns faster than she set out. Both the direction and the number are needed.'},
  {'n':'2','marks':4,'lines':['Axes labelled "time (s)" and "distance (m)" with sensible scales <b>[1]</b>',
    'Straight line from (0, 0) to (30, 300) <b>[1]</b>','Horizontal line from (30, 300) to (50, 300) <b>[1]</b>',
    'Straight line from (50, 300) to (70, 400), visibly <b>less steep</b> than the first section <b>[1]</b>'],
   'note':'The gradients are 10 m/s and 5 m/s, so the second sloped section must be noticeably shallower. A parallel final section loses that mark.'},
  {'n':'3','marks':4,'lines':['Three sentences, each containing a number <b>[1]</b>',
    'Section 1 described with distance or speed: 300 m in 30 s, at 10 m/s <b>[1]</b>',
    'The stop described with its duration: stationary for 20 s <b>[1]</b>',
    'Section 3 described: a further 100 m in 20 s, at 5 m/s <b>[1]</b>']},
  {'n':'4','marks':4,'lines':['Total distance = 20 + 30 = 50 km <b>[1]</b>',
    'Total time = 0.5 + 1 = 1.5 h <b>[1]</b>','50 &divide; 1.5 <b>[1]</b>','= <b>33.3 km/h</b> <b>[1]</b>']},
  {'n':'5','marks':4,'lines':['Total distance = 15 + 10 = 25 km <b>[1]</b>',
    'Total time = 30 + 15 + 15 = 60 minutes = 1 h <b>[1]</b>','25 &divide; 1 <b>[1]</b>','= <b>25 km/h</b> <b>[1]</b>'],
   'note':'The rest must be included in the total time. Leaving it out gives 33.3 km/h.'},
  {'n':'6','marks':3,'lines':['The rest adds to the total time <b>[1]</b>','but adds nothing to the total distance <b>[1]</b>',
    'Average speed is total distance &divide; total time, so a larger bottom with the same top gives a smaller answer <b>[1]</b>']},
  {'n':'7','marks':3,'lines':['12 &times; 3.6 = 43.2 km/h <b>[1]</b> (or 40 &divide; 3.6 = 11.1 m/s) <b>[1]</b>',
    '<b>12 m/s is faster</b> <b>[1]</b>'],
   'note':'Either conversion direction is fine, provided both speeds end up in the same unit before they are compared.'},
  {'n':'8','marks':3,'lines':['The gradient represents the <b>speed</b> of the object <b>[1]</b>',
    'Pick two points where the line crosses gridlines exactly and read off their coordinates <b>[1]</b>',
    'Divide the change in distance by the change in time, using the axis values rather than counting squares <b>[1]</b>']},
 ]},

 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) 60 &divide; 60 = <b>1 h</b> <b>[1]</b>; 60 &divide; 120 = <b>0.5 h</b> <b>[1]</b>',
    '(b) Total 120 km in 1.5 h <b>[1]</b>; 120 &divide; 1.5 = <b>80 km/h</b> <b>[1]</b>',
    '(c) The car spends twice as long at the slower speed, so 60 km/h counts for more of the journey than 120 km/h does <b>[1]</b>']},
  {'n':'2','marks':5,'lines':['(a) Distance = <b>1000 m</b> <b>[1]</b>; time = 50 + 200 = <b>250 s</b> <b>[1]</b>',
    '(b) 1000 &divide; 250 <b>[1]</b> = <b>4 m/s</b> <b>[1]</b>',
    '(c) He spends four times as long walking as running, so the slow speed dominates; the answer is much closer to 2.5 than to 10 <b>[1]</b>'],
   'note':'Averaging the two speeds gives 6.25 m/s, more than half as big again as the truth.'},
  {'n':'3','marks':4,'lines':['(a) 330 &times; 6 <b>[1]</b> = <b>1980 m</b> <b>[1]</b>','(b) <b>1.98 km</b> <b>[1]</b>',
    '(c) Light travels roughly a million times faster than sound, so it covers 1980 m in a tiny fraction of a second — far too short to notice <b>[1]</b>']},
  {'n':'4','marks':4,'lines':['15 m/s = 15 &times; 3.6 = 54 km/h <b>[1]</b>',
    '840 m/min = 840 &divide; 60 = 14 m/s <b>[1]</b>, which is 14 &times; 3.6 = 50.4 km/h <b>[1]</b>',
    'Order: <b>50 km/h, 840 m/min, 15 m/s</b> <b>[1]</b>'],
   'note':'The two slowest differ by only 0.4 km/h, so this cannot be settled by eye. Working is essential.'},
  {'n':'5','marks':5,'lines':['(a) Total time allowed = <b>4 h</b> <b>[1]</b>; time used = 100 &divide; 50 = <b>2 h</b> <b>[1]</b>',
    '(b) 200 km still to travel, in 2 h remaining <b>[1]</b>',
    '(c) 200 &divide; 2 <b>[1]</b> = <b>100 km/h</b> <b>[1]</b>'],
   'note':'The first line of any target-average question should be total distance &divide; target speed. Everything else follows from that time budget.'},
  {'n':'6','marks':3,'lines':['The two parts of the journey almost never take the same amount of time <b>[1]</b>',
    'More time is spent travelling at the slower speed <b>[1]</b>',
    'so the slower speed counts for more, and the true average is always closer to it than the midpoint is <b>[1]</b>']},
  {'n':'7','marks':4,'lines':['The fastest section is the last one: 6 km between 15 and 20 minutes <b>[1]</b>',
    '5 minutes = 1/12 h <b>[1]</b>','6 &divide; (1/12) <b>[1]</b>','= <b>72 km/h</b> <b>[1]</b>'],
   'note':'Identifying the right section matters as much as the arithmetic. The first two sections are 3 km per 5 minutes; the third is a stop.'},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) 1000 &divide; 5 = <b>200 s</b> <b>[1]</b>',
    '(b) Time used = 400 &divide; 4 = <b>100 s</b> <b>[1]</b>; time remaining = 200 &minus; 100 = <b>100 s</b> <b>[1]</b>',
    '(c) 600 m in 100 s <b>[1]</b> = <b>6 m/s</b> <b>[1]</b>'],
   'note':'She must run the last 600 m half as fast again as the first 400 m, simply to lift her average by 1 m/s.'},
  {'n':'2','marks':5,'lines':['(a) 120 km in 2 h <b>[1]</b> = <b>60 km/h</b> <b>[1]</b>',
    '(b) Times are 1 h and 0.5 h, so 80 km in 1.5 h <b>[1]</b> = <b>53.3 km/h</b> <b>[1]</b>',
    '(c) Driver A spends equal <i>times</i> at the two speeds, so the average is the midpoint. Driver B covers equal <i>distances</i>, which means longer spent at the slow speed, pulling the average below the midpoint <b>[1]</b>'],
   'note':'This is the cleanest illustration in the topic of why "it depends what is being shared equally".'},
  {'n':'3','marks':4,'lines':['The car gains on the lorry at 25 &minus; 20 = 5 m/s <b>[1]</b> <b>[1]</b>',
    '100 &divide; 5 <b>[1]</b>','= <b>20 s</b> <b>[1]</b>'],
   'note':'Award both opening marks for any clear statement that only the difference in speeds matters.'},
  {'n':'4','marks':4,'lines':['The sound travels to the cliff and back, so it covers twice the distance <b>[1]</b>',
    'Total distance = 340 &times; 3 = 1020 m <b>[1]</b> <b>[1]</b>','Distance to the cliff = 1020 &divide; 2 = <b>510 m</b> <b>[1]</b>'],
   'note':'Answering 1020 m scores three of four. The halving is the entire point of an echo question.'},
  {'n':'5','marks':4,'lines':['72 &divide; 3.6 = 20 m/s <b>[1]</b> <b>[1]</b>','20 &times; 90 <b>[1]</b>','= <b>1800 m</b> <b>[1]</b>'],
   'note':'Alternative route: 90 s = 0.025 h, and 72 &times; 0.025 = 1.8 km. Full marks either way.'},
  {'n':'6','marks':4,'lines':[
    '(a) The straight line means a <b>constant speed</b> <b>[1]</b>; the curve getting steeper means the object is <b>speeding up</b> <b>[1]</b>',
    '(b) Compare the steepness of the two lines at the end of the journey <b>[1]</b>; whichever is steeper there has the greater gradient and so the greater speed at that moment <b>[1]</b>']},
  {'n':'7','marks':4,'lines':[
    '(i) The mistake: dividing by 20 without converting minutes into hours <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;20 min = 1/3 h, so the speed is 30 &divide; (1/3) = <b>90 km/h</b> <b>[1]</b>',
    '(ii) The mistake: a flat line means the distance is not changing, so the car is <b>stationary</b>, not moving steadily <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;A constant speed is shown by a straight line that <b>slopes</b> <b>[1]</b>']},
 ]},
]

files = []
for spec, code in [(A,'a'), (B,'b'), (C,'c'), (D,'d')]:
    t = sum(q.get('marks',0) for q in spec['questions'])
    assert t == 30, (spec['title'], t)
    p = os.path.join(OUT, 'physics-speed-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)
for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)
p = os.path.join(OUT, 'physics-speed-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Award method marks for a correct '
             'formula and a correct substitution even when the arithmetic fails. Almost every mark lost on '
             'this topic goes one of three ways: minutes treated as decimals of an hour, the m/s to km/h '
             'factor applied backwards, or two speeds averaged when the journey should have been. '
             'The notes under each answer flag the specific mistake that question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
