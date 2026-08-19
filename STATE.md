# State and roadmap

Last updated: August 2026.

## Done

| Topic | Subject | Page | Tools | Papers |
|---|---|---|---|---|
| Fractions, decimals, percentages | Maths | `fdp.html` | converter grid, multiplier machine | A–D + scheme |
| The turning effect | Physics | `moments.html` | balance beam | A–D + scheme |
| Speed, distance, time | Physics | `speed.html` | journey machine, solver | A–D + scheme |
| Gas exchange | Biology | `respiration.html` | lung machine, alveoli lab | — |
| The particle model | Chemistry | `particles.html` | particle box, heating curve | A–D + scheme |

The hub carries all five, a climb ladder, a six-puzzle weekly rotation, and sixteen linked papers.

## Next

1. **Biology papers** for `respiration.html` — the only completed page without its four papers. Its `#papers` section already describes A–D; the papers must match those descriptions.
2. **`moments.html` has no videos section.** It predates the format. Add six videos with written tasks, matching the other four pages.
3. **Ratio and proportion** (Maths) — flagged `next` in `TOPICS`. Natural follow-on from `fdp.html` because it reuses the multiplier idea.
4. **Acids and alkalis** (Chemistry) — flagged `next`.

Eleven further topics are listed as `planned` in `TOPICS` in `index.html`; that array is the roadmap.

## Known issues

- **Puzzle overlap.** The hub's weekly puzzle rotation includes a metre-rule balance problem close to Q11 on `moments.html`. Swap one out when convenient.
- **No cross-device sync.** Progress is per-browser by design. Only revisit if the student count grows past a handful, since it needs a backend.
- **The two `sheets/` mark schemes are not linked anywhere**, deliberately. If a future tutor-facing page is added, link them there rather than in `SHEETS`.

## Decisions already made — don't relitigate without reason

- **No Jekyll.** The pages are finished HTML; Jekyll would wrap them in a theme and hide underscore paths. `.nojekyll` is committed.
- **Answers ship as one booklet per topic**, not one key per paper. Five files per topic instead of nine, and marking usually means flipping between papers anyway.
- **Papers are per topic page, not per subject.** Physics has two topics and therefore eight papers.
- **The heating curve uses true energy proportions**, which makes the boiling plateau 73% of the graph. That looks lopsided and is the point — do not "fix" it.
- **Self-marking over auto-marking** for written answers. He types an answer, opens the scheme, awards himself 0–3. Immediate auto-marking would let him skip the writing.
- **Staged hints, never a single reveal.** Three escalating hints before the full solution.
