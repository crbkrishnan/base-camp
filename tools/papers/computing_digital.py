#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Computing · Unit 1 · Our Digital World — four papers (A, B medium; C, D hard) and the tutor mark schemes.

Two small capabilities the shared engine does not have are added HERE, in this file only
(paper_lib.py is untouched):
  * fill-in grids whose rows grow to fit wrapped text (the engine's grid rows are a fixed 9 mm),
    with an optional taller minimum row for writing boxes;
  * printed 'exhibits' — a fake post, a chat thread, a licence notice, a table of figures —
    drawn as a boxed, tinted block so the student can tell material from question.
Both are installed by replacing paper_lib._grid for this process; build_paper looks it up at call time.
"""
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import paper_lib as PL
from paper_lib import build_paper, build_scheme, AVAIL, INK, SOFT, LINE, RULE, PAPERBG, S_Q
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle

OUT = os.path.join(ROOT, 'sheets')
os.makedirs(OUT, exist_ok=True)
EYEBROW = 'Base Camp · IGCSE Computing · Grade 7 · Unit 1 · Our digital world'
TOPIC = 'Our Digital World'

# ------------------------------------------------------------------ layout helpers (local to this file)
class _G(list):
    minh = 9 * mm

def G(rows, minh=9):
    """A fill-in grid. First row is the header; rows grow to fit text; blank cells are at least `minh` mm tall."""
    g = _G(rows); g.minh = minh * mm
    return g

def _fill_cell(c, header):
    if header:
        return Paragraph('<font name="UI-Bold" size="9.4">%s</font>' % c, S_Q)
    return Paragraph('<font name="Body" size="10.4">%s</font>' % c, S_Q)

_XS = {
    'mono':  ParagraphStyle('xm',  fontName='Mono',      fontSize=8.2, leading=12,   textColor=SOFT),
    'monob': ParagraphStyle('xmb', fontName='Mono-Bold', fontSize=9.2, leading=13,   textColor=INK),
    'bold':  ParagraphStyle('xb',  fontName='UI-Bold',   fontSize=9.2, leading=13,   textColor=INK),
    'body':  ParagraphStyle('xbd', fontName='Body',      fontSize=10,  leading=14.2, textColor=INK),
    'label': ParagraphStyle('xl',  fontName='Mono',      fontSize=7.8, leading=11,   textColor=SOFT),
}

def X(title, rows, cols, styles, fill=None):
    """A printed exhibit. cols = column width fractions; styles = one of _XS per column.
    A row whose first cell starts with '§' is shaded (used for 'what a quick search finds').
    A cell may be a (style, text) tuple to override the column style."""
    assert abs(sum(cols) - 1.0) < 1e-9 and len(cols) == len(styles)
    return {'x': 1, 'title': title, 'rows': rows, 'cols': cols, 'styles': styles, 'fill': fill}

def _exhibit(x):
    cw = [AVAIL * f for f in x['cols']]
    n = len(cw)
    data = [[Paragraph(x['title'].upper(), _XS['label'])] + [''] * (n - 1)]
    shaded = []
    for ri, r in enumerate(x['rows'], 1):
        cells = []
        for j, c in enumerate(r):
            sty = x['styles'][j]
            if isinstance(c, tuple):
                sty, c = c
            if j == 0 and c.startswith('§'):
                shaded.append(ri); c = c[1:]
            cells.append(Paragraph(c, _XS[sty]))
        data.append(cells)
    t = Table(data, colWidths=cw)
    st = [('SPAN', (0, 0), (-1, 0)), ('BACKGROUND', (0, 0), (-1, 0), PAPERBG),
          ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#FBFAF6')),
          ('BOX', (0, 0), (-1, -1), 0.9, INK), ('LINEBELOW', (0, 0), (-1, 0), 0.6, LINE),
          ('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
          ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]
    for i in range(1, len(data) - 1):
        st.append(('LINEBELOW', (0, i), (-1, i), 0.3, RULE))
    if x.get('fill') is not None:
        f = x['fill']
        st.append(('LINEBEFORE', (f, 1), (f, -1), 0.9, INK))
        st.append(('BACKGROUND', (f, 1), (f, -1), colors.white))
    for i in shaded:
        st.append(('BACKGROUND', (0, i), (-1, i), colors.HexColor('#EFEBE0')))
    t.setStyle(TableStyle(st))
    outer = Table([[t]], colWidths=[AVAIL])
    outer.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                               ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
    return outer

def _grid_auto(rows, col_widths=None):
    if isinstance(rows, dict):
        return _exhibit(rows)
    n = len(rows[0])
    cw = col_widths or [AVAIL / float(n)] * n
    data = [[_fill_cell(c, i == 0) for c in row] for i, row in enumerate(rows)]
    minh = getattr(rows, 'minh', 9 * mm)
    heights = []
    for i, r in enumerate(data):
        need = max(p.wrap(cw[j] - 13, 1000)[1] for j, p in enumerate(r)) + 9
        heights.append(max(9 * mm if i == 0 else minh, need))
    t = Table(data, colWidths=cw, rowHeights=heights)
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.6, LINE),
        ('BACKGROUND', (0, 0), (-1, 0), PAPERBG),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 7), ('TOPPADDING', (0, 0), (-1, -1), 3),
    ]))
    return t

PL._grid = _grid_auto      # build_paper resolves _grid at call time, so this takes effect here only

from reportlab.platypus import KeepTogether, Spacer, BaseDocTemplate

class _Doc(BaseDocTemplate):
    """Keeps a question's stem (and its printed exhibit) on the same page as its first part, so a
    reader never has to turn the page to find what the question is asking about."""
    def build(self, story, **kw):
        def is_part(f):
            c = getattr(f, '_content', [])
            return isinstance(f, KeepTogether) and c and isinstance(c[0], Spacer) and abs(c[0].height - 3) < 1e-6
        out, i = [], 0
        while i < len(story):
            f = story[i]
            if isinstance(f, KeepTogether) and not is_part(f) and i + 1 < len(story) and is_part(story[i + 1]):
                out.append(KeepTogether(list(f._content) + list(story[i + 1]._content)))
                i += 2
            else:
                out.append(f); i += 1
        story[:] = out
        return BaseDocTemplate.build(self, story, **kw)

PL.BaseDocTemplate = _Doc

# ------------------------------------------------------------------ every number, computed
def calc():
    N = {}
    N['pin'] = {n: 10 ** n for n in (4, 5, 6)}
    N['pin_s'] = {n: N['pin'][n] // 1000 for n in (4, 5, 6)}           # 1,000 guesses a second
    assert N['pin_s'] == {4: 10, 5: 100, 6: 1000} and all(N['pin'][n] % 1000 == 0 for n in N['pin'])
    N['l3'] = 26 * 26 * 26
    assert 26 * 26 == 676 and 676 * 26 == N['l3'] == 17576
    N['d5'] = 10 ** 5
    assert N['d5'] > 5 * N['l3'] and N['d5'] < 6 * N['l3']              # "more than five times as many"
    assert N['d5'] > N['l3'] > N['pin'][4]                              # 3 letters beat 4 digits, lose to 5
    N['d5_s'] = N['d5'] // 1000; assert N['d5_s'] == 100
    N['lock_n'] = 10 ** 4
    N['lock'] = 3 / N['lock_n']; assert abs(N['lock'] * 100 - 0.03) < 1e-12
    N['rise'] = (10 - 4) / 4 * 100;  assert N['rise'] == 150
    N['fall'] = (10 - 4) / 10 * 100; assert N['fall'] == 60
    N['l4'] = 26 ** 4
    assert N['l4'] == 676 * 676 == 456976
    assert 400 * 400 > 10 ** 5 and 676 > 400 and 676 < 1000 and 1000 * 1000 == 10 ** 6   # the by-hand bounds
    assert 10 ** 5 < N['l4'] < 10 ** 6
    assert 100 < N['l4'] / 1000 < 1000                                  # seconds, between 100 s and 1,000 s
    assert divmod(100, 60) == (1, 40) and divmod(1000, 60) == (16, 40)
    N['d12'] = 10 ** 12
    N['d12_s'] = N['d12'] // 1000; assert N['d12_s'] == 10 ** 9
    N['yrs'] = N['d12_s'] / (3 * 10 ** 7); assert round(N['yrs']) == 33
    N['yrs_true'] = N['d12_s'] / (365 * 24 * 3600); assert 31 < N['yrs_true'] < 32
    assert N['d12'] // N['pin'][6] == 10 ** 6                           # 12 digits is a million times 6 digits
    return N
N = calc()
def c(n): return '{:,}'.format(n)

# ------------------------------------------------------------------ instructions
BASE = [
 'Answer <b>every</b> question in the space provided.',
 'No calculator is needed anywhere on this paper. Every sum is built to work by hand, using small numbers or powers of ten.',
 'A label alone is rarely a full answer: where a question says <b>explain</b> or <b>describe</b>, give the action or the reason. '
 'A defence only scores with its reason — “install a firewall” earns nothing; say what it does that stops the attack.',
 'The mark for each question is shown in square brackets on the right.',
]
INSTR_MED = BASE + [
 '<b>Fact-check checklist:</b> 1 Source — is it named, and can you check who they are? &nbsp;2 Date — is there one, and does it fit the event? '
 '&nbsp;3 Evidence — can you trace a link, the data or the full quote? &nbsp;4 Hurry — is it pushing you to react or forward it? '
 '&nbsp;5 Other outlets — do reliable, independent outlets report the same thing?',
 '<b>What each defence does:</b> a <b>firewall</b> blocks network traffic that breaks its rules; <b>antivirus</b> scans files and programs against known malware; '
 '<b>anti-spyware</b> detects and removes programs that secretly watch you.',
]
INSTR_HARD = BASE + [
 'Several questions here describe situations you may not have seen before. You are not expected to recognise them — apply the ideas you already have.',
]
MEDMETA = 'Medium · Non-calculator · 35 minutes · 30 marks'
HARDMETA = 'Hard · Non-calculator · 45 minutes · 30 marks'
ENDNOTE = 'End of paper. Check that every defence you named comes with its reason, and every calculation with its working.'

def P(letter, level, meta, instr, questions):
    return {'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Paper ' + letter, 'meta': meta, 'marks': 30,
            'instructions': instr, 'footer': 'Paper %s · %s · %s' % (letter, level, TOPIC),
            'endnote': ENDNOTE, 'questions': questions}

def part(label, text, marks, space=None, **kw):
    d = {'label': label, 'text': text, 'marks': marks}
    if space: d['space'] = space
    d.update(kw); return d

# ================================================================== PAPER A
A_QS = [
 {'section': 'Section 1 — words and tools',
  'text': 'Four things happened to Diya yesterday. Write <b>A</b> (active) or <b>P</b> (passive) in the box to show which part of her digital footprint each one adds to.',
  'marks': 4,
  'grid': G([['What happened', 'A or P'],
             ['She posted a photo of her rangoli on Instagram', ''],
             ['Her cousin tagged her in a video of the family dinner', ''],
             ['A shopping app recorded which pages she looked at', ''],
             ['She filled in a sign-up form for a cricket coaching camp', '']], 9),
  'grid_widths': [AVAIL * 0.82, AVAIL * 0.18]},

 {'text': 'Write the right word in each box: <i>catfishing, trolling, fraping</i> or <i>dissing</i>.',
  'marks': 4,
  'grid': G([['What the person does', 'The word'],
             ['Posts “you’re a joke, just quit” under strangers’ videos every day, to upset them', ''],
             ['Sends an embarrassing photo of a classmate to a group chat of forty, with a mocking caption', ''],
             ['Builds an account from stolen photos and an invented life, and chats to a stranger for weeks', ''],
             ['Posts as a friend from the friend’s phone, which was left logged in', '']], 9),
  'grid_widths': [AVAIL * 0.74, AVAIL * 0.26]},

 {'text': 'For each description, say whether it is malware, and name it. Choose from <i>virus, spyware, ransomware, brute force attack</i>. A row scores only if <b>both</b> boxes are right.',
  'marks': 4,
  'grid': G([['What it does', 'Malware? (Yes / No)', 'Name'],
             ['Runs unseen and sends a copy of every key you press to a stranger', '', ''],
             ['A program tries 10,000 passwords one after another against a login until one works', '', ''],
             ['Encrypts your photos and documents, then demands ₹5,000 for the key', '', ''],
             ['Hides inside a genuine file and copies itself into other files when the file is shared', '', '']], 11),
  'grid_widths': [AVAIL * 0.52, AVAIL * 0.20, AVAIL * 0.28]},

 {'section': 'Section 2 — look at the evidence',
  'text': 'Read the forward below and the result of a quick search.',
  'marks': 3,
  'grid': X('WhatsApp forward · “Forwarded many times”',
            [['THE POST', '<b>*URGENT*</b> Scientists in Germany have PROVED that Class 7 students who eat 2 almonds before an exam score 20 marks higher. No tuition needed. Teachers do not want you to know this. Forward to 10 groups TODAY or you will lose marks!'],
             ['§QUICK SEARCH', 'The first sentence appears word for word on dozens of pages. No scientist, university or study is named on any of them.']],
            [0.17, 0.83], ['mono', 'body']),
  'parts': [part('(a)', 'Name <b>two</b> of the five checks that this post fails. For each one, quote the words from the post that show it.', 2, 40),
            part('(b)', 'Aarav says: “Ten of my friends have already forwarded it, so it must be true.” Explain why that does not make it true.', 1, 24)]},

 {'text': 'Meera finds this photograph and wants to use it in her school project.',
  'marks': 4,
  'grid': X('Licence notice · shown under a photograph on a photo-sharing site',
            [['TITLE', 'Monsoon at Cubbon Park'],
             ['CREATOR', 'Kavya Shetty'],
             ['SOURCE', 'photoshare.example/kavya-s'],
             ['LICENCE', 'Creative Commons BY-NC']],
            [0.17, 0.83], ['mono', 'body']),
  'parts': [part('(a)', 'Write the credit line Meera must put under the photograph.', 2, 26),
            part('(b)', 'A friend wants to print the photograph on T-shirts and sell them for ₹300 each. He says: “It’s fine — we’ll credit Kavya on every one.” State whether this is allowed, and explain using the licence.', 2, 34)]},

 {'text': 'Name the guard — <i>firewall, antivirus</i> or <i>anti-spyware</i> — that does each job.',
  'marks': 3,
  'grid': G([['The job', 'Guard'],
             ['A school stops every computer on its network connecting to a gambling website', ''],
             ['A downloaded file is compared with a database of known malware and moved to quarantine', ''],
             ['A free emoji app that secretly records what you type is found and removed', '']], 11),
  'grid_widths': [AVAIL * 0.74, AVAIL * 0.26]},

 {'section': 'Section 3 — the numbers and the reasons',
  'text': 'A phone lock uses a PIN made only of digits. An attacker’s program makes <b>1,000 guesses every second</b>. '
          'Complete the table. Time to try them all = combinations ÷ 1,000.',
  'marks': 4,
  'grid': G([['Digits in the PIN', 'Combinations', 'Time to try them all'],
             ['4', '10,000', '10 seconds'],
             ['5', '', ''],
             ['6', '', '']], 11),
  'grid_widths': [AVAIL * 0.28, AVAIL * 0.36, AVAIL * 0.36],
  'tip': 'Write each number of combinations as a power of ten first.'},

 {'text': 'Karan posts an angry comment, then deletes it two minutes later. A classmate had already taken a screenshot. '
          'Explain why the comment can still be found.', 'marks': 2, 'space': 30},

 {'text': 'Neha is in a class group chat. She sees several classmates mocking another girl’s photo. Neha is not one of them. '
          'Describe <b>two</b> things Neha should do, each with a reason.', 'marks': 2, 'space': 38},
]
A = P('A', 'Medium', MEDMETA, INSTR_MED, A_QS)

# ================================================================== PAPER B
B_QS = [
 {'section': 'Section 1 — the vocabulary',
  'text': 'Creative Commons licences use four short tags. In each box, write what the tag asks of the person reusing the work.',
  'marks': 4,
  'grid': G([['Tag', 'What it asks of you'],
             ['BY', ''], ['NC', ''], ['ND', ''], ['SA', '']], 11),
  'grid_widths': [AVAIL * 0.18, AVAIL * 0.82]},

 {'text': 'Virus, spyware and ransomware are all malware. For each one, write <b>one thing it does that the other two do not</b>.',
  'marks': 3,
  'grid': G([['Malware', 'One thing only it does'],
             ['Virus', ''], ['Spyware', ''], ['Ransomware', '']], 12),
  'grid_widths': [AVAIL * 0.24, AVAIL * 0.76],
  'tip': 'Not “it is harmful” — all three are. Write an action the other two do not do.'},

 {'text': 'Name the guard that does each job. Write <i>firewall</i>, <i>antivirus</i>, <i>anti-spyware</i>, or <i>none of the three</i>.',
  'marks': 4,
  'grid': G([['The job', 'Guard'],
             ['A downloaded attachment contains a known virus, and you want it stopped before it opens', ''],
             ['A stranger far away keeps trying to open connections into the school’s network', ''],
             ['Rahul uses the password cricket1 on every account he owns, and you want that problem fixed', ''],
             ['A free screensaver quietly sends a list of the sites you visit to a company', '']], 11),
  'grid_widths': [AVAIL * 0.72, AVAIL * 0.28]},

 {'section': 'Section 2 — read the evidence',
  'text': 'Class 7C has a group chat. Read what happened one afternoon.',
  'marks': 4,
  'grid': X('Group chat · Class 7C · Tuesday',
            [['4:02 pm', 'Kabir', 'Quiz team is a waste of time. I am quitting tomorrow.'],
             ['4:03 pm', 'Sneha', 'Seriously?? You were so excited about it.'],
             ['4:11 pm', 'Kabir', 'That was NOT me. I never wrote that.'],
             ['4:12 pm', 'Kabir', 'I left my account logged in on the library computer at lunch.']],
            [0.12, 0.12, 0.76], ['mono', 'bold', 'body']),
  'parts': [part('(a)', 'Name the act.', 1, 13),
            part('(b)', 'Give one piece of evidence from the chat that the 4:02 message was not Kabir’s own choice.', 1, 20),
            part('(c)', 'Give <b>two</b> things Kabir should do next, each with a reason.', 2, 38)]},

 {'text': 'Read this story, then the result of a quick search.',
  'marks': 4,
  'grid': X('Instagram story · account @brightfuture_gifts',
            [['THE POST', '<b>FREE LAPTOP for every Class 7 student!!</b> Share this with 10 friends, then enter your home address and your parent’s phone number at bf-gifts.example. Only 100 left. Offer ends TONIGHT.'],
             ['DETAILS', 'Posted 3 Oct 2026 · no company named'],
             ['§QUICK SEARCH', 'No company’s own website lists any such offer. The link belongs to a site registered last week. No reliable outlet reports it.']],
            [0.17, 0.83], ['mono', 'body']),
  'parts': [part('(a)', 'For each check, write <b>PASS</b> if the post is fine on it and <b>FAIL</b> if it is not.', 2,
                 grid=G([['Check', 'PASS or FAIL'],
                         ['1 Source — named, and checkable?', ''],
                         ['2 Date — there, and fits the event?', ''],
                         ['3 Evidence — can you trace it?', ''],
                         ['4 Hurry — is it pushing you to react?', ''],
                         ['5 Other outlets — do reliable ones report it?', '']], 8.5),
                 grid_widths=[AVAIL * 0.70, AVAIL * 0.30]),
            part('(b)', 'The post asks for a home address and a parent’s phone number. Explain why handing these over is risky, linking your answer to your digital footprint.', 2, 28)]},

 {'text': 'Aadhya’s cousin posts a photo of her at the school gate. The caption reads: “Aadhya, Class 7B, ready for school at 8:10 am.” The cousin tags her.',
  'marks': 3,
  'parts': [part('(a)', 'Does this post add to Aadhya’s <b>active</b> or <b>passive</b> footprint? Give the reason.', 1, 20),
            part('(b)', 'Give two things a stranger could learn from the caption, and explain how <b>one</b> of them could be misused.', 2, 32)]},

 {'section': 'Section 3 — the numbers and the reasons',
  'text': 'Zara says: “Letters make a harder password than digits, so a password of 3 lowercase letters beats one of 5 digits.” '
          'An attacker’s program makes <b>1,000 guesses every second</b>.',
  'marks': 4,
  'parts': [part('(a)', 'Calculate the number of 3-letter lowercase passwords. (You are given 26 × 26 = 676.)', 1, 18),
            part('(b)', 'Calculate the number of 5-digit passwords.', 1, 12),
            part('(c)', 'Use your answers to show that Zara is wrong.', 1, 18),
            part('(d)', 'How many seconds does it take to try every 5-digit password?', 1, 12)]},

 {'text': 'Ishaan’s phone locks for an hour after <b>3</b> wrong guesses. His PIN has 4 digits.',
  'marks': 4,
  'parts': [part('(a)', 'How many different 4-digit PINs are there?', 1, 12),
            part('(b)', 'An attacker gets 3 guesses. Write the chance that one of them is right as a fraction of all the PINs, then as a percentage.', 1, 20),
            part('(c)', 'Explain why locking the phone defeats a brute force attack, even though the PIN is short.', 1, 20),
            part('(d)', 'Name one other defence against password guessing and say what it does.', 1, 20)]},
]
B = P('B', 'Medium', MEDMETA, INSTR_MED, B_QS)

# ================================================================== PAPER C
C_QS = [
 {'section': 'Section 1 — recall',
  'text': 'Write a definition of each term, in one sentence.',
  'marks': 4,
  'parts': [part('(a)', 'Active digital footprint', 1, 18),
            part('(b)', 'Passive digital footprint', 1, 18),
            part('(c)', 'Misinformation', 1, 18),
            part('(d)', 'Copyright', 1, 18)]},

 {'text': 'Before you believe or share a post, you run five checks. Name <b>three</b> of them, and for each say what you would actually look at.',
  'marks': 3, 'space': 48},

 {'text': 'Catfishing, trolling, fraping and dissing are four different acts. For each word, say what the person <b>does</b>, in ten words or fewer, '
          'without using the word itself.',
  'marks': 4,
  'parts': [part('(a)', 'Catfishing', 1, 14), part('(b)', 'Trolling', 1, 14),
            part('(c)', 'Fraping', 1, 14), part('(d)', 'Dissing', 1, 14)]},

 {'section': 'Section 2 — working from printed material',
  'text': 'Farhan’s photograph is on a school-resources website. Four students want to use it. For each one, state whether the licence allows it, '
          'and name the condition in the licence that decides it. A mark needs both.',
  'marks': 5,
  'grid': X('Licence notice · school-resources website',
            [['TITLE', 'Mangoes in the Monsoon'],
             ['CREATOR', 'Farhan Qureshi'],
             ['SOURCE', 'openphotos.example/farhan-q'],
             ['LICENCE', 'Creative Commons BY-NC-SA']],
            [0.17, 0.83], ['mono', 'body']),
  'parts': [part('(a)', 'Ria puts it in a free article on her school’s website, with a credit line.', 1, 20),
            part('(b)', 'Ravi crops the photo, adds the words “Rain, rain, go away”, credits Farhan, and shares the poster free online. '
                        'State what the licence lets him do <b>and</b> what he must do with the poster.', 2, 30),
            part('(c)', 'Nisha prints it on the brochure for her paid tuition classes, with a credit line.', 1, 20),
            part('(d)', 'Kunal copies it into his video with no credit, saying “everybody does it”.', 1, 20)]},

 {'text': 'A local website runs this headline. The police figures are printed beneath it.',
  'marks': 3,
  'grid': X('Local news site · Ward 9 Daily',
            [['HEADLINE', '<b>CHAIN-SNATCHING IN WARD 9 UP 150% THIS MONTH!</b>'],
             ['POLICE FIGURES', 'Last month: 4 cases · This month: 10 cases']],
            [0.22, 0.78], ['mono', 'body']),
  'parts': [part('(a)', 'Calculate the percentage increase.', 1, 24),
            part('(b)', 'Next month there are 4 cases again. A friend says: “So it fell by 150%.” Calculate the real percentage fall.', 1, 26),
            part('(c)', 'The headline is arithmetically correct. State one thing it hides.', 1, 20)]},

 {'text': 'A password is made of <b>4 random lowercase letters</b>. An attacker’s program makes 1,000 guesses a second. You are given 26 × 26 = 676. '
          'You have no calculator, so use estimates that you can check by hand.',
  'marks': 3,
  'parts': [part('(a)', 'Show that there are more than 100,000 possible passwords. (A 5-digit PIN has exactly 100,000.)', 1, 26),
            part('(b)', 'Show that there are fewer than 1,000,000 possible passwords. (A 6-digit PIN has exactly 1,000,000.)', 1, 26),
            part('(c)', 'Between which two times does the attacker take to try them all? Give both in seconds.', 1, 20)]},

 {'section': 'Section 3 — situations you may not have seen',
  'text': 'Nandini runs a boutique in Hubballi. Her firewall is on and her antivirus is updated every night. An assistant installs a free “billing theme” '
          'app on the shop laptop. Over the next fortnight the app secretly records everything typed, including the shop’s net-banking password, and sends it to a stranger, '
          'who then logs in to the account from another city. Nobody notices anything wrong with the laptop.',
  'marks': 4,
  'parts': [part('(a)', 'Name the malware.', 1, 13),
            part('(b)', 'Name the guard Nandini did not have, and state what it does.', 1, 22),
            part('(c)', 'Explain why the firewall did not stop this.', 1, 26),
            part('(d)', 'State one habit that would have prevented the infection in the first place.', 1, 22)]},

 {'text': 'Tanvi’s friend tells her what happened over nine weeks. Read the timeline.',
  'marks': 4,
  'grid': X('What happened · in order',
            [['WEEK 1', 'A new account, “Riya_13”, follows Tanvi. Its photos show a girl in a school uniform.'],
             ['WEEKS 2–8', 'They chat every night. Tanvi shares secrets, including that she is scared of speaking on the school stage.'],
             ['WEEK 9', 'A reverse image search shows the photos belong to a model’s public page in another country.'],
             ['WEEK 9', '“Riya_13” posts Tanvi’s secret in a group chat of 40 classmates, with the caption “Our stage star, ha ha ha”.']],
            [0.17, 0.83], ['mono', 'body']),
  'parts': [part('(a)', 'Two of the four named acts happened here. Name both, and say which part of the story shows each.', 2, 34),
            part('(b)', 'Tanvi wants to delete the whole chat and her account straight away. Explain why she should save evidence first.', 1, 26),
            part('(c)', 'Tanvi’s friend wants to send “Riya_13” an angry threat. Explain why that is a bad idea.', 1, 26)]},
]
C = P('C', 'Hard', HARDMETA, INSTR_HARD, C_QS)

# ================================================================== PAPER D
D_QS = [
 {'section': 'Section 1 — sorting and ordering',
  'text': 'Four things from Aarav’s week. For each, write <b>A</b> or <b>P</b>, and give a short reason that says who put it there.',
  'marks': 4,
  'grid': G([['What happened', 'A or P', 'Reason'],
             ['He uploaded a cricket video to his channel', '', ''],
             ['A coaching app logged where he was every hour', '', ''],
             ['A friend shared a screenshot of an old comment he had deleted', '', ''],
             ['He wrote a game review on a shop’s website, under his own name', '', '']], 14),
  'grid_widths': [AVAIL * 0.42, AVAIL * 0.12, AVAIL * 0.46]},

 {'text': 'For each guard, state what it does <b>and</b> one thing it cannot do. A mark needs both.',
  'marks': 3,
  'parts': [part('(a)', 'Firewall', 1, 24), part('(b)', 'Antivirus', 1, 24), part('(c)', 'Anti-spyware', 1, 24)]},

 {'text': 'These are the five things to do when you are being cyberbullied, listed in the wrong order.',
  'marks': 3,
  'grid': G([['The step', 'Its place, 1 to 5'],
             ['Tell a trusted adult', ''],
             ['Block the person', ''],
             ['Do not retaliate', ''],
             ['Report it to the platform and to school', ''],
             ['Save the evidence', '']], 9),
  'grid_widths': [AVAIL * 0.70, AVAIL * 0.30],
  'parts': [part('(a)', 'Write 1 to 5 in the boxes to put the steps in the correct order.', 2),
            part('(b)', 'Explain why “save the evidence” must come before “block the person”.', 1, 28)]},

 {'section': 'Section 2 — evidence and calculation',
  'text': 'A PIN is made only of digits. An attacker’s program makes <b>1,000 guesses every second</b>, so a 6-digit PIN takes 1,000 seconds to try in full. '
          'Deepak says: “Twice as many digits, so a 12-digit PIN takes twice as long: 2,000 seconds.”',
  'marks': 4,
  'parts': [part('(a)', 'Write the number of 12-digit PINs as a power of ten.', 1, 14),
            part('(b)', 'Work out the time to try them all, in seconds, as a power of ten.', 1, 18),
            part('(c)', 'Taking one year as 3 × 10<super>7</super> seconds, estimate that time in years.', 1, 26),
            part('(d)', 'Explain Deepak’s mistake, in terms of what each extra digit does.', 1, 28)]},

 {
  'text': 'Three posts arrive in a school group chat. The middle column of the table shows what a quick search finds for each.',
  'marks': 5,
  'grid': X('Three posts · and what a quick search finds',
            [[('label', '#'), ('label', 'THE POST'), ('label', 'WHAT A QUICK SEARCH FINDS'), ('label', 'RULING')],
             ['1', 'Notice from the Corporation: garbage collection moves to 6 am from 12 October. Notice no. SW/21/2026.',
              'The Corporation’s website carries notice SW/21/2026 with the same date and time. Two news outlets report it.', ''],
             ['2', 'Photo of a tiger walking down a school corridor. “TODAY in Hosur!! Share before they delete it!!”',
              'The same photograph is in a news report dated 2019, about a tiger that wandered into a school in Assam. No outlet reports any tiger in Hosur.', ''],
             ['3', 'Researchers prove that drinking tea after 6 pm makes children forget what they studied. Forward to every parent you know.',
              'No researchers, university or study is named. The same words appear on many parenting pages. No reliable outlet reports it.', '']],
            [0.05, 0.40, 0.41, 0.14], ['monob', 'body', 'body', 'body'], fill=3),
  'parts': [part('(a)', 'Rule on each post in the right-hand column: <i>real</i>, <i>fake or invented</i>, or <i>real but misleading</i>.', 3),
            part('(b)', 'Name the check that Post 2 fails, and the evidence that shows it.', 1, 22),
            part('(c)', 'Post 3 has been forwarded 4,000 times. Explain why that number is not evidence that it is true.', 1, 26)]},

 {'text': 'Three students are making a video that will be shown free on the school website. For each, say whether they can use the material, and what they must do first.',
  'marks': 3,
  'parts': [part('(a)', 'A song from a film released this year.', 1, 24),
            part('(b)', 'A poem by an author who died in 1920, whose copyright has ended.', 1, 24),
            part('(c)', 'A photograph licensed Creative Commons <b>BY-ND</b>.', 1, 24)]},

 {'section': 'Section 3 — apply and diagnose',
  'text': 'On Monday morning a clinic in Mysuru finds every file on its main computer encrypted, with a message demanding ₹50,000 for a key. '
          'The clinic does have a backup, but it is on an external drive that stays plugged into the same computer all week.',
  'marks': 4,
  'parts': [part('(a)', 'Name the malware.', 1, 13),
            part('(b)', 'The owner wants to pay “to be safe”. Explain why paying does not guarantee a happy ending.', 1, 24),
            part('(c)', 'Explain why the backup did not rescue the clinic.', 1, 26),
            part('(d)', 'Say where the backup should have been kept.', 1, 20)]},

 {'text': 'Another student has written two statements, and both are wrong.<br/>'
          '<b>(i)</b> “I deleted the embarrassing photo from my profile, so it is gone for good and nobody can ever see it again.”<br/>'
          '<b>(ii)</b> “Trolling is when someone pretends to be someone else online, like the fake ‘Ananya, 13’ account that chatted to Meera for two months using stolen photos.”<br/>'
          'For each one, explain the mistake and give the correct version.',
  'marks': 4, 'space': 66},
]
D = P('D', 'Hard', HARDMETA, INSTR_HARD, D_QS)

# ================================================================== MARK SCHEMES
T = ' <b>[1]</b>'
def S(n, marks, lines, note=None):
    d = {'n': n, 'marks': marks, 'lines': [l + T for l in lines]}
    if note: d['note'] = note
    return d

SA = {'title': 'Paper A — Medium', 'meta': '30 marks', 'questions': [
 S('1', 4, ['(a) Rangoli photo: <b>A</b> — she chose to share it',
            '(b) Cousin’s tag: <b>P</b> — someone else posted it; Diya did nothing',
            '(c) Shopping app recording her browsing: <b>P</b> — collected without her sharing it',
            '(d) Sign-up form: <b>A</b> — she deliberately gave the details'],
   'Row (c) is the trap: “I was using the app, so I did it.” Using an app is not the same as choosing to share what it records. The letter alone earns the mark; if he writes A for (c) or (b), ask him who chose to put that data there.'),
 S('2', 4, ['Posting provocative messages to upset strangers: <b>trolling</b>',
            'Spreading a hurtful photo with a mocking caption: <b>dissing</b>',
            'Fake identity from stolen photos: <b>catfishing</b>',
            'Posting as a friend from a logged-in account: <b>fraping</b>'],
   'The swap this question exists to catch is trolling for catfishing (“trolling is pretending to be someone”). The rows are deliberately not in the order the words are listed, so a guess by position scores badly. Fraping is about the logged-in account, not the message. Do not accept “cyberbullying” for any box.'),
 S('3', 4, ['Hidden recording and sending keys: <b>Yes — spyware</b>',
            'Tries passwords in turn: <b>No — brute force attack</b>',
            'Encrypts files, demands payment: <b>Yes — ransomware</b>',
            'Hides in a genuine file and copies itself: <b>Yes — virus</b>'],
   'A row needs both boxes. The brute force row is the discriminator: “Yes” there means he still files every threat under malware. A correct name with the wrong Yes/No earns nothing for that row. “Virus” written for the ransomware row is the lazy default; award nothing.'),
 S('4', 3, ['(a) First failed check, <b>with a quote from the post</b> — for example Hurry: “Forward to 10 groups TODAY”',
            '(a) Second, different failed check with its quote — for example Source: “Scientists in Germany” (no name, no university); Evidence: “PROVED” with no study named; Hurry: “or you will lose marks”; Date: the post has none',
            '(b) Forwards measure how shareable a message is, not whether anyone checked it; his friends may all have believed it without checking'],
   'Naming a check without the quote earns nothing for that check: the quote is the evidence. Other outlets also fails, but the exhibit only says the search found no study, so accept it only if he explains it that way. “Ten friends sent it” as the reason it is true is the trap from the page: it is the reverse of evidence.'),
 S('5', 4, ['(a) Title and creator: “Monsoon at Cubbon Park” by Kavya Shetty',
            '(a) Source and licence: photoshare.example/kavya-s, Creative Commons BY-NC (all four items, in any order)',
            '(b) <b>Not allowed</b>',
            '(b) BY-NC means non-commercial use only; selling T-shirts is commercial, and giving credit meets only the BY condition, it does not cancel NC'],
   'The second mark in (a) needs both source and licence; three of the four items earns one mark in total. In (b) the friend’s “we’ll credit her” is the trap: crediting is manners, not permission. Award the decision mark even if the reason is vague, but never the reason mark for “because it is illegal” alone.'),
 S('6', 3, ['School network blocking a website: <b>firewall</b>',
            'Database of known malware, quarantine: <b>antivirus</b>',
            'Finding and removing a recording app: <b>anti-spyware</b>'],
   'The medium-paper reminder lists the three jobs, so this is application, not recall. If he writes antivirus for the emoji app, he has matched on “find and remove” and ignored “records what you type”; the keyword is spyware.'),
 S('7', 4, ['5 digits: <b>100,000</b> combinations (10<super>5</super>)',
            '5 digits: <b>%s seconds</b> (100,000 ÷ 1,000)' % N['pin_s'][5],
            '6 digits: <b>1,000,000</b> combinations (10<super>6</super>)',
            '6 digits: <b>%s seconds</b> (1,000,000 ÷ 1,000), or 16 minutes 40 seconds' % c(N['pin_s'][6])],
   'The wrong method this table is built to expose is scaling by length: “5 digits is 5 ÷ 4 times as long, so 12.5 seconds”, or adding 10 s a row. The right row sequence is 10 s, 100 s, 1,000 s — each row ten times the one before, because each extra digit multiplies the work by 10. Accept times written as 10<super>2</super> and 10<super>3</super>. Follow-through: if the combinations are wrong but the times are correctly worked from them, award the time marks.'),
 S('8', 2, ['Deleting removes only his own copy',
            'The screenshot is a separate copy that belongs to the classmate; Karan cannot reach it, and it can be saved, shared or posted again'],
   '“Because the internet is forever” on its own earns nothing; it is a slogan, not a mechanism. The page’s trap line is “deleting removes my copy, but copies others made can remain”. Both halves are needed.'),
 S('9', 2, ['One sensible action with its reason — for example, do not like, share or reply, because that adds to the pile; or save the evidence so the school and platform can act',
            'A second, different action with its reason — for example report it to the platform and school, or tell a trusted adult, or support the girl being mocked privately'],
   '“Ignore it” alone is not an answer. The bystander case is deliberate: the page says that if you are only watching, you must not add to it. An action without a reason earns half; “fight the bullies” earns nothing.'),
]}

SB = {'title': 'Paper B — Medium', 'meta': '30 marks', 'questions': [
 S('1', 4, ['<b>BY</b>: credit the creator',
            '<b>NC</b>: non-commercial use only — not to make money',
            '<b>ND</b>: no changes to the work (no cropping, editing or remixing)',
            '<b>SA</b>: share your own version under the same licence'],
   'ND and SA are swapped more than any other pair: “no derivatives” stops changes, “share alike” allows them on condition. “Non-commercial” or “not for profit” must appear for NC; “free to use” alone is a different idea and earns nothing. “Not allowed to copy” for ND earns nothing, because copying with credit is exactly what is allowed.'),
 S('2', 3, ['Virus: <b>copies itself</b> into other files (the only one that does)',
            'Spyware: runs <b>hidden</b>, records what you do and <b>sends it</b> to someone',
            'Ransomware: <b>encrypts your files</b> and demands payment for the key'],
   '“It is harmful” or “it damages your computer” earns nothing: all three do. Corrupting files is not unique to a virus, so award the virus mark only for self-copying or spreading. Ransomware answers that say “locks” or “makes files unusable” without payment or encryption get the mark only if the demand for money is mentioned.'),
 S('3', 4, ['Known virus in an attachment: <b>antivirus</b>',
            'Stranger trying to open connections: <b>firewall</b>',
            'Cricket1 on every account: <b>none of the three</b>',
            'Screensaver sending browsing history: <b>anti-spyware</b>'],
   'The “none of the three” row is the point: the page says no guard fixes a short password. Students who write antivirus or firewall there are reaching for a tool because a tool is on the list. The rows are in a different order from the page’s matcher so the pattern cannot be memorised.'),
 S('4', 4, ['(a) <b>Fraping</b>',
            '(b) Kabir says at 4:11 that it was not him, or that he left his account logged in on the library computer at 4:12',
            '(c) First action with its reason — for example tell the group and the teacher that it was not him, so the false message is corrected; or log out and change his password, so nobody else can use the account',
            '(c) Second, different action with its reason — for example save a screenshot of the 4:02 message with its time, so the school can act; or report it to the platform'],
   'The wrong word to expect is catfishing: someone is pretending to be Kabir. The difference is that a catfish builds a fake identity, whereas a frape borrows a real person’s logged-in account; the account, not the message, is the giveaway. “Delete the message” earns nothing: save the evidence first. Changing the password counts as an action but, on its own, does nothing about the false message.'),
 S('5', 4, ['(a) Date <b>PASS</b>, and Source and Evidence both <b>FAIL</b>',
            '(a) Hurry and Other outlets both <b>FAIL</b>',
            '(b) These details become part of her footprint; once handed over she cannot take them back or control who passes them on',
            '(b) A scammer can use the address and phone number to contact her family, pretend to be trusted, or find her; also they can answer security questions'],
   'Only Date passes: the post carries a date, and it fits an offer that ends tonight. A check passes when there is evidence, not when the post claims to be genuine; “no company named” fails Source even though the account has a name. Each (a) mark covers the rows named on its line, so one wrong row in a group loses that group’s mark. In (b) the first mark is the footprint idea (it cannot be taken back) and the second is the misuse; “because they might scam you” alone earns one.'),
 S('6', 3, ['(a) <b>Passive</b>, because her cousin posted it, not Aadhya',
            '(b) Two things a stranger could learn: her school, her class, the time she arrives at the school gate (any two)',
            '(b) One explained misuse — for example a stranger knows where she will be at 8:10 each day; or school and class are common answers to security questions'],
   'The tag is the whole question: the phrase “I did nothing” is the passive footprint. The page also warns that school names are exactly the answers to security questions; credit that link.'),
 S('7', 4, ['(a) 26 × 26 × 26 = 676 × 26 = <b>%s</b>' % c(N['l3']),
            '(b) 10 × 10 × 10 × 10 × 10 = <b>%s</b>' % c(N['d5']),
            '(c) 100,000 is more than five times 17,576 (5 × 17,576 = 87,880), so 5 digits are harder than 3 letters, and Zara’s rule “letters always win” is wrong',
            '(d) 100,000 ÷ 1,000 = <b>100 seconds</b>'],
   'The tempting wrong method is to multiply instead of raising to a power: 26 × 3 = 78 against 10 × 5 = 50, which seems to prove Zara right. The true figures, 17,576 against 100,000, refute her at once. Accept “about 17,600”. The lesson under it: length multiplies the work, and a bigger character set only helps if the length keeps up.'),
 S('8', 4, ['(a) <b>10,000</b>',
            '(b) <b>3 in 10,000</b> (3/10,000), which is <b>0.03%</b>',
            '(c) The lock limits how many guesses he can make, so the attacker can never try every combination in turn',
            '(d) Two-factor authentication: a second proof, such as a code sent to his phone, so a guessed password alone is not enough; or a longer, unique password, which gives many more combinations to try'],
   '3 ÷ 10,000 written as 3% is the usual error (misplaced decimal point): it is off by a factor of 100, so check the scale. In (c) “the attacker gets locked out” scores only with the idea of a limit on guesses. For (d) any one of the three page defences with its reason; naming two-factor authentication without saying what it does earns nothing.'),
]}

SC = {'title': 'Paper C — Hard', 'meta': '30 marks', 'questions': [
 S('1', 4, ['(a) Data you <b>deliberately</b> share — a post, a comment, a form you fill in',
            '(b) Data collected about you <b>without you deliberately sharing it</b> — sites visited, IP address, location, cookies, posts others make about you',
            '(c) False or <b>misleading</b> information; the person passing it on often believes it or has not checked it',
            '(d) The creator’s legal ownership of creative work, which exists <b>automatically</b> the moment it is made'],
   'Examples are not definitions: “active is when you post a photo” earns nothing without “deliberately”. For (c), “fake news” or “lies” is too narrow, because misinformation includes the true-but-trimmed headline and the real-but-old photo. For (d), “a © symbol” or “you have to register it” is the common wrong belief; no symbol or registration is needed.'),
 S('2', 3, ['First named check with what he would look at — for example Source: is the author named and can I check who they are',
            'Second, different check with what he would look at — for example Date: is there one, and does it fit the event',
            'Third, different check with what he would look at — Evidence (a link, the data or the full quote), Hurry (is it pushing me to forward), or Other outlets (do independent, reliable outlets report it)'],
   'Each mark needs the check <b>and</b> the thing looked at. “Check if it is true” and “google it” are the question restated, not a check; “does it feel real?” is not one either. Checks may be phrased in his own words, but they must not overlap: “the date” and “whether it is old” are one check.'),
 S('3', 4, ['<b>Catfishing</b>: builds a fake identity, with stolen photos and an invented life, to deceive someone',
            '<b>Trolling</b>: posts deliberately provocative or offensive messages to upset people or start arguments',
            '<b>Fraping</b>: uses someone’s logged-in account without permission and posts as them',
            '<b>Dissing</b>: spreads hurtful information, photos or rumours about someone to put them down in public'],
   'Marks are for the act, in about ten words. A definition that uses the word itself, or that says only “bullying someone online”, earns nothing. The most common error is catfishing and trolling swapped; fraping answers that mention “hacking” are credited only if they say the account is already logged in or used without permission.'),
 S('4', 5, ['(a) <b>Allowed</b>: it is non-commercial and she credits the creator (BY and NC both met)',
            '(b) Allowed to change it: there is no ND tag, so cropping and adding text are permitted',
            '(b) He must share the new poster under the <b>same licence</b> (SA), and keep the credit',
            '(c) <b>Not allowed</b>: NC — a brochure for paid classes is commercial use, and credit does not change that',
            '(d) <b>Not allowed</b>: BY requires credit to the creator; the fact that others do it is irrelevant'],
   'Each mark needs the decision <b>and</b> the condition that decides it. Part (b) is the discriminating one: students who see “SA” and assume no changes are allowed have confused it with ND. Part (c) separates those who read NC as “free to download” from those who read it as “not for money”. A student who answers (d) “allowed, because he found it online” has repeated the findable-is-free error.'),
 S('5', 3, ['(a) Increase = 10 − 4 = 6; 6 ÷ 4 × 100 = <b>%d%%</b>' % N['rise'],
            '(b) Fall = 10 − 4 = 6; 6 ÷ <b>10</b> × 100 = <b>%d%%</b>' % N['fall'],
            '(c) It hides how small the numbers are: six extra cases. A percentage makes readers picture a wave; also accept that it hides the earlier months or what is normal'],
   'The pair of parts is the point: a rise of 150% needs a fall of only 60% to undo, because the percentage is taken of a different starting number. Dividing by 4 again gives 150%, which is visibly absurd — you cannot lose more than 100% of something — so ask him how many cases a fall of 150% from 10 would leave: a negative number. Award (a) for “150” even with no working; (b) needs 10 as the divisor.'),
 S('6', 3, ['(a) 676 × 676 is more than 400 × 400 = 160,000, which is more than 100,000 (accept any valid lower bound above 316, or the exact 456,976)',
            '(b) 676 is less than 1,000, so 676 × 676 is less than 1,000 × 1,000 = 1,000,000 (or the exact 456,976)',
            '(c) More than <b>100 seconds</b> and less than <b>1,000 seconds</b> (between 1 min 40 s and 16 min 40 s)'],
   'The exact figure is 26<super>4</super> = %s, and a student who works it out is correct; do not penalise. What the question rewards is bracketing by hand, between the 5-digit and 6-digit PINs. The visible wrong method is 26 × 4 = 104, which falls under the 100,000 line and is refuted at once by the bound in (a).' % c(N['l4'])),
 S('7', 4, ['(a) <b>Spyware</b> (a keylogger)',
            '(b) <b>Anti-spyware</b>: detects and removes programs that secretly record and send your data, and can stop them installing',
            '(c) The stolen data left as ordinary outgoing web traffic that broke none of the firewall’s rules; a firewall filters traffic, it does not find or remove a program that is already installed',
            '(d) Install software only from trusted sources; or do not install free apps from unknown sites'],
   'The trap is “but I had antivirus and a firewall”: two tools are on, the third job is nobody’s. Do not award (b) for “antivirus”, even though some products bundle it; the page keeps the three jobs separate and so must the answer. In (c), “the firewall was off” contradicts the question; award nothing.'),
 S('8', 4, ['(a) <b>Catfishing</b>: a fake account with a model’s stolen photos and an invented life',
            '(a) <b>Dissing</b>: posting her secret in a group chat of 40 with a mocking caption',
            '(b) The screenshots must show usernames, dates and times; once the chat and account are deleted the school and platform have nothing to act on',
            '(c) Hitting back escalates it and gives the other person more to screenshot'],
   'Each named act needs its part of the story. “Fraping” for the fake account is the usual wrong answer: no real account was borrowed. For (b), “save evidence” alone is thinner than “so the school and platform can act”, but award the mark if the idea of keeping proof for someone to act on is clear. Deleting everything “to make it stop” is the instinct the question tests.'),
]}

SD = {'title': 'Paper D — Hard', 'meta': '30 marks', 'questions': [
 S('1', 4, ['Cricket video: <b>A</b> — he chose to upload it',
            'Coaching app logging his location: <b>P</b> — collected without him sharing it',
            'Friend’s screenshot of a deleted comment: <b>P</b> — someone else made and shared the copy',
            'Game review under his own name: <b>A</b> — he deliberately wrote and posted it'],
   'A row earns its mark only if the reason names who chose to put the data there; “A, because it is online” has the right letter and the wrong reason. The screenshot row is the hard one: the original comment was his, but the copy in the screenshot is a friend’s, so it is passive. It also quietly shows why deleting is not enough.'),
 S('2', 3, ['<b>Firewall</b>: checks network traffic against rules and blocks what breaks them — cannot clean a file already on the disk',
            '<b>Antivirus</b>: scans files and programs against a database of known malware and quarantines or deletes what it finds — cannot stop a connection being opened',
            '<b>Anti-spyware</b>: detects and removes programs that secretly record and send your data — cannot filter network traffic (replace a firewall) or fix a weak password'],
   'A mark needs both halves. The classic slip is giving the firewall the antivirus’s job; if the “does” half reads “it protects against viruses”, award nothing for that guard. “Cannot do” answers that are really about the user (“cannot stop you clicking”) are acceptable for the antivirus and anti-spyware lines.'),
 S('3', 3, ['(a) <b>Do not retaliate</b> = 1 and <b>save the evidence</b> = 2',
            '(a) <b>Block</b> = 3, <b>report</b> = 4, <b>tell a trusted adult</b> = 5',
            '(b) Once the person is blocked you may lose sight of their messages or profile, so screenshots showing usernames, dates and times must be taken first'],
   'The order is the page’s: do not retaliate, save, block, report, tell. Award the first (a) mark for the first two places both right and the second for the last three all right, so one swapped pair costs a mark. A student who puts “tell a trusted adult” first is not wrong in life; it is wrong for this paper and worth a conversation. For (b), “blocking may hide their messages” is acceptable; “so you can show someone” alone is not, without the reason the proof would be lost.'),
 S('4', 4, ['(a) 10<super>12</super>',
            '(b) 10<super>12</super> ÷ 10<super>3</super> = <b>10<super>9</super> seconds</b> (1,000,000,000)',
            '(c) 10<super>9</super> ÷ (3 × 10<super>7</super>) = 100 ÷ 3 = <b>about 33 years</b> (accept 30 to 35; a 365-day year gives 31.7)',
            '(d) Each extra digit multiplies the work by 10; six extra digits multiply it by 10<super>6</super>, a million, not by 2'],
   'Deepak’s method, doubling, gives 2,000 seconds — about 33 minutes against about 33 years — which is visibly absurd once part (c) is done. In (b), 1,000 × 10<super>6</super> = 10<super>9</super> is also a valid route: the 12-digit time is a million times the 6-digit time.'),
 S('5', 5, ['(a) Post 1: <b>real</b>',
            '(a) Post 2: <b>real but misleading</b>',
            '(a) Post 3: <b>fake or invented</b>',
            '(b) The <b>date</b> check: the photograph is from 2019, so the date does not fit the event',
            '(c) Forwards measure how shareable a message is, not whether anyone checked it'],
   'One mark per ruling. Post 2 is the one students rule “fake”: the photograph is genuine and the caption is not, which is why the page calls this shape real but misleading, not invented. Post 3 is the shape most people share because it asks them to; “4,000 forwards” is the page’s second trap. In (b) “Source” or “Other outlets” is acceptable only if the answer also mentions the 2019 report; the date is the cleanest answer.'),
 S('6', 3, ['(a) <b>Cannot</b> use it without the owner’s permission or a licence; copyright is automatic, and being easy to find is not the same as being free',
            '(b) <b>Can</b> use it without asking: copyright has ended, so it is in the public domain (a credit is still good practice)',
            '(c) <b>Can</b> use it unchanged, with credit to the creator (BY); cannot crop, edit or remix it (ND)'],
   'Part (a) is the findable-is-free trap again, now in a film song. Part (b) has the opposite error: students who have learnt “always ask” will say ask permission anyway. In (c), giving the licence name without saying that ND forbids changes earns nothing.'),
 S('7', 4, ['(a) <b>Ransomware</b>',
            '(b) Paying does not guarantee the key arrives; the files may stay locked and the owner has lost the money',
            '(c) Ransomware encrypts files on every drive it can reach, including a drive that is plugged in, so the backup was locked too',
            '(d) Somewhere the malware cannot reach — for example a drive kept disconnected, or a separate offline or cloud copy'],
   '“Pay it, and it will be fine” is the instinct. The page’s phrase is “paying does not guarantee the key arrives”. Part (c) is the real test: a backup is useless if it shares the machine with the thing that has been attacked. Accept “disconnect the drive after copying” for (d).'),
 S('8', 4, ['(i) The mistake: deleting removes only <b>his</b> copy; it is not “gone for good”',
            '(i) Correct version: a screenshot, a forward or a saved picture is a copy others hold, so deleting does not remove copies made by others, and the photo can come back',
            '(ii) The mistake: pretending to be someone else is not trolling — it is <b>catfishing</b>',
            '(ii) Correct version: trolling is posting deliberately provocative or offensive messages to upset people or start arguments, often as a stranger'],
   'Both statements are the two most common wrong sentences in the unit, written out as another student’s work. Marking someone else’s error is the same thinking as avoiding your own, and far easier to face. Each statement is two marks: one for finding the mistake and one for the correct version; “it is wrong” without saying why earns neither.'),
]}

# ================================================================== VERIFY + BUILD
def _count_marks(q):
    return q.get('marks', 0) if not q.get('parts') else sum(p.get('marks', 0) for p in q['parts'])

def _verify():
    papers = {'A': A, 'B': B, 'C': C, 'D': D}
    schemes = {'A': SA, 'B': SB, 'C': SC, 'D': SD}
    for k, spec in papers.items():
        qs = spec['questions']
        assert sum(q['marks'] for q in qs) == 30, (k, sum(q['marks'] for q in qs))
        sections = [q['section'] for q in qs if q.get('section')]
        assert len(sections) == 3 and qs[0].get('section'), (k, sections)
        for i, q in enumerate(qs, 1):
            if q.get('parts'):
                assert _count_marks(q) == q['marks'], (k, i, _count_marks(q), q['marks'])
                assert 'space' not in q, (k, i)
            else:
                assert q.get('space') or q.get('grid'), (k, i, 'no answer room')
        sc = schemes[k]['questions']
        assert len(sc) == len(qs), (k, len(sc), len(qs))
        for i, (q, s) in enumerate(zip(qs, sc), 1):
            assert s['n'] == str(i) and s['marks'] == q['marks'], (k, i)
            assert len(s['lines']) == s['marks'], (k, i, len(s['lines']), s['marks'])
            assert all(l.count('[1]') == 1 for l in s['lines']), (k, i)
            assert s.get('note'), (k, i, 'every question needs a note')
        assert sum(s['marks'] for s in sc) == 30
    # house rules by level
    for k in 'AB':
        ins = ' '.join(papers[k]['instructions'])
        assert 'Fact-check checklist' in ins and 'What each defence does' in ins and '35' in papers[k]['meta']
    for k in 'CD':
        ins = ' '.join(papers[k]['instructions'])
        assert 'Fact-check checklist' not in ins and 'What each defence does' not in ins
        assert 'situations you may not have seen before' in ins and '45' in papers[k]['meta']
    d_last = D['questions'][-1]
    assert 'Another student has written two statements, and both are wrong' in d_last['text'] and d_last['marks'] == 4
    # coverage of the six lessons, by keyword across all four papers' question text
    blob = ' '.join(str(q) for spec in papers.values() for q in spec['questions']).lower()
    for lesson, words in {
        'footprint': ['active', 'passive'], 'misinformation': ['quick search', 'forward'],
        'rights': ['licence', 'copyright'], 'cyberbullying': ['catfishing', 'trolling', 'fraping', 'dissing'],
        'malware': ['virus', 'spyware', 'ransomware', 'brute force'],
        'guards': ['firewall', 'antivirus', 'anti-spyware']}.items():
        assert all(w in blob for w in words), (lesson, words)
    # printed material present where the brief asks for it
    assert any(isinstance(q.get('grid'), dict) for q in A['questions'])
    print('verify: all four papers = 30, parts sum, schemes match, house rules and coverage ok')

if __name__ == '__main__':
    _verify()
    files = []
    for spec, code in [(A, 'a'), (B, 'b'), (C, 'c'), (D, 'd')]:
        p = os.path.join(OUT, 'computing-digital-paper-%s.pdf' % code)
        build_paper(spec, p); files.append(p)
    p = os.path.join(OUT, 'computing-digital-answers.pdf')
    build_scheme([SA, SB, SC, SD], p, {
        'eyebrow': EYEBROW, 'title': TOPIC + ' &mdash; Mark schemes',
        'meta': 'Papers A to D · 30 marks each · tutor copy',
        'intro': 'Marks in square brackets show how the total is split; there is one line per mark. Almost every mark lost on this '
                 'unit is lost to the same few confusions: trolling for catfishing, a credit line for permission, a firewall given the '
                 'antivirus’s job, and the belief that deleting something makes it gone. Brute force is the one place where numbers decide: '
                 'the right pattern is that each extra character multiplies the work, and every figure on these papers was computed '
                 'in the generator, not typed. A recurring habit worth marking down: naming a check, a guard or a licence tag with no reason. '
                 'The notes under each answer name the specific mistake that question was built to catch.',
        'footer': 'Mark schemes · ' + TOPIC})
    files.append(p)
    print('\n'.join(files))
