#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C25: aritmética de punto flotante, cancelación y suma compensada.

Datos: ninguno observado. Se usan números de ejemplo SINTÉTICOS: 0.1 y 0.2; x = 1e-8
para 1 - cos x; la ecuación x^2 - 1e8 x + 1 = 0 (raíces 1e8 - 1e-8 y 1e-8 aprox.);
10^6 sumandos iguales a 0.1.
Modelo: doble precisión IEEE 754 binary64 de Python (53 bits de mantisa). Referencias
exactas: aritmética racional (fractions) y la solución analítica
1 - cos x = 2 sin^2(x/2), de modo que 1 - cos(1e-8) = 5e-17 (a 1e-32 relativo).
Supuestos: redondeo al más cercano (valor por defecto). Validez: valores normales.
Tolerancia: el épsilon medido coincide con sys.float_info.epsilon; la forma estable de
1 - cos x tiene error relativo < 1e-15 y la ingenua más de 0.1; la suma de Kahan tiene
error al menos 100 veces menor que la ingenua; math.fsum coincide con la suma exacta
redondeada una vez.
"""
import math, platform, sys
from fractions import Fraction

print(f"Python {platform.python_version()}")
eps = sys.float_info.epsilon
e = 1.0
while 1.0 + e / 2 > 1.0:
    e /= 2
print(f"épsilon de máquina: medido {e:.4e} = 2^{int(round(math.log2(e)))} ; sys.float_info.epsilon = {eps:.4e}")
assert e == eps
print(f"0.1 = {Fraction(0.1)} (exacto almacenado) -> diferencia con 1/10: {float(Fraction(0.1) - Fraction(1, 10)):.3e}")
print(f"0.1 + 0.2 = {0.1 + 0.2!r} ; igual a 0.3: {0.1 + 0.2 == 0.3} ; diferencia = {0.1 + 0.2 - 0.3:.3e} ; isclose = {math.isclose(0.1 + 0.2, 0.3)}")
assert 0.1 + 0.2 != 0.3 and math.isclose(0.1 + 0.2, 0.3)
print(f"espaciado (ulp) en 1: {math.ulp(1.0):.3e} ; en 1e8: {math.ulp(1e8):.3e} ; en 1e16: {math.ulp(1e16):.3e} (1e16 + 1 = {1e16 + 1:.1f})")
assert 1e16 + 1 == 1e16
print(f"límites: máximo {sys.float_info.max:.3e}; mínimo normal {sys.float_info.min:.3e}; mínimo subnormal {5e-324:.3e}; 1e308*10 = {1e308*10}")

# cancelación
x = 1e-8
ingenua = 1 - math.cos(x)
estable = 2 * math.sin(x / 2) ** 2
exacta = x * x / 2 * (1 - x * x / 12)
print(f"1 - cos({x}): ingenua = {ingenua:.6e} ; estable = {estable:.6e} ; serie = {exacta:.6e}")
rel_ing, rel_est = abs(ingenua - exacta) / exacta, abs(estable - exacta) / exacta
print(f"   errores relativos: ingenua {rel_ing:.3e} ; estable {rel_est:.3e}")
assert rel_ing > 0.1 and rel_est < 1e-15

# ecuación cuadrática
a, b, c = 1.0, -1e8, 1.0
disc = math.sqrt(b * b - 4 * a * c)
r_ing = (-b - disc) / (2 * a)
r_est = (2 * c) / (-b + disc)
print(f"x^2 - 1e8 x + 1 = 0, raíz pequeña: fórmula directa {r_ing:.6e} ; forma estable {r_est:.6e} ; producto de raíces = c/a = 1")
r_grande = (-b + disc) / (2 * a)
print(f"   producto con la raíz grande: directa {r_ing * r_grande:.6f} ; estable {r_est * r_grande:.12f}")
assert abs(r_est * r_grande - 1) < 1e-12 and abs(r_ing * r_grande - 1) > 1e-3

# suma
N = 10**6
terms = [0.1] * N
exact = Fraction(0.1) * N
naive = 0.0
for t in terms:
    naive += t
s, comp = 0.0, 0.0
for t in terms:
    y = t - comp
    tt = s + y
    comp = (tt - s) - y
    s = tt
fs = math.fsum(terms)
err = lambda v: abs(Fraction(v) - exact) / exact
print(f"suma de 10^6 sumandos 0.1 (suma exacta de lo almacenado = {float(exact):.12f}):")
print(f"   ingenua  : {naive!r} error relativo = {float(err(naive)):.3e}")
print(f"   Kahan    : {s!r} error relativo = {float(err(s)):.3e}")
print(f"   fsum     : {fs!r} error relativo = {float(err(fs)):.3e}")
assert float(err(s)) * 100 < float(err(naive)) and fs == float(exact)
print("Pruebas superadas.")
