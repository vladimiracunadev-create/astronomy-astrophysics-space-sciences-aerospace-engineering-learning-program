#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C19: presion de Casimir y regularizacion de sumas divergentes.

Datos: h, c y hbar = h/(2 pi) (NIST CODATA 2022), consultados 2026-11-09. Las separaciones (10 nm, 100 nm, 1 um), el area (1 cm^2) y los parametros de regularizacion (epsilon = 0.1; 0.05; 0.02)
son ILUSTRATIVOS (sinteticos). La presion calculada es la de placas ideales perfectamente conductoras, no la medida en un experimento real.
Modelo: energia de punto cero de un oscilador hbar omega/2; presion de Casimir entre placas paralelas ideales P = pi^2 hbar c/(240 d^4); regularizacion con un corte exponencial:
S_1(epsilon) = Sum n e^(-n epsilon) = 1/epsilon^2 - 1/12 + O(epsilon^2) y S_3(epsilon) = Sum n^3 e^(-n epsilon) = 6/epsilon^4 + 1/120 + O(epsilon^2); la parte finita (-1/12, 1/120) es la
que reaparece en la zeta de Riemann (zeta(-1) = -1/12, zeta(-3) = 1/120).
Supuestos: placas ideales, temperatura cero. Validez: separaciones mucho mayores que la longitud de plasma del metal (no verificado aqui).
Tolerancia: partes finitas dentro de 1e-3 de -1/12 y 1/120 con epsilon = 0.02; presion de Casimir escala como d^-4 a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

H, C = 6.62607015e-34, 299792458.0
HBAR = H / (2 * math.pi)


def casimir(d):
    return math.pi ** 2 * HBAR * C / (240 * d ** 4)


def suma(p, eps, nmax=None):
    nmax = nmax or int(60 / eps)
    return sum(n ** p * math.exp(-n * eps) for n in range(1, nmax + 1))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'d':>8} {'P = pi^2 hbar c/(240 d^4) [Pa]':>32} {'fuerza sobre 1 cm^2 [N]':>26}")
    for d in (1e-8, 1e-7, 1e-6):
        p = casimir(d)
        print(f"{d:8.0e} {p:32.4e} {p * 1e-4:26.4e}")
    assert abs(casimir(1e-7) / casimir(1e-6) / 1e4 - 1) < 1e-12
    print(f"1 atm = 101325 Pa (definicion): la presion de Casimir a 10 nm equivale a {casimir(1e-8) / 101325:.2f} atm")
    print(f"{'epsilon':>8} {'S1 - 1/eps^2':>14} {'-1/12':>9} {'S3 - 6/eps^4':>14} {'1/120':>9}")
    for eps in (0.1, 0.05, 0.02):
        s1 = suma(1, eps) - 1 / eps ** 2
        s3 = suma(3, eps) - 6 / eps ** 4
        print(f"{eps:8.2f} {s1:14.6f} {-1 / 12:9.6f} {s3:14.6f} {1 / 120:9.6f}")
    eps = 0.02
    assert abs(suma(1, eps) - 1 / eps ** 2 + 1 / 12) < 1e-3
    assert abs(suma(3, eps) - 6 / eps ** 4 - 1 / 120) < 1e-3
    # energia de punto cero de un oscilador a omega = 1e15 rad/s
    w = 1e15
    print(f"energia de punto cero hbar omega/2 con omega = 1e15 rad/s: {HBAR * w / 2:.4e} J = {HBAR * w / 2 / 1.602176634e-19:.4f} eV")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
