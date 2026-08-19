# Base Camp

A static study site for one Grade 7 IGCSE student: five interactive topic pages, sixteen printable
test papers, and a hub that tracks progress across all of them.

**Working on this with Claude Code? Start at [CLAUDE.md](CLAUDE.md).**

## Run it locally

```
python3 -m http.server 8000     # then open http://localhost:8000
```

## Check it before committing

```
npm install
node tools/smoke.js
```

Loads every page in a real DOM, runs the scripts, and reports uncaught errors plus what rendered.
A syntax check is not sufficient — see CLAUDE.md.

## Rebuild the test papers

```
pip install -r requirements.txt
for f in tools/papers/*.py; do python3 "$f"; done
```

## Deploy

GitHub Pages, deploy from branch, root directory. `.nojekyll` is committed and must stay.
