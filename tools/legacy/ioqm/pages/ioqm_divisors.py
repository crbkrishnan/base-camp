# -*- coding: utf-8 -*-
ID = 'ioqm-divisors'
SHORT_TITLE = 'What Divides What'
SUB = 'IOQM · Number theory I: divisibility rules, counting divisors, Euclid'
BLURB = ("Prove the divisibility rules instead of memorising them, then count a number's divisors without listing a single one. "
         "Test any number on the rule bench and build numbers with exactly the divisor count a puzzle demands.")
META_TOOL = 'divisor grid'
COLOURS = ('#1F5F70', '#E4EFF2', '#8A3B12', '#F7ECE4', '#5B3F8C', '#EEE9F6')
EYEBROW = 'IOQM Olympiad Prep · Number theory I'
H1 = 'What <i>Divides</i><br><em>What</em>'
LEDE = ("Olympiad number theory starts with one question asked a hundred ways: does this divide that? "
        "This page gives you the tests, the reason each test works, and the trick that counts every divisor of a number "
        "without writing a single one down.")
TARGET = ("You've been landing around <span class=\"num\">10 out of 15</span> at school. This page is out of <span class=\"num\">30</span>, "
          "and the honest targets are <span class=\"num\">21</span> on the first pass and <span class=\"num\">26</span> on the second. "
          "These are Olympiad questions, so they are harder than your school papers on purpose. No calculator — IOQM doesn't allow one.")
VIDEO_MIN = '~50 min total'
LESSON_MIN = '~40 min total'
NAV = [('bench', 'Rule bench'), ('videos', '6 videos'), ('lessons', '6 lessons'), ('grid', 'Divisor grid'),
       ('quick', 'Quick checks'), ('short', 'Short answers'), ('word', 'Word problems'), ('traps', 'Exam traps')]

EXTRA_CSS = r'''
.dchips{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px;padding:14px 16px}
.dchip{border:1px solid var(--line);border-radius:10px;padding:8px 10px;background:var(--paper)}
.dchip b{font-family:var(--mono);font-size:16px}
.dchip .why{font-family:var(--mono);font-size:11px;color:var(--ink-soft);margin-top:3px;line-height:1.35}
.dchip.yes{background:var(--ok-tint);border-color:var(--ok)}
.dchip.yes b{color:var(--ok)}
.dchip.no b{color:var(--no)}
#dnum{width:220px;font-size:17px}
.dgrids{display:flex;gap:14px;flex-wrap:wrap;padding:14px 16px}
.dgrids table{border-collapse:collapse;font-family:var(--mono);font-size:12.5px}
.dgrids td{border:1px solid var(--line);padding:5px 7px;text-align:right;background:var(--card);min-width:38px}
.dgrids td.hd{background:var(--paper);color:var(--ink-soft);font-size:11px}
.dgrids td.sq{background:var(--rt-tint);color:var(--rt);font-weight:700}
.dgrids .cap{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:4px}
'''

TOOL1_HTML = r'''
<section id="bench">
  <div class="panel">
    <div class="panel-top">
      <h2>The divisibility rule bench</h2>
      <p>Type any whole number. Every rule is applied the way you would apply it on paper — last digits, digit sum, alternating sum — and each verdict shows its evidence. Nothing here does a division you couldn't do in your head.</p>
    </div>
    <div class="ctrl">
      <label for="dnum">Number</label>
      <input id="dnum" type="text" inputmode="numeric" value="7524" aria-label="A whole number to test" maxlength="12">
    </div>
    <div class="dchips" id="dchips"></div>
    <div class="rows">
      <div class="cell f"><div class="lab">Digit sum</div><div class="val" id="b-ds">—</div><div class="sub">decides 3 and 9</div></div>
      <div class="cell d"><div class="lab">Alternating sum</div><div class="val" id="b-alt">—</div><div class="sub">from the right: + − + − … decides 11</div></div>
      <div class="cell p"><div class="lab">Last three digits</div><div class="val" id="b-l3">—</div><div class="sub">decide 2, 4 and 8</div></div>
      <div class="phasebar">
        <span class="pill go" id="b-pill">Testing</span>
        <span id="b-note">Change one digit and watch which verdicts flip — and which can't.</span>
        <span class="push"><button class="btn ghost" type="button" id="benchPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="benchQuiz"></div>
    </div>
  </div>
</section>
'''

TOOL2_HTML = r'''
<section id="grid">
  <div class="panel">
    <div class="panel-top">
      <h2>The divisor grid</h2>
      <p>Build a number out of 2s, 3s and 5s. Every divisor is one choice of how many 2s, how many 3s and how many 5s to keep — so the divisors fall into a grid, and counting them is just counting the cells. Ochre cells are the perfect squares.</p>
    </div>
    <div class="ctrl">
      <label for="ga">Power of 2</label><input id="ga" type="range" min="0" max="5" value="3" aria-label="Power of 2"><span class="num" id="ga-v">3</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="gb">Power of 3</label><input id="gb" type="range" min="0" max="4" value="2" aria-label="Power of 3"><span class="num" id="gb-v">2</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="gc">Power of 5</label><input id="gc" type="range" min="0" max="2" value="1" aria-label="Power of 5"><span class="num" id="gc-v">1</span>
    </div>
    <div class="dgrids" id="dgrids"></div>
    <div class="rows">
      <div class="cell f"><div class="lab">The number</div><div class="val" id="g-n">—</div><div class="sub" id="g-ns"></div></div>
      <div class="cell p"><div class="lab">Divisors</div><div class="val" id="g-d">—</div><div class="sub" id="g-ds"></div></div>
      <div class="cell d"><div class="lab">Square divisors</div><div class="val" id="g-sq">—</div><div class="sub">cells where every power is even</div></div>
      <div class="phasebar">
        <span class="pill up" id="g-pill">Building</span>
        <span id="g-note">Each slider adds a row, a column or a whole layer. That's where the +1 comes from.</span>
        <span class="push"><button class="btn ghost" type="button" id="gridPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="gridQuiz"></div>
    </div>
  </div>
</section>
'''

