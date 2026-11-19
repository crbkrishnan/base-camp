# -*- coding: utf-8 -*-
ID = 'ioqm-counting'
SHORT_TITLE = 'Count Without Listing'
SUB = 'IOQM · Combinatorics I: multiply, arrange, choose, complement'
BLURB = ("Counting questions are won by never writing the list. Fill a grid with path counts that add up like Pascal's triangle, "
         "block a corner and watch the numbers reroute, then join dots on a circle to see where n(n − 1) ÷ 2 comes from.")
META_TOOL = 'path grid'
COLOURS = ('#2E4C8C', '#E6ECF7', '#A2431A', '#F9EBE2', '#4E7A27', '#ECF3E4')
EYEBROW = 'IOQM Olympiad Prep · Combinatorics I'
H1 = 'Count <i>Without</i><br><em>Listing</em>'
LEDE = ("\"How many ways…\" is the question smart students lose marks on, because they start listing and miss one. "
        "The fix is four ideas — multiply, arrange, choose, and count the opposite — and the discipline to decide which one before writing anything.")
TARGET = ("You've been landing around <span class=\"num\">10 out of 15</span> at school. This page is out of <span class=\"num\">30</span>; "
          "the targets are <span class=\"num\">21</span> on the first pass and <span class=\"num\">26</span> on the second. "
          "Before every question, say out loud: does order matter, and can things repeat? Half the wrong answers come from skipping that.")
VIDEO_MIN = '~45 min total'
LESSON_MIN = '~40 min total'
NAV = [('paths', 'Path grid'), ('videos', '6 videos'), ('lessons', '6 lessons'), ('circle', 'Handshake circle'),
       ('quick', 'Quick checks'), ('short', 'Short answers'), ('word', 'Word problems'), ('traps', 'Exam traps')]

EXTRA_CSS = r'''
.modebar{display:flex;gap:8px;padding:0 16px 12px;flex-wrap:wrap}
#gStage circle.node{cursor:pointer}
'''

TOOL1_HTML = r'''
<section id="paths">
  <div class="panel">
    <div class="panel-top">
      <h2>The path grid</h2>
      <p>Walk from the bottom-left corner to the top-right, only ever moving right or up. The number at each crossing is how many ways there are to reach it — and it's always the number to its left plus the number below, because every route arrives from one of those two. <strong>Click a crossing</strong> to block it and watch every count beyond it change.</p>
    </div>
    <svg class="stage" viewBox="0 0 700 330" role="img" aria-label="A grid of streets with the number of shortest routes to each crossing"><g id="gStage"></g></svg>
    <div class="ctrl">
      <label for="gw">Blocks across</label><input id="gw" type="range" min="1" max="8" value="4" aria-label="Blocks across"><span class="num" id="gw-v">4</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="gh">Blocks up</label><input id="gh" type="range" min="1" max="6" value="3" aria-label="Blocks up"><span class="num" id="gh-v">3</span>
      <button class="btn ghost small" type="button" id="gClear">Clear blocks</button>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">Routes to the corner</div><div class="val" id="g-n">—</div><div class="sub" id="g-ns"></div></div>
      <div class="cell p"><div class="lab">As a choice</div><div class="val" id="g-c" style="font-size:16px">—</div><div class="sub">which of the moves are 'up'</div></div>
      <div class="cell d"><div class="lab">Blocked</div><div class="val" id="g-b" style="font-size:16px">none</div><div class="sub">click a crossing to toggle</div></div>
      <div class="phasebar">
        <span class="pill go" id="g-pill">Adding</span>
        <span id="g-note">Each number is the one to its left plus the one below. That's Pascal's triangle, tilted.</span>
        <span class="push"><button class="btn ghost" type="button" id="gPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="gQuiz"></div>
    </div>
  </div>
</section>
'''

TOOL2_HTML = r'''
<section id="circle">
  <div class="panel">
    <div class="panel-top">
      <h2>The handshake circle</h2>
      <p>n people stand in a circle and every pair shakes hands once. Each person shakes n − 1 hands, but that counts every handshake twice — once from each end. In <strong>triangles</strong> mode the same idea counts groups of three, which overcounts by 3 × 2 × 1 = 6.</p>
    </div>
    <div class="modebar">
      <button class="btn small on" type="button" id="cPairs">Pairs (handshakes)</button>
      <button class="btn ghost small" type="button" id="cTrips">Triangles (groups of 3)</button>
    </div>
    <svg class="stage" viewBox="0 0 700 300" role="img" aria-label="Points on a circle joined in pairs"><g id="cStage"></g></svg>
    <div class="ctrl">
      <label for="cn">People n</label><input id="cn" type="range" min="2" max="12" value="6" aria-label="Number of people"><span class="num" id="cn-v">6</span>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab" id="c-l1">Handshakes</div><div class="val" id="c-v1">—</div><div class="sub" id="c-s1"></div></div>
      <div class="cell p"><div class="lab" id="c-l2">Ordered count</div><div class="val" id="c-v2">—</div><div class="sub" id="c-s2"></div></div>
      <div class="cell d"><div class="lab">Diagonals of the n-gon</div><div class="val" id="c-v3">—</div><div class="sub">all pairs minus the n sides</div></div>
      <div class="phasebar">
        <span class="pill up" id="c-pill">Joining</span>
        <span id="c-note">Count ordered, then divide by how many orders each group has.</span>
        <span class="push"><button class="btn ghost" type="button" id="cPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="cQuiz"></div>
    </div>
  </div>
</section>
'''

