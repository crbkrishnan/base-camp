#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Two biology mock papers — 80 marks each, medium to hard, 90 minutes.

These are end-of-term mocks, not topic drills, so the 30-mark rule in
docs/WRITING-PAPERS.md does not apply here: _verify() asserts 80 for each paper
and checks that every part-mark total agrees with its question. They span
Unit 2.2 (gas exchange), 2.3 (circulation), 3.1 (ecosystems) and 3.2 (human
impact), which are the four biology topics taught on the site.

Every number below was computed by _verify() before it was typeset.
"""
import os, sys
from fractions import Fraction as F
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)

EYEBROW = 'Base Camp · IGCSE Biology · Grade 7 · Mock examination'

INSTR = [
 'Answer <b>every</b> question in the space provided. Show your working and your reasoning — method marks are awarded even when the final answer is wrong.',
 'A calculator is allowed, but every number on this paper is designed to work without one.',
 'The mark for each question is shown in square brackets on the right. There are <b>80 marks</b> in <b>90 minutes</b>.',
 'Where a question says <b>explain</b>, a feature on its own is not enough — say what it achieves. &ldquo;The wall is thin&rdquo; is a description; &ldquo;thin, so the diffusion distance is short&rdquo; is an explanation.',
 'Where a question asks for a sequence, write it <b>in order</b> and make each step the cause of the next. Naming only the first and last steps scores the marks for neither.',
 'Section 1 is recall, Section 2 is explanation, Section 3 is data and problems. Work in order and do not spend more than six minutes stuck on any one question.',
]

# ===================================================================== MOCK 1
M1 = [
 # ----------------------------------------------- Section 1 — 22 marks
 {'section':'Section 1 — the mechanics',
  'text':'The thorax and its muscles.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name the muscle that forms the floor of the thorax.','marks':1,'space':18},
           {'label':'(b)','text':'State what this muscle does during inhalation.','marks':1,'space':20}]},

 {'text':'Complete these figures for the composition of <b>expired</b> air.', 'marks':2,
  'parts':[{'label':'(a)','text':'Approximate percentage of oxygen.','marks':1,'space':18},
           {'label':'(b)','text':'Approximate percentage of carbon dioxide.','marks':1,'space':18}]},

 {'text':'Blood returning from the lungs.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name the blood vessel that carries blood from the lungs to the heart.','marks':1,'space':18},
           {'label':'(b)','text':'Name the chamber of the heart that this blood enters.','marks':1,'space':18}]},

 {'text':'Valves in the heart.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name the valve between the right atrium and the right ventricle.','marks':1,'space':18},
           {'label':'(b)','text':'State the function of this valve.','marks':1,'space':22}]},

 {'text':'Name <b>two</b> components of blood other than plasma, and state one function of each.',
  'marks':2, 'space':30},

 {'text':'Define each of these ecological terms.', 'marks':2,
  'parts':[{'label':'(a)','text':'Habitat','marks':1,'space':20},
           {'label':'(b)','text':'Community','marks':1,'space':22}]},

 {'text':'A food chain in a lake is: &nbsp;algae &rarr; water flea &rarr; small fish &rarr; heron.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name the producer.','marks':1,'space':16},
           {'label':'(b)','text':'State the trophic level of the small fish, as a number and as a name.','marks':1,'space':20}]},

 {'text':'Decomposers.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name the <b>two</b> groups of organisms that act as decomposers.','marks':1,'space':18},
           {'label':'(b)','text':'State what decomposers return to the soil.','marks':1,'space':18}]},

 {'text':'Greenhouse gases.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name one greenhouse gas other than water vapour.','marks':1,'space':16},
           {'label':'(b)','text':'State one human activity that increases the concentration of the gas you named.','marks':1,'space':20}]},

 {'text':'Testing for carbon dioxide.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name the solution used, and state what you would see if carbon dioxide is present.','marks':1,'space':20},
           {'label':'(b)','text':'State whether inspired or expired air produces this change faster, and why.','marks':1,'space':22}]},

 {'text':'State <b>two</b> differences between inspired and expired air, other than the oxygen content.',
  'marks':2, 'space':26,
  'tip':'Two marks, two differences. One of them is not a gas at all.'},

 # ----------------------------------------------- Section 2 — 33 marks
 {'section':'Section 2 — explanation',
  'text':'Describe, in order, what happens in the thorax during <b>inhalation</b>. Begin with the muscles and end with the movement of air.',
  'marks':3, 'space':46,
  'tip':'Three marks, and the order is the mark scheme. Muscles change volume; volume changes pressure; pressure moves the air.'},

 {'text':'Explain <b>three</b> ways in which an alveolus is adapted for rapid gas exchange. In each case state what the adaptation achieves.',
  'marks':3, 'space':48},

 {'text':'Explain why the wall of the left ventricle is much thicker than the wall of the right ventricle.',
  'marks':3, 'space':44,
  'tip':'Start by stating what is the <i>same</i> about the two ventricles. That sentence is worth a mark and it stops you writing the usual wrong answer.'},

 {'text':'Compare an artery with a vein. Give <b>three</b> structural differences.', 'marks':3, 'space':44},

 {'text':'Blood travels more slowly through the capillaries than through any other vessel. '
         'Explain why, and explain why this is an advantage.', 'marks':3, 'space':46},

 {'text':'Describe the path taken by a drop of blood from the vena cava to the aorta, naming every '
         'chamber and vessel it passes through, in order.', 'marks':3, 'space':46},

 {'text':'Explain the difference between the way <b>energy</b> moves through an ecosystem and the way '
         '<b>nutrients</b> move through it.', 'marks':3, 'space':46,
  'tip':'One of the two words in bold goes in a straight line and one goes round in a circle. Say which, and say what happens at the end of the straight line.'},

 {'text':'Explain why food chains rarely contain more than four or five trophic levels.', 'marks':3, 'space':44},

 {'text':'Describe how a student would use a quadrat to estimate the number of dandelions in a field.',
  'marks':3, 'space':46},

 {'text':'Explain how cutting down a forest raises the concentration of carbon dioxide in the atmosphere. '
         'Give two separate mechanisms, then state one <b>other</b> consequence of deforestation.',
  'marks':3, 'space':48},

 {'text':'Describe how the greenhouse effect warms the Earth. Write it as three linked steps.',
  'marks':3, 'space':46},

 # ----------------------------------------------- Section 3 — 25 marks
 {'section':'Section 3 — data and problems',
  'text':'At rest, Priya takes 14 breaths a minute and moves 480 cm&sup3; of air with each breath. '
         'Her heart beats 68 times a minute and pushes out 72 cm&sup3; of blood per beat.', 'marks':5,
  'parts':[{'label':'(a)','text':'Calculate her ventilation rate, in dm&sup3; per minute.','marks':2,'space':34},
           {'label':'(b)','text':'Calculate her cardiac output, in dm&sup3; per minute.','marks':2,'space':34},
           {'label':'(c)','text':'During exercise both of these values rise. Explain why.','marks':1,'space':30}],
  'tip':'Both calculations are the same shape: how many times a minute, multiplied by how much each time. Convert to dm&sup3; once, at the end.'},

 {'text':'A healthy pair of lungs contains 3.0 &times; 10<super>8</super> alveoli, each with a surface area of '
         '2.4 &times; 10<super>&minus;7</super> m&sup2;.', 'marks':5,
  'parts':[{'label':'(a)','text':'Calculate the total surface area available for gas exchange, in m&sup2;.','marks':2,'space':34},
           {'label':'(b)','text':'A patient with emphysema has 9.0 &times; 10<super>7</super> alveoli, each with a surface area of '
                                 '4.0 &times; 10<super>&minus;7</super> m&sup2;. Calculate his total surface area and the percentage '
                                 'reduction compared with a healthy pair of lungs.','marks':2,'space':40},
           {'label':'(c)','text':'Explain why he becomes breathless climbing one flight of stairs.','marks':1,'space':30}],
  'tip':'Multiply the numbers, then add the powers of ten. Note that his individual alveoli are <i>larger</i> — and his total area is still smaller.'},

 {'text':'A food web in a meadow contains these feeding relationships:<br/>'
         'grass &rarr; grasshopper &rarr; shrew &rarr; owl &nbsp;&middot;&nbsp; grass &rarr; rabbit &rarr; fox '
         '&nbsp;&middot;&nbsp; shrew &rarr; fox', 'marks':5,
  'parts':[{'label':'(a)','text':'Name the organisms at trophic level 2.','marks':1,'space':20},
           {'label':'(b)','text':'A disease kills every rabbit. State and explain what happens to (i) the grass '
                                 'and (ii) the fox population.','marks':2,'space':40},
           {'label':'(c)','text':'Use this web to explain why a food web is more stable than a single food chain.',
             'marks':2,'space':38}]},

 {'text':'The producers in a lake capture 48 000 kJ of energy per square metre per year. About 10% of the '
         'energy at each trophic level is passed on to the next.', 'marks':5,
  'parts':[{'label':'(a)','text':'Calculate the energy available to the primary consumers, in kJ/m&sup2;/year.','marks':1,'space':28},
           {'label':'(b)','text':'Calculate the energy available to the tertiary consumers, and express it as a '
                                 'percentage of the energy captured by the producers.','marks':2,'space':38},
           {'label':'(c)','text':'A fish farm grinds small fish into pellets and feeds them to larger fish, which are '
                                 'then sold. Explain, in energy terms, why selling the small fish for people to eat '
                                 'would feed more people.','marks':2,'space':40}]},

 {'text':'Water was sampled downstream of a pipe carrying run-off from a fertilised field. '
         'Fish need more than 5 mg/dm&sup3; of dissolved oxygen to survive.', 'marks':5,
  'grid':[['Distance / m','0','100','300','600','1200'],
          ['Nitrate / mg dm&#8315;&sup3;','48','41','26','11','4'],
          ['Oxygen / mg dm&#8315;&sup3;','8.8','2.6','1.4','4.9','8.1']],
  'grid_widths':[AVAIL*0.30] + [AVAIL*0.14]*5,
  'parts':[{'label':'(a)','text':'State the distance at which the dissolved oxygen is lowest.','marks':1,'space':18},
           {'label':'(b)','text':'Calculate the percentage decrease in nitrate concentration between 0 m and 600 m.','marks':2,'space':34},
           {'label':'(c)','text':'Explain, in order, how the nitrate in the water causes the fall in dissolved oxygen.','marks':2,'space':44}],
  'tip':'In (c) there are five links between the nitrate and the oxygen, and none of them involves anything poisonous.'},
]

# ===================================================================== MOCK 2
M2 = [
 # ----------------------------------------------- Section 1 — 22 marks
 {'section':'Section 1 — the mechanics',
  'text':'The trachea.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name the tissue that forms rings around the trachea.','marks':1,'space':18},
           {'label':'(b)','text':'Explain why these rings are needed.','marks':1,'space':22}]},

 {'text':'Two types of cell line the airways.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name the cells that produce mucus, and state what the mucus does.','marks':1,'space':20},
           {'label':'(b)','text':'State what the cilia do.','marks':1,'space':20}]},

 {'text':'Aerobic respiration.', 'marks':2,
  'parts':[{'label':'(a)','text':'Write the word equation for aerobic respiration.','marks':1,'space':22},
           {'label':'(b)','text':'State where in a cell it takes place.','marks':1,'space':16}]},

 {'text':'Blood on its way to the lungs.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name the blood vessel that carries blood from the heart to the lungs.','marks':1,'space':18},
           {'label':'(b)','text':'Name the chamber of the heart that this blood leaves from.','marks':1,'space':18}]},

 {'text':'State <b>two</b> ways in which a red blood cell is adapted for carrying oxygen.',
  'marks':2, 'space':28},

 {'text':'Define each of these ecological terms.', 'marks':2,
  'parts':[{'label':'(a)','text':'Population','marks':1,'space':20},
           {'label':'(b)','text':'Ecosystem','marks':1,'space':24}]},

 {'text':'Food chains.', 'marks':2,
  'parts':[{'label':'(a)','text':'State what the arrows in a food chain represent.','marks':1,'space':20},
           {'label':'(b)','text':'State what a producer does that no consumer can do.','marks':1,'space':20}]},

 {'text':'Energy transfer between trophic levels.', 'marks':2,
  'parts':[{'label':'(a)','text':'State approximately what percentage of the energy is passed on to the next level.','marks':1,'space':16},
           {'label':'(b)','text':'Name the route by which most of the rest is lost.','marks':1,'space':18}]},

 {'text':'Fertiliser and rivers.', 'marks':2,
  'parts':[{'label':'(a)','text':'Name the process by which nitrates are washed from fields into a river.','marks':1,'space':18},
           {'label':'(b)','text':'Name the organisms whose rapid growth follows.','marks':1,'space':16}]},

 {'text':'Name <b>two</b> human activities that reduce biodiversity.', 'marks':2, 'space':26},

 {'text':'Breathing and respiration.', 'marks':2,
  'parts':[{'label':'(a)','text':'State one difference between breathing and respiration.','marks':1,'space':22},
           {'label':'(b)','text':'State where in the body respiration takes place.','marks':1,'space':18}]},

 # ----------------------------------------------- Section 2 — 33 marks
 {'section':'Section 2 — explanation',
  'text':'Describe, in order, what happens in the thorax during quiet <b>exhalation</b>. Begin with the muscles '
         'and end with the movement of air.', 'marks':3, 'space':46,
  'tip':'One word earns a mark here and most candidates avoid it because it sounds like doing nothing. The muscles <i>relax</i>.'},

 {'text':'Explain <b>three</b> separate ways in which smoking damages the gas exchange and transport systems.',
  'marks':3, 'space':48},

 {'text':'Explain why veins contain valves along their length but arteries do not.', 'marks':3, 'space':44},

 {'text':'Explain what is meant by a <b>double circulation</b>, and give one advantage of having one.',
  'marks':3, 'space':46},

 {'text':'Describe <b>three</b> features of a capillary that make it suited to exchanging substances with '
         'body cells. In each case state what the feature achieves.', 'marks':3, 'space':48},

 {'text':'Describe what happens to blood pressure between the aorta and the vena cava, and explain how blood '
         'is returned to the heart despite this.', 'marks':3, 'space':46},

 {'text':'Explain why a pyramid of numbers is sometimes inverted, while a pyramid of biomass for the same '
         'food chain is not.', 'marks':3, 'space':46},

 {'text':'Describe the role of decomposers in an ecosystem, and explain what would happen to the ecosystem '
         'without them.', 'marks':3, 'space':46},

 {'text':'Describe how a <b>transect</b> is used, and explain when it is a better method than placing quadrats '
         'at random.', 'marks':3, 'space':46},

 {'text':'Explain how the enhanced greenhouse effect causes sea levels to rise, and state one consequence '
         'for living organisms.', 'marks':3, 'space':46},

 {'text':'Describe <b>three</b> measures that would reduce eutrophication in a river running past farmland.',
  'marks':3, 'space':44},

 # ----------------------------------------------- Section 3 — 25 marks
 {'section':'Section 3 — data and problems',
  'text':'A student measures his breathing before and after exercise.<br/>'
         'At rest: 15 breaths per minute, 500 cm&sup3; per breath. '
         'After exercise: 28 breaths per minute, 1750 cm&sup3; per breath.', 'marks':5,
  'parts':[{'label':'(a)','text':'Calculate his ventilation rate at rest and after exercise, both in dm&sup3; per minute.','marks':2,'space':36},
           {'label':'(b)','text':'Calculate how many times greater the second value is, to one decimal place.','marks':1,'space':26},
           {'label':'(c)','text':'Explain why both the rate and the depth of his breathing increased.','marks':2,'space':38}]},

 {'text':'Fully working blood carries 200 cm&sup3; of oxygen per dm&sup3;. A heavy smoker has 15% of his '
         'haemoglobin permanently bound to carbon monoxide. His cardiac output at rest is 5.2 dm&sup3; per minute.',
  'marks':5,
  'parts':[{'label':'(a)','text':'Calculate the volume of oxygen 1 dm&sup3; of his blood can carry.','marks':1,'space':28},
           {'label':'(b)','text':'Calculate the volume of oxygen his blood delivers each minute, and how much less '
                                 'this is than a non-smoker with the same cardiac output.','marks':2,'space':38},
           {'label':'(c)','text':'His alveoli are undamaged and his breathing rate is normal, yet he is breathless '
                                 'walking uphill. Explain why.','marks':2,'space':40}],
  'tip':'If 15% is out of action, multiply by what is left. Subtracting 15 from 200 is the error this question is built to catch.'},

 {'text':'A student estimates the number of plantains in a field of area 250 m&sup2;. She places a quadrat '
         'measuring 0.25 m &times; 0.25 m at eight random positions and counts:<br/>'
         '<b>3, 5, 2, 6, 4, 3, 5, 4</b>', 'marks':5,
  'parts':[{'label':'(a)','text':'Calculate the mean number per quadrat and estimate the total number of plantains '
                                 'in the field.','marks':2,'space':38},
           {'label':'(b)','text':'Give one way she could make her estimate more reliable.','marks':1,'space':24},
           {'label':'(c)','text':'In a predator&ndash;prey cycle, the peak in the predator population always comes '
                                 '<i>after</i> the peak in the prey population. Explain why.','marks':2,'space':40}],
  'tip':'The quadrat is a quarter of a metre on each side, so its area is not 0.25 m&sup2;. Work the area out before you divide by it.'},

 {'text':'A forest covers 480 000 hectares and absorbs about 5.5 tonnes of carbon dioxide per hectare each year. '
         '12 000 hectares are cleared every year.', 'marks':5,
  'parts':[{'label':'(a)','text':'Calculate the mass of carbon dioxide the whole forest absorbs in one year. '
                                 'Give your answer in tonnes, in standard form.','marks':2,'space':34},
           {'label':'(b)','text':'Calculate the reduction in the forest’s annual absorption caused by one year of clearing.','marks':1,'space':28},
           {'label':'(c)','text':'Explain why the total effect on atmospheric carbon dioxide is greater than your '
                                 'answer to (b).','marks':2,'space':40}]},

 {'text':'Three answers from another student’s mock paper are shown below. Each one is wrong. For each, '
         'explain what is wrong with it and give the correct version.', 'marks':5,
  'parts':[{'label':'(a)','text':'&ldquo;Arteries carry oxygenated blood and veins carry deoxygenated blood.&rdquo;','marks':2,'space':36},
           {'label':'(b)','text':'&ldquo;Fertiliser running into a river poisons the fish and they die.&rdquo;','marks':2,'space':38},
           {'label':'(c)','text':'&ldquo;Energy is recycled around an ecosystem by the decomposers.&rdquo;','marks':1,'space':30}],
  'tip':'A mark for saying what is wrong, a mark for the correction. Naming the rule the student broke is worth more than simply writing a better sentence.'},
]


def spec(name, questions, marks=80):
    return {
      'eyebrow': EYEBROW,
      'title': 'Biology Mock ' + name + ' &mdash; Units 2 and 3',
      'meta': 'MtoH · 90 minutes · 80 marks',
      'marks': marks, 'instructions': INSTR,
      'footer': 'Biology Mock ' + name + ' · MtoH · gas exchange, circulation, ecosystems, human impact',
      'endnote': 'End of paper. Go back to every question that asked you to <i>explain</i> and check that each '
                 'feature you named is followed by what it achieves. That is where this paper is won and lost.',
      'questions': questions,
    }


# ----------------------------------------------------------------- mark scheme
def B(n):
    return ' <b>[%d]</b>' % n

S1 = [
 {'n':'1','marks':2,
  'lines':['(a) the <b>diaphragm</b>' + B(1),
           '(b) it <b>contracts</b> and flattens, moving down' + B(1)],
  'note':'&ldquo;The diaphragm goes down&rdquo; without the word contracts scores 0 in (b). The muscle action is the mark; the movement is the consequence.'},
 {'n':'2','marks':2,
  'lines':['(a) about <b>16%</b> oxygen' + B(1),
           '(b) about <b>4%</b> carbon dioxide' + B(1)],
  'note':'Accept 15–17% and 3–5%. A candidate who writes 0.04% for expired carbon dioxide has memorised the inspired figure — worth pointing out, because the hundredfold difference is the whole basis of the limewater test.'},
 {'n':'3','marks':2,
  'lines':['(a) the <b>pulmonary vein</b>' + B(1),
           '(b) the <b>left atrium</b>' + B(1)],
  'note':'Pulmonary artery in (a) is the standard error. If they also wrote &ldquo;right atrium&rdquo; in (b) they have the whole right side of the heart mirrored — worth a two-minute redraw rather than a correction.'},
 {'n':'4','marks':2,
  'lines':['(a) the <b>tricuspid</b> valve (accept right atrioventricular valve)' + B(1),
           '(b) it prevents blood flowing backwards into the atrium when the ventricle contracts' + B(1)],
  'note':'&ldquo;It stops the blood&rdquo; is not enough for (b) — the direction and the moment both matter.'},
 {'n':'5','marks':2,
  'lines':['Any two of: <b>red blood cells</b> — carry oxygen as oxyhaemoglobin; <b>white blood cells</b> — '
           'defend against microbes by engulfing them or making antibodies; <b>platelets</b> — cause blood to clot'
           + B(2) + ' (1 for each component with a correct function)'],
  'note':'A component with no function, or a function with no component, scores nothing. Plasma is excluded by the question.'},
 {'n':'6','marks':2,
  'lines':['(a) <b>habitat</b>: the place where an organism lives' + B(1),
           '(b) <b>community</b>: all the populations of all the different species living in an area' + B(1)],
  'note':'The word &ldquo;all&rdquo; is doing the work in (b). A community of one species is a population, and that confusion runs through the whole unit.'},
 {'n':'7','marks':2,
  'lines':['(a) the <b>algae</b>' + B(1),
           '(b) trophic level <b>3</b>, a <b>secondary consumer</b>' + B(1)],
  'note':'Level 2 is the commonest wrong answer — counting the water flea as level 1 because it is the first animal. Count from the producer.'},
 {'n':'8','marks':2,
  'lines':['(a) <b>bacteria</b> and <b>fungi</b>' + B(1) + ' (both needed)',
           '(b) <b>mineral ions</b> / nutrients such as nitrates' + B(1)],
  'note':'&ldquo;Nutrients&rdquo; alone is acceptable; &ldquo;energy&rdquo; is not, and is the answer to watch for — it is the flow-versus-cycle confusion appearing early.'},
 {'n':'9','marks':2,
  'lines':['(a) carbon dioxide, methane or nitrous oxide' + B(1),
           '(b) a matching activity: burning fossil fuels or deforestation (carbon dioxide); cattle farming, rice '
           'paddies or landfill (methane); nitrogen fertilisers or vehicle exhausts (nitrous oxide)' + B(1)],
  'note':'The two marks must match each other. Naming methane and then writing &ldquo;burning fossil fuels&rdquo; scores the first only.'},
 {'n':'10','marks':2,
  'lines':['(a) <b>limewater</b>; it turns <b>milky / cloudy</b>' + B(1),
           '(b) <b>expired</b> air, because it contains about a hundred times more carbon dioxide (about 4% against 0.04%)' + B(1)],
  'note':'Both halves are needed in (a). &ldquo;It goes white&rdquo; is acceptable; &ldquo;it changes colour&rdquo; is not.'},
 {'n':'11','marks':2,
  'lines':['Any two of: expired air contains <b>more carbon dioxide</b>; contains <b>more water vapour</b> '
           '(saturated); is <b>warmer</b>' + B(2)],
  'note':'Temperature is the one most candidates miss, because they are looking for a gas. Nitrogen is unchanged and scores nothing.'},

 {'n':'12','marks':3,
  'lines':['the diaphragm contracts and flattens; the external intercostal muscles contract, pulling the ribs up and out' + B(1),
           'the volume of the thorax increases' + B(1),
           'so the pressure inside the lungs falls below atmospheric pressure, and air flows in down the pressure gradient' + B(1)],
  'note':'Order is the mark scheme. &ldquo;The lungs suck air in&rdquo; scores 0 for the whole question — nothing sucks, and a candidate who writes it has not understood any of the three steps.'},
 {'n':'13','marks':3,
  'lines':['very large total surface area (about 50 m² from 300 million alveoli) — more area for diffusion' + B(1),
           'wall only one cell thick — a very short diffusion distance' + B(1),
           'dense capillary network with blood constantly flowing, and a moist lining — maintains the concentration '
           'gradient and lets gases dissolve before they diffuse' + B(1)],
  'note':'Each mark needs feature <i>plus</i> consequence. Three bare features score 1 at most, and telling a candidate that once is worth more than marking it three times.'},
 {'n':'14','marks':3,
  'lines':['both ventricles pump the same volume of blood per beat' + B(1),
           'the left ventricle pumps blood all round the body, a far greater distance against far greater resistance, '
           'while the right pumps only to the lungs' + B(1),
           'so the left ventricle must generate a much higher pressure, which needs more muscle' + B(1)],
  'note':'&ldquo;It holds more blood&rdquo; scores 0 and contradicts the first marking point. Candidates who open with the same-volume sentence almost never then write the wrong reason.'},
 {'n':'15','marks':3,
  'lines':['artery wall thick with muscle and elastic tissue; vein wall thin' + B(1),
           'artery lumen narrow; vein lumen wide' + B(1),
           'artery has no valves; vein has valves along its length' + B(1)],
  'note':'The question said <i>structural</i>, so &ldquo;arteries carry blood away from the heart&rdquo; earns nothing here even though it is true. Marks are for the three physical differences.'},
 {'n':'16','marks':3,
  'lines':['the capillaries together have a far greater total cross-sectional area than the aorta (about 1000 times)' + B(1),
           'the same volume of blood must pass every point each second, so a greater area means a lower speed' + B(1),
           'the slow flow gives time for diffusion, so exchange of oxygen, glucose and waste can be completed' + B(1)],
  'note':'This is the hardest of the Section 2 questions. A candidate who says &ldquo;capillaries are narrow so blood is slow&rdquo; has the right answer for the wrong reason and scores the third mark only.'},
 {'n':'17','marks':3,
  'lines':['vena cava → right atrium → right ventricle' + B(1),
           '→ pulmonary artery → lungs → pulmonary vein' + B(1),
           '→ left atrium → left ventricle → aorta' + B(1)],
  'note':'Any route that misses the lungs, or that goes from the lungs straight to the aorta, loses everything after the error. The double circulation is the point of the question.'},
 {'n':'18','marks':3,
  'lines':['energy enters as light, is captured by producers and passes up the trophic levels in one direction' + B(1),
           'it is lost as heat at every level and is never reused, which is why the Sun must keep supplying more' + B(1),
           'nutrients (carbon, nitrogen, mineral ions) are taken up, passed on, released by decomposers and taken up '
           'again — they cycle indefinitely' + B(1)],
  'note':'&ldquo;Energy is recycled&rdquo; anywhere in the answer caps it at 1. This single sentence appears in most papers on this unit and is the most useful thing to correct.'},
 {'n':'19','marks':3,
  'lines':['only about 10% of the energy at one level is transferred to the next' + B(1),
           'about 90% is lost as heat in respiration, in faeces and urine, and in parts that are not eaten' + B(1),
           'after four or five levels there is too little energy left to support another population' + B(1)],
  'note':'&ldquo;Energy is lost&rdquo; without the figure scores 1. The 10% is what turns a vague answer into a full one.'},
 {'n':'20','marks':3,
  'lines':['place the quadrat at <b>random</b> positions, e.g. using random number coordinates' + B(1),
           'count the dandelions inside it and <b>repeat</b> many times, then calculate the mean per quadrat' + B(1),
           'divide by the area of the quadrat to get a density per m², then multiply by the total area of the field' + B(1)],
  'note':'The two words that carry marks are random and repeat. &ldquo;Throw the quadrat over your shoulder&rdquo; is accepted as random in most schemes but is worth discouraging.'},
 {'n':'21','marks':3,
  'lines':['fewer trees photosynthesising, so less carbon dioxide is removed from the atmosphere' + B(1),
           'carbon stored in the wood is released as carbon dioxide when it is burned or decays' + B(1),
           'plus any one other: habitats destroyed and biodiversity lost; soil erosion and leaching once the roots '
           'are gone; less transpiration so reduced local rainfall' + B(1)],
  'note':'Most candidates give the first mechanism only and then a consequence, scoring 2 of 3. The release from the felled wood is the missing mark almost every time.'},
 {'n':'22','marks':3,
  'lines':['short-wave radiation from the Sun passes through the atmosphere and warms the Earth’s surface' + B(1),
           'the warmed surface radiates energy back out as longer-wave infrared' + B(1),
           'greenhouse gases absorb this infrared and re-radiate it in all directions, including back towards the '
           'surface, so less heat escapes to space' + B(1)],
  'note':'Any mention of the ozone layer or a &ldquo;hole&rdquo; is a different topic and scores nothing. It is worth naming that explicitly when returning the paper.'},

 {'n':'23','marks':5,
  'lines':['(a) 14 × 480 = 6720 cm³ per minute' + B(1) + ' = <b>6.72 dm³ per minute</b>' + B(1),
           '(b) 68 × 72 = 4896 cm³ per minute' + B(1) + ' = <b>4.90 dm³ per minute</b> (4.896)' + B(1),
           '(c) her muscles respire faster, so they need more oxygen and produce more carbon dioxide; more air must '
           'be moved and more blood delivered each minute' + B(1)],
  'note':'The conversion is where marks go: dividing by 100 instead of 1000 gives 67.2 and 48.96, which look wrong '
         'by inspection — a resting person does not breathe 67 dm³ a minute. Teach the sanity check, not the rule.'},
 {'n':'24','marks':5,
  'lines':['(a) 3.0 × 10⁸ × 2.4 × 10⁻⁷: multiply 3.0 × 2.4 = 7.2, add the powers 8 + (−7) = 1' + B(1) +
           ' = 7.2 × 10¹ = <b>72 m²</b>' + B(1),
           '(b) 9.0 × 10⁷ × 4.0 × 10⁻⁷ = 3.6 × 10¹ = <b>36 m²</b>' + B(1) +
           '; reduction = (72 − 36) ÷ 72 × 100 = <b>50%</b>' + B(1),
           '(c) with half the surface area oxygen diffuses into the blood far more slowly; climbing stairs makes his '
           'muscles demand much more oxygen, which his lungs cannot supply, so he is breathless' + B(1)],
  'note':'Note the trap in (b): his individual alveoli are <i>larger</i> (4.0 against 2.4 × 10⁻⁷ m²) and his total '
         'area is still halved, because there are so many fewer of them. A candidate who answers &ldquo;his surface '
         'area went up&rdquo; has reasoned from the wrong number and should redo it, not be told the answer.'},
 {'n':'25','marks':5,
  'lines':['(a) the <b>grasshopper</b> and the <b>rabbit</b>' + B(1),
           '(b)(i) the grass <b>increases</b>, because fewer herbivores are eating it' + B(1),
           '(b)(ii) the fox population <b>falls at first but survives</b>, because it can eat more shrews instead' + B(1),
           '(c) most organisms in a web have more than one food source, so they can switch when one prey species is '
           'lost' + B(1) + '; energy has alternative routes through the web, so losing one species does not break '
           'every link and the community stays stable' + B(1)],
  'note':'In (b)(ii) an answer of &ldquo;the fox dies out&rdquo; scores 0 and shows the candidate read the web as two '
         'separate chains. Point at the shrew → fox arrow rather than explaining it.'},
 {'n':'26','marks':5,
  'lines':['(a) 48 000 × 0.1 = <b>4800 kJ/m²/year</b>' + B(1),
           '(b) 4800 × 0.1 = 480, then 480 × 0.1 = <b>48 kJ/m²/year</b>' + B(1) +
           '; (48 ÷ 48 000) × 100 = <b>0.1%</b>' + B(1),
           '(c) feeding small fish to larger fish adds an extra trophic level' + B(1) +
           '; about 90% of the energy is lost at that transfer, so only about a tenth as much energy reaches people '
           'as would if they ate the small fish directly' + B(1)],
  'note':'The level-counting error gives 480 in (b) instead of 48. Ask which organism is the tertiary consumer before '
         'correcting the arithmetic — the arithmetic is usually right, the counting is not.'},
 {'n':'27','marks':5,
  'lines':['(a) <b>300 m</b>' + B(1),
           '(b) decrease = 48 − 11 = 37 mg/dm³' + B(1) + '; (37 ÷ 48) × 100 = <b>77.1%</b>' + B(1),
           '(c) the nitrate causes algae to grow rapidly (an algal bloom), which blocks light so the plants on the '
           'river bed die' + B(1) + '; decomposer bacteria multiply on the dead material and use up the dissolved '
           'oxygen in their aerobic respiration' + B(1)],
  'note':'&ldquo;The nitrate uses up the oxygen&rdquo; scores 0 in (c) — nitrate does nothing to oxygen directly. '
         'The chain runs nitrate → algae → light → dead plants → bacteria → oxygen, and the two most-dropped words '
         'are <i>light</i> and <i>aerobic</i>.'},
]

S2 = [
 {'n':'1','marks':2,
  'lines':['(a) rings of <b>cartilage</b>' + B(1),
           '(b) they hold the trachea open / stop it collapsing when air is drawn in at low pressure' + B(1)],
  'note':'&ldquo;To protect it&rdquo; scores 0. The rings solve a specific mechanical problem, and naming that problem is the mark.'},
 {'n':'2','marks':2,
  'lines':['(a) <b>goblet cells</b>; the mucus traps dust, pollen, bacteria and other particles' + B(1),
           '(b) cilia beat to sweep the mucus and trapped particles up the trachea to the throat, where it is swallowed' + B(1)],
  'note':'Both halves needed in (a). A candidate who has these two cells the wrong way round will also get the smoking question wrong — check Q13 before deciding it was a slip.'},
 {'n':'3','marks':2,
  'lines':['(a) glucose + oxygen → carbon dioxide + water (energy released)' + B(1),
           '(b) in the <b>mitochondria</b>' + B(1)],
  'note':'&ldquo;Energy is made&rdquo; or &ldquo;energy is produced&rdquo; loses the mark in some schemes. Energy is released from glucose; it is not created.'},
 {'n':'4','marks':2,
  'lines':['(a) the <b>pulmonary artery</b>' + B(1),
           '(b) the <b>right ventricle</b>' + B(1)],
  'note':'&ldquo;Right atrium&rdquo; in (b) is common. Blood always leaves the heart from a ventricle; atria only pass it downwards.'},
 {'n':'5','marks':2,
  'lines':['Any two of: <b>biconcave disc shape</b> — large surface area and a short diffusion distance to the centre; '
           '<b>no nucleus</b> — more room for haemoglobin; <b>contains haemoglobin</b> — binds oxygen to form '
           'oxyhaemoglobin' + B(2)],
  'note':'A shape with no consequence scores half an idea and no mark. &ldquo;It is small so it fits through capillaries&rdquo; is true but is not an adaptation for <i>carrying</i> oxygen, which is what the question asked.'},
 {'n':'6','marks':2,
  'lines':['(a) <b>population</b>: all the members of one species living in an area' + B(1),
           '(b) <b>ecosystem</b>: all the organisms in an area together with the non-living parts of their '
           'surroundings, interacting' + B(1)],
  'note':'An ecosystem definition with no mention of non-living factors scores 0. This is a one-word fix and worth insisting on.'},
 {'n':'7','marks':2,
  'lines':['(a) the direction in which <b>energy</b> (and biomass) is transferred, from the organism eaten to the '
           'organism eating it' + B(1),
           '(b) a producer makes its own food by <b>photosynthesis</b>, capturing light energy' + B(1)],
  'note':'&ldquo;Shows what eats what&rdquo; scores 0 — it describes the diagram without saying what the arrow means.'},
 {'n':'8','marks':2,
  'lines':['(a) about <b>10%</b>' + B(1),
           '(b) lost as <b>heat</b> released during respiration' + B(1)],
  'note':'Accept faeces/urine or uneaten parts in (b), but heat is the largest route and the one to teach.'},
 {'n':'9','marks':2,
  'lines':['(a) <b>leaching</b> (accept run-off)' + B(1),
           '(b) <b>algae</b> (an algal bloom)' + B(1)],
  'note':'&ldquo;Bacteria&rdquo; in (b) is the right organism at the wrong step — they come in later, feeding on the dead material.'},
 {'n':'10','marks':2,
  'lines':['Any two of: deforestation and habitat destruction; pollution (fertilisers, sewage, pesticides, plastics); '
           'overfishing or over-hunting; climate change from burning fossil fuels' + B(2)],
  'note':'Both marks need distinct activities. &ldquo;Pollution&rdquo; twice, in two forms, is acceptable only if the two forms are clearly different.'},
 {'n':'11','marks':2,
  'lines':['(a) breathing (ventilation) is the muscular movement of air in and out of the lungs; respiration is a '
           'chemical reaction that releases energy from glucose' + B(1),
           '(b) in <b>every living cell</b> of the body (in the mitochondria)' + B(1)],
  'note':'&ldquo;Respiration takes place in the lungs&rdquo; in (b) scores 0 and is the single most repeated error in the whole of Unit 2.'},

 {'n':'12','marks':3,
  'lines':['the diaphragm <b>relaxes</b> and moves up into its domed shape; the intercostal muscles relax so the ribs '
           'move down and in' + B(1),
           'the volume of the thorax decreases' + B(1),
           'so the pressure inside the lungs rises above atmospheric pressure and air flows out' + B(1)],
  'note':'&ldquo;The diaphragm pushes the air out&rdquo; scores 0 — it describes a relaxed muscle doing work it cannot do. At rest, exhalation is elastic recoil.'},
 {'n':'13','marks':3,
  'lines':['tar paralyses and destroys the cilia, so mucus is not swept out; it accumulates, causing coughing and '
           'repeated infection' + B(1),
           'alveolar walls break down and alveoli merge into fewer, larger sacs (emphysema), reducing the surface '
           'area for gas exchange' + B(1),
           'carbon monoxide binds to haemoglobin in place of oxygen, so the blood carries less oxygen' + B(1)],
  'note':'The third point is about transport, not gas exchange, and is the one that separates a 3 from a 2. Marks are for three <i>different</i> mechanisms, not three symptoms.'},
 {'n':'14','marks':3,
  'lines':['blood in a vein is at very low pressure and moves slowly, so it could flow backwards' + B(1),
           'valves close to prevent backflow, so blood travels only towards the heart (helped by skeletal muscles '
           'squeezing the veins)' + B(1),
           'blood in an artery is at high pressure straight from the ventricle, so backflow cannot occur and valves '
           'are unnecessary' + B(1)],
  'note':'Most answers cover the veins and stop. The question has two halves and the artery half is a full mark.'},
 {'n':'15','marks':3,
  'lines':['blood passes through the heart <b>twice</b> for each complete circuit of the body' + B(1),
           'the pulmonary circuit runs heart → lungs → heart; the systemic circuit runs heart → body → heart' + B(1),
           'advantage: blood is pumped again after the lungs, so it travels to the body at high pressure and '
           'delivers oxygen quickly, supporting a high rate of respiration and activity' + B(1)],
  'note':'A comparison with a fish’s single circulation is a legitimate route to the third mark and is worth praising.'},
 {'n':'16','marks':3,
  'lines':['wall one cell thick — a very short diffusion distance between blood and cells' + B(1),
           'very narrow lumen, roughly one red blood cell wide — slows the blood and brings it close to the wall' + B(1),
           'enormous number of them, forming a dense network with a huge total surface area — more area for exchange '
           'and no cell far from a capillary' + B(1)],
  'note':'Feature plus consequence on every line. Three bare features score 1.'},
 {'n':'17','marks':3,
  'lines':['pressure falls continuously from the aorta (about 16 kPa) to the vena cava (about 0.5 kPa)' + B(1),
           'most of the fall happens across the arterioles and capillaries' + B(1),
           'blood returns because skeletal muscles contract and squeeze the veins, and valves ensure the squeeze '
           'moves blood only towards the heart' + B(1)],
  'note':'&ldquo;The heart sucks it back&rdquo; scores 0. If a candidate writes it, the muscle-pump idea has not landed at all.'},
 {'n':'18','marks':3,
  'lines':['a pyramid of numbers counts organisms and ignores their size' + B(1),
           'so one very large producer, such as a single tree supporting hundreds of caterpillars, gives a narrow '
           'bottom bar and an inverted pyramid' + B(1),
           'a pyramid of biomass measures the total mass at each level, and the tree’s mass is far greater than all '
           'the caterpillars together, so it comes out the usual way up' + B(1)],
  'note':'A worked example (one oak, 500 caterpillars) is the clearest route to all three marks and should be encouraged over abstract phrasing.'},
 {'n':'19','marks':3,
  'lines':['decomposers (bacteria and fungi) feed on dead organisms, dead plant material and waste, breaking them down' + B(1),
           'this releases mineral ions such as nitrates back into the soil, where plants absorb them again' + B(1),
           'without them, dead material would accumulate and the mineral ions locked inside it would not be returned, '
           'so plant growth would eventually fail' + B(1)],
  'note':'&ldquo;Everything would smell&rdquo; is not the answer. The third mark is about nutrients becoming unavailable, not about tidiness.'},
 {'n':'20','marks':3,
  'lines':['a line (tape or rope) is laid across the area being studied' + B(1),
           'quadrats are placed at fixed, regular intervals along the line and the organisms in each are counted or '
           'their percentage cover recorded' + B(1),
           'a transect is used when studying how a population changes along a gradient — up a shore, out from a path, '
           'into shade — where random placement would hide the very pattern being investigated' + B(1)],
  'note':'The third mark is the one that matters. A candidate who describes the method but cannot say when it beats random sampling has learned a procedure, not a technique.'},
 {'n':'21','marks':3,
  'lines':['extra greenhouse gases trap more of the infrared radiated by the Earth, so the mean global temperature '
           'rises' + B(1),
           'ice sheets and glaciers melt, and seawater expands as it warms, so sea level rises' + B(1),
           'low-lying habitats are flooded and lost; species that cannot move or adapt fast enough die out' + B(1)],
  'note':'Thermal expansion is the half most candidates miss — they name melting ice only. Both contribute, and expansion is roughly comparable in size.'},
 {'n':'22','marks':3,
  'lines':['use less fertiliser, and do not apply it just before heavy rain' + B(1),
           'leave an unfertilised buffer strip of vegetation along the riverbank to catch run-off' + B(1),
           'treat sewage before discharging it, so it does not add nitrates and organic matter directly' + B(1)],
  'note':'&ldquo;Stop farming&rdquo; scores 0. The question asks for measures, which means things a farmer could actually do next season.'},

 {'n':'23','marks':5,
  'lines':['(a) rest: 15 × 500 = 7500 cm³ = <b>7.5 dm³ per minute</b>' + B(1) +
           '; exercise: 28 × 1750 = 49 000 cm³ = <b>49 dm³ per minute</b>' + B(1),
           '(b) 49 ÷ 7.5 = <b>6.5 times greater</b> (6.53)' + B(1),
           '(c) the muscles respire faster, so they need more oxygen and produce more carbon dioxide' + B(1) +
           '; receptors detect the rising carbon dioxide and the brain increases both the rate and the depth of '
           'breathing, so more air is exchanged each minute' + B(1)],
  'note':'In (c), &ldquo;because he needs more oxygen&rdquo; alone scores 1. The second mark is for the carbon dioxide '
         'being the signal — which is also the answer to why holding your breath becomes unbearable.'},
 {'n':'24','marks':5,
  'lines':['(a) 85% still works: 200 × 0.85 = <b>170 cm³ per dm³</b>' + B(1),
           '(b) 5.2 × 170 = <b>884 cm³ per minute</b>' + B(1) +
           '; non-smoker 5.2 × 200 = 1040, so <b>156 cm³ per minute less</b>' + B(1),
           '(c) the limit is <b>transport</b>, not gas exchange' + B(1) +
           '; oxygen diffuses into his blood normally, but 15% of his haemoglobin is permanently occupied, so every '
           'dm³ leaving his lungs is 15% short; walking uphill raises his muscles’ demand and he cannot meet it' + B(1)],
  'note':'200 − 15 = 185 in (a) is the error this question exists to catch — a percentage of a quantity is not a '
         'subtraction. Everything downstream then follows from a wrong number, so award follow-through in (b).'},
 {'n':'25','marks':5,
  'lines':['(a) total = 3+5+2+6+4+3+5+4 = 32, mean = 32 ÷ 8 = <b>4 per quadrat</b>' + B(1) +
           '; quadrat area = 0.25 × 0.25 = 0.0625 m², density = 4 ÷ 0.0625 = 64 per m², total = 64 × 250 = '
           '<b>16 000 plantains</b>' + B(1),
           '(b) take many more quadrats, and place them using random number coordinates rather than by eye' + B(1),
           '(c) predator numbers can only rise once prey is already plentiful, and breeding takes time, so the '
           'predator increase lags behind' + B(1) +
           '; the increased predation then reduces the prey, and the predators decline afterwards through lack of food' + B(1)],
  'note':'The quadrat area is the trap: 0.25 m on a side is 0.0625 m², not 0.25 m². Using 0.25 gives 4000, which is '
         'a quarter of the truth and looks entirely plausible. Award the mean mark and withhold the second.'},
 {'n':'26','marks':5,
  'lines':['(a) 480 000 × 5.5 = 2 640 000 tonnes' + B(1) + ' = <b>2.64 × 10⁶ tonnes per year</b>' + B(1),
           '(b) 12 000 × 5.5 = <b>66 000 tonnes per year</b> of absorption lost' + B(1),
           '(c) the carbon stored in the felled trees is also released as carbon dioxide when the timber is burned '
           'or decays' + B(1) +
           '; and the loss is cumulative — another 12 000 hectares goes every year, so the absorption lost grows '
           'year on year (accept: carbon is also released from the disturbed soil)' + B(1)],
  'note':'Part (c) separates the strong candidates. Most give one reason; the cumulative point and the released-carbon '
         'point are genuinely different and both are available.'},
 {'n':'27','marks':5,
  'lines':['(a) the definition is about <b>direction</b>, not oxygen: arteries carry blood away from the heart and '
           'veins carry it towards the heart' + B(1) +
           '; the pulmonary artery carries deoxygenated blood and the pulmonary vein carries oxygenated blood' + B(1),
           '(b) nothing in the chain is a poison — nitrate is a plant nutrient' + B(1) +
           '; it causes an algal bloom that blocks the light, the plants below die, decomposer bacteria multiply and '
           'use up the dissolved oxygen in aerobic respiration, and the fish suffocate' + B(1),
           '(c) energy is <b>not</b> recycled — it flows through and is lost as heat; it is <b>nutrients</b> that '
           'decomposers recycle' + B(1)],
  'note':'Marking someone else’s error is the same cognitive work as marking your own and far easier to face. If a '
         'candidate corrects all three here but made the same mistakes earlier in the paper, that is worth showing '
         'them side by side — it is usually the most useful two minutes of the whole review.'},
]

SCHEME = [
  {'title': 'Biology Mock 1 — mark scheme', 'meta': 'MtoH · 80 marks · tutor copy', 'questions': S1},
  {'title': 'Biology Mock 2 — mark scheme', 'meta': 'MtoH · 80 marks · tutor copy', 'questions': S2},
]

SCHEME_HEADER = {
 'eyebrow': EYEBROW,
 'title': 'Biology Mocks 1 and 2 — mark scheme',
 'meta': 'Tutor copy · 160 marks · not linked from the hub',
 'intro': 'Marks in brackets are awarded line by line: a line of correct method or a correct marking point scores '
          'even when what follows it is wrong. Follow through an earlier wrong answer wherever the later reasoning is '
          'sound — the calculation questions in Section 3 are written so that this matters. The note under each '
          'question names the specific mistake that question was built to catch; across two papers those notes are '
          'meant to be read as a set, because the same three or four errors account for most of the marks lost.',
 'footer': 'Biology Mocks 1 and 2 · mark scheme · tutor copy',
}


# ----------------------------------------------------------------- verification
def _verify():
    # --- Mock 1, Section 3
    assert 14 * 480 == 6720 and F(6720, 1000) == F(672, 100)          # 6.72 dm³
    assert 68 * 72 == 4896 and round(4896 / 1000, 2) == 4.90          # 4.896 → 4.90 dm³
    assert 3.0e8 * 2.4e-7 == 72.0
    assert abs(9.0e7 * 4.0e-7 - 36.0) < 1e-9
    assert (72 - 36) / 72 * 100 == 50.0
    assert 48000 * F(1, 10) == 4800
    assert 48000 * F(1, 1000) == 48 and F(48, 48000) * 100 == F(1, 10)   # 0.1%
    assert 48 - 11 == 37 and round(37 / 48 * 100, 1) == 77.1
    # oxygen minimum really is at 300 m in the printed table
    o2 = {0: 8.8, 100: 2.6, 300: 1.4, 600: 4.9, 1200: 8.1}
    assert min(o2, key=o2.get) == 300
    assert [d for d, v in o2.items() if v < 5] == [100, 300, 600]

    # --- Mock 2, Section 3
    assert 15 * 500 == 7500 and 28 * 1750 == 49000
    assert round(49 / 7.5, 1) == 6.5
    assert 200 * F(85, 100) == 170
    assert F(52, 10) * 170 == 884 and F(52, 10) * 200 == 1040 and 1040 - 884 == 156
    counts = [3, 5, 2, 6, 4, 3, 5, 4]
    assert sum(counts) == 32 and F(32, 8) == 4
    assert F(1, 4) * F(1, 4) == F(1, 16) and float(F(1, 16)) == 0.0625
    assert 4 / 0.0625 == 64 and 64 * 250 == 16000
    assert 480000 * F(55, 10) == 2640000
    assert 12000 * F(55, 10) == 66000

    # --- structure
    for name, qs, sc in (('Mock 1', M1, S1), ('Mock 2', M2, S2)):
        total = sum(q['marks'] for q in qs)
        assert total == 80, '%s totals %d marks, expected 80' % (name, total)
        for q in qs:
            if q.get('parts'):
                s = sum(p['marks'] for p in q['parts'])
                assert s == q['marks'], '%s: part marks %d != %d in %r' % (name, s, q['marks'], q['text'][:44])
        st = sum(q['marks'] for q in sc)
        assert st == 80, '%s mark scheme totals %d' % (name, st)
        assert len(sc) == len(qs), '%s: %d schemes for %d questions' % (name, len(sc), len(qs))
        for i, (q, s) in enumerate(zip(qs, sc), 1):
            assert s['n'] == str(i), '%s: scheme out of order at %s' % (name, s['n'])
            assert s['marks'] == q['marks'], '%s Q%d: scheme %d marks, paper %d' % (name, i, s['marks'], q['marks'])
            assert s.get('note'), '%s Q%d: mark scheme has no note' % (name, i)
        spread = {}
        for q in qs:
            spread[q['marks']] = spread.get(q['marks'], 0) + 1
        one_mark_parts = sum(1 for q in qs for p in q.get('parts', []) if p['marks'] == 1)
        print('%s: %d questions, %d marks, question spread %s, %d one-mark parts'
              % (name, len(qs), total, sorted(spread.items()), one_mark_parts))


if __name__ == '__main__':
    _verify()
    print(build_paper(spec('1', M1), os.path.join(OUT, 'biology-mock-1.pdf')))
    print(build_paper(spec('2', M2), os.path.join(OUT, 'biology-mock-2.pdf')))
    print(build_scheme(SCHEME, os.path.join(OUT, 'biology-mock-answers.pdf'), SCHEME_HEADER))
