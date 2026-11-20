# Writer C brief: Topics 7, 8 (Chapter 3) and 9 (Chapter 4)

Read `notes-build/BRIEF-common.md` first; this file adds what is specific to you.
Your letter is **C**. Plan file: `notes-build/plans/writer-C-plan.md`.
Fragments: `notes-build/fragments/t7.html`, `t8.html`, `t9.html` (plus `tN-symbols.html` and `tN-results.html`).
Chapter class: `c3` for Topics 7 and 8, `c4` for Topic 9.
Midsem scope: §3.1–3.4 and §3.7 (§3.5, 3.6 and 3.8 are out); all of Chapter 4.

## Chapter 3 PDF page map (PDF page = book page minus 54)

| Item | PDF pages |
|---|---|
| §3.1 body and surface forces | 1–2 |
| §3.2 traction vector and stress tensor | 2–6 |
| §3.3 stress transformation | 6–7 |
| §3.4 principal stresses, Mohr's circles | 7–10 |
| Example 3.1 | 10 |
| §3.7 equilibrium equations | 15–17 |
| Exercises 3.1–3.2 (3.1 figure) | 20 |
| Exercises 3.3–3.7 | 21 |
| Exercises 3.8–3.11 | 22 |
| Exercises 3.12–3.18 | 23 |
| Exercises 3.19–3.22 | 24 |
| Exercises 3.23–3.25 (3.25 figure may run to p. 26) | 25 |
| Exercises 3.26–3.27 | 26 |

## Chapter 4 PDF page map (PDF page = book page minus 80)

| Item | PDF pages |
|---|---|
| §4.1 material characterization | 1–3 |
| §4.2 Hooke's law | 3–6 |
| §4.3 meaning of the moduli (4.3.1–4.3.3 on pp. 7–8; Tables 4.1, 4.2 on p. 9) | 6–10 |
| §4.4 thermoelastic relations | 10 |
| Exercises 4.1–4.6 | 11 |
| Exercises 4.7–4.12 (4.8 figure, 4.9 field) | 12 |
| Exercises 4.13–4.16 | 13 |
| Exercises 4.17–4.20 (4.17 figure) | 14 |

Earlier pages you may need for "What you need from earlier": Chapter 1: (1.5.1) p. 8; (1.6.1)–(1.6.5)
pp. 10–12; (1.8.6)–(1.8.12) pp. 18–19; Exercise 1.9 p. 25. Chapter 2: (2.2.5)–(2.2.6) p. 6–7; (2.3.6) p. 10;
(2.4.2) p. 11; (2.5.1)–(2.5.3) p. 11.

## Topic 7 · Traction, the stress tensor and stress transformation
Eyebrow: `Chapter 3 · §3.1–3.3 · Exam weight: high (estimate)`

Ideas:
1. Body forces $F_i$ (per unit volume) and surface forces; traction $\mathbf T^{n}=\lim_{\Delta A\to0}\Delta\mathbf F/\Delta A$
   (3.2.1), which depends on the point and the normal; action and reaction.
2. Stress components on coordinate faces (3.2.2)–(3.2.3) and the sign convention; Cauchy's relation
   $T_i^{n}=\sigma_{ji}n_j$ (3.2.5)–(3.2.6), derived from the force balance on the pyramid element (show the
   area relations); traction versus stress; normal and shear parts $N=\mathbf T^{n}\cdot\mathbf n$ and
   $S=(|\mathbf T^{n}|^2-N^2)^{1/2}$ (3.4.4).
3. Transformation $\sigma_{ij}'=Q_{ip}Q_{jq}\sigma_{pq}$ (3.3.1)–(3.3.3); 2D form (3.3.4) and double-angle form
   (3.3.5), derived; polar components (Exercise 3.3).

