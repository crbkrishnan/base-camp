#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared scaffolding for the study pages, taken from the three pages already
   in the series so the new ones are identical in behaviour and styling."""
import io, re, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
_fdp = io.open(os.path.join(ROOT, 'fdp.html'), encoding='utf-8').read()
BASE_CSS = re.search(r'<style>(.*?)</style>', _fdp, re.S).group(1)
# everything after the :root block is topic-neutral and gets reused as-is
SHARED_CSS = BASE_CSS[BASE_CSS.index('*{box-sizing'):]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;'
 '12..96,700;12..96,800&family=Newsreader:opsz,wght@6..72,400;6..72,600&'
 'family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">')

SHIM = r"""
<script>
/* ---- hub bridge (1/2): storage that works both inside Claude and on a plain web server ---- */
(function(){
  if(window.storage) return;
  var mem = {};
  var ls = null;
  try{ ls = window.localStorage; ls.setItem('__t','1'); ls.removeItem('__t'); }catch(e){ ls = null; }
  window.storage = {
    get: function(k){ var v = ls ? ls.getItem(k) : (k in mem ? mem[k] : null);
                      return Promise.resolve(v===null||v===undefined ? null : {key:k, value:v}); },
    set: function(k,v){ try{ ls ? ls.setItem(k,v) : (mem[k]=v); }catch(e){}
                        return Promise.resolve({key:k, value:v}); },
    delete: function(k){ try{ ls ? ls.removeItem(k) : delete mem[k]; }catch(e){}
                         return Promise.resolve({key:k, deleted:true}); },
    list: function(p){ p = p||''; var keys=[];
                       try{ var src = ls ? Object.keys(ls) : Object.keys(mem);
                            keys = src.filter(function(k){ return k.indexOf(p)===0; }); }catch(e){}
                       return Promise.resolve({keys:keys, prefix:p}); }
  };
})();
</script>"""

BACKLINK = ('<a href="index.html" style="display:inline-block;margin:22px 0 -20px;font-family:var(--mono);'
 'font-size:12px;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;color:var(--ink-soft);'
 'border:1px solid var(--line);border-radius:99px;padding:6px 14px;background:var(--card)">'
 '&larr;&nbsp; Base camp</a>')

def bridge(pid, subject, title):
    return (r"""
