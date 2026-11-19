# -*- coding: utf-8 -*-
ID = 'ioqm-logic'
SHORT_TITLE = "It Can't Be Done"
SUB = 'IOQM · Combinatorics II: pigeonhole, parity, colouring, invariants, logic'
BLURB = ("The cleverest Olympiad answers prove that something must happen, or that it never can. Find the worst case that forces "
         "the pigeonhole, then knock squares off a chessboard and learn why balanced colours still don't guarantee a tiling.")
META_TOOL = 'domino board'
COLOURS = ('#5A3E85', '#EEE9F6', '#1F6E4E', '#E3F2EB', '#9A4A12', '#F9ECE1')
EYEBROW = 'IOQM Olympiad Prep · Combinatorics II'
H1 = "It <i>Can't</i><br>Be <em>Done</em>"
LEDE = ("Some questions don't want a number. They want a reason: why two of these must match, why that move can never finish, "
        "why the tiling is impossible. The tools are tiny — boxes, odd and even, two colours — and the proofs they give are the most satisfying in mathematics.")
TARGET = ("You've been landing around <span class=\"num\">10 out of 15</span> at school. This page is out of <span class=\"num\">30</span>; "
          "the targets are <span class=\"num\">21</span> on the first pass and <span class=\"num\">26</span> on the second. "
          "Many answers here are explanations. A correct number with no reason earns little; a clear reason earns almost everything.")
VIDEO_MIN = '~40 min total'
LESSON_MIN = '~40 min total'
NAV = [('holes', 'Pigeonholes'), ('videos', '6 videos'), ('lessons', '6 lessons'), ('board', 'Domino board'),
       ('quick', 'Quick checks'), ('short', 'Short answers'), ('word', 'Word problems'), ('traps', 'Exam traps')]

EXTRA_CSS = r'''
#bStageL rect.sq{cursor:pointer}
select{font-family:var(--mono);font-size:15px;padding:7px 9px;border:1px solid var(--line);border-radius:9px;background:var(--paper);color:var(--ink)}
'''

TOOL1_HTML = r'''
<section id="holes">
  <div class="panel">
    <div class="panel-top">
      <h2>The pigeonholes</h2>
      <p>Drop pigeons into boxes as <em>evenly as possible</em> — that's the worst case, the arrangement trying hardest to avoid a crowded box. Even then, once there are more pigeons than boxes, some box has two. The machine shows the fullest box in the most even spread.</p>
    </div>
    <svg class="stage" viewBox="0 0 700 260" role="img" aria-label="Pigeons spread as evenly as possible across boxes"><g id="hStage"></g></svg>
    <div class="ctrl">
      <label for="hn">Boxes</label><input id="hn" type="range" min="2" max="12" value="4" aria-label="Number of boxes"><span class="num" id="hn-v">4</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="hk">Pigeons</label><input id="hk" type="range" min="1" max="40" value="9" aria-label="Number of pigeons"><span class="num" id="hk-v">9</span>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">Fullest box (at least)</div><div class="val" id="h-max">—</div><div class="sub" id="h-maxs"></div></div>
      <div class="cell d"><div class="lab">One fewer pigeon</div><div class="val" id="h-less">—</div><div class="sub">would the guarantee still hold?</div></div>
      <div class="cell p"><div class="lab">To force t in a box</div><div class="val" id="h-force" style="font-size:16px">—</div><div class="sub">boxes × (t − 1) + 1</div></div>
      <div class="phasebar">
        <span class="pill go" id="h-pill">Spreading</span>
        <span id="h-note">Guarantee questions are answered by the worst case, plus one.</span>
        <span class="push"><button class="btn ghost" type="button" id="hPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="hQuiz"></div>
    </div>
  </div>
</section>
'''

TOOL2_HTML = r'''
<section id="board">
  <div class="panel">
    <div class="panel-top">
      <h2>The domino board</h2>
      <p>Each domino covers two neighbouring squares — always one dark and one light. <strong>Click squares</strong> to remove them. The machine counts the colours and then actually searches for a tiling. Equal colours are needed; they are not always enough.</p>
    </div>
    <svg class="stage" viewBox="0 0 700 330" role="img" aria-label="A chessboard with squares that can be removed"><g id="bStageL"></g></svg>
    <div class="ctrl">
      <label for="bsz">Board</label>
      <select id="bsz" aria-label="Board size"><option value="4">4 × 4</option><option value="5">5 × 5</option><option value="6" selected>6 × 6</option><option value="8">8 × 8</option></select>
      <button class="btn ghost small" type="button" id="bReset">Restore all squares</button>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">Dark / light left</div><div class="val" id="bl-c">—</div><div class="sub" id="bl-cs"></div></div>
      <div class="cell d"><div class="lab">Colour test</div><div class="val" id="bl-t" style="font-size:16px">—</div><div class="sub">necessary, not sufficient</div></div>
      <div class="cell p"><div class="lab">Tiling exists?</div><div class="val" id="bl-m" style="font-size:16px">—</div><div class="sub" id="bl-ms">found by search</div></div>
      <div class="phasebar">
        <span class="pill up" id="bl-pill">Tiling</span>
        <span id="bl-note">Remove two opposite corners of an 8 × 8 and see what the colours say.</span>
        <span class="push"><button class="btn ghost" type="button" id="blPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="blQuiz"></div>
    </div>
  </div>
</section>
'''

