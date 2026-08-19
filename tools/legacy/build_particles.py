#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from build_lib import page

ROOT = """:root{
  --ink:#1A1A22;
  --ink-soft:#575463;
  --paper:#EDEAE3;
  --card:#FFFFFF;
  --line:#D8D2C6;
  --line-soft:#E8E3DA;
  --sol:#2B4E9B;        /* solid — always indigo */
  --sol-tint:#E9EDF7;
  --liq:#0E7C6B;        /* liquid — always green-teal */
  --liq-tint:#E2F1EE;
  --gas:#B4560B;        /* gas — always amber */
  --gas-tint:#FBEFE3;
  --fr:var(--sol);  --fr-tint:var(--sol-tint);
  --de:var(--liq);  --de-tint:var(--liq-tint);
  --pc:var(--gas);  --pc-tint:var(--gas-tint);
  --steel:#A29B8C;
  --steel-dark:#6F6A5D;
  --ok:#1B7F4B;
  --ok-tint:#E6F3EC;
  --no:#98241B;
  --no-tint:#FBEAE8;
  --display:'Bricolage Grotesque','Trebuchet MS',sans-serif;
  --body:'Newsreader',Georgia,serif;
  --mono:'JetBrains Mono',ui-monospace,Menlo,monospace;
  --r:14px;
}
"""

EXTRA = """
nav.jump{background:rgba(237,234,227,.93)}
.soltxt{color:var(--sol);font-weight:700}
.liqtxt{color:var(--liq);font-weight:700}
.gastxt{color:var(--gas);font-weight:700}
.pill.sol{background:var(--sol-tint);color:var(--sol)}
.pill.liq{background:var(--liq-tint);color:var(--liq)}
.pill.gas{background:var(--gas-tint);color:var(--gas)}
"""

MAST = """<header class="mast">
  <div class="eyebrow">IGCSE Chemistry · Grade 7 · States of matter</div>
  <h1>Small Bits,<br><em>Always</em> <b>Moving</b></h1>
  <p class="lede">One idea explains this entire topic: everything is made of particles that are always moving, and the only things that change between a solid, a liquid and a gas are <strong>how the particles are arranged</strong> and <strong>how much energy they have</strong>. The particles themselves never change. Hold on to that and the rest is detail.</p>

  <div class="target">
    <strong>The deal.</strong> You've been landing around <span class="num">10 out of 15</span>. This page is out of <span class="num">30</span>, so the honest target is <span class="num">21</span> on the first pass and <span class="num">26</span> on the second. Every mark here comes from writing about <em>particles</em>, not about how things feel — that switch in language is worth more than anything else on the page.
  </div>

  <div class="strip">
    <div class="stat"><b class="num" id="s-marks">0<span style="font-size:15px;color:var(--ink-soft)">/30</span></b><span>marks banked</span><div class="bar"><i id="bar-marks"></i></div></div>
    <div class="stat"><b class="num" id="s-lessons">0<span style="font-size:15px;color:var(--ink-soft)">/6</span></b><span>lessons finished</span><div class="bar"><i id="bar-lessons"></i></div></div>
    <div class="stat"><b class="num" id="s-puzzles">0</b><span>machine puzzles solved</span><div class="bar"><i id="bar-puzzles"></i></div></div>
  </div>
</header>"""

NAV = """<nav class="jump" aria-label="Sections">
  <a href="#box">Particle box</a>
  <a href="#videos">6 videos</a>
  <a href="#lessons">6 lessons</a>
  <a href="#curve">Heating curve</a>
  <a href="#quick">Quick checks</a>
  <a href="#short">Short answers</a>
  <a href="#word">Word problems</a>
  <a href="#traps">Exam traps</a>
  <a href="#papers">Test papers</a>
</nav>"""

HEROES = """
<!-- ============ HERO 1: THE PARTICLE BOX ============ -->
<section id="box">
  <div class="panel">
    <div class="panel-top">
      <h2>The particle box</h2>
      <p>Thirty-six particles of water, and one temperature dial. Drag it from a deep freeze up past boiling and watch what actually changes — because the particles do not get bigger, softer or hotter to the touch. They only move differently and sit differently.</p>
    </div>

    <svg class="stage" id="pbox" viewBox="0 0 500 280" role="img" aria-label="A box of particles whose arrangement changes with temperature">
      <rect x="40" y="30" width="420" height="220" rx="4" fill="var(--paper)" stroke="var(--line)" stroke-width="2"/>
      <g id="parts"></g>
      <text x="46" y="24" font-family="var(--mono)" font-size="12" fill="var(--ink-soft)" id="pb-cap">SEALED CONTAINER</text>
    </svg>

    <div class="ctrl">
      <label for="temp">Temperature</label>
      <input id="temp" type="range" min="-30" max="160" value="-20" step="1" aria-label="Temperature in degrees Celsius">
      <span class="num" id="tempval" style="min-width:70px;text-align:right">-20 °C</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <button class="btn ghost small" type="button" data-temp="-20">Ice</button>
      <button class="btn ghost small" type="button" data-temp="0">Melting point</button>
      <button class="btn ghost small" type="button" data-temp="50">Water</button>
      <button class="btn ghost small" type="button" data-temp="100">Boiling point</button>
      <button class="btn ghost small" type="button" data-temp="140">Steam</button>
    </div>

    <div class="rows">
      <div class="cell f"><div class="lab">Arrangement</div><div class="val" id="pb-arr">Regular</div><div class="sub" id="pb-arrs">fixed pattern, touching</div></div>
      <div class="cell d"><div class="lab">Movement</div><div class="val" id="pb-mov">Vibrating</div><div class="sub" id="pb-movs">about fixed positions</div></div>
      <div class="cell p"><div class="lab">Spacing</div><div class="val" id="pb-spa">Very close</div><div class="sub" id="pb-spas">strong forces between them</div></div>
      <div class="phasebar">
        <span class="pill sol" id="pb-pill">Solid</span>
        <span id="pb-note">Ice. The particles are locked in a pattern but still vibrating — they are never completely still.</span>
        <span class="push"><button class="btn ghost" type="button" id="boxPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="boxQuiz"></div>
    </div>
  </div>
</section>

<!-- ============ VIDEOS ============ -->
<section id="videos">
  <div class="shead"><h2>Watch these six, in this order</h2><span class="tag">~35 min total</span></div>
  <p class="snote">Each video comes with one small written job. Do the job, or the video was a screensaver with chemistry on it. Pause and write as you go — don't tell yourself you'll rewind at the end, because you won't.</p>
  <div id="videoList"></div>
</section>

<!-- ============ LESSONS ============ -->
<section id="lessons">
  <div class="shead"><h2>Six lessons</h2><span class="tag">~35 min total</span></div>
  <div id="lessonList"></div>
</section>

<!-- ============ HERO 2: THE HEATING CURVE ============ -->
<section id="curve">
  <div class="panel">
    <div class="panel-top">
      <h2>The heating curve</h2>
      <p>Take a lump of ice at −20 °C and pour energy in at a steady rate. This is the graph you get, drawn with the real energies for water — which means the two flat sections are exactly as long as they really are. Drag the slider and watch where the energy actually goes.</p>
    </div>

    <svg class="stage" id="hcurve" viewBox="0 0 700 330" role="img" aria-label="A graph of temperature against energy added, showing two flat sections">
      <line x1="60" y1="40" x2="60" y2="280" stroke="var(--line)" stroke-width="2"/>
      <line x1="60" y1="280" x2="668" y2="280" stroke="var(--line)" stroke-width="2"/>
      <g id="hgrid-lines"></g>
      <polyline id="hc-faint" fill="none" stroke="var(--line)" stroke-width="6" stroke-linejoin="round" points=""/>
      <polyline id="hc-live" fill="none" stroke="var(--sol)" stroke-width="6" stroke-linejoin="round" points=""/>
      <circle id="hc-dot" cx="60" cy="280" r="8" fill="var(--sol)" stroke="#fff" stroke-width="2.5"/>
      <text x="60" y="308" font-family="var(--mono)" font-size="12" fill="var(--ink-soft)">ENERGY ADDED &#8594;</text>
      <text x="14" y="46" font-family="var(--mono)" font-size="12" fill="var(--ink-soft)">°C</text>
    </svg>

    <div class="ctrl">
      <label for="energy">Energy added</label>
      <input id="energy" type="range" min="0" max="1000" value="0" step="1" aria-label="Energy added to the ice">
      <span class="num" id="energyval" style="min-width:76px;text-align:right">0%</span>
    </div>

    <div class="rows">
      <div class="cell f"><div class="lab">Temperature</div><div class="val" id="hc-temp">−20 °C</div><div class="sub" id="hc-temps">rising steadily</div></div>
      <div class="cell d"><div class="lab">State</div><div class="val" id="hc-state">Solid</div><div class="sub" id="hc-states">ice, below its melting point</div></div>
      <div class="cell p"><div class="lab">The energy is</div><div class="val" id="hc-job">Speeding up</div><div class="sub" id="hc-jobs">particles vibrate faster</div></div>
      <div class="phasebar">
        <span class="pill sol" id="hc-pill">Heating the ice</span>
        <span id="hc-note">Drag the slider. Watch for the two places where the line goes flat even though energy is still going in.</span>
        <span class="push"><button class="btn ghost" type="button" id="curvePuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="curveQuiz"></div>
    </div>
  </div>
</section>
"""

