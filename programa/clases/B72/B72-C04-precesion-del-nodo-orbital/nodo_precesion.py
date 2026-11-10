#!/usr/bin/env python3
"""B72-C04 — Precesion del nodo orbital.

Tasa de regresion del nodo por J2, d(Omega)/dt = -3/2 n J2 (Re/p)^2 cos i, contrastada con el
promedio numerico de las ecuaciones de Gauss con la aceleracion J2 completa.
Orbitas SINTETICAS. Unidades SI; angulos en grados en la salida. Marco: ecuador de la fecha.
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


def tasa_nodo(a, e, inc, mu=MU, re=RE, j2=J2):
    n = math.sqrt(mu / a ** 3)
    p = a * (1 - e * e)
    return -1.5 * n * j2 * (re / p) ** 2 * math.cos(inc)


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Orbitas SINTETICAS; J2 = 1082.63e-6 (NSSDC), mu = 3.986004e14 (IAU 2015), Re = 6378137 m")

print("\nVerificacion: formula cerrada frente al promedio numerico de Gauss (e = 0.05, omega = 40 deg)")
print(f"{'a [km]':>9}{'i [deg]':>9}{'formula [deg/dia]':>19}{'Gauss [deg/dia]':>17}{'dif. relativa':>15}")
for a_km, i in ((6778.137, 51.6), (7078.137, 98.2), (8378.137, 28.5), (26560.0, 55.0)):
    a = a_km * 1e3
    f = tasa_nodo(a, 0.05, math.radians(i)) * DIA * RAD
    g = promedio_gauss(a, 0.05, math.radians(i), math.radians(40.0))[0] * DIA * RAD
    rel = abs(f - g) / abs(f)
    print(f"{a_km:>9.3f}{i:>9.1f}{f:>19.5f}{g:>17.5f}{rel:>15.2e}")
    assert rel < 1e-6

print("\nTasa del nodo [deg/dia], e = 0 (tabla de diseno)")
incs = (0, 28.5, 51.6, 63.4, 90, 98.2, 120)
print(f"{'h [km]':>8}" + "".join(f"{i:>10.1f}" for i in incs))
for h in (400, 800, 1500, 20200):
    a = RE + h * 1e3
    print(f"{h:>8}" + "".join(f"{tasa_nodo(a, 0.0, math.radians(i)) * DIA * RAD:>10.3f}" for i in incs))

a = RE + 400e3
dO = tasa_nodo(a, 0.0, math.radians(51.6))
print(f"\nPeriodo de regresion del nodo a 400 km y 51.6 deg: {360.0 / abs(dO * DIA * RAD):.1f} dias")
# Marte con J2 y radio de la ficha NSSDC; GM de la ficha
mu_m, re_m, j2_m = 0.042828e15, 3396.2e3, 1960.45e-6
am = re_m + 400e3
dm = tasa_nodo(am, 0.0, math.radians(51.6), mu_m, re_m, j2_m) * DIA * RAD
print(f"Marte, 400 km, 51.6 deg (GM, Re y J2 de la ficha NSSDC): {dm:.3f} deg/dia")
print("Pruebas superadas.")
