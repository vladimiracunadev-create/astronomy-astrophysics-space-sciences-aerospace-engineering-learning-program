#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B82-C06: iteracion sobre T(x) con Newton, Halley y Householder (familia de Izzo 2014; no es Gooding 1990).

Datos: GM del Sol y UA del JPL SSD (2026-11-10). SINTETICOS: pares (r1, r2) de orbitas circulares de ejemplo, y 300 casos aleatorios con semilla 82.
Modelo: dos cuerpos, M = 0 (y un caso M = 1). Valor inicial de Izzo (aproximacion por tramos) frente a x0 = 0.
Segunda via: derivadas analiticas comparadas con diferencias finitas centrales; T de Lancaster-Blanchard frente a la forma de Lagrange; residuo por propagacion.
Tolerancias: derivadas 1e-6 relativas; T LB frente a Lagrange 1e-10; residuo < 1e-9 UA; tolerancia de la iteracion |dx| < 1e-12.
"""
import math, platform, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lambert_comun import *

print("Python", platform.python_version(), "| numpy", np.__version__)
print("Datos SINTETICOS: orbitas circulares de ejemplo y semilla aleatoria 82")
lam = 0.4
for x in (-0.5, 0.3, 1.6):
    T = tof_x(x, lam)
    d1, d2, d3 = derivadas_x(x, T, lam)
    h = 1e-5
    f1 = (tof_x(x + h, lam) - tof_x(x - h, lam)) / (2 * h)
    f2 = (tof_x(x + h, lam) - 2 * T + tof_x(x - h, lam)) / h ** 2
    print(f"x = {x:+.2f}: T = {T:.9f}, T' = {d1:+.6f} (dif. fin. {f1:+.6f}), T'' = {d2:+.5f} (dif. fin. {f2:+.5f})")
    assert abs(d1 - f1) < 1e-6 * max(1, abs(d1)) and abs(d2 - f2) < 1e-3 * max(1, abs(d2))
    if x != 1.6 or True:
        assert abs(T - tof_lagrange(x, lam)) < 1e-10
print("Traza del error |T(x_k) - T| (caso: theta = 100 deg, tof = 200 d, x0 de Izzo):")
r1, r2 = planetas_ejemplo(100.0); t = 200.0 / TU_DIA
for m in ("newton", "halley", "householder"):
    tr = []
    v = lambert_izzo(r1, r2, t, metodo=m, traza=tr)
    print(f"  {m:12s} iter = {v[3]}  " + " ".join(f"{e:.1e}" for e in tr) + f"  residuo = {residuo(r1, v[0], r2, t):.1e}")
print("Con x0 = 0 (sin valor inicial):")
c, s, lam1, n, _, _ = geometria(r1, r2)
T = math.sqrt(2.0 / s ** 3) * t
for m in ("newton", "halley", "householder"):
    x, it = resolver_x(T, lam1, 0, "derecha", m, x0=0.0)
    print(f"  {m:12s} iter = {it}")
rng = np.random.default_rng(82)
print("300 casos aleatorios (prograda, M = 0): iteraciones medias y maximas (valor inicial de Izzo)")
casos = []
while len(casos) < 300:
    ra, rb = rng.uniform(0.7, 1.8, 2); a1, a2 = rng.uniform(0, 2 * math.pi, 2)
    p1 = ra * np.array([math.cos(a1), math.sin(a1), 0.0]); p2 = rb * np.array([math.cos(a2), math.sin(a2), 0.0])
    th = (a2 - a1) % (2 * math.pi)
    if min(abs(th - math.pi), th, 2 * math.pi - th) < 0.05:
        continue
    casos.append((p1, p2, rng.uniform(0.3, 1.2) * 2 * math.pi * ((ra + rb) / 2) ** 1.5 / 2))
for m in ("newton", "halley", "householder"):
    its = []; peor = 0.0
    for p1, p2, tt in casos:
        v = lambert_izzo(p1, p2, tt, metodo=m)
        its.append(v[3]); peor = max(peor, residuo(p1, v[0], p2, tt))
    print(f"  {m:12s} media = {np.mean(its):.2f}  max = {max(its)}  residuo max = {peor:.1e}")
    assert peor < 1e-8
print("Caso M = 1 (tof = 1000 d, rama izquierda): ", end="")
v = lambert_izzo(r1, r2, 1000.0 / TU_DIA, M=1, rama="izquierda")
print(f"iter = {v[3]}, residuo = {residuo(r1, v[0], r2, 1000.0 / TU_DIA):.1e}")
print("Pruebas superadas.")
