"""Writer A, Topic 2: check every number and identity used in the Topic 2 plan.

Run:  python -I notes-build/scripts/writer-A/a_topic2.py

numpy and sympy are installed in the user site-packages, which `python -I` hides,
so that folder is added to sys.path explicitly below.
"""
import itertools
import sys

sys.path.append(r"C:\Users\amy23\AppData\Roaming\Python\Python312\site-packages")

import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402
from sympy import Matrix, Rational, cos, pi, sin, sqrt  # noqa: E402

R = range(3)
ok = True


def check(label, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS  " if cond else "FAIL  ") + label)


def simp(m):
    return m.applyfunc(sp.nsimplify).applyfunc(sp.simplify)


def num(m, nd=4):
    return np.array(m.evalf(nd + 4).tolist(), dtype=float).round(nd)


def rotz(t):   # Example 1.2 pattern: x1' turned from x1 toward x2
    return Matrix([[cos(t), sin(t), 0], [-sin(t), cos(t), 0], [0, 0, 1]])


def rotx(t):   # same cyclic pattern about x1: x2' turned from x2 toward x3
    return Matrix([[1, 0, 0], [0, cos(t), sin(t)], [0, -sin(t), cos(t)]])


def transform2(Q, A):   # a'_ij = Q_ip Q_jq a_pq written out with explicit sums
    return Matrix(3, 3, lambda i, j: sum(Q[i, p] * Q[j, q] * A[p, q] for p in R for q in R))


def invariants(A):
    I = A.trace()
    II = sp.Rational(1, 2) * (I ** 2 - (A * A).trace())
    III = A.det()
    return sp.nsimplify(sp.simplify(I)), sp.nsimplify(sp.simplify(II)), sp.nsimplify(sp.simplify(III))


# ======================================================================= Example 1.2 (PDF p.9)
print("=== Example 1.2: 60 deg about x3")
Q = rotz(pi / 3)
Q = Q.applyfunc(sp.nsimplify)
cosines = Matrix([[cos(pi / 3), cos(pi / 6), cos(pi / 2)],
                  [cos(5 * pi / 6), cos(pi / 3), cos(pi / 2)],
                  [cos(pi / 2), cos(pi / 2), cos(0)]])
check("Q equals the printed table of cosines (60,30,90 / 150,60,90 / 90,90,0 degrees)", sp.simplify(Q - cosines) == sp.zeros(3, 3))
print("  Q =", Q.tolist())
check("Q = [[1/2, sqrt3/2, 0],[-sqrt3/2, 1/2, 0],[0,0,1]]", Q == Matrix([[Rational(1, 2), sqrt(3) / 2, 0], [-sqrt(3) / 2, Rational(1, 2), 0], [0, 0, 1]]))
check("Q Q^T = I and Q^T Q = I", sp.simplify(Q * Q.T) == sp.eye(3) and sp.simplify(Q.T * Q) == sp.eye(3))
check("det Q = +1", sp.simplify(Q.det()) == 1)
a_vec = Matrix([1, 4, 2])
A12 = Matrix([[1, 0, 3], [0, 2, 2], [3, 2, 4]])
ap = sp.simplify(Q * a_vec)
print("  a'_i = Q a =", ap.tolist(), " numeric", num(ap).flatten())
check("a' = (1/2 + 2 sqrt3, 2 - sqrt3/2, 2)", sp.simplify(ap - Matrix([Rational(1, 2) + 2 * sqrt(3), 2 - sqrt(3) / 2, 2])) == sp.zeros(3, 1))
QA = sp.simplify(Q * A12)
print("  Q a (intermediate) =", QA.tolist())
Ap = sp.simplify(Q * A12 * Q.T)
print("  a'_ij = Q a Q^T =", Ap.tolist())
print("  numeric =\n", num(Ap))
book_Ap = Matrix([[Rational(7, 4), sqrt(3) / 4, Rational(3, 2) + sqrt(3)],
                  [sqrt(3) / 4, Rational(5, 4), 1 - 3 * sqrt(3) / 2],
                  [Rational(3, 2) + sqrt(3), 1 - 3 * sqrt(3) / 2, 4]])
check("a' matches the printed 7/4, sqrt3/4, 3/2+sqrt3 ... matrix", sp.simplify(Ap - book_Ap) == sp.zeros(3, 3))
check("index form Q_ip Q_jq a_pq equals Q a Q^T", sp.simplify(transform2(Q, A12) - Ap) == sp.zeros(3, 3))
check("|a'|^2 = |a|^2 = 21", sp.simplify((ap.T * ap)[0, 0]) == 21 and (a_vec.T * a_vec)[0, 0] == 21)
check("trace a' = trace a = 7", sp.simplify(Ap.trace()) == 7 and A12.trace() == 7)
print("  invariants before:", invariants(A12), " after:", tuple(sp.simplify(v) for v in invariants(Ap)))
check("invariants I, II, III unchanged by the rotation", all(sp.simplify(x - y) == 0 for x, y in zip(invariants(A12), invariants(Ap))))
check("a' stays symmetric", sp.simplify(Ap - Ap.T) == sp.zeros(3, 3))
print("  second route: Q^T a' recovers a:", sp.simplify(Q.T * ap).tolist())
check("inverse law (1.4.7) v = Q^T v' recovers (1,4,2)", sp.simplify(Q.T * ap) == a_vec)
check("inverse law for the matrix: a = Q^T a' Q", sp.simplify(Q.T * Ap * Q - A12) == sp.zeros(3, 3))
# the wrong versions
print("  WRONG Q^T a Q (not the transformation):", sp.simplify(Q.T * A12 * Q).tolist())

# ======================================================================= Exercise 1.6 (case (b) data)
print("\n=== Exercise 1.6: 45 deg about x1, case (b) data")
Qx = rotx(pi / 4).applyfunc(sp.nsimplify)
cos_table = Matrix([[1, cos(pi / 2), cos(pi / 2)],
                    [cos(pi / 2), cos(pi / 4), cos(pi / 4)],
                    [cos(pi / 2), cos(3 * pi / 4), cos(pi / 4)]])
check("Q table: x1'=x1; x2' is 45 deg from x2 and from x3; x3' is 135 deg from x2, 45 deg from x3", sp.simplify(Qx - cos_table) == sp.zeros(3, 3))
print("  Q =", Qx.tolist())
check("Q Q^T = I, det = +1", sp.simplify(Qx * Qx.T) == sp.eye(3) and sp.simplify(Qx.det()) == 1)
Ab = Matrix([[1, 2, 0], [0, 2, 1], [0, 4, 2]])
bb = Matrix([2, 1, 1])
bp = sp.simplify(Qx * bb)
print("  b' =", bp.tolist(), " numeric", num(bp).flatten())
check("b' = (2, sqrt2, 0)", sp.simplify(bp - Matrix([2, sqrt(2), 0])) == sp.zeros(3, 1))
QAb = sp.simplify(Qx * Ab)
print("  Q a (intermediate) =", QAb.tolist())
Abp = sp.simplify(Qx * Ab * Qx.T)
print("  a' =", Abp.tolist(), "\n  numeric =\n", num(Abp))
check("a' = [[1, sqrt2, -sqrt2],[0, 9/2, -3/2],[0, 3/2, -1/2]]",
      sp.simplify(Abp - Matrix([[1, sqrt(2), -sqrt(2)], [0, Rational(9, 2), -Rational(3, 2)], [0, Rational(3, 2), -Rational(1, 2)]])) == sp.zeros(3, 3))
check("index form Q_ip Q_jq a_pq = Q a Q^T", sp.simplify(transform2(Qx, Ab) - Abp) == sp.zeros(3, 3))
check("|b'|^2 = |b|^2 = 6", sp.simplify((bp.T * bp)[0, 0]) == 6 and (bb.T * bb)[0, 0] == 6)
check("trace a' = 5 = trace a", sp.simplify(Abp.trace()) == 5 and Ab.trace() == 5)
print("  invariants before:", invariants(Ab), " after:", tuple(sp.simplify(v) for v in invariants(Abp)))
check("I, II, III unchanged", all(sp.simplify(x - y) == 0 for x, y in zip(invariants(Ab), invariants(Abp))))
check("a_ij b_j transforms like a vector: (a b)' = a' b'", sp.simplify(Qx * (Ab * bb) - Abp * bp) == sp.zeros(3, 1))
print("  a b =", (Ab * bb).tolist(), " (a b)' =", sp.simplify(Qx * (Ab * bb)).tolist())
Qalt = rotx(-pi / 4).applyfunc(sp.nsimplify)
print("  OTHER SENSE (x2' turned toward -x3): b' =", sp.simplify(Qalt * bb).tolist(),
      " a' =", sp.simplify(Qalt * Ab * Qalt.T).tolist())
print("  entries of a' as decimals:", num(Abp).tolist())

# ======================================================================= orthogonality conditions (1.4.9)-(1.4.11)
print("\n=== Orthogonality, determinant")
rng = np.random.default_rng(1)
th = rng.uniform(0, 2 * np.pi, 3)
Qn = np.array(rotz(th[0]).evalf(), dtype=float) @ np.array(rotx(th[1]).evalf(), dtype=float) @ np.array(rotz(th[2]).evalf(), dtype=float)
check("(1.4.9) Q_ji Q_jk = delta_ik (random rotation)", np.allclose(np.einsum("ji,jk->ik", Qn, Qn), np.eye(3)))
check("(1.4.10) Q_ij Q_kj = delta_ik (random rotation)", np.allclose(np.einsum("ij,kj->ik", Qn, Qn), np.eye(3)))
check("(1.4.11) det Q = +1 for the rotation", np.isclose(np.linalg.det(Qn), 1))
refl = Qn @ np.diag([1, 1, -1])
check("a reflection also satisfies (1.4.9)-(1.4.10) but has det = -1", np.allclose(refl @ refl.T, np.eye(3)) and np.isclose(np.linalg.det(refl), -1))
v = rng.standard_normal(3)
vp = Qn @ v
check("(1.4.6) v' = Q v and (1.4.7) v = Q^T v' round trip", np.allclose(Qn.T @ vp, v))
check("lengths preserved", np.isclose(vp @ vp, v @ v))
e_new = Qn  # rows = new axes in old axes
check("rows of Q are orthonormal: e'_i . e'_j = delta_ij", np.allclose(e_new @ e_new.T, np.eye(3)))
e_old_in_new = Qn.T
check("columns of Q give old axes in the new axes: e_i = Q_ji e'_j", np.allclose(Qn.T @ Qn, np.eye(3)))
Atest = rng.standard_normal((3, 3))
Atest = Atest + Atest.T
Aprime = np.einsum("ip,jq,pq->ij", Qn, Qn, Atest)
check("second-order law a'_ij = Q_ip Q_jq a_pq equals Q a Q^T", np.allclose(Aprime, Qn @ Atest @ Qn.T))
# derivation of the second-order law from the dyad: A'_ij = e'_i . A . e'_j
dy = np.einsum("pq,ip,jq->ij", Atest, Qn, Qn)
check("A'_ij = e'_i . (A_pq e_p e_q) . e'_j = A_pq (e'_i.e_p)(e_q.e'_j)", np.allclose(dy, Aprime))

# ======================================================================= Exercise 1.8 and 1.9, epsilon
print("\n=== Isotropic tensors")
al = sp.symbols("alpha")
Qs = (rotz(pi / 3) * rotx(pi / 4)).applyfunc(sp.nsimplify)
d3 = sp.eye(3)
check("Exercise 1.8: Q (alpha I) Q^T = alpha I (exact rotation: 60 deg about x3 then 45 deg about x1)",
      sp.simplify(Qs * (al * d3) * Qs.T - al * d3) == sp.zeros(3, 3))
tt = sp.symbols("theta")
check("Exercise 1.8 for the 2D rotation of Exercise 1.7 with symbolic angle",
      sp.simplify(Matrix([[sp.cos(tt), sp.sin(tt)], [-sp.sin(tt), sp.cos(tt)]]) * (al * sp.eye(2)) * Matrix([[sp.cos(tt), sp.sin(tt)], [-sp.sin(tt), sp.cos(tt)]]).T - al * sp.eye(2)) == sp.zeros(2, 2))
dl = np.eye(3)
al_, be_, ga_ = 2.0, -3.5, 0.75
C = (al_ * np.einsum("ij,kl->ijkl", dl, dl) + be_ * np.einsum("ik,jl->ijkl", dl, dl) + ga_ * np.einsum("il,jk->ijkl", dl, dl))
Cp = np.einsum("ip,jq,kr,ls,pqrs->ijkl", Qn, Qn, Qn, Qn, C)
check("Exercise 1.9: C'_ijkl = Q_ip Q_jq Q_kr Q_ls C_pqrs equals C_ijkl (random rotation)", np.allclose(Cp, C))
# the three terms one by one, as in the answer
t1 = np.einsum("ip,jq,kr,ls,pq,rs->ijkl", Qn, Qn, Qn, Qn, dl, dl)
t2 = np.einsum("ip,jq,kr,ls,pr,qs->ijkl", Qn, Qn, Qn, Qn, dl, dl)
t3 = np.einsum("ip,jq,kr,ls,ps,qr->ijkl", Qn, Qn, Qn, Qn, dl, dl)
check("term 1 -> (Q_ip Q_jp)(Q_kr Q_lr) = d_ij d_kl", np.allclose(t1, np.einsum("ij,kl->ijkl", dl, dl)))
check("term 2 -> (Q_ip Q_kp)(Q_jq Q_lq) = d_ik d_jl", np.allclose(t2, np.einsum("ik,jl->ijkl", dl, dl)))
check("term 3 -> (Q_ip Q_lp)(Q_jq Q_kq) = d_il d_jk", np.allclose(t3, np.einsum("il,jk->ijkl", dl, dl)))
# symmetry C_ijkl = C_klij when beta = gamma (Exercise 1.10, not used but good for the isotropic form)
C2 = (al_ * np.einsum("ij,kl->ijkl", dl, dl) + be_ * (np.einsum("ik,jl->ijkl", dl, dl) + np.einsum("il,jk->ijkl", dl, dl)))
check("(Ex 1.10) beta = gamma gives C_ijkl = C_klij", np.allclose(C2, np.einsum("klij->ijkl", C2)))
eps = np.zeros((3, 3, 3))
for i, j, k in itertools.product(R, repeat=3):
    eps[i, j, k] = float(sp.LeviCivita(i, j, k))
epsp = np.einsum("ip,jq,kr,pqr->ijk", Qn, Qn, Qn, eps)
check("eps_ijk is unchanged by a proper rotation (det Q = +1)", np.allclose(epsp, eps))
epsr = np.einsum("ip,jq,kr,pqr->ijk", refl, refl, refl, eps)
check("eps_ijk changes sign under a reflection (det Q = -1)", np.allclose(epsr, -eps))
check("Q_ip Q_jq Q_kr eps_pqr = det(Q) eps_ijk", np.allclose(epsp, np.linalg.det(Qn) * eps))

# ======================================================================= Example 1.3 (PDF pp.12-13)
print("\n=== Example 1.3")
lam = sp.symbols("lambda")
A13 = Matrix([[2, 0, 0], [0, 3, 4], [0, 4, -3]])
I13, II13, III13 = invariants(A13)
minors = (Matrix([[2, 0], [0, 3]]).det(), Matrix([[3, 4], [4, -3]]).det(), Matrix([[2, 0], [0, -3]]).det())
print("  I, II, III =", I13, II13, III13, " minors:", minors, "sum", sum(minors))
check("I = 2, II = 6 - 25 - 6 = -25, III = 2(-9-16) = -50", (I13, II13, III13) == (2, -25, -50) and minors == (6, -25, -6))
cp = sp.expand((A13 - lam * sp.eye(3)).det())
print("  det(a - lambda I) =", cp, " factored:", sp.factor(cp))
check("-lambda^3 + 2 lambda^2 + 25 lambda - 50 (book)", sp.expand(cp - (-lam ** 3 + 2 * lam ** 2 + 25 * lam - 50)) == 0)
check("= -(lambda-2)(lambda^2-25)", sp.expand(cp + (lam - 2) * (lam ** 2 - 25)) == 0)
roots = sp.solve(cp, lam)
print("  roots:", sorted(roots, reverse=True))
check("roots 5, 2, -5", sorted(roots, reverse=True) == [5, 2, -5])
check("(1.6.5): sum, pair sum, product of roots = I, II, III", (5 + 2 - 5, 5 * 2 + 2 * (-5) + (-5) * 5, 5 * 2 * (-5)) == (2, -25, -50))
for lv in (5, 2, -5):
    print(f"  (a - {lv} I) =", (A13 - lv * sp.eye(3)).tolist())
n1 = Matrix([0, 2, 1]) / sqrt(5)
n2 = Matrix([1, 0, 0])
n3 = Matrix([0, 1, -2]) / sqrt(5)
for nm, nv, lv in (("n(1)", n1, 5), ("n(2)", n2, 2), ("n(3)", n3, -5)):
    check(f"{nm}: a n = {lv} n and unit length", sp.simplify(A13 * nv - lv * nv) == sp.zeros(3, 1) and sp.simplify((nv.T * nv)[0, 0]) == 1)
check("n(1).n(2) = n(1).n(3) = n(2).n(3) = 0", all(sp.simplify((x.T * y)[0, 0]) == 0 for x, y in ((n1, n2), (n1, n3), (n2, n3))))
check("n(1) x n(2) = n(3): right-handed", sp.simplify(n1.cross(n2) - n3) == sp.zeros(3, 1))
Q13 = Matrix.vstack(n1.T, n2.T, n3.T)
print("  Q =", Q13.tolist())
check("Q = [[0, 2/sqrt5, 1/sqrt5],[1,0,0],[0,1/sqrt5,-2/sqrt5]]", Q13 == Matrix([[0, 2 / sqrt(5), 1 / sqrt(5)], [1, 0, 0], [0, 1 / sqrt(5), -2 / sqrt(5)]]))
check("Q orthogonal, det +1", sp.simplify(Q13 * Q13.T) == sp.eye(3) and sp.simplify(Q13.det()) == 1)
QA13 = sp.simplify(Q13 * A13)
print("  Q a (intermediate) =", QA13.tolist())
Ad = sp.simplify(Q13 * A13 * Q13.T)
print("  a' =", Ad.tolist())
check("a' = diag(5, 2, -5)", Ad == sp.diag(5, 2, -5))
check("trace and det preserved", Ad.trace() == 2 and Ad.det() == -50)
# the 3-line proof of the diagonal form: a'_ij = n(i).(a n(j)) = lambda_j n(i).n(j)
ns = [n1, n2, n3]
lams = [5, 2, -5]
check("a'_ij = n(i) . a n(j) = lambda_j delta_ij", all(
    sp.simplify((ns[i].T * A13 * ns[j])[0, 0] - lams[j] * (1 if i == j else 0)) == 0 for i in R for j in R))
# extremal property: diagonal entries of the rotated matrix lie between lambda_3 and lambda_1
worst = []
for _ in range(2000):
    th = rng.uniform(0, 2 * np.pi, 3)
    Qr = np.array(rotz(th[0]).evalf(), dtype=float) @ np.array(rotx(th[1]).evalf(), dtype=float) @ np.array(rotz(th[2]).evalf(), dtype=float)
    d = np.diag(Qr @ np.array(A13.tolist(), dtype=float) @ Qr.T)
    worst.append((d.min(), d.max()))
lo = min(w[0] for w in worst)
hi = max(w[1] for w in worst)
print("  diagonal entries over 2000 random rotations: min %.4f, max %.4f" % (lo, hi))
check("diagonal entries stay within [lambda3, lambda1] = [-5, 5]", lo >= -5 - 1e-9 and hi <= 5 + 1e-9)
# the three-roots argument for the diagonal entry in direction n: n.a.n = sum lambda_k (n.n(k))^2
nn = np.array([0.3, -0.5, 0.8]); nn /= np.linalg.norm(nn)
lhs = nn @ np.array(A13.tolist(), dtype=float) @ nn
rhs = sum(l * (nn @ np.array(nv.evalf().tolist(), dtype=float).flatten()) ** 2 for l, nv in zip(lams, ns))
check("n.a.n = sum lambda_k (n.n(k))^2 (weights sum to 1)", np.isclose(lhs, rhs))

# ======================================================================= Exercise 1.12 (PDF p.26)
print("\n=== Exercise 1.12 matrices (checking my reading against the printed answers)")
mats = {
    "a": (Matrix([[-1, 1, 0], [1, -1, 0], [0, 0, 1]]), [-2, 0, 1]),
    "b": (Matrix([[-2, 1, 0], [1, -2, 0], [0, 0, 0]]), [-3, -1, 0]),
    "c": (Matrix([[-1, 1, 0], [1, -1, 0], [0, 0, 0]]), [-2, 0, 0]),
    "d": (Matrix([[6, -3, 0], [-3, 6, 0], [0, 0, 6]]), [3, 6, 9]),
}
for k, (m, ans) in mats.items():
    ev = sorted(sp.roots(sp.Poly((m - lam * sp.eye(3)).det(), lam), multiple=True))
    print(f"  ({k}) eigenvalues {ev}   printed answer {ans}")
    check(f"1.12({k}) eigenvalues equal the printed answer", ev == sorted(ans))

print("\n=== Exercise 1.12(d)")
A12d = mats["d"][0]
I_, II_, III_ = invariants(A12d)
minors_d = (Matrix([[6, -3], [-3, 6]]).det(), Matrix([[6, 0], [0, 6]]).det(), Matrix([[6, 0], [0, 6]]).det())
print("  I, II, III =", I_, II_, III_, " minors", minors_d)
check("I = 18, II = 27 + 36 + 36 = 99, III = 162", (I_, II_, III_) == (18, 99, 162) and minors_d == (27, 36, 36))
cpd = sp.expand((A12d - lam * sp.eye(3)).det())
print("  det(a - lambda I) =", cpd, "=", sp.factor(cpd))
check("-lambda^3 + 18 lambda^2 - 99 lambda + 162 = -(lambda-3)(lambda-6)(lambda-9)",
      sp.expand(cpd - (-lam ** 3 + 18 * lam ** 2 - 99 * lam + 162)) == 0 and sp.expand(cpd + (lam - 3) * (lam - 6) * (lam - 9)) == 0)
for lv in (9, 6, 3):
    print(f"  (a - {lv} I) =", (A12d - lv * sp.eye(3)).tolist())
m1 = Matrix([1, -1, 0]) / sqrt(2)      # lambda = 9
m2 = Matrix([0, 0, 1])                 # lambda = 6
m3 = Matrix([-1, -1, 0]) / sqrt(2)     # lambda = 3, sign chosen so that m1 x m2 = m3
check("a m1 = 9 m1, a m2 = 6 m2, a m3 = 3 m3",
      all(sp.simplify(A12d * mv - lv * mv) == sp.zeros(3, 1) for mv, lv in ((m1, 9), (m2, 6), (m3, 3))))
check("m1 x m2 = m3 (right-handed) with m3 = (-1,-1,0)/sqrt2", sp.simplify(m1.cross(m2) - m3) == sp.zeros(3, 1))
Qd = Matrix.vstack(m1.T, m2.T, m3.T)
print("  Q =", Qd.tolist(), " det =", sp.simplify(Qd.det()))
check("det Q = +1", sp.simplify(Qd.det()) == 1)
QAd = sp.simplify(Qd * A12d)
print("  Q a (intermediate) =", QAd.tolist())
Add = sp.simplify(Qd * A12d * Qd.T)
print("  a' =", Add.tolist())
check("a' = diag(9, 6, 3)", Add == sp.diag(9, 6, 3))
# if the other sign for m3 were used
Qbad = Matrix.vstack(m1.T, m2.T, (-m3).T)
print("  with m3 = (+1,+1,0)/sqrt2 : det Q =", sp.simplify(Qbad.det()), " a' =", sp.simplify(Qbad * A12d * Qbad.T).tolist())
# ascending order used by the book's list (3, 6, 9)
Qasc = Matrix.vstack((-m3).T, m2.T, m1.T)
print("  ascending order (3,6,9): rows (1,1,0)/sqrt2, e3, (1,-1,0)/sqrt2: det =", sp.simplify(Qasc.det()),
      " a' =", sp.simplify(Qasc * A12d * Qasc.T).tolist())

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
