#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Four reading-comprehension papers plus the tutor's mark-scheme booklet.

25 marks, 35 minutes, nine questions — the shape of the school's English Paper 2,
not the house 30. See docs/READING-COMPREHENSION.md; CLAUDE.md #5 is unchanged and
this is a recorded exception, like the 80-mark maths mock.

Passages are PRE-WRAPPED: one list entry per printed line, because the line numbers
are what the questions cite. `_verify()` re-checks, on every build, that every line
fits the frame, that every range a question names exists, and that the words the
mark scheme expects are actually inside the range it names.
"""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from paper_lib import build_paper, build_scheme, AVAIL
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE English · Grade 7 · Reading comprehension'
TOPIC = 'Between the Lines'

BASE = [
 'Answer <b>every</b> question in the space provided.',
 'Read <b>both</b> texts once, properly, before you answer anything. The last two questions need both.',
 'Answer only from the lines the question names. A perfect answer from the wrong lines scores nothing.',
 'When a question asks for <b>two things</b>, give two separate ideas. One idea written twice is one mark.',
 'Pay attention to punctuation and spelling. The number of marks is shown in brackets [ ] on the right.',
]
INSTR_MED = BASE + [
 'The ladder: <b>Says</b> (what happened) &rarr; <b>Shows</b> (what the writer chose to put there) &rarr; '
 '<b>So what</b> (what that implies). A question asking what something <i>tells</i> or <i>suggests</i> '
 'wants the third rung, proved with the second.',
 'For any explanation mark: <b>quote short, zoom to one word inside your quotation, then say what it '
 'suggests.</b> An inference with no word behind it scores the same as a blank.',
]
INSTR_HARD = BASE + [
 'One of the two texts on this paper is not a story. You have not been taught that text type &mdash; apply '
 'the ideas you already have.',
 'No framework is printed on this paper. Remembering the three rungs is part of what it is testing.',
]

ENDNOTE = ('End of paper. Before you hand it in, check every explanation names a word from inside your '
           'own quotation. That is the mark most often left behind on a paper like this.')


# ================================================================ passages

A_TEXT = {
 'intro': 'Meera is twelve. Her father delivers tiffin boxes across four streets every morning; today he '
          'has a fever, and she has taken the cycle out alone for the first time.',
 'start': 3,
 'lines': [
  "The cycle is too big for her and always has been. Meera stands on the pedals rather",
  "than sitting, and the crate of tins behind her complains at every pothole on Sampige",
  "Road. Eleven tins. She counted them at the gate, and then, at the corner, she counted",
  "them again.",
  "",
  "Her father does this round in fifty minutes. He has done it for nineteen years and he",
  "does not carry the list, because the list is in his head: Sharma, second floor, no",
  "chilli. Fernandes, ground floor, ring twice. The Iyer boys, who will not come down",
  "unless you shout.",
  "",
  "Meera carries the list. She has it folded in her pocket and she has already taken it",
  "out four times, and the folds are going soft.",
  "",
  "The first three are easy. The fourth is a flat on the third floor with a lift that is",
  "switched off until nine, and by the time she reaches the landing her arms are shaking",
  "and the tin is warm against her shirt. A woman opens the door before she knocks.",
  "",
  "&lsquo;You are Raju&rsquo;s daughter,&rsquo; the woman says. It is not a question. &lsquo;He is ill?&rsquo;",
  "",
  "Meera nods. She has not said a word to anyone all morning and is surprised to find",
  "that her voice, when she tries it, is still there.",
  "",
  "&lsquo;Two minutes,&rsquo; the woman says. She comes back with a steel tumbler of water, and",
  "stands in the doorway while Meera drinks it, not talking, not going back inside.",
  "&lsquo;Tell him Mrs Kamath asked after him.&rsquo;",
  "",
  "On Kanakapura Lane a tin slips as she lifts the crate and lands on its side. Nothing",
  "spills &mdash; her father&rsquo;s tins are packed the way he packs everything, as though someone",
  "will drop them &mdash; but the lid dents. Meera looks at it for a while. Then she turns it",
  "so the dent faces in, and carries it up.",
  "",
  "She finishes in an hour and twenty. Her father is asleep when she gets back. She puts",
  "the empty crate exactly where he leaves it, wheel against the wall, and washes the",
  "tins, and puts the list back in the drawer with the folds flattened out.",
 ]}

A_TEXT_B = {
 'intro': 'That night, Meera writes in the back of her maths notebook.',
 'start': 30,
 'lines': [
  "Did the round. Did NOT die.",
  "",
  "1 hour 20. Appa does it in 50. I know because he says it roughly four times a week,",
  "usually while eating.",
  "",
  "Counted the tins about nine times. Nobody told me to. I just kept thinking, what if",
  "it&rsquo;s ten, what if I&rsquo;ve left one at the gate and someone&rsquo;s kid gets no lunch.",
  "",
  "Mrs Kamath (402) gave me water and just stood there watching me drink it, which was",
  "weird, and then also nice? Both. She said tell him I asked.",
  "",
  "Dented one lid. Turned it round so the dent faced the wall. I&rsquo;m not writing that",
  "anywhere he can see it, and I am aware that this is a notebook.",
  "",
  "The thing nobody tells you is the lift is off till nine. He knows that. He knows all",
  "of it, he just doesn&rsquo;t say any of it out loud, it&rsquo;s all in his head and I had a piece",
  "of paper.",
  "",
  "Doing it again tomorrow if he&rsquo;s still ill. Not saying that to him though.",
 ]}

B_TEXT = {
 'intro': 'Vikram is thirteen. For three weeks a stray dog has been sitting behind the stumps at evening '
          'practice on the maidan, and the team has started to argue about it.',
 'start': 3,
 'lines': [
  "The dog arrives at ten past five, which is four minutes after Vikram does, and sits",
  "down behind the stumps as though somebody has paid it to be there. It is brown, with",
  "one ear that will not stand up, and it watches the ball and not the boys. When a shot",
  "goes past it, the ear lifts. It never once chases.",
  "",
  "&lsquo;It&rsquo;s going to get hit,&rsquo; says Adil, who is captain this month and enjoys it.",
  "",
  "&lsquo;It&rsquo;s been three weeks and it hasn&rsquo;t been hit,&rsquo; says Vikram.",
  "",
  "&lsquo;That&rsquo;s not an argument.&rsquo;",
  "",
  "&lsquo;It&rsquo;s the same argument you used about the tree.&rsquo;",
  "",
  "Adil throws the ball from hand to hand and does not answer, which is what he does",
  "instead of agreeing.",
  "",
  "The truth, which Vikram does not say, is that he has been bringing half a chapati in",
  "his kit bag since the second week, and that the dog knows the sound of the zip. He",
  "has worked out the exact place to leave it &mdash; behind the roller, where nobody walks",
  "&mdash; and the exact moment, which is while the others are arguing about the light.",
  "",
  "On Thursday the dog is not there.",
  "",
  "Practice goes on. Vikram takes two wickets and does not enjoy either of them. At six",
  "the boys start packing up and he finds himself walking the long way round the maidan,",
  "past the roller, past the gap in the fence, looking at the ground rather than at",
  "anything in particular.",
  "",
  "It is behind the water tank, lying on its side, breathing in a way he does not like.",
  "There is a cut across one back leg, straight and clean, the kind a sheet of roofing",
  "metal makes.",
  "",
  "He does not know what to do, so he does the only thing he can think of, which is to",
  "sit down on the concrete beside it and stay there. After some time the ear lifts.",
  "",
  "He is still there at seven, when the lights on the far side go on, and he has missed",
  "dinner, and he has not once thought about the two wickets.",
 ]}

B_TEXT_B = {
 'intro': "A week later a letter arrives from Vikram's grandmother in Thrissur. She writes by hand, in "
          "English, once a month.",
 'start': 30,
 'lines': [
  "My dear Vikku,",
  "",
  "So you have a dog. I notice you did not say the word &lsquo;dog&rsquo; anywhere in your letter. You",
  "said &lsquo;it&rsquo; fourteen times. I counted, because I am old and I have time.",
  "",
  "You ask me whether you should tell your mother. You did not ask me whether you should",
  "keep feeding it, which tells me you have already decided that part.",
  "",
  "Now listen. I am not going to say what you want me to say. A dog that is fed by one",
  "boy at one time in one place is not a free animal any more; it will wait for you on",
  "the day you have exams, and on the day you go to Mysuru, and it will not understand.",
  "Kindness that comes and goes is a hard thing to be on the end of.",
  "",
  "Either it is your dog or it is the maidan&rsquo;s dog. Half is worse than neither.",
  "",
  "Your grandfather said the same thing to me about a cat in 1971 and I did not speak to",
  "him for two days, and then I got the cat properly, and he fed it for eleven years",
  "without once saying anything about it.",
  "",
  "Come in December. Bring the dog if by then it is yours. &mdash; Ammamma",
 ]}

C_TEXT = {
 'intro': 'Ananya is thirteen. Her mother entered her for the district swimming trial in February; it is '
          'now April, and Ananya is standing behind block four.',
 'start': 3,
 'lines': [
  "Behind block four the tiles are cold and slightly wet and Ananya has been standing on",
  "the same two of them for six minutes. She has not looked at the water. She has looked",
  "at the clock, at the roof, at the line of parents along the glass, and at her own",
  "feet, which is where she is looking now.",
  "",
  "Her mother filled in the form in February. Ananya found out in February too, from her",
  "mother, who said it the way you say a thing that has already been done: brightly, and",
  "while doing something else.",
  "",
  "There is a version of this morning in which she swims badly. She has thought about it",
  "in some detail. Not falling in, nothing dramatic &mdash; just an ordinary fourth place, the",
  "kind nobody asks about in the car. It would take about forty seconds and it would",
  "settle the question of next year.",
  "",
  "The girl in block three is doing something complicated with her shoulders. Somebody&rsquo;s",
  "father shouts a name that is not anyone&rsquo;s name here. The air smells of chlorine and",
  "of the inside of a bag.",
  "",
  "&lsquo;Take your marks.&rsquo;",
  "",
  "Here is the thing Ananya has not told anyone, including herself, in any sentence that",
  "used actual words: she likes the first four strokes. Not the racing. The four strokes",
  "after the water closes over, when it is quiet and nobody is anything.",
  "",
  "The starter goes.",
  "",
  "She does not decide to swim well. Her arms decide, somewhere around the fifteen-metre",
  "mark, and by the turn she is second, and coming off the wall she is first, and the",
  "last ten metres are the loudest silence she has ever been in.",
  "",
  "She touches. She hangs on the lane rope with her chest going and looks up at the",
  "board, which says her name, and then along the glass at her mother, who is already",
  "turning to the woman beside her to say something.",
  "",
  "Ananya puts her face back in the water, which is the only place nobody can see it.",
 ]}

C_TEXT_B = {
 'intro': 'From a blog kept by a swimming coach who has run district trials for eleven years.',
 'start': 30,
 'lines': [
  "Every February I get the same email. &lsquo;I have entered my daughter. She doesn&rsquo;t know yet.&rsquo;",
  "",
  "I want to be careful here, because the parents who write that email are not villains.",
  "They are usually right about the talent. That is the difficult part: if they were",
  "wrong, the problem would solve itself in April.",
  "",
  "What they are wrong about is the order. A child who is entered for a thing and then",
  "told about it has been given the result of a decision and no part in making it. At",
  "thirteen, that child has one way left to have an opinion, and it is not a good one:",
  "to swim slowly enough that nobody enters her again.",
  "",
  "I have watched perhaps two hundred children do this. It is very hard to spot, because",
  "it looks exactly like a bad day.",
  "",
  "My advice is always the same and it is almost never taken. Ask her in January. Accept",
  "the answer. If the answer is no, you have lost one season, and if the answer is yes,",
  "you have gained a swimmer instead of a passenger.",
 ]}

D_TEXT = {
 'intro': "Three weeks after his grandfather's funeral, Ravi's family spend a Saturday emptying the house "
          "in Mylapore.",
 'start': 3,
 'lines': [
  "The house is full of people being efficient. Ravi&rsquo;s mother has a system and the system",
  "involves three piles, and the piles have acquired the names Keep, Give and Ask Chithi,",
  "which is where things go when nobody wants to decide.",
  "",
  "Ravi has been given the shelf in the back room, which everyone agrees is the easy one,",
  "because it is only books.",
  "",
  "It is not only books. It is books with things inside them. A bus ticket at page ninety",
  "of a book about bridges. A photograph of nobody Ravi recognises, standing in front of",
  "this house when the gate was a different gate. Four rupees in an envelope marked, in",
  "handwriting he knows, FOR THE BOY.",
  "",
  "He does not ask which boy. There are two possible answers and he only wants one of",
  "them.",
  "",
  "In the front room somebody laughs at something, and then stops laughing in the",
  "particular way people do in a house like this, as if laughing had been issued to them",
  "by mistake and they are handing it back.",
  "",
  "&lsquo;Ravi,&rsquo; his mother calls. &lsquo;Books done?&rsquo;",
  "",
  "&lsquo;Nearly.&rsquo;",
  "",
  "He has done nine. There are about four hundred.",
  "",
  "At one o&rsquo;clock a neighbour comes with rice and a tiffin carrier and stands in the",
  "doorway saying the same four sentences to everybody in turn, which is what she is",
  "there to do and everybody knows it and it helps.",
  "",
  "The almirah in the back room is locked and the key is not in the house. Ravi&rsquo;s uncle",
  "says they will force it next Saturday. Ravi says nothing, because he would like there",
  "to be a next Saturday, and the almirah is the reason there has to be one.",
  "",
  "By evening the piles have won. The house looks like a house that anybody could have",
  "lived in, which Ravi had not known was a thing that could be done to a room in one",
  "day.",
  "",
  "He takes the envelope. He does not take the four rupees out of it.",
 ]}

D_TEXT_B = {
 'intro': 'The following advertisement appeared in a Chennai newspaper the following month.',
 'start': 31,
 'lines': [
  "MYLAPORE &mdash; INDEPENDENT HOUSE &mdash; 2,400 SQ FT",
  "",
  "A rare opportunity to acquire a well-located independent property in one of the city&rsquo;s",
  "most established residential neighbourhoods. Built 1968 and held by the same family",
  "since construction, the property is offered with vacant possession and clear title.",
  "",
  "The accommodation comprises four bedrooms, a large front room and a rear room",
  "currently used for storage, together with an original almirah and fittings. The",
  "structure is sound throughout, although the interiors are dated and the property would",
  "benefit from comprehensive modernisation.",
  "",
  "Given the plot dimensions and the current zoning, there is considerable scope for",
  "redevelopment, and the site may be of particular interest to builders.",
  "",
  "Viewing strictly by appointment. Price on application.",
  "",
  "Contact: Sundaram Estates, Luz Corner.",
 ]}


def texts(a, b):
    return [{'lines': a['lines'], 'start': a['start'], 'intro': '<b>Text A</b> &mdash; ' + a['intro']},
            {'lines': b['lines'], 'start': b['start'], 'intro': '<b>Text B</b> &mdash; ' + b['intro']}]


def quote_parts(n=2):
    """The reference paper's Quotation/Explanation block: one mark each.

    The heading goes in `text`, not in `label` — the label column is 26pt wide and
    would set "Quotation 1" one character per line.
    """
    out = []
    for i in range(1, n + 1):
        out.append({'label': '', 'text': '<b>Quotation %d</b>' % i, 'marks': 1, 'space': 16})
        out.append({'label': '', 'text': '<b>Explanation %d</b>' % i, 'marks': 1, 'space': 24})
    return out


def order_grid(events):
    rows = [['Event', 'Order of events']]
    for e, v in events:
        rows.append([e, v])
    return rows


# ================================================================ Paper A

A = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper A',
 'meta': 'Medium · 35 minutes · 25 marks', 'marks': 25, 'instructions': INSTR_MED,
 'footer': 'Paper A · Medium · ' + TOPIC, 'endnote': ENDNOTE,
 'inserts': texts(A_TEXT, A_TEXT_B),
 'questions': [
  {'section': 'Section A — reading', 'text': 'Look at <b>lines 3&ndash;12</b>.', 'marks': 3,
   'ref': (3, 12), 'keys': ['counted', 'folds'],
   'parts': [
     {'label': '(a)', 'text': 'Meera is anxious about the round before it has properly begun. '
                              'Which <b>two</b> things tell the reader this?', 'marks': 2, 'space': 28},
     {'label': '(b)', 'text': 'What does the detail that her father <i>does not carry the list</i> '
                              'tell the reader about him? Tick (<font name="UI">&#10003;</font>) <b>one</b> box.', 'marks': 1,
      'tick': ['He is careless about his work',
               'He has done the round so long that it is all memorised',
               'He cannot read his own handwriting',
               'He does not care which tin goes where']}]},

  {'text': 'Look at <b>lines 13&ndash;21</b>.', 'marks': 2, 'ref': (13, 21), 'keys': ['shaking', 'landing'],
   'parts': [
     {'label': '(a)', 'text': 'Give a <b>three-word phrase</b> that shows the climb has been physically hard.',
      'marks': 1, 'space': 16},
     {'label': '(b)', 'text': 'Give <b>one word</b> that means &lsquo;the flat floor at the top of a '
                              'flight of stairs&rsquo;.', 'marks': 1, 'space': 16}]},

  {'text': 'Look at <b>lines 22&ndash;28</b>. Meera is careful to leave no sign that anything went wrong. '
           'Give <b>two</b> things she does that show this.', 'marks': 2, 'space': 28,
   'ref': (22, 28), 'keys': ['dent faces in', 'flattened out']},

  {'section': 'Section B — quotation and explanation',
   'text': 'Look at <b>lines 15&ndash;21</b>. Which of these opinions do you agree with most? '
           'Tick (<font name="UI">&#10003;</font>) <b>one</b> box, then give <b>two</b> quotations that support the opinion you '
           'chose, and explain how each one supports it.', 'marks': 4, 'ref': (15, 21),
   'keys': ['before she knocks', 'not going back inside'],
   'tick': ['Mrs Kamath is simply being polite to a neighbour&rsquo;s child.',
            'Mrs Kamath can see that Meera is struggling, and helps without saying so.'],
   'parts': quote_parts()},

  {'text': 'Look at <b>Text B (lines 30&ndash;42)</b>. Meera writes informally because it is a private '
           'notebook. Give <b>two</b> quotations that are examples of informal writing, and explain how '
           'each one shows informality.<br/><br/>'
           '<i>An example has been given.</i><br/>'
           'Quotation: <i>Did NOT die.</i><br/>'
           'Explanation: capital letters are used for the emphasis of speech, as if she were saying it '
           'out loud to a friend.', 'marks': 4, 'ref': (30, 42), 'keys': ['Appa', 'weird'],
   'parts': quote_parts()},

  {'section': 'Section C — the whole text', 'text': 'Look at <b>lines 39&ndash;41</b>.', 'marks': 2,
   'ref': (39, 41), 'keys': ['piece'],
   'parts': [
     {'label': '(a)', 'text': 'Give <b>one word</b> that means &lsquo;a single part of something '
                              'larger&rsquo;.', 'marks': 1, 'space': 16},
     {'label': '(b)', 'text': 'What does <i>it&rsquo;s all in his head and I had a piece of paper</i> tell '
                              'the reader about how Meera now sees her father?', 'marks': 1, 'space': 22}]},

  {'text': 'Look at <b>lines 22&ndash;25</b>. What does <i>as though someone will drop them</i> suggest '
           'about Meera&rsquo;s father? Tick (<font name="UI">&#10003;</font>) <b>one</b> box.', 'marks': 1, 'ref': (22, 25),
   'keys': ['drop them'],
   'tick': ['He expects his daughter to be careless',
            'He packs for the worst thing that could happen, every time',
            'He has dropped a tin himself in the past',
            'He does not trust the people on the round']},

  {'text': 'Look at <b>Text B</b>. What features tell the reader that this text is a private journal '
           'rather than a story? Give <b>two</b> features.', 'marks': 2, 'space': 28,
   'ref': (30, 42), 'keys': ['Appa', 'notebook']},

  {'text': 'Look at the <b>whole text</b>.', 'marks': 5, 'ref': (3, 42), 'keys': ['wheel against the wall'],
   'parts': [
     {'label': '(a)', 'text': 'Meera and her father both take a pride in the round that neither of them '
                              'says out loud. Give <b>one</b> phrase for each that shows this.',
      'marks': 2, 'space': 30},
     {'label': '(b)', 'text': 'Put these events into chronological order, numbering them from first (1) '
                              'to last (5). <b>One</b> example has been done for you.', 'marks': 3,
      'grid': order_grid([('Meera counts the tins at the gate', '1'),
                          ('Mrs Kamath brings a tumbler of water', ''),
                          ('Meera writes in her maths notebook', ''),
                          ('A tin lid is dented on Kanakapura Lane', ''),
                          ('Meera takes out the list for the fourth time', '')])}]},
 ]}


# ================================================================ Paper B

B = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper B',
 'meta': 'Medium · 35 minutes · 25 marks', 'marks': 25, 'instructions': INSTR_MED,
 'footer': 'Paper B · Medium · ' + TOPIC, 'endnote': ENDNOTE,
 'inserts': texts(B_TEXT, B_TEXT_B),
 'questions': [
  {'section': 'Section A — reading', 'text': 'Look at <b>lines 3&ndash;6</b>.', 'marks': 3,
   'ref': (3, 6), 'keys': ['never once chases', 'ten past five'],
   'parts': [
     {'label': '(a)', 'text': 'Give <b>two</b> things that show this dog does not behave like an '
                              'ordinary stray.', 'marks': 2, 'space': 28},
     {'label': '(b)', 'text': 'What does <i>which is four minutes after Vikram does</i> tell the reader? '
                              'Tick (<font name="UI">&#10003;</font>) <b>one</b> box.', 'marks': 1,
      'tick': ['The dog is always slightly late',
               'Vikram has been timing it, so he has been watching for some time',
               'Practice always begins at ten past five',
               'The dog follows Vikram to the maidan']}]},

  {'text': 'Look at <b>lines 13&ndash;24</b>.', 'marks': 2, 'ref': (13, 24), 'keys': ['does not say', 'cut'],
   'parts': [
     {'label': '(a)', 'text': 'Give a short phrase from lines 13&ndash;14 that shows Vikram has kept the '
                              'feeding to himself.', 'marks': 1, 'space': 16},
     {'label': '(b)', 'text': 'Give <b>one word</b> from lines 22&ndash;24 that means &lsquo;a wound made '
                              'by something sharp&rsquo;.', 'marks': 1, 'space': 16}]},

  {'text': 'Look at <b>lines 17&ndash;21</b>. Give <b>two</b> things that show Vikram is more worried '
           'about the dog than he will admit.', 'marks': 2, 'space': 28,
   'ref': (17, 21), 'keys': ['does not enjoy', 'long way round']},

  {'section': 'Section B — quotation and explanation',
   'text': 'Look at <b>lines 25&ndash;28</b>. Which of these opinions do you agree with most? '
           'Tick (<font name="UI">&#10003;</font>) <b>one</b> box, then give <b>two</b> quotations that support the opinion you '
           'chose, and explain how each one supports it.', 'marks': 4, 'ref': (25, 28),
   'keys': ['stay there', 'two wickets'],
   'tick': ['Vikram sits with the dog because he cannot think what else to do.',
            'Vikram sits with the dog because he has already decided it is his.'],
   'parts': quote_parts()},

  {'text': 'Look at <b>Text B (lines 30&ndash;43)</b>. Vikram&rsquo;s grandmother is deliberately blunt '
           'with him. Give <b>two</b> quotations that show this, and explain how each one does.'
           '<br/><br/><i>An example has been given.</i><br/>'
           'Quotation: <i>I counted, because I am old and I have time.</i><br/>'
           'Explanation: she makes a joke at her own expense, which lets her admit she has studied his '
           'letter closely without sounding as though she is prying.',
   'marks': 4, 'ref': (30, 43), 'keys': ['Now listen', 'Half is worse than neither'],
   'parts': quote_parts()},

  {'section': 'Section C — the whole text', 'text': 'Look at <b>lines 35&ndash;38</b>.', 'marks': 2,
   'ref': (35, 38), 'keys': ['free animal'],
   'parts': [
     {'label': '(a)', 'text': 'Give <b>one word</b> that means &lsquo;not owned or controlled by '
                              'anyone&rsquo;.', 'marks': 1, 'space': 16},
     {'label': '(b)', 'text': 'What does <i>Kindness that comes and goes is a hard thing to be on the end '
                              'of</i> tell the reader about her view of what Vikram has been doing?',
      'marks': 1, 'space': 22}]},

  {'text': 'What does <i>Half is worse than neither</i> (line 39) mean here? '
           'Tick (<font name="UI">&#10003;</font>) <b>one</b> box.', 'marks': 1, 'ref': (39, 39), 'keys': ['Half is worse'],
   'tick': ['Half a chapati is not enough food for a dog',
            'A partly-kept promise leaves the dog worse off than none at all',
            'Two owners are worse for a dog than one',
            'The team should share the responsibility between them']},

  {'text': 'Look at <b>Text B</b>. What features tell the reader that this text is a personal letter '
           'rather than a printed article? Give <b>two</b> features.', 'marks': 2, 'space': 28,
   'ref': (30, 43), 'keys': ['My dear Vikku', 'Ammamma']},

  {'text': 'Look at the <b>whole text</b>.', 'marks': 5, 'ref': (3, 43), 'keys': ['Bring the dog'],
   'parts': [
     {'label': '(a)', 'text': 'Vikram and his grandmother have each understood that the dog is no longer '
                              'really a stray. Give <b>one</b> phrase from each text that shows this.',
      'marks': 2, 'space': 30},
     {'label': '(b)', 'text': 'Put these events into chronological order, numbering them from first (1) '
                              'to last (5). <b>One</b> example has been done for you.', 'marks': 3,
      'grid': order_grid([('Vikram begins bringing half a chapati', '1'),
                          ('Vikram sits on the concrete until seven', ''),
                          ('The letter arrives from Thrissur', ''),
                          ('The dog does not come to practice', ''),
                          ('Vikram finds the dog behind the water tank', '')])}]},
 ]}


# ================================================================ Paper C

C = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper C',
 'meta': 'Hard · 35 minutes · 25 marks', 'marks': 25, 'instructions': INSTR_HARD,
 'footer': 'Paper C · Hard · ' + TOPIC, 'endnote': ENDNOTE,
 'inserts': texts(C_TEXT, C_TEXT_B),
 'questions': [
  {'section': 'Section A — reading', 'text': 'Look at <b>lines 3&ndash;10</b>.', 'marks': 3,
   'ref': (3, 10), 'keys': ['not looked at the water', 'brightly'],
   'parts': [
     {'label': '(a)', 'text': 'Give <b>two</b> things that tell the reader Ananya does not want to be at '
                              'the trial.', 'marks': 2, 'space': 28},
     {'label': '(b)', 'text': 'What does <i>brightly, and while doing something else</i> suggest about '
                              'how her mother told her? Tick (<font name="UI">&#10003;</font>) <b>one</b> box.', 'marks': 1,
      'tick': ['She was in a hurry that morning',
               'She presented it as settled, so that it could not be argued with',
               'She was genuinely delighted for her daughter',
               'She had forgotten to mention it earlier']}]},

  {'text': 'Look at <b>lines 10&ndash;13</b>.', 'marks': 2, 'ref': (10, 13), 'keys': ['ordinary fourth place', 'settle'],
   'parts': [
     {'label': '(a)', 'text': 'Give the <b>three-word phrase</b> that describes the result Ananya has in '
                              'mind.', 'marks': 1, 'space': 16},
     {'label': '(b)', 'text': 'Give <b>one word</b> that means &lsquo;to decide something finally&rsquo;.',
      'marks': 1, 'space': 16}]},

  {'text': 'Look at <b>lines 18&ndash;20</b>. Ananya has avoided admitting something to herself. '
           'Give <b>two</b> things in the writing that show this.', 'marks': 2, 'space': 28,
   'ref': (18, 20), 'keys': ['including herself', 'actual words']},

  {'section': 'Section B — quotation and explanation',
   'text': 'Look at <b>lines 22&ndash;28</b>. Which of these opinions do you agree with most? '
           'Tick (<font name="UI">&#10003;</font>) <b>one</b> box, then give <b>two</b> quotations that support the opinion you '
           'chose, and explain how each one supports it.', 'marks': 4, 'ref': (22, 28),
   'keys': ['Her arms decide', 'nobody can see it'],
   'tick': ['Ananya is pleased to have won, but cannot show it in front of her mother.',
            'Ananya has won the race she meant to lose, and does not yet know what she feels.'],
   'parts': quote_parts()},

  {'text': 'Look at <b>Text B (lines 30&ndash;42)</b>. The coach is careful to be fair to the parents he '
           'disagrees with. Give <b>two</b> quotations that show this, and explain how each one does.',
   'marks': 4, 'ref': (30, 42), 'keys': ['not villains', 'right about the talent'],
   'parts': quote_parts()},

  {'section': 'Section C — the whole text', 'text': 'Look at <b>lines 36&ndash;42</b>.', 'marks': 2,
   'ref': (36, 42), 'keys': ['passenger', 'not a good one'],
   'parts': [
     {'label': '(a)', 'text': 'Give <b>one word</b> that means &lsquo;a person who is carried along '
                              'without taking any part&rsquo;.', 'marks': 1, 'space': 16},
     {'label': '(b)', 'text': 'What does <i>and it is not a good one</i> tell the reader about the '
                              'coach&rsquo;s attitude to a child who swims slowly on purpose?',
      'marks': 1, 'space': 22}]},

  {'text': 'What does <i>It is very hard to spot, because it looks exactly like a bad day</i> '
           '(lines 38&ndash;39) mean? Tick (<font name="UI">&#10003;</font>) <b>one</b> box.', 'marks': 1, 'ref': (38, 39),
   'keys': ['bad day'],
   'tick': ['Children often swim badly for no particular reason',
            'A deliberately slow swim cannot be told apart from a genuine one',
            'The coach cannot watch every lane at once',
            'Weather and illness affect times more than people think']},

  {'text': 'Look at <b>Text B</b>. What features tell the reader that this text is written to persuade '
           'rather than to tell a story? Give <b>two</b> features.', 'marks': 2, 'space': 28,
   'ref': (30, 42), 'keys': ['My advice', 'two hundred children']},

  {'text': 'Look at the <b>whole text</b>.', 'marks': 5, 'ref': (3, 42), 'keys': ['one way left'],
   'parts': [
     {'label': '(a)', 'text': 'Text B says that such a child <i>has one way left to have an opinion</i>. '
                              'Give <b>one</b> phrase from Text A showing Ananya considering exactly '
                              'that, and <b>one</b> showing why she did not do it in the end.',
      'marks': 2, 'space': 30},
     {'label': '(b)', 'text': 'Put these events into chronological order, numbering them from first (1) '
                              'to last (5). <b>One</b> example has been done for you.', 'marks': 3,
      'grid': order_grid([('Her mother fills in the entry form', '1'),
                          ('Ananya plans an ordinary fourth place', ''),
                          ('Ananya looks along the glass at her mother', ''),
                          ('Ananya is told she has been entered', ''),
                          ('The starter goes', '')])}]},
 ]}


# ================================================================ Paper D

D = {
 'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper D',
 'meta': 'Hard · 35 minutes · 25 marks', 'marks': 25, 'instructions': INSTR_HARD,
 'footer': 'Paper D · Hard · ' + TOPIC, 'endnote': ENDNOTE,
 'inserts': texts(D_TEXT, D_TEXT_B),
 'questions': [
  {'section': 'Section A — reading', 'text': 'Look at <b>lines 8&ndash;13</b>.', 'marks': 3,
   'ref': (8, 13), 'keys': ['FOR THE BOY', 'two possible answers'],
   'parts': [
     {'label': '(a)', 'text': 'The adults thought this shelf was the easy job. Give <b>two</b> things '
                              'Ravi finds that show it is not.', 'marks': 2, 'space': 28},
     {'label': '(b)', 'text': 'What does <i>There are two possible answers and he only wants one of '
                              'them</i> suggest about Ravi? Tick (<font name="UI">&#10003;</font>) <b>one</b> box.', 'marks': 1,
      'tick': ['He does not much care who the envelope was meant for',
               'He would rather not find out that it was not meant for him',
               'He has forgotten that he has cousins',
               'He intends to keep the money whatever the answer is']}]},

  {'text': 'Look at <b>lines 14&ndash;19</b>.', 'marks': 2, 'ref': (14, 19), 'keys': ['issued', 'Nearly'],
   'parts': [
     {'label': '(a)', 'text': 'Give the <b>one word</b> Ravi says that hides how little he has actually '
                              'done.', 'marks': 1, 'space': 16},
     {'label': '(b)', 'text': 'Give <b>one word</b> from lines 14&ndash;16 that means &lsquo;handed out '
                              'officially&rsquo;.', 'marks': 1, 'space': 16}]},

  {'text': 'Look at <b>lines 23&ndash;25</b>. Give <b>two</b> things that show Ravi wants the clearing '
           'of the house to take longer.', 'marks': 2, 'space': 28,
   'ref': (23, 25), 'keys': ['says nothing', 'next Saturday']},

  {'section': 'Section B — quotation and explanation',
   'text': 'Look at <b>lines 26&ndash;29</b>. Which of these opinions do you agree with most? '
           'Tick (<font name="UI">&#10003;</font>) <b>one</b> box, then give <b>two</b> quotations that support the opinion you '
           'chose, and explain how each one supports it.', 'marks': 4, 'ref': (26, 29),
   'keys': ['takes the envelope', 'does not take the four rupees'],
   'tick': ['Ravi takes the envelope because of the money inside it.',
            'Ravi takes the envelope because of the handwriting on it.'],
   'parts': quote_parts()},

  {'text': 'Look at <b>Text B (lines 31&ndash;42)</b>. The advertisement describes the house as a product '
           'rather than as somebody&rsquo;s home. Give <b>two</b> quotations that show this, and explain '
           'how each one does.', 'marks': 4, 'ref': (31, 42),
   'keys': ['original almirah', 'scope for'],
   'parts': quote_parts()},

  {'section': 'Section C — the whole text', 'text': 'Look at <b>lines 37&ndash;40</b>.', 'marks': 2,
   'ref': (37, 40), 'keys': ['dated', 'builders'],
   'parts': [
     {'label': '(a)', 'text': 'Give <b>one word</b> that means &lsquo;old-fashioned and in need of '
                              'updating&rsquo;.', 'marks': 1, 'space': 16},
     {'label': '(b)', 'text': 'What does <i>may be of particular interest to builders</i> tell the reader '
                              'about what is likely to happen to the house?', 'marks': 1, 'space': 22}]},

  {'text': 'What does <i>offered with vacant possession</i> (line 34) mean? '
           'Tick (<font name="UI">&#10003;</font>) <b>one</b> box.', 'marks': 1, 'ref': (34, 34), 'keys': ['vacant possession'],
   'tick': ['The house has been emptied of furniture',
            'Nobody is living there, so a buyer can take it over at once',
            'The house has stood abandoned for several years',
            'There is a vacancy for a caretaker at the property']},

  {'text': 'Look at <b>Text B</b>. What features of its language show that it is written to sell rather '
           'than to describe accurately? Give <b>two</b> features.', 'marks': 2, 'space': 28,
   'ref': (31, 42), 'keys': ['comprehensive modernisation', 'rare opportunity']},

  {'section': 'Section D — marking somebody else',
   'text': 'Look at the <b>whole text</b>.', 'marks': 5, 'ref': (3, 42), 'keys': ['almirah'],
   'parts': [
     {'label': '(a)', 'text': 'The same room and the same piece of furniture appear in both texts. '
                              'Choose <b>one</b> of them, and explain what it means in each text.',
      'marks': 2, 'space': 30},
     {'label': '(b)', 'text': 'Another student has written the two answers below. For <b>each</b>, say '
                              'what is wrong with it. Then rewrite <b>one</b> of them properly.<br/><br/>'
                              '<b>Answer 1.</b> <i>&lsquo;A rare opportunity to acquire a well-located '
                              'independent property in one of the city&rsquo;s most established '
                              'residential neighbourhoods.&rsquo; This shows the advertisement is trying '
                              'to sell the house.</i><br/><br/>'
                              '<b>Answer 2.</b> <i>This shows that Ravi is sad.</i>',
      'marks': 3, 'space': 56}]},
 ]}


PAPERS = [A, B, C, D]


# ================================================================ mark schemes

SCHEMES = [
 {'title': 'Paper A &mdash; The Round', 'meta': 'Medium · 25 marks', 'questions': [
  {'n': '1(a)', 'marks': 2,
   'lines': ['Any two of: she counts the eleven tins at the gate and counts them again at the corner '
             '<b>[1]</b>',
             'she has taken the list out of her pocket four times already, so the folds are going soft '
             '<b>[1]</b>',
             'she carries the list at all, when her father does not.'],
   'note': 'Both marks need separate evidence. &ldquo;She is nervous&rdquo; and &ldquo;she is worried&rdquo; '
           'is one idea twice — award one. The soft folds are the answer most students walk past, because '
           'the detail is about paper rather than about Meera.'},
  {'n': '1(b)', 'marks': 1, 'lines': ['<b>He has done the round so long that it is all memorised.</b>'],
   'note': 'The careless option is chosen by students reading &ldquo;does not carry&rdquo; as a failing '
           'rather than as evidence of nineteen years. Point them at the list of names that follows it.'},
  {'n': '2(a)', 'marks': 1, 'lines': ['<b>arms are shaking</b>'],
   'note': 'If they give a whole clause, no mark: the question specified three words, and precision is '
           'the thing being tested. Counting the words before writing is the habit worth building here.'},
  {'n': '2(b)', 'marks': 1, 'lines': ['<b>landing</b>'],
   'note': 'Accept nothing else. &ldquo;Floor&rdquo; and &ldquo;stairs&rdquo; are both in the passage and '
           'both wrong — the definition given is specific.'},
  {'n': '3', 'marks': 2,
   'lines': ['Any two of: she turns the dented tin so the dent faces in <b>[1]</b>',
             'she puts the crate exactly where he leaves it, wheel against the wall <b>[1]</b>',
             'she washes the tins; she returns the list to the drawer with the folds flattened out.'],
   'note': 'The folds being flattened is the strongest answer, because she is erasing the evidence of her '
           'own anxiety, not just tidying. Credit it warmly if it appears.'},
  {'n': '4', 'marks': 4,
   'lines': ['Either opinion may be chosen; the marks are for the quotations and explanations, not the box.',
             'For the second opinion: &ldquo;A woman opens the door before she knocks&rdquo; <b>[1]</b> — '
             'she was already waiting, so she knew Meera would be coming and how long the stairs take '
             '<b>[1]</b>',
             '&ldquo;not talking, not going back inside&rdquo; <b>[1]</b> — she stays without making '
             'conversation, so Meera can rest without it being called resting <b>[1]</b>'],
   'note': 'Cap at 2 if both quotations prove the same point. The commonest loss here is quoting '
           '&ldquo;Tell him Mrs Kamath asked after him&rdquo; twice in two forms.'},
  {'n': '5', 'marks': 4,
   'lines': ['Any two, each with a feature named: &ldquo;Appa does it in 50&rdquo; — family word plus '
             'numerals, written as she would say it <b>[2]</b>',
             '&ldquo;which was weird, and then also nice? Both.&rdquo; — a question asked of nobody and '
             'answered in a fragment, so the reader watches her think <b>[2]</b>',
             'also accept &ldquo;(402)&rdquo;, &ldquo;Did the round. Did NOT die.&rdquo;, or the joke '
             'about the notebook.'],
   'note': 'One mark for the quotation, one for an explanation that <i>names a feature</i>. '
           '&ldquo;This is informal&rdquo; is the question repeated back and earns nothing.'},
  {'n': '6(a)', 'marks': 1, 'lines': ['<b>piece</b>']},
  {'n': '6(b)', 'marks': 1,
   'lines': ['She has realised how much her father knows that is never said aloud, and that the list she '
             'needed is the measure of the distance between them — respect, with some feeling of being '
             'small alongside it.'],
   'note': 'Accept any answer that gets the contrast between his memory and her paper. Do not accept '
           '&ldquo;she thinks he is clever&rdquo; on its own.'},
  {'n': '7', 'marks': 1, 'lines': ['<b>He packs for the worst thing that could happen, every time.</b>'],
   'note': 'The &ldquo;expects his daughter to be careless&rdquo; option catches students who read the '
           'clause as being about Meera. It is about how he packs, every day, for everyone.'},
  {'n': '8', 'marks': 2,
   'lines': ['Any two features, named: capitals for spoken emphasis; sentences with no verb; a note she '
             'must keep from her father; the family word &ldquo;Appa&rdquo;; the flat number in brackets; '
             'she talks about the notebook itself. <b>[2]</b>'],
   'note': 'Features means the furniture of the text type. &ldquo;It is about her day&rdquo; is a summary '
           'and scores zero, however accurate.'},
  {'n': '9(a)', 'marks': 2,
   'lines': ['Meera: &ldquo;puts the empty crate exactly where he leaves it, wheel against the wall&rdquo; '
             'or &ldquo;Doing it again tomorrow&rdquo; <b>[1]</b>',
             'Her father: &ldquo;he does not carry the list&rdquo; or &ldquo;packed the way he packs '
             'everything&rdquo; <b>[1]</b>'],
   'note': 'One phrase for each character. Two phrases about Meera caps at one mark even if both are '
           'excellent — the question named both.'},
  {'n': '9(b)', 'marks': 3,
   'lines': ['Tins at the gate <b>1</b>; list out for the fourth time <b>2</b>; Mrs Kamath&rsquo;s water '
             '<b>3</b>; the dented lid <b>4</b>; the notebook <b>5</b>.',
             'All four correct <b>[3]</b>; three correct <b>[2]</b>; two correct <b>[1]</b>.'],
   'note': 'The dent and the water are the pair most often swapped, because the water is the more '
           'memorable scene. Order comes from the lines, not from how much the reader noticed.'},
 ]},

 {'title': 'Paper B &mdash; The Dog on the Maidan', 'meta': 'Medium · 25 marks', 'questions': [
  {'n': '1(a)', 'marks': 2,
   'lines': ['Any two of: it arrives at the same time every day <b>[1]</b>',
             'it sits behind the stumps &ldquo;as though somebody has paid it to be there&rdquo; <b>[1]</b>',
             'it watches the ball rather than the boys; it never chases.'],
   'note': '&ldquo;It never once chases&rdquo; is the strongest, because chasing is what strays do. '
           'Students who answer &ldquo;it is brown with one ear up&rdquo; have given description, not '
           'behaviour — no mark.'},
  {'n': '1(b)', 'marks': 1,
   'lines': ['<b>Vikram has been timing it, so he has been watching for some time.</b>'],
   'note': 'The question is really about who noticed, not about the dog. Nobody knows a four-minute gap '
           'unless they have been checking.'},
  {'n': '2(a)', 'marks': 1,
   'lines': ['&ldquo;which Vikram does not say&rdquo; (accept &ldquo;does not say&rdquo;).']},
  {'n': '2(b)', 'marks': 1, 'lines': ['<b>cut</b>']},
  {'n': '3', 'marks': 2,
   'lines': ['Any two of: he takes two wickets and does not enjoy either <b>[1]</b>',
             'he walks the long way round the maidan, past the roller and the gap in the fence <b>[1]</b>',
             'he looks at the ground rather than at anything in particular.'],
   'note': 'The two wickets are the key evidence and the one most often missed: taking wickets is the '
           'thing he came for, and it has stopped counting.'},
  {'n': '4', 'marks': 4,
   'lines': ['Either opinion. For the second: &ldquo;the only thing he can think of&rdquo; <b>[1]</b> — '
             'admits he has no plan, which supports the first opinion, so a good answer handles it '
             '<b>[1]</b>',
             '&ldquo;he has not once thought about the two wickets&rdquo; <b>[1]</b> — the thing he came '
             'for has stopped mattering, which is a change of loyalty rather than a lack of ideas '
             '<b>[1]</b>'],
   'note': 'Full marks require the two quotations to make different points. Reward any student who '
           'quotes evidence for the opinion they did <i>not</i> choose and then explains it away.'},
  {'n': '5', 'marks': 4,
   'lines': ['Any two, each explained: &ldquo;Now listen.&rdquo; — two words, imperative, ends the polite '
             'opening and marks where the letter turns <b>[2]</b>',
             '&ldquo;I am not going to say what you want me to say&rdquo; — names his motive for writing '
             'before answering it, so he cannot pretend he was only asking <b>[2]</b>',
             '&ldquo;Half is worse than neither&rdquo; — five words, no softening, and phrased as a rule '
             'rather than an opinion <b>[2]</b>'],
   'note': 'Do not accept the example given in the paper. The mark for explanation is for naming what the '
           'language <i>does</i>; &ldquo;she is being blunt&rdquo; repeats the question.'},
  {'n': '6(a)', 'marks': 1, 'lines': ['<b>free</b>']},
  {'n': '6(b)', 'marks': 1,
   'lines': ['She thinks half-kindness is worse than none: the dog will now wait for him on days he cannot '
             'come, and will not understand why it has been abandoned.'],
   'note': 'Students who answer &ldquo;she thinks he should stop feeding it&rdquo; have missed the last '
           'line of the letter. She is asking him to commit, not to withdraw — and line 43 proves it.'},
  {'n': '7', 'marks': 1,
   'lines': ['<b>A partly-kept promise leaves the dog worse off than none at all.</b>'],
   'note': 'The chapati option is bait for anyone answering from memory of line 13 rather than reading '
           'line 39 in context.'},
  {'n': '8', 'marks': 2,
   'lines': ['Any two: the opening address &ldquo;My dear Vikku&rdquo;; the signature &ldquo;&mdash; '
             'Ammamma&rdquo;; second person throughout; it answers questions the reader cannot see; a '
             'shared family memory from 1971. <b>[2]</b>'],
   'note': 'Answering questions we never saw is the sophisticated answer. Credit it fully — it shows the '
           'student has noticed that a letter is one half of something.'},
  {'n': '9(a)', 'marks': 2,
   'lines': ['Text A: &ldquo;the dog knows the sound of the zip&rdquo; or &ldquo;the exact place&hellip; '
             'the exact moment&rdquo; <b>[1]</b>',
             'Text B: &ldquo;is not a free animal any more&rdquo; or &ldquo;Bring the dog if by then it is '
             'yours&rdquo; <b>[1]</b>'],
   'note': 'The pairing is the point: he shows it through a routine he will not name, she says it '
           'outright. Either may be quoted, but one from each text.'},
  {'n': '9(b)', 'marks': 3,
   'lines': ['Chapati <b>1</b>; dog absent <b>2</b>; found behind the tank <b>3</b>; sits until seven '
             '<b>4</b>; letter arrives <b>5</b>.',
             'All four correct <b>[3]</b>; three <b>[2]</b>; two <b>[1]</b>.'],
   'note': 'The chapati is given as the example precisely because it is told in flashback at line 13 — '
           'students who order by where events appear on the page rather than when they happened get this '
           'one wrong every time.'},
 ]},

 {'title': 'Paper C &mdash; Block Four', 'meta': 'Hard · 25 marks', 'questions': [
  {'n': '1(a)', 'marks': 2,
   'lines': ['Any two of: she has not looked at the water <b>[1]</b>',
             'she has stood on the same two tiles for six minutes <b>[1]</b>',
             'she looks at the clock, the roof, the parents and her own feet — anywhere but the race.'],
   'note': 'Not looking at the water is the best answer available and it is a <i>negative</i> — a thing '
           'that does not happen. Students trained only to hunt for actions miss it.'},
  {'n': '1(b)', 'marks': 1,
   'lines': ['<b>She presented it as settled, so that it could not be argued with.</b>'],
   'note': '&ldquo;Genuinely delighted&rdquo; is not a stupid answer; it is simply not what the sentence '
           'is built to show. Ask what &ldquo;while doing something else&rdquo; is doing there.'},
  {'n': '2(a)', 'marks': 1, 'lines': ['<b>ordinary fourth place</b>']},
  {'n': '2(b)', 'marks': 1, 'lines': ['<b>settle</b>']},
  {'n': '3', 'marks': 2,
   'lines': ['Any two of: &ldquo;has not told anyone, including herself&rdquo; <b>[1]</b>',
             '&ldquo;in any sentence that used actual words&rdquo; — she has known it without ever '
             'phrasing it <b>[1]</b>',
             'the correction &ldquo;Not the racing.&rdquo; — she narrows it the moment she has said it.'],
   'note': 'This question is really about how a thought can be held without language, and the phrase '
           '&ldquo;actual words&rdquo; is the evidence. Accept nothing vague about &ldquo;deep '
           'down&rdquo;.'},
  {'n': '4', 'marks': 4,
   'lines': ['Either opinion. For the second: &ldquo;Her arms decide&rdquo; <b>[1]</b> — the decision is '
             'given to her body, so she never chose to win and cannot take credit or blame <b>[1]</b>',
             '&ldquo;the only place nobody can see it&rdquo; <b>[1]</b> — she hides her face at the moment '
             'she is expected to celebrate, which suggests what she feels is not what a winner should '
             '<b>[1]</b>'],
   'note': 'The strongest answers notice that her mother is already turning away to talk to someone else, '
           'so the face is hidden from an audience that has stopped looking. Reward that.'},
  {'n': '5', 'marks': 4,
   'lines': ['Any two, each explained: &ldquo;are not villains&rdquo; <b>[1]</b> — he names and rejects the '
             'harshest reading before anyone can accuse him of it <b>[1]</b>',
             '&ldquo;They are usually right about the talent&rdquo; <b>[1]</b> — he concedes the parents&rsquo; '
             'strongest point, which makes his disagreement about method rather than motive <b>[1]</b>',
             'also accept &ldquo;I want to be careful here&rdquo;.'],
   'note': 'This is a concession-and-rebuttal question in disguise. A student who writes &ldquo;he is being '
           'nice about them&rdquo; has the point and not the vocabulary — award one, and give them the word.'},
  {'n': '6(a)', 'marks': 1, 'lines': ['<b>passenger</b>']},
  {'n': '6(b)', 'marks': 1,
   'lines': ['He does not blame the child: he treats swimming slowly as the only power she has left, while '
             'still being clear that it is a bad way to use it.'],
   'note': 'Both halves are needed. &ldquo;He thinks it is wrong&rdquo; alone misses the sympathy, and '
           '&ldquo;he understands her&rdquo; alone misses the judgement.'},
  {'n': '7', 'marks': 1,
   'lines': ['<b>A deliberately slow swim cannot be told apart from a genuine one.</b>']},
  {'n': '8', 'marks': 2,
   'lines': ['Any two: direct advice (&ldquo;My advice is always the same&rdquo;); evidence by number '
             '(&ldquo;perhaps two hundred children&rdquo;); concession then rebuttal; direct address to '
             '&ldquo;you&rdquo;; the balanced if/then ending. <b>[2]</b>'],
   'note': 'Naming the structure — he admits the other side first, then answers it — is worth full credit '
           'even if the student has no technical word for it.'},
  {'n': '9(a)', 'marks': 2,
   'lines': ['Considering it: &ldquo;There is a version of this morning in which she swims badly&rdquo; or '
             '&ldquo;an ordinary fourth place&rdquo; <b>[1]</b>',
             'Why she did not: &ldquo;Her arms decide&rdquo; or &ldquo;she likes the first four '
             'strokes&rdquo; <b>[1]</b>'],
   'note': 'The best answers connect the two texts explicitly: Text B predicts the plan, and Text A shows '
           'the one thing the coach did not account for, which is that she enjoys part of it.'},
  {'n': '9(b)', 'marks': 3,
   'lines': ['Form filled <b>1</b>; told <b>2</b>; plans the fourth place <b>3</b>; starter <b>4</b>; '
             'looks at her mother <b>5</b>.',
             'All four correct <b>[3]</b>; three <b>[2]</b>; two <b>[1]</b>.'],
   'note': 'Filling the form and being told are both in February and are given in that order in lines '
           '7&ndash;8 — &ldquo;filled in the form&hellip; found out&hellip; too&rdquo;.'},
 ]},

 {'title': 'Paper D &mdash; The House in Mylapore', 'meta': 'Hard · 25 marks', 'questions': [
  {'n': '1(a)', 'marks': 2,
   'lines': ['Any two of: a bus ticket left at page ninety <b>[1]</b>',
             'a photograph of someone he does not recognise, outside this house when the gate was '
             'different <b>[1]</b>',
             'four rupees in an envelope marked FOR THE BOY in handwriting he knows.'],
   'note': 'The answer &ldquo;there are four hundred books&rdquo; is about quantity and comes at line 19 — '
           'no mark inside this range. The question is about what the books contain.'},
  {'n': '1(b)', 'marks': 1,
   'lines': ['<b>He would rather not find out that it was not meant for him.</b>'],
   'note': 'The strongest single inference in the paper, and it rests on one clause. Students who tick the '
           'money option have read his character from the situation rather than from the sentence.'},
  {'n': '2(a)', 'marks': 1, 'lines': ['<b>Nearly</b>'],
   'note': 'One word, as asked. It is doing an enormous amount of work: nine books out of four hundred.'},
  {'n': '2(b)', 'marks': 1, 'lines': ['<b>issued</b>']},
  {'n': '3', 'marks': 2,
   'lines': ['Any two of: he says nothing when his uncle proposes forcing the almirah <b>[1]</b>',
             '&ldquo;he would like there to be a next Saturday&rdquo; <b>[1]</b>',
             '&ldquo;the almirah is the reason there has to be one&rdquo; — he needs a reason to return, '
             'and the locked door supplies it.'],
   'note': 'Saying nothing is an action here. Point out to any student who missed it that silence is the '
           'fourth tell — a gap — and that this paragraph is built entirely out of one.'},
  {'n': '4', 'marks': 4,
   'lines': ['Either opinion, though the second is far better supported.',
             '&ldquo;in handwriting he knows&rdquo; <b>[1]</b> — the envelope is identified by the hand '
             'that wrote it rather than by what is in it <b>[1]</b>',
             '&ldquo;He does not take the four rupees out of it&rdquo; <b>[1]</b> — leaving the money '
             'inside proves the money is not the point; the object matters intact <b>[1]</b>',
             'The final sentence is two sentences on purpose. Credit any student who notices the full stop.'],
   'note': 'An answer choosing the money opinion can still score four if the quotations are handled '
           'honestly — but it almost never happens, because the evidence runs the other way. Mark what is '
           'written, not what was ticked.'},
  {'n': '5', 'marks': 4,
   'lines': ['Any two, each explained: &ldquo;a rear room currently used for storage&rdquo; <b>[1]</b> — '
             'the room where Ravi found his grandfather&rsquo;s life is reduced to its current function '
             '<b>[1]</b>',
             '&ldquo;an original almirah and fittings&rdquo; <b>[1]</b> — the locked almirah nobody could '
             'open becomes a selling feature, listed beside the taps <b>[1]</b>',
             'also accept &ldquo;held by the same family since construction&rdquo; — sixty years of one '
             'family offered as provenance.'],
   'note': 'The whole question turns on the student having connected two texts that never mention each '
           'other. If they quote well from Text B but do not link it to Text A, cap at two.'},
  {'n': '6(a)', 'marks': 1, 'lines': ['<b>dated</b>']},
  {'n': '6(b)', 'marks': 1,
   'lines': ['It will probably be demolished: builders buy for the plot, so the value is in the land and '
             'the zoning rather than in the house.'],
   'note': 'Accept &ldquo;knocked down&rdquo;, &ldquo;rebuilt&rdquo;, &ldquo;flats&rdquo;. Do not accept '
           '&ldquo;it will be repaired&rdquo; — that is what &ldquo;modernisation&rdquo; sounds like and '
           'is not what &ldquo;scope for redevelopment&rdquo; means.'},
  {'n': '7', 'marks': 1,
   'lines': ['<b>Nobody is living there, so a buyer can take it over at once.</b>']},
  {'n': '8', 'marks': 2,
   'lines': ['Any two: euphemism (&ldquo;dated&rdquo;, &ldquo;would benefit from comprehensive '
             'modernisation&rdquo;); age presented as provenance; formal noun phrases (&ldquo;vacant '
             'possession&rdquo;, &ldquo;clear title&rdquo;); no person mentioned anywhere. <b>[2]</b>'],
   'note': 'That no human being appears in seventeen lines about a family home is the observation worth '
           'having. Give it both marks on its own if it is explained.'},
  {'n': '9(a)', 'marks': 2,
   'lines': ['The almirah: in Text A it is locked, unopened, and the reason Ravi needs there to be another '
             'Saturday <b>[1]</b>; in Text B it is &ldquo;an original almirah and fittings&rdquo;, a '
             'feature in a list <b>[1]</b>',
             'The back room is equally acceptable: the shelf of books with things inside them, against '
             '&ldquo;a rear room currently used for storage&rdquo;.'],
   'note': 'One mark for each text. An answer that only describes Text A, however moving, takes one.'},
  {'n': '9(b)', 'marks': 3,
   'lines': ['<b>Answer 1</b> — the quotation is three lines long and no word is picked out, and the '
             'explanation only repeats what the question already said. <b>[1]</b>',
             '<b>Answer 2</b> — there is no quotation at all, and &ldquo;sad&rdquo; names a feeling '
             'without showing how any words produce it. <b>[1]</b>',
             'A correct rewrite of either, following quote &rarr; zoom &rarr; so what. For example: '
             '&ldquo;&lsquo;rare opportunity&rsquo; — the word <i>opportunity</i> turns one family&rsquo;s '
             'loss into somebody else&rsquo;s luck.&rdquo; Or: &ldquo;&lsquo;He does not take the four '
             'rupees out of it&rsquo; — leaving the money inside shows he wants the envelope for the '
             'handwriting, not for what it holds.&rdquo; <b>[1]</b>'],
   'note': 'The point of this question is that both faults are his own. Ask him which of the two he wrote '
           'last week. Marking somebody else&rsquo;s error is identical work to marking your own and far '
           'easier to face, which is why every Paper D on this site ends here.'},
 ]},
]


# ================================================================ verification

ENTS = [('&mdash;', '—'), ('&ndash;', '–'), ('&lsquo;', '‘'), ('&rsquo;', '’'),
        ('&ldquo;', '“'), ('&rdquo;', '”'), ('&hellip;', '…'), ('&amp;', '&'),
        ('&#10003;', '✓')]


def plain(s):
    s = re.sub(r'<[^>]+>', '', s)
    for a, b in ENTS:
        s = s.replace(a, b)
    return s


def numbered(text):
    """{line number: text} for one insert, blanks skipped, exactly as paper_lib prints it."""
    out, n = {}, text['start']
    for ln in text['lines']:
        if not ln:
            continue
        out[n] = plain(ln)
        n += 1
    return out


def _verify():
    problems = []
    for spec in PAPERS:
        name = plain(spec['title'])

        # 1. marks
        total = 0
        for q in spec['questions']:
            if q.get('parts'):
                psum = sum(p.get('marks', 0) for p in q['parts'])
                if psum != q['marks']:
                    problems.append('%s: parts of "%s" sum to %d, not %d'
                                    % (name, plain(q['text'])[:40], psum, q['marks']))
            total += q['marks']
        if total != spec['marks']:
            problems.append('%s: questions total %d, not %d' % (name, total, spec['marks']))
        if len(spec['questions']) != 9:
            problems.append('%s: %d questions, not 9' % (name, len(spec['questions'])))

        # 2. every passage line fits the frame at its printed size
        for ins in spec['inserts']:
            n = ins['start']
            for ln in ins['lines']:
                if not ln:
                    continue
                w = pdfmetrics.stringWidth(plain(ln), 'Body', 10.2)
                if w > AVAIL - 22:
                    problems.append('%s line %d overflows by %.0fpt: %s'
                                    % (name, n, w - (AVAIL - 22), plain(ln)[:46]))
                n += 1

        # 3. every cited range exists, and the words the scheme expects are inside it
        lines = {}
        for ins in spec['inserts']:
            lines.update(numbered(ins))
        lo_all, hi_all = min(lines), max(lines)
        for q in spec['questions']:
            lo, hi = q['ref']
            if lo < lo_all or hi > hi_all:
                problems.append('%s: question cites lines %d-%d, passage runs %d-%d'
                                % (name, lo, hi, lo_all, hi_all))
                continue
            body = ' '.join(lines[i] for i in range(lo, hi + 1) if i in lines)
            for k in q.get('keys', []):
                if plain(k).lower() not in body.lower():
                    problems.append('%s: "%s" is not in lines %d-%d (question "%s")'
                                    % (name, k, lo, hi, plain(q['text'])[:38]))

        # 4. tick-box questions offer exactly four options
        for q in spec['questions']:
            for t in ([q] + q.get('parts', [])):
                if t.get('tick') and len(t['tick']) not in (2, 4):
                    problems.append('%s: a tick question has %d options' % (name, len(t['tick'])))

    # 5. the scheme covers every question of every paper
    for spec, sc in zip(PAPERS, SCHEMES):
        smarks = sum(q['marks'] for q in sc['questions'])
        if smarks != spec['marks']:
            problems.append('%s: mark scheme totals %d, not %d'
                            % (plain(sc['title']), smarks, spec['marks']))
        missing = [q['n'] for q in sc['questions'] if not q.get('lines')]
        if missing:
            problems.append('%s: empty scheme for %s' % (plain(sc['title']), missing))

    if problems:
        print('VERIFY FAILED:')
        for p in problems:
            print('  ! ' + p)
        raise SystemExit(1)
    print('verify ok — 4 papers, 9 questions each, 25 marks each, every cited line range resolves')


if __name__ == '__main__':
    _verify()
    for spec, letter in zip(PAPERS, 'abcd'):
        path = os.path.join(OUT, 'english-reading-paper-%s.pdf' % letter)
        build_paper(spec, path)
        print('wrote', os.path.relpath(path, ROOT))

    path = os.path.join(OUT, 'english-reading-answers.pdf')
    build_scheme(SCHEMES, path, {
        'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; mark schemes, Papers A to D',
        'meta': 'Tutor copy · four papers · 25 marks each',
        'intro': 'One booklet for all four papers. The <i>note</i> under each question is the point of '
                 'this document: it names the specific mistake the question was built to catch, and says '
                 'how to mark it. The pattern to watch across the four papers is the explanation mark — '
                 'a correct quotation followed by an explanation that only restates it is the single '
                 'largest source of dropped marks in this topic.',
        'footer': 'Mark schemes · tutor copy · ' + TOPIC})
    print('wrote', os.path.relpath(path, ROOT))
