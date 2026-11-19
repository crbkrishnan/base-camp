# -*- coding: utf-8 -*-
ID = 'ioqm-identities'
SHORT_TITLE = 'Shapes Behind the Algebra'
SUB = 'IOQM · Algebra I: identities, difference of squares, factoring tricks'
BLURB = ("Every identity Olympiad algebra leans on is a picture of areas. Pull a square apart into its pieces, cut a corner off "
         "and rearrange it into a rectangle, then use the same idea to solve equations that only have whole-number answers.")
META_TOOL = 'area square'
COLOURS = ('#3D5A1E', '#EAF1E1', '#A0362B', '#F9E9E6', '#245E8C', '#E4EEF7')
EYEBROW = 'IOQM Olympiad Prep · Algebra I'
H1 = 'Shapes <i>Behind</i><br>the <em>Algebra</em>'
LEDE = ("(a + b)² is a square you can draw. a² − b² is a square with a corner missing, and it rearranges into a rectangle. "
        "Olympiad algebra is mostly these pictures used cleverly — to do arithmetic in your head, to get a² + b² without knowing a or b, "
        "and to solve equations by factorising them.")
TARGET = ("You've been landing around <span class=\"num\">10 out of 15</span> at school. This page is out of <span class=\"num\">30</span>; "
          "the targets are <span class=\"num\">21</span> on the first pass and <span class=\"num\">26</span> on the second. "
          "No calculator. You've done expanding brackets on the school page — this is what Olympiad questions do with it.")
VIDEO_MIN = '~40 min total'
LESSON_MIN = '~40 min total'
NAV = [('square', 'Area square'), ('videos', '6 videos'), ('lessons', '6 lessons'), ('sfft', 'Border trick'),
       ('quick', 'Quick checks'), ('short', 'Short answers'), ('word', 'Word problems'), ('traps', 'Exam traps')]

EXTRA_CSS = r'''
.modebar{display:flex;gap:8px;padding:0 16px 12px;flex-wrap:wrap}
'''

TOOL1_HTML = r'''
<section id="square">
  <div class="panel">
    <div class="panel-top">
      <h2>The area square</h2>
      <p>Two lengths, a and b. In <strong>square</strong> mode, a square of side a + b splits into four pieces — and two of them are the same. In <strong>difference</strong> mode, a b × b corner is cut off an a × a square and the leftover L-shape is rearranged into a rectangle. Same area, two shapes, one identity.</p>
    </div>
    <div class="modebar">
      <button class="btn small on" type="button" id="modeSq">Square: (a + b)²</button>
      <button class="btn ghost small" type="button" id="modeDiff">Difference: a² − b²</button>
    </div>
    <svg class="stage" viewBox="0 0 700 320" role="img" aria-label="Areas of squares and rectangles built from lengths a and b"><g id="sqStage"></g></svg>
    <div class="ctrl">
      <label for="sa">a</label><input id="sa" type="range" min="1" max="12" value="7" aria-label="Length a"><span class="num" id="sa-v">7</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="sb">b</label><input id="sb" type="range" min="1" max="12" value="3" aria-label="Length b"><span class="num" id="sb-v">3</span>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab" id="q-l1">Whole square</div><div class="val" id="q-v1">—</div><div class="sub" id="q-s1"></div></div>
      <div class="cell d"><div class="lab" id="q-l2">Pieces</div><div class="val" id="q-v2">—</div><div class="sub" id="q-s2"></div></div>
      <div class="cell p"><div class="lab" id="q-l3">Check</div><div class="val" id="q-v3">—</div><div class="sub" id="q-s3"></div></div>
      <div class="phasebar">
        <span class="pill go" id="q-pill">Square</span>
        <span id="q-note">The two ab rectangles are the 2ab people forget.</span>
        <span class="push"><button class="btn ghost" type="button" id="sqPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="sqQuiz"></div>
    </div>
  </div>
</section>
'''

TOOL2_HTML = r'''
<section id="sfft">
  <div class="panel">
    <div class="panel-top">
      <h2>The border trick</h2>
      <p>An x × y rectangle of tiles, plus one extra row (x tiles) and one extra column (y tiles). That's xy + x + y tiles — and it is <em>one tile short</em> of a full (x + 1) × (y + 1) rectangle. Add the missing corner tile and the messy expression becomes a product you can factorise.</p>
    </div>
    <svg class="stage" viewBox="0 0 700 330" role="img" aria-label="A rectangle of tiles with an extra row, an extra column and a corner tile"><g id="bStage"></g></svg>
    <div class="ctrl">
      <label for="bx">x</label><input id="bx" type="range" min="1" max="15" value="4" aria-label="x"><span class="num" id="bx-v">4</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="by">y</label><input id="by" type="range" min="1" max="15" value="6" aria-label="y"><span class="num" id="by-v">6</span>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">xy + x + y</div><div class="val" id="b-v1">—</div><div class="sub">the messy expression</div></div>
      <div class="cell p"><div class="lab">+ the corner</div><div class="val" id="b-v2">—</div><div class="sub">= (x + 1)(y + 1)</div></div>
      <div class="cell d"><div class="lab">Factor pairs of that</div><div class="val" id="b-v3" style="font-size:15px">—</div><div class="sub">each pair is a solution</div></div>
      <div class="phasebar">
        <span class="pill up" id="b-pill">Tiling</span>
        <span id="b-note">The orange tile is the "+1" you add to both sides.</span>
        <span class="push"><button class="btn ghost" type="button" id="bPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="bQuiz"></div>
    </div>
  </div>
</section>
'''

