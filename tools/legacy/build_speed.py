#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from build_lib import page

ROOT = """:root{
  --ink:#131F2B;
  --ink-soft:#4E6072;
  --paper:#E7ECF0;
  --card:#FFFFFF;
  --line:#CFD9E1;
  --line-soft:#E4EAEF;
  --dist:#0B6E75;       /* distance — always teal */
  --dist-tint:#E4F2F2;
  --time:#4A4E9B;       /* time — always indigo */
  --time-tint:#EBECF7;
  --spd:#C2560E;        /* speed — always amber */
  --spd-tint:#FDF0E6;
  --fr:var(--dist); --fr-tint:var(--dist-tint);
  --de:var(--time); --de-tint:var(--time-tint);
  --pc:var(--spd);  --pc-tint:var(--spd-tint);
  --steel:#9AA7B1;
  --steel-dark:#6E7E8B;
  --ok:#1B7F4B;
  --ok-tint:#E6F3EC;
  --no:#A62A21;
  --no-tint:#FBEAE8;
  --display:'Bricolage Grotesque','Trebuchet MS',sans-serif;
  --body:'Newsreader',Georgia,serif;
  --mono:'JetBrains Mono',ui-monospace,Menlo,monospace;
  --r:14px;
}
"""

EXTRA = """
nav.jump{background:rgba(231,236,240,.93)}
.dtxt{color:var(--dist);font-weight:700}
.ttxt{color:var(--time);font-weight:700}
.stxt{color:var(--spd);font-weight:700}
.pill.dis{background:var(--dist-tint);color:var(--dist)}
.pill.tim{background:var(--time-tint);color:var(--time)}
.pill.spe{background:var(--spd-tint);color:var(--spd)}
.solve{display:grid;grid-template-columns:auto 1fr;gap:18px;padding:16px 18px;align-items:center}
.solve .tri{width:210px;height:auto}
.solve .fields{display:grid;gap:9px}
.frow{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.frow label{font-family:var(--display);font-size:13px;color:var(--ink-soft);min-width:74px}
.frow input[type=number]{width:120px}
select{font-family:var(--mono);font-size:14px;padding:7px 9px;border:1px solid var(--line);
  border-radius:9px;background:var(--paper);color:var(--ink)}
.working{font-family:var(--mono);font-size:14.5px;background:var(--paper);padding:10px 13px;
  border-radius:9px;line-height:1.9;overflow-x:auto}
.working b{color:var(--spd)}
@media (max-width:600px){ .solve{grid-template-columns:1fr} .solve .tri{margin:0 auto} }
"""

MAST = """<header class="mast">
  <div class="eyebrow">IGCSE Physics · Grade 7 · Motion</div>
  <h1>How <em>Fast</em>,<br>How <i>Far</i>, How <b>Long</b></h1>
  <p class="lede">Three quantities, one relationship, and almost every dropped mark in the topic comes from the same two places: mixing up the units, or averaging speeds that should never have been averaged. The physics here is easy. The carelessness is what costs you.</p>

  <div class="target">
    <strong>The deal.</strong> You've been landing around <span class="num">10 out of 15</span>. This page is out of <span class="num">30</span>, so the honest target is <span class="num">21</span> on the first pass and <span class="num">26</span> on the second. Write the formula, substitute the numbers, then answer with a unit — every single time, even when you can do it in your head. That habit alone is worth several marks a paper.
  </div>

  <div class="strip">
    <div class="stat"><b class="num" id="s-marks">0<span style="font-size:15px;color:var(--ink-soft)">/30</span></b><span>marks banked</span><div class="bar"><i id="bar-marks"></i></div></div>
    <div class="stat"><b class="num" id="s-lessons">0<span style="font-size:15px;color:var(--ink-soft)">/6</span></b><span>lessons finished</span><div class="bar"><i id="bar-lessons"></i></div></div>
    <div class="stat"><b class="num" id="s-puzzles">0</b><span>machine puzzles solved</span><div class="bar"><i id="bar-puzzles"></i></div></div>
  </div>
</header>"""

NAV = """<nav class="jump" aria-label="Sections">
  <a href="#journey">Journey machine</a>
  <a href="#videos">6 videos</a>
  <a href="#lessons">6 lessons</a>
  <a href="#solver">The solver</a>
  <a href="#quick">Quick checks</a>
  <a href="#short">Short answers</a>
  <a href="#word">Word problems</a>
  <a href="#traps">Exam traps</a>
  <a href="#papers">Test papers</a>
</nav>"""

