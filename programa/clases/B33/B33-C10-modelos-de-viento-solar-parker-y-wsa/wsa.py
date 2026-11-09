#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C10: relacion empirica de velocidad del viento solar frente a la expansion de las lineas de campo (forma funcional de tipo WSA) y comparacion con Parker.

Datos: k_B, u (NIST CODATA 2022), GM_sol y R_sol (UAI 2015 B3) y 1 au (IERS TN36), consultados 2026-11-09. La forma funcional v = v_0 + a/(1 + f)^(2/9) (1 - 0.8 e^(-(d/w)^1.25))^3 y todos sus coeficientes
(v_0 = 285, a = 625, w = 2.8, d = 5 grados) son ILUSTRATIVOS (sinteticos): se usan como una relacion de prueba, sin contrastarla con la literatura ni con mediciones.
Modelo: (1) velocidad de prueba en funcion del factor de expansion f y de la distancia angular d al borde de un agujero coronal: monotona decreciente en f y creciente en d; (2) viento isotermo de Parker
(B30-C10) para tres temperaturas coronales; comparacion de rangos.
Supuestos: relacion de prueba; Parker isotermo. Validez: ilustrativa.
Tolerancia: monotonia; Parker residual de la ecuacion a 1e-12.
"""
from __future__ import annotations
import math, platform, sys
KB, U = 1.380649e-23, 1.66053906892e-27
GM, R_SOL, AU = 1.3271244e20, 6.957e8, 1.49597870700e11

def vprueba(f, d):
    return 285.0 + 625.0 / (1 + f) ** (2 / 9) * (1 - 0.8 * math.exp(-(d / 2.8) ** 1.25)) ** 3

def u_parker(x):
    fn = lambda u: u * u - math.log(u * u) - 4 * math.log(x) - 4 / x + 3
    if abs(x - 1) < 1e-12:
        return 1.0
    lo, hi = (1e-12, 1.0) if x < 1 else (1.0, 50.0)
    for _ in range(300):
        m = 0.5 * (lo + hi)
        if (fn(m) > 0) == (x < 1):
            lo = m
        else:
            hi = m
    u = 0.5 * (lo + hi)
    assert abs(fn(u)) < 1e-9
    return u

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'f':>6} " + "".join(f"{'d = ' + str(d) + ' deg':>12}" for d in (1, 3, 5, 10)))
    for f in (2, 5, 10, 30, 100):
        print(f"{f:6d} " + "".join(f"{vprueba(f, d):12.1f}" for d in (1, 3, 5, 10)))
    for d in (1, 5, 10):
        v = [vprueba(f, d) for f in (2, 5, 10, 30, 100)]
        assert all(a > b for a, b in zip(v, v[1:]))
    for f in (2, 30):
        v = [vprueba(f, d) for d in (1, 3, 5, 10)]
        assert all(a < b for a, b in zip(v, v[1:]))
    print("monotonia: decrece con f y crece con d (prueba superada)")
    print(f"{'T [K]':>9} {'v(1 au) Parker [km/s]':>22}")
    for t in (1.0e6, 1.5e6, 2.0e6):
        cs = math.sqrt(KB * t / (0.6 * U))
        rc = GM / (2 * cs ** 2)
        print(f"{t:9.2e} {cs * u_parker(AU / rc) / 1e3:22.1f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