TRAPS = [
 ("Not deciding whether order matters",
  "Choosing 2 reps from 8 students is <strong>28</strong>. Choosing a captain and a vice-captain from 8 is <strong>56</strong>. The difference is whether swapping the two people gives a new answer. Decide that before you write a single number."),
 ("Letting a number start with 0",
  "There are 900 three-digit numbers, not 1000: the first digit has 9 choices (1–9), the others 10. Every digit question needs the first digit handled on its own, before the rest."),
 ("Counting 'at least one' by cases, and double-counting",
  "3-digit numbers with at least one 7: counting 'a 7 first' + 'a 7 second' + 'a 7 third' counts 777 three times. Count the opposite instead: 900 − (numbers with no 7 at all) = 900 − 648 = <strong>252</strong>."),
 ("Arranging repeated letters as if they were different",
  "LEVEL has 5 letters, but the two Ls and two Es are interchangeable, so 5! = 120 counts each arrangement 2 × 2 = 4 times. The answer is <strong>30</strong>. Divide by the factorial of each repeat count."),
 ("Adding when you should multiply",
  "A starter <strong>and</strong> a main and a dessert: multiply (3 × 4 × 2 = 24). A starter <strong>or</strong> a dessert: add (3 + 2 = 5). If your answer to a 'choose one of each' question is small, you probably added.")
]

