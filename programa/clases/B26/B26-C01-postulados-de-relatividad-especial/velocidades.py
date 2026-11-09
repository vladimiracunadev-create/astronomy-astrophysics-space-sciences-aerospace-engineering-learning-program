#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C01: composicion de velocidades y constancia de c.

Datos: c = 299 792 458 m/s exacta (NIST CODATA 2022, consultado 2026-11-09); 1 au =
1.495 978 707 00e11 m (IERS Conventions 2010, TN36, Tabla 1.1, consultado 2026-11-09). Velocidades
de ejemplo: valores ILUSTRATIVOS (sinteticos).
Modelo: composicion relativista w = (u + v)/(1 + u v/c^2) comparada con la via independiente de la
rapidez: beta = tanh(eta), y las rapideces se suman (eta_w = eta_u + eta_v). Limite galileano
w = u + v para u, v << c.
Supuestos: movimiento colineal, marcos inerciales. Validez: cualquier velocidad < c.
Tolerancia: 1e-12 (relativa a c) entre la formula y la via de la rapidez.
"""
from __future__ import annotations
import math
import platform
import sys

C = 299792458.0
AU = 1.49597870700e11


def suma(u, v):
    return (u + v) / (1 + u * v / C ** 2)


def suma_rapidez(u, v):
    return C * math.tanh(math.atanh(u / C) + math.atanh(v / C))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for u, v in ((0.5 * C, 0.5 * C), (0.8 * C, 0.8 * C), (0.9 * C, 0.99 * C), (3.0e4, 3.0e4)):
        w1, w2 = suma(u, v), suma_rapidez(u, v)
        assert abs(w1 - w2) <= 1e-12 * C, "formula y rapidez difieren"
        assert w1 < C
        print(f"u = {u / C:.6f} c, v = {v / C:.6f} c -> w = {w1 / C:.8f} c (galileano {(u + v) / C:.6f} c)")
    for v in (3.0e4, 0.5 * C, 0.99 * C):
        assert abs(suma(C, v) - C) < 1e-6, "c no es invariante"
    print("c compuesta con v = 3e4, 0.5c, 0.99c: sigue valiendo c")
    d = suma(3.0e4, 3.0e4) - 6.0e4
    print(f"diferencia con galileano para 30 km/s + 30 km/s = {d:.3e} m/s")
    print(f"tiempo de luz por 1 au = {AU / C:.3f} s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
