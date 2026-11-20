# Writer B brief: Topics 4, 5, 6 (Chapter 2)

Read `notes-build/BRIEF-common.md` first; this file adds what is specific to you.
Your letter is **B**. Plan file: `notes-build/plans/writer-B-plan.md`.
Fragments: `notes-build/fragments/t4.html`, `t5.html`, `t6.html` (plus `tN-symbols.html` and `tN-results.html`).
Chapter class: `c2` for all three topics. Midsem scope in Chapter 2 is §2.1–2.6 only (§2.7 is out).

## Chapter 2 PDF page map (PDF page = book page minus 30)

| Item | PDF pages |
|---|---|
| §2.1 general deformations | 1–4 |
| §2.2 geometric construction, rigid-body motion | 4–8 |
| Example 2.1 | 8 |
| §2.3 strain transformation | 9–10 |
| §2.4 principal strains | 10–11 |
| §2.5 spherical and deviatoric strains | 11 |
| §2.6 strain compatibility | 11–16 |
| Exercise 2.1 | 18 |
| Exercises 2.2–2.6 | 19 |
| Exercises 2.7–2.9 (2.7 rosette figure, 2.9 figure) | 20 |
| Exercises 2.10–2.15 | 21 |
| Exercises 2.16–2.19 | 22 |
| Exercise 2.20 | 23 |

Chapter 1 pages you may need for "What you need from earlier": (1.2.10) split, PDF p. 3; (1.5.1)
transformation laws, p. 8; (1.6.1)–(1.6.5) principal values, pp. 10–12; Exercise 1.15 dual vector, p. 26;
(1.8.4) gradient and curl, p. 16; Stokes theorem (1.8.8), p. 18.

## Topic 4 · Displacements, strain and rotation
Eyebrow: `Chapter 2 · §2.1–2.2 · Exam weight: high (estimate)`

Ideas:
1. Displacement field; Taylor expansion to $\Delta r_i=u_{i,j}r_j$ (2.1.4); split $u_{i,j}=e_{ij}+\omega_{ij}$
   (2.1.6)–(2.1.7); rotation vector $\omega_i$ and $\boldsymbol\omega=\tfrac12\nabla\times\mathbf u$ (2.1.9),
   using the dual vector from Topic 1. Derived.
2. Geometric meaning: $e_x=\partial u/\partial x$ from Fig. 2.4 with the small-deformation step explained
   (2.2.1); engineering shear strain $\gamma_{xy}=\partial u/\partial y+\partial v/\partial x$ (2.2.3);
   $e_{xy}=\tfrac12\gamma_{xy}$; sign conventions; the six relations (2.2.4)–(2.2.6); the strain matrix (2.2.8).
   Derived.
3. Rigid-body motion: rotation $\omega_z$ (Fig. 2.5); rigid displacement fields (2.2.9)–(2.2.10) give zero
   strain; integrating strains recovers the displacements only up to a rigid-body motion. Teach the
   step-by-step procedure (integrate the normal strains, get arbitrary functions, use the shear strain to
   separate variables, recognise the constants as rigid-body terms).

Concept blocks:
- **4A** (ideas 1–2): worked = Example 2.1. Your turn = Exercise 2.2 (strains, deformed shape of the element,
  and $\omega_z$; read the signs of $u$ and $v$ and the element figure on PDF p. 19).
- **4B** (idea 3): worked = Exercise 2.3, solved (integrate the constant strain field; pick out the
  rigid-body terms). Your turn = Exercise 2.4 (bar stretched under its own weight).

## Topic 5 · Strain transformation, principal strains, spherical and deviatoric strain
Eyebrow: `Chapter 2 · §2.3–2.5 · Exam weight: high (estimate)`

Ideas:
1. $e_{ij}'=Q_{ip}Q_{jq}e_{pq}$ (2.3.1) with $Q$ in $l,m,n$ form (2.3.2)–(2.3.3), stated; the 2D rotation
   (2.3.4)–(2.3.5) and the double-angle form (2.3.6), derived; polar components (the result of Exercise 2.6);
   strain rosettes.
2. Principal strains: characteristic equation (2.4.1); invariants $\vartheta_1,\vartheta_2,\vartheta_3$ (2.4.2);
   diagonal form (2.4.3), no shear on principal axes; dilatation $\vartheta=e_{kk}=\Delta V/V_0$ (Exercise 2.11),
   derived in the explanation.