HEROES = """
<!-- ============ HERO 1: THE JOURNEY MACHINE ============ -->
<section id="journey">
  <div class="panel">
    <div class="panel-top">
      <h2>The journey machine</h2>
      <p>The road on top, the distance–time graph underneath, both running at the same moment. Drive it yourself with the slider, or press one of the four journeys and watch which shape of line it draws. The point of this machine is to stop the graph being an abstract picture and make it a recording of something that actually happened.</p>
    </div>

    <svg class="stage" id="jstage" viewBox="0 0 700 330" role="img" aria-label="A road with a moving car above a distance-time graph that draws itself">
      <rect x="60" y="34" width="600" height="30" rx="5" fill="var(--paper)" stroke="var(--line)"/>
      <g id="ticks"></g>
      <rect id="car" x="60" y="39" width="26" height="20" rx="5" fill="var(--spd)"/>
      <text x="60" y="24" font-family="var(--mono)" font-size="11" fill="var(--ink-soft)">THE ROAD · 0 to 600 m</text>

      <line x1="60" y1="110" x2="60" y2="300" stroke="var(--line)" stroke-width="2"/>
      <line x1="60" y1="300" x2="668" y2="300" stroke="var(--line)" stroke-width="2"/>
      <g id="glines"></g>
      <polyline id="dtline" fill="none" stroke="var(--dist)" stroke-width="4" stroke-linejoin="round" points=""/>
      <circle id="dtdot" cx="60" cy="300" r="6" fill="var(--dist)" stroke="#fff" stroke-width="2"/>
      <text x="20" y="116" font-family="var(--mono)" font-size="11" fill="var(--ink-soft)">m</text>
      <text x="600" y="322" font-family="var(--mono)" font-size="11" fill="var(--ink-soft)">time (s)</text>
    </svg>

    <div class="ctrl">
      <label for="spd">Your speed</label>
      <input id="spd" type="range" min="0" max="20" value="10" step="1" aria-label="Speed in metres per second">
      <span class="num" id="spdval" style="min-width:70px;text-align:right">10 m/s</span>
      <button class="btn" type="button" id="runBtn">Start</button>
      <button class="btn ghost small" type="button" id="resetJ">Reset</button>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label>Or run one</label>
      <button class="btn ghost small" type="button" data-journey="steady">Steady all the way</button>
      <button class="btn ghost small" type="button" data-journey="slow">Fast, then slower</button>
      <button class="btn ghost small" type="button" data-journey="stop">Stop for a while</button>
      <button class="btn ghost small" type="button" data-journey="back">There and back</button>
    </div>

    <div class="rows">
      <div class="cell d"><div class="lab">Time</div><div class="val" id="j-t">0 s</div><div class="sub">since you set off</div></div>
      <div class="cell f"><div class="lab">Distance</div><div class="val" id="j-d">0 m</div><div class="sub" id="j-ds">from the start</div></div>
      <div class="cell p"><div class="lab">Speed now</div><div class="val" id="j-v">0 m/s</div><div class="sub" id="j-vs">the gradient of the line</div></div>
      <div class="phasebar">
        <span class="pill dis" id="j-pill">Ready</span>
        <span id="j-note">Press Start. Watch the car and the line at the same time — the steeper the line, the faster the car.</span>
        <span class="push"><button class="btn ghost" type="button" id="jPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="jQuiz"></div>
    </div>
  </div>
</section>

<!-- ============ VIDEOS ============ -->
<section id="videos">
  <div class="shead"><h2>Watch these six, in this order</h2><span class="tag">~40 min total</span></div>
  <p class="snote">Each video comes with one small written job. Do the job, or the video was a screensaver with physics on it. Pause and write as you go — don't tell yourself you'll rewind at the end, because you won't.</p>
  <div id="videoList"></div>
</section>

<!-- ============ LESSONS ============ -->
<section id="lessons">
  <div class="shead"><h2>Six lessons</h2><span class="tag">~35 min total</span></div>
  <div id="lessonList"></div>
</section>

<!-- ============ HERO 2: THE SOLVER ============ -->
<section id="solver">
  <div class="panel">
    <div class="panel-top">
      <h2>The solver</h2>
      <p>Choose what you are looking for and the triangle covers it, leaving the arrangement you need. Then put the numbers in — with whatever units the question gave you — and watch the working line build itself. Copy that layout in the exam: formula, substitution, answer with a unit.</p>
    </div>

    <div class="solve">
      <svg class="tri" viewBox="0 0 220 190" role="img" aria-label="The speed, distance and time formula triangle">
        <path d="M110 12 L208 178 L12 178 Z" fill="none" stroke="var(--line)" stroke-width="2.5" stroke-linejoin="round"/>
        <line x1="47" y1="110" x2="173" y2="110" stroke="var(--line)" stroke-width="2.5"/>
        <line x1="110" y1="110" x2="110" y2="178" stroke="var(--line)" stroke-width="2.5"/>
        <text id="tri-d" x="110" y="86" text-anchor="middle" font-family="var(--display)" font-weight="700" font-size="26" fill="var(--dist)">d</text>
        <text id="tri-s" x="72" y="155" text-anchor="middle" font-family="var(--display)" font-weight="700" font-size="26" fill="var(--spd)">s</text>
        <text id="tri-t" x="150" y="155" text-anchor="middle" font-family="var(--display)" font-weight="700" font-size="26" fill="var(--time)">t</text>
        <rect id="tri-cover" x="0" y="0" width="0" height="0" fill="var(--ink)" opacity="0.86" rx="8"/>
      </svg>

      <div class="fields">
        <div class="frow">
          <label>I want</label>
          <button class="btn ghost small" type="button" data-find="s">Speed</button>
          <button class="btn ghost small" type="button" data-find="d">Distance</button>
          <button class="btn ghost small" type="button" data-find="t">Time</button>
        </div>
        <div class="frow" id="rowA">
          <label id="labA">Distance</label>
          <input id="inA" type="number" value="240" step="any" aria-label="First quantity">
          <select id="unA"></select>
        </div>
        <div class="frow" id="rowB">
          <label id="labB">Time</label>
          <input id="inB" type="number" value="30" step="any" aria-label="Second quantity">
          <select id="unB"></select>
        </div>
        <div class="working" id="work"></div>
      </div>
    </div>

    <div class="rows two">
      <div class="cell p"><div class="lab">Answer</div><div class="val" id="sv-main">8 m/s</div><div class="sub" id="sv-mains">in SI units</div></div>
      <div class="cell d"><div class="lab">Same thing, other unit</div><div class="val" id="sv-alt">28.8 km/h</div><div class="sub" id="sv-alts">×3.6 to go from m/s to km/h</div></div>
      <div class="phasebar">
        <span class="pill spe" id="sv-pill">Finding speed</span>
        <span id="sv-note">Change the units in the dropdowns and watch the working line convert them before it divides. That conversion is the step people skip.</span>
        <span class="push"><button class="btn ghost" type="button" id="svPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="svQuiz"></div>
    </div>
  </div>
</section>
"""

TRAPS = """
<section id="traps">
  <div class="shead"><h2>Five traps</h2><span class="tag">Read before any test</span></div>
  <div class="traps">
    <div class="trap"><h4>Averaging the speeds instead of the journey</h4><p>Half a journey at 4 m/s and half at 6 m/s does <strong>not</strong> average 5 m/s. You spend longer at the slow speed, so the slow speed counts for more. Average speed is always <span class="num">total distance ÷ total time</span> — work out both totals and divide once, at the end.</p></div>
    <div class="trap"><h4>Minutes pretending to be hours</h4><p><span class="num">30 km in 20 minutes</span> is not 1.5 km/h. Twenty minutes is 1/3 of an hour, so the answer is 90 km/h. Before you divide, look at the unit you have been asked for and convert the time to match it — minutes to hours means divide by 60, not by 100.</p></div>
    <div class="trap"><h4>A flat line means stopped, not gone</h4><p>On a distance–time graph a horizontal section means the distance from the start is not changing — the object is <strong>stationary</strong>. It has not disappeared, and it is not moving at a steady speed. Steady speed is a straight line that slopes.</p></div>
    <div class="trap"><h4>Reading the gradient in squares instead of units</h4><p>Gradient is <span class="num">change in distance ÷ change in time</span> read off the <em>axes</em>, not counted in grid squares. Always pick two points that sit exactly on gridlines, write down both coordinates, and subtract.</p></div>
    <div class="trap"><h4>An answer without a unit</h4><p><span class="num">20</span> is not an answer; <span class="num">20 m/s</span> is. And if the question gave kilometres and hours, the expected unit is almost certainly km/h. The unit is frequently the last mark of the question, and it is the cheapest mark on the whole paper.</p></div>
  </div>
</section>
"""

PAPERS = """
<section id="papers">
  <div class="shead"><h2>The four test papers</h2><span class="tag">30 marks each</span></div>
  <p class="snote">These are the printed papers that go with this page. Do them on paper, timed, with your phone in another room. Medium first; only move to the hard papers once you're clearing 21 on a medium one.</p>
  <div class="papers">
    <div class="paper"><span class="pn">A</span><span class="pt">Paper A — Medium</span><span class="num" style="color:var(--ink-soft);font-size:13px">35 min</span>
      <p class="pd">Straight substitution into the formula in all three directions, simple unit conversions, and reading speeds off a distance–time graph.</p></div>
    <div class="paper"><span class="pn">B</span><span class="pt">Paper B — Medium</span><span class="num" style="color:var(--ink-soft);font-size:13px">35 min</span>
      <p class="pd">Drawing a distance–time graph from a written journey, describing a journey from a graph in sentences, and two average-speed calculations.</p></div>
    <div class="paper"><span class="pn hard">C</span><span class="pt">Paper C — Hard</span><span class="num" style="color:var(--ink-soft);font-size:13px">45 min</span>
      <p class="pd">Two-part journeys, mixed units within one question, and the "what speed must the second half be" style of reverse problem.</p></div>
    <div class="paper"><span class="pn hard">D</span><span class="pt">Paper D — Hard</span><span class="num" style="color:var(--ink-soft);font-size:13px">45 min</span>
      <p class="pd">Multi-step problems where the method is hidden: overtaking, sound and light timing, and questions built to punish every trap listed above.</p></div>
  </div>
</section>
"""

