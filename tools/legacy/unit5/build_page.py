#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off scaffolding that assembled mixtures.html, separating.html and
solutions.html from particles.html plus a content module each.

Like the rest of tools/legacy/, this ran ONCE. The three pages are now
hand-maintained — do not re-run this over a page you have since edited,
or you will silently revert it (see CLAUDE.md, "Source of truth").

    python3 tools/legacy/unit5/build_page.py mixtures

Pieces are located by unique text anchors, never by index (CLAUDE.md #2).
"""
import io, os, re, sys, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)


def between(src, a, b, include_a=False, include_b=False):
    i = src.index(a)
    j = src.index(b, i + len(a))
    s = i if include_a else i + len(a)
    e = j + len(b) if include_b else j
    return src[s:e]


def build(name):
    mod = importlib.import_module(name)
    tpl = io.open(os.path.join(ROOT, 'particles.html'), encoding='utf-8').read()

    css = between(tpl, '<style>', '</style>')
    # swap the :root block for the page's own colours
    root_old = between(css, ':root{', '}', include_a=True, include_b=True)
    css = css.replace(root_old, mod.ROOT_CSS, 1)
    # drop particles' trailing overrides (nav tint + state colour classes) and add the page's own
    tail_old = between(css, 'nav.jump{background:rgba(237,234,227,.93)}', '.pill.gas{background:var(--gas-tint);color:var(--gas)}',
                       include_a=True, include_b=True)
    css = css.replace(tail_old, mod.EXTRA_CSS, 1)

    shim = between(tpl, '<script>\n/* ---- hub bridge (1/2)', '</script>\n</head>', include_a=True, include_b=True)
    engine = between(tpl, '/* ---------------- storage (safe wrapper) ---------------- */',
                     '/* ================= HERO 1: the particle box ================= */')
    engine = engine.replace("const KEY = 'particles-progress-v1';", "const KEY = '%s-progress-v1';" % mod.ID, 1)
    assert "'%s-progress-v1'" % mod.ID in engine
    # the data arrays live inside the engine slice; replace them with the page's own
    data_old = between(engine, '/* ---------------- videos ---------------- */', '/* ---------------- render videos ---------------- */')
    engine = engine.replace(data_old, mod.DATA_JS + '\n\n', 1)
    assert '/* ---------------- boot' not in engine  # boot is re-emitted after the tools

    bridge = between(tpl, '<script>\n/* ---- hub bridge (2/2)', '</script>\n</body>', include_a=True, include_b=True)
    bridge = bridge.replace("var ID='particles', SUBJECT='chemistry', TITLE='Small Bits, Always Moving'",
                            "var ID='%s', SUBJECT='chemistry', TITLE=%s" % (mod.ID, repr(mod.BRIDGE_TITLE)), 1)
    assert "var ID='%s'" % mod.ID in bridge

    head = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>%s</title>\n' % mod.TITLE +
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Newsreader:opsz,wght@6..72,400;6..72,600&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">\n'
            + mod.MANIFEST + '\n<style>' + css + '</style>\n\n' + shim + '\n')

    page = (head + '<body>\n<div class="wrap">\n\n' + mod.BODY_HTML +
            '\n\n</div>\n\n<script>\n\n' + engine +
            mod.TOOLS_JS +
            '\n\n/* ---------------- boot ---------------- */\n(async function(){\n  await loadState();\n  restore();\n  boot();\n})();\n</script>\n\n'
            + bridge + '\n</html>\n')
    out = os.path.join(ROOT, mod.ID + '.html')
    io.open(out, 'w', encoding='utf-8').write(page)
    print('wrote', out, len(page), 'bytes')


if __name__ == '__main__':
    for n in sys.argv[1:]:
        build(n)
