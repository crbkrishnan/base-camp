# -*- coding: utf-8 -*-
ID = 'ioqm-sequences'
SHORT_TITLE = 'Pair Them Up'
SUB = 'IOQM · Algebra II: sums, sequences, systems, AM–GM'
BLURB = ("Gauss's pairing trick, telescoping sums that collapse to two terms, and the one inequality every Olympiad uses. "
         "Build a staircase of numbers and fit its upside-down copy on top, then hunt for the biggest rectangle a fence can hold.")
META_TOOL = 'Gauss staircase'
COLOURS = ('#7A3E8E', '#F2E9F5', '#1E6B5C', '#E3F2EE', '#A35A14', '#F8EDE0')
EYEBROW = 'IOQM Olympiad Prep · Algebra II'
H1 = 'Pair <i>Them</i><br><em>Up</em>'
LEDE = ("Adding a hundred numbers one by one is how you lose twenty minutes and a mark. Adding them in pairs is how a nine-year-old Gauss did it in "
        "his head. This page is about seeing structure in long sums and in equations — so that the work collapses before you start it.")
TARGET = ("You've been landing around <span class=\"num\">10 out of 15</span> at school. This page is out of <span class=\"num\">30</span>; "
          "the targets are <span class=\"num\">21</span> on the first pass and <span class=\"num\">26</span> on the second. No calculator. "
          "If a question has a 100-term sum in it, there is a shortcut — the question is which one.")
VIDEO_MIN = '~45 min total'
LESSON_MIN = '~40 min total'
NAV = [('stairs', 'Gauss staircase'), ('videos', '6 videos'), ('lessons', '6 lessons'), ('fence', 'Fence machine'),
       ('quick', 'Quick checks'), ('short', 'Short answers'), ('word', 'Word problems'), ('traps', 'Exam traps')]

EXTRA_CSS = r'''
'''

TOOL1_HTML = r'''
<section id="stairs">
  <div class="panel">
    <div class="panel-top">
      <h2>The Gauss staircase</h2>
      <p>An arithmetic sequence drawn as a staircase of bars. Its upside-down copy (faint) fits on top exactly, and together they make a rectangle n bars wide and (first + last) tall. Half the rectangle is your sum — that's the whole formula.</p>
    </div>
    <svg class="stage" viewBox="0 0 700 300" role="img" aria-label="A staircase of bars and its flipped copy forming a rectangle"><g id="stStage"></g></svg>
    <div class="ctrl">
      <label for="sta">First term</label><input id="sta" type="range" min="1" max="30" value="1" aria-label="First term"><span class="num" id="sta-v">1</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="std">Step</label><input id="std" type="range" min="1" max="5" value="1" aria-label="Common difference"><span class="num" id="std-v">1</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="stn">Terms</label><input id="stn" type="range" min="1" max="30" value="10" aria-label="Number of terms"><span class="num" id="stn-v">10</span>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">Sequence</div><div class="val" id="st-seq" style="font-size:15px">—</div><div class="sub" id="st-last"></div></div>
      <div class="cell p"><div class="lab">Rectangle</div><div class="val" id="st-rect">—</div><div class="sub">n × (first + last)</div></div>
      <div class="cell d"><div class="lab">Sum = half of it</div><div class="val" id="st-sum">—</div><div class="sub" id="st-sums"></div></div>
      <div class="phasebar">
        <span class="pill go" id="st-pill">Pairing</span>
        <span id="st-note">Every column of the rectangle is first + last. That's the pairing.</span>
        <span class="push"><button class="btn ghost" type="button" id="stPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="stQuiz"></div>
    </div>
  </div>
</section>
'''

TOOL2_HTML = r'''
<section id="fence">
  <div class="panel">
    <div class="panel-top">
      <h2>The fence machine</h2>
      <p>Two sides of a rectangle, x and y, with a fixed total x + y. Slide x and watch the area x × y rise and fall. The top of the curve is always at x = y — which is the arithmetic mean–geometric mean inequality, drawn.</p>
    </div>
    <svg class="stage" viewBox="0 0 700 280" role="img" aria-label="A rectangle with fixed perimeter and a graph of its area"><g id="fStage"></g></svg>
    <div class="ctrl">
      <label for="fs">x + y</label><input id="fs" type="range" min="4" max="30" value="20" aria-label="Fixed total x plus y"><span class="num" id="fs-v">20</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="fx">x</label><input id="fx" type="range" min="0" max="20" value="5" aria-label="Side x"><span class="num" id="fx-v">5</span>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">Sides</div><div class="val" id="f-sides">—</div><div class="sub">x and y = total − x</div></div>
      <div class="cell p"><div class="lab">Area xy</div><div class="val" id="f-area">—</div><div class="sub" id="f-areas"></div></div>
      <div class="cell d"><div class="lab">AM vs GM</div><div class="val" id="f-amgm">—</div><div class="sub">(x + y)/2 ≥ √(xy)</div></div>
      <div class="phasebar">
        <span class="pill up" id="f-pill">Fencing</span>
        <span id="f-note">The mean (x + y)/2 never moves. The area is biggest when x and y both equal it.</span>
        <span class="push"><button class="btn ghost" type="button" id="fPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="fQuiz"></div>
    </div>
  </div>
</section>
'''

