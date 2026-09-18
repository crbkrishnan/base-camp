# -*- coding: utf-8 -*-
# Content module for separating.html — Chemistry 5.2, separating mixtures.
ID = 'separating'
TITLE = 'Take It Apart — Grade 7 IGCSE Chemistry'
BRIDGE_TITLE = 'Take It Apart'

MANIFEST = '''<script type="application/json" id="hub-card">
{
  "id": "separating",
  "file": "separating.html",
  "subject": "chemistry",
  "status": "ready",
  "papers": 4,
  "title": "Take It Apart",
  "sub": "Chemistry · separating mixtures",
  "blurb": "Plan a separation step by step on a bench that actually runs it — filter salt water and watch nothing happen — then run a chromatogram, read the distances off the paper and work out Rf yourself. Filtration, evaporation, distillation and chromatography, with the reasons that earn the marks.",
  "meta": ["30 marks", "6 lessons", "separation bench"]
}
</script>'''

ROOT_CSS = ''':root{
  --ink:#1A1A22;
  --ink-soft:#575463;
  --paper:#ECEAE4;
  --card:#FFFFFF;
  --line:#D8D2C6;
  --line-soft:#E8E3DA;
  --sd:#2B4E9B;         /* solid / residue — always indigo */
  --sd-tint:#E9EDF7;
  --lq:#0E7C6B;         /* liquid / filtrate — always green-teal */
  --lq-tint:#E2F1EE;
  --vp:#B4560B;         /* vapour / solvent front — always amber */
  --vp-tint:#FBEFE3;
  --fr:var(--sd);  --fr-tint:var(--sd-tint);
  --de:var(--lq);  --de-tint:var(--lq-tint);
  --pc:var(--vp);  --pc-tint:var(--vp-tint);
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
}'''

EXTRA_CSS = '''nav.jump{background:rgba(236,234,228,.93)}
.sdtxt{color:var(--sd);font-weight:700}
.lqtxt{color:var(--lq);font-weight:700}
.vptxt{color:var(--vp);font-weight:700}
.pill.sd{background:var(--sd-tint);color:var(--sd)}
.pill.lq{background:var(--lq-tint);color:var(--lq)}
.pill.vp{background:var(--vp-tint);color:var(--vp)}
.chips{display:flex;gap:8px;flex-wrap:wrap;padding:12px 16px;border-top:1px solid var(--line);align-items:center}
.chips .lab{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft);flex:0 0 100%}
.chip{font-family:var(--display);font-weight:700;font-size:13px;cursor:pointer;border-radius:99px;padding:7px 13px;
  border:1px solid var(--line);background:var(--paper);color:var(--ink)}
.chip.on{border-color:var(--ink);background:var(--card);box-shadow:inset 0 0 0 1px var(--ink)}
.chip:disabled{opacity:.45;cursor:default}
.steps{display:flex;gap:6px;flex-wrap:wrap;align-items:center;font-family:var(--mono);font-size:12.5px}
.steps .st{background:var(--paper);border:1px solid var(--line);border-radius:8px;padding:4px 9px}
.steps .st.bad{border-color:var(--no);color:var(--no);background:var(--no-tint)}
.rfin{font-family:var(--mono);font-size:15px;width:90px;padding:7px 9px;border:1px solid var(--line);border-radius:9px;background:var(--paper);color:var(--ink)}'''