Concept blocks:
- **7A** (ideas 1–2): worked = Example 3.1, traction part, extended with $N$ and $S$. Data to verify on PDF p. 10:
  $\sigma_{ij}=\begin{bmatrix}3&1&1\\1&0&2\\1&2&0\end{bmatrix}$, $\mathbf n=(0,1,1)/\sqrt2$; expect
  $\mathbf T^{n}=(2,2,2)/\sqrt2$, $N=2$, $S=\sqrt2$. Your turn = Exercise 3.1 (biaxial plate $\sigma_x=X$,
  $\sigma_y=Y$; traction and normal and shear stress on the oblique plane $S$: read how the plane's angle is
  defined from the figure on PDF p. 20 and say so in your plan).
- **7B** (idea 3): worked = Exercise 3.3, solved (Cartesian to polar). Your turn = Exercise 3.4 (polar to
  Cartesian).

## Topic 8 · Principal stresses and the equilibrium equations
Eyebrow: `Chapter 3 · §3.4, 3.7 · Exam weight: high (estimate)`

Ideas:
1. Principal stresses: $\sigma_{ij}n_j=\sigma n_i$; characteristic equation (3.4.1); invariants (3.4.2);
   diagonal form (3.4.3); in-plane principal stresses and maximum shear for plane stress (the result of
   Exercise 3.5, derived from the characteristic equation with $\sigma_z=\sigma_{xz}=\sigma_{yz}=0$).
2. Normal and shear stress on any plane in principal axes (3.4.5)–(3.4.9); Mohr's circles (3.4.10);
   $S_{\max}=\tfrac12|\sigma_1-\sigma_3|$, acting on the plane that bisects the $\sigma_1$ and $\sigma_3$
   directions (the result of Exercise 3.13, stated).
3. Equilibrium: $\int_S T_i^{n}\,dS+\int_V F_i\,dV=0$ (3.7.1); Cauchy's relation; the divergence theorem;
   the zero-value theorem; so $\sigma_{ji,j}+F_i=0$ (3.7.4), derived; the moment balance (3.7.6) gives
   $\epsilon_{ijk}\sigma_{jk}=0$, so $\sigma_{ij}=\sigma_{ji}$ (3.7.7), derived step by step; scalar forms
   (3.7.5); 2D forms.

Concept blocks:
- **8A** (ideas 1–2): worked = Example 3.1, principal-stress part. Data to verify on PDF p. 10: $I_1=3$,
  $I_2=-6$, $I_3=-8$; $\sigma=4,1,-2$; $\mathbf n^{(1)}=(2,1,1)/\sqrt6$, $\mathbf n^{(2)}=(-1,1,1)/\sqrt3$,
  $\mathbf n^{(3)}=(0,-1,1)/\sqrt2$; add $S_{\max}=3$. Your turn = Exercise 3.8 (principal stresses and
  directions in the cantilever; read the stresses on PDF p. 22).
- **8B** (idea 3): worked = Exercise 3.25, solved (prismatic bar under its own weight; read the axis and the
  free end from the figure; expect $\sigma_x=\rho g(l-x)$). Your turn = Exercise 3.22 (with no body forces,
  stresses written from an arbitrary stress function $\phi(x,y)$ satisfy the 2D equilibrium equations
  identically).

## Topic 9 · Hooke's law: isotropic linear elastic materials
Eyebrow: `Chapter 4 · §4.1–4.4 · Exam weight: high (estimate)`

Ideas:
1. Material characterization (tension test, proportional and elastic limits, $\sigma=Ee$); generalized
   Hooke's law $\sigma_{ij}=C_{ijkl}e_{kl}$ (4.2.3); 81 constants reduce to 36 by the symmetries (4.2.4)
   (Exercise 4.2), then to 21 by strain energy (stated, Chapter 6); homogeneous versus nonhomogeneous;
   isotropic versus anisotropic.
2. Isotropy: (4.2.6) gives $\sigma_{ij}=\lambda e_{kk}\delta_{ij}+2\mu e_{ij}$ (4.2.7) (Exercise 4.3), derived;
   scalar form (4.2.8); inversion by contraction (4.2.9) to (4.2.10), with $E=\mu(3\lambda+2\mu)/(\lambda+\mu)$
   and $\nu=\lambda/[2(\lambda+\mu)]$, derived; scalar form (4.2.11).