TRAPS = [
 ("Answering the worst case instead of worst case + 1",
  "With 3 colours of sock, you could pull out 3 and have no pair — one of each. The 4th forces a pair. So the answer is <strong>4</strong>, not 3. Always build the worst case first, count it, then add one."),
 ("Thinking pigeonhole tells you which box",
  "Pigeonhole proves that <em>some</em> box has two pigeons. It never says which. If your answer names the box — 'so January has two birthdays' — it's wrong. Say 'some month'."),
 ("Proving impossibility with examples",
  "Trying ten ways to tile a board and failing proves nothing — maybe the eleventh works. Impossibility needs an <strong>invariant</strong>: a quantity no move can change, which is different at the start and the end."),
 ("Trusting balanced colours",
  "Each domino covers one dark and one light, so unequal colours make tiling impossible. But equal colours <strong>don't</strong> make it possible: a corner cut off by its two neighbours can't be covered whatever the counts say. Try it on the domino board."),
 ("Checking only one case in a logic puzzle",
  "\"Suppose A is a knight — that works, so A is a knight.\" Not until you've shown that A being a knave <strong>fails</strong>. A logic answer is only complete when every other case has been killed with a contradiction.")
]

DATA_JS = r'''
/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"Pigeonhole Principle", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=zLm_qGfZA_Q",
  why:"The principle and its general form: n + 1 pigeons in n holes force a double; kn + 1 force k + 1. Short and clear.",
  task:"How many people do you need to be sure two share a birthday month? Three share one? (13 and 25.) Write the worst case for each."},

 {t:"Pigeonhole Principle — Intermediate Problems", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=onnyFEJ8ix4",
  why:"Problems where the hard part is choosing the boxes — remainders, pairs that add to a fixed total, regions of a square. That's lesson 2.",
  task:"For each problem, pause after it's read and write what the boxes should be before he says. Count how many you got."},

 {t:"Mutilated Chessboard Problem Explained", ch:"Melissa Maths", url:"https://www.youtube.com/watch?v=iT6gHHsVjss",
  why:"The most famous colouring argument there is: 31 dominoes can't cover a chessboard missing two opposite corners. The domino board below lets you try.",
  task:"Before the explanation, try for two minutes to tile a 4 × 4 board missing two opposite corners on paper. Then write the colour argument in two sentences."},

 {t:"Invariance Principle in Math Olympiad", ch:"Cheenta", url:"https://www.youtube.com/watch?v=0Ob3iFvpFCs",
  why:"Put + or − signs between 1 to 6 — can you ever get 0? An Olympiad class working out why not. Exactly the parity idea of lesson 3.",
  task:"Can you put + and − signs between 1, 2, …, 7 to get 0? (Yes — 1 + … + 7 = 28 is even, so parity allows it, and 1 + 2 − 3 + 4 − 5 − 6 + 7 = 0.) Then explain why 1 to 6 can't."},

 {t:"Can You Say What is Invariant?", ch:"Cheenta", url:"https://www.youtube.com/watch?v=6-PoEI-kWcY",
  why:"More invariant problems: a process that changes things, and the one quantity it can't change. Lesson 5 and Q15.",
  task:"Seven coins are heads up. Each move turns over exactly two coins. Can you make all seven tails? Write the invariant in one line."},

 {t:"Knights and Knaves logic puzzle", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=MoXB06XqWG0",
  why:"Two methods for knights-and-knaves puzzles and which is better. Logic puzzles turn up in IOQM, and they train the 'test every case' habit.",
  task:"A says 'B is a knave.' B says 'A and I are the same kind.' Work out both. (A knight, B knave.)"}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"The pigeonhole principle", len:"6 min",
  body:`<p>Put 5 pigeons into 4 holes and some hole has at least 2. Obvious — and yet it proves things that look impossible to prove.</p>
        <div class="eqline">k pigeons in n holes &nbsp;⟹&nbsp; some hole has at least ⌈k ÷ n⌉ pigeons</div>
        <p>(⌈ ⌉ means round up.) 30 students and 12 months: 30 ÷ 12 = 2.5, so some month has at least <strong>3</strong> birthdays.</p>
        <p><strong>'How many to guarantee' questions</strong> are answered by building the worst case. Socks in 3 colours: the worst case is one of each — 3 socks, no pair. One more forces a pair: <strong>4</strong>. To force 3 of one colour: worst case is 2 of each (6 socks), so <strong>7</strong>. In general:</p>
        <div class="eqline">to force t in one of n boxes: n(t − 1) + 1</div>`,
  demo:`<strong>Do this:</strong> on the pigeonholes tool, set 7 boxes (days of the week). How many people force 4 to share a day? Predict, then slide. (7 × 3 + 1 = 22.)`,
  cliff:`The principle is easy. The skill is choosing what the 'holes' are — they're almost never given.`},

 {t:"Choosing the boxes", len:"7 min",
  body:`<p><strong>Remainders as boxes.</strong> Among any 6 whole numbers, two differ by a multiple of 5. The boxes are the 5 possible remainders on division by 5 (0–4). Six numbers, five boxes: two share a remainder, and their difference is a multiple of 5.</p>
        <p><strong>Pairs as boxes.</strong> Choose any 6 numbers from 1 to 10. Two of them add to 11. Boxes: {1, 10}, {2, 9}, {3, 8}, {4, 7}, {5, 6}. Six numbers in five boxes: some box gets both its numbers.</p>
        <p><strong>Regions as boxes.</strong> Five points in a 2 × 2 square: two are at most √2 apart. Cut the square into four 1 × 1 squares; two points share one, and the farthest apart two points in a unit square can be is its diagonal, √2.</p>
        <p>In each case the work is in the boxes. Once you've chosen them, the proof is one line.</p>`,
  demo:`<strong>Do this:</strong> prove that among any 4 whole numbers, two differ by a multiple of 3. Write the boxes first.`,
  cliff:`Remainders on division by 2 are the simplest boxes of all. They have a name.`},

 {t:"Parity: odd and even", len:"6 min",
  body:`<p>odd + odd = even, odd + even = odd, and changing a + to a − never changes whether a sum is odd or even (a + b and a − b differ by 2b).</p>
        <p><strong>Example.</strong> Put + or − in front of each of 1, 2, …, 10. Can the total be 0? The plain sum 1 + … + 10 = 55 is odd, and flipping signs keeps it odd. 0 is even. <strong>Never.</strong></p>
        <p><strong>Handshakes.</strong> Add up how many hands each person shook. Every handshake adds 2 (one for each person), so the total is even. That means 9 people can't each shake exactly 3 hands — the total would be 27, odd. It also means the number of people who shook an odd number of hands is always even.</p>
        <p>Parity is the first thing to check when a question asks "is it possible?"</p>`,
  demo:`<strong>Do this:</strong> can 7 people each shake hands with exactly 5 others? (Total 35, odd — no.) Can 8 people each shake hands with exactly 5? (Total 40 — parity allows it; try to draw it.)`,
  cliff:`Odd and even split numbers into two kinds. Colouring does the same to squares.`},

 {t:"Colouring", len:"7 min",
  body:`<p>Colour a chessboard as usual. Every domino covers two <em>neighbouring</em> squares, which are always one dark and one light. So any set of dominoes covers equal numbers of each colour.</p>
        <p>Remove two opposite corners from an 8 × 8 board. Opposite corners are the <strong>same colour</strong>, so what's left has 32 of one colour and 30 of the other. 31 dominoes would cover 31 of each. <strong>Impossible</strong> — and you never tried a single arrangement.</p>
        <p><strong>Equal colours aren't enough.</strong> On the domino board, remove the two squares next to a corner, plus two of the other colour somewhere else. The colours balance, but the corner square is cut off and nothing can cover it. A colour count can prove a tiling impossible; it can't prove one exists.</p>
        <p>Odd boards: a 5 × 5 has 13 of one colour and 12 of the other. Remove one square of the <em>majority</em> colour and tiling becomes possible; remove a minority square and it's impossible.</p>`,
  demo:`<strong>Do this:</strong> on the domino board, choose 8 × 8 and remove two opposite corners. Read the colour counts. Then put them back and remove one corner plus a square next to it.`,
  cliff:`Colour counts don't change when you add dominoes. Things that don't change are the most powerful idea on this page.`},

 {t:"Invariants", len:"7 min",
  body:`<p>An <strong>invariant</strong> is a quantity that no allowed move can change. If it's different at the start and at the target, the target is unreachable.</p>
        <p><strong>Example.</strong> The numbers 1 to 10 are on a board. A move: rub out any two, a and b, and write their difference. After nine moves one number is left. Can it be 0?</p>
        <p>The total changes from … + a + b + … to … + (a − b) + …, a drop of 2b — even. So the <em>parity</em> of the total never changes. It starts at 55, odd. 0 is even. <strong>No.</strong></p>
        <p><strong>Coins.</strong> 7 coins heads up; a move turns over exactly 2. The number of heads changes by −2, 0 or +2, so its parity is invariant: it stays odd and can never reach 0. Change the rule to "turn over exactly 3" and parity is no longer invariant — and then it can be done (Q15).</p>`,
  demo:`<strong>Do this:</strong> the numbers 1 to 6 are written down. A move adds 1 to any two of them. Can you ever make all six equal? (The total starts at 21 and rises by 2 each move, so it stays odd. Six equal numbers add to an even total. Never.)`,
  cliff:`Invariants kill impossible things. Logic puzzles kill impossible cases.`},

 {t:"Logic: try every case", len:"6 min",
  body:`<p>On an island, <strong>knights</strong> always tell the truth and <strong>knaves</strong> always lie.</p>
        <p>A says: "We are both knaves." Test both cases for A:</p>
        <ul><li>If A is a knight, the statement is true, so A is a knave. Contradiction.</li>
            <li>So A is a knave, and the statement is false: they are <em>not</em> both knaves. Since A is one, <strong>B is a knight</strong>.</li></ul>
        <p>The method is <strong>proof by cases</strong>: suppose each possibility in turn, follow it until it contradicts itself or survives. The answer is whatever survives — and you must have killed everything else.</p>
        <p>Same habit, harder dress: "Three boxes are labelled Apples, Oranges and Mixed; every label is wrong. You may take one fruit from one box. Which box?" (The one labelled Mixed — it must be all apples or all oranges, and that one fruit tells you which; then the other two labels follow.)</p>`,
  demo:`<strong>Do this:</strong> A says "B is a knave." B says "A and I are the same kind." Test all four cases (KK, KN, NK, NN) in a table. Only one survives: A knight, B knave.`,
  cliff:`That's the lessons. Q14 picks six numbers and forces two of them to add to 11, and Q15 is seven coins that won't all turn over. Go and lose to them, then take them apart.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"A drawer has socks in 3 colours. In the dark, how many must you take to be <strong>sure</strong> of a matching pair?",
  o:["2","3","4","6"], a:2,
  why:"Worst case: one of each colour, 3 socks, no pair. The 4th must match one. Option B is the worst case itself, without the + 1."},
 {n:2, lvl:"standard", q:"In a class of 30, what is the largest number of students that must share a birth month, whatever their birthdays?",
  o:["2","3","4","12"], a:1,
  why:"30 ÷ 12 = 2.5, rounded up is 3. Spread as evenly as possible, 6 months get 3 and 6 get 2 — so 3 is guaranteed but 4 isn't."},
 {n:3, lvl:"standard", q:"Put a + or − sign in front of each of the numbers 1, 2, 3, …, 10 and add. Can the result be 0?",
  o:["Yes, with the right signs","No — the total is always odd","No — because 10 is even","Only with exactly five minus signs"], a:1,
  why:"1 + 2 + … + 10 = 55 is odd, and turning a + into a − changes the total by an even amount. So every total is odd, and 0 is even."},
 {n:4, lvl:"standard", q:"Two opposite corner squares are removed from an 8 × 8 chessboard. Can the remaining 62 squares be covered by 31 dominoes?",
  o:["Yes","No — the two removed squares are the same colour","No — 62 is not a multiple of 4","Only if the dominoes can overlap"], a:1,
  why:"Every domino covers one dark and one light square. Opposite corners are the same colour, leaving 30 of one colour and 32 of the other — but 31 dominoes cover 31 of each."},
 {n:5, lvl:"trap", q:"Among <strong>any</strong> five whole numbers, two of them must:",
  o:["have the same last digit","differ by a multiple of 4","both be even","both be odd"], a:1,
  why:"There are 4 possible remainders on division by 4, so two of the five share one — and then their difference is a multiple of 4. Options C and D can fail (1, 3, 5, 7, 9 has no evens; 2, 4, 6, 8, 10 no odds), and five numbers can easily have different last digits."}
];

const SHORTS = [
 {n:6, m:2, lvl:"warm-up", q:"A drawer holds 6 red, 4 blue and 2 green socks. You take socks in the dark.<br><strong>(a)</strong> How many must you take to be sure of two the same colour? <span class='num'>[1]</span><br><strong>(b)</strong> How many to be sure of two <strong>blue</strong> socks? <span class='num'>[1]</span>",
  scheme:["(a) Worst case one of each colour (3), so <strong>4</strong> <span class='num'>[1]</span>",
          "(b) Worst case all 6 red, both green and 1 blue (9), so <strong>10</strong> <span class='num'>[1]</span>"],
  tip:"In (b) the worst case uses up every non-blue sock first. The numbers of socks of each colour suddenly matter, where in (a) they didn't."},
 {n:7, m:2, lvl:"standard", q:"<strong>(a)</strong> Explain why, among any 13 people, two were born in the same month. <span class='num'>[1]</span><br><strong>(b)</strong> How many people are needed to be sure that <strong>three</strong> share a birth month? <span class='num'>[1]</span>",
  scheme:["(a) 12 months are 12 boxes; 13 people in 12 boxes puts two in one box <span class='num'>[1]</span>",
          "(b) Worst case two per month = 24, so <strong>25</strong> <span class='num'>[1]</span>"],
  tip:"The formula n(t − 1) + 1 gives 12 × 2 + 1. But write the worst case in words — it's the reason, and it's what earns the mark."},
 {n:8, m:2, lvl:"standard", q:"Knights always tell the truth; knaves always lie. A says: \"We are both knaves.\" What are A and B?",
  scheme:["If A were a knight, the statement would be true and A a knave — contradiction, so <strong>A is a knave</strong> <span class='num'>[1]</span>",
          "So the statement is false: not both knaves. A is one, so <strong>B is a knight</strong> <span class='num'>[1]</span>"],
  tip:"Both marks need the reasoning. 'A knave, B knight' alone earns at most one."},
 {n:9, m:2, lvl:"standard", q:"The numbers 1 to 10 are written on a board. A move: rub out any two numbers and write their difference. After nine moves one number is left. Explain why it cannot be 0.",
  scheme:["Replacing a and b by a − b changes the total by 2b, an even number, so the parity of the total never changes <span class='num'>[1]</span>",
          "It starts at 55, odd, so the final number is odd and <strong>can't be 0</strong> <span class='num'>[1]</span>"],
  tip:"Name the invariant (parity of the sum), show a move can't change it, compare start and target. That three-step shape is every invariant proof."},
 {n:10, m:2, lvl:"hard", q:"Prove that among any 6 whole numbers there are two whose difference is a multiple of 5.",
  scheme:["Use the 5 possible remainders on division by 5 (0, 1, 2, 3, 4) as boxes <span class='num'>[1]</span>",
          "6 numbers in 5 boxes: two share a remainder, so their difference is a <strong>multiple of 5</strong> <span class='num'>[1]</span>"],
  tip:"Why does sharing a remainder give a multiple of 5? Because a = 5p + r and b = 5q + r give a − b = 5(p − q). One extra line, and it makes the proof watertight."}
];

const WORDS = [
 {n:11, m:3, lvl:"standard", q:"Two diagonally opposite corner squares are cut from an 8 × 8 chessboard.<br><br><strong>(a)</strong> How many dark and how many light squares are left? <span class='num'>[1]</span><br><strong>(b)</strong> Explain why any number of dominoes covers equal numbers of dark and light squares. <span class='num'>[1]</span><br><strong>(c)</strong> Hence show that 31 dominoes cannot cover the board. <span class='num'>[1]</span>",
  hints:["A full board has 32 of each colour. What colour are two opposite corners?",
         "Where does a domino sit? Are its two squares ever the same colour?",
         "31 dominoes cover how many of each colour? Compare with (a)."],
  sol:["(a) Opposite corners are the same colour, so one colour has <strong>30</strong> left and the other <strong>32</strong>.",
       "(b) A domino covers two neighbouring squares, and neighbours on a chessboard are always opposite colours: one dark and one light each.",
       "(c) 31 dominoes cover 31 dark and 31 light, but the board has 30 of one colour. <strong>Impossible.</strong>",
       "The proof never mentions a single attempt at tiling. That's what makes it a proof."]},

 {n:12, m:3, lvl:"standard", q:"Five points are placed anywhere inside a square of side 2.<br><br><strong>(a)</strong> Describe how to divide the square into 4 regions. <span class='num'>[1]</span><br><strong>(b)</strong> Explain why two of the points lie in the same region. <span class='num'>[1]</span><br><strong>(c)</strong> Hence show that two points are at most √2 apart. <span class='num'>[1]</span>",
  hints:["Four equal smaller squares.",
         "Five points, four regions.",
         "What's the longest distance between two points inside a 1 × 1 square?"],
  sol:["(a) Join the midpoints of opposite sides, making four <strong>1 × 1 squares</strong>.",
       "(b) Five points in four squares: by pigeonhole, some square holds two (points on a shared edge can go in either).",
       "(c) The farthest apart two points in a 1 × 1 square can be is the diagonal, √(1² + 1²) = <strong>√2</strong>.",
       "Notice you can't do it with fewer regions of the right size, and you can't say which two points — pigeonhole never tells you."]},

 {n:13, m:3, lvl:"standard", q:"At a party, everyone counts how many people they shook hands with.<br><br><strong>(a)</strong> Explain why the sum of everyone's counts is always even. <span class='num'>[1]</span><br><strong>(b)</strong> Could each of 9 people shake hands with exactly 3 others? <span class='num'>[1]</span><br><strong>(c)</strong> Could each of 10 people shake hands with exactly 3 others? Describe how, or explain why not. <span class='num'>[1]</span>",
  hints:["Each handshake involves two people. How much does one handshake add to the sum?",
         "9 × 3 = ?",
         "Parity allows 10 × 3 = 30. Try 10 people in a circle: each shakes with both neighbours, and one more person each."],
  sol:["(a) Each handshake adds 1 to two people's counts, so 2 to the sum. The sum is 2 × (number of handshakes): even.",
       "(b) 9 × 3 = 27 is odd. <strong>No.</strong>",
       "(c) <strong>Yes.</strong> Sit them in a circle: each shakes hands with the two neighbours and the person directly opposite. That's 3 each, 15 handshakes.",
       "Parity can only rule things out. In (c) it allowed the answer, so the only way to finish was to build an example."]},

 {n:14, m:3, lvl:"hard", q:"Six different numbers are chosen from 1, 2, 3, …, 10.<br><br><strong>(a)</strong> Split 1 to 10 into five pairs that each add to 11. <span class='num'>[1]</span><br><strong>(b)</strong> Prove that two of the chosen numbers add to 11. <span class='num'>[1]</span><br><strong>(c)</strong> Show that choosing only five numbers is not enough. <span class='num'>[1]</span>",
  hints:["1 goes with 10.",
         "Treat each pair as a box.",
         "Find five numbers with no two adding to 11 — one from each pair."],
  sol:["(a) <strong>{1, 10}, {2, 9}, {3, 8}, {4, 7}, {5, 6}</strong>.",
       "(b) Six numbers in five boxes: some box gets both of its numbers, and those two add to 11.",
       "(c) <strong>1, 2, 3, 4, 5</strong> — one from each pair — has no two adding to 11.",
       "(c) is what turns 'six works' into 'six is the smallest that works'. Olympiad questions about 'the least number' always need both halves."]},

 {n:15, m:3, lvl:"hard", q:"Seven coins lie heads up on a table.<br><br><strong>(a)</strong> A move turns over exactly <strong>two</strong> coins. Explain how a move can change the number of heads. <span class='num'>[1]</span><br><strong>(b)</strong> Prove that with these moves you can never get all seven tails. <span class='num'>[1]</span><br><strong>(c)</strong> Now a move turns over exactly <strong>three</strong> coins. Show how to get all tails in three moves. <span class='num'>[1]</span>",
  hints:["Two heads turned, two tails turned, or one of each. What happens to the head count in each case?",
         "What stays the same about the number of heads?",
         "Turning three coins changes the count by an odd amount, so parity is no longer stuck. Aim for 6, then 3, then 0."],
  sol:["(a) By −2 (two heads), +2 (two tails) or 0 (one of each).",
       "(b) The number of heads always changes by an even amount, so it stays odd. It starts at 7; 0 is even. <strong>Never.</strong>",
       "(c) Turn 2 heads and 1 tail: 7 → 6. Turn 3 heads: 6 → 3. Turn 3 heads: 3 → <strong>0</strong>.",
       "Same question, one rule changed, opposite answer — because the invariant disappeared. When an invariant proof stops working, look for a construction instead."]}
];
'''