TRAPS = [
 ("Gluing two rules together when the numbers share a factor",
  "Divisible by 4 and by 6 does <strong>not</strong> mean divisible by 24 — 12 is divisible by both and isn't. You can only combine rules for numbers with no common factor: 24 = <strong>3 × 8</strong>, so test 3 and 8. Likewise 12 = 3 × 4 and 36 = 4 × 9, never 2 × 6 or 3 × 12."),
 ("Reading the alternating sum wrongly for 11",
  "Start from the <strong>units digit with a plus</strong>, then alternate. A result of 0 counts — 0 is a multiple of 11 — and so do 11, −11 and 22. Students who get 0 often write \"not divisible\" because nothing is left. It is divisible."),
 ("Forgetting the +1 when counting divisors",
  "72 = 2³ × 3² has <strong>(3+1)(2+1) = 12</strong> divisors, not 3 × 2 = 6. The +1 is the choice of taking <em>none</em> of that prime. Leave it out and you have forgotten that 1, 8 and 9 are divisors of 72."),
 ("Using the digit-sum test for 27",
  "The digit sum decides 3 and 9 and nothing else. 99 has digit sum 18, which is a multiple of 27's friend 9 — but 99 ÷ 27 is not whole. The test works because 10 leaves remainder 1 on division by 9; it leaves remainder 10 on division by 27, so the trick dies."),
 ("Reporting 0 as the HCF",
  "In the Euclidean algorithm you stop when a remainder hits 0, and the answer is the <strong>last non-zero remainder</strong>. If your final line is 34 = 2 × 17 + 0, the HCF is 17. Writing 0 throws away the whole calculation in the last second.")
]