3. Meaning of the moduli: simple tension ($E$, $\nu$), pure shear ($\mu$), hydrostatic pressure
   ($k=E/[3(1-2\nu)]$, $p=-k\vartheta$, (4.3.1)); the Table 4.1 relations students need
   ($\mu=E/[2(1+\nu)]$, $\lambda=E\nu/[(1+\nu)(1-2\nu)]$, $k=\lambda+\tfrac23\mu$); $\nu\to\tfrac12$ means
   incompressible; Table 4.2 values; the same form in cylindrical and spherical coordinates (4.3.2).
4. Thermoelasticity: $e_{ij}=e_{ij}^{(M)}+\alpha(T-T_0)\delta_{ij}$ (4.4.1)–(4.4.3); (4.4.4) and (4.4.6);
   no thermal shear strain in an isotropic solid.

Concept blocks:
- **9A** (ideas 1–2): worked = Exercise 4.5, solved (invert (4.2.7) to (4.2.10); find $E$ and $\nu$), with
  Exercise 4.6 ($\mu$ and $\lambda$ in terms of $E$, $\nu$) as its last steps. Your turn = Exercise 4.9 (the
  given displacements to strains to stresses; show it is pure bending; copy the displacement field exactly
  from PDF p. 12).
- **9B** (idea 3): worked = Exercise 4.17, solved (steel plate, 4 mm thick; read the dimensions and which
  edges carry 30 MPa and 20 MPa from the figure on PDF p. 14; Table 4.2 steel values from PDF p. 9, expected
  $E=207\ \mathrm{GPa}$, $\nu=0.29$). Your turn = Exercise 4.8 (rosette on the surface of a stress-free
  steel solid; read the gauge directions and the surface plane from the figure on PDF p. 12; the surface is
  traction-free, so use that to decide which stresses vanish).
- **9C** (idea 4): worked = Exercise 4.19, solved (bar constrained in $x$, free in $y$ and $z$:
  $\sigma_x=-E\alpha T$, $e_y=e_z=\alpha(1+\nu)T$). Your turn = Exercise 4.20 (thermoelastic Hooke's law in
  component form).

## Looking ahead · leads to verify (Topics 7 to 9)

These leads were drafted from garbled text. Check every section and equation number on the PDF page and
keep only what holds. Your syllabus for these links: §5.1–5.6; §6.1–6.3, 6.5, 6.6; Chapter 7; §8.1, 8.3–8.5.

Topic 7:
- §5.2: traction boundary conditions (5.2.1); on coordinate surfaces they reduce to stress components
  (Fig. 5.3); the inclined face of the tapered beam (Fig. 5.4) needs $T_x=\sigma_xn_x+\sigma_{xy}n_y=0$,
  $T_y=\sigma_{xy}n_x+\sigma_yn_y=0$; interface conditions; 2D form (7.1.9); antiplane form (7.4.7).
- §5.6 Saint-Venant's principle replaces pointwise tractions by resultants; §8.1 end conditions such as
  $\int\sigma_x\,dy$, $\int\sigma_x y\,dy$, $\int\sigma_{xy}\,dy$ in (8.1.7), (8.1.15), (8.1.24).
- Body forces in Navier's equations (5.4.3), Beltrami–Michell (5.3.3), the Airy potential $V$ (7.5.1)–(7.5.3),
  and the rotating disk, Example 8.11.
- Exercise 3.3 leads to the polar Airy relations (7.6.7) (Exercise 7.21); §8.4 turns far-field Cartesian loads
  into polar boundary values (Example 8.7, hole in a plate); Flamant problem §8.4.7; contact §8.5.
- §6.2 uniqueness and §6.5 virtual work use $T_i^{n}=\sigma_{ij}n_j$ to turn surface work into a volume integral.

Topic 8:
- §5.1 (5.1.3): equilibrium is a field equation; §5.4 Navier's equations are equilibrium written in
  displacements (5.4.3); §5.3 Beltrami–Michell uses $\sigma_{ij,j}=-F_i$ (5.3.2); Example 5.1 (PDF Ch 5 p. 13)
  is outside §5.1–5.6, so mention it only as "the same bar, solved in 3D, if you read on".
