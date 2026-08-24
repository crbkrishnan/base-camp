# Adding `indices.html` to the repo

Two files to drop in, then one command.

## 1. Place the files

```
indices.html                 → repo root, next to index.html
tools/register_topic.py      → tools/
```

## 2. Register it in the hub

```bash
python3 tools/register_topic.py indices.html
node tools/smoke.js
```

That's it. The script reads the `<script type="application/json" id="hub-card">`
manifest that `indices.html` carries in its own `<head>`, and inserts the matching
entry into the `TOPICS` array in `index.html`.

Expected output:

```
added "indices" in TOPICS (maths, ready) — 6 ready topics now listed
now run: node tools/smoke.js
```

and then every page reporting `ok`, with `index.html` showing one more card than before.

## Why a script rather than a hand edit

Editing the `TOPICS` array by hand is what produced the blank homepage earlier in this
project: a splice matched the wrong `];` and silently deleted the two arrays that followed
it. The file still parsed, so a syntax check passed, and every render function threw at
runtime.

`register_topic.py` locates the array by brace matching that understands quoted strings,
so it cannot run past the end of the array. It is also idempotent — run it twice and the
second run updates the entry instead of adding a duplicate. If a placeholder entry with the
same `id` already exists (`status:'planned'` or `'next'`), it is replaced in place.

It refuses to write at all if:

- the page has no `hub-card` manifest
- the manifest is not valid JSON
- `subject` is not one of maths / physics / biology / chemistry
- `status` is not one of ready / next / planned
- `file` points at something not in the repo root
- **the manifest `id` disagrees with the `var ID='…'` in the page's hub bridge** — the
  single easiest thing to get wrong, and it fails silently in the browser: the card renders
  but its progress bar never fills

## For every future topic page

Add a manifest block before `</head>`, then the same one command works:

```html
<script type="application/json" id="hub-card">
{
  "id": "ratio",
  "file": "ratio.html",
  "subject": "maths",
  "status": "ready",
  "title": "…",
  "sub": "…",
  "blurb": "One or two sentences on what the page actually does.",
  "meta": ["30 marks", "6 lessons", "live tool name"]
}
</script>
```

`id` must equal the `ID` in the page's hub bridge and the `KEY` prefix
(`ratio` → `ratio-progress-v1`). Worth adding a line to `docs/ADDING-A-TOPIC.md`
pointing at this script, so the next session finds it.
