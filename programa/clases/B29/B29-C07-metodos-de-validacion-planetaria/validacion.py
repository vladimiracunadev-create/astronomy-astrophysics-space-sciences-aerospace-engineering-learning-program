#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C07: probabilidad bayesiana de falso positivo y su calibracion por simulacion.

Datos: ninguna constante fisica. Contexto: Morton propone un procedimiento general para calcular la probabilidad de falso positivo de un candidato a
partir de su periodo, profundidad, duracion y forma, de los colores de la estrella y de observaciones de seguimiento; en su momento Kepler tenia mas de 2300
candidatos y solo 77 planetas confirmados (arXiv:1206.1568, resumen, consultado 2026-11-09). Las frecuencias a priori (planeta 0.30, binaria de fondo 0.40,
binaria jerarquica 0.30) y las distribuciones del observable (un cociente de ingreso a duracion) por escenario son ILUSTRATIVAS (sinteticas).
Modelo: tres escenarios s con prior pi_s y observable x ~ Normal(mu_s, sigma_s); probabilidad posterior P(s | x) = pi_s N(x; mu_s, sigma_s)/Sum pi N.
Calibracion: se simulan 200000 candidatos (semilla fija) con la verdad extraida de los priors y se comprueba que, entre los que reciben una probabilidad de planeta
en un intervalo, la fraccion que realmente son planetas coincide con la probabilidad media del intervalo.
Supuestos: observable unico y modelos conocidos. Validez: ilustrativa.
Tolerancia: diferencia absoluta entre fraccion real y probabilidad media menor que 0.015 en cada intervalo con mas de 1000 candidatos.
"""
from __future__ import annotations
import math
import platform
import random
import sys

ESC = {"planeta": (0.30, 0.10, 0.05), "binaria de fondo": (0.40, 0.40, 0.20), "binaria jerarquica": (0.30, 0.25, 0.10)}


def pdf(x, mu, sg):
    return math.exp(-0.5 * ((x - mu) / sg) ** 2) / (sg * math.sqrt(2 * math.pi))


def posterior(x):
    pesos = {s: pi * pdf(x, mu, sg) for s, (pi, mu, sg) in ESC.items()}
    tot = sum(pesos.values())
    return {s: w / tot for s, w in pesos.items()}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'x':>6} {'P(planeta)':>11} {'P(BEB)':>8} {'P(HEB)':>8} {'FPP':>7}")
    for x in (0.02, 0.10, 0.15, 0.20, 0.30, 0.50):
        p = posterior(x)
        print(f"{x:6.2f} {p['planeta']:11.4f} {p['binaria de fondo']:8.4f} {p['binaria jerarquica']:8.4f} {1 - p['planeta']:7.4f}")
    rng = random.Random(20261109)
    n = 200000
    nombres = list(ESC)
    cumul = [ESC[s][0] for s in nombres]
    filas = []
    for _ in range(n):
        r = rng.random()
        acc = 0.0
        for s, pi in zip(nombres, cumul):
            acc += pi
            if r <= acc:
                break
        _, mu, sg = ESC[s]
        x = rng.gauss(mu, sg)
        filas.append((posterior(x)["planeta"], s == "planeta"))
    bordes = [0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99, 1.0001]
    print(f"{'intervalo P(planeta)':>22} {'n':>7} {'P media':>9} {'fraccion real':>14} {'dif.':>7}")
    for lo, hi in zip(bordes[:-1], bordes[1:]):
        sel = [(p, es) for p, es in filas if lo <= p < hi]
        if len(sel) < 1000:
            print(f"[{lo:4.2f}, {min(hi, 1):4.2f})   {len(sel):7d}  (pocos candidatos)")
            continue
        pm = sum(p for p, _ in sel) / len(sel)
        fr = sum(1 for _, es in sel if es) / len(sel)
        assert abs(pm - fr) < 0.015, f"calibracion en [{lo}, {hi})"
        print(f"[{lo:4.2f}, {min(hi, 1):4.2f}) {'':>9} {len(sel):7d} {pm:9.4f} {fr:14.4f} {pm - fr:7.4f}")
    # prior global
    fr_pl = sum(1 for _, es in filas if es) / n
    pm_pl = sum(p for p, _ in filas) / n
    print(f"fraccion de planetas en la poblacion simulada = {fr_pl:.4f} ; P(planeta) media = {pm_pl:.4f} ; prior = 0.3000")
    assert abs(fr_pl - 0.30) < 0.005 and abs(pm_pl - fr_pl) < 0.005
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
