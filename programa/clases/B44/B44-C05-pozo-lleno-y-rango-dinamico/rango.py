#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C05: rango dinamico, relacion senal-ruido y saturacion del pozo.

Datos: ninguna constante fisica. El pozo lleno (50 000 e-), el ruido de lectura (5 e-) y el ADC de 16 bits son ILUSTRATIVOS (sinteticos); no describen una camara real.
Modelo: DR = pozo / ruido de lectura; SNR = S / sqrt(S + RN^2); ganancia g = pozo / (2^bits - 1); simulacion de recorte con semilla 20261109 frente a la cola normal.
Supuestos: ruido de Poisson mas lectura gaussiana; el pozo recorta de forma abrupta. Validez: ilustrativa.
Tolerancia: fraccion recortada simulada frente a la normal dentro de 4 sigma binomiales.
"""
from __future__ import annotations
import math, platform, random, sys

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    fw, rn, bits = 50000.0, 5.0, 16
    dr = fw / rn
    print(f"rango dinamico: {dr:.0f} = {20*math.log10(dr):.1f} dB = {math.log2(dr):.2f} pasos")
    g = fw / (2 ** bits - 1)
    print(f"ganancia para usar todo el ADC: {g:.4f} e-/ADU ; ruido de lectura = {rn/g:.2f} ADU")
    assert abs(20 * math.log10(dr) - 80.0) < 1e-9
    print(f"{'S [e-]':>8} {'SNR':>8} {'SNR solo Poisson':>17}")
    for s in (10, 100, 1000, 10000, 49000):
        snr = s / math.sqrt(s + rn ** 2)
        print(f"{s:8d} {snr:8.2f} {math.sqrt(s):17.2f}")
        assert snr <= math.sqrt(s)
    # recorte: media 49 800, sigma Poisson ~ 223 -> P(S > 50 000)
    rng = random.Random(20261109)
    mu, n = 49800.0, 20000
    cont = sum(1 for _ in range(n) if rng.gauss(mu, math.sqrt(mu)) > fw)
    z = (fw - mu) / math.sqrt(mu)
    p = 0.5 * math.erfc(z / math.sqrt(2))
    sig = math.sqrt(n * p * (1 - p))
    print(f"fraccion recortada: simulada {cont/n:.4f}, analitica {p:.4f} (z = {z:.3f})")
    assert abs(cont - n * p) < 4 * sig
    # nivel maximo con 1 % de recorte
    zc = 2.3263478740408408
    smax = mu_max = None
    lo, hi = 0.0, fw
    for _ in range(100):
        mid = (lo + hi) / 2
        if (fw - mid) / math.sqrt(mid) > zc:
            lo = mid
        else:
            hi = mid
    print(f"media maxima con 1 % de pixeles recortados: {lo:.0f} e-")
    assert 49000 < lo < 50000
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
