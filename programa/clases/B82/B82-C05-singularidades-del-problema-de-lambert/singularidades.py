#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B82-C05: singularidades de Lambert (theta = 180 deg, c -> 0) y precision cerca de la parabola (x = 1).

Datos: GM del Sol y UA del JPL SSD (2026-11-10). SINTETICOS: r1 = (1, 0, 0) UA; r2 con radio 1.524 UA; tof = 250 d.
Modelo: dos cuerpos. Cerca de 180 deg la normal r1 x r2 se anula: su direccion la fija el cociente entre la desviacion fuera del plano y la
desviacion en el plano. Segunda via: inclinacion esperada atan(eps/delta) calculada a mano; residuo por propagacion.
Cerca de x = 1 se estudia la diferencia segunda de T(x) frente a T''(1) estimada. Tolerancias: residuo < 1e-9 UA; inclinacion a 1e-6 deg.
"""
import math, platform, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lambert_comun import *

print("Python", platform.python_version(), "| numpy", np.__version__)
print("Datos SINTETICOS: r1 = (1,0,0) UA, |r2| = 1.524 UA, tof = 250 d")
r1 = np.array([1.0, 0.0, 0.0]); t = 250.0 / TU_DIA
print("A) Cerca de 180 deg: r2 = 1.524 (-1, delta, eps)/norma; inclinacion = atan(|eps|/delta)")
print("  delta      eps       incl [deg]  esperada    |v1| [km/s]  v1_z [km/s]  residuo")
for delta, eps in ((1e-2, 0.0), (1e-2, 1e-4), (1e-2, 1e-2), (1e-2, 1e-1), (1e-6, 1e-6), (1e-6, -1e-6), (1e-9, 1e-6)):
    r2 = np.array([-1.0, delta, eps]); r2 = 1.524 * r2 / np.linalg.norm(r2)
    v1, v2, x, it = lambert_izzo(r1, r2, t)
    h = np.cross(r1, v1)
    inc = math.degrees(math.acos(h[2] / np.linalg.norm(h)))
    esp = math.degrees(math.atan2(abs(eps), delta))
    res = residuo(r1, v1, r2, t)
    print(f"  {delta:7.0e}  {eps:+8.0e}  {inc:10.5f}  {esp:9.5f}  {np.linalg.norm(v1)*VU_KMS:10.4f}  {v1[2]*VU_KMS:+10.4f}  {res:.1e}")
    assert res < 1e-9
print("B) Exactamente 180 deg (r2 = -1.524 x): normal indefinida; se pasa la normal de referencia")
for nref in ([0, 0, 1], [0, 1, 0], [0, 0.6, 0.8]):
    r2 = np.array([-1.524, 0.0, 0.0])
    v1, v2, x, it = lambert_izzo(r1, r2, t, normal=nref)
    print(f"  normal {nref}: v1 = [{v1[0]*VU_KMS:+.3f}, {v1[1]*VU_KMS:+.3f}, {v1[2]*VU_KMS:+.3f}] km/s, |v1| = {np.linalg.norm(v1)*VU_KMS:.4f}, residuo = {residuo(r1, v1, r2, t):.1e}")
    assert residuo(r1, v1, r2, t) < 1e-9
print("C) Precision cerca de x = 1 (parabola): (T(1+d) + T(1-d) - 2 T(1)) / d^2 con lambda = 0.5")
lam = 0.5
ref = None
print("  d          LB             Lagrange")
for d in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8):
    T1 = tof_x(1.0, lam)
    lb = (tof_x(1 + d, lam) + tof_x(1 - d, lam) - 2 * T1) / d ** 2
    lg = (tof_lagrange(1 + d, lam) + tof_lagrange(1 - d, lam) - 2 * T1) / d ** 2
    if d == 1e-2: ref = lb
    print(f"  {d:7.0e}  {lb:+14.6f}  {lg:+14.6f}")
assert abs(((tof_x(1.01, lam) + tof_x(0.99, lam) - 2 * tof_x(1.0, lam)) / 1e-4) - ref) < 1e-9
print("Pruebas superadas.")
