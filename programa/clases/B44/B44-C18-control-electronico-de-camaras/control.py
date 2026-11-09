#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C18: tiempo de lectura, tiempo muerto, cuantizacion del ADC y binning.

Datos: ninguna constante fisica. Sensor de 4096 x 4096 pixeles, 4 puertos de salida, 1 MHz por puerto, 0,5 s de sobrecarga por cuadro, ADC de 16 bits, pozo de 100 000 e-, ruido de lectura
de 4 e- son ILUSTRATIVOS (sinteticos); no describen una camara real.
Modelo: tiempo de lectura = pixeles / (puertos x frecuencia) + sobrecarga, contado por un bucle de reloj y por formula; fraccion de tiempo muerto = t_lectura / (t_exp + t_lectura);
cuantizacion: sigma_q = g/sqrt(12) en electrones con g = pozo/(2^bits - 1); binning 2 x 2 en el chip (una lectura) frente a la suma por programa (cuatro lecturas): ruido RN frente a 2 RN. Semilla 20261109.
Supuestos: la sobrecarga no depende del binning; ruido de lectura gaussiano independiente por lectura. Validez: ilustrativa.
Tolerancia: tiempo contado frente a la formula a 1e-9 s; ruido simulado del binning dentro de 3 %.
"""
from __future__ import annotations
import math, platform, random, sys

def t_lectura(nx, ny, puertos, f, over):
    ciclos = 0
    por_puerto = nx * ny // puertos
    while ciclos < por_puerto:
        ciclos += 1
    return ciclos / f + over

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    nx = ny = 4096
    puertos, f, over = 4, 1e6, 0.5
    print(f"{'binning':>8} {'pixeles':>10} {'t lectura [s]':>14} {'formula [s]':>12} {'muerto (60 s) [%]':>18}")
    ts = {}
    for b in (1, 2, 4):
        n = nx // b
        t = t_lectura(n, n, puertos, f, over)
        fo = n * n / (puertos * f) + over
        ts[b] = t
        print(f"{b:8d} {n*n:10d} {t:14.4f} {fo:12.4f} {100*t/(60+t):18.2f}")
        assert abs(t - fo) < 1e-9
    assert abs(ts[1] - 4.6943) < 1e-3
    g = 100000 / (2 ** 16 - 1)
    sq = g / math.sqrt(12)
    print(f"ganancia {g:.4f} e-/ADU ; ruido de cuantizacion {sq:.4f} e- frente a 4 e- de lectura (efecto relativo {math.sqrt(16+sq*sq)/4-1:.5f})")
    for bits in (8, 12, 16):
        gb = 100000 / (2 ** bits - 1)
        print(f"  ADC de {bits:2d} bits: {gb:9.3f} e-/ADU ; cuantizacion {gb/math.sqrt(12):8.3f} e-")
    assert 7.0 < 100000 / (2 ** 12 - 1) / math.sqrt(12) < 7.1 and sq < 0.5
    rng = random.Random(20261109)
    rn, m = 4.0, 40000
    chip, soft = [], []
    for _ in range(m):
        chip.append(rng.gauss(0, rn))
        soft.append(sum(rng.gauss(0, rn) for _ in range(4)))
    def sd(xs):
        mu = sum(xs) / len(xs)
        return math.sqrt(sum((x - mu) ** 2 for x in xs) / (len(xs) - 1))
    print(f"binning 2x2 en el chip: ruido {sd(chip):.3f} e- ; por programa: {sd(soft):.3f} e- (esperados {rn:.3f} y {2*rn:.3f})")
    assert abs(sd(chip) / rn - 1) < 0.03 and abs(sd(soft) / (2 * rn) - 1) < 0.03
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
