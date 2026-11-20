"""Writer B, Topic 4 checks: Example 2.1, Exercises 2.2, 2.3, 2.4 and the small-strain step of (2.2.1).

Run:  python -I notes-build/scripts/writer-B/t4_checks.py
numpy/sympy live in the user site-packages, which -I hides, so that folder is added explicitly below.
"""
import sys
sys.path.append(r"C:\Users\amy23\AppData\Roaming\Python\Python312\site-packages")
import sympy as sp

x, y, z = sp.symbols("x y z", real=True)
A, B, C, k = sp.symbols("A B C k", real=True)
X = [x, y, z]
half = sp.Rational(1, 2)


def grad(U):
    """Displacement gradient u_{i,j} (row i = component, column j = derivative)."""
    return sp.Matrix(3, 3, lambda i, j: sp.diff(U[i], X[j]))


def split(U):
    G = grad(U)
    return G, (G + G.T) / 2, (G - G.T) / 2


def dual(W):
    """omega_i = -1/2 eps_ijk omega_jk  (book p.34, Exercise 1.15)."""
    return sp.Matrix([-half * sum(sp.LeviCivita(i, j, kk) * W[j, kk] for j in range(3) for kk in range(3))
                      for i in range(3)])


def half_curl(U):
    return half * sp.Matrix([sp.diff(U[2], y) - sp.diff(U[1], z),
                             sp.diff(U[0], z) - sp.diff(U[2], x),
                             sp.diff(U[1], x) - sp.diff(U[0], y)])


def zero(M):
    return sp.simplify(M) == sp.zeros(*M.shape)


print("=== Example 2.1: u = A x^2 y, v = B y z, w = C x z^3 ===")
U = [A * x**2 * y, B * y * z, C * x * z**3]
G, e, w = split(U)
book_G = sp.Matrix([[2*A*x*y, A*x**2, 0], [0, B*z, B*y], [C*z**3, 0, 3*C*x*z**2]])
book_e = sp.Matrix([[2*A*x*y, A*x**2/2, C*z**3/2], [A*x**2/2, B*z, B*y/2], [C*z**3/2, B*y/2, 3*C*x*z**2]])
book_w = sp.Matrix([[0, A*x**2/2, -C*z**3/2], [-A*x**2/2, 0, B*y/2], [C*z**3/2, -B*y/2, 0]])
book_om = half * sp.Matrix([-B*y, -C*z**3, -A*x**2])
assert zero(G - book_G), "u_ij differs from the book"
assert zero(e - book_e), "e_ij differs from the book"
assert zero(w - book_w), "omega_ij differs from the book"
assert zero(half_curl(U) - book_om), "omega = 1/2 curl u differs from the book"
assert zero(dual(w) - book_om), "dual vector from omega_ij differs from 1/2 curl u"
assert zero(G - (e + w)), "u_ij != e_ij + omega_ij"
assert sp.simplify(e.trace() - sum(sp.diff(U[i], X[i]) for i in range(3))) == 0
print("u_ij, e_ij, omega_ij, omega (curl form and dual-vector form) all match the book; trace(e) = div u =",
      sp.simplify(e.trace()))
# pointwise numbers, handy for a student's spot check at (x, y, z) = (1, 1, 1) with A = B = C = 1
sub = {A: 1, B: 1, C: 1, x: 1, y: 1, z: 1}
print("spot check A=B=C=1 at (1,1,1): e_ij =", e.subs(sub).tolist(), " omega_ij =", w.subs(sub).tolist(),
      " omega =", book_om.subs(sub).T.tolist())

print()
print("=== Exercise 2.2: u = k(x^2+y^2), v = k(2x - y), w = 0 ===")
U2 = [k * (x**2 + y**2), k * (2*x - y), sp.Integer(0)]
G2, e2, w2 = split(U2)
print("u_ij =", G2.tolist())
print("e_x, e_y, e_xy =", e2[0, 0], "|", e2[1, 1], "|", sp.expand(e2[0, 1]))
omz = sp.expand(half * (sp.diff(U2[1], x) - sp.diff(U2[0], y)))
print("omega_z = 1/2(dv/dx - du/dy) =", omz, "   check vs dual vector:", sp.simplify(dual(w2)[2] - omz) == 0)
at0 = {x: 0, y: 0, z: 0}
print("at the origin: e_x, e_y, e_xy, omega_z =", e2[0, 0].subs(at0), e2[1, 1].subs(at0), e2[0, 1].subs(at0), omz.subs(at0))
# deformed corners of the differential element (first-order Taylor about the origin)
dx, dy = sp.symbols("dx dy", positive=True)
corners = {"A": (0, 0), "B": (dx, 0), "C": (0, dy), "D": (dx, dy)}
G0 = G2.subs(at0)
u0 = sp.Matrix([U2[0].subs(at0), U2[1].subs(at0), 0])
print("first-order deformed corners (origin-based Taylor):")
newpos = {}
for name, (cx, cy) in corners.items():
    r = sp.Matrix([cx, cy, 0])
    rp = r + u0 + G0 * r
    newpos[name] = (sp.simplify(rp[0]), sp.simplify(rp[1]))
    print("  ", name, "->", name + "'", "=", newpos[name])
