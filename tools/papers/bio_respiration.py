#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Biology · Grade 7 · Gas exchange in humans'
TOPIC = 'Breathing In, Breathing Out'

BASE = [
 'Answer <b>every</b> question in the space provided.',
 'A calculator is allowed, but every number here is designed to work without one.',
 'Where a question asks about air moving in or out, your answer must follow the chain in order: '
 '<b>muscles change the volume, the volume change causes a pressure change, air then flows down the '
 'pressure gradient.</b> A muscle never sucks or pushes air by itself.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + ['You may need: <b>1000 cm<super>3</super> = 1 dm<super>3</super></b>.']
INSTR_HARD = BASE + [
 'Several questions here describe experiments and data you may not have seen before. You are not '
 'expected to recognise them — apply the ideas you already have.',
 'Never write that respiration takes place in the lungs. Respiration is a reaction inside cells; '
 'the lungs carry out ventilation and gas exchange.',
]

# ---------------------------------------------------------------- Paper A

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — air in, air out',
   'text':'Complete the table to describe quiet breathing. Each empty box is worth one mark.','marks':6,
   'grid':[['','Breathing in','Breathing out'],
           ['Diaphragm','contracts and flattens',''],
           ['Ribs','','move down and in'],
           ['Volume of thorax','',''],
           ['Pressure in lungs','falls',''],
           ['Air','','flows out']],
   'grid_widths':[AVAIL*0.30, AVAIL*0.35, AVAIL*0.35]},

  {'text':'Name the structure described in each case.','marks':4,
   'parts':[{'label':'(a)','text':'The tube from the throat down towards the lungs, held open by rings of cartilage.','marks':1,'space':14},
            {'label':'(b)','text':'The two tubes that carry air from that tube, one into each lung.','marks':1,'space':14},
            {'label':'(c)','text':'The tiny air sacs where gases are exchanged with the blood.','marks':1,'space':14},
            {'label':'(d)','text':'The sheet of muscle below the lungs that flattens when you breathe in.','marks':1,'space':14}]},

  {'text':'Breathing and respiration are not the same thing. Write one sentence about each to say '
          'what it is and where in the body it happens.','marks':2,'space':34,
   'tip':'One sentence each. If both your sentences mention the lungs, one of them is wrong.'},

  {'section':'Section 2 — where the swap happens',
   'text':'Give three features of an alveolus that make gas exchange fast.','marks':3,'space':34},

  {'text':'Answer these three questions about diffusion at an alveolus.','marks':3,
   'parts':[{'label':'(a)','text':'Name the gas that diffuses from the air in the alveolus into the blood.','marks':1,'space':14},
            {'label':'(b)','text':'Name the gas that diffuses in the opposite direction.','marks':1,'space':14},
            {'label':'(c)','text':'State what both of these movements have in common.','marks':1,'space':16}]},

  {'text':'The inside of an alveolus is coated with a thin film of liquid. Explain why a gas exchange '
          'surface has to be moist.','marks':2,'space':28},

  {'section':'Section 3 — the reaction, and the evidence for it',
   'text':'Answer these questions about aerobic respiration.','marks':3,
   'parts':[{'label':'(a)','text':'Complete the word equation:<br/><br/>'
             '<font name="Mono" size="10">glucose &nbsp;+ &nbsp;__________ &nbsp;&rarr; &nbsp;__________ &nbsp;+ &nbsp;water</font>',
             'marks':2,'space':16},
            {'label':'(b)','text':'Name the part of the cell in which the reaction takes place.','marks':1,'space':14}],
   'tip':'Write that energy is <i>released</i>, never that it is made or produced.'},

  {'text':'Name the liquid used to test for carbon dioxide, and state what you would see when a person '
          'breathes out through it.','marks':2,'space':24},

  {'text':'Complete the table of gas percentages. Each empty box is worth one mark.','marks':3,
   'grid':[['Gas','Inspired air','Expired air'],
           ['Oxygen','21%',''],
           ['Carbon dioxide','','4%'],
           ['Nitrogen','78%','']],
   'grid_widths':[AVAIL*0.34, AVAIL*0.33, AVAIL*0.33]},

  {'text':'State the two things about a person&rsquo;s breathing that change when they start to exercise.',
   'marks':2,'space':24},
 ]}