TOOLS_JS = r'''
/* ---------------- the pigeonholes ---------------- */
let hTarget=null, curHPuzzle=null;
function drawHoles(){
  const n=+document.getElementById('hn').value, k=+document.getElementById('hk').value;
  document.getElementById('hn-v').textContent=n; document.getElementById('hk-v').textContent=k;
  const base=Math.floor(k/n), extra=k%n, maxv=Math.ceil(k/n);
  const counts=Array.from({length:n},(_,i)=>base+(i<extra?1:0));
  const bw=Math.min(640/n, 90), ox=(700-bw*n)/2, top=20, H=200;
  const per=Math.max(maxv,1), dot=Math.min(bw*0.32, (H-20)/per*0.42, 14);
  let g='';
  counts.forEach((c,i)=>{
    const x=ox+i*bw;
    const full = c===maxv && k>n;
    g+=`<rect x="${x+4}" y="${top}" width="${bw-8}" height="${H}" rx="8" fill="${full?'var(--rt-tint)':'var(--paper)'}" stroke="${full?'var(--rt)':'var(--line)'}" stroke-width="2"/>`;
    for(let j=0;j<c;j++){
      const cy=top+H-14-j*(dot*2.2);
      if(cy<top+8){ g+=`<text x="${x+bw/2}" y="${top+16}" text-anchor="middle" font-family="var(--mono)" font-size="11" fill="var(--ink-soft)">…</text>`; break; }
      g+=`<circle cx="${x+bw/2}" cy="${cy.toFixed(1)}" r="${dot.toFixed(1)}" fill="var(--pm)"/>`;
    }
    g+=`<text x="${x+bw/2}" y="${top+H+20}" text-anchor="middle" font-family="var(--mono)" font-size="13" font-weight="700" fill="var(--ink)">${c}</text>`;
  });
  document.getElementById('hStage').innerHTML=g;
  document.getElementById('h-max').textContent=maxv;
  document.getElementById('h-maxs').textContent=`⌈${k} ÷ ${n}⌉`;
  const less=Math.ceil((k-1)/n);
  document.getElementById('h-less').textContent = k>1 ? `${less}` : '—';
  const t=maxv+1;
  document.getElementById('h-force').textContent=`${t} needs ${n*(t-1)+1}`;
  const pill=document.getElementById('h-pill'), note=document.getElementById('h-note');
  if(hTarget){
    const T=hTarget; pill.className='pill up'; pill.textContent='Puzzle running';
    if(n!==T.n){ note.textContent=`Set the boxes to ${T.n} first.`; return; }
    if(k===T.k){
      hTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('hQuiz'); box.classList.add('on');
      box.innerHTML=`<strong>${k}.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="hAgain">Another one</button></div>`;
      document.getElementById('hAgain').addEventListener('click', ()=>document.getElementById('hPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Worst case: everything spread as evenly as possible. Then one more.';
    }else note.textContent = maxv>=T.t ? `${k} guarantees ${T.t} — but is it the smallest that does? Try one fewer.` : `${k} only guarantees ${maxv}. Not enough.`;
  }else{
    pill.className='pill go'; pill.textContent='Spreading';
    note.textContent='Guarantee questions are answered by the worst case, plus one.';
  }
}
const H_PUZZLES=[
 {n:5, t:2, k:6, txt:'socks in 5 colours: how many guarantee a matching pair?', more:'Worst case one of each colour (5), then one more.'},
 {n:4, t:3, k:9, txt:'socks in 4 colours: how many guarantee three of the same colour?', more:'Worst case two of each (8), then one more.'},
 {n:12, t:2, k:13, txt:'how many people guarantee two share a birth month?', more:'One per month is 12; the 13th must double up.'},
 {n:7, t:4, k:22, txt:'how many people guarantee four were born on the same day of the week?', more:'Three per day is 21; the 22nd makes four.'},
 {n:10, t:3, k:21, txt:'how many whole numbers guarantee three with the same last digit?', more:'10 possible last digits, two each is 20, so 21.'},
 {n:5, t:4, k:16, txt:'a bag of sweets in 5 flavours: how many guarantee four of one flavour?', more:'5 × 3 + 1 = 16.'}
];
['hn','hk'].forEach(id=>document.getElementById(id).addEventListener('input', drawHoles));
document.getElementById('hPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*H_PUZZLES.length);
  if(curHPuzzle===i) i=(i+1)%H_PUZZLES.length;
  curHPuzzle=i; hTarget=H_PUZZLES[i];
  document.getElementById('hk').value=1;   /* start from an unsolved state */
  const T=hTarget, box=document.getElementById('hQuiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> ${T.txt.charAt(0).toUpperCase()+T.txt.slice(1)} Set the boxes to ${T.n}, then set the pigeons to the <strong>smallest</strong> number that guarantees it.`;
  drawHoles();
});

/* ---------------- the domino board ---------------- */
let blTarget=null, curBlPuzzle=null, removed=new Set();
function boardN(){ return +document.getElementById('bsz').value; }
function tilingExists(n, rem){
  const cells=[]; const id={};
  for(let r=0;r<n;r++) for(let c=0;c<n;c++){ const k=r+','+c; if(!rem.has(k)){ id[k]=cells.length; cells.push([r,c]); } }
  const dark=cells.filter(([r,c])=>(r+c)%2===0), light=cells.filter(([r,c])=>(r+c)%2===1);
  if(dark.length!==light.length) return false;
  const match={};
  function tryCell(cell, seen){
    const [r,c]=cell;
    for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){
      const k=(r+dr)+','+(c+dc);
      if(!(k in id) || seen.has(k)) continue;
      seen.add(k);
      if(!(k in match) || tryCell(match[k], seen)){ match[k]=cell; return true; }
    }
    return false;
  }
  for(const cell of dark){ if(!tryCell(cell, new Set())) return false; }
  return true;
}
function drawBoard(){
  const n=boardN();
  [...removed].forEach(k=>{ const [r,c]=k.split(',').map(Number); if(r>=n||c>=n) removed.delete(k); });
  const u=Math.min(300/n, 44), ox=(700-n*u)/2, oy=(330-n*u)/2;
  let g='';
  for(let r=0;r<n;r++) for(let c=0;c<n;c++){
    const k=r+','+c, gone=removed.has(k), dark=(r+c)%2===0;
    g+=`<rect class="sq" data-k="${k}" x="${(ox+c*u).toFixed(1)}" y="${(oy+r*u).toFixed(1)}" width="${(u-1).toFixed(1)}" height="${(u-1).toFixed(1)}" fill="${gone?'var(--card)':(dark?'var(--pm)':'var(--pm-tint)')}" stroke="${gone?'var(--line)':'none'}" stroke-dasharray="${gone?'4 3':''}"/>`;
    if(gone) g+=`<text x="${(ox+c*u+u/2).toFixed(1)}" y="${(oy+r*u+u/2+5).toFixed(1)}" text-anchor="middle" font-family="var(--mono)" font-size="14" fill="var(--steel)" pointer-events="none">×</text>`;
  }
  document.getElementById('bStageL').innerHTML=g;
  let d=0,l=0; for(let r=0;r<n;r++) for(let c=0;c<n;c++){ if(removed.has(r+','+c)) continue; ((r+c)%2===0)?d++:l++; }
  const ok=tilingExists(n, removed);
  document.getElementById('bl-c').textContent=`${d} / ${l}`;
  document.getElementById('bl-cs').textContent=`${removed.size} square${removed.size===1?'':'s'} removed`;
  document.getElementById('bl-t').textContent = d===l ? 'balanced — passes' : 'unbalanced — impossible';
  document.getElementById('bl-m').textContent = ok ? 'yes' : 'no';
  document.getElementById('bl-ms').textContent = (d===l && !ok) ? 'balanced, and still impossible' : 'found by search';
  const pill=document.getElementById('bl-pill'), note=document.getElementById('bl-note');
  if(blTarget){
    const T=blTarget; pill.className='pill up'; pill.textContent='Puzzle running';
    if(n!==T.n){ note.textContent=`Choose the ${T.n} × ${T.n} board first.`; return; }
    if(T.check(removed, d, l, ok)){
      blTarget=null; S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('blQuiz'); box.classList.add('on');
      box.innerHTML=`<strong>Done.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="blAgain">Another one</button></div>`;
      document.getElementById('blAgain').addEventListener('click', ()=>document.getElementById('blPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Colours first. If they balance and it still fails, look for a cut-off square.';
    }else note.textContent=`${removed.size} removed, colours ${d} / ${l}, tiling ${ok?'exists':'impossible'}.`;
  }else{
    pill.className='pill up'; pill.textContent='Tiling';
    note.textContent='Remove two opposite corners of an 8 × 8 and see what the colours say.';
  }
}
document.getElementById('bStageL').addEventListener('click', e=>{
  const s=e.target.closest('[data-k]'); if(!s) return;
  const k=s.dataset.k; if(removed.has(k)) removed.delete(k); else removed.add(k);
  drawBoard();
});
document.getElementById('bsz').addEventListener('change', ()=>{ removed.clear(); drawBoard(); });
document.getElementById('bReset').addEventListener('click', ()=>{ removed.clear(); drawBoard(); });
const BL_PUZZLES=[
 {n:6, txt:'Remove exactly 2 squares so the board <strong>cannot</strong> be tiled.', check:(R,d,l,ok)=>R.size===2&&!ok, more:'Any two squares of the same colour leave 16 of one and 18 of the other.'},
 {n:6, txt:'Remove exactly 2 squares so the board <strong>can</strong> still be tiled.', check:(R,d,l,ok)=>R.size===2&&ok, more:'One dark and one light. (On a full board, removing one of each colour always leaves a tiling — a theorem worth looking up: Gomory\'s.)'},
 {n:5, txt:'A 5 × 5 board has 25 squares. Remove exactly 1 so the rest <strong>can</strong> be tiled.', check:(R,d,l,ok)=>R.size===1&&ok, more:'It has to be a square of the corner colour — there are 13 of those and 12 of the other.'},
 {n:5, txt:'On the 5 × 5, remove exactly 1 square so the rest <strong>cannot</strong> be tiled.', check:(R,d,l,ok)=>R.size===1&&!ok, more:'Removing a square of the minority colour leaves 13 against 11.'},
 {n:8, txt:'Remove the two <strong>opposite corners</strong> of the 8 × 8 board.', check:(R,d,l,ok)=>R.size===2&&((R.has('0,0')&&R.has('7,7'))||(R.has('0,7')&&R.has('7,0'))), more:'32 of one colour, 30 of the other: 31 dominoes can\'t do it. The search agrees.'},
 {n:4, txt:'Remove exactly 4 squares from the 4 × 4 so the colours still <strong>balance</strong> but it <strong>can\'t</strong> be tiled.', check:(R,d,l,ok)=>R.size===4&&d===l&&!ok, more:'Cutting off a corner (remove its two neighbours) and balancing elsewhere does it. Equal colours are necessary, not sufficient.'}
];
document.getElementById('blPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*BL_PUZZLES.length);
  if(curBlPuzzle===i) i=(i+1)%BL_PUZZLES.length;
  curBlPuzzle=i; blTarget=BL_PUZZLES[i];
  removed.clear();   /* start from an unsolved state */
  const box=document.getElementById('blQuiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> On the ${blTarget.n} × ${blTarget.n} board: ${blTarget.txt} Predict with colours before you click.`;
  drawBoard();
});
'''

BOOT = ['drawHoles()', 'drawBoard()']
