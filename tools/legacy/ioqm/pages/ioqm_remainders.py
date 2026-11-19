# -*- coding: utf-8 -*-
ID = 'ioqm-remainders'
SHORT_TITLE = 'Clock Arithmetic'
SUB = 'IOQM · Number theory II: remainders, last digits, cycles'
BLURB = ("Huge numbers like 7²⁰²⁶ are answered by their remainders, and remainders live on a clock. "
         "Wrap numbers round a clock of any size, then watch powers fall into cycles that give away their last digit.")
META_TOOL = 'remainder clock'
COLOURS = ('#2B5B84', '#E5EEF6', '#9C2F5A', '#F8E8EF', '#6E5A10', '#F4EFDC')
EYEBROW = 'IOQM Olympiad Prep · Number theory II'
H1 = 'Clock<br><i>Arith</i><em>metic</em>'
LEDE = ("Nobody can work out 7<sup>2026</sup>. Everybody can work out its last digit, once they stop thinking about the number and start "
        "thinking about its remainder. This page is about doing arithmetic on remainders alone — the single most useful trick in Olympiad number theory.")
TARGET = ("You've been landing around <span class=\"num\">10 out of 15</span> at school. This page is out of <span class=\"num\">30</span>; "
          "the targets are <span class=\"num\">21</span> on the first pass and <span class=\"num\">26</span> on the second. No calculator. "
          "If you find yourself multiplying out a big power, stop: you have missed the point of the question.")
VIDEO_MIN = '~45 min total'
LESSON_MIN = '~40 min total'
NAV = [('clock', 'Remainder clock'), ('videos', '6 videos'), ('lessons', '6 lessons'), ('cycles', 'Cycle machine'),
       ('quick', 'Quick checks'), ('short', 'Short answers'), ('word', 'Word problems'), ('traps', 'Exam traps')]

EXTRA_CSS = r'''
.clockwrap{display:grid;grid-template-columns:minmax(220px,320px) 1fr;gap:14px;padding:12px 16px;align-items:center}
.clockwrap svg{width:100%;height:auto}
.conds{font-family:var(--mono);font-size:13.5px;display:grid;gap:6px}
.conds div{padding:6px 10px;border-radius:8px;background:var(--paper);border:1px solid var(--line)}
.conds div.yes{background:var(--ok-tint);border-color:var(--ok);color:#14512F}
.cyc{display:flex;flex-wrap:wrap;gap:6px;padding:12px 16px}
.cyc span{font-family:var(--mono);font-size:13px;border:1px solid var(--line);border-radius:8px;padding:6px 8px;background:var(--paper);min-width:64px;text-align:center}
.cyc span b{display:block;font-size:17px}
.cyc span.first{border-color:var(--rt);background:var(--rt-tint)}
.cyc span.hit{border-color:var(--pm);background:var(--pm-tint);color:var(--pm)}
select{font-family:var(--mono);font-size:15px;padding:7px 9px;border:1px solid var(--line);border-radius:9px;background:var(--paper);color:var(--ink)}
@media (max-width:600px){.clockwrap{grid-template-columns:1fr}}
'''

TOOL1_HTML = r'''
<section id="clock">
  <div class="panel">
    <div class="panel-top">
      <h2>The remainder clock</h2>
      <p>A clock with m positions, 0 to m − 1. Count round it a number of times and you land on the number's remainder. Two numbers that land on the same spot are "the same" as far as division by m is concerned — that is all modular arithmetic means.</p>
    </div>
    <div class="clockwrap">
      <svg viewBox="0 0 300 300" role="img" aria-label="A clock face with m positions"><g id="clockFace"></g></svg>
      <div>
        <div class="conds" id="clockConds"></div>
      </div>
    </div>
    <div class="ctrl">
      <label for="cm">Clock size m</label><input id="cm" type="range" min="2" max="12" value="7" aria-label="Clock size"><span class="num" id="cm-v">7</span>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="ca">Number</label><input id="ca" type="number" value="100" min="0" max="999" step="1" aria-label="The number to wrap round the clock">
      <button class="btn ghost small" type="button" id="caDown">− 1</button>
      <button class="btn ghost small" type="button" id="caUp">+ 1</button>
      <button class="btn ghost small" type="button" id="caJump">+ m</button>
    </div>
    <div class="rows">
      <div class="cell f"><div class="lab">Division</div><div class="val" id="c-div">—</div><div class="sub">number = laps × m + remainder</div></div>
      <div class="cell p"><div class="lab">Lands on</div><div class="val" id="c-r">—</div><div class="sub" id="c-rs"></div></div>
      <div class="cell d"><div class="lab">Laps</div><div class="val" id="c-q">—</div><div class="sub">full trips round the clock</div></div>
      <div class="phasebar">
        <span class="pill go" id="c-pill">Wrapping</span>
        <span id="c-note">Press + m. The number jumps, the remainder doesn't move.</span>
        <span class="push"><button class="btn ghost" type="button" id="clockPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="clockQuiz"></div>
    </div>
  </div>
</section>
'''

