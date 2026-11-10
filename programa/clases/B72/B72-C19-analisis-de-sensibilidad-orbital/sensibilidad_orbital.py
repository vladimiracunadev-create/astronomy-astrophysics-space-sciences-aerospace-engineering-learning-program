#!/usr/bin/env python3
"""B72-C19 — Analisis de sensibilidad orbital.

Sensibilidad por diferencias finitas de una orbita baja con J2 y arrastre (atmosfera exponencial
ILUSTRATIVA): (1) crecimiento del error a lo largo de la trayectoria frente a un error de semieje,
-3/2 n da t; (2) linealidad de la respuesta a una perturbacion de velocidad; (3) sensibilidad al
coeficiente balistico (error que crece con t^2). Orbita y atmosfera SINTETICAS.
Unidades SI; marco inercial del ecuador de la fecha. Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14
RE = 6378137.0
J2 = 1082.63e-6
OM_T = 2 * math.pi / (23.9345 * 3600.0)
RHO_REF, H_REF, ESC = 3.0e-12, 400e3, 60e3     # ILUSTRATIVOS
DIA = 86400.0


def acel(r, v, B):
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    k = -1.5 * J2 * MU * RE ** 2 / d ** 5
    zz = 5 * z * z / (d * d)
    a = [-MU * x / d ** 3 + k * x * (1 - zz), -MU * y / d ** 3 + k * y * (1 - zz), -MU * z / d ** 3 + k * z * (3 - zz)]
    if B:
        vr = [v[0] + OM_T * y, v[1] - OM_T * x, v[2]]
        vm = math.sqrt(vr[0] ** 2 + vr[1] ** 2 + vr[2] ** 2)
        kd = -0.5 * RHO_REF * math.exp(-(d - RE - H_REF) / ESC) * vm / B
        for i in range(3):
            a[i] += kd * vr[i]
    return a


def paso(r, v, dt, B):
    a1 = acel(r, v, B)
    r2 = [r[i] + .5 * dt * v[i] for i in range(3)]; v2 = [v[i] + .5 * dt * a1[i] for i in range(3)]
    a2 = acel(r2, v2, B)
    r3 = [r[i] + .5 * dt * v2[i] for i in range(3)]; v3 = [v[i] + .5 * dt * a2[i] for i in range(3)]
    a3 = acel(r3, v3, B)
    r4 = [r[i] + dt * v3[i] for i in range(3)]; v4 = [v[i] + dt * a3[i] for i in range(3)]
    a4 = acel(r4, v4, B)
    return ([r[i] + dt / 6 * (v[i] + 2 * v2[i] + 2 * v3[i] + v4[i]) for i in range(3)],
            [v[i] + dt / 6 * (a1[i] + 2 * a2[i] + 2 * a3[i] + a4[i]) for i in range(3)])


def propaga(r, v, tiempos, B, dt=20.0):
    out, t = {}, 0.0
    for T in tiempos:
        for _ in range(int(round((T - t) / dt))):
            r, v = paso(r, v, dt, B)
        t = T
        out[T] = (list(r), list(v))
    return out


def unitario(v):
    m = math.sqrt(sum(c * c for c in v))
    return [c / m for c in v]


def inicial(a, e, inc, da=0.0, dv=(0.0, 0.0, 0.0)):
    """Estado en el perigeo del plano (x, y, z) con semieje a+da (vis-viva) mas dv sumado en la velocidad."""
    rp = a * (1 - e)
    ap = a + da
    vp = math.sqrt(MU * (2.0 / rp - 1.0 / ap))
    r = [rp, 0.0, 0.0]
    v = [0.0, vp * math.cos(inc), vp * math.sin(inc)]
    return r, [v[i] + dv[i] for i in range(3)]


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
a0, e0, i0 = 6878.137e3, 0.001, math.radians(51.6)
n = math.sqrt(MU / a0 ** 3)
print(f"Orbita SINTETICA a = {a0 / 1e3:.3f} km, e = {e0}, i = 51.6 deg ; n = {n:.4e} rad/s ; J2 y arrastre ILUSTRATIVO (B = 45 kg/m2) ; RK4 paso 20 s")
B0 = 45.0
tiempos = [1 * DIA, 3 * DIA, 5 * DIA]

# 1) Error de semieje -> error a lo largo de la trayectoria (sin arrastre para aislar el efecto)
r0, v0 = inicial(a0, e0, i0)
nom = propaga(r0, v0, tiempos, None)
rp, vp = inicial(a0, e0, i0, da=1.0)
per = propaga(rp, vp, tiempos, None)
print("\n(1) da = +1 m, sin arrastre: error a lo largo de la trayectoria frente a -3/2 n da t")
print(f"{'t [dias]':>9}{'along-track [m]':>18}{'-1.5 n da t [m]':>18}{'dif. relativa':>15}{'|error radial| [m]':>20}")
for T in tiempos:
    dr = [per[T][0][i] - nom[T][0][i] for i in range(3)]
    u = unitario(nom[T][1])
    s = sum(dr[i] * u[i] for i in range(3))
    teo = -1.5 * n * 1.0 * T
    rad = unitario(nom[T][0])
    radial = sum(dr[i] * rad[i] for i in range(3))
    print(f"{T / DIA:>9.0f}{s:>18.1f}{teo:>18.1f}{abs(s - teo) / abs(teo):>15.2%}{abs(radial):>20.2f}")
    assert abs(s - teo) / abs(teo) < 0.05

# 2) Linealidad frente a una perturbacion de velocidad (sin arrastre, 1 dia)
print("\n(2) Perturbacion de velocidad a lo largo de la trayectoria, 1 dia: linealidad")
res = []
for dv in (1e-3, 2e-3, 4e-3):
    vh = unitario(v0)
    ri, vi = inicial(a0, e0, i0, dv=tuple(dv * c for c in vh))
    p = propaga(ri, vi, [DIA], None)[DIA]
    dr = [p[0][i] - nom[DIA][0][i] for i in range(3)]
    res.append(math.sqrt(sum(c * c for c in dr)))
print(f"{'dv [m/s]':>10}{'|dr| a 1 dia [m]':>20}{'|dr|/dv [s]':>16}")
for dv, r_ in zip((1e-3, 2e-3, 4e-3), res):
    print(f"{dv:>10.0e}{r_:>20.3f}{r_ / dv:>16.1f}")
lin = abs(res[1] / (2 * res[0]) - 1)
print(f"Desviacion de la linealidad (|dr(2dv)|/(2|dr(dv)|) - 1) = {lin:.2e}")
assert lin < 1e-3

# 3) Sensibilidad al coeficiente balistico
print("\n(3) Con arrastre: +10 % en B, error a lo largo de la trayectoria")
nom_d = propaga(r0, v0, tiempos, B0)
per_d = propaga(r0, v0, tiempos, B0 * 1.1)
print(f"{'t [dias]':>9}{'along-track [m]':>18}{'cociente con t=1 d':>20}{'t^2 relativo':>14}")
base = None
for T in tiempos:
    dr = [per_d[T][0][i] - nom_d[T][0][i] for i in range(3)]
    u = unitario(nom_d[T][1])
    s = sum(dr[i] * u[i] for i in range(3))
    if base is None:
        base = s
    print(f"{T / DIA:>9.0f}{s:>18.2f}{s / base:>20.2f}{(T / DIA) ** 2:>14.0f}")
print("Con arrastre el error crece mas deprisa que t (tendiendo a t^2 si la densidad cambia poco); el valor depende de la atmosfera ilustrativa.")
print("Pruebas superadas.")
