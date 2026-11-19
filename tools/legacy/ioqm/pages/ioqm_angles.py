# -*- coding: utf-8 -*-
ID = 'ioqm-angles'
SHORT_TITLE = 'Chase the Angle'
SUB = 'IOQM · Geometry I: angle facts, triangles, polygons, circles'
BLURB = ("Olympiad geometry starts with angle chasing: label one angle, follow the facts round the figure, and let it come back to bite. "
         "Bend a triangle and watch the exterior angle keep up, then cut any polygon into triangles to see where (n − 2) × 180 comes from.")
META_TOOL = 'triangle machine'
COLOURS = ('#8C2D2D', '#F8E8E8', '#1F5A7A', '#E3EEF5', '#4F6B1A', '#EDF3E1')
EYEBROW = 'IOQM Olympiad Prep · Geometry I'
H1 = 'Chase <i>the</i><br><em>Angle</em>'
LEDE = ("A geometry question gives you two angles and asks for a third that seems to have nothing to do with them. "
        "The answer is never a new theorem — it's the same five facts used in a chain. This page gives you the five facts and the habit of chaining them.")
TARGET = ("You've been landing around <span class=\"num\">10 out of 15</span> at school. This page is out of <span class=\"num\">30</span>; "
          "the targets are <span class=\"num\">21</span> on the first pass and <span class=\"num\">26</span> on the second. "
          "Draw every figure yourself, big, with a ruler. Most geometry marks are lost to a sketch too small to think on.")
VIDEO_MIN = '~45 min total'
LESSON_MIN = '~40 min total'
NAV = [('tri', 'Triangle machine'), ('videos', '6 videos'), ('lessons', '6 lessons'), ('poly', 'Polygon machine'),
       ('quick', 'Quick checks'), ('short', 'Short answers'), ('word', 'Word problems'), ('traps', 'Exam traps')]

EXTRA_CSS = r'''
'''

TOOL1_HTML = r'''
<section id="tri">
  <div class="panel">
    <div class="panel-top">
      <h2>The triangle machine</h2>
      <p>Set two angles; the third is whatever is left of 180°. The side BC is extended past C, and the exterior angle there always equals A + B — watch it keep pace however you bend the triangle.</p>
    </div>
    <svg class="stage" viewBox="0 0 700 300" role="img" aria-label="A triangle ABC with its exterior angle at C"><g id="tStage"></g></svg>
    <div class="ctrl">
      <label for="tA">Angle A</label><input id="tA" type="range" min="5" max="170" step="5" value="60" aria-label="Angle A"><span class="num" id="tA-v">60°</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="tB">Angle B</label><input id="tB" type="range" min="5" max="170" step="5" value="50" aria-label="Angle B"><span class="num" id="tB-v">50°</span>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">Angle C</div><div class="val" id="t-C">—</div><div class="sub">180° − A − B</div></div>
      <div class="cell d"><div class="lab">Exterior at C</div><div class="val" id="t-E">—</div><div class="sub">= A + B, always</div></div>
      <div class="cell p"><div class="lab">Type</div><div class="val" id="t-T" style="font-size:16px">—</div><div class="sub" id="t-Ts"></div></div>
      <div class="phasebar">
        <span class="pill go" id="t-pill">Bending</span>
        <span id="t-note">The exterior angle and C sit on a straight line, so they add to 180°. So does A + B + C. That's the proof.</span>
        <span class="push"><button class="btn ghost" type="button" id="tPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="tQuiz"></div>
    </div>
  </div>
</section>
'''

TOOL2_HTML = r'''
<section id="poly">
  <div class="panel">
    <div class="panel-top">
      <h2>The polygon machine</h2>
      <p>A regular polygon with n sides. Every diagonal from one corner is drawn, cutting it into n − 2 triangles — which is why the interior angles add to (n − 2) × 180°. Walk round the outside and you turn through the exterior angles, which always add to one full turn.</p>
    </div>
    <svg class="stage" viewBox="0 0 700 300" role="img" aria-label="A regular polygon cut into triangles from one vertex"><g id="pStage"></g></svg>
    <div class="ctrl">
      <label for="pn">Sides n</label><input id="pn" type="range" min="3" max="20" value="6" aria-label="Number of sides"><span class="num" id="pn-v">6</span>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">Interior sum</div><div class="val" id="p-sum">—</div><div class="sub" id="p-sums"></div></div>
      <div class="cell p"><div class="lab">Each interior</div><div class="val" id="p-int">—</div><div class="sub">sum ÷ n</div></div>
      <div class="cell d"><div class="lab">Each exterior</div><div class="val" id="p-ext">—</div><div class="sub">360° ÷ n</div></div>
      <div class="phasebar">
        <span class="pill up" id="p-pill">Cutting</span>
        <span id="p-note" style="font-size:15px">Diagonals in total: —</span>
        <span class="push"><button class="btn ghost" type="button" id="pPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="pQuiz"></div>
    </div>
  </div>
</section>
'''

