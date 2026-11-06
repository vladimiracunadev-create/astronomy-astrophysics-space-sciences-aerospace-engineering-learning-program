#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C15: relacion senal-ruido de un detector CCD.

Datos: ruido de lectura R = 3.0 e- rms y ganancia 1.6 e-/DN, del orden de los
valores del canal UVIS de la camara WFC3 del telescopio espacial Hubble (STScI,
Instrument Handbook sec. 5.4: lectura 2.90-3.01 e- por amplificador en 2009;
ganancia 1.584-1.615 e-/DN en sept. 2025; pozo maximo ~72 400 e-; consultado
2026-11-05). Cielo B = 0.50 e-/s/pix, oscuro D = 0.002 e-/s/pix, apertura de
25 pixeles y tiempo t = 600 s son valores SINTETICOS de ejemplo.
Modelo (ecuacion del CCD): con N e- de senal en la apertura,
  SNR = N / sqrt(N + npix (B + D) t + npix R^2).
Inversion cerrada para SNR objetivo q: N^2 - q^2 N - q^2 V = 0,
  N = (q^2 + sqrt(q^4 + 4 q^2 V)) / 2, V = npix ((B + D) t + R^2).
Supuestos: ruido de disparo de Poisson, lectura gaussiana, sin ruido de
patron fijo ni cuantizacion relevante. Validez: N, V > 0.
Tolerancia: identidades 1e-12; Monte Carlo (numpy, 2e5 ensayos) dentro del 1.5 %.
"""
from __future__ import annotations
import math
import platform
import sys

import numpy as np

R, GAIN = 3.0, 1.6
B, D = 0.50, 0.002
NPIX, T = 25, 600.0


def snr(N, npix=NPIX, b=B, d=D, t=T, r=R):
    return N / math.sqrt(N + npix * (b + d) * t + npix * r * r)


def senal_para(q, npix=NPIX, b=B, d=D, t=T, r=R):
    v = npix * ((b + d) * t + r * r)
    return 0.5 * (q * q + math.sqrt(q ** 4 + 4 * q * q * v))


def main() -> None:
    print(f"Python {platform.python_version()}, numpy {np.__version__}")
    # Limite de Poisson: sin fondo, oscuro ni lectura -> SNR = sqrt(N)
    assert abs(snr(10000.0, b=0, d=0, r=0) - 100.0) < 1e-12
    # Limite de lectura: N pequeno, sin fondo -> SNR ~ N/(sqrt(npix) R)
    lim = snr(5.0, npix=1, b=0, d=0, r=30.0)
    assert abs(lim - 5.0 / 30.0) / (5.0 / 30.0) < 0.005
    # Inversion cerrada
    for q in (3.0, 5.0, 10.0, 50.0):
        N = senal_para(q)
        assert abs(snr(N) - q) < 1e-9
        print(f"SNR = {q:5.1f}: N = {N:9.1f} e- = {N/GAIN:8.1f} DN = {N/T:7.3f} e-/s")
    # Terminos de ruido en N = 1000 e-
    N = 1000.0
    disparo, cielo, oscuro, lectura = N, NPIX * B * T, NPIX * D * T, NPIX * R * R
    tot = disparo + cielo + oscuro + lectura
    print(f"N = 1000 e-: varianza total {tot:.0f} e-^2 = disparo {disparo:.0f} + cielo {cielo:.0f} + oscuro {oscuro:.0f} + lectura {lectura:.0f}")
    print(f"SNR = {snr(N):.3f}")
    # Cuantizacion: sigma = g/sqrt(12)
    print(f"ruido de cuantizacion = {GAIN/math.sqrt(12):.3f} e- (frente a R = {R} e-)")
    # Monte Carlo
    rng = np.random.default_rng(1)
    M = 200000
    senal = rng.poisson(N, M)
    fondo = rng.poisson(NPIX * (B + D) * T, M)
    lect = rng.normal(0.0, R * math.sqrt(NPIX), M)
    medido = senal + fondo + lect - NPIX * (B + D) * T
    snr_mc = medido.mean() / medido.std()
    print(f"Monte Carlo: SNR = {snr_mc:.3f} (formula {snr(N):.3f})")
    assert abs(snr_mc - snr(N)) / snr(N) < 0.015
    # Saturacion: tiempo maximo para una fuente puntual con 20 % del flujo en el pixel central
    tasa_pico = 80.0            # e-/s en el pixel central (sintetico)
    print(f"tiempo hasta saturar 72 400 e-: {72400 / (tasa_pico + B + D):.0f} s (tasa pico {tasa_pico} e-/s)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
