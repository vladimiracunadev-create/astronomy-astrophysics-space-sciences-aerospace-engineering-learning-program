#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B02-C09: cuántas "alineaciones" aparecen por azar.

Datos: SINTÉTICOS (orientaciones aleatorias uniformes; ningún sitio real).
Modelo: cada estructura apunta a un azimut uniforme en [0°, 360°); hay K direcciones
"de interés" (ventanas de ±tol grados que no se solapan). Hipótesis nula = distribución
uniforme, como en los análisis de orientaciones (Muratore et al. 2023, arXiv:2311.02134).
Referencia analítica: probabilidad por estructura p = K·2·tol/360; número de aciertos
~ Binomial(N, p). Validez: ventanas disjuntas; no usa horizontes reales.
Tolerancia: la simulación debe coincidir con la fórmula dentro de 3 desviaciones típicas.
"""

from __future__ import annotations

import math
import random
import sys


def p_acierto(k: int, tol: float) -> float:
    return k * 2.0 * tol / 360.0


def prob_binomial_al_menos(n: int, p: float, m: int) -> float:
    return 1.0 - sum(math.comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(m))


def simular(n: int, k: int, tol: float, ensayos: int, semilla: int) -> tuple[float, float]:
    rng = random.Random(semilla)
    centros = [(360.0 / k) * i for i in range(k)]           # ventanas disjuntas y equiespaciadas
    aciertos_total = 0
    con_alguno = 0
    for _ in range(ensayos):
        h = 0
        for _ in range(n):
            az = rng.uniform(0.0, 360.0)
            if any(min(abs(az - c), 360.0 - abs(az - c)) <= tol for c in centros):
                h += 1
        aciertos_total += h
        con_alguno += h > 0
    return aciertos_total / (ensayos * n), con_alguno / ensayos


def pruebas() -> None:
    assert abs(p_acierto(1, 1.0) - 2.0 / 360.0) < 1e-12
    assert abs(prob_binomial_al_menos(10, 0.5, 0) - 1.0) < 1e-12        # al menos 0 = 1
    assert abs(prob_binomial_al_menos(1, 0.3, 1) - 0.3) < 1e-12
    n, k, tol, ens = 40, 6, 2.0, 4000
    p = p_acierto(k, tol)
    p_sim, _ = simular(n, k, tol, ens, 12345)
    sigma = math.sqrt(p * (1 - p) / (n * ens))
    assert abs(p_sim - p) < 3 * sigma, (p_sim, p, sigma)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    n, k, tol = 40, 6, 2.0
    p = p_acierto(k, tol)
    print(f"{n} estructuras SINTÉTICAS, {k} direcciones de interés, tolerancia ±{tol}°")
    print(f"Probabilidad de acierto por estructura: p = {p:.4f} ({100 * p:.1f} %)")
    print(f"Aciertos esperados por azar: {n * p:.2f}")
    print(f"P(al menos 1 acierto) = {prob_binomial_al_menos(n, p, 1):.4f}")
    print(f"P(al menos 4 aciertos) = {prob_binomial_al_menos(n, p, 4):.4f}")
    p_sim, alguno = simular(n, k, tol, 20000, 2026)
    print(f"Simulación (20 000 ensayos, semilla 2026): p = {p_sim:.4f}; ensayos con ≥1 acierto: {alguno:.4f}")
    for kk in (1, 6, 12, 24):
        print(f"  K = {kk:2d}: p = {p_acierto(kk, tol):.4f}; P(≥1 acierto en {n}) = {prob_binomial_al_menos(n, p_acierto(kk, tol), 1):.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