DATA_JS = r'''
/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"Divisibility Rules for 2, 4, 5, and 25", ch:"Art of Problem Solving", url:"https://www.youtube.com/watch?v=S_VvZ0yIC-I",
  why:"Richard Rusczyk doesn't state the rules — he discovers them, by asking which part of a number 100 already divides. That 'why' is what lets you invent a rule for 8 or 125 in an exam.",
  task:"Before the video ends, pause and write a rule for 8 and a rule for 125 in the same style. Then test both on 7,000,125 and 3,416."},

 {t:"Divisibility Rules for 2, 3, 4, 5, 6, 7, 8, 9 & 10", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=uiSDZ3zB_d4",
  why:"A fast sweep of every rule in one place, with timestamps. Treat it as a checklist, not a lesson — the reasons come in lesson 1 below.",
  task:"Write each rule on one line of a card. Next to the 3 and 9 rules write 'because 10 = 9 + 1'. Next to the 2, 4, 8 rules write 'because 10, 100, 1000 are multiples'."},

 {t:"Divisibility by 11 Explained", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=nijj3y9upQU",
  why:"This one proves the alternating-sum rule rather than just using it — the key fact is that 10 is one less than 11. Q2 and Q12 lean on it.",
  task:"Test 918,082 and 123,456 for 11 by the alternating sum. You should find the first works and the second doesn't. Then write one sentence on why 100 is 'one more than a multiple of 11'."},

 {t:"Number of Whole Number Divisors", ch:"Math for Teachers", url:"https://www.youtube.com/watch?v=jkDqmDjRiYk",
  why:"The (a+1)(b+1) formula, built from prime factorisation. This is the single most-used idea on the page — Q3, Q7, Q9, Q14 and Q15 all need it.",
  task:"Count the divisors of 360, 1000 and 1024 using the formula. Answers: 24, 16, 11. If you got 10 for 1024, you forgot the +1."},

 {t:"The Euclidean Algorithm (Finding the GCD)", ch:"Math for Teachers", url:"https://www.youtube.com/watch?v=SR-jmdjzw-Y",
  why:"How to find the HCF of two big numbers when factorising them would take forever. IOQM likes numbers like 391 and 119 precisely because you can't spot their factors.",
  task:"Find gcd(1071, 462) by the algorithm. You should go 1071 → 462 → 147 → 21 and stop at 21. Write each line as a = q × b + r."},

 {t:"Product of Divisors", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=aZmvcZo7K5o",
  why:"A short extension: divisors pair up to multiply to n, so their product is n raised to half the divisor count. It's a classic Olympiad one-liner and a good test of whether lesson 5 landed.",
  task:"Find the product of all divisors of 12 two ways: by multiplying them out, and by the formula 12^(6/2). Both should give 1728."}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"Why the rules work, not just what they are", len:"7 min",
  body:`<p>Every divisibility rule comes from one idea: split the number into a part you <em>know</em> is divisible, and a part you still have to check.</p>
        <p><strong>Last-digit rules.</strong> 10 is a multiple of 2 and 5, so in 7,524 the 7,520 part is automatically divisible by 2 and 5 — only the last digit matters. 100 is a multiple of 4 (and 25), so only the last <em>two</em> digits matter. 1000 is a multiple of 8 (and 125), so only the last <em>three</em> matter.</p>
        <div class="eqline">7,524 = 7,500 + 24 &nbsp;→&nbsp; 24 ÷ 4 = 6, so 7,524 is divisible by 4</div>
        <p><strong>Digit-sum rules.</strong> 10 = 9 + 1, 100 = 99 + 1, 1000 = 999 + 1. So each digit is "worth" one more than a multiple of 9 in its place:</p>
        <div class="eqline">7,524 = 7×999 + 5×99 + 2×9 &nbsp;+&nbsp; (7 + 5 + 2 + 4)</div>
        <p>The first chunk is always a multiple of 9 (and 3). What's left is the <span class="frtxt">digit sum</span>. So a number and its digit sum leave the <strong>same remainder</strong> when divided by 9 — which is more than the rule says, and it's the version Olympiad questions use.</p>`,
  demo:`<strong>Do this:</strong> without dividing, find the remainder when 52,817 is divided by 9. (Digit sum 23, and 23 leaves 5.) Then check by dividing on paper.`,
  cliff:`10 is one more than 9. But it's also one <em>less</em> than 11. What does that do?`},

 {t:"Eleven, and gluing rules together", len:"7 min",
  body:`<p>10 = 11 − 1, so 10 behaves like −1 when you divide by 11. Then 100 behaves like (−1)² = +1, 1000 like −1, and so on. That gives the <span class="detxt">alternating sum</span>, starting from the units digit with a plus:</p>
        <div class="eqline">918,082 → 2 − 8 + 0 − 8 + 1 − 9 = −22 &nbsp;→ multiple of 11, so 918,082 is divisible by 11</div>
        <p>A result of 0, 11, −11, 22… all count.</p>
        <p><strong>Gluing rules.</strong> To test 12, test 3 and 4. To test 36, test 4 and 9. To test 72, test 8 and 9. To test 99, test 9 and 11. The rule: the two pieces must have <strong>no common factor</strong>. 4 and 6 share a 2, so "divisible by 4 and 6" only guarantees 12, not 24.</p>
        <table class="data"><tr><th>To test</th><th>Test these</th><th>Not these</th></tr>
        <tr><td>12</td><td>3 and 4</td><td>2 and 6</td></tr>
        <tr><td>24</td><td>3 and 8</td><td>4 and 6</td></tr>
        <tr><td>36</td><td>4 and 9</td><td>3 and 12</td></tr>
        <tr><td>99</td><td>9 and 11</td><td>3 and 33</td></tr></table>`,
  demo:`<strong>Do this:</strong> say whether 5,214 is divisible by 66. (66 = 6 × 11, and 6 and 11 share nothing. Check 2, 3 and 11.) It is: 5,214 = 66 × 79.`,
  cliff:`Now turn it round. The number is 7a2b, it's divisible by 36, and you don't know a or b.`},

 {t:"Missing-digit problems", len:"6 min",
  body:`<p>This is the most common way IOQM uses divisibility. A number has blanks; it is divisible by something; find the blanks. The method is always the same: <strong>use the last-digit rule first</strong>, because it pins down the end, then the digit-sum or alternating rule for the rest.</p>
        <p><strong>Example.</strong> The four-digit number 7a2b is divisible by 36. Find every possibility.</p>
        <ol>
          <li>36 = 4 × 9, so test 4 and 9.</li>
          <li><span class="pctxt">4</span>: the last two digits "2b" must be divisible by 4: 20, 24 or 28. So <strong>b = 0, 4 or 8</strong>.</li>
          <li><span class="frtxt">9</span>: 7 + a + 2 + b = 9 + a + b must be a multiple of 9, so <strong>a + b = 0, 9 or 18</strong>.</li>
          <li>b = 0 → a = 0 or 9. &nbsp; b = 4 → a = 5. &nbsp; b = 8 → a = 1.</li>
        </ol>
        <div class="eqline">7020, 7920, 7524, 7128 &nbsp;— four numbers</div>
        <p>The trap is stopping at the first answer. "Find all" means every case, and a + b = 0 is a case.</p>`,
  demo:`<strong>Do this:</strong> find every digit d that makes 48d6 divisible by 12. (4: "d6" ÷ 4 means d is odd. 3: 18 + d is a multiple of 3. Both: d = 3 or 9.)`,
  cliff:`You can now test whether 6 divides a number. Next: how many numbers divide it?`},

 {t:"Counting divisors without listing them", len:"7 min",
  body:`<p>Take 72 = 2³ × 3². Every divisor of 72 is made of some 2s and some 3s — and nothing else. So to build a divisor you make two choices:</p>
        <ul><li>how many 2s: 0, 1, 2 or 3 — that's <strong>4 choices</strong></li>
            <li>how many 3s: 0, 1 or 2 — that's <strong>3 choices</strong></li></ul>
        <p>Every pair of choices gives a different divisor, so there are 4 × 3 = <strong>12</strong>. In general:</p>
        <div class="eqline">n = p<sup>a</sup> × q<sup>b</sup> × r<sup>c</sup> &nbsp;→&nbsp; number of divisors = (a+1)(b+1)(c+1)</div>
        <p>The +1 is the choice of taking <em>none</em> of that prime. The divisor grid below draws exactly this: one column per choice of 2s, one row per choice of 3s.</p>
        <p><strong>Running it backwards.</strong> Which numbers have exactly 6 divisors? 6 = 6 or 3 × 2, so n = p⁵ or p² × q. The smallest is 2² × 3 = <strong>12</strong>. To make a number small, give the <em>biggest</em> power to the <em>smallest</em> prime.</p>`,
  demo:`<strong>Do this:</strong> count the divisors of 360 = 2³ × 3² × 5. You should get 24. Then list the divisors of 18 = 2 × 3² on a 2 × 3 grid, one row per power of 3.`,
  cliff:`Almost every number has an even number of divisors. Some don't. Which ones — and why would a school corridor care?`},

 {t:"Odd divisor counts, and the locker problem", len:"6 min",
  body:`<p>Divisors come in pairs that multiply to n: for 36 they are 1×36, 2×18, 3×12, 4×9 — and 6×6. The last "pair" is one number. So:</p>
        <div class="eqline">n has an odd number of divisors &nbsp;⟺&nbsp; n is a perfect square</div>
        <p>In formula terms: (a+1)(b+1)… is odd only if every a, b, … is even — which is exactly what makes n a square.</p>
        <p><strong>The locker problem.</strong> 100 closed lockers; student 1 opens every locker, student 2 toggles every 2nd, student 3 every 3rd, … student 100 toggles locker 100. Locker n is toggled once for every divisor of n. It ends <em>open</em> if it's toggled an odd number of times — so the open lockers are the squares: 1, 4, 9, …, 100. Ten lockers.</p>
        <p><strong>Product of divisors.</strong> The pairs each multiply to n, and there are d/2 pairs, so the product of all divisors is <span class="pctxt">n<sup>d/2</sup></span>. For 12: 12³ = 1728.</p>`,
  demo:`<strong>Do this:</strong> with 30 lockers, which are open at the end? Write the list, then check locker 12 by hand — its divisors 1, 2, 3, 4, 6, 12 toggle it six times, so it's shut.`,
  cliff:`Two big numbers, no idea what their factors are, and you need the highest common factor. Factorising won't work.`},

 {t:"Euclid's algorithm", len:"7 min",
  body:`<p>If d divides both a and b, it also divides a − b, and a − 2b, and any a − qb. In particular it divides the <strong>remainder</strong> r when a is divided by b. So:</p>
        <div class="eqline">gcd(a, b) = gcd(b, r) &nbsp;&nbsp; where a = q × b + r</div>
        <p>Keep replacing the pair with a smaller pair until a remainder is 0. The last non-zero remainder is the HCF.</p>
        <div class="eqline">391 = 3 × 119 + 34<br>119 = 3 × 34 + 17<br>&nbsp;34 = 2 × 17 + 0 &nbsp;&nbsp;→&nbsp; gcd(391, 119) = <b>17</b></div>
        <p>You never needed to know that 391 = 17 × 23. That's the point.</p>
        <p>Pair it with the fact from the school page: <strong>gcd × lcm = a × b</strong>. So lcm(391, 119) = 391 × 119 ÷ 17 = 23 × 119 = 2737.</p>`,
  demo:`<strong>Do this:</strong> find gcd(252, 198) by Euclid (252 → 198 → 54 → 36 → 18), then check it by prime factorisation.`,
  cliff:`That's the lessons. Q14 asks for the smallest number with exactly twelve divisors, and Q15 asks how many divisors of 10,800 are perfect squares. Go and lose to them, then take them apart.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"Which of these is divisible by <strong>9</strong>?",
  o:["4,517","2,349","6,283","7,401"], a:1,
  why:"Digit sums: 17, 18, 19 and 12. Only 18 is a multiple of 9, so 2,349 = 9 × 261. The trap is 7,401: its digit sum 12 makes it divisible by 3, but not by 9."},
 {n:2, lvl:"standard", q:"Which of these is divisible by <strong>11</strong>?",
  o:["2,817","3,729","4,375","9,182"], a:1,
  why:"Alternating sums from the right: 2,817 → 7−1+8−2 = 12; 3,729 → 9−2+7−3 = 11 ✓; 4,375 → 5−7+3−4 = −3; 9,182 → 2−8+1−9 = −14. Only 11 is a multiple of 11, and 3,729 = 11 × 339."},
 {n:3, lvl:"standard", q:"How many positive divisors does <span class='num'>72</span> have?",
  o:["8","10","12","36"], a:2,
  why:"72 = 2³ × 3², so (3+1)(2+1) = 12. Answering 6 or 8 usually means a missing +1. Option D is 72 ÷ 2, which is not a count of anything."},
 {n:4, lvl:"standard", q:"Which of these has an <strong>odd</strong> number of divisors?",
  o:["48","64","72","96"], a:1,
  why:"Only perfect squares have an odd number of divisors, because only then does a divisor pair with itself (8 × 8). 64 = 2⁶ has 7 divisors; the others have 10, 12 and 12."},
 {n:5, lvl:"trap", q:"A number is divisible by both <span class='num'>4</span> and <span class='num'>6</span>. Which statement is true?",
  o:["It must be divisible by 24, because 4 × 6 = 24","It must be divisible by 12, but not necessarily by 24","It must be divisible by 10","It must be divisible by 8"], a:1,
  why:"4 and 6 share a factor 2, so multiplying them double-counts it. What's guaranteed is lcm(4, 6) = 12. The number 12 itself is divisible by 4 and 6 and not by 24 — one counterexample kills option A."}
];

const SHORTS = [
 {n:6, m:2, lvl:"warm-up", q:"<strong>(a)</strong> Find the digit d that makes <span class='num'>47d2</span> divisible by 9. <span class='num'>[1]</span><br><strong>(b)</strong> Is the number you found also divisible by 4? Give a reason. <span class='num'>[1]</span>",
  scheme:["(a) 4 + 7 + d + 2 = 13 + d must be 9 or 18, so <strong>d = 5</strong> (the number is 4752) <span class='num'>[1]</span>",
          "(b) <strong>Yes</strong> — its last two digits 52 = 4 × 13 <span class='num'>[1]</span>"],
  tip:"d is a single digit, so 13 + d can only be 18 — it can't reach 27. Saying 'd = 5 or 14' loses nothing in (a), but it shows you forgot d is a digit."},
 {n:7, m:2, lvl:"standard", q:"Write <span class='num'>360</span> as a product of prime powers, and hence find how many positive divisors it has.",
  scheme:["360 = 2³ × 3² × 5 <span class='num'>[1]</span>",
          "(3+1)(2+1)(1+1) = <strong>24</strong> <span class='num'>[1]</span>"],
  tip:"The 5 is 5¹, so it contributes (1+1) = 2, not 1. A 5 with no visible power is where the +1 most often goes missing."},
 {n:8, m:2, lvl:"standard", q:"Use the Euclidean algorithm to find the highest common factor of <span class='num'>391</span> and <span class='num'>119</span>. Show each line.",
  scheme:["391 = 3 × 119 + 34 and 119 = 3 × 34 + 17 <span class='num'>[1]</span>",
          "34 = 2 × 17 + 0, so the HCF is <strong>17</strong> <span class='num'>[1]</span>"],
  tip:"Check: 391 = 17 × 23 and 119 = 17 × 7. Neither 23 nor 7 shares a factor with the other, so 17 really is the highest."},
 {n:9, m:2, lvl:"standard", q:"<strong>(a)</strong> Find the smallest positive whole number with exactly <span class='num'>6</span> divisors. <span class='num'>[1]</span><br><strong>(b)</strong> List its divisors. <span class='num'>[1]</span>",
  scheme:["(a) 6 = 6 or 3 × 2, so n = p⁵ or p² × q; the smallest is 2² × 3 = <strong>12</strong> (2⁵ = 32 is bigger) <span class='num'>[1]</span>",
          "(b) <strong>1, 2, 3, 4, 6, 12</strong> <span class='num'>[1]</span>"],
  tip:"Give the bigger power to the smaller prime: 2² × 3 = 12 beats 3² × 2 = 18."},
 {n:10, m:2, lvl:"hard", q:"Explain why every six-digit number of the form <span class='num'>abcabc</span> (for example 418,418) is divisible by <span class='num'>7</span>, <span class='num'>11</span> and <span class='num'>13</span>.",
  scheme:["abcabc = abc × 1000 + abc = abc × <strong>1001</strong> <span class='num'>[1]</span>",
          "1001 = <strong>7 × 11 × 13</strong>, so all three divide it <span class='num'>[1]</span>"],
  tip:"This is a proof question, so an example (418,418 ÷ 7 = 59,774) earns nothing on its own. The mark is for writing the number as abc × 1001."}
];

const WORDS = [
 {n:11, m:3, lvl:"standard", q:"A corridor has <span class='num'>50</span> closed lockers, numbered 1 to 50. Student 1 opens every locker. Student 2 toggles (opens if closed, closes if open) every 2nd locker, student 3 every 3rd locker, and so on up to student 50.<br><br><strong>(a)</strong> How many times is locker 36 toggled? <span class='num'>[1]</span><br><strong>(b)</strong> Is locker 36 open or closed at the end? <span class='num'>[1]</span><br><strong>(c)</strong> How many lockers are open at the end? <span class='num'>[1]</span>",
  hints:["Student k touches locker 36 exactly when k divides 36.",
         "Each toggle flips the locker. Starting closed, an odd number of flips leaves it open.",
         "Which numbers have an odd number of divisors? List those up to 50."],
  sol:["(a) Once for each divisor of 36 = 2² × 3²: (2+1)(2+1) = <strong>9 times</strong>.",
       "(b) 9 is odd, so locker 36 ends <strong>open</strong>.",
       "(c) A locker ends open exactly when it has an odd number of divisors, i.e. it is a perfect square: 1, 4, 9, 16, 25, 36, 49 — <strong>7 lockers</strong>.",
       "The whole problem is one fact in disguise. Spotting the disguise is the skill IOQM is testing."]},

 {n:12, m:3, lvl:"standard", q:"The four-digit number <span class='num'>7a2b</span> is divisible by <span class='num'>36</span>, where a and b are digits.<br><br><strong>(a)</strong> Explain why b must be 0, 4 or 8. <span class='num'>[1]</span><br><strong>(b)</strong> Explain why a + b must be 0, 9 or 18. <span class='num'>[1]</span><br><strong>(c)</strong> Find all such numbers. <span class='num'>[1]</span>",
  hints:["36 = 4 × 9, and 4 and 9 share no factor, so test those two.",
         "For 4 you only need the last two digits, '2b'. For 9 you need the digit sum, 9 + a + b.",
         "Go through b = 0, 4, 8 one at a time. Remember a + b = 0 is possible."],
  sol:["(a) Divisible by 4 means the last two digits 2b are divisible by 4: 20, 24, 28 work and 22, 26 don't, so <strong>b ∈ {0, 4, 8}</strong>.",
       "(b) Divisible by 9 means 7 + a + 2 + b = 9 + a + b is a multiple of 9, so <strong>a + b ∈ {0, 9, 18}</strong>.",
       "(c) b = 0: a = 0 or 9; b = 4: a = 5; b = 8: a = 1. The numbers are <strong>7020, 7128, 7524 and 7920</strong>.",
       "Check one: 7524 ÷ 36 = 209. Most students find three and miss 7020, because a = 0 doesn't feel like a real answer."]},

 {n:13, m:3, lvl:"standard", q:"A rectangular floor measures <span class='num'>391 cm</span> by <span class='num'>119 cm</span>.<br><br><strong>(a)</strong> What is the largest square tile, in whole centimetres, that covers the floor exactly with no cutting? <span class='num'>[1]</span><br><strong>(b)</strong> How many of those tiles are needed? <span class='num'>[1]</span><br><strong>(c)</strong> Rectangular mats of size 391 cm by 119 cm, all the same way round, are laid to make the smallest possible square. How many mats are used? <span class='num'>[1]</span>",
  hints:["The tile side must divide both lengths. You want the biggest such number.",
         "For (b), work out how many tiles fit along each side and multiply.",
         "For (c), the square's side must be a multiple of both 391 and 119 — the smallest one."],
  sol:["(a) The HCF of 391 and 119, which Euclid gives as <strong>17 cm</strong>.",
       "(b) 391 ÷ 17 = 23 and 119 ÷ 17 = 7, so 23 × 7 = <strong>161 tiles</strong>.",
       "(c) The side is lcm(391, 119) = 391 × 119 ÷ 17 = 2737 cm. Mats needed: (2737 ÷ 391) × (2737 ÷ 119) = 7 × 23 = <strong>161 mats</strong>.",
       "The same 161 twice is not a coincidence: in both cases you are counting 23 × 7. Noticing that is a free check."]},

 {n:14, m:3, lvl:"hard", q:"<strong>(a)</strong> Write down every way of writing <span class='num'>12</span> as a product of whole numbers greater than 1, ignoring order. <span class='num'>[1]</span><br><strong>(b)</strong> Hence find the smallest positive whole number with exactly 12 divisors. <span class='num'>[1]</span><br><strong>(c)</strong> How many of that number's divisors are even? <span class='num'>[1]</span>",
  hints:["Each factorisation of 12 is a list of (power + 1) values. 12 = 4 × 3 means a number of the form p³ × q².",
         "For each shape, put the biggest power on 2, the next on 3, then 5. Compare the four candidates.",
         "An even divisor must contain at least one 2. How many choices does that leave for the power of 2?"],
  sol:["(a) <strong>12, 6 × 2, 4 × 3, 3 × 2 × 2</strong>.",
       "(b) The shapes give 2¹¹ = 2048, 2⁵ × 3 = 96, 2³ × 3² = 72 and 2² × 3 × 5 = 60. The smallest is <strong>60</strong>.",
       "(c) 60 = 2² × 3 × 5. An even divisor takes 1 or 2 twos (2 choices), then 0 or 1 threes and 0 or 1 fives: 2 × 2 × 2 = <strong>8</strong>.",
       "Check by listing: 2, 4, 6, 10, 12, 20, 30, 60. The lesson: more small primes beats bigger powers — 60 uses three primes and wins."]},

 {n:15, m:3, lvl:"hard", q:"Let <span class='num'>N = 2⁴ × 3³ × 5² = 10,800</span>.<br><br><strong>(a)</strong> How many positive divisors does N have? <span class='num'>[1]</span><br><strong>(b)</strong> How many of them are perfect squares? <span class='num'>[1]</span><br><strong>(c)</strong> How many of them are multiples of 10? <span class='num'>[1]</span>",
  hints:["Part (a) is the formula. Parts (b) and (c) are the same formula with fewer choices allowed for each power.",
         "A divisor is a square when every power in it is even. List the even powers available for 2, for 3 and for 5.",
         "A multiple of 10 needs at least one 2 and at least one 5. Count the allowed powers of each prime."],
  sol:["(a) (4+1)(3+1)(2+1) = <strong>60</strong>.",
       "(b) Powers of 2: 0, 2, 4 (3 choices); of 3: 0, 2 (2); of 5: 0, 2 (2). So 3 × 2 × 2 = <strong>12</strong>.",
       "(c) Powers of 2: 1–4 (4 choices); of 3: 0–3 (4); of 5: 1–2 (2). So 4 × 4 × 2 = <strong>32</strong>.",
       "This 'count the choices for each exponent' move is the whole of Olympiad divisor counting. Once you see it, the variations (odd divisors, cube divisors, divisors of N² …) are all one line."]}
];
'''

