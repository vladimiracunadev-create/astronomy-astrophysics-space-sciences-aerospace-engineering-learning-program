#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B111-C05: decision en equipo bajo incertidumbre (modelos SINTETICOS).

(a) Votacion mayoritaria: n miembros acierta cada uno con probabilidad p. Independientes: exactitud binomial.
    Correlacionados: con probabilidad rho todos adoptan la opinion de una senal comun (que acierta con prob p) y con
    1 - rho votan independientemente; P_grupo = rho * p + (1 - rho) * P_binomial. Segunda via: Monte Carlo (semilla 115,
    100000 decisiones); tolerancia 0.006. n impar para evitar empates.
(b) Actualizacion bayesiana: prior de falla P0 = 0.10; dos informes independientes con sensibilidad 0.90 y falsa alarma 0.20.
    Posterior tras informes positivos y tras uno positivo y uno negativo.
(c) Utilidad esperada go/no-go: beneficio B = 100 si se procede y no hay falla, costo C = 400 si se procede y hay falla,
    0 si no se procede (unidades arbitrarias SINTETICAS). Se procede si p_falla < B/(B + C) = 0.20.
Supuestos: informes y votos ilustrativos; no se modelan sesgos de la psicologia de la decision (p. ej. teoria de las
perspectivas, Kahneman y Tversky 1979, solo metadatos consultados), ni jerarquia ni presion de tiempo.
"""
from __future__ import annotations
import math, platform, random


def binomial_mayoria(n, p):
    k0 = n // 2 + 1
    return sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(k0, n + 1))


def grupo(n, p, rho):
    return rho * p + (1 - rho) * binomial_mayoria(n, p)


def montecarlo(n, p, rho, rng, m=100000):
    ok = 0
    for _ in range(m):
        if rng.random() < rho:
            ok += rng.random() < p
        else:
            ok += sum(rng.random() < p for _ in range(n)) > n // 2
    return ok / m


def posterior(prior, sens, fa, positivo):
    l1 = sens if positivo else 1 - sens
    l0 = fa if positivo else 1 - fa
    return prior * l1 / (prior * l1 + (1 - prior) * l0)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(115)
    print("Votacion mayoritaria (SINTETICA), p = 0.70 por miembro")
    print("  n   rho   exactitud analitica   Monte Carlo   diferencia")
    dmax = 0.0
    for n in (1, 3, 5, 9):
        for rho in (0.0, 0.5, 1.0):
            a, m = grupo(n, 0.70, rho), montecarlo(n, 0.70, rho, rng)
            dmax = max(dmax, abs(a - m))
            print(f"  {n:d}  {rho:4.1f}  {a:19.4f}  {m:12.4f}  {abs(a - m):10.5f}")
    print(f"Diferencia maxima = {dmax:.5f}")
    p1 = posterior(0.10, 0.90, 0.20, True)
    p2 = posterior(p1, 0.90, 0.20, True)
    p3 = posterior(p1, 0.90, 0.20, False)
    print(f"Bayes: prior = 0.1000 ; tras 1 informe positivo = {p1:.4f} ; tras 2 positivos = {p2:.4f} ; tras positivo y negativo = {p3:.4f}")
    umbral = 100.0 / (100.0 + 400.0)
    print(f"Umbral de decision p* = B/(B+C) = {umbral:.4f}")
    for pf in (0.10, p1, p2, p3):
        eu = (1 - pf) * 100.0 - pf * 400.0
        print(f"  p_falla = {pf:.4f}  utilidad esperada de proceder = {eu:8.3f}  decision: {'proceder' if eu > 0 else 'no proceder'}")
    assert dmax < 0.006
    assert abs(grupo(3, 0.7, 0.0) - (3 * 0.49 * 0.3 + 0.343)) < 1e-12
    assert grupo(9, 0.7, 1.0) == 0.7 and grupo(9, 0.7, 0.0) > grupo(9, 0.7, 0.5) > 0.7
    assert abs((1 - umbral) * 100 - umbral * 400) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
