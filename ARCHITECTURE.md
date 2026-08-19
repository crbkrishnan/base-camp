# Architecture

No framework, no build step, no backend. Six HTML files that link to each other by relative path, plus generated PDFs. That is the whole system, and the constraint is deliberate: a student can be emailed a single file and it still works.

## Storage: why `window.storage` and not `localStorage`

The first three pages were authored inside Claude's artifact environment, which provides an async `window.storage` API. Served from an ordinary web server that object does not exist, so the pages would have silently stopped saving.

Every page therefore carries a shim in `<head>`, marked `hub bridge (1/2)`, which defines `window.storage` **only if it is absent**, backed by `localStorage`, with an in-memory fallback when even that is blocked (Safari on `file://`). It is promise-based to match the original API.

**Consequence for you: page code must call `window.storage.get/set/delete`, never `localStorage` directly.** Doing otherwise breaks the artifact environment and skips the in-memory fallback.

Keys in use:

| Key | Written by | Holds |
|---|---|---|
| `fdp-progress-v1` | fdp.html | `{lessons, mcq, marks, notes, puzzles}` |
| `moments-progress-v1` | moments.html | same shape |
| `speed-progress-v1` | speed.html | same shape |
| `respiration-progress-v1` | respiration.html | same shape |
| `particles-progress-v1` | particles.html | same shape |
| `hub-progress-v1` | every topic page | per-topic summary the hub reads |
| `hub-state-v1` | index.html | puzzle record, subject filter |

Progress is per-browser, per-device. No accounts, no sync, nothing collected. Adding sync would need a backend and is not worth it for one student.

## The hub bridge

Each topic page ends with a second block marked `hub bridge (2/2)`. Rather than duplicating the mark-counting logic, it **reads the page's own rendered progress strip** — `#s-marks`, `#s-lessons`, `#s-puzzles` — via a `MutationObserver` plus a slow interval, and writes a summary row into `hub-progress-v1`:

```js
{ marks, marksTotal:30, lessons, lessonsTotal:6, puzzles, subject, title, seen }
```

The hub reads that map to draw the climb ladder and per-topic progress bars. So a new page gets hub integration for free **provided it has a progress strip with those three element ids**. Change the ids and the hub goes quiet without erroring — that is the failure mode to watch for.

## Anatomy of a topic page

Every page follows the same order, and the shared CSS class names are identical across all five:

1. Back-link pill to `index.html`
2. `header.mast` — eyebrow, title, lede, `.target` box stating the 21/26 goal, `.strip` progress stats
3. `nav.jump` — sticky section links
4. **Hero tool 1** — the signature interactive, in a `.panel`
5. `#videos` — six curated videos, each with a written task
6. `#lessons` — six `<details>` accordions
7. **Hero tool 2** — second interactive
8. `#quick` (5 MCQ), `#short` (5 × 2 marks), `#word` (5 × 3 marks)
9. `#traps` — five exam traps
10. `#papers` — the four printed papers
11. Footer with reset

Data lives in `VIDEOS`, `LESSONS`, `MCQS`, `SHORTS`, `WORDS` arrays; a shared engine renders them and handles self-marking, staged hints and persistence. Copy the engine verbatim from an existing page.

`moments.html` is the exception: it predates the video format and has no `#videos` section. Worth filling in.

## Colour convention

Each page defines semantically-named accents, then aliases them to the generic names the shared CSS uses:

```css
--sol:#2B4E9B;  --liq:#0E7C6B;  --gas:#B4560B;
--fr:var(--sol); --de:var(--liq); --pc:var(--gas);
```

This lets the stylesheet be copied unchanged between pages while the content uses meaningful names. A concept keeps one colour for the whole page — anticlockwise is always teal, gas is always amber — so colour carries meaning rather than decoration.

## The hub

`index.html` is driven by four arrays near the top of its script: `TOPICS`, `SHEETS`, `SUBJECTS`, `BANDS`, plus `PUZZLES`. Adding content means adding an entry, not editing render code.

The signature element is the **climb ladder**: five bands from Cold start to Top band, with a marker on the band the student's banked marks put him in, and a line computing how many more marks reach the next rung. It reads only topics that have actually been opened, so an untouched library does not display a demoralising 0%.

## Accessibility and robustness floor

Keep these when adding anything: visible `:focus-visible` outlines, `prefers-reduced-motion` respected (animation loops must check it), responsive down to ~360px, `aria-label` on sliders and canvas-like SVGs, and no reliance on colour alone.
