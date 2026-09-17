# Reading comprehension — the framework and the paper shape

The English sibling of `WRITING-PAPERS.md`. Read this before touching `reading.html` or
`tools/papers/english_reading.py`.

The source of truth for the format is `reference/reading_comprehension_reference.pdf` — the real
school paper: **English Paper 2, Grade 7, 25 marks, 35 minutes**, a narrative extract paired with a
journal entry by the same character, lines numbered 3–49, nine questions.

## Why this topic exists

He answers what the text says and stops there. On the reference paper, literal retrieval is worth
about 7 of the 25 marks. The other 18 go to inference, word-in-context, writer's choices, register
and structure. The page and the papers exist to move him up one rung, and to stop him falling off
the other side into invention.

---

## The framework

Four pieces. They appear in the masthead of `reading.html`, in Lesson 3, in the two interactive
tools, and printed in the instructions box of Papers A and B. Keep the wording identical everywhere —
it is meant to become a reflex, and a reflex needs one form of words.

### 1. The ladder — Says → Shows → So what

| Rung | The question | On the reference passage |
|---|---|---|
| **Says** | What literally happened? | He checks his pockets and his jacket. |
| **Shows** | What did the writer *choose* to put there? | He checks **three** places. "Of course." — two words, its own sentence. |
| **So what** | What does that imply about the person? | He already knew it was gone. The searching is him refusing to admit it. |

Every "what does this tell the reader" question wants rung 3, proved with rung 2. An answer that
stops on rung 1 has restated the question and scores nothing.

### 2. The five tells — where rung 2 hides

A writer gives things away the way a bad liar does. Five places to look:

1. **Bodies** — what a body does while the mouth says nothing. *His stomach tightens.* *He turns away quickly.*
2. **Repeats** — anything done or said twice. *checks the other one, then his jacket.* Repetition is never an accident.
3. **Loaded words** — the writer picked this word over a neutral one. *lurches*, *dissolve*, *sighs to a halt*.
4. **Gaps** — what is missing. He never asks her name. *Almost.* standing alone as a sentence.
5. **Turns** — what is different by the end. He starts calculating risk and ends up laughing at himself.

### 3. The answer shape — Quote → Zoom → So what

The move that turns a 1-mark answer into a 2-mark one.

- **Quote short.** The shortest run of words that still carries the meaning. A three-line quotation
  is a confession that you have not found the part that matters.
- **Zoom to one word inside it** and say what that word is doing.
- **Name the feeling or idea**, and say what it *suggests* rather than what it *says*.

> ✗ "'He breathes in slowly, the way his swimming coach had always told him to before a race.'
> This shows he is nervous." — one mark. True, and stops on rung 1.
>
> ✓ "'the way his swimming coach had always told him to' — *always* suggests this is a practised
> habit, so he is frightened but deliberately managing it rather than panicking." — two marks.

### 4. The brake — could you point at a word?

Reading between the lines is not inventing. Before writing an inference, find the word you would
underline if an examiner challenged you. No word, no mark: an overreach scores zero exactly like a
blank. This half is why the Evidence Bench has a **not in the text** bin.

---

## The six sub-skills

These are the question types on the reference paper, and they are the six lessons on
`reading.html`, in the order it teaches them.

| # | Lesson, as titled on the page | What it drills | Reference Qs |
|---|---|---|---|
| 1 | The ladder, and the rung most answers stop on | Which rung a question's verb is asking for; retrieval done properly — two *separate* ideas, inside the named line range, never a copied sentence | Q1(a), Q3 |
| 2 | Words in context: the substitution test | "Give one word that means…" — put the answer back in the sentence; the word must do the sentence's job, not the dictionary's | Q2(b), Q6(a), Q7 |
| 3 | The five tells | Inference from bodies, repeats, loaded words, gaps and turns — and the brake that stops it becoming invention | Q1(b), Q6(b) |
| 4 | Quote, zoom, so what | The 4-mark opinion question: shortest quote, explain *how* not *that*, two quotes must make two different points | Q4 |
| 5 | Why that word and not the other one | Name the flat word the writer refused, then say what refusing it bought her. Also sentence length and punctuation | Q5 |
| 6 | Two voices, one evening | What makes a journal a journal; formal vs informal; ordering events; what each voice knows that the other does not | Q5, Q8, Q9 |

