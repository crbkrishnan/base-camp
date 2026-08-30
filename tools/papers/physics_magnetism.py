#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Physics · Grade 7 · Magnetism'
TOPIC = 'Magnetic Fields'

BASE = [
 'Answer <b>every</b> question in the space provided. Write in sentences — a list of single words scores badly on this topic.',
 'Every field line you draw must carry an <b>arrowhead</b>. A line without one does not score.',
 'Where a question asks for a number, that number must carry a <b>unit</b>.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + ['Reminder: outside a magnet the field lines run from <b>north to south</b>, '
                    'like poles repel and unlike poles attract.']
INSTR_HARD = BASE + ['No rules and no reminders are given on this paper.',
                     'Several questions describe experiments you may not have seen before — apply the ideas you already have.']

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'endnote': 'End of paper. Before you hand it in, go back over every diagram and check that each field line carries an arrowhead pointing from north to south.',
 'footer': 'Paper A · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — materials and poles',
   'text':'Name <b>two</b> magnetic materials, and <b>two</b> metals that are <b>not</b> magnetic.',
   'marks':2,'space':24},
  {'text':'Complete the table. Write <i>yes</i> or <i>no</i> in each empty box.','marks':3,
   'grid':[['Material','Attracted by a magnet?'],['iron',''],['copper',''],['nickel',''],
           ['aluminium',''],['cobalt',''],['brass','']],
   'grid_widths':[AVAIL*0.42, AVAIL*0.58]},
  {'text':'State what happens in each case.','marks':3,
   'parts':[{'label':'(a)','text':'The north poles of two magnets are brought together.','marks':1,'space':16},
            {'label':'(b)','text':'The south poles of two magnets are brought together.','marks':1,'space':16},
            {'label':'(c)','text':'The north pole of one magnet is brought near the south pole of another.','marks':1,'space':16}]},
  {'text':'Explain the difference between a <b>magnetic material</b> and a <b>magnet</b>.','marks':2,'space':26},

  {'section':'Section 2 — the magnetic field',
   'text':'A bar magnet lies on the page with its north pole on the left.','marks':4,
   'parts':[{'label':'(a)','text':'Draw the magnetic field pattern around it. Draw at least four lines.','marks':3,'space':62},
            {'label':'(b)','text':'State which pole your arrows point away from.','marks':1,'space':14}]},
  {'text':'State <b>three</b> rules that must be obeyed when drawing magnetic field lines.','marks':3,'space':36},
  {'text':'On a correct diagram the field lines are drawn closer together at the poles than at the sides. '
          'State what this tells you, and why the spacing is worth marks.','marks':2,'space':26},
  {'text':'Describe how you would use a <b>plotting compass</b> to plot one magnetic field line around a bar magnet.',
   'marks':3,'space':40},

  {'section':'Section 3 — induced magnetism and the Earth',
   'text':'Explain what is meant by <b>induced magnetism</b>.','marks':2,'space':26},
  {'text':'State one difference between <b>soft iron</b> and <b>steel</b>, and name one thing each is used to make.',
   'marks':2,'space':28},
  {'text':'Explain why the needle of a compass always comes to rest pointing north.','marks':2,'space':26},
  {'text':'State the test that proves an object is a magnet, and explain why attraction on its own is not enough.',
   'marks':2,'space':30},
 ]}

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · 40 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_MED,
 'endnote': 'End of paper. Before you hand it in, go back over every diagram and check that each field line carries an arrowhead pointing from north to south.',
 'footer': 'Paper B · Medium · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — testing materials',
   'text':'Meera tests six objects with a bar magnet: an <b>iron nail</b>, a length of <b>copper wire</b>, '
          'a <b>steel spoon</b>, an <b>aluminium can</b>, a <b>plastic comb</b> and a disc of pure <b>nickel</b>.','marks':4,
   'parts':[{'label':'(a)','text':'List the objects that are attracted to the magnet.','marks':2,'space':22},
            {'label':'(b)','text':'Meera says her results prove that all metals are magnetic. '
                                  'Explain why her results show the opposite, naming two of her objects.','marks':2,'space':30}]},
  {'text':'A brass key and a steel key look almost identical. Explain why only one of them is attracted to a magnet.',
   'marks':3,'space':34},

  {'section':'Section 2 — drawing and plotting the field',
   'text':'A bar magnet lies on the page with its north pole on the left.','marks':5,
   'parts':[{'label':'(a)','text':'Draw the magnetic field pattern around it, using at least four lines.','marks':3,'space':62},
            {'label':'(b)','text':'State two things, other than the shape of the curves, that a marker '
                                  'looks for in your diagram.','marks':2,'space':24}]},
  {'text':'Describe, step by step, how to plot a magnetic field line using a plotting compass. '
          'Your answer must say what you do with the compass and how the line ends up with an arrow on it.',
   'marks':3,'space':40},
  {'text':'Arjun draws a field diagram in which two lines cross just above the north pole. '
          'Explain why this cannot be correct, and state what he should have drawn instead.','marks':3,'space':34},

  {'section':'Section 3 — magnets at work',
   'text':'The north pole of a bar magnet is touched to a steel paper clip. The clip sticks, and a second '
          'clip then hangs from the first.','marks':4,
   'parts':[{'label':'(a)','text':'Explain why the first clip sticks to the magnet.','marks':2,'space':26},
            {'label':'(b)','text':'Explain why the second clip hangs from the first, even though the first clip '
                                  'is not a permanent magnet.','marks':2,'space':26}]},
  {'text':'The Earth behaves as though a huge bar magnet were buried along its axis.','marks':4,
   'parts':[{'label':'(a)','text':'State what kind of magnetic pole lies at the geographic North Pole, and justify your answer.',
             'marks':2,'space':26},
            {'label':'(b)','text':'Explain why a bar magnet hung freely on a thread always settles pointing roughly north to south.',
             'marks':2,'space':26}]},
  {'text':'An object is attracted to a magnet.','marks':4,
   'parts':[{'label':'(a)','text':'Explain why this does not prove the object is a magnet.','marks':2,'space':26},
            {'label':'(b)','text':'Describe the test that would prove it, and state what you would observe.','marks':2,'space':26}]},
 ]}

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'endnote': 'End of paper. Before you hand it in, go back over every diagram and check that each field line carries an arrowhead pointing from north to south.',
 'footer': 'Paper C · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — reading the evidence',
   'text':'A steel bar hangs from a thread so that it can swing freely. When the <b>north</b> pole of a magnet is '
          'brought up to end X of the bar, the bar swings towards the magnet. When the <b>south</b> pole is brought '
          'up to the same end X, the bar swings towards the magnet again.','marks':5,
   'parts':[{'label':'(a)','text':'State what these two observations show about the steel bar.','marks':1,'space':18},
            {'label':'(b)','text':'Explain the observations in terms of induced magnetism.','marks':2,'space':30},
            {'label':'(c)','text':'Describe how the observations would have been different if the bar had been a magnet.',
             'marks':2,'space':28}]},
  {'text':'Three bars look identical. One is a magnet, one is unmagnetised steel and one is brass. '
          'Describe how you would identify all three, using nothing but the three bars themselves. '
          'State clearly what you would observe in each case.','marks':4,'space':52},

  {'section':'Section 2 — fields, neutral points and compasses',
   'text':'Two identical bar magnets lie in a line on a bench with their <b>north poles facing each other</b>, '
          '6 cm apart.','marks':5,
   'parts':[{'label':'(a)','text':'State and explain what happens when they are released.','marks':2,'space':26},
            {'label':'(b)','text':'A plotting compass placed at one particular point between them will not settle '
                                  'in any direction. State where that point is and explain why.','marks':2,'space':30},
            {'label':'(c)','text':'The magnets are pushed until the gap is 2 cm. Assuming the force follows an '
                                  'inverse-square law, state the factor by which the force increases.','marks':1,'space':20}]},
  {'text':'A bar magnet lies on a bench with its north pole on the left and its south pole on the right. '
          'A plotting compass is placed at three points in turn. State the direction the compass needle&rsquo;s '
          '<b>north end</b> points in each case.','marks':4,
   'parts':[{'label':'(a)','text':'On the axis, just beyond the north pole.','marks':1,'space':16},
            {'label':'(b)','text':'On the axis, just beyond the south pole.','marks':1,'space':16},
            {'label':'(c)','text':'Directly above the middle of the magnet.','marks':1,'space':16},
            {'label':'(d)','text':'Explain how you worked out your answer to (c).','marks':1,'space':22}]},

  {'section':'Section 3 — applying the ideas',
   'text':'A crane at a scrapyard lifts material out of a mixed heap using a very strong magnet. '
          'The heap contains steel cans, aluminium cans, copper wire and iron girders.','marks':4,
   'parts':[{'label':'(a)','text':'State which items the magnet lifts and which it leaves behind, with a reason.',
             'marks':2,'space':28},
            {'label':'(b)','text':'The operator wants to separate the copper wire from the aluminium cans. '
                                  'Explain why a second pass with the magnet cannot do it.','marks':2,'space':26}]},
  {'text':'A magnet holds a hanging chain of three steel paper clips.','marks':4,
   'parts':[{'label':'(a)','text':'Explain why each clip in the chain is a weaker magnet than the one above it.',
             'marks':2,'space':28},
            {'label':'(b)','text':'A thin sheet of copper is slid between the magnet and the first clip. '
                                  'Predict what happens to the chain, and explain your prediction.','marks':2,'space':30}]},
  {'text':'The Earth&rsquo;s magnetic field is usually drawn as though a huge bar magnet were buried along its axis.','marks':4,
   'parts':[{'label':'(a)','text':'State which end of that buried magnet lies at the geographic North Pole, and justify it.',
             'marks':2,'space':26},
            {'label':'(b)','text':'Give one way in which the buried-bar-magnet picture is useful, and one way in which '
                                  'it is not literally true.','marks':2,'space':30}]},
 ]}

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · 50 minutes · 30 marks', 'marks': 30, 'instructions': INSTR_HARD,
 'endnote': 'End of paper. Before you hand it in, go back over every diagram and check that each field line carries an arrowhead pointing from north to south.',
 'footer': 'Paper D · Hard · ' + TOPIC,
 'questions': [
  {'section':'Section 1 — arrangements and evidence',
   'text':'Two bar magnets lie in a line on a bench.','marks':5,
   'parts':[{'label':'(a)','text':'Describe how they must be arranged so that a neutral point exists between them.',
             'marks':2,'space':26},
            {'label':'(b)','text':'State what a neutral point is.','marks':1,'space':20},
            {'label':'(c)','text':'One of the magnets is replaced by a weaker one, still arranged the same way. '
                                  'State how the position of the neutral point changes, and explain why.','marks':2,'space':30}]},
  {'text':'Kabir has two steel bars that look identical. One is a magnet; the other is not. He has nothing else — '
          'no compass, no iron filings, no second magnet.','marks':5,
   'parts':[{'label':'(a)','text':'Describe a test using only the two bars that tells him which one is the magnet, '
                                  'and state what he would observe in each case.','marks':3,'space':40},
            {'label':'(b)','text':'Explain why the test works.','marks':2,'space':30}]},

  {'section':'Section 2 — diagrams and materials',
   'text':'A student hands in a field diagram for a bar magnet with four faults: the lines <b>stop in mid-air</b>; '
          'they are <b>evenly spaced everywhere</b>; the arrows point <b>into</b> the north pole; and two of the '
          'lines <b>touch</b> near a pole. For each fault, state what is wrong and what should have been drawn.',
   'marks':4,'space':56},
  {'text':'Compass needles are made from steel. The cores of electromagnets are made from soft iron.','marks':4,
   'parts':[{'label':'(a)','text':'Explain why each material is the right choice for its job.','marks':2,'space':28},
            {'label':'(b)','text':'Bar magnets left loose in a drawer gradually get weaker. State one way magnets '
                                  'should be stored, and explain how it helps.','marks':2,'space':28}]},

  {'section':'Section 3 — judgement',
   'text':'A hiker uses a compass.','marks':4,
   'parts':[{'label':'(a)','text':'Explain why saying &ldquo;the compass points to the North Pole&rdquo; is loosely '
                                  'worded. Use the words <i>geographic</i> and <i>magnetic</i> in your answer.',
             'marks':2,'space':30},
            {'label':'(b)','text':'Standing next to a large steel gate, she finds the compass gives a different '
                                  'reading. Explain why.','marks':2,'space':30}]},
  {'text':'A bar magnet is dipped into a tray of iron filings and lifted out.','marks':4,
   'parts':[{'label':'(a)','text':'Describe where the filings collect and explain why.','marks':2,'space':26},
            {'label':'(b)','text':'The magnet is then snapped in half. State what you now have, and explain.',
             'marks':2,'space':28}]},
  {'text':'Another student has written two answers, and both are wrong.<br/>'
          '<b>(i)</b> &ldquo;The paper clip stuck to the magnet, so the paper clip must be a magnet as well.&rdquo;<br/>'
          '<b>(ii)</b> &ldquo;I drew the field lines running from the south pole to the north pole outside the magnet, '
          'and I made them all the same distance apart.&rdquo;<br/>'
          'For each one, explain the mistake and give the correct version.','marks':4,'space':56},
 ]}

