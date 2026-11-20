# Writer A plan: Topics 1, 2, 3 (Chapter 1)

Phase 1 plan, no HTML written. Every number below is checked in `notes-build/scripts/writer-A/a_topic1.py`, `a_topic2.py`, `a_topic3.py`
(run with `python -I`; all checks PASS, 0 FAIL). Conventions in this plan: matrices are written by rows, `[[row 1],[row 2],[row 3]]`;
"PDF p." is the Chapter 1 PDF page (book page minus 2); `e1,e2,e3` are the unit basis vectors; "Ex" is a book exercise.
This file is for you, so it uses Unicode maths; the fragments will be pure LaTeX.

## 0. Points that apply to all three topics

**How I read the book.** The Read tool cannot render PDF pages here (`pdftoppm` is missing). I rendered all 27 pages of the Chapter 1 PDF to
PNG (2433×3000 px) with Windows' built-in PDF renderer (`notes-build/scripts/writer-A/render_pdf.ps1`, usage in its header) and read every
page image, with zoomed crops for (1.5.1), Example 1.5, Exercises 1.1, 1.12, 1.14 to 1.16, the list (1.8.5), (1.8.8) to (1.8.11) and Exercise 1.18.
Nothing was unreadable. Every equation, sign and number below comes from those images, not from `book-text`.

**Python.** `python -I` hides the user site-packages where numpy and sympy are installed (`import numpy` fails under `-I`). My scripts add
`C:\Users\amy23\AppData\Roaming\Python\Python312\site-packages` to `sys.path` at the top and still run with `-I`. Writer B does the same.

**Misprints and convention clashes in the book** (all seen on the page image; each is checked by script):

| # | Where | The book prints | What I will write | Why |
|---|---|---|---|---|
| 1 | (1.5.1), third-order line, PDF p.8 | `a'_ijk = Q_ip Q_jp Q_kr a_pqr` | `Q_ip Q_jq Q_kr a_pqr` | `p` would appear three times (illegal); the other lines use `p,q,r` in order |
| 2 | Example 1.5, `∇u`, PDF p.23 | last coefficient `(1/r)(∂u_θ/∂θ − u_r)` on `ê_θ ê_θ` | `(1/r)(∂u_θ/∂θ + u_r)` | derived from (1.9.17) and (1.9.20), and checked by chain rule with generic `u_r(r,θ)`, `u_θ(r,θ)`; the test field `u = r ê_r` (= `x1 e1 + x2 e2`) must give `∇u = ê_r ê_r + ê_θ ê_θ`: `+u_r` gives coefficient 1, the printed `−u_r` gives −1 |
| 3 | Ex 1.18, spherical `∇·u`, PDF p.27 | no "+" between the 2nd and 3rd terms | insert "+" | checked against a Cartesian computation |
| 4 | (1.8.10), (1.8.11), PDF p.18 | plain `∫_C` for a closed curve | `∮_C` as in (1.8.8) | cosmetic |
| 5 | §1.1 stress matrix, PDF p.1 | shear stress written `τ_xy` | notes use `σ_xy` (your notation rules); Topic 1 does not print the matrix | – |
| 6 | `∇u` convention, PDF pp.16, 17, 22, 23 (the pages of (1.8.4), Example 1.4, (1.9.17), Example 1.5) | Cartesian (1.8.4) and Example 1.4: `∇u = u_i,j e_i e_j`, matrix row = component, column = derivative direction. Curvilinear (1.9.17) and Example 1.5: the first dyad vector is the derivative direction, so its coefficient matrix is the transpose | I state both and say which is which (Topic 3, Common mistake) | the book switches convention between §1.8 and §1.9 |


**Additions beyond the book's text.** The book states these without proof or does not give them; none is a derivation the exam is likely to ask for. My default is in the last column; tell me to flip any.

| | Addition | Length | Default |
|---|---|---|---|
| (a) | second-order law (1.5.1)₃ from the dyad (1.5.3); explains `Q a Qᵀ` | 3 lines | keep |
| (b) | `Q a Qᵀ` is diagonal when the rows of `Q` are eigenvectors (1.6.4) | 3 lines | keep |
| (c) | the diagonal entry in any direction lies between `λ3` and `λ1` (extremal property) | 2 lines | left out (state as in the book) |
| (d) | why `I, II, III` do not change with the axes | 1 line | left out (shown numerically in 2A) |
| (e) | why the cubic (1.6.2) has coefficients `I, II, III` | 4 lines | keep |
| (f) | `det Q = +1` for right-handed to right-handed; `ε_ijk` unchanged only then | 1 sentence | keep |
| (g) | physical component `u_<i>` and (1.9.7), needed because (1.9.14) to (1.9.16) use `u_<i>` | 2 lines | keep |

**Where the integral theorems go.** The book has no example or exercise for §1.8.1 to 1.8.4, and your brief gives idea 2 of Topic 3 no concept block.
A fourth concept would need its own worked example and your-turn box (the checker demands one of each per concept). My plan: put them in a short
sub-section "Integral theorems (stated)" at the end of the explanation of **3B**, with no extra worked example or your-turn. See question Q1.

## 1. Topic 1 · Index notation, Kronecker delta and the permutation symbol

**Pages read.** Chapter 1 PDF pp. 1 to 5 (§1.1 to 1.3), p. 4 (Example 1.1), pp. 14 to 15 (§1.7); exercises: PDF pp. 24 to 25 (Ex 1.1 to 1.5), p. 26 (Ex 1.15).
Eyebrow: `Chapter 1 · §1.1–1.3, 1.7 · Exam weight: medium (estimate)`.

**Where we are** (draft). First topic. The course builds towards three things: how a body deforms (strain), the internal forces in it (stress), and the
material law that links them. Each needs nine numbers at a point (six independent, §1.1), so without a shorthand the equations fill pages. This topic builds
the shorthand: index notation with the summation rule, and two special symbols, `δ_ij` and `ε_ijk`.

**What you need from earlier** (draft). There is no earlier topic (the checker needs this box). I will fill it with the school mathematics used, each restated:
row-times-column matrix product, transpose, the 3×3 determinant by expansion along the first row, `a·b = a1b1+a2b2+a3b3`, and `a×b` as a determinant.

### Ideas

1. **Tensors of order 0, 1, 2; index notation; free and dummy indices; summation convention; contraction; outer and inner products** (§1.1 to 1.2, PDF pp. 1 to 4).
   *Picture:* `a_i` is a list of three numbers and `a_ij` a 3×3 table (first index row, second index column). A repeated letter means "add over 1, 2, 3", and a letter
   that is not repeated is a slot you fill with 1, 2, 3, so `a_ij b_j = c_i` is three equations at once.
   *Derivation:* none, these are definitions (book gives none). I will list the four rules (an index appears once or twice in a term; free indices agree on both sides of `=`;
   a dummy index may be renamed; three or more equal indices, e.g. `a_iii`, are not allowed), plus `3^N` numbers for `N` indices, (1.2.1) to (1.2.6) (in (1.2.3) the book's scalar multiplier is `λ`; I write `c`, since `λ` is an eigenvalue in Topic 2 and Lamé's constant in Topic 9), outer
   product (1.2.4) and inner product `a_ij b_jk` as a contraction of `a_ij b_mk`. A small table "expression → free indices → scalar, vector or matrix".