3. Spherical $\tilde e_{ij}=\tfrac13e_{kk}\delta_{ij}$ and deviatoric $\hat e_{ij}=e_{ij}-\tfrac13e_{kk}\delta_{ij}$
   (2.5.1)–(2.5.3); volume change versus shape change; $\hat e_{kk}=0$; same principal directions.

Concept blocks:
- **5A** (idea 1): worked = Exercise 2.7, solved (rosette: $e_a=0.001$, $e_b=0.002$, $e_c=0.004$; read the
  arm directions from the figure on PDF p. 20 and state them in your plan). Your turn = Exercise 2.8 by hand:
  for $e_x=0.002$, $e_y=-0.004$, $e_{xy}=0.001$, find the rotation angles at which $e_x'$ and $e_{xy}'$ are
  largest and their values (drop the MATLAB plotting; say so in the statement).
- **5B** (idea 2): worked = the principal strains and directions of the Exercise 2.9 strain tensor, solved
  (read the matrix from PDF p. 20; it is block-diagonal, so the cubic factors: expect $5\times10^{-3}$ and
  $\tfrac12(-3\pm\sqrt{41})\times10^{-3}$, but verify). Tag it `Worked example · Book Exercise 2.9 data,
  principal strains`. Your turn = Exercise 2.10 with a calculator (read the matrix from PDF p. 21; the cubic
  does not factor, so give the invariants and the numerical roots in the answer).
- **5C** (idea 3): worked = Exercise 2.12, solved (spherical and deviatoric parts of the Exercise 2.10 strain;
  show $\hat e_{kk}=0$ and say what it means, using Exercise 2.11). Your turn = the same split for the
  Exercise 2.9 strain, checking $\hat e_{kk}=0$ and that the deviatoric principal values are the principal
  strains minus $\tfrac13\vartheta$ (tag: `Your turn · Exercise 2.12 method on the Exercise 2.9 strain`).

## Topic 6 · Strain compatibility
Eyebrow: `Chapter 2 · §2.6 · Exam weight: medium (estimate)`

Ideas:
1. Why compatibility is needed: six strain–displacement equations for three displacements; the picture of
   Fig. 2.7.
2. Saint-Venant equations (2.6.1) derived in index form; of the 81, six are meaningful (set $k=l$); the six
   scalar equations (2.6.2); only three are independent (stated).
3. Sufficiency: necessary and sufficient in simply connected regions (outline the line-integral argument of
   (2.6.3)–(2.6.7) in words and key equations; say it is not examinable in full); simply versus multiply
   connected regions (Fig. 2.9) and cuts; Cesàro integrals (named only); compatible strains can still give a
   multivalued displacement in a multiply connected body.

Concept blocks:
- **6A** (ideas 1–2): worked = Exercise 2.17, solved (expect $A=2B/3$; verify). Your turn = Exercise 2.13
  (derive the first equation of (2.6.2) by differentiating the scalar strain–displacement relations).
- **6B** (idea 3): worked = Exercise 2.18, first half, solved (screw dislocation
  $u=v=0$, $w=\tfrac{b}{2\pi}\tan^{-1}(y/x)$: the strains, and the jump of $b$ in $w$ once around the
  $z$-axis, which is why the region must exclude the axis and is multiply connected). Your turn = Exercise 2.18,
  second half (show these strains satisfy all six compatibility equations, so compatibility alone cannot rule
  out the jump).

## Looking ahead · leads to verify (Topics 4 to 6)

These leads were drafted from garbled text. Check every section and equation number on the PDF page and
keep only what holds. Your syllabus for these links: §5.1–5.6; §6.1–6.3, 6.5, 6.6; Chapter 7; §8.1, 8.3–8.5.

Topic 4:
- §5.1 (5.1.1): strain–displacement relations are one of the 15 field equations. §5.4: substituting
  $e_{ij}=\tfrac12(u_{i,j}+u_{j,i})$ into Hooke's law gives (5.4.1); then equilibrium gives Navier's
  equations (5.4.3)–(5.4.5).
- §5.3 and §6.2: displacements found by integrating strains are fixed only up to a rigid-body motion; with
  tractions given on the whole boundary the solution is unique up to a rigid-body motion.