TRAPS = """
<section id="traps">
  <div class="shead"><h2>Five traps</h2><span class="tag">Read before any test</span></div>
  <div class="traps">
    <div class="trap"><h4>Saying the particles melt, expand or get hot</h4><p>A particle of water is the same particle at −20 °C and at 140 °C. It does not melt, soften, swell or change colour. What changes is how fast it moves and how far apart it sits from its neighbours. Write "the particles move further apart", never "the particles get bigger" — that sentence costs the mark every time.</p></div>
    <div class="trap"><h4>Thinking the flat part of the graph means nothing is happening</h4><p>Energy is still going in at exactly the same rate. It is being used to <em>break the forces</em> holding particles together instead of making them move faster, and temperature only measures how fast they move. Flat line, busy particles.</p></div>
    <div class="trap"><h4>Using boiling and evaporation as the same word</h4><p>Boiling happens at one fixed temperature, throughout the whole liquid, with bubbles. Evaporation happens at <em>any</em> temperature, only at the surface, from the fastest particles escaping. A puddle drying on a cold day is evaporation, and calling it boiling loses marks.</p></div>
    <div class="trap"><h4>Thinking mass changes when the state changes</h4><p>Melt 20 g of ice and you have 20 g of water. Boil it and you have 20 g of steam, spread thinly. The particles are all still there and still weigh what they weighed. If a question says the mass "decreased", something escaped from the container — say where it went.</p></div>
    <div class="trap"><h4>Drawing solids and liquids with big gaps</h4><p>In a diagram, solid particles touch and sit in a regular pattern; liquid particles touch but are jumbled; only gas particles have real space between them, and far more than students draw. Neat touching circles for two states, scattered ones for the third.</p></div>
  </div>
</section>
"""

PAPERS = """
<section id="papers">
  <div class="shead"><h2>The four test papers</h2><span class="tag">30 marks each</span></div>
  <p class="snote">These are the printed papers that go with this page. Do them on paper, timed, with your phone in another room. Medium first; only move to the hard papers once you're clearing 21 on a medium one.</p>
  <div class="papers">
    <div class="paper"><span class="pn">A</span><span class="pt">Paper A — Medium</span><span class="num" style="color:var(--ink-soft);font-size:13px">35 min</span>
      <p class="pd">The three states and their properties, naming the changes of state, particle diagrams, and two short explanations in terms of particles.</p></div>
    <div class="paper"><span class="pn">B</span><span class="pt">Paper B — Medium</span><span class="num" style="color:var(--ink-soft);font-size:13px">35 min</span>
      <p class="pd">Reading a heating curve, melting and boiling points from data, diffusion, and a conservation-of-mass question.</p></div>
    <div class="paper"><span class="pn hard">C</span><span class="pt">Paper C — Hard</span><span class="num" style="color:var(--ink-soft);font-size:13px">45 min</span>
      <p class="pd">Evaporation versus boiling, cooling by evaporation, gas pressure in a sealed container, and explaining an unfamiliar experiment.</p></div>
    <div class="paper"><span class="pn hard">D</span><span class="pt">Paper D — Hard</span><span class="num" style="color:var(--ink-soft);font-size:13px">45 min</span>
      <p class="pd">Multi-step problems: interpreting a cooling curve for an unknown substance, the ammonia and hydrogen chloride diffusion tube, and a six-mark particle explanation.</p></div>
  </div>
</section>
"""