TRAPS = [
 ("Assuming which angle of an isosceles triangle is given",
  "\"An isosceles triangle has an angle of 70°\" has <strong>two</strong> answers: 70° is a base angle (others 70° and 40°) or the apex (others 55° and 55°). Unless the question says which, give both. If the given angle is over 90°, it can only be the apex."),
 ("Trusting the diagram",
  "Lines that look parallel aren't parallel unless the question says so or marks them with arrows. Angles that look equal aren't equal. IOQM figures are often drawn slightly wrong <em>on purpose</em>. Every step in your chain needs a reason you could say out loud."),
 ("Dividing the polygon sum by n when it isn't regular",
  "(n − 2) × 180° is the <strong>total</strong>. Each angle is that ÷ n only if the polygon is regular. For an irregular pentagon you know the angles add to 540°, nothing about any single one."),
 ("Mixing up interior and exterior",
  "The exterior angle of a regular polygon is 360° ÷ n, and interior + exterior = 180°. A regular polygon with 'angle 20°' — if that's the exterior angle it has 18 sides; if it's the interior angle, it doesn't exist. Read which one the question means."),
 ("Forgetting the hour hand moves",
  "At 3:30 the hour hand is not on the 3 — it's halfway to the 4. The hour hand moves 0.5° per minute, the minute hand 6° per minute. The angle at 3:30 is 75°, not 90°.")
]