TRAPS = [
 ("Counting the terms wrongly",
  "From 5 to 101 in steps of 3 is not 96 ÷ 3 = 32 terms. It's <strong>(last − first) ÷ step + 1 = 33</strong>. The +1 is the fence-post: 10 metres of fence with a post every metre needs 11 posts. Check with something tiny — 5, 8, 11 is (11 − 5) ÷ 3 + 1 = 3 terms."),
 ("Using n = 100 for the even numbers up to 100",
  "2 + 4 + … + 100 has <strong>50</strong> terms, not 100. Sum = 50 × (2 + 100) ÷ 2 = 2550. A quicker way: it's 2 × (1 + 2 + … + 50) = 2 × 1275."),
 ("Losing track of what survives a telescope",
  "In (1 − ½) + (½ − ⅓) + … + (1/99 − 1/100), everything cancels except the <strong>very first</strong> and the <strong>very last</strong>. Write out the first three brackets and the last one before you cancel. Most errors are an off-by-one at the end: 1 − 1/100, not 1 − 1/99."),
 ("Using AM–GM on numbers that might be negative",
  "x + y ≥ 2√(xy) is only true for <strong>positive</strong> x and y. x + 1/x ≥ 2 fails at x = −1, where it's −2. And the inequality is only useful if equality can actually happen: say where it does (x = y) and check that value is allowed."),
 ("Dividing by something that could be zero",
  "x² = 5x, divide by x, get x = 5 — and you've lost <strong>x = 0</strong>. Instead write x² − 5x = 0, so x(x − 5) = 0, so x = 0 or 5. Never cancel an unknown; factorise it out.")
]

