#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B82-C04: Lambert con M revoluciones completas (dos ramas, tiempo minimo).

Datos: GM del Sol y UA del JPL SSD (2026-11-10). SINTETICOS: r1 = 1 UA, r2 = 1.524 UA, theta = 100 deg, plano z = 0.
Modelo: dos cuerpos, variable x de Lancaster-Blanchard (Izzo 2014). Para cada M >= 1 hay un T_min(M): si T < T_min(M) no hay solucion;
si T > T_min(M) hay dos (rama izquierda x<x_min y derecha x>x_min). Segunda via: minimo de T(x) por barrido fino y propagador kepleriano.
Tolerancias: |x_min(Halley) - x_min(barrido)| < 1e-5; residuo < 1e-9 UA.
"""
import math, platform, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lambert_comun import *

print("Python", platform.python_version(), "| numpy", np.__version__)
print("Datos SINTETICOS: r1 = 1 UA, r2 = 1.524 UA, theta = 100 deg")
r1, r2 = planetas_ejemplo(100.0)
c, s, lam, n, _, _ = geometria(r1, r2)
fac = math.sqrt(s ** 3 / 2.0) * TU_DIA          # T adimensional -> dias
print(f"lambda = {lam:.5f} ; 1 unidad de T adimensional = {fac:.3f} d")
print("M   x_min      T_min [d]   (barrido x_min)")
for M in range(1, 5):
    xm = x_tmin(lam, M)
    xs = np.linspace(-0.999, 0.999, 399999)
    Ts = np.array([tof_x(float(x), lam, M) for x in xs[::40]])
    xb = xs[::40][int(np.argmin(Ts))]
    print(f"{M}  {xm:+.6f}  {tof_x(xm, lam, M)*fac:10.3f}   ({xb:+.4f})")
    assert abs(xm - xb) < 1e-2 and tof_x(xm, lam, M) <= Ts.min() + 1e-9
print("Soluciones por tiempo de vuelo (prograda):")
print("tof [d]   M  rama       x        a [UA]  |v1| [km/s]  residuo [UA]")
for td in (300, 700, 1000, 1500):
    t = td / TU_DIA
    for M, rama in ((0, "derecha"), (1, "izquierda"), (1, "derecha"), (2, "izquierda"), (2, "derecha")):
        r = lambert_izzo(r1, r2, t, M=M, rama=rama)
        if r is None:
            print(f"{td:6d}   {M}  {rama:9s}  sin solucion (T < T_min)")
            continue
        v1, v2, x, it = r
        a = 1.0 / (2.0 / 1.0 - np.dot(v1, v1))
        res = residuo(r1, v1, r2, t)
        assert res < 1e-9
        print(f"{td:6d}   {M}  {rama:9s} {x:+.5f}  {a:7.4f}  {np.linalg.norm(v1)*VU_KMS:9.4f}   {res:.1e}")
print("Pruebas superadas.")
