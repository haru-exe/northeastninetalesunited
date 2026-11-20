# Elasticity midsem notes: common brief for Writers A, B and C

## 1. The job

You are one of three writers producing study notes for a student revising Elasticity for a midsem exam.
Textbook: M. H. Sadd, *Elasticity: Theory, Applications, and Numerics*, 3rd ed., Elsevier, 2014.
A coordinator (the session that started you) assigned your three topics, will review your plan, and will
review your writing as a student would. The finished notes are one web page; your topics go into it as
HTML fragments.

**The reader.** A student working alone the night before the exam, with nothing else open, who has
forgotten most of the lectures. An undefined symbol or a skipped step is where they get stuck.
Include only what the exam could ask, or what is needed to understand something it could ask.
No history, no motivation that fails this test.

**Style the student chose: board walkthrough.** Intuition first, then the precise statement, then every
algebraic step with the reason for each step.

**The student's rule for every concept:** explain the concept, then show a good example from the book,
then give one book exercise to solve. Exam questions are at the level of the book's worked examples and
end-of-chapter exercises.

## 2. Workflow: two phases

### Phase 1: plan only (do this now)
1. Read this brief, your writer brief (`notes-build/brief-writer-X.md`) and the block template
   `notes-build/template-fragment.html`.
2. Read the book pages for your topics from the PDFs with the Read tool and its `pages` parameter
   (at most 20 pages per call). Read every worked example and every exercise you will use on the
   page images, figures included.
3. Solve every worked example and every your-turn exercise you plan to use, and check the numbers
   with Python.
4. Write your plan to `notes-build/plans/writer-X-plan.md` in the format of section 9.
5. **Stop.** End your turn with exactly one line: `Plan ready: notes-build/plans/writer-X-plan.md`.
   Do not write any HTML yet. The coordinator will message you with corrections and the word "proceed".

### Phase 2: write (only after the coordinator's message says proceed)
1. Write each topic to `notes-build/fragments/tN.html`: one `<section>` element per file, nothing else.
2. Write the formula-sheet rows to `notes-build/fragments/tN-symbols.html` and
   `notes-build/fragments/tN-results.html` (format in section 8).
3. Run the checker on each topic and fix every ERROR; read every WARNING and fix the real ones:
   `python -I notes-build/scripts/check_fragment.py notes-build/fragments/tN.html`
4. Do the self-check in section 7 for each topic.
5. Report in one short final message: files written, the checker result per topic, the self-check
   result per topic, and anything the coordinator must decide. Then stop and wait; the coordinator may
   send fixes after reading your topics as a student.

Write only those files. Do not edit `page-src.html`, the template, the scripts, or another writer's files.
Put any scratch scripts in `notes-build/scripts/writer-X/` (X is your letter).

## 3. Sources