DATA = r"""
/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"Speed, Distance, Time", ch:"Corbettmaths", url:"https://www.youtube.com/watch?v=dHVK7IeLGT8",
  why:"The relationship itself, with exam-shaped worked examples. Start here even if you think you already know it — watch how he lays the working out, because the layout is where the method marks live.",
  task:"Copy out one of his worked examples exactly as he writes it: formula line, substitution line, answer line with a unit. That is the layout you use for every question on this page."},

 {t:"Speed, Distance, Time — Alternative Approach", ch:"Corbettmaths", url:"https://www.youtube.com/watch?v=dOnpaBN5DAk",
  why:"The same content done a second way. Two routes to the same answer is genuinely useful — one of them will feel more natural to you, and having a spare method rescues you when you blank.",
  task:"Write one line saying which of the two approaches you are going to use in the exam, and why. Then stick to it."},

 {t:"Distance–Time Graphs", ch:"Corbettmaths", url:"https://www.youtube.com/watch?v=oxOiuqUfWKA",
  why:"How to read the graph: what the gradient means, what a flat section means, and how to answer the two standard exam questions about them.",
  task:"Sketch four small graphs from memory: steady, faster, stopped, coming back. Label each with one sentence describing the journey. Then check them against the journey machine above."},

 {t:"GCSE Physics — Distance–Time Graphs", ch:"Cognito", url:"https://www.youtube.com/watch?v=RM02SnuJ0MY",
  why:"The physics-department version, including calculating a speed directly from the gradient using the axes. Slightly beyond Grade 7 at the end, and that is fine.",
  task:"Pause when he calculates a gradient and do it yourself first, writing both coordinates before subtracting. Compare. Q12 uses exactly this skill."},

 {t:"Distance–Time Graphs (Travel Graphs)", ch:"GCSE Maths Tutor", url:"https://www.youtube.com/watch?v=C6S7QQn38XU",
  why:"Longer and slower, built around full exam questions rather than the idea. Watch this one when the questions below start biting.",
  task:"Do one of his questions on paper before he does it, then mark yourself against his working. Write down any step he took that you skipped."},

 {t:"Units of Speed — m/s and km/h", ch:"Khan Academy", url:"https://www.youtube.com/watch?v=q5PptXscgh0",
  why:"The conversion that quietly costs more marks than anything else in this topic, done properly rather than as a trick to memorise.",
  task:"Convert these four without a calculator and check with the solver: 72 km/h, 90 km/h, 15 m/s, 25 m/s. Write down the two rules you used, in your own words."}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"What speed actually means", len:"5 min",
  body:`<p><strong>Speed is distance covered in each unit of time.</strong> That is the whole definition, and it tells you the formula without memorising it — "metres per second" literally means metres divided by seconds.</p>
        <div class="eqline"><span class="stxt">speed</span> = <span class="dtxt">distance</span> ÷ <span class="ttxt">time</span></div>
        <p>Rearranged, the same relationship gives the other two:</p>
        <div class="eqline"><span class="dtxt">distance</span> = <span class="stxt">speed</span> × <span class="ttxt">time</span> &nbsp;&nbsp;·&nbsp;&nbsp; <span class="ttxt">time</span> = <span class="dtxt">distance</span> ÷ <span class="stxt">speed</span></div>
        <p>The triangle in the solver is a memory aid for those three, with <span class="dtxt">d</span> on top and <span class="stxt">s</span> × <span class="ttxt">t</span> underneath. Cover the one you want and the arrangement of the other two is your formula. It is a crutch, not a method — but a useful one under exam pressure.</p>
        <p><strong>The layout that earns method marks.</strong> Three lines, every time, even when the arithmetic is trivial:</p>
        <div class="eqline">speed = distance ÷ time<br>speed = 240 ÷ 30<br>speed = 8 m/s</div>
        <p>Why bother when you can do 240 ÷ 30 in your head? Because if you slip and write 9, a marker who can see a correct formula and a correct substitution can still award the method marks. An answer alone, if it is wrong, scores nothing at all.</p>`,
  demo:`<strong>Do this:</strong> time yourself walking the length of a room you have measured. Write out the three lines and get your walking speed in m/s. Most people walk at about 1.4 m/s.`,
  cliff:`You have a speed. But is it in m/s or km/h — and does the question care?`},

 {t:"Units, and the two conversions that cost marks", len:"6 min",
  body:`<p>The SI unit of speed is <strong>metres per second (m/s)</strong>. Journeys in real life are usually quoted in <strong>kilometres per hour (km/h)</strong>. Nearly every mark lost in this topic is lost between those two.</p>
        <p><strong>The rule.</strong> There are 1000 m in a km and 3600 s in an hour, and 3600 ÷ 1000 = 3.6. So:</p>
        <div class="eqline">m/s &#8594; km/h: <strong>× 3.6</strong> &nbsp;&nbsp;·&nbsp;&nbsp; km/h &#8594; m/s: <strong>÷ 3.6</strong></div>
        <p>Check it against something you know. A car at 20 m/s: 20 × 3.6 = 72 km/h, which is a sensible road speed. If your answer comes out at 7200 km/h or 5.5 km/h, you have gone the wrong way — and noticing that is a skill worth more than the conversion itself.</p>
        <p><strong>Time units are the second trap.</strong> Minutes are not decimal:</p>
        <ul>
          <li>30 minutes = 0.5 h &nbsp;·&nbsp; 20 minutes = 1/3 h ≈ 0.333 h &nbsp;·&nbsp; 45 minutes = 0.75 h</li>
          <li>1 h 30 min = 1.5 h, <strong>not 1.30 h</strong>. This one appears on every paper.</li>
          <li>To get hours from minutes, divide by 60. To get seconds from minutes, multiply by 60.</li>
        </ul>
        <p><strong>Match the units to the answer you want.</strong> If the question asks for km/h, put the distance in km and the time in hours <em>before</em> you divide. If it asks for m/s, convert to metres and seconds first. Convert at the start, not at the end — converting a final answer is where sign and factor errors creep in.</p>`,
  demo:`<strong>Do this:</strong> without a calculator, convert 90 km/h to m/s and 12 m/s to km/h. (25 m/s and 43.2 km/h.) Then check both in the solver.`,
  cliff:`A car does 60 km/h for an hour and 120 km/h for half an hour. Is its average speed 90 km/h?`},

 {t:"Average speed, and why you cannot average speeds", len:"7 min",
  body:`<p>A car almost never travels at one steady speed. <strong>Average speed</strong> is the single steady speed that would have covered the same journey in the same time:</p>
        <div class="eqline">average speed = <span class="dtxt">total distance</span> ÷ <span class="ttxt">total time</span></div>
        <p>The word <em>total</em> is doing all the work. Add up every kilometre travelled, add up every minute taken — <strong>including the time spent stopped</strong> — and divide once, at the end.</p>
        <p><strong>Why averaging the speeds fails.</strong> Take the cliffhanger from the last lesson: 60 km at 60 km/h takes 1 hour; 60 km at 120 km/h takes half an hour. Total distance 120 km, total time 1.5 h:</p>
        <div class="eqline">average = 120 ÷ 1.5 = <strong>80 km/h</strong>, not 90 km/h</div>
        <p>The two speeds average to 90, but the answer is 80, because the car spent <em>twice as long</em> going slowly. Slower speeds always take up more of the journey's time, so they always pull the average down harder than the fast ones pull it up. The average of the speeds and the average speed are two different quantities, and only one of them is ever the answer.</p>
        <p><strong>Instantaneous speed</strong> is the speed at one particular moment — what a speedometer shows. A journey with an average of 80 km/h may never actually have been at 80 km/h at any instant.</p>`,
  demo:`<strong>Do this:</strong> a runner does 100 m at 5 m/s, then walks 100 m at 1 m/s. Work out the average speed for the whole 200 m before reading on. (20 s + 100 s = 120 s, so 200 ÷ 120 = 1.67 m/s — nowhere near the 3 m/s you get by averaging the speeds.)`,
  cliff:`All of this is easier to see as a picture. What does a journey look like when you draw it?`},

 {t:"Reading a distance–time graph", len:"6 min",
  body:`<p>Time along the bottom, distance from the starting point up the side. Every feature of the line means something specific:</p>
        <table class="data">
          <tr><th>What the line does</th><th>What the object is doing</th></tr>
          <tr><td>Straight and sloping up</td><td>moving away at a steady speed</td></tr>
          <tr><td>Steeper</td><td>moving faster</td></tr>
          <tr><td>Horizontal (flat)</td><td>stationary — the distance is not changing</td></tr>
          <tr><td>Sloping down</td><td>coming back towards the start</td></tr>
          <tr><td>Curving upwards</td><td>speeding up</td></tr>
        </table>
        <p><strong>The gradient is the speed.</strong> Not "like" the speed — it <em>is</em> the speed, because gradient is the change in distance divided by the change in time, which is the definition of speed.</p>
        <div class="eqline">gradient = (d&#8322; − d&#8321;) ÷ (t&#8322; − t&#8321;)</div>
        <p>To calculate one properly: pick two points where the line crosses gridlines exactly, write down both pairs of coordinates, subtract, then divide. Read the values off the axis labels — counting squares is how people end up with an answer ten times too big.</p>
        <p><strong>Describing a journey in words</strong> is a standard question, and the mark scheme wants three things for each section: <em>what</em> it did, <em>how fast</em>, and <em>for how long</em>. "It went along, then it stopped, then it came back" scores badly. "It travelled 300 m away in the first 20 s, at 15 m/s, then stayed still for 5 s" scores well.</p>`,
  demo:`<strong>Do this:</strong> run "There and back" on the journey machine, then write three sentences describing that journey, with a number in every sentence. Check your numbers against the readouts.`,
  cliff:`Real exam questions rarely give you one clean journey. They give you two joined together.`},

 {t:"Two-part journeys, done in a table", len:"6 min",
  body:`<p>The most common hard question in this topic joins two or three legs together and asks for the average speed of the whole thing. It is the same calculation each time, and a small table stops you losing track:</p>
        <table class="data">
          <tr><th>Leg</th><th>Distance</th><th>Speed</th><th>Time</th></tr>
          <tr><td>1</td><td>60 km</td><td>60 km/h</td><td>1 h</td></tr>
          <tr><td>2</td><td>60 km</td><td>120 km/h</td><td>0.5 h</td></tr>
          <tr><th>Total</th><th>120 km</th><th>—</th><th>1.5 h</th></tr>
        </table>
        <p><strong>The method, every time:</strong></p>
        <ol>
          <li>Fill in what each leg gives you, converting units as you go.</li>
          <li>Work out the missing box in each row with the formula.</li>
          <li>Add the distance column and add the time column. <strong>Never add the speed column.</strong></li>
          <li>Divide the two totals, once, and give the answer a unit.</li>
        </ol>
        <p>Time spent stopped gets its own row with a distance of zero. It contributes nothing to the distance and a lot to the time, which is exactly why a rest stop drags an average speed down so sharply.</p>
        <p>Reverse versions of this question — "what speed must the second leg be to average X overall?" — are solved the same way, just filling in the table from the bottom: work out the <em>total time allowed</em> first, subtract the time already used, and you have the time available for the remaining leg.</p>`,
  demo:`<strong>Do this:</strong> a cyclist rides 12 km in 40 minutes, rests for 20 minutes, then rides 8 km in 20 minutes. Draw the table and find the average speed for the whole journey in km/h. (20 km in 80 min = 15 km/h.)`,
  cliff:`One more idea, and it is the one that makes the hardest question on this page solvable.`},

 {t:"Working backwards from the time", len:"5 min",
  body:`<p>Most questions hand you distance and time and ask for speed. The hard ones hand you a <em>target average speed</em> and make you work out what is still required. The trick is to stop thinking about speeds and start thinking about <strong>time budgets</strong>.</p>
        <p>Worked example. A runner wants to average <span class="num">6 m/s</span> over <span class="num">1200 m</span>. She runs the first 600 m at 4 m/s. How fast must she run the rest?</p>
        <ol>
          <li><strong>Total time allowed:</strong> 1200 ÷ 6 = <strong>200 s</strong>. That is the whole budget.</li>
          <li><strong>Time already spent:</strong> 600 ÷ 4 = <strong>150 s</strong>.</li>
          <li><strong>Time left:</strong> 200 − 150 = <strong>50 s</strong>, and there are still 600 m to cover.</li>
          <li><strong>Required speed:</strong> 600 ÷ 50 = <strong>12 m/s</strong>.</li>
        </ol>
        <p>Notice how brutal the arithmetic is. To lift the average from 4 to 6 — a rise of only 2 — she has to run the second half at <em>three times</em> her first-half speed. The instinct is to answer 8 m/s, because 4 and 8 average to 6. That instinct is wrong for the same reason as Lesson 3: the slow half ate three-quarters of the time budget before she had covered half the distance.</p>
        <p>Whenever a question gives you a target average, your first line should always be <span class="num">total distance ÷ target speed</span> to find the time budget. Everything else follows from there.</p>`,
  demo:`<strong>Do this:</strong> a driver wants to average 60 km/h over 120 km. After the first 60 km she has been driving for 1 hour 30 minutes. What speed does she need for the rest? (Budget 2 h, used 1.5 h, 60 km in 0.5 h — she needs 120 km/h.)`,
  cliff:`That is every idea this topic uses. The questions below are where you find out which ones you can actually write down.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"A car travels <span class='num'>150 m</span> in <span class='num'>10 s</span>. What is its speed?", o:["1.5 m/s","15 m/s","150 m/s","1500 m/s"], a:1,
  why:"speed = distance ÷ time = 150 ÷ 10 = 15 m/s. Sensible check: 15 m/s is 54 km/h, a believable town speed."},
 {n:2, lvl:"warm-up", q:"A distance–time graph has a <strong>horizontal</strong> section. During that section the object is:", o:["moving at a steady speed","stationary","speeding up","moving backwards"], a:1,
  why:"Horizontal means the distance from the start is not changing, so the object is not moving. A steady speed is a straight line that <em>slopes</em>."},
 {n:3, lvl:"standard", q:"Convert <span class='num'>20 m/s</span> into km/h.", o:["5.6 km/h","36 km/h","72 km/h","200 km/h"], a:2,
  why:"m/s to km/h is × 3.6, so 20 × 3.6 = 72 km/h. Going the wrong way would give 5.6, which is slower than walking — the sanity check catches it."},
 {n:4, lvl:"standard", q:"Runner A covers <span class='num'>100 m</span> in <span class='num'>25 s</span>. Runner B moves at <span class='num'>18 km/h</span>. Who is faster?", o:["Runner A","Runner B","They are exactly the same","Not enough information"], a:1,
  why:"Put both into the same unit before comparing. A is 100 ÷ 25 = 4 m/s. B is 18 ÷ 3.6 = 5 m/s. Runner B is faster — and the only way to see that is to convert first."},
 {n:5, lvl:"trap", q:"A train travels <span class='num'>30 km</span> in <span class='num'>20 minutes</span>. What is its average speed in km/h?", o:["1.5 km/h","10 km/h","60 km/h","90 km/h"], a:3,
  why:"20 minutes is 1/3 of an hour, so speed = 30 ÷ (1/3) = 90 km/h. Dividing 30 by 20 gives 1.5, which is the classic mistake — that answer is in km per minute, not km/h."}
];

const SHORTS = [
 {n:6, lvl:"standard", m:2, q:"Write down the formula linking speed, distance and time, and state the SI unit of speed.",
  scheme:["speed = distance ÷ time (accept distance = speed × time, correctly rearranged). <span class='num'>[1]</span>",
          "The SI unit is metres per second, m/s. <span class='num'>[1]</span>"],
  tip:"Write m/s, not \"metres\" and not \"mps\". The unit is a division and the notation should show it."},

 {n:7, lvl:"standard", m:2, q:"A train travels <span class='num'>240 km</span> in <span class='num'>3 hours</span>. Calculate its average speed, and give the unit.",
  scheme:["speed = distance ÷ time = 240 ÷ 3. <span class='num'>[1]</span>",
          "= <strong>80 km/h</strong>. <span class='num'>[1]</span>"],
  tip:"The distance was in km and the time in hours, so the answer is in km/h — no conversion needed. Converting when nothing asked you to is a good way to lose a mark you had already earned."},

 {n:8, lvl:"standard", m:2, q:"State what the <strong>gradient</strong> of a distance–time graph represents, and what a <strong>horizontal line</strong> on such a graph tells you.",
  scheme:["The gradient represents the speed of the object (a steeper gradient means a greater speed). <span class='num'>[1]</span>",
          "A horizontal line means the object is stationary — its distance from the start is not changing. <span class='num'>[1]</span>"],
  tip:"\"The gradient is how fast it's going\" gets the mark, but \"the gradient shows the distance\" does not. Gradient is a rate, not a quantity."},

 {n:9, lvl:"standard", m:2, q:"Convert <span class='num'>90 km/h</span> into metres per second. Show your method.",
  scheme:["Method: divide by 3.6, or convert 90 km to 90 000 m and 1 h to 3600 s. <span class='num'>[1]</span>",
          "90 ÷ 3.6 = <strong>25 m/s</strong>. <span class='num'>[1]</span>"],
  tip:"One mark is for the method and one is for the number. Writing only \"25 m/s\" risks half the marks if you have miscopied the question."},

 {n:10, lvl:"hard", m:2, q:"A student writes: <em>\"She ran the first half of the race at 4 m/s and the second half at 6 m/s, so her average speed was 5 m/s.\"</em> Explain why this is wrong.",
  scheme:["Average speed must be found from total distance ÷ total time, not by averaging the two speeds. <span class='num'>[1]</span>",
          "She spends longer running the slow half than the fast half, so the slower speed counts for more and the true average is below 5 m/s (it is 4.8 m/s). <span class='num'>[1]</span>"],
  tip:"The second mark needs the <em>reason</em>, which is about time, not distance. Saying \"you can't average speeds\" states the rule without explaining it, and usually scores one."}
];

const WORDS = [
 {n:11, lvl:"standard", m:3, q:"A cyclist rides <span class='num'>12 km</span> in <span class='num'>40 minutes</span>, rests for <span class='num'>20 minutes</span>, then rides a further <span class='num'>8 km</span> in <span class='num'>20 minutes</span>.<br><br><strong>(a)</strong> Find the total distance and the total time. <span class='num'>[1]</span><br><strong>(b)</strong> Calculate the average speed for the whole journey in km/h. <span class='num'>[1]</span><br><strong>(c)</strong> Explain what effect the rest had on the average speed, and why. <span class='num'>[1]</span>",
  hints:["Add the distances. Then add all three times — the rest counts as time even though no distance was covered.",
         "80 minutes needs to become hours before you divide, because the answer is wanted in km/h.",
         "For (c), think about what the rest added to the bottom of the fraction and what it added to the top."],
  sol:["(a) Total distance = 12 + 8 = <strong>20 km</strong>. Total time = 40 + 20 + 20 = <strong>80 minutes</strong>, which is 80 ÷ 60 = 1.333 h.",
       "(b) average speed = total distance ÷ total time = 20 ÷ 1.333 = <strong>15 km/h</strong>.",
       "(c) The rest lowered the average speed. It added 20 minutes to the total time while adding nothing to the total distance, so the same distance is being divided by a larger time.",
       "Without the rest the average would have been 20 km in 60 minutes = 20 km/h. The 20-minute stop cost 5 km/h."]},

 {n:12, lvl:"standard", m:3, q:"A walker's journey is recorded:<br><br><span class='num'>Time (s): &nbsp; &nbsp;0 &nbsp; &nbsp;20 &nbsp; &nbsp;40 &nbsp; &nbsp;60 &nbsp; &nbsp;80</span><br><span class='num'>Distance (m): 0 &nbsp; 30 &nbsp; &nbsp;60 &nbsp; &nbsp;60 &nbsp; &nbsp;20</span><br><br><strong>(a)</strong> Calculate the speed during the first 40 seconds. <span class='num'>[1]</span><br><strong>(b)</strong> Describe what happens between 40 s and 60 s, and how you know. <span class='num'>[1]</span><br><strong>(c)</strong> Describe what happens between 60 s and 80 s, and calculate the speed during it. <span class='num'>[1]</span>",
  hints:["For the first 40 s the distance goes up by the same amount every 20 s, so the speed is steady. Use the whole 40 s in one calculation.",
         "Look at the two distance readings at 40 s and 60 s. If the distance from the start does not change, what is the walker doing?",
         "The distance is getting smaller. That does not mean negative speed in the answer — it means the walker is heading back towards the start. Use the size of the change."],
  sol:["(a) speed = distance ÷ time = 60 ÷ 40 = <strong>1.5 m/s</strong>.",
       "(b) The walker is <strong>stationary</strong>. The distance from the start stays at 60 m for the whole 20 s, which on a graph would be a horizontal line.",
       "(c) The walker is <strong>returning towards the start</strong>, because the distance falls from 60 m to 20 m. That is 40 m in 20 s, so the speed is 40 ÷ 20 = <strong>2 m/s</strong>.",
       "Worth noting for (c): she walks back faster than she walked out. A grader looks for both the direction and the number."]},

 {n:13, lvl:"standard", m:3, q:"During a storm, a student sees a flash of lightning and hears the thunder <span class='num'>6 seconds</span> later. Sound travels at <span class='num'>330 m/s</span>.<br><br><strong>(a)</strong> Calculate how far away the lightning was. <span class='num'>[1]</span><br><strong>(b)</strong> Give your answer in kilometres. <span class='num'>[1]</span><br><strong>(c)</strong> The student assumes the light reached her instantly. Explain why that assumption is reasonable. <span class='num'>[1]</span>",
  hints:["You have a speed and a time, and you want a distance. Which arrangement of the formula is that?",
         "1 km is 1000 m.",
         "Light travels at about 300 000 000 m/s. Work out roughly how long light would take to cover the distance you found in (a)."],
  sol:["(a) distance = speed × time = 330 × 6 = <strong>1980 m</strong>.",
       "(b) 1980 ÷ 1000 = <strong>1.98 km</strong> (about 2 km).",
       "(c) Light travels roughly a million times faster than sound, so it covers 1980 m in about 0.0000066 s. That is far too short to notice, so treating the flash as instant introduces no measurable error.",
       "This is where the old rule comes from: count the seconds and divide by three to get the distance in kilometres."]},

 {n:14, lvl:"hard", m:3, q:"A car travels <span class='num'>60 km</span> at <span class='num'>60 km/h</span>, then a further <span class='num'>60 km</span> at <span class='num'>120 km/h</span>.<br><br><strong>(a)</strong> Calculate the time taken for each part of the journey. <span class='num'>[1]</span><br><strong>(b)</strong> Calculate the average speed for the whole journey. <span class='num'>[1]</span><br><strong>(c)</strong> A student says the average speed must be 90 km/h. Explain, in terms of time, why the true answer is lower. <span class='num'>[1]</span>",
  hints:["time = distance ÷ speed, done separately for each leg. Both legs are 60 km but the speeds differ.",
         "Add the two distances, add the two times, then divide once. Do not touch the speeds after part (a).",
         "Compare the two times you found. The car is not spending equal amounts of time at the two speeds — which speed does it spend longer at?"],
  sol:["(a) First part: 60 ÷ 60 = <strong>1 hour</strong>. Second part: 60 ÷ 120 = <strong>0.5 hours</strong>.",
       "(b) Total distance = 120 km, total time = 1.5 h. Average speed = 120 ÷ 1.5 = <strong>80 km/h</strong>.",
       "(c) The car spends 1 hour at the slow speed but only half an hour at the fast one, so twice as much of the journey's time is spent at 60 km/h. The slow speed therefore counts for twice as much in the average, pulling it below the halfway value of 90 km/h.",
       "This works for any journey split into equal distances: the average is always closer to the slower speed than to the faster one."]},

 {n:15, lvl:"hard", m:3, q:"A runner wants to average <span class='num'>6 m/s</span> over a <span class='num'>1200 m</span> race. She covers the first <span class='num'>600 m</span> at <span class='num'>4 m/s</span>.<br><br><strong>(a)</strong> Calculate the total time she is allowed for the whole race. <span class='num'>[1]</span><br><strong>(b)</strong> Calculate the time she has left for the second 600 m. <span class='num'>[1]</span><br><strong>(c)</strong> Calculate the speed she must run for the rest of the race, and comment on whether the popular answer of 8 m/s could ever have been right. <span class='num'>[1]</span>",
  hints:["Start with a time budget for the whole race, not with a speed. Total distance ÷ target average speed.",
         "Work out how long the first 600 m actually took her, then subtract it from the budget.",
         "You now have a distance still to run and a time left to run it in. One division gives the required speed — and it will be larger than you expect."],
  sol:["(a) Total time allowed = 1200 ÷ 6 = <strong>200 s</strong>.",
       "(b) The first 600 m took 600 ÷ 4 = 150 s, so the time remaining is 200 − 150 = <strong>50 s</strong>.",
       "(c) She must cover 600 m in 50 s, so she needs 600 ÷ 50 = <strong>12 m/s</strong> — three times her first-half speed. 8 m/s could never be right: it comes from averaging 4 and 8 to get 6, which ignores the fact that running the first half slowly used three-quarters of the entire time budget before she had covered half the distance.",
       "A useful sanity check: at 8 m/s the second half would take 75 s, giving 225 s overall and an average of 1200 ÷ 225 = 5.3 m/s, not 6."]}
];
"""