<script>
/* ---- hub bridge (2/2): mirror this page's progress strip into the hub ---- */
(function(){
  var ID='%s', SUBJECT='%s', TITLE='%s', HKEY='hub-progress-v1';
  function num(id){ var el=document.getElementById(id); if(!el) return 0;
                    var m=(el.textContent||'').match(/-?\d+/); return m?parseInt(m[0],10):0; }
  var last='';
  function report(){
    var row = { marks:num('s-marks'), marksTotal:30,
                lessons:num('s-lessons'), lessonsTotal:6,
                puzzles:num('s-puzzles'), subject:SUBJECT, title:TITLE, seen:Date.now() };
    var sig = row.marks+'|'+row.lessons+'|'+row.puzzles;
    if(sig===last) return; last=sig;
    window.storage.get(HKEY).then(function(r){
      var all={}; try{ all = r&&r.value ? JSON.parse(r.value) : {}; }catch(e){}
      all[ID]=row;
      return window.storage.set(HKEY, JSON.stringify(all));
    }).catch(function(){});
  }
  function start(){
    var el=document.getElementById('s-marks');
    if(!el){ return; }
    try{ new MutationObserver(report).observe(document.querySelector('.strip')||el,
          {childList:true, subtree:true, characterData:true}); }catch(e){}
    setInterval(report, 4000);
    window.addEventListener('pagehide', report);
    document.addEventListener('visibilitychange', function(){ if(document.hidden) report(); });
    setTimeout(report, 900);
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
</script>""" % (pid, subject, title))


# ---- the question / lesson / video engine, identical in behaviour to the other pages ----
ENGINE = r"""
/* ---------------- render videos ---------------- */
const videoList = document.getElementById('videoList');
VIDEOS.forEach((V,i)=>{
  const c = document.createElement('div');
  c.className = 'vid';
  c.innerHTML = `
    <div class="play">${i+1}</div>
    <div>
      <h3><a href="${V.url}" target="_blank" rel="noopener">${V.t}</a></h3>
      <div class="chan">${V.ch}</div>
      <p>${V.why}</p>
      <div class="task"><strong>Your job:</strong> ${V.task}</div>
    </div>`;
  videoList.appendChild(c);
});

/* ---------------- render lessons ---------------- */
const lessonList = document.getElementById('lessonList');
LESSONS.forEach((L,i)=>{
  const d = document.createElement('details');
  d.className = 'lesson';
  d.innerHTML = `
    <summary><span class="no">${i+1}</span><span class="ttl">${L.t}</span><span class="len">${L.len}</span></summary>
    <div class="lbody">
      ${L.body}
      <div class="kicker">Do this away from the screen</div>
      <div class="demo">${L.demo}</div>
      <div class="kicker">Before you move on</div>
      <div class="cliff">${L.cliff}</div>
      <label class="done"><input type="checkbox" data-lesson="${i}"> I've worked through this lesson</label>
    </div>`;
  lessonList.appendChild(d);
});

/* ---------------- render questions ---------------- */
const mcqList = document.getElementById('mcqList');
MCQS.forEach(Q=>{
  const c = document.createElement('div');
  c.className='qcard';
  c.innerHTML = `
    <div class="qhead"><span class="qn">Q${Q.n}</span><span class="lvl">${Q.lvl}</span><span class="mk">1 mark</span></div>
    <p class="qtext">${Q.q}</p>
    <div class="opts" data-mcq="${Q.n}">
      ${Q.o.map((o,j)=>`<button type="button" class="opt" data-i="${j}"><span class="k">${'ABCD'[j]}</span><span>${o}</span></button>`).join('')}
    </div>
    <div class="fb" id="fb${Q.n}"></div>`;
  mcqList.appendChild(c);
});

const shortList = document.getElementById('shortList');
SHORTS.forEach(Q=>{
  const c = document.createElement('div');
  c.className='qcard';
  c.innerHTML = `
    <div class="qhead"><span class="qn">Q${Q.n}</span><span class="lvl">${Q.lvl}</span><span class="mk">${Q.m} marks</span></div>
    <p class="qtext">${Q.q}</p>
    <textarea data-note="${Q.n}" placeholder="Your answer…" aria-label="Your answer to question ${Q.n}"></textarea>
    <div class="row"><button class="btn ghost" type="button" data-reveal="s${Q.n}">Show mark scheme</button></div>
    <div class="solbox" id="s${Q.n}" style="display:none">
      <ol>${Q.scheme.map(s=>`<li>${s}</li>`).join('')}</ol>
      <p class="tipline">${Q.tip}</p>
    </div>
    ${markRow(Q.n,Q.m)}`;
  shortList.appendChild(c);
});

const wordList = document.getElementById('wordList');
WORDS.forEach(Q=>{
  const c = document.createElement('div');
  c.className='qcard';
  c.innerHTML = `
    <div class="qhead"><span class="qn">Q${Q.n}</span><span class="lvl${Q.lvl==='hard'?' hard':''}">${Q.lvl}</span><span class="mk">${Q.m} marks</span></div>
    <p class="qtext">${Q.q}</p>
    <textarea data-note="${Q.n}" placeholder="Your working…" aria-label="Your working for question ${Q.n}"></textarea>
    <div class="row">
      <button class="btn ghost" type="button" data-hint="${Q.n}">Give me a hint</button>
      <button class="btn ghost" type="button" data-reveal="w${Q.n}">Show full solution</button>
    </div>
    <div id="h${Q.n}"></div>
    <div class="solbox" id="w${Q.n}" style="display:none">
      <ol>${Q.sol.map(s=>`<li>${s}</li>`).join('')}</ol>
    </div>
    ${markRow(Q.n,Q.m)}`;
  wordList.appendChild(c);
});

function markRow(n,m){
  let b='';
  for(let i=0;i<=m;i++) b += `<button class="mbtn" type="button" data-mark="${n}" data-v="${i}">${i}</button>`;
  return `<div class="selfmark"><span class="q">I scored</span>${b}<span class="q">out of ${m}</span></div>`;
}

/* ---------------- interactions ---------------- */
document.addEventListener('click', e=>{
  const opt = e.target.closest('.opt');
  if(opt && !opt.disabled){
    const n = +opt.closest('.opts').dataset.mcq;
    answerMcq(n, +opt.dataset.i);
    S.mcq[n] = +opt.dataset.i;
    save(); refresh(); return;
  }
  const rev = e.target.closest('[data-reveal]');
  if(rev){ document.getElementById(rev.dataset.reveal).style.display='block'; rev.remove(); return; }

  const hb = e.target.closest('[data-hint]');
  if(hb){
    const n = +hb.dataset.hint;
    const Q = WORDS.find(x=>x.n===n);
    const host = document.getElementById('h'+n);
    const shown = host.children.length;
    if(shown < Q.hints.length){
      const d=document.createElement('div');
      d.className='hintbox';
      d.innerHTML = `<strong>Hint ${shown+1}.</strong> ${Q.hints[shown]}`;
      host.appendChild(d);
      if(host.children.length===Q.hints.length) hb.textContent='No hints left';
    }
    return;
  }
  const mb = e.target.closest('[data-mark]');
  if(mb){
    const n = mb.dataset.mark, v = +mb.dataset.v;
    S.marks[n] = v;
    mb.parentElement.querySelectorAll('.mbtn').forEach(b=>b.classList.toggle('sel', +b.dataset.v===v));
    save(); refresh(); return;
  }
});

function answerMcq(n, i){
  const Q = MCQS.find(x=>x.n===n);
  const box = document.querySelector(`.opts[data-mcq="${n}"]`);
  if(!box) return;
  box.querySelectorAll('.opt').forEach(b=>{
    b.disabled = true;
    if(+b.dataset.i === Q.a) b.classList.add('right');
    else if(+b.dataset.i === i) b.classList.add('wrong');
  });
  const fb = document.getElementById('fb'+n);
  fb.className = 'fb on ' + (i===Q.a ? 'good':'bad');
  fb.innerHTML = (i===Q.a ? '<strong>Correct.</strong> ' : '<strong>Not this time.</strong> ') + Q.why;
}

document.addEventListener('change', e=>{
  const cb = e.target.closest('[data-lesson]');
  if(cb){ S.lessons[cb.dataset.lesson] = cb.checked; save(); refresh(); }
});
document.addEventListener('input', e=>{
  const ta = e.target.closest('[data-note]');
  if(ta){ S.notes[ta.dataset.note] = ta.value; save(); }
});

document.getElementById('resetBtn').addEventListener('click', async ()=>{
  if(!confirm('Clear every answer, mark and finished lesson on this page?')) return;
  S = { lessons:{}, mcq:{}, marks:{}, notes:{}, puzzles:0 };
  try{ await window.storage.delete(KEY); }catch(e){}
  location.reload();
});

/* ---------------- progress ---------------- */
function refresh(){
  let marks = 0;
  MCQS.forEach(Q=>{ if(S.mcq[Q.n]===Q.a) marks += 1; });
  [...SHORTS,...WORDS].forEach(Q=>{ if(typeof S.marks[Q.n]==='number') marks += S.marks[Q.n]; });
  const lessons = Object.values(S.lessons).filter(Boolean).length;
  const small = 'font-size:15px;color:var(--ink-soft)';
  document.getElementById('s-marks').innerHTML = marks + `<span style="${small}">/30</span>`;
  document.getElementById('s-lessons').innerHTML = lessons + `<span style="${small}">/6</span>`;
  document.getElementById('s-puzzles').textContent = S.puzzles||0;
  document.getElementById('bar-marks').style.width = (marks/30*100)+'%';
  document.getElementById('bar-lessons').style.width = (lessons/6*100)+'%';
  document.getElementById('bar-puzzles').style.width = Math.min(100,(S.puzzles||0)*10)+'%';
}

function restore(){
  Object.keys(S.lessons).forEach(i=>{
    const cb = document.querySelector(`[data-lesson="${i}"]`);
    if(cb) cb.checked = !!S.lessons[i];
  });
  Object.keys(S.mcq).forEach(n=>{ if(MCQS.find(x=>x.n==n)) answerMcq(+n, S.mcq[n]); });
  Object.keys(S.marks).forEach(n=>{
    const btn = document.querySelector(`[data-mark="${n}"][data-v="${S.marks[n]}"]`);
    if(btn) btn.classList.add('sel');
  });
  Object.keys(S.notes).forEach(n=>{
    const ta = document.querySelector(`[data-note="${n}"]`);
    if(ta) ta.value = S.notes[n];
  });
  refresh();
}
"""

STATE_JS = r"""
/* ---------------- storage (safe wrapper) ---------------- */
const KEY = '%s';
let S = { lessons:{}, mcq:{}, marks:{}, notes:{}, puzzles:0 };
let saveTimer = null;
async function loadState(){
  try{
    const r = await window.storage.get(KEY);
    if(r && r.value) S = Object.assign(S, JSON.parse(r.value));
  }catch(e){}
}
function save(){
  clearTimeout(saveTimer);
  saveTimer = setTimeout(async ()=>{
    try{ await window.storage.set(KEY, JSON.stringify(S)); }catch(e){}
  }, 350);
}
"""

QUESTION_SECTIONS = """
<section id="quick">
  <div class="shead"><h2>Quick checks</h2><span class="tag">Q1–Q5 · 5 marks</span></div>
  <p class="snote">One try each, and the feedback tells you why. %s These are the five marks you should never drop.</p>
  <div id="mcqList"></div>
</section>

<section id="short">
  <div class="shead"><h2>Short answers</h2><span class="tag">Q6–Q10 · 10 marks</span></div>
  <p class="snote">Write your answer first, <em>then</em> open the mark scheme and mark yourself honestly. Marking your own work is where the improvement actually happens.</p>
  <div id="shortList"></div>
</section>

<section id="word">
  <div class="shead"><h2>Word problems</h2><span class="tag">Q11–Q15 · 15 marks</span></div>
  <p class="snote">Stuck? Take one hint, not the whole solution. A hint costs you nothing; reading the answer costs you the question. Q14 and Q15 are the two that separate a 21 from a 26.</p>
  <div id="wordList"></div>
</section>
"""

FOOTER = """
<footer>
  <span>Your answers, marks and finished lessons are saved on this device.</span>
  <button class="btn ghost" type="button" id="resetBtn" style="margin-left:auto">Reset my progress</button>
</footer>
"""

def page(title, root_css, extra_css, mast, nav, heroes, question_note,
         traps, papers, data_js, tools_js, key, pid, subject, hubtitle):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
%s
<style>
%s
%s
%s
</style>
%s
</head>
<body>
<div class="wrap">

%s

%s

%s

%s

%s

%s

%s

%s

</div>

<script>
%s

%s

%s

%s

/* ---------------- boot ---------------- */
(async function(){
  await loadState();
  restore();
  boot();
})();
</script>
%s
</body>
</html>
""" % (title, FONTS, root_css, SHARED_CSS, extra_css, SHIM,
       BACKLINK, mast, nav, heroes, QUESTION_SECTIONS % question_note, traps, papers, FOOTER,
       STATE_JS % key, data_js, ENGINE, tools_js, bridge(pid, subject, hubtitle))
