#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C09: ancho equivalente de una linea gaussiana y curva de crecimiento.

Datos: ninguna constante fisica. Los parametros (profundidad central, ancho, profundidades opticas 0.01 a 1000) son ILUSTRATIVOS (sinteticos).
Modelo: perfil de absorcion I/I_c = 1 - A exp(-x^2/(2 s^2)); ancho equivalente W = Int (1 - I/I_c) dx = A s sqrt(2 pi) por Simpson; curva de crecimiento
W(tau0) = Int (1 - exp(-tau0 e^(-x^2))) dx (x en unidades Doppler): regimen debil W ~ sqrt(pi) tau0, saturado W ~ 2 sqrt(ln tau0).
Supuestos: perfil gaussiano (Doppler puro). Validez: ideal.
Tolerancia: W numerico frente a A s sqrt(2 pi) a 1e-8; W/(sqrt(pi) tau0) -> 1 para tau0 = 0.01 a 1e-2.
"""
from __future__ import annotations
import math, platform, sys

def simpson(f, a, b, n=40000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    a, s = 0.6, 0.05
    w = simpson(lambda x: a * math.exp(-x * x / (2 * s * s)), -1, 1)
    print(f"linea gaussiana A = {a}, s = {s}: W numerico = {w:.8f} ; A s sqrt(2 pi) = {a * s * math.sqrt(2 * math.pi):.8f}")
    assert abs(w / (a * s * math.sqrt(2 * math.pi)) - 1) < 1e-8
    print(f"{'tau0':>8} {'W (unidades Doppler)':>21} {'sqrt(pi) tau0':>14} {'2 sqrt(ln tau0)':>16} {'regimen':>10}")
    for t0 in (0.01, 0.1, 1, 10, 100, 1000):
        wt = simpson(lambda x: 1 - math.exp(-t0 * math.exp(-x * x)), -12, 12, 20000)
        debil = math.sqrt(math.pi) * t0
        sat = 2 * math.sqrt(math.log(t0)) if t0 > 1 else float("nan")
        reg = "lineal" if t0 <= 0.1 else ("saturado" if t0 >= 10 else "transicion")
        print(f"{t0:8g} {wt:21.6f} {debil:14.6f} {sat:16.6f} {reg:>10}")
        if t0 == 0.01:
            assert abs(wt / debil - 1) < 1e-2
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
