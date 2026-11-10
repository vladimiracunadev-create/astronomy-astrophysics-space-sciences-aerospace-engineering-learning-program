#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C05: una NRHO sur de L2 por correccion diferencial en el CR3BP y su monodromia.

Datos CONSULTADOS (2026-11-10): constantes de cislunar_lib.py; referencia publicada (Davis, Khoury, Howell y Sweeney, NASA NTRS 20200000733):
periodo medio 6.56 d (6.26-6.76), radio de perilune medio 3366 km (3195-3557), radio de apolune medio 71100 km (70005-71849).
ILUSTRATIVO: la semilla (x0 = 1.0213, z0 = -0.1818, vy0 = -0.1) es una suposicion inicial del autor; z0 se fija y se corrigen x0 y vy0.
Modelo: CR3BP circular (sin Sol ni excentricidad lunar), Dormand-Prince 5(4) adaptativo (tolerancia 1e-12). La NRHO publicada es de un modelo de efemerides:
las diferencias con el CR3BP son esperables. Correccion: Newton sobre (x0, vy0) para vx = vz = 0 en el segundo cruce de y = 0.
Monodromia M por diferencias finitas centrales (1e-6); estabilidad con numpy.linalg.eigvals.
Tolerancias: |vx|, |vz| < 1e-11 en el cruce; Jacobi conservado < 1e-8; det(M) = 1 +- 1e-5.
"""
from __future__ import annotations
import math, os, platform, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

H = 2e-3


def disparo(x0, z0, vy0):
    return cruce_y0((x0, 0.0, z0, 0.0, vy0, 0.0))


def corregir(x0, z0, vy0):
    for _ in range(20):
        t, s = disparo(x0, z0, vy0)
        f = [s[3], s[5]]
        if max(abs(f[0]), abs(f[1])) < 1e-11:
            return x0, vy0, t
        d = 1e-7
        j = [[0, 0], [0, 0]]
        for k, (a, b) in enumerate([(x0 + d, vy0), (x0, vy0 + d)]):
            _, s2 = disparo(a, z0, b)
            j[0][k] = (s2[3] - f[0]) / d
            j[1][k] = (s2[5] - f[1]) / d
        dx = solve(j, [-f[0], -f[1]])
        x0 += dx[0]
        vy0 += dx[1]
    raise RuntimeError("sin convergencia")


def monodromia(s0, T):
    m = [[0.0] * 6 for _ in range(6)]
    d = 1e-6
    for k in range(6):
        sp = list(s0); sm = list(s0)
        sp[k] += d; sm[k] -= d
        fp = propagar_ad(tuple(sp), T, tol=1e-13); fm = propagar_ad(tuple(sm), T, tol=1e-13)
        for i in range(6):
            m[i][k] = (fp[i] - fm[i]) / (2 * d)
    return np.array(m)


def calcular():
    z0 = -0.1818
    x0, vy0, th = corregir(1.0213, z0, -0.1)
    s0 = (x0, 0.0, z0, 0.0, vy0, 0.0)
    T = 2 * th
    # muestreo de la orbita para perilune y apolune
    s, t, rmin, rmax, c0, dc = s0, 0.0, 9, 0, jacobi(s0), 0.0
    n = int(T / 5e-4) + 1
    for _ in range(n):
        s, _e = dp_paso(rhs, s, T / n)
        d = math.sqrt((s[0] - 1 + MU) ** 2 + s[1] ** 2 + s[2] ** 2)
        rmin, rmax = min(rmin, d), max(rmax, d)
        dc = max(dc, abs(jacobi(s) - c0))
    cierre = math.sqrt(sum((a - b) ** 2 for a, b in zip(propagar_ad(s0, T, tol=1e-13)[:3], s0[:3])))
    M = monodromia(s0, T)
    ev = np.linalg.eigvals(M)
    lam = max(abs(ev))
    nu = 0.5 * (lam + 1 / lam)
    return dict(x0=x0, z0=z0, vy0=vy0, T_d=T * T_U / DIA, rper=rmin * A_L, rapo=rmax * A_L, C=c0, dC=dc,
                cierre_km=cierre * A_L, det=float(np.linalg.det(M)), lam=float(lam), nu=float(nu),
                res=2 * P_SIN / (T * T_U / DIA), np=np.__version__, ev=sorted(abs(ev), reverse=True))


def main():
    r = calcular()
    print(f"Python {platform.python_version()} ; numpy {r['np']}")
    print(f"Semilla ILUSTRATIVA corregida: x0 = {r['x0']:.8f} ; z0 = {r['z0']:.4f} ; vy0 = {r['vy0']:.8f} (adimensional)")
    print(f"Periodo = {r['T_d']:.4f} d (publicado, modelo de efemerides: 6.56 d, rango 6.26-6.76)")
    print(f"Radio de perilune = {r['rper']:.0f} km (publicado medio 3366 km) ; radio de apolune = {r['rapo']:.0f} km (publicado medio 71100 km)")
    print(f"Altitud de perilune sobre R_L = {r['rper'] - R_L:.0f} km")
    print(f"Resonancia: 2*P_sin/T = {r['res']:.3f} revoluciones por dos meses sinodicos (9:2 si es 9)")
    print(f"Constante de Jacobi C = {r['C']:.6f} ; deriva maxima = {r['dC']:.2e}")
    print(f"Cierre de la orbita tras un periodo = {r['cierre_km']:.3e} km ; det(M) = {r['det']:.6f}")
    print(f"|autovalores de M| = " + ", ".join(f"{v:.4g}" for v in r['ev']) + f" ; indice de estabilidad nu = {r['nu']:.3f}")
    assert r['dC'] < 1e-8
    assert abs(r['det'] - 1) < 1e-5
    assert 6.26 < r['T_d'] < 6.76
    assert r['cierre_km'] < 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