# ---------------------------------------------------------------- Paper B

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — what goes in is not what comes out',
   'text':'The table shows the composition of inspired and expired air.<br/><br/>'
          '<font name="Mono" size="9.4">Gas &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Inspired &nbsp; &nbsp;Expired<br/>'
          'Oxygen &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;21% &nbsp; &nbsp; &nbsp; &nbsp; 16%<br/>'
          'Carbon dioxide &nbsp; &nbsp;0.04% &nbsp; &nbsp; &nbsp; 4%<br/>'
          'Nitrogen &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;78% &nbsp; &nbsp; &nbsp; &nbsp; 78%</font>','marks':5,
   'parts':[{'label':'(a)','text':'Name the gas whose percentage does not change, and explain why it does not.','marks':2,'space':24},
            {'label':'(b)','text':'Calculate how many times more carbon dioxide there is in expired air than in inspired air.','marks':1,'space':18},
            {'label':'(c)','text':'State by how many percentage points the oxygen falls.','marks':1,'space':14},
            {'label':'(d)','text':'Name one way, not shown in the table, in which expired air differs from inspired air.','marks':1,'space':14}]},

  {'text':'A student blows through a tube into a flask of limewater. A second flask of limewater has '
          'ordinary room air drawn through it at the same rate.','marks':3,
   'parts':[{'label':'(a)','text':'State what happens in the flask the student blows into.','marks':1,'space':16},
            {'label':'(b)','text':'The second flask changes too, but takes far longer. Explain why.','marks':2,'space':26}]},

  {'section':'Section 2 — the airways',
   'text':'The trachea and bronchi are lined with goblet cells and ciliated cells. Describe how these '
          'two cell types work together to keep the lungs clean.','marks':3,'space':36},

  {'text':'The trachea is held open by C-shaped rings of cartilage. Explain what would happen when you '
          'breathed in hard if these rings were not there.','marks':2,'space':28},

  {'text':'Give two reasons why breathing in through the nose is better for the lungs than breathing in '
          'through the mouth.','marks':2,'space':26},

  {'section':'Section 3 — breathing and exercise',
   'text':'At rest, Nikhil takes 12 breaths each minute and moves 500 cm<super>3</super> of air with '
          'every breath. While he is running he takes 24 breaths each minute and moves 2000 cm<super>3</super> '
          'with every breath.','marks':6,
   'parts':[{'label':'(a)','text':'Calculate the volume of air he breathes each minute at rest. Give your answer in dm<super>3</super>.','marks':2,'space':26},
            {'label':'(b)','text':'Calculate the volume of air he breathes each minute while running, in dm<super>3</super>.','marks':2,'space':26},
            {'label':'(c)','text':'State how many times greater the running value is, and name the two things about his breathing that changed.','marks':2,'space':26}],
   'tip':'Work in cm<super>3</super> throughout, then convert once at the very end. Mixing the two units halfway is the usual way marks are lost here.'},

  {'text':'Explain, step by step, why breathing becomes faster and deeper during exercise. Begin with '
          'what the muscles are doing.','marks':4,'space':48},

  {'text':'A student wants to measure her resting breathing rate accurately. Describe how she should do '
          'it, and give two things she must keep the same each time she repeats the measurement.','marks':3,'space':38},

  {'text':'Explain why expired air is warmer and carries more water vapour than the air that was '
          'breathed in.','marks':2,'space':28},
 ]}

