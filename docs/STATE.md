# State and roadmap

Last updated: 28 August 2026.

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

All eleven topics carry their four papers, and every paper is linked from the `#papers` section of the page that teaches it. The hub carries all eleven, a climb ladder, a six-puzzle weekly rotation, and a Practice sheets section that signposts each topic's papers rather than listing forty-four PDFs.

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

**`firstmove.html` — the two-minute drill.** Not a topic page: 32 cross-subject questions where he picks the opening line of working rather than solving anything, graded against eight named techniques. No marks, no lessons, no papers, so it stays out of the climb and keeps its own record. The hub surfaces it in a Two-minute drill section above Topic pages, driven by the `DRILLS` array. See the drill-pages note in `ARCHITECTURE.md`.

## Next

1. **`moments.html` has no videos section.** It predates the format. Add six videos with written tasks, matching the other five pages.
2. **Acids and alkalis** (Chemistry) — flagged `next`.

Grade 7 maths is complete, so the roadmap is now science-led. Ten further topics are listed as `planned` in `TOPICS` in `index.html`; that array is the roadmap. The two remaining maths entries there (`geometry`, `averages`) are beyond the Grade 7 portions above and are not blocking anything.

## Known issues

- **Puzzle overlap.** The hub's weekly puzzle rotation includes a metre-rule balance problem close to Q11 on `moments.html`. Swap one out when convenient.
- **No cross-device sync.** Progress is per-browser by design. Only revisit if the student count grows past a handful, since it needs a backend.
- **The six `sheets/*-answers.pdf` mark schemes are not linked anywhere**, deliberately. If a future tutor-facing page is added, link them there rather than from a topic page.
- **`<b>` inside mark-scheme text does not render bold.** `paper_lib.py` registers `Body-Bold` but never calls `registerFontFamily`, so reportlab silently drops the tag — the booklets read fine because the `[1]` splits carry the structure. Affects every booklet equally. Fixing it means re-rendering all seven.

- **The paper generators need reportlab and pypdf, which the system Python usually does not have.** On the machine this was last built on they live in a gitignored `.venv` at the repo root: run `.venv/bin/python tools/papers/<topic>.py`, not `python3 tools/papers/<topic>.py`. `CLAUDE.md`, `README.md` and `WRITING-PAPERS.md` all still document the bare form.
- **`node tools/smoke.js` fails with no argument.** It defaults to `/home/claude/hub`, a path from the environment the project started in. Pass the directory: `node tools/smoke.js .`. `CLAUDE.md`, `README.md` and `package.json`'s `check` script all still document the bare form.

## Decisions already made — don't relitigate without reason

- **No Jekyll.** The pages are finished HTML; Jekyll would wrap them in a theme and hide underscore paths. `.nojekyll` is committed.
- **Answers ship as one booklet per topic**, not one key per paper. Five files per topic instead of nine, and marking usually means flipping between papers anyway.
- **Papers are per topic page, not per subject.** Physics has two topics and therefore eight papers.
- **The heating curve uses true energy proportions**, which makes the boiling plateau 73% of the graph. That looks lopsided and is the point — do not "fix" it.
- **Self-marking over auto-marking** for written answers. He types an answer, opens the scheme, awards himself 0–3. Immediate auto-marking would let him skip the writing.
- **Staged hints, never a single reveal.** Three escalating hints before the full solution.
