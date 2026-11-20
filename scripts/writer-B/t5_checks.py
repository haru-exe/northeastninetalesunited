"""Writer B, Topic 5 checks: strain transformation, rosette (Ex 2.7), rotation extremes (Ex 2.8),
principal strains (Ex 2.9 data, Ex 2.10), dilatation (Ex 2.11), spherical/deviatoric split (Ex 2.12).

Run:  python -I notes-build/scripts/writer-B/t5_checks.py
numpy/sympy live in the user site-packages, which -I hides, so that folder is added explicitly below.
"""
import sys
sys.path.append(r"C:\Users\amy23\AppData\Roaming\Python\Python312\site-packages")
import numpy as np
import sympy as sp

half = sp.Rational(1, 2)
th = sp.symbols("theta", real=True)
ex, ey, exy = sp.symbols("e_x e_y e_xy", real=True)

print("=== (2.3.4)-(2.3.6): 2D transformation derived from e' = Q e Q^T ===")
Q = sp.Matrix([[sp.cos(th), sp.sin(th)], [-sp.sin(th), sp.cos(th)]])
e2 = sp.Matrix([[ex, exy], [exy, ey]])
ep = sp.simplify(Q * e2 * Q.T)
c, s = sp.cos(th), sp.sin(th)
book_235 = sp.Matrix([[ex*c**2 + ey*s**2 + 2*exy*s*c, -ex*s*c + ey*s*c + exy*(c**2 - s**2)],
                      [-ex*s*c + ey*s*c + exy*(c**2 - s**2), ex*s**2 + ey*c**2 - 2*exy*s*c]])
assert sp.simplify(ep - book_235) == sp.zeros(2, 2), "(2.3.5) does not follow from (2.3.1),(2.3.4)"
book_236 = sp.Matrix([
    [(ex + ey)/2 + (ex - ey)/2*sp.cos(2*th) + exy*sp.sin(2*th), (ey - ex)/2*sp.sin(2*th) + exy*sp.cos(2*th)],
    [(ey - ex)/2*sp.sin(2*th) + exy*sp.cos(2*th), (ex + ey)/2 - (ex - ey)/2*sp.cos(2*th) - exy*sp.sin(2*th)]])
assert sp.simplify(ep - book_236) == sp.zeros(2, 2), "(2.3.6) does not follow"
print("(2.3.5) and (2.3.6) as transcribed from the page both equal Q e Q^T: OK")
print("double-angle identities used: cos^2 = (1+cos2t)/2, sin^2 = (1-cos2t)/2, 2 sin cos = sin2t, cos^2 - sin^2 = cos2t")
# invariance of e_x + e_y under rotation
assert sp.simplify(ep[0, 0] + ep[1, 1] - (ex + ey)) == 0
print("e'_x + e'_y = e_x + e_y (trace invariant): OK")

print()
print("=== Exercise 2.6 (polar components): e_r = n_r^T e n_r with n_r = (cos t, sin t), n_theta = (-sin t, cos t) ===")
nr = sp.Matrix([c, s]); nt = sp.Matrix([-s, c])
er = sp.simplify((nr.T * e2 * nr)[0]); et = sp.simplify((nt.T * e2 * nt)[0]); ert = sp.simplify((nr.T * e2 * nt)[0])
assert sp.simplify(er - book_236[0, 0]) == 0 and sp.simplify(et - book_236[1, 1]) == 0 and sp.simplify(ert - book_236[0, 1]) == 0
print("e_r, e_theta, e_r theta = (2.3.6) with x'->r, y'->theta: OK")

print()
print("=== Exercise 2.7 rosette: arms a, b, c at 30, 90, 150 degrees from +x ===")
ea, eb, ec = sp.Rational(1, 1000), sp.Rational(2, 1000), sp.Rational(4, 1000)
exx, eyy, exyy = sp.symbols("exx eyy exyy")
eqs = []
for ang, val in ((30, ea), (90, eb), (150, ec)):
    t = sp.rad(ang)
    eqs.append(sp.Eq((exx + eyy)/2 + (exx - eyy)/2*sp.cos(2*t) + exyy*sp.sin(2*t), val))