- §7.1 plane strain: $u(x,y)$, $v(x,y)$, $w=0$ give $e_z=e_{xz}=e_{yz}=0$ (7.1.1)–(7.1.2); §7.2 (7.2.3) and the
  inconsistency it shows; §7.4 antiplane strain (7.4.1)–(7.4.2); §7.6 polar strain–displacement (7.6.1).
- §8.1 Example 8.1: the beam's displacements are found by the Exercise 2.3 procedure (functions $f(y)$, $g(x)$;
  rigid-body constants fixed by "fixity conditions"), (8.1.11)–(8.1.14); Example 8.2; Example 8.6 displacements.
- §6.1: strain energy written with $\gamma_{xy}$ (6.1.7) and (6.1.9) (factor-of-2 trap); §6.5 virtual strains
  $\delta e_{ij}=\tfrac12(\delta u_{i,j}+\delta u_{j,i})$.

Topic 5:
- Exercise 2.6 polar components, then §7.6 (7.6.1) and Exercise 7.16 (polar strain–displacement relations by
  transformation), used in the polar solutions of §8.3–8.4.
- Dilatation $\vartheta=e_{kk}=\nabla\cdot\mathbf u$: in Hooke's law and in Navier's equations (5.4.4),
  $\mu\nabla^2\mathbf u+(\lambda+\mu)\nabla(\nabla\cdot\mathbf u)+\mathbf F=\mathbf 0$.
- Spherical/deviatoric split: Exercise 4.14 ($\tilde\sigma_{ij}=3k\tilde e_{ij}$, $\hat\sigma_{ij}=2\mu\hat e_{ij}$)
  leads to the volumetric and distortional strain energy in §6.1 (6.1.15)–(6.1.17).
- Principal strains: principal axes of stress and strain coincide (Exercise 4.7); strain energy in principal
  strains (Exercise 6.5).

Topic 6:
- §5.1 (5.1.2): compatibility is set aside in the displacement formulation (it holds automatically) but is
  essential in the stress formulation: with Hooke's law it becomes the Beltrami–Michell equations
  (5.3.1)–(5.3.4).
- §7.1–7.2: one compatibility equation in 2D, (7.1.6)/(7.2.6), written in stress as (7.1.7)/(7.2.7); with the
  Airy function it becomes the biharmonic equation (7.5.4)–(7.5.6), and (7.6.8) in polar form.
- §8.1: a polynomial Airy function must satisfy the biharmonic equation, which ties its coefficients together
  (8.1.4)–(8.1.6), for example $3A_{40}+A_{22}+3A_{04}=0$.
- Multiply connected bodies: the remark at the end of §7.5; §8.3–8.4 drop terms that give multivalued
  displacements (check the reason Example 8.6 keeps no log terms, around (8.3.8)–(8.3.9) and (8.4.1)).

Chapters 5 to 8 PDF page maps:
- Ch 5 (PDF = book minus 94): §5.1 pp. 1–2; §5.2 pp. 2–6; §5.3 pp. 7–8; §5.4 pp. 8–9; §5.5 pp. 9–11;
  §5.6 pp. 11–12.
- Ch 6 (PDF = book minus 118): §6.1 pp. 1–6; §6.2 p. 6; §6.3 pp. 7–8; §6.5 pp. 10–12; §6.6 pp. 12–14.
- Ch 7 (PDF = book minus 140): §7.1 pp. 1–4; §7.2 pp. 4–7 (Table 7.1 p. 7); §7.3 pp. 7–9; §7.4 pp. 9–10;
  §7.5 pp. 10–12; §7.6 pp. 12–14; exercises pp. 14–17.
- Ch 8 (PDF = book minus 158): §8.1 pp. 1–11 (Example 8.1 pp. 3–5, Example 8.2 pp. 5–7, Example 8.3 pp. 7–11);
  §8.3 pp. 20–22; §8.4 pp. 22–55 (Example 8.6 pp. 22–24; §8.4.1 p. 24; §8.4.2 p. 25; Example 8.7 pp. 26–29;
  §8.4.7 Flamant pp. 33–38; Example 8.10 pp. 49–53; Example 8.11 pp. 53–55); §8.5 pp. 55–61.
