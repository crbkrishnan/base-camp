# -*- coding: utf-8 -*-
ID = 'ioqm-areas'
SHORT_TITLE = 'Same Base, Same Height'
SUB = 'IOQM · Geometry II: area chasing, Pythagoras, similar triangles'
BLURB = ("Slide a triangle's top corner along a parallel line and its area doesn't move — the fact behind most Olympiad area problems. "
         "Then build squares on the sides of a right triangle and hunt for the rare ones where every side is a whole number.")
META_TOOL = 'sliding apex'
COLOURS = ('#0E6E6E', '#E1F2F2', '#8E3B6E', '#F6E8F1', '#7C5A12', '#F5EEDF')
EYEBROW = 'IOQM Olympiad Prep · Geometry II'
H1 = 'Same <i>Base</i>,<br>Same <em>Height</em>'
LEDE = ("Half base times height looks like the easiest formula you know. Used cleverly, it answers questions where you can't measure "
        "a single height. Add Pythagoras and similar triangles, and you have nearly every length-and-area tool IOQM asks for.")
TARGET = ("You've been landing around <span class=\"num\">10 out of 15</span> at school. This page is out of <span class=\"num\">30</span>; "
          "the targets are <span class=\"num\">21</span> on the first pass and <span class=\"num\">26</span> on the second. No calculator — "
          "which is exactly why Pythagorean triples are worth learning by heart.")
VIDEO_MIN = '~40 min total'
LESSON_MIN = '~40 min total'
NAV = [('apex', 'Sliding apex'), ('videos', '6 videos'), ('lessons', '6 lessons'), ('pyth', 'Square builder'),
       ('quick', 'Quick checks'), ('short', 'Short answers'), ('word', 'Word problems'), ('traps', 'Exam traps')]

EXTRA_CSS = r'''
'''

TOOL1_HTML = r'''
<section id="apex">
  <div class="panel">
    <div class="panel-top">
      <h2>The sliding apex</h2>
      <p>Triangle ABC sits on base BC. The top corner A rides along a dashed line parallel to the base. Slide A as far as you like — the triangle leans, stretches, goes obtuse — and its area doesn't change, because the base and the height don't.</p>
    </div>
    <svg class="stage" viewBox="0 0 700 300" role="img" aria-label="A triangle with its apex on a line parallel to the base"><g id="aStage"></g></svg>
    <div class="ctrl">
      <label for="ab">Base BC</label><input id="ab" type="range" min="2" max="12" value="8" aria-label="Base length"><span class="num" id="ab-v">8</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="ah">Height</label><input id="ah" type="range" min="1" max="10" value="5" aria-label="Height"><span class="num" id="ah-v">5</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="ao">Slide A</label><input id="ao" type="range" min="-6" max="18" value="3" aria-label="Horizontal position of A, measured from B"><span class="num" id="ao-v">3</span>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">Area</div><div class="val" id="a-area">—</div><div class="sub">½ × base × height</div></div>
      <div class="cell d"><div class="lab">Sides AB, AC</div><div class="val" id="a-sides" style="font-size:16px">—</div><div class="sub">these change; the area doesn't</div></div>
      <div class="cell p"><div class="lab">Angle at B</div><div class="val" id="a-ang" style="font-size:16px">—</div><div class="sub" id="a-angs"></div></div>
      <div class="phasebar">
        <span class="pill go" id="a-pill">Sliding</span>
        <span id="a-note">The height is measured straight down to the base line — even when A is outside the base.</span>
        <span class="push"><button class="btn ghost" type="button" id="aPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="aQuiz"></div>
    </div>
  </div>
</section>
'''

TOOL2_HTML = r'''
<section id="pyth">
  <div class="panel">
    <div class="panel-top">
      <h2>The square builder</h2>
      <p>A right-angled triangle with legs a and b, and a square on each side. The two smaller squares always have exactly the area of the big one. Most of the time the hypotenuse comes out as an ugly root — the green flag goes up when it's a whole number.</p>
    </div>
    <svg class="stage" viewBox="0 0 700 320" role="img" aria-label="A right triangle with squares on its three sides"><g id="pStage2"></g></svg>
    <div class="ctrl">
      <label for="pa">Leg a</label><input id="pa" type="range" min="1" max="20" value="3" aria-label="Leg a"><span class="num" id="pa-v">3</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="pb">Leg b</label><input id="pb" type="range" min="1" max="20" value="4" aria-label="Leg b"><span class="num" id="pb-v">4</span>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">a² + b²</div><div class="val" id="p-ab">—</div><div class="sub" id="p-abs"></div></div>
      <div class="cell p"><div class="lab">Hypotenuse c</div><div class="val" id="p-c">—</div><div class="sub" id="p-cs"></div></div>
      <div class="cell d"><div class="lab">Whole-number triple?</div><div class="val" id="p-t" style="font-size:16px">—</div><div class="sub" id="p-ts"></div></div>
      <div class="phasebar">
        <span class="pill up" id="p2-pill">Building</span>
        <span id="p2-note">Try 3 and 4, then 6 and 8, then 9 and 12. Multiples of a triple are triples.</span>
        <span class="push"><button class="btn ghost" type="button" id="p2Puzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="p2Quiz"></div>
    </div>
  </div>
</section>
'''