TRAPS = [
 ("Writing (a + b)² = a² + b²",
  "The square of a sum has <strong>four</strong> pieces, and two of them are ab. (3 + 4)² = 49, but 3² + 4² = 25 — the missing 24 is exactly 2 × 3 × 4. Test any identity you're unsure of with two small numbers before you trust it."),
 ("Trying to factorise a² + b²",
  "a² − b² = (a − b)(a + b). There is no matching factorisation of a² + b² with whole numbers. If an equation needs a² + b², reach for (a + b)² − 2ab instead."),
 ("Missing factor pairs",
  "When you solve (x − y)(x + y) = 45, list <strong>every</strong> pair: 1 × 45, 3 × 15, 5 × 9. Students stop after the first one that works. A question that asks for 'all solutions' is usually marked on whether you found the last one."),
 ("Squaring x + 1/x and forgetting the middle",
  "(x + 1/x)² = x² + <strong>2</strong> + 1/x², because the middle term is 2 × x × (1/x) = 2. So if x + 1/x = 4, then x² + 1/x² = 16 − 2 = 14, not 16."),
 ("Adding the wrong number in the border trick",
  "To turn xy + 2x + 3y into a product you need (x + 3)(y + 2) = xy + 2x + 3y + <strong>6</strong>. The number you add is the product of the two shifts — and you add it to <strong>both</strong> sides. Adding 6 on the left only changes the equation.")
]

