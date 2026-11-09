#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B34-C03: estratificacion hidrostatica de un bucle semicircular y conservacion del flujo.

Datos: k_B, u (NIST CODATA 2022) y GM_sol, R_sol (UAI 2015 B3), consultados 2026-11-09. La temperatura (1.5e6 K), la masa molecular media (0.6), las longitudes de semibucle (3e7, 5e7, 1e8 m) y el campo de la base
(0.01 T) con expansion de la seccion son ILUSTRATIVOS (sinteticos).
Modelo: bucle semicircular de semilongitud L con gravedad efectiva g_par(s) = g cos(pi s/(2 L)) (g constante, base en la superficie); presion isoterma dP/ds = -rho g_par con rho = mu u P/(k T): cociente
apice/base P_top/P_0 = exp(-2 L/(pi H)) con H = kT/(mu u g), verificado por integracion numerica RK4; conservacion del flujo B A = constante con una seccion que se ensancha en el apice (factor 1.3).
Supuestos: isotermo y estatico; g no varia con la altura. Validez: orientativa para L pequena frente al radio solar.
Tolerancia: cociente numerico frente al cerrado a 1e-9.
"""
from __future__ import annotations
import math, platform, sys
KB, U = 1.380649e-23, 1.66053906892e-27
GM, R = 1.3271244e20, 6.957e8

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    g = GM / R ** 2
    t, mu = 1.5e6, 0.6
    h = KB * t / (mu * U * g)
    print(f"g = {g:.3f} m/s2 ; H = kT/(mu u g) = {h / 1e6:.2f} Mm")
    print(f"{'L [Mm]':>7} {'P_top/P_0 numerico':>19} {'exp(-2L/(pi H))':>17} {'cociente':>10}")
    for l in (3e7, 5e7, 1e8):
        n = 2000
        ds = l / n
        f = lambda s, p: -p / h * math.cos(math.pi * s / (2 * l))
        p, s = 1.0, 0.0
        for _ in range(n):
            k1 = f(s, p); k2 = f(s + ds / 2, p + ds / 2 * k1); k3 = f(s + ds / 2, p + ds / 2 * k2); k4 = f(s + ds, p + ds * k3)
            p += ds * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            s += ds
        ana = math.exp(-2 * l / (math.pi * h))
        print(f"{l / 1e6:7.0f} {p:19.9f} {ana:17.9f} {p / ana:10.8f}")
        assert abs(p / ana - 1) < 1e-9
    b0 = 0.01
    print(f"flujo: B_base = {b0} T con seccion A0 ; en el apice con A = 1.3 A0, B = {b0 / 1.3:.5f} T (B A = constante)")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
