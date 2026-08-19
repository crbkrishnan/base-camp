# Adding a topic page

Roughly a full session's work. Do not try to shortcut the interactive tools — they are the reason the pages get used twice.

## 1. Pick the closest existing page and copy it

| New topic is… | Copy |
|---|---|
| Maths | `fdp.html` |
| Physics | `speed.html` |
| Biology | `respiration.html` |
| Chemistry | `particles.html` |

Copying preserves the shared CSS, the question engine, the storage shim and both hub-bridge blocks. Write the new file from the copy; do not author one from scratch.

## 2. Change the identity

- `<title>`
- `:root` — the three semantic accent colours and their tints, then the `--fr/--de/--pc` aliases. Pick a paper colour close to its subject siblings but not identical.
- `nav.jump` background rgba must match the new `--paper`, or the sticky nav looks wrong on scroll.
- Masthead: eyebrow, `<h1>`, lede, `.target` box.
- **Both hub-bridge blocks**: in block 2/2 set `ID`, `SUBJECT`, `TITLE`. `ID` must match the `id` you add to `TOPICS` in `index.html`.
- The `KEY` constant: `'<topic>-progress-v1'`. Must be unique or two pages will overwrite each other's answers.

## 3. Build two interactive tools

One near the top, one after the lessons. This is the part that matters most and the part most easily fudged.

A good tool makes an abstraction physical and lets a wrong intuition fail visibly. Existing ones, for calibration:

- **Balance beam** (moments) — drag masses, moments recompute live
- **Converter grid** (fdp) — shade squares, see fraction/decimal/percentage move together
- **Particle box** (particles) — one temperature dial, 36 particles rearrange
- **Heating curve** (particles) — drawn with real energies, so the boiling plateau honestly occupies 73% of the graph
- **Journey machine** (speed) — a car on a road with its distance–time graph drawing underneath, simultaneously

Each tool needs a **"Set me a puzzle"** button that poses a task, checks the machine's actual state, and increments `S.puzzles` on success. Puzzles that ask the student to *reach a state* ("set the box to the state with a fixed volume but no fixed shape") beat multiple choice, because the machine does the marking.

Respect `prefers-reduced-motion`: if it is set, render a static frame instead of running `requestAnimationFrame`.

## 4. Six videos, six lessons

**Videos.** Web-search for each; never write a URL from memory. Good channels: FuseSchool, Cognito, Corbettmaths, Math Antics, Khan Academy, Freesciencelessons. Each entry needs `t`, `ch`, `url`, `why` (what this one adds that the others don't), and `task` — a specific written job. The task is the anti-passive mechanism and is not optional.

**Lessons.** Each has `t`, `len`, `body` (HTML), `demo` (an away-from-screen action), `cliff` (a question the next lesson answers). Six lessons that build, ending on a cliffhanger that sets up the hardest question.

## 5. Fifteen questions, thirty marks

Fixed: 5 MCQ × 1, 5 short × 2, 5 word × 3. Levels `warm-up`, `standard`, `trap`, `hard`. Q14 and Q15 are the hard pair.

- MCQ `why` explains the answer whether right or wrong, and names the trap.
- Short answers get a `scheme` array (one line per mark) and a `tip`.
- Word problems get staged `hints` (three, escalating, none giving the answer away) and a `sol` array. A fourth `sol` entry as a closing observation works well.
- Follow `docs/WRITING-PAPERS.md` for the mark-scheme conventions; they are the same here.

## 6. Five traps and the papers section

Traps are the specific wrong sentences students write. Name the sentence, say why it is wrong, give the correct version.

The `#papers` section lists Papers A–D with one-line descriptions. Those descriptions are a contract — the papers you generate later must match them. Each card is an `<a … download>` pointing into `sheets/`; until the PDFs exist the section stays out of the page, because a card that downloads nothing is worse than no card.

## 7. Register it in the hub

In `index.html`, find `TOPICS` and change the placeholder entry (or add one):

```js
{id:'ratio', file:'ratio.html', subject:'maths', status:'ready', papers:4,
 title:'…', sub:'…',
 blurb:'One or two sentences on what the page actually does.',
 meta:['30 marks','6 lessons','live tool name']},
```

`status` is `ready`, `next` or `planned`. `subject` must be one of `maths`, `physics`, `biology`, `chemistry`. **`id` must match the bridge `ID`** or the progress bar stays empty forever. `papers` is how many PDFs the page's `#papers` section links; it drives the hub's Practice sheets row, so leave it off until the papers actually exist.

Use `str_replace` on a unique anchor. Do not splice by string index — see `CLAUDE.md` non-negotiable 2.

## 8. Verify

```
node tools/smoke.js
```

Expect `ok` for every page, and for the new one `videos=6 lessons=6 qcards=15`. Then open it in a browser and actually use both tools, including the puzzle buttons, and reload to confirm progress persisted.

Finally re-run `node tools/smoke.js` after touching `index.html` — the hub is where breakage hides, because it renders from arrays and fails silently when one goes missing.