DATA_JS = r'''
/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"Angles: Parallel Lines", ch:"Corbettmaths", url:"https://www.youtube.com/watch?v=mM-PU6hmkrg",
  why:"Alternate, corresponding and co-interior angles, with exam-style examples. These three plus 'angles on a line' are most of angle chasing.",
  task:"Draw two parallel lines and a transversal. Mark one angle 58° and fill in all seven others with a reason for each (alternate, corresponding, vertically opposite, on a line)."},

 {t:"Angles in Polygons", ch:"Corbettmaths", url:"https://www.youtube.com/watch?v=gVo8ZrtlSp0",
  why:"Interior and exterior angles of polygons, regular and irregular. The polygon machine below draws why the formula works.",
  task:"Find the interior angle of a regular 9-gon two ways: from (n − 2) × 180 ÷ n, and from 180 − 360 ÷ n. Both should give 140°."},

 {t:"Angles in a Triangle (Part 2)", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=3NKNIgcJgwQ",
  why:"Problems that use the angle sum in less obvious ways — the bridge from school questions to competition ones.",
  task:"Pause before each solution and write the first angle you would label with a letter. That choice is the skill."},

 {t:"Proof: the exterior angle equals the sum of the two opposite interior angles", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=y8aehS_kTS4",
  why:"A short proof you are expected to be able to reproduce — Q10 asks for exactly this.",
  task:"After watching, close the video and write the proof in three lines. Then check it against lesson 2."},

 {t:"Isosceles and Equilateral Triangles", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=BcsQxx5zFy4",
  why:"Equal sides give equal angles, and the converse. Chains of isosceles triangles are where Olympiad angle chasing gets interesting — see Q13.",
  task:"In triangle PQR, PQ = PR and angle Q = 65°. Find angle P. Then: if instead angle P = 65°, find angle Q. (50° and 57.5°.)"},

 {t:"Preparation for Geometry in Math Olympiad: Angle Chasing", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=oEGXjyEYKig",
  why:"A full Olympiad-style angle chase from start to finish. Watch it after the lessons — it's harder than anything else on this page.",
  task:"Note every fact the solution uses, as a list. You should find nothing that isn't in lessons 1–6 below."}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"The five facts", len:"6 min",
  body:`<p>Almost every angle chase uses only these:</p>
        <ol>
          <li><strong>On a straight line</strong>, angles add to 180°.</li>
          <li><strong>Round a point</strong>, angles add to 360°.</li>
          <li><strong>Vertically opposite</strong> angles (the X shape) are equal.</li>
          <li><strong>Parallel lines</strong>: alternate angles (Z shape) are equal, corresponding angles (F shape) are equal, co-interior angles (C shape) add to 180°.</li>
          <li><strong>Triangle</strong>: angles add to 180°, and equal sides face equal angles.</li>
        </ol>
        <p>Every step you write should name one of them. "x = 72° (alternate angles)" earns the mark; "x = 72°" often doesn't, and on a proof question it never does.</p>`,
  demo:`<strong>Do this:</strong> draw two parallel lines cut by one transversal. Mark one angle 58°. Fill in the other seven, with a reason for each. Four should be 58° and four 122°.`,
  cliff:`Fact 5 says a triangle's angles add to 180°. Why? It follows from fact 4.`},

 {t:"Why 180°, and the exterior angle", len:"7 min",
  body:`<p>Draw triangle ABC, and through A draw a line parallel to BC. The two angles either side of A at that line are alternate angles to B and C. Together with A they sit on a straight line, so <strong>A + B + C = 180°</strong>.</p>
        <p>Now extend BC past C. The angle outside the triangle at C is the <span class="detxt">exterior angle</span>. It sits on a straight line with C, so exterior + C = 180°. But A + B + C = 180° too. So:</p>
        <div class="eqline">exterior angle at C = A + B</div>
        <p>This is the fastest tool on the page: one step instead of two. The triangle machine above shows it holding for every shape.</p>`,
  demo:`<strong>Do this:</strong> an exterior angle of a triangle is 110° and one of the two opposite interior angles is 45°. Find the other in one step. (65°.)`,
  cliff:`If two sides of a triangle are equal, two angles are. That turns one known angle into three.`},

 {t:"Isosceles triangles, and chains of them", len:"7 min",
  body:`<p>In an isosceles triangle the two angles <em>opposite</em> the equal sides are equal. So one angle gives you all three:</p>
        <ul><li>Apex 40° → base angles (180 − 40) ÷ 2 = 70° each.</li>
            <li>Base angle 70° → apex 180 − 140 = 40°.</li></ul>
        <p>Olympiad questions chain them. <strong>Example:</strong> AB = AC, and D is on AC with AD = DB = BC. Call angle A = x.</p>
        <ol><li>AD = DB, so angle ABD = x.</li>
            <li>Exterior angle of triangle ABD at D: angle BDC = x + x = 2x.</li>
            <li>DB = BC, so angle BCD = angle BDC = 2x.</li>
            <li>AB = AC, so angle ABC = angle ACB = 2x. Triangle ABC: x + 2x + 2x = 180°, so <strong>x = 36°</strong>.</li></ol>
        <p>Label one angle x, push it round, and let the triangle close the loop. That's angle chasing.</p>`,
  demo:`<strong>Do this:</strong> draw the 36° triangle above with a protractor (A = 36°, B = C = 72°). Mark D on AC so that BD bisects angle B. Measure AD, DB and BC — they should look equal.`,
  cliff:`Triangles add to 180°. What about a shape with twelve sides?`},

 {t:"Polygons: cut them into triangles", len:"6 min",
  body:`<p>From one corner of an n-sided polygon you can draw diagonals to every corner except itself and its two neighbours: n − 3 diagonals, making <strong>n − 2 triangles</strong>. Their angles make up the polygon's angles exactly:</p>
        <div class="eqline">interior angles add to (n − 2) × 180°</div>
        <p>Walk round the outside of any convex polygon and you turn once completely, so:</p>
        <div class="eqline">exterior angles add to 360° &nbsp;&nbsp;&nbsp; regular: each exterior = 360° ÷ n</div>
        <p>For regular polygons the exterior route is quicker: a regular 9-gon has exterior 40°, so interior 140°. Total number of diagonals: each of n corners sends n − 3, and each diagonal gets counted from both ends, so <strong>n(n − 3) ÷ 2</strong>.</p>`,
  demo:`<strong>Do this:</strong> find n for a regular polygon with interior angle 150°. (Exterior 30°, so n = 12.) Then count its diagonals. (54.)`,
  cliff:`Facts are easy to know and hard to chain. How do you choose the next step when you're stuck?`},

 {t:"How to chase", len:"6 min",
  body:`<p>A method for when you can't see the answer:</p>
        <ol><li><strong>Draw it big</strong>, with a ruler, and slightly un-special (don't make an angle look like 90° if it isn't).</li>
            <li><strong>Mark everything given</strong>: equal sides with dashes, parallel lines with arrows, known angles.</li>
            <li><strong>Name the angle you want x.</strong> If there's no obvious start, name a <em>different</em> angle x and express everything in terms of it.</li>
            <li><strong>Hunt for isosceles triangles and exterior angles</strong> — they move an angle across the figure in one step.</li>
            <li><strong>Close a loop</strong>: find a triangle, line or point where your expressions must add to 180° or 360°. That gives the equation.</li></ol>
        <p><strong>Clock hands</strong> are angle chasing with motion: the minute hand turns 6° per minute, the hour hand 0.5° per minute. At 4:20 the hour hand is at 4 × 30 + 20 × 0.5 = 130°, the minute hand at 120°: 10° apart.</p>`,
  demo:`<strong>Do this:</strong> find the angle between the hands at 3:30 and at 9:45. (75° and 22.5°.)`,
  cliff:`IOQM geometry also uses circles. One fact about circles comes straight from isosceles triangles.`},

 {t:"Circles: the radius makes isosceles triangles", len:"7 min",
  body:`<p>Any two radii of a circle are equal, so a triangle with two corners on the circle and one at the centre O is <strong>isosceles</strong>. That's enough to prove the big circle fact:</p>
        <div class="eqline">the angle at the centre is twice the angle at the circumference</div>
        <p><strong>Why.</strong> A, B, C on a circle, centre O. Join OC. Triangles OAC and OBC are isosceles. If angle OCA = p and angle OCB = q, then the exterior angles at O are 2p and 2q, so angle AOB = 2p + 2q = 2 × angle ACB.</p>
        <p><strong>Consequences.</strong> If AB is a diameter, angle AOB = 180°, so the angle at C is <strong>90°</strong> — the angle in a semicircle. If C moves to the other arc, the angle at C becomes 180° minus the old one.</p>`,
  demo:`<strong>Do this:</strong> draw a circle, a diameter AB, and three different points C on the circle. Measure angle ACB each time. It should be 90° every time.`,
  cliff:`That's the lessons. Q14 hides a polygon behind one missing angle, and Q15 puts a triangle in a circle. Go and lose to them, then take them apart.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"Two angles of a triangle are <span class='num'>47°</span> and <span class='num'>68°</span>. The third angle is:",
  o:["55°","65°","75°","115°"], a:1,
  why:"180 − 47 − 68 = 65. Option D is 47 + 68 — that's the exterior angle, not the third interior angle."},
 {n:2, lvl:"standard", q:"Each interior angle of a regular hexagon is:",
  o:["60°","108°","120°","135°"], a:2,
  why:"Exterior 360 ÷ 6 = 60°, so interior 180 − 60 = 120°. Option A is the exterior angle; B is a pentagon; D an octagon."},
 {n:3, lvl:"standard", q:"An exterior angle of a triangle is <span class='num'>110°</span>. One of the two interior angles opposite it is <span class='num'>45°</span>. The other is:",
  o:["45°","65°","70°","135°"], a:1,
  why:"Exterior angle = sum of the two opposite interior angles, so 110 − 45 = 65. Option C is the interior angle next to the exterior one (180 − 110)."},
 {n:4, lvl:"standard", q:"An isosceles triangle has an angle of <span class='num'>100°</span>. Its other two angles are:",
  o:["40° and 40°","100° and 40°","50° and 30°","80° and 80°"], a:0,
  why:"100° can't be a base angle — two of them would already exceed 180°. So it's the apex, and the base angles are (180 − 100) ÷ 2 = 40° each."},
 {n:5, lvl:"trap", q:"An isosceles triangle has an angle of <span class='num'>70°</span>. Its other two angles are:",
  o:["55° and 55° only","70° and 40° only","either 55° and 55°, or 70° and 40°","70° and 70°"], a:2,
  why:"70° could be the apex (base angles 55° each) or a base angle (other base 70°, apex 40°). Both triangles exist. Picking one is the trap — compare Q4, where only one case was possible."}
];

const SHORTS = [
 {n:6, m:2, lvl:"warm-up", q:"Two parallel lines are crossed by a third line, making eight angles. One of them is <span class='num'>58°</span>.<br><strong>(a)</strong> How many of the eight angles are 58°? <span class='num'>[1]</span><br><strong>(b)</strong> What size are the others? <span class='num'>[1]</span>",
  scheme:["(a) <strong>4</strong> (vertically opposite, corresponding, alternate) <span class='num'>[1]</span>",
          "(b) <strong>122°</strong> (angles on a straight line) <span class='num'>[1]</span>"],
  tip:"Every angle in that figure is either the acute one or its supplement. If you got a third value, something isn't parallel."},
 {n:7, m:2, lvl:"standard", q:"The interior angles of a pentagon are <span class='num'>x, x + 10, x + 20, x + 30</span> and <span class='num'>x + 40</span> degrees. Find x.",
  scheme:["Sum = (5 − 2) × 180 = 540, so 5x + 100 = 540 <span class='num'>[1]</span>",
          "<strong>x = 88</strong> <span class='num'>[1]</span>"],
  tip:"Check the angles: 88, 98, 108, 118, 128 add to 540. Notice the middle one is 108 — the regular pentagon angle — which is no coincidence."},
 {n:8, m:2, lvl:"standard", q:"Each exterior angle of a regular polygon is <span class='num'>24°</span>.<br><strong>(a)</strong> How many sides does it have? <span class='num'>[1]</span><br><strong>(b)</strong> What do its interior angles add to? <span class='num'>[1]</span>",
  scheme:["(a) 360 ÷ 24 = <strong>15</strong> <span class='num'>[1]</span>",
          "(b) (15 − 2) × 180 = <strong>2340°</strong> <span class='num'>[1]</span>"],
  tip:"For (b) you could also do 15 × 156 (each interior angle). Both routes should agree — use one to check the other."},
 {n:9, m:2, lvl:"standard", q:"In triangle ABC, angle A = <span class='num'>50°</span>. The bisectors of angles B and C meet at I. Find angle BIC.",
  scheme:["B + C = 130°, so half of each together: ½B + ½C = 65° <span class='num'>[1]</span>",
          "Triangle BIC: angle BIC = 180 − 65 = <strong>115°</strong> <span class='num'>[1]</span>"],
  tip:"You never needed B or C separately. In general angle BIC = 90° + ½A — a fact worth knowing, but derive it, don't just quote it."},
 {n:10, m:2, lvl:"hard", q:"Prove that an exterior angle of a triangle equals the sum of the two interior angles opposite it.",
  scheme:["Exterior angle at C and angle C lie on a straight line, so they add to 180° <span class='num'>[1]</span>",
          "A + B + C = 180° too, so exterior = 180° − C = <strong>A + B</strong> <span class='num'>[1]</span>"],
  tip:"A proof names its facts. 'Straight line' and 'angle sum of a triangle' are the two words the marks hang on."}
];

const WORDS = [
 {n:11, m:3, lvl:"standard", q:"Find the smaller angle between the hands of a clock at:<br><strong>(a)</strong> 3:00 <span class='num'>[1]</span> &nbsp; <strong>(b)</strong> 3:30 <span class='num'>[1]</span> &nbsp; <strong>(c)</strong> 4:20 <span class='num'>[1]</span>",
  hints:["Measure both hands clockwise from 12. The minute hand moves 360° in 60 minutes: 6° per minute.",
         "The hour hand moves 30° per hour, which is 0.5° per minute. At 3:30 it has gone 3 hours and 30 minutes.",
         "Subtract the two positions. If the result is over 180°, take 360° minus it."],
  sol:["(a) Hour hand 90°, minute hand 0°: <strong>90°</strong>.",
       "(b) Hour hand 90 + 15 = 105°, minute hand 180°: <strong>75°</strong>.",
       "(c) Hour hand 120 + 10 = 130°, minute hand 120°: <strong>10°</strong>.",
       "At 4:20 the hands look almost on top of each other — and they nearly are. Saying 0° here is the trap: the hour hand has moved a third of the way to the 5."]},

 {n:12, m:3, lvl:"standard", q:"Each interior angle of a regular polygon is four times its exterior angle.<br><br><strong>(a)</strong> Find the exterior angle. <span class='num'>[1]</span><br><strong>(b)</strong> How many sides does the polygon have? <span class='num'>[1]</span><br><strong>(c)</strong> How many diagonals does it have? <span class='num'>[1]</span>",
  hints:["Interior + exterior = 180°. If the exterior is e, the interior is 4e.",
         "Number of sides = 360 ÷ exterior angle.",
         "Each corner sends a diagonal to every corner except itself and its two neighbours. Then don't count each diagonal twice."],
  sol:["(a) e + 4e = 180, so <strong>e = 36°</strong>.",
       "(b) 360 ÷ 36 = <strong>10 sides</strong>.",
       "(c) 10 × (10 − 3) ÷ 2 = <strong>35 diagonals</strong>.",
       "Check: interior 144° = 4 × 36° ✓. The ÷ 2 in (c) is the counting idea from the combinatorics page: each diagonal has two ends."]},

 {n:13, m:3, lvl:"standard", q:"In triangle ABC, AB = AC. Point D lies on AC so that AD = DB = BC. Let angle BAC = x.<br><br><strong>(a)</strong> Explain why angle ABD = x. <span class='num'>[1]</span><br><strong>(b)</strong> Show that angle BCA = 2x. <span class='num'>[1]</span><br><strong>(c)</strong> Find x. <span class='num'>[1]</span>",
  hints:["Draw it. AD = DB makes triangle ABD isosceles — which two angles are equal?",
         "Angle BDC is an exterior angle of triangle ABD. Then DB = BC makes triangle DBC isosceles.",
         "AB = AC, so angle ABC = angle ACB. Add up the angles of triangle ABC."],
  sol:["(a) AD = DB, so triangle ABD is isosceles with angle DAB = angle ABD = <strong>x</strong>.",
       "(b) Angle BDC is exterior to triangle ABD, so it equals x + x = 2x. DB = BC, so angle BCD = angle BDC = <strong>2x</strong>, and angle BCD is angle BCA.",
       "(c) AB = AC gives angle ABC = angle ACB = 2x. So x + 2x + 2x = 180 and <strong>x = 36°</strong>.",
       "This is the 36°–72°–72° 'golden triangle'. Three isosceles triangles, one exterior angle, one loop closed — that's an angle chase."]},

 {n:14, m:3, lvl:"hard", q:"All but one of the interior angles of a convex polygon add up to <span class='num'>2190°</span>.<br><br><strong>(a)</strong> Explain why the full sum must be a multiple of 180° and less than 2190° + 180°. <span class='num'>[1]</span><br><strong>(b)</strong> How many sides does the polygon have? <span class='num'>[1]</span><br><strong>(c)</strong> Find the missing angle. <span class='num'>[1]</span>",
  hints:["The full sum is (n − 2) × 180°. And in a convex polygon each angle is less than 180°.",
         "Find the first multiple of 180 that is bigger than 2190.",
         "Missing angle = full sum − 2190."],
  sol:["(a) The full sum is (n − 2) × 180°. The missing angle is between 0° and 180° (convex), so the full sum is between 2190° and 2370°.",
       "(b) 12 × 180 = 2160 is too small, 13 × 180 = 2340 fits. So n − 2 = 13 and <strong>n = 15</strong>.",
       "(c) 2340 − 2190 = <strong>150°</strong>.",
       "The word 'convex' is doing the work. Without it an angle could exceed 180°, and 14 × 180 = 2520 (missing angle 330°) would be possible too."]},

 {n:15, m:3, lvl:"hard", q:"A, B and C lie on a circle with centre O. Angle AOB = <span class='num'>110°</span>.<br><br><strong>(a)</strong> Explain why triangles OAC and OBC are isosceles. <span class='num'>[1]</span><br><strong>(b)</strong> C lies on the major arc AB (the long way round). Show that angle ACB = 55°. <span class='num'>[1]</span><br><strong>(c)</strong> C is moved onto the minor arc AB. Find angle ACB now. <span class='num'>[1]</span>",
  hints:["What do OA, OB and OC have in common?",
         "Let angle OCA = p and angle OCB = q. Extend CO through O. Each isosceles triangle has an exterior angle at O equal to twice its base angle.",
         "With C on the minor arc, the angle at the centre that it 'sees' is the reflex angle, 360° − 110°."],
  sol:["(a) OA, OB and OC are all radii, so OA = OC and OB = OC.",
       "(b) In OAC the base angles are p and p, so the exterior angle at O (on line CO extended) is 2p; likewise 2q in OBC. Those add to angle AOB: 2p + 2q = 110°, so angle ACB = p + q = <strong>55°</strong>.",
       "(c) Now C faces the reflex angle 250°, so angle ACB = 250 ÷ 2 = <strong>125°</strong>.",
       "55° + 125° = 180°: that's the cyclic quadrilateral fact (opposite angles add to 180°) falling out for free. Every circle theorem you'll meet in IGCSE is this isosceles argument in disguise."]}
];
'''