DATA_JS = r'''
/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"Counting is as Easy as 1, 2, 3", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=3u5wGmU6A1U",
  why:"Counting how many numbers are in a list like 42, 43, …, 97 — the warm-up that catches out more people than it should. The fence-post idea again.",
  task:"How many numbers from 42 to 97 inclusive? How many multiples of 7 between 100 and 300? (56 and 28.) Write the method next to each."},

 {t:"Counting Permutations", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=ejbhqUi-7tY",
  why:"Arranging things in order — the multiplication principle applied over and over. This is lesson 2.",
  task:"How many ways can 6 runners finish first, second and third? (120.) And in how many orders can all 6 finish? (720.)"},

 {t:"Counting with Combinations (Part 1)", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=T4dJ_GeKx1Y",
  why:"Choosing when order doesn't matter: count ordered, divide by the overcount. The single most important idea on this page.",
  task:"Choose 3 books from 7 to take on holiday. Count it as ordered first (210), then explain why you divide by 6. (35.)"},

 {t:"Counting Pairs", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=wSyJrywDOXM",
  why:"The handshake problem — the handshake circle below draws it. Short and exactly on point.",
  task:"In a league of 12 teams, each pair plays twice (home and away). How many matches? (132.) Why is this one not divided by 2?"},

 {t:"Complementary Counting (Part 1)", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=tb9jwxr0HyU",
  why:"Count what you don't want and subtract. The way out of every 'at least one' question.",
  task:"How many 3-digit numbers have at least one even digit? Count those with all digits odd first (5 × 5 × 5 = 125). Answer: 775."},

 {t:"Counting Paths on a Grid", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=M8BYckxI8_U",
  why:"The path grid tool, explained: add from the corner, or count as a choice of which moves are 'up'. Q9 and Q14 are this.",
  task:"Count the routes across a 4 × 3 grid both ways — by adding numbers at crossings, and as a choice of 3 'ups' out of 7 moves. Both give 35."}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"AND multiplies, OR adds", len:"6 min",
  body:`<p>A café has 3 starters, 4 mains and 2 desserts. A meal with one of each: for every starter there are 4 mains, and for each of those 2 desserts, so <strong>3 × 4 × 2 = 24</strong>. A choice that's this <em>and</em> that multiplies.</p>
        <p>If you can have a starter <em>or</em> a dessert (not both), there are 3 + 2 = 5 options. A choice that's this <em>or</em> that, with no overlap, adds.</p>
        <p><strong>Digits.</strong> A 4-digit PIN from 0–9: 10 × 10 × 10 × 10 = 10000. With no repeated digit: 10 × 9 × 8 × 7 = 5040 — each choice uses up a digit. A 3-digit <em>number</em> can't start with 0: 9 × 10 × 10 = 900.</p>
        <p><strong>Always fill the most restricted place first.</strong> Even 3-digit numbers with different digits from 1–6: the last digit has 3 choices (2, 4, 6) — do it first — then 5 for the first place, then 4.</p>`,
  demo:`<strong>Do this:</strong> how many 3-digit numbers have all digits odd? (5 × 5 × 5 = 125.) How many have all digits different? (9 × 9 × 8 = 648 — why is the second 9 not a 10?)`,
  cliff:`If everything is different and you use all of it, the multiplying has a name and a shorthand.`},

 {t:"Arrangements and n!", len:"6 min",
  body:`<p>Arrange 5 different books on a shelf: 5 choices for the first place, 4 for the next, …, 1 for the last. That's 5 × 4 × 3 × 2 × 1, written <strong>5! = 120</strong> ("5 factorial").</p>
        <p>Arrange only 3 of the 5 (first, second, third prize): 5 × 4 × 3 = 60 — stop multiplying after 3 places. As factorials: 5! ÷ 2!.</p>
        <p><strong>Blocks.</strong> 5 friends in a row, two of them insist on sitting together. Glue them into one block: now 4 things to arrange (4! = 24), and the block can be either way round (× 2). <strong>48</strong>. And the arrangements where they're <em>not</em> together: 120 − 48 = 72.</p>
        <p><strong>Repeats.</strong> LEVEL: 5! counts the two Ls as different, so each real arrangement is counted 2! times; same for the Es. 120 ÷ (2 × 2) = <strong>30</strong>.</p>`,
  demo:`<strong>Do this:</strong> how many arrangements of BANANA? (6! ÷ (3! × 2!) = 60.) Of MISSISSIPPI? (11! ÷ (4! × 4! × 2!) = 34650.)`,
  cliff:`Arranging cares about order. Choosing a team doesn't. How do you count without order?`},

 {t:"Choosing: count ordered, then divide", len:"7 min",
  body:`<p>Choose 3 people from 7 for a team. Pretend order matters: 7 × 6 × 5 = 210. But each team of 3 has been counted once for every order of its members — 3! = 6 times. So there are 210 ÷ 6 = <strong>35</strong> teams.</p>
        <div class="eqline">choose r from n = n! ÷ (r! × (n − r)!) &nbsp;&nbsp; written C(n, r) or ⁿCᵣ</div>
        <p>The two you need most:</p>
        <ul><li>C(n, 2) = n(n − 1) ÷ 2 — <strong>handshakes</strong>, pairs, matches in a league, segments between points.</li>
            <li>C(n, 3) = n(n − 1)(n − 2) ÷ 6 — triangles from points.</li></ul>
        <p>Useful symmetry: C(n, r) = C(n, n − r). Choosing 3 to be in the team is the same as choosing 4 to leave out.</p>`,
  demo:`<strong>Do this:</strong> on the handshake circle, set n = 10 and read the handshakes. (45.) Check: 10 × 9 ÷ 2. Then switch to triangles. (120.)`,
  cliff:`'At least one girl on the committee.' Counting the cases one at a time is slow and easy to get wrong.`},

 {t:"Count the opposite", len:"6 min",
  body:`<p>Committees of 4 from 6 boys and 4 girls, with at least one girl. Cases (1 girl, 2 girls, 3, 4) work, but there's a faster way:</p>
        <div class="eqline">at least one girl = all committees − committees with no girls<br>= C(10, 4) − C(6, 4) = 210 − 15 = 195</div>
        <p>That's <strong>complementary counting</strong>. It wins whenever the thing you want is "at least one", "not all", or "some", and the opposite is "none" or "all".</p>
        <p><strong>Digits again.</strong> 3-digit numbers with at least one 7: all 3-digit numbers (900) minus those with no 7 at all (8 × 9 × 9 = 648) = <strong>252</strong>. The first digit has 8 choices (1–9 except 7), the others 9 (0–9 except 7).</p>`,
  demo:`<strong>Do this:</strong> how many 4-digit PINs contain at least one repeated digit? (10000 − 5040 = 4960.)`,
  cliff:`Back to choices. Walking across a grid of streets is a choice too — of which moves go up.`},

 {t:"Paths on a grid, and Pascal's triangle", len:"7 min",
  body:`<p>From the bottom-left corner to the top-right of a 4 × 3 grid, moving only right or up, every route is 7 moves: 4 rights and 3 ups in some order. Choosing which 3 of the 7 moves are 'up' fixes the route:</p>
        <div class="eqline">routes = C(7, 3) = 35</div>
        <p>The path grid tool shows the other way to get it: each crossing's count is the sum of the one to its left and the one below. Those numbers <em>are</em> Pascal's triangle, tipped on its side.</p>
        <p><strong>Through a point.</strong> Routes from (0, 0) to (4, 3) passing through (2, 1): routes to (2, 1) × routes from there on = C(3, 1) × C(4, 2) = 3 × 6 = 18. <strong>Avoiding</strong> a point: total − through it.</p>`,
  demo:`<strong>Do this:</strong> on the path grid, make a 4 × 4 grid and block the centre crossing (2, 2). Predict the count first: 70 − 6 × 6 = 34.`,
  cliff:`Grids, teams, letters, handshakes: it's all choosing and arranging. One last tool turns geometry into counting.`},

 {t:"Counting shapes", len:"6 min",
  body:`<p>12 points, no three in a line: every 3 of them make a triangle, so C(12, 3) = 220 triangles.</p>
        <p>But put 5 of the points on one line L and the other 7 on a parallel line M. Now three points on the same line don't make a triangle. Count the opposite:</p>
        <div class="eqline">triangles = C(12, 3) − C(5, 3) − C(7, 3) = 220 − 10 − 35 = 175</div>
        <p>Quadrilaterals with two corners on each line: choose 2 from L <em>and</em> 2 from M: C(5, 2) × C(7, 2) = 10 × 21 = 210.</p>
        <p><strong>Diagonals</strong> of an n-gon: every pair of corners is a side or a diagonal, so diagonals = C(n, 2) − n. For a decagon, 45 − 10 = 35 — the same answer as the angles page, by a completely different route.</p>`,
  demo:`<strong>Do this:</strong> how many rectangles are there on a 3 × 3 grid of squares (any size)? Choose 2 of the 4 vertical lines and 2 of the 4 horizontal lines: 6 × 6 = 36.`,
  cliff:`That's the lessons. Q14 is a 5 × 5 grid with a roadblock, and Q15 is triangles on two parallel lines. Go and lose to them, then take them apart.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"A café offers 3 starters, 4 mains and 2 desserts. How many different meals of one starter, one main and one dessert are there?",
  o:["9","24","12","48"], a:1,
  why:"Starter and main and dessert: multiply, 3 × 4 × 2 = 24. Option A added them — that counts choosing just one course."},
 {n:2, lvl:"standard", q:"In how many orders can the letters of <span class='num'>MATHS</span> be arranged?",
  o:["25","60","120","3125"], a:2,
  why:"Five different letters: 5! = 120. Option D is 5⁵, which lets letters repeat; option B is 5 × 4 × 3."},
 {n:3, lvl:"standard", q:"Ten people meet and every pair shakes hands once. How many handshakes are there?",
  o:["20","45","90","100"], a:1,
  why:"Each of 10 people shakes 9 hands: 90 — but that counts each handshake from both ends, so 45. Option C forgot to halve."},
 {n:4, lvl:"standard", q:"How many three-digit whole numbers are there?",
  o:["899","900","999","1000"], a:1,
  why:"From 100 to 999 inclusive: 999 − 100 + 1 = 900. Or 9 × 10 × 10. Option A is the fence-post error."},
 {n:5, lvl:"trap", q:"A class of 8 must choose 2 representatives (both with the same role). How many ways are there?",
  o:["16","28","56","64"], a:1,
  why:"Order doesn't matter: choosing Asha then Ravi is the same pair as Ravi then Asha. 8 × 7 ÷ 2 = 28. Option C is the answer if there were a captain and a vice-captain."}
];

const SHORTS = [
 {n:6, m:2, lvl:"warm-up", q:"A PIN has 4 digits, each from 0 to 9.<br><strong>(a)</strong> How many PINs are possible? <span class='num'>[1]</span><br><strong>(b)</strong> How many have four different digits? <span class='num'>[1]</span>",
  scheme:["(a) 10 × 10 × 10 × 10 = <strong>10000</strong> <span class='num'>[1]</span>",
          "(b) 10 × 9 × 8 × 7 = <strong>5040</strong> <span class='num'>[1]</span>"],
  tip:"A PIN can start with 0 — it's a code, not a number. That's the difference from Q4."},
 {n:7, m:2, lvl:"standard", q:"How many three-digit numbers contain at least one digit 7?",
  scheme:["Numbers with no 7: 8 × 9 × 9 = 648 <span class='num'>[1]</span>",
          "900 − 648 = <strong>252</strong> <span class='num'>[1]</span>"],
  tip:"The first digit can't be 0 or 7, so 8 choices; the others can't be 7, so 9 each. Counting the 7s directly almost always double-counts 77x, x77 and 777."},
 {n:8, m:2, lvl:"standard", q:"In how many different orders can the letters of the word <span class='num'>LEVEL</span> be arranged?",
  scheme:["5! = 120 if all letters were different <span class='num'>[1]</span>",
          "Divide by 2! for the Ls and 2! for the Es: 120 ÷ 4 = <strong>30</strong> <span class='num'>[1]</span>"],
  tip:"The V is the only letter on its own. Check one arrangement — say LEVEL itself — and see that swapping the two Ls gives the same word."},
 {n:9, m:2, lvl:"standard", q:"Moving only right or up along grid lines, how many shortest routes are there from (0, 0) to (4, 3)?<br><strong>(a)</strong> in total <span class='num'>[1]</span> &nbsp; <strong>(b)</strong> passing through (2, 1) <span class='num'>[1]</span>",
  scheme:["(a) 7 moves, 3 of them up: C(7, 3) = <strong>35</strong> <span class='num'>[1]</span>",
          "(b) To (2, 1): C(3, 1) = 3. From (2, 1) to (4, 3): C(4, 2) = 6. 3 × 6 = <strong>18</strong> <span class='num'>[1]</span>"],
  tip:"Check (a) on the path grid with 4 across and 3 up. For (b), 'through a point' splits the walk into two independent walks — multiply."},
 {n:10, m:2, lvl:"hard", q:"Explain why the number of handshakes among n people, when every pair shakes hands once, is <span class='num'>n(n − 1) ÷ 2</span>.",
  scheme:["Each of the n people shakes hands with the n − 1 others, giving n(n − 1) <span class='num'>[1]</span>",
          "Every handshake involves two people, so it has been counted <strong>twice</strong>; divide by 2 <span class='num'>[1]</span>"],
  tip:"The second mark is for saying <em>why</em> you divide by 2. 'Because of the formula' is not a reason."}
];

const WORDS = [
 {n:11, m:3, lvl:"standard", q:"A committee of 4 is chosen from 6 boys and 4 girls.<br><br><strong>(a)</strong> How many different committees are possible? <span class='num'>[1]</span><br><strong>(b)</strong> How many have exactly 2 girls? <span class='num'>[1]</span><br><strong>(c)</strong> How many have at least one girl? <span class='num'>[1]</span>",
  hints:["(a) is choosing 4 from 10, order not mattering.",
         "(b): choose 2 girls from 4 and 2 boys from 6. AND means multiply.",
         "(c): count the committees with no girls at all, and subtract."],
  sol:["(a) C(10, 4) = 10 × 9 × 8 × 7 ÷ 24 = <strong>210</strong>.",
       "(b) C(4, 2) × C(6, 2) = 6 × 15 = <strong>90</strong>.",
       "(c) No girls: C(6, 4) = 15. So 210 − 15 = <strong>195</strong>.",
       "Check (c) by cases: 1 girl 4 × 20 = 80, 2 girls 90, 3 girls 4 × 6 = 24, 4 girls 1. Total 195 ✓. Same answer — the complement was just faster."]},

 {n:12, m:3, lvl:"standard", q:"Three-digit numbers are made from the digits 1, 2, 3, 4, 5, 6, with no digit used twice.<br><br><strong>(a)</strong> How many can be made? <span class='num'>[1]</span><br><strong>(b)</strong> How many are even? <span class='num'>[1]</span><br><strong>(c)</strong> How many are divisible by 5? <span class='num'>[1]</span>",
  hints:["6 choices, then 5, then 4.",
         "Fill the most restricted place first: the units digit must be 2, 4 or 6.",
         "Divisible by 5 means the units digit is 5 (there's no 0)."],
  sol:["(a) 6 × 5 × 4 = <strong>120</strong>.",
       "(b) Units: 3 choices. Then 5 for hundreds and 4 for tens: 3 × 5 × 4 = <strong>60</strong>.",
       "(c) Units must be 5: 1 choice, then 5 × 4: <strong>20</strong>.",
       "Half the numbers are even because exactly half the digits are. That symmetry is a free check on (b)."]},

 {n:13, m:3, lvl:"standard", q:"Five friends sit in a row of five chairs for a photo. Two of them, Anu and Bina, are sisters.<br><br><strong>(a)</strong> How many different seating orders are there? <span class='num'>[1]</span><br><strong>(b)</strong> In how many do the sisters sit next to each other? <span class='num'>[1]</span><br><strong>(c)</strong> In how many are they not next to each other? <span class='num'>[1]</span>",
  hints:["5 people in 5 places.",
         "Glue the sisters into one block. How many things are you now arranging? And which way round can the block go?",
         "Count the opposite."],
  sol:["(a) 5! = <strong>120</strong>.",
       "(b) The block plus 3 others: 4! = 24 orders, and the sisters can swap inside the block: 24 × 2 = <strong>48</strong>.",
       "(c) 120 − 48 = <strong>72</strong>.",
       "Forgetting the × 2 in (b) is the usual slip — AB and BA are different photos."]},

 {n:14, m:3, lvl:"hard", q:"A city is a 5 × 5 grid of streets. You walk from the south-west corner (0, 0) to the north-east corner (5, 5), always going east or north.<br><br><strong>(a)</strong> How many routes are there? <span class='num'>[1]</span><br><strong>(b)</strong> How many pass through the crossing (2, 2)? <span class='num'>[1]</span><br><strong>(c)</strong> The crossing (2, 2) is closed for roadworks. How many routes remain? <span class='num'>[1]</span>",
  hints:["Every route is 10 moves, 5 of them north. Which 5?",
         "Split the walk at (2, 2): routes to it, times routes from it to (5, 5).",
         "Routes avoiding a point = all routes − routes through it."],
  sol:["(a) C(10, 5) = <strong>252</strong>.",
       "(b) To (2, 2): C(4, 2) = 6. From (2, 2) to (5, 5): C(6, 3) = 20. 6 × 20 = <strong>120</strong>.",
       "(c) 252 − 120 = <strong>132</strong>.",
       "Nearly half of all routes go through that one crossing — central points are on a lot of paths. Try it on the path grid with a 5 × 5 grid: you'll see 132 appear in the corner."]},

 {n:15, m:3, lvl:"hard", q:"Five points are marked on a straight line L, and seven points on a different line M parallel to L.<br><br><strong>(a)</strong> How many line segments join a point of L to a point of M? <span class='num'>[1]</span><br><strong>(b)</strong> How many triangles have all three corners among the 12 points? <span class='num'>[1]</span><br><strong>(c)</strong> How many quadrilaterals have two corners on L and two on M? <span class='num'>[1]</span>",
  hints:["One point from L and one from M.",
         "Choose any 3 of the 12, then throw away the choices that are all on one line — they don't make a triangle.",
         "Choose 2 from L and 2 from M."],
  sol:["(a) 5 × 7 = <strong>35</strong>.",
       "(b) C(12, 3) − C(5, 3) − C(7, 3) = 220 − 10 − 35 = <strong>175</strong>.",
       "(c) C(5, 2) × C(7, 2) = 10 × 21 = <strong>210</strong>.",
       "Check (b) by cases: 2 on L and 1 on M is 10 × 7 = 70, 1 on L and 2 on M is 5 × 21 = 105, total 175 ✓."]}
];
'''

