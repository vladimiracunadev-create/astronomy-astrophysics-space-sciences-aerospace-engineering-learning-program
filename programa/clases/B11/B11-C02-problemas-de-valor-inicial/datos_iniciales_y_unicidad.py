#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C02: datos iniciales, sensibilidad y unicidad.

Datos: GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m
(valores nominales de la Resolución B3 de la IAU, 2015). Velocidad inicial de
7000 m/s: dato SINTÉTICO de ejemplo (lanzamiento vertical, sin atmósfera).
Modelo: (a) y' = sqrt|y|, y(0) = 0 admite dos soluciones; (b) y' = y amplifica
una diferencia inicial como e^t; (c) r'' = -GM/r^2 con r(0) = R, r'(0) = v0
conserva la energía específica e = v^2/2 - GM/r, de donde sale la altura máxima
(solución exacta) y la velocidad de escape.
Supuestos: movimiento radial, Tierra esférica y sin rotación, sin atmósfera.
Validez: v0 < v_escape para que exista un punto de retorno.
Tolerancia: 1e-12 relativa en las comprobaciones algebraicas; 1e-9 en la
altura máxima calculada por dos caminos independientes (fórmula y bisección).
"""
import math, platform

GM, R = 3.986004e14, 6.3781e6

# (a) no unicidad: dos soluciones de y' = sqrt|y|, y(0) = 0
f = lambda y: math.sqrt(abs(y))
y1 = lambda t: 0.0
y2 = lambda t: t * t / 4.0
t = 3.0
h = 1e-6
res1 = (y1(t + h) - y1(t - h)) / (2 * h) - f(y1(t))
res2 = (y2(t + h) - y2(t - h)) / (2 * h) - f(y2(t))
assert abs(res1) < 1e-9 and abs(res2) < 1e-6
print(f"(a) residuos de las dos soluciones en t=3: {res1:.1e} y {res2:.1e}; valores {y1(t)} y {y2(t)}")
for y in (1e-2, 1e-4, 1e-6):
    print(f"    cociente |f(y)-f(0)|/|y| = {f(y)/y:.1f}  (y = {y})")

# (b) sensibilidad: y' = y
d0 = 1e-6
dif = (1 + d0) * math.exp(10) - math.exp(10)
assert abs(dif - d0 * math.exp(10)) < 1e-9 * math.exp(10)
print(f"(b) diferencia inicial 1e-6 -> en t=10: {dif:.4e} (factor e^10 = {math.exp(10):.1f})")

# (c) lanzamiento vertical
v0 = 7000.0
e0 = v0**2 / 2 - GM / R
v_esc = math.sqrt(2 * GM / R)
rmax = -GM / e0                      # en el punto de retorno v = 0 -> e0 = -GM/rmax
# camino independiente: bisección de e(r) = e0 con v = 0
lo, hi = R, 1e9
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if -GM / mid < e0:
        lo = mid
    else:
        hi = mid
rmax_b = 0.5 * (lo + hi)
assert abs(rmax - rmax_b) / rmax < 1e-9
print(f"(c) e0 = {e0:.6e} J/kg; v_escape = {v_esc:.3f} m/s")
print(f"    r_max = {rmax/1e3:.3f} km; altura = {(rmax-R)/1e3:.3f} km; (bisección {(rmax_b-R)/1e3:.3f} km)")
print(f"    sin variación de g (g0 = GM/R^2 = {GM/R**2:.4f} m/s2): h = {v0**2/(2*GM/R**2)/1e3:.3f} km")
assert v0 < v_esc
print(f"Python {platform.python_version()}")
print("Pruebas superadas.")
