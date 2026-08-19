# Base Camp — Grade 7 IGCSE study app

Four files, one folder, no build step, no server-side code.

```
index.html        the hub  — climb ladder, topic library, practice sheets, weekly puzzle
fdp.html          Maths    — fractions, decimals, percentages
moments.html      Physics  — the turning effect
respiration.html  Biology  — gas exchange in humans
sheets/           (create this) PDFs you want students to download
```

## Getting it online

Keep all four HTML files in the same folder — the links between them are relative.

**GitHub Pages (free, recommended)**
1. Create a repository, upload the four files to the root.
2. Settings → Pages → Source: `main` branch, `/ (root)`.
3. The site appears at `https://<username>.github.io/<repo>/` within a minute or two.

**Netlify Drop** — drag the folder onto `app.netlify.com/drop`. Instant URL, no account needed for the first deploy.

**Local testing** — `python3 -m http.server` inside the folder, then open `http://localhost:8000`. Opening the files directly by double-clicking works in Chrome and Firefox but progress saving is unreliable in Safari, so serve it if you can.

## How progress works

Each topic page saves its own answers, marks and finished lessons in the browser, and also writes a one-line summary into a shared record (`hub-progress-v1`). The hub reads that record to draw the climb ladder and the per-topic progress bars.

Consequences worth knowing:
- Progress is per browser, per device. It does not follow a student to another machine, and there is no login. That is deliberate — no accounts, no data collected.
- Clearing browser data wipes it. So does a different browser profile.
- The hub's own reset button clears the dashboard and puzzle record only. Answers inside a topic page are reset from that page's own reset button.
- If you ever want progress to sync across devices, that needs a real backend — worth doing only if the student count grows past a handful.

## Adding a new topic page

At the top of the `<script>` block in `index.html` there is a `TOPICS` array. Each entry looks like this:

```js
{id:'particles', file:'particles.html', subject:'chemistry', status:'ready',
 title:'The Particle Model', sub:'States of matter, changes of state',
 blurb:'One or two sentences on what the page actually does.',
 meta:['30 marks','6 lessons','live simulator']},
```

- `status` is `'ready'` (renders a live card with a progress bar), `'next'`, or `'planned'`.
- `subject` must be one of `maths`, `physics`, `biology`, `chemistry`.
- `id` must match the `id` used in the topic page's own reporter script, or the progress bar stays empty.

Every new topic page needs the same two bridge scripts the existing three carry — search any of them for `hub bridge (1/2)` and `hub bridge (2/2)`, copy both blocks across, and change `ID`, `SUBJECT` and `TITLE` in the second one.

## Adding a practice sheet

Create a `sheets/` folder, drop the PDF in, then add a row to the `SHEETS` array in `index.html`:

```js
{title:'Squares, cubes and roots', subject:'maths',
 note:'No-calculator drill sheet with ruled working space.',
 file:'sheets/squares-cubes-roots.pdf'},
```

Leave `file:null` for anything you only hand out on paper — the card then reads "In class · paper only" instead of showing a download button that goes nowhere.

## The puzzle rotation

`PUZZLES` in `index.html` holds six puzzles, each with a nudge and a full explanation. The hub shows one per calendar week and cycles automatically; "Another one" steps through the rest. Add more by appending to the array — the rotation adjusts itself to the new length.