SCHEMES = [
 {'title':'Paper A — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':2,'lines':['Two from: iron, nickel, cobalt, steel <b>[1]</b>',
    'Two from: copper, aluminium, brass, gold, silver, zinc, lead, tin <b>[1]</b>'],
   'note':'The second half must be <i>metals</i>. Answering plastic and wood misses the entire point of the question and scores zero for that mark.'},
  {'n':'2','marks':3,'lines':['iron <b>yes</b> · copper <b>no</b> · nickel <b>yes</b> · aluminium <b>no</b> · cobalt <b>yes</b> · brass <b>no</b>',
    'All six correct <b>[3]</b>; four or five correct <b>[2]</b>; two or three correct <b>[1]</b>'],
   'note':'Brass is the one that separates them. It is copper and zinc, so it is not magnetic — students who guess from the word "metal" get it wrong, and students who know the three magnetic elements get it right.'},
  {'n':'3','marks':3,'lines':['(a) They <b>repel</b> (push apart) <b>[1]</b>','(b) They <b>repel</b> <b>[1]</b>',
    '(c) They <b>attract</b> <b>[1]</b>'],
   'note':'(b) catches anyone who has memorised "north repels north" as a fact about north rather than about like poles.'},
  {'n':'4','marks':2,'lines':['A magnetic material is one that a magnet attracts, such as iron, nickel, cobalt or steel <b>[1]</b>',
    'A magnet is a magnetic material that has been magnetised, so it has its own poles and produces its own field <b>[1]</b>'],
   'note':'Every magnet is made of a magnetic material; almost no magnetic material is a magnet. Accept any wording that keeps those two apart.'},
  {'n':'5','marks':4,'lines':['(a) At least four smooth lines running from one pole round to the other <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Arrowheads on every line, pointing north to south outside the magnet <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Lines closer together at the poles than at the sides, and never crossing <b>[1]</b>',
    '(b) Away from the <b>north</b> pole <b>[1]</b>'],
   'note':'Award the shape mark generously and the arrow mark strictly. A beautiful pattern with no arrows scores 1 out of 3 here, which is exactly the lesson.'},
  {'n':'6','marks':3,'lines':['Arrows on every line, running from north to south outside the magnet <b>[1]</b>',
    'Lines never cross <b>[1]</b>',
    'Lines are closer together where the field is stronger (at the poles) <b>[1]</b>',
    'Also accept: lines form complete loops / lines leave and enter the <b>pole faces</b> at right angles (true at the ends of the bar, not along its sides)'],
   'note':'"Draw them neatly" and "use a pencil" are not rules and score nothing. Three physics statements are wanted.'},
  {'n':'7','marks':2,'lines':['Closer lines mean a <b>stronger field</b>, so the field is strongest at the poles <b>[1]</b>',
    'The spacing is the only part of the diagram that carries the strength information, so even spacing states something untrue <b>[1]</b>']},
  {'n':'8','marks':3,'lines':['Place the compass near one pole and mark a dot at each end of the needle <b>[1]</b>',
    'Move the compass so its tail sits on the previous head dot, mark the new head, and repeat to the other pole <b>[1]</b>',
    'Join the dots into a smooth curve and add an arrow in the direction the compass north end pointed <b>[1]</b>'],
   'note':'The arrow is part of the method. A described procedure that ends with a bare curve has recorded the shape and thrown away the direction — cap at 2.'},
  {'n':'9','marks':2,'lines':['Magnetism produced in a magnetic material by placing it in a magnetic field <b>[1]</b>',
    'It is temporary: the near end becomes the opposite pole so the object is attracted, and the magnetism is lost when the field is taken away <b>[1]</b>']},
  {'n':'10','marks':2,'lines':['Soft iron magnetises easily but loses it at once; steel is harder to magnetise but keeps it <b>[1]</b>',
    'Soft iron: electromagnet cores (temporary magnets). Steel: bar magnets and compass needles (permanent magnets) <b>[1]</b>'],
   'note':'The pairing gets reversed under pressure. Soft iron with temporary, steel with permanent — reversing it loses both marks, not one.'},
  {'n':'11','marks':2,'lines':['The Earth has a magnetic field, and the needle is a small magnet free to turn <b>[1]</b>',
    'The needle&rsquo;s north-seeking pole is attracted towards the magnetic pole in the far north (which is a magnetic <b>south</b> pole), so it lines up along the field <b>[1]</b>']},
  {'n':'12','marks':2,'lines':['The test is <b>repulsion</b>: only a magnet can be repelled by a magnet <b>[1]</b>',
    'Attraction is not enough because an unmagnetised magnetic material is attracted to either pole by induced magnetism <b>[1]</b>'],
   'note':'This appears in some form on all four papers because it is the single most reliable source of dropped marks in the topic.'},
 ]},

 {'title':'Paper B — Medium','meta':'30 marks','questions':[
  {'n':'1','marks':4,'lines':['(a) Iron nail, steel spoon and nickel disc <b>[1]</b> and no others <b>[1]</b>',
    '(b) Copper wire and the aluminium can are both metals and were <b>not</b> attracted <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;so being a metal does not make something magnetic; only iron, nickel, cobalt and their alloys are <b>[1]</b>'],
   'note':'The nickel disc is the one that gets left off (a). Pure nickel is magnetic — it is the third element, and it is forgotten more often than cobalt.'},
  {'n':'2','marks':3,'lines':['Steel is mostly iron, and iron is magnetic <b>[1]</b>',
    'Brass is an alloy of copper and zinc <b>[1]</b>',
    'Neither copper nor zinc is magnetic, so the brass key is not attracted <b>[1]</b>'],
   'note':'Award the third mark only if the answer names why brass fails, rather than simply asserting that it does.'},
  {'n':'3','marks':5,'lines':['(a) Four or more smooth lines from pole to pole <b>[1]</b>; arrowheads on every line running north to south <b>[1]</b>; closer spacing at the poles, no crossings <b>[1]</b>',
    '(b) Two from: arrowheads present and pointing the right way; lines not crossing; spacing tighter at the poles; lines starting and ending on the magnet <b>[1] [1]</b>']},
  {'n':'4','marks':3,'lines':['Compass placed near a pole, dots marked at each end of the needle <b>[1]</b>',
    'Compass moved so the tail sits on the last head dot, repeated across to the other pole <b>[1]</b>',
    'Dots joined into a smooth curve with an arrow added in the direction the compass north end pointed <b>[1]</b>']},
  {'n':'5','marks':3,'lines':['A crossing point would mean the field there pointed in two directions at once <b>[1]</b>',
    'which is impossible, since a compass placed there settles in one direction only <b>[1]</b>',
    'The two lines should run side by side without meeting <b>[1]</b>'],
   'note':'Answers that only say "field lines never cross" have restated the rule, not explained it. That is worth one.'},
  {'n':'6','marks':4,'lines':['(a) The magnet&rsquo;s field <b>induces magnetism</b> in the steel clip <b>[1]</b>; the near end becomes a south pole, and unlike poles attract <b>[1]</b>',
    '(b) The first clip is now itself a (temporary) magnet <b>[1]</b>, so it induces magnetism in the second clip in the same way <b>[1]</b>'],
   'note':'Watch for "the magnetism travels down the chain". Nothing travels — each clip is magnetised in turn by the field of the one above it.'},
  {'n':'7','marks':4,'lines':['(a) A magnetic <b>south</b> pole <b>[1]</b>, because the needle&rsquo;s north-seeking pole is attracted to it and unlike poles attract <b>[1]</b>',
    '(b) The Earth&rsquo;s field exerts forces on both poles of the magnet, turning it <b>[1]</b> until its north-seeking pole lines up along the field, pointing north; there is then no turning effect left <b>[1]</b>'],
   'note':'"Because the Earth is a magnet" alone scores one in (a). The justification mark needs the words <i>unlike poles attract</i>.'},
  {'n':'8','marks':4,'lines':['(a) An unmagnetised magnetic material becomes a temporary magnet by induction <b>[1]</b>, and is attracted to either pole, so attraction only proves it is magnetic material <b>[1]</b>',
    '(b) Bring the object near one pole of a known magnet, then the other <b>[1]</b>; if it is <b>repelled</b> by either, it is a magnet <b>[1]</b>']},
 ]},
]