TOOLS_JS = r'''
/* ---------------- the path grid ---------------- */
let gTarget=null, curGPuzzle=null, gBlocked=new Set();
function C(n,r){ if(r<0||r>n) return 0; let v=1; for(let i=1;i<=r;i++) v=v*(n-r+i)/i; return Math.round(v); }
function pathCounts(W,H,blocked){
  const N=[]; for(let i=0;i<=W;i++){ N.push([]); for(let j=0;j<=H;j++){
    if(blocked.has(i+','+j)) N[i][j]=0;
    else if(i===0&&j===0) N[i][j]=1;
    else N[i][j]=(i?N[i-1][j]:0)+(j?N[i][j-1]:0);
  } }
  return N;
}
function drawGrid(){
  const W=+document.getElementById('gw').value, H=+document.getElementById('gh').value;
  document.getElementById('gw-v').textContent=W; document.getElementById('gh-v').textContent=H;
  [...gBlocked].forEach(k=>{ const [i,j]=k.split(',').map(Number); if(i>W||j>H||(i===0&&j===0)||(i===W&&j===H)) gBlocked.delete(k); });
  const N=pathCounts(W,H,gBlocked);
  const u=Math.min(600/Math.max(W,1), 280/Math.max(H,1), 80), ox=(700-W*u)/2, oy=20+H*u;
  let g='';
  for(let i=0;i<=W;i++) g+=`<line x1="${ox+i*u}" y1="${oy}" x2="${ox+i*u}" y2="${oy-H*u}" stroke="var(--line)" stroke-width="3"/>`;
  for(let j=0;j<=H;j++) g+=`<line x1="${ox}" y1="${oy-j*u}" x2="${ox+W*u}" y2="${oy-j*u}" stroke="var(--line)" stroke-width="3"/>`;
  for(let i=0;i<=W;i++) for(let j=0;j<=H;j++){
    const x=ox+i*u, y=oy-j*u, bl=gBlocked.has(i+','+j), end=(i===W&&j===H), st=(i===0&&j===0);
    const fill = bl ? 'var(--ng)' : end ? 'var(--pm)' : st ? 'var(--rt)' : 'var(--card)';
    const col = (bl||end||st) ? '#fff' : 'var(--ink)';
    g+=`<circle class="node" data-n="${i},${j}" cx="${x}" cy="${y}" r="16" fill="${fill}" stroke="var(--steel)" stroke-width="1.5"/>`;
    g+=`<text x="${x}" y="${y+4.5}" text-anchor="middle" font-family="var(--mono)" font-size="${N[i][j]>999?9.5:12}" font-weight="700" fill="${col}" pointer-events="none">${bl?'×':N[i][j]}</text>`;
  }
  document.getElementById('gStage').innerHTML=g;
  const total=N[W][H];
  document.getElementById('g-n').textContent=total;
  document.getElementById('g-ns').textContent=`${W} rights and ${H} ups`;
  document.getElementById('g-c').textContent = gBlocked.size ? `C(${W+H}, ${H}) = ${C(W+H,H)} before blocks` : `C(${W+H}, ${H}) = ${C(W+H,H)}`;
  document.getElementById('g-b').textContent = gBlocked.size ? [...gBlocked].map(k=>'('+k+')').join(' ') : 'none';
  const pill=document.getElementById('g-pill'), note=document.getElementById('g-note');
  if(gTarget){
    const T=gTarget; pill.className='pill up'; pill.textContent='Puzzle running';
    let ok;
    if(T.grid){ ok = W===T.grid[0] && H===T.grid[1] && gBlocked.size===1 && total===T.count; if(W!==T.grid[0]||H!==T.grid[1]) { note.textContent=`Set the grid to ${T.grid[0]} × ${T.grid[1]} first.`; } else note.textContent=`${total} routes. You need ${T.count}, with exactly one crossing blocked.`; }
    else { ok = gBlocked.size===0 && total===T.count; note.textContent = gBlocked.size ? 'This puzzle needs no blocks — clear them.' : `${total} routes. You need ${T.count}.`; }
    if(ok){
      gTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('gQuiz'); box.classList.add('on');
      box.innerHTML=`<strong>${total} routes.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="gAgain">Another one</button></div>`;
      document.getElementById('gAgain').addEventListener('click', ()=>document.getElementById('gPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Routes = choose which moves are up. Blocked = total minus through.';
    }
  }else{
    pill.className='pill go'; pill.textContent='Adding';
    note.textContent='Each number is the one to its left plus the one below. That\'s Pascal\'s triangle, tilted.';
  }
}
function toggleBlock(key){
  const W=+document.getElementById('gw').value, H=+document.getElementById('gh').value;
  if(key==='0,0' || key===W+','+H) return;
  if(gBlocked.has(key)) gBlocked.delete(key); else gBlocked.add(key);
  drawGrid();
}
document.getElementById('gStage').addEventListener('click', e=>{ const c=e.target.closest('[data-n]'); if(c) toggleBlock(c.dataset.n); });
['gw','gh'].forEach(id=>document.getElementById(id).addEventListener('input', drawGrid));
document.getElementById('gClear').addEventListener('click', ()=>{ gBlocked.clear(); drawGrid(); });
const G_PUZZLES=[
 {count:20, more:'C(6, 3) = 20: a 3 × 3 grid.'},
 {count:35, more:'C(7, 3) = 35: 4 × 3 or 3 × 4.'},
 {count:15, more:'C(6, 2) = 15: 4 × 2 or 2 × 4. (1 × 14 won\'t fit.)'},
 {count:56, more:'C(8, 3) = 56: 5 × 3 or 3 × 5.'},
 {grid:[3,3], count:10, more:'Block a crossing next to the start (or the end): 10 routes go through it, 20 − 10 = 10 remain.'},
 {grid:[4,4], count:34, more:'The centre (2, 2) has 6 × 6 = 36 routes through it, and 70 − 36 = 34.'}
];
document.getElementById('gPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*G_PUZZLES.length);
  if(curGPuzzle===i) i=(i+1)%G_PUZZLES.length;
  curGPuzzle=i; gTarget=G_PUZZLES[i];
  gBlocked.clear(); document.getElementById('gw').value=1; document.getElementById('gh').value=1;   /* start from an unsolved state */
  const T=gTarget, box=document.getElementById('gQuiz'); box.classList.add('on');
  box.innerHTML = T.grid
    ? `<strong>Puzzle.</strong> On a ${T.grid[0]} × ${T.grid[1]} grid, block exactly <strong>one</strong> crossing so that exactly <span class="num" style="font-size:17px">${T.count}</span> routes remain. Work out how many routes each crossing carries first.`
    : `<strong>Puzzle.</strong> Make a grid with no blocks that has exactly <span class="num" style="font-size:17px">${T.count}</span> routes to the corner. Which C(a + b, b) is it?`;
  drawGrid();
});

/* ---------------- the handshake circle ---------------- */
let cMode='pairs', cTarget=null, curCPuzzle=null;
function drawCircle(){
  const n=+document.getElementById('cn').value;
  document.getElementById('cn-v').textContent=n;
  const cx=350, cy=150, R=120, pts=[];
  for(let k=0;k<n;k++){ const a=-Math.PI/2+2*Math.PI*k/n; pts.push([cx+R*Math.cos(a), cy+R*Math.sin(a)]); }
  let g='';
  if(cMode==='pairs'){
    for(let i=0;i<n;i++) for(let j=i+1;j<n;j++){
      const side = (j===i+1)||(i===0&&j===n-1);
      g+=`<line x1="${pts[i][0].toFixed(1)}" y1="${pts[i][1].toFixed(1)}" x2="${pts[j][0].toFixed(1)}" y2="${pts[j][1].toFixed(1)}" stroke="${side?'var(--pm)':'var(--ng)'}" stroke-width="${side?2.5:1.3}" opacity="${side?1:.6}"/>`;
    }
  }else{
    // draw one highlighted triangle and faint sides
    for(let i=0;i<n;i++){ const j=(i+1)%n; g+=`<line x1="${pts[i][0].toFixed(1)}" y1="${pts[i][1].toFixed(1)}" x2="${pts[j][0].toFixed(1)}" y2="${pts[j][1].toFixed(1)}" stroke="var(--line)" stroke-width="1.5"/>`; }
    if(n>=3) g+=`<polygon points="${[0,Math.floor(n/3),Math.floor(2*n/3)].map(k=>pts[k].map(v=>v.toFixed(1)).join(',')).join(' ')}" fill="var(--rt-tint)" stroke="var(--rt)" stroke-width="2.5"/>`;
  }
  pts.forEach((p,k)=>{ g+=`<circle cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="11" fill="var(--card)" stroke="var(--ink)" stroke-width="2"/><text x="${p[0].toFixed(1)}" y="${(p[1]+4).toFixed(1)}" text-anchor="middle" font-family="var(--mono)" font-size="10.5" font-weight="700" fill="var(--ink)">${k+1}</text>`; });
  document.getElementById('cStage').innerHTML=g;
  const pairs=n*(n-1)/2, trips=n*(n-1)*(n-2)/6;
  if(cMode==='pairs'){
    document.getElementById('c-l1').textContent='Handshakes';
    document.getElementById('c-v1').textContent=pairs;
    document.getElementById('c-s1').textContent=`${n} × ${n-1} ÷ 2`;
    document.getElementById('c-l2').textContent='Ordered pairs';
    document.getElementById('c-v2').textContent=n*(n-1);
    document.getElementById('c-s2').textContent='each handshake counted from both ends';
  }else{
    document.getElementById('c-l1').textContent='Triangles';
    document.getElementById('c-v1').textContent=trips;
    document.getElementById('c-s1').textContent=`${n} × ${n-1} × ${n-2} ÷ 6`;
    document.getElementById('c-l2').textContent='Ordered triples';
    document.getElementById('c-v2').textContent=n*(n-1)*(n-2);
    document.getElementById('c-s2').textContent='each triangle counted 3! = 6 times';
  }
  document.getElementById('c-v3').textContent = n>=4 ? pairs-n : 0;
  const pill=document.getElementById('c-pill'), note=document.getElementById('c-note');
  if(cTarget){
    const T=cTarget; pill.className='pill up'; pill.textContent='Puzzle running';
    const val = T.kind==='pairs' ? pairs : T.kind==='trips' ? trips : pairs-n;
    const modeOk = T.kind==='diag' || cMode===T.kind;
    if(modeOk && val===T.v){
      cTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('cQuiz'); box.classList.add('on');
      box.innerHTML=`<strong>n = ${n}.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="cAgain">Another one</button></div>`;
      document.getElementById('cAgain').addEventListener('click', ()=>document.getElementById('cPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Count ordered, then divide by how many orders each group has.';
    }else note.textContent = modeOk ? 'Not this n. Set up the equation and solve it first.' : `Switch to ${T.kind==='pairs'?'pairs':'triangles'} mode.`;
  }else{
    pill.className='pill up'; pill.textContent='Joining';
    note.textContent='Count ordered, then divide by how many orders each group has.';
  }
}
function setCMode(m){
  cMode=m;
  document.getElementById('cPairs').className='btn small '+(m==='pairs'?'on':'ghost');
  document.getElementById('cTrips').className='btn small '+(m==='trips'?'on':'ghost');
  drawCircle();
}
document.getElementById('cPairs').addEventListener('click', ()=>setCMode('pairs'));
document.getElementById('cTrips').addEventListener('click', ()=>setCMode('trips'));
document.getElementById('cn').addEventListener('input', drawCircle);
const C_PUZZLES=[
 {kind:'pairs', v:45, more:'n(n − 1) = 90 = 10 × 9.'},
 {kind:'pairs', v:28, more:'n(n − 1) = 56 = 8 × 7.'},
 {kind:'pairs', v:66, more:'n(n − 1) = 132 = 12 × 11.'},
 {kind:'trips', v:20, more:'n(n − 1)(n − 2) = 120 = 6 × 5 × 4.'},
 {kind:'trips', v:56, more:'n(n − 1)(n − 2) = 336 = 8 × 7 × 6.'},
 {kind:'diag', v:27, more:'n(n − 3) ÷ 2 = 27 gives n(n − 3) = 54 = 9 × 6.'}
];
document.getElementById('cPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*C_PUZZLES.length);
  if(curCPuzzle===i) i=(i+1)%C_PUZZLES.length;
  curCPuzzle=i; cTarget=C_PUZZLES[i];
  document.getElementById('cn').value=2;   /* start from an unsolved state */
  const T=cTarget, what = T.kind==='pairs' ? `exactly <span class="num" style="font-size:17px">${T.v}</span> handshakes`
    : T.kind==='trips' ? `exactly <span class="num" style="font-size:17px">${T.v}</span> triangles (in triangles mode)`
    : `a polygon with exactly <span class="num" style="font-size:17px">${T.v}</span> diagonals`;
  const box=document.getElementById('cQuiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> Find the n that gives ${what}. Solve it on paper, then set it.`;
  drawCircle();
});
'''

BOOT = ['drawGrid()', 'drawCircle()']
