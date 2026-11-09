#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C06: ruido de lectura medido con dos cuadros de bias y efecto de la cuantizacion.

Datos: ninguna constante fisica. Ruido de lectura verdadero (5,0 e-), ganancia (1,5 e-/ADU), nivel de bias (1000 ADU) y cuadros de 64 x 64 pixeles son
ILUSTRATIVOS (sinteticos); no describen una camara real.
Modelo: cada cuadro = bias + ruido gaussiano de sigma_e/g ADU, redondeado al entero (ADC). El ruido de lectura se estima como std(A - B)/sqrt(2) (se cancela el patron fijo) y se
compara con la std de un solo cuadro (que mezcla el patron fijo). Cuantizacion: varianza 1/12 ADU^2.
Supuestos: ruido gaussiano, independiente entre cuadros y pixeles; patron fijo estable. Validez: ilustrativa.
Tolerancia: estimacion por diferencia dentro de 2 % del valor verdadero; semilla 20261109.
"""
from __future__ import annotations
import math, platform, random, sys

def std(xs):
    m = sum(xs) / len(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    n = 64 * 64
    g, rn, b0 = 1.5, 5.0, 1000.0
    patron = [rng.gauss(0, 3.0) for _ in range(n)]       # patron fijo en ADU
    def cuadro():
        return [round(b0 + patron[i] + rng.gauss(0, rn / g)) for i in range(n)]
    A, B = cuadro(), cuadro()
    dif = [a - b for a, b in zip(A, B)]
    s_dif = std(dif) / math.sqrt(2)
    s_uno = std(A)
    print(f"std de un solo cuadro: {s_uno:.3f} ADU (incluye patron fijo)")
    print(f"std(A-B)/sqrt(2): {s_dif:.3f} ADU = {s_dif*g:.3f} e-  (verdadero {rn:.3f} e-)")
    esp1 = math.sqrt((rn / g) ** 2 + 1 / 12)
    print(f"esperado por diferencia con cuantizacion: {esp1:.3f} ADU ; sin cuantizacion {rn/g:.3f} ADU")
    assert abs(s_dif * g / rn - 1) < 0.02
    assert abs(s_dif / esp1 - 1) < 0.02
    assert s_uno > s_dif
    print(f"{'ruido [ADU]':>12} {'cuantizacion [ADU]':>19} {'efecto relativo':>16}")
    for r_adu in (0.3, 1.0, 3.33):
        tot = math.sqrt(r_adu ** 2 + 1 / 12)
        print(f"{r_adu:12.2f} {math.sqrt(1/12):19.4f} {tot/r_adu-1:16.4f}")
    assert abs(math.sqrt(1 / 12) - 0.288675) < 1e-6
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
