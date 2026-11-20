"""Writer B, Topic 6 checks: Saint-Venant equations (2.6.1)/(2.6.2), Exercise 2.13, 2.17, 2.18.

Run:  python -I notes-build/scripts/writer-B/t6_checks.py
numpy/sympy live in the user site-packages, which -I hides, so that folder is added explicitly below.
"""
import sys
sys.path.append(r"C:\Users\amy23\AppData\Roaming\Python\Python312\site-packages")
import itertools
import numpy as np
import sympy as sp

x, y, z = sp.symbols("x y z", real=True)
X = [x, y, z]
half = sp.Rational(1, 2)
d = sp.diff

print("=== (2.6.1): which of the 81 index equations are distinct? ===")


def sym(i, j, k, l):
    """symbol for e_{ij,kl}: symmetric in (i,j) and in (k,l)"""
    a, b = sorted((i, j)); c, dd = sorted((k, l))
    return sp.Symbol("e%d%d_%d%d" % (a + 1, b + 1, c + 1, dd + 1))


R = {}
for i, j, k, l in itertools.product(range(3), repeat=4):
    R[(i, j, k, l)] = sym(i, j, k, l) + sym(k, l, i, j) - sym(i, k, j, l) - sym(j, l, i, k)
nonzero = {key: sp.expand(v) for key, v in R.items() if sp.expand(v) != 0}
print("number of index combinations (i,j,k,l):", len(R), "; not identically zero:", len(nonzero))
distinct = {}
for key, v in nonzero.items():
    canon = v if str(v) <= str(-v) else -v
    canon = sp.expand(canon)
    distinct.setdefault(str(canon), []).append(key)
print("distinct non-zero equations up to an overall sign:", len(distinct))
syms = sorted({s_ for v in nonzero.values() for s_ in v.free_symbols}, key=str)
Mx = sp.Matrix([[v.coeff(s_) for s_ in syms] for v in nonzero.values()])
print("rank of the coefficient matrix (independent linear equations among the e_ij,kl):", Mx.rank())
print("specific choices with k = l (no sum):")
for key in [(0, 0, 1, 1), (1, 1, 2, 2), (2, 2, 0, 0), (1, 2, 0, 0), (2, 0, 1, 1), (0, 1, 2, 2)]:
    print("   (i,j,k,l) =", tuple(a + 1 for a in key), "->", R[key], "= 0")

print()
print("=== (2.6.2) as transcribed from p.43, tested on strains built from arbitrary displacements u, v, w ===")
u = sp.Function("u")(x, y, z); v = sp.Function("v")(x, y, z); w = sp.Function("w")(x, y, z)
ex_, ey_, ez_ = d(u, x), d(v, y), d(w, z)
exy_, eyz_, ezx_ = half*(d(u, y) + d(v, x)), half*(d(v, z) + d(w, y)), half*(d(w, x) + d(u, z))
eqs = [
    d(ex_, y, 2) + d(ey_, x, 2) - 2*d(exy_, x, y),
    d(ey_, z, 2) + d(ez_, y, 2) - 2*d(eyz_, y, z),
    d(ez_, x, 2) + d(ex_, z, 2) - 2*d(ezx_, z, x),
    d(ex_, y, z) - d(-d(eyz_, x) + d(ezx_, y) + d(exy_, z), x),
    d(ey_, z, x) - d(-d(ezx_, y) + d(exy_, z) + d(eyz_, x), y),
    d(ez_, x, y) - d(-d(exy_, z) + d(eyz_, x) + d(ezx_, y), z),
]
for n, e_ in enumerate(eqs, 1):
    assert sp.simplify(sp.expand(e_)) == 0, "equation (%d) of (2.6.2) fails for compatible strains" % n
print("all six equations of (2.6.2) vanish identically when e_ij come from u, v, w (necessity): OK")

