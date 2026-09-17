# State and roadmap

Last updated: 17 September 2026.

## Done

| Topic | Subject | Page | Tools | Papers |
|---|---|---|---|---|
| Fractions, decimals, percentages | Maths | `fdp.html` | converter grid, multiplier machine | A–D + scheme |
| The turning effect | Physics | `moments.html` | balance beam | A–D + scheme |
| Speed, distance, time | Physics | `speed.html` | journey machine, solver | A–D + scheme |
| Gas exchange | Biology | `respiration.html` | lung machine, alveoli lab | A–D + scheme |
| The particle model | Chemistry | `particles.html` | particle box, heating curve | A–D + scheme |
| Ratio and proportion | Maths | `ratio.html` | share bar, best-buy comparer | A–D + scheme |
| Laws of indices | Maths | `indices.html` | factor counter, pattern ladder | A–D + scheme |
| Integers, primes and roots | Maths | `integers.html` | twin factor trees, square/cube stacker | A–D + scheme |
| Expressions and formulae | Maths | `expressions.html` | tile mat, bracket grid | A–D + scheme |
| Constructing and solving equations | Maths | `equations.html` | balance scales, step machine | A–D + scheme |
| Place value, rounding, estimating | Maths | `placevalue.html` | place-value board, rounding line | A–D + scheme |
| Characteristics of forces | Physics | `forces.html` | tug-of-war rig, weighing bay | A–D + scheme |
| Pressure in solids and liquids | Physics | `pressure.html` | pressure pad, depth tank | A–D + scheme |
| Gas pressure and diffusion | Physics | `gaspressure.html` | gas box, diffusion tube | A–D + scheme |
| Magnets and magnetic fields | Physics | `magnetism.html` | field plotter, two-magnet bench | A–D + scheme |
| Reading comprehension | English | `reading.html` | evidence bench, mark machine | A–D + scheme |

All fifteen topics carry their four papers, and every paper is linked from the `#papers` section of the page that teaches it. The hub carries all fifteen, a climb ladder, a six-puzzle weekly rotation, and a Practice sheets section that signposts each topic's papers rather than listing sixty PDFs.

## Grade 7 maths syllabus coverage

Checked against the Grade 7 portions in August 2026. **Every listed subtopic is now taught, practised on-page for 30 marks, and examined across four papers.** Recorded here so the next session can check completion without re-deriving it.

| Unit | Subtopic | Page |
|---|---|---|
| 1.1 | Factors, multiples and primes | `integers.html` |
| 1.2 | Multiplying and dividing integers | `integers.html` |
| 1.3 | Square roots and cube roots | `integers.html` |
| 1.4 | Indices | `indices.html` |
| 2.1 | Constructing expressions | `expressions.html` |
| 2.2 | Using expressions and formulae | `expressions.html` |
| 2.3 | Expanding brackets | `expressions.html` |
| 2.4 | Factorising | `expressions.html` |
| 2.5 | Constructing and solving equations | `equations.html` |
| 3.1 | Multiplying and dividing by 0.1 and 0.01 | `placevalue.html` |
| 3.2 | Rounding | `placevalue.html` |
| 4.1–4.3 | Ordering, multiplying, dividing decimals | `fdp.html` lesson 4 |
| 7.1 | Fractions and recurring decimals | `fdp.html` lesson 4 |
| 7.2 | Ordering fractions | `fdp.html` lesson 2 |
| 7.3 | Subtracting mixed numbers | `fdp.html` lesson 3 |
| 7.4 | Multiplying an integer by a mixed number | `fdp.html` lesson 3 |
| 7.5 | Dividing an integer by a fraction | `fdp.html` lesson 3 |
| 10.1–10.2 | Percentage change, multipliers | `fdp.html` lessons 5–6 |
| 12.1–12.3 | Simplifying, sharing, direct proportion | `ratio.html` |

Two notes on how this was closed:

- **Unit 2 was split across two pages** rather than one. The old `TOPICS` entry `{id:'algebra', title:'Letters as Numbers'}` covered both halves and has been deleted; `expressions` and `equations` replace it. Do not re-add it.
- **`fdp.html` lesson 3 was strengthened in place** for 7.3 and 7.4 — mixed-number subtraction with borrowing, and integer × mixed number by both routes (partition, and improper fraction). Lesson, question and mark counts are unchanged at 6 / 15 / 30, so the meta chip and hub card were untouched.

  The fdp **papers were not regenerated**, because Paper B already examines this: Q2(b) is `3 1/3 − 1 5/6`, which genuinely needs a borrow, and Q2(c) is `1 1/4 × 2 2/5`. Note that 7.4 is examined there as *mixed × mixed* rather than literally *integer × mixed* — a harder case that subsumes the skill, but not the syllabus's literal wording. If a future paper revision wants the literal form, add it to Paper C or D, which carry no mixed numbers at all.
