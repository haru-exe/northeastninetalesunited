"""Writer A, Topic 3: check every number and formula used in the Topic 3 plan.

Run:  python -I notes-build/scripts/writer-A/a_topic3.py

numpy and sympy are installed in the user site-packages, which `python -I` hides,
so that folder is added to sys.path explicitly below.

Curvilinear formulas are tested two ways: (1) with generic functions, where all
derivatives are taken through the inverse Jacobian (no curvilinear formula is used
to build the reference), and (2) numerically at random points on polynomial test fields.
"""
import itertools
import sys

sys.path.append(r"C:\Users\amy23\AppData\Roaming\Python\Python312\site-packages")

import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402
from sympy import LeviCivita, Matrix, Rational, cos, sin, sqrt  # noqa: E402

R3 = range(3)
ok = True


def check(label, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS  " if cond else "FAIL  ") + label)


def zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


# ====================================================================== Cartesian operators
x, y, z = sp.symbols("x y z", real=True)
X = (x, y, z)


def grad(f):
    return Matrix([sp.diff(f, v) for v in X])


def div(u):
    return sum(sp.diff(u[i], X[i]) for i in R3)


def curl(u):
    return Matrix([sp.diff(u[2], y) - sp.diff(u[1], z), sp.diff(u[0], z) - sp.diff(u[2], x), sp.diff(u[1], x) - sp.diff(u[0], y)])


def lap(f):
    return sum(sp.diff(f, v, 2) for v in X)


def lapv(u):
    return Matrix([lap(c) for c in u])


def gradv(u):   # u_i,j : row = component, column = derivative direction (Cartesian convention (1.8.4))
    return Matrix(3, 3, lambda i, j: sp.diff(u[i], X[j]))


def curl_index(u):   # (curl u)_i = eps_ijk u_k,j
    return Matrix([sum(LeviCivita(i, j, k) * sp.diff(u[k], X[j]) for j in R3 for k in R3) for i in R3])


# ====================================================================== Example 1.4 (PDF p.17)
print("=== Example 1.4")
phi = x ** 2 - y ** 2
u = Matrix([2 * x, 3 * y * z, x * y])
print("  grad phi =", grad(phi).T.tolist(), " lap phi =", lap(phi), " div u =", div(u))
print("  grad u (u_i,j) =", gradv(u).tolist())
print("  curl u =", curl(u).T.tolist(), " lap u =", lapv(u).T.tolist())
check("grad phi = (2x, -2y, 0)", grad(phi) == Matrix([2 * x, -2 * y, 0]))
check("lap phi = 2 - 2 = 0", lap(phi) == 0)
check("div u = 2 + 3z + 0", sp.expand(div(u) - (2 + 3 * z)) == 0)
check("grad u = [[2,0,0],[0,3z,3y],[y,x,0]]", gradv(u) == Matrix([[2, 0, 0], [0, 3 * z, 3 * y], [y, x, 0]]))
check("curl u = (x - 3y) e1 - y e2", sp.expand(curl(u) - Matrix([x - 3 * y, -y, 0])) == sp.zeros(3, 1))
check("curl from index form eps_ijk u_k,j agrees with the determinant form", sp.expand(curl_index(u) - curl(u)) == sp.zeros(3, 1))
check("tr(grad u) = div u", sp.expand(gradv(u).trace() - div(u)) == 0)
check("lap u = 0 for this u", lapv(u) == sp.zeros(3, 1))
# gradient is perpendicular to the contour phi = const (check at (1,0))
pt = {x: 1, y: 0, z: 0}
g1 = grad(phi).subs(pt)
tangent = Matrix([0, 1, 0])   # contour x^2 - y^2 = 1 through (1,0): 2x dx - 2y dy = 0 -> dx = 0
print("  at (1,0,0): grad phi =", g1.T.tolist(), "tangent to contour =", tangent.T.tolist(), "dot =", (g1.T * tangent)[0, 0])
check("grad phi . tangent = 0 at (1,0)", (g1.T * tangent)[0, 0] == 0)
# directional derivative (1.8.1) example
nvec = Matrix([1, 1, 0]) / sqrt(2)
print("  directional derivative of phi at (1,0,0) along (1,1,0)/sqrt2 =", sp.simplify((nvec.T * g1)[0, 0]))

# ====================================================================== Exercise 1.14
print("\n=== Exercise 1.14 (a), (b), (c)  with x1,x2,x3 = x,y,z")
fields = {
    "a": Matrix([x, x * y, 2 * x * y * z]),
    "b": Matrix([x ** 2, 2 * x * y, z ** 3]),
    "c": Matrix([y ** 2, 2 * y * z, 4 * x ** 2]),
}
for k, uu in fields.items():
    print(f"  ({k}) u =", uu.T.tolist())
    print("      div u =", sp.expand(div(uu)), "| curl u =", curl(uu).T.tolist(), "| lap u =", lapv(uu).T.tolist())
    print("      grad u =", gradv(uu).tolist(), "| tr =", sp.expand(gradv(uu).trace()))
ua = fields["a"]
check("1.14(a) div u = 1 + x1 + 2 x1 x2", sp.expand(div(ua) - (1 + x + 2 * x * y)) == 0)
check("1.14(a) curl u = (2 x1 x3, -2 x2 x3, x2)", sp.expand(curl(ua) - Matrix([2 * x * z, -2 * y * z, y])) == sp.zeros(3, 1))
check("1.14(a) lap u = 0", lapv(ua) == sp.zeros(3, 1))
check("1.14(a) grad u = [[1,0,0],[x2,x1,0],[2x2x3, 2x1x3, 2x1x2]]", gradv(ua) == Matrix([[1, 0, 0], [y, x, 0], [2 * y * z, 2 * x * z, 2 * x * y]]))
check("1.14(a) tr(grad u) = 1 + x1 + 2 x1 x2", sp.expand(gradv(ua).trace() - (1 + x + 2 * x * y)) == 0)

# ====================================================================== identities (1.8.5), generic functions
print("\n=== Identities (1.8.5), printed order 1..10")
f1 = sp.Function("phi")(x, y, z)
f2 = sp.Function("psi")(x, y, z)
U = Matrix([sp.Function(f"u{i}")(x, y, z) for i in (1, 2, 3)])
V = Matrix([sp.Function(f"v{i}")(x, y, z) for i in (1, 2, 3)])


def dot(a, b):
    return sum(a[i] * b[i] for i in R3)


ident = {
    1: (grad(f1 * f2), grad(f1) * f2 + f1 * grad(f2)),
    2: (lap(f1 * f2), lap(f1) * f2 + f1 * lap(f2) + 2 * dot(grad(f1), grad(f2))),
    3: (div(f1 * U), dot(grad(f1), U) + f1 * div(U)),
    4: (curl(f1 * U), grad(f1).cross(U) + f1 * curl(U)),
    5: (div(U.cross(V)), dot(V, curl(U)) - dot(U, curl(V))),
    6: (curl(grad(f1)), sp.zeros(3, 1)),
    7: (div(grad(f1)), lap(f1)),
    8: (div(curl(U)), 0),
    9: (curl(curl(U)), grad(div(U)) - lapv(U)),
    10: (U.cross(curl(U)), Rational(1, 2) * grad(dot(U, U)) - Matrix([sum(U[j] * sp.diff(U[i], X[j]) for j in R3) for i in R3])),
}
for n, (l, r) in ident.items():
    d = l - r
    d = d if isinstance(d, Matrix) else Matrix([d])
    check(f"(1.8.5)_{n}", all(sp.simplify(sp.expand(e)) == 0 for e in d))
# (1.8.5)_3 on the fields of Example 1.4
lhs3 = sp.expand(div(phi * u))
rhs3 = sp.expand(dot(grad(phi), u) + phi * div(u))
print("  (1.8.5)_3 on Example 1.4 fields: div(phi u) =", lhs3, " | grad phi . u =", sp.expand(dot(grad(phi), u)), " phi div u =", sp.expand(phi * div(u)))
check("(1.8.5)_3 with phi = x^2 - y^2 and u of Example 1.4", sp.expand(lhs3 - rhs3) == 0)
print("  (1.8.5)_3 numerically at (1,2,3):", lhs3.subs({x: 1, y: 2, z: 3}), rhs3.subs({x: 1, y: 2, z: 3}))
check("(1.8.5)_6 curl grad phi = 0 for phi = x^2 - y^2", curl(grad(phi)) == sp.zeros(3, 1))
# index-notation steps for _8 and _9 (the your-turn answer)
S8 = sum(LeviCivita(k, p, q) * sp.diff(U[q], X[p], X[k]) for k in R3 for p in R3 for q in R3)
check("_8 in index form: eps_kpq u_q,pk = 0 (each term cancels with its partner)", sp.simplify(S8) == 0)
S9 = Matrix([sum(LeviCivita(i, j, k) * LeviCivita(k, p, q) * sp.diff(U[q], X[p], X[j]) for j in R3 for k in R3 for p in R3 for q in R3) for i in R3])
S9b = Matrix([sum((int(i == p) * int(j == q) - int(i == q) * int(j == p)) * sp.diff(U[q], X[p], X[j]) for j in R3 for p in R3 for q in R3) for i in R3])
check("_9 step: eps_ijk eps_kpq u_q,pj = (d_ip d_jq - d_iq d_jp) u_q,pj", sp.simplify(S9 - S9b) == sp.zeros(3, 1))
S9c = Matrix([sum(sp.diff(U[j], X[i], X[j]) for j in R3) - sum(sp.diff(U[i], X[j], X[j]) for j in R3) for i in R3])
check("_9 step: = u_j,ji - u_i,jj = [grad(div u) - lap u]_i", sp.simplify(S9b - S9c) == sp.zeros(3, 1) and sp.simplify(S9c - (grad(div(U)) - lapv(U))) == sp.zeros(3, 1))
# numeric illustration for _8 and _9 on a concrete field
Uc = Matrix([x ** 2 * y, y * z ** 2, x * y * z])
print("  concrete field u =", Uc.T.tolist(), ": div curl u =", sp.expand(div(curl(Uc))),
      "| curl curl u =", sp.expand(curl(curl(Uc))).T.tolist(), "| grad div u - lap u =", sp.expand(grad(div(Uc)) - lapv(Uc)).T.tolist())
check("_9 on the concrete field", sp.expand(curl(curl(Uc)) - (grad(div(Uc)) - lapv(Uc))) == sp.zeros(3, 1))

# ====================================================================== scale factors (1.9.6)
print("\n=== Scale factors from (1.9.6)")
r, th, zc = sp.symbols("r theta z", positive=True)
Rr, ph = sp.symbols("R phi", positive=True)


def scale_factors_squared(xs, xis):
    # (1.9.6): h_i^2 = (dx^k/dxi^i)(dx^k/dxi^i), summed over k
    return [sp.simplify(sum(sp.diff(c, xi) ** 2 for c in xs)) for xi in xis]


cyl = (r * cos(th), r * sin(th), zc)
sph = (Rr * cos(th) * sin(ph), Rr * sin(th) * sin(ph), Rr * cos(ph))
hc2 = scale_factors_squared(cyl, (r, th, zc))
hs2 = scale_factors_squared(sph, (Rr, ph, th))
hc = [1, r, 1]
print("  cylindrical (r, theta, z): h^2 =", hc2, "-> h = (1, r, 1)")
print("  spherical (R, phi, theta): h^2 =", hs2, "-> h = (1, R, R sin phi) for 0 < phi < pi")
check("cylindrical h^2 = (1, r^2, 1)", hc2 == [1, r ** 2, 1])
check("spherical h^2 = (1, R^2, R^2 sin^2 phi)", [sp.simplify(a - b) for a, b in zip(hs2, [1, Rr ** 2, Rr ** 2 * sin(ph) ** 2])] == [0, 0, 0])
print("  polar: dx/dr =", [sp.diff(c, r) for c in cyl[:2]], " dx/dtheta =", [sp.diff(c, th) for c in cyl[:2]])
print("  spherical dx/dR =", [sp.simplify(sp.diff(c, Rr)) for c in sph], " dx/dphi =", [sp.simplify(sp.diff(c, ph)) for c in sph], " dx/dtheta =", [sp.simplify(sp.diff(c, th)) for c in sph])

# ====================================================================== polar (Example 1.5) with generic functions
print("\n=== Example 1.5 polar coordinates, generic functions u_r(r,theta), u_t(r,theta)")
ur = sp.Function("u_r")(r, th)
ut = sp.Function("u_t")(r, th)
fp = sp.Function("f")(r, th)
er = Matrix([cos(th), sin(th)])
et = Matrix([-sin(th), cos(th)])
check("(1.9.19) e_r = cos e1 + sin e2, e_theta = -sin e1 + cos e2 follows from (1.9.5) with h = (1, r)",
      [sp.simplify(sp.diff(cyl[i], r) / 1) for i in (0, 1)] == [cos(th), sin(th)] and
      [sp.simplify(sp.diff(cyl[i], th) / r) for i in (0, 1)] == [-sin(th), cos(th)])
check("(1.9.20) d e_r/d theta = e_theta, d e_theta/d theta = - e_r, d/dr = 0",
      sp.diff(er, th) == et and sp.diff(et, th) == -er and sp.diff(er, r) == sp.zeros(2, 1) and sp.diff(et, r) == sp.zeros(2, 1))


def Dx(F):
    return cos(th) * sp.diff(F, r) - sin(th) / r * sp.diff(F, th)


def Dy(F):
    return sin(th) * sp.diff(F, r) + cos(th) / r * sp.diff(F, th)


ucart = ur * er + ut * et
# the derivative operators come from the chain rule through the inverse Jacobian; check them on x and y
check("chain-rule operators: Dx(r cos) = 1, Dy(r cos) = 0, Dx(r sin) = 0, Dy(r sin) = 1",
      sp.simplify(Dx(r * cos(th))) == 1 and sp.simplify(Dy(r * cos(th))) == 0 and sp.simplify(Dx(r * sin(th))) == 0 and sp.simplify(Dy(r * sin(th))) == 1)
G = Matrix(2, 2, lambda i, j: (Dx if i == 0 else Dy)(ucart[j]))     # G_ij = d u_j / d x_i  (derivative FIRST, as in (1.9.17))
c = lambda a, b: sp.simplify((a.T * G * b)[0, 0])   # coefficient of e_a e_b in the book's dyad form
c_rr, c_rt, c_tr, c_tt = c(er, er), c(er, et), c(et, er), c(et, et)
print("  c_rr =", c_rr, "\n  c_r theta =", c_rt, "\n  c_theta r =", c_tr, "\n  c_theta theta =", c_tt)
check("coefficient of e_r e_r = du_r/dr", zero(c_rr - sp.diff(ur, r)))
check("coefficient of e_r e_theta = du_theta/dr", zero(c_rt - sp.diff(ut, r)))
check("coefficient of e_theta e_r = (1/r)(du_r/dtheta - u_theta)", zero(c_tr - (sp.diff(ur, th) - ut) / r))
check("coefficient of e_theta e_theta = (1/r)(du_theta/dtheta + u_r)   <- plus sign", zero(c_tt - (sp.diff(ut, th) + ur) / r))
check("book as printed, (1/r)(du_theta/dtheta - u_r), is NOT equal (misprint)", not zero(c_tt - (sp.diff(ut, th) - ur) / r))
div_p = sp.diff(r * ur, r) / r + sp.diff(ut, th) / r
check("div u = (1/r) d(r u_r)/dr + (1/r) du_theta/dtheta  (= trace of the dyad)", zero(Dx(ucart[0]) + Dy(ucart[1]) - div_p) and zero(c_rr + c_tt - div_p))
curlz_p = sp.diff(r * ut, r) / r - sp.diff(ur, th) / r
check("(curl u)_z = (1/r) d(r u_theta)/dr - (1/r) du_r/dtheta", zero(Dx(ucart[1]) - Dy(ucart[0]) - curlz_p) and zero(c_rt - c_tr - curlz_p))
gx = Matrix([Dx(fp), Dy(fp)])
check("grad f = e_r df/dr + e_theta (1/r) df/dtheta", zero((gx.T * er)[0, 0] - sp.diff(fp, r)) and zero((gx.T * et)[0, 0] - sp.diff(fp, th) / r))
lap_f_p = sp.diff(r * sp.diff(fp, r), r) / r + sp.diff(fp, th, 2) / r ** 2
check("lap f = (1/r) d/dr (r df/dr) + (1/r^2) d2f/dtheta2", zero(Dx(Dx(fp)) + Dy(Dy(fp)) - lap_f_p))
lap_ur = sp.diff(r * sp.diff(ur, r), r) / r + sp.diff(ur, th, 2) / r ** 2
lap_ut = sp.diff(r * sp.diff(ut, r), r) / r + sp.diff(ut, th, 2) / r ** 2
lapu = Matrix([Dx(Dx(ucart[0])) + Dy(Dy(ucart[0])), Dx(Dx(ucart[1])) + Dy(Dy(ucart[1]))])
lap_r_c = (lapu.T * er)[0, 0]
lap_t_c = (lapu.T * et)[0, 0]
check("(lap u)_r = lap u_r - (2/r^2) du_theta/dtheta - u_r/r^2",
      zero(lap_r_c - (lap_ur - 2 / r ** 2 * sp.diff(ut, th) - ur / r ** 2)))
check("(lap u)_theta = lap u_theta + (2/r^2) du_r/dtheta - u_theta/r^2",
      zero(lap_t_c - (lap_ut + 2 / r ** 2 * sp.diff(ur, th) - ut / r ** 2)))
# special fields used as checks in the worked example
for name, (a_r, a_t) in {"u = r e_r (= x e1 + y e2)": (r, 0), "u = r e_theta (= -y e1 + x e2)": (0, r), "u = e_r": (1, 0)}.items():
    sub = {ur: a_r, ut: a_t}
    vals = [sp.simplify(e.subs(sub).doit()) for e in (c_rr, c_rt, c_tr, c_tt, div_p, curlz_p)]
    print(f"  {name}: c_rr, c_r_theta, c_theta_r, c_theta_theta, div, curl_z =", vals)
# a scalar check
ff = r ** 2
print("  lap(r^2) =", sp.simplify(sp.diff(r * sp.diff(ff, r), r) / r), "(Cartesian: lap(x^2 + y^2) = 4)")
# cartesian convention vs the book's convention: transpose
print("  Cartesian (component first) matrix [u_i,j] in the (e_r, e_theta) basis is the TRANSPOSE of [[c_rr, c_r_theta],[c_theta_r, c_theta_theta]]")

# basis derivatives (1.9.10) for polar, cylindrical, spherical (explicit unit vectors)
print("\n=== Derivatives of the unit basis (1.9.10)")


def check_basis_derivatives(name, xs, xis, hs_):
    jac = [Matrix([sp.diff(c_, xi) for c_ in xs]) for xi in xis]
    ehat = [sp.simplify(jac[i] / hs_[i]) for i in range(3)]
    good = True
    for m in range(3):
        for n in range(3):
            direct = sp.simplify(sp.diff(ehat[m], xis[n]))
            if m != n:
                rhs = sp.simplify(sp.diff(hs_[n], xis[m]) / hs_[m] * ehat[n])
            else:
                rr_ = [k for k in range(3) if k != m]
                rhs = sp.simplify(-sum(((sp.diff(hs_[m], xis[k]) / hs_[k]) * ehat[k] for k in rr_), sp.zeros(3, 1)))
            if not sp.simplify(direct - rhs) == sp.zeros(3, 1):
                good = False
                print("   mismatch", name, m, n, direct.T, rhs.T)
    return good, ehat


g1, e_cyl = check_basis_derivatives("cyl", cyl, (r, th, zc), hc)
check("(1.9.10) reproduces d e_i / d xi^j for cylindrical coordinates", g1)
g2, e_sph = check_basis_derivatives("sph", sph, (Rr, ph, th), [1, Rr, Rr * sin(ph)])
check("(1.9.10) reproduces d e_i / d xi^j for spherical coordinates", g2)
print("  spherical unit vectors e_R, e_phi, e_theta:", [e.T.tolist() for e in e_sph])
check("spherical triad e_R x e_phi = e_theta (right-handed)", sp.simplify(e_sph[0].cross(e_sph[1]) - e_sph[2]) == sp.zeros(3, 1))
check("cylindrical triad e_r x e_theta = e_z", sp.simplify(e_cyl[0].cross(e_cyl[1]) - e_cyl[2]) == sp.zeros(3, 1))

# ====================================================================== general formulas (1.9.12)-(1.9.16) applied to cylindrical coordinates
print("\n=== General formulas (1.9.13)-(1.9.16) with h = (1, r, 1) vs generic functions")
ff3 = sp.Function("f")(r, th, zc)
u3 = [sp.Function("u_r")(r, th, zc), sp.Function("u_t")(r, th, zc), sp.Function("u_z")(r, th, zc)]
xi = (r, th, zc)
h = hc


def gen_grad(f):
    return [sp.diff(f, xi[i]) / h[i] for i in range(3)]


def gen_div(u_):
    H = h[0] * h[1] * h[2]
    return sum(sp.diff(H / h[i] * u_[i], xi[i]) for i in range(3)) / H


def gen_lap(f):
    H = h[0] * h[1] * h[2]
    return sum(sp.diff(H / h[i] ** 2 * sp.diff(f, xi[i]), xi[i]) for i in range(3)) / H


def gen_curl(u_):
    out = []
    for i in range(3):
        s_ = 0
        for j in range(3):
            for k in range(3):
                e = LeviCivita(i, j, k)
                if e != 0:
                    s_ += e / (h[j] * h[k]) * sp.diff(u_[k] * h[k], xi[j])
        out.append(s_)
    return out


cg = gen_grad(ff3)
cd = gen_div(u3)
cl = gen_lap(ff3)
cc = gen_curl(u3)
exp_grad = [sp.diff(ff3, r), sp.diff(ff3, th) / r, sp.diff(ff3, zc)]
exp_div = sp.diff(r * u3[0], r) / r + sp.diff(u3[1], th) / r + sp.diff(u3[2], zc)
exp_lap = sp.diff(r * sp.diff(ff3, r), r) / r + sp.diff(ff3, th, 2) / r ** 2 + sp.diff(ff3, zc, 2)
exp_curl = [sp.diff(u3[2], th) / r - sp.diff(u3[1], zc), sp.diff(u3[0], zc) - sp.diff(u3[2], r), sp.diff(r * u3[1], r) / r - sp.diff(u3[0], th) / r]
check("grad f (cylindrical) from (1.9.13)", all(zero(a - b) for a, b in zip(cg, exp_grad)))
check("div u (cylindrical) from (1.9.14)", zero(cd - exp_div))
check("lap f (cylindrical) from (1.9.15)", zero(cl - exp_lap))
check("curl u (cylindrical) from (1.9.16)", all(zero(a - b) for a, b in zip(cc, exp_curl)))
print("  div u =", exp_div)
print("  curl u components =", exp_curl)
# step values used in the answer: h1 h2 h3 = r and the three sums
print("  (1.9.14) with h1 h2 h3 = r: (1/r)[ d(r u_r)/dr + d(u_theta)/d theta + d(r u_z)/dz ] =",
      sp.simplify(sum(sp.diff(r / h[i] * u3[i], xi[i]) for i in range(3)) / r))

# independent check of the same formulas with the chain rule through the inverse Jacobian, polynomial test fields
print("\n=== Cylindrical formulas against Cartesian calculation at random points")
rng = np.random.default_rng(7)
fT = x ** 2 * y + y ** 3 * z + x * z ** 2
UT = Matrix([x * y + z ** 2, x ** 2 - y * z, x * y * z + y ** 2])
sub_c = {x: r * cos(th), y: r * sin(th), z: zc}   # the cylindrical z is the Cartesian z (different sympy symbol, so substitute it)
erc, etc_, ezc = Matrix([cos(th), sin(th), 0]), Matrix([-sin(th), cos(th), 0]), Matrix([0, 0, 1])


def to_polar(expr):
    return expr.subs(sub_c)


def comps(vec):   # Cartesian components -> (r, theta, z) components, as functions of r, theta, z
    v = vec.subs(sub_c)
    return [sp.simplify((v.T * e)[0, 0]) for e in (erc, etc_, ezc)]


fp3 = to_polar(fT)
Up = comps(UT)
cart_grad = comps(grad(fT))
cart_div = to_polar(div(UT))
cart_lap = to_polar(lap(fT))
cart_curl = comps(curl(UT))
cart_lapu = comps(lapv(UT))
pg = [sp.diff(fp3, r), sp.diff(fp3, th) / r, sp.diff(fp3, zc)]
pdv = sp.diff(r * Up[0], r) / r + sp.diff(Up[1], th) / r + sp.diff(Up[2], zc)
plp = sp.diff(r * sp.diff(fp3, r), r) / r + sp.diff(fp3, th, 2) / r ** 2 + sp.diff(fp3, zc, 2)
pcl = [sp.diff(Up[2], th) / r - sp.diff(Up[1], zc), sp.diff(Up[0], zc) - sp.diff(Up[2], r), sp.diff(r * Up[1], r) / r - sp.diff(Up[0], th) / r]
check("cylindrical grad f", all(zero(a - b) for a, b in zip(pg, cart_grad)))
check("cylindrical div u", zero(pdv - cart_div))
check("cylindrical lap f", zero(plp - cart_lap))
check("cylindrical curl u", all(zero(a - b) for a, b in zip(pcl, cart_curl)))
print("  position vector u = r e_r + z e_z: div =", sp.simplify(sp.diff(r * r, r) / r + 0 + sp.diff(zc, zc)), " (should be 3);  f = r^2 + z^2: lap =",
      sp.simplify(sp.diff(r * sp.diff(r ** 2 + zc ** 2, r), r) / r + sp.diff(r ** 2 + zc ** 2, zc, 2)), " (should be 6)")

# ====================================================================== spherical (Exercise 1.18) numeric
print("\n=== Spherical formulas (Exercise 1.18) against Cartesian calculation")
sub_s = {x: Rr * cos(th) * sin(ph), y: Rr * sin(th) * sin(ph), z: Rr * cos(ph)}
eR, ephi, eth = e_sph


def comps_s(vec):
    v = vec.subs(sub_s)
    return [sp.simplify((v.T * e)[0, 0]) for e in (eR, ephi, eth)]


fs = fT.subs(sub_s)
Us = comps_s(UT)
cart_grad_s = comps_s(grad(fT))
cart_div_s = div(UT).subs(sub_s)
cart_lap_s = lap(fT).subs(sub_s)
cart_curl_s = comps_s(curl(UT))
s_ph = sin(ph)
sg = [sp.diff(fs, Rr), sp.diff(fs, ph) / Rr, sp.diff(fs, th) / (Rr * s_ph)]
sdv = sp.diff(Rr ** 2 * Us[0], Rr) / Rr ** 2 + sp.diff(s_ph * Us[1], ph) / (Rr * s_ph) + sp.diff(Us[2], th) / (Rr * s_ph)
slp = sp.diff(Rr ** 2 * sp.diff(fs, Rr), Rr) / Rr ** 2 + sp.diff(s_ph * sp.diff(fs, ph), ph) / (Rr ** 2 * s_ph) + sp.diff(fs, th, 2) / (Rr ** 2 * s_ph ** 2)
scl = [(sp.diff(s_ph * Us[2], ph) - sp.diff(Us[1], th)) / (Rr * s_ph),
       sp.diff(Us[0], th) / (Rr * s_ph) - sp.diff(Rr * Us[2], Rr) / Rr,
       (sp.diff(Rr * Us[1], Rr) - sp.diff(Us[0], ph)) / Rr]


def numeq(a, b, n=4):
    for _ in range(n):
        pt = {Rr: float(rng.uniform(0.5, 2)), ph: float(rng.uniform(0.3, 2.8)), th: float(rng.uniform(0, 6.2))}
        if abs(complex(sp.N(a.subs(pt) - b.subs(pt)))) > 1e-9:
            return False
    return True


check("spherical grad f", all(numeq(a, b) for a, b in zip(sg, cart_grad_s)))
check("spherical div u with a PLUS before the last term", numeq(sdv, cart_div_s))
check("spherical lap f", numeq(slp, cart_lap_s))
check("spherical curl u (e_R, e_phi, e_theta components as printed)", all(numeq(a, b) for a, b in zip(scl, cart_curl_s)))
print("  (book prints no '+' between the second and third terms of div u in Exercise 1.18)")

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
