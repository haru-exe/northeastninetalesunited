# Writer A brief: Topics 1, 2, 3 (Chapter 1)

Read `notes-build/BRIEF-common.md` first; this file adds what is specific to you.
Your letter is **A**. Plan file: `notes-build/plans/writer-A-plan.md`.
Fragments: `notes-build/fragments/t1.html`, `t2.html`, `t3.html` (plus `tN-symbols.html` and `tN-results.html`).
Chapter class: `c1` for all three topics.

**No Looking-ahead box.** The student excluded Chapter 1 from the links to Chapters 5 to 8. Your
"What comes next" lines point to later midsem topics instead:
Topic 1 to Topic 2; Topic 2 to Topics 5, 7 and 8 (strain transformation, stress transformation,
principal strains and stresses use these laws word for word); Topic 3 to Topic 4 (differentiating the
displacement field) and Topic 8 (the divergence theorem gives the equilibrium equations).

## Chapter 1 PDF page map (PDF page = book page minus 2)

| Item | PDF pages |
|---|---|
| §1.1 | 1–2 |
| §1.2 index notation | 2–4 |
| Example 1.1 | 4 |
| §1.3 Kronecker delta, alternating symbol | 5 |
| §1.4 coordinate transformations | 6–7 |
| §1.5 Cartesian tensors | 8–9 |
| Example 1.2 | 9–10 |
| §1.6 principal values | 10–13 |
| Example 1.3 | 12–13 |
| §1.7 algebra | 14–15 |
| §1.8 calculus | 15–19 |
| Example 1.4 | 17 |
| §1.8.1–1.8.4 integral theorems | 18–19 |
| §1.9 curvilinear coordinates | 19–25 |
| Example 1.5 | 23–24 |
| Exercises 1.1 | 24 |
| Exercises 1.2–1.10 | 25 |
| Exercises 1.11–1.17 (1.14 is printed next to 1.13) | 26 |
| Exercise 1.18 | 27 |

## Topic 1 · Index notation, Kronecker delta and the permutation symbol
Eyebrow: `Chapter 1 · §1.1–1.3, 1.7 · Exam weight: medium (estimate)`

Ideas, in teaching order:
1. Scalars, vectors and matrices as tensors of order 0, 1, 2; index notation; free and dummy indices;
   the summation convention and its rules (an index at most twice per term; free indices match across
   terms); contraction; outer and inner products. Definitions, no derivation.
2. Symmetric and antisymmetric parts $a_{(ij)}$, $a_{[ij]}$ and the split (1.2.10); a symmetric symbol times
   an antisymmetric one, summed, is zero (1.2.9): prove it (examinable).
3. $\delta_{ij}$ and its substitution rule (1.3.2); $\epsilon_{ijk}$ (1.3.3); determinants (1.3.4); the
   $\epsilon$–$\delta$ identity (1.3.5) and its contracted form
   $\epsilon_{ijk}\epsilon_{imn}=\delta_{jm}\delta_{kn}-\delta_{jn}\delta_{km}$, derived by contraction
   (examinable; Exercise 1.15 and Topic 4 need it); dot, cross and triple products and matrix products in
   index form (1.7.1)–(1.7.7).

Concept blocks:
- **1A** (idea 1): worked = Example 1.1, first part ($a_{ii}$, $a_{ij}a_{ij}$, $a_{ij}a_{jk}$, $a_{ij}b_j$,
  $a_{ij}b_ib_j$, $b_ib_i$, $b_ib_j$, each labelled scalar, vector or matrix). Your turn = Exercise 1.1(b).
- **1B** (idea 2): worked = Example 1.1, second part ($a_{(ij)}$, $a_{[ij]}$), together with the proof of (1.2.9).
  Your turn = Exercise 1.2 using the matrix of Exercise 1.1(b) only.
- **1C** (idea 3): worked = Exercise 1.15, solved (the dual vector of an antisymmetric tensor and its
  inversion with the contracted $\epsilon$–$\delta$ identity; read the sign convention from PDF page 26).
  Your turn = Exercise 1.5 (expand both index forms of (1.3.4) and match the usual determinant).

Topic 1's "Where we are" says what the course builds towards: describing deformation (strain), internal
force (stress) and the material law that links them, all written in this notation.

## Topic 2 · Coordinate transformations, Cartesian tensors and principal values
Eyebrow: `Chapter 1 · §1.4–1.6 · Exam weight: high (estimate)`