BODY_HTML = r'''<a href="index.html" style="display:inline-block;margin:22px 0 -20px;font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;color:var(--ink-soft);border:1px solid var(--line);border-radius:99px;padding:6px 14px;background:var(--card)">&larr;&nbsp; Base camp</a>

<header class="mast">
  <div class="eyebrow">IGCSE Chemistry · Grade 7 · Unit 5.2 · Separating mixtures</div>
  <h1>Take It <b>Apart</b></h1>
  <p class="lede">A mixture is two or more substances that are not joined to each other, and each one keeps its own properties. So to separate a mixture you find <strong>one property that differs</strong> — one dissolves and the other does not, one boils first, one sticks to a magnet — and build the method around it. Every technique on this page is that one idea wearing different apparatus.</p>

  <div class="target">
    <strong>The deal.</strong> You've been landing around <span class="num">10 out of 15</span>. This page is out of <span class="num">30</span>, so the honest target is <span class="num">21</span> on the first pass and <span class="num">26</span> on the second. The marks here are for <em>why</em> a method works, not for naming it — "filter it" is one mark, "filter it because sand is insoluble and cannot pass through the paper, but the dissolved salt can" is three.
  </div>

  <div class="strip">
    <div class="stat"><b class="num" id="s-marks">0<span style="font-size:15px;color:var(--ink-soft)">/30</span></b><span>marks banked</span><div class="bar"><i id="bar-marks"></i></div></div>
    <div class="stat"><b class="num" id="s-lessons">0<span style="font-size:15px;color:var(--ink-soft)">/6</span></b><span>lessons finished</span><div class="bar"><i id="bar-lessons"></i></div></div>
    <div class="stat"><b class="num" id="s-puzzles">0</b><span>machine puzzles solved</span><div class="bar"><i id="bar-puzzles"></i></div></div>
  </div>
</header>

<nav class="jump" aria-label="Sections">
  <a href="#bench">Separation bench</a>
  <a href="#videos">6 videos</a>
  <a href="#lessons">6 lessons</a>
  <a href="#chrom">Chromatography</a>
  <a href="#quick">Quick checks</a>
  <a href="#short">Short answers</a>
  <a href="#word">Word problems</a>
  <a href="#traps">Exam traps</a>
  <a href="#papers">Test papers</a>
</nav>


<!-- ============ HERO 1: THE SEPARATION BENCH ============ -->
<section id="bench">
  <div class="panel">
    <div class="panel-top">
      <h2>The separation bench</h2>
      <p>Pick a mixture, then add steps one at a time. The bench runs each step honestly: filter salt water and the salt goes straight through; try a magnet on sand and nothing moves. Some mixtures need three steps in the right order, and the order is the whole question.</p>
    </div>

    <div class="chips" id="mixChips"><span class="lab">Start with</span></div>
    <div class="chips" id="stepChips" style="border-top:1px solid var(--line-soft)"><span class="lab">Then do this</span></div>

    <svg class="stage" id="benchSvg" viewBox="0 0 500 240" role="img" aria-label="A beaker showing what is left of the mixture, and a tray showing what has been collected">
      <text x="60" y="22" font-family="var(--mono)" font-size="12" fill="var(--ink-soft)">STILL IN THE BEAKER</text>
      <path d="M70 40 L70 200 Q70 214 84 214 L196 214 Q210 214 210 200 L210 40" fill="none" stroke="var(--ink)" stroke-width="2.5"/>
      <g id="beakerContents"></g>
      <text x="290" y="22" font-family="var(--mono)" font-size="12" fill="var(--ink-soft)">COLLECTED</text>
      <rect x="280" y="40" width="190" height="174" rx="8" fill="var(--paper)" stroke="var(--line)" stroke-width="2"/>
      <g id="trayContents"></g>
    </svg>

    <div class="rows">
      <div class="cell f"><div class="lab">In the beaker</div><div class="val" id="bn-beaker" style="font-size:16px">sand, water</div><div class="sub" id="bn-beakers">a solid and a liquid</div></div>
      <div class="cell d"><div class="lab">Collected</div><div class="val" id="bn-tray" style="font-size:16px">nothing yet</div><div class="sub" id="bn-trays">add a step</div></div>
      <div class="cell p"><div class="lab">Steps so far</div><div class="val"><div class="steps" id="bn-steps"><span class="st">none</span></div></div><div class="sub"><button class="btn ghost small" type="button" id="benchUndo" style="margin-top:6px">Undo last step</button></div></div>
      <div class="phasebar">
        <span class="pill sd" id="bn-pill">Mixture</span>
        <span id="bn-note">Sand does not dissolve, so it sits in the water as separate grains. Which property differs — and which step uses it?</span>
        <span class="push"><button class="btn ghost" type="button" id="benchPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="benchQuiz"></div>
    </div>
  </div>
</section>

<!-- ============ VIDEOS ============ -->
<section id="videos">
  <div class="shead"><h2>Watch these six, in this order</h2><span class="tag">~30 min total</span></div>
  <p class="snote">Each video comes with one small written job. Do the job, or the video was a screensaver with chemistry on it. If you are not going to write the lines underneath, close the video and go straight to the questions instead — that is a legitimate choice.</p>
  <div id="videoList"></div>
</section>

<!-- ============ LESSONS ============ -->
<section id="lessons">
  <div class="shead"><h2>Six lessons</h2><span class="tag">~35 min total</span></div>
  <div id="lessonList"></div>
</section>

<!-- ============ HERO 2: THE CHROMATOGRAM ============ -->
<section id="chrom">
  <div class="panel">
    <div class="panel-top">
      <h2>The chromatogram</h2>
      <p>Three known dyes and one unknown ink on the same paper. Raise the solvent and every spot moves — each at its own fraction of the solvent's speed. The paper shows you distances; the machine does <em>not</em> show you R<sub>f</sub> unless you ask, because working it out is the skill being tested.</p>
    </div>

    <svg class="stage" id="chromSvg" viewBox="0 0 700 340" role="img" aria-label="A chromatography paper with four lanes, a pencil baseline and a solvent front that rises with the slider">
      <rect x="140" y="20" width="420" height="290" fill="#FBFAF6" stroke="var(--line)" stroke-width="2"/>
      <rect id="wet" x="141" y="290" width="418" height="0" fill="var(--vp-tint)" opacity=".7"/>
      <line x1="140" y1="290" x2="560" y2="290" stroke="var(--ink-soft)" stroke-width="1.5" stroke-dasharray="5 4"/>
      <text x="565" y="294" font-family="var(--mono)" font-size="11" fill="var(--ink-soft)">baseline</text>
      <line id="front" x1="140" y1="290" x2="560" y2="290" stroke="var(--vp)" stroke-width="2"/>
      <text id="frontLab" x="565" y="294" font-family="var(--mono)" font-size="11" fill="var(--vp)"></text>
      <g id="ruler"></g>
      <g id="lanes"></g>
    </svg>

    <div class="ctrl">
      <label for="solv">Solvent front</label>
      <input id="solv" type="range" min="0" max="120" value="0" step="1" aria-label="Distance the solvent front has travelled from the baseline, in millimetres">
      <span class="num" id="solvval" style="min-width:76px;text-align:right">0.0 cm</span>
      <button class="btn ghost small" type="button" id="showRf" aria-pressed="false">Show R<sub>f</sub> values</button>
    </div>

    <div class="rows">
      <div class="cell f"><div class="lab">Solvent front</div><div class="val" id="ch-front">0.0 cm</div><div class="sub">measured from the baseline</div></div>
      <div class="cell d"><div class="lab">Spot distances</div><div class="val" id="ch-spots" style="font-size:15px">—</div><div class="sub" id="ch-spotss">red · green · blue</div></div>
      <div class="cell p"><div class="lab">R<sub>f</sub> values</div><div class="val" id="ch-rf" style="font-size:15px">hidden</div><div class="sub">distance moved by spot ÷ distance moved by solvent</div></div>
      <div class="phasebar">
        <span class="pill vp" id="ch-pill">Dry paper</span>
        <span id="ch-note">Raise the solvent. Watch which spot keeps up with it and which one barely leaves the line.</span>
        <span class="push"><button class="btn ghost" type="button" id="chromPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="chromQuiz"></div>
    </div>
  </div>
</section>



<section id="quick">
  <div class="shead"><h2>Quick checks</h2><span class="tag">Q1–Q5 · 5 marks</span></div>
  <p class="snote">One try each, and the feedback tells you why. No notes, no looking back at the lessons. These are the five marks you should never drop.</p>
  <div id="mcqList"></div>
</section>

<section id="short">
  <div class="shead"><h2>Short answers</h2><span class="tag">Q6–Q10 · 10 marks</span></div>
  <p class="snote">Write your answer first, <em>then</em> open the mark scheme and mark yourself honestly. Marks only count if you write your answer before opening the scheme — otherwise you're just reading, and reading feels like learning without being learning.</p>
  <div id="shortList"></div>
</section>

<section id="word">
  <div class="shead"><h2>Word problems</h2><span class="tag">Q11–Q15 · 15 marks</span></div>
  <p class="snote">Stuck? Take one hint, not the whole solution. A hint costs you nothing; reading the answer costs you the question. Q14 and Q15 are the two that separate a 21 from a 26.</p>
  <div id="wordList"></div>
</section>



<section id="traps">
  <div class="shead"><h2>Five traps</h2><span class="tag">Read before any test</span></div>
  <div class="traps">
    <div class="trap"><h4>Filtering salt water to get the salt</h4><p>Dissolved salt is broken up into particles far smaller than the holes in filter paper, and they pass straight through with the water. Filtration only catches <em>insoluble</em> solids. If the solid has dissolved, you need evaporation to get the solid or distillation to get the liquid. The bench above will show you the salt going through.</p></div>
    <div class="trap"><h4>Evaporating sea water to get pure water</h4><p>Evaporation loses the water into the air and leaves the salt behind — it gives you the <em>solid</em>. If the question asks for the <em>liquid</em>, the answer is distillation, where the vapour is cooled in a condenser and collected. Ask yourself which part you have been asked to keep before you choose.</p></div>
    <div class="trap"><h4>Drawing the chromatography baseline in ink</h4><p>Ink is a mixture of dyes and dissolves in the solvent, so an ink baseline runs up the paper and ruins the result. The baseline is drawn in <strong>pencil</strong> — graphite is insoluble. And the solvent level must start <em>below</em> the baseline, or the spots wash off into the solvent instead of travelling up the paper.</p></div>
    <div class="trap"><h4>Getting R<sub>f</sub> upside down</h4><p>R<sub>f</sub> = distance moved by the <strong>spot</strong> ÷ distance moved by the <strong>solvent</strong>. Both distances from the baseline. Because the spot can never overtake the solvent, R<sub>f</sub> is always between 0 and 1. If you get 1.6, you divided the wrong way round — and an examiner will not award a mark for an R<sub>f</sub> greater than 1.</p></div>
    <div class="trap"><h4>Naming the method and stopping</h4><p>"Use a magnet" is one mark. Why does it work? Because iron is magnetic and sand is not — each substance in a mixture keeps its own properties, and the method exploits the one that differs. Every method answer should name the property that is different. That sentence is usually the second and third marks.</p></div>
  </div>
</section>



<section id="papers">
  <div class="shead"><h2>The four test papers</h2><span class="tag">30 marks each</span></div>
  <p class="snote">These are the printed papers that go with this page. Do them on paper, timed, with your phone in another room. Medium first; only move to the hard papers once you're clearing 21 on a medium one.</p>
  <div class="papers">
    <a class="paper" href="sheets/chemistry-separating-paper-a.pdf" download><span class="pn">A</span><span class="pt">Paper A — Medium</span><span class="num" style="color:var(--ink-soft);font-size:13px">35 min</span>
      <p class="pd">Matching methods to mixtures, the words residue and filtrate, labelling the filtration and evaporation apparatus, and explaining why each method works.</p></a>
    <a class="paper" href="sheets/chemistry-separating-paper-b.pdf" download><span class="pn">B</span><span class="pt">Paper B — Medium</span><span class="num" style="color:var(--ink-soft);font-size:13px">35 min</span>
      <p class="pd">Simple distillation step by step, a chromatogram to read and R<sub>f</sub> values to calculate, and the salt-and-sand three-step separation.</p></a>
    <a class="paper" href="sheets/chemistry-separating-paper-c.pdf" download><span class="pn hard">C</span><span class="pt">Paper C — Hard</span><span class="num" style="color:var(--ink-soft);font-size:13px">45 min</span>
      <p class="pd">Choosing and justifying methods for unfamiliar mixtures, chromatography of a food dye with an unknown to identify, and what goes wrong when the apparatus is set up badly.</p></a>
    <a class="paper" href="sheets/chemistry-separating-paper-d.pdf" download><span class="pn hard">D</span><span class="pt">Paper D — Hard</span><span class="num" style="color:var(--ink-soft);font-size:13px">45 min</span>
      <p class="pd">Multi-step problems: planning a full separation of a three-part mixture, R<sub>f</sub> in reverse, a six-mark distillation explanation, and two wrong answers to diagnose and correct.</p></a>
  </div>
</section>



<footer>
  <span>Your answers, marks and finished lessons are saved on this device.</span>
  <button class="btn ghost" type="button" id="resetBtn" style="margin-left:auto">Reset my progress</button>
</footer>
'''