sol = sp.solve(eqs, [exx, eyy, exyy], dict=True)[0]
sol = {k_: sp.nsimplify(sp.simplify(v)) for k_, v in sol.items()}
print("exact:", sol)
print("e_x = ", sp.N(sol[exx], 6), " e_y = ", sp.N(sol[eyy], 6), " e_xy = ", sp.N(sol[exyy], 6))
# arm equations written out
print("arm b (90 deg): e_b = e_y")
print("arm a (30 deg): e_a = (e_x+e_y)/2 + (e_x-e_y)/4 + (sqrt3/2) e_xy")
print("arm c (150 deg): e_c = (e_x+e_y)/2 + (e_x-e_y)/4 - (sqrt3/2) e_xy")
print("e_a + e_c = 3e_x/2 + e_y/2 ->", sp.simplify(ea + ec), "; e_a - e_c = sqrt3 e_xy ->", sp.simplify(ea - ec))
# check by direct n^T e n
E = sp.Matrix([[sol[exx], sol[exyy]], [sol[exyy], sol[eyy]]])
for ang, val in ((30, ea), (90, eb), (150, ec)):
    n = sp.Matrix([sp.cos(sp.rad(ang)), sp.sin(sp.rad(ang))])
    got = sp.simplify((n.T * E * n)[0])
    print("  arm at", ang, "deg: n^T e n =", sp.N(got, 8), "(data", sp.N(val, 8), ")")
    assert abs(sp.N(got - val, 20)) < 1e-15
# opposite reading (a on the left) would flip the sign of e_xy only
print("if arms a and c were swapped, e_x and e_y unchanged and e_xy ->", sp.N(-sol[exyy], 6))

print()
print("=== Exercise 2.8: e_x = 0.002, e_y = -0.004, e_xy = 0.001 ===")
vx, vy, vxy = 0.002, -0.004, 0.001
mean, diff, R = (vx + vy)/2, (vx - vy)/2, np.hypot((vx - vy)/2, vxy)
print("mean (e_x+e_y)/2 =", mean, "; half-difference (e_x-e_y)/2 =", diff, "; R = sqrt(diff^2 + exy^2) =", R)
t_ex = 0.5*np.arctan2(vxy, diff)          # maximises e'_x
print("e'_x(theta) = %.4g + %.4g cos2t + %.4g sin2t" % (mean, diff, vxy))
print("   max at tan2t = exy/diff = 1/3 : 2t = %.4f deg, t = %.4f deg = %.5f rad; e'_x max = %.6g ; min = %.6g at t = %.4f deg"
      % (np.degrees(2*t_ex), np.degrees(t_ex), t_ex, mean + R, mean - R, np.degrees(t_ex) + 90))
# e'_xy = -diff sin2t + exy cos2t
t_exy = 0.5*np.arctan2(-diff, vxy) * -1.0   # placeholder, recomputed below by brute force
grid = np.radians(np.linspace(-90, 90, 3600001))
f_xy = -diff*np.sin(2*grid) + vxy*np.cos(2*grid)
i = np.argmax(f_xy); j = np.argmin(f_xy)
print("e'_xy(theta) = %.4g sin2t + %.4g cos2t" % (-diff, vxy))
print("   brute-force max e'_xy = %.6g at t = %.4f deg ; min = %.6g at t = %.4f deg"
      % (f_xy[i], np.degrees(grid[i]), f_xy[j], np.degrees(grid[j])))
# analytic: e'_xy = R cos(2t + phi), phi = atan2(diff, exy)
phi = np.arctan2(diff, vxy)
print("   analytic: phi = atan2(diff, exy) = %.4f deg ; max when 2t + phi = 0  ->  t = %.4f deg (and +180 = %.4f deg)"
      % (np.degrees(phi), -np.degrees(phi)/2, 180 - np.degrees(phi)/2))
print("   e'_xy max = R = %.6g = (e_1 - e_3)/2 ; angle between e'_x-max and e'_xy-max directions = 45 deg: %.4f"
      % (R, np.degrees(t_ex) - (-np.degrees(phi)/2)))
