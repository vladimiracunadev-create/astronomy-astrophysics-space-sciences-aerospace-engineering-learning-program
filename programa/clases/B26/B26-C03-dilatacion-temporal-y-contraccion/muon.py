#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C03: supervivencia de muones con dilatacion temporal y contraccion de longitudes.

Datos: vida media del muon positivo en reposo 2 196 980.3 ps (MuLan, Tishchenko et al.,
arXiv:1211.0960, resumen, consultado 2026-11-09); c exacta (NIST CODATA 2022). Altura de produccion
de 15 km y velocidades de los muones: valores SINTETICOS (ilustrativos).
Modelo: en el marco del laboratorio, fraccion superviviente exp(-d/(gamma beta c tau)); en el marco
del muon, la longitud contraida d/gamma se recorre a beta c y el tiempo propio es d/(gamma beta c).
Ambas descripciones deben dar el mismo resultado. Sin relatividad: exp(-d/(beta c tau)).
Supuestos: trayectoria recta a velocidad constante, desintegracion exponencial. Validez: ilustrativa.
Tolerancia: 1e-12 (relativa) entre los dos marcos.
"""
from __future__ import annotations
import math
import platform
import sys

C = 299792458.0
TAU = 2196980.3e-12     # s
D = 15.0e3               # m (sintetico)


def gamma(beta):
    return 1 / math.sqrt(1 - beta * beta)


def sup_lab(beta, d=D):
    return math.exp(-d / (gamma(beta) * beta * C * TAU))


def sup_muon(beta, d=D):
    longitud = d / gamma(beta)
    t_propio = longitud / (beta * C)
    return math.exp(-t_propio / TAU)


def sup_clasico(beta, d=D):
    return math.exp(-d / (beta * C * TAU))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"vida media en reposo = {TAU * 1e6:.7f} us ; c tau = {C * TAU:.2f} m")
    print(f"{'beta':>8} {'gamma':>9} {'S (lab)':>12} {'S (muon)':>12} {'S (sin SR)':>12}")
    for beta in (0.9, 0.99, 0.999, 0.9999):
        a, b, c = sup_lab(beta), sup_muon(beta), sup_clasico(beta)
        assert abs(a - b) <= 1e-12 * a + 1e-300, "marcos no coinciden"
        print(f"{beta:8.4f} {gamma(beta):9.3f} {a:12.4e} {b:12.4e} {c:12.4e}")
    assert sup_lab(0.999) > 1e3 * sup_clasico(0.999)
    lo, hi = 1.0000001, 1e4
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        beta = math.sqrt(1 - 1 / mid ** 2)
        if sup_lab(beta) < 0.5:
            lo = mid
        else:
            hi = mid
    print(f"gamma para S = 1/2 tras 15 km: {hi:.2f} (beta = {math.sqrt(1 - 1 / hi ** 2):.8f})")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