DATA_JS = r'''
/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"Sum the Numbers from 1 to 100", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=j-EB1O-vRS4",
  why:"The famous Gauss trick, told by someone who teaches it to competition students every year. It's the idea the staircase tool draws.",
  task:"Add 1 to 200 his way, then 1 to 999. Answers: 20100 and 499500. Write the general formula in words before you check lesson 1."},

 {t:"Arithmetic Series Introduction", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=HbNfN569TOg",
  why:"From consecutive numbers to any evenly spaced list. The 'average of first and last, times the number of terms' version is the one to memorise.",
  task:"Find 7 + 11 + 15 + … + 403. First count the terms (you need 100), then use the formula. Answer: 20500."},

 {t:"Arithmetic Series Problem Solving", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=LIqJB6Aoc2Q",
  why:"Harder problems where the series is hidden inside a word problem — the IOQM style.",
  task:"Pause before each solution and write your own first line. Count how many times your first line matched his."},

 {t:"Systems of Equations and Word Problems (Part 2)", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=t14-vD0zcdM",
  why:"Turning words into two equations, then solving them without blundering. Lesson 4 adds the Olympiad shortcut: add all the equations together first.",
  task:"Solve a + b = 13, b + c = 15, c + a = 16 by adding all three first. You should get a + b + c = 22, then a = 7, b = 6, c = 9."},

 {t:"The AM–GM Inequality", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=br05-gIAk2s",
  why:"The inequality, its one-line proof from (√x − √y)² ≥ 0, and the equality case. Q4, Q10 and Q14 all use it.",
  task:"Prove that x + 1/x ≥ 2 for every positive x, in one line, using AM–GM. Then say for which x it's equal."},

 {t:"Visual Proof of the AM–GM Inequality", ch:"Mathematical Visual Proofs", url:"https://www.youtube.com/watch?v=62G9fak1vyk",
  why:"A one-minute proof with areas. Watching the picture once makes the inequality something you can see, not just quote.",
  task:"After watching, explain in two sentences why a square has the biggest area of all rectangles with the same perimeter."}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"Pair the first with the last", len:"6 min",
  body:`<p>1 + 2 + … + 100. Write it forwards and backwards:</p>
        <div class="eqline">&nbsp;&nbsp;1 + &nbsp;&nbsp;2 + &nbsp;&nbsp;3 + … + 100<br>100 + &nbsp;99 + &nbsp;98 + … + &nbsp;&nbsp;1</div>
        <p>Each column adds to 101, and there are 100 columns. That's twice the sum, so the sum is 100 × 101 ÷ 2 = <strong>5050</strong>.</p>
        <div class="eqline">1 + 2 + … + n = n(n + 1) ÷ 2</div>
        <p>The same argument works for <em>any</em> evenly spaced list:</p>
        <div class="eqline">sum = number of terms × (first + last) ÷ 2</div>
        <p>That's "number of terms × the average term", because the average of an evenly spaced list is the average of its ends. The staircase tool above draws exactly this: the sequence and its flipped copy make a rectangle.</p>`,
  demo:`<strong>Do this:</strong> find 1 + 2 + … + 50 and 51 + 52 + … + 100 without writing more than two lines each. (1275 and 3775.) Add them: you should get 5050.`,
  cliff:`The formula needs the number of terms. For 1 to 100 that's obvious. For 7, 11, 15, …, 403 it isn't.`},

 {t:"Counting terms: the fence-post rule", len:"6 min",
  body:`<p>An arithmetic sequence starts at a and goes up by d each time:</p>
        <div class="eqline">a, a + d, a + 2d, … &nbsp;&nbsp;&nbsp; n-th term = a + (n − 1)d</div>
        <p>The (n − 1) is there because the first term has had no steps yet. Turned round, it counts the terms:</p>
        <div class="eqline">number of terms = (last − first) ÷ d + 1</div>
        <p><strong>Example.</strong> 7, 11, 15, …, 403: (403 − 7) ÷ 4 + 1 = 99 + 1 = 100 terms. Sum = 100 × (7 + 403) ÷ 2 = <strong>20500</strong>.</p>
        <p><strong>Is a number in the sequence?</strong> 4, 11, 18, … has n-th term 7n − 3. Is 2026 a term? 7n = 2029, and 2029 isn't a multiple of 7, so no. Equivalently: every term leaves remainder 4 on division by 7, and 2026 leaves 3.</p>`,
  demo:`<strong>Do this:</strong> how many multiples of 3 are there between 100 and 200? (First 102, last 198: (198 − 102) ÷ 3 + 1 = 33.) Then find their sum.`,
  cliff:`Some sums aren't evenly spaced at all — 1/(1×2) + 1/(2×3) + … — and yet they collapse even faster.`},

 {t:"Telescoping: let the middle cancel", len:"7 min",
  body:`<p>Notice that 1/(1 × 2) = 1 − ½, and 1/(2 × 3) = ½ − ⅓, and in general:</p>
        <div class="eqline">1 / (n(n + 1)) = 1/n − 1/(n + 1)</div>
        <p>So the sum</p>
        <div class="eqline">1/(1×2) + 1/(2×3) + … + 1/(99×100)<br>= (1 − ½) + (½ − ⅓) + (⅓ − ¼) + … + (1/99 − 1/100)</div>
        <p>has every middle term appear once with + and once with −. Like a telescope folding up, only the ends are left: 1 − 1/100 = <strong>99/100</strong>.</p>
        <p>The skill is spotting a term that is a <em>difference</em> of two things where the second one of each term is the first one of the next. Other examples: (n + 1)² − n² (difference of squares page), and √(n + 1) − √n.</p>`,
  demo:`<strong>Do this:</strong> find 1/(1×2) + 1/(2×3) + … + 1/(49×50). Write the first three brackets and the last one, then cancel. (49/50.)`,
  cliff:`Sums are one kind of structure. Equations have structure too — and sometimes you can solve three at once by adding them.`},

 {t:"Systems: add, subtract, look for symmetry", len:"6 min",
  body:`<p>Two unknowns, two equations: x + y = 12 and x − y = 4. Add them: 2x = 16, so x = 8 and y = 4. You don't always need x and y separately — xy = 32 straight away.</p>
        <p><strong>Symmetric systems.</strong> a + b = 13, b + c = 15, c + a = 16. Every letter appears twice, so <strong>add all three</strong>:</p>
        <div class="eqline">2(a + b + c) = 44 &nbsp;→&nbsp; a + b + c = 22</div>
        <p>Then subtract each original: c = 22 − 13 = 9, a = 22 − 15 = 7, b = 22 − 16 = 6.</p>
        <p><strong>Whole-number equations.</strong> Pens at ₹12 and notebooks at ₹35, total ₹200. 12p + 35n = 200 has one equation and two unknowns — but p and n must be positive whole numbers, so check the few possibilities. Use parity first: 12p and 200 are even, so 35n is even, so n is even.</p>`,
  demo:`<strong>Do this:</strong> x + y + z = 11, x − y = 1, y − z = 2. Find x, y, z. (Write x and z in terms of y; you should get y = 4.)`,
  cliff:`With x + y fixed, how big can xy get?`},

 {t:"AM–GM: the inequality every Olympiad uses", len:"7 min",
  body:`<p>A square of a real number is never negative. So for positive x and y:</p>
        <div class="eqline">(√x − √y)² ≥ 0 &nbsp;⟹&nbsp; x − 2√(xy) + y ≥ 0 &nbsp;⟹&nbsp; (x + y)/2 ≥ √(xy)</div>
        <p>The arithmetic mean is at least the geometric mean, and they're equal <strong>only when x = y</strong>. Two uses:</p>
        <ul><li><strong>Fixed sum → biggest product.</strong> If x + y = 20, then xy ≤ 10² = 100, reached at x = y = 10. A square beats every other rectangle with the same perimeter.</li>
            <li><strong>Fixed product → smallest sum.</strong> If xy = 36, then x + y ≥ 2 × 6 = 12.</li></ul>
        <p>The favourite special case: x + 1/x ≥ 2, because the product x × 1/x is 1. Similarly x + 9/x ≥ 2√9 = 6, equal at x = 3.</p>`,
  demo:`<strong>Do this:</strong> on the fence machine, set x + y = 20 and slide x from 0 to 20. Write down the areas at x = 8, 9, 10, 11, 12. Notice they are symmetric about 10 and drop by 1, then 4.`,
  cliff:`AM–GM came from "a square is never negative". That one fact can find minimums all on its own.`},

 {t:"Squares are never negative", len:"6 min",
  body:`<p>To find the smallest value of x² − 6x + 13, complete the square:</p>
        <div class="eqline">x² − 6x + 13 = (x − 3)² + 4</div>
        <p>(x − 3)² is at least 0, so the whole thing is at least <strong>4</strong>, and it equals 4 exactly when x = 3. No graph needed.</p>
        <p>The same idea proves inequalities: x + 9/x − 6 = (x² − 6x + 9)/x = (x − 3)²/x, which is ≥ 0 for positive x. That's Q10, in one line.</p>
        <p>And it solves equations: if (a − 1)² + (b + 2)² = 0, both squares must be 0, so a = 1 and b = −2. A sum of squares is zero only when every square is.</p>`,
  demo:`<strong>Do this:</strong> find the smallest value of x² + 10x + 30, and the x that gives it. (−5 and 5.)`,
  cliff:`That's the lessons. Q14 fences a pen against a wall, and Q15 is a telescoping sum hiding inside Gauss's formula. Go and lose to them, then take them apart.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"<span class='num'>1 + 2 + 3 + … + 50</span> equals:",
  o:["1250","1275","2500","2550"], a:1,
  why:"50 × 51 ÷ 2 = 1275. Option D forgets to halve; option A uses 50 × 50 ÷ 2."},
 {n:2, lvl:"standard", q:"How many terms are in the sequence <span class='num'>5, 8, 11, …, 101</span>?",
  o:["32","33","34","96"], a:1,
  why:"(101 − 5) ÷ 3 + 1 = 32 + 1 = 33. Option A is the fence-post error — it counts the gaps, not the posts."},
 {n:3, lvl:"standard", q:"If <span class='num'>x + y = 12</span> and <span class='num'>x − y = 4</span>, then <span class='num'>xy</span> is:",
  o:["16","32","48","128"], a:1,
  why:"Adding gives x = 8, so y = 4, and xy = 32. Or, without x and y: 4xy = (x + y)² − (x − y)² = 144 − 16 = 128, so xy = 32. Option D is that 128 before dividing by 4."},
 {n:4, lvl:"standard", q:"What is the largest possible value of <span class='num'>x(10 − x)</span>?",
  o:["10","20","25","100"], a:2,
  why:"x and 10 − x add to 10, so their product is biggest when both are 5: 25. Option D is (x + (10 − x))², the square of the sum."},
 {n:5, lvl:"trap", q:"<span class='num'>2 + 4 + 6 + … + 100</span> equals:",
  o:["2500","2550","5050","5100"], a:1,
  why:"There are 50 terms, not 100. 50 × (2 + 100) ÷ 2 = 2550. Option A is the sum of the odd numbers 1 + 3 + … + 99, which is 50²."}
];

const SHORTS = [
 {n:6, m:2, lvl:"warm-up", q:"The sequence <span class='num'>4, 11, 18, 25, …</span> goes up by 7 each time.<br><strong>(a)</strong> Write an expression for the n-th term. <span class='num'>[1]</span><br><strong>(b)</strong> Is 2026 a term of the sequence? Give a reason. <span class='num'>[1]</span>",
  scheme:["(a) <strong>7n − 3</strong> <span class='num'>[1]</span>",
          "(b) <strong>No</strong>: 7n − 3 = 2026 gives 7n = 2029, which is not a multiple of 7 <span class='num'>[1]</span>"],
  tip:"For (b), 'no' alone gets nothing — the mark is for the reason. 2029 = 7 × 289 + 6."},
 {n:7, m:2, lvl:"standard", q:"Find the sum of all the multiples of 3 between 100 and 200.",
  scheme:["First 102, last 198, number of terms (198 − 102) ÷ 3 + 1 = 33 <span class='num'>[1]</span>",
          "Sum = 33 × (102 + 198) ÷ 2 = <strong>4950</strong> <span class='num'>[1]</span>"],
  tip:"Check: the average term is (102 + 198) ÷ 2 = 150, and 33 × 150 = 4950."},
 {n:8, m:2, lvl:"standard", q:"Find the exact value of <span class='num'>1/(1×2) + 1/(2×3) + 1/(3×4) + … + 1/(49×50)</span>.",
  scheme:["Each term 1/(n(n + 1)) = 1/n − 1/(n + 1) <span class='num'>[1]</span>",
          "The sum telescopes to 1 − 1/50 = <strong>49/50</strong> <span class='num'>[1]</span>"],
  tip:"The last term is 1/(49 × 50) = 1/49 − 1/50, so 1/50 survives — not 1/49."},
 {n:9, m:2, lvl:"standard", q:"Three numbers satisfy <span class='num'>a + b = 13</span>, <span class='num'>b + c = 15</span> and <span class='num'>c + a = 16</span>. Find a, b and c.",
  scheme:["Adding all three: 2(a + b + c) = 44, so a + b + c = 22 <span class='num'>[1]</span>",
          "<strong>a = 7, b = 6, c = 9</strong> <span class='num'>[1]</span>"],
  tip:"c = 22 − (a + b) = 22 − 13. Each letter is the total minus the equation it's missing from."},
 {n:10, m:2, lvl:"hard", q:"Prove that <span class='num'>x + 9/x ≥ 6</span> for every positive number x, and state when equality holds.",
  scheme:["x + 9/x − 6 = (x² − 6x + 9)/x = <strong>(x − 3)²/x</strong> <span class='num'>[1]</span>",
          "Square ≥ 0 and x > 0, so it's ≥ 0; equality exactly when <strong>x = 3</strong> <span class='num'>[1]</span>"],
  tip:"AM–GM also works: x + 9/x ≥ 2√(x × 9/x) = 2√9 = 6. Either proof gets both marks — but only if you say where equality happens."}
];

const WORDS = [
 {n:11, m:3, lvl:"standard", q:"A theatre has 25 rows. Row 1 has 20 seats, and each row has 2 more seats than the row in front of it.<br><br><strong>(a)</strong> How many seats are in row 25? <span class='num'>[1]</span><br><strong>(b)</strong> How many seats are there altogether? <span class='num'>[1]</span><br><strong>(c)</strong> Which is the first row with more than 50 seats? <span class='num'>[1]</span>",
  hints:["Row n has 20 + 2(n − 1) seats. Row 1 has had no increases yet.",
         "Sum = number of rows × (first row + last row) ÷ 2.",
         "Solve 20 + 2(n − 1) > 50, and remember n has to be a whole number."],
  sol:["(a) 20 + 2 × 24 = <strong>68</strong>.",
       "(b) 25 × (20 + 68) ÷ 2 = 25 × 44 = <strong>1100</strong>.",
       "(c) 20 + 2(n − 1) > 50 gives n − 1 > 15, so n > 16: <strong>row 17</strong> (52 seats).",
       "Row 16 has exactly 50, which is not 'more than 50'. Strict inequalities are where (c) marks go."]},

 {n:12, m:3, lvl:"standard", q:"<strong>(a)</strong> Show that the sum of four consecutive whole numbers starting at a is <span class='num'>4a + 6</span>. <span class='num'>[1]</span><br><strong>(b)</strong> Write 2026 as the sum of four consecutive whole numbers. <span class='num'>[1]</span><br><strong>(c)</strong> Explain why 2026 cannot be written as the sum of three consecutive whole numbers. <span class='num'>[1]</span>",
  hints:["a + (a + 1) + (a + 2) + (a + 3).",
         "Solve 4a + 6 = 2026.",
         "Write three consecutive numbers as b − 1, b, b + 1. What's their sum always a multiple of?"],
  sol:["(a) a + (a + 1) + (a + 2) + (a + 3) = 4a + 6.",
       "(b) 4a = 2020, a = 505: <strong>505 + 506 + 507 + 508</strong>.",
       "(c) (b − 1) + b + (b + 1) = 3b, a multiple of 3. 2026 has digit sum 10, so it isn't a multiple of 3 — impossible.",
       "Writing the middle number as b makes the sum 3b instantly. Choosing the variable well is half of algebra."]},

 {n:13, m:3, lvl:"standard", q:"Pens cost ₹12 and notebooks cost ₹35. Riya buys at least one of each and spends exactly ₹200.<br><br><strong>(a)</strong> Write an equation for p pens and n notebooks. <span class='num'>[1]</span><br><strong>(b)</strong> Explain why n must be even. <span class='num'>[1]</span><br><strong>(c)</strong> How many of each did she buy? <span class='num'>[1]</span>",
  hints:["Cost of pens plus cost of notebooks equals 200.",
         "12p is even and 200 is even. So what about 35n?",
         "n is even and 35n ≤ 200 − 12, so n is 2 or 4. Test both."],
  sol:["(a) <strong>12p + 35n = 200</strong>.",
       "(b) 35n = 200 − 12p, which is even minus even, so even. 35 is odd, so n must be even.",
       "(c) n = 2: 12p = 130, not a multiple of 12. n = 4: 12p = 60, p = 5. So <strong>5 pens and 4 notebooks</strong>.",
       "Check: 60 + 140 = 200 ✓. The parity step halved the cases; on a harder version it can cut them to one."]},

 {n:14, m:3, lvl:"hard", q:"A farmer has <span class='num'>60 m</span> of fencing to make a rectangular pen against a long straight wall. The wall is one side, so only three sides need fencing. The two sides that meet the wall are each x m long.<br><br><strong>(a)</strong> Show that the area of the pen is <span class='num'>x(60 − 2x)</span> m². <span class='num'>[1]</span><br><strong>(b)</strong> Find the largest possible area. <span class='num'>[1]</span><br><strong>(c)</strong> Give the dimensions of the pen with that area, and explain why it is not a square. <span class='num'>[1]</span>",
  hints:["The side opposite the wall uses what's left of the 60 m after the two x sides.",
         "AM–GM works best when the two things add to a constant. x + (60 − 2x) doesn't — but 2x + (60 − 2x) does.",
         "2x × (60 − 2x) is biggest when 2x = 60 − 2x. The area is half of that product."],
  sol:["(a) The far side is 60 − 2x, so the area is x(60 − 2x).",
       "(b) Area = ½ × 2x × (60 − 2x). The two factors 2x and 60 − 2x add to 60, so their product is at most 30 × 30 = 900, giving area ≤ <strong>450 m²</strong>.",
       "(c) Equality when 2x = 30, so x = 15: the pen is <strong>15 m by 30 m</strong>. It's not a square because the wall is free fencing — the side opposite it uses up only one length of fence, not two.",
       "The trick in (b) is rewriting x(60 − 2x) so that the two factors have a fixed sum. If you used x and 60 − 2x directly, AM–GM points at x = 20, which is wrong — check: 20 × 20 = 400 < 450."]},

 {n:15, m:3, lvl:"hard", q:"Find the exact value of<br><span class='num'>1/(1 + 2) + 1/(1 + 2 + 3) + 1/(1 + 2 + 3 + 4) + … + 1/(1 + 2 + … + 100)</span>.<br><br><strong>(a)</strong> Show that 1/(1 + 2 + … + n) = 2/(n(n + 1)). <span class='num'>[1]</span><br><strong>(b)</strong> Show that 2/(n(n + 1)) = 2/n − 2/(n + 1). <span class='num'>[1]</span><br><strong>(c)</strong> Find the sum. <span class='num'>[1]</span>",
  hints:["Use Gauss: 1 + 2 + … + n = n(n + 1)/2. Take the reciprocal.",
         "Put 2/n − 2/(n + 1) over a common denominator.",
         "The sum runs from n = 2 to n = 100. Telescope: write the first two terms and the last one."],
  sol:["(a) 1 + 2 + … + n = n(n + 1)/2, so its reciprocal is 2/(n(n + 1)).",
       "(b) 2/n − 2/(n + 1) = (2(n + 1) − 2n)/(n(n + 1)) = 2/(n(n + 1)).",
       "(c) Sum from n = 2 to 100 of (2/n − 2/(n + 1)) = 2/2 − 2/101 = 1 − 2/101 = <strong>99/101</strong>.",
       "The first term is n = 2, not n = 1 — the question starts at 1 + 2. Starting at n = 1 would give 2 − 2/101 = 200/101, which counts a 1/1 that isn't there."]}
];
'''