# ---------------------------------------------------------------- Paper C

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — the size of the surface',
   'text':'An adult lung holds about 3.0 &times; 10<super>8</super> alveoli. Each alveolus has a surface '
          'area of about 1.6 &times; 10<super>&minus;7</super> m<super>2</super>. A single smooth sac holding '
          'the same volume of air would have a surface area of 0.06 m<super>2</super>.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the total surface area of the alveoli, in m<super>2</super>.','marks':2,'space':30},
            {'label':'(b)','text':'Calculate how many times larger this is than the single smooth sac.','marks':1,'space':20},
            {'label':'(c)','text':'Explain why dividing the same volume of lung into millions of tiny sacs speeds up gas exchange.','marks':2,'space':28}],
   'tip':'Multiply the numbers in front first, then add the powers of ten.'},

  {'text':'Oxygen crosses about 1 micrometre of tissue on its way from alveolar air into the blood.','marks':3,
   'parts':[{'label':'(a)','text':'One micrometre is one millionth of a metre. Write this distance in metres, in standard form.','marks':1,'space':18},
            {'label':'(b)','text':'A disease thickens this barrier so that oxygen must cross twice the distance. Explain the effect on the person.','marks':2,'space':30}]},

  {'section':'Section 2 — reading something you have not seen before',
   'text':'A <b>spirometer</b> records the volume of air a person breathes as a moving trace on a chart. '
          'A trace taken while a patient sat still showed 6 complete breaths in 30 seconds, and each '
          'breath moved 0.45 dm<super>3</super> of air.','marks':6,
   'parts':[{'label':'(a)','text':'State the volume of air moved in one breath. This is called the tidal volume.','marks':1,'space':16},
            {'label':'(b)','text':'Calculate the patient&rsquo;s breathing rate, in breaths per minute.','marks':1,'space':20},
            {'label':'(c)','text':'Calculate the total volume of air breathed in one minute, in dm<super>3</super>.','marks':2,'space':28},
            {'label':'(d)','text':'The patient then walks on a treadmill. Describe the two ways the trace would change, and say what each one shows.','marks':2,'space':30}]},

  {'text':'A model of the thorax is built from a sealed glass bell jar with a rubber sheet stretched '
          'across its open base, and two balloons hanging inside from a Y-shaped tube through the lid. '
          'Pulling the rubber sheet downwards makes the balloons inflate.','marks':4,
   'parts':[{'label':'(a)','text':'State what the rubber sheet, the glass jar and the balloons each represent in a real person.','marks':3,'space':34},
            {'label':'(b)','text':'Give one way in which the model is unlike a real thorax.','marks':1,'space':18}]},

  {'section':'Section 3 — when the oxygen runs short',
   'text':'A sprinter runs 200 m flat out.','marks':3,
   'parts':[{'label':'(a)','text':'Write the word equation for the respiration taking place in her leg muscles near the end of the race.','marks':1,'space':18},
            {'label':'(b)','text':'Give one advantage and one disadvantage of this type of respiration compared with aerobic respiration.','marks':2,'space':28}]},

  {'text':'She stands bent over, breathing hard, for almost a minute after she has stopped running. '
          'Explain why, using the term <b>oxygen debt</b>.','marks':3,'space':38},

  {'text':'Two students measure their breathing rates, in breaths per minute, before exercise, at the '
          'end of exercise, and three minutes after stopping.<br/><br/>'
          '<font name="Mono" size="9.4">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Before &nbsp; At the end &nbsp; After 3 min<br/>'
          'Student P &nbsp; &nbsp;16 &nbsp; &nbsp; &nbsp; &nbsp;40 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;17<br/>'
          'Student Q &nbsp; &nbsp;20 &nbsp; &nbsp; &nbsp; &nbsp;45 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;30</font>','marks':6,
   'parts':[{'label':'(a)','text':'Calculate the percentage increase in Student P&rsquo;s breathing rate during exercise.','marks':2,'space':28},
            {'label':'(b)','text':'State which student is fitter, and give two reasons from the data.','marks':2,'space':28},
            {'label':'(c)','text':'Both students are still above their resting rate at the end of exercise. Explain why breathing does not return to normal the moment exercise stops.','marks':2,'space':30}],
   'tip':'Percentage increase is measured against the value you started from, not the value you finished on.'},
 ]}

