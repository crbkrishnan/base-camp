#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off scaffolding that assembled the eight IOQM (Olympiad) pages from
integers.html plus one content module each (pages/<id>.py).

Like the rest of tools/legacy/, this ran ONCE. The pages are now
hand-maintained — do not re-run this over a page you have since edited,
or you will silently revert it (see CLAUDE.md, "Source of truth").

    python3 tools/legacy/ioqm/build_page.py ../../.. ioqm_divisors ioqm_remainders ...

Pieces are located by unique text anchors, never by index (CLAUDE.md #2).
"""
import io, os, sys, json, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'pages'))

PAPER = '#EBEDEF'           # every Olympiad page shares this paper colour
PAPER_RGBA = 'rgba(235,237,239,.93)'


def between(src, a, b, include_a=False, include_b=False):
    assert src.count(a) == 1, ('anchor not unique', a[:60], src.count(a))
    i = src.index(a)
    j = src.index(b, i + len(a))
    s = i if include_a else i + len(a)
    e = j + len(b) if include_b else j
    return src[s:e]


def root_css(m):
    a, at, b, bt, c, ct = m.COLOURS
    return (':root{\n  --ink:#1A1E22;\n  --ink-soft:#535B63;\n  --paper:%s;\n  --card:#FFFFFF;\n'
            '  --line:#D3D8DD;\n  --line-soft:#E2E6EA;\n'
            '  --pm:%s; --pm-tint:%s;\n  --ng:%s; --ng-tint:%s;\n  --rt:%s; --rt-tint:%s;\n'
            '  --fr:var(--pm); --fr-tint:var(--pm-tint);\n  --de:var(--ng); --de-tint:var(--ng-tint);\n'
            '  --pc:var(--rt); --pc-tint:var(--rt-tint);\n'
            '  --steel:#9AA2A9;\n  --steel-dark:#66707A;\n  --ok:#1B7F4B;\n  --ok-tint:#E6F3EC;\n'
            '  --no:#98241B;\n  --no-tint:#FBEAE8;\n'
            "  --display:'Bricolage Grotesque','Trebuchet MS',sans-serif;\n"
            "  --body:'Newsreader',Georgia,serif;\n"
            "  --mono:'JetBrains Mono',ui-monospace,Menlo,monospace;\n  --r:14px;\n}"
            % (PAPER, a, at, b, bt, c, ct))


def build(root, name):
    m = importlib.import_module(name)
    tpl = io.open(os.path.join(root, 'integers.html'), encoding='utf-8').read()

    css = between(tpl, '<style>', '</style>')
    css = css.replace(between(css, ':root{', '}', True, True), root_css(m), 1)
    css = css.replace('background:rgba(236,237,231,.93)', 'background:' + PAPER_RGBA, 1)
    assert PAPER_RGBA in css
    css = css.replace(between(css, '/* ---------- factor trees ---------- */', '/* ---------- videos ---------- */', True),
                      '/* ---------- this page\'s two machines ---------- */\n' + m.EXTRA_CSS + '\n\n', 1)
    css = css.replace('  #treeWrap{grid-template-columns:1fr}\n', '', 1)

    shim = between(tpl, '<script>\n/* ---- hub bridge (1/2)', '</script>\n</head>', True, True)
    backlink = between(tpl, '<a href="index.html"', '</a>', True, True)
    vids_lessons = between(tpl, '<!-- ============ VIDEOS ============ -->', '<!-- ============ HERO 2', True)
    vids_lessons = vids_lessons.replace('~45 min total', m.VIDEO_MIN, 1).replace('~35 min total', m.LESSON_MIN, 1)
    questions = between(tpl, '<!-- ============ QUESTIONS ============ -->', '<section id="traps">', True)
    footer = between(tpl, '<footer>', '</footer>', True, True)

    engine = between(tpl, '/* ---------------- storage (safe wrapper) ---------------- */',
                     '/* ---------------- number theory helpers ---------------- */', True)
    engine = engine.replace("const KEY = 'integers-progress-v1';", "const KEY = '%s-progress-v1';" % m.ID, 1)
    assert "'%s-progress-v1'" % m.ID in engine
    data_old = between(engine, '/* ---------------- videos ---------------- */', '/* ---------------- render videos ---------------- */', True)
    engine = engine.replace(data_old, m.DATA_JS.strip() + '\n\n', 1)

    bridge = between(tpl, '<script>\n/* ---- hub bridge (2/2)', '</script>\n</body>', True, True)
    old = "var ID='integers', SUBJECT='maths', TITLE='Every Number Breaks Down'"
    assert old in bridge
    bridge = bridge.replace(old, "var ID='%s', SUBJECT='olympiad', TITLE=%s" % (m.ID, json.dumps(m.SHORT_TITLE, ensure_ascii=False)), 1)

    card = dict(id=m.ID, file=m.ID + '.html', subject='olympiad', status='ready',
                title=m.SHORT_TITLE, sub=m.SUB, blurb=m.BLURB, meta=['30 marks', '6 lessons', m.META_TOOL])
    manifest = ('<script type="application/json" id="hub-card">\n'
                + json.dumps(card, indent=2, ensure_ascii=False) + '\n</script>\n')

    nav = '<nav class="jump" aria-label="Sections">\n' + ''.join(
        '  <a href="#%s">%s</a>\n' % (h, t) for h, t in m.NAV) + '</nav>\n'

    traps = ('<section id="traps">\n  <div class="shead"><h2>Five traps</h2><span class="tag">Read before any test</span></div>\n'
             '  <div class="traps">\n' + ''.join('    <div class="trap"><h4>%s</h4><p>%s</p></div>\n' % t for t in m.TRAPS)
             + '  </div>\n</section>\n')
    assert len(m.TRAPS) == 5

    mast = ('<header class="mast">\n  <div class="eyebrow">%s</div>\n  <h1>%s</h1>\n  <p class="lede">%s</p>\n\n'
            '  <div class="target">\n    <strong>The deal.</strong> %s\n  </div>\n\n' % (m.EYEBROW, m.H1, m.LEDE, m.TARGET)
            + between(tpl, '  <div class="strip">', '</header>', True, True) + '\n')

    head = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>%s — IOQM Olympiad Prep</title>\n' % m.SHORT_TITLE +
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Newsreader:opsz,wght@6..72,400;6..72,600&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">\n\n'
            + manifest + '\n<style>' + css + '</style>\n\n' + shim + '\n')

    body = ('<body>\n<div class="wrap">\n\n' + backlink + '\n\n\n' + mast + '\n' + nav + '\n'
            + '<!-- ============ HERO 1 ============ -->\n' + m.TOOL1_HTML.strip() + '\n\n'
            + vids_lessons + '<!-- ============ HERO 2 ============ -->\n' + m.TOOL2_HTML.strip() + '\n\n'
            + questions + traps + '\n' + footer + '\n\n</div>\n')

    page = (head + body + '\n<script>\n' + engine + m.TOOLS_JS.strip() +
            '\n\n/* ---------------- boot ---------------- */\n(async ()=>{\n  await loadState();\n  restore();\n'
            + ''.join('  %s;\n' % c for c in m.BOOT) + '})();\n</script>\n\n' + bridge + '\n</html>\n')
    out = os.path.join(root, m.ID + '.html')
    io.open(out, 'w', encoding='utf-8').write(page)
    print('wrote', out, len(page), 'bytes')


if __name__ == '__main__':
    root = os.path.abspath(sys.argv[1])
    for n in sys.argv[2:]:
        build(root, n)
