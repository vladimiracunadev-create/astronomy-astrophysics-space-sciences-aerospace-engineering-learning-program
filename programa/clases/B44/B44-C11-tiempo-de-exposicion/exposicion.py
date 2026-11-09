#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C11: relacion senal-ruido frente al tiempo de exposicion y exposicion minima limitada por el cielo.

Datos: ninguna constante fisica. Tasa de la fuente (20 e-/s), cielo (2 e-/s/pix), corriente oscura (0,1 e-/s/pix), ruido de lectura (6 e-), apertura de 20 pixeles y
tiempo total de 3600 s son ILUSTRATIVOS (sinteticos); no corresponden a ninguna observacion.
Modelo: SNR(t) = S t / sqrt(S t + n (B t + D t + RN^2)); con N cuadros de duracion t = T/N, SNR_total = sqrt(N) SNR(t). Exposicion minima limitada por el cielo: (B + D) t = k RN^2 (k = 10).
Verificacion Monte Carlo (semilla 20261109) con ruido gaussiano equivalente.
Supuestos: ruidos independientes y gaussianos; sin saturacion. Validez: ilustrativa.
Tolerancia: SNR simulada dentro de 3 % de la analitica.
"""
from __future__ import annotations
import math, platform, random, sys

S, B, D, RN, NPIX, TTOT = 20.0, 2.0, 0.1, 6.0, 20, 3600.0

def snr(t):
    return S * t / math.sqrt(S * t + NPIX * ((B + D) * t + RN ** 2))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'t [s]':>7} {'N cuadros':>10} {'SNR 1 cuadro':>13} {'SNR total':>10}")
    res = {}
    for t in (10, 30, 100, 300, 1000, 3600):
        n = TTOT / t
        tot = math.sqrt(n) * snr(t)
        res[t] = tot
        print(f"{t:7d} {n:10.1f} {snr(t):13.3f} {tot:10.3f}")
    assert res[10] < res[100] < res[3600]
    tmin = 10 * RN ** 2 / (B + D)
    print(f"exposicion minima limitada por el cielo (k = 10): {tmin:.1f} s")
    # a esa exposicion la penalizacion frente a un unico cuadro largo
    n = TTOT / tmin
    pen = math.sqrt(n) * snr(tmin) / snr(TTOT)
    print(f"con t = {tmin:.0f} s: SNR total {math.sqrt(n)*snr(tmin):.3f} frente a {snr(TTOT):.3f} (cociente {pen:.4f})")
    assert 0.95 < pen < 1.0
    # Monte Carlo en un cuadro de 100 s
    rng = random.Random(20261109)
    t, m = 100.0, 40000
    xs = []
    for _ in range(m):
        senal = rng.gauss(S * t, math.sqrt(S * t))
        fondo = sum(rng.gauss((B + D) * t, math.sqrt((B + D) * t)) + rng.gauss(0, RN) for _ in range(NPIX))
        xs.append(senal + fondo - NPIX * (B + D) * t)
    mu = sum(xs) / m
    sd = math.sqrt(sum((x - mu) ** 2 for x in xs) / (m - 1))
    print(f"Monte Carlo (t = 100 s): SNR simulada {mu/sd:.3f} ; analitica {snr(t):.3f}")
    assert abs(mu / sd / snr(t) - 1) < 0.03
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
