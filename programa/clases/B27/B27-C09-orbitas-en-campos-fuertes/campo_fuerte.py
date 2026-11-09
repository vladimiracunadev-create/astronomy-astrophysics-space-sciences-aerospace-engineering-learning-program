#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C09: esfera de fotones, parametro de impacto critico y precesion en campo fuerte (Schwarzschild).

Datos: G, c (NIST CODATA 2022), GM_sol (IAU 2015 B3), 1 au (IERS TN36), consultados 2026-11-09. Masa de M87*:
6.5e9 Msol (Event Horizon Telescope, arXiv:1906.11238, resumen). Las orbitas de prueba (p, e) son ILUSTRATIVAS.
Modelo: unidades geometricas G = c = M = 1. Potencial efectivo de un fotón V(r) = (1 - 2/r)/r^2: su maximo (esfera de
fotones) esta en r = 3 y b_c = 1/sqrt(V) = 3 sqrt(3). Orbita de una particula: u = 1/r, u'' + u = 1/p + 3u^2, con
p el semilado recto newtoniano; la precesion por vuelta es 2 pi/(...) - 2 pi, comparada con la formula debil 6 pi/p.
Supuestos: Schwarzschild, cuerpo de prueba, sin radiacion. Validez: p grande para la formula debil.
Tolerancia: 1e-6 en r_fotones y b_c; 2 % entre la precesion integrada y 6 pi/p para p = 1000.
"""
from __future__ import annotations
import math
import platform
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20
AU = 1.49597870700e11


def maximo_V():
    a, b = 2.5, 10.0
    g = (math.sqrt(5) - 1) / 2
    f = lambda r: (1 - 2 / r) / r ** 2
    c_, d_ = b - g * (b - a), a + g * (b - a)
    for _ in range(200):
        if f(c_) > f(d_):
            b = d_
        else:
            a = c_
        c_, d_ = b - g * (b - a), a + g * (b - a)
    r = 0.5 * (a + b)
    return r, 1 / math.sqrt(f(r))


def precesion(p, e, n=40000):
    """RK4 en phi de u'' + u = 1/p + 3 u^2 desde el apoastro; devuelve phi(2 vuelta de u') - 2 pi."""
    u, v = (1 - e) / p, 0.0
    h = 2 * math.pi * 2.0 / n
    fz = lambda uu, vv: (vv, 1 / p + 3 * uu * uu - uu)
    phi = 0.0
    ceros = []
    for _ in range(n):
        k1 = fz(u, v)
        k2 = fz(u + 0.5 * h * k1[0], v + 0.5 * h * k1[1])
        k3 = fz(u + 0.5 * h * k2[0], v + 0.5 * h * k2[1])
        k4 = fz(u + h * k3[0], v + h * k3[1])
        un = u + h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        vn = v + h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        if v < 0 <= vn and phi > 1.0:
            ceros.append(phi + h * (-v) / (vn - v))
            break
        u, v, phi = un, vn, phi + h
    # cero ascendente de u' = siguiente apoastro (u minimo)
    return ceros[0] - 2 * math.pi


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r_ph, b_c = maximo_V()
    assert abs(r_ph - 3) < 1e-6 and abs(b_c - 3 * math.sqrt(3)) < 1e-6, "esfera de fotones"
    print(f"esfera de fotones: r = {r_ph:.6f} M ; b_c = {b_c:.6f} M (3 sqrt 3 = {3 * math.sqrt(3):.6f})")
    rg = 6.5e9 * GM_SOL / C ** 2
    print(f"M87* (6.5e9 Msol): r_g = {rg / AU:.1f} au ; diametro de la sombra 2 b_c r_g = {2 * b_c * rg / AU:.0f} au")
    f_isco = C ** 3 / (2 * math.pi * 6 ** 1.5 * GM_SOL * 10)
    print(f"frecuencia orbital en el ISCO (10 Msol): {f_isco:.1f} Hz ; en la esfera de fotones: {C ** 3 / (2 * math.pi * 3 ** 1.5 * GM_SOL * 10):.1f} Hz")
    print(f"{'p [M]':>8} {'e':>5} {'dphi integrada [rad]':>22} {'6 pi/p':>10} {'cociente':>9}")
    for p, e in ((1000.0, 0.2), (100.0, 0.2), (30.0, 0.3), (20.0, 0.2)):
        d = precesion(p, e)
        print(f"{p:8.1f} {e:5.2f} {d:22.6f} {6 * math.pi / p:10.6f} {d / (6 * math.pi / p):9.4f}")
    d = precesion(1000.0, 0.2)
    assert abs(d / (6 * math.pi / 1000.0) - 1) < 0.02, "precesion debil != 6 pi/p"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