# lengths and angle
AB = sp.Matrix(newpos["B"]) - sp.Matrix(newpos["A"])
AC = sp.Matrix(newpos["C"]) - sp.Matrix(newpos["A"])
print("  length A'B' / dx =", sp.simplify(AB.norm() / dx), "  (first order: 1 + e_x = 1)")
print("  length A'C' / dy =", sp.simplify(AC.norm() / dy), "  (first order: 1 + e_y = 1 - k)")
ang = sp.acos(AB.dot(AC) / (AB.norm() * AC.norm()))
kv = sp.Rational(1, 10)
print("  angle C'A'B' for k = 0.1 (rad):", sp.N(ang.subs({k: kv, dx: 1, dy: 1})), " ; pi/2 - 2k =", sp.N(sp.pi / 2 - 2 * kv))
print("  A'B' rotates by atan(2k) ~ 2k =", sp.N(sp.atan(2 * kv)), "; A'C' stays vertical (rotation -du/dy = 0)")
print("  mean rotation = k:", sp.N((sp.atan(2 * kv) + 0) / 2), " vs omega_z(0) = k =", kv)

print()
print("=== Exercise 2.3: e = diag(C1, -C2, 0), field depends on x, y only ===")
C1, C2, u0c, v0c, w0c, om = sp.symbols("C1 C2 u0 v0 w0 omega_z", real=True)
Uc = [C1 * x + u0c - om * y, -C2 * y + v0c + om * x, w0c]
Gc, ec, wc = split(Uc)
assert zero(ec - sp.diag(C1, -C2, 0)), "strain of the integrated field is not diag(C1,-C2,0)"
assert sp.simplify(half * (sp.diff(Uc[1], x) - sp.diff(Uc[0], y)) - om) == 0
print("u = C1 x + u0 - omega_z y ; v = -C2 y + v0 + omega_z x ; w = w0  gives e =", ec.tolist(), "and omega_z =", om)
# the separation step: f'(y) + g'(x) = 0 -> both constant. Check the generic route with u = C1 x + f(y), v = -C2 y + g(x)
f = sp.Function("f")
g = sp.Function("g")
e_xy_gen = half * (sp.diff(C1 * x + f(y), y) + sp.diff(-C2 * y + g(x), x))
print("e_xy for u = C1 x + f(y), v = -C2 y + g(x):", e_xy_gen, " -> f'(y) = -g'(x) = constant")

print()
print("=== Exercise 2.4: e = diag(A z, A z, B z) ===")
u0, v0, w0, wx, wy, wz = sp.symbols("u0 v0 w0 omega_x omega_y omega_z", real=True)
rig = [u0 - wz * y + wy * z, v0 - wx * z + wz * x, w0 - wy * x + wx * y]  # (2.2.10)
assert zero(grad(rig) + grad(rig).T), "(2.2.10) does not give zero strain"
print("(2.2.10) rigid-body field gives zero strain: OK (Exercise 2.5 first half)")
part = [A * x * z, A * y * z, B * z**2 / 2 - A * (x**2 + y**2) / 2]
Gp, ep, wp = split(part)
assert zero(ep - sp.diag(A * z, A * z, B * z)), "particular solution has wrong strain"
sol = [part[i] + rig[i] for i in range(3)]
assert zero(split(sol)[1] - sp.diag(A * z, A * z, B * z))
print("particular displacement: u = A x z, v = A y z, w = B z^2/2 - A (x^2+y^2)/2 ; strain =", ep.tolist())
print("   its local rotation vector (position dependent, NOT rigid-body):", sp.simplify(half_curl(part).T).tolist())
# Step-by-step integration check used in the notes
f_ = sp.Function("f")(y, z)
g_ = sp.Function("g")(x, z)
h_ = sp.Function("h")(x, y)
uu = A * x * z + f_
vv = A * y * z + g_
ww = B * z**2 / 2 + h_
print("after integrating the three normal strains:  u = A x z + f(y,z),  v = A y z + g(x,z),  w = B z^2/2 + h(x,y)")
print("e_xy = 0  ->", sp.diff(uu, y) + sp.diff(vv, x), "= 0")
print("e_yz = 0  ->", sp.simplify(sp.diff(vv, z) + sp.diff(ww, y)), "= 0")
print("e_zx = 0  ->", sp.simplify(sp.diff(ww, x) + sp.diff(uu, z)), "= 0")

print()
print("=== Step (2.2.1): size of the terms dropped in A'B' ===")
ux, vx = sp.Rational(1, 1000), sp.Rational(2, 1000)   # displacement gradients of order 10^-3
exact = sp.sqrt((1 + ux)**2 + vx**2)
print("exact A'B'/dx =", sp.N(exact, 12), " ; first-order 1 + du/dx =", 1 + ux,
      " ; difference =", sp.N(exact - (1 + ux), 4))
print("ALL TOPIC 4 CHECKS PASSED")
