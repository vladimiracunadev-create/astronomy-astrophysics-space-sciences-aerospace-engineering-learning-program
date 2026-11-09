#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C12: propagacion de errores en la escalera de distancias y sesgo de 1/paralaje.

Datos: Riess et al. (2019, arXiv:1903.07603, resumen, consultado 2026-11-09): distancia a la LMC con 1.2 %
de precision, incertidumbre total de la escalera 2.5 % -> 1.3 %, H0 = 74.22 +/- 1.82 km/s/Mpc (solo LMC).
Los errores en magnitudes de los demas peldanos (0.03 y 0.04 mag) y el paralaje sintetico (10 +/- 1 mas)
son valores ILUSTRATIVOS (sinteticos).
Modelo: una distancia d = d0 * 10^{0.2 (dmu1 + dmu2)}; el error fraccional de un peldano con error de
modulo sigma_mu es (ln 10 / 5) sigma_mu. En cuadratura: (sigma_d/d)^2 = suma de cuadrados. Monte Carlo con
1e5 muestras como comprobacion independiente. Para el paralaje: d = 1/p con p gaussiana tiene sesgo.
Supuestos: errores independientes y gaussianos. Validez: errores fraccionales pequenos.
Tolerancia: 2 % relativa entre Monte Carlo y cuadratura (semilla fija).
"""
from __future__ import annotations
import math
import platform
import random
import sys

LN10_5 = math.log(10) / 5


def frac(sig_mag):
    return LN10_5 * sig_mag


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    pasos = [("distancia LMC (1.2 %)", 0.012), ("peldano 2 (0.03 mag)", frac(0.03)), ("peldano 3 (0.04 mag)", frac(0.04))]
    ana = math.sqrt(sum(s * s for _, s in pasos))
    for n, s in pasos:
        print(f"{n:28s}: error fraccional = {100 * s:.2f} %")
    print(f"cuadratura: error total = {100 * ana:.3f} %")
    rng = random.Random(12)
    N = 100000
    muestras = []
    for _ in range(N):
        d = 1.0
        d *= 1 + rng.gauss(0, 0.012)
        d *= 10 ** (0.2 * rng.gauss(0, 0.03))
        d *= 10 ** (0.2 * rng.gauss(0, 0.04))
        muestras.append(d)
    m = sum(muestras) / N
    sd = math.sqrt(sum((x - m) ** 2 for x in muestras) / (N - 1))
    print(f"Monte Carlo ({N} muestras): media = {m:.5f} ; desviacion = {100 * sd / m:.3f} %")
    assert abs(sd / m / ana - 1) < 0.02, "Monte Carlo y cuadratura difieren > 2 %"
    # paralaje 10 +/- 1 mas: d = 1/p
    ps = [rng.gauss(10.0, 1.0) for _ in range(N)]
    ds = [1000.0 / p for p in ps if p > 0]
    md = sum(ds) / len(ds)
    print(f"paralaje 10 +/- 1 mas: media de 1/p = {md:.3f} pc ; valor nominal 100 pc ; sesgo = {100 * (md / 100 - 1):+.2f} %")
    assert md > 100.0, "1/p debe sesgar al alza"
    # H0 de la LMC
    h0, e = 74.22, 1.82
    print(f"Riess et al. 2019 (solo LMC): H0 = {h0} +/- {e} -> precision {100 * e / h0:.2f} %")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