TOOLS_JS = r'''
/* ---------------- the divisibility rule bench ---------------- */
function cleanDigits(s){ return (s||'').replace(/[^0-9]/g,'').replace(/^0+(?=\d)/,'').slice(0,12); }
function benchFacts(str){
  const d = str.split('').map(Number);
  const ds = d.reduce((a,b)=>a+b,0);
  let alt = 0; for(let i=0;i<d.length;i++){ alt += (i%2===0?1:-1)*d[d.length-1-i]; }
  const last = k => parseInt(str.slice(-k),10);
  return {ds, alt, l1:last(1), l2:last(2), l3:last(3)};
}
function divides(str, k){ return (BigInt(str) % BigInt(k)) === 0n; }
function renderBench(){
  const inp = document.getElementById('dnum');
  const str = cleanDigits(inp.value) || '0';
  const F = benchFacts(str);
  const ok = k => divides(str,k);
  const tick = b => b ? '✓' : '✗';
  const rules = [
    [2,  `last digit ${F.l1} is ${F.l1%2===0?'even':'odd'}`],
    [3,  `digit sum ${F.ds} ${F.ds%3===0?'is':'is not'} a multiple of 3`],
    [4,  `last two digits ${String(F.l2).padStart(Math.min(2,str.length),'0')} ${F.l2%4===0?'÷ 4 works':'÷ 4 fails'}`],
    [5,  `last digit is ${F.l1}`],
    [6,  `2 ${tick(ok(2))} and 3 ${tick(ok(3))}`],
    [8,  `last three digits ${String(F.l3).padStart(Math.min(3,str.length),'0')} ${F.l3%8===0?'÷ 8 works':'÷ 8 fails'}`],
    [9,  `digit sum ${F.ds} ${F.ds%9===0?'is':'is not'} a multiple of 9`],
    [10, `last digit is ${F.l1}`],
    [11, `alternating sum ${F.alt} ${F.alt%11===0?'is':'is not'} a multiple of 11`],
    [12, `3 ${tick(ok(3))} and 4 ${tick(ok(4))}`],
    [36, `4 ${tick(ok(4))} and 9 ${tick(ok(9))}`],
    [99, `9 ${tick(ok(9))} and 11 ${tick(ok(11))}`]
  ];
  document.getElementById('dchips').innerHTML = rules.map(([k,why])=>{
    const y = ok(k);
    return `<div class="dchip ${y?'yes':'no'}"><b>÷ ${k} ${y?'✓':'✗'}</b><div class="why">${why}</div></div>`;
  }).join('');
  document.getElementById('b-ds').textContent = F.ds;
  document.getElementById('b-alt').textContent = F.alt;
  document.getElementById('b-l3').textContent = str.slice(-3);

  const pill = document.getElementById('b-pill'), note = document.getElementById('b-note');
  if(benchTarget){
    const T = benchTarget;
    const fits = str.length===T.p.length && T.p.split('').every((c,i)=>c==='*' || c===str[i]);
    pill.className='pill up'; pill.textContent='Puzzle running';
    if(!fits){ note.textContent = `Your number must look like ${T.p} — same digits, with one digit where the * is.`; return; }
    const allOk = T.by.every(k=>ok(k));
    if(allOk){
      benchTarget = null;
      S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('benchQuiz');
      box.classList.add('on');
      box.innerHTML = `<strong>That works.</strong> ${str} is divisible by ${T.by.join(' and ')}. ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="benchAgain">Another one</button></div>`;
      document.getElementById('benchAgain').addEventListener('click', ()=>document.getElementById('benchPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Last-digit rules first, sum rules second. That order is the method.';
    }else{
      note.textContent = `${str} fits the pattern but fails ÷ ${T.by.filter(k=>!ok(k)).join(' and ÷ ')}. Work out the digit first, then type it.`;
    }
  }else{
    pill.className='pill go'; pill.textContent='Testing';
    note.textContent='Change one digit and watch which verdicts flip — and which can\'t.';
  }
}
let benchTarget = null;
const BENCH_PUZZLES = [
 {p:'3*72', by:[9],  more:'The digit sum had to reach 18, so the missing digit is 6.'},
 {p:'52*4', by:[11], more:'4 − d + 2 − 5 = 1 − d had to be 0, so d = 1.'},
 {p:'48*6', by:[12], more:'d = 3 and d = 9 both work — 4 forces d odd, 3 forces 18 + d to be a multiple of 3.'},
 {p:'*1234', by:[9], more:'The leading digit can\'t be 0, and 10 + d = 18 gives d = 8.'},
 {p:'1*56', by:[24], more:'24 = 3 × 8. The 8-rule forces d even, the 3-rule forces 12 + d to be a multiple of 3, so d = 0 or 6.'},
 {p:'9*81', by:[11], more:'1 − 8 + d − 9 = d − 16 had to be a multiple of 11, so d = 5.'}
];
let curBPuzzle = null;
document.getElementById('dnum').addEventListener('input', renderBench);
document.getElementById('benchPuzzle').addEventListener('click', ()=>{
  let i = Math.floor(Math.random()*BENCH_PUZZLES.length);
  if(curBPuzzle===i) i=(i+1)%BENCH_PUZZLES.length;
  curBPuzzle=i; benchTarget = BENCH_PUZZLES[i];
  const box=document.getElementById('benchQuiz');
  box.classList.add('on');
  box.innerHTML = `<strong>Puzzle.</strong> Replace the * in <span class="num" style="font-size:17px">${benchTarget.p}</span> with a digit so the number is divisible by <strong>${benchTarget.by.join(' and ')}</strong>. Work it out first, then type the whole number into the box.`;
  renderBench();
});

/* ---------------- the divisor grid ---------------- */
function gval(id){ return +document.getElementById(id).value; }
function minWithCount(T){
  let best = null;
  for(let a=0;a<=5;a++) for(let b=0;b<=4;b++) for(let c=0;c<=2;c++){
    if((a+1)*(b+1)*(c+1)!==T) continue;
    const n = 2**a * 3**b * 5**c;
    if(best===null || n<best) best=n;
  }
  return best;
}
function renderGrid(){
  const a=gval('ga'), b=gval('gb'), c=gval('gc');
  ['ga','gb','gc'].forEach(id=>document.getElementById(id+'-v').textContent=gval(id));
  const n = 2**a * 3**b * 5**c;
  const sup = k => ['⁰','¹','²','³','⁴','⁵'][k];
  let html='';
  for(let k=0;k<=c;k++){
    let t = `<div><div class="cap">× 5${sup(k)}</div><table><tr><td class="hd"></td>`;
    for(let i=0;i<=a;i++) t += `<td class="hd">2${sup(i)}</td>`;
    t+='</tr>';
    for(let j=0;j<=b;j++){
      t += `<tr><td class="hd">3${sup(j)}</td>`;
      for(let i=0;i<=a;i++){
        const v = 2**i * 3**j * 5**k;
        const sq = (i%2===0 && j%2===0 && k%2===0);
        t += `<td class="${sq?'sq':''}">${v}</td>`;
      }
      t+='</tr>';
    }
    html += t+'</table></div>';
  }
  document.getElementById('dgrids').innerHTML = html;
  const cnt = (a+1)*(b+1)*(c+1);
  const sqc = (Math.floor(a/2)+1)*(Math.floor(b/2)+1)*(Math.floor(c/2)+1);
  const parts = []; if(a) parts.push('2'+sup(a)); if(b) parts.push('3'+sup(b)); if(c) parts.push('5'+sup(c));
  document.getElementById('g-n').textContent = n;
  document.getElementById('g-ns').textContent = parts.length ? '= '+parts.join(' × ') : '= 1';
  document.getElementById('g-d').textContent = cnt;
  document.getElementById('g-ds').textContent = `(${a}+1)(${b}+1)(${c}+1)`;
  document.getElementById('g-sq').textContent = sqc;

  const pill=document.getElementById('g-pill'), note=document.getElementById('g-note');
  if(gridTarget){
    const T=gridTarget, best=minWithCount(T);
    pill.className='pill up'; pill.textContent='Puzzle running';
    if(cnt!==T){ note.textContent=`${n} has ${cnt} divisors. You need exactly ${T}.`; return; }
    if(n!==best){ note.textContent=`${n} has ${T} divisors — but it isn't the smallest. Move the bigger power onto a smaller prime.`; return; }
    gridTarget=null;
    S.puzzles=(S.puzzles||0)+1; save(); refresh();
    const box=document.getElementById('gridQuiz');
    box.classList.add('on');
    box.innerHTML=`<strong>Smallest possible.</strong> ${n} = ${parts.join(' × ')||'1'} has exactly ${T} divisors, and nothing smaller does. Puzzles solved: ${S.puzzles}.
      <div class="qrow"><button class="btn ghost small" type="button" id="gridAgain">Another one</button></div>`;
    document.getElementById('gridAgain').addEventListener('click', ()=>document.getElementById('gridPuzzle').click());
    pill.className='pill bal'; pill.textContent='Solved';
    note.textContent='Biggest power on the smallest prime — and more primes usually beat bigger powers.';
  }else{
    pill.className='pill up'; pill.textContent='Building';
    note.textContent = cnt%2 ? `${cnt} is odd — so ${n} must be a perfect square. Check: every power is even.` : 'Each slider adds a row, a column or a whole layer. That\'s where the +1 comes from.';
  }
}
let gridTarget=null, curGPuzzle=null;
const GRID_PUZZLES=[6,8,9,10,12,16];
['ga','gb','gc'].forEach(id=>document.getElementById(id).addEventListener('input', renderGrid));
document.getElementById('gridPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*GRID_PUZZLES.length);
  if(curGPuzzle===i) i=(i+1)%GRID_PUZZLES.length;
  curGPuzzle=i; gridTarget=GRID_PUZZLES[i];
  const box=document.getElementById('gridQuiz');
  box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> Build the <strong>smallest</strong> number with exactly <span class="num" style="font-size:17px">${gridTarget}</span> divisors. Decide the powers on paper first — the machine only tells you whether you were right.`;
  renderGrid();
});
'''

BOOT = ['renderBench()', 'renderGrid()']