- **`integers.html` carries two tools for three subtopics.** The factor trees cover 1.1 and the stacker covers 1.3; multiplying and dividing negatives (1.2) is carried by lesson 4 with a number-line pattern demo instead. That was a deliberate choice over inventing a thin third tool.

`indices.html` arrived as a finished page rather than being built in place, so it was registered with `python3 tools/register_topic.py indices.html` — see `ADDING-A-TOPIC.md` step 7. Its papers were written afterwards, against the four descriptions the page already carried in `#papers`; those descriptions are the contract the papers had to match.

**The maths mock exam — four cross-topic papers, 80 marks each.** `tools/papers/maths_mock.py` → `sheets/maths-mock-paper-a..d.pdf` plus `maths-mock-answers.pdf`. A and B medium, C and D hard, 75 minutes, eight pages each, spanning all 24 subtopics of Units 1, 2, 3, 4, 7, 10 and 12 in every paper. Every topic paper examines one unit in isolation; nothing else on the site makes him face seven at once with no heading telling him which method a question wants.

Three deliberate departures, recorded here so they are not "fixed" back:

- **80 marks, not 30.** `CLAUDE.md` non-negotiable #5 fixes 30 marks per paper. That rule is about *topic* papers, where 30 mirrors the 30 on-screen marks of the page that teaches it. A mock is a different artefact and the tutor set 80. The assert was not removed — it asserts 80, alongside a section-balance assert of 10 / 16 / 24 / 30. **Do not change #5**; this is an exception, not a new rule.
- **No formula or method reminder on any of the four.** `WRITING-PAPERS.md` says medium papers print the formula and only hard papers withhold it. Overridden on the tutor's instruction — recall is part of what a mock is for — so A and B carry the same bare instruction box as C and D. Difficulty separates the pairs through the questions alone.
- **The hub carries them in a hand-written `<section id="mock">`**, not through `TOPICS`. `renderSheets()` derives the Practice sheets list from `TOPICS` and hardcodes "30 marks each", so it cannot carry these, and a mock belongs to no topic page. The section is static HTML reusing the existing `.sheet` / `.badge` classes, so no render function can break on it. The mark-scheme booklet is linked from nowhere, like the other seven.

`maths_mock.py` runs `_verify()` on every build, recomputing all four papers' answers from scratch, and `coverage_check()`, which fails the build if an edit ever drops one of the 24 subtopics. The ordering questions assert that no two values tie.

**`firstmove.html` — the two-minute drill.** Not a topic page: 32 cross-subject questions where he picks the opening line of working rather than solving anything, graded against eight named techniques. No marks, no lessons, no papers, so it stays out of the climb and keeps its own record. The hub surfaces it in a Two-minute drill section above Topic pages, driven by the `DRILLS` array. See the drill-pages note in `ARCHITECTURE.md`.

## Grade 7 physics syllabus coverage

Checked against the Grade 7 portions in August 2026. Four pages were added on 30 August to close Units 8, 9 and 11.

| Unit | Subtopic | Page |
|---|---|---|
| 8.1–8.2 | Speed, distance, time and travel graphs | `speed.html` |
| 8.3 | Characteristics of forces | `forces.html` |
| 8.4 | Turning effect / moment of a force | `moments.html` |
| 9.1 | Pressure | `pressure.html` |
| 9.2 | Pressure in liquids | `pressure.html` |
| 9.3 | Gas pressure | `gaspressure.html` |
| 9.4 | The particle model and pressure | `gaspressure.html` |
| 9.5 | Diffusion | `gaspressure.html` |
| 11.1 | Magnetic fields | `magnetism.html` |

Two notes on how this was split:

- **Unit 9 was split across two pages, not one.** `pressure.html` takes the calculation half (`p = F/A` and `p = ρgh`); `gaspressure.html` takes the explanation half, where the marks go to the wording about collisions per unit area per second rather than to arithmetic. One page covering all five subtopics would have had to drop one of those two skills.
- **The old `density` roadmap entry was retitled** from "Density and Pressure" to "Density and Floating", because `pressure.html` now teaches the pressure half. Do not re-add pressure to it.

## English — a fifth subject

Added 17 September 2026, from a real school paper the tutor supplied
(`reference/reading_comprehension_reference.pdf`: English Paper 2, Grade 7, 25 marks, 35 minutes).
`docs/READING-COMPREHENSION.md` is the guide; read it before touching `reading.html` or
`tools/papers/english_reading.py`.

The diagnosis behind the topic: retrieval is worth about 7 of the 25 marks and he already gets most
of them. The other 18 go to inference, word-in-context, writer's choices and register. So the page
teaches **one named framework** — the ladder (Says → Shows → So what), the five tells, the answer
shape (quote → zoom → so what), and the brake (*could you point at a word?*) — and nothing else.
Keep that wording identical wherever it appears; it is meant to become a reflex.

Four deliberate departures, recorded so they are not "fixed" back:

