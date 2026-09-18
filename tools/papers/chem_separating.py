#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Chemistry · Grade 7 · Unit 5.2 · Separating mixtures'
TOPIC = 'Separating Mixtures'

# ---- every Rf on these papers, computed here and read from here, never typed from memory ----
def rf(spot, solvent): return round(spot/solvent, 2)
RF = {
 'B4a_E102': rf(2.0, 8.0),    # 0.25
 'B4a_E133': rf(6.8, 8.0),    # 0.85
 'B4_E110':  rf(5.6, 8.0),    # 0.70
 'B5_green': rf(9.0, 12.0),   # 0.75
 'C3_blue':  rf(4.5, 7.5),    # 0.6
 'C3_yellow':rf(1.5, 7.5),    # 0.2
 'D2_spot':  0.80 * 9.0,      # 7.2 cm — Rf in reverse
 'D2_rev':   rf(3.6, 9.0),    # 0.4
}
assert RF['B4a_E102'] == 0.25 and RF['B4a_E133'] == 0.85 and RF['B4_E110'] == 0.70
assert RF['B5_green'] == 0.75 and RF['C3_blue'] == 0.6 and RF['C3_yellow'] == 0.2
assert abs(RF['D2_spot'] - 7.2) < 1e-9 and RF['D2_rev'] == 0.4