DATA_JS = r'''/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"How To Separate Solutions, Mixtures & Emulsions", ch:"FuseSchool", url:"https://www.youtube.com/watch?v=XC1RxloV0Mo",
  why:"The overview: every technique on this page in one pass, each tied to the property it exploits. Watch it first so the rest have somewhere to go.",
  task:"Draw a two-column table: method on the left, the property that differs on the right. Fill in every method the video names. If a row's right-hand side is blank, you do not yet understand that method."},

 {t:"Separating Mixtures: Filtration and Crystallisation", ch:"Freesciencelessons", url:"https://www.youtube.com/watch?v=cSOb9HlhPDQ",
  why:"Filtration and crystallisation at exam pitch, with the two words that examiners insist on: residue and filtrate. Q6 and Q7 are lifted from here.",
  task:"Write the definitions of residue and filtrate in one line each. Then write why salt water gives no residue — using the word 'dissolved'."},

 {t:"GCSE Chemistry Revision — Simple Distillation", ch:"Freesciencelessons", url:"https://www.youtube.com/watch?v=wXxFg7tdPjw",
  why:"Distillation is the technique students describe worst, because it has four stages and they usually write two. He does all four, slowly, in order.",
  task:"Write the four stages as four numbered lines: what happens to the liquid, to the vapour, in the condenser, and in the receiving flask. Each line must name a change of state."},

 {t:"GCSE Chemistry — Paper Chromatography", ch:"Cognito", url:"https://www.youtube.com/watch?v=TdJ57SQ6GAQ",
  why:"The method, the reasons behind each rule (pencil baseline, solvent below the line), and how to read a chromatogram. Everything the machine below does, explained.",
  task:"Write down the two set-up rules and the reason for each. Then explain in one sentence why a more soluble dye ends up higher on the paper."},

 {t:"Chromatograms & Calculating Rf Values", ch:"KayScience", url:"https://www.youtube.com/watch?v=X1DdTOTRa28",
  why:"The one calculation in this topic, worked through on real chromatograms. Short enough that you have no excuse for getting R<sub>f</sub> upside down in the papers.",
  task:"Write the formula. Then invent a spot distance and a solvent distance, calculate the R<sub>f</sub>, and check that the answer is less than 1. If it is not, you have divided the wrong way."},

 {t:"Paper & Thin Layer Chromatography", ch:"FuseSchool", url:"https://www.youtube.com/watch?v=ByJ6lzD2Vbg",
  why:"Goes one step further than Grade 7 — what the paper and solvent are actually doing to the dyes — which is the explanation behind 'more soluble goes further'. Stop when it moves to thin-layer plates if you like.",
  task:"Finish this sentence in writing: 'A dye that is more soluble in the solvent travels further because…' Then finish: 'A dye that is more attracted to the paper travels less far because…'"}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"One idea: find the property that differs", len:"5 min",
  body:`<p>In a mixture nothing is chemically joined, so <strong>every substance keeps its own properties</strong>. Sand in water is still sand: insoluble, gritty, heavy. Salt in water is still salt: soluble, and it comes back as crystals if you take the water away. A separation method is nothing more than a way of using one property that one substance has and the other does not.</p>
        <table class="data">
          <tr><th>The property that differs</th><th>Method</th><th>Example</th></tr>
          <tr><td>one solid is insoluble, the liquid is not</td><td><strong>filtration</strong></td><td>sand from water</td></tr>
          <tr><td>a solid is dissolved and you want the <em>solid</em></td><td><strong>evaporation / crystallisation</strong></td><td>salt from sea water</td></tr>
          <tr><td>a solid is dissolved and you want the <em>liquid</em></td><td><strong>simple distillation</strong></td><td>pure water from sea water</td></tr>
          <tr><td>several dissolved substances, different solubilities</td><td><strong>chromatography</strong></td><td>the dyes in ink</td></tr>
          <tr><td>one solid is magnetic</td><td><strong>magnet</strong></td><td>iron filings from sand</td></tr>
          <tr><td>two liquids that do not mix</td><td><strong>separating funnel</strong></td><td>oil from water</td></tr>
          <tr><td>solid pieces of different sizes</td><td><strong>sieving</strong></td><td>stones from sand</td></tr>
        </table>
        <p>Read the left-hand column twice. In an exam, the method is the easy mark; the property is where the other two marks live. "Filter it" scores one. "Filter it, because the sand is insoluble and is trapped by the paper while the water passes through" scores three.</p>`,
  demo:`<strong>Do this:</strong> take four things from the kitchen — say rice, salt, oil and water — and write which pairs you could separate, by what method, and the property you would be using. There are six pairs.`,
  cliff:`Sand in water: filter it. Salt in water: filter it? Try that on the bench above and watch where the salt goes.`},

 {t:"Filtration, residue and filtrate", len:"6 min",
  body:`<p>Filter paper is full of tiny holes. Water particles are far smaller than the holes, so water pours through. Grains of sand are enormous by comparison, so they cannot. That is the whole mechanism, and it tells you when filtration works: <strong>only for a solid that has not dissolved</strong>.</p>
        <p>Two words the examiner expects, and will not accept substitutes for:</p>
        <ul>
          <li>The <span class="sdtxt">residue</span> is what stays on the paper — the insoluble solid.</li>
          <li>The <span class="lqtxt">filtrate</span> is what passes through — the liquid, plus anything dissolved in it.</li>
        </ul>
        <p>The second word carries a warning. A dissolved solid <em>is in the filtrate</em>. Filter salt water and the filtrate is still salt water; the paper stays clean, because dissolved salt is split into particles smaller than water's own holes in the paper can catch. Students lose a mark on this every year by writing that filtering gives "pure water".</p>
        <p><strong>Apparatus words:</strong> filter paper folded into a cone inside a <strong>filter funnel</strong>, standing in a <strong>conical flask</strong> or beaker to catch the filtrate. Pouring slowly down a glass rod stops the mixture sloshing over the paper's edge.</p>
        <p><strong>Decanting</strong> is the lazy version: let the solid settle, then pour the liquid off the top. Quicker, but some liquid always stays with the solid and some solid always comes with the liquid. Use it when "roughly" is good enough.</p>`,
  demo:`<strong>Do this:</strong> stir a spoon of sand into a glass of water, then a spoon of salt into another. Pour each through a coffee filter or a folded kitchen towel. Write down what the paper looks like in each case and what that proves.`,
  cliff:`So the salt went through with the water. It is still in there — you can taste it. How do you get it back?`},

 {t:"Evaporation and crystallisation: keeping the solid", len:"5 min",
  body:`<p>To get a dissolved solid back, remove the liquid. Heat the solution in an <strong>evaporating dish</strong>; the water turns to vapour and leaves; the salt cannot evaporate at that temperature, so it is left behind. Note what you have kept and what you have lost: the <strong>solid stays, the water is gone</strong> into the room.</p>
        <p>There are two ways to run it, and the exam likes the difference:</p>
        <ul>
          <li><strong>Evaporate to dryness</strong> — boil until the dish is dry. Fast; gives a crust of tiny crystals; and some substances decompose if you keep heating them once they are dry.</li>
          <li><strong>Crystallisation</strong> — heat gently until the solution is concentrated (a saturated solution, where crystals start to appear at the edge), then stop and let it cool slowly. <strong>Slow cooling gives large crystals</strong>; fast cooling gives small ones. Filter the crystals off and dry them between sheets of paper.</li>
        </ul>
        <p>Both use the same property: the solid and the liquid have wildly different <strong>boiling points</strong>. Water leaves at 100 °C; salt would need over 1400 °C.</p>`,
  demo:`<strong>Do this:</strong> dissolve as much salt as you can in a few spoons of warm water, pour it into a saucer and leave it on a windowsill for two days. Write down when the first crystals appeared and what shape they are.`,
  cliff:`Evaporation throws the water away. On a ship at sea, the water is the thing you want. Now what?`},

 {t:"Simple distillation: keeping the liquid", len:"7 min",
  body:`<p>Distillation is evaporation with the vapour caught. Four stages, and you need all four in an answer:</p>
        <ol>
          <li>The solution is <strong>heated</strong> and the liquid with the lowest boiling point <strong>boils</strong> — for sea water, that is the water, at 100 °C.</li>
          <li>The <strong>vapour</strong> rises out of the flask, leaving the salt behind because salt does not boil at that temperature.</li>
          <li>The vapour passes through a <strong>condenser</strong> — a tube with cold water flowing round the outside — where it <strong>cools and condenses</strong> back into a liquid.</li>
          <li>The liquid, now called the <span class="lqtxt">distillate</span>, drips into a <strong>receiving flask</strong>. It is pure water.</li>
        </ol>
        <p>Three details examiners test. The <strong>thermometer</strong> sits at the top of the flask where the vapour leaves, so it reads the boiling point of whatever is being collected — 100 °C tells you it is water coming over. The cooling water enters the condenser at the <strong>bottom</strong> and leaves at the top, so the condenser is always full and the coldest part is nearest the receiver. And the salt <strong>stays in the flask</strong>, more concentrated than before.</p>
        <p>Distillation separates any dissolved solid from its solvent, and any two liquids whose boiling points differ enough — ink from water, alcohol from wine. What it costs is energy: every gram of water has to be boiled and then cooled again.</p>`,
  demo:`<strong>Do this:</strong> hold a cold plate above a steaming kettle for ten seconds (carefully — the steam burns). Drops form on the plate. Write the four stages of distillation next to what you just did, matching each stage to something you saw.`,
  cliff:`Filtration, evaporation and distillation all separate a solid from a liquid. What if the mixture is several dissolved things, all in the same liquid?`},

 {t:"Chromatography and R<sub>f</sub>", len:"7 min",
  body:`<p>Black ink is usually a mixture of several dyes, all dissolved in the same solvent. Nothing above can pull them apart. Chromatography can, because the dyes differ in <strong>how soluble they are</strong> in the solvent and <strong>how strongly they cling to the paper</strong>.</p>
        <p><strong>The method.</strong> Draw a baseline in <strong>pencil</strong> near the bottom of a strip of paper (pencil, because graphite is insoluble and will not run). Put a small spot of ink on the line. Stand the paper in a little solvent, with the solvent level <strong>below</strong> the baseline so the spot is not washed off. The solvent soaks up the paper, and as it passes the spot it carries the dyes with it — the more soluble a dye, the further it travels. Take the paper out before the solvent reaches the top and mark the <span class="vptxt">solvent front</span> at once, because it fades as it dries.</p>
        <p><strong>Reading it.</strong> One spot means one substance (probably pure). Several spots mean a mixture, and the number of spots is the number of dyes. Two spots at the same height, from different samples, are probably the same dye.</p>
        <div class="eqline">R<sub>f</sub> = distance moved by the substance &nbsp;÷&nbsp; distance moved by the solvent &nbsp; (both measured from the baseline)</div>
        <p>R<sub>f</sub> has <strong>no units</strong> — it is one distance divided by another — and it is <strong>always less than 1</strong>, because nothing travels faster than the solvent that carries it. A dye has the same R<sub>f</sub> every time in the same solvent, which is how you identify it: measure, calculate, compare with the data book. If the solvent moved 8.0 cm and the spot moved 6.0 cm, R<sub>f</sub> = 6.0 ÷ 8.0 = 0.75.</p>`,
  demo:`<strong>Do this:</strong> put a dot of washable felt-tip on a strip of kitchen towel 2 cm from the bottom and stand it in 1 cm of water. Wait ten minutes. Measure how far the water rose and how far the highest colour rose, and calculate its R<sub>f</sub>. Then try the machine below.`,
  cliff:`Salt and sand in the same jar, both dry. No single method works. What order would three of them go in?`},

 {t:"Multi-step separations, and how to write them", len:"5 min",
  body:`<p>Real mixtures rarely need one step. The classic exam case is <strong>salt and sand</strong>, and it goes in exactly one order:</p>
        <ol>
          <li><strong>Add water and stir.</strong> The salt dissolves; the sand does not. Now the two are different in a way you can use.</li>
          <li><strong>Filter.</strong> The sand is the residue on the paper. The salt solution is the filtrate. Rinse the sand with a little water so no salt clings to it.</li>
          <li><strong>Evaporate the filtrate.</strong> The water leaves; the salt crystals stay in the dish.</li>
        </ol>
        <p>Every step has a reason, and the mark scheme awards the reasons: <em>water because salt is soluble and sand is not; filter because the sand is now the only insoluble thing; evaporate because the salt is dissolved and cannot be filtered</em>. Swap steps 2 and 3 and you evaporate a wet sandy mess and get salty sand.</p>
        <p><strong>Iron filings and sand:</strong> one step, a magnet, because iron is magnetic. No water needed. <strong>Iron, sand and salt:</strong> magnet first, then the three steps above. <strong>Ink:</strong> distillation if you want the water; chromatography if you want to know what dyes are in it — you cannot collect the dyes in a jar by chromatography, which is a common wrong answer.</p>
        <p>The shape of a full-mark answer: <strong>step — reason — what you now have</strong>, repeated. Write it as a numbered list. Examiners can tick a list; they struggle to find marks in a paragraph.</p>`,
  demo:`<strong>Do this:</strong> write the salt-and-sand method as three numbered steps in the step—reason—result shape, from memory. Then run it on the bench above and check that the machine ends with sand on the paper and salt in the dish.`,
  cliff:`You now know every method and every reason. The questions below are where you find out whether you write the reason without being asked.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"Which method would you use to separate <strong>sand from water</strong>?", o:["Evaporation","Distillation","Filtration","Chromatography"], a:2,
  why:"Sand is insoluble, so its grains are trapped by the filter paper while the water passes through. Evaporation or distillation would work but waste time and energy — the examiner wants the simplest method that fits the property."},
 {n:2, lvl:"warm-up", q:"In filtration, the liquid that passes through the paper is called the…", o:["residue","solvent","distillate","filtrate"], a:3,
  why:"Filtrate passes through; residue stays on the paper. Distillate is what drips out of a condenser — a different technique altogether."},
 {n:3, lvl:"standard", q:"Which method gives you <strong>pure water</strong> from sea water?", o:["Filtration","Evaporation","Simple distillation","A separating funnel"], a:2,
  why:"Filtration cannot remove dissolved salt; evaporation removes the water and keeps the salt. Only distillation boils the water off and then condenses it back so you can collect it."},
 {n:4, lvl:"standard", q:"On a chromatogram the solvent front moved 10 cm and a spot moved 4 cm. The R<sub>f</sub> value of the spot is…", o:["2.5","0.4","6","0.6"], a:1,
  why:"R<sub>f</sub> = distance moved by the spot ÷ distance moved by the solvent = 4 ÷ 10 = 0.4. It has no units. 2.5 is the division done upside down — and an R<sub>f</sub> above 1 is impossible, which is your check."},
 {n:5, lvl:"trap", q:"Why is the baseline in chromatography drawn in <strong>pencil</strong>?", o:["Pencil is easier to see","Pencil lines are thinner","Graphite is insoluble, so the line does not run","Ink would react with the paper"], a:2,
  why:"Ink is a mixture of soluble dyes, so an ink baseline would travel up the paper with everything else and wreck the result. Graphite does not dissolve in the solvent, so a pencil line stays put."}
];

const SHORTS = [
 {n:6, lvl:"standard", m:2, q:"Explain why sand can be separated from water by filtration but salt cannot.",
  scheme:["Sand is insoluble; its grains are too large to pass through the holes in the filter paper, so they are trapped as the residue. <span class='num'>[1]</span>",
          "Salt has dissolved, so its particles are small enough to pass through the paper with the water, into the filtrate. <span class='num'>[1]</span>"],
  tip:"The mark is for the mechanism — particle size against the holes in the paper — not for restating that one is soluble."},

 {n:7, lvl:"standard", m:2, q:"Describe how you would obtain <strong>dry salt crystals</strong> from a salt solution.",
  scheme:["Heat the solution in an evaporating dish so the water evaporates (or heat gently until crystals begin to form, then leave to cool). <span class='num'>[1]</span>",
          "The salt is left behind as crystals because it does not evaporate; dry them (e.g. between filter papers or in a warm oven). <span class='num'>[1]</span>"],
  tip:"\"Boil it\" is not a description. Name the apparatus, say which substance leaves and which stays, and say why."},

 {n:8, lvl:"standard", m:2, q:"In simple distillation, state the purpose of the <strong>condenser</strong> and explain how it does its job.",
  scheme:["It turns the vapour back into a liquid (condenses it) so it can be collected. <span class='num'>[1]</span>",
          "Cold water flows through the outer jacket, cooling the vapour in the inner tube below its boiling point. <span class='num'>[1]</span>"],
  tip:"\"It cools the gas\" is half a mark. Say what the cooling does — condenses the vapour — and how — cold water round the outside."},

 {n:9, lvl:"standard", m:2, q:"On a chromatogram, the solvent front is <span class='num'>12.0 cm</span> from the baseline and a green spot is <span class='num'>9.0 cm</span> from the baseline. Calculate the R<sub>f</sub> value of the green dye. Show your working.",
  scheme:["R<sub>f</sub> = 9.0 ÷ 12.0 <span class='num'>[1]</span>",
          "= 0.75 (no units) <span class='num'>[1]</span>"],
  tip:"Write the formula in words before the numbers. If your answer comes out above 1, you have divided the wrong way round."},

 {n:10, lvl:"hard", m:2, q:"Two samples of ink are run side by side on the same chromatography paper. Explain how you could tell whether they contain the <strong>same</strong> dye.",
  scheme:["If both produce a spot at the same height (the same distance from the baseline), they contain the same dye — <span class='num'>[1]</span>",
          "because the same substance always has the same R<sub>f</sub> value in the same solvent (travels the same fraction of the solvent's distance). <span class='num'>[1]</span>"],
  tip:"\"Same colour\" is not evidence — two different dyes can be the same colour. Height on the paper, or R<sub>f</sub>, is the evidence."}
];

const WORDS = [
 {n:11, lvl:"standard", m:3, q:"A jar contains a dry mixture of <strong>salt and sand</strong>. Describe how you would obtain a sample of dry salt from it.<br><br><strong>(a)</strong> State the first step and why it is needed. <span class='num'>[1]</span><br><strong>(b)</strong> State the second step and what it removes. <span class='num'>[1]</span><br><strong>(c)</strong> State the final step and what is left. <span class='num'>[1]</span>",
  hints:["Right now the two solids look alike. Find something that makes them behave differently — one of them dissolves.",
         "Once the salt is dissolved, only one thing in the beaker is a solid. What catches solids?",
         "The salt is now in the filtrate, dissolved. To get the solid back, remove the liquid."],
  sol:["(a) <strong>Add water and stir</strong>, so that the salt dissolves and the sand does not — now they can be told apart.",
       "(b) <strong>Filter</strong> the mixture. The sand is trapped on the paper as the residue; the salt solution passes through as the filtrate.",
       "(c) <strong>Evaporate</strong> the filtrate in an evaporating dish. The water leaves as vapour and the salt is left behind as dry crystals.",
       "The bench above will show you what happens if you evaporate before you filter: a dish of salty sand and nothing separated. Order is the answer."]},

 {n:12, lvl:"standard", m:3, q:"A chromatogram is run with four spots on the baseline: three known food dyes <span class='num'>E102, E110, E133</span> and an unknown sweet colouring. The solvent front travels <span class='num'>8.0 cm</span>. The known dyes travel <span class='num'>2.0 cm, 5.6 cm</span> and <span class='num'>6.8 cm</span>. The sweet produces two spots, at <span class='num'>2.0 cm</span> and <span class='num'>6.8 cm</span>.<br><br><strong>(a)</strong> Calculate the R<sub>f</sub> values of E102 and E133. <span class='num'>[1]</span><br><strong>(b)</strong> State which dyes the sweet contains, and how you know. <span class='num'>[1]</span><br><strong>(c)</strong> Explain why the sweet's colouring cannot be a pure substance. <span class='num'>[1]</span>",
  hints:["R<sub>f</sub> is spot distance divided by solvent distance. Both from the baseline.",
         "Match heights. A spot at the same height as a known dye is that dye.",
         "How many spots did the sweet give? What does more than one spot mean?"],
  sol:["(a) E102: 2.0 ÷ 8.0 = <strong>0.25</strong>. E133: 6.8 ÷ 8.0 = <strong>0.85</strong>. (E110 would be 5.6 ÷ 8.0 = 0.70.)",
       "(b) The sweet contains <strong>E102 and E133</strong>, because its two spots are at exactly the same heights (the same R<sub>f</sub> values) as those two dyes, and the same substance always travels the same distance in the same solvent.",
       "(c) It gave <strong>two spots</strong>, so it contains at least two different substances — a pure substance would give one spot only. It is a mixture.",
       "Check your R<sub>f</sub> values are below 1 before you move on. 8.0 ÷ 2.0 = 4 is the upside-down version, and it is the most common wrong number in this topic."]},

 {n:13, lvl:"hard", m:3, q:"A student wants pure water from ink, which is a mixture of dyes dissolved in water. She sets up simple distillation.<br><br><strong>(a)</strong> Explain why the water and not the dyes comes out of the condenser. <span class='num'>[1]</span><br><strong>(b)</strong> State what the thermometer at the top of the flask reads while water is being collected, and why. <span class='num'>[1]</span><br><strong>(c)</strong> The student says she could have used chromatography instead to get the water. Explain why she is wrong. <span class='num'>[1]</span>",
  hints:["Which substance boils at 100 °C? Which one cannot leave the flask as a vapour at that temperature?",
         "The thermometer is in the vapour, so it reads the boiling point of whatever is boiling off.",
         "Chromatography spreads the dyes out on a piece of paper. Does it give you a jar of anything?"],
  sol:["(a) Water has a much <strong>lower boiling point</strong> than the dyes, so when the ink is heated only the water boils and turns to vapour; the dyes stay behind in the flask. The vapour is then condensed and collected.",
       "(b) <strong>100 °C</strong> — the boiling point of water — because the thermometer sits in the vapour leaving the flask, and that vapour is water.",
       "(c) Chromatography <strong>separates the dyes from each other on paper</strong> so they can be seen and identified; it does not collect the water. The water soaks into the paper and evaporates. It is a method for analysing a mixture, not for recovering the solvent.",
       "The thermometer detail in (b) is a favourite: students put the thermometer in the liquid, where it would read the (higher) boiling point of the whole solution instead."]},

 {n:14, lvl:"hard", m:3, q:"A student runs a chromatogram but sets it up badly: the baseline is drawn in ink, and the solvent is poured in above the baseline. She also removes the paper only after the solvent has reached the top.<br><br><strong>(a)</strong> Explain what goes wrong because of the ink baseline. <span class='num'>[1]</span><br><strong>(b)</strong> Explain what goes wrong because of the solvent level. <span class='num'>[1]</span><br><strong>(c)</strong> Explain why she can no longer calculate any R<sub>f</sub> values. <span class='num'>[1]</span>",
  hints:["Ink is soluble. What does the solvent do to everything soluble on the paper?",
         "If the spot is under the solvent, it does not travel up the paper. Where does it go?",
         "R<sub>f</sub> needs the distance the solvent moved. Where is the solvent front now?"],
  sol:["(a) Ink is a <strong>mixture of soluble dyes</strong>, so the baseline itself dissolves and travels up the paper, smearing across the results so the sample's spots cannot be told from the line's.",
       "(b) With the solvent above the baseline, the spots are <strong>washed off into the solvent</strong> at the bottom instead of being carried up the paper. Nothing separates.",
       "(c) Because the solvent reached the top, the <strong>solvent front cannot be measured</strong> — its distance is unknown (or it has run off the paper and dried). R<sub>f</sub> is spot distance ÷ solvent distance, and without the denominator there is no value.",
       "Three set-up rules, three reasons. Examiners ask for the reason far more often than the rule, and (c) is the one students cannot explain."]},

 {n:15, lvl:"hard", m:3, q:"A dry mixture contains <strong>iron filings, sand and salt</strong>. Plan a method to obtain all three, each on its own and dry. Give the steps in order with a reason for each.<br><br><strong>(a)</strong> Describe how to remove the iron, and why this must be done first. <span class='num'>[1]</span><br><strong>(b)</strong> Describe how to separate the sand from the salt. <span class='num'>[1]</span><br><strong>(c)</strong> Describe how to recover the salt, and explain why distillation would be the wrong choice here. <span class='num'>[1]</span>",
  hints:["One of the three has a property nothing else has, and it works on a dry mixture. Use it before you add anything.",
         "Now it is salt and sand — Q11 again.",
         "You want the solid, not the water. Which of evaporation and distillation keeps which?"],
  sol:["(a) Pass a <strong>magnet</strong> over the dry mixture; the iron filings stick to it because iron is magnetic and sand and salt are not. It goes first because once water is added the iron would be wet, mixed with the sand as residue, and start to rust.",
       "(b) Add water and stir so the salt <strong>dissolves</strong> and the sand does not; then <strong>filter</strong>. The sand is the residue (rinse and dry it); the salt solution is the filtrate.",
       "(c) <strong>Evaporate</strong> the filtrate in an evaporating dish: the water leaves and the salt is left as dry crystals. Distillation would collect the water and leave the salt in the flask — it keeps the wrong part, and costs far more energy for no benefit.",
       "This is the whole page in one question. Three steps, three properties — magnetic, insoluble, soluble — and a reason for the order. If you can write this cold, you can write any separation question they set."]}
];
'''