# ---------------------------------------------------------------- Paper D

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — a lung that stops working',
   'text':'In a long-term smoker the walls between neighbouring alveoli break down, so many small '
          'alveoli merge into fewer, much larger sacs. This is emphysema. One patient&rsquo;s total gas '
          'exchange surface falls from 50 m<super>2</super> to 20 m<super>2</super>.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the percentage fall in his gas exchange surface area.','marks':2,'space':28},
            {'label':'(b)','text':'Explain the effect this has on gas exchange, and what the patient would notice when he climbs a flight of stairs.','marks':3,'space':40}]},

  {'text':'Tobacco smoke also contains carbon monoxide, which binds to haemoglobin in red blood cells '
          'far more readily than oxygen does, and does not let go.','marks':4,
   'parts':[{'label':'(a)','text':'Explain why this reduces the amount of oxygen the blood can deliver, even from healthy alveoli.','marks':2,'space':30},
            {'label':'(b)','text':'At rest this patient&rsquo;s blood delivers 12% less oxygen than it should. If it should deliver 250 cm<super>3</super> of oxygen each minute, calculate how much it actually delivers.','marks':2,'space':30}]},

  {'text':'Tar in the smoke paralyses and then destroys the cilia lining the airways. Predict two things '
          'that happen as a result, and explain each one.','marks':3,'space':40},

  {'section':'Section 2 — the whole chain, end to end',
   'text':'Describe and explain the complete journey of an oxygen molecule from the air just outside a '
          'person&rsquo;s nose to a mitochondrion inside a muscle cell in her leg. Name the structures it '
          'passes through and explain what makes it move at each stage.','marks':6,'space':84,
   'tip':'Six marks means at least six separate ideas. Plan the order of the structures in the margin before you begin writing.'},

  {'text':'High in the mountains the air is still 21% oxygen, but the air pressure is much lower, so each '
          'breath contains fewer oxygen molecules. A climber who arrives at 4000 m breathes faster and '
          'more deeply than at sea level, even when sitting still.','marks':4,
   'parts':[{'label':'(a)','text':'Explain why breathing faster and more deeply helps the climber.','marks':2,'space':28},
            {'label':'(b)','text':'After two weeks at altitude the climber makes more red blood cells than before. Explain how this helps.','marks':2,'space':28}]},

  # section titles are passed through .upper(), which would mangle an HTML entity
  # into &RSQUO; — use the literal character here, not &rsquo;
  {'section':'Section 3 — marking someone else’s work',
   'text':'Complete the comparison of the two types of respiration. Each empty box is worth one mark.',
   'marks':3,
   'grid':[['','Aerobic','Anaerobic (in muscle)'],
           ['Oxygen needed?','yes',''],
           ['Products','carbon dioxide + water',''],
           ['Energy released','','much less']],
   'grid_widths':[AVAIL*0.28, AVAIL*0.36, AVAIL*0.36]},

  {'text':'Another student has answered two questions on this topic. Both answers are wrong. For each '
          'one, state the mistake and write out a correct version.<br/><br/>'
          '<font name="Body-Italic" size="10.4">(i) &ldquo;Respiration takes place in the lungs, where '
          'oxygen is turned into carbon dioxide.&rdquo;<br/><br/>'
          '(ii) &ldquo;When you breathe out, the diaphragm pushes down on the lungs and forces the air '
          'out of them.&rdquo;</font>','marks':5,'space':78,
   'tip':'Each one has more than one thing wrong with it. Deal with them separately.'},
 ]}