TOOL2_HTML = r'''
<section id="cycles">
  <div class="panel">
    <div class="panel-top">
      <h2>The cycle machine</h2>
      <p>Powers of a number, but only their remainders. Sooner or later a remainder repeats, and from then on the whole list repeats. The ochre box is where the cycle starts again; the teal box is the power you asked for.</p>
    </div>
    <div class="ctrl">
      <label for="yb">Base</label><input id="yb" type="range" min="2" max="19" value="7" aria-label="Base"><span class="num" id="yb-v">7</span>
      <label for="ym">Divide by</label>
      <select id="ym" aria-label="Divide by"><option value="10" selected>10 (last digit)</option><option value="7">7</option><option value="9">9</option><option value="11">11</option><option value="13">13</option></select>
    </div>
    <div class="ctrl" style="border-top:none;padding-top:0">
      <label for="yn">Power</label><input id="yn" type="range" min="1" max="60" value="22" aria-label="Power"><span class="num" id="yn-v">22</span>
    </div>
    <div class="cyc" id="cycRow"></div>
    <div class="rows">
      <div class="cell f"><div class="lab">Cycle length</div><div class="val" id="y-len">—</div><div class="sub" id="y-lens"></div></div>
      <div class="cell d"><div class="lab">Power ÷ cycle</div><div class="val" id="y-pos">—</div><div class="sub">the remainder picks the box</div></div>
      <div class="cell p"><div class="lab">Answer</div><div class="val" id="y-ans">—</div><div class="sub" id="y-anss"></div></div>
      <div class="phasebar">
        <span class="pill up" id="y-pill">Cycling</span>
        <span id="y-note">Remainder 0 means the <em>last</em> box of the cycle, not the first.</span>
        <span class="push"><button class="btn ghost" type="button" id="cycPuzzle">Set me a puzzle</button></span>
      </div>
      <div class="quizbox" id="cycQuiz"></div>
    </div>
  </div>
</section>
'''

TRAPS = [
 ("Giving a 'remainder' that is too big",
  "A remainder on division by 6 is one of 0, 1, 2, 3, 4, 5 — nothing else. If x leaves 5, then 2x 'leaves 10' is not an answer; 10 = 6 + 4, so the remainder is <strong>4</strong>. Always finish by wrapping round the clock once more."),
 ("Treating 'cycle position 0' as the first term",
  "The last digits of 2ⁿ go 2, 4, 8, 6. For 2¹⁰⁰, 100 ÷ 4 leaves 0 — which means the <strong>fourth</strong> box, 6, not the first. Remainder 0 is the end of a lap, not the start. Sanity check with a small case: 2⁴ = 16 ends in 6."),
 ("Dividing remainders",
  "You can add, subtract and multiply remainders freely. You can't divide. 2x leaves remainder 2 on division by 6 does <strong>not</strong> force x to leave 1: x = 4 works too (2 × 4 = 8 = 6 + 2). Dividing is only safe when the divisor shares no factor with m."),
 ("Leaving a negative remainder as the final answer",
  "Using −1 instead of 10 when dividing by 11 is a brilliant shortcut in the working. But the answer to 'what is the remainder' is between 0 and m − 1. If your working ends at −1 on division by 7, the answer is <strong>6</strong>."),
 ("Off by one on the calendar",
  "100 days after a Monday is 100 mod 7 = 2 days on, so Wednesday — you count forward from Monday, not from Tuesday. And check for 29 February: 2028 is a leap year, 2027 is not. Most calendar marks are lost to one of these two.")
]