- §6.2 uniqueness uses $\sigma_{ij,j}=0$ with the divergence theorem (6.2.2)–(6.2.5); §6.5 virtual work gives
  back $\sigma_{ij,j}+F_i=0$ and the natural boundary conditions (6.5.8)–(6.5.9).
- §7.1–7.2: 2D equilibrium (7.1.4)/(7.2.4); §7.5 the Airy function is built to satisfy it (Exercise 3.22 is
  (7.5.3) without body force); polar equilibrium (7.6.3) is Exercise 3.23.
- §8.1–8.4: principal and maximum shear stresses interpret the solutions (stress concentration of 3 at a
  hole, Example 8.7; maximum-shear fringes; Flamant).
- Symmetry $\sigma_{ij}=\sigma_{ji}$ gives the minor symmetry of $C_{ijkl}$ in Topic 9.

Topic 9:
- §5.1 (5.1.4): Hooke's law completes 15 equations for 15 unknowns (5.1.5); §5.4 (5.4.1)
  $\sigma_{ij}=\lambda u_{k,k}\delta_{ij}+\mu(u_{i,j}+u_{j,i})$ leads to Navier's equations; §5.3 the inverse
  law inside compatibility gives Beltrami–Michell; §5.5 superposition works because every equation,
  Hooke's law included, is linear.
- §6.1: $U=\tfrac12\sigma_{ij}e_{ij}$ becomes $U(e)$ (6.1.9) and $U(\sigma)$ (6.1.10); $C_{ijkl}=C_{klij}$ leaves
  21 constants (6.1.14); §6.3: the three tests of §4.3 give $E\gt0$, $-1\lt\nu\lt\tfrac12$, $k\gt0$, $\mu\gt0$
  (6.3.3)–(6.3.11) (compare Exercises 4.10–4.11).
- §7.1 plane strain (7.1.3) with $\sigma_z=\nu(\sigma_x+\sigma_y)$; §7.2 plane stress (7.2.2) with
  $e_z=-\tfrac{\nu}{E}(\sigma_x+\sigma_y)$; Table 7.1 swaps $E$ and $\nu$ between the two; §7.3 $\lambda^*$;
  §7.6 (7.6.2) is (4.3.2) in polar form; §7.4 $\sigma_{xz}=\mu\,\partial w/\partial x$.
- §8.1 Example 8.1: strains from Hooke's law (8.1.11), then integrated for displacements; Example 8.6
  displacements depend on $E$ and $\nu$; §8.5 contact uses the plane-strain modulus.
- §4.4 thermoelasticity is used in Chapter 12, which is outside the syllabus: say so in one line, no link.

Chapters 5 to 8 PDF page maps:
- Ch 5 (PDF = book minus 94): §5.1 pp. 1–2; §5.2 pp. 2–6; §5.3 pp. 7–8; §5.4 pp. 8–9; §5.5 pp. 9–11;
  §5.6 pp. 11–12.
- Ch 6 (PDF = book minus 118): §6.1 pp. 1–6; §6.2 p. 6; §6.3 pp. 7–8; §6.5 pp. 10–12; §6.6 pp. 12–14.
- Ch 7 (PDF = book minus 140): §7.1 pp. 1–4; §7.2 pp. 4–7 (Table 7.1 p. 7); §7.3 pp. 7–9; §7.4 pp. 9–10;
  §7.5 pp. 10–12; §7.6 pp. 12–14; exercises pp. 14–17.
- Ch 8 (PDF = book minus 158): §8.1 pp. 1–11 (Example 8.1 pp. 3–5, Example 8.2 pp. 5–7, Example 8.3 pp. 7–11);
  §8.3 pp. 20–22; §8.4 pp. 22–55 (Example 8.6 pp. 22–24; §8.4.1 p. 24; §8.4.2 p. 25; Example 8.7 pp. 26–29;
  §8.4.7 Flamant pp. 33–38; Example 8.10 pp. 49–53; Example 8.11 pp. 53–55); §8.5 pp. 55–61.