DATA_JS = r'''
/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"Visual Proof of (a + b)² = a² + 2ab + b²", ch:"YouTube lesson (IGCSE Math)", url:"https://www.youtube.com/watch?v=m6ZDlUOcbho",
  why:"The square split into four pieces — the same picture as the area square on this page, explained slowly. If 2ab has ever surprised you, watch this first.",
  task:"Draw the picture for (5 + 2)² on squared paper and label all four pieces with their areas. They must add to 49."},

 {t:"Difference of Squares — Explained Visually", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=mcNdTPqvXps",
  why:"Two proofs-without-words of a² − b² = (a + b)(a − b). The 'cut and slide' version is what the difference mode in the area square animates.",
  task:"Use the identity to work out 23 × 17 in your head (it's 20² − 3²). Then do 46 × 54 and 99 × 101. Answers: 391, 2484, 9999."},

 {t:"An Algebraic Areas Identity (visual proof)", ch:"Mathematical Visual Proofs", url:"https://www.youtube.com/watch?v=P9RojjVRumA",
  why:"(a + b)² + (a − b)² = 2(a² + b²), shown with areas. A short one — its job is to make you expect that every identity has a picture.",
  task:"Check the identity with a = 5, b = 2: 49 + 9 = 2 × 29. Then use it to find a² + b² if a + b = 9 and a − b = 3, without finding a or b."},

 {t:"Simon's Favorite Factoring Trick", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=0nN3H7w2LnI",
  why:"The trick behind lesson 5 and the border tool, from the people who named it. This is one of the most-used moves in IOQM algebra and number theory.",
  task:"Solve xy + x + y = 34 in positive whole numbers, his way. You should reach (x + 1)(y + 1) = 35 and the pair x = 4, y = 6 (or the other way round)."},

 {t:"Simon's Favorite Factoring Trick, as on AMC and MATHCOUNTS", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=aryJ3IJqr94",
  why:"Competition problems where the trick is hidden — the coefficients aren't 1, or you have to rearrange first. Watch how the shifts are chosen.",
  task:"Rewrite xy + 2x + 3y = 29 as a product equal to a number. (You should get (x + 3)(y + 2) = 35.) Then find both positive solutions."},

 {t:"Completing the Square via the Difference of Squares", ch:"Mathematical Visual Proofs", url:"https://www.youtube.com/watch?v=72Ssn7ZVjtU",
  why:"Ties the two identities on this page together and previews completing the square, which you'll meet again in quadratics.",
  task:"Write x² + 6x as (x + 3)² − 9. Then x² + 10x, and x² − 8x. Say in one line where the 9, 25 and 16 come from."}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"(a + b)² is a picture", len:"6 min",
  body:`<p>A square of side a + b splits into a square a × a, a square b × b, and <strong>two</strong> rectangles a × b:</p>
        <div class="eqline">(a + b)² = a² + 2ab + b² &nbsp;&nbsp;&nbsp; (a − b)² = a² − 2ab + b²</div>
        <p>Use it as an arithmetic machine. Split an awkward number into a round one plus a small one:</p>
        <div class="eqline">103² = (100 + 3)² = 10000 + 600 + 9 = 10609<br>&nbsp;97² = (100 − 3)² = 10000 − 600 + 9 = 9409</div>
        <p>Squares ending in 5 are a special case: 65² = 60 × 70 + 25 = 4225. (That's (a + 5)² = a(a + 10) + 25.)</p>
        <p>The most common error in all of algebra is writing (a + b)² = a² + b². The area square shows why it can't be: two whole rectangles would be missing.</p>`,
  demo:`<strong>Do this:</strong> work out 21², 49², 85² and 1001² in your head, using the identity. Write only the answers. (441, 2401, 7225, 1002001.)`,
  cliff:`What if you take the small square away instead of adding it on?`},

 {t:"a² − b²: the most useful factorisation there is", len:"7 min",
  body:`<p>Cut a b × b corner out of an a × a square. The L-shape that's left can be cut once and slid into a rectangle (a + b) long and (a − b) wide:</p>
        <div class="eqline">a² − b² = (a + b)(a − b)</div>
        <p><strong>Arithmetic:</strong> 47 × 53 = (50 − 3)(50 + 3) = 2500 − 9 = 2491. And backwards: 101² − 99² = (200)(2) = 400 — no squaring needed.</p>
        <p><strong>Spotting it:</strong> anything of the form (something)² − (something)²: 9x² − 25 = (3x)² − 5² = (3x − 5)(3x + 5). Also x⁴ − 1 = (x² − 1)(x² + 1) = (x − 1)(x + 1)(x² + 1).</p>
        <p>a² + b² does <strong>not</strong> factorise like this. That asymmetry matters in lesson 3.</p>`,
  demo:`<strong>Do this:</strong> compute 1003 × 997 and 68² − 32² in your head. (999991 and 3600.) Then factorise 4x² − 49.`,
  cliff:`Suppose you know a + b and ab, but not a or b. Can you still find a² + b²?`},

 {t:"Using identities backwards", len:"7 min",
  body:`<p>Olympiad questions love giving you combinations and asking for other combinations. Rearrange the identity:</p>
        <div class="eqline">a² + b² = (a + b)² − 2ab &nbsp;&nbsp;&nbsp; (a − b)² = (a + b)² − 4ab</div>
        <p><strong>Example.</strong> a + b = 7 and ab = 10. Then a² + b² = 49 − 20 = <strong>29</strong>, and (a − b)² = 49 − 40 = 9, so a − b = ±3. You never needed a = 5, b = 2 — and in harder questions a and b aren't whole numbers, so you couldn't find them anyway.</p>
        <p><strong>The x + 1/x family.</strong> If x + 1/x = 3, square both sides: x² + 2 + 1/x² = 9, so x² + 1/x² = <strong>7</strong>. Square again: x⁴ + 2 + 1/x⁴ = 49, so x⁴ + 1/x⁴ = 47.</p>`,
  demo:`<strong>Do this:</strong> a − b = 3 and ab = 10. Find a² + b². (Use (a − b)² = a² − 2ab + b²: 9 + 20 = 29.)`,
  cliff:`Factorising isn't just for simplifying. It solves equations where the answers have to be whole numbers.`},

 {t:"Factorise, then list factor pairs", len:"7 min",
  body:`<p>Find all positive whole numbers x and y with x² − y² = 45.</p>
        <p>Factorise: (x − y)(x + y) = 45. Now x − y and x + y are whole numbers that multiply to 45, and x + y is the bigger one. List the pairs:</p>
        <table class="data"><tr><th>x − y</th><th>x + y</th><th>x</th><th>y</th></tr>
        <tr><td>1</td><td>45</td><td>23</td><td>22</td></tr>
        <tr><td>3</td><td>15</td><td>9</td><td>6</td></tr>
        <tr><td>5</td><td>9</td><td>7</td><td>2</td></tr></table>
        <p>Three solutions, and no others — because there are no other factor pairs.</p>
        <p><strong>Parity check.</strong> x − y and x + y differ by 2y, so they are both odd or both even. With 60 on the right, a pair like 4 × 15 (one even, one odd) is impossible, and that kills half the list at once.</p>`,
  demo:`<strong>Do this:</strong> find every pair with x² − y² = 21. (1 × 21 → 11, 10; 3 × 7 → 5, 2.) Check both.`,
  cliff:`x² − y² factorised itself. What about xy + 2x + 3y = 29, which doesn't?`},

 {t:"Simon's Favourite Factoring Trick", len:"7 min",
  body:`<p>xy + 2x + 3y looks like part of a product. Try (x + 3)(y + 2):</p>
        <div class="eqline">(x + 3)(y + 2) = xy + 2x + 3y + 6</div>
        <p>It's the expression <em>plus 6</em>. So add 6 to both sides of the equation:</p>
        <div class="eqline">xy + 2x + 3y = 29 &nbsp;⟹&nbsp; (x + 3)(y + 2) = 35</div>
        <p>Now it's lesson 4. 35 = 5 × 7 = 7 × 5 = 1 × 35 = 35 × 1. With positive x and y, x + 3 ≥ 4 and y + 2 ≥ 3, which leaves:</p>
        <ul><li>x + 3 = 5, y + 2 = 7 → <strong>x = 2, y = 5</strong></li>
            <li>x + 3 = 7, y + 2 = 5 → <strong>x = 4, y = 3</strong></li></ul>
        <p>The shifts are the coefficients <em>swapped</em>: the 2 on x goes with y, the 3 on y goes with x. The number you add is their product. The border tool below is the simplest case, xy + x + y.</p>`,
  demo:`<strong>Do this:</strong> solve xy + x + y = 23 in positive whole numbers. (Add 1: (x + 1)(y + 1) = 24. You should find three pairs.)`,
  cliff:`Squares have a sum-and-product trick. Do cubes?`},

 {t:"Cubes, and getting out of the tangle", len:"6 min",
  body:`<p>The cube versions:</p>
        <div class="eqline">a³ + b³ = (a + b)(a² − ab + b²) &nbsp;&nbsp;&nbsp; a³ − b³ = (a − b)(a² + ab + b²)</div>
        <p>and the one you'll use most:</p>
        <div class="eqline">a³ + b³ = (a + b)³ − 3ab(a + b)</div>
        <p><strong>Example.</strong> a + b = 5 and ab = 6. Then a³ + b³ = 125 − 3 × 6 × 5 = <strong>35</strong>. (Check: a = 2, b = 3 gives 8 + 27.)</p>
        <p><strong>The general move</strong> behind this whole page: when a question gives you a + b and ab, everything symmetric in a and b — a² + b², a³ + b³, 1/a + 1/b = (a + b)/ab — can be built out of those two numbers. Don't try to find a and b first.</p>`,
  demo:`<strong>Do this:</strong> a + b = 4 and ab = 1. Find 1/a + 1/b, a² + b² and a³ + b³. (4, 14 and 52.)`,
  cliff:`That's the lessons. Q14 alternates the signs of 2026 squares and asks for the total; Q15 asks for every solution of m² − n² = 60. Go and lose to them, then take them apart.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"<span class='num'>(x + 5)²</span> is equal to:",
  o:["x² + 10x + 25","x² + 25","x² + 5x + 25","x² + 10x + 10"], a:0,
  why:"x² + 2 × 5 × x + 5². Option B is the classic error — it leaves out the two 5x rectangles. Option C has only one of them."},
 {n:2, lvl:"standard", q:"<span class='num'>51² − 49²</span> equals:",
  o:["2","100","200","400"], a:2,
  why:"(51 + 49)(51 − 49) = 100 × 2 = 200. Option A is (51 − 49)² — subtracting before squaring isn't the same thing."},
 {n:3, lvl:"standard", q:"If <span class='num'>a + b = 7</span> and <span class='num'>ab = 10</span>, then <span class='num'>a² + b²</span> is:",
  o:["29","39","49","69"], a:0,
  why:"(a + b)² − 2ab = 49 − 20 = 29. Option C forgets to take off the 2ab; option D adds it instead."},
 {n:4, lvl:"standard", q:"Which of these equals <span class='num'>98 × 102</span>?",
  o:["9996","10004","9994","10000"], a:0,
  why:"(100 − 2)(100 + 2) = 100² − 2² = 10000 − 4. Option B adds the 4; the product of two numbers either side of 100 is always a little <em>less</em> than 100²."},
 {n:5, lvl:"trap", q:"If <span class='num'>x² = 9</span> and <span class='num'>y² = 4</span>, which of these <strong>must</strong> be true?",
  o:["x − y = 1","x² − y² = 5","x + y = 5","xy = 6"], a:1,
  why:"x could be 3 or −3, and y could be 2 or −2, so A, C and D can all fail (try x = −3, y = 2). Only x² − y² = 9 − 4 is fixed. 'Must' questions are won by looking for a counterexample to each option."}
];

const SHORTS = [
 {n:6, m:2, lvl:"warm-up", q:"<strong>(a)</strong> Expand <span class='num'>(2x − 3)²</span>. <span class='num'>[1]</span><br><strong>(b)</strong> Factorise <span class='num'>9x² − 25</span>. <span class='num'>[1]</span>",
  scheme:["(a) <strong>4x² − 12x + 9</strong> <span class='num'>[1]</span>",
          "(b) <strong>(3x − 5)(3x + 5)</strong> <span class='num'>[1]</span>"],
  tip:"In (a), the middle term is 2 × 2x × (−3) = −12x. Writing −6x means you used one rectangle, not two."},
 {n:7, m:2, lvl:"standard", q:"Without a calculator, work out <span class='num'>997²</span>. Show the identity you used.",
  scheme:["(1000 − 3)² = 1000² − 2 × 3 × 1000 + 3² <span class='num'>[1]</span>",
          "= 1000000 − 6000 + 9 = <strong>994009</strong> <span class='num'>[1]</span>"],
  tip:"Check the size: 997² must be a little under 1000² = 1000000. If your answer ends in anything but 9, the last term is wrong — 7² ends in 9."},
 {n:8, m:2, lvl:"standard", q:"Given that <span class='num'>x + 1/x = 4</span>, find the value of <span class='num'>x² + 1/x²</span>.",
  scheme:["(x + 1/x)² = x² + 2 + 1/x² = 16 <span class='num'>[1]</span>",
          "x² + 1/x² = <strong>14</strong> <span class='num'>[1]</span>"],
  tip:"The 2 is x × (1/x) twice. If you answered 16, you squared the two terms separately — trap 4."},
 {n:9, m:2, lvl:"standard", q:"Find all pairs of positive whole numbers x and y with <span class='num'>x² − y² = 15</span>.",
  scheme:["(x − y)(x + y) = 15, with pairs 1 × 15 and 3 × 5 <span class='num'>[1]</span>",
          "<strong>x = 8, y = 7</strong> and <strong>x = 4, y = 1</strong> <span class='num'>[1]</span>"],
  tip:"Second mark needs both pairs. Check: 64 − 49 = 15 and 16 − 1 = 15."},
 {n:10, m:2, lvl:"hard", q:"Show that <span class='num'>n(n + 1)(n + 2)(n + 3) + 1</span> is a perfect square for every whole number n. (Try n = 1: 1 × 2 × 3 × 4 + 1 = 25.)",
  scheme:["Pair the outer and inner brackets: n(n + 3) = n² + 3n and (n + 1)(n + 2) = n² + 3n + 2 <span class='num'>[1]</span>",
          "Let t = n² + 3n + 1. The expression is (t − 1)(t + 1) + 1 = t² − 1 + 1 = <strong>(n² + 3n + 1)²</strong> <span class='num'>[1]</span>"],
  tip:"The pairing is the whole trick — both products then start n² + 3n. Expanding all four brackets also works, but it's a page of algebra and easy to get wrong."}
];

const WORDS = [
 {n:11, m:3, lvl:"standard", q:"A square garden has side s metres. A path 2 m wide runs all the way round the outside of it.<br><br><strong>(a)</strong> Show that the area of the path is <span class='num'>8s + 16</span> m². <span class='num'>[1]</span><br><strong>(b)</strong> The path has area 96 m². Find s. <span class='num'>[1]</span><br><strong>(c)</strong> For a garden of side 46 m, find the area of the path using the difference of two squares. <span class='num'>[1]</span>",
  hints:["The outer edge of the path is a square of side s + 4 — the path adds 2 m on each side.",
         "Path = big square − garden. That's a difference of two squares.",
         "For (c), you can use 8s + 16, but the question wants (s + 4)² − s² written as a product."],
  sol:["(a) (s + 4)² − s² = (s + 4 + s)(s + 4 − s) = (2s + 4) × 4 = 8s + 16.",
       "(b) 8s + 16 = 96, so 8s = 80 and <strong>s = 10</strong>.",
       "(c) 50² − 46² = (50 + 46)(50 − 46) = 96 × 4 = <strong>384 m²</strong>.",
       "Check (c) against (a): 8 × 46 + 16 = 384. ✓ The common mistake in (a) is s + 2 for the outer side — the path is on both sides."]},

 {n:12, m:3, lvl:"standard", q:"Two numbers a and b, with a > b, satisfy <span class='num'>a + b = 10</span> and <span class='num'>ab = 21</span>. Without finding a and b, work out:<br><strong>(a)</strong> <span class='num'>a² + b²</span> <span class='num'>[1]</span> &nbsp; <strong>(b)</strong> <span class='num'>a − b</span> <span class='num'>[1]</span> &nbsp; <strong>(c)</strong> <span class='num'>a³ + b³</span> <span class='num'>[1]</span>",
  hints:["(a + b)² = a² + 2ab + b². Rearrange.",
         "(a − b)² = (a + b)² − 4ab. Then take the square root — and use a > b to choose the sign.",
         "a³ + b³ = (a + b)³ − 3ab(a + b)."],
  sol:["(a) 100 − 2 × 21 = <strong>58</strong>.",
       "(b) (a − b)² = 100 − 84 = 16, so a − b = ±4; since a > b, <strong>a − b = 4</strong>.",
       "(c) 1000 − 3 × 21 × 10 = 1000 − 630 = <strong>370</strong>.",
       "Now check: a = 7, b = 3 gives 49 + 9 = 58, 7 − 3 = 4, 343 + 27 = 370. In the exam you won't always be able to find a and b, which is why the method matters."]},

 {n:13, m:3, lvl:"standard", q:"A rectangle has whole-number sides x and y metres, with x ≤ y. The number of square metres in its area plus the number of metres in its perimeter is <span class='num'>76</span>.<br><br><strong>(a)</strong> Show that <span class='num'>(x + 2)(y + 2) = 80</span>. <span class='num'>[1]</span><br><strong>(b)</strong> Find every possible rectangle. <span class='num'>[1]</span><br><strong>(c)</strong> Which of them has the largest area? <span class='num'>[1]</span>",
  hints:["Area + perimeter = xy + 2x + 2y. Which product does that look like part of?",
         "(x + 2)(y + 2) = xy + 2x + 2y + 4. So add 4 to both sides.",
         "List factor pairs of 80 where both factors are at least 3 (since x, y ≥ 1), and the first is no bigger than the second."],
  sol:["(a) xy + 2x + 2y = 76; adding 4 gives xy + 2x + 2y + 4 = 80, which is (x + 2)(y + 2).",
       "(b) Pairs of 80 with both factors ≥ 3: 4 × 20, 5 × 16, 8 × 10. So <strong>2 × 18, 3 × 14, 6 × 8</strong>.",
       "(c) Areas 36, 42 and 48: the <strong>6 × 8</strong> rectangle.",
       "Check 6 × 8: area 48, perimeter 28, total 76 ✓. The pair 2 × 40 gives x = 0, which isn't a rectangle — the 'at least 3' condition is what removes it."]},

 {n:14, m:3, lvl:"hard", q:"Find the value of<br><span class='num'>2026² − 2025² + 2024² − 2023² + … + 4² − 3² + 2² − 1²</span>.<br><br><strong>(a)</strong> Show that (n + 1)² − n² = (n + 1) + n for any n. <span class='num'>[1]</span><br><strong>(b)</strong> Hence explain why the whole expression equals 1 + 2 + 3 + … + 2026. <span class='num'>[1]</span><br><strong>(c)</strong> Find its value. <span class='num'>[1]</span>",
  hints:["Difference of two squares: (n + 1)² − n² = ((n + 1) + n)((n + 1) − n).",
         "Group the expression into pairs: (2026² − 2025²) + (2024² − 2023²) + … Each pair becomes a sum of two consecutive numbers.",
         "1 + 2 + … + N = N(N + 1)/2. Then 2026 × 2027 / 2 = 1013 × 2027."],
  sol:["(a) (n + 1)² − n² = ((n + 1) + n)((n + 1) − n) = (n + 1) + n, since the second bracket is 1.",
       "(b) Each pair 2026² − 2025² = 2026 + 2025, 2024² − 2023² = 2024 + 2023, …, 2² − 1² = 2 + 1. Together these use every number from 1 to 2026 exactly once.",
       "(c) 2026 × 2027 ÷ 2 = 1013 × 2027 = 2027000 + 26351 = <strong>2053351</strong>.",
       "1013 × 2027: 1000 × 2027 = 2027000, plus 13 × 2027 = 26351, total 2053351. Year-number questions like this appear in IOQM almost every year — the year is decoration."]},

 {n:15, m:3, lvl:"hard", q:"Find every pair of positive whole numbers m and n with <span class='num'>m² − n² = 60</span>.<br><br><strong>(a)</strong> Explain why m − n and m + n are either both odd or both even. <span class='num'>[1]</span><br><strong>(b)</strong> Explain why, here, they must both be even. <span class='num'>[1]</span><br><strong>(c)</strong> Find all the pairs. <span class='num'>[1]</span>",
  hints:["Add them: (m − n) + (m + n) = 2m. What does that say about their parity?",
         "Their product is 60, which is even. Could both be odd?",
         "List factor pairs of 60 with both factors even and the first smaller: 2 × 30, 6 × 10. Check for any others."],
  sol:["(a) (m − n) + (m + n) = 2m is even, so the two have the same parity.",
       "(b) If both were odd, their product would be odd — but 60 is even. So both are even.",
       "(c) Even pairs: 2 × 30 gives m = 16, n = 14; 6 × 10 gives m = 8, n = 2. Pairs like 4 × 15 and 1 × 60 mix parities. So <strong>(16, 14)</strong> and <strong>(8, 2)</strong>.",
       "Check: 256 − 196 = 60 and 64 − 4 = 60. Without the parity step you'd test six factor pairs; with it, two. That's the point of (a) and (b)."]}
];
'''