Book PDFs are in the course folder `C:\Users\amy23\Downloads\elasticity\`:

| Chapter | File | PDF pages | PDF page = book page minus |
|---|---|---|---|
| 1 | `Chapter-1---Mathematical-Preliminaries_2014_Elasticity.pdf` | 27 | 2 |
| 2 | `Chapter-2---Deformation--Displacements-and-Strains_2014_Elasticity.pdf` | 23 | 30 |
| 3 | `Chapter-3---Stress-and-Equilibrium_2014_Elasticity.pdf` | 26 | 54 |
| 4 | `Chapter-4---Material-Behavior-Linear-Elastic-Solids_2014_Elasticity.pdf` | 14 | 80 |
| 5 | `Chapter-5---Formulation-and-Solution-Strategies_2014_Elasticity.pdf` | 23 | 94 |
| 6 | `Chapter-6---Strain-Energy-and-Related-Principles_2014_Elasticity.pdf` | 21 | 118 |
| 7 | `Chapter-7---Two-Dimensional-Formulation_2014_Elasticity.pdf` | 17 | 140 |
| 8 | `Chapter-8---Two-Dimensional-Problem-Solution_2014_Elasticity.pdf` | 76 | 158 |

Your writer brief gives the PDF pages of every section, example and exercise you need.

`notes-build/book-text/chN.txt` is a raw text extraction. Use it only to find where things are.
It garbles Greek letters, minus signs and equations. For example, it prints the second principal
direction of Example 3.1 as "(e1, 1, 1)/√3" where the book has $(-1,1,1)/\sqrt3$.
**Every equation, sign and number you write must come from the PDF page image.**
Read figure-based data (angles, which face carries which load, dimensions) from the page image, and
write in your plan exactly what you read, so the coordinator can check it.

## 4. Shape of every topic (follow `template-fragment.html` exactly)

1. **Header.** Number badge with the chapter class (`c1` for Chapter 1, `c2` for 2, `c3` for 3, `c4` for 4),
   eyebrow `Chapter N · §… · Exam weight: … (estimate)`, and the title exactly as in your writer brief.
2. **Where we are** (`box recap`). Two or three sentences: what the previous topic established, the
   question it left open, how this topic answers it. Topic 1 instead says what the course builds towards.
3. **What you need from earlier** (`box recap`). Write out in full the definitions and equations this topic
   relies on, and name the topic each comes from. Restate them; never just cite. Take them from the book
   pages of that earlier topic (another writer is writing it in parallel; do not wait for their file).
4. **Symbols in this topic** (`box sym`). Every symbol the topic uses: symbol, meaning, units.
5. **Concept blocks** A, B (and C), each in this order:
   - Heading `h3.concept` labelled `NA`, `NB`, `NC` (for Topic 4: `4A`, `4B`). Never `4.1`-style labels:
     they clash with the book's section numbers.
   - **Explanation.** Intuition first (2 to 4 sentences, a physical picture before symbols); a definition box
     for each new term; the precise statement; the derivation with every step if it is examinable (each
     line changes one thing, and the text says what changed and why); then one `p.inwords` sentence on
     what the result says. If a derivation is not examinable, state the result, say it is stated without
     proof in the book, and explain what it means.
   - **Worked example** (`box ex`). Tag `Worked example · Book Example X.Y` or, when the book has no worked
     example, `Worked example · Book Exercise X.Y, solved`. Full problem statement with all data. Numbered
     steps (`ol.steps`), each with a `p.why` reason. Each time an equation is used, write it out again and
     say where it came from before substituting. Carry units. Finish with a check where one applies.
   - **Your turn** (`box turn`). Exactly one book exercise. Write its full statement with all data, and
     describe any figure in words (or a simple SVG), so it can be done without the book. Then
     `<details><summary>Hint</summary>…</details>` and
     `<details><summary>Answer and key steps</summary>…</details>` with every step present (brief reasons)
     and the final answer.
6. **Common mistake** (`box mistake`). Only mistakes students really make (sign conventions, the factor of 2
   between $\gamma_{xy}$ and $e_{xy}$, transposed indices, degrees versus radians). Never invent one to fill
   the box. Red is used for this box only.
7. **Key results** (`box key`). The equations and facts to memorise, each with its book equation number.
8. **Looking ahead · Ch 5–8** (`box ahead`). Writers B and C only. See section 6.
9. **What comes next** (`p.next`). One sentence: which later topic uses these results, and for what.

**House standard.** Every idea opens with 2 to 4 sentences of intuition before any symbols. Every
derivation changes one thing per line and says why. Every worked example has 5 to 12 numbered steps, each
with its reason. Every concept block ends with exactly one your-turn book exercise with a hint and a hidden
answer. Every symbol is defined in the topic where it is first used.

## 5. No shortcuts

Write every topic as if it were the only one the student will read.
- Never write "similarly", "as before", "as in Topic N", "by the same method", "it can be shown",
  "the rest follows", "and so on", "clearly", "obviously", "trivially", or dots in place of steps.
  When a method is used a second time, carry it out in full a second time.
- In a derivation or a worked example, each line changes one thing, and the text says what changed and why.
- Define every symbol in this topic before its first use, even if an earlier topic defined it.
- If something the topic needs is not in the book pages, say so in your report instead of filling it in.

## 6. Looking ahead (Writers B and C only: Topics 4 to 9)

The student asked that every topic from Chapters 2 to 4 show how it will be used, and why it is useful,
in the later syllabus: **§5.1–5.6; §6.1–6.3, 6.5, 6.6; Chapter 7 (all of it); §8.1, 8.3, 8.4, 8.5.**
Nothing outside these sections.
- Each link: a `.where` line naming the section and equation number(s), then 2 or 3 concrete sentences:
  which result of this topic is used there, how it is used, and why understanding it now makes that section
  easier. Where it helps, show the one later equation it produces (in LaTeX, copied from the PDF page).
- Verify every section and equation number on the PDF page before citing it, and give the page in your plan.
  The starting map in your writer brief was drafted from garbled text: treat it as leads to check.
- Four to six links per topic. Quality over count.
- Chapter 1 topics are excluded by the student: Writer A writes no Looking-ahead box.

## 7. Maths, HTML and the self-check

All maths is LaTeX, rendered by KaTeX auto-render with `$…$` (inline) and `$$…$$` (display).
- Every symbol, even a single letter in a sentence, goes in maths: "the stiffness $k$", never "the stiffness k".
  Every subscript, Greek letter, unit with a power ($\mathrm{N\,m^{-2}}$), every equation, in prose, tables,
  captions and lists.
- No Unicode maths anywhere: no σ, ε, ×, ², ≈, ≤, ∂, √, ∇. Use `\sigma`, `\times`, `^2`, `\approx`, `\le`,
  `\partial`, `\sqrt{}`, `\nabla`.
- Display equations: `<div class="eqblock"><div class="math">$$…$$</div><span class="eqref">(2.2.6)</span></div>`.
  Leave out the eqref span when the book gives no number. Never `\tag`.
- Inside maths write `\lt`, `\gt`, `\le`, `\ge`. Never a raw `<` or `>`: the HTML parser breaks it.
  Never put HTML tags inside `$…$`.
- Matrices: `\begin{bmatrix} a & b \\ c & d \end{bmatrix}` with spaces around `&`. Several lines:
  `\begin{aligned} … \end{aligned}` inside `$$…$$`. Not allowed: `\begin{equation}`, `\begin{align}`,
  `\tag`, `\label`, `\eqref`, `\over`, `\bm`, `\newcommand`, `\def`.
- Vectors in bold: `\mathbf{u}`, `\mathbf{n}`, `\mathbf{T}^{n}`; bold Greek: `\boldsymbol{\omega}`.
  Permutation symbol `\epsilon_{ijk}`. Strain is $e_{ij}$ (Sadd's letter, not $\varepsilon_{ij}$).
  Dilatation is $\vartheta$.
- `$` means maths only.
- Numbers with units: `$200\ \mathrm{mm}$`, `$207\ \mathrm{GPa}$`, `$300\times10^{-6}$`.
- Simple SVG diagrams only where a problem depends on geometry (the template shows how): `currentColor`
  only, plain letters only inside the SVG (no `$`), at most two per topic.

**Numbers.** Compute every numeric result with Python 3.12 (numpy and sympy are installed); keep scripts in
`notes-build/scripts/writer-X/` and run them with `python -I script.py`. Give exact forms first, then
decimals to 3 or 4 significant figures.

**Self-check for each topic** (report the result):
1. Plan: every idea, derivation, example and exercise in the approved plan is present.
2. Definitions: every symbol and term is defined in this topic before its first use.
3. Steps: read each derivation and example line by line; a student can get each line from the one before
   with one named operation. Add any missing line.
4. Shortcuts: none of the banned phrases (the checker searches for them).
5. Consistency: every symbol follows the notation rules in section 8.
6. House standard: met for every idea.
7. Scope: nothing outside the syllabus.
8. LaTeX: all maths in delimiters; the checker passes.

## 8. Notation rules (Sadd's) and formula-sheet rows

- Indices $i,j,k,\dots$ run over $1,2,3$; a repeated index is summed; a comma is a partial derivative,
  $u_{i,j}=\partial u_i/\partial x_j$. Coordinates $x_1,x_2,x_3$ are also $x,y,z$.
- Displacement $u_i=(u,v,w)$. Strain $e_{ij}$ with components $e_x,e_y,e_z,e_{xy},e_{yz},e_{zx}$;
  engineering shear strain $\gamma_{xy}=2e_{xy}$. Rotation tensor $\omega_{ij}$, rotation vector $\omega_i$.
- Stress $\sigma_{ij}$ with components $\sigma_x,\sigma_y,\sigma_z,\sigma_{xy},\sigma_{yz},\sigma_{zx}$
  (Sadd writes shear stress as $\sigma_{xy}$, not $\tau_{xy}$). Traction $\mathbf{T}^{n}$, $T_i^{n}$.
  Body force per unit volume $F_i$.
- Rotation of axes: $Q_{ij}=\cos(x_i',x_j)$; primes mark components in the rotated axes.
- Invariants: $I_a, II_a, III_a$ for a general tensor $a_{ij}$; $\vartheta_1,\vartheta_2,\vartheta_3$ for
  strain with dilatation $\vartheta=e_{kk}$; $I_1,I_2,I_3$ for stress. Principal strains $e_1,e_2,e_3$;
  principal stresses $\sigma_1,\sigma_2,\sigma_3$, ranked $\sigma_1\ge\sigma_2\ge\sigma_3$ where order matters.
- Spherical parts carry a tilde ($\tilde e_{ij}$), deviatoric parts a hat ($\hat e_{ij}$).
- Elastic constants $\lambda$ (Lamé), $\mu$ (shear modulus; some texts write $G$), $E$, $\nu$,
  $k$ (bulk modulus); elasticity tensor $C_{ijkl}$; thermal expansion $\alpha$; temperature change $T-T_0$.
  $\lambda$ also names an eigenvalue in Chapter 1: say which meaning you use.
- Signs: normal stress and strain positive in tension or extension; a shear stress is positive on a positive
  face in a positive direction; a shear strain is positive when the right angle between the positive axes
  decreases.
- Units: stress in $\mathrm{Pa}=\mathrm{N\,m^{-2}}$ (usually $\mathrm{MPa}$, $\mathrm{GPa}$); strain is
  dimensionless.

**Formula-sheet rows.** `tN-symbols.html` contains only table rows, one per symbol you define:
`<tr><td>$e_{ij}$</td><td>small-strain tensor</td><td>dimensionless</td><td>4</td></tr>`
`tN-results.html` contains only rows, one per key result:
`<tr><td>$e_{ij}=\tfrac12\left(u_{i,j}+u_{j,i}\right)$</td><td>strain–displacement relations</td><td>(2.2.6)</td><td>4</td></tr>`

## 9. Plan file format (Phase 1)

For each of your topics, in Markdown:
- **Pages read**: PDF pages per chapter.
- **Ideas**: for each idea, the intuition picture you will use (one or two lines), and the derivation you
  will show as its sequence of steps with equation numbers, or "stated, not derived" with the reason.
- **Concept blocks**: for each block, the worked example (book reference and PDF page), its data exactly as
  read from the page (figure data included), and your verified answers; then the your-turn exercise (book
  reference and PDF page), its full statement as you will write it, and your verified answer.
- **Symbols** you will define.
- **Common mistakes** you will include, and why each one is real.
- **Looking ahead** (Writers B and C): each link with its section, equation numbers, the PDF page where you
  verified them, and the sentence saying how this topic is used there.
- **Risks or questions** for the coordinator: anything unreadable, anything in your brief that does not work.

Keep the plan to what the coordinator needs to check. No HTML in the plan.
