# State and roadmap

Last updated: 3 October 2026.

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
| Hindi sentence construction | Hindi | `hindi.html` | sentence builder, marker machine | **none yet** |
| Letters and email (पत्र और ईमेल) | Hindi | `letters.html` | letter assembler, register switcher | **none yet** |
| Tenses and pronouns (काल और सर्वनाम) | Hindi | `tenses.html` | tense forge, pronoun switchboard | **none yet** |
| Essay writing (निबंध) | Hindi | `essay.html` | outline builder, sentence upgrader | **none yet** |
| Words and spelling (शब्द और वर्तनी) | Hindi | `wordbank.html` | agreement machine, spelling doctor | **none yet** |
| Our digital world (Unit 1) | Computing | `digital.html` | fact-check bench, brute-force bench | A–D + scheme |
| Data handling in Google Sheets (Unit 2) | Computing | `spreadsheets.html` | formula bench, data gate | A–D + scheme |
| Logic gates (Unit 3) | Computing | `logicgates.html` | gate lab, circuit builder | A–D + scheme |
| Designing with the double diamond (Unit 4a) | Computing | `uxdesign.html` | double-diamond sorter, wireframe studio | A–D + scheme |
| HTML and CSS (Unit 4b) | Computing | `htmlcss.html` | code-and-see editor, box-model explorer | A–D + scheme |
| Pure substances and mixtures | Chemistry | `mixtures.html` | particle builder, melting-point test | A–D + scheme |
| Separating mixtures | Chemistry | `separating.html` | separation bench, chromatogram | A–D + scheme |
| Solutions and solubility | Chemistry | `solutions.html` | dissolving tank, solubility curves | A–D + scheme |

All topic pages above carry their four papers, and every paper is linked from the `#papers` section of the page that teaches it. The hub carries them all, a climb ladder, a six-puzzle weekly rotation, and a Practice sheets section that signposts each topic's papers rather than listing sixty PDFs.

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

## Chemistry Unit 5 — mixtures and solubility

Added 18 September 2026, unattended, from the tutor's brief: 5.1 pure substances and mixtures, 5.2 separating mixtures
(with R<sub>f</sub> calculation), 5.3 solutions (with factors affecting solubility). Three pages, twelve papers, three mark-scheme
booklets, all on the standard chemistry template (`particles.html`), 30 marks each, 4 papers each.

| Unit | Subtopic | Page |
|---|---|---|
| 5.1 | Pure substances and mixtures — element, compound, mixture; the melting-point purity test | `mixtures.html` |
| 5.2 | Separating mixtures — filtration, evaporation, distillation, chromatography, magnet, funnel; R<sub>f</sub> | `separating.html` |
| 5.3 | Solutions — solute/solvent/saturated, solubility and its factors, rate against amount, solubility curves | `solutions.html` |

Notes for whoever touches these next:

- **The three pages were assembled by `tools/legacy/unit5/build_page.py`** from `particles.html` plus one content module each
  (`mixtures.py`, `separating.py`, `solutions.py`). Like the rest of `tools/legacy/`, it ran once. The HTML files are now the
  source of truth — **do not re-run the builder over a page that has since been edited by hand**, or the edit is silently lost.
  If you want the builder again, edit the module and accept that the page is regenerated from scratch.
- **One solubility table, three places.** `solutions.html` (`SOLUTES` in the script), Lesson 4's table on the same page, and
  `tools/papers/chem_solutions.py` (`SOL`) all carry the same rounded g-per-100-g values for potassium nitrate, copper sulfate
  and sodium chloride. The paper generator asserts that its printed table matches its data, and computes every number on the
  papers from it (`N` dict) before typesetting. If the table ever changes, change all three.
- **Every R<sub>f</sub> on the separating papers is computed in `chem_separating.py`** (`RF` dict, asserted) — never typed.
- **The old `separation` placeholder in `TOPICS`** ("Mixtures and Separation") was removed; `separating` replaces it. Do not re-add it.
- **Videos.** Channels were taken from search-result titles (FuseSchool, Freesciencelessons, Cognito, Khan Academy, Tyler DeWitt,
  KayScience, Straight Science, The Organic Chemistry Tutor). YouTube itself rate-limited every direct fetch during the build, so
  the pages were not opened in a browser. Worth a two-minute click-through of the eighteen links before the student is sent to them.
- **The hub bridge key** for each page is `<id>-progress-v1` (`mixtures-progress-v1`, `separating-progress-v1`, `solutions-progress-v1`).

## Hindi — a sixth subject

Added 30 September 2026 for a student who is fluent in English but weak at Hindi sentence construction and essays.
`hindi.html` was built on the `reading.html` engine. Three small edits made Hindi a subject (`--hindi` in `index.html`,
one row in `SUBJECTS`, `'hindi'` in the `register_topic.py` allowlist).

- **Two tools:** the sentence builder (tap tiles into Hindi order; the machine names the rule broken; 10 sentences + 6 first-time-right puzzles) and the marker machine (noun + number + marker, showing the oblique change; 8 state-checked puzzles).
- **Extras that are not marks:** a 100-verb bank (`VERBS`; every-day/past/future forms, T/I/B badge for ने) and a 24-sentence marker drill (`DRILL`). Neither counts towards the 30.
- **The 30 marks are unchanged:** 5 MCQ + 5 short + 5 word. Progress key `hindi-progress-v1`.
- **Papers: A–D + scheme on all five**, in `tools/papers/computing_<page>.py` → `sheets/computing-<page>-paper-a..d.pdf` plus `-answers.pdf`. Each generator carries its own independent evaluator (spreadsheet formulas, truth tables, HTML/CSS checkers, WCAG contrast) and asserts 30 marks. They monkeypatch layout helpers inside the generator rather than editing `paper_lib.py` (keep-stem-with-first-part, taller grids, drawn gate symbols, code listings); folding those into `paper_lib.py` would be a tidy-up, but re-render every paper if you do.
- **Video durations are unchecked.** Every URL was confirmed to exist via YouTube oEmbed, but nobody
  has watched them; skim all 30 before the student does.
