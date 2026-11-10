#!/usr/bin/env python3
"""B72-C14 — Orbitas congeladas.

Excentricidad congelada de primer orden e_f = -(J3/(2 J2)) (Re/p) sin i (omega = 90 deg) contrastada con
la raiz numerica de d(omega)/dt = 0 obtenida promediando las ecuaciones de Gauss con las aceleraciones
zonales J2 y J3 completas. Orbitas SINTETICAS. Unidades SI; angulos en grados en la salida.
Marco: ecuador de la fecha. Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14
RE = 6378137.0
J = {2: 1082.63e-6,      # NSSDC
     3: -2.53881e-6}     # WGS-72, Spacetrack Report 3 (Hoots y Roehrich)
DIA = 86400.0
RAD = 180.0 / math.pi


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def pert_zonal(r, terminos=(2, 3)):
    """Aceleracion perturbadora de los armonicos zonales (sin la central): -grad(T_n)."""
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    s = z / d
    a = [0.0, 0.0, 0.0]
    for n in terminos:
        p = [1.0, s]; dp = [0.0, 1.0]
        for k in range(2, n + 1):
            p.append(((2 * k - 1) * s * p[k - 1] - (k - 1) * p[k - 2]) / k)
            dp.append(dp[k - 2] + (2 * k - 1) * p[k - 1])
        c = MU * J[n] * RE ** n
        for i, comp in enumerate((x, y, z)):
            gr = -(n + 1) * p[n] * comp / d ** (n + 3)
            gz = dp[n] / d ** (n + 2) * ((1.0 if i == 2 else 0.0) - s * comp / d)
            a[i] += -c * (gr + gz)
    return a


def promedios(a, e, inc, w, terminos=(2, 3), N=1500):
    """Promedio sobre la anomalia media de de/dt y domega/dt (rad/s) con las ecuaciones de Gauss."""
    p = a * (1 - e * e); h = math.sqrt(MU * p)
    ci, si, cw, sw = math.cos(inc), math.sin(inc), math.cos(w), math.sin(w)
    R = [[cw, -sw, 0.0], [sw * ci, cw * ci, -si], [sw * si, cw * si, ci]]   # Omega = 0
    # matriz R = Rz(0) Rx(i) Rz(w)
    R = [[cw, -sw, 0.0], [ci * sw, ci * cw, -si], [si * sw, si * cw, ci]]
    f = lambda x: [sum(R[i][j] * x[j] for j in range(3)) for i in range(3)]
    se = sw_ = 0.0
    for k in range(N):
        M = 2 * math.pi * (k + 0.5) / N
        E = M
        for _ in range(60):
            E -= (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        nu = 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))
        r = p / (1 + e * math.cos(nu))
        rv = f([r * math.cos(nu), r * math.sin(nu), 0.0])
        ap = pert_zonal(rv, terminos)
        rh = [c / r for c in rv]; wh = f([0.0, 0.0, 1.0]); sh = cross(wh, rh)
        Rc, Sc, Wc = dot(ap, rh), dot(ap, sh), dot(ap, wh)
        u = w + nu
        se += (p * math.sin(nu) * Rc + ((p + r) * math.cos(nu) + r * e) * Sc) / h
        sw_ += (-p * math.cos(nu) * Rc + (p + r) * math.sin(nu) * Sc) / (e * h) - r * math.sin(u) * ci / (h * si) * Wc
    return se / N, sw_ / N


def congelada_numerica(a, inc, w=math.pi / 2, terminos=(2, 3)):
    lo, hi = 2e-4, 2e-2
    flo = promedios(a, lo, inc, w, terminos, N=600)[1]
    for _ in range(22):
        mid = 0.5 * (lo + hi)
        fm = promedios(a, mid, inc, w, terminos, N=600)[1]
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Orbitas SINTETICAS; J2 = 1082.63e-6 (NSSDC); J3 = -2.53881e-6 (WGS-72, Spacetrack Report 3); omega = 90 deg")
print(f"J3/(2 J2) = {J[3] / (2 * J[2]):.6e}")

print("\nExcentricidad congelada: formula de primer orden frente a la raiz numerica de d(omega)/dt = 0")
print(f"{'h [km]':>8}{'i [deg]':>9}{'e formula':>13}{'e numerica':>13}{'dif. relativa':>15}")
for h, i in ((700, 98.188), (800, 98.603), (500, 97.4), (1300, 66.0)):
    a = RE + h * 1e3; inc = math.radians(i)
    ef = -(J[3] / (2 * J[2])) * (RE / a) * math.sin(inc)
    en = congelada_numerica(a, inc)
    print(f"{h:>8}{i:>9.3f}{ef:>13.6f}{en:>13.6f}{abs(ef - en) / en:>15.2%}")
    assert abs(ef - en) / en < 0.05

print("\nTasas promediadas en h = 700 km, i = 98.188 deg, omega = 90 deg [deg/dia]: signo de domega/dt con e")
a = RE + 700e3; inc = math.radians(98.188)
print(f"{'e':>10}{'domega/dt solo J2':>20}{'domega/dt J2+J3':>18}{'de/dt J2+J3':>16}")
for e in (0.0005, 0.001, 0.0015, 0.003):
    _, w2 = promedios(a, e, inc, math.pi / 2, (2,))
    de, w23 = promedios(a, e, inc, math.pi / 2, (2, 3))
    print(f"{e:>10.4f}{w2 * DIA * RAD:>20.4f}{w23 * DIA * RAD:>18.4f}{de * DIA:>16.2e}")
print("En omega = 90 deg, de/dt = 0 y domega/dt cambia de signo con e: ahi esta la orbita congelada.")
print("Pruebas superadas.")
