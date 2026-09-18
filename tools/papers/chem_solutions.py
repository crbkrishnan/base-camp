#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Chemistry · Grade 7 · Unit 5.3 · Solutions and solubility'
TOPIC = 'Solutions and Solubility'

# ---- the solubility table, g per 100 g water, identical to the one on solutions.html ----
SOL = {
 'kno3':  {0:13, 10:21, 20:32, 30:46, 40:64, 50:86, 60:110, 70:138, 80:169, 90:202, 100:246},
 'cuso4': {0:14, 10:17, 20:21, 30:25, 40:29, 50:33, 60:40, 70:47, 80:55, 90:64, 100:75},
 'nacl':  {0:36, 10:36, 20:36, 30:36, 40:37, 50:37, 60:37, 70:38, 80:38, 90:39, 100:40},
}
def sol(s, t): return SOL[s][t]
def scaled(s, t, water): return sol(s, t) * water / 100.0
def crystals(s, hot, cold, water=100): return scaled(s, hot, water) - scaled(s, cold, water)

# ---- every number on these papers, computed here and read from here (CLAUDE.md #6) ----
N = {
 'A5_mass':     80 + 20,                          # 100 g
 'A7_left':     40 - sol('kno3', 20),             # 8 g undissolved
 'B2_25g':      scaled('kno3', 40, 25),           # 16 g
 'B2_250g':     scaled('kno3', 40, 250),          # 160 g
 'B3_cuso4_60': sol('cuso4', 60),                 # 40
 'B3_kno3_30':  sol('kno3', 30),                  # 46 — so 30 g at 30 °C is unsaturated
 'B3_extra':    sol('kno3', 30) - 30,             # 16 g more would dissolve
 'B4_cryst':    crystals('kno3', 60, 20),         # 110 - 32 = 78
 'C2_left_P':   50 - sol('nacl', 20),             # 14
 'C2_left_A':   50 - sol('nacl', 80),             # 12
 'C2_gain':     sol('nacl', 80) - sol('nacl', 20),# 2
 'C4_hot50':    scaled('kno3', 60, 50),           # 55
 'C4_cold50':   scaled('kno3', 20, 50),           # 16
 'C4_cryst':    crystals('kno3', 60, 20, 50),     # 39
 'C5_cu_200':   crystals('cuso4', 80, 20, 200),   # (55-21)*2 = 68
 'D1_kno3_70':  sol('kno3', 70),                  # 138
 'D1_cryst':    crystals('kno3', 80, 40),         # 169-64 = 105
 'D1_nacl':     crystals('nacl', 100, 0),         # 4
 'D3_total':    150 + 30,                         # 180
 'D3_left':     30 - scaled('cuso4', 20, 150),    # 30 - 31.5 -> negative, so all dissolves; see assert
 'D3_cap':      scaled('cuso4', 20, 150),         # 31.5
}
assert N['A5_mass'] == 100 and N['A7_left'] == 8
assert N['B2_25g'] == 16 and N['B2_250g'] == 160
assert N['B3_cuso4_60'] == 40 and N['B3_kno3_30'] == 46 and N['B3_extra'] == 16
assert N['B4_cryst'] == 78
assert N['C2_left_P'] == 14 and N['C2_left_A'] == 12 and N['C2_gain'] == 2
assert N['C4_hot50'] == 55 and N['C4_cold50'] == 16 and N['C4_cryst'] == 39
assert N['C5_cu_200'] == 68
assert N['D1_kno3_70'] == 138 and N['D1_cryst'] == 105 and N['D1_nacl'] == 4
assert N['D3_total'] == 180 and N['D3_cap'] == 31.5 and N['D3_left'] < 0
# ordering questions: no ties
assert len({sol('kno3',20), sol('cuso4',20), sol('nacl',20)}) == 3
assert len({sol('kno3',60), sol('cuso4',60), sol('nacl',60)}) == 3

