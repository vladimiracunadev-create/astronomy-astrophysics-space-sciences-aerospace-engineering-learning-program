#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C16: propagacion de incertidumbre (GUM y Monte Carlo).

Datos: GM de la Tierra = 3.986004e14 m3/s2 (valor nominal IAU 2015 B3,
arXiv:1510.07674, consultado 2026-11-05), tomado SIN incertidumbre. Semieje
a = 6 778 100 m (radio ecuatorial nominal 6.3781e6 m + 400 km ilustrativos)
con u(a) = 1000 m (ILUSTRATIVO). Paralaje p = 10 mas con u(p) = 2 mas
(SINTETICO).
Modelo: v = sqrt(GM/a) (velocidad circular) y d = 1000/p (pc, p en mas).
Ley de propagacion (GUM 5.1.2): u_c^2 = sum (df/dx_i)^2 u^2(x_i).
Metodo de Monte Carlo (JCGM 101): M = 1 000 000 pruebas.
Supuestos: entradas independientes y normales (o rectangular donde se indique).
Validez: linealizacion buena si u/x es pequena (v) y mala si es grande (d).
Tolerancia: u(v) de GUM vs Monte Carlo a menos de 0.5 %; para d (u/x = 20 %)
la discrepancia debe superar 5 % en el limite de cobertura. Detienen la ejecucion.
"""
import math
import platform

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")
GM = 3.986004e14
a, ua = 6_778_100.0, 1000.0
v = math.sqrt(GM / a)
dv_da = -0.5 * v / a
uv_gum = abs(dv_da) * ua
print(f"v = {v:.3f} m/s; sensibilidad dv/da = {dv_da:.3e} (m/s)/m; u(v) por GUM = {uv_gum:.4f} m/s")

rng = np.random.default_rng(1616)
M = 1_000_000
aa = rng.normal(a, ua, M)
vv = np.sqrt(GM / aa)
print(f"MC normal: media = {vv.mean():.3f}; u(v) = {vv.std():.4f} m/s; IC 95 % = [{np.percentile(vv, 2.5):.3f}, {np.percentile(vv, 97.5):.3f}]")
assert abs(vv.std() / uv_gum - 1) < 0.005

# tolerancia rectangular +-1500 m -> u = a/sqrt(3)
half = 1500.0
ur = half / math.sqrt(3)
aa_r = rng.uniform(a - half, a + half, M)
vr = np.sqrt(GM / aa_r)
print(f"rectangular +-{half:.0f} m: u(a) = {ur:.1f} m; u(v) GUM = {abs(dv_da)*ur:.4f}; MC = {vr.std():.4f} m/s")
assert abs(vr.std() / (abs(dv_da) * ur) - 1) < 0.005

# no linealidad: d = 1000/p con 20 % de incertidumbre relativa
p0, up = 10.0, 2.0
d0 = 1000.0 / p0
ud_gum = 1000.0 / p0**2 * up
pp = rng.normal(p0, up, M)
pp = pp[pp > 0]
dd = 1000.0 / pp
lo, hi = np.percentile(dd, [2.5, 97.5])
print(f"d = {d0:.1f} pc; GUM: u(d) = {ud_gum:.1f} pc -> [{d0-1.96*ud_gum:.1f}, {d0+1.96*ud_gum:.1f}]")
print(f"MC: media = {dd.mean():.1f}; mediana = {np.median(dd):.1f}; u(d) = {dd.std():.1f}; IC 95 % = [{lo:.1f}, {hi:.1f}] pc (asimetrico)")
assert abs(hi - (d0 + 1.96 * ud_gum)) / (d0 + 1.96 * ud_gum) > 0.05

# con 1 % el linealizado coincide
p1, up1 = 100.0, 1.0
d1 = 1000.0 / p1
ud1 = 1000.0 / p1**2 * up1
x1 = 1000.0 / rng.normal(p1, up1, M)
print(f"p = 100 +/- 1 mas: u(d) GUM = {ud1:.4f}; MC = {x1.std():.4f} pc")
assert abs(x1.std() / ud1 - 1) < 0.01
print("Pruebas superadas.")