SCHEMES += [
 {'title':'Paper C — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) The bar is <b>not a magnet</b> — it is unmagnetised magnetic material <b>[1]</b>',
    '(b) The magnet&rsquo;s field <b>induces magnetism</b> in the steel <b>[1]</b>; whichever pole is offered, the near end of the bar becomes the opposite pole, so it is attracted either way <b>[1]</b>',
    '(c) If the bar were a magnet it would have been <b>attracted by one pole and repelled by the other</b> <b>[1]</b>; the absence of any repulsion is what rules that out <b>[1]</b>'],
   'note':'Two attractions look like two pieces of evidence and are worth one between them. The candidate has to notice that the informative observation — a repulsion — never happened.'},
  {'n':'2','marks':4,'lines':['Try all three pairs of ends and look for attraction <b>[1]</b>',
    'The bar attracted by nothing at all is the <b>brass</b> <b>[1]</b>',
    'Of the remaining two, touch the end of one to the <b>middle</b> of the other <b>[1]</b>',
    'Strong attraction there means the bar being held is the <b>magnet</b>, because the middle of a magnet has almost no field of its own <b>[1]</b>'],
   'note':'Repulsion is unavailable here — only one bar is magnetised, so nothing ever repels. Candidates who insist on the repulsion test and stop have applied a correct rule to the wrong situation; award the first two marks.'},
  {'n':'3','marks':5,'lines':['(a) They <b>push apart</b> <b>[1]</b>; two north poles are like poles and like poles repel <b>[1]</b>',
    '(b) At the <b>neutral point</b>, midway between them, 3 cm from each <b>[1]</b>; the two fields there are equal in size and opposite in direction, so they cancel and the resultant field is zero <b>[1]</b>',
    '(c) 6 &divide; 2 = 3, and 3&#178; = <b>9 times</b> stronger <b>[1]</b>'],
   'note':'In (c) the common wrong answer is 3, from forgetting to square. The midpoint answer in (b) is only correct because the magnets are identical — say so if the candidate does.'},
  {'n':'4','marks':4,'lines':['(a) <b>Away from the magnet</b> (to the left) <b>[1]</b>',
    '(b) <b>Towards the magnet</b> (also to the left) <b>[1]</b>',
    '(c) <b>Horizontally, to the right</b> — from the north pole towards the south pole <b>[1]</b>',
    '(d) Above the magnet the field lines run across from the north pole to the south pole, and the compass north end lies along the field <b>[1]</b>'],
   'note':'(a) and (b) both point left, which is why they are set together. Beyond the north pole the field leaves the magnet; beyond the south pole it returns to it. Candidates who answer "left" and "right" have reasoned from the picture rather than the field.'},
  {'n':'5','marks':4,'lines':['(a) Lifts the <b>steel cans and iron girders</b>; leaves the aluminium cans and copper wire <b>[1]</b>; because only iron and its alloys are magnetic <b>[1]</b>',
    '(b) Copper and aluminium are <b>both</b> non-magnetic <b>[1]</b>, so the magnet ignores both equally and cannot tell them apart <b>[1]</b>'],
   'note':'This is the "all metals are magnetic" trap dressed as an application question. Answers that lift the aluminium cans lose both marks in (a).'},
  {'n':'6','marks':4,'lines':['(a) The field inducing each clip is weaker the further it is from the magnet <b>[1]</b>, so the magnetism induced in each clip is weaker than in the one above it <b>[1]</b>',
    '(b) The chain <b>stays up</b> <b>[1]</b>; copper is not magnetic and does not block a magnetic field, which passes straight through non-magnetic materials <b>[1]</b>'],
   'note':'(b) is the discriminating question on this paper. Most candidates predict the chain falls, reasoning that the copper is in the way. Award the first mark only for a correct prediction with no explanation.'},
  {'n':'7','marks':4,'lines':['(a) The buried magnet&rsquo;s <b>south</b> end is at the geographic North Pole <b>[1]</b>; a compass needle&rsquo;s north-seeking pole is attracted to it and unlike poles attract <b>[1]</b>',
    '(b) Useful: it predicts the shape of the field and which way a compass points anywhere on the surface <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Not literally true: the core is far too hot to stay permanently magnetised — the field is produced by moving molten iron, and it drifts over time <b>[1]</b>'],
   'note':'Accept any sensible limitation in (b), including that the magnetic poles move and do not sit exactly at the geographic poles.'},
 ]},

 {'title':'Paper D — Hard','meta':'30 marks','questions':[
  {'n':'1','marks':5,'lines':['(a) In a line, with <b>like poles facing each other</b> across the gap — north facing north, or south facing south <b>[1] [1]</b>',
    '(b) A point where the fields of the two magnets are equal and opposite, so they cancel and the resultant field is zero <b>[1]</b>',
    '(c) It moves <b>towards the weaker magnet</b> <b>[1]</b>; you have to get closer to the weaker one before its field has grown enough to match the stronger one&rsquo;s <b>[1]</b>'],
   'note':'(c) separates the candidates who have memorised "halfway" from the ones who understand what is cancelling. Halfway is only right for identical magnets.'},
  {'n':'2','marks':5,'lines':['(a) Touch the <b>end</b> of one bar to the <b>middle</b> of the other <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Strong attraction: the bar being held is the magnet <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Little or no attraction: the other bar is the magnet, and repeating the test the other way round confirms it <b>[1]</b>',
    '(b) The middle of a magnet has almost no field, because the poles are at the ends <b>[1]</b>; an unmagnetised bar has no poles anywhere, so its middle behaves the same as its ends <b>[1]</b>'],
   'note':'With only two bars and one magnet, nothing ever repels — the repulsion test is unavailable and candidates must find another route. Reward any test that uses the weak middle of a magnet.'},
  {'n':'3','marks':4,'lines':['Lines stopping in mid-air: every line must run from the magnet&rsquo;s surface back to it, forming a closed loop <b>[1]</b>',
    'Even spacing: spacing shows strength, so the lines must be closer together at the poles <b>[1]</b>',
    'Arrows into the north pole: outside the magnet the arrows run <b>north to south</b>, so they should point out of the north pole <b>[1]</b>',
    'Lines touching: field lines never cross or touch, since the field has one direction at each point <b>[1]</b>']},
  {'n':'4','marks':4,'lines':['(a) Steel keeps its magnetism, so a compass needle stays magnetised permanently <b>[1]</b>; soft iron magnetises and demagnetises easily, so an electromagnet can be switched off <b>[1]</b>',
    '(b) Store them in pairs with unlike poles together, and soft iron <b>keepers</b> across the ends <b>[1]</b>; this gives the field a closed path through magnetic material, so the magnet does not gradually demagnetise itself <b>[1]</b>'],
   'note':'Storage is often not taught and often examined. Accept "keep them away from heat, hammering and dropping" for one mark in (b) with a correct reason.'},
  {'n':'5','marks':4,'lines':['(a) The compass points to <b>magnetic</b> north, not <b>geographic</b> north <b>[1]</b>; the magnetic pole is not in the same place as the geographic pole, so the two directions differ by an angle <b>[1]</b>',
    '(b) The steel gate is magnetised by induction in the Earth&rsquo;s field <b>[1]</b>; the Earth&rsquo;s field is very weak, so close to the gate the gate&rsquo;s own field is stronger and the needle lines up with that instead <b>[1]</b>'],
   'note':'(b) rewards anyone who has grasped how weak the Earth&rsquo;s field actually is. It is also why a plotting-compass practical says to clear iron off the bench.'},
  {'n':'6','marks':4,'lines':['(a) The filings collect at the two <b>ends</b> — the poles <b>[1]</b>; that is where the field is strongest <b>[1]</b>',
    '(b) Two shorter magnets, each with its own north and south pole <b>[1]</b>; a single isolated pole cannot be produced, however many times you break it <b>[1]</b>'],
   'note':'"One half is north and the other half is south" is the wrong answer here and is chosen often. It scores nothing.'},
  {'n':'7','marks':4,'lines':[
    '(i) The mistake: attraction only shows the clip is <b>magnetic material</b>, not a magnet <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: the steel clip is temporarily magnetised by <b>induction</b>; only <b>repulsion</b> would prove it was a magnet <b>[1]</b>',
    '(ii) The mistake: outside the magnet the lines run <b>north to south</b>, not south to north <b>[1]</b>',
    '&nbsp; &nbsp; &nbsp;Correct version: reverse every arrow, and draw the lines <b>closer together at the poles</b> rather than evenly spaced <b>[1]</b>'],
   'note':'Both statements are the two most common errors in the topic, written out as another student&rsquo;s work. Diagnosing them is the same cognitive job as avoiding them, and much easier to face.'},
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
    p = os.path.join(OUT, 'physics-magnetism-paper-%s.pdf' % code)
    build_paper(spec, p); files.append(p)
for sc in SCHEMES:
    t = sum(q['marks'] for q in sc['questions'])
    assert t == 30, (sc['title'], t)
assert len(SCHEMES) == 4
for spec, sc in zip([A,B,C,D], SCHEMES):
    assert len(spec['questions']) == len(sc['questions']), (spec['title'], len(spec['questions']), len(sc['questions']))
    for q, s in zip(spec['questions'], sc['questions']):
        assert q['marks'] == s['marks'], (spec['title'], s['n'], q['marks'], s['marks'])
p = os.path.join(OUT, 'physics-magnetism-answers.pdf')
build_scheme(SCHEMES, p, {
    'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
    'meta': 'Papers A to D · 30 marks each · tutor copy',
    'intro': 'Marks in square brackets show how the total is split. This topic is marked on wording, not on '
             'arithmetic, so award marks for the specific statement rather than for the general idea. Almost every '
             'mark lost goes one of four ways: assuming every metal is magnetic; field lines drawn without '
             'arrowheads or with the arrows reversed; treating attraction as proof that something is a magnet; and '
             'confusing the geographic North Pole with a magnetic north pole. The notes under each answer flag the '
             'specific mistake that question was built to catch.',
    'footer': 'Mark schemes · ' + TOPIC})
files.append(p)
print('\n'.join(files))
