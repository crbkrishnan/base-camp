# Writing test papers

Four papers per topic — **A and B medium, C and D hard** — plus one combined mark-scheme booklet. Each paper is 30 marks. Papers are PDFs generated from Python; never edit a PDF.

## Files

```
tools/paper_lib.py        layout engine — do not change without re-rendering every paper
tools/papers/<topic>.py   content: four paper specs + four mark schemes
```

Copy `tools/papers/chem_particles.py` for a science topic or `maths_fdp.py` for maths, then rewrite the content. Run it:

```
python3 tools/papers/<topic>.py
node tools/smoke.js          # confirms the hub's links resolve to real files
```

It writes into `sheets/` and asserts every paper totals exactly 30. If an assert fires, the marks do not add up — fix the content, not the assert.

## Spec shape

```python
{'eyebrow': …, 'title': …, 'meta': 'Medium · 40 minutes · 30 marks',
 'marks': 30, 'instructions': [...], 'footer': …,
 'questions': [
   {'section':'Section 1 — …',          # optional, starts a new section
    'text':'…', 'marks':3, 'space':32,  # space = mm of ruled writing room
    'tip':'…',                          # optional italic method nudge
    'grid':[[...],[...]],               # optional bordered table for the student to fill
    'parts':[{'label':'(a)','text':'…','marks':1,'space':18}]},
 ]}
```

Give a question either `marks` + `space`, or `parts` (whose marks must sum to the question's `marks`). Ruled space: roughly 16–20 mm for a one-line answer, 26–34 mm for a calculation, 40–48 mm for a multi-step or explanation, 60–84 mm for a sketch or a six-marker.

## House conventions

- Medium papers **print the formula** in the instructions box; hard papers deliberately do not, so C and D test recall too.
- Science papers: calculator allowed, but every number is designed to work without one. Maths and chemistry papers are non-calculator.
- Physics instructions always demand a unit on every answer. Chemistry instructions always demand answers in terms of particles, and forbid "the particles get bigger".
- Hard papers add: *"Several questions describe experiments you may not have seen before — apply the ideas you already have"* or the equivalent for maths.
- Structure each paper in three named sections that progress from mechanical to interpretive.
- **Every Paper D ends with the same question type**: two wrong statements in another student's handwriting, to be diagnosed and corrected. Marking someone else's error is far easier to face than being told you made it, and it is identical cognitive work. Keep this.

## Mark schemes

One booklet per topic, all four papers, tutor copy. It is deliberately **not** linked from the hub — it lives in `sheets/` for the tutor only. Do not add it to `SHEETS` in `index.html`.

```python
{'n':'6', 'marks':3,
 'lines':['Change = 800 − 680 = 120 <b>[1]</b>', '120 ÷ 800 <b>[1]</b>', '= <b>15% decrease</b> <b>[1]</b>'],
 'note':'Dividing by 680 instead of 800 gives 17.6% — the most common error in this topic. Award the first mark only.'}
```

The `note` is the point of the whole booklet. It names the specific mistake the question was built to catch and says how to mark it. A scheme that only lists answers is half-built — the tutor is trying to spot *patterns* across papers, and the notes are what make that possible.

## Getting the numbers right

Before typesetting, write a throwaway script that computes every answer in the paper and print the results. Read them. Then write the content from that output.

Also choose numbers that make wrong methods *visibly* wrong. Examples worth reusing:

- Equal-distance journeys at 60 and 120 km/h average **80**, not 90 — averaging the speeds is refuted by the arithmetic itself.
- A 25% rise needs a **20%** fall to undo, not 25%.
- Two shops offering "25% then 10%" versus "30%" land 60 rupees apart.

And avoid accidental ties: an ordering question where two of the four values are equal has no answer. Check for that explicitly.

## Linking the papers

Papers are linked from the topic page they belong to, never from the hub. Two steps.

**1. The topic page's `#papers` section.** Each of the four cards is an `<a>`, not a `<div>`, and the description already there is a contract with the paper you just generated — if they disagree, one of them is wrong:

```html
<a class="paper" href="sheets/chemistry-particles-paper-a.pdf" download><span class="pn">A</span><span class="pt">Paper A — Medium</span><span class="num" style="color:var(--ink-soft);font-size:13px">35 min</span>
  <p class="pd">What the paper covers.</p></a>
```

Papers C and D take `class="pn hard"`, which tints the badge with the page's warning accent.

**2. The hub.** Set `papers:4` on that topic's entry in `TOPICS` in `index.html`. The hub's Practice sheets section derives itself from that field and links to `<topic>.html#papers` — there is no list of individual PDFs to maintain. Use `str_replace` on a unique anchor; the last time an array here was edited by string index, the splice ate the two arrays that followed it and the homepage went blank.

The mark-scheme booklet is linked from nowhere at all. It sits in `sheets/` for the tutor, and that is deliberate.