- **English is a fifth subject.** Three small edits made it possible: `--english` / `--english-t` in
  `index.html`, one row in `SUBJECTS`, and `'english'` added to the allowlist in
  `tools/register_topic.py`. Everything else in the hub is data-driven off `SUBJECTS`.
- **The papers are 25 marks, not 30**, at 35 minutes, nine questions, in the reference's own mark
  distribution. `CLAUDE.md` #5 fixes *topic* papers at 30 because that mirrors the 30 on-screen
  marks; a reading paper's job is to rehearse the exact artefact he sits, and the school's is 25.
  This is an exception like the 80-mark maths mock — **do not change #5**, and do not "correct"
  these to 30. The generator asserts 25.
- **The on-page 30 marks are unchanged**, still 5 MCQ + 5 short + 5 word. One paired text (Arjun and
  the power cut, plus his journal) is line-numbered 3–33 and 35–49 and mounted at the head of all
  three question sections, so he never scrolls back.
- **`paper_lib.py` gained three additive pieces** — `passage()`, `_tickboxes()`, and `q['tick']` /
  `p['tick']` / `spec['inserts']` wiring. No existing code path was touched.

`english_reading.py` runs `_verify()` on every build. The reading-paper equivalent of checking the
arithmetic (`CLAUDE.md` #6) is checking the **line references**, and they fail the same silent way.
It re-checks that every passage line fits the frame at its printed size, that every range a question
cites exists, that the words the mark scheme expects are inside the range it names, and that the
marks total 25. On the first build it caught 35 wrong references — every single question had been
numbered by eye. Trust it over your own counting.

## Next

1. **`moments.html` has no videos section.** It predates the format. Add six videos with written tasks, matching the other five pages.
2. **Acids and alkalis** (Chemistry) — flagged `next`.

Grade 7 maths is complete and the Grade 7 physics units above are complete, so the roadmap is now biology- and chemistry-led. Ten further topics are listed as `planned` in `TOPICS` in `index.html`; that array is the roadmap. The two remaining maths entries there (`geometry`, `averages`) are beyond the Grade 7 portions above and are not blocking anything.

## Known issues

- **Puzzle overlap.** The hub's weekly puzzle rotation includes a metre-rule balance problem close to Q11 on `moments.html`. Swap one out when convenient.
- **No cross-device sync.** Progress is per-browser by design. Only revisit if the student count grows past a handful, since it needs a backend.
- **The six `sheets/*-answers.pdf` mark schemes are not linked anywhere**, deliberately. If a future tutor-facing page is added, link them there rather than from a topic page.
- ~~**`<b>` inside mark-scheme text does not render bold.**~~ **Fixed 17 September 2026.**
  `paper_lib.py` now calls `registerFontFamily` for `Body`, `UI` and `Mono`, so `<b>` and `<i>` are
  no longer silently dropped. Every generator was re-run and **not one question paper changed page
  count** — the fix affects glyphs, not pagination. (The booklet number column was widened 21pt →
  32pt at the same time so that `1(a)` stops wrapping, which added one page to three of the answer
  booklets.) It mattered enough to do now because the English papers
  carry their instructions in bold (*give **two** things*, *one **word***), and losing that loses the
  instruction. If you edit a paper, expect bold to work.

- **`&#10003;` does not exist in DejaVu Serif.** A tick in body text renders as an empty box. Wrap it:
  `Tick (<font name="UI">&#10003;</font>) one box`. `english_reading.py` does this everywhere.

- **The paper generators need reportlab and pypdf, which the system Python usually does not have.** On the machine this was last built on they live in a gitignored `.venv` at the repo root: run `.venv/bin/python tools/papers/<topic>.py`, not `python3 tools/papers/<topic>.py`. `CLAUDE.md`, `README.md` and `WRITING-PAPERS.md` all still document the bare form.
- **`node tools/smoke.js` fails with no argument.** It defaults to `/home/claude/hub`, a path from the environment the project started in. Pass the directory: `node tools/smoke.js .`. `CLAUDE.md`, `README.md` and `package.json`'s `check` script all still document the bare form.

## Decisions already made — don't relitigate without reason

- **No Jekyll.** The pages are finished HTML; Jekyll would wrap them in a theme and hide underscore paths. `.nojekyll` is committed.
- **Answers ship as one booklet per topic**, not one key per paper. Five files per topic instead of nine, and marking usually means flipping between papers anyway.
- **Papers are per topic page, not per subject.** Physics has two topics and therefore eight papers.
- **The heating curve uses true energy proportions**, which makes the boiling plateau 73% of the graph. That looks lopsided and is the point — do not "fix" it.
- **Self-marking over auto-marking** for written answers. He types an answer, opens the scheme, awards himself 0–3. Immediate auto-marking would let him skip the writing.
- **Staged hints, never a single reveal.** Three escalating hints before the full solution.
