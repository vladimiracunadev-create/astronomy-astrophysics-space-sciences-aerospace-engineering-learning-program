#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C19: estadistica de conteos, significancia de una deteccion y sensibilidad.

Datos: ninguna constante fisica. Contexto de instrumento: Fermi-LAT cubre de menos de 20 MeV a mas de 300 GeV con un
campo de vision de 2.4 sr (Atwood et al., arXiv:0902.1089, resumen, consultado 2026-11-09). El fondo medio (20 cuentas
en la region de la fuente), el cociente de tiempos alpha = 0.2 y los demas numeros son ILUSTRATIVOS (sinteticos).
Modelo: N_on = S + alpha B_off-region y N_off ~ Poisson; significancia por la formula de razon de verosimilitudes
S = sqrt(2) sqrt( N_on ln[(1+a)/a N_on/(N_on+N_off)] + N_off ln[(1+a) N_off/(N_on+N_off)] ) con signo, frente a la
simple (N_on - a N_off)/sqrt(N_on + a^2 N_off). Se estima por Monte Carlo (semilla fija) la tasa de falsos positivos por
encima de 3 sigma bajo la hipotesis nula y se halla por biseccion la senal minima para 5 sigma.
Supuestos: conteos de Poisson independientes, fondo constante. Validez: orientativa.
Tolerancia: la tasa nula de la razon de verosimilitudes debe estar entre 90 y 190 casos de 100 000 (esperado ~135).
"""
from __future__ import annotations
import math
import platform
import random
import sys


def poisson(lam, rng):
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1


def lima(non, noff, a):
    if non == 0 or noff == 0:
        return 0.0
    t1 = non * math.log((1 + a) / a * non / (non + noff))
    t2 = noff * math.log((1 + a) * noff / (non + noff))
    s = math.sqrt(2 * max(t1 + t2, 0.0))
    return s if non - a * noff >= 0 else -s


def simple(non, noff, a):
    den = math.sqrt(non + a * a * noff)
    return (non - a * noff) / den if den > 0 else 0.0


def sensibilidad(b, a, objetivo):
    """Senal minima S tal que la significancia 'Asimov' (N_on = S + b, N_off = b/a) = objetivo."""
    lo, hi = 0.0, 1000.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if lima(mid + b, b / a, a) < objetivo:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    a, b = 0.2, 20.0
    n = 100000
    c_lm = c_s = 0
    for _ in range(n):
        non = poisson(b, rng)
        noff = poisson(b / a, rng)
        if lima(non, noff, a) > 3:
            c_lm += 1
        if simple(non, noff, a) > 3:
            c_s += 1
    gauss = 0.5 * math.erfc(3 / math.sqrt(2))
    print(f"hipotesis nula: fondo {b} en la region, alpha = {a}, {n} ensayos (semilla 20261109)")
    print(f"probabilidad gaussiana de > 3 sigma = {gauss:.3e} ({gauss * n:.1f} casos esperados)")
    print(f"razon de verosimilitudes: {c_lm} casos ({c_lm / n:.3e}) ; formula simple: {c_s} casos ({c_s / n:.3e})")
    assert 90 < c_lm < 190, "tasa nula de la razon de verosimilitudes"
    print(f"{'fondo B':>8} {'S minima 3 sigma':>17} {'S minima 5 sigma':>17} {'S/sqrt(B) a 5 sigma':>20}")
    for bb in (1.0, 5.0, 20.0, 100.0, 1000.0):
        s3, s5 = sensibilidad(bb, a, 3.0), sensibilidad(bb, a, 5.0)
        print(f"{bb:8.0f} {s3:17.3f} {s5:17.3f} {s5 / math.sqrt(bb):20.3f}")
    # significancia de ejemplos
    for non, noff in ((30, 100), (45, 100), (60, 100)):
        print(f"N_on = {non}, N_off = {noff}, alpha = {a}: Li-Ma = {lima(non, noff, a):.3f} ; simple = {simple(non, noff, a):.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
