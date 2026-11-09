#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C05: modelo de costo-perdida para decidir una alerta, puntuacion de Brier y fiabilidad de pronosticos probabilisticos.

Datos: ninguna constante fisica. El costo de protegerse (C = 1), la perdida evitable (L = 10), las probabilidades pronosticadas (calibradas, uniformes en [0, 0.6]), los 20 000 casos y la semilla
fija son ILUSTRATIVOS (sinteticos); no se estiman costos de ningun sector real.
Modelo: el usuario protege si p > C/L; gasto esperado por caso = C si protege, p L si no; gasto de referencia (nunca proteger = p_clim L, siempre proteger = C); puntuacion de Brier BS = media (p - o)^2,
con el valor esperado para pronosticos calibrados media p(1 - p); diagrama de fiabilidad por 6 intervalos.
Supuestos: pronosticos calibrados, costos fijos. Validez: ilustrativa.
Tolerancia: BS simulado dentro de 4 errores estandar del esperado; frecuencia observada por intervalo dentro de 4 errores estandar de la probabilidad media del intervalo.
"""
from __future__ import annotations
import math, platform, random, sys

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    c, l, n = 1.0, 10.0, 20000
    rng = random.Random(20261109)
    ps = [0.6 * rng.random() for _ in range(n)]
    obs = [1 if rng.random() < p else 0 for p in ps]
    clim = sum(obs) / n
    umbral = c / l
    gasto = sum(c if p > umbral else (l if o else 0.0) for p, o in zip(ps, obs)) / n
    nunca = sum(l if o else 0.0 for o in obs) / n
    siempre = c
    optimo_clim = min(nunca, siempre)
    print(f"umbral de decision p > C/L = {umbral:.2f} ; frecuencia climatologica = {clim:.4f}")
    print(f"gasto medio por caso: con pronostico = {gasto:.4f} ; nunca proteger = {nunca:.4f} ; siempre proteger = {siempre:.4f} ; mejor referencia = {optimo_clim:.4f}")
    print(f"ahorro relativo respecto de la mejor referencia = {(1 - gasto / optimo_clim) * 100:.1f} %")
    assert gasto < optimo_clim
    bs = sum((p - o) ** 2 for p, o in zip(ps, obs)) / n
    esp = sum(p * (1 - p) for p in ps) / n
    err = math.sqrt(sum((p * (1 - p)) * (1 - 2 * p) ** 2 + p * (1 - p) * 0 for p in ps) / n ** 2 + 1e-12)
    errb = math.sqrt(sum(((1 - 2 * p) ** 2 * p * (1 - p)) for p in ps)) / n
    print(f"Brier simulado = {bs:.5f} ; esperado para pronosticos calibrados = {esp:.5f} ; error estandar = {errb:.5f}")
    assert abs(bs - esp) < 4 * errb
    print(f"{'intervalo':>11} {'casos':>6} {'p media':>8} {'frecuencia':>11} {'desviacion [errores]':>21}")
    for k in range(6):
        lo, hi = 0.1 * k, 0.1 * (k + 1)
        idx = [i for i, p in enumerate(ps) if lo <= p < hi]
        pm = sum(ps[i] for i in idx) / len(idx)
        fr = sum(obs[i] for i in idx) / len(idx)
        e = math.sqrt(pm * (1 - pm) / len(idx))
        print(f"{lo:4.1f}-{hi:4.1f} {len(idx):6d} {pm:8.4f} {fr:11.4f} {abs(fr - pm) / e:21.2f}")
        assert abs(fr - pm) < 4 * e
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
