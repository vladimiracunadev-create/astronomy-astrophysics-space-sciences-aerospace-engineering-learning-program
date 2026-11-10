#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B82-C02: Lambert de arco largo (theta > 180 deg), sentido de giro y normal del plano.

Datos: GM del Sol y UA del JPL SSD (consultados 2026-11-10). SINTETICOS: r1 = 1 UA, r2 = 1.524 UA (orbitas circulares de ejemplo),
tiempo de vuelo 300 d, sistema inercial heliocentrico de ejemplo (referencia +z). Modelo: dos cuerpos.
Convenio: theta se mide en sentido antihorario alrededor de la normal n del movimiento; lambda = +sqrt(1-c/s) si theta < 180, negativo si > 180.
Segunda via: propagador kepleriano y solucionador de variables universales (con Delta theta = 2 pi - arccos). Tolerancia: residuo < 1e-10 UA.
"""
import math, platform, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lambert_comun import *

print("Python", platform.python_version(), "| numpy", np.__version__)
print("Datos SINTETICOS: r1 = 1 UA, r2 = 1.524 UA, tof = 300 d")
t = 300.0 / TU_DIA
vc = 1.0
print("Mismo par (r1, r2 a 260 deg antihorario), tres lecturas:")
r1, r2 = planetas_ejemplo(260.0)
for nombre, pro in (("prograda (theta = 260 deg)", True), ("retrograda (theta = 100 deg horario)", False)):
    v1, v2, x, it = lambert_izzo(r1, r2, t, prograda=pro)
    h = np.cross(r1, v1)
    c, s, lam, n, _, _ = geometria(r1, r2, pro)
    print(f"  {nombre}: lambda = {lam:+.4f}, h_z = {h[2]:+.4f}, |v1| = {np.linalg.norm(v1)*VU_KMS:.4f} km/s, "
          f"x = {x:+.5f}, iter = {it}, residuo = {residuo(r1, v1, r2, t):.1e}")
    assert residuo(r1, v1, r2, t) < 1e-10 and (h[2] > 0) == pro
vu = lambert_universal(r1, r2, t, prograda=True)
vi = lambert_izzo(r1, r2, t, prograda=True)
print(f"Prograda: |v1(universal) - v1(Izzo)| = {np.linalg.norm(vu[0]-vi[0]):.2e}")
assert np.linalg.norm(vu[0] - vi[0]) < 1e-8

print("Barrido de theta (prograda, tof 300 d): theta, lambda, |v1| [km/s], energia, residuo")
for th in (60, 120, 170, 190, 230, 270, 320, 350):
    a, b = planetas_ejemplo(float(th))
    v1, v2, x, it = lambert_izzo(a, b, t)
    lam = geometria(a, b)[2]
    print(f"  {th:4d}  {lam:+.4f}  {np.linalg.norm(v1)*VU_KMS:9.4f}  {energia(a, v1):+.5f}  {residuo(a, v1, b, t):.1e}")

print("Caso 3D (r2 con z = +0.15 UA, SINTETICO): la normal sale de r1 x r2")
r2z = np.array([1.2, 0.9, 0.15])
for pro in (True, False):
    v1, v2, x, it = lambert_izzo(r1, r2z, t, prograda=pro)
    h = np.cross(r1, v1)
    inc = math.degrees(math.acos(h[2] / np.linalg.norm(h)))
    print(f"  prograda={pro}: inclinacion = {inc:.3f} deg, residuo = {residuo(r1, v1, r2z, t):.1e}")
    assert residuo(r1, v1, r2z, t) < 1e-10
print("Pruebas superadas.")
