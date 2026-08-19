# Base Camp — Grade 7 IGCSE study site

A static site of interactive study pages and printable test papers, built by a tutor for **one student**: Grade 7 IGCSE, scoring around **10 out of 15**, smart but lazy. Every design decision follows from that. The site's job is to make him *do* things rather than read things.

Subjects: Maths, Physics, Biology, Chemistry.

## Read these before working

| If you are… | Read |
|---|---|
| adding a new topic page | `docs/ADDING-A-TOPIC.md` |
| writing test papers | `docs/WRITING-PAPERS.md` |
| writing any student-facing words | `docs/CONTENT-VOICE.md` |
| wondering why something is built this way | `docs/ARCHITECTURE.md` |
| wondering what's done and what's next | `docs/STATE.md` |

## Non-negotiables

1. **Verify by running, never by parsing.** `node --check` passes on a file with a deleted variable. That exact mistake shipped a blank homepage once — a splice deleted `SUBJECTS` and `BANDS`, the syntax check passed, and every render function threw at runtime. Always finish with:
   ```
   npm install          # first time only
   node tools/smoke.js  # loads every page in jsdom, runs the scripts, reports errors
   ```
   It must print `ok` for all six pages and show non-zero counts. Zero cards or zero questions means something threw.

2. **Never edit HTML with index-based string splicing.** Use `str_replace` on a unique, generously sized anchor, or a proper parser. The blank-homepage bug came from `h.index('];', start)` matching the end of a *later* array.

3. **Every page stays a single self-contained file.** No bundler, no npm runtime deps, no shared CSS or JS file. A student must be able to be sent one `.html` and have it work offline. Google Fonts is the only external request, and pages degrade acceptably without it.

4. **Never use `localStorage` directly in a page.** Use `window.storage`, which the shim provides. See `docs/ARCHITECTURE.md`.

5. **Marks are fixed at 30 per topic page and 30 per paper.** 15 questions per page (5 MCQ × 1, 5 short × 2, 5 word × 3). Assert the total in any generator; the existing ones do.

6. **Check arithmetic in code before it reaches a document.** Write a throwaway script that computes every answer, run it, read the output. Every number in every paper was verified this way. Do not typeset a number you have only worked out in your head.

7. **Verify external links exist.** Web-search for YouTube videos rather than recalling URLs. A dead video on a study page is worse than no video.

## Layout

```
index.html              the hub — climb ladder, topic cards, paper signposts, weekly puzzle
fdp.html                Maths     · fractions, decimals, percentages
moments.html            Physics   · the turning effect
speed.html              Physics   · speed, distance, time
respiration.html        Biology   · gas exchange
particles.html          Chemistry · the particle model
sheets/*.pdf            20 test papers + 5 mark schemes (generated)
.nojekyll               stops GitHub Pages hiding underscore paths
tools/
  smoke.js              runtime check — the one that matters
  paper_lib.py          PDF engine: layout, ruled space, mark schemes
  papers/*.py           one file per topic; content + answers live here
  legacy/               scaffolding used to generate particles.html and speed.html
docs/                   the guides listed above
```

## Source of truth

- **HTML pages are hand-maintained.** Edit them directly. `tools/legacy/` generated two of them once; do **not** re-run those scripts over a page you have since edited by hand, or you will silently revert it.
- **PDFs are build artifacts.** Never edit a PDF. Change the Python in `tools/papers/`, re-run it, commit both.

## Commands

```
python3 -m http.server 8000        # serve locally; open http://localhost:8000
python3 tools/papers/maths_fdp.py  # rebuild one topic's papers into sheets/
for f in tools/papers/*.py; do python3 "$f"; done   # rebuild all papers
node tools/smoke.js                # runtime check, run before every commit
```

Requires Python 3 with `reportlab` and `pypdf`, DejaVu fonts at `/usr/share/fonts/truetype/dejavu/`, and Node with `jsdom` (`npm install`).

## Deployment

GitHub Pages, Settings → Pages → deploy from branch, root. **Do not add Jekyll.** If a theme was ever selected, delete `_config.yml` and `index.md`; `index.md` competes with `index.html`.