2. **Symmetric and antisymmetric parts; (1.2.7) to (1.2.10); symmetric × antisymmetric = 0 (1.2.9).**
   *Picture:* fold the table along its diagonal. A symmetric table equals its mirror image; an antisymmetric one equals the mirror image with every sign flipped, so its
   diagonal is zero. Every table is half "sum with mirror" plus half "difference with mirror".
   *Derivation (examinable, shown):* (1.2.10) in 3 lines: add and subtract `½a_ji`; show `a_(ij)` is symmetric, `a_[ij]` antisymmetric, and `a_[ii] = 0`; counts 6 and 3.
   Proof of (1.2.9), 5 lines: let `A_mn = a_{ij…m…n…k}` and `B_mn = b_{pq…m…n…r}` with all other indices frozen, `A_mn = A_nm`, `B_mn = −B_nm`;
   `S = A_mn B_mn`; (i) rename the dummy pair `m↔n`: `S = A_nm B_nm`; (ii) `A_nm = A_mn`: `S = A_mn B_nm`; (iii) `B_nm = −B_mn`: `S = −A_mn B_mn = −S`; (iv) `2S = 0`.
   (This also covers book Ex 1.3.)
3. **δ_ij and its substitution rule (1.3.1), (1.3.2); ε_ijk (1.3.3); determinants (1.3.4); ε–δ identity (1.3.5) and its contraction; products in index form (1.7.1) to (1.7.7)** (§1.3 and §1.7, PDF pp. 5, 14 and 15).
   *Picture:* `δ_ij` is the identity matrix; contracting with it just renames an index (it "eats" the repeated index). `ε_ijk` keeps the sign of the order: `+1` for 123, 231, 312;
   `−1` for 321, 132, 213; `0` if any index repeats (3 plus, 3 minus, 21 zeros). It builds cross products and determinants.
   *Derivation (examinable, shown):* the contracted identity from (1.3.5) in 7 lines. (1.3.5) itself is stated without proof in the book, I use it as given and say so.
   (i) (1.3.5): `ε_ijk ε_pqr = det[[δ_ip, δ_iq, δ_ir],[δ_jp, δ_jq, δ_jr],[δ_kp, δ_kq, δ_kr]]`;
   (ii) expand along the first row: `δ_ip(δ_jq δ_kr − δ_jr δ_kq) − δ_iq(δ_jp δ_kr − δ_jr δ_kp) + δ_ir(δ_jp δ_kq − δ_jq δ_kp)`;
   (iii) set `p = i` and sum (contraction), left side becomes `ε_ijk ε_iqr`;
   (iv) term 1: `δ_ii = 3`, giving `3(δ_jq δ_kr − δ_jr δ_kq)`;
   (v) term 2: `δ_iq δ_ji = δ_jq`, `δ_iq δ_ki = δ_kq`, giving `−(δ_jq δ_kr − δ_jr δ_kq)`;
   (vi) term 3: `δ_ir δ_ji = δ_jr`, `δ_ir δ_ki = δ_kr`, giving `δ_jr δ_kq − δ_jq δ_kr = −(δ_jq δ_kr − δ_jr δ_kq)`;
   (vii) add: `(3−1−1)(δ_jq δ_kr − δ_jr δ_kq)`; rename `q→m, r→n`: **`ε_ijk ε_imn = δ_jm δ_kn − δ_jn δ_km`**. Check: setting `m=j, n=k` gives `ε_ijk ε_ijk = 9 − 3 = 6`, the six non-zero entries.
   Also shown: the shifted form `ε_kij ε_kpq = δ_ip δ_jq − δ_iq δ_jp` (the repeated index must sit in the same place in both `ε`; cyclic shifts change no sign), used in 1C and 3B.
   `δ_ij a_j = a_i` written out (only the term `j = i` survives); `(a×b)_1 = ε_1jk a_j b_k = a2b3 − a3b2` matching the determinant (1.7.3); (1.7.1) to (1.7.7) stated as index forms.
   Verified numerically: (1.3.5) for all 729 index choices, the contraction for all 81, the three terms `3X, −X, −X`, the shifted form.

### Concept blocks

**1A · Index notation (idea 1).**