TABLE = ('<font name="Mono" size="9.5">Solubility (g per 100 g water)<br/>'
         'Temperature (°C): &nbsp; &nbsp;0 &nbsp; &nbsp;20 &nbsp; &nbsp;40 &nbsp; &nbsp;60 &nbsp; &nbsp;80 &nbsp; 100<br/>'
         'potassium nitrate: &nbsp; 13 &nbsp; &nbsp;32 &nbsp; &nbsp;64 &nbsp; 110 &nbsp; 169 &nbsp; 246<br/>'
         'copper sulfate: &nbsp; &nbsp; &nbsp;14 &nbsp; &nbsp;21 &nbsp; &nbsp;29 &nbsp; &nbsp;40 &nbsp; &nbsp;55 &nbsp; &nbsp;75<br/>'
         'sodium chloride: &nbsp; &nbsp; 36 &nbsp; &nbsp;36 &nbsp; &nbsp;37 &nbsp; &nbsp;37 &nbsp; &nbsp;38 &nbsp; &nbsp;40</font>')
for s, row in [('kno3', [13,32,64,110,169,246]), ('cuso4', [14,21,29,40,55,75]), ('nacl', [36,36,37,37,38,40])]:
    assert [sol(s, t) for t in (0,20,40,60,80,100)] == row, s   # the printed table matches the data