BASE = [
 'Answer <b>every</b> question in the space provided.',
 'No calculator is needed anywhere on this paper.',
 'Where a question says <b>explain</b>, name the <b>property that differs</b> between the substances — '
 'soluble or insoluble, boiling point, magnetic, particle size — because that property is why the method works.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + ['R<sub>f</sub> = distance moved by the substance &divide; distance moved by the solvent. Both from the baseline. No units.']
INSTR_HARD = BASE + ['Several questions here describe mixtures or experiments you may not have seen before. '
                     'You are not expected to recognise them — apply the ideas you already have.',
                     'Naming a method scores one mark. Saying why it works is where the rest are.']

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — matching the method',
   'text':'For each mixture, write the best method to separate it.','marks':5,
   'grid':[['Mixture','Method'],['sand and water',''],['salt dissolved in water — you want the salt',''],
           ['salt dissolved in water — you want the water',''],['iron filings and sand',''],['the dyes in a black ink','']],
   'grid_widths':[AVAIL*0.6, AVAIL*0.4]},
  {'text':'In filtration, give the name for:','marks':2,
   'parts':[{'label':'(a)','text':'the solid left on the filter paper.','marks':1,'space':12},
            {'label':'(b)','text':'the liquid that passes through.','marks':1,'space':12}]},
  {'text':'Muddy water is poured through filter paper.','marks':3,
   'parts':[{'label':'(a)','text':'State what is left on the paper and what passes through.','marks':1,'space':16},
            {'label':'(b)','text':'Explain, in terms of particle size, why the mud is trapped but the water is not.','marks':2,'space':26}]},
  {'section':'Section 2 — apparatus',
   'text':'The diagram below is left for you to draw. Draw and label the apparatus for <b>filtration</b>: filter funnel, filter paper, conical flask, residue, filtrate.','marks':4,'space':60},
  {'text':'Describe how you would obtain dry salt crystals from a salt solution, naming the apparatus you would use.','marks':3,'space':34},
  {'text':'A student wants to separate iron filings from sand.','marks':3,
   'parts':[{'label':'(a)','text':'Name the method.','marks':1,'space':12},
            {'label':'(b)','text':'Explain why the method works.','marks':2,'space':24}]},
  {'section':'Section 3 — explaining the choice',
   'text':'Explain why <b>filtration</b> cannot be used to remove salt from sea water.','marks':3,'space':32},
  {'text':'Explain why <b>evaporation</b> is the wrong method if you want to collect pure water from sea water, and name the right one.','marks':3,'space':32},
  {'text':'State <b>two</b> rules for setting up paper chromatography correctly, and give the reason for each.','marks':4,'space':44},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — simple distillation',
   'text':'Sea water is separated by simple distillation to collect pure water.','marks':7,
   'parts':[{'label':'(a)','text':'Describe what happens to the water in the flask when it is heated.','marks':1,'space':16},
            {'label':'(b)','text':'State the purpose of the condenser, and explain how it works.','marks':2,'space':26},
            {'label':'(c)','text':'Give the name of the liquid collected in the receiving flask.','marks':1,'space':12},
            {'label':'(d)','text':'State what is left in the heating flask at the end, and explain why it did not come over with the water.','marks':2,'space':26},
            {'label':'(e)','text':'State the reading on the thermometer while the water is being collected.','marks':1,'space':12}]},
  {'text':'Explain why the cooling water enters the condenser at the end nearest the receiving flask and leaves at the end nearest the heating flask.','marks':2,'space':26},
  {'section':'Section 2 — chromatography',
   'text':'Explain why a spot of ink separates into several colours when a chromatogram is run.','marks':3,'space':34},
  {'text':'A chromatogram is run with three known food dyes and one sweet colouring. The solvent front travels <b>8.0 cm</b>. '
          'E102 travels 2.0 cm, E110 travels 5.6 cm and E133 travels 6.8 cm. The sweet gives spots at 2.0 cm and 6.8 cm.','marks':5,
   'parts':[{'label':'(a)','text':'Calculate the R<sub>f</sub> values of E102 and E133. Show your working.','marks':2,'space':26},
            {'label':'(b)','text':'State which dyes the sweet contains, and how you know.','marks':2,'space':24},
            {'label':'(c)','text':'Explain why the sweet colouring cannot be a pure substance.','marks':1,'space':16}]},
  {'text':'On another chromatogram the solvent front is 12.0 cm from the baseline and a green spot is 9.0 cm from the baseline. Calculate the R<sub>f</sub> value of the green dye.','marks':2,'space':22},
  {'section':'Section 3 — salt and sand',
   'text':'A jar contains a dry mixture of salt and sand. Describe, step by step, how to obtain a sample of dry salt from it. Give a reason for each step.','marks':6,'space':64},
  {'text':'Explain why the steps in the previous question must be done in that order, and what would go wrong if the filtering and the evaporating were swapped.','marks':3,'space':32},
  {'text':'Name a method that could separate oil from water, and state the property it relies on.','marks':2,'space':22},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — unfamiliar mixtures',
   'text':'For each mixture below, choose a method, and explain the property it uses. Each part is worth three marks: one for the method, two for the reason.','marks':9,
   'parts':[{'label':'(a)','text':'Copper sulfate crystals dissolved in water — you want the crystals back.','marks':3,'space':30},
            {'label':'(b)','text':'Chalk powder (insoluble) stirred into water.','marks':3,'space':30},
            {'label':'(c)','text':'Ethanol (boiling point 78 °C) mixed with water (boiling point 100 °C) — you want the ethanol.','marks':3,'space':30}]},
  {'section':'Section 2 — chromatography of an unknown',
   'text':'A green food colouring is tested. On the chromatogram the solvent front travels <b>7.5 cm</b>. The colouring gives two spots: '
          'a blue one 4.5 cm from the baseline and a yellow one 1.5 cm from the baseline. A known dye, Tartrazine, run alongside, gives a yellow spot at 1.5 cm.','marks':6,
   'parts':[{'label':'(a)','text':'Calculate the R<sub>f</sub> values of the blue and yellow spots.','marks':2,'space':26},
            {'label':'(b)','text':'State, with a reason, whether the colouring contains Tartrazine.','marks':2,'space':24},
            {'label':'(c)','text':'The blue dye travelled much further than the yellow. Explain why, in terms of the dyes and the solvent.','marks':2,'space':26}]},
  {'text':'Explain why R<sub>f</sub> values are always less than 1, and why a student who calculates an R<sub>f</sub> of 1.5 must have made a mistake.','marks':3,'space':32},
  {'section':'Section 3 — when it goes wrong',
   'text':'A student sets up chromatography with the baseline drawn in ink and the solvent level above the baseline. Explain what goes wrong in each case.','marks':4,'space':40},
  {'text':'A student distils ink to obtain water, but puts the thermometer bulb in the liquid instead of at the top of the flask. State what the thermometer reads compared with 100 °C, and explain why this matters.','marks':3,'space':32},
  {'text':'A student tries to separate salt from sea water by filtering and is surprised the filtrate still tastes salty. Explain what has happened and what she should do instead.','marks':3,'space':32},
  {'text':'Explain why distillation needs far more energy than filtration, even though both can separate a solid from a liquid.','marks':2,'space':24},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — planning a full separation',
   'text':'A dry mixture contains <b>iron filings, sand and salt</b>. Plan a method to obtain all three separately and dry. '
          'Give the steps in order, with a reason for each, and say what you have after every step.','marks':7,'space':80},
  {'section':'Section 2 — R<sub>f</sub> in reverse',
   'text':'A dye has an R<sub>f</sub> value of <b>0.80</b> in a particular solvent.','marks':5,
   'parts':[{'label':'(a)','text':'On a chromatogram where the solvent front moves 9.0 cm, calculate how far the dye will travel.','marks':2,'space':24},
            {'label':'(b)','text':'A second spot on the same paper is 3.6 cm from the baseline. Calculate its R<sub>f</sub> value.','marks':2,'space':22},
            {'label':'(c)','text':'The same dye is run in a different solvent and its R<sub>f</sub> changes. Explain why the R<sub>f</sub> can still be used to identify it.','marks':1,'space':18}]},
  {'section':'Section 3 — the long explanation',
   'text':'Describe and explain how simple distillation produces pure water from sea water. Your answer should cover what happens to the water and to the salt in the flask, '
          'what the condenser does and how, what the thermometer shows, and why the collected liquid is pure.','marks':6,'space':84},
  {'text':'Sea water is left in a shallow dish in the sun and, after several days, only white crystals remain. State the name of this process, what has happened to the water, and why the salt did not leave with it.','marks':3,'space':32},
  {'text':'A student says: "Chromatography could be used to get the water out of ink." Explain why this is wrong, and state what chromatography <b>would</b> tell you about the ink.','marks':3,'space':32},
  {'text':'Two students wrote the following in a test. Neither answer is correct.<br/><br/>'
          '<b>(i)</b> &ldquo;To get the salt out of salt water, filter it — the salt stays on the paper.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;R<sub>f</sub> = distance moved by the solvent &divide; distance moved by the spot.&rdquo;<br/>'
          'For each one, explain the mistake and write a correct version.','marks':6,'space':66},
 ]}

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['<b>filtration</b>; <b>evaporation</b> (or crystallisation); <b>simple distillation</b>; <b>magnet</b>; <b>chromatography</b>','One mark each.'],
   'note':'Rows 2 and 3 are the same mixture with a different aim. A candidate who writes the same method for both has not asked "which part do I want?"'},
  {'n':'2','marks':2,'lines':['(a) <b>residue</b> <b>[1]</b>','(b) <b>filtrate</b> <b>[1]</b>']},
  {'n':'3','marks':3,'lines':['(a) mud (residue) on the paper; water (filtrate) passes through <b>[1]</b>',
    '(b) the mud particles are larger than the holes in the filter paper, so they cannot pass <b>[1]</b>; water particles are much smaller than the holes, so they go through <b>[1]</b>']},
  {'n':'4','marks':4,'lines':['Funnel with cone of filter paper, standing in a conical flask <b>[1]</b>',
    'Filter paper and funnel labelled <b>[1]</b>','Residue labelled on the paper <b>[1]</b>','Filtrate labelled in the flask <b>[1]</b>']},
  {'n':'5','marks':3,'lines':['Pour the solution into an evaporating dish and heat it (gently, over a beaker of water or a tripod) <b>[1]</b>',
    'The water evaporates / turns to vapour and leaves <b>[1]</b>','The salt cannot evaporate and is left behind as crystals; dry them <b>[1]</b>']},
  {'n':'6','marks':3,'lines':['(a) Use a <b>magnet</b> <b>[1]</b>',
    '(b) Iron is magnetic and is attracted to the magnet <b>[1]</b>; sand is not magnetic and stays behind <b>[1]</b>']},
  {'n':'7','marks':3,'lines':['The salt has dissolved <b>[1]</b>','so its particles are small enough to pass through the holes in the filter paper <b>[1]</b>',
    'along with the water — filtration only removes insoluble solids <b>[1]</b>']},
  {'n':'8','marks':3,'lines':['Evaporation lets the water escape into the air as vapour, so it is lost — only the salt is kept <b>[1]</b>',
    'To collect the water it must be condensed back into a liquid <b>[1]</b>','so <b>simple distillation</b> is the right method <b>[1]</b>']},
  {'n':'9','marks':4,'lines':['Baseline in pencil <b>[1]</b> — ink is soluble and would run up the paper with the sample <b>[1]</b>',
    'Solvent level below the baseline <b>[1]</b> — otherwise the spots dissolve into the solvent instead of travelling up the paper <b>[1]</b>',
    'Also accept: small concentrated spots (so they do not smear); lid on the container (stops solvent evaporating); mark the solvent front immediately (it fades).']},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':7,'lines':['(a) The water boils (at 100 °C) and turns into vapour / steam <b>[1]</b>',
    '(b) To turn the vapour back into liquid (condense it) <b>[1]</b>; cold water flows around the outside, cooling the vapour below its boiling point <b>[1]</b>',
    '(c) <b>Distillate</b> (accept: pure water) <b>[1]</b>',
    '(d) The salt <b>[1]</b>; its boiling point is far higher, so it did not turn into vapour at 100 °C <b>[1]</b>',
    '(e) <b>100 °C</b> <b>[1]</b>']},
  {'n':'2','marks':2,'lines':['So the condenser is always full of cold water <b>[1]</b>',
    'and the coldest water is nearest the outlet, so the vapour meets colder and colder walls as it travels and is fully condensed by the end <b>[1]</b>']},
  {'n':'3','marks':3,'lines':['Ink is a mixture of different dyes <b>[1]</b>',
    'The dyes differ in how soluble they are in the solvent (and how strongly they are attracted to the paper) <b>[1]</b>',
    'so as the solvent moves up it carries the more soluble dyes further, and they separate into spots at different heights <b>[1]</b>']},
  {'n':'4','marks':5,'lines':['(a) E102: 2.0 &divide; 8.0 = <b>%.2f</b> <b>[1]</b>; E133: 6.8 &divide; 8.0 = <b>%.2f</b> <b>[1]</b>' % (RF['B4a_E102'], RF['B4a_E133']),
    '(b) <b>E102 and E133</b> <b>[1]</b>; its spots are at the same heights (same R<sub>f</sub>) as those dyes, and the same substance always travels the same distance in the same solvent <b>[1]</b>',
    '(c) It gives two spots, so it contains at least two substances <b>[1]</b>'],
   'note':'Working must be shown in (a). 8.0 &divide; 2.0 = 4 is the upside-down version — no marks, and it is impossible because R<sub>f</sub> cannot exceed 1.'},
  {'n':'5','marks':2,'lines':['9.0 &divide; 12.0 <b>[1]</b>','= <b>%.2f</b> (no units) <b>[1]</b>' % RF['B5_green']]},
  {'n':'6','marks':6,'lines':['Add water and stir <b>[1]</b> — the salt dissolves and the sand does not <b>[1]</b>',
    'Filter <b>[1]</b> — the sand is the residue; the salt solution is the filtrate <b>[1]</b>',
    'Evaporate the filtrate in an evaporating dish <b>[1]</b> — the water leaves and dry salt crystals remain <b>[1]</b>'],
   'note':'The reasons are half the marks. A bare list of three steps scores three.'},
  {'n':'7','marks':3,'lines':['The salt must be dissolved before filtering so that it can pass through and be separated from the sand <b>[1]</b>',
    'If evaporated first, the water would leave and the salt would be deposited back onto the sand <b>[1]</b>',
    'leaving salty sand — nothing separated <b>[1]</b>']},
  {'n':'8','marks':2,'lines':['Separating funnel (accept decanting) <b>[1]</b>','Oil and water do not mix, and the oil floats on top (less dense) <b>[1]</b>']},
 ]},

 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':9,'lines':['(a) Evaporation / crystallisation <b>[1]</b>; the copper sulfate is dissolved so cannot be filtered <b>[1]</b>; water has a much lower boiling point and leaves, the solid stays <b>[1]</b>',
    '(b) Filtration <b>[1]</b>; chalk is insoluble, so its particles are large enough to be trapped by the paper <b>[1]</b>; water passes through <b>[1]</b>',
    '(c) (Simple) distillation <b>[1]</b>; the two liquids have different boiling points <b>[1]</b>; ethanol boils first at 78 °C, is condensed and collected, water is left behind <b>[1]</b>'],
   'note':'(c) is beyond what the page teaches directly and is meant to be: the boiling-point property is the same one as for sea water. A candidate who answers "fractional distillation" with the same reasoning gets full marks.'},
  {'n':'2','marks':6,'lines':['(a) Blue: 4.5 &divide; 7.5 = <b>%.1f</b> <b>[1]</b>; yellow: 1.5 &divide; 7.5 = <b>%.1f</b> <b>[1]</b>' % (RF['C3_blue'], RF['C3_yellow']),
    '(b) <b>Yes</b> <b>[1]</b>; the yellow spot is at the same height / same R<sub>f</sub> as the Tartrazine spot <b>[1]</b>',
    '(c) The blue dye is more soluble in the solvent (or less attracted to the paper) <b>[1]</b>; so the solvent carries it further before it is left behind <b>[1]</b>']},
  {'n':'3','marks':3,'lines':['The spot is carried by the solvent, so it can never travel further than the solvent front <b>[1]</b>',
    'so spot distance &divide; solvent distance is always less than (or at most equal to) 1 <b>[1]</b>',
    '1.5 means the student divided the solvent distance by the spot distance — the wrong way round <b>[1]</b>']},
  {'n':'4','marks':4,'lines':['Ink baseline: the ink is soluble, so the line dissolves and moves up the paper <b>[1]</b>, mixing with the sample and making the spots impossible to read <b>[1]</b>',
    'Solvent above baseline: the spots are under the solvent and dissolve into it <b>[1]</b>, so they are washed off instead of travelling up the paper <b>[1]</b>']},
  {'n':'5','marks':3,'lines':['It reads above 100 °C <b>[1]</b>',
    'because it measures the boiling point of the whole solution, which is raised by the dissolved dyes <b>[1]</b>',
    'so the student cannot tell from the thermometer that pure water is what is coming over <b>[1]</b>']},
  {'n':'6','marks':3,'lines':['The salt is dissolved, so its particles pass through the filter paper with the water <b>[1]</b>',
    'Filtration only removes insoluble solids <b>[1]</b>',
    'She should evaporate the water (or crystallise) to obtain the salt <b>[1]</b>']},
  {'n':'7','marks':2,'lines':['Distillation has to boil every bit of the liquid — turning it all into vapour takes a great deal of energy <b>[1]</b>',
    'Filtration just lets the liquid run through the paper; nothing has to change state <b>[1]</b>']},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':7,'lines':['Magnet first <b>[1]</b> — iron is magnetic, the others are not; and it must be done while everything is dry <b>[1]</b>; now: iron on the magnet, sand and salt left',
    'Add water and stir <b>[1]</b> — salt dissolves, sand does not <b>[1]</b>',
    'Filter <b>[1]</b> — sand is the residue (rinse and dry it), salt solution is the filtrate',
    'Evaporate the filtrate <b>[1]</b> — water leaves, dry salt crystals remain <b>[1]</b>'],
   'note':'The order mark is for the magnet coming before the water. After the water, the iron would be wet, rusting, and mixed into the residue with the sand.'},
  {'n':'2','marks':5,'lines':['(a) distance = R<sub>f</sub> &times; solvent distance = 0.80 &times; 9.0 <b>[1]</b> = <b>%.1f cm</b> <b>[1]</b>' % RF['D2_spot'],
    '(b) 3.6 &divide; 9.0 <b>[1]</b> = <b>%.1f</b> <b>[1]</b>' % RF['D2_rev'],
    '(c) R<sub>f</sub> is fixed for a given dye in a given solvent, so it identifies the dye as long as it is compared with a value measured in the same solvent <b>[1]</b>'],
   'note':'(a) is R<sub>f</sub> rearranged, which most candidates have never done. Award the first mark for the rearrangement even if the arithmetic slips.'},
  {'n':'3','marks':6,'lines':['Award one mark for each of these, up to six:',
    'The sea water is heated and the water boils at 100 °C, turning to vapour.',
    'The salt has a much higher boiling point and stays in the flask (the solution becomes more concentrated).',
    'The vapour passes into the condenser, which has cold water flowing round the outside.',
    'The vapour is cooled below its boiling point and condenses back to liquid water.',
    'The thermometer at the top of the flask reads 100 °C while water is coming over, showing what is being collected.',
    'The collected distillate is pure because only the water turned to vapour; nothing dissolved could travel with it.'],
   'note':'For full marks the answer must say why the product is pure (only water vaporised), not just that it "is pure". Award at most four if the condenser is described without saying what it does to the vapour.'},
  {'n':'4','marks':3,'lines':['<b>Evaporation</b> <b>[1]</b>','The water has turned to vapour and escaped into the air <b>[1]</b>',
    'The salt cannot evaporate at that temperature (far higher boiling point), so it is left behind as crystals <b>[1]</b>']},
  {'n':'5','marks':3,'lines':['Chromatography does not collect anything — the water soaks into the paper and evaporates <b>[1]</b>',
    'To obtain the water you would need distillation <b>[1]</b>',
    'Chromatography would show how many dyes the ink contains and, with R<sub>f</sub> values, which ones <b>[1]</b>']},
  {'n':'6','marks':6,'lines':[
    '(i) The mistake: dissolved salt passes straight through filter paper — filtration only catches insoluble solids <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: evaporate the water from the solution (or crystallise); the salt is left behind in the dish <b>[2]</b>',
    '(ii) The mistake: the division is upside down, which would give values above 1 <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: R<sub>f</sub> = distance moved by the spot &divide; distance moved by the solvent, both measured from the baseline <b>[2]</b>'],
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
    p = os.path.join(OUT, 'chemistry-separating-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)
for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)
p = os.path.join(OUT, 'chemistry-separating-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. On this topic the method is the cheap mark and the '
             '<b>property that differs</b> is the expensive one: insist on "because the sand is insoluble", "because water has '
             'the lower boiling point", "because iron is magnetic". Every R<sub>f</sub> on these papers was computed in the generator, '
             'not typed; any value above 1 in a candidate\'s work is the division done upside down. The notes under each answer '
             'flag the specific mistake that question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
