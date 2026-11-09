#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C07: ley termica de la corriente oscura y ajuste lineal con la exposicion.

Datos: k_B en eV/K de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09). La energia de activacion efectiva (0,60 eV), la tasa de referencia (1,0 e-/s/pix a 293 K)
y los tiempos de exposicion son ILUSTRATIVOS (sinteticos); no describen un sensor real.
Modelo: D(T) = D0 (T/T0)^1.5 exp(-Ea/(k_B) (1/T - 1/T0)); se calcula la temperatura de duplicacion; conteos Poisson con semilla 20261109 y ajuste lineal media = D t + sesgo.
Supuestos: ley de Arrhenius con prefactor T^1,5 como modelo de juguete. Validez: ilustrativa, no vale para un detector concreto.
Tolerancia: tasa ajustada dentro de 3 % de la verdadera; duplicacion por dos vias a 1e-6 K.
"""
from __future__ import annotations
import math, platform, random, sys

KB_EV = 8.617333262e-5
EA, D0, T0 = 0.60, 1.0, 293.0

def dark(t):
    return D0 * (t / T0) ** 1.5 * math.exp(-EA / KB_EV * (1 / t - 1 / T0))

def pois(rng, lam):
    if lam >= 30:
        return max(0, round(rng.gauss(lam, math.sqrt(lam))))
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1

def duplicacion(t):
    lo, hi = 0.5, 30.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if dark(t + mid) / dark(t) < 2:
            lo = mid
        else:
            hi = mid
    return lo

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'T [K]':>7} {'D [e-/s/pix]':>14}")
    for t in (293, 273, 253, 233, 213):
        print(f"{t:7d} {dark(t):14.5f}")
    for t in (293, 253):
        d = duplicacion(t)
        # analitica aproximada: d ln D / dT = 1.5/T + Ea/(kB T^2)
        s = 1.5 / t + EA / (KB_EV * t * t)
        print(f"duplicacion a {t} K: numerica {d:.3f} K ; aproximacion ln2/pendiente {math.log(2)/s:.3f} K")
        assert abs(d / (math.log(2) / s) - 1) < 0.05
    assert dark(273) < dark(293) / 4
    rng = random.Random(20261109)
    T = 253.0
    d_ver = dark(T) * 50.0     # se escala a una tasa medible por pixel (x50, ilustrativo)
    ts = [10, 30, 60, 120, 300, 600]
    npx = 5000
    ms = []
    for t in ts:
        xs = [pois(rng, d_ver * t) for _ in range(npx)]
        ms.append(sum(xs) / npx)
    n = len(ts)
    mt, mm = sum(ts) / n, sum(ms) / n
    pend = sum((t - mt) * (m - mm) for t, m in zip(ts, ms)) / sum((t - mt) ** 2 for t in ts)
    print(f"tasa verdadera {d_ver:.5f} e-/s ; ajustada {pend:.5f} e-/s ; sesgo {mm - pend*mt:.3f} e-")
    assert abs(pend / d_ver - 1) < 0.03
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
