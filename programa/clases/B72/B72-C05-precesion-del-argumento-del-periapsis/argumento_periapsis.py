#!/usr/bin/env python3
"""B72-C05 — Precesion del argumento del periapsis.

d(omega)/dt = 3/4 n J2 (Re/p)^2 (5 cos^2 i - 1), contrastada con el promedio numerico de las
ecuaciones de Gauss; inclinacion critica y orbita tipo Molniya. Orbitas SINTETICAS.
Unidades SI; angulos en grados en la salida. Marco: ecuador de la fecha.
Solo biblioteca estandar.
"""
import sys

import math
MU = 3.986004e14
RE = 6378137.0
J2 = 1082.63e-6
DIA = 86400.0
RAD = 180.0 / math.pi


def pert_j2(r):
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    k = -1.5 * J2 * MU * RE ** 2 / d ** 5
    zz = 5 * z * z / (d * d)
    return [k * x * (1 - zz), k * y * (1 - zz), k * z * (3 - zz)]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def promedio_gauss(a, e, inc, w, N=4000):
    """Promedia sobre la anomalia media las ecuaciones de Gauss con la perturbacion J2
    (elementos fijos a, e, i, omega, Omega = 0). Devuelve (dOmega/dt, domega/dt) en rad/s."""
    p = a * (1 - e * e)
    h = math.sqrt(MU * p)
    sO, cO = 0.0, 1.0
    ci, si, cw, sw = math.cos(inc), math.sin(inc), math.cos(w), math.sin(w)
    R = [[cO * cw - sO * sw * ci, -cO * sw - sO * cw * ci, sO * si],
         [sO * cw + cO * sw * ci, -sO * sw + cO * cw * ci, -cO * si],
         [sw * si, cw * si, ci]]
    f = lambda x: [sum(R[i][j] * x[j] for j in range(3)) for i in range(3)]
    sumO = sumw = 0.0
    for k in range(N):
        M = 2 * math.pi * (k + 0.5) / N
        E = M
        for _ in range(60):
            E -= (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        nu = 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))
        r = p / (1 + e * math.cos(nu))
        rv = f([r * math.cos(nu), r * math.sin(nu), 0.0])
        ap = pert_j2(rv)
        rh = [c / r for c in rv]
        wh = f([0.0, 0.0, 1.0])
        sh = cross(wh, rh)
        Rc, Sc, Wc = dot(ap, rh), dot(ap, sh), dot(ap, wh)
        u = w + nu
        sumO += r * math.sin(u) / (h * si) * Wc
        sumw += (-p * math.cos(nu) * Rc + (p + r) * math.sin(nu) * Sc) / (e * h) - r * math.sin(u) * ci / (h * si) * Wc
    return sumO / N, sumw / N


def tasa_omega(a, e, inc):
    n = math.sqrt(MU / a ** 3)
    p = a * (1 - e * e)
    return 0.75 * n * J2 * (RE / p) ** 2 * (5 * math.cos(inc) ** 2 - 1)


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Orbitas SINTETICAS; J2 = 1082.63e-6 (NSSDC), mu = 3.986004e14 (IAU 2015), Re = 6378137 m")
ic = math.degrees(math.acos(1 / math.sqrt(5)))
print(f"\nInclinacion critica: acos(1/raiz(5)) = {ic:.4f} deg (y {180 - ic:.4f} deg retrograda)")
assert abs(tasa_omega(7.0e6, 0.1, math.acos(1 / math.sqrt(5)))) < 1e-18

print("\nVerificacion: formula cerrada frente al promedio numerico de Gauss (omega = 40 deg)")
print(f"{'a [km]':>9}{'e':>7}{'i [deg]':>9}{'formula [deg/dia]':>19}{'Gauss [deg/dia]':>17}{'dif. relativa':>15}")
for a_km, e, i in ((6778.137, 0.05, 51.6), (7078.137, 0.05, 98.2), (26600.0, 0.74, 63.4), (26600.0, 0.74, 80.0)):
    a = a_km * 1e3
    f = tasa_omega(a, e, math.radians(i)) * DIA * RAD
    g = promedio_gauss(a, e, math.radians(i), math.radians(40.0), N=20000)[1] * DIA * RAD
    rel = abs(f - g) / max(abs(f), 1e-3)
    print(f"{a_km:>9.3f}{e:>7.2f}{i:>9.1f}{f:>19.5f}{g:>17.5f}{rel:>15.2e}")
    assert rel < 1e-5

print("\nTasa de omega [deg/dia], e = 0.01 (tabla de diseno)")
incs = (0, 30, 51.6, 63.4349, 80, 90, 98.2)
print(f"{'h [km]':>8}" + "".join(f"{i:>10.2f}" for i in incs))
for h in (400, 800, 1500):
    a = RE + h * 1e3
    print(f"{h:>8}" + "".join(f"{tasa_omega(a, 0.01, math.radians(i)) * DIA * RAD:>10.3f}" for i in incs))

# Molniya sintetica: a = 26600 km, e = 0.74
for i in (63.4349, 70.0):
    a = 26600e3
    d = tasa_omega(a, 0.74, math.radians(i)) * DIA * RAD
    print(f"Tipo Molniya a = 26600 km, e = 0.74, i = {i:.4f} deg: d(omega)/dt = {d:.4f} deg/dia = {d * 365.25:.1f} deg/ano")
print("Pruebas superadas.")