The on-page 30 marks map onto them the house way (`CLAUDE.md` #5 unchanged):

- **5 MCQ × 1** — tick-box inference and word-in-context.
- **5 short × 2** — "give two things", two-feature retrieval, two-part inference.
- **5 word × 3** — quotation + explanation, register comparison, ordering, whole-text synthesis.

Staged hints translate directly: hint 1 points at a line range, hint 2 names the tell, hint 3 gives
the zoom word — never the explanation.

---

## The paper shape

**25 marks, 35 minutes, nine questions.** This is a deliberate departure from `CLAUDE.md` #5, which
fixes topic papers at 30. A reading paper's job is to rehearse the exact artefact he sits, and the
school's is 25. Recorded in `STATE.md` beside the 80-mark maths mock. **Do not change #5**, and do
not "fix" these to 30. `english_reading.py` asserts 25.

The four papers, all built by `tools/papers/english_reading.py`:

| Paper | Level | The two texts |
|---|---|---|
| A | Medium | Meera takes over her father's tiffin round · her journal that night |
| B | Medium | A stray dog on the maidan · a letter from his grandmother in Thrissur, who disagrees |
| C | Hard | Ananya at a swimming trial she never wanted · a coach's blog post about parents who enter their children |
| D | Hard | Clearing a grandfather's house in Mylapore · the estate agent's advertisement for it |

The mark distribution copies the reference exactly:

| Q | Type | Marks |
|---|---|---|
| 1 | (a) retrieval ×2 · (b) tick-box inference | 3 |
| 2 | (a) phrase retrieval · (b) word in context | 2 |
| 3 | retrieval of two details | 2 |
| 4 | opinion + 2 quotations + 2 explanations | 4 |
| 5 | register: 2 quotations + 2 explanations, worked example given | 4 |
| 6 | (a) word in context · (b) meaning of an image | 2 |
| 7 | tick-box: meaning in context | 1 |
| 8 | text-type features ×2 | 2 |
| 9 | (a) one phrase per character · (b) chronological ordering | 5 |
|  | | **25** |

Each paper is **self-contained** — the passage is bound into the same PDF, not issued as a separate
insert. One file to print.

### Conventions

- **Two texts per paper**, a narrative plus a second voice on the same events: a journal, a letter,
  a blog post, a notice. The pairing is what makes Q8 and Q9 possible.
- **Indian settings and names**, per `CONTENT-VOICE.md`.
- **A and B print the framework** in the instructions box and carry a worked example on the
  explanation questions, as the reference does on Q5. **C and D print neither** — recall is part of
  what the hard pair tests.
- **C and D pair narrative with non-fiction**, so the register contrast is doing real work.
- **Paper D keeps the house closing question**: two weak answers in another student's handwriting —
  a three-line copied quotation and a "this shows he is sad" — to be diagnosed and rewritten.
- **One mark-scheme booklet** for all four, tutor-only, linked from nowhere.

### Getting the line references right

`CLAUDE.md` #6 says check the arithmetic in code before it reaches a document. The reading-paper
equivalent is the **line references**, and they fail the same silent way: a question says
"look at lines 12–19", the passage gets edited, and the answer is now on line 20.

Passages are therefore authored as **pre-wrapped lines** — one list entry per printed line — and
`english_reading.py` runs `_verify()` on every build:

- every passage line fits the frame at its font size (`pdfmetrics.stringWidth`);
- every line range cited by a question exists in that paper's passage;
- the keywords the mark scheme expects actually occur inside the cited range;
- each tick-box question has exactly one defensible key;
- the marks total 25 and the type mix matches the table above.

If an assert fires, fix the content, not the assert.
