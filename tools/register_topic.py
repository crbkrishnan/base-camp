#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Register a topic page in the hub.

    python3 tools/register_topic.py indices.html

Reads the <script type="application/json" id="hub-card"> block that every topic
page carries, then inserts or updates the matching entry in the TOPICS array in
index.html. Safe to run twice — a second run replaces the entry rather than
adding a duplicate. Never splices by raw string index: the array is located by
brace matching that understands quoted strings, which is what the homepage
outage was caused by not doing.
"""
import io, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HUB = os.path.join(ROOT, 'index.html')


def die(msg):
    print('register_topic: ' + msg, file=sys.stderr)
    sys.exit(1)


def read_manifest(path):
    html = io.open(path, encoding='utf-8').read()
    m = re.search(r'<script[^>]*id="hub-card"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        die('%s has no <script id="hub-card"> manifest. Add one before the '
            'closing </head> tag — see docs/ADDING-A-TOPIC.md.' % path)
    try:
        card = json.loads(m.group(1))
    except ValueError as e:
        die('the hub-card manifest in %s is not valid JSON: %s' % (path, e))

    for key in ('id', 'file', 'subject', 'status', 'title', 'sub'):
        if key not in card:
            die('the manifest is missing "%s"' % key)
    if card['subject'] not in ('maths', 'physics', 'biology', 'chemistry'):
        die('subject must be maths, physics, biology or chemistry')
    if card['status'] not in ('ready', 'next', 'planned'):
        die('status must be ready, next or planned')

    # the page's own hub bridge must agree, or its progress bar stays empty
    bridge = re.search(r"var ID='([^']+)', SUBJECT='([^']+)'", html)
    if bridge and bridge.group(1) != card['id']:
        die('manifest id "%s" does not match the hub bridge ID "%s" in the page. '
            'They must be identical or the progress bar never fills.'
            % (card['id'], bridge.group(1)))
    return card


def scan_array(src, start):
    """Return (open_index, close_index) of the array literal beginning at `start`,
    skipping over anything inside quoted strings."""
    i, depth, quote = start, 0, None
    while i < len(src):
        c = src[i]
        if quote:
            if c == '\\':
                i += 2
                continue
            if c == quote:
                quote = None
        elif c in '\'"`':
            quote = c
        elif c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                return start, i
        i += 1
    die('could not find the end of the TOPICS array in index.html')


def scan_object(src, start):
    i, depth, quote = start, 0, None
    while i < len(src):
        c = src[i]
        if quote:
            if c == '\\':
                i += 2
                continue
            if c == quote:
                quote = None
        elif c in '\'"`':
            quote = c
        elif c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return start, i
        i += 1
    die('could not find the end of an entry in the TOPICS array')


def js_str(v):
    return "'" + v.replace('\\', '\\\\').replace("'", "\\'") + "'"


def render(card):
    parts = ["{id:%s, " % js_str(card['id'])]
    if card.get('file'):
        parts.append("file:%s, " % js_str(card['file']))
    parts.append("subject:%s, status:%s,\n  title:%s, sub:%s"
                 % (js_str(card['subject']), js_str(card['status']),
                    js_str(card['title']), js_str(card['sub'])))
    if card.get('blurb'):
        parts.append(",\n  blurb:%s" % js_str(card['blurb']))
    if card.get('meta'):
        parts.append(",\n  meta:[%s]" % ', '.join(js_str(m) for m in card['meta']))
    parts.append('}')
    return ''.join(parts)


def main():
    if len(sys.argv) != 2:
        die('usage: python3 tools/register_topic.py <topic-page.html>')
    page = sys.argv[1]
    if not os.path.isabs(page):
        page = os.path.join(ROOT, page)
    if not os.path.exists(page):
        die('no such file: ' + page)
    if not os.path.exists(HUB):
        die('index.html not found at ' + HUB)

    card = read_manifest(page)
    if card.get('file') and not os.path.exists(os.path.join(ROOT, card['file'])):
        die('manifest points at %s, which does not exist in the repo root' % card['file'])

    hub = io.open(HUB, encoding='utf-8').read()
    m = re.search(r'const\s+TOPICS\s*=\s*\[', hub)
    if not m:
        die('could not find "const TOPICS = [" in index.html')

    a_open, a_close = scan_array(hub, hub.index('[', m.start()))
    body = hub[a_open + 1:a_close]

    entry = render(card)
    hit = re.search(r"\{\s*id:\s*'%s'" % re.escape(card['id']), body)

    if hit:
        o_start, o_end = scan_object(body, body.index('{', hit.start()))
        new_body = body[:o_start] + entry + body[o_end + 1:]
        action = 'updated'
    else:
        new_body = '\n ' + entry + ',\n' + body.lstrip('\n')
        action = 'added'

    out = hub[:a_open + 1] + new_body + hub[a_close:]
    io.open(HUB, 'w', encoding='utf-8').write(out)

    ready = len(re.findall(r"status:\s*'ready'", new_body))
    print('%s "%s" in TOPICS (%s, %s) — %d ready topics now listed'
          % (action, card['id'], card['subject'], card['status'], ready))
    print('now run: node tools/smoke.js')


if __name__ == '__main__':
    main()