f_x = mean + diff*np.cos(2*grid) + vxy*np.sin(2*grid)
print("   brute-force e'_x max %.6g at t = %.4f deg" % (f_x.max(), np.degrees(grid[np.argmax(f_x)])))
# e'_y
f_y = mean - diff*np.cos(2*grid) - vxy*np.sin(2*grid)
print("   brute-force e'_y max %.6g at t = %.4f deg" % (f_y.max(), np.degrees(grid[np.argmax(f_y)])))
print("   principal strains of this 2D state = mean +/- R = %.6g, %.6g ; e'_xy = 0 at t = %.4f deg" % (mean + R, mean - R, np.degrees(t_ex)))
# common-mistake illustration: using the engineering shear strain in place of the tensor shear strain
t30 = np.radians(30)
good = mean + diff*np.cos(2*t30) + vxy*np.sin(2*t30)
bad = mean + diff*np.cos(2*t30) + 2*vxy*np.sin(2*t30)
print("   mistake illustration at theta = 30 deg: e'_x = %.6g (correct) vs %.6g (if gamma_xy = 0.002 is used as e_xy)" % (good, bad))

print()
print("=== Exercise 2.9 strain (x 1e-3): [[1,-2,0],[-2,-4,0],[0,0,5]] ===")
M9 = sp.Matrix([[1, -2, 0], [-2, -4, 0], [0, 0, 5]])
print("invariants (units 1e-3, 1e-6, 1e-9): theta1 =", M9.trace(),
      " theta2 =", sum(M9.minor_submatrix(i, i).det() for i in range(3)), " theta3 =", M9.det())
lam = sp.symbols("lam")
cp = sp.factor((M9 - lam*sp.eye(3)).det())
print("det(e - s I) =", cp, " -> roots:", sp.solve(cp, lam))
roots9 = sorted([sp.N(r, 10) for r in sp.solve(cp, lam)], reverse=True)
print("principal values (x 1e-3):", [float(r) for r in roots9])
w9, v9 = np.linalg.eigh(np.array(M9.tolist(), dtype=float))
order = np.argsort(w9)[::-1]
for idx in order:
    vec = v9[:, idx]
    vec = vec if vec[np.argmax(np.abs(vec))] > 0 else -vec
    print("   s = %.5f   n = (%.5f, %.5f, %.5f)" % (w9[idx], *vec))
print("   2D angle: tan 2t_p = 2 e_xy/(e_x - e_y) = -4/5 -> t_p = %.4f deg (direction of the larger in-plane root)" % (0.5*np.degrees(np.arctan2(-4, 5))))
print("   exact in-plane roots (-3 +/- sqrt41)/2 =", float((-3 + sp.sqrt(41))/2), float((-3 - sp.sqrt(41))/2))
print("   check sum = ", float(sum(roots9)), " product = ", float(roots9[0]*roots9[1]*roots9[2]))
# eigenvector exact for lam = (-3+sqrt41)/2 : (e_x - lam) n1 + e_xy n2 = 0 -> n prop. to (2, 1-lam)
lam_p = (-3 + sp.sqrt(41))/2
vv = sp.Matrix([2, 1 - lam_p]); vv = vv / vv.norm()
print("   exact direction for (-3+sqrt41)/2: (2, (5 - sqrt41)/2)/norm =", [float(a) for a in vv])
lam_m = (-3 - sp.sqrt(41))/2
vm = sp.Matrix([2, 1 - lam_m]); vm = vm / vm.norm()
print("   exact direction for (-3-sqrt41)/2: (2, (5 + sqrt41)/2)/norm =", [float(a) for a in vm], " dot product =", float(vv.dot(vm)))

print()
print("=== Exercise 2.10 strain (x 1e-3): [[2,-2,0],[-2,-4,1],[0,1,6]] ===")
M10 = sp.Matrix([[2, -2, 0], [-2, -4, 1], [0, 1, 6]])
I1 = M10.trace(); I2 = sum(M10.minor_submatrix(i, i).det() for i in range(3)); I3 = M10.det()
print("theta1, theta2, theta3 =", I1, I2, I3)
cp10 = sp.expand((M10 - lam*sp.eye(3)).det())
print("det(e - s I) =", cp10, " i.e. s^3 - 4 s^2 - 25 s + 74 = 0  (", sp.expand(-cp10), ")")
r10 = sorted([complex(r).real for r in sp.Poly(sp.expand(-cp10), lam).nroots(n=15)], reverse=True)
print("principal values (x 1e-3):", ["%.5f" % r for r in r10])
print("   sum = %.6f (= theta1), sum of pair products = %.6f (= theta2), product = %.6f (= theta3)"
      % (sum(r10), r10[0]*r10[1] + r10[1]*r10[2] + r10[2]*r10[0], r10[0]*r10[1]*r10[2]))