# ---------------------------------------------------------------- mark schemes

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':6,'lines':[
    'Diaphragm, breathing out: <b>relaxes and domes upwards</b>',
    'Ribs, breathing in: <b>move up and out</b>',
    'Volume of thorax: breathing in <b>increases</b>; breathing out <b>decreases</b>',
    'Pressure in lungs, breathing out: <b>rises</b> (above atmospheric)',
    'Air, breathing in: <b>flows in</b>'],
   'note':'One mark per box. "The diaphragm pushes up" is not the same as "relaxes" — relaxing is what earns '
          'the mark, and a student who writes push has the muscle doing something it cannot do.'},
  {'n':'2','marks':4,'lines':['(a) <b>Trachea</b>','(b) <b>Bronchi</b> (one bronchus per lung)',
    '(c) <b>Alveoli</b>','(d) <b>Diaphragm</b>'],
   'note':'Accept windpipe for trachea. Do not accept "lungs" for (c) — the question asks for the sacs.'},
  {'n':'3','marks':2,'lines':[
    'Breathing (ventilation) is the movement of air into and out of the lungs, done by muscles <b>[1]</b>',
    'Respiration is a chemical reaction that releases energy from glucose, and it happens in every cell '
    'of the body, in the mitochondria <b>[1]</b>'],
   'note':'The single most examined distinction in this topic. If the answer places respiration in the lungs, '
          'award nothing for the second mark however well it is written.'},
  {'n':'4','marks':3,'lines':['Any three, one mark each: <b>very large total surface area</b>; '
    '<b>wall only one cell thick</b> (short diffusion distance); <b>moist lining</b>; '
    '<b>dense network of capillaries</b> / good blood supply maintaining the concentration gradient; '
    '<b>constantly ventilated</b>'],
   'note':'"They are small" on its own scores nothing — smallness matters because of what it does to the '
          'surface area, and the answer has to say so.'},
  {'n':'5','marks':3,'lines':['(a) <b>Oxygen</b>','(b) <b>Carbon dioxide</b>',
    '(c) Both move by <b>diffusion, from where they are in higher concentration to where they are in lower '
    'concentration</b> — each down its own gradient'],
   'note':'A common half-answer to (c) is "they both go through the wall". That is where, not why.'},
  {'n':'6','marks':2,'lines':['Gases must <b>dissolve in the liquid film</b> before they can diffuse across '
    'the cell membranes <b>[1]</b>',
    'so a dry surface would slow gas exchange down, or stop it <b>[1]</b>'],
   'note':'Links directly to why a fish drowns in air — same idea, different animal.'},
  {'n':'7','marks':3,'lines':[
    '(a) glucose + <b>oxygen</b> &rarr; <b>carbon dioxide</b> + water <b>[2]</b> (one mark per gap)',
    '(b) <b>Mitochondria</b> <b>[1]</b>'],
   'note':'If the student has added "energy" as a product in the equation, do not deduct here, but write '
          '"released, not produced" in the margin — it costs marks in worded questions later.'},
  {'n':'8','marks':2,'lines':['<b>Limewater</b> <b>[1]</b>',
    'It turns <b>milky / cloudy</b>, and does so within a few breaths <b>[1]</b>'],
   'note':'"It goes white" is acceptable; "it changes colour" alone is not specific enough.'},
  {'n':'9','marks':3,'lines':['Oxygen, expired: <b>16%</b>','Carbon dioxide, inspired: <b>0.04%</b>',
    'Nitrogen, expired: <b>78%</b>'],
   'note':'The nitrogen box is the one that catches people out — many students change it because every other '
          'box changed. Nitrogen is not used by the body at all.'},
  {'n':'10','marks':2,'lines':['The <b>rate</b> of breathing increases — more breaths per minute <b>[1]</b>',
    'The <b>depth</b> of breathing increases — more air moved per breath <b>[1]</b>'],
   'note':'Two marks, two distinct changes. "He breathes more" is one idea written twice.'},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':[
    '(a) <b>Nitrogen</b> <b>[1]</b>; it is not used by the body in any reaction, so the same amount is '
    'breathed out as was breathed in <b>[1]</b>',
    '(b) 4 &divide; 0.04 = <b>100 times more</b> <b>[1]</b>',
    '(c) <b>5 percentage points</b> (21% to 16%) <b>[1]</b>',
    '(d) Any one of: expired air is <b>warmer</b>; expired air is <b>saturated with water vapour</b> <b>[1]</b>'],
   'note':'In (b) the arithmetic 4 &divide; 0.04 defeats a lot of students because of the decimal. If the answer '
          'is 10 or 1000, the method mark is still there — the error is place value, and it is worth saying so.'},
  {'n':'2','marks':3,'lines':['(a) The limewater turns <b>milky / cloudy</b>, and quite quickly <b>[1]</b>',
    '(b) Room air contains far less carbon dioxide — about 0.04% against about 4% in expired air <b>[1]</b>; '
    'so it takes about a hundred times as much air, and therefore far longer, to produce the same change <b>[1]</b>'],
   'note':'The second flask does eventually go cloudy. An answer claiming "nothing happens" has misread the '
          'experiment and cannot have the explanation mark.'},
  {'n':'3','marks':3,'lines':['<b>Goblet cells secrete mucus</b> <b>[1]</b>',
    'which <b>traps dust, pollen and bacteria</b> in the air breathed in <b>[1]</b>',
    '<b>Cilia beat and sweep the dirty mucus up the trachea</b> to the throat, where it is swallowed, '
    'keeping the airways clear <b>[1]</b>'],
   'note':'Both cell types must appear. An answer that only describes mucus has done half the job and gets '
          'at most two.'},
  {'n':'4','marks':2,'lines':['Breathing in hard lowers the pressure inside the trachea <b>[1]</b>',
    'so without the cartilage rings the tube would be <b>squashed shut</b> by the higher pressure outside '
    'and air could not reach the lungs <b>[1]</b>'],
   'note':'The straw-in-a-thick-milkshake image from the page is a legitimate way to earn the second mark if '
          'the physics behind it is stated.'},
  {'n':'5','marks':2,'lines':['Any two, one mark each: the nose <b>warms</b> the air; the nose <b>moistens</b> '
    'the air, which matters because gases diffuse across a moist surface; nose hairs and mucus <b>filter '
    'out dust and bacteria</b>'],
   'note':'Three valid answers exist and only two are needed, so this should be two easy marks. If it is not, '
          'the lesson on the airways has not been read.'},
  {'n':'6','marks':6,'lines':[
    '(a) 12 &times; 500 = 6000 cm<super>3</super> per minute <b>[1]</b> = <b>6 dm<super>3</super> per minute</b> <b>[1]</b>',
    '(b) 24 &times; 2000 = 48 000 cm<super>3</super> per minute <b>[1]</b> = <b>48 dm<super>3</super> per minute</b> <b>[1]</b>',
    '(c) 48 &divide; 6 = <b>8 times greater</b> <b>[1]</b>; both the <b>rate</b> (12 &rarr; 24 breaths per minute) '
    'and the <b>depth</b> (500 &rarr; 2000 cm<super>3</super> per breath) increased <b>[1]</b>'],
   'note':'Award the first mark of (a) and (b) for the multiplication even if the conversion is missing or '
          'wrong — the conversion is the second mark and is where this question is usually lost.'},
  {'n':'7','marks':4,'lines':['The muscles <b>respire faster</b> to release more energy for contraction <b>[1]</b>',
    'so they use more oxygen and produce <b>more carbon dioxide</b>, which raises the carbon dioxide '
    'concentration in the blood <b>[1]</b>',
    'This rise is <b>detected by the brain</b> <b>[1]</b>',
    'which increases both the <b>rate and the depth</b> of breathing, so oxygen is delivered and carbon '
    'dioxide removed faster <b>[1]</b>'],
   'note':'It is the rising carbon dioxide, not the falling oxygen, that triggers the change. An answer built '
          'entirely on "the body needs more oxygen" describes the purpose but never gives the mechanism, and '
          'tops out at two.'},
  {'n':'8','marks':3,'lines':[
    'Count the number of breaths in a <b>full minute</b> (or count for 30 s and double it), sitting still <b>[1]</b>',
    '<b>Repeat and take a mean</b> to reduce the effect of an unusual reading <b>[1]</b>',
    'Any two kept the same, for one mark: <b>same time of day</b>; <b>same position</b> (sitting, not standing); '
    '<b>no exercise beforehand</b>; <b>same room temperature</b> <b>[1]</b>'],
   'note':'Watch for the student who counts "in and out" as two breaths. It is one.'},
  {'n':'9','marks':2,'lines':['The air is warmed by the body as it passes through the nose and airways, so it '
    'leaves at close to body temperature <b>[1]</b>',
    'and it picks up water vapour from the moist lining of the airways and alveoli, so it leaves '
    'saturated <b>[1]</b>'],
   'note':'Both marks are about the air being conditioned on the way through, not about respiration producing '
          'water — although the water produced in respiration does contribute, and should not be marked wrong.'},
 ]},

 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':[
    '(a) 3.0 &times; 1.6 = 4.8 and 10<super>8</super> &times; 10<super>&minus;7</super> = 10<super>1</super> <b>[1]</b>, '
    'so the total is 4.8 &times; 10<super>1</super> = <b>48 m<super>2</super></b> <b>[1]</b>',
    '(b) 48 &divide; 0.06 = <b>800 times larger</b> <b>[1]</b>',
    '(c) Diffusion is faster across a larger surface area <b>[1]</b>; dividing the lung into millions of tiny '
    'sacs multiplies the area available without the chest getting any bigger <b>[1]</b>'],
   'note':'The powers of ten are the whole difficulty in (a). A student who writes 4.8 without the power has '
          'the method and loses only the second mark.'},
  {'n':'2','marks':3,'lines':['(a) <b>1 &times; 10<super>&minus;6</super> m</b> <b>[1]</b>',
    '(b) The diffusion distance is doubled, so oxygen crosses into the blood more slowly <b>[1]</b>; less '
    'oxygen reaches the blood each minute, so the person becomes breathless and tires quickly, especially '
    'when exercising <b>[1]</b>'],
   'note':'(b) needs a consequence for the person, not only for the molecule. An answer that stops at '
          '"diffusion is slower" has answered half the question.'},
  {'n':'3','marks':6,'lines':['(a) <b>0.45 dm<super>3</super></b> <b>[1]</b>',
    '(b) 6 breaths in 30 s, so <b>12 breaths per minute</b> <b>[1]</b>',
    '(c) 12 &times; 0.45 <b>[1]</b> = <b>5.4 dm<super>3</super> per minute</b> <b>[1]</b>',
    '(d) The trace becomes <b>taller</b>, showing a greater tidal volume / deeper breaths <b>[1]</b>, and the '
    'peaks come <b>closer together</b>, showing a faster breathing rate <b>[1]</b>'],
   'note':'In (d) many students give two versions of "he breathes more". Insist on one statement about height '
          'and one about spacing — depth and rate are separate measurements and the spirometer shows them '
          'separately.'},
  {'n':'4','marks':4,'lines':[
    '(a) Rubber sheet = <b>diaphragm</b> <b>[1]</b>; glass jar = <b>rib cage / thorax</b> <b>[1]</b>; '
    'balloons = <b>lungs</b> <b>[1]</b>',
    '(b) Any one: the glass jar <b>cannot change shape</b>, whereas real ribs move up and out; there are no '
    '<b>intercostal muscles</b> in the model; the balloons have <b>no alveoli</b>, so no gas exchange takes '
    'place; the rubber sheet is <b>pulled by hand</b> rather than contracting by itself <b>[1]</b>'],
   'note':'Almost everyone gets (a). (b) is the mark that separates, and it is where a student who has actually '
          'thought about the model shows it.'},
  {'n':'5','marks':3,'lines':['(a) glucose &rarr; <b>lactic acid</b> (energy released) <b>[1]</b>',
    '(b) Advantage: it releases energy <b>without needing oxygen</b>, so the muscles can keep working when '
    'oxygen cannot be delivered fast enough <b>[1]</b>. Disadvantage: it releases <b>far less energy</b> per '
    'glucose molecule and leaves <b>lactic acid</b>, which causes fatigue and pain <b>[1]</b>'],
   'note':'Carbon dioxide and water are not products of anaerobic respiration in muscle. Writing them there is '
          'the standard error and costs the first mark outright.'},
  {'n':'6','marks':3,'lines':['During the sprint her muscles respired anaerobically and built up <b>lactic '
    'acid</b> <b>[1]</b>',
    'Extra oxygen is needed to break that lactic acid down — this is the <b>oxygen debt</b> <b>[1]</b>',
    'so she keeps breathing hard after stopping until the debt has been repaid <b>[1]</b>'],
   'note':'"She is out of breath" is a description of what we can see, not an explanation. No marks for it.'},
  {'n':'7','marks':6,'lines':[
    '(a) Increase = 40 &minus; 16 = 24 <b>[1]</b>; (24 &divide; 16) &times; 100 = <b>150%</b> <b>[1]</b>',
    '(b) <b>Student P</b> <b>[1]</b>; two reasons from: P has the <b>lower resting rate</b> (16 against 20), '
    'and P has <b>almost fully recovered</b> after three minutes (17 against a resting 16) while Q is still '
    'far above resting (30 against 20) <b>[1]</b>',
    '(c) The muscles built up an <b>oxygen debt</b> during the exercise <b>[1]</b>; breathing must stay raised '
    'to supply the extra oxygen needed to remove the lactic acid before it can return to normal <b>[1]</b>'],
   'note':'In (a), dividing by 40 instead of 16 gives 60% — measuring the change against the value you finished '
          'on rather than the one you started from. Award the first mark only. This is the same trap as the '
          'percentage change work in the maths papers, in a biology costume.'},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':[
    '(a) Fall = 50 &minus; 20 = 30 m<super>2</super> <b>[1]</b>; (30 &divide; 50) &times; 100 = <b>60%</b> <b>[1]</b>',
    '(b) The surface area for gas exchange is much smaller, so <b>less oxygen diffuses into the blood each '
    'minute</b> <b>[1]</b>; his muscles cannot get enough oxygen for aerobic respiration <b>[1]</b>; so he '
    'becomes <b>breathless and has to stop part-way up the stairs</b> <b>[1]</b>'],
   'note':'Dividing by 20 rather than 50 gives 150% — an impossible answer, since a quantity cannot fall by more '
          'than 100%. Point that out rather than just marking it wrong; the check is free and he can do it '
          'himself next time.'},
  {'n':'2','marks':4,'lines':[
    '(a) Carbon monoxide binds to the haemoglobin and does not release it <b>[1]</b>, so fewer haemoglobin '
    'molecules are left free to carry oxygen and the blood carries less oxygen even though the lungs are '
    'working normally <b>[1]</b>',
    '(b) 12% of 250 = 30 cm<super>3</super> <b>[1]</b>; 250 &minus; 30 = <b>220 cm<super>3</super> per minute</b> <b>[1]</b>'],
   'note':'Accept 250 &times; 0.88 in one step for both marks. An answer of 30 has calculated the loss and '
          'forgotten to subtract it — one mark.'},
  {'n':'3','marks':3,'lines':['<b>Mucus is no longer swept out of the airways</b>, so it collects in the '
    'lungs <b>[1]</b>',
    'The smoker <b>coughs repeatedly</b> to shift it — smoker&rsquo;s cough <b>[1]</b>',
    'Trapped dust and bacteria stay in the lungs, so <b>chest infections become more frequent</b> <b>[1]</b>'],
   'note':'Any two clear consequences with explanations reach three marks. A bare list without reasons gets one.'},
  {'n':'4','marks':6,'lines':[
    'Into the <b>nose</b>, where the air is warmed, moistened and filtered <b>[1]</b>',
    'Down the <b>trachea</b>, into a <b>bronchus</b>, then a <b>bronchiole</b>, and into an <b>alveolus</b>; '
    'it moves because the diaphragm and intercostals contracted, increasing the volume of the thorax and '
    'lowering the pressure inside the lungs <b>[2]</b>',
    'Across the <b>alveolus wall and the capillary wall</b> — about 1 &micro;m of tissue, both one cell thick — '
    'by <b>diffusion</b>, because oxygen is at a higher concentration in the alveolar air than in the '
    'blood <b>[1]</b>',
    'It binds to <b>haemoglobin</b> in a red blood cell and is carried in the blood, pumped by the heart, to '
    'the leg muscle <b>[1]</b>',
    'It <b>diffuses out of the blood into the muscle cell</b>, down the concentration gradient, because the '
    'respiring cell keeps using oxygen up and so keeps its concentration low <b>[1]</b>'],
   'note':'This is the question that shows whether the topic has been joined up or learnt in pieces. Diffusion '
          'must be named at both ends, and a gradient must be explained at least once. An answer that lists the '
          'structures correctly but never says why the oxygen moves cannot go above three.'},
  {'n':'5','marks':4,'lines':[
    '(a) Each breath contains fewer oxygen molecules, so breathing faster and more deeply moves <b>more air, '
    'and therefore more oxygen, into the lungs each minute</b> <b>[1]</b>; this keeps the concentration '
    'gradient between alveolar air and blood as large as possible <b>[1]</b>',
    '(b) More red blood cells means more <b>haemoglobin</b> <b>[1]</b>, so the blood can carry more oxygen from '
    'each breath to the respiring cells <b>[1]</b>'],
   'note':'Nothing here has been taught directly — it is the alveolus material applied to an unfamiliar '
          'situation. Credit any answer that reaches the right idea by a different route.'},
  {'n':'6','marks':3,'lines':['Anaerobic, oxygen needed: <b>no</b>',
    'Anaerobic, products: <b>lactic acid</b>',
    'Aerobic, energy released: <b>much more</b> (per glucose molecule)'],
   'note':'One mark per box.'},
  {'n':'7','marks':5,'lines':[
    '(i) The mistakes: respiration does <b>not</b> take place in the lungs, and oxygen is <b>not</b> turned '
    'into carbon dioxide <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: respiration takes place in <b>every cell of the body</b>, in the '
    'mitochondria; the lungs carry out gas exchange <b>[1]</b>. The carbon in the carbon dioxide comes from '
    'the <b>glucose</b>, not from the oxygen — oxygen is a reactant, not raw material that is converted <b>[1]</b>',
    '(ii) The mistake: during exhalation the diaphragm <b>relaxes and moves up</b>; it does not push down, and '
    'muscles cannot push air at all <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: the diaphragm relaxes and domes upwards and the ribs move down and '
    'in, so the <b>volume of the thorax decreases</b>, the <b>pressure inside rises above atmospheric</b>, and '
    'air flows out down the pressure gradient <b>[1]</b>'],
   'note':'These are the two sentences this whole topic is built to prevent. Sentence (i) is the breathing / '
          'respiration confusion plus the "oxygen turns into carbon dioxide" error; sentence (ii) skips the '
          'volume and pressure steps entirely. Marking them in someone else&rsquo;s work is the same cognitive '
          'job as not writing them, and far easier to face.'},
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
    p = os.path.join(OUT, 'biology-respiration-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)

for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)

p = os.path.join(OUT, 'biology-respiration-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Almost every mark lost on this topic is '
             'lost to language rather than to knowledge, and always in the same three places: putting '
             'respiration in the lungs, giving a muscle the job that pressure does, and describing a feature '
             'without saying what it achieves. Three phrases are worth insisting on &mdash; "in every cell, in '
             'the mitochondria", "the volume changes, so the pressure changes, so the air moves", and "down the '
             'concentration gradient". The notes under each answer name the specific mistake that question was '
             'built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
