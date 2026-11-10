#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B82-C01: Lambert de arco corto (theta < 180 deg) con el teorema de Lambert y coeficientes de Lagrange.

Datos: GM del Sol y UA del JPL SSD (consultados 2026-11-10). SINTETICOS: r1 = 1 UA, r2 = 1.524 UA en orbitas circulares
coplanares de ejemplo (no son efemerides), theta = 100 deg, tiempo de vuelo 200 d. Sistema: inercial heliocentrico de ejemplo, z = 0.
Modelo: dos cuerpos. t = sqrt(a^3/mu) [(al - sin al) - (be - sin be)], sin(al/2) = sqrt(s/2a), sin(be/2) = sqrt((s-c)/2a).
Segunda via: propagador kepleriano (variables universales) y solucionador x-lambda de Izzo. Tolerancias: residuo < 1e-10 UA,
velocidades entre metodos < 1e-9 (canonico). Dominio: elipse, theta < 180 deg, M = 0.
"""
import math, platform, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lambert_comun import *

r1, r2 = planetas_ejemplo(100.0)
c = float(np.linalg.norm(r2 - r1)); s = 0.5 * (1.0 + 1.524 + c)
am = s / 2.0
be_m = 2 * math.asin(math.sqrt((s - c) / s))
t_m = am ** 1.5 * (math.pi - (be_m - math.sin(be_m)))
t_p = math.sqrt(2.0) / 3.0 * (s ** 1.5 - (s - c) ** 1.5)


def tiempo(a):
    """Devuelve (t_rama_corta, t_rama_larga) para semieje a, arco corto."""
    al0 = 2 * math.asin(math.sqrt(s / (2 * a))); be = 2 * math.asin(math.sqrt((s - c) / (2 * a)))
    f = lambda al: a ** 1.5 * ((al - math.sin(al)) - (be - math.sin(be)))
    return f(al0), f(2 * math.pi - al0)


def resolver(t):
    rama_larga = t > t_m
    lo, hi = am, 1e4
    for _ in range(200):
        a = 0.5 * (lo + hi)
        tc, tl = tiempo(a)
        tt = tl if rama_larga else tc
        # en la rama corta t decrece con a; en la larga crece con a hasta infinito: se biseca segun la rama
        if rama_larga:
            if tt > t: hi = a
            else: lo = a
        else:
            if tt > t: lo = a
            else: hi = a
    return a, rama_larga


def velocidades(t):
    a, larga = resolver(t)
    al0 = 2 * math.asin(math.sqrt(s / (2 * a))); be = 2 * math.asin(math.sqrt((s - c) / (2 * a)))
    al = 2 * math.pi - al0 if larga else al0
    dE = al - be
    f = 1 - a / 1.0 * (1 - math.cos(dE))
    g = t - a ** 1.5 * (dE - math.sin(dE))
    return a, (r2 - f * r1) / g, larga


print("Python", platform.python_version(), "| numpy", np.__version__)
print(f"Datos SINTETICOS: r1 = 1 UA, r2 = 1.524 UA, theta = 100 deg; TU = {TU_DIA:.5f} d; VU = {VU_KMS:.4f} km/s")
print(f"c = {c:.6f}  s = {s:.6f}  a_min = s/2 = {am:.6f} UA")
print(f"t_min-energia = {t_m*TU_DIA:.3f} d ; t_parabolico = {t_p*TU_DIA:.3f} d")
t = 200.0 / TU_DIA
a, v1, larga = velocidades(t)
vi = lambert_izzo(r1, r2, t)
res = residuo(r1, v1, r2, t)
print(f"Transferencia de 200 d: a = {a:.6f} UA, rama {'larga' if larga else 'corta'}")
p = np.linalg.norm(np.cross(r1, v1)) ** 2
e = math.sqrt(1 - p / a)
print(f"  e = {e:.6f} ; v1 = [{v1[0]*VU_KMS:.4f}, {v1[1]*VU_KMS:.4f}] km/s ; |v1| = {np.linalg.norm(v1)*VU_KMS:.4f} km/s")
print(f"  energia = {energia(r1, v1):.8f} ; -1/(2a) = {-1/(2*a):.8f}")
print(f"  residuo de propagacion = {res:.2e} UA ; |v1 - v1(Izzo)| = {np.linalg.norm(v1 - vi[0]):.2e}")
print("t [d]   a [UA]   rama   |v1| [km/s]  residuo [UA]")
for td in (110, 130, 160, 200, 260, 330, 450):
    tt = td / TU_DIA
    if tt <= t_p:
        print(f"{td:5d}   (menor que el parabolico: hiperbola, no cubierto aqui)"); continue
    aa, vv, lg = velocidades(tt)
    print(f"{td:5d}  {aa:8.5f}  {'larga' if lg else 'corta'}  {np.linalg.norm(vv)*VU_KMS:10.4f}  {residuo(r1, vv, r2, tt):.1e}")
assert res < 1e-10 and np.linalg.norm(v1 - vi[0]) < 1e-9 and abs(energia(r1, v1) + 1 / (2 * a)) < 1e-10
print("Pruebas superadas.")
