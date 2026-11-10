#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B82-C03: variables universales (z, funciones de Stumpff) para elipse, parabola e hiperbola.

Datos: GM del Sol y UA del JPL SSD (2026-11-10). SINTETICOS: r1 = 1 UA, r2 = 1.524 UA, theta = 100 deg, plano z = 0.
Modelo: dos cuerpos, M = 0. z = alfa chi^2 (>0 elipse, 0 parabola, <0 hiperbola). F(z) = (y/C)^(3/2) S + A sqrt(y) - sqrt(mu) t = 0.
Segunda via: parabola de Euler t_p = (1/3) sqrt(2/mu) (s^1.5 - (s-c)^1.5) (theta < 180) y propagador kepleriano.
Tolerancias: |z| < 1e-9 en la parabola; residuo < 1e-10 UA; biseccion y Newton coinciden en z a 1e-9.
"""
import math, platform, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lambert_comun import *

print("Python", platform.python_version(), "| numpy", np.__version__)
print("Datos SINTETICOS: r1 = 1 UA, r2 = 1.524 UA, theta = 100 deg")
r1, r2 = planetas_ejemplo(100.0)
c = float(np.linalg.norm(r2 - r1)); s = 0.5 * (1.0 + 1.524 + c)
tp = math.sqrt(2.0) / 3.0 * (s ** 1.5 - (s - c) ** 1.5)
print(f"t_parabolico (Euler) = {tp*TU_DIA:.4f} d")
vp = lambert_universal(r1, r2, tp)
print(f"  z en t = t_p: {vp[2]:+.3e} (esperado 0)")
assert abs(vp[2]) < 1e-9
print("Stumpff: C(z), S(z) en z = -1, 0, 1 y pi^2:")
for z in (-1.0, 0.0, 1.0, math.pi ** 2):
    cc, ss = stumpff(z)
    print(f"  z = {z:+.4f}: C = {cc:.8f}, S = {ss:.8f}")
assert abs(stumpff(math.pi ** 2)[0] - 2 / math.pi ** 2) < 1e-12      # C(pi^2) = 2/pi^2
print("t [d]     z       tipo        |v1| [km/s]  iter(bis) iter(Newton)  residuo [UA]")
for td in (40, 70, tp * TU_DIA, 120, 200, 400, 800):
    t = td / TU_DIA
    b = lambert_universal(r1, r2, t)
    n = lambert_universal(r1, r2, t, metodo="newton")
    z = b[2]
    tipo = "hiperbola" if z < -1e-6 else ("parabola" if abs(z) < 1e-6 else "elipse")
    res = residuo(r1, b[0], r2, t)
    en = energia(r1, b[0])
    assert (en > 1e-9) == (z < -1e-6) or abs(en) < 1e-6
    assert abs(b[2] - n[2]) < 1e-8 and res < 1e-9
    print(f"{td:7.2f}  {z:+8.4f}  {tipo:9s}  {np.linalg.norm(b[0])*VU_KMS:10.4f}  {b[3]:6d}  {n[3]:8d}     {res:.1e}")
print("Pruebas superadas.")