Ideas:
1. $Q_{ij}=\cos(x_i',x_j)$; $\mathbf e_i'=Q_{ij}\mathbf e_j$; derive $v_i'=Q_{ij}v_j$ and $v_i=Q_{ji}v_j'$;
   derive the orthogonality conditions (1.4.9)–(1.4.10) and $\det Q=\pm1$ (1.4.11).
2. Transformation laws for tensors of any order (1.5.1); a tensor versus its components; dyadic form (1.5.3);
   isotropic tensors: $\delta_{ij}$ (proved), $\epsilon_{ijk}$, and the fourth-order form
   $\alpha\delta_{ij}\delta_{kl}+\beta\delta_{ik}\delta_{jl}+\gamma\delta_{il}\delta_{jk}$ (stated here; Topic 9
   builds Hooke's law from it).
3. Principal values and directions: $a_{ij}n_j=\lambda n_i$ ($\lambda$ here is an eigenvalue, say so);
   $\det(a_{ij}-\lambda\delta_{ij})=0$; characteristic equation (1.6.2); invariants (1.6.3) and in principal
   values (1.6.5); the three root cases; principal axes and the diagonal form (1.6.4); rows of $Q$ are the unit
   eigenvectors; the largest and smallest diagonal values.

Concept blocks:
- **2A** (ideas 1–2): worked = Example 1.2 (rotation of $60^\circ$ about $x_3$: vector and matrix; read $Q$
  from PDF pages 9–10 and the figure). Your turn = Exercise 1.6 ($45^\circ$ about $x_1$, positive sense as in
  Example 1.2), using the vector and matrix of Exercise 1.1(b); say "case (b) data" in the statement.
- **2B** (isotropic tensors): worked = Exercise 1.8, solved ($\alpha\delta_{ij}$ keeps its form under any $Q$).
  Your turn = Exercise 1.9 (the fourth-order isotropic form keeps its form under (1.5.1)$_5$).
- **2C** (idea 3): worked = Example 1.3 (invariants; $\lambda=5,2,-5$; directions; $Q$; diagonal form).
  Your turn = Exercise 1.12(d) (the book gives $\lambda=3,6,9$; ask for invariants, principal values,
  directions and the rotation to diagonal form, as the exercise does).

## Topic 3 · Tensor calculus and curvilinear coordinates
Eyebrow: `Chapter 1 · §1.8–1.9 · Exam weight: medium (estimate)`

Ideas:
1. Fields; comma notation $a_{i,j}$ (a free derivative index raises the order by one); directional
   derivative $df/ds=\mathbf n\cdot\nabla f$ (1.8.1); gradient, divergence, curl and Laplacian (1.8.4);
   identities (1.8.5) proved in index notation.
2. Integral theorems: divergence (1.8.6)–(1.8.7), Stokes (1.8.8)–(1.8.9), Green (1.8.10)–(1.8.11),
   zero-value (1.8.12). State each with its meaning; not derived (the book does not derive them). Say that
   Topic 8 uses the divergence and zero-value theorems to derive equilibrium, and Topic 6 uses Stokes.
3. Orthogonal curvilinear coordinates: cylindrical and spherical (1.9.1)–(1.9.2); scale factors (1.9.4),
   (1.9.6); unit basis (1.9.5); derivatives of the basis (1.9.10); general $\nabla$, $\nabla f$,
   $\nabla\cdot\mathbf u$, $\nabla^2 f$, $\nabla\times\mathbf u$ (1.9.12)–(1.9.16) stated; the polar case
   worked in full.

Concept blocks:
- **3A** (idea 1): worked = Example 1.4. Your turn = Exercise 1.14(a)
  ($\nabla\cdot\mathbf u$, $\nabla\times\mathbf u$, $\nabla^2\mathbf u$, $\nabla\mathbf u$, $\mathrm{tr}(\nabla\mathbf u)$).
- **3B** (identities): worked = Exercise 1.16, solved for identities (1.8.5)$_3$ and (1.8.5)$_6$. Your turn =
  Exercise 1.16 for (1.8.5)$_8$ and (1.8.5)$_9$. Number the identities of (1.8.5) in the order printed on
  PDF page 16 and state the identities in full in the exercise text, so the numbering cannot confuse.
- **3C** (idea 3): worked = Example 1.5 (polar coordinates). Your turn = Exercise 1.17 (cylindrical:
  $\nabla f$, $\nabla\cdot\mathbf u$, $\nabla^2 f$, $\nabla\times\mathbf u$).

## Notes
- Everything in Chapter 1 is in the midsem, including §1.9.
- The worked examples here are all book Examples except 1C (Exercise 1.15) and 2B (Exercise 1.8),
  which are book exercises solved in full; tag them `Worked example · Book Exercise 1.15, solved`.