DATA_JS = r'''
/* ---------------- videos ---------------- */
const VIDEOS = [
 {t:"Modular arithmetic 1 — clocks and telling the time", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=SR3oLCYoh-I",
  why:"Starts where you already are: a clock is a remainder machine. Short and gentle — use it to set up the picture the clock tool on this page draws.",
  task:"It is 10 o'clock. Work out the time 50, 100 and 1000 hours from now on a 12-hour clock. Answers: 12, 2, 2. Write one line explaining why 100 and 1000 give the same answer."},

 {t:"Modular Arithmetic: A New Way To Divide", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=G3Wkr5RFVzU",
  why:"Moves from clocks to the notation a ≡ b (mod m) and what it means: same remainder, or equivalently m divides a − b. You need the notation to read Olympiad solutions.",
  task:"Write three numbers ≡ 2 (mod 5) that are bigger than 100, and one negative number ≡ 2 (mod 5). Check each by working out number − 2."},

 {t:"Intro to Modular Arithmetic (AoPS Number Theory, §5.4)", ch:"YouTube walkthrough", url:"https://www.youtube.com/watch?v=HpzcRVmSaOo",
  why:"A walk through the Art of Problem Solving textbook section, including adding and multiplying in mod. This is the rule that lesson 2 turns into a weapon.",
  task:"Without multiplying, find the remainder of 1234 × 5678 on division by 9 and by 10. Then multiply on paper and check both."},

 {t:"How To Get The Last Digit Of Any Number Raised To Any Power", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=bx-0hcOOarc",
  why:"Last digits are remainders on division by 10, and they cycle. The video lists the cycles for every digit; the cycle machine below lets you see them grow.",
  task:"Make a table of the cycles for last digits 2, 3, 4, 7, 8 and 9. Mark the length of each cycle. You should find only lengths 1, 2 and 4."},

 {t:"Find the last digit of 7²⁵ — cyclicity", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=nPaA9tiPbs4",
  why:"One clean worked example, including the step people forget: what to do when the power divides exactly into the cycle length.",
  task:"Find the last digit of 7²⁵, 7¹⁰⁰ and 7²⁰²⁶. Answers: 7, 1, 9. If you wrote 7 for 7¹⁰⁰, read trap 2."},

 {t:"Understanding Remainder Cycles", ch:"YouTube lesson", url:"https://www.youtube.com/watch?v=lrhOXuQsdcE",
  why:"The same cycle idea when you divide by something other than 10 — like 4¹²⁴ ÷ 7. This is where IOQM questions actually live.",
  task:"Find the remainder when 2¹⁰⁰ is divided by 7 (cycle 2, 4, 1). Then set the cycle machine to base 2, divide by 7, power 58 — predict the answer before you look."}
];

/* ---------------- lessons ---------------- */
const LESSONS = [
 {t:"Remainders are positions on a clock", len:"6 min",
  body:`<p>Divide 100 by 7: 100 = 14 × 7 + 2. Fourteen laps of a 7-clock, and you land on <strong>2</strong>. Every whole number lands somewhere on the clock, and numbers that land on the same spot behave the same way whenever you divide by 7.</p>
        <p>The notation for "same spot" is:</p>
        <div class="eqline">100 ≡ 2 (mod 7) &nbsp;&nbsp; read: "100 is congruent to 2, mod 7"</div>
        <p>It means the same thing as either of these:</p>
        <ul><li>100 and 2 leave the same remainder when divided by 7;</li>
            <li>7 divides 100 − 2 = 98.</li></ul>
        <p>The second version is the one you use in proofs: <strong>a ≡ b (mod m) exactly when m divides a − b</strong>. Adding m to a number doesn't move it on the clock — that's the + m button on the tool.</p>`,
  demo:`<strong>Do this:</strong> without a calculator, which of 365, 366 and 371 are ≡ 1 (mod 7)? (Subtract 1 and check for 7: 364 = 52 × 7, yes; 365, no; 370, no.)`,
  cliff:`If you only know where two numbers land, can you tell where their sum lands? Their product?`},

 {t:"Do the arithmetic on the remainders", len:"7 min",
  body:`<p>Yes — and this is the whole trick. If a lands on r and b lands on s, then:</p>
        <div class="eqline">a + b lands on r + s &nbsp;&nbsp; a × b lands on r × s &nbsp;&nbsp; aⁿ lands on rⁿ &nbsp;&nbsp;(then wrap)</div>
        <p><strong>Example.</strong> Remainder of 1234 × 5678 on division by 9. Digit sums give 1234 ≡ 10 ≡ 1 and 5678 ≡ 26 ≡ 8. So the product ≡ 1 × 8 = <strong>8</strong>. You never multiplied.</p>
        <p><strong>Why it works.</strong> Write a = 9p + 1 and b = 9q + 8. Multiply out: every term except 1 × 8 has a 9 in it.</p>
        <p>What you <em>can't</em> do is divide. 2 × 4 = 8 ≡ 2 (mod 6), and 2 × 1 = 2 too, so "2x ≡ 2" doesn't tell you x. Stick to +, −, ×.</p>`,
  demo:`<strong>Do this:</strong> find the remainder when 47 × 53 is divided by 5, using 47 ≡ 2 and 53 ≡ 3. You should get 1. Then check: 47 × 53 = 2491.`,
  cliff:`Every remainder is between 0 and m − 1. But sometimes it's much easier to pretend one of them is negative.`},

 {t:"The −1 trick", len:"6 min",
  body:`<p>On a 7-clock, 6 is one step <em>before</em> 0. So 6 ≡ −1 (mod 7). That makes powers easy:</p>
        <div class="eqline">6⁵⁰ ≡ (−1)⁵⁰ = 1 (mod 7) &nbsp;&nbsp;&nbsp; 6⁵¹ ≡ (−1)⁵¹ = −1 ≡ 6 (mod 7)</div>
        <p>Look for a base that is one less than the divisor — or one more, because then it's ≡ 1 and every power is 1:</p>
        <table class="data"><tr><th>Number</th><th>mod</th><th>Behaves like</th><th>So a huge power is</th></tr>
        <tr><td>8</td><td>9</td><td>−1</td><td>±1</td></tr>
        <tr><td>8</td><td>7</td><td>+1</td><td>1</td></tr>
        <tr><td>10</td><td>11</td><td>−1</td><td>±1</td></tr>
        <tr><td>99</td><td>100</td><td>−1</td><td>±1</td></tr></table>
        <p>This is exactly why the 11-rule from the divisibility page works: 10 ≡ −1 (mod 11), so 10², 10⁴, … ≡ +1 and 10, 10³, … ≡ −1.</p>`,
  demo:`<strong>Do this:</strong> find the remainder when 8¹⁰¹ is divided by 9. (8 ≡ −1, odd power, so −1 ≡ 8.)`,
  cliff:`Most bases are not ±1. What do their powers do?`},

 {t:"Last digits go round in cycles", len:"7 min",
  body:`<p>The last digit of a number is its remainder on division by 10. Powers of 7, last digits only:</p>
        <div class="eqline">7, 9, 3, 1, 7, 9, 3, 1, …</div>
        <p>Once a 1 appears, multiplying by 7 starts the list again. So the cycle has length 4, and to find the last digit of 7²⁰²⁶ you only need 2026 ÷ 4:</p>
        <div class="eqline">2026 = 4 × 506 + 2 &nbsp;→&nbsp; second box &nbsp;→&nbsp; last digit <b>9</b></div>
        <table class="data"><tr><th>Last digit</th><th>Cycle</th><th>Length</th></tr>
        <tr><td>0, 1, 5, 6</td><td>stays put</td><td>1</td></tr>
        <tr><td>4</td><td>4, 6</td><td>2</td></tr><tr><td>9</td><td>9, 1</td><td>2</td></tr>
        <tr><td>2</td><td>2, 4, 8, 6</td><td>4</td></tr><tr><td>3</td><td>3, 9, 7, 1</td><td>4</td></tr>
        <tr><td>7</td><td>7, 9, 3, 1</td><td>4</td></tr><tr><td>8</td><td>8, 4, 2, 6</td><td>4</td></tr></table>
        <p>Only the base's last digit matters: 1237²⁰ ends the same way as 7²⁰.</p>`,
  demo:`<strong>Do this:</strong> find the last digit of 2¹⁰⁰. 100 ÷ 4 leaves 0, which means the <em>fourth</em> box: 6. Check the pattern on 2⁴ = 16.`,
  cliff:`Last digits are remainders mod 10. Does the same cycling happen when you divide by 7, or 13?`},

 {t:"Cycles for any divisor", len:"6 min",
  body:`<p>Yes. There are only m possible remainders, so the list of powers must eventually repeat — and once it hits 1, it starts again. Powers of 2 on a 7-clock:</p>
        <div class="eqline">2, 4, 1, 2, 4, 1, … &nbsp;&nbsp; cycle length 3</div>
        <p>So 2¹⁰⁰: 100 = 3 × 33 + 1, first box, remainder <strong>2</strong>.</p>
        <p><strong>The method, every time:</strong></p>
        <ol><li>List powers' remainders until you reach 1 (or a repeat).</li>
            <li>Divide the exponent by the cycle length.</li>
            <li>Remainder picks the box. Remainder 0 picks the last box.</li></ol>
        <p>Short cut worth knowing: 3³ = 27 = 2 × 13 + 1, so 3³ ≡ 1 (mod 13) and the cycle of 3 mod 13 has length 3. Spotting a small power that is ≡ 1 saves listing.</p>`,
  demo:`<strong>Do this:</strong> find the remainder of 4¹²⁴ on division by 7. (4, 2, 1 — length 3; 124 = 3 × 41 + 1; first box: 4.) Then check on the cycle machine with a power you can reach, like 4⁵⁸.`,
  cliff:`One condition pins a number to a spot on one clock. What if it has to sit on three clocks at once?`},

 {t:"Several clocks at once", len:"7 min",
  body:`<p>"A number leaves 2 when divided by 3, 3 when divided by 4, and 4 when divided by 5." Two ways in.</p>
        <p><strong>Look for the shift.</strong> Every remainder is one less than the divisor. So n + 1 is divisible by 3, 4 and 5, hence by 60. So n = 59, 119, 179, …</p>
        <p><strong>List and filter</strong> when there's no shift. n ≡ 3 (mod 7) and n ≡ 0 (mod 4): multiples of 4 are 4, 8, 12, …; the first one ≡ 3 (mod 7) is <strong>24</strong>, and after that every 28 (because lcm(4, 7) = 28): 24, 52, 80, …</p>
        <p>Either way, once you have one answer, the rest are spaced by the <strong>lcm</strong> of the divisors. That's the remainder clock puzzles below.</p>`,
  demo:`<strong>Do this:</strong> find the smallest positive number that leaves remainder 1 when divided by 2, 3, 4, 5 and 6. (n − 1 is divisible by 60, so n = 1, 61, 121, … — and 1 counts, because 1 ÷ 2 is 0 remainder 1. Had the question said 'greater than 1', the answer would be 61.)`,
  cliff:`That's the lessons. Q14 wants the last digit of a sum of three enormous powers, and Q15 is a box of sweets that must sit on four clocks at once.`}
];

/* ---------------- questions ---------------- */
const MCQS = [
 {n:1, lvl:"warm-up", q:"What is the remainder when <span class='num'>100</span> is divided by <span class='num'>7</span>?",
  o:["1","2","3","5"], a:1,
  why:"14 × 7 = 98, and 100 − 98 = 2. If you said 3 you used 97, which isn't a multiple of 7."},
 {n:2, lvl:"standard", q:"It is 9 o'clock now. On a 12-hour clock, what time will it be <span class='num'>100</span> hours from now?",
  o:["1 o'clock","4 o'clock","7 o'clock","9 o'clock"], a:0,
  why:"100 = 8 × 12 + 4, so 100 hours is 8 full laps plus 4 hours. 9 + 4 = 13, which wraps to 1. Option B forgot to add the starting 9."},
 {n:3, lvl:"standard", q:"What is the last digit of <span class='num'>3²⁰²⁶</span>?",
  o:["1","3","7","9"], a:3,
  why:"Last digits of powers of 3 cycle 3, 9, 7, 1. 2026 = 4 × 506 + 2, so it's the second box: 9."},
 {n:4, lvl:"standard", q:"What is the remainder when <span class='num'>2¹⁰⁰</span> is divided by <span class='num'>7</span>?",
  o:["1","2","4","6"], a:1,
  why:"Powers of 2 mod 7 go 2, 4, 1 and repeat — cycle length 3. 100 = 3 × 33 + 1: first box, 2. Option D is the last digit of 2¹⁰⁰, which answers a different question."},
 {n:5, lvl:"trap", q:"A number x leaves remainder <span class='num'>5</span> when divided by <span class='num'>6</span>. What remainder does <span class='num'>2x</span> leave when divided by 6?",
  o:["10","4","5","2"], a:1,
  why:"2 × 5 = 10, but 10 is not a remainder on division by 6 — it wraps to 10 − 6 = 4. Check with x = 11: 2x = 22 = 3 × 6 + 4."}
];

const SHORTS = [
 {n:6, m:2, lvl:"warm-up", q:"Without multiplying or adding the numbers themselves, find the remainder when each is divided by 9:<br><strong>(a)</strong> <span class='num'>1234 × 5678</span> <span class='num'>[1]</span> &nbsp; <strong>(b)</strong> <span class='num'>1234 + 5678</span> <span class='num'>[1]</span>",
  scheme:["(a) 1234 ≡ 1 and 5678 ≡ 26 ≡ 8, so the product ≡ <strong>8</strong> <span class='num'>[1]</span>",
          "(b) 1 + 8 = 9 ≡ <strong>0</strong> — the sum, 6912, is a multiple of 9 <span class='num'>[1]</span>"],
  tip:"In (b), 9 is not a remainder on division by 9. It wraps to 0. Writing 9 loses the mark."},
 {n:7, m:2, lvl:"standard", q:"Find the last digit of <span class='num'>7²⁰²⁶</span>. Show your reasoning.",
  scheme:["Last digits of 7ⁿ cycle 7, 9, 3, 1 (length 4) <span class='num'>[1]</span>",
          "2026 = 4 × 506 + 2, so the second term: <strong>9</strong> <span class='num'>[1]</span>"],
  tip:"The first mark is for showing the cycle. An answer of 9 with no cycle written down is a guess as far as the examiner is concerned."},
 {n:8, m:2, lvl:"standard", q:"Find the remainder when <span class='num'>6⁵⁰ + 8⁵¹</span> is divided by <span class='num'>7</span>.",
  scheme:["6 ≡ −1 so 6⁵⁰ ≡ 1; 8 ≡ 1 so 8⁵¹ ≡ 1 <span class='num'>[1]</span>",
          "1 + 1 = <strong>2</strong> <span class='num'>[1]</span>"],
  tip:"Both bases are next door to a multiple of 7. Spotting that is the whole question — if you started listing powers, you did ten times more work than needed."},
 {n:9, m:2, lvl:"standard", q:"Find the smallest whole number <strong>greater than 10</strong> that leaves remainder 2 when divided by each of 3, 4 and 5.",
  scheme:["n − 2 must be divisible by 3, 4 and 5, so by lcm = 60 <span class='num'>[1]</span>",
          "n = 2, 62, 122, … — the smallest above 10 is <strong>62</strong> <span class='num'>[1]</span>"],
  tip:"n = 2 itself satisfies all three conditions, which is why the question says 'greater than 10'. Read conditions like that slowly — they are there because the obvious answer is too small."},
 {n:10, m:2, lvl:"hard", q:"Prove that the square of every odd number leaves remainder <span class='num'>1</span> when divided by <span class='num'>8</span>.",
  scheme:["Write the odd number as 2k + 1: (2k + 1)² = 4k² + 4k + 1 = <strong>4k(k + 1) + 1</strong> <span class='num'>[1]</span>",
          "k(k + 1) is a product of consecutive numbers, so it's even; then 4k(k + 1) is a multiple of 8 <span class='num'>[1]</span>"],
  tip:"Checking 3² = 9, 5² = 25, 7² = 49 is evidence, not proof. The second mark is for saying why k(k + 1) is even — one of two consecutive numbers is always even."}
];

const WORDS = [
 {n:11, m:3, lvl:"standard", q:"1 January 2027 is a <strong>Friday</strong>. 2027 is not a leap year.<br><br><strong>(a)</strong> What day of the week is 1 March 2027? <span class='num'>[1]</span><br><strong>(b)</strong> What day of the week is 1 January 2028? <span class='num'>[1]</span><br><strong>(c)</strong> 2028 <em>is</em> a leap year. What day of the week is 1 January 2029? <span class='num'>[1]</span>",
  hints:["Count the days from 1 January to 1 March: all of January and all of February.",
         "Only the remainder on division by 7 matters. 365 = 52 × 7 + 1.",
         "A leap year has 366 days. What is 366 mod 7?"],
  sol:["(a) 31 + 28 = 59 days later; 59 = 8 × 7 + 3, so 3 days after Friday: <strong>Monday</strong>.",
       "(b) 365 ≡ 1 (mod 7), so one day after Friday: <strong>Saturday</strong>.",
       "(c) 366 ≡ 2 (mod 7), so two days after Saturday: <strong>Monday</strong>.",
       "This is why a date's weekday usually moves on by one each year, and by two when a 29 February is crossed."]},

 {n:12, m:3, lvl:"standard", q:"A whole number n leaves remainder <span class='num'>3</span> when divided by <span class='num'>7</span>. Find the remainder when each of these is divided by 7:<br><strong>(a)</strong> <span class='num'>5n</span> <span class='num'>[1]</span> &nbsp; <strong>(b)</strong> <span class='num'>n² + n</span> <span class='num'>[1]</span> &nbsp; <strong>(c)</strong> <span class='num'>n³</span> <span class='num'>[1]</span>",
  hints:["Replace n by 3 everywhere — that's what n ≡ 3 (mod 7) lets you do.",
         "Work out each expression with n = 3, then wrap the answer round a 7-clock.",
         "Check with a real number: n = 10 leaves remainder 3. Try your answers on it."],
  sol:["(a) 5 × 3 = 15 = 2 × 7 + 1 → <strong>1</strong>.",
       "(b) 9 + 3 = 12 = 7 + 5 → <strong>5</strong>.",
       "(c) 27 = 3 × 7 + 6 → <strong>6</strong>.",
       "Check with n = 10: 5n = 50 → 1 ✓, n² + n = 110 → 5 ✓, n³ = 1000 → 6 ✓."]},

 {n:13, m:3, lvl:"standard", q:"Let <span class='num'>S = 1! + 2! + 3! + … + 100!</span>, where n! = 1 × 2 × 3 × … × n.<br><br><strong>(a)</strong> Explain why every term from 4! onwards is a multiple of 12. <span class='num'>[1]</span><br><strong>(b)</strong> Find the remainder when S is divided by 12. <span class='num'>[1]</span><br><strong>(c)</strong> Find the last digit of S. <span class='num'>[1]</span>",
  hints:["4! = 24. Every later factorial is 4! times more numbers.",
         "So only the first three terms affect the remainder mod 12.",
         "For the last digit you want the remainder mod 10. Which factorial is the first to be a multiple of 10?"],
  sol:["(a) For n ≥ 4, n! = 24 × (5 × 6 × … × n), and 24 = 2 × 12, so it's a multiple of 12.",
       "(b) S ≡ 1 + 2 + 6 = 9 (mod 12) → <strong>9</strong>.",
       "(c) From 5! = 120 on, every term ends in 0. So the last digit is that of 1 + 2 + 6 + 24 = 33: <strong>3</strong>.",
       "A sum of a hundred gigantic numbers, and only the first four mattered. Most 'enormous' IOQM questions collapse like this once you think in remainders."]},

 {n:14, m:3, lvl:"hard", q:"Let <span class='num'>N = 2²⁰²⁷ + 3²⁰²⁷ + 7²⁰²⁷</span>.<br><br><strong>(a)</strong> Find the last digit of 2²⁰²⁷. <span class='num'>[1]</span><br><strong>(b)</strong> Find the last digits of 3²⁰²⁷ and 7²⁰²⁷. <span class='num'>[1]</span><br><strong>(c)</strong> Hence find the last digit of N. <span class='num'>[1]</span>",
  hints:["All three bases have last-digit cycles of length 4. Find 2027 mod 4 once and use it three times.",
         "2027 = 4 × 506 + 3, so you want the third box of each cycle.",
         "Add the three last digits, then take the last digit of that."],
  sol:["(a) 2, 4, 8, 6 — third box: <strong>8</strong>.",
       "(b) 3, 9, 7, 1 → <strong>7</strong>; 7, 9, 3, 1 → <strong>3</strong>.",
       "(c) 8 + 7 + 3 = 18, so N ends in <strong>8</strong>.",
       "You can add last digits because last digits are remainders mod 10, and remainders add. The 3 and 7 cycles are each other backwards — 7 + 3 = 10 — which is why 3ⁿ + 7ⁿ always ends in 0 for odd n."]},

 {n:15, m:3, lvl:"hard", q:"A box holds fewer than <span class='num'>300</span> sweets. Counted out in 3s, 2 are left over. In 4s, 3 are left. In 5s, 4 are left. In 7s, none are left.<br><br><strong>(a)</strong> Explain why the number of sweets plus one is a multiple of 60. <span class='num'>[1]</span><br><strong>(b)</strong> List every number of sweets below 300 that satisfies the first three conditions. <span class='num'>[1]</span><br><strong>(c)</strong> How many sweets are in the box? <span class='num'>[1]</span>",
  hints:["Each leftover is one less than the group size. What happens if you add one more sweet?",
         "If n + 1 is divisible by 3, 4 and 5, it's divisible by their lcm. List n + 1 = 60, 120, … below 301.",
         "Now test each candidate for divisibility by 7."],
  sol:["(a) Adding one sweet makes each leftover a full group, so n + 1 is divisible by 3, 4 and 5, hence by lcm(3, 4, 5) = 60.",
       "(b) n + 1 = 60, 120, 180, 240, 300, so <strong>n = 59, 119, 179, 239, 299</strong>.",
       "(c) Only 119 = 7 × 17 is a multiple of 7, so there are <strong>119</strong> sweets.",
       "The same move as the remainder clock puzzles: find one condition that collapses the others, then filter. Checking 119 in 3s, 4s and 5s (39 r 2, 29 r 3, 23 r 4) takes ten seconds and is worth doing."]}
];
'''