DATA = r"""
/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"States Of Matter — Solids, Liquids & Gases", ch:"FuseSchool", url:"https://www.youtube.com/watch?v=21CR01rlmv4",
  why:"The clean starting point: the three states, what the particles are doing in each, and the properties that follow from that. Everything on this page hangs off these four minutes.",
  task:"Draw the three particle diagrams from memory afterwards, then write one line under each saying what the particles are doing. Compare with the table in Lesson 1 and correct in a different colour."},

 {t:"GCSE Physics — Particle Theory & States of Matter", ch:"Cognito", url:"https://www.youtube.com/watch?v=OTksau0_VoI",
  why:"The same content pitched at exam level, with the language examiners actually reward. Notice how often he says \"the forces between the particles\" — that phrase is worth marks.",
  task:"Write down three phrases he uses that you would not have used yourself. Those three phrases are the difference between a 1-mark answer and a 2-mark one."},

 {t:"Changes of State", ch:"FuseSchool · Chemistry", url:"https://www.youtube.com/watch?v=s2ObEtQKePI",
  why:"Melting, freezing, boiling, condensing and sublimation, with the names going in both directions. Q6 and Q7 come straight from here.",
  task:"Draw a triangle with solid, liquid and gas at the corners. Label every arrow both ways with the correct name. Six arrows, six names — no gaps."},

 {t:"Changes of State", ch:"FuseSchool · Physics", url:"https://www.youtube.com/watch?v=xYU7RSoOZ0U",
  why:"The physics-side version, which does the energy story properly: where the energy goes when a substance changes state rather than warms up.",
  task:"Finish this sentence in writing: \"During melting the temperature stays the same because the energy is being used to…\" Get this one sentence right and Q8 and Q15 are both easier."},

 {t:"What Is Brownian Motion?", ch:"FuseSchool", url:"https://www.youtube.com/watch?v=NHo6LTXdFns",
  why:"The evidence that particles are real and really moving — smoke specks jittering because invisible air particles are hitting them. Short, and it explains diffusion at the same time.",
  task:"Write two sentences: one saying what you can see under the microscope, and one saying what is causing it that you cannot see. Examiners want both halves."},

 {t:"GCSE Physics — Specific Latent Heat", ch:"Cognito", url:"https://www.youtube.com/watch?v=3itqmCtmJPc",
  why:"This is the video for the flat sections of the heating curve. It goes slightly beyond Grade 7, so watch the first half and stop when the equations start.",
  task:"Copy the heating curve from the video into your book, then label the two flat parts with what is happening to the particles at each. Check it against the machine above."}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"Three states, three questions", len:"6 min",
  body:`<p>Every question about states of matter is really asking one of three things: how are the particles <strong>arranged</strong>, how do they <strong>move</strong>, and how far <strong>apart</strong> are they? Answer those and the properties come out on their own.</p>
        <table class="data">
          <tr><th></th><th>Solid</th><th>Liquid</th><th>Gas</th></tr>
          <tr><th>Arrangement</th><td>regular pattern, touching</td><td>touching but jumbled</td><td>far apart, random</td></tr>
          <tr><th>Movement</th><td>vibrate about fixed points</td><td>slide past each other</td><td>fast, random, in all directions</td></tr>
          <tr><th>Forces between</th><td>strong</td><td>weaker</td><td>almost none</td></tr>
          <tr><th>Shape</th><td>fixed</td><td>takes the container</td><td>fills the container</td></tr>
          <tr><th>Volume</th><td>fixed</td><td>fixed</td><td>not fixed</td></tr>
        </table>
        <p>Now read the last two rows again, because that is where the marks hide. A <span class="liqtxt">liquid</span> has a <strong>fixed volume but no fixed shape</strong> — pour 200 ml between three different jugs and it is still 200 ml. A <span class="gastxt">gas</span> has <strong>neither</strong>; it spreads out until it hits the walls.</p>
        <p>Why can a gas be squashed but a liquid barely at all? Because squashing means pushing particles closer, and in a liquid they are <em>already touching</em>. There is nothing left to squash out. In a gas there is mostly empty space.</p>`,
  demo:`<strong>Do this:</strong> put your finger over the end of a syringe full of air and push. Now fill it with water and try again. Write one sentence explaining the difference using the word "spacing".`,
  cliff:`If the particles never change, what exactly is being added when you heat something — and where does it go?`},

 {t:"Changing state, and its six names", len:"6 min",
  body:`<p>Six arrows, six names. Learn them in pairs, because each pair is the same journey in opposite directions:</p>
        <div class="eqline"><span class="soltxt">solid</span> &#8594; <span class="liqtxt">liquid</span> is <strong>melting</strong> &nbsp;·&nbsp; <span class="liqtxt">liquid</span> &#8594; <span class="soltxt">solid</span> is <strong>freezing</strong></div>
        <div class="eqline"><span class="liqtxt">liquid</span> &#8594; <span class="gastxt">gas</span> is <strong>boiling</strong> or <strong>evaporating</strong> &nbsp;·&nbsp; <span class="gastxt">gas</span> &#8594; <span class="liqtxt">liquid</span> is <strong>condensing</strong></div>
        <div class="eqline"><span class="soltxt">solid</span> &#8594; <span class="gastxt">gas</span> directly is <strong>sublimation</strong> &nbsp;·&nbsp; the reverse is <strong>deposition</strong></div>
        <p>Two facts that carry marks:</p>
        <ul>
          <li>The melting point and the freezing point of a substance are the <strong>same temperature</strong>. Water melts at 0 °C and freezes at 0 °C. Which way it goes depends on whether energy is going in or coming out.</li>
          <li>Changes of state are <strong>physical changes</strong>. No new substance is made, nothing is destroyed, and the change can be reversed. Steam is still water.</li>
        </ul>
        <p>Because nothing is created or destroyed, <strong>mass is conserved</strong>. 20 g of ice becomes 20 g of water becomes 20 g of steam. If a mass reading drops when something boils, it is because the gas escaped the container — not because the particles vanished.</p>`,
  demo:`<strong>Do this:</strong> write the six names on a triangle from memory. Then answer, in one line: an open beaker of water is left on a balance for a week and the reading falls. Has mass been destroyed?`,
  cliff:`If you heat ice steadily, the temperature climbs — and then, for a long stretch, refuses to. Why?`},

 {t:"Where the energy goes", len:"7 min",
  body:`<p>Temperature is a measure of how fast the particles are moving, on average. Nothing else. So when you add energy to a substance, only one of two things can happen to it:</p>
        <ol>
          <li>The particles <strong>speed up</strong> — the temperature rises.</li>
          <li>The particles <strong>break away from each other</strong> — the temperature stays exactly where it is.</li>
        </ol>
        <p>Both cannot happen at once, and that single fact is the whole heating curve. While ice is melting, every joule you put in is spent pulling particles out of the lattice and away from their neighbours. None of it is left over to make them move faster, so the thermometer sits at 0 °C and does not budge until the last crystal has gone.</p>
        <p>Then the same thing happens again, much more dramatically, at 100 °C. Breaking a liquid apart into a gas takes far more energy than loosening a solid into a liquid, because the particles have to be separated completely rather than just unlocked:</p>
        <div class="eqline">melting 1 kg of ice: about 334 kJ &nbsp;·&nbsp; boiling 1 kg of water: about 2260 kJ</div>
        <p>That is nearly seven times as much — which is why the boiling plateau in the machine above swallows almost three-quarters of the whole graph. It is also why a steam burn is far worse than a burn from boiling water: all that energy comes back out when the steam condenses on your skin.</p>
        <p>Running the film backwards works too. When a liquid freezes, energy is <em>released</em> as the particles settle into the lattice, and the temperature holds steady at the freezing point while it happens.</p>`,
  demo:`<strong>Do this:</strong> sketch the heating curve for water from −20 °C to 120 °C with no help. Mark on it: 0 °C, 100 °C, the two flat parts, and which state exists on each sloped part. Then check it against the machine.`,
  cliff:`Water boils at 100 °C. So how does a puddle disappear on a day that never gets above 15 °C?`},

 {t:"Evaporation is not boiling", len:"6 min",
  body:`<p>Examiners test this distinction constantly, and most students blur the two words together. They are different processes.</p>
        <table class="data">
          <tr><th></th><th>Boiling</th><th>Evaporation</th></tr>
          <tr><th>Temperature</th><td>only at the boiling point</td><td>at any temperature</td></tr>
          <tr><th>Where</th><td>throughout the liquid</td><td>only at the surface</td></tr>
          <tr><th>Speed</th><td>fast</td><td>slow</td></tr>
          <tr><th>Bubbles</th><td>yes</td><td>no</td></tr>
        </table>
        <p><strong>How evaporation works.</strong> "Average speed" means some particles are slower than average and some are faster. A few of the fastest ones, right at the surface, are moving quickly enough to escape the forces holding them in the liquid — so they leave. No boiling required.</p>
        <p><strong>Why it cools what is left behind.</strong> The particles that escape are the fastest ones. Remove the fastest and the average speed of those remaining drops — and average speed <em>is</em> temperature. So the liquid gets colder. This is why you shiver when you climb out of a pool, why sweating works, and why a wet cloth around a bottle keeps it cool.</p>
        <p><strong>What makes evaporation faster:</strong> a higher temperature (more particles are fast enough to escape), a larger surface area (more particles are at the surface), and wind (it blows escaped particles away before they can fall back in).</p>`,
  demo:`<strong>Do this:</strong> put one drop of water on the back of each hand. Blow gently on one. Write down which feels colder and explain it in two sentences, using the words "fastest particles" and "average".`,
  cliff:`You can smell dinner from another room. Nobody carried the smell there — so how did it travel?`},

 {t:"Diffusion, and the proof particles are real", len:"6 min",
  body:`<p><strong>Diffusion</strong> is the spreading of particles from where they are crowded to where they are not, caused by nothing more than their own random movement. No stirring, no wind, no pushing.</p>
        <p>It works because particles in a gas or liquid move constantly in random directions. Start them all in one corner and, purely by chance, more will wander outwards than back — until they are spread evenly and there is nowhere left to spread to.</p>
        <p>Diffusion is <strong>faster in gases than in liquids</strong> (the particles move faster and have space to move through), <strong>faster when hot</strong> (more energy, faster particles), and <strong>faster for lighter particles</strong> at the same temperature.</p>
        <p><strong>Brownian motion</strong> is the evidence. Look at smoke in a glass cell under a microscope and the specks jiggle about in random zigzags. The specks are big enough to see; what is hitting them is not. Air particles, invisible and moving fast, are knocking them about unevenly from every side.</p>
        <p>The classic experiment: a long glass tube with cotton wool soaked in ammonia at one end and hydrogen chloride at the other. Both diffuse along the tube and a white ring of ammonium chloride forms where they meet — but <strong>not in the middle</strong>. It forms nearer the hydrogen chloride end, because ammonia particles are lighter, so they travel faster and cover more of the tube before the two meet.</p>`,
  demo:`<strong>Do this:</strong> drop food colouring into a glass of cold water and an identical glass of hot water, and do not stir either. Time how long each takes to go evenly coloured. Write down the two times and the reason.`,
  cliff:`Gas particles are constantly hitting the walls of their container. What does that add up to?`},

 {t:"Gas pressure, explained by collisions", len:"5 min",
  body:`<p>Gas particles move fast and in all directions, so they are permanently colliding with the walls of whatever contains them. Each collision is a tiny push. Billions of tiny pushes per second, spread over the wall, is what we call <strong>pressure</strong>.</p>
        <p>Once you see pressure as collisions, every question answers itself:</p>
        <ul>
          <li><strong>Heat a sealed can.</strong> The particles gain energy and move faster, so they hit the walls <em>harder</em> and <em>more often</em>. Pressure rises — and if it rises enough, the can bursts. This is why aerosols carry a warning about fire.</li>
          <li><strong>Squash a gas into half the space.</strong> Same number of particles, smaller area of wall and less room to travel, so collisions happen more often. Pressure rises.</li>
          <li><strong>Cool a gas.</strong> Slower particles, gentler and rarer collisions, lower pressure. A sealed plastic bottle left in a fridge crumples slightly for exactly this reason.</li>
        </ul>
        <p>The answer phrase that earns marks is always two-part: the particles hit the walls <strong>harder and more frequently</strong>. Give one half only and you usually get one mark of two.</p>`,
  demo:`<strong>Do this:</strong> explain in three sentences why a bicycle tyre feels harder on a hot afternoon than it did in the cool morning, without using the word "expand".`,
  cliff:`You now have every idea this topic uses. The questions below are where you find out which ones you can actually write down.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"Which state of matter has a <strong>fixed volume</strong> but takes the shape of its container?", o:["Solid","Liquid","Gas","None of them"], a:1,
  why:"A liquid keeps its volume — pour 200 ml between jugs and it stays 200 ml — but flows into whatever shape holds it. A solid fixes both; a gas fixes neither."},
 {n:2, lvl:"warm-up", q:"When water boils, what happens to the water particles themselves?", o:["They break apart into smaller particles","They get bigger","They stay exactly the same, but move much faster and further apart","They turn into air"], a:2,
  why:"Boiling is a physical change. Nothing is created, destroyed or altered — the particles simply gain enough energy to escape from each other. Steam is still water."},
 {n:3, lvl:"standard", q:"A pure substance is melting. What happens to its temperature while it melts?", o:["It rises steadily","It stays the same","It falls","It rises, then falls"], a:1,
  why:"All the energy going in is used to break the forces between particles rather than to speed them up, and temperature only measures speed. The thermometer holds still until the last of the solid has gone."},
 {n:4, lvl:"standard", q:"A gas in a sealed syringe is squashed to half its original volume. What happens to the <strong>mass</strong> of the gas?", o:["It doubles","It halves","It stays the same","It becomes zero"], a:2,
  why:"Squashing changes the spacing, not the number of particles. Same particles, same mass — the gas is simply denser, because the same mass now occupies half the volume."},
 {n:5, lvl:"trap", q:"In which of these would a drop of dye spread out fastest?", o:["Cold water","Hot water","Cold air","Hot air"], a:3,
  why:"Two effects stack up. Diffusion is faster in gases than liquids because the particles move faster and have space to move through, and faster when hot because the particles have more energy. Hot air wins on both counts."}
];

const SHORTS = [
 {n:6, lvl:"standard", m:2, q:"Describe the <strong>arrangement</strong> and the <strong>movement</strong> of the particles in a solid.",
  scheme:["Arrangement: the particles are close together and touching, in a regular fixed pattern. <span class='num'>[1]</span>",
          "Movement: they vibrate about fixed positions — they cannot move past each other. <span class='num'>[1]</span>"],
  tip:"Two marks means two ideas. Answering \"they are close together and don't move\" scores one and loses one, because solid particles are never still."},

 {n:7, lvl:"standard", m:2, q:"Explain, in terms of particles, why a gas can easily be compressed but a liquid can hardly be compressed at all.",
  scheme:["In a gas the particles are far apart with large spaces between them, so they can be pushed closer together. <span class='num'>[1]</span>",
          "In a liquid the particles are already touching, so there is almost no space left to remove. <span class='num'>[1]</span>"],
  tip:"The word \"already\" is doing the work in the second mark. Compression is about the space between particles, never about the particles themselves being squashed."},

 {n:8, lvl:"standard", m:2, q:"A beaker of pure wax is heated steadily. While it is melting, the temperature stays at 58 °C even though the heater is still on. Explain why.",
  scheme:["The energy is being used to break (or weaken) the forces holding the particles in their fixed positions. <span class='num'>[1]</span>",
          "It is not being used to make the particles move faster, and temperature depends on how fast the particles move — so the temperature does not rise. <span class='num'>[1]</span>"],
  tip:"\"The energy is used up melting it\" is not enough on its own. Say what the energy does to the forces, and say why that leaves the temperature unchanged."},

 {n:9, lvl:"standard", m:2, q:"Give <strong>two</strong> differences between evaporation and boiling.",
  scheme:["Any one: boiling happens only at the boiling point, evaporation happens at any temperature. <span class='num'>[1]</span>",
          "Any one other: boiling happens throughout the liquid (with bubbles), evaporation happens only at the surface; or boiling is fast while evaporation is slow. <span class='num'>[1]</span>"],
  tip:"Each mark needs a genuine comparison — say what each process does, not just what one of them does. \"Evaporation is at the surface\" is half an answer."},

 {n:10, lvl:"hard", m:2, q:"A sealed metal tin containing air is placed in a hot oven. Explain, in terms of particles, why the pressure inside the tin increases.",
  scheme:["The particles gain energy and move faster. <span class='num'>[1]</span>",
          "So they collide with the walls of the tin harder and more frequently, and pressure is the effect of those collisions. <span class='num'>[1]</span>"],
  tip:"Harder <em>and</em> more often. Students who write only one of the two usually get one mark, and it is the most commonly dropped mark in this whole topic."}
];

const WORDS = [
 {n:11, lvl:"standard", m:3, q:"A solid substance is heated steadily and its temperature is recorded every minute.<br><br><span class='num'>Time (min): &nbsp;0 &nbsp; 2 &nbsp; 4 &nbsp; 6 &nbsp; 8 &nbsp; 10 &nbsp; 12</span><br><span class='num'>Temp (°C): &nbsp;30 &nbsp;54 &nbsp;80 &nbsp;80 &nbsp;80 &nbsp;96 &nbsp;118</span><br><br><strong>(a)</strong> State the melting point of the substance. <span class='num'>[1]</span><br><strong>(b)</strong> State how long the substance took to melt. <span class='num'>[1]</span><br><strong>(c)</strong> Describe what is happening to the particles between 4 and 8 minutes. <span class='num'>[1]</span>",
  hints:["A pure substance melts at one fixed temperature. Look for the reading that appears more than once.",
         "The melting is happening for as long as the temperature refuses to change — find the first and last times at that temperature.",
         "During that stretch the energy is not speeding the particles up. So what else could it possibly be doing?"],
  sol:["(a) <strong>80 °C</strong> — the temperature stops rising and holds there, which is what melting looks like on a table of readings.",
       "(b) From 4 minutes to 8 minutes, so <strong>4 minutes</strong>.",
       "(c) The energy going in is breaking the forces holding the particles in their fixed pattern, so the particles are becoming free to slide past each other instead of speeding up. The substance is changing from solid to liquid, and the temperature stays at 80 °C throughout.",
       "Worth noticing: the readings climb 24 degrees in the first two minutes and 22 in the last two, so the heater was working just as hard during the flat section."]},

 {n:12, lvl:"standard", m:3, q:"20 g of ice at −5 °C is left in a sealed, rigid container in a warm room until everything inside has become steam.<br><br><strong>(a)</strong> State the mass of steam produced. <span class='num'>[1]</span><br><strong>(b)</strong> Explain your answer in terms of particles. <span class='num'>[1]</span><br><strong>(c)</strong> Explain why the pressure inside the sealed container rises sharply. <span class='num'>[1]</span>",
  hints:["Did any particles get into or out of the container?",
         "A change of state is a physical change — count the particles before and after.",
         "For (c), think about what gas particles do to the walls, and how that changes when a liquid becomes a gas in a container that cannot grow."],
  sol:["(a) <strong>20 g.</strong>",
       "(b) Melting and boiling are physical changes: the same particles are still present, just arranged differently and moving faster. Nothing entered or left the sealed container, so the total mass cannot change.",
       "(c) As a gas, the particles are free, fast and spread throughout the whole container, so they collide with the walls hard and very frequently. The container cannot expand, so those collisions produce a much higher pressure than the liquid did.",
       "The trap here is answering (a) with a smaller number because the water \"disappeared\". Invisible is not the same as absent."]},

 {n:13, lvl:"hard", m:3, q:"A drop of ink is placed carefully at the bottom of a tall glass of still water. Nobody stirs it. Two days later the whole glass is evenly coloured.<br><br><strong>(a)</strong> Name the process. <span class='num'>[1]</span><br><strong>(b)</strong> Explain how the ink reached the top without anything stirring it. <span class='num'>[1]</span><br><strong>(c)</strong> State and explain <strong>one</strong> change that would make it happen faster. <span class='num'>[1]</span>",
  hints:["The name is one word, and it means spreading from crowded to less crowded.",
         "Water particles are not still, even in \"still\" water. What are they doing, and what does that do to the ink particles?",
         "For (c), anything that makes particles move faster will speed it up. Say what the change is and why it works."],
  sol:["(a) <strong>Diffusion.</strong>",
       "(b) The particles in the water and the ink are in constant random motion, colliding with each other. Because the ink starts crowded in one place, random movement carries more ink particles outwards than back, so over time they spread until they are evenly mixed.",
       "(c) Warming the water. The particles gain energy and move faster, so they collide and spread more quickly and the mixing takes less time. (Accept: using a shallower container, or a liquid where particles move more freely.)",
       "The phrase examiners look for in (b) is \"random motion of the particles\". \"It just spread out\" describes the result rather than explaining it, and scores nothing."]},

 {n:14, lvl:"hard", m:3, q:"On a cold, windy day a puddle of water dries up completely, even though the air temperature never rises above 9 °C.<br><br><strong>(a)</strong> Name the process, and explain how water can become a gas so far below 100 °C. <span class='num'>[1]</span><br><strong>(b)</strong> Explain why the wind makes it happen faster. <span class='num'>[1]</span><br><strong>(c)</strong> The ground under the puddle ends up slightly colder than the ground beside it. Explain why. <span class='num'>[1]</span>",
  hints:["Not every particle in a liquid moves at the same speed. What can the fastest ones at the surface do?",
         "Escaped particles do not always stay escaped. What does wind do to them before they can come back?",
         "If the fastest particles are the ones that leave, what happens to the average speed of the particles left behind — and what is average speed a measure of?"],
  sol:["(a) <strong>Evaporation.</strong> The particles in the puddle have a range of speeds. The fastest ones at the surface have enough energy to overcome the forces holding them in the liquid and escape as a gas, and this can happen at any temperature — boiling is not required.",
       "(b) Wind carries the escaped water particles away from just above the surface, so far fewer of them are recaptured by the liquid, and the puddle loses particles faster overall.",
       "(c) Only the fastest particles escape, so the average speed of the particles remaining falls. Temperature is a measure of average particle speed, so the water — and the ground it is in contact with — cools down.",
       "Part (c) is the same physics as sweating. If you can explain the puddle, you can explain why you feel cold getting out of a swimming pool."]},

 {n:15, lvl:"hard", m:3, q:"A long glass tube has cotton wool soaked in <strong>ammonia</strong> pushed into one end and cotton wool soaked in <strong>hydrogen chloride</strong> pushed into the other, at the same moment. Both give off gases. After a few minutes a white ring of solid ammonium chloride forms inside the tube — but it forms closer to the hydrogen chloride end, not in the middle.<br><br><strong>(a)</strong> Explain how the two gases travelled along the tube. <span class='num'>[1]</span><br><strong>(b)</strong> Explain why the ring does not form in the middle. <span class='num'>[1]</span><br><strong>(c)</strong> Predict, with a reason, what would happen to the position of the ring if the whole experiment were repeated in a warmer room. <span class='num'>[1]</span>",
  hints:["Nothing pushed the gases. The name of the process is the same one from Q13.",
         "The ring forms where the two gases meet. If it is nearer one end, one gas must have covered more of the tube — so one gas travelled faster. Which one, and what is different about its particles?",
         "For (c), warming speeds up <em>both</em> gases. Ask yourself whether it speeds them up by the same proportion, and therefore whether the meeting point moves or just arrives sooner."],
  sol:["(a) By <strong>diffusion</strong>. The gas particles are in constant random motion and spread out from where they are concentrated at each end towards the empty space in the middle of the tube.",
       "(b) The ring forms where the two gases meet. Ammonia particles are lighter than hydrogen chloride particles, so at the same temperature they travel faster and cover more of the tube in the same time. The meeting point is therefore nearer the hydrogen chloride end.",
       "(c) The ring would form in <strong>about the same place, but sooner</strong>. Warming gives both gases more energy so both diffuse faster, but ammonia is still the lighter and faster of the two by the same proportion, so the position where they meet is essentially unchanged.",
       "Part (c) is the one that separates a 26 from a 21. The instinct is to say the ring moves, because \"faster\" feels like it should change the position. Both gases speed up, so the race is still won by the same margin."]}
];
"""

