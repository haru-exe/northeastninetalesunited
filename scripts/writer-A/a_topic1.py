"""Writer A, Topic 1: check every number and identity used in the Topic 1 plan.

Run:  python -I notes-build/scripts/writer-A/a_topic1.py

numpy and sympy are installed in the user site-packages, which `python -I` hides,
so that folder is added to sys.path explicitly below.
"""
import itertools
import sys

sys.path.append(r"C:\Users\amy23\AppData\Roaming\Python\Python312\site-packages")

import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402
from sympy import LeviCivita, Matrix, Rational  # noqa: E402

R = range(3)
ok = True


def check(label, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS  " if cond else "FAIL  ") + label)


def delta(i, j):
    return 1 if i == j else 0


# ---------------------------------------------------------------- index-sum helpers
def a_ii(a):
    return sum(a[i, i] for i in R)


def a_ij_a_ij(a):
    return sum(a[i, j] * a[i, j] for i in R for j in R)


def a_ij_a_jk(a):
    return Matrix(3, 3, lambda i, k: sum(a[i, j] * a[j, k] for j in R))


def a_ij_b_j(a, b):
    return Matrix(3, 1, lambda i, _: sum(a[i, j] * b[j] for j in R))


def a_ij_b_i_b_j(a, b):
    return sum(a[i, j] * b[i] * b[j] for i in R for j in R)


def b_i_b_i(b):
    return sum(b[i] * b[i] for i in R)


def b_i_b_j(b):
    return Matrix(3, 3, lambda i, j: b[i] * b[j])


def sym(a):
    return Matrix(3, 3, lambda i, j: Rational(1, 2) * (a[i, j] + a[j, i]))


def asym(a):
    return Matrix(3, 3, lambda i, j: Rational(1, 2) * (a[i, j] - a[j, i]))


def all_quantities(a, b, name):
    print(f"--- {name}")
    out = {
        "a_ii": a_ii(a),
        "a_ij a_ij": a_ij_a_ij(a),
        "a_ij a_jk": a_ij_a_jk(a),
        "a_ij b_j": a_ij_b_j(a, b),
        "a_ij b_i b_j": a_ij_b_i_b_j(a, b),
        "b_i b_i": b_i_b_i(b),
        "b_i b_j": b_i_b_j(b),
    }
    for k, v in out.items():
        print(f"  {k} = {v.tolist() if hasattr(v, 'tolist') else v}")
    # cross-check against ordinary matrix algebra
    check(f"{name}: a_ii = trace", out["a_ii"] == a.trace())
    check(f"{name}: a_ij a_jk = a*a", out["a_ij a_jk"] == a * a)
    check(f"{name}: a_ij b_j = a*b", out["a_ij b_j"] == a * b)
    check(f"{name}: a_ij b_i b_j = b^T a b", out["a_ij b_i b_j"] == (b.T * a * b)[0, 0])
    check(f"{name}: b_i b_j = b*b^T", out["b_i b_j"] == b * b.T)
    return out


# ---------------------------------------------------------------- Example 1.1 (book PDF p.4)
a11 = Matrix([[1, 2, 0], [0, 4, 3], [2, 1, 2]])
b11 = Matrix([2, 4, 0])
o = all_quantities(a11, b11, "Example 1.1")
check("Ex1.1 a_ii = 7", o["a_ii"] == 7)
check("Ex1.1 a_ij a_ij = 39", o["a_ij a_ij"] == 39)
check("Ex1.1 a_ij a_jk = [[1,10,6],[6,19,18],[6,10,7]]", o["a_ij a_jk"] == Matrix([[1, 10, 6], [6, 19, 18], [6, 10, 7]]))
check("Ex1.1 a_ij b_j = (10,16,8)", o["a_ij b_j"] == Matrix([10, 16, 8]))
check("Ex1.1 a_ij b_i b_j = 84", o["a_ij b_i b_j"] == 84)
check("Ex1.1 b_i b_i = 20", o["b_i b_i"] == 20)
check("Ex1.1 b_i b_j = [[4,8,0],[8,16,0],[0,0,0]]", o["b_i b_j"] == Matrix([[4, 8, 0], [8, 16, 0], [0, 0, 0]]))
check("Ex1.1 sym part", sym(a11) == Matrix([[1, 1, 1], [1, 4, 2], [1, 2, 2]]))
check("Ex1.1 antisym part", asym(a11) == Matrix([[0, 1, -1], [-1, 0, 1], [1, -1, 0]]))
check("Ex1.1 a = sym + antisym", sym(a11) + asym(a11) == a11)
s = sum(sym(a11)[i, j] * asym(a11)[i, j] for i in R for j in R)
print("  a_(ij) a_[ij] summed term by term =", s)
check("Ex1.1 a_(ij) a_[ij] = 0 (1.2.9)", s == 0)
terms = [sym(a11)[i, j] * asym(a11)[i, j] for i in R for j in R]
print("  the nine products (row by row):", terms)

# ---------------------------------------------------------------- Exercise 1.1(b) (book PDF p.25)
ab = Matrix([[1, 2, 0], [0, 2, 1], [0, 4, 2]])
bb = Matrix([2, 1, 1])
ob = all_quantities(ab, bb, "Exercise 1.1(b)")
check("Ex1.1(b) a_ii = 5", ob["a_ii"] == 5)
check("Ex1.1(b) a_ij a_ij = 30", ob["a_ij a_ij"] == 30)
check("Ex1.1(b) a_ij a_jk = [[1,6,2],[0,8,4],[0,16,8]]", ob["a_ij a_jk"] == Matrix([[1, 6, 2], [0, 8, 4], [0, 16, 8]]))
check("Ex1.1(b) a_ij b_j = (4,3,6)", ob["a_ij b_j"] == Matrix([4, 3, 6]))
check("Ex1.1(b) a_ij b_i b_j = 17", ob["a_ij b_i b_j"] == 17)
check("Ex1.1(b) b_i b_i = 6", ob["b_i b_i"] == 6)
check("Ex1.1(b) b_i b_j", ob["b_i b_j"] == Matrix([[4, 2, 2], [2, 1, 1], [2, 1, 1]]))
print("  the nine squares in a_ij a_ij:", [ab[i, j] ** 2 for i in R for j in R])
print("  a_ij b_i b_j expanded term by term:", [(i + 1, j + 1, ab[i, j] * bb[i] * bb[j]) for i in R for j in R if ab[i, j] != 0])

# ---------------------------------------------------------------- Exercise 1.2 with the matrix of 1.1(b)
S, A = sym(ab), asym(ab)
print("--- Exercise 1.2, matrix of 1.1(b)")
print("  a_(ij) =", S.tolist())
print("  a_[ij] =", A.tolist())
check("Ex1.2 sym part", S == Matrix([[1, 1, 0], [1, 2, Rational(5, 2)], [0, Rational(5, 2), 2]]))
check("Ex1.2 antisym part", A == Matrix([[0, 1, 0], [-1, 0, Rational(-3, 2)], [0, Rational(3, 2), 0]]))
check("Ex1.2 sum = a", S + A == ab)
check("Ex1.2 S symmetric", S == S.T)
check("Ex1.2 A antisymmetric, zero diagonal", A == -A.T and all(A[i, i] == 0 for i in R))
s2 = sum(S[i, j] * A[i, j] for i in R for j in R)
print("  a_(ij) a_[ij] =", s2, " terms:", [S[i, j] * A[i, j] for i in R for j in R])
check("Ex1.2 a_(ij) a_[ij] = 0", s2 == 0)
print("  independent components: symmetric", sorted({S[i, j] for i in R for j in range(i, 3)}, key=str),
      "(6 entries i<=j:", [S[i, j] for i in R for j in range(i, 3)], ")  antisymmetric upper entries:", [A[0, 1], A[0, 2], A[1, 2]])

# ---------------------------------------------------------------- (1.2.9) for general index pairs (numeric)
rng = np.random.default_rng(0)
X = rng.standard_normal((3, 3, 3, 3))
Y = rng.standard_normal((3, 3, 3, 3))
Asym = X + X.swapaxes(2, 3)        # symmetric in the last pair (m,n)
Basym = Y - Y.swapaxes(2, 3)       # antisymmetric in the last pair (m,n)
c = np.einsum("ijmn,pqmn->ijpq", Asym, Basym)
check("(1.2.9) symmetric x antisymmetric over a pair = 0 (random 4th-order arrays)", np.allclose(c, 0))
M = rng.standard_normal((3, 3))
Ms, Ma = (M + M.T) / 2, (M - M.T) / 2
check("(1.2.10) split reproduces M", np.allclose(Ms + Ma, M))
check("symmetric part has 6, antisymmetric 3 independent numbers (counts)", (6, 3) == (3 * 4 // 2, 3 * 2 // 2))

# ---------------------------------------------------------------- delta rules (1.3.2)
d = Matrix(3, 3, lambda i, j: delta(i, j))
check("delta_ii = 3", sum(delta(i, i) for i in R) == 3)
check("delta_ij delta_ij = 3", sum(delta(i, j) * delta(i, j) for i in R for j in R) == 3)
check("delta_ij a_j = a_i (symbolic)", all(
    sum(delta(i, j) * sp.Symbol(f"a{j+1}") for j in R) == sp.Symbol(f"a{i+1}") for i in R))
aa = Matrix(3, 3, lambda i, j: sp.Symbol(f"a{i+1}{j+1}"))
check("delta_ij a_jk = a_ik (symbolic)", Matrix(3, 3, lambda i, k: sum(delta(i, j) * aa[j, k] for j in R)) == aa)
check("delta_ij a_ij = a_ii (symbolic)", sum(delta(i, j) * aa[i, j] for i in R for j in R) == aa.trace())

# ---------------------------------------------------------------- epsilon-delta identity (1.3.5) and contraction
def det_deltas(i, j, k, p, q, r):
    return Matrix([[delta(i, p), delta(i, q), delta(i, r)],
                   [delta(j, p), delta(j, q), delta(j, r)],
                   [delta(k, p), delta(k, q), delta(k, r)]]).det()


check("(1.3.5) eps_ijk eps_pqr = det of deltas, all 729 index combinations",
      all(LeviCivita(i, j, k) * LeviCivita(p, q, r) == det_deltas(i, j, k, p, q, r)
          for i, j, k, p, q, r in itertools.product(R, repeat=6)))
check("contracted: eps_ijk eps_imn = d_jm d_kn - d_jn d_km, all 81 combinations",
      all(sum(LeviCivita(i, j, k) * LeviCivita(i, m, n) for i in R)
          == delta(j, m) * delta(k, n) - delta(j, n) * delta(k, m)
          for j, k, m, n in itertools.product(R, repeat=4)))
# the three terms of the expansion after setting p = i (used in the derivation)
def term_check(j, q, r, k):
    X = delta(j, q) * delta(k, r) - delta(j, r) * delta(k, q)
    t1 = sum(delta(i, i) for i in R) * X                          # delta_ii (...)   = 3X
    t2 = -sum(delta(i, q) * (delta(j, i) * delta(k, r) - delta(j, r) * delta(k, i)) for i in R)   # = -X
    t3 = sum(delta(i, r) * (delta(j, i) * delta(k, q) - delta(j, q) * delta(k, i)) for i in R)    # = -X
    return (t1 == 3 * X) and (t2 == -X) and (t3 == -X) and (t1 + t2 + t3 == X)


check("derivation: the three terms are 3X, -X, -X (X = d_jq d_kr - d_jr d_kq), sum = X",
      all(term_check(j, q, r, k) for j, q, r, k in itertools.product(R, repeat=4)))
check("shifted form eps_kij eps_kpq = d_ip d_jq - d_iq d_jp (used in 3B)",
      all(sum(LeviCivita(k, i, j) * LeviCivita(k, p, q) for k in R) == delta(i, p) * delta(j, q) - delta(i, q) * delta(j, p)
          for i, j, p, q in itertools.product(R, repeat=4)))
check("cyclic reorder eps_ijk = eps_kij = eps_jki", all(
    LeviCivita(i, j, k) == LeviCivita(k, i, j) == LeviCivita(j, k, i) for i, j, k in itertools.product(R, repeat=3)))
n_plus = sum(1 for i, j, k in itertools.product(R, repeat=3) if LeviCivita(i, j, k) == 1)
n_minus = sum(1 for i, j, k in itertools.product(R, repeat=3) if LeviCivita(i, j, k) == -1)
check("eps: three +1, three -1, 21 zeros", (n_plus, n_minus) == (3, 3))

# ---------------------------------------------------------------- Exercise 1.15 (dual vector)
p, q, r_ = sp.symbols("p q r")
akj = Matrix([[0, p, q], [-p, 0, r_], [-q, -r_, 0]])    # general antisymmetric a_jk
dual = [sp.simplify(-Rational(1, 2) * sum(LeviCivita(i, j, k) * akj[j, k] for j in R for k in R)) for i in R]
print("--- Exercise 1.15")
print("  a_jk = ", akj.tolist())
print("  dual a_i = -1/2 eps_ijk a_jk =", dual)
check("a_1 = -a_23, a_2 = -a_31, a_3 = -a_12", dual == [-akj[1, 2], -akj[2, 0], -akj[0, 1]])
back = Matrix(3, 3, lambda j, k: sp.simplify(-sum(LeviCivita(i, j, k) * dual[i] for i in R)))
check("inversion a_jk = -eps_ijk a_i recovers a_jk", back == akj)
print("  recovered matrix:", back.tolist())
# numeric example: the antisymmetric part of Example 1.1
A11 = asym(a11)
d11 = [-Rational(1, 2) * sum(LeviCivita(i, j, k) * A11[j, k] for j in R for k in R) for i in R]
back11 = Matrix(3, 3, lambda j, k: -sum(LeviCivita(i, j, k) * d11[i] for i in R))
print("  Example 1.1 antisymmetric part:", A11.tolist(), "-> dual vector", d11, "-> rebuilt", back11.tolist())
check("Ex 1.15 numeric example round trip", back11 == A11 and d11 == [-1, -1, -1])
# the step-by-step algebra of the inversion, written with the contracted identity
def lhs_step(pp, qq):  # eps_ipq a_i
    return sum(LeviCivita(i, pp, qq) * dual[i] for i in R)


def rhs_step(pp, qq):  # -1/2 (a_pq - a_qp)
    return -Rational(1, 2) * (akj[pp, qq] - akj[qq, pp])


check("step: eps_ipq a_i = -1/2 (a_pq - a_qp) for all p,q", all(sp.simplify(lhs_step(pp, qq) - rhs_step(pp, qq)) == 0
                                                         for pp in R for qq in R))
check("step: -1/2 (a_pq - a_qp) = -a_pq when a is antisymmetric", all(
    sp.simplify(rhs_step(pp, qq) + akj[pp, qq]) == 0 for pp in R for qq in R))

# ---------------------------------------------------------------- Exercise 1.5 (determinant, both index forms)
print("--- Exercise 1.5")
a = Matrix(3, 3, lambda i, j: sp.Symbol(f"a{i+1}{j+1}"))
row_terms, col_terms = [], []
for i, j, k in itertools.product(R, repeat=3):
    e = LeviCivita(i, j, k)
    if e != 0:
        row_terms.append(((i + 1, j + 1, k + 1), e * a[0, i] * a[1, j] * a[2, k]))
        col_terms.append(((i + 1, j + 1, k + 1), e * a[i, 0] * a[j, 1] * a[k, 2]))
row_sum = sum(t for _, t in row_terms)
col_sum = sum(t for _, t in col_terms)
for (ijk, t) in row_terms:
    print("  row form  eps_ijk a_1i a_2j a_3k  (i,j,k)=%s : %s" % (ijk, t))
for (ijk, t) in col_terms:
    print("  column form eps_ijk a_i1 a_j2 a_k3 (i,j,k)=%s : %s" % (ijk, t))
trad = a[0, 0] * (a[1, 1] * a[2, 2] - a[1, 2] * a[2, 1]) - a[0, 1] * (a[1, 0] * a[2, 2] - a[1, 2] * a[2, 0]) \
    + a[0, 2] * (a[1, 0] * a[2, 1] - a[1, 1] * a[2, 0])
check("only 6 of the 27 triples survive (row form)", len(row_terms) == 6)
check("row form = traditional first-row cofactor expansion", sp.expand(row_sum - trad) == 0)
check("column form = traditional first-row cofactor expansion", sp.expand(col_sum - trad) == 0)
check("both = sympy det", sp.expand(row_sum - a.det()) == 0 and sp.expand(col_sum - a.det()) == 0)
check("(1.3.6) det = 1/6 eps_ijk eps_pqr a_ip a_jq a_kr (symbolic)", sp.expand(
    Rational(1, 6) * sum(LeviCivita(i, j, k) * LeviCivita(pp, qq, rr) * a[i, pp] * a[j, qq] * a[k, rr]
                         for i, j, k, pp, qq, rr in itertools.product(R, repeat=6)) - a.det()) == 0)
print("  traditional:", sp.expand(trad))
# numeric example for the answer's check
nm = Matrix([[1, 2, 0], [0, 2, 1], [0, 4, 2]])
print("  numeric example (matrix of 1.1(b)): det =", nm.det())
nm2 = Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
print("  numeric example sym matrix [[2,1,0],[1,3,1],[0,1,4]]: det =", nm2.det())

# ---------------------------------------------------------------- products in index form (1.7.x)
u = Matrix([1, 2, 3])
v = Matrix([4, -1, 2])
w = Matrix([0, 5, 1])
cross_eps = Matrix([sum(LeviCivita(i, j, k) * u[j] * v[k] for j in R for k in R) for i in R])
check("(1.7.3) cross product = eps_ijk a_j b_k", cross_eps == u.cross(v))
trip = sum(LeviCivita(i, j, k) * u[i] * v[j] * w[k] for i in R for j in R for k in R)
check("(1.7.4) triple product = eps_ijk a_i b_j c_k = det of rows", trip == Matrix([u.T, v.T, w.T]).det())
check("(1.7.6) tr(A B^T) = A_ij B_ij", (ab * a11.T).trace() == sum(ab[i, j] * a11[i, j] for i in R for j in R))
x1 = Matrix([1, 0, 0]); x2 = Matrix([0, 1, 0])
print("  (a x b)_1 = eps_1jk a_j b_k = eps_123 a_2 b_3 + eps_132 a_3 b_2 :",
      LeviCivita(0, 1, 2) * u[1] * v[2] + LeviCivita(0, 2, 1) * u[2] * v[1], "vs", u.cross(v)[0])

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