print()
print("=== Exercise 2.13: first equation of (2.6.2) by scalar differentiation ===")
lhs = d(ex_.subs(w, 0), y, 2) + d(ey_.subs(w, 0), x, 2)
print("d2 e_x/dy2 = d3 u/(dx dy2):", d(ex_, y, 2), "; d2 e_y/dx2 = d3 v/(dx2 dy):", d(ey_, x, 2))
print("2 d2 e_xy/(dx dy) =", sp.simplify(2*d(exy_, x, y)))
assert sp.simplify(d(ex_, y, 2) + d(ey_, x, 2) - 2*d(exy_, x, y)) == 0
print("sum of the first two equals the third (mixed third derivatives commute): OK")

print()
print("=== Exercise 2.17: e_x = A y^3, e_y = A x^3, e_xy = B x y (x+y), others 0 ===")
A, B = sp.symbols("A B", real=True)
E = {"x": A*y**3, "y": A*x**3, "z": sp.Integer(0), "xy": B*x*y*(x + y), "yz": sp.Integer(0), "zx": sp.Integer(0)}
res = [
    d(E["x"], y, 2) + d(E["y"], x, 2) - 2*d(E["xy"], x, y),
    d(E["y"], z, 2) + d(E["z"], y, 2) - 2*d(E["yz"], y, z),
    d(E["z"], x, 2) + d(E["x"], z, 2) - 2*d(E["zx"], z, x),
    d(E["x"], y, z) - d(-d(E["yz"], x) + d(E["zx"], y) + d(E["xy"], z), x),
    d(E["y"], z, x) - d(-d(E["zx"], y) + d(E["xy"], z) + d(E["yz"], x), y),
    d(E["z"], x, y) - d(-d(E["xy"], z) + d(E["yz"], x) + d(E["zx"], y), z),
]
for n, r in enumerate(res, 1):
    print("  residual of equation", n, ":", sp.factor(sp.expand(r)))
print("equation 1: d2 e_x/dy2 = %s ; d2 e_y/dx2 = %s ; 2 d2 e_xy/(dx dy) = %s" %
      (d(E["x"], y, 2), d(E["y"], x, 2), sp.expand(2*d(E["xy"], x, y))))
print("  e_xy = B(x^2 y + x y^2): d/dx = %s ; then d/dy = %s" % (sp.expand(d(E["xy"], x)), sp.expand(d(E["xy"], x, y))))
print("solve residual 1 = 0 for A:", sp.solve(sp.expand(res[0]/(x + y)), A))
# integration when A = 2B/3
Av = sp.Rational(2, 3)*B   # same real symbol B as above
f = sp.Function("f"); g = sp.Function("g")
uu = Av*x*y**3 + f(y); vv = Av*x**3*y + g(x)
shear = sp.expand(d(uu, y) + d(vv, x) - 2*E["xy"].subs(A, Av))
print("with A = 2B/3: u = A x y^3 + f(y), v = A x^3 y + g(x) gives 2e_xy mismatch =", shear, " -> f'(y) + g'(x) = 0")
c0, u0, v0 = sp.symbols("c0 u0 v0")
uf = Av*x*y**3 + c0*y + u0; vf = Av*x**3*y - c0*x + v0
chk = [d(uf, x) - E["x"].subs(A, Av), d(vf, y) - E["y"].subs(A, Av), half*(d(uf, y) + d(vf, x)) - E["xy"].subs(A, Av)]
assert all(sp.simplify(c_) == 0 for c_ in chk)
print("displacements for A = 2B/3: u = (2B/3) x y^3 + c0 y + u0 ; v = (2B/3) x^3 y - c0 x + v0 -> all three strains reproduced: OK")
# why other A fails: mixed derivative of the separation condition
print("for general A: (3A - 2B)(x y^2 + x^2 y) = -(f'(y) + g'(x)); apply d2/(dx dy):",
      sp.factor(d((3*A - 2*B)*(x*y**2 + x**2*y), x, y)), " must vanish -> A = 2B/3")