TOOLS = r"""
/* ================= HERO 1: the particle box ================= */
const BOX = {x0:40, y0:30, x1:460, y1:250};
const RAD = 9, NP = 36, LIQ_TOP = 132;
const parts = [];
const partsG = document.getElementById('parts');
const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

for(let i=0;i<NP;i++){
  const c = i%6, r = Math.floor(i/6);
  const hx = 172 + c*26 + 13, hy = 94 + r*26 + 13;
  let vx = Math.random()*2-1, vy = Math.random()*2-1;
  const s = Math.hypot(vx,vy) || 1;
  const el = document.createElementNS('http://www.w3.org/2000/svg','circle');
  el.setAttribute('r', RAD);
  el.setAttribute('cx', hx); el.setAttribute('cy', hy);
  partsG.appendChild(el);
  parts.push({hx, hy, x:hx, y:hy, vx:vx/s, vy:vy/s, ph:Math.random()*6.283, el});
}

let temp = -20;
function stateOf(t){ return t < 0 ? 'solid' : (t < 100 ? 'liquid' : 'gas'); }

const STATE_TEXT = {
  solid:{pill:'Solid', cls:'sol', arr:['Regular','fixed pattern, particles touching'],
    mov:['Vibrating','about fixed positions, never still'],
    spa:['Very close','strong forces hold them in place'],
    note:'Ice. Fixed shape and fixed volume — the particles cannot get past each other, so the whole block keeps its shape.'},
  liquid:{pill:'Liquid', cls:'liq', arr:['Jumbled','still touching, but no pattern'],
    mov:['Sliding','past each other, in all directions'],
    spa:['Close','weaker forces — they can move but not escape'],
    note:'Water. Fixed volume but no fixed shape: it flows into the bottom of whatever holds it, and it can barely be squashed because the particles already touch.'},
  gas:{pill:'Gas', cls:'gas', arr:['Random','spread out, no pattern at all'],
    mov:['Fast and random','in every direction, colliding with the walls'],
    spa:['Far apart','almost no forces between them'],
    note:'Steam. No fixed shape and no fixed volume — it fills the whole container, and all that empty space is why a gas can be compressed.'}
};

function paintBox(){
  const st = stateOf(temp);
  const T = STATE_TEXT[st];
  const col = st==='solid' ? 'var(--sol)' : (st==='liquid' ? 'var(--liq)' : 'var(--gas)');
  parts.forEach(p=>{ p.el.setAttribute('fill', col); p.el.setAttribute('fill-opacity', st==='gas'?'0.85':'1'); });

  document.getElementById('pb-arr').textContent = T.arr[0];
  document.getElementById('pb-arrs').textContent = T.arr[1];
  document.getElementById('pb-mov').textContent = T.mov[0];
  document.getElementById('pb-movs').textContent = T.mov[1];
  document.getElementById('pb-spa').textContent = T.spa[0];
  document.getElementById('pb-spas').textContent = T.spa[1];

  const pill = document.getElementById('pb-pill');
  pill.className = 'pill ' + T.cls;
  let note = T.note;
  if(temp === 0){ pill.textContent = 'At the melting point'; note = 'Exactly 0 °C. Add energy here and the temperature will not move — every joule goes into breaking the pattern apart instead.'; }
  else if(temp === 100){ pill.textContent = 'At the boiling point'; note = 'Exactly 100 °C. The longest flat section of the heating curve starts right here, and it takes nearly seven times as much energy as melting did.'; }
  else pill.textContent = T.pill;
  document.getElementById('pb-note').textContent = note;
  document.getElementById('tempval').textContent = temp + ' °C';
}

function stepBox(now){
  const st = stateOf(temp);
  if(st === 'solid'){
    const amp = 1.1 + (temp + 30) / 30 * 1.5;
    parts.forEach(p=>{
      p.x = p.hx + amp * Math.sin(now*0.004 + p.ph);
      p.y = p.hy + amp * Math.cos(now*0.005 + p.ph);
    });
  } else {
    const top = st === 'liquid' ? LIQ_TOP : BOX.y0;
    const sp  = st === 'liquid' ? 0.5 + temp/100*0.9 : 1.9 + (temp-100)/60;
    parts.forEach(p=>{
      p.x += p.vx * sp; p.y += p.vy * sp;
      if(p.x < BOX.x0+RAD){ p.x = BOX.x0+RAD; p.vx *= -1; }
      if(p.x > BOX.x1-RAD){ p.x = BOX.x1-RAD; p.vx *= -1; }
      if(p.y < top+RAD){ p.y = top+RAD; p.vy *= -1; }
      if(p.y > BOX.y1-RAD){ p.y = BOX.y1-RAD; p.vy *= -1; }
      if(st === 'liquid' && Math.random() < 0.04){
        p.vx += (Math.random()-0.5)*0.5; p.vy += (Math.random()-0.5)*0.5;
        const s = Math.hypot(p.vx,p.vy) || 1; p.vx /= s; p.vy /= s;
      }
    });
  }
  parts.forEach(p=>{ p.el.setAttribute('cx', p.x.toFixed(1)); p.el.setAttribute('cy', p.y.toFixed(1)); });
}

function frame(now){ stepBox(now); requestAnimationFrame(frame); }

const tempSlider = document.getElementById('temp');
tempSlider.addEventListener('input', ()=>{ temp = +tempSlider.value; paintBox(); if(reduceMotion) stepBox(performance.now()); });
document.querySelectorAll('[data-temp]').forEach(b=>{
  b.addEventListener('click', ()=>{ temp = +b.dataset.temp; tempSlider.value = temp; paintBox(); if(reduceMotion) stepBox(performance.now()); });
});

/* --- box puzzles: set the machine to match a description --- */
const BOX_PUZZLES = [
 {ask:"Set the box to the state that has a <strong>fixed volume but no fixed shape</strong>.", want:'liquid',
  why:"A liquid keeps its volume but flows into the shape of its container."},
 {ask:"Set the box to the state whose particles <strong>vibrate about fixed positions</strong>.", want:'solid',
  why:"Only in a solid are the particles locked into a pattern — but they still vibrate."},
 {ask:"Set the box to the state that can be <strong>compressed easily</strong>.", want:'gas',
  why:"Only a gas has large spaces between the particles for you to squash out."},
 {ask:"Set the box to the state in which particles <strong>touch but are jumbled up</strong>.", want:'liquid',
  why:"Touching rules out a gas; jumbled rules out a solid."},
 {ask:"Set the box to the state whose particles <strong>collide with the container walls constantly</strong>.", want:'gas',
  why:"Those collisions are what gas pressure actually is."}
];
let boxQ = null;
document.getElementById('boxPuzzle').addEventListener('click', ()=>{
  boxQ = BOX_PUZZLES[Math.floor(Math.random()*BOX_PUZZLES.length)];
  const box = document.getElementById('boxQuiz');
  box.classList.add('on');
  box.innerHTML = '<strong>Puzzle.</strong> ' + boxQ.ask +
    '<div class="qrow"><button class="btn ghost small" type="button" id="boxCheck">Check the box</button>' +
    '<span id="boxFb" class="num" style="font-size:13px"></span></div>';
  document.getElementById('boxCheck').addEventListener('click', ()=>{
    const got = stateOf(temp);
    const fb = document.getElementById('boxFb');
    if(got === boxQ.want){
      fb.style.color = 'var(--ok)';
      fb.textContent = 'Correct — ' + boxQ.why;
      S.puzzles = (S.puzzles||0) + 1; save(); refresh();
      document.getElementById('boxCheck').disabled = true;
    } else {
      fb.style.color = 'var(--no)';
      fb.textContent = 'That is a ' + got + '. Try again.';
    }
  });
});

/* ================= HERO 2: the heating curve ================= */
/* real energies for 1 kg of water, so the flat sections are honestly proportioned */
const E = {ice:2.1*20, melt:334, water:4.18*100, boil:2260, steam:2.0*20};
const ETOT = E.ice + E.melt + E.water + E.boil + E.steam;
const C1 = E.ice/ETOT;
const C2 = C1 + E.melt/ETOT;
const C3 = C2 + E.water/ETOT;
const C4 = C3 + E.boil/ETOT;

const PX0 = 60, PX1 = 660, PY0 = 40, PY1 = 280;
function xOf(f){ return PX0 + f*(PX1-PX0); }
function yOf(t){ return PY1 - (t + 20)/140 * (PY1-PY0); }
function tempAt(f){
  if(f <= C1) return -20 + f/C1*20;
  if(f <= C2) return 0;
  if(f <= C3) return (f-C2)/(C3-C2)*100;
  if(f <= C4) return 100;
  return 100 + (f-C4)/(1-C4)*20;
}

/* gridlines at 0 and 100 °C */
(function(){
  const g = document.getElementById('hgrid-lines');
  [[0,'0 °C'],[100,'100 °C']].forEach(([t,lab])=>{
    const ln = document.createElementNS('http://www.w3.org/2000/svg','line');
    ln.setAttribute('x1', PX0); ln.setAttribute('x2', PX1);
    ln.setAttribute('y1', yOf(t)); ln.setAttribute('y2', yOf(t));
    ln.setAttribute('stroke','var(--line-soft)'); ln.setAttribute('stroke-width','1.5');
    ln.setAttribute('stroke-dasharray','4 5');
    g.appendChild(ln);
    const tx = document.createElementNS('http://www.w3.org/2000/svg','text');
    tx.setAttribute('x', 14); tx.setAttribute('y', yOf(t)+4);
    tx.setAttribute('font-family','var(--mono)'); tx.setAttribute('font-size','11');
    tx.setAttribute('fill','var(--ink-soft)');
    tx.textContent = lab;
    g.appendChild(tx);
  });
})();

const STEPS = 300;
(function(){
  let pts = [];
  for(let i=0;i<=STEPS;i++){ const f = i/STEPS; pts.push(xOf(f).toFixed(1)+','+yOf(tempAt(f)).toFixed(1)); }
  document.getElementById('hc-faint').setAttribute('points', pts.join(' '));
})();

const CURVE_PHASE = [
 {upto:()=>C1, name:'Heating the ice',  cls:'sol', col:'var(--sol)', state:['Solid','ice, below its melting point'],
  job:['Speeding up','the particles vibrate faster'], temps:'rising steadily',
  note:'Energy is going into particle speed, so the temperature climbs. This section is short — ice warms up easily.'},
 {upto:()=>C2, name:'Melting',          cls:'sol', col:'var(--liq)', state:['Solid + liquid','both at once, at 0 °C'],
  job:['Breaking the pattern','forces between particles are being broken'], temps:'not moving at all',
  note:'The heater is still on and the thermometer has stopped. Every joule is breaking particles out of the lattice, none is making them faster.'},
 {upto:()=>C3, name:'Heating the water',cls:'liq', col:'var(--liq)', state:['Liquid','water, between 0 and 100 °C'],
  job:['Speeding up','the particles slide faster'], temps:'rising steadily again',
  note:'Melting is finished, so the energy goes back into speed and the line climbs again.'},
 {upto:()=>C4, name:'Boiling',          cls:'gas', col:'var(--gas)', state:['Liquid + gas','both at once, at 100 °C'],
  job:['Separating particles','pulling them completely apart'], temps:'stuck at 100 °C',
  note:'This flat stretch is about three-quarters of the whole graph. Separating water particles completely takes nearly seven times the energy that melting did.'},
 {upto:()=>1,  name:'Heating the steam',cls:'gas', col:'var(--gas)', state:['Gas','steam, above 100 °C'],
  job:['Speeding up','the particles fly faster'], temps:'rising once more',
  note:'All liquid is gone. The energy goes into speed again, and steam heats up quickly.'}
];

let ef = 0;
function paintCurve(){
  const t = tempAt(ef);
  let ph = CURVE_PHASE[CURVE_PHASE.length-1];
  for(const p of CURVE_PHASE){ if(ef <= p.upto()){ ph = p; break; } }

  let pts = [];
  const n = Math.max(1, Math.round(ef*STEPS));
  for(let i=0;i<=n;i++){ const f = ef*i/n; pts.push(xOf(f).toFixed(1)+','+yOf(tempAt(f)).toFixed(1)); }
  const live = document.getElementById('hc-live');
  live.setAttribute('points', pts.join(' '));
  live.setAttribute('stroke', ph.col);
  const dot = document.getElementById('hc-dot');
  dot.setAttribute('cx', xOf(ef).toFixed(1));
  dot.setAttribute('cy', yOf(t).toFixed(1));
  dot.setAttribute('fill', ph.col);

  document.getElementById('hc-temp').textContent = (t<0?'−':'') + Math.abs(Math.round(t)) + ' °C';
  document.getElementById('hc-temps').textContent = ph.temps;
  document.getElementById('hc-state').textContent = ph.state[0];
  document.getElementById('hc-states').textContent = ph.state[1];
  document.getElementById('hc-job').textContent = ph.job[0];
  document.getElementById('hc-jobs').textContent = ph.job[1];
  const pill = document.getElementById('hc-pill');
  pill.className = 'pill ' + ph.cls;
  pill.textContent = ph.name;
  document.getElementById('hc-note').textContent = ph.note;
  document.getElementById('energyval').textContent = Math.round(ef*100) + '%';
}

const eSlider = document.getElementById('energy');
eSlider.addEventListener('input', ()=>{ ef = +eSlider.value/1000; paintCurve(); });

const CURVE_PUZZLES = [
 {ask:"Drag the energy slider to the exact moment the <strong>last of the ice has just melted</strong>.", target:()=>C2, tol:0.02,
  why:"That is where the first flat section ends and the line starts climbing again."},
 {ask:"Drag the slider to the point where the water is at <strong>50 °C</strong>.", target:()=>C2+(C3-C2)*0.5, tol:0.012,
  why:"Halfway along the sloped section between melting and boiling."},
 {ask:"Drag the slider to the moment the <strong>last drop of water has just boiled away</strong>.", target:()=>C4, tol:0.025,
  why:"The end of the long flat section — and notice how far along the graph that is."},
 {ask:"Drag the slider to a point where <strong>solid and liquid exist at the same time</strong>.", target:()=>(C1+C2)/2, tol:(C2-C1)/2,
  why:"Anywhere on the first flat section: the substance is part melted."}
];
let curveQ = null;
document.getElementById('curvePuzzle').addEventListener('click', ()=>{
  curveQ = CURVE_PUZZLES[Math.floor(Math.random()*CURVE_PUZZLES.length)];
  const box = document.getElementById('curveQuiz');
  box.classList.add('on');
  box.innerHTML = '<strong>Puzzle.</strong> ' + curveQ.ask +
    '<div class="qrow"><button class="btn ghost small" type="button" id="curveCheck">Check my position</button>' +
    '<span id="curveFb" class="num" style="font-size:13px"></span></div>';
  document.getElementById('curveCheck').addEventListener('click', ()=>{
    const fb = document.getElementById('curveFb');
    if(Math.abs(ef - curveQ.target()) <= curveQ.tol){
      fb.style.color = 'var(--ok)';
      fb.textContent = 'Correct — ' + curveQ.why;
      S.puzzles = (S.puzzles||0) + 1; save(); refresh();
      document.getElementById('curveCheck').disabled = true;
    } else {
      fb.style.color = 'var(--no)';
      fb.textContent = ef < curveQ.target() ? 'Not far enough along. Keep going.' : 'Too far along. Come back a little.';
    }
  });
});

function boot(){
  paintBox();
  paintCurve();
  if(reduceMotion) stepBox(0); else requestAnimationFrame(frame);
}
"""

html = page(
    title="Small Bits, Always Moving — Grade 7 IGCSE Chemistry",
    root_css=ROOT, extra_css=EXTRA, mast=MAST, nav=NAV, heroes=HEROES,
    question_note="No notes, no looking back at the lessons.",
    traps=TRAPS, papers=PAPERS, data_js=DATA, tools_js=TOOLS,
    key='particles-progress-v1', pid='particles', subject='chemistry',
    hubtitle='Small Bits, Always Moving')

io.open(os.path.join(REPO,'particles.html'),'w',encoding='utf-8').write(html)
print('written', len(html))
