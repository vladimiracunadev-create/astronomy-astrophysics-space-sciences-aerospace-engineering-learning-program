#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C13: de valor p a sigma, factor de pruebas y combinacion de valores p independientes.

Datos: ninguna constante fisica. Contexto: la probabilidad fortuita de la coincidencia GW170817-GRB 170817A fue 5e-8
(arXiv:1710.05834, resumen) y GW150914 tuvo una tasa de falsas alarmas menor que 1 por 203 000 anios (arXiv:1602.03837, resumen,
consultados 2026-11-09). Los valores p de los ejemplos y los numeros de pruebas son ILUSTRATIVOS (sinteticos).
Modelo: sigma = Phi^-1(1 - p) (una cola), con p = 0.5 erfc(sigma/sqrt 2), invertido por biseccion; factor de pruebas
p_global = 1 - (1 - p)^N; combinacion de k valores p independientes: Fisher X = -2 Sum ln p_i ~ chi2 con 2k grados de libertad
(cola exacta de la distribucion de Erlang: P = exp(-X/2) Sum_{j<k} (X/2)^j/j!) y Stouffer Z = Sum z_i/sqrt(k).
Verificacion por Monte Carlo bajo la hipotesis nula (valores p uniformes, semilla fija): la fraccion con p_combinado < alfa debe ser alfa.
Supuestos: valores p independientes y calibrados. Validez: orientativa.
Tolerancia: 1e-12 en la inversion p <-> sigma; 5 desviaciones binomiales en las tasas Monte Carlo.
"""
from __future__ import annotations
import math
import platform
import random
import sys


def p_de_sigma(s):
    return 0.5 * math.erfc(s / math.sqrt(2))


def sigma_de_p(p):
    lo, hi = -10.0, 40.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if p_de_sigma(mid) > p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def fisher_p(ps):
    k = len(ps)
    x = -2 * sum(math.log(p) for p in ps)
    h = x / 2
    return math.exp(-h) * sum(h ** j / math.factorial(j) for j in range(k))


def stouffer_p(ps):
    z = sum(sigma_de_p(p) for p in ps) / math.sqrt(len(ps))
    return p_de_sigma(z)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'sigma':>6} {'p (una cola)':>14} {'p (dos colas)':>14} {'1 contra':>12}")
    for s in (1, 2, 3, 4, 5, 6):
        p = p_de_sigma(s)
        assert abs(sigma_de_p(p) - s) < 1e-9, "inversion p <-> sigma"
        print(f"{s:6d} {p:14.4e} {2 * p:14.4e} {1 / p:12.4e}")
    for p in (5e-8, 1 / 203000 / 1.0):
        print(f"p = {p:.3e} -> {sigma_de_p(p):.3f} sigma (una cola)")
    # factor de pruebas
    print(f"{'N':>6} {'p local':>10} {'p global':>10} {'sigma global':>13}")
    for n in (1, 10, 100, 1000):
        pl = 1e-4
        pg = 1 - (1 - pl) ** n
        print(f"{n:6d} {pl:10.1e} {pg:10.4e} {sigma_de_p(pg):13.3f}")
    # combinacion
    ps = [0.04, 0.03, 0.2]
    print(f"valores p {ps}: Fisher = {fisher_p(ps):.5f} ; Stouffer = {stouffer_p(ps):.5f} ; el menor solo = {min(ps)}")
    # comprobacion: para k = 1 Fisher y Stouffer coinciden con p
    assert abs(fisher_p([0.03]) - 0.03) < 1e-12 and abs(stouffer_p([0.03]) - 0.03) < 1e-9
    # Monte Carlo nulo
    rng = random.Random(20261109)
    n, alfa = 100000, 0.02
    cf = cs = 0
    for _ in range(n):
        q = [1 - rng.random() for _ in range(3)]
        if fisher_p(q) < alfa:
            cf += 1
        if stouffer_p(q) < alfa:
            cs += 1
    esp = n * alfa
    tol = 5 * math.sqrt(n * alfa * (1 - alfa))
    print(f"Monte Carlo nulo ({n} ensayos de k = 3): p_combinado < {alfa}: Fisher = {cf}, Stouffer = {cs} (esperados {esp:.0f} +/- {math.sqrt(esp):.0f})")
    assert abs(cf - esp) < tol and abs(cs - esp) < tol, "calibracion nula"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