TRAPS = [
 ("Using a slanted side as the height",
  "The height is the <strong>perpendicular</strong> distance from the apex to the base line. In an obtuse triangle it lands outside the triangle — slide the apex past B on the tool and watch. Using the side AB instead of the height gives a bigger, wrong area every time."),
 ("Using Pythagoras on the wrong side",
  "c² = a² + b² only when c is the <strong>hypotenuse</strong> — the longest side, opposite the right angle. If you're given a leg and the hypotenuse, you subtract: a² = c² − b². And it only works for right-angled triangles at all."),
 ("Scaling area by k instead of k²",
  "If two similar triangles have sides in ratio 1 : 3, their areas are in ratio <strong>1 : 9</strong>. Lengths scale by k, areas by k², volumes by k³. A photo enlarged to twice the width uses four times the paper."),
 ("Matching the wrong sides in similar triangles",
  "Corresponding sides face <strong>equal angles</strong>. Write the triangles with their equal angles in the same order (ADE ~ ABC) and read the ratios straight off: AD/AB = AE/AC = DE/BC. Matching by 'the one that looks the same size' goes wrong whenever the small triangle is flipped."),
 ("Thinking √(a² + b²) = a + b",
  "√(9 + 16) = 5, not 3 + 4 = 7. Square roots don't split over addition. The hypotenuse is always shorter than the two legs added together — it's the straight route.")
]

