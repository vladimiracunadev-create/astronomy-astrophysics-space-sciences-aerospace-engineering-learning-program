#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C09: ganancia por cascada (registro de multiplicacion) y factor de ruido en exceso.

Datos: ninguna constante fisica. El numero de etapas (40) y la probabilidad por etapa (0,05) son ILUSTRATIVOS (sinteticos); un EMCCD real usa cientos de etapas con p menor.
Modelo: en cada etapa cada electron produce un electron extra con probabilidad p (proceso de ramificacion). Ganancia media g = (1+p)^N. Para un electron de entrada, la varianza de salida es
p(1-p) m^(N-1) (m^N - 1)/(m-1) con m = 1+p; factor de ruido en exceso F^2 = 1 + Var/g^2 (limite 2 para g grande). Simulacion con semilla 20261109.
Supuestos: etapas independientes, sin saturacion ni ruido de reloj. Validez: ilustrativa.
Tolerancia: media simulada dentro de 4 errores estandar y F^2 simulado dentro de 3 % del valor analitico.
"""
from __future__ import annotations
import math, platform, random, sys

N, P = 40, 0.05

def cascada(rng, n0):
    n = n0
    for _ in range(N):
        n += sum(1 for _ in range(n) if rng.random() < P)
    return n

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m = 1 + P
    g = m ** N
    var = P * (1 - P) * m ** (N - 1) * (m ** N - 1) / (m - 1)
    f2 = 1 + var / g ** 2
    print(f"N = {N}, p = {P}: ganancia analitica g = {g:.4f} ; varianza = {var:.3f} ; F^2 = {f2:.4f}")
    rng = random.Random(20261109)
    trials = 20000
    xs = [cascada(rng, 1) for _ in range(trials)]
    mu = sum(xs) / trials
    v = sum((x - mu) ** 2 for x in xs) / (trials - 1)
    f2s = 1 + v / mu ** 2
    print(f"simulacion ({trials} entradas de 1 e-): g = {mu:.4f} ; varianza = {v:.3f} ; F^2 = {f2s:.4f}")
    assert abs(mu - g) < 4 * math.sqrt(v / trials)
    assert abs(f2s / f2 - 1) < 0.03
    print(f"{'N':>5} {'g':>12} {'F^2':>8}")
    for n in (10, 40, 100, 400, 600):
        pp = 0.0147
        mm = 1 + pp
        gg = mm ** n
        vv = pp * (1 - pp) * mm ** (n - 1) * (mm ** n - 1) / (mm - 1)
        print(f"{n:5d} {gg:12.2f} {1 + vv/gg**2:8.4f}")
    gg = (1.0147) ** 600
    f600 = 1 + (0.0147 * (1 - 0.0147) * 1.0147 ** 599 * (1.0147 ** 600 - 1) / 0.0147) / gg ** 2
    assert 1.9 < f600 < 2.0
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
