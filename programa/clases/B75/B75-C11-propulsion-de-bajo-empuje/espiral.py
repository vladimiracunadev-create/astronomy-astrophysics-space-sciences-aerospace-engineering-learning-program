#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C11: espiral heliocentrica de bajo empuje Tierra -> radio de Marte (empuje tangencial constante, planos coplanares y circulares).

Datos consultados (2026-11-10): semiejes de las fichas NASA/NSSDC (Tierra 149.598e6 km, Marte 227.956e6 km). GM_sol = 1.32712440e11 km3/s2 y g0 = 9.80665 m/s2 (estandar, no consultados).
SINTETICOS / ILUSTRATIVOS: aceleraciones de 1e-5 a 4e-4 m/s2 (constantes), Isp = 3000 s, masa inicial 1000 kg; sin sombras ni sistema de potencia.
Modelo: dos cuerpos con aceleracion tangencial (en la direccion de la velocidad) de modulo constante, RK4 con paso de 3600 s; se detiene al cruzar el radio de Marte.
Delta-v de Edelbaum para espiral circular-circular coplanar de baja aceleracion: V_Tierra - V_Marte (aproximacion exacta cuando a -> 0).
Pruebas: (1) con la aceleracion mas baja, |a t - (V_T - V_M)| / (V_T - V_M) < 1 % y excentricidad final < 0.02; (2) la diferencia con Edelbaum crece de forma monotona con la aceleracion
(Edelbaum es exacto en el limite a -> 0).
"""
import math, platform
MU = 1.32712440e11
RE_, RM_ = 149.598e6, 227.956e6
G0 = 9.80665e-3


def acc(r, v, a):
    rn = math.hypot(*r); vn = math.hypot(*v)
    return [-MU * r[0] / rn**3 + a * v[0] / vn, -MU * r[1] / rn**3 + a * v[1] / vn]


def espiral(a_ms2):
    a = a_ms2 * 1e-3
    r = [RE_, 0.0]; v = [0.0, math.sqrt(MU / RE_)]
    dt = 3600.0; t = 0.0; ang = 0.0
    while math.hypot(*r) < RM_:
        k1v = acc(r, v, a); k1r = v
        r2 = [x + 0.5 * dt * y for x, y in zip(r, k1r)]; v2 = [x + 0.5 * dt * y for x, y in zip(v, k1v)]
        k2v = acc(r2, v2, a); k2r = v2
        r3 = [x + 0.5 * dt * y for x, y in zip(r, k2r)]; v3 = [x + 0.5 * dt * y for x, y in zip(v, k2v)]
        k3v = acc(r3, v3, a); k3r = v3
        r4 = [x + dt * y for x, y in zip(r, k3r)]; v4 = [x + dt * y for x, y in zip(v, k3v)]
        k4v = acc(r4, v4, a); k4r = v4
        rn = [x + dt / 6 * (p + 2 * q + 2 * s + w) for x, p, q, s, w in zip(r, k1r, k2r, k3r, k4r)]
        vn = [x + dt / 6 * (p + 2 * q + 2 * s + w) for x, p, q, s, w in zip(v, k1v, k2v, k3v, k4v)]
        ang += math.atan2(r[0] * rn[1] - r[1] * rn[0], r[0] * rn[0] + r[1] * rn[1])
        r, v, t = rn, vn, t + dt
    rr = math.hypot(*r); eps = 0.5 * (v[0] ** 2 + v[1] ** 2) - MU / rr
    h = r[0] * v[1] - r[1] * v[0]
    e = math.sqrt(max(0.0, 1 + 2 * eps * h * h / MU**2))
    return t, a * t, e, ang / (2 * math.pi), math.hypot(*v)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    VT, VM = math.sqrt(MU / RE_), math.sqrt(MU / RM_)
    at = 0.5 * (RE_ + RM_)
    hoh = (math.sqrt(MU * (2 / RE_ - 1 / at)) - VT) + (VM - math.sqrt(MU * (2 / RM_ - 1 / at)))
    tH = math.pi * math.sqrt(at**3 / MU) / 86400
    print(f"V_Tierra = {VT:.4f} km/s ; V_Marte = {VM:.4f} km/s ; Edelbaum |dV| = {VT-VM:.4f} km/s ; Hohmann (suma de 2 impulsos) = {hoh:.4f} km/s en {tH:.2f} d")
    print(" a [m/s2]    t [d]   dv = a t [km/s]   dif. con Edelbaum [%]   e final   vueltas   v final [km/s]   propulsante (Isp 3000 s) [%]")
    ts = []; difs = []; es = []
    for a in (1e-5, 2e-5, 5e-5, 1e-4, 2e-4, 4e-4):
        t, dv, e, rev, vf = espiral(a)
        dif = 100 * (dv - (VT - VM)) / (VT - VM)
        prop = 100 * (1 - math.exp(-dv / (3000 * G0)))
        print(f"{a:9.1e} {t/86400:8.1f} {dv:14.4f} {dif:20.3f} {e:12.4f} {rev:9.2f} {vf:14.4f} {prop:20.2f}")
        difs.append(abs(dif)); es.append(e)
        ts.append((a, t))
    assert all(x < y for x, y in zip(difs, difs[1:])), difs  # la diferencia crece con la aceleracion
    assert difs[0] < 1.0 and es[0] < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