DATA_JS = r'''
/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"Areas of Rectangles and Right Triangles", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=4NNUvO8pvME",
  why:"Where ½ × base × height comes from: a triangle is half a rectangle. Short, and it sets up every other video.",
  task:"Draw a right-angled triangle with legs 6 and 8 on squared paper, and the rectangle it's half of. Count squares to check the area is 24."},

 {t:"Triangles on the same base and between the same parallels are equal in area", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=qH_E3W7XiWA",
  why:"The theorem the sliding apex tool demonstrates, with its proof. Q15 and the hardest area-chasing questions rest on it.",
  task:"Write the theorem in your own words in one sentence. Then draw two different triangles with base 6 and height 4 that look nothing alike."},

 {t:"Triangles with the same base or height", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=xThL_w07M4g",
  why:"The ratio version: same height means areas are in the ratio of the bases. This is the single most useful area-chasing fact.",
  task:"Triangle ABC has area 60 and D is on BC with BD : DC = 1 : 2. Find the areas of ABD and ADC. (20 and 40.)"},

 {t:"Pythagorean Theorem II (visual proof)", ch:"Mathematical Visual Proofs", url:"https://www.youtube.com/watch?v=yfGtbNgcrQ8",
  why:"One of the oldest proofs: one square cut up two ways. Seeing it once is worth memorising the formula ten times.",
  task:"After watching, draw the two arrangements yourself with a = 3 and b = 4 and label every area."},

 {t:"Power of Pythagorean Triples", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=mYXcwRAXWjA",
  why:"Why knowing 3-4-5, 5-12-13, 8-15-17 and 7-24-25 saves minutes in a no-calculator exam.",
  task:"Write the four triples on a card. Add the first two multiples of 3-4-5 and of 5-12-13. Test yourself until you can say the third number instantly."},

 {t:"Pythagorean Triple Warning!", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=RgUZkmhA9bw",
  why:"The trap: seeing a 5 and a 13 and assuming the missing side is 12 when 13 isn't actually the hypotenuse.",
  task:"A right triangle has legs 5 and 13. Find the hypotenuse. (√194 — not 12, and not a whole number.)"}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"Half base times height, and why sliding doesn't matter", len:"7 min",
  body:`<p>A triangle's area is ½ × base × height, where the height is the perpendicular distance from the apex to the line the base sits on. Two consequences do most of the work in Olympiad area questions:</p>
        <ol><li><strong>Same base, same height, same area.</strong> If two triangles share a base and their apexes lie on a line parallel to it, their areas are equal — however different they look. That's the sliding apex tool.</li>
            <li><strong>Same height, areas in the ratio of bases.</strong> If D is on BC, triangles ABD and ADC have the same height from A, so</li></ol>
        <div class="eqline">area ABD : area ADC = BD : DC</div>
        <p>In particular a <span class="frtxt">median</span> (A to the midpoint of BC) always cuts a triangle into two equal areas — for every triangle, not just special ones.</p>`,
  demo:`<strong>Do this:</strong> on the sliding apex, set base 8 and height 5, and slide A from −6 to 18. Write down AB at three positions. The area stays 20 while AB changes a lot.`,
  cliff:`What if a triangle sits on a grid with no side lying flat?`},

 {t:"Area by subtraction", len:"6 min",
  body:`<p>Triangle with corners (0, 0), (6, 2) and (2, 5). No side is horizontal, so no height is easy. Instead, <strong>box it in</strong>:</p>
        <ul><li>The rectangle around it is 6 × 5 = 30.</li>
            <li>Three right-angled triangles fill the corners: ½ × 6 × 2 = 6, ½ × 4 × 3 = 6, ½ × 2 × 5 = 5.</li></ul>
        <div class="eqline">area = 30 − 6 − 6 − 5 = 13</div>
        <p>The same idea in reverse: to find a strange shaded region, find something simple that contains it, and subtract the simple pieces that aren't shaded. Q12 is exactly this inside a square.</p>
        <p>A <strong>trapezium</strong> (one pair of parallel sides a and b, height h) has area ½(a + b)h — it's two triangles, or a rectangle with two bits moved.</p>`,
  demo:`<strong>Do this:</strong> find the area of the triangle with corners (1, 1), (7, 3) and (3, 6) by boxing it in. (6 × 5 = 30, minus 6, 6 and 5: 13 — the same triangle, moved.)`,
  cliff:`Right-angled triangles keep appearing as the corner pieces. They have a secret about their sides.`},

 {t:"Pythagoras, and why it's true", len:"7 min",
  body:`<p>In a right-angled triangle with legs a, b and hypotenuse c:</p>
        <div class="eqline">a² + b² = c²</div>
        <p><strong>A proof you can draw.</strong> Put four copies of the triangle inside a square of side a + b, with their hypotenuses making a tilted square in the middle. The middle square has area c². The four triangles have area 4 × ½ab = 2ab. So:</p>
        <div class="eqline">(a + b)² = c² + 2ab &nbsp;⟹&nbsp; a² + 2ab + b² = c² + 2ab &nbsp;⟹&nbsp; a² + b² = c²</div>
        <p>That's the identity from the algebra page doing geometry.</p>
        <p><strong>The converse</strong> is also true: if a² + b² = c², the angle opposite c is exactly 90°. That's how builders check a corner with a 3-4-5 rope. And if a² + b² > c², the angle is acute; if less, obtuse.</p>`,
  demo:`<strong>Do this:</strong> a ladder 13 m long has its foot 5 m from a wall. How high up the wall does it reach? (12 m.) Now the foot slides out to 12 m. How far did the top slide down? (7 m.)`,
  cliff:`3, 4, 5. 5, 12, 13. Are there many triangles where all three sides are whole numbers?`},

 {t:"Pythagorean triples", len:"6 min",
  body:`<p>Whole-number right triangles are rare and worth learning. The four primitive ones under 30:</p>
        <table class="data"><tr><th>Triple</th><th>Check</th></tr>
        <tr><td>3, 4, 5</td><td>9 + 16 = 25</td></tr>
        <tr><td>5, 12, 13</td><td>25 + 144 = 169</td></tr>
        <tr><td>8, 15, 17</td><td>64 + 225 = 289</td></tr>
        <tr><td>7, 24, 25</td><td>49 + 576 = 625</td></tr>
        <tr><td>20, 21, 29</td><td>400 + 441 = 841</td></tr></table>
        <p>Every multiple of a triple is a triple: 6-8-10, 9-12-15, 15-20-25. In an exam, spot the multiple first: 15 and 20 are 5 × 3 and 5 × 4, so the hypotenuse is 25 with no squaring at all.</p>
        <p><strong>Finding them all.</strong> If one leg is fixed, use difference of squares: c² − b² = a², so (c − b)(c + b) = a², and list factor pairs. That's Q14.</p>`,
  demo:`<strong>Do this:</strong> on the square builder, find every triple with a leg of 12 that fits on the sliders (both legs up to 20). You should find 5-12-13, 9-12-15 and 12-16-20.`,
  cliff:`Two triangles can be different sizes and still the same shape. What stays the same?`},

 {t:"Similar triangles", len:"7 min",
  body:`<p>Triangles are <strong>similar</strong> when their angles are equal. Then their sides are in proportion — one is a scaled copy of the other. Two equal angles are enough (the third follows).</p>
        <p>The commonest setup: a line DE parallel to BC cuts AB at D and AC at E. Corresponding angles give ADE ~ ABC, so</p>
        <div class="eqline">AD/AB = AE/AC = DE/BC = k</div>
        <p><strong>Areas scale by k².</strong> If AD = 4 and DB = 6, then k = 4/10 = 2/5, so DE = 2/5 × BC and area ADE = 4/25 of area ABC.</p>
        <p>Shadows are similar triangles: the sun's rays are parallel, so a person and a tree make triangles with the same angles. Height/shadow is the same for both.</p>`,
  demo:`<strong>Do this:</strong> a 1.5 m student casts a 2 m shadow; a tree at the same moment casts a 14 m shadow. How tall is the tree? (10.5 m.)`,
  cliff:`One right triangle, two different ways to compute its area. Set them equal and something falls out.`},

 {t:"Area two ways", len:"6 min",
  body:`<p>A right triangle with legs 6 and 8 has hypotenuse 10 and area ½ × 6 × 8 = 24. But you could also take the hypotenuse as the base, with the altitude h from the right angle as the height:</p>
        <div class="eqline">½ × 10 × h = 24 &nbsp;⟹&nbsp; h = 4.8</div>
        <p>In general the altitude to the hypotenuse is <strong>ab ÷ c</strong>. No trigonometry, no similar triangles — just the same area written twice.</p>
        <p>This "compute one quantity two ways" move is everywhere in Olympiad geometry. It also proves the ratio rule: chasing areas through a figure, with each step using a shared height, often gives a length you couldn't measure directly. Q15 does exactly this with a midpoint.</p>`,
  demo:`<strong>Do this:</strong> find the altitude to the hypotenuse of the 5-12-13 triangle. (60/13.) Then of the 9-12-15 triangle. (7.2.)`,
  cliff:`That's the lessons. Q14 finds every right triangle with a leg of 12, and Q15 chases an area through a midpoint. Go and lose to them, then take them apart.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"A triangle has base <span class='num'>10 cm</span> and height <span class='num'>7 cm</span>. Its area is:",
  o:["17 cm²","35 cm²","70 cm²","140 cm²"], a:1,
  why:"½ × 10 × 7 = 35. Option C forgets the half — that's the rectangle the triangle is half of."},
 {n:2, lvl:"standard", q:"A right-angled triangle has legs <span class='num'>9</span> and <span class='num'>12</span>. Its hypotenuse is:",
  o:["13","15","21","225"], a:1,
  why:"9-12-15 is 3 × (3-4-5). Or: 81 + 144 = 225 = 15². Option D forgot the square root; option C added the legs."},
 {n:3, lvl:"standard", q:"Which of these is <strong>not</strong> the side lengths of a right-angled triangle?",
  o:["5, 12, 13","8, 15, 17","7, 24, 25","6, 9, 11"], a:3,
  why:"36 + 81 = 117, but 11² = 121. The other three are the standard triples."},
 {n:4, lvl:"standard", q:"Two similar triangles have sides in the ratio <span class='num'>1 : 3</span>. Their areas are in the ratio:",
  o:["1 : 3","1 : 6","1 : 9","1 : 27"], a:2,
  why:"Areas scale by the square of the length ratio: 1² : 3². Option D is the volume ratio for similar solids."},
 {n:5, lvl:"trap", q:"A median joins a corner of a triangle to the midpoint of the opposite side. The two triangles it makes have areas that are:",
  o:["always equal","equal only if the triangle is isosceles","in the ratio of the other two sides","equal only for right-angled triangles"], a:0,
  why:"Both small triangles have equal bases (half the side each) and the same height from the shared corner. So their areas are always equal — whatever the triangle looks like. The diagram never matters for this."}
];

const SHORTS = [
 {n:6, m:2, lvl:"warm-up", q:"A <span class='num'>13 m</span> ladder leans against a vertical wall with its foot <span class='num'>5 m</span> from the wall.<br><strong>(a)</strong> How high up the wall does it reach? <span class='num'>[1]</span><br><strong>(b)</strong> The foot slides out until it is 12 m from the wall. How far has the top slid down? <span class='num'>[1]</span>",
  scheme:["(a) √(169 − 25) = √144 = <strong>12 m</strong> <span class='num'>[1]</span>",
          "(b) New height √(169 − 144) = 5 m, so it slid <strong>7 m</strong> <span class='num'>[1]</span>"],
  tip:"Same triple both times, just swapped: 5-12-13 then 12-5-13. Recognising the triple means no square roots at all."},
 {n:7, m:2, lvl:"standard", q:"Find the area of the triangle with corners at <span class='num'>(0, 0)</span>, <span class='num'>(6, 2)</span> and <span class='num'>(2, 5)</span>.",
  scheme:["Enclosing rectangle 6 × 5 = 30; corner triangles 6, 6 and 5 <span class='num'>[1]</span>",
          "30 − 17 = <strong>13</strong> <span class='num'>[1]</span>"],
  tip:"Sketch it on squared paper first. The corner triangles are ½ × 6 × 2, ½ × 4 × 3 and ½ × 2 × 5 — one leg of each runs along the rectangle."},
 {n:8, m:2, lvl:"standard", q:"A right-angled triangle has legs 6 cm and 8 cm. Find the length of the altitude from the right angle to the hypotenuse.",
  scheme:["Area = ½ × 6 × 8 = 24 and hypotenuse = 10 <span class='num'>[1]</span>",
          "½ × 10 × h = 24, so <strong>h = 4.8 cm</strong> <span class='num'>[1]</span>"],
  tip:"Area two ways. The answer ab ÷ c = 48 ÷ 10 works for every right triangle."},
 {n:9, m:2, lvl:"standard", q:"In triangle ABC, a line parallel to BC meets AB at D and AC at E. AD = 4, DB = 6 and BC = 15.<br><strong>(a)</strong> Find DE. <span class='num'>[1]</span><br><strong>(b)</strong> Find the ratio area ADE : area ABC. <span class='num'>[1]</span>",
  scheme:["(a) AD/AB = 4/10, so DE = 15 × 4/10 = <strong>6</strong> <span class='num'>[1]</span>",
          "(b) (4/10)² = 16/100, so <strong>4 : 25</strong> <span class='num'>[1]</span>"],
  tip:"The ratio is AD : AB = 4 : 10, not AD : DB = 4 : 6. AB is the whole side of the big triangle — that's what corresponds to AD."},
 {n:10, m:2, lvl:"hard", q:"Prove that a median of any triangle divides it into two triangles of equal area.",
  scheme:["M is the midpoint of BC, so BM = MC <span class='num'>[1]</span>",
          "Triangles ABM and AMC have the same height from A to BC, so their areas ½ × BM × h and ½ × MC × h are <strong>equal</strong> <span class='num'>[1]</span>"],
  tip:"The key word is 'same height'. Both triangles hang from A down to the same line BC."}
];

const WORDS = [
 {n:11, m:3, lvl:"standard", q:"A room is a cuboid <span class='num'>12 m</span> long, <span class='num'>9 m</span> wide and <span class='num'>8 m</span> high.<br><br><strong>(a)</strong> Find the length of the diagonal across the floor. <span class='num'>[1]</span><br><strong>(b)</strong> Find the length of the longest straight rod that fits in the room. <span class='num'>[1]</span><br><strong>(c)</strong> How much further is it to walk along two edges of the floor than straight across it? <span class='num'>[1]</span>",
  hints:["The floor diagonal is the hypotenuse of a 12 by 9 right triangle. Spot the triple.",
         "The longest rod goes from a floor corner to the opposite ceiling corner. It's the hypotenuse of a right triangle whose legs are the floor diagonal and the height.",
         "Two edges: 12 + 9."],
  sol:["(a) 9-12-15 is 3 × (3-4-5): <strong>15 m</strong>.",
       "(b) Legs 15 and 8: 225 + 64 = 289 = 17², so <strong>17 m</strong> (8-15-17).",
       "(c) 21 − 15 = <strong>6 m</strong>.",
       "Two triples stacked: the answer to (a) became a leg in (b). IOQM 3-D questions almost always flatten into two right triangles like this."]},

 {n:12, m:3, lvl:"standard", q:"ABCD is a square of side <span class='num'>12</span>, labelled anticlockwise from A at the bottom left. E is the midpoint of BC. F lies on CD with CF = 4.<br><br><strong>(a)</strong> Find the area of triangle ABE. <span class='num'>[1]</span><br><strong>(b)</strong> Find the areas of triangles ECF and FDA. <span class='num'>[1]</span><br><strong>(c)</strong> Hence find the area of triangle AEF. <span class='num'>[1]</span>",
  hints:["Draw it big. ABE is right-angled at B with legs AB = 12 and BE = 6.",
         "ECF has legs CE = 6 and CF = 4. FDA has legs FD = 8 and DA = 12.",
         "The three corner triangles plus AEF make the whole square."],
  sol:["(a) ½ × 12 × 6 = <strong>36</strong>.",
       "(b) ECF: ½ × 6 × 4 = <strong>12</strong>. FDA: ½ × 8 × 12 = <strong>48</strong>.",
       "(c) 144 − 36 − 12 − 48 = <strong>48</strong>.",
       "Area by subtraction: the shape you want has no easy height, but everything around it does."]},

 {n:13, m:3, lvl:"standard", q:"A student <span class='num'>1.5 m</span> tall casts a shadow <span class='num'>2 m</span> long. At the same moment a tree casts a shadow <span class='num'>14 m</span> long.<br><br><strong>(a)</strong> Explain why the two triangles formed (object, shadow, sun's ray) are similar. <span class='num'>[1]</span><br><strong>(b)</strong> Find the height of the tree. <span class='num'>[1]</span><br><strong>(c)</strong> Later in the day the tree's shadow is 21 m long. How long is the student's shadow then? <span class='num'>[1]</span>",
  hints:["Both objects are vertical and both shadows are on flat ground. And the sun's rays are parallel.",
         "Height ÷ shadow is the same for both.",
         "Find the new height-to-shadow ratio from the tree first."],
  sol:["(a) Both have a right angle at the ground, and the rays are parallel so they meet the ground at the same angle. Two equal angles: similar.",
       "(b) 1.5/2 = h/14, so h = <strong>10.5 m</strong>.",
       "(c) Tree: 10.5/21 = 0.5. Student: 1.5/s = 0.5, so <strong>s = 3 m</strong>.",
       "The ratio changed between (b) and (c) because the sun moved — the triangles are similar to each other at any one moment, not across the day."]},

 {n:14, m:3, lvl:"hard", q:"Find every right-angled triangle with whole-number sides in which one of the two shorter sides is <span class='num'>12</span>.<br><br><strong>(a)</strong> With the other leg b and hypotenuse c, show that <span class='num'>(c − b)(c + b) = 144</span>. <span class='num'>[1]</span><br><strong>(b)</strong> Explain why c − b and c + b must both be even. <span class='num'>[1]</span><br><strong>(c)</strong> Find all such triangles. <span class='num'>[1]</span>",
  hints:["12² + b² = c². Move b² across and factorise.",
         "c − b and c + b add to 2c, so they have the same parity. Their product is even.",
         "List factor pairs of 144 with both factors even and the first smaller than the second."],
  sol:["(a) c² − b² = 144, and c² − b² = (c − b)(c + b).",
       "(b) Their sum 2c is even, so they're both odd or both even; their product 144 is even, so both even.",
       "(c) Pairs 2 × 72, 4 × 36, 6 × 24, 8 × 18 give (b, c) = (35, 37), (16, 20), (9, 15), (5, 13). So <strong>12-35-37, 12-16-20, 9-12-15 and 5-12-13</strong>.",
       "12 × 12 would give b = 0, which isn't a triangle. The method — difference of squares, parity, factor pairs — is the identities page solving a geometry question."]},

 {n:15, m:3, lvl:"hard", q:"Triangle ABC has area <span class='num'>60</span>. D lies on BC with BD : DC = 1 : 2. E is the midpoint of AD.<br><br><strong>(a)</strong> Find the areas of triangles ABD and ADC. <span class='num'>[1]</span><br><strong>(b)</strong> Find the areas of triangles BED and CED. <span class='num'>[1]</span><br><strong>(c)</strong> Find the area of triangle BEC. <span class='num'>[1]</span>",
  hints:["ABD and ADC share the height from A. Split 60 in the ratio 1 : 2.",
         "In triangle ABD, BE is a median (E is the midpoint of AD). What does a median do to area? Same for CE in triangle ADC.",
         "Triangle BEC is made of BED and CED."],
  sol:["(a) Ratio 1 : 2 of 60: ABD = <strong>20</strong>, ADC = <strong>40</strong>.",
       "(b) BE is a median of ABD, so BED = 10; CE is a median of ADC, so CED = 20.",
       "(c) BEC = 10 + 20 = <strong>30</strong> — exactly half of ABC.",
       "Two moves, both 'same height'. You never found a single length or height in the whole question."]}
];
'''