TOOLS_JS = r'''/* ================= HERO 1: the separation bench ================= */
/* components: sand (insoluble solid), salt (soluble solid), water, iron (magnetic solid), dye (soluble dyes), oil (immiscible liquid) */
const MIXES = [
 {id:'sandwater', label:'Sand + water',        has:{sand:1, water:1}},
 {id:'saltwater', label:'Salt water',          has:{salt:1, water:1}},
 {id:'saltsand',  label:'Salt + sand (dry)',   has:{salt:1, sand:1}},
 {id:'ironsand',  label:'Iron filings + sand', has:{iron:1, sand:1}},
 {id:'ink',       label:'Ink (dyes in water)', has:{dye:1, water:1}},
 {id:'oilwater',  label:'Oil + water',         has:{oil:1, water:1}},
 {id:'three',     label:'Iron + sand + salt',  has:{iron:1, sand:1, salt:1}}
];
const STEPS = [
 {id:'water',  label:'Add water & stir'},
 {id:'filter', label:'Filter'},
 {id:'evap',   label:'Evaporate'},
 {id:'distil', label:'Distil'},
 {id:'magnet', label:'Magnet'},
 {id:'chrom',  label:'Chromatography'},
 {id:'funnel', label:'Separating funnel'}
];
const NAMES = {sand:'sand', salt:'salt', water:'water', iron:'iron filings', dye:'dyes', oil:'oil'};
let mixId = 'sandwater';
let beaker = {}, tray = [], stepLog = [];

function resetBench(){
  beaker = Object.assign({}, MIXES.find(m=>m.id===mixId).has);
  tray = []; stepLog = [];
  paintBench('Which property differs — and which step uses it?');
}
function dissolved(){ return !!beaker.water; }
function runStep(id){
  let note = '', ok = true;
  const b = beaker;
  if(id==='water'){
    if(b.water){ ok=false; note='There is already water in the beaker. Adding more changes nothing.'; }
    else { b.water = 1; note = (b.salt||b.dye) ? 'The ' + (b.salt?'salt':'dyes') + ' dissolve' + (b.salt?'s':'') + '; ' + (b.sand?'the sand ':'') + (b.iron?'the iron ':'') + (b.sand||b.iron?'stay' + ((b.sand&&b.iron)?'':'s') + ' as grains. ':'') + 'Now the solids differ in a way you can use.' : 'Nothing here dissolves. That step gained you nothing.'; if(!(b.salt||b.dye)) ok=false; }
  } else if(id==='filter'){
    if(!b.water && !b.oil){ ok=false; note='Dry solids cannot be filtered — nothing flows through the paper, so nothing separates.'; }
    else if(b.sand||b.iron){ const got=[]; if(b.sand){got.push('sand');delete b.sand;} if(b.iron){got.push('iron filings');delete b.iron;} tray.push('residue: '+got.join(' + ')); note='Residue on the paper: '+got.join(' and ')+'. Everything dissolved goes straight through into the filtrate' + (b.salt||b.dye ? ' — the '+(b.salt?'salt':'dyes')+' included.' : '.'); }
    else { ok=false; note='Nothing is trapped. ' + (b.salt?'Dissolved salt passes':(b.dye?'The dissolved dyes pass':'Dissolved substances pass')) + ' straight through the paper with the water. The filtrate is exactly what you poured in.'; }
  } else if(id==='evap'){
    if(!b.water){ ok=false; note='There is no liquid to evaporate.'; }
    else { delete b.water; const kept=[]; if(b.salt){kept.push('salt crystals');delete b.salt;} if(b.dye){kept.push('dried dyes');delete b.dye;} if(b.sand||b.iron){ /* wet solids dry out in the dish, still mixed */ }
      if(kept.length){ tray.push('in the dish: '+kept.join(' + ') + ((b.sand||b.iron)?' (mixed with '+[b.sand?'sand':'',b.iron?'iron':''].filter(Boolean).join(' and ')+')':'')); if(b.sand||b.iron){ ok=false; note='The water left as vapour, but the dish holds the '+kept.join(' and ')+' mixed back in with the '+[b.sand?'sand':'',b.iron?'iron':''].filter(Boolean).join(' and ')+'. You evaporated before you filtered.'; delete b.sand; delete b.iron; } else note='The water left as vapour — it is gone into the room. The '+kept.join(' and ')+' could not evaporate and stay in the dish.'; }
      else { note='The water is gone into the room' + (b.oil?', leaving the oil':'') + '. Nothing was collected: evaporation throws the liquid away.'; if(!b.oil) ok=false; }
    }
  } else if(id==='distil'){
    if(!b.water){ ok=false; note='There is no liquid to distil.'; }
    else { delete b.water; tray.push('distillate: pure water'); const left=Object.keys(b).map(k=>NAMES[k]); note='The water boils at 100 °C, its vapour is condensed and collected as pure water. ' + (left.length?'Left in the flask: '+left.join(', ')+'.':'The flask is empty.'); }
  } else if(id==='magnet'){
    if(b.iron){ delete b.iron; tray.push('on the magnet: iron filings'); note='The iron filings jump to the magnet. Sand and salt are not magnetic and stay where they are.'; }
    else { ok=false; note='Nothing here is magnetic. The magnet comes away clean.'; }
  } else if(id==='chrom'){
    if(b.dye && b.water){ delete b.dye; delete b.water; tray.push('on the paper: the dyes, separated into spots'); note='The dyes spread up the paper into separate spots — you can now count and identify them. Note that this gives you no jar of anything: the water soaks away.'; }
    else { ok=false; note='Chromatography needs dissolved substances that differ in solubility. ' + (b.salt&&b.water ? 'Salt gives one colourless spot — nothing to see.' : 'There is nothing here for it to separate.'); }
  } else if(id==='funnel'){
    if(b.oil && b.water){ delete b.oil; tray.push('from the funnel: oil'); note='Oil and water do not mix and the oil floats. Open the tap, run the water off from the bottom, close it as the oil reaches the tap.'; }
    else { ok=false; note='A separating funnel needs two liquids that do not mix. ' + (b.oil ? 'There is no water for the oil to sit on.' : 'There is only one liquid here.'); }
  }
  stepLog.push({id, ok});
  paintBench(note);
}

function paintBench(note){
  const NS='http://www.w3.org/2000/svg';
  const g = document.getElementById('beakerContents'); while(g.firstChild) g.removeChild(g.firstChild);
  const b = beaker;
  function el(tag, attrs){ const e=document.createElementNS(NS,tag); Object.keys(attrs).forEach(k=>e.setAttribute(k,attrs[k])); g.appendChild(e); return e; }
  if(b.water){ el('rect',{x:72,y:110,width:136,height:102,rx:8,fill: b.dye?'#7B5EA7':(b.salt?'#DDEBE8':'var(--lq-tint)'),opacity: b.dye?0.55:0.9}); }
  if(b.oil){ el('rect',{x:72,y: b.water?86:150,width:136,height:24,rx:6,fill:'#E4C25A',opacity:.85}); }
  const grains=[]; if(b.sand) grains.push('#C9A46A'); if(b.iron) grains.push('#555B66'); if(b.salt && !b.water) grains.push('#F2F0EA');
  grains.forEach((col,gi)=>{ for(let i=0;i<14;i++){ el('circle',{cx: 82 + ((i*37 + gi*11)%118), cy: 196 - (gi*7) - ((i*13)%14), r:3.2, fill:col, stroke:'#00000022'}); } });
  if(b.salt && b.water){ const t=el('text',{x:140,y:160,'text-anchor':'middle','font-family':'var(--mono)','font-size':'11',fill:'var(--ink-soft)'}); t.textContent='salt, dissolved'; }
  if(b.dye && b.water){ const t=el('text',{x:140,y:160,'text-anchor':'middle','font-family':'var(--mono)','font-size':'11',fill:'#fff'}); t.textContent='dyes, dissolved'; }
  if(!Object.keys(b).length){ const t=el('text',{x:140,y:135,'text-anchor':'middle','font-family':'var(--mono)','font-size':'11',fill:'var(--ink-soft)'}); t.textContent='empty'; }

  const tg = document.getElementById('trayContents'); while(tg.firstChild) tg.removeChild(tg.firstChild);
  tray.slice(-6).forEach((line,i)=>{ const t=document.createElementNS(NS,'text'); t.setAttribute('x',292); t.setAttribute('y',64+i*24); t.setAttribute('font-family','var(--mono)'); t.setAttribute('font-size','11.5'); t.setAttribute('fill','var(--ink)'); t.textContent='• '+line; tg.appendChild(t); });

  const left = Object.keys(b).map(k=>NAMES[k]);
  document.getElementById('bn-beaker').textContent = left.length ? left.join(', ') : 'empty';
  const solids = ['sand','salt','iron'].filter(k=>b[k]).length, liquids=['water','oil'].filter(k=>b[k]).length;
  document.getElementById('bn-beakers').textContent = !left.length ? 'everything is somewhere else' : (left.length===1 ? 'one substance — separated' : (solids && liquids ? 'solid and liquid together' : (solids ? 'dry solids' : 'liquids')));
  document.getElementById('bn-tray').textContent = tray.length ? tray.length + (tray.length>1?' things':' thing') : 'nothing yet';
  document.getElementById('bn-trays').textContent = tray.length ? tray[tray.length-1] : 'add a step';
  const sl = document.getElementById('bn-steps');
  sl.innerHTML = stepLog.length ? stepLog.map(s=>`<span class="st${s.ok?'':' bad'}">${STEPS.find(x=>x.id===s.id).label}</span>`).join('<span style="color:var(--ink-soft)">→</span>') : '<span class="st">none</span>';
  const pill = document.getElementById('bn-pill');
  const done = left.length<=1;
  pill.className = 'pill ' + (done ? 'lq' : 'sd'); pill.textContent = done ? (left.length ? 'Separated' : 'All collected') : 'Still a mixture';
  document.getElementById('bn-note').textContent = note;
  document.querySelectorAll('#stepChips .chip').forEach(c=>{ c.disabled = false; });
}

(function(){
  const mh = document.getElementById('mixChips');
  MIXES.forEach(m=>{ const c=document.createElement('button'); c.type='button'; c.className='chip'+(m.id===mixId?' on':''); c.textContent=m.label; c.dataset.mix=m.id;
    c.addEventListener('click', ()=>{ mixId=m.id; document.querySelectorAll('#mixChips .chip').forEach(x=>x.classList.toggle('on', x.dataset.mix===mixId)); resetBench(); });
    mh.appendChild(c); });
  const sh = document.getElementById('stepChips');
  STEPS.forEach(s=>{ const c=document.createElement('button'); c.type='button'; c.className='chip'; c.textContent=s.label; c.dataset.step=s.id;
    c.addEventListener('click', ()=>runStep(s.id)); sh.appendChild(c); });
  document.getElementById('benchUndo').addEventListener('click', ()=>{
    const log = stepLog.slice(0,-1); resetBench(); log.forEach(s=>runStep(s.id)); if(!log.length) paintBench('Back to the start.');
  });
})();

const BENCH_PUZZLES = [
 {ask:"Start from <strong>salt water</strong> and end with <strong>pure water</strong> in the collected tray.", mix:'saltwater',
  test:()=>mixId==='saltwater' && tray.some(t=>t.startsWith('distillate')),
  why:"Only distillation catches the water: boil it off, condense it, collect it. Evaporation would have thrown it away."},
 {ask:"Start from <strong>salt water</strong> and end with <strong>salt crystals</strong> collected — without wasting a step.", mix:'saltwater',
  test:()=>mixId==='saltwater' && tray.some(t=>t.includes('salt crystals')) && stepLog.every(s=>s.ok),
  why:"Evaporate, and nothing else. Filtering first is the classic wasted step — the salt goes straight through."},
 {ask:"Start from <strong>salt + sand (dry)</strong> and end with the sand and the salt crystals collected <strong>separately</strong>.", mix:'saltsand',
  test:()=>mixId==='saltsand' && tray.some(t=>t==='residue: sand') && tray.some(t=>t==='in the dish: salt crystals'),
  why:"Dissolve, filter, evaporate — in that order. Evaporate first and you get a dish of salty sand."},
 {ask:"Start from <strong>iron filings + sand</strong> and separate them <strong>without using any water</strong>.", mix:'ironsand',
  test:()=>mixId==='ironsand' && tray.some(t=>t.startsWith('on the magnet')) && !stepLog.some(s=>s.id==='water'),
  why:"Iron is magnetic; sand is not. One step, and it works dry."},
 {ask:"Start from <strong>ink</strong> and find out how many dyes it contains.", mix:'ink',
  test:()=>mixId==='ink' && tray.some(t=>t.startsWith('on the paper')),
  why:"Chromatography spreads the dyes into separate spots. Distillation would give you the water but tell you nothing about the dyes."},
 {ask:"Start from <strong>iron + sand + salt</strong> and end with all three collected separately, using <strong>every step successfully</strong> — no wasted moves.", mix:'three',
  test:()=>mixId==='three' && tray.some(t=>t.startsWith('on the magnet')) && tray.some(t=>t==='residue: sand') && tray.some(t=>t==='in the dish: salt crystals') && stepLog.every(s=>s.ok),
  why:"Magnet, then water, then filter, then evaporate. Four steps, four properties, one order."}
];
let benchQ = null;
document.getElementById('benchPuzzle').addEventListener('click', ()=>{
  benchQ = BENCH_PUZZLES[Math.floor(Math.random()*BENCH_PUZZLES.length)];
  mixId = benchQ.mix; document.querySelectorAll('#mixChips .chip').forEach(x=>x.classList.toggle('on', x.dataset.mix===mixId)); resetBench();
  const box = document.getElementById('benchQuiz');
  box.classList.add('on');
  box.innerHTML = '<strong>Puzzle.</strong> ' + benchQ.ask +
    '<div class="qrow"><button class="btn ghost small" type="button" id="benchCheck">Check the bench</button>' +
    '<span id="benchFb" class="num" style="font-size:13px"></span></div>';
  document.getElementById('benchCheck').addEventListener('click', ()=>{
    const fb = document.getElementById('benchFb');
    if(benchQ.test()){
      fb.style.color = 'var(--ok)'; fb.textContent = 'Correct — ' + benchQ.why;
      S.puzzles = (S.puzzles||0) + 1; save(); refresh();
      document.getElementById('benchCheck').disabled = true;
    } else {
      fb.style.color = 'var(--no)';
      fb.textContent = stepLog.some(s=>!s.ok) ? 'A step in red did nothing useful. Undo it and think about which property differs.' : 'Not there yet. Look at what is still in the beaker.';
    }
  });
});

/* ================= HERO 2: the chromatogram ================= */
const DYES = [
 {id:'red',   label:'red',   rf:0.25, col:'#C4472B'},
 {id:'green', label:'green', rf:0.55, col:'#4C9A3E'},
 {id:'blue',  label:'blue',  rf:0.80, col:'#3B5BA9'}
];
const UNKNOWN = ['red','blue'];                 // the mystery ink is red + blue
const PX_PER_CM = 22, BASE_Y = 290, MAXCM = 12;
let solv = 0, showRf = false;
const LANE_X = [200, 300, 400, 500];

(function(){
  const NS='http://www.w3.org/2000/svg';
  const r = document.getElementById('ruler');
  for(let cm=0; cm<=MAXCM; cm++){
    const y = BASE_Y - cm*PX_PER_CM;
    const ln=document.createElementNS(NS,'line'); ln.setAttribute('x1',142); ln.setAttribute('x2', cm%5===0?160:152); ln.setAttribute('y1',y); ln.setAttribute('y2',y); ln.setAttribute('stroke','var(--ink-soft)'); ln.setAttribute('stroke-width','1'); r.appendChild(ln);
    if(cm%2===0){ const t=document.createElementNS(NS,'text'); t.setAttribute('x',110); t.setAttribute('y',y+4); t.setAttribute('font-family','var(--mono)'); t.setAttribute('font-size','11'); t.setAttribute('fill','var(--ink-soft)'); t.textContent=cm+' cm'; r.appendChild(t); }
  }
  const lanes = document.getElementById('lanes');
  const labels = DYES.map(d=>d.label).concat(['unknown ink']);
  labels.forEach((lab,i)=>{ const t=document.createElementNS(NS,'text'); t.setAttribute('x',LANE_X[i]); t.setAttribute('y',326); t.setAttribute('text-anchor','middle'); t.setAttribute('font-family','var(--mono)'); t.setAttribute('font-size','11'); t.setAttribute('fill','var(--ink-soft)'); t.textContent=lab; lanes.appendChild(t); });
  DYES.forEach((d,i)=>{ const c=document.createElementNS(NS,'ellipse'); c.setAttribute('id','spot-'+d.id); c.setAttribute('cx',LANE_X[i]); c.setAttribute('cy',BASE_Y); c.setAttribute('rx',11); c.setAttribute('ry',7); c.setAttribute('fill',d.col); c.setAttribute('opacity','.9'); lanes.appendChild(c); });
  UNKNOWN.forEach(id=>{ const d=DYES.find(x=>x.id===id); const c=document.createElementNS(NS,'ellipse'); c.setAttribute('id','uspot-'+id); c.setAttribute('cx',LANE_X[3]); c.setAttribute('cy',BASE_Y); c.setAttribute('rx',11); c.setAttribute('ry',7); c.setAttribute('fill',d.col); c.setAttribute('opacity','.9'); lanes.appendChild(c); });
})();

function spotCm(d){ return Math.round(d.rf*solv*10)/10; }  // machine works to the nearest mm, like a ruler
function paintChrom(){
  const fy = BASE_Y - solv*PX_PER_CM;
  document.getElementById('front').setAttribute('y1', fy); document.getElementById('front').setAttribute('y2', fy);
  document.getElementById('frontLab').setAttribute('y', fy+4); document.getElementById('frontLab').textContent = solv>0 ? 'solvent front' : '';
  const wet = document.getElementById('wet'); wet.setAttribute('y', fy); wet.setAttribute('height', BASE_Y+20-fy);
  DYES.forEach(d=>{ const cy = BASE_Y - spotCm(d)*PX_PER_CM; document.getElementById('spot-'+d.id).setAttribute('cy', cy); const u=document.getElementById('uspot-'+d.id); if(u) u.setAttribute('cy', cy); });
  document.getElementById('solvval').textContent = solv.toFixed(1) + ' cm';
  document.getElementById('ch-front').textContent = solv.toFixed(1) + ' cm';
  document.getElementById('ch-spots').textContent = solv>0 ? DYES.map(d=>spotCm(d).toFixed(1)).join(' · ') + ' cm' : '—';
  document.getElementById('ch-rf').textContent = showRf ? (solv>0 ? DYES.map(d=>(spotCm(d)/solv).toFixed(2)).join(' · ') : '—') : 'hidden';
  const pill = document.getElementById('ch-pill');
  pill.textContent = solv===0 ? 'Dry paper' : (solv>=MAXCM ? 'Solvent at the top' : 'Running');
  document.getElementById('ch-note').textContent = solv===0 ? 'Raise the solvent. Watch which spot keeps up with it and which one barely leaves the line.'
    : (solv>=MAXCM ? 'The solvent front has reached the top of the paper. In a real run you should have taken the paper out before this — once the front runs off, its distance can no longer be measured.'
    : 'Every spot is a fixed fraction of the way to the front: the blue keeps up best, the red barely moves. Those fractions are the Rf values.');
}
const solvSlider = document.getElementById('solv');
solvSlider.addEventListener('input', ()=>{ solv = +solvSlider.value/10; paintChrom(); });
document.getElementById('showRf').addEventListener('click', e=>{ showRf = !showRf; e.currentTarget.setAttribute('aria-pressed', showRf?'true':'false'); e.currentTarget.classList.toggle('on', showRf); paintChrom(); });

const CHROM_PUZZLES = [
 {kind:'num', ask:"Set the solvent front to <strong>8.0 cm</strong>, read the distance the <strong>green</strong> spot has moved, and type its R<sub>f</sub> value to 2 decimal places.",
  test:v=>Math.abs(solv-8)<0.05 && Math.abs(v - spotCm(DYES[1])/8)<0.006, why:"4.4 ÷ 8.0 = 0.55. Spot over solvent, both from the baseline, no units."},
 {kind:'num', ask:"Set the solvent front to <strong>10.0 cm</strong> and type the R<sub>f</sub> value of the <strong>red</strong> dye.",
  test:v=>Math.abs(solv-10)<0.05 && Math.abs(v - spotCm(DYES[0])/10)<0.006, why:"2.5 ÷ 10.0 = 0.25. The red dye is the least soluble in this solvent, so it travels the smallest fraction."},
 {kind:'pos', ask:"Move the solvent front so that the <strong>blue</strong> spot sits exactly <strong>6.4 cm</strong> above the baseline.",
  test:()=>Math.abs(spotCm(DYES[2])-6.4)<0.05, why:"R<sub>f</sub> 0.80 × 8.0 cm = 6.4 cm. Rf works in reverse too: spot distance = Rf × solvent distance."},
 {kind:'pick', ask:"Run the paper as far as you like, then decide: which known dyes does the <strong>unknown ink</strong> contain?",
  test:v=>v==='red+blue', why:"Its two spots line up exactly with the red and the blue lanes — same height, same Rf, same substance. The green is absent."},
 {kind:'num', ask:"Set the solvent front to <strong>6.0 cm</strong> and type the R<sub>f</sub> value of the <strong>blue</strong> dye.",
  test:v=>Math.abs(solv-6)<0.05 && Math.abs(v - spotCm(DYES[2])/6)<0.006, why:"4.8 ÷ 6.0 = 0.80 — the same as at any other solvent distance. That constancy is what makes Rf useful."}
];
let chromQ = null;
document.getElementById('chromPuzzle').addEventListener('click', ()=>{
  chromQ = CHROM_PUZZLES[Math.floor(Math.random()*CHROM_PUZZLES.length)];
  showRf = false; document.getElementById('showRf').classList.remove('on'); document.getElementById('showRf').setAttribute('aria-pressed','false'); paintChrom();
  const box = document.getElementById('chromQuiz');
  box.classList.add('on');
  let input = '';
  if(chromQ.kind==='num') input = '<input class="rfin" id="chromIn" type="number" step="0.01" min="0" max="1" placeholder="0.00" aria-label="Your Rf value">';
  if(chromQ.kind==='pick') input = '<select class="rfin" id="chromIn" style="width:150px" aria-label="Which dyes"><option value="">choose…</option><option value="red">red only</option><option value="green">green only</option><option value="blue">blue only</option><option value="red+green">red + green</option><option value="red+blue">red + blue</option><option value="green+blue">green + blue</option><option value="all">all three</option></select>';
  box.innerHTML = '<strong>Puzzle.</strong> ' + chromQ.ask +
    '<div class="qrow">' + input + '<button class="btn ghost small" type="button" id="chromCheck">Check</button>' +
    '<span id="chromFb" class="num" style="font-size:13px"></span></div>';
  document.getElementById('chromCheck').addEventListener('click', ()=>{
    const fb = document.getElementById('chromFb');
    const inEl = document.getElementById('chromIn');
    const v = inEl ? (chromQ.kind==='num' ? parseFloat(inEl.value) : inEl.value) : null;
    const pass = chromQ.kind==='pos' ? chromQ.test() : (chromQ.kind==='num' ? (!isNaN(v) && chromQ.test(v)) : chromQ.test(v));
    if(pass){
      fb.style.color = 'var(--ok)'; fb.innerHTML = 'Correct — ' + chromQ.why;
      S.puzzles = (S.puzzles||0) + 1; save(); refresh();
      document.getElementById('chromCheck').disabled = true;
    } else {
      fb.style.color = 'var(--no)';
      fb.textContent = chromQ.kind==='num' && !isNaN(v) && v>1 ? 'Above 1 — you have divided the wrong way round.' : (chromQ.kind==='num' && Math.abs(solv-(chromQ.ask.includes('8.0')?8:chromQ.ask.includes('10.0')?10:6))>=0.05 ? 'The solvent front is not where the puzzle asked for it yet.' : 'Not quite. Check the distances on the paper and try again.');
    }
  });
});

function boot(){
  resetBench();
  paintChrom();
}
'''