TOOLS_JS = r'''
/* ---------------- the remainder clock ---------------- */
function mod(a,m){ return ((a%m)+m)%m; }
function clampA(v){ v=Math.round(+v||0); return Math.max(0, Math.min(999, v)); }
let clockTarget=null, curCPuzzle=null;
function drawClock(){
  const m=+document.getElementById('cm').value, a=clampA(document.getElementById('ca').value);
  document.getElementById('cm-v').textContent=m;
  const r=mod(a,m), q=Math.floor(a/m);
  let g='<circle cx="150" cy="150" r="118" fill="var(--card)" stroke="var(--line)" stroke-width="2"/>';
  for(let k=0;k<m;k++){
    const ang=-Math.PI/2 + 2*Math.PI*k/m;
    const x=150+100*Math.cos(ang), y=150+100*Math.sin(ang);
    const on=(k===r);
    g+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${on?19:15}" fill="${on?'var(--pm)':'var(--paper)'}" stroke="${on?'var(--pm)':'var(--line)'}"/>`;
    g+=`<text x="${x.toFixed(1)}" y="${(y+5).toFixed(1)}" text-anchor="middle" font-family="var(--mono)" font-size="${on?16:14}" font-weight="700" fill="${on?'#fff':'var(--ink)'}">${k}</text>`;
  }
  const ang=-Math.PI/2 + 2*Math.PI*r/m;
  g+=`<line x1="150" y1="150" x2="${(150+70*Math.cos(ang)).toFixed(1)}" y2="${(150+70*Math.sin(ang)).toFixed(1)}" stroke="var(--pm)" stroke-width="5" stroke-linecap="round"/>`;
  g+=`<circle cx="150" cy="150" r="6" fill="var(--ink)"/>`;
  g+=`<text x="150" y="190" text-anchor="middle" font-family="var(--mono)" font-size="13" fill="var(--ink-soft)">${a} on a ${m}-clock</text>`;
  document.getElementById('clockFace').innerHTML=g;
  document.getElementById('c-div').textContent=`${a} = ${q} × ${m} + ${r}`;
  document.getElementById('c-r').textContent=r;
  document.getElementById('c-rs').textContent=`${a} ≡ ${r} (mod ${m})`;
  document.getElementById('c-q').textContent=q;

  const conds=document.getElementById('clockConds'), pill=document.getElementById('c-pill'), note=document.getElementById('c-note');
  if(clockTarget){
    const T=clockTarget;
    const inRange = a>=T.lo && a<=T.hi;
    const rows=T.c.map(([mm,rr])=>({mm,rr,ok:mod(a,mm)===rr}));
    conds.innerHTML = `<div class="${inRange?'yes':''}">between ${T.lo} and ${T.hi} ${inRange?'✓':'✗'}</div>` +
      rows.map(o=>`<div class="${o.ok?'yes':''}">leaves ${o.rr} on ÷ ${o.mm} &nbsp;(now ${mod(a,o.mm)}) ${o.ok?'✓':'✗'}</div>`).join('');
    pill.className='pill up'; pill.textContent='Puzzle running';
    if(inRange && rows.every(o=>o.ok)){
      clockTarget=null;
      S.puzzles=(S.puzzles||0)+1; save(); refresh();
      const box=document.getElementById('clockQuiz'); box.classList.add('on');
      box.innerHTML=`<strong>All conditions met.</strong> ${a} works. ${T.more} Puzzles solved: ${S.puzzles}.
        <div class="qrow"><button class="btn ghost small" type="button" id="clockAgain">Another one</button></div>`;
      document.getElementById('clockAgain').addEventListener('click', ()=>document.getElementById('clockPuzzle').click());
      pill.className='pill bal'; pill.textContent='Solved';
      note.textContent='Find one answer, then the rest are spaced by the lcm of the divisors.';
    }else{
      note.textContent='Change the clock size to check each condition — the number stays the same.';
    }
  }else{
    conds.innerHTML = [2,3,4,5,6,7,8,9,10,11,12].map(mm=>`<div>${a} ≡ ${mod(a,mm)} (mod ${mm})</div>`).slice(0,6).join('');
    pill.className='pill go'; pill.textContent='Wrapping';
    note.textContent='Press + m. The number jumps, the remainder doesn\'t move.';
  }
}
const CLOCK_PUZZLES=[
 {lo:50, hi:100, c:[[7,3],[4,0]], more:'The answers are 52 and 80 — 28 apart, because lcm(7, 4) = 28.'},
 {lo:20, hi:60,  c:[[5,2],[3,1]], more:'22, 37 and 52 all work — 15 apart, because lcm(5, 3) = 15.'},
 {lo:100,hi:150, c:[[9,4],[2,0]], more:'112, 130 and 148 — 18 apart.'},
 {lo:1,  hi:100, c:[[3,2],[4,3],[5,4]], more:'Every remainder is one short, so n + 1 is a multiple of 60: the only answer is 59.'},
 {lo:1,  hi:100, c:[[11,0],[2,1],[3,2]], more:'11 and 77 — odd multiples of 11 that sit on 2 of a 3-clock, 66 apart.'},
 {lo:1,  hi:100, c:[[6,5],[7,6]], more:'n + 1 is a multiple of 42, so 41 or 83.'}
];
['cm','ca'].forEach(id=>document.getElementById(id).addEventListener('input', drawClock));
document.getElementById('caUp').addEventListener('click', ()=>{const e=document.getElementById('ca'); e.value=clampA(+e.value+1); drawClock();});
document.getElementById('caDown').addEventListener('click', ()=>{const e=document.getElementById('ca'); e.value=clampA(+e.value-1); drawClock();});
document.getElementById('caJump').addEventListener('click', ()=>{const e=document.getElementById('ca'); e.value=clampA(+e.value + +document.getElementById('cm').value); drawClock();});
document.getElementById('clockPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*CLOCK_PUZZLES.length);
  if(curCPuzzle===i) i=(i+1)%CLOCK_PUZZLES.length;
  curCPuzzle=i; clockTarget=CLOCK_PUZZLES[i];
  document.getElementById('ca').value=0;   /* start from an unsolved state */
  const T=clockTarget;
  const box=document.getElementById('clockQuiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> Find a number between ${T.lo} and ${T.hi} that ${T.c.map(([m,r])=> r===0?`is a multiple of ${m}`:`leaves ${r} when divided by ${m}`).join(', and ')}. Reason it out, then type it in. The conditions tick as they're met.`;
  drawClock();
});

/* ---------------- the cycle machine ---------------- */
function powCycle(b,m){
  const seen=new Map(), list=[];
  let v=mod(b,m), k=1;
  while(!seen.has(v)){ seen.set(v,k); list.push(v); v=mod(v*b,m); k++; }
  return {list, start:seen.get(v), len:k-seen.get(v)};
}
function powMod(b,n,m){ let r=1%m; for(let i=0;i<n;i++) r=mod(r*b,m); return r; }
let cycTarget=null, curYPuzzle=null;
function drawCycle(){
  const b=+document.getElementById('yb').value, m=+document.getElementById('ym').value, n=+document.getElementById('yn').value;
  document.getElementById('yb-v').textContent=b; document.getElementById('yn-v').textContent=n;
  const C=powCycle(b,m);
  const ans=powMod(b,n,m);
  let html='';
  const show=Math.max(C.list.length+C.len, 8);
  for(let k=1;k<=show;k++){
    const v=powMod(b,k,m);
    const same = (n<C.start) ? (k===n) : (k>=C.start && k<C.start+C.len && (k-C.start)%C.len===(n-C.start)%C.len);
    const cls = same ? 'hit' : (k===C.list.length+1 ? 'first' : '');
    const lab = (same && k!==n) ? `<i style="font-style:normal;font-size:10.5px;display:block">same box as ${b}<sup>${n}</sup></i>` : '';
    html+=`<span class="${cls}">${b}<sup>${k}</sup><b>${v}</b>${lab}</span>`;
  }
  document.getElementById('cycRow').innerHTML=html;
  document.getElementById('y-len').textContent=C.len;
  document.getElementById('y-lens').textContent = C.start===1 ? 'repeats from the first power' : `repeats from power ${C.start}`;
  let pos='—';
  if(n>=C.start){ const k=(n-C.start)%C.len; pos = `box ${k+1} of ${C.len}`; }
  else pos='before the cycle';
  document.getElementById('y-pos').textContent=pos;
  document.getElementById('y-ans').textContent=ans;
  document.getElementById('y-anss').innerHTML = m===10 ? `${b}<sup>${n}</sup> ends in ${ans}` : `${b}<sup>${n}</sup> ≡ ${ans} (mod ${m})`;

  const pill=document.getElementById('y-pill'), note=document.getElementById('y-note');
  if(cycTarget){
    const T=cycTarget;
    pill.className='pill up'; pill.textContent='Puzzle running';
    if(b!==T.b || m!==T.m){ note.textContent=`Set the base to ${T.b} and divide by ${T.m} first.`; return; }
    if(n<T.lo || n>T.hi){ note.textContent=`Keep the power between ${T.lo} and ${T.hi}.`; return; }
    if(ans!==T.want){ note.textContent=`${b}^${n} gives ${ans}, not ${T.want}. Which box of the cycle is ${T.want} in?`; return; }
    cycTarget=null;
    S.puzzles=(S.puzzles||0)+1; save(); refresh();
    const box=document.getElementById('cycQuiz'); box.classList.add('on');
    box.innerHTML=`<strong>Yes.</strong> ${T.more} Puzzles solved: ${S.puzzles}.
      <div class="qrow"><button class="btn ghost small" type="button" id="cycAgain">Another one</button></div>`;
    document.getElementById('cycAgain').addEventListener('click', ()=>document.getElementById('cycPuzzle').click());
    pill.className='pill bal'; pill.textContent='Solved';
    note.textContent='The box number is the power\'s remainder on division by the cycle length.';
  }else{
    pill.className='pill up'; pill.textContent='Cycling';
    note.innerHTML='Remainder 0 means the <em>last</em> box of the cycle, not the first.';
  }
}
const CYC_PUZZLES=[
 {b:3, m:10, want:7, lo:20, hi:40, more:'3ⁿ ends in 7 when n leaves 3 on division by 4: 23, 27, 31, 35 or 39.'},
 {b:7, m:10, want:1, lo:50, hi:60, more:'7ⁿ ends in 1 exactly when 4 divides n: 52, 56 or 60.'},
 {b:2, m:10, want:6, lo:30, hi:40, more:'The fourth box — so n is a multiple of 4: 32, 36 or 40.'},
 {b:2, m:7,  want:4, lo:40, hi:50, more:'2, 4, 1 has length 3, and 4 is box 2, so n ≡ 2 (mod 3): 41, 44, 47 or 50.'},
 {b:4, m:7,  want:2, lo:1,  hi:20, more:'4, 2, 1 — box 2 again, so any n ≡ 2 (mod 3).'},
 {b:9, m:10, want:9, lo:41, hi:49, more:'9, 1, 9, 1 — odd powers end in 9.'}
];
['yb','ym','yn'].forEach(id=>document.getElementById(id).addEventListener('input', drawCycle));
document.getElementById('ym').addEventListener('change', drawCycle);
document.getElementById('cycPuzzle').addEventListener('click', ()=>{
  let i=Math.floor(Math.random()*CYC_PUZZLES.length);
  if(curYPuzzle===i) i=(i+1)%CYC_PUZZLES.length;
  curYPuzzle=i; cycTarget=CYC_PUZZLES[i];
  document.getElementById('yn').value=1;   /* start from an unsolved state */
  const T=cycTarget, what = T.m===10 ? `ends in ${T.want}` : `leaves remainder ${T.want} when divided by ${T.m}`;
  const box=document.getElementById('cycQuiz'); box.classList.add('on');
  box.innerHTML=`<strong>Puzzle.</strong> Find a power n between ${T.lo} and ${T.hi} so that <span class="num">${T.b}ⁿ</span> ${what}. Work out which n on paper first — then set the base, the divisor and the power.`;
  drawCycle();
});
'''

BOOT = ['drawClock()', 'drawCycle()']