BASE = [
 'Answer <b>every</b> question in the space provided.',
 'No calculator is needed anywhere on this paper.',
 'Where a question says <b>explain</b>, your answer must talk about <b>particles</b> — solute particles spreading between solvent particles, '
 'collisions, or how much the solvent can hold at that temperature.',
 'Solubility is always given in <b>g per 100 g of water</b>. If a question uses a different mass of water, scale it.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + ['Reminder: stirring, crushing and heating change how <b>fast</b> something dissolves. Only temperature changes how <b>much</b>.']
INSTR_HARD = BASE + ['Several questions here describe experiments you may not have seen before. '
                     'You are not expected to recognise them — apply the ideas you already have.',
                     'Show every subtraction. A correct number with no working is one mark, not three.']

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — the words',
   'text':'For each solution, name the solute and the solvent.','marks':4,
   'grid':[['Solution','Solute','Solvent'],['sea water','',''],['sugar dissolved in tea','',''],
           ['nail varnish dissolved in propanone','',''],['a fizzy drink (carbon dioxide in water)','','']],
   'grid_widths':[AVAIL*0.5, AVAIL*0.25, AVAIL*0.25]},
  {'text':'State what is meant by each word.','marks':3,
   'parts':[{'label':'(a)','text':'soluble','marks':1,'space':12},
            {'label':'(b)','text':'insoluble','marks':1,'space':12},
            {'label':'(c)','text':'saturated solution','marks':1,'space':14}]},
  {'text':'Sand is stirred into a glass of water; salt is stirred into another. Describe what you would see in each glass after ten minutes, and name the type of mixture in each.','marks':4,'space':40},
  {'section':'Section 2 — particles',
   'text':'Describe, in terms of particles, what happens when sugar dissolves in water.','marks':3,'space':34},
  {'text':'20 g of salt is dissolved in 80 g of water.','marks':3,
   'parts':[{'label':'(a)','text':'State the mass of the solution.','marks':1,'space':12},
            {'label':'(b)','text':'Explain your answer.','marks':2,'space':24}]},
  {'text':'A solution of copper sulfate is clear and blue. A student says "clear means nothing is dissolved in it". Explain why the student is wrong.','marks':2,'space':26},
  {'section':'Section 3 — how much',
   'text':'The solubility of potassium nitrate at 20 °C is 32 g per 100 g of water. A student stirs 40 g into 100 g of water at 20 °C.','marks':4,
   'parts':[{'label':'(a)','text':'State the mass that dissolves and the mass left undissolved.','marks':2,'space':20},
            {'label':'(b)','text':'State whether the solution is saturated, and how you can tell.','marks':2,'space':24}]},
  {'text':'Give <b>three</b> ways to make a solid dissolve faster.','marks':3,'space':30},
  {'text':'State the units of solubility, and explain why a solubility must always be given with a temperature.','marks':4,'space':40},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — saturated solutions',
   'text':'Describe how you could make a saturated solution of salt in water, and how you would know it was saturated.','marks':3,'space':34},
  {'text':'The solubility of potassium nitrate at 40 °C is 64 g per 100 g of water.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the mass that will dissolve in 25 g of water at 40 °C.','marks':2,'space':22},
            {'label':'(b)','text':'Calculate the mass that will dissolve in 250 g of water at 40 °C.','marks':2,'space':22}]},
  {'section':'Section 2 — reading the data',
   'text':'Use the table.<br/><br/>' + TABLE,'marks':7,
   'parts':[{'label':'(a)','text':'State the solubility of copper sulfate at 60 °C.','marks':1,'space':12},
            {'label':'(b)','text':'Which of the three substances is most soluble at 20 °C? Which is most soluble at 60 °C?','marks':2,'space':20},
            {'label':'(c)','text':'A solution contains 30 g of potassium nitrate in 100 g of water at 30 °C. Is it saturated? Explain, using a value from the table.','marks':2,'space':26},
            {'label':'(d)','text':'Which substance would you <b>not</b> bother heating to dissolve more of? Give a reason from the data.','marks':2,'space':24}]},
  {'text':'A saturated solution of potassium nitrate in 100 g of water is made at 60 °C and cooled to 20 °C. Use the table to calculate the mass of crystals that forms. Show your working.','marks':3,'space':32},
  {'text':'Explain why crystals form when the solution in the previous question is cooled.','marks':2,'space':26},
  {'section':'Section 3 — faster',
   'text':'For each change, explain in terms of particles why it makes a solid dissolve faster.','marks':6,
   'parts':[{'label':'(a)','text':'Stirring the solution.','marks':2,'space':24},
            {'label':'(b)','text':'Crushing the solid into a powder.','marks':2,'space':24},
            {'label':'(c)','text':'Warming the water.','marks':2,'space':24}]},
  {'text':'Which <b>one</b> of the three changes in the previous question also increases how <b>much</b> can dissolve? Explain why the other two do not.','marks':3,'space':32},
  {'text':'Explain why a fizzy drink goes flat faster when it is warm.','marks':2,'space':24},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — amount against speed',
   'text':'A student stirs a saturated sugar solution for ten minutes, expecting the sugar on the bottom to dissolve. It does not.','marks':4,
   'parts':[{'label':'(a)','text':'Explain why stirring did not dissolve the remaining sugar.','marks':2,'space':26},
            {'label':'(b)','text':'State what stirring does change, and explain it in terms of particles.','marks':2,'space':26}]},
  {'text':'Two students each stir 50 g of sodium chloride into 100 g of water. Priya uses water at 20 °C; Arjun uses water at 80 °C. '
          'Solubility of sodium chloride: 36 g per 100 g at 20 °C, 38 g per 100 g at 80 °C.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the mass left undissolved in each beaker.','marks':2,'space':24},
            {'label':'(b)','text':'Arjun says heating "made hardly any difference". Use the data to explain why he is right about the amount.','marks':1,'space':18},
            {'label':'(c)','text':'Arjun\'s salt dissolved much faster than Priya\'s. Explain why, in terms of particles.','marks':2,'space':26}]},
  {'section':'Section 2 — gases',
   'text':'A pond warms up in summer and fish are seen gasping at the surface.','marks':3,
   'parts':[{'label':'(a)','text':'State how the solubility of oxygen in water changes as the water warms.','marks':1,'space':14},
            {'label':'(b)','text':'Explain why, in terms of particles.','marks':2,'space':26}]},
  {'section':'Section 3 — calculations and planning',
   'text':'A saturated solution of potassium nitrate is made in <b>50 g</b> of water at 60 °C and cooled to 20 °C. '
          'Solubility: 110 g per 100 g at 60 °C; 32 g per 100 g at 20 °C.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the mass dissolved at 60 °C.','marks':2,'space':22},
            {'label':'(b)','text':'Calculate the mass of crystals that forms on cooling to 20 °C. Show your working.','marks':3,'space':30}]},
  {'text':'A saturated solution of copper sulfate is made in <b>200 g</b> of water at 80 °C and cooled to 20 °C. Solubility: 55 g per 100 g at 80 °C; 21 g per 100 g at 20 °C. '
          'Calculate the mass of crystals that forms. Show your working.','marks':3,'space':30},
  {'text':'A student wants to find out whether sugar is more soluble in water than salt is, at room temperature. '
          'Describe a fair test she could do. Say what she would measure, what she must keep the same, and what result would show sugar is more soluble.','marks':5,'space':56},
  {'text':'Explain why a dilute solution can still be a saturated solution.','marks':2,'space':24},
  {'text':'A beaker of salt solution is left on a balance for a week and the reading falls by 12 g. A student says "some of the salt has disappeared". Explain what has really happened.','marks':3,'space':32},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — an unfamiliar curve',
   'text':'Use the table.<br/><br/>' + TABLE,'marks':8,
   'parts':[{'label':'(a)','text':'Sketch, in the space, the solubility curves for potassium nitrate and sodium chloride on one set of axes (temperature along the bottom, solubility up the side). Label both.','marks':3,'space':60},
            {'label':'(b)','text':'Estimate the solubility of potassium nitrate at 70 °C, and explain how you got it from the table.','marks':2,'space':24},
            {'label':'(c)','text':'A saturated potassium nitrate solution in 100 g of water cools from 80 °C to 40 °C. Calculate the mass of crystals that forms.','marks':2,'space':22},
            {'label':'(d)','text':'A saturated sodium chloride solution in 100 g of water cools from 100 °C to 0 °C. Calculate the mass of crystals, and state what this tells you about recovering salt by cooling.','marks':1,'space':20}]},
  {'section':'Section 2 — the long explanation',
   'text':'A student keeps adding sugar to a glass of water at room temperature, stirring each spoonful until it dissolves. Eventually a spoonful will not dissolve, however long she stirs. She warms the glass and it dissolves.<br/><br/>'
          'Explain everything she observed in terms of particles: what dissolving is, why the sugar stopped dissolving, why stirring could not help, and why warming did.','marks':6,'space':84},
  {'section':'Section 3 — applying the ideas',
   'text':'30 g of copper sulfate is stirred into 150 g of water at 20 °C. Solubility of copper sulfate at 20 °C: 21 g per 100 g of water.','marks':4,
   'parts':[{'label':'(a)','text':'Calculate the maximum mass of copper sulfate that 150 g of water can hold at 20 °C.','marks':2,'space':22},
            {'label':'(b)','text':'State whether all 30 g dissolves, and the total mass of the beaker\'s contents.','marks':2,'space':22}]},
  {'text':'Explain why dissolving is classed as a <b>physical</b> change and a solution is classed as a <b>mixture</b>. Give one piece of evidence for each.','marks':4,'space':44},
  {'text':'Nail varnish does not dissolve in water but dissolves easily in propanone. A student says "nail varnish is insoluble". Explain what is incomplete about this statement.','marks':2,'space':26},
  {'text':'Two students wrote the following in a test. Neither answer is correct.<br/><br/>'
          '<b>(i)</b> &ldquo;When salt dissolves it melts into the water, so the solution weighs a bit less than the salt and water did.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;Crushing the salt lets more of it dissolve, because smaller pieces fit between the water particles.&rdquo;<br/>'
          'For each one, explain the mistake and write a correct version.','marks':6,'space':66},
 ]}

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':4,'lines':['sea water: <b>salt / water</b>','tea: <b>sugar / water (tea)</b>','nail varnish: <b>nail varnish / propanone</b>','fizzy drink: <b>carbon dioxide / water</b>','One mark per row.'],
   'note':'Row 3 is the check that "solvent" has not been learnt as "water".'},
  {'n':'2','marks':3,'lines':['(a) dissolves in a solvent <b>[1]</b>','(b) does not dissolve <b>[1]</b>','(c) a solution that holds as much solute as it can at that temperature — no more will dissolve <b>[1]</b>']},
  {'n':'3','marks':4,'lines':['Sand: cloudy at first, then the sand settles on the bottom, water clear above <b>[1]</b>; a suspension <b>[1]</b>',
    'Salt: the salt disappears and the water stays clear / stays mixed <b>[1]</b>; a solution <b>[1]</b>']},
  {'n':'4','marks':3,'lines':['The sugar particles break away from the solid / from each other <b>[1]</b>',
    'and spread out between the water particles <b>[1]</b>','until they are evenly mixed throughout (too small to see) <b>[1]</b>']},
  {'n':'5','marks':3,'lines':['(a) <b>%d g</b> <b>[1]</b>' % N['A5_mass'],
    '(b) The salt particles are still in the beaker, spread between the water particles <b>[1]</b>; nothing has left, so mass is conserved <b>[1]</b>']},
  {'n':'6','marks':2,'lines':['Clear means you can see through it — the dissolved particles are too small to see <b>[1]</b>',
    'The blue colour shows the copper sulfate is there; clear is not the same as colourless <b>[1]</b>']},
  {'n':'7','marks':4,'lines':['(a) 32 g dissolves <b>[1]</b>; %d g left undissolved <b>[1]</b>' % N['A7_left'],
    '(b) Saturated <b>[1]</b>; undissolved solid remains on the bottom, showing the water holds as much as it can <b>[1]</b>']},
  {'n':'8','marks':3,'lines':['Stir it; crush it (smaller pieces / larger surface area); warm the water. One mark each.']},
  {'n':'9','marks':4,'lines':['g per 100 g of water <b>[1]</b>','Solubility changes with temperature <b>[1]</b>',
    'usually rising as the water warms <b>[1]</b>','so the same substance has a different solubility at each temperature and the number means nothing without one <b>[1]</b>']},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':3,'lines':['Keep adding salt to the water, stirring after each addition <b>[1]</b>',
    'until some salt will not dissolve however long it is stirred <b>[1]</b>','Undissolved salt on the bottom shows it is saturated <b>[1]</b>']},
  {'n':'2','marks':4,'lines':['(a) 25 g is a quarter of 100 g, so 64 &divide; 4 <b>[1]</b> = <b>%d g</b> <b>[1]</b>' % N['B2_25g'],
    '(b) 250 g is 2.5 times 100 g, so 64 &times; 2.5 <b>[1]</b> = <b>%d g</b> <b>[1]</b>' % N['B2_250g']]},
  {'n':'3','marks':7,'lines':['(a) <b>%d g</b> per 100 g of water <b>[1]</b>' % N['B3_cuso4_60'],
    '(b) At 20 °C: <b>sodium chloride</b> (36 g) <b>[1]</b>; at 60 °C: <b>potassium nitrate</b> (110 g) <b>[1]</b>',
    '(c) Not saturated / unsaturated <b>[1]</b>; the solubility at 30 °C is %d g, so another %d g could dissolve <b>[1]</b>' % (N['B3_kno3_30'], N['B3_extra']),
    '(d) <b>Sodium chloride</b> <b>[1]</b>; its solubility only rises from 36 to 40 g across the whole range, so heating dissolves almost no more <b>[1]</b>'],
   'note':'(c) uses 30 °C, a column not printed. The candidate must interpolate between 20 and 40 — 46 g is the value the page gives; accept 45–50.'},
  {'n':'4','marks':3,'lines':['110 g dissolved at 60 °C <b>[1]</b>; 32 g can stay dissolved at 20 °C <b>[1]</b>','110 &minus; 32 = <b>%d g</b> of crystals <b>[1]</b>' % N['B4_cryst']],
   'note':'"78 g" alone is one mark. The two readings are the other two.'},
  {'n':'5','marks':2,'lines':['Solubility falls as the temperature falls, so the cooler water can hold less <b>[1]</b>',
    'The excess comes out of solution as solid crystals <b>[1]</b>']},
  {'n':'6','marks':6,'lines':['(a) Moves solvent that is already full of solute away from the solid <b>[1]</b> and brings fresh solvent particles into contact with it <b>[1]</b>',
    '(b) Increases the surface area <b>[1]</b>, so more solute particles are in contact with water particles at once — more collisions per second <b>[1]</b>',
    '(c) Water particles move faster <b>[1]</b>, so they collide with the solid more often and with more energy, pulling particles off faster <b>[1]</b>']},
  {'n':'7','marks':3,'lines':['<b>Warming</b> <b>[1]</b>','Stirring and crushing only change the rate at which the limit is reached <b>[1]</b>',
    'The limit (solubility) depends only on temperature, so it is unchanged by stirring or crushing <b>[1]</b>']},
  {'n':'8','marks':2,'lines':['Gases (carbon dioxide) are less soluble in warm water <b>[1]</b>','so less can stay dissolved and it escapes as bubbles more quickly <b>[1]</b>']},
 ]},

 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':4,'lines':['(a) The solution is saturated — the water already holds the maximum it can at that temperature <b>[1]</b>; stirring cannot raise that limit <b>[1]</b>',
    '(b) It changes only the rate of dissolving <b>[1]</b>; it brings fresh water particles to the solid and carries dissolved ones away, so dissolving happens faster up to the limit <b>[1]</b>']},
  {'n':'2','marks':5,'lines':['(a) Priya: 50 &minus; 36 = <b>%d g</b> <b>[1]</b>; Arjun: 50 &minus; 38 = <b>%d g</b> <b>[1]</b>' % (N['C2_left_P'], N['C2_left_A']),
    '(b) The solubility rose by only %d g per 100 g across 60 degrees <b>[1]</b>' % N['C2_gain'],
    '(c) At 80 °C the water particles move faster <b>[1]</b>, colliding with the salt more often and more energetically, so it dissolves more quickly <b>[1]</b>'],
   'note':'The point of the question: heating changed the amount by almost nothing and the speed by a lot. A candidate who says heating "made no difference" in (c) has merged the two.'},
  {'n':'3','marks':3,'lines':['(a) It falls / oxygen is less soluble in warmer water <b>[1]</b>',
    '(b) Gas particles in the warm water have more energy <b>[1]</b>; so they can escape from the liquid more easily and less stays dissolved <b>[1]</b>']},
  {'n':'4','marks':5,'lines':['(a) 110 &divide; 2 <b>[1]</b> = <b>%d g</b> <b>[1]</b>' % N['C4_hot50'],
    '(b) At 20 °C, 50 g of water holds 32 &divide; 2 = %d g <b>[1]</b>; crystals = %d &minus; %d <b>[1]</b> = <b>%d g</b> <b>[1]</b>' % (N['C4_cold50'], N['C4_hot50'], N['C4_cold50'], N['C4_cryst'])],
   'note':'78 g is the answer for 100 g of water. A candidate who writes 78 has ignored the 50 g twice.'},
  {'n':'5','marks':3,'lines':['Per 100 g: 55 &minus; 21 = 34 g <b>[1]</b>','For 200 g: 34 &times; 2 <b>[1]</b>','= <b>%d g</b> <b>[1]</b>' % N['C5_cu_200']]},
  {'n':'6','marks':5,'lines':['Measure a fixed mass (or volume) of water into two beakers <b>[1]</b>',
    'Add sugar to one and salt to the other, a measured spoonful at a time, stirring until each dissolves, until no more will dissolve <b>[1]</b>',
    'Record the mass of each that dissolved <b>[1]</b>',
    'Keep the same: mass of water, temperature, stirring, time allowed <b>[1]</b>',
    'Sugar is more soluble if a greater mass of it dissolved in the same mass of water at the same temperature <b>[1]</b>']},
  {'n':'7','marks':2,'lines':['Saturated means the solvent holds the maximum it can; if the solubility is very small, that maximum is small <b>[1]</b>',
    'so the solution holds very little solute (dilute) yet cannot hold any more (saturated) <b>[1]</b>']},
  {'n':'8','marks':3,'lines':['Nothing dissolved has disappeared — the salt particles are all still in the beaker <b>[1]</b>',
    '12 g of <b>water</b> has evaporated into the air <b>[1]</b>',
    'The solution is now more concentrated; if it evaporated to dryness, all the original salt would remain <b>[1]</b>']},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':8,'lines':['(a) Axes labelled with units (°C, g per 100 g water) <b>[1]</b>; potassium nitrate a steep curve rising from 13 to 246 <b>[1]</b>; sodium chloride a nearly flat line near 36–40 <b>[1]</b>',
    '(b) About <b>%d g</b> (accept 130–145) <b>[1]</b>; between the 110 at 60 °C and 169 at 80 °C, nearer the middle <b>[1]</b>' % N['D1_kno3_70'],
    '(c) 169 &minus; 64 = <b>%d g</b> <b>[1]</b> (working shown) <b>[1]</b>' % N['D1_cryst'],
    '(d) 40 &minus; 36 = <b>%d g</b>; cooling recovers almost no salt, so salt is obtained by evaporation instead <b>[1]</b>' % N['D1_nacl']],
   'note':'The sodium chloride line must be drawn nearly flat. A candidate who draws both curves rising steeply has not read the data — that is the point of (a).'},
  {'n':'2','marks':6,'lines':['Award one mark for each of these, up to six:',
    'Dissolving: sugar particles break away from the solid and spread out between the water particles.',
    'The water can only hold a certain mass of sugar at a given temperature — the solubility.',
    'When that limit is reached the solution is saturated, and any more sugar stays solid.',
    'Stirring only speeds up dissolving (fresh water to the solid); it cannot raise the limit.',
    'Warming makes the water particles move faster and collide harder, and raises the solubility.',
    'So at the higher temperature the water can hold more sugar, and the extra spoonful dissolves.'],
   'note':'For full marks the answer must separate the limit (amount) from the rate (speed). Award at most four if stirring and warming are treated as doing the same thing.'},
  {'n':'3','marks':4,'lines':['(a) 150 g is 1.5 times 100 g, so 21 &times; 1.5 <b>[1]</b> = <b>%.1f g</b> <b>[1]</b>' % N['D3_cap'],
    '(b) Yes, all 30 g dissolves (30 is less than 31.5) <b>[1]</b>; total mass 150 + 30 = <b>%d g</b> <b>[1]</b>' % N['D3_total']],
   'note':'The trap is the instinct that 30 g "sounds like more than 21 g", so some must be left. Scale the water first.'},
  {'n':'4','marks':4,'lines':['Physical: no new substance is made <b>[1]</b>; evidence: evaporate the water and the original solute comes back unchanged <b>[1]</b>',
    'Mixture: the solute and solvent are not chemically joined <b>[1]</b>; evidence: they can be separated by physical means / the proportions can vary (dilute or concentrated) <b>[1]</b>']},
  {'n':'5','marks':2,'lines':['Solubility depends on the solvent as well as the solute <b>[1]</b>',
    'so the statement must say what it is insoluble <b>in</b> — insoluble in water, but soluble in propanone <b>[1]</b>']},
  {'n':'6','marks':6,'lines':[
    '(i) The mistake: dissolving is not melting, and mass is not lost <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: the salt particles break away and spread between the water particles; every particle is still there, so the solution weighs exactly what the salt and water weighed <b>[2]</b>',
    '(ii) The mistake: crushing changes only how fast the salt dissolves, not how much can dissolve <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: crushing gives a larger surface area, so more collisions with water particles and faster dissolving; the amount that dissolves is fixed by the temperature <b>[2]</b>'],
   'note':'These are the two most common wrong sentences in the whole topic. If he can mark them in someone else&rsquo;s work, he is unlikely to write them in his own.'},
 ]},
]

files = []
for spec, code in [(A,'a'), (B,'b'), (C,'c'), (D,'d')]:
    t = sum(q.get('marks',0) for q in spec['questions'])
    assert t == 30, (spec['title'], t)
    for q in spec['questions']:
        if 'parts' in q:
            assert sum(p['marks'] for p in q['parts']) == q['marks'], (spec['title'], q['text'][:40])
    p = os.path.join(OUT, 'chemistry-solutions-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)
for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)
p = os.path.join(OUT, 'chemistry-solutions-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Every number on these papers is computed from the same '
             'solubility table the study page uses, by the generator, and checked with asserts before typesetting. The two '
             'recurring losses on this topic are the same two every year: treating "faster" and "more" as the same thing, and '
             'forgetting to scale a solubility when the water is not 100 g. The notes under each answer flag the specific mistake '
             'that question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