TOOLS_JS = r'''
/* ---------------- the area square ---------------- */
let sqMode='sq', sqTarget=null, curQPuzzle=null;
function rect(x,y,w,h,fill,stroke,label,lc){
  let s=`<rect x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="${w.toFixed(1)}" height="${h.toFixed(1)}" fill="${fill}" stroke="${stroke}" stroke-width="2"/>`;
  if(label && w>26 && h>18) s+=`<text x="${(x+w/2).toFixed(1)}" y="${(y+h/2+5).toFixed(1)}" text-anchor="middle" font-family="var(--mono)" font-size="${w>70&&h>40?15:11}" font-weight="700" fill="${lc}">${label}</text>`;
  return s;
}
function drawSquare(){
  const a=+document.getElementById('sa').value, b=+document.getElementById('sb').value;
  document.getElementById('sa-v').textContent=a; document.getElementById('sb-v').textContent=b;
  let g='';
  const T='var(--pm)', Tt='var(--pm-tint)', R='var(--ng)', Rt='var(--ng-tint)', B='var(--rt)', Bt='var(--rt-tint)';
  const pill=document.getElementById('q-pill'), note=document.getElementById('q-note');
  if(sqMode==='sq'){
    const u=270/(a+b), ox=350-(a+b)*u/2, oy=14;
    g+=rect(ox,oy,a*u,a*u,Tt,T,`a² = ${a*a}`,T);
    g+=rect(ox+a*u,oy,b*u,a*u,Rt,R,`ab = ${a*b}`,R);
    g+=rect(ox,oy+a*u,a*u,b*u,Rt,R,`ab = ${a*b}`,R);
    g+=rect(ox+a*u,oy+a*u,b*u,b*u,Bt,B,`b² = ${b*b}`,B);
    g+=`<text x="${ox+(a+b)*u/2}" y="${oy+(a+b)*u+22}" text-anchor="middle" font-family="var(--mono)" font-size="13" fill="var(--ink-soft)">side a + b = ${a+b}</text>`;
    document.getElementById('q-l1').textContent='Whole square';
    document.getElementById('q-v1').textContent=(a+b)*(a+b);
    document.getElementById('q-s1').textContent=`(${a} + ${b})² = ${a+b}²`;
    document.getElementById('q-l2').textContent='Four pieces';
    document.getElementById('q-v2').textContent=`${a*a} + ${2*a*b} + ${b*b}`;
    document.getElementById('q-s2').textContent='a² + 2ab + b²';
    document.getElementById('q-l3').textContent='The mistake';
    document.getElementById('q-v3').textContent=a*a+b*b;
    document.getElementById('q-s3').textContent=`a² + b² is short by 2ab = ${2*a*b}`;
  }else{
    const big=Math.max(a,b), small=Math.min(a,b);
    const u=240/a, ox=40, oy=24;
    // left: a×a with b×b corner cut (if b<a)
    if(b<a){
      g+=rect(ox,oy,(a-b)*u,a*u,Tt,T,'',T);
      g+=rect(ox+(a-b)*u,oy,b*u,(a-b)*u,Rt,R,'',R);
      g+=`<rect x="${(ox+(a-b)*u).toFixed(1)}" y="${(oy+(a-b)*u).toFixed(1)}" width="${(b*u).toFixed(1)}" height="${(b*u).toFixed(1)}" fill="none" stroke="var(--steel)" stroke-dasharray="5 4" stroke-width="2"/>`;
      g+=`<text x="${ox+(a-b+b/2)*u}" y="${oy+(a-b+b/2)*u+5}" text-anchor="middle" font-family="var(--mono)" font-size="12" fill="var(--steel-dark)">cut b²</text>`;
      g+=`<text x="${ox+a*u/2}" y="${oy+a*u+22}" text-anchor="middle" font-family="var(--mono)" font-size="13" fill="var(--ink-soft)">a² − b² = ${a*a} − ${b*b}</text>`;
      // right: rectangle (a+b) × (a−b)
      const rx=380, ry=60;
      const k=Math.min(0.62, 290/((a+b)*u)); const W=(a+b)*u*k, H=(a-b)*u*k;
      g+=rect(rx,ry,a*u*k,H,Tt,T,`${a}×${a-b}`,T);
      g+=rect(rx+a*u*k,ry,b*u*k,H,Rt,R,`${b}×${a-b}`,R);
      g+=`<text x="${rx+W/2}" y="${ry+H+22}" text-anchor="middle" font-family="var(--mono)" font-size="13" fill="var(--ink-soft)">(a + b)(a − b) = ${a+b} × ${a-b} = ${(a+b)*(a-b)}</text>`;
      g+=`<text x="${rx}" y="${ry-14}" font-family="var(--mono)" font-size="12" fill="var(--ink-soft)">turn the red strip on its side, slide it on →</text>`;
    }else{
      g+=`<text x="350" y="160" text-anchor="middle" font-family="var(--mono)" font-size="15" fill="var(--ink-soft)">Make a bigger than b to cut a corner off.</text>`;
    }
    document.getElementById('q-l1').textContent='a² − b²';
    document.getElementById('q-v1').textContent=a*a-b*b;
    document.getElementById('q-s1').textContent=`${a*a} − ${b*b}`;
    document.getElementById('q-l2').textContent='Rectangle';
    document.getElementById('q-v2').textContent=`${a+b} × ${a-b}`;
    document.getElementById('q-s2').textContent='(a + b)(a − b)';
    document.getElementById('q-l3').textContent='Same?';
    document.getElementById('q-v3').textContent=(a*a-b*b)===(a+b)*(a-b)?'always':'—';
    document.getElementById('q-s3').textContent='one shape, rearranged';
  }
  document.getElementById('sqStage').innerHTML=g;

  if(sqTarget){
    const P=sqTarget;
    pill.className='pill up'; pill.textContent='Puzzle running';
    let ok=false;
    if(P.mode==='diff'){ ok = sqMode==='diff' && a>b && a*a-b*b===P.t; note.textContent = sqMode!=='diff' ? 'Switch to difference mode.' : `a² − b² is ${a*a-b*b} right now. You need ${P.t}.`; }
    else { ok = sqMode==='sq' && a+b===P.s && a*b===P.p; note.textContent = sqMode!=='sq' ? 'Switch to square mode.' : `Right now a + b = ${a+b} and ab = ${a*b}.`; }
    if(ok){
      sqTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('sqQuiz'); box.classList.add('on');
      box.innerHTML=`<strong>Done.</strong> ${P.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="sqAgain">Another one</button></div>`;
      document.getElementById('sqAgain').addEventListener('click', ()=>document.getElementById('sqPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Factor pairs did the work — the sliders only confirmed it.';
    }
  }else{
    pill.className='pill go'; pill.textContent = sqMode==='sq' ? 'Square' : 'Difference';
    note.textContent = sqMode==='sq' ? 'The two ab rectangles are the 2ab people forget.' : 'Cut the corner, slide the strip: a² − b² becomes a rectangle (a + b) by (a − b).';
  }
}
function setMode(m){
  sqMode=m;
  document.getElementById('modeSq').className = 'btn small ' + (m==='sq'?'on':'ghost');
  document.getElementById('modeDiff').className = 'btn small ' + (m==='diff'?'on':'ghost');
  drawSquare();
}
document.getElementById('modeSq').addEventListener('click', ()=>setMode('sq'));
document.getElementById('modeDiff').addEventListener('click', ()=>setMode('diff'));
['sa','sb'].forEach(id=>document.getElementById(id).addEventListener('input', drawSquare));
const SQ_PUZZLES=[
 {mode:'diff', t:33, more:'(a + b)(a − b) = 33 = 11 × 3, so a = 7 and b = 4.'},
 {mode:'diff', t:45, more:'45 = 9 × 5 gives 7 and 2; 45 = 15 × 3 gives 9 and 6. Both fit on the sliders.'},
 {mode:'diff', t:24, more:'24 = 6 × 4 gives 5 and 1; 12 × 2 gives 7 and 5. 8 × 3 is no good — one odd, one even.'},
 {mode:'diff', t:40, more:'40 = 10 × 4 gives 7 and 3; 20 × 2 gives 11 and 9.'},
 {mode:'sq', s:12, p:32, more:'a + b = 12 and ab = 32 means 8 and 4 — and a² + b² = 144 − 64 = 80.'},
 {mode:'sq', s:13, p:42, more:'6 and 7. The square is 169 = 36 + 84 + 49.'}
];
document.getElementById('sqPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*SQ_PUZZLES.length);
  if(curQPuzzle===i) i=(i+1)%SQ_PUZZLES.length;
  curQPuzzle=i; sqTarget=SQ_PUZZLES[i];
  document.getElementById('sa').value=1; document.getElementById('sb').value=1;   /* start from an unsolved state */
  const P=sqTarget, box=document.getElementById('sqQuiz'); box.classList.add('on');
  box.innerHTML = P.mode==='diff'
    ? `<strong>Puzzle.</strong> In difference mode, set a and b so that <span class="num">a² − b² = ${P.t}</span>. Factorise ${P.t} into (a + b)(a − b) on paper first.`
    : `<strong>Puzzle.</strong> In square mode, set a and b so that <span class="num">a + b = ${P.s}</span> and <span class="num">ab = ${P.p}</span>.`;
  drawSquare();
});

/* ---------------- the border trick ---------------- */
let bTarget=null, curBPuzzle=null;
function pairsOf(N){ const r=[]; for(let d=1; d*d<=N; d++) if(N%d===0) r.push(d+'×'+(N/d)); return r; }
function drawBorder(){
  const x=+document.getElementById('bx').value, y=+document.getElementById('by').value;
  document.getElementById('bx-v').textContent=x; document.getElementById('by-v').textContent=y;
  const cols=x+1, rows=y+1, u=Math.min(560/cols, 290/rows, 34), ox=(700-cols*u)/2, oy=12;
  let g='';
  for(let j=0;j<rows;j++) for(let i=0;i<cols;i++){
    let f='var(--pm-tint)', s='var(--pm)';
    if(i===x && j===y){ f='var(--ng)'; s='var(--ng)'; }
    else if(i===x || j===y){ f='var(--rt-tint)'; s='var(--rt)'; }
    g+=`<rect x="${(ox+i*u+1).toFixed(1)}" y="${(oy+j*u+1).toFixed(1)}" width="${(u-2).toFixed(1)}" height="${(u-2).toFixed(1)}" rx="3" fill="${f}" stroke="${s}" stroke-width="1"/>`;
  }
  g+=`<text x="350" y="${oy+rows*u+20}" text-anchor="middle" font-family="var(--mono)" font-size="13" fill="var(--ink-soft)">inner block: xy = ${x*y} &nbsp; edge strips: x + y = ${x+y} &nbsp; red corner: the missing 1</text>`;
  document.getElementById('bStage').innerHTML=g;
  const v1=x*y+x+y, v2=(x+1)*(y+1);
  document.getElementById('b-v1').textContent=v1;
  document.getElementById('b-v2').textContent=v2;
  document.getElementById('b-v3').textContent=pairsOf(v2).join(', ');
  const pill=document.getElementById('b-pill'), note=document.getElementById('b-note');
  if(bTarget){
    pill.className='pill up'; pill.textContent='Puzzle running';
    if(v1===bTarget.t){
      const T=bTarget; bTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('bQuiz'); box.classList.add('on');
      box.innerHTML=`<strong>x = ${x}, y = ${y} works.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="bAgain">Another one</button></div>`;
      document.getElementById('bAgain').addEventListener('click', ()=>document.getElementById('bPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Add the corner, factorise, subtract 1 from each factor.';
    }else note.textContent=`xy + x + y is ${v1}. You need ${bTarget.t}.`;
  }else{
    pill.className='pill up'; pill.textContent='Tiling';
    note.textContent='The red tile is the "+1" you add to both sides.';
  }
}
const B_PUZZLES=[
 {t:34, more:'34 + 1 = 35 = 5 × 7, so x + 1 and y + 1 are 5 and 7.'},
 {t:23, more:'24 = 2 × 12 = 3 × 8 = 4 × 6, so (1, 11), (2, 7) and (3, 5) all work.'},
 {t:54, more:'55 = 5 × 11, so 4 and 10. 1 × 55 would need x = 0.'},
 {t:44, more:'45 = 3 × 15 = 5 × 9: (2, 14) or (4, 8).'},
 {t:62, more:'63 = 7 × 9 gives 6 and 8. 3 × 21 would need y = 20 — off the slider.'},
 {t:29, more:'30 = 2 × 15 = 3 × 10 = 5 × 6: (1, 14), (2, 9) or (4, 5).'}
];
['bx','by'].forEach(id=>document.getElementById(id).addEventListener('input', drawBorder));
document.getElementById('bPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*B_PUZZLES.length);
  if(curBPuzzle===i) i=(i+1)%B_PUZZLES.length;
  curBPuzzle=i; bTarget=B_PUZZLES[i];
  document.getElementById('bx').value=1; document.getElementById('by').value=1;   /* start from an unsolved state */
  const box=document.getElementById('bQuiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> Find whole numbers x and y (1 to 15) with <span class="num">xy + x + y = ${bTarget.t}</span>. Add the corner tile on paper, factorise, then set the sliders.`;
  drawBorder();
});
'''

BOOT = ['drawSquare()', 'drawBorder()']
