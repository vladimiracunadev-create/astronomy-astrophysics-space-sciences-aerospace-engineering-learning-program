#!/usr/bin/env python3
"""B72-C12 — Variaciones de elementos osculadores.

Conversion estado <-> elementos (ida y vuelta), oscilaciones de corto periodo de los elementos
osculadores bajo J2 y comparacion con la amplitud de primer orden de Kozai. Orbita SINTETICA.
Unidades SI; angulos en grados en la salida. Marco: ecuador de la fecha, inercial.
Solo biblioteca estandar.
"""
import math
import random
import sys

MU = 3.986004e14
RE = 6378137.0
J2 = 1082.63e-6


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def rv2coe(r, v):
    d = math.sqrt(dot(r, r)); vv = dot(v, v)
    h = cross(r, v); hm = math.sqrt(dot(h, h))
    n = [-h[1], h[0], 0.0]; nm = math.hypot(n[0], n[1])
    ev = [((vv - MU / d) * r[i] - dot(r, v) * v[i]) / MU for i in range(3)]
    e = math.sqrt(dot(ev, ev))
    a = 1.0 / (2.0 / d - vv / MU)
    inc = math.acos(h[2] / hm)
    Om = math.atan2(n[1], n[0])
    ph = [c / hm for c in h]; nh = [n[0] / nm, n[1] / nm, 0.0]; qh = cross(ph, nh)
    w = math.atan2(dot(ev, qh), dot(ev, nh))
    ex = [c / e for c in ev]; ey = cross(ph, ex)
    nu = math.atan2(dot(r, ey), dot(r, ex))
    return a, e, inc, Om, w, nu


def coe2rv(a, e, inc, Om, w, nu):
    p = a * (1 - e * e); r = p / (1 + e * math.cos(nu))
    rp = [r * math.cos(nu), r * math.sin(nu), 0.0]
    vp = [-math.sqrt(MU / p) * math.sin(nu), math.sqrt(MU / p) * (e + math.cos(nu)), 0.0]
    cO, sO, ci, si, cw, sw = math.cos(Om), math.sin(Om), math.cos(inc), math.sin(inc), math.cos(w), math.sin(w)
    R = [[cO * cw - sO * sw * ci, -cO * sw - sO * cw * ci, sO * si],
         [sO * cw + cO * sw * ci, -sO * sw + cO * cw * ci, -cO * si],
         [sw * si, cw * si, ci]]
    f = lambda x: [sum(R[i][j] * x[j] for j in range(3)) for i in range(3)]
    return f(rp), f(vp)


def acel(r):
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    k = -1.5 * J2 * MU * RE ** 2 / d ** 5
    zz = 5 * z * z / (d * d)
    return [-MU * x / d ** 3 + k * x * (1 - zz), -MU * y / d ** 3 + k * y * (1 - zz), -MU * z / d ** 3 + k * z * (3 - zz)]


def rk4(r, v, dt):
    a1 = acel(r); r2 = [r[i] + .5 * dt * v[i] for i in range(3)]; v2 = [v[i] + .5 * dt * a1[i] for i in range(3)]
    a2 = acel(r2); r3 = [r[i] + .5 * dt * v2[i] for i in range(3)]; v3 = [v[i] + .5 * dt * a2[i] for i in range(3)]
    a3 = acel(r3); r4 = [r[i] + dt * v3[i] for i in range(3)]; v4 = [v[i] + dt * a3[i] for i in range(3)]
    a4 = acel(r4)
    return ([r[i] + dt / 6 * (v[i] + 2 * v2[i] + 2 * v3[i] + v4[i]) for i in range(3)],
            [v[i] + dt / 6 * (a1[i] + 2 * a2[i] + 2 * a3[i] + a4[i]) for i in range(3)])


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Orbitas SINTETICAS; J2 = 1082.63e-6 (NSSDC), mu = 3.986004e14 (IAU 2015)")

# 1) Ida y vuelta estado -> elementos -> estado
random.seed(72)
peor = 0.0
for _ in range(1000):
    a = random.uniform(6.8e6, 4.5e7); e = random.uniform(0.0005, 0.9)
    if a * (1 - e) < 6.6e6:
        continue
    inc = math.radians(random.uniform(1, 179)); Om = random.uniform(0, 2 * math.pi)
    w = random.uniform(0, 2 * math.pi); nu = random.uniform(-math.pi, math.pi)
    r, v = coe2rv(a, e, inc, Om, w, nu)
    el = rv2coe(r, v)
    r2, v2 = coe2rv(*el)
    peor = max(peor, math.dist(r, r2) / math.hypot(*r), math.dist(v, v2) / math.hypot(*v))
print(f"\nIda y vuelta estado->elementos->estado (1000 casos, semilla 72): error relativo maximo = {peor:.2e}")
assert peor < 1e-9

# 2) Oscilaciones de corto periodo bajo J2
a0, e0, i0 = 7000e3, 0.01, math.radians(40.0)
r, v = coe2rv(a0, e0, i0, math.radians(30.0), math.radians(60.0), 0.0)
T = 2 * math.pi * math.sqrt(a0 ** 3 / MU)
dt = 10.0
norb = 10
nsteps = int(norb * T / dt)
paso_m = 6
A, E, I = [], [], []
for k in range(nsteps):
    if k % paso_m == 0:
        el = rv2coe(r, v)
        A.append(el[0]); E.append(el[1]); I.append(el[2])
    r, v = rk4(r, v, dt)
mA = sum(A) / len(A); mE = sum(E) / len(E); mI = sum(I) / len(I)
print(f"\nOrbita: a0 = {a0 / 1e3:.1f} km, e0 = {e0}, i0 = 40 deg ; periodo = {T:.1f} s ; {norb} vueltas ; RK4 paso {dt:.0f} s")
print(f"{'elemento':<10}{'inicial':>14}{'medio':>14}{'minimo':>14}{'maximo':>14}{'semirrango':>14}")
print(f"{'a [km]':<10}{A[0] / 1e3:>14.3f}{mA / 1e3:>14.3f}{min(A) / 1e3:>14.3f}{max(A) / 1e3:>14.3f}{(max(A) - min(A)) / 2e3:>14.3f}")
print(f"{'e':<10}{E[0]:>14.6f}{mE:>14.6f}{min(E):>14.6f}{max(E):>14.6f}{(max(E) - min(E)) / 2:>14.6f}")
print(f"{'i [deg]':<10}{math.degrees(I[0]):>14.5f}{math.degrees(mI):>14.5f}{math.degrees(min(I)):>14.5f}{math.degrees(max(I)):>14.5f}{math.degrees((max(I) - min(I)) / 2):>14.5f}")
amp_a = 1.5 * J2 * RE ** 2 * math.sin(i0) ** 2 / a0
print(f"\nAmplitud de primer orden del termino en cos(2u) de a (Kozai): 3/2 J2 Re^2 sin^2(i)/a = {amp_a / 1e3:.3f} km")
print(f"  semirrango observado de a = {(max(A) - min(A)) / 2e3:.3f} km")
print(f"Diferencia a_inicial - a_medio = {(A[0] - mA) / 1e3:.3f} km -> el periodo calculado con a_osculador inicial difiere del medio en {2 * math.pi * (math.sqrt(A[0] ** 3 / MU) - math.sqrt(mA ** 3 / MU)):.2f} s")
assert abs((max(A) - min(A)) / 2 - amp_a) / amp_a < 0.1
print("Pruebas superadas.")