*Worked example · Book Example 1.1, first part (PDF p. 4).* Data as read: `a_ij = [[1,2,0],[0,4,3],[2,1,2]]`, `b_i = (2,4,0)ᵀ` (column).
Quantities asked: `a_ii, a_ij a_ij, a_ij a_jk, a_ij b_j, a_ij b_i b_j, b_i b_i, b_i b_j`, each labelled scalar, vector or matrix.
Steps (8): data and the rule "free indices decide the type", then one step per quantity, each with its free/dummy analysis as the reason.
Verified answers (match the book's printed values):
`a_ii = 7` (scalar); `a_ij a_ij = 1+4+0+0+16+9+4+1+4 = 39` (scalar); `a_ij a_jk = [[1,10,6],[6,19,18],[6,10,7]]` (matrix; one entry shown in full, `(1,2): 1·2+2·4+0·1 = 10`);
`a_ij b_j = (10,16,8)ᵀ` (vector); `a_ij b_i b_j = 2·10+4·16+0·8 = 84` (scalar); `b_i b_i = 4+16+0 = 20` (scalar); `b_i b_j = [[4,8,0],[8,16,0],[0,0,0]]` (matrix).
Check: `a_ij b_i b_j` computed term by term and as `b·(a b)` agree.

*Your turn · Book Exercise 1.1(b) (PDF pp. 24 to 25).* Statement as I will write it: the same seven quantities for `a_ij = [[1,2,0],[0,2,1],[0,4,2]]`, `b_i = (2,1,1)ᵀ`; "say for each whether it is a scalar, a vector or a matrix; `a_ij b_j` is the matrix product `[a]{b}` and `a_ij a_jk` is `[a][a]`".
Data as read (zoomed): case (b) is `[[1,2,0],[0,2,1],[0,4,2]]` and `(2,1,1)`.
Hint: decide the type from the free indices, then sum over the repeated index.
Verified answer: `a_ii = 1+2+2 = 5` (scalar); `a_ij a_ij = 1+4+0+0+4+1+0+16+4 = 30` (scalar); `a_ij a_jk = [[1,6,2],[0,8,4],[0,16,8]]` (matrix); `a_ij b_j = (4,3,6)ᵀ` (vector);
`a_ij b_i b_j = 2·4+1·3+1·6 = 17` (scalar); `b_i b_i = 6` (scalar); `b_i b_j = [[4,2,2],[2,1,1],[2,1,1]]` (matrix).

**1B · Symmetric and antisymmetric parts (idea 2).**

*Worked example · Book Example 1.1, second part (PDF p. 4)*, with the proof of (1.2.9) shown in the explanation above it. Same `a_ij` as 1A. Steps (8): form `a_ji`; `a_ij + a_ji = [[2,2,2],[2,8,4],[2,4,4]]`;
halve to `a_(ij) = [[1,1,1],[1,4,2],[1,2,2]]`; `a_ij − a_ji = [[0,2,−2],[−2,0,2],[2,−2,0]]`; halve to `a_[ij] = [[0,1,−1],[−1,0,1],[1,−1,0]]`; check symmetric, and antisymmetric with zero diagonal;
check `a_(ij) + a_[ij] = a_ij`; illustrate (1.2.9): the nine products `a_(ij) a_[ij]` are `0, 1, −1, −1, 0, 2, 1, −2, 0`, sum `0`.

*Your turn · Book Exercise 1.2 with the matrix of Exercise 1.1(b) only (PDF p. 25).* Statement: "Use (1.2.10) to write `a_ij = [[1,2,0],[0,2,1],[0,4,2]]` (case (b) of Exercise 1.1) as the sum of a symmetric and an antisymmetric matrix. Check that `a_(ij)` has six independent components and `a_[ij]` has zero diagonal and three independent components."
Hint: form `a_ji` first.
Verified answer: `a_(ij) = [[1,1,0],[1,2,5/2],[0,5/2,2]]` (independent entries 1, 1, 0, 2, 5/2, 2), `a_[ij] = [[0,1,0],[−1,0,−3/2],[0,3/2,0]]` (independent entries 1, 0, −3/2), sum `= a_ij`;
extra check from (1.2.9): the nine products are `0, 1, 0, −1, 0, −15/4, 0, 15/4, 0`, sum `0`.

**1C · δ, ε, determinants and the ε–δ identity (idea 3).**

*Worked example · Book Exercise 1.15, solved* (PDF p. 26; the book has no worked example here). Sign convention as printed: the dual vector of an antisymmetric `a_jk` is `a_i = −½ ε_ijk a_jk`; to show `a_jk = −ε_ijk a_i`.
Steps (8): (1) state the goal, `a_kj = −a_jk`; (2) write out `a_1 = −½(ε_123 a_23 + ε_132 a_32) = −½(a_23 − a_32) = −a_23`, and likewise `a_2 = −a_31`, `a_3 = −a_12` (so `a_i` holds the three independent entries; this is the "3" of 1B);
(3) multiply the definition by `ε_ipq`: `ε_ipq a_i = −½ ε_ipq ε_ijk a_jk`; (4) contracted identity (repeated index first in both): `ε_ipq ε_ijk = δ_pj δ_qk − δ_pk δ_qj`; (5) substitute; (6) δ rule term by term: `ε_ipq a_i = −½(a_pq − a_qp)`;
(7) antisymmetry `a_qp = −a_pq` gives `−a_pq`, so `a_pq = −ε_ipq a_i`, rename `p→j, q→k`; (8) numeric check with `a_[ij]` of Example 1.1 (`[[0,1,−1],[−1,0,1],[1,−1,0]]`): `a_i = (−1,−1,−1)`, rebuilding gives `a_12 = −ε_312 a_3 = 1`, `a_23 = 1`, `a_31 = 1`. (General check by script: `[[0,p,q],[−p,0,r],[−q,−r,0]]` has dual `(−r, q, −p)`.)
I will add one sentence that this dual vector returns in Topic 4 as the rotation vector (your outline's thread), without quoting a Chapter 2 equation.

*Your turn · Book Exercise 1.5 (PDF p. 25).* Statement: "Expand `det[a_ij] = ε_ijk a_1i a_2j a_3k = ε_ijk a_i1 a_j2 a_k3` (1.3.4) term by term and show that each form gives the traditional expansion of the determinant."
Hint: of the 27 triples `(i,j,k)` only six have `ε ≠ 0`; list them with their signs.
Verified answer (script prints all twelve terms): row form `+a11a22a33 −a11a23a32 −a12a21a33 +a12a23a31 +a13a21a32 −a13a22a31`; column form (triples 123, 132, 213, 231, 312, 321) `+a11a22a33 −a11a23a32 −a12a21a33 +a13a21a32 +a12a23a31 −a13a22a31`: the same six products with the same signs, equal to
`a11(a22a33 − a23a32) − a12(a21a33 − a23a31) + a13(a21a32 − a22a31)`.
**Symbols (Topic 1).** `a_i, b_i` (components of a vector, 3 numbers); `a_ij` (matrix, 9 numbers); `a_{ij…k}` (`N` indices, `3^N` numbers); `i, j, k, …` (indices, range 1 to 3); `e_i` (unit basis vectors); `δ_ij`; `ε_ijk`; `a_(ij), a_[ij]`; `a·b, a×b, |a|`;
`A, [A], Aᵀ, tr A, det[a_ij]`; `a_i` as the dual vector in 1C. Units: none (pure numbers).

**Common mistakes (Topic 1)**, each shown wrong then right:
(i) index rules broken: `a_ij b_j = c_j` (free index `i` on the left, `j` on the right) or three equal indices; real because the book itself warns about `a_i = b_j` and `a_iii` (PDF p. 3);
(ii) `δ_ii = 1`: it is 3 (the 1 is the "no sum" case `δ_ii` underlined, (1.3.2));
(iii) `a_ij a_ij` is a scalar (39 in Example 1.1) but `a_ij a_jk` is a matrix, and `b_i b_i = 20` is a scalar while `b_i b_j` is a matrix: same letters, different objects;
(iv) the `ε–δ` contraction needs the repeated index in the same position in both `ε` (cycle first, no sign change) and the second term carries the minus sign.

**What comes next (draft).** Topic 2 uses `δ_ij` and the summation rules to find how the components `a_i` and `a_ij` change when the axes are rotated.

## 2. Topic 2 · Coordinate transformations, Cartesian tensors and principal values

**Pages read.** Chapter 1 PDF pp. 6 to 13 (§1.4 to 1.6), Example 1.2 (pp. 9 to 10, figure p. 10), Example 1.3 (pp. 12 to 13, figure p. 13); exercises: PDF p. 25 (Ex 1.6, 1.8, 1.9), p. 26 (Ex 1.12).
Eyebrow: `Chapter 1 · §1.4–1.6 · Exam weight: high (estimate)`.

**Where we are** (draft). Topic 1 gave the shorthand but kept one fixed set of axes. A vector, or the state of stress at a point, is a physical thing; its components depend on the axes chosen. This topic answers two
questions: how do the components change when the axes are rotated (transformation laws), and is there a best set of axes (principal axes, in which a symmetric tensor is diagonal)?

**What you need from earlier** (from Topic 1, each restated in full): summation rule and free/dummy indices; `δ_ij` (1.3.1) and the substitution rule (1.3.2); `ε_ijk` (1.3.3); matrix products in index form (1.7.6)
(`AB = A_ij B_jk`, `ABᵀ = A_ij B_kj`, `AᵀB = A_ji B_jk`); transpose and trace (1.7.7); determinant (1.3.4); symmetric tensor (1.2.7).

### Ideas

1. **Q_ij, `e_i' = Q_ij e_j`, `v_i' = Q_ij v_j`, `v_i = Q_ji v_j'`, orthogonality, `det Q = ±1`** (§1.4, PDF pp. 6 to 7).
   *Picture:* one arrow, two sets of axes. The arrow does not change, only its projections on the axes do. Row `i` of `Q` is the new axis `x_i'` written in the old axes; `Q_ij = cos(x_i', x_j)` (first index new axis, second old axis).
   *Derivation (all shown, nine lines):* (a) `e_i'·e_j = cos(x_i', x_j) = Q_ij` for unit vectors, so `e_i' = Q_ij e_j` (1.4.1) to (1.4.3); (b) the same with roles swapped, `e_i = Q_ji e_j'` (1.4.4); (c) `v = v_i e_i = v_i' e_i'` (1.4.5);
   (d) put (1.4.4) in `v = v_i e_i`: `v = v_i Q_ji e_j'`, compare the coefficient of `e_j'` with `v = v_j' e_j'`, rename: `v_i' = Q_ij v_j` (1.4.6); (e) put (1.4.3) in `v = v_i' e_i'` and compare with `v = v_j e_j`: `v_i = Q_ji v_j'` (1.4.7);
   (f) put (1.4.6) into (1.4.7): `v_i = Q_ji Q_jk v_k` (1.4.8); write `v_i = δ_ik v_k`; `(Q_ji Q_jk − δ_ik) v_k = 0` for every `v`, choose `v = e1, e2, e3` in turn so each column of the bracket vanishes: `Q_ji Q_jk = δ_ik` (1.4.9);
   (g) the same elimination the other way (carried out in full a second time, not "similarly"): put (1.4.7) into (1.4.6): `v_i' = Q_ij Q_kj v_k'`, so `Q_ij Q_kj = δ_ik` (1.4.10); (h) matrix form `Q Qᵀ = I`, `det(QQᵀ) = (det Q)² = 1`, so `det Q = ±1` (1.4.11).
   Meaning: rows of `Q` are orthonormal, `Q⁻¹ = Qᵀ`, so `v' = Qv` is undone by `v = Qᵀv'`; `det Q = +1` for a right-handed frame turned into a right-handed frame (addition (f)), `−1` includes a reflection.
2. **Tensors of any order (1.5.1); tensor versus components; dyadic form (1.5.3); isotropic tensors** (§1.5, PDF pp. 8 to 9).
   *Picture:* a tensor is the physical object (stress at a point); components are its shadows on the chosen axes and each index casts its own shadow, so each index gets one `Q`. "Isotropic" means identical components from every set of axes, like a sphere or a pressure.
   *Derivation:* (1.5.1) is stated without proof in the book. I add the 3-line derivation for second order (addition (a)): `A = A_pq e_p e_q`, `A'_ij = e_i'·A·e_j' = A_pq (e_i'·e_p)(e_q·e_j') = Q_ip Q_jq A_pq`, then matrix form `a' = Q a Qᵀ` (since `Q_jq = (Qᵀ)_qj`, (1.7.6)).
   I write (1.5.1) with `Q_jq` in the third-order line (misprint 1). Isotropic: `δ_ij` proved (block 2B); `ε_ijk` stated ("found to be" in the book, no proof), with the remark that it is unchanged only for `det Q = +1`
   (`Q_ip Q_jq Q_kr ε_pqr = det(Q) ε_ijk`, script-checked, addition (f)); the fourth-order form `α δ_ij δ_kl + β δ_ik δ_jl + γ δ_il δ_jk` is stated as in Ex 1.9 and verified in the your-turn of 2B.
3. **Principal values and directions; invariants; diagonal form; extremal property** (§1.6, PDF pp. 10 to 13).
   *Picture:* look for the axes along which the tensor only stretches: for such `n` the tensor sends `n` to `λn` with no turning; in those axes the table is diagonal. (The book's picture: turn `x3` onto a vector and its components become `(0,0,|v|)`, PDF p. 10.)
   *Derivation (shown, ten lines):* (a) `a_ij n_j = λ n_i` (1.6.1), with the warning that `λ` here is an eigenvalue (principal value), not Lamé's constant; (b) with `n_i = δ_ij n_j`: `(a_ij − λδ_ij) n_j = 0`, three linear homogeneous equations,
   non-trivial `n` only if `det[a_ij − λδ_ij] = 0`; (c) expansion `−λ³ + I_a λ² − II_a λ + III_a = 0` (1.6.2), with `I_a = a_ii`, `II_a = ½(a_ii a_jj − a_ij a_ij)` = sum of the three 2×2 principal minors, `III_a = det[a_ij]` (1.6.3), and a one-paragraph reason for the coefficients (addition (e));
   (d) real roots and orthogonal directions for symmetric `a_ij` (stated, "it can be shown" in the book), the three cases (distinct; `λ1 ≠ λ2 = λ3`, then `n(1)` unique and every direction perpendicular to it is principal; all equal, then every direction is principal and the tensor is isotropic);
   (e) finding directions: for each root solve `(a − λ_k I) n = 0`, two independent equations fix the direction, normalise `n·n = 1`, sign free, choose signs so that `n(1)×n(2) = n(3)` (right-handed, `det Q = +1`);
   (f) principal axes: rows of `Q` are `n(1), n(2), n(3)` because `Q_ij = e_i'·e_j` (book, PDF p. 13);
   (g) proof that `a' = Q a Qᵀ` is diagonal (1.6.4), addition (b): `a'_ij = n(i)_p a_pq n(j)_q = n(i)·(a n(j)) = λ_j n(i)·n(j) = λ_j δ_ij`; (h) (1.6.5) by evaluating (1.6.3) on `diag(λ1,λ2,λ3)` (this is book Ex 1.11), and why `I, II, III` are the same in every frame (addition (d));
   (i) extremal property: for a unit `n` the diagonal entry in direction `n` is `n·a·n = Σ λ_k (n·n(k))²`, a weighted average (weights `≥ 0`, sum 1) of the `λ_k`, so it lies between `λ3` and `λ1` (addition (c); script-checked over 2000 random rotations of Example 1.3's tensor).

### Concept blocks

**2A · Rotation of axes, laws for vectors and matrices (ideas 1 and 2).**

*Worked example · Book Example 1.2 (PDF pp. 9 to 10).* Data as read: `a_i = (1,4,2)ᵀ`, `a_ij = [[1,0,3],[0,2,2],[3,2,4]]`; new frame by a rotation of 60° (π/3) about `x3`, the book's wording "counterclockwise when viewing down the negative x3-axis (Figure 1.2)".
Figure 1.2 as read: `x3` up, `x2` to the right, `x1` towards the lower left; dashed `x3'` coincides with `x3`; the dashed `x1'`, `x2'` are `x1`, `x2` turned by 60° about `x3`, the 60° arc is drawn between `x1` and `x1'`, and `x1'` lies on the `x2` side of `x1`.
The book's `Q` (printed as cosines): `[[cos60°, cos30°, cos90°],[cos150°, cos60°, cos90°],[cos90°, cos90°, cos0°]] = [[1/2, √3/2, 0],[−√3/2, 1/2, 0],[0,0,1]]` (script-checked equal).
Steps (8): (1) describe the rotation in words and read the angles; (2) fill `Q` row by row, explaining 30° and 150°; (3) check `Q` (rows orthonormal, `det Q = 1/4 + 3/4 = 1`); (4) restate (1.5.1)₂ and substitute; (5) evaluate; (6) restate (1.5.1)₃, matrix form `Q a Qᵀ`, first product `Q a`; (7) second product; (8) checks.
Verified answers (match the book): `a_i' = (1/2 + 2√3, 2 − √3/2, 2) ≈ (3.964, 1.134, 2)`; `Q a = [[1/2, √3, 3/2+√3],[−√3/2, 1, 1−3√3/2],[3,2,4]]`;
`a'_ij = [[7/4, √3/4, 3/2+√3],[√3/4, 5/4, 1−3√3/2],[3/2+√3, 1−3√3/2, 4]] ≈ [[1.750, 0.433, 3.232],[0.433, 1.250, −1.598],[3.232, −1.598, 4]]`.
Checks: `|a'|² = (1/2+2√3)² + (2−√3/2)² + 4 = 21 = 1+16+4`; trace `7/4+5/4+4 = 7 = 1+2+4`; `I, II, III = 7, 1, −14` before and after; inverse `Qᵀ a' = a`; and the wrong order `Qᵀ a Q` gives `[[7/4, −√3/4, …]]` (sign of the off-diagonal flipped), used in Common mistake.
One simple SVG (x1–x2 plane seen from +x3, `x1'` at 60° counterclockwise from `x1`), plain letters only.

*Your turn · Book Exercise 1.6, case (b) data (PDF p. 25).* Statement: "Take case (b) of Exercise 1.1: `a_ij = [[1,2,0],[0,2,1],[0,4,2]]`, `b_i = (2,1,1)ᵀ` ('case (b) data'). Find their components in the frame obtained by rotating the axes through 45° (π/4) about `x1`, in the positive sense of Example 1.2
(about `x3` that rotation carried `x1` towards `x2`; the same cyclic order about `x1` carries `x2` towards `x3`)."
Hint: `x1' = x1`; `x2'` makes 45° with `x2` and 45° with `x3`; `x3'` makes 135° with `x2` and 45° with `x3`; fill `Q` from these cosines, then use (1.5.1)₂ and (1.5.1)₃.
Verified answer: `Q = [[1,0,0],[0,√2/2,√2/2],[0,−√2/2,√2/2]]`, `det Q = 1`; `b' = (2, √2, 0)`; `Q a = [[1,2,0],[0,3√2,3√2/2],[0,√2,√2/2]]`; `a' = [[1, √2, −√2],[0, 9/2, −3/2],[0, 3/2, −1/2]] ≈ [[1, 1.414, −1.414],[0, 4.5, −1.5],[0, 1.5, −0.5]]`.
Checks: `|b'|² = 6 = |b|²`; trace `5` both; `det = 0` both; `(a b)' = a' b'`. (`a` is not symmetric here, so `a'` is not either.)

**2B · Isotropic tensors (idea 2).**

*Worked example · Book Exercise 1.8, solved (PDF p. 25).* The book writes the constant as `a`; I write `α` so that `a_ij` stays free for a general tensor, and say so. Steps (7): (1) the claim and the meaning of "isotropic"; (2) restate (1.5.1)₃; (3) substitute `a_pq = α δ_pq`; (4) δ rule `δ_pq Q_jq = Q_jp`;
(5) restate (1.4.10) `Q_ip Q_jp = δ_ij`; (6) conclude `a'_ij = α δ_ij`; (7) numeric check with `Q` of Example 1.2 (entry (1,1): `α(1/4+3/4) = α`; entry (1,2): `α(−√3/4+√3/4) = 0`). Script: `Q(αI)Qᵀ = αI` for an exact 60°-then-45° rotation and for the 2D rotation with symbolic angle.

*Your turn · Book Exercise 1.9 (PDF p. 25).* Statement: "`C_ijkl = α δ_ij δ_kl + β δ_ik δ_jl + γ δ_il δ_jk` with arbitrary constants `α, β, γ` is the most general fourth-order isotropic tensor. Verify that it keeps this form under the transformation law (1.5.1)₅, `C'_ijkl = Q_ip Q_jq Q_kr Q_ls C_pqrs`."
Hint: transform each of the three terms separately; apply the δ rule to each pair of `δ` and (1.4.10) twice.
Verified answer (script checks each term and the whole): term 1 gives `(Q_ip Q_jp)(Q_kr Q_lr) = δ_ij δ_kl`; term 2 (`δ_pr δ_qs`) gives `(Q_ip Q_kp)(Q_jq Q_lq) = δ_ik δ_jl`; term 3 (`δ_ps δ_qr`) gives `(Q_ip Q_lp)(Q_jq Q_kq) = δ_il δ_jk`; so `C'_ijkl = C_ijkl` with the same `α, β, γ`.

**2C · Principal values and directions (idea 3).**

*Worked example · Book Example 1.3 (PDF pp. 12 to 13).* Data as read: `a_ij = [[2,0,0],[0,3,4],[0,4,−3]]`. Figure 1.3 as read: principal axes `x1'` along `n(1)` (up and to the right), `x2'` along `x1`, `x3'` along `n(3)` (down and in front).
Steps (10): (1) symmetric, so real roots and orthogonal directions; (2) `I = 2+3−3 = 2`; (3) `II = (6) + (−25) + (−6) = −25` from the three 2×2 minors, `III = 2(−9−16) = −50`; (4) `−λ³+2λ²+25λ−50 = −(λ−2)(λ²−25) = 0`, roots `λ = 5, 2, −5`, ranked `λ1 > λ2 > λ3`, all distinct, check against (1.6.5): sum 2, pair sum `10−10−25 = −25`, product −50;
(5) `λ1 = 5`: as printed `−3n1 = 0`, `−2n2+4n3 = 0`, `4n2−8n3 = 0`, so `n(1) = ±(2e2+e3)/√5`; (6) `λ2 = 2`: rows `(0,0,0)`, `n2+4n3 = 0`, `4n2−5n3 = 0`, so `n2 = n3 = 0`, `n(2) = ±e1`; (7) `λ3 = −5`: `7n1 = 0`, `8n2+4n3 = 0`, `4n2+2n3 = 0`, so `n(3) = ±(e2−2e3)/√5`;
(8) mutually orthogonal, and `n(1)×n(2) = n(3)` with the + signs (right-handed); (9) `Q` with these as rows, `[[0, 2/√5, 1/√5],[1,0,0],[0,1/√5,−2/√5]]` (the book's, "the eigenvectors actually form the rows of the Q matrix"); (10) `Q a = [[0, 2√5, √5],[2,0,0],[0,−√5, 2√5]]`, then `(Qa)Qᵀ = diag(5, 2, −5)` as (1.6.4); trace 2 and det −50 kept.
All printed values reproduced by script.

*Your turn · Book Exercise 1.12(d) (PDF p. 26).* Statement: "For `a_ij = [[6,−3,0],[−3,6,0],[0,0,6]]` find the invariants, the principal values and the principal directions. Take the principal directions as the rows of `Q_ij` (a right-handed set), rotate `a_ij` into the principal axes with (1.5.1)₃, and show that the result is diagonal. (The book gives the principal values as 3, 6, 9.)"
My reading was checked: the four matrices of Ex 1.12 reproduce the book's printed answers `−2,0,1`; `−3,−1,0`; `−2,0,0`; `3,6,9` by script.
Hint: expand `det[a_ij − λδ_ij]` using the block structure (the third row and column are decoupled); solve `(a − λI)n = 0` for each root; if `det Q = −1`, reverse one direction.
Verified answer: `I = 18`; `II = 27+36+36 = 99`; `III = 162`; `−λ³+18λ²−99λ+162 = −(λ−3)(λ−6)(λ−9)`, so `λ = 9, 6, 3` (ranked; the book lists 3, 6, 9).
Directions: `λ=9`: `−3n1−3n2 = 0`, `n3 = 0`, `n(1) = (1,−1,0)/√2`; `λ=6`: `n1 = n2 = 0`, `n(2) = (0,0,1)`; `λ=3`: `n1 = n2`, `n3 = 0`, `±(1,1,0)/√2`, and since `n(1)×n(2) = (−1,−1,0)/√2` the right-handed choice is `n(3) = (−1,−1,0)/√2` (the other sign gives `det Q = −1`, still diagonal but left-handed).
`Q = [[1/√2, −1/√2, 0],[0,0,1],[−1/√2, −1/√2, 0]]`, `det Q = 1`; `Q a = [[9/√2, −9/√2, 0],[0,0,6],[−3/√2, −3/√2, 0]]`; `Q a Qᵀ = diag(9, 6, 3)`. (In the book's order 3, 6, 9: rows `(1,1,0)/√2, e3, (1,−1,0)/√2`, which is already right-handed, giving `diag(3,6,9)`.)

**Symbols (Topic 2).** `x_i, x_i'` (coordinates in old and new axes, m); `e_i, e_i'`; `Q_ij` (direction cosines, dimensionless); `Q, Qᵀ`; `v_i, v_i'`; `a_ij, a'_ij`; `λ` (eigenvalue or principal value, not Lamé's constant);
`n_i, n` (unit principal direction), `n(k)`, `λ_k`; `I_a, II_a, III_a`; `α, β, γ` (constants of the isotropic fourth-order tensor, not the thermal expansion coefficient); `C_ijkl` (name used in Ex 1.10 for the same tensor).

**Common mistakes (Topic 2).** (i) Transposes: `v' = Qv` but `v = Qᵀv'`; `a' = Q a Qᵀ`, not `Qᵀ a Q` (that is the inverse rotation: in Example 1.2 it flips the sign of the off-diagonal `√3/4`) and not `Q a Q`; first index of `Q_ij` is the new axis, second the old (`Q_21 = cos150°`, negative).
(ii) Eigenvectors put in as columns instead of rows of `Q` (linear-algebra habit; the book stresses rows, PDF p. 13). (iii) Eigenvectors not normalised, or a left-handed set (`det Q = −1`): a direction from `(a−λI)n = 0` has no length and no sign.
Real because they change the numbers in Example 1.2 and Example 1.3 exactly as shown by script.

**What comes next (draft).** Topics 5, 7 and 8 use these laws and the principal-value method word for word: strain transformation, stress transformation, principal strains and principal stresses (as in your writer brief; your page outline also names Topic 3 here, see Q6). Topic 9's use of the isotropic fourth-order tensor is said in block 2B.

## 3. Topic 3 · Tensor calculus and curvilinear coordinates

**Pages read.** Chapter 1 PDF pp. 15 to 25 (§1.8 to 1.9), Example 1.4 (p. 17), Example 1.5 (p. 23, figure p. 24); exercises: PDF p. 26 (Ex 1.14, 1.16, 1.17), p. 27 (Ex 1.18, used only for the spherical statements).
Eyebrow: `Chapter 1 · §1.8–1.9 · Exam weight: medium (estimate)`.

**Where we are** (draft). Topic 2 treated a tensor at one point. In a loaded body the components change from point to point, so they are fields, and we must differentiate and integrate them, in Cartesian axes and in the polar, cylindrical and spherical coordinates used for round bodies. This topic gives the rules.

**What you need from earlier.** From Topic 1: summation rule; `δ_ij` and `ε_ijk`; the contracted identity `ε_kij ε_kpq = δ_ip δ_jq − δ_iq δ_jp`; the result that symmetric × antisymmetric sums to zero (1.2.9); `(a×b)_i = ε_ijk a_j b_k` (1.7.3), `a·b = a_i b_i` (1.7.1).
From Topic 2: the basis change `e_i' = Q_ij e_j` (1.4.3) with orthonormal rows (1.4.10), reused for the curvilinear basis (1.9.5), (1.9.7).

### Ideas

1. **Fields, comma notation, `df/ds = n·∇f`, `∇f`, `∇·u`, `∇×u`, `∇²`, identities** (§1.8, PDF pp. 15 to 17).
   *Picture:* a field gives a number or an arrow at every point (temperature in a room). A comma means "rate of change in the `x_j` direction"; `∇f` points uphill and `n·∇f` is the slope when you walk in direction `n`; `∇·u` is net outflow per unit volume (a source strength), `∇×u` is local spin.
   *Derivation:* (1.8.1) in 4 lines: chain rule `df/ds = (∂f/∂x)(dx/ds) + (∂f/∂y)(dy/ds) + (∂f/∂z)(dz/ds)`; the unit tangent is `n = (dx/ds, dy/ds, dz/ds)` because `ds² = dx²+dy²+dz²`; recognise a dot product; define `∇f` (1.8.2), `∇` (1.8.3).
   A free derivative index raises the order by one (stated as in the book, PDF p. 15): `a_i,j` is a matrix, written out. Index forms (1.8.4) are definitions; I check the curl component `(∇×u)_1 = ε_1jk u_k,j = u_3,2 − u_2,3` against the determinant form. The ten identities (1.8.5) are proved in 3B (four of them in full).
2. **Integral theorems (1.8.6) to (1.8.12)** (PDF pp. 18 to 19).
   *Picture:* divergence: total outflow through a closed surface equals the sum of the sources inside; Stokes: circulation round a loop equals the total spin through any surface it bounds; Green: the plane special case; zero-value: if the integral vanishes over every region, the integrand vanishes everywhere.
   *Derivation:* stated, not derived (the book "simply lists" them, PDF p. 18; their proofs belong to vector calculus). Meaning and conditions (continuity, outer unit normal, positive sense with `S` on the left) as printed. Later use: Topic 8 uses the divergence theorem (1.8.7) and the zero-value theorem (1.8.12) to turn a force balance into the equilibrium equations; Topic 6 uses Stokes (1.8.8), (1.8.9).
3. **Orthogonal curvilinear coordinates: (1.9.1), (1.9.2); scale factors (1.9.4), (1.9.6); basis (1.9.5), (1.9.7); basis derivatives (1.9.10); `∇, ∇f, ∇·u, ∇²f, ∇×u` (1.9.12) to (1.9.16); the polar case in full** (§1.9, PDF pp. 19 to 25).
   *Picture:* "east" and "north" change as you walk round a circle: `ê_r` and `ê_θ` turn with `θ`, while `e1, e2` never do. Differentiating a vector field therefore also differentiates its basis vectors, and that is where the extra terms come from. A step `dθ` moves you a distance `r dθ`, so the scale factor for `θ` is `r`.
   *Derivation:* (1.9.6) from (1.9.5) and `ê_i·ê_i = 1` in two lines; scale factors by script from (1.9.6): cylindrical `h = (1, r, 1)`, spherical `(R, φ, θ)` `h = (1, R, R sin φ)` (Ex 1.18, derivation shown in three lines for `∂x/∂R, ∂x/∂φ, ∂x/∂θ`); general operators (1.9.12) to (1.9.16) and `∇u` (1.9.17) stated as in the book (their proofs are not in the book);
   the physical component `u_<i>` defined (addition (g)); the polar case worked in full in block 3C. (1.9.18), `∇²u` in general curvilinear form, is not reproduced; the polar form is in the example.
   Spherical operators: I will state (1.9.2), the `h`'s and, in Key results, `∇f, ∇·u, ∇²f, ∇×u` as printed in Ex 1.18 with the missing "+" restored (misprint 3). See Q4.
   One simple SVG (polar axes with `ê_r, ê_θ` at angle `θ`, PDF p. 24).

### Concept blocks

**3A · Gradient, divergence, curl, Laplacian in Cartesian axes (idea 1).**

*Worked example · Book Example 1.4 (PDF p. 17).* Data as read: `φ = x² − y²`, `u = 2x e1 + 3yz e2 + xy e3` (with `x, y, z = x1, x2, x3`). Asked: `∇φ, ∇²φ, ∇·u, ∇u, ∇×u`.
Steps (7): (1) data and the index forms (1.8.4); (2) `∇φ = φ,i e_i`; (3) `∇²φ = φ,ii`; (4) `∇·u = u_i,i`; (5) `∇u = u_i,j`, row = component, column = derivative, written as a matrix; (6) `∇×u = ε_ijk u_k,j e_i` component by component, then the determinant form as a check; (7) checks.
Verified answers (match the book): `∇φ = 2x e1 − 2y e2`; `∇²φ = 2 − 2 = 0`; `∇·u = 2 + 3z + 0 = 2 + 3z`; `∇u = [[2,0,0],[0,3z,3y],[y,x,0]]`; `∇×u = (x − 3y) e1 − y e2` (components `u_3,2 − u_2,3 = x − 3y`; `u_1,3 − u_3,1 = 0 − y`; `u_2,1 − u_1,2 = 0`).
Checks: `tr(∇u) = 2+3z = ∇·u`; at `(1,0)`, `∇φ = 2 e1` is perpendicular to the contour `φ = 1`, which runs along `e2` there (the book's Figure 1.4 remark); `∇²u = 0` for this `u`.

*Your turn · Book Exercise 1.14(a) (PDF p. 26).* Statement: "For `u = x1 e1 + x1x2 e2 + 2x1x2x3 e3` calculate `∇·u`, `∇×u`, `∇²u`, `∇u` and `tr(∇u)`."
Hint: `∇u` is the matrix of all nine `∂u_i/∂x_j`; the other four follow from it or from (1.8.4).
Verified answer: `∇·u = 1 + x1 + 2x1x2`; `∇×u = 2x1x3 e1 − 2x2x3 e2 + x2 e3`; `∇²u = 0` (every pure second derivative of every component vanishes); `∇u = [[1,0,0],[x2,x1,0],[2x2x3, 2x1x3, 2x1x2]]`; `tr(∇u) = 1 + x1 + 2x1x2 = ∇·u`.

**3B · Vector identities by index notation (idea 1), with the integral theorems stated (idea 2).**

*Worked example · Book Exercise 1.16, solved for (1.8.5)₃ and (1.8.5)₆ (PDF p. 26).* The list (1.8.5) in the order printed on PDF p. 16 (checked on a zoomed crop): 1 `∇(φψ) = (∇φ)ψ + φ(∇ψ)`; 2 `∇²(φψ) = (∇²φ)ψ + φ(∇²ψ) + 2∇φ·∇ψ`; 3 `∇·(φu) = ∇φ·u + φ(∇·u)`; 4 `∇×(φu) = ∇φ×u + φ(∇×u)`;
5 `∇·(u×v) = v·(∇×u) − u·(∇×v)`; 6 `∇×∇φ = 0`; 7 `∇·∇φ = ∇²φ`; 8 `∇·∇×u = 0`; 9 `∇×(∇×u) = ∇(∇·u) − ∇²u`; 10 `u×(∇×u) = ½∇(u·u) − u·∇u`. The notes print identities 3, 6, 8, 9 in full in the example and exercise text so the numbering cannot confuse.
Steps (8): (1) plan: write each side with (1.8.4); (2) `(∇·(φu)) = (φ u_i),i`; (3) product rule `φ,i u_i + φ u_i,i`; (4) recognise `∇φ·u + φ(∇·u)` (identity 3); (5) numeric check with Example 1.4's `φ, u`: both sides `6x² − 2y² + 3x²z − 9y²z` (value −101 at `(1,2,3)`);
(6) `(∇×∇φ)_i = ε_ijk φ,kj`; (7) `φ,kj = φ,jk` (mixed partials commute for continuous second derivatives), `ε_ijk` antisymmetric in `jk`, so zero by (1.2.9) (identity 6); (8) explicit check `i = 1`: `ε_123 φ,32 + ε_132 φ,23 = φ,32 − φ,23 = 0`, and `∇×∇φ = 0` for `φ = x² − y²`.
Script verifies all ten identities with generic functions.
Then the sub-section **Integral theorems (stated)**: (1.8.6) to (1.8.12), no worked example, as in idea 2.

*Your turn · Book Exercise 1.16 for (1.8.5)₈ and (1.8.5)₉ (PDF p. 26).* Statement: "Using index notation, verify (i) `∇·(∇×u) = 0` and (ii) `∇×(∇×u) = ∇(∇·u) − ∇²u` for a vector field `u`. (These are the 8th and 9th identities of (1.8.5).)"
Hint: write the curl with `ε` (1.8.4); in (i) look for a symmetric pair against an antisymmetric one; in (ii) use `ε_ijk = ε_kij` and the contracted ε–δ identity.
Verified answer: (i) `(∇×u)_k = ε_kpq u_q,p`, so `∇·(∇×u) = (ε_kpq u_q,p),k = ε_kpq u_q,pk`; `u_q,pk` is symmetric in `pk`, `ε_kpq` antisymmetric in `kp`, so the sum is 0 by (1.2.9).
(ii) `[∇×(∇×u)]_i = ε_ijk (∇×u)_k,j = ε_ijk (ε_kpq u_q,p),j = ε_ijk ε_kpq u_q,pj`; `ε_ijk = ε_kij`, so `ε_kij ε_kpq = δ_ip δ_jq − δ_iq δ_jp`; this gives `u_j,ij − u_i,jj = (u_j,j),i − u_i,jj = [∇(∇·u)]_i − [∇²u]_i`. Script: both sides equal for generic `u`, and for `u = (x²y, yz², xyz)` both curl-curl and `∇(∇·u) − ∇²u` equal `(y, 3x − 2y, 2z)`, `∇·(∇×u) = 0`.

**3C · Curvilinear coordinates, polar and cylindrical (idea 3).**

*Worked example · Book Example 1.5 (PDF p. 23, Figure 1.8 on p. 24).* Data as read: plane polar coordinates `(r, θ)`, `x1 = r cosθ`, `x2 = r sinθ` (Figure 1.8: `r` from the origin, `θ` counterclockwise from `x1`, `ê_r` along increasing `r`, `ê_θ` perpendicular, counterclockwise); `(ds)² = (dr)² + (r dθ)²`, so `h1 = 1`, `h2 = r`; `u = u_r ê_r + u_θ ê_θ`, `ê_z = ê_r × ê_θ`.
The book's results: (1.9.19) `ê_r = cosθ e1 + sinθ e2`, `ê_θ = −sinθ e1 + cosθ e2`; (1.9.20) `∂ê_r/∂θ = ê_θ`, `∂ê_θ/∂θ = −ê_r`, `∂/∂r = 0`; (1.9.21) `∇ = ê_r ∂/∂r + ê_θ (1/r) ∂/∂θ`, `∇φ = ê_r ∂φ/∂r + ê_θ (1/r) ∂φ/∂θ`, `∇·u = (1/r) ∂(r u_r)/∂r + (1/r) ∂u_θ/∂θ`,
`∇²φ = (1/r) ∂/∂r (r ∂φ/∂r) + (1/r²) ∂²φ/∂θ²`, `∇×u = [(1/r) ∂(r u_θ)/∂r − (1/r) ∂u_r/∂θ] ê_z`, `∇u` as in misprint 2 (I write the plus), `∇²u = (∇²u_r − (2/r²) ∂u_θ/∂θ − u_r/r²) ê_r + (∇²u_θ + (2/r²) ∂u_r/∂θ − u_θ/r²) ê_θ`. I write the scalar as `f` (the book writes `φ` here) so that `φ` stays free for the spherical angle.
Steps (10, plus checks), derived from the basis rules rather than only quoted: (1) `h1 = 1, h2 = r` from `(ds)²` and by (1.9.6); (2) `ê_r, ê_θ` from (1.9.5), the same numbers as `Q` of Topic 2 for a rotation through `θ`; (3) differentiate (1.9.19) to get (1.9.20), cross-checked with the second line of (1.9.10); (4) `∇` from (1.9.12);
(5) `∇f`; (6) `∇·u = ê_r·∂u/∂r + ê_θ·(1/r)∂u/∂θ` with `∂u/∂θ = (∂u_r/∂θ − u_θ) ê_r + (u_r + ∂u_θ/∂θ) ê_θ`, giving `∂u_r/∂r + u_r/r + (1/r)∂u_θ/∂θ`, and agreement with (1.9.14); (7) `∇²f = ∇·(∇f)` using step 6 with `u_r = ∂f/∂r`, `u_θ = (1/r)∂f/∂θ`;
(8) `∇×u` using `ê_r×ê_θ = ê_z`, `ê_θ×ê_r = −ê_z`; (9) `∇u` as four dyads, derivative direction first as in (1.9.17); (10) `∇²u` stated (the book gives no derivation) with the reason for the extra terms.
Checks (script, generic functions and a chain-rule reference): `u = r ê_r` (= `x1 e1 + x2 e2`): `∇·u = 2`, `∇×u = 0`, `∇u = ê_r ê_r + ê_θ ê_θ`; `u = r ê_θ` (= `−x2 e1 + x1 e2`): `∇·u = 0`, `∇×u = 2 ê_z`, dyad coefficients `+1` on `ê_r ê_θ` and `−1` on `ê_θ ê_r`; `f = r²`: `∇²f = 4 = ∇²(x1²+x2²)`.

*Your turn · Book Exercise 1.17 (PDF p. 26).* Statement: "Extend the polar results of Example 1.5 to three-dimensional cylindrical coordinates `(r, θ, z)`, with `x1 = r cosθ`, `x2 = r sinθ`, `x3 = z` (1.9.1) and unit vectors `ê_r, ê_θ, ê_z` (`ê_z = e3` is fixed along the axis; Figure 1.5). Find `∇f`, `∇·u`, `∇²f` and `∇×u` for `u = u_r ê_r + u_θ ê_θ + u_z ê_z`."
Hint: `ξ = (r, θ, z)`; find `h1, h2, h3` from `(ds)² = dr² + r²dθ² + dz²` or from (1.9.6), then use (1.9.13) to (1.9.16).
Verified answer: `h = (1, r, 1)`, `h1h2h3 = r`; `∇f = ê_r ∂f/∂r + ê_θ (1/r) ∂f/∂θ + ê_z ∂f/∂z`; `∇·u = (1/r) ∂(r u_r)/∂r + (1/r) ∂u_θ/∂θ + ∂u_z/∂z` (from (1.9.14): `(1/r)[∂(r u_r)/∂r + ∂u_θ/∂θ + ∂(r u_z)/∂z]`, with `r` constant in `z`);
`∇²f = (1/r) ∂/∂r (r ∂f/∂r) + (1/r²) ∂²f/∂θ² + ∂²f/∂z²`; `∇×u = ê_r[(1/r) ∂u_z/∂θ − ∂u_θ/∂z] + ê_θ[∂u_r/∂z − ∂u_z/∂r] + ê_z[(1/r) ∂(r u_θ)/∂r − (1/r) ∂u_r/∂θ]` (three components, each from the `ε_ijk` sum in (1.9.16)).
Script: the general formulas with `h = (1, r, 1)` give exactly these, and the results agree with a Cartesian computation at random points. Checks for the student: `u = r ê_r + z ê_z` (position vector) has `∇·u = 3`, `∇×u = 0`; `f = r² + z²` has `∇²f = 6`.

**Symbols (Topic 3).** `φ, ψ` (scalar fields in 3A and 3B, as in Example 1.4 and (1.8.5)); `f` (scalar field in 3C, Exercise 1.17 and the curvilinear Key results); `u, v` (vector fields); `u_i,j`; `∇, ∇f, ∇·u, ∇×u, ∇²` (div, curl, Laplacian); `s` (distance along a direction, m); `n` (unit vector, outer unit normal on a surface); `S, V, C` (surface, volume, curve); `dS, dV, dr`; `(r, θ, z)` and `(R, φ, θ)` (cylindrical and spherical coordinates; `φ` is the polar angle from `x3`, `θ` the azimuth, as in (1.9.2); `φ` means this angle only in spherical coordinates, where the text says "here φ is an angle, not a field" and the Symbols box has one row for each meaning);
`ξ^m` (curvilinear coordinates), `x^k` (Cartesian coordinates, superscripts as in §1.9); `h_i` (scale factors); `ê_i, ê_r, ê_θ, ê_z, ê_R, ê_φ` (curvilinear unit vectors); `u_<i>` (physical component of `u` along `ê_i`); `u_r, u_θ, u_z`; `Q^k_r` (1.9.7).

**Common mistakes (Topic 3).** (i) Differentiating `u_r ê_r + u_θ ê_θ` as if `ê_r, ê_θ` were constant: the divergence loses `u_r/r`, and `∇²u` is not `(∇²u_r) ê_r + (∇²u_θ) ê_θ` (the book warns about the Laplacian of a vector, PDF p. 23); test with `u = r ê_r`, whose divergence must be 2, not 1.
(ii) `(∇×u)_i = ε_ijk u_k,j`: the derivative index is the middle one, swapping `j` and `k` reverses the sign of the curl. (iii) `∇u` transposed: `u_i,j` in Cartesian axes (derivative second) against (1.9.17) and Example 1.5 (derivative first); always say which one is used; the polar `ê_θ ê_θ` coefficient is `(1/r)(∂u_θ/∂θ + u_r)` (the printed minus is a misprint).

**What comes next (draft).** Topic 4 differentiates the displacement field `u_i` to get `u_i,j` and from it the strain; Topic 8 uses the divergence theorem and the zero-value theorem to turn a force balance into the equilibrium equations.

## 4. Questions for the coordinator (each has my default)

- **Q1. Integral theorems.** No book example or exercise exists for (1.8.6) to (1.8.12). Default: stated sub-section at the end of 3B, no extra worked example or your-turn box. Alternative: a worked divergence-theorem check on a cube, which is my own example, not the book's.
- **Q2. Exercise 1.6, sense of rotation.** "Positive sense presented in Example 1.2": I read it as the right-hand rule, the sense in which `x1'` turned towards `x2` about `x3` (so `x2'` turns towards `x3` about `x1`). The opposite sense gives `b' = (2, 0, √2)` and `a' = [[1,√2,√2],[0,−1/2,−3/2],[0,3/2,9/2]]`. I will state the sense in the problem so the answer is unambiguous. Please confirm.
- **Q3. Topic 1 box "What you need from earlier".** Default: school prerequisites (matrix product, transpose, 3×3 determinant, dot and cross product), since the checker needs the box and no earlier topic exists.
- **Q4. Spherical operators (Ex 1.18, PDF p. 27).** Default: `h`'s derived, `ε`-free statement of the four operators in Key results (with the "+" restored), no worked example. Cut if you want the topic shorter.
- **Q5. Misprints.** Default: write the correct forms, add a one-line note to the student only for misprints 1 (2A) and 2 (3C), where the printed form would otherwise mislead a student comparing with the book.
- **Q6. Topic 2 "What comes next".** Writer brief: Topics 5, 7, 8. Your page outline: Topic 3, plus 5, 7, 8. Default: the writer brief.
- **Q7. Exercise 1.12(d) ordering.** Default: ranked `9, 6, 3` with the handedness check shown; the book's list reads 3, 6, 9.