TOOLS = r"""
/* ================= HERO 1: the journey machine ================= */
const TMAX = 60, DMAX = 600;
const GX0 = 60, GX1 = 660, GY0 = 110, GY1 = 300;
const RX0 = 60, RX1 = 660;
function xT(t){ return GX0 + t/TMAX*(GX1-GX0); }
function yD(d){ return GY1 - d/DMAX*(GY1-GY0); }

(function(){
  const g = document.getElementById('glines');
  for(let d=200; d<=600; d+=200){
    const ln = document.createElementNS('http://www.w3.org/2000/svg','line');
    ln.setAttribute('x1',GX0); ln.setAttribute('x2',GX1);
    ln.setAttribute('y1',yD(d)); ln.setAttribute('y2',yD(d));
    ln.setAttribute('stroke','var(--line-soft)'); ln.setAttribute('stroke-width','1.5');
    ln.setAttribute('stroke-dasharray','4 5');
    g.appendChild(ln);
    const tx = document.createElementNS('http://www.w3.org/2000/svg','text');
    tx.setAttribute('x',22); tx.setAttribute('y',yD(d)+4);
    tx.setAttribute('font-family','var(--mono)'); tx.setAttribute('font-size','11');
    tx.setAttribute('fill','var(--ink-soft)'); tx.textContent = d;
    g.appendChild(tx);
  }
  const tk = document.getElementById('ticks');
  for(let d=0; d<=600; d+=100){
    const x = RX0 + d/DMAX*(RX1-RX0);
    const ln = document.createElementNS('http://www.w3.org/2000/svg','line');
    ln.setAttribute('x1',x); ln.setAttribute('x2',x);
    ln.setAttribute('y1',64); ln.setAttribute('y2',70);
    ln.setAttribute('stroke','var(--line)'); ln.setAttribute('stroke-width','1.5');
    tk.appendChild(ln);
  }
})();

const JOURNEYS = {
  steady:{name:'Steady all the way', legs:[{v:10,dur:60}],
    tale:'One steady speed for the whole minute, so the graph is a single straight line. The gradient never changes because the speed never changes.'},
  slow:{name:'Fast, then slower', legs:[{v:15,dur:20},{v:5,dur:40}],
    tale:'Fast for 20 s, then slow for 40 s. The line gets noticeably less steep — same direction, smaller gradient.'},
  stop:{name:'Stop for a while', legs:[{v:12,dur:15},{v:0,dur:20},{v:12,dur:25}],
    tale:'Moving, stopped, moving again. The flat middle section is the stop: distance from the start is not changing, so the object is stationary.'},
  back:{name:'There and back', legs:[{v:15,dur:20},{v:0,dur:5},{v:-12,dur:35}],
    tale:'Out to 300 m, a short pause, then back towards the start. The falling line means the distance from the start is decreasing.'}
};

let jT = 0, jD = 0, jV = 0, jRun = false, jLegs = null, lastPreset = null, jPts = [];
let lastFrame = null;
const SIMX = 1.6;   /* simulated seconds per real second */

function jPaint(){
  document.getElementById('j-t').textContent = jT.toFixed(1) + ' s';
  document.getElementById('j-d').textContent = Math.round(jD) + ' m';
  document.getElementById('j-v').textContent = Math.abs(jV).toFixed(0) + ' m/s';
  const pill = document.getElementById('j-pill');
  let note;
  if(!jRun && jT === 0){ pill.className='pill dis'; pill.textContent='Ready';
    note = 'Press Start. Watch the car and the line at the same time — the steeper the line, the faster the car.'; }
  else if(jV === 0){ pill.className='pill tim'; pill.textContent='Stationary';
    note = 'The car is not moving, so the distance from the start is not changing and the line is flat. Flat means stopped — never "steady speed".'; }
  else if(jV > 0){ pill.className='pill spe'; pill.textContent='Moving away';
    note = 'Distance from the start is increasing, so the line rises. Its gradient is exactly the speed shown on the right.'; }
  else { pill.className='pill dis'; pill.textContent='Coming back';
    note = 'Distance from the start is decreasing, so the line falls. The car is still moving — it is just heading home.'; }
  if(jLegs && jT >= 60) note = JOURNEYS[lastPreset].tale;
  document.getElementById('j-note').textContent = note;

  document.getElementById('car').setAttribute('x', (RX0 + jD/DMAX*(RX1-RX0) - 13).toFixed(1));
  document.getElementById('dtline').setAttribute('points', jPts.join(' '));
  document.getElementById('dtdot').setAttribute('cx', xT(jT).toFixed(1));
  document.getElementById('dtdot').setAttribute('cy', yD(jD).toFixed(1));
}

function jReset(){
  jT = 0; jD = 0; jV = 0; jRun = false; jLegs = null; jPts = ['60,300'];
  document.getElementById('runBtn').textContent = 'Start';
  jPaint();
}

function jStep(dt){
  if(!jRun) return;
  const step = Math.min(dt, 0.1) * SIMX;
  if(jLegs){
    let acc = 0, v = 0;
    for(const leg of jLegs){ acc += leg.dur; if(jT < acc){ v = leg.v; break; } }
    jV = v;
  } else {
    jV = +document.getElementById('spd').value;
  }
  jT += step;
  jD += jV * step;
  if(jD < 0){ jD = 0; jV = 0; }
  if(jD > DMAX){ jD = DMAX; jV = 0; }
  jPts.push(xT(jT).toFixed(1) + ',' + yD(jD).toFixed(1));
  if(jT >= TMAX){ jT = TMAX; jRun = false; document.getElementById('runBtn').textContent = 'Start again'; }
  jPaint();
}

function jFrame(now){
  const dt = lastFrame === null ? 0 : (now - lastFrame)/1000;
  lastFrame = now;
  jStep(dt);
  requestAnimationFrame(jFrame);
}

document.getElementById('spd').addEventListener('input', e=>{
  document.getElementById('spdval').textContent = e.target.value + ' m/s';
  if(!jLegs && jRun){ jV = +e.target.value; }
});
document.getElementById('runBtn').addEventListener('click', ()=>{
  if(jT >= TMAX) jReset();
  jRun = !jRun;
  document.getElementById('runBtn').textContent = jRun ? 'Pause' : 'Start';
});
document.getElementById('resetJ').addEventListener('click', jReset);
document.querySelectorAll('[data-journey]').forEach(b=>{
  b.addEventListener('click', ()=>{
    jReset();
    lastPreset = b.dataset.journey;
    jLegs = JOURNEYS[lastPreset].legs;
    jRun = true;
    document.getElementById('runBtn').textContent = 'Pause';
  });
});

const J_PUZZLES = [
 {ask:"Run the journey whose graph is a <strong>single straight line</strong> from start to finish.", want:'steady',
  why:"One unchanging gradient, because the speed never changes."},
 {ask:"Run the journey that produces a <strong>flat section in the middle</strong> of the graph.", want:'stop',
  why:"Flat means the distance from the start is not changing — the object is stationary."},
 {ask:"Run the journey whose line <strong>comes back down</strong> towards zero.", want:'back',
  why:"A falling line means the distance from the start is decreasing."},
 {ask:"Run the journey where the line stays rising but <strong>becomes less steep</strong> partway through.", want:'slow',
  why:"Still moving away, but with a smaller gradient — so a smaller speed."}
];
let jQ = null;
document.getElementById('jPuzzle').addEventListener('click', ()=>{
  jQ = J_PUZZLES[Math.floor(Math.random()*J_PUZZLES.length)];
  const box = document.getElementById('jQuiz');
  box.classList.add('on');
  box.innerHTML = '<strong>Puzzle.</strong> ' + jQ.ask +
    '<div class="qrow"><button class="btn ghost small" type="button" id="jCheck">Check my journey</button>' +
    '<span id="jFb" class="num" style="font-size:13px"></span></div>';
  document.getElementById('jCheck').addEventListener('click', ()=>{
    const fb = document.getElementById('jFb');
    if(lastPreset === jQ.want){
      fb.style.color = 'var(--ok)';
      fb.textContent = 'Correct — ' + jQ.why;
      S.puzzles = (S.puzzles||0) + 1; save(); refresh();
      document.getElementById('jCheck').disabled = true;
    } else {
      fb.style.color = 'var(--no)';
      fb.textContent = lastPreset ? 'That was "' + JOURNEYS[lastPreset].name + '". Try another.' : 'Run one of the four journeys first.';
    }
  });
});

/* ================= HERO 2: the solver ================= */
const DIST_U = {'m':1, 'km':1000};
const TIME_U = {'s':1, 'min':60, 'h':3600};
const SPD_U  = {'m/s':1, 'km/h':1/3.6};

let finding = 's';
const inA = document.getElementById('inA'), inB = document.getElementById('inB');
const unA = document.getElementById('unA'), unB = document.getElementById('unB');

function fillUnits(sel, units, chosen){
  sel.innerHTML = Object.keys(units).map(u=>'<option'+(u===chosen?' selected':'')+'>'+u+'</option>').join('');
}

function setupFields(){
  if(finding === 's'){
    document.getElementById('labA').textContent = 'Distance';
    document.getElementById('labB').textContent = 'Time';
    fillUnits(unA, DIST_U, 'm'); fillUnits(unB, TIME_U, 's');
    inA.value = 240; inB.value = 30;
  } else if(finding === 'd'){
    document.getElementById('labA').textContent = 'Speed';
    document.getElementById('labB').textContent = 'Time';
    fillUnits(unA, SPD_U, 'm/s'); fillUnits(unB, TIME_U, 's');
    inA.value = 12; inB.value = 25;
  } else {
    document.getElementById('labA').textContent = 'Distance';
    document.getElementById('labB').textContent = 'Speed';
    fillUnits(unA, DIST_U, 'm'); fillUnits(unB, SPD_U, 'm/s');
    inA.value = 400; inB.value = 8;
  }
  coverTriangle();
  solve();
}

function coverTriangle(){
  const cov = document.getElementById('tri-cover');
  const spots = {d:[62,52,96,44], s:[26,120,76,44], t:[104,120,76,44]};
  const p = spots[finding];
  cov.setAttribute('x',p[0]); cov.setAttribute('y',p[1]);
  cov.setAttribute('width',p[2]); cov.setAttribute('height',p[3]);
}

function tidy(x){
  if(!isFinite(x)) return '—';
  const r = Math.round(x*100)/100;
  return (Math.abs(r) >= 1000) ? r.toLocaleString('en-GB') : String(r);
}

function solve(){
  const a = parseFloat(inA.value), b = parseFloat(inB.value);
  const ua = unA.value, ub = unB.value;
  const work = document.getElementById('work');
  const pill = document.getElementById('sv-pill');
  if(isNaN(a) || isNaN(b)){ work.innerHTML = 'Put a number in both boxes.'; return; }

  let lines = [], main = '', alt = '', mains = '', alts = '';

  if(finding === 's'){
    pill.textContent = 'Finding speed';
    const dm = a * DIST_U[ua], ts = b * TIME_U[ub];
    lines.push('speed = distance ÷ time');
    if(ua !== 'm' || ub !== 's') lines.push('convert first: ' + a + ' ' + ua + ' = ' + tidy(dm) + ' m, &nbsp;' + b + ' ' + ub + ' = ' + tidy(ts) + ' s');
    lines.push('speed = ' + tidy(dm) + ' ÷ ' + tidy(ts));
    const v = dm/ts;
    lines.push('speed = <b>' + tidy(v) + ' m/s</b>');
    main = tidy(v) + ' m/s'; mains = 'the SI unit for speed';
    alt = tidy(v*3.6) + ' km/h'; alts = '× 3.6 to go from m/s to km/h';
  } else if(finding === 'd'){
    pill.textContent = 'Finding distance';
    const v = a * SPD_U[ua], ts = b * TIME_U[ub];
    lines.push('distance = speed × time');
    if(ua !== 'm/s' || ub !== 's') lines.push('convert first: ' + a + ' ' + ua + ' = ' + tidy(v) + ' m/s, &nbsp;' + b + ' ' + ub + ' = ' + tidy(ts) + ' s');
    lines.push('distance = ' + tidy(v) + ' × ' + tidy(ts));
    const d = v*ts;
    lines.push('distance = <b>' + tidy(d) + ' m</b>');
    main = tidy(d) + ' m'; mains = 'the SI unit for distance';
    alt = tidy(d/1000) + ' km'; alts = '÷ 1000 to go from m to km';
  } else {
    pill.textContent = 'Finding time';
    const dm = a * DIST_U[ua], v = b * SPD_U[ub];
    lines.push('time = distance ÷ speed');
    if(ua !== 'm' || ub !== 'm/s') lines.push('convert first: ' + a + ' ' + ua + ' = ' + tidy(dm) + ' m, &nbsp;' + b + ' ' + ub + ' = ' + tidy(v) + ' m/s');
    lines.push('time = ' + tidy(dm) + ' ÷ ' + tidy(v));
    const t = dm/v;
    lines.push('time = <b>' + tidy(t) + ' s</b>');
    main = tidy(t) + ' s'; mains = 'the SI unit for time';
    alt = tidy(t/60) + ' min'; alts = '÷ 60 to go from seconds to minutes';
  }
  work.innerHTML = lines.join('<br>');
  document.getElementById('sv-main').textContent = main;
  document.getElementById('sv-mains').textContent = mains;
  document.getElementById('sv-alt').textContent = alt;
  document.getElementById('sv-alts').textContent = alts;
}

document.querySelectorAll('[data-find]').forEach(b=>{
  b.addEventListener('click', ()=>{
    finding = b.dataset.find;
    document.querySelectorAll('[data-find]').forEach(x=>x.classList.toggle('on', x===b));
    setupFields();
  });
});
[inA, inB, unA, unB].forEach(el=> el.addEventListener('input', solve));

const SV_PUZZLES = [
 {ask:"Convert <strong>72 km/h</strong> into m/s.", ans:20, unit:'m/s', why:"Divide by 3.6: 72 ÷ 3.6 = 20 m/s."},
 {ask:"Convert <strong>15 m/s</strong> into km/h.", ans:54, unit:'km/h', why:"Multiply by 3.6: 15 × 3.6 = 54 km/h."},
 {ask:"A train covers <strong>30 km in 20 minutes</strong>. What is its speed in km/h?", ans:90, unit:'km/h', why:"20 minutes is 1/3 h, so 30 ÷ (1/3) = 90 km/h. Dividing 30 by 20 gives 1.5, which is the trap."},
 {ask:"A runner covers <strong>400 m in 50 s</strong>. What is her speed in m/s?", ans:8, unit:'m/s', why:"400 ÷ 50 = 8 m/s, which is about 29 km/h — quick, but possible over a short distance."},
 {ask:"A car travels at <strong>25 m/s for 4 minutes</strong>. How far does it go, in metres?", ans:6000, unit:'m', why:"4 minutes is 240 s, so 25 × 240 = 6000 m, or 6 km."}
];
let svQ = null;
document.getElementById('svPuzzle').addEventListener('click', ()=>{
  svQ = SV_PUZZLES[Math.floor(Math.random()*SV_PUZZLES.length)];
  const box = document.getElementById('svQuiz');
  box.classList.add('on');
  box.innerHTML = '<strong>Puzzle.</strong> ' + svQ.ask + ' Work it out on paper first — then type the number.' +
    '<div class="qrow"><input id="svIn" type="number" step="any" style="width:120px" aria-label="Your answer">' +
    '<span class="num" style="font-size:13px">' + svQ.unit + '</span>' +
    '<button class="btn ghost small" type="button" id="svCheck">Check</button>' +
    '<span id="svFb" class="num" style="font-size:13px"></span></div>';
  document.getElementById('svCheck').addEventListener('click', ()=>{
    const v = parseFloat(document.getElementById('svIn').value);
    const fb = document.getElementById('svFb');
    if(!isNaN(v) && Math.abs(v - svQ.ans) < 0.05){
      fb.style.color = 'var(--ok)';
      fb.textContent = 'Correct — ' + svQ.why;
      S.puzzles = (S.puzzles||0) + 1; save(); refresh();
      document.getElementById('svCheck').disabled = true;
    } else {
      fb.style.color = 'var(--no)';
      fb.textContent = 'Not yet. Check which unit you are converting into.';
    }
  });
});

function boot(){
  jReset();
  document.querySelector('[data-find="s"]').classList.add('on');
  setupFields();
  requestAnimationFrame(jFrame);
}
"""

html = page(
    title="How Fast, How Far, How Long — Grade 7 IGCSE Physics",
    root_css=ROOT, extra_css=EXTRA, mast=MAST, nav=NAV, heroes=HEROES,
    question_note="No calculator on Q1 to Q5.",
    traps=TRAPS, papers=PAPERS, data_js=DATA, tools_js=TOOLS,
    key='speed-progress-v1', pid='speed', subject='physics',
    hubtitle='How Fast, How Far, How Long')

io.open(os.path.join(REPO,'speed.html'),'w',encoding='utf-8').write(html)
print('written', len(html))