TOOLS_JS = r'''
/* ---------------- the sliding apex ---------------- */
let aTarget=null, curAPuzzle=null;
function drawApex(){
  const b=+document.getElementById('ab').value, h=+document.getElementById('ah').value, o=+document.getElementById('ao').value;
  ['ab','ah','ao'].forEach(id=>document.getElementById(id+'-v').textContent=document.getElementById(id).value);
  const u=Math.min(26, 230/h), ox=200, oy=270;
  const B=[ox,oy], C=[ox+b*u,oy], A=[ox+o*u, oy-h*u];
  let g='';
  g+=`<line x1="20" y1="${oy-h*u}" x2="680" y2="${oy-h*u}" stroke="var(--rt)" stroke-dasharray="6 5" stroke-width="1.5"/>`;
  g+=`<line x1="20" y1="${oy}" x2="680" y2="${oy}" stroke="var(--line)" stroke-width="1.5"/>`;
  g+=`<line x1="${A[0]}" y1="${A[1]}" x2="${A[0]}" y2="${oy}" stroke="var(--ng)" stroke-width="2" stroke-dasharray="3 4"/>`;
  g+=`<rect x="${A[0]}" y="${oy-10}" width="10" height="10" fill="none" stroke="var(--ng)" stroke-width="1.5"/>`;
  g+=`<polygon points="${A.join(',')} ${B.join(',')} ${C.join(',')}" fill="var(--pm-tint)" stroke="var(--pm)" stroke-width="2.5" stroke-linejoin="round"/>`;
  const lab=(t,p,dx,dy)=>`<text x="${p[0]+dx}" y="${p[1]+dy}" font-family="var(--display)" font-size="16" font-weight="700" fill="var(--ink)">${t}</text>`;
  g+=lab('A',A,-5,-10)+lab('B',B,-16,20)+lab('C',C,4,20);
  g+=`<text x="${A[0]+8}" y="${oy-h*u/2}" font-family="var(--mono)" font-size="12" fill="var(--ng)">h = ${h}</text>`;
  document.getElementById('aStage').innerHTML=g;
  const area=b*h/2, AB=Math.hypot(o,h), AC=Math.hypot(o-b,h);
  const fmt=v=>Number.isInteger(v)?String(v):v.toFixed(2);
  const angB = Math.round(Math.atan2(h, o)*180/Math.PI);
  document.getElementById('a-area').textContent=fmt(area);
  document.getElementById('a-sides').textContent=`${fmt(AB)}, ${fmt(AC)}`;
  document.getElementById('a-ang').textContent=angB+'°';
  document.getElementById('a-angs').textContent = o===0 ? 'right angle at B' : (o<0 ? 'obtuse at B: the height falls outside' : (o>b ? 'obtuse at C: the height falls outside' : 'height falls inside the base'));
  const pill=document.getElementById('a-pill'), note=document.getElementById('a-note');
  if(aTarget){
    const T=aTarget; pill.className='pill up'; pill.textContent='Puzzle running';
    if(T.check(b,h,o)){
      aTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('aQuiz'); box.classList.add('on');
      box.innerHTML=`<strong>Base ${b}, height ${h}, area ${fmt(area)}.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="aAgain">Another one</button></div>`;
      document.getElementById('aAgain').addEventListener('click', ()=>document.getElementById('aPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Area = ½ × base × height, and only those two numbers matter.';
    }else note.textContent=`Area is ${fmt(area)} right now.`;
  }else{
    pill.className='pill go'; pill.textContent='Sliding';
    note.textContent='The height is measured straight down to the base line — even when A is outside the base.';
  }
}
const A_PUZZLES=[
 {txt:'a triangle with base 8, area 24 and a right angle at B', check:(b,h,o)=>b===8&&h===6&&o===0, more:'½ × 8 × h = 24 gives h = 6; a right angle at B puts A directly above B.'},
 {txt:'a triangle with base 12 and area 30', check:(b,h,o)=>b===12&&h===5, more:'Any slide works — the area only cares that h = 5.'},
 {txt:'a triangle whose base equals its height, with area 18', check:(b,h,o)=>b===h&&b*h===36, more:'½b² = 18, so b = h = 6.'},
 {txt:'an isosceles triangle (AB = AC) with area 20', check:(b,h,o)=>b*h===40&&2*o===b, more:'A must sit above the middle of BC, and base × height = 40: base 4, 8 or 10 all fit on the sliders.'},
 {txt:'a right-angled triangle at B with legs 6 and 8', check:(b,h,o)=>o===0&&((b===6&&h===8)||(b===8&&h===6)), more:'The hypotenuse AC is 10 — the 3-4-5 triple doubled.'},
 {txt:'a triangle with area 15 that is obtuse at B', check:(b,h,o)=>b*h===30&&o<0, more:'Base × height = 30, and A slid back past B. The height now lands outside the triangle.'}
];
['ab','ah','ao'].forEach(id=>document.getElementById(id).addEventListener('input', drawApex));
document.getElementById('aPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*A_PUZZLES.length);
  if(curAPuzzle===i) i=(i+1)%A_PUZZLES.length;
  curAPuzzle=i; aTarget=A_PUZZLES[i];
  document.getElementById('ah').value=1;   /* start from an unsolved state */
  const box=document.getElementById('aQuiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> Make ${aTarget.txt}. Decide base, height and where A goes before you touch the sliders.`;
  drawApex();
});

/* ---------------- the square builder ---------------- */
let pyTarget=null, curPyPuzzle=null;
function drawPyth(){
  const a=+document.getElementById('pa').value, b=+document.getElementById('pb').value;
  document.getElementById('pa-v').textContent=a; document.getElementById('pb-v').textContent=b;
  const c2=a*a+b*b, c=Math.sqrt(c2), whole=Number.isInteger(c);
  // right angle at P; leg a vertical up, leg b horizontal right. Squares outward.
  const sc=Math.min(168/(a+b), 140/b, 280/a);
  const Px=300, Py=178, Q=[Px+b*sc,Py], R=[Px,Py-a*sc], P=[Px,Py];
  let g='';
  g+=`<polygon points="${P.join(',')} ${Q.join(',')} ${Q[0]},${Py+b*sc} ${Px},${Py+b*sc}" fill="var(--pm-tint)" stroke="var(--pm)" stroke-width="2"/>`;
  g+=`<polygon points="${P.join(',')} ${R.join(',')} ${Px-a*sc},${R[1]} ${Px-a*sc},${Py}" fill="var(--rt-tint)" stroke="var(--rt)" stroke-width="2"/>`;
  const dx=Q[0]-R[0], dy=Q[1]-R[1];
  const R2=[R[0]-dy, R[1]+dx], Q2=[Q[0]-dy, Q[1]+dx];
  // outward normal for hypotenuse points up-right: (-dy?) choose the one away from P
  const n1=[dy,-dx];
  const out=[R[0]+n1[0],R[1]+n1[1]], out2=[Q[0]+n1[0],Q[1]+n1[1]];
  g+=`<polygon points="${R.join(',')} ${Q.join(',')} ${out2.map(v=>v.toFixed(1)).join(',')} ${out.map(v=>v.toFixed(1)).join(',')}" fill="${whole?'var(--ok-tint)':'var(--ng-tint)'}" stroke="${whole?'var(--ok)':'var(--ng)'}" stroke-width="2"/>`;
  g+=`<polygon points="${P.join(',')} ${Q.join(',')} ${R.join(',')}" fill="var(--card)" stroke="var(--ink)" stroke-width="2.5"/>`;
  g+=`<rect x="${Px}" y="${Py-10}" width="10" height="10" fill="none" stroke="var(--ink)" stroke-width="1.5"/>`;
  const t=(x,y,s,col)=>`<text x="${x.toFixed(1)}" y="${y.toFixed(1)}" text-anchor="middle" font-family="var(--mono)" font-size="13" font-weight="700" fill="${col}">${s}</text>`;
  g+=t(Px+b*sc/2, Py+b*sc/2+5, `${b}² = ${b*b}`, 'var(--pm)');
  g+=t(Px-a*sc/2, Py-a*sc/2+5, `${a}² = ${a*a}`, 'var(--rt)');
  g+=t((R[0]+out2[0])/2, (R[1]+out2[1])/2+5, `c² = ${c2}`, whole?'var(--ok)':'var(--ng)');
  document.getElementById('pStage2').innerHTML=g;
  document.getElementById('p-ab').textContent=c2;
  document.getElementById('p-abs').textContent=`${a*a} + ${b*b}`;
  document.getElementById('p-c').textContent= whole ? c : `√${c2} ≈ ${c.toFixed(2)}`;
  document.getElementById('p-cs').textContent= whole ? `${c} × ${c} = ${c2}` : 'not a whole number';
  document.getElementById('p-t').textContent= whole ? `yes: ${Math.min(a,b)}-${Math.max(a,b)}-${c}` : 'no';
  const g0=(x,y)=>y?g0(y,x%y):x, k=whole?g0(g0(a,b),c):1;
  document.getElementById('p-ts').textContent= whole ? (k>1 ? `${k} × (${Math.min(a,b)/k}-${Math.max(a,b)/k}-${c/k})` : 'a primitive triple') : '';
  const pill=document.getElementById('p2-pill'), note=document.getElementById('p2-note');
  if(pyTarget){
    const T=pyTarget; pill.className='pill up'; pill.textContent='Puzzle running';
    if(T.check(a,b,c)){
      pyTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('p2Quiz'); box.classList.add('on');
      box.innerHTML=`<strong>${Math.min(a,b)}-${Math.max(a,b)}-${c}.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="p2Again">Another one</button></div>`;
      document.getElementById('p2Again').addEventListener('click', ()=>document.getElementById('p2Puzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Know the five primitive triples and their multiples, and these take seconds.';
    }else note.textContent = whole ? `${Math.min(a,b)}-${Math.max(a,b)}-${c} is a triple, but not the one asked for.` : `c² = ${c2} isn't a perfect square.`;
  }else{
    pill.className='pill up'; pill.textContent='Building';
    note.textContent='Try 3 and 4, then 6 and 8, then 9 and 12. Multiples of a triple are triples.';
  }
}
const isInt=v=>Number.isInteger(v);
const PY_PUZZLES=[
 {txt:'a whole-number right triangle with hypotenuse 13', check:(a,b,c)=>c===13, more:'169 − 25 = 144. The only one.'},
 {txt:'a whole-number right triangle with hypotenuse 17', check:(a,b,c)=>c===17, more:'289 − 64 = 225.'},
 {txt:'a whole-number right triangle with hypotenuse 25 (both legs at most 20)', check:(a,b,c)=>c===25, more:'15-20-25 is 5 × (3-4-5). 7-24-25 also has hypotenuse 25, but 24 won\'t fit on the slider.'},
 {txt:'a whole-number right triangle with a leg of 9', check:(a,b,c)=>isInt(c)&&(a===9||b===9), more:'9-12-15 is 3 × (3-4-5). (9-40-41 exists too, off the slider.)'},
 {txt:'a primitive triple (no common factor) with hypotenuse over 15', check:(a,b,c)=>{const g=(x,y)=>y?g(y,x%y):x; return isInt(c)&&c>15&&g(a,b)===1;}, more:'8-15-17 is the only primitive one that fits on the sliders. 15-20-25 and 12-16-20 are both multiples of 3-4-5.'},
 {txt:'a whole-number right triangle with hypotenuse 10', check:(a,b,c)=>c===10, more:'6-8-10, double 3-4-5.'}
];
['pa','pb'].forEach(id=>document.getElementById(id).addEventListener('input', drawPyth));
document.getElementById('p2Puzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*PY_PUZZLES.length);
  if(curPyPuzzle===i) i=(i+1)%PY_PUZZLES.length;
  curPyPuzzle=i; pyTarget=PY_PUZZLES[i];
  document.getElementById('pa').value=1; document.getElementById('pb').value=1;   /* start from an unsolved state */
  const box=document.getElementById('p2Quiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> Build ${pyTarget.txt}. Find it on paper first, then set the legs.`;
  drawPyth();
});
'''

BOOT = ['drawApex()', 'drawPyth()']
