#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C14: umbral y angulo de Cherenkov, rendimiento de fotones y resolucion de un calorimetro.

Datos: masas del electron (0.510 998 950 69 MeV), del muon (105.658 3755 MeV) y del proton (938.272 089 43 MeV) y la constante de estructura fina (7.297 352 5643e-3) (NIST CODATA 2022),
consultados 2026-11-09. El indice de refraccion (1.33), la banda de longitudes de onda (300 a 600 nm) y los parametros del calorimetro (a = 10 % sqrt(GeV), b = 1 %) son ILUSTRATIVOS (sinteticos).
Modelo: umbral beta > 1/n (gamma_th = 1/sqrt(1 - 1/n^2)) y energia cinetica T_th = m c^2 (gamma_th - 1); angulo cos(theta_C) = 1/(n beta); rendimiento de fotones por unidad de longitud
dN/dx = 2 pi alpha sen^2(theta_C) (1/lambda_1 - 1/lambda_2); resolucion sigma/E = a/sqrt(E) sumada en cuadratura con b, muestreada con semilla fija (20 000 sucesos por energia).
Supuestos: medio no dispersivo, eficiencia de deteccion del 100 %, errores gaussianos. Validez: ilustrativa.
Tolerancia: angulo a beta = 1 igual a arccos(1/n) a 1e-12; resolucion simulada dentro del 3 % de la formula.
"""
from __future__ import annotations
import math
import platform
import random
import sys

ME, MMU, MP = 0.51099895069, 105.6583755, 938.27208943
ALPHA = 7.2973525643e-3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n = 1.33
    gth = 1 / math.sqrt(1 - 1 / n ** 2)
    print(f"n = {n} (ilustrativo): beta_th = {1 / n:.5f} ; gamma_th = {gth:.5f}")
    print(f"{'particula':<10} {'m c^2 [MeV]':>12} {'T_umbral [MeV]':>15}")
    for nombre, m in (("electron", ME), ("muon", MMU), ("proton", MP)):
        print(f"{nombre:<10} {m:12.4f} {m * (gth - 1):15.4f}")
    th = math.degrees(math.acos(1 / n))
    print(f"angulo de Cherenkov para beta -> 1: {th:.3f} grados")
    print(f"{'beta':>7} {'cos(theta) = 1/(n beta)':>24} {'theta [deg]':>12}")
    for b in (0.76, 0.8, 0.9, 0.99, 1.0):
        print(f"{b:7.2f} {1 / (n * b):24.5f} {math.degrees(math.acos(1 / (n * b))):12.3f}")
    assert abs(math.degrees(math.acos(1 / n)) - th) < 1e-12
    l1, l2 = 300e-9, 600e-9
    dn = 2 * math.pi * ALPHA * (1 - 1 / n ** 2) * (1 / l1 - 1 / l2)
    print(f"rendimiento de fotones (300 a 600 nm, beta = 1): dN/dx = {dn:.1f} por m = {dn / 100:.1f} por cm")
    # calorimetro
    rng = random.Random(20261109)
    a, b = 0.10, 0.01
    print(f"{'E [GeV]':>8} {'sigma/E formula':>16} {'sigma/E simulada':>17} {'cociente':>9}")
    for e in (1.0, 10.0, 100.0):
        s_rel = math.sqrt(a ** 2 / e + b ** 2)
        med = [rng.gauss(e, s_rel * e) for _ in range(20000)]
        m = sum(med) / len(med)
        sd = math.sqrt(sum((x - m) ** 2 for x in med) / (len(med) - 1))
        print(f"{e:8.1f} {s_rel:16.5f} {sd / e:17.5f} {sd / e / s_rel:9.4f}")
        assert abs(sd / e / s_rel - 1) < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
