#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C04: eficiencia cuantica efectiva integrada sobre una banda.

Datos: ninguna constante fisica. La curva QE(lambda) es una gaussiana ILUSTRATIVA (maximo 0,90 en 650 nm, anchura 150 nm) y la banda de 500 a 800 nm es sintetica;
no es la curva de ningun detector real.
Modelo: QE_ef = integral(phi QE d lambda) / integral(phi d lambda) con espectro plano en fotones (phi constante); integral exacta con erf; regla del trapecio y de Simpson.
Supuestos: espectro plano en fotones por unidad de longitud de onda. Validez: ilustrativa.
Tolerancia: Simpson con 400 intervalos frente a la solucion exacta a 1e-9 relativo; el trapecio a 1e-4.
"""
from __future__ import annotations
import math, platform, sys

QMAX, L0, S = 0.90, 650.0, 150.0

def qe(l):
    return QMAX * math.exp(-0.5 * ((l - L0) / S) ** 2)

def exacta(a, b):
    f = lambda x: math.erf((x - L0) / (S * math.sqrt(2)))
    return QMAX * S * math.sqrt(math.pi / 2) * (f(b) - f(a)) / (b - a)

def trapecio(a, b, n):
    h = (b - a) / n
    return h * (0.5 * qe(a) + sum(qe(a + i * h) for i in range(1, n)) + 0.5 * qe(b)) / (b - a)

def simpson(a, b, n):
    h = (b - a) / n
    s = qe(a) + qe(b) + 4 * sum(qe(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1)) + 2 * sum(qe(a + 2 * i * h) for i in range(1, n // 2))
    return s * h / 3 / (b - a)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'lambda [nm]':>12} {'QE':>8}")
    for l in (400, 500, 650, 800, 900):
        print(f"{l:12d} {qe(l):8.4f}")
    a, b = 500.0, 800.0
    ex = exacta(a, b)
    print(f"{'n':>6} {'trapecio':>12} {'Simpson':>12}")
    for n in (4, 10, 40, 400):
        print(f"{n:6d} {trapecio(a, b, n):12.8f} {simpson(a, b, n):12.8f}")
    print(f"exacta (erf): {ex:.8f}")
    assert abs(simpson(a, b, 400) / ex - 1) < 1e-9
    assert abs(trapecio(a, b, 400) / ex - 1) < 1e-4
    ele = 1.0e6 * ex
    print(f"1 000 000 fotones en la banda -> {ele:.0f} electrones")
    assert abs(ele - 1e6 * ex) < 1e-6
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