TOOLS_JS = r'''
/* ---------------- the Gauss staircase ---------------- */
let stTarget=null, curStPuzzle=null;
function stVals(){ return {a:+document.getElementById('sta').value, d:+document.getElementById('std').value, n:+document.getElementById('stn').value}; }
function drawStairs(){
  const {a,d,n}=stVals();
  ['sta','std','stn'].forEach(id=>document.getElementById(id+'-v').textContent=document.getElementById(id).value);
  const last=a+(n-1)*d, top=a+last, sum=n*top/2;
  const W=620, H=250, ox=40, oy=20, bw=W/n, u=H/top;
  let g='';
  for(let i=0;i<n;i++){
    const v=a+i*d, x=ox+i*bw;
    g+=`<rect x="${(x+1).toFixed(1)}" y="${(oy+H-v*u).toFixed(1)}" width="${(bw-2).toFixed(1)}" height="${(v*u).toFixed(1)}" fill="var(--pm)" opacity=".85"/>`;
    const w=top-v;
    g+=`<rect x="${(x+1).toFixed(1)}" y="${oy.toFixed(1)}" width="${(bw-2).toFixed(1)}" height="${(w*u).toFixed(1)}" fill="var(--rt-tint)" stroke="var(--rt)" stroke-width="1"/>`;
    if(bw>18) g+=`<text x="${(x+bw/2).toFixed(1)}" y="${(oy+H-v*u+14).toFixed(1)}" text-anchor="middle" font-family="var(--mono)" font-size="${bw>30?11:9}" fill="#fff">${v}</text>`;
  }
  g+=`<rect x="${ox}" y="${oy}" width="${W}" height="${H}" fill="none" stroke="var(--ink)" stroke-width="1.5" stroke-dasharray="6 4"/>`;
  g+=`<text x="${ox+W/2}" y="${oy+H+20}" text-anchor="middle" font-family="var(--mono)" font-size="12.5" fill="var(--ink-soft)">${n} columns, each ${a} + ${last} = ${top} tall</text>`;
  document.getElementById('stStage').innerHTML=g;
  const seq = n<=6 ? Array.from({length:n},(_,i)=>a+i*d).join(', ') : `${a}, ${a+d}, ${a+2*d}, …, ${last}`;
  document.getElementById('st-seq').textContent=seq;
  document.getElementById('st-last').textContent=`last = ${a} + (${n} − 1) × ${d} = ${last}`;
  document.getElementById('st-rect').textContent=`${n} × ${top} = ${n*top}`;
  document.getElementById('st-sum').textContent=sum;
  document.getElementById('st-sums').textContent=`${n*top} ÷ 2`;
  const pill=document.getElementById('st-pill'), note=document.getElementById('st-note');
  if(stTarget){
    const T=stTarget; pill.className='pill up'; pill.textContent='Puzzle running';
    const fixedOk = Object.keys(T.fix).every(k=>({a,d,n})[k]===T.fix[k]);
    if(!fixedOk){ note.textContent='Set '+Object.entries(T.fix).map(([k,v])=>({a:'first term',d:'step',n:'terms'})[k]+' = '+v).join(', ')+' first.'; return; }
    if(sum!==T.sum){ note.textContent=`The sum is ${sum}. You need ${T.sum}.`; return; }
    stTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
    const box=document.getElementById('stQuiz'); box.classList.add('on');
    box.innerHTML=`<strong>Sum ${T.sum}.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
      <div class="qrow"><button class="btn ghost small" type="button" id="stAgain">Another one</button></div>`;
    document.getElementById('stAgain').addEventListener('click', ()=>document.getElementById('stPuzzle').click());
    pill.className='pill bal'; pill.textContent='Solved';
    note.textContent='n × (first + last) ÷ 2 — set it equal to the target and solve.';
  }else{
    pill.className='pill go'; pill.textContent='Pairing';
    note.textContent='Every column of the rectangle is first + last. That\'s the pairing.';
  }
}
const ST_PUZZLES=[
 {fix:{d:1}, sum:100, more:'9 + … + 16 (8 terms) and 18 + … + 22 (5 terms) both work: n(2a + n − 1) = 200 has two solutions with n ≥ 2.'},
 {fix:{a:1,d:2}, sum:144, more:'The odd numbers add to perfect squares: 1 + 3 + … + 23 = 12².'},
 {fix:{a:1,d:1}, sum:210, more:'n(n + 1)/2 = 210 gives n = 20.'},
 {fix:{d:1,n:5}, sum:45, more:'Five consecutive numbers average the middle one, so the middle is 45 ÷ 5 = 9: 7 to 11.'},
 {fix:{a:2,d:3}, sum:155, more:'n(3n + 1)/2 = 155 gives n = 10, ending at 29.'},
 {fix:{d:1,n:6}, sum:93, more:'6a + 15 = 93 gives a = 13: 13 to 18.'}
];
['sta','std','stn'].forEach(id=>document.getElementById(id).addEventListener('input', drawStairs));
document.getElementById('stPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*ST_PUZZLES.length);
  if(curStPuzzle===i) i=(i+1)%ST_PUZZLES.length;
  curStPuzzle=i; stTarget=ST_PUZZLES[i];
  document.getElementById('stn').value=1;   /* start from an unsolved state */
  const T=stTarget, fx=Object.entries(T.fix).map(([k,v])=>({a:'first term',d:'step',n:'number of terms'})[k]+' '+v).join(' and ');
  const box=document.getElementById('stQuiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> With ${fx}, make the sequence add up to exactly <span class="num" style="font-size:17px">${T.sum}</span>. Set up the equation on paper first.`;
  drawStairs();
});

/* ---------------- the fence machine ---------------- */
let fTarget=null, curFPuzzle=null;
function drawFence(){
  const fs=document.getElementById('fs'), fx=document.getElementById('fx');
  const S0=+fs.value; fx.max=S0; if(+fx.value>S0) fx.value=S0;
  const x=+fx.value, y=S0-x, A=x*y;
  document.getElementById('fs-v').textContent=S0; document.getElementById('fx-v').textContent=x;
  let g='';
  // rectangle on the left
  const u=Math.min(200/Math.max(x,y,1), 16);
  g+=`<rect x="${30}" y="${30}" width="${(x*u).toFixed(1)}" height="${(y*u).toFixed(1)}" fill="var(--pm-tint)" stroke="var(--pm)" stroke-width="2"/>`;
  g+=`<text x="${30}" y="${22}" font-family="var(--mono)" font-size="12" fill="var(--ink-soft)">${x} × ${y}</text>`;
  // graph on the right
  const gx=330, gy=20, gw=340, gh=220, Amax=S0*S0/4;
  g+=`<line x1="${gx}" y1="${gy+gh}" x2="${gx+gw}" y2="${gy+gh}" stroke="var(--line)" stroke-width="1.5"/>`;
  g+=`<line x1="${gx}" y1="${gy}" x2="${gx}" y2="${gy+gh}" stroke="var(--line)" stroke-width="1.5"/>`;
  let path='';
  for(let k=0;k<=60;k++){ const t=S0*k/60, a=t*(S0-t); path += (k?'L':'M') + (gx+gw*t/S0).toFixed(1)+' '+(gy+gh-gh*a/Amax).toFixed(1)+' '; }
  g+=`<path d="${path}" fill="none" stroke="var(--pm)" stroke-width="2.5"/>`;
  g+=`<line x1="${gx+gw/2}" y1="${gy}" x2="${gx+gw/2}" y2="${gy+gh}" stroke="var(--rt)" stroke-dasharray="4 4"/>`;
  g+=`<circle cx="${(gx+gw*x/S0).toFixed(1)}" cy="${(gy+gh-gh*A/Amax).toFixed(1)}" r="7" fill="var(--ng)"/>`;
  g+=`<text x="${gx+gw/2+6}" y="${gy+12}" font-family="var(--mono)" font-size="11.5" fill="var(--rt)">x = y = ${S0/2}</text>`;
  g+=`<text x="${gx+gw}" y="${gy+gh+18}" text-anchor="end" font-family="var(--mono)" font-size="11.5" fill="var(--ink-soft)">x →</text>`;
  g+=`<text x="${gx-6}" y="${gy+10}" text-anchor="end" font-family="var(--mono)" font-size="11.5" fill="var(--ink-soft)">area</text>`;
  document.getElementById('fStage').innerHTML=g;
  document.getElementById('f-sides').textContent=`${x} and ${y}`;
  document.getElementById('f-area').textContent=A;
  document.getElementById('f-areas').textContent=`most possible: ${(S0/2)}² = ${Amax}`;
  document.getElementById('f-amgm').textContent=`${S0/2} ≥ ${Math.sqrt(A).toFixed(2)}`;
  const pill=document.getElementById('f-pill'), note=document.getElementById('f-note');
  if(fTarget){
    const T=fTarget; pill.className='pill up'; pill.textContent='Puzzle running';
    if(S0!==T.s){ note.textContent=`Set x + y to ${T.s} first.`; return; }
    const want = T.area==='max' ? T.s*T.s/4 : T.area;
    if(A!==want){ note.textContent=`Area ${A}. You need ${T.area==='max'?'the biggest possible area':T.area}.`; return; }
    fTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
    const box=document.getElementById('fQuiz'); box.classList.add('on');
    box.innerHTML=`<strong>Area ${A}.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
      <div class="qrow"><button class="btn ghost small" type="button" id="fAgain">Another one</button></div>`;
    document.getElementById('fAgain').addEventListener('click', ()=>document.getElementById('fPuzzle').click());
    pill.className='pill bal'; pill.textContent='Solved';
    note.textContent='Fixed sum, two numbers: their product is a parabola with its top at x = y.';
  }else{
    pill.className='pill up'; pill.textContent='Fencing';
    note.textContent='The mean (x + y)/2 never moves. The area is biggest when x and y both equal it.';
  }
}
const F_PUZZLES=[
 {s:18, area:'max', more:'9 × 9 = 81 beats every other split of 18.'},
 {s:20, area:96, more:'x(20 − x) = 96 gives x = 8 or 12 — symmetric about 10.'},
 {s:14, area:40, more:'4 × 10 = 40. The two solutions always add to the total.'},
 {s:24, area:'max', more:'12 × 12 = 144.'},
 {s:30, area:200, more:'10 × 20 = 200. Factor pairs of 200 that add to 30.'},
 {s:16, area:55, more:'5 × 11 = 55.'}
];
['fs','fx'].forEach(id=>document.getElementById(id).addEventListener('input', drawFence));
document.getElementById('fPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*F_PUZZLES.length);
  if(curFPuzzle===i) i=(i+1)%F_PUZZLES.length;
  curFPuzzle=i; fTarget=F_PUZZLES[i];
  document.getElementById('fx').value=0;   /* start from an unsolved state */
  const T=fTarget, box=document.getElementById('fQuiz'); box.classList.add('on');
  box.innerHTML = T.area==='max'
    ? `<strong>Puzzle.</strong> With x + y = ${T.s}, set x to give the <strong>largest</strong> possible area. Say what it is before you slide.`
    : `<strong>Puzzle.</strong> With x + y = ${T.s}, set x so the area is exactly <span class="num" style="font-size:17px">${T.area}</span>. Find the factor pair on paper first.`;
  drawFence();
});
'''

BOOT = ['drawStairs()', 'drawFence()']
