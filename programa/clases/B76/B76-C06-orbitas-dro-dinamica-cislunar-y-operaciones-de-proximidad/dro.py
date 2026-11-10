#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C06: familia de orbitas retrogradas distantes (DRO) planas en el CR3BP.

Datos CONSULTADOS (2026-11-10): constantes de cislunar_lib.py (JPL DE440, NASA/NSSDC).
ILUSTRATIVO: amplitudes de partida (distancia a la Luna en el cruce inicial) 30000-100000 km y la semilla vy0 = 0.486 (adimensional).
Modelo: CR3BP plano, ejes sinodicos. Orbita simetrica: x0 = 1 - mu - A/a con vx0 = 0, vy0 > 0 (retrograda en el marco sinodico); Newton en vy0
para vx = 0 en el siguiente cruce de y = 0 (semiperiodo). Continuacion en A (paso 10000 km) usando la solucion anterior como semilla.
Estabilidad: monodromia plana (4x4, diferencias finitas centrales 1e-6) y numpy.linalg.eigvals; estable si todos los |autovalores| = 1 (tolerancia 1e-3: el par doble en 1 es defectivo y las diferencias finitas lo separan ~2e-4).
Tolerancias: |vx| < 1e-11 en el cruce; det(M plana) = 1 +- 1e-5; cierre de la orbita < 1e-3 km.
"""
from __future__ import annotations
import math, os, platform, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *


def semiperiodo(a_km, vy):
    x0 = 1 - MU - a_km / A_L
    return cruce_y0((x0, 0.0, 0.0, 0.0, vy, 0.0))


def resolver(a_km, vy):
    for _ in range(30):
        t, s = semiperiodo(a_km, vy)
        if abs(s[3]) < 1e-11:
            return vy, t, s
        d = 1e-7
        _, s2 = semiperiodo(a_km, vy + d)
        vy -= s[3] / ((s2[3] - s[3]) / d)
    raise RuntimeError("sin convergencia")


def monodromia_plana(s0, T):
    idx = (0, 1, 3, 4)
    m = np.zeros((4, 4))
    d = 1e-6
    for j, k in enumerate(idx):
        sp = list(s0); sm = list(s0)
        sp[k] += d; sm[k] -= d
        fp = propagar_ad(tuple(sp), T, tol=1e-13); fm = propagar_ad(tuple(sm), T, tol=1e-13)
        for i, ii in enumerate(idx):
            m[i, j] = (fp[ii] - fm[ii]) / (2 * d)
    return m


def calcular():
    out = []
    vy = 0.486
    for a in range(30000, 100001, 10000):
        vy, t, s = resolver(float(a), vy)
        if a in (30000, 50000, 70000, 100000):
            x0 = 1 - MU - a / A_L
            s0 = (x0, 0.0, 0.0, 0.0, vy, 0.0)
            T = 2 * t
            M = monodromia_plana(s0, T)
            ev = np.linalg.eigvals(M)
            sf = propagar_ad(s0, T, tol=1e-13)
            cierre = math.hypot(sf[0] - s0[0], sf[1] - s0[1]) * A_L
            out.append(dict(a=a, vy=vy, T=T * T_U / DIA, x_este=(s[0] - (1 - MU)) * A_L, C=jacobi(s0),
                            lam=float(max(abs(ev))), det=float(np.linalg.det(M)), cierre=cierre))
    return out


def main():
    r = calcular()
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    print(" A [km]    vy0 (adim)   P [d]    x este [km]   C         max|lambda|   det(M)     cierre [km]")
    for q in r:
        print(f"{q['a']:7d}  {q['vy']:10.6f}  {q['T']:7.3f}  {q['x_este']:11.0f}  {q['C']:8.5f}  {q['lam']:9.6f}  {q['det']:9.6f}  {q['cierre']:.2e}")
    for q in r:
        assert abs(q['det'] - 1) < 1e-5 and q['cierre'] < 1e-3
        assert q['lam'] < 1.001
    assert r[-1]['T'] > r[0]['T']
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
