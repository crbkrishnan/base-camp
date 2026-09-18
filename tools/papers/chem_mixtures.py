#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Chemistry · Grade 7 · Unit 5.1 · Pure substances and mixtures'
TOPIC = 'Pure Substances and Mixtures'

BASE = [
 'Answer <b>every</b> question in the space provided.',
 'No calculator is needed anywhere on this paper.',
 'Where a question says <b>explain</b>, your answer must say whether the atoms are <b>chemically joined</b> or <b>not joined</b>, '
 'and whether there is <b>one kind of particle</b> or more than one.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + ['Reminder: a pure substance melts <b>sharply</b> at one temperature; an impure one melts <b>over a range</b>, and lower.']
INSTR_HARD = BASE + ['Several questions here describe substances or experiments you may not have seen before. '
                     'You are not expected to recognise them — apply the ideas you already have.',
                     '"Pure" on this paper always has its chemical meaning: one substance only.']

MP_TABLE = ('<font name="Mono" size="10">Sample &nbsp; Melting point<br/>'
            'P &nbsp; &nbsp; &nbsp; &nbsp;118 °C<br/>'
            'Q &nbsp; &nbsp; &nbsp; &nbsp;109–115 °C<br/>'
            'R &nbsp; &nbsp; &nbsp; &nbsp;122 °C<br/>'
            'S &nbsp; &nbsp; &nbsp; &nbsp;117–121 °C</font>')

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — the three words',
   'text':'Complete each definition.','marks':3,
   'parts':[{'label':'(a)','text':'An <b>element</b> contains only one kind of ____________.','marks':1,'space':12},
            {'label':'(b)','text':'A <b>compound</b> contains two or more kinds of atom that are ____________ ____________ together.','marks':1,'space':12},
            {'label':'(c)','text':'A <b>mixture</b> contains two or more ____________ that are not chemically joined.','marks':1,'space':12}]},
  {'text':'Sort these six substances into the table: <b>oxygen, sea water, water, air, iron, carbon dioxide</b>. Write each name in one column only.','marks':6,
   'grid':[['Element','Compound','Mixture'],['','',''],['','',''],['','','']],
   'grid_widths':[AVAIL/3, AVAIL/3, AVAIL/3]},
  {'text':'State what is meant by a <b>pure substance</b> in chemistry, and explain why a carton labelled "pure orange juice" is not pure in this sense.','marks':2,'space':26},
  {'section':'Section 2 — particle diagrams',
   'text':'In the space below, draw a particle diagram for each of the following. Use circles of different shading for different kinds of atom, and label each box.','marks':4,
   'parts':[{'label':'(a)','text':'An element made of single atoms.','marks':1,'space':30},
            {'label':'(b)','text':'A compound.','marks':1,'space':30},
            {'label':'(c)','text':'A mixture of two elements.','marks':1,'space':30},
            {'label':'(d)','text':'A mixture of an element and a compound.','marks':1,'space':30}]},
  {'text':'A box contains particles. Every particle is a group of one large shaded circle joined to two small white circles, and every group is identical.','marks':3,
   'parts':[{'label':'(a)','text':'How many kinds of atom are present?','marks':1,'space':12},
            {'label':'(b)','text':'Is the contents of the box an element, a compound or a mixture? Give a reason.','marks':2,'space':24}]},
  {'section':'Section 3 — properties of mixtures',
   'text':'Give <b>two</b> properties of a mixture that are different from the properties of a compound.','marks':2,'space':26},
  {'text':'Iron filings and sulfur powder are stirred together in a dish.','marks':4,
   'parts':[{'label':'(a)','text':'State what you would see, and how you could separate the two again.','marks':2,'space':24},
            {'label':'(b)','text':'The dish is heated strongly and a single grey solid forms. State whether this solid is a mixture or a compound, and give one piece of evidence.','marks':2,'space':26}]},
  {'text':'Air is a mixture of gases. State the two main gases in air and explain why air is classed as a mixture rather than a compound.','marks':3,'space':32},
  {'text':'Give one example of a mixture of two <b>solids</b> that is useful, and say what it is used for.','marks':3,'space':26},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · Non-calculator · 35 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — compound against mixture',
   'text':'Complete the table comparing a compound with a mixture. Each empty box is worth one mark.','marks':6,
   'grid':[['','Compound','Mixture'],
           ['Are the atoms chemically joined?','',''],
           ['Is the ratio of the substances fixed?','',''],
           ['Can it be separated by physical methods?','',''],
           ['Does it keep the properties of the substances in it?','','no — new properties'],
           ['Sharp melting point?','','']],
   'grid_widths':[AVAIL*0.46, AVAIL*0.27, AVAIL*0.27]},
  {'text':'Sodium is a soft metal that fizzes violently in water. Chlorine is a poisonous green gas. Sodium chloride is the white solid you put on chips.',
   'marks':3,
   'parts':[{'label':'(a)','text':'State whether sodium chloride is an element, a compound or a mixture.','marks':1,'space':12},
            {'label':'(b)','text':'Explain why sodium chloride does not behave like sodium or like chlorine.','marks':2,'space':26}]},
  {'section':'Section 2 — iron and sulfur',
   'text':'A student mixes iron filings with sulfur powder, then heats half of the mixture in a test tube until it glows. The unheated half stays in a dish.','marks':6,
   'parts':[{'label':'(a)','text':'A magnet is held over the dish. State what happens and explain why.','marks':2,'space':24},
            {'label':'(b)','text':'The magnet is held over the heated product. State what happens and explain why.','marks':2,'space':24},
            {'label':'(c)','text':'The student says the ratio of iron to sulfur in the heated product is "whatever we started with". Explain why this is wrong.','marks':2,'space':26}]},
  {'section':'Section 3 — testing for purity',
   'text':'Four samples labelled "benzoic acid" are tested. The data book gives the melting point of pure benzoic acid as <b>122 °C</b>.<br/><br/>' + MP_TABLE,
   'marks':6,
   'parts':[{'label':'(a)','text':'Which sample is pure benzoic acid? Give two reasons.','marks':2,'space':24},
            {'label':'(b)','text':'Which two samples are impure? How can you tell?','marks':2,'space':22},
            {'label':'(c)','text':'Sample P melts sharply but not at 122 °C. What does this tell you about P?','marks':2,'space':24}]},
  {'text':'Describe how you would test whether a sample of a solid is pure, and the result you would expect if it is.','marks':3,'space':34},
  {'text':'The nitrogen in air is not chemically joined to the oxygen. Give <b>two</b> pieces of evidence that air is a mixture.','marks':3,'space':30},
  {'text':'Explain why water is a pure substance even though it contains two different elements.','marks':3,'space':32},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — heating curves',
   'text':'Two solid samples are heated at the same steady rate and their temperatures recorded every minute.<br/><br/>'
          '<font name="Mono" size="10">Time (min): &nbsp; 0 &nbsp; &nbsp;1 &nbsp; &nbsp;2 &nbsp; &nbsp;3 &nbsp; &nbsp;4 &nbsp; &nbsp;5 &nbsp; &nbsp;6 &nbsp; &nbsp;7<br/>'
          'Sample X: &nbsp; &nbsp; 40 &nbsp; 60 &nbsp; 80 &nbsp; 80 &nbsp; 80 &nbsp; 80 &nbsp; 95 &nbsp; 110<br/>'
          'Sample Y: &nbsp; &nbsp; 40 &nbsp; 60 &nbsp; 71 &nbsp; 74 &nbsp; 77 &nbsp; 79 &nbsp; 94 &nbsp; 109</font>','marks':6,
   'parts':[{'label':'(a)','text':'State the melting point of sample X, and how you can tell it is pure.','marks':2,'space':24},
            {'label':'(b)','text':'State the temperature range over which sample Y melts.','marks':1,'space':14},
            {'label':'(c)','text':'Explain what the readings for Y tell you about the sample, giving two reasons.','marks':3,'space':34}]},
  {'text':'Explain, in terms of particles, why an impurity makes a solid start to melt at a lower temperature than the pure solid.','marks':3,'space':34},
  {'section':'Section 2 — planning a test',
   'text':'A student is given a white powder and told it is either pure sodium chloride or a mixture of sodium chloride and sand. '
          'She has a beaker, water, filter paper and a funnel. Describe a test she could do, the result that would show it is a mixture, and the result that would show it is pure.',
   'marks':4,'space':46},
  {'text':'Salt is spread on icy roads in winter.','marks':4,
   'parts':[{'label':'(a)','text':'Explain, using the idea of impure substances, why the ice melts even though the air is below 0 °C.','marks':2,'space':26},
            {'label':'(b)','text':'A student says the salt "heats up the ice". Explain what is wrong with this, and what has actually changed.','marks':2,'space':26}]},
  {'section':'Section 3 — unfamiliar substances',
   'text':'Each description below is of an unfamiliar substance. For each, state whether it is an <b>element</b>, a <b>compound</b> or a <b>mixture</b>, and give a reason.','marks':6,
   'parts':[{'label':'(a)','text':'Neon: every particle is a single atom, and every atom is the same.','marks':2,'space':22},
            {'label':'(b)','text':'Ammonia: every particle is one nitrogen atom joined to three hydrogen atoms.','marks':2,'space':22},
            {'label':'(c)','text':'Brass: copper atoms and zinc atoms packed together in a solid, in any proportion the maker chooses, not joined to each other.','marks':2,'space':22}]},
  {'text':'A student says: "Carbon dioxide must be a mixture, because it is made from carbon and oxygen and both of those are elements." Explain why the student is wrong.','marks':3,'space':34},
  {'text':'Sea water boils at a slightly higher temperature than pure water, and the temperature keeps rising as it boils. Explain both observations.','marks':4,'space':40},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · Non-calculator · 45 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — identifying from data',
   'text':'A data book lists the melting points of four pure white solids:<br/><br/>'
          '<font name="Mono" size="10">urea 133 °C &nbsp; · &nbsp; benzoic acid 122 °C &nbsp; · &nbsp; stearic acid 69 °C &nbsp; · &nbsp; naphthalene 80 °C</font><br/><br/>'
          'Three unlabelled samples are tested. Sample 1 melts at 80 °C. Sample 2 melts between 61 and 67 °C. Sample 3 melts between 118 and 122 °C.','marks':6,
   'parts':[{'label':'(a)','text':'Identify sample 1 and explain how you know it is pure.','marks':2,'space':24},
            {'label':'(b)','text':'Sample 2 is most likely an impure form of which solid? Give two reasons.','marks':2,'space':26},
            {'label':'(c)','text':'A student says sample 3 must be pure benzoic acid because "it reaches 122 °C". Explain why this is wrong.','marks':2,'space':26}]},
  {'section':'Section 2 — the long explanation',
   'text':'Hydrogen is a gas that burns. Oxygen is a gas that makes things burn faster. Water, which is made from only these two elements, puts fires out. '
          'A student says this proves water is a mixture of hydrogen and oxygen.<br/><br/>'
          'Explain why water is a <b>compound</b> and not a mixture, and why it is nevertheless a <b>pure substance</b>. '
          'Your answer should refer to how the atoms are held, the ratio of the elements, the properties of water compared with its elements, '
          'and what it would take to separate the hydrogen from the oxygen.','marks':6,'space':84},
  {'section':'Section 3 — applying the ideas',
   'text':'A jar contains a mixture of hydrogen gas and oxygen gas. A spark is put in and there is a bang; afterwards the jar contains only water droplets.','marks':4,
   'parts':[{'label':'(a)','text':'State whether the contents of the jar before the spark were pure or a mixture, and why.','marks':2,'space':24},
            {'label':'(b)','text':'Explain what the spark caused to happen to the particles.','marks':2,'space':26}]},
  {'text':'Give <b>three</b> differences between the mixture of iron and sulfur before heating and the compound iron sulfide formed after heating. Each difference must say something about both.','marks':3,'space':36},
  {'text':'A student draws a "mixture of two elements" as pairs of one black circle joined to one white circle, scattered across the box.','marks':3,
   'parts':[{'label':'(a)','text':'State what the student has actually drawn.','marks':1,'space':14},
            {'label':'(b)','text':'Describe how the diagram should be corrected, and explain why the correction matters.','marks':2,'space':28}]},
  {'text':'Two students wrote the following in a test. Neither answer is correct.<br/><br/>'
          '<b>(i)</b> &ldquo;A pure substance is one that occurs naturally and has had nothing added to it.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;An impure sample melts at a lower temperature, so the melting point simply moves down.&rdquo;<br/>'
          'For each one, explain the mistake and write a correct version.','marks':5,'space':60},
  {'text':'Explain why the melting point of a pure substance can be used to identify it, but the melting range of a mixture cannot.','marks':3,'space':34},
 ]}

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':3,'lines':['(a) <b>atom</b>','(b) <b>chemically joined</b> (bonded)','(c) <b>substances</b> (accept: elements or compounds)']},
  {'n':'2','marks':6,'lines':['Element: <b>oxygen, iron</b>','Compound: <b>water, carbon dioxide</b>','Mixture: <b>sea water, air</b>',
    'One mark per correctly placed substance.'],
   'note':'Air and sea water in the compound column is the standard error — "made of more than one thing" is not the test; "joined" is.'},
  {'n':'3','marks':2,'lines':['A pure substance contains only one substance / one type of particle <b>[1]</b>',
    'Orange juice contains many substances (water, sugars, acids) mixed together, so it is a mixture <b>[1]</b>']},
  {'n':'4','marks':4,'lines':['(a) identical single circles, well spaced or touching, all the same <b>[1]</b>',
    '(b) identical groups of two or more different circles joined together, every group the same <b>[1]</b>',
    '(c) two kinds of single circle scattered among each other, none joined <b>[1]</b>',
    '(d) single circles of one kind scattered among identical joined groups <b>[1]</b>'],
   'note':'The mark in (c) is lost if the two kinds are drawn touching in pairs — that is a compound. Check for it specifically.'},
  {'n':'5','marks':3,'lines':['(a) <b>Two</b> <b>[1]</b>',
    '(b) <b>Compound</b> <b>[1]</b>; two kinds of atom are joined together and every particle is the same (fixed ratio) <b>[1]</b>'],
   'note':'"Mixture, because there are two kinds of circle" is the trap. Two kinds of atom in one particle is a compound.'},
  {'n':'6','marks':2,'lines':['Any two: the substances are not chemically joined; can be separated by physical means; no fixed ratio / any proportions; '
    'each substance keeps its own properties; no chemical reaction when it is made; melts over a range.']},
  {'n':'7','marks':4,'lines':['(a) Grey and yellow specks visible / still looks like both <b>[1]</b>; a magnet pulls the iron out <b>[1]</b>',
    '(b) <b>Compound</b> <b>[1]</b>; evidence: magnet no longer attracts it / uniform grey / cannot be separated physically / a reaction (glowing) took place <b>[1]</b>']},
  {'n':'8','marks':3,'lines':['<b>Nitrogen</b> and <b>oxygen</b> <b>[1]</b>',
    'The gases are not chemically joined to each other <b>[1]</b>',
    'so they can be separated physically / the proportions can vary / each keeps its own properties <b>[1]</b>']},
  {'n':'9','marks':3,'lines':['An alloy such as brass (copper + zinc), steel (iron + carbon), bronze (copper + tin) <b>[1]</b>',
    'Named use, e.g. brass for taps and instruments, steel for buildings and cars <b>[1]</b>',
    'Accept any sensible solid–solid mixture with a use; award the third mark for saying why the mixture is better than the pure metal (harder, stronger, does not corrode) <b>[1]</b>']},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':6,'lines':['Joined: compound <b>yes</b>, mixture <b>no</b>','Fixed ratio: compound <b>yes</b>, mixture <b>no</b>',
    'Separated physically: compound <b>no</b>, mixture <b>yes</b>','Keeps properties: mixture <b>yes</b>','Sharp melting point: compound <b>yes</b>, mixture <b>no</b> (a range)',
    'One mark per box, six boxes marked (the seventh is given).']},
  {'n':'2','marks':3,'lines':['(a) <b>Compound</b> <b>[1]</b>',
    '(b) The sodium and chlorine atoms are chemically joined <b>[1]</b>, and a compound has its own properties, different from the elements it is made from <b>[1]</b>']},
  {'n':'3','marks':6,'lines':['(a) The iron filings are pulled out / jump to the magnet <b>[1]</b>; in a mixture the iron keeps its own property of being magnetic <b>[1]</b>',
    '(b) Nothing happens <b>[1]</b>; the iron atoms are now chemically joined to sulfur in a compound with its own (non-magnetic) properties <b>[1]</b>',
    '(c) In a compound the ratio is fixed <b>[1]</b>; any extra iron or sulfur is left over unreacted, it does not become part of the compound <b>[1]</b>'],
   'note':'(c) is the discriminator. Students who think a compound is "whatever you mixed" have not separated compound from mixture.'},
  {'n':'4','marks':6,'lines':['(a) <b>R</b> <b>[1]</b>; it melts sharply (one temperature) and at the data-book value <b>[1]</b>',
    '(b) <b>Q and S</b> <b>[1]</b>; they melt over a range <b>[1]</b>',
    '(c) P is pure (sharp melting point) <b>[1]</b> but is a different substance, not benzoic acid, because 118 °C does not match <b>[1]</b>'],
   'note':'Sample S melts over 117–121, a range just below 122 — it is impure, and a strong candidate may say it is only slightly impure. P is the trap: sharp does not mean "the substance on the label".'},
  {'n':'5','marks':3,'lines':['Measure its melting point (heat slowly, note when it starts and finishes melting) <b>[1]</b>',
    'Compare with the data-book value <b>[1]</b>',
    'A pure sample melts sharply at one temperature, equal to the data-book value <b>[1]</b>']},
  {'n':'6','marks':3,'lines':['Any two, with the reasoning making three marks in total:',
    'the proportions of the gases vary from place to place (e.g. water vapour) — a compound has a fixed ratio',
    'the gases can be separated physically (fractional distillation of liquid air) — a compound cannot',
    'each gas keeps its own properties (oxygen still supports burning) — a compound has new properties']},
  {'n':'7','marks':3,'lines':['The hydrogen and oxygen atoms are chemically joined <b>[1]</b>',
    'in a fixed ratio, so every water particle is identical <b>[1]</b>',
    'so there is only one kind of particle / one substance present, which is what pure means <b>[1]</b>']},
 ]},

 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':6,'lines':['(a) <b>80 °C</b> <b>[1]</b>; the temperature stays constant at one value while it melts (sharp melting point) <b>[1]</b>',
    '(b) <b>71 °C to 79 °C</b> (accept 71–80) <b>[1]</b>',
    '(c) Y is <b>impure</b> / a mixture <b>[1]</b>; because it melts over a range rather than at one temperature <b>[1]</b>, and starts melting below the pure melting point of 80 °C <b>[1]</b>'],
   'note':'Both samples were heated at the same rate and both climb 20 °C per minute either side of melting — the impurity changed only the shape of the middle.'},
  {'n':'2','marks':3,'lines':['Impurity particles get in between the particles of the solid / disrupt the regular arrangement <b>[1]</b>',
    'so the forces holding the pattern together are weakened <b>[1]</b>',
    'and less energy (a lower temperature) is needed to start breaking it apart <b>[1]</b>']},
  {'n':'3','marks':4,'lines':['Add water and stir <b>[1]</b>; filter <b>[1]</b>',
    'Mixture: a residue (sand) is left on the paper <b>[1]</b>','Pure: nothing is left on the paper, it all dissolves <b>[1]</b>',
    'Accept instead: measure the melting point — sharp for pure, a range for the mixture — for full marks if described properly.'],
   'note':'The question hands over filtration apparatus, so the filtration test is expected, but the melting-point test is a correct and complete alternative.'},
  {'n':'4','marks':4,'lines':['(a) Salt mixed with ice makes it impure <b>[1]</b>; an impure substance melts at a lower temperature, so the melting point falls below the air temperature and the ice melts <b>[1]</b>',
    '(b) Nothing has been heated — the temperature is unchanged <b>[1]</b>; what has changed is the <b>melting point</b> of the ice, which has dropped <b>[1]</b>']},
  {'n':'5','marks':6,'lines':['(a) <b>Element</b> <b>[1]</b>; only one kind of atom <b>[1]</b>',
    '(b) <b>Compound</b> <b>[1]</b>; two kinds of atom chemically joined in a fixed ratio <b>[1]</b>',
    '(c) <b>Mixture</b> <b>[1]</b>; the two kinds of atom are not joined and the proportion can vary <b>[1]</b>'],
   'note':'Brass is the one they get wrong — "it is a solid, so it must be a compound". Alloys are mixtures.'},
  {'n':'6','marks':3,'lines':['In carbon dioxide the carbon and oxygen atoms are chemically joined <b>[1]</b>',
    'in a fixed ratio (one carbon to two oxygen), so every particle is the same <b>[1]</b>',
    'A mixture would have separate carbon and oxygen particles, not joined, and could be separated physically — carbon dioxide cannot <b>[1]</b>']},
  {'n':'7','marks':4,'lines':['Sea water is impure (salt dissolved in it) <b>[1]</b>; impurities raise the boiling point <b>[1]</b>',
    'As it boils, water leaves as steam but the salt stays <b>[1]</b>, so the solution becomes more concentrated / more impure and the boiling point keeps rising <b>[1]</b>'],
   'note':'The second half is the hard part: the impurity lowers melting points but raises boiling points, and the rising temperature during boiling is a range, just as melting over a range is.'},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':6,'lines':['(a) <b>Naphthalene</b> <b>[1]</b>; it melts sharply at one temperature which matches the data-book value <b>[1]</b>',
    '(b) <b>Stearic acid</b> <b>[1]</b>; the range sits just below 69 °C, and an impurity lowers the melting point and spreads it into a range <b>[1]</b>',
    '(c) It melts over a range (118–122), so it is not pure <b>[1]</b>; a pure substance melts at one temperature, and reaching 122 °C at the end of a range is not the same as melting at 122 °C <b>[1]</b>'],
   'note':'(b): a candidate who says "urea" because 61–67 is "below 133" has not understood that impurities lower the melting point by a few degrees, not by seventy.'},
  {'n':'2','marks':6,'lines':['Award one mark for each of these, up to six:',
    'In water the hydrogen and oxygen atoms are chemically joined (bonded) together.',
    'They are joined in a fixed ratio — two hydrogen to one oxygen in every particle.',
    'So every water particle is identical: one kind of particle, which is what pure means.',
    'A compound has its own properties, different from its elements — water does not burn or support burning.',
    'A mixture would keep the properties of both gases and could have any proportions.',
    'The hydrogen and oxygen cannot be separated by physical means; it takes a chemical reaction.'],
   'note':'For full marks the answer must address both halves: why compound (joined, fixed ratio, new properties, not physically separable) and why pure (one kind of particle). Award at most four if only one half is covered.'},
  {'n':'3','marks':4,'lines':['(a) A <b>mixture</b> <b>[1]</b>; the hydrogen and oxygen particles were separate, not joined to each other <b>[1]</b>',
    '(b) The spark started a chemical reaction <b>[1]</b>; hydrogen and oxygen atoms became chemically joined to form water particles (a new substance, a compound) <b>[1]</b>']},
  {'n':'4','marks':3,'lines':['One mark for each genuine comparison, any three:',
    'mixture: iron is attracted to a magnet / compound: not attracted',
    'mixture: grey and yellow specks visible / compound: one uniform grey solid',
    'mixture: any ratio of iron to sulfur / compound: fixed ratio',
    'mixture: can be separated physically / compound: needs a chemical reaction',
    'mixture: made by stirring, no energy change / compound: made by a reaction that gives out heat and light']},
  {'n':'5','marks':3,'lines':['(a) A <b>compound</b> (joined pairs of two different atoms) <b>[1]</b>',
    '(b) Draw the black circles and the white circles as separate single circles scattered among each other, not touching in pairs <b>[1]</b>; '
    'because joining them means the atoms are chemically bonded, which is a compound, not a mixture of elements <b>[1]</b>']},
  {'n':'6','marks':5,'lines':[
    '(i) The mistake: "pure" in chemistry has nothing to do with being natural or untouched <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: a pure substance contains only one substance / one kind of particle, with nothing else mixed in <b>[2]</b>',
    '(ii) The mistake: it does not just move down — it also spreads out <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: an impure sample melts over a range of temperatures, and that range starts below the pure melting point <b>[1]</b>'],
   'note':'These are the two most common wrong sentences in the whole topic. If he can mark them in someone else&rsquo;s work, he is unlikely to write them in his own.'},
  {'n':'7','marks':3,'lines':['Every pure substance has its own fixed, sharp melting point, listed in data books <b>[1]</b>',
    'so measuring it and matching the value identifies the substance <b>[1]</b>',
    'A mixture melts over a range that depends on how much impurity is present and what it is, so the range is not a fixed property of any one substance <b>[1]</b>']},
 ]},
]

files = []
for spec, code in [(A,'a'), (B,'b'), (C,'c'), (D,'d')]:
    t = sum(q.get('marks',0) for q in spec['questions'])
    assert t == 30, (spec['title'], t)
    for q in spec['questions']:
        if 'parts' in q:
            assert sum(p['marks'] for p in q['parts']) == q['marks'], (spec['title'], q['text'][:40])
    p = os.path.join(OUT, 'chemistry-mixtures-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)
for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)
p = os.path.join(OUT, 'chemistry-mixtures-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. Almost every mark on this topic turns on one word — '
             '<b>joined</b>. Two kinds of atom joined is a compound and pure; two kinds side by side is a mixture. The other '
             'recurring loss is the melting-point test written by halves: "lower" without "over a range", or the reverse. '
             'The notes under each answer flag the specific mistake that question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