TOOLS_JS = r'''
/* ---------------- the triangle machine ---------------- */
let tTarget=null, curTPuzzle=null;
function deg(r){ return r*180/Math.PI; } function rad(d){ return d*Math.PI/180; }
function arc(cx,cy,r,a0,a1,col){
  const x0=cx+r*Math.cos(rad(a0)), y0=cy-r*Math.sin(rad(a0)), x1=cx+r*Math.cos(rad(a1)), y1=cy-r*Math.sin(rad(a1));
  const large = ((a1-a0+360)%360)>180?1:0;
  return `<path d="M${cx} ${cy} L${x0.toFixed(1)} ${y0.toFixed(1)} A${r} ${r} 0 ${large} 0 ${x1.toFixed(1)} ${y1.toFixed(1)} Z" fill="${col}" opacity=".28"/>`;
}
function drawTri(){
  const A=+document.getElementById('tA').value, Bv=+document.getElementById('tB').value;
  document.getElementById('tA-v').textContent=A+'°'; document.getElementById('tB-v').textContent=Bv+'°';
  const pill=document.getElementById('t-pill'), note=document.getElementById('t-note');
  let g='';
  if(A+Bv>=180){
    g=`<text x="350" y="150" text-anchor="middle" font-family="var(--mono)" font-size="15" fill="var(--no)">A + B = ${A+Bv}° — no room left for C. No triangle.</text>`;
    document.getElementById('tStage').innerHTML=g;
    ['t-C','t-E','t-T'].forEach(id=>document.getElementById(id).textContent='—');
    note.textContent='Two angles of a triangle always add to less than 180°.';
    return;
  }
  const C=180-A-Bv;
  // B at left, C at right on base; A above. base length L; use sine rule: AB/sinC = BC/sinA
  const L=1, AB=L*Math.sin(rad(C))/Math.sin(rad(A));
  let Bx=0,By=0,Cx=L,Cy=0, Ax=AB*Math.cos(rad(Bv)), Ay=AB*Math.sin(rad(Bv));
  const xs=[Bx,Cx,Ax, Cx+0.45], ys=[By,Cy,Ay];
  const minx=Math.min(...xs), maxx=Math.max(...xs), maxy=Math.max(...ys);
  const sc=Math.min(520/(maxx-minx), 230/Math.max(maxy,0.05));
  const tx=x=>90+(x-minx)*sc, ty=y=>265-y*sc;
  const P={B:[tx(Bx),ty(By)], C:[tx(Cx),ty(Cy)], A:[tx(Ax),ty(Ay)]};
  g+=`<line x1="${P.C[0]}" y1="${P.C[1]}" x2="${tx(Cx+0.45)}" y2="${P.C[1]}" stroke="var(--steel)" stroke-width="2" stroke-dasharray="6 5"/>`;
  // angle arcs (directions measured in screen coords with y up)
  const dir=(p,q)=>{ const d=deg(Math.atan2(-(q[1]-p[1]), q[0]-p[0])); return (d+360)%360; };
  g+=arc(P.B[0],P.B[1],30,0,dir(P.B,P.A),'var(--pm)');
  g+=arc(P.A[0],P.A[1],26,dir(P.A,P.B),dir(P.A,P.C),'var(--ng)');
  g+=arc(P.C[0],P.C[1],24,dir(P.C,P.A),180,'var(--rt)');
  g+=arc(P.C[0],P.C[1],40,0,dir(P.C,P.A),'var(--ng)');
  g+=`<polygon points="${P.A.join(',')} ${P.B.join(',')} ${P.C.join(',')}" fill="none" stroke="var(--ink)" stroke-width="2.5" stroke-linejoin="round"/>`;
  const lab=(t,p,dx,dy)=>`<text x="${(p[0]+dx).toFixed(1)}" y="${(p[1]+dy).toFixed(1)}" font-family="var(--display)" font-size="17" font-weight="700" fill="var(--ink)">${t}</text>`;
  g+=lab('A',P.A,-6,-12)+lab('B',P.B,-20,6)+lab('C',P.C,-6,22);
  const ext=dir(P.C,P.A)/2;
  g+=`<text x="${(P.C[0]+58*Math.cos(rad(ext))).toFixed(1)}" y="${(P.C[1]-58*Math.sin(rad(ext))).toFixed(1)}" font-family="var(--mono)" font-size="13" font-weight="700" fill="var(--ng)">${A+Bv}°</text>`;
  document.getElementById('tStage').innerHTML=g;
  document.getElementById('t-C').textContent=C+'°';
  document.getElementById('t-E').textContent=(A+Bv)+'°';
  const angs=[A,Bv,C].sort((a,b)=>a-b);
  let kind = angs[2]===90?'right-angled':angs[2]>90?'obtuse':'acute';
  let sides = (A===Bv&&Bv===C)?'equilateral':(A===Bv||Bv===C||A===C)?'isosceles':'scalene';
  document.getElementById('t-T').textContent=kind+', '+sides;
  document.getElementById('t-Ts').textContent=`angles ${A}°, ${Bv}°, ${C}°`;
  if(tTarget){
    const T=tTarget; pill.className='pill up'; pill.textContent='Puzzle running';
    if(T.check(A,Bv,C)){
      tTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('tQuiz'); box.classList.add('on');
      box.innerHTML=`<strong>That's the one: ${A}°, ${Bv}°, ${C}°.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="tAgain">Another one</button></div>`;
      document.getElementById('tAgain').addEventListener('click', ()=>document.getElementById('tPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Set up the equation, solve it, then set the sliders — not the other way round.';
    }else note.textContent=`Now: A = ${A}°, B = ${Bv}°, C = ${C}°, exterior at C = ${A+Bv}°.`;
  }else{
    pill.className='pill go'; pill.textContent='Bending';
    note.textContent='The exterior angle and C sit on a straight line, so they add to 180°. So does A + B + C. That\'s the proof.';
  }
}
const sameSet=(x,y)=>x.slice().sort((a,b)=>a-b).join()===y.slice().sort((a,b)=>a-b).join();
const T_PUZZLES=[
 {txt:'an isosceles triangle with angle C = 40° at the apex (so A = B)', check:(A,B,C)=>C===40&&A===B, more:'Base angles (180 − 40) ÷ 2 = 70° each.'},
 {txt:'a triangle with A = 50° and an exterior angle of 130° at C', check:(A,B,C)=>A===50&&A+B===130, more:'Exterior = A + B, so B = 80°.'},
 {txt:'a right-angled triangle whose smallest angle is 35°', check:(A,B,C)=>sameSet([A,B,C],[35,55,90]), more:'The other two angles share 90°, so 35° and 55°.'},
 {txt:'a triangle whose angles are in the ratio 1 : 2 : 3', check:(A,B,C)=>sameSet([A,B,C],[30,60,90]), more:'6 parts make 180°, so one part is 30°.'},
 {txt:'a triangle whose angles are in the ratio 2 : 3 : 4', check:(A,B,C)=>sameSet([A,B,C],[40,60,80]), more:'9 parts make 180°: 20° each.'},
 {txt:'an isosceles triangle with A = B and an exterior angle of 100° at C', check:(A,B,C)=>A===B&&A+B===100, more:'A + B = 100° and A = B, so 50° each and C = 80°.'}
];
['tA','tB'].forEach(id=>document.getElementById(id).addEventListener('input', drawTri));
document.getElementById('tPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*T_PUZZLES.length);
  if(curTPuzzle===i) i=(i+1)%T_PUZZLES.length;
  curTPuzzle=i; tTarget=T_PUZZLES[i];
  document.getElementById('tA').value=5; document.getElementById('tB').value=5;   /* start from an unsolved state */
  const box=document.getElementById('tQuiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> Make ${tTarget.txt}. Work out the angles first, then set A and B.`;
  drawTri();
});

/* ---------------- the polygon machine ---------------- */
let pTarget=null, curPPuzzle=null;
function drawPoly(){
  const n=+document.getElementById('pn').value;
  document.getElementById('pn-v').textContent=n;
  const cx=200, cy=150, R=125, pts=[];
  for(let k=0;k<n;k++){ const a=-Math.PI/2+2*Math.PI*k/n; pts.push([cx+R*Math.cos(a), cy+R*Math.sin(a)]); }
  let g='';
  const cols=['var(--pm-tint)','var(--ng-tint)','var(--rt-tint)'];
  for(let k=1;k<n-1;k++) g+=`<polygon points="${pts[0].join(',')} ${pts[k].join(',')} ${pts[k+1].join(',')}" fill="${cols[k%3]}" stroke="var(--steel)" stroke-width="1"/>`;
  g+=`<polygon points="${pts.map(p=>p.map(v=>v.toFixed(1)).join(',')).join(' ')}" fill="none" stroke="var(--ink)" stroke-width="2.5"/>`;
  g+=`<circle cx="${pts[0][0]}" cy="${pts[0][1]}" r="5" fill="var(--pm)"/>`;
  const sum=(n-2)*180, each=sum/n, ext=360/n, diag=n*(n-3)/2;
  const fmt=v=>Number.isInteger(v)?v+'°':v.toFixed(2)+'°';
  g+=`<text x="420" y="70" font-family="var(--mono)" font-size="14" fill="var(--ink)">${n} sides</text>`;
  g+=`<text x="420" y="100" font-family="var(--mono)" font-size="14" fill="var(--ink)">${n-2} triangles from one corner</text>`;
  g+=`<text x="420" y="130" font-family="var(--mono)" font-size="14" fill="var(--ink)">${n-3} diagonals from that corner</text>`;
  g+=`<text x="420" y="175" font-family="var(--mono)" font-size="14" fill="var(--ink-soft)">${n-2} × 180° = ${sum}°</text>`;
  g+=`<text x="420" y="205" font-family="var(--mono)" font-size="14" fill="var(--ink-soft)">interior + exterior</text>`;
  g+=`<text x="420" y="228" font-family="var(--mono)" font-size="14" fill="var(--ink-soft)">= ${fmt(each)} + ${fmt(ext)} = 180°</text>`;
  document.getElementById('pStage').innerHTML=g;
  document.getElementById('p-sum').textContent=sum+'°';
  document.getElementById('p-sums').textContent=`(${n} − 2) × 180°`;
  document.getElementById('p-int').textContent=fmt(each);
  document.getElementById('p-ext').textContent=fmt(ext);
  const pill=document.getElementById('p-pill'), note=document.getElementById('p-note');
  if(pTarget){
    const T=pTarget; pill.className='pill up'; pill.textContent='Puzzle running';
    if(n===T.n){
      pTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('pQuiz'); box.classList.add('on');
      box.innerHTML=`<strong>${n} sides.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="pAgain">Another one</button></div>`;
      document.getElementById('pAgain').addEventListener('click', ()=>document.getElementById('pPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent=`Diagonals in total: ${diag}.`;
    }else note.textContent='Not this one. Work it out from 360° ÷ n or (n − 2) × 180°, then slide.';
  }else{
    pill.className='pill up'; pill.textContent='Cutting';
    note.textContent=`Diagonals in total: ${n} × ${n-3} ÷ 2 = ${diag}.`;
  }
}
const P_PUZZLES=[
 {txt:'each interior angle is 140°', n:9, more:'Exterior 40°, and 360 ÷ 40 = 9.'},
 {txt:'each exterior angle is 24°', n:15, more:'360 ÷ 24 = 15.'},
 {txt:'the interior angles add to 1440°', n:10, more:'1440 ÷ 180 = 8 triangles, so 10 sides.'},
 {txt:'each interior angle is 3 times each exterior angle', n:8, more:'4 × exterior = 180°, so exterior 45° and n = 8.'},
 {txt:'each interior angle is 150°', n:12, more:'Exterior 30°, so 12 sides.'},
 {txt:'it has 44 diagonals altogether', n:11, more:'n(n − 3) ÷ 2 = 44 gives n(n − 3) = 88 = 11 × 8.'}
];
document.getElementById('pn').addEventListener('input', drawPoly);
document.getElementById('pPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*P_PUZZLES.length);
  if(curPPuzzle===i) i=(i+1)%P_PUZZLES.length;
  curPPuzzle=i; pTarget=P_PUZZLES[i];
  document.getElementById('pn').value=3;   /* start from an unsolved state */
  const box=document.getElementById('pQuiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> Find the regular polygon where ${pTarget.txt}. Work out n on paper, then set it.`;
  drawPoly();
});
'''

BOOT = ['drawTri()', 'drawPoly()']