print()
print("=== Exercise 2.18: screw dislocation u = v = 0, w = b/(2 pi) atan(y/x) ===")
b = sp.Symbol("b", real=True)
W = b/(2*sp.pi)*sp.atan(y/x)
wx, wy = sp.simplify(d(W, x)), sp.simplify(d(W, y))
print("dw/dx =", wx, " ; dw/dy =", wy)
e_xz = sp.simplify(half*wx); e_yz = sp.simplify(half*wy)
book_exz = -b/(4*sp.pi)*y/(x**2 + y**2); book_eyz = b/(4*sp.pi)*x/(x**2 + y**2)
assert sp.simplify(e_xz - book_exz) == 0 and sp.simplify(e_yz - book_eyz) == 0
print("e_xz = -(b/4pi) y/(x^2+y^2), e_yz = (b/4pi) x/(x^2+y^2); e_x = e_y = e_z = e_xy = 0 : OK")
F = {"x": 0, "y": 0, "z": 0, "xy": 0, "yz": book_eyz, "zx": book_exz}
comp = [
    d(F["x"], y, 2) + d(F["y"], x, 2) - 2*d(F["xy"], x, y),
    d(F["y"], z, 2) + d(F["z"], y, 2) - 2*d(F["yz"], y, z),
    d(F["z"], x, 2) + d(F["x"], z, 2) - 2*d(F["zx"], z, x),
    d(F["x"], y, z) - d(-d(F["yz"], x) + d(F["zx"], y) + d(F["xy"], z), x),
    d(F["y"], z, x) - d(-d(F["zx"], y) + d(F["xy"], z) + d(F["yz"], x), y),
    d(F["z"], x, y) - d(-d(F["xy"], z) + d(F["yz"], x) + d(F["zx"], y), z),
]
for n, r in enumerate(comp, 1):
    print("  residual of compatibility equation", n, ":", sp.simplify(r))
    assert sp.simplify(r) == 0
inner = sp.simplify(-d(book_eyz, x) + d(book_exz, y))
print("  key bracket in equations 4 and 5, -de_yz/dx + de_zx/dy =", inner, "  (zero for r > 0, so its x- and y-derivatives vanish)")
print("  de_yz/dx =", sp.simplify(d(book_eyz, x)), " ; de_zx/dy =", sp.simplify(d(book_exz, y)))
# jump of w once round the z-axis
R_, phi = sp.symbols("R phi", positive=True)
xs, ys = R_*sp.cos(phi), R_*sp.sin(phi)
integrand = (2*book_exz*d(xs, phi) + 2*book_eyz*d(ys, phi)).subs({x: xs, y: ys})
jump = sp.integrate(sp.simplify(integrand), (phi, 0, 2*sp.pi))
print("  line integral of dw = 2 e_xz dx + 2 e_yz dy once round the circle of radius R:", sp.simplify(jump), "  (= b)")
print("  integrand simplifies to", sp.simplify(integrand))
# a loop that does NOT enclose the axis: circle of radius 1 centred at (3, 0)
t = sp.symbols("t", real=True)
xs2, ys2 = 3 + sp.cos(t), sp.sin(t)
integ2 = (2*book_exz*d(xs2, t) + 2*book_eyz*d(ys2, t)).subs({x: xs2, y: ys2})
val2 = sp.N(sp.Integral(integ2.subs(b, 1), (t, 0, 2*sp.pi)), 12)   # b = 1
print("  loop not enclosing the axis (circle radius 1 centre (3,0)), numeric:", val2, "(should be ~0)")
# the principal value of atan(y/x) jumps at x = 0: continuous angle needed
print("  w = (b/2pi) theta with theta the continuous polar angle: theta goes 0 -> 2pi so w changes by b")
print("ALL TOPIC 6 CHECKS PASSED")