w10, v10 = np.linalg.eigh(np.array(M10.tolist(), dtype=float))
order = np.argsort(w10)[::-1]
for idx in order:
    vec = v10[:, idx]
    vec = vec if vec[np.argmax(np.abs(vec))] > 0 else -vec
    print("   s = %.5f   n = (%.5f, %.5f, %.5f)" % (w10[idx], *vec))
V = v10[:, order]
print("   directions orthonormal:", np.allclose(V.T @ V, np.eye(3)), " ; V^T e V diagonal:", np.allclose(V.T @ np.array(M10.tolist(), float) @ V, np.diag(w10[order])))
# a hand-method for the directions: cofactor (adjugate) of (e - s I): any non-zero row/column of the adjugate is the eigenvector
for sroot in r10:
    adj = (M10 - sroot*sp.eye(3)).adjugate()
    row = [float(adj[0, j]) for j in range(3)]
    nrm = np.linalg.norm(row)
    print("   hand method (first row of adjugate) for s = %.5f: n prop. to (%.5f, %.5f, %.5f)" % (sroot, *[a/nrm for a in row]))

print()
print("=== Exercise 2.11: volume of a box with edges along the principal directions ===")
e1, e2_, e3 = sp.symbols("e1 e2 e3")
ratio = sp.expand((1 + e1)*(1 + e2_)*(1 + e3) - 1)
print("(1+e1)(1+e2)(1+e3) - 1 =", ratio, "  = theta1 + theta2 + theta3")
r10n = r10
exact_dilat = (1 + r10n[0]*1e-3)*(1 + r10n[1]*1e-3)*(1 + r10n[2]*1e-3) - 1
print("Ex 2.10 numbers: exact DV/V0 = %.9f ; theta1 = %.9f ; relative difference %.3g" % (exact_dilat, 4e-3, (exact_dilat - 4e-3)/4e-3))

print()
print("=== Exercise 2.12: spherical and deviatoric parts of the Exercise 2.10 strain ===")
th10 = I1
sph = sp.Rational(1, 3)*th10*sp.eye(3)
dev = M10 - sph
print("theta = e_kk =", th10, "(x 1e-3);  spherical e~_ij = (theta/3) delta_ij = ", sp.Rational(1, 3)*th10, "x delta_ij (x 1e-3)")
print("deviatoric e^_ij (x 1e-3) =", dev.tolist(), "; trace =", dev.trace())
assert dev.trace() == 0
dev_roots = sorted([complex(r).real for r in sp.Poly(sp.expand(-(dev - lam*sp.eye(3)).det()), lam).nroots(n=15)], reverse=True)
print("deviatoric principal values:", ["%.5f" % r for r in dev_roots], "= e_i - theta/3:", ["%.5f" % (r - float(th10)/3) for r in r10])
wd, vd = np.linalg.eigh(np.array(dev.tolist(), float))
ordd = np.argsort(wd)[::-1]
same = all(abs(abs(np.dot(v10[:, order[q]], vd[:, ordd[q]])) - 1) < 1e-9 for q in range(3))
print("deviatoric eigenvectors equal those of e (up to sign):", same)
print("deviatoric invariants: theta1_hat =", dev.trace(), " theta2_hat =", sum(dev.minor_submatrix(i, i).det() for i in range(3)), " theta3_hat =", dev.det())

print()
print("=== Your turn 5C: split of the Exercise 2.9 strain (x 1e-3) ===")
th9 = M9.trace()
dev9 = M9 - sp.Rational(1, 3)*th9*sp.eye(3)
print("theta =", th9, " spherical = ", sp.Rational(1, 3)*th9, "x delta_ij ; deviatoric =", dev9.tolist(), "; trace =", dev9.trace())
print("deviatoric principal values exact: 13/3, (-13+3 sqrt41)/6, (-13-3 sqrt41)/6 =",
      float(sp.Rational(13, 3)), float((-13 + 3*sp.sqrt(41))/6), float((-13 - 3*sp.sqrt(41))/6))
print("   = e_i - theta/3 :", [float(r) - float(th9)/3 for r in roots9])
print("   sum =", float(sp.Rational(13, 3) + (-13 + 3*sp.sqrt(41))/6 + (-13 - 3*sp.sqrt(41))/6))
print("ALL TOPIC 5 CHECKS PASSED")
