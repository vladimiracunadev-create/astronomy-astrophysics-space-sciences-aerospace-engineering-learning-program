#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C20: significancia estadistica, efecto de mirar en muchos lugares y actualizacion bayesiana.

Datos: ninguna constante fisica. Los numeros de zonas independientes (1, 10, 100, 1000), las probabilidades a priori (1e-3 a 1e-9), los factores de Bayes (10 a 1e9) y la semilla fija de la
simulacion (20 000 experimentos) son ILUSTRATIVOS (sinteticos); ninguna afirmacion real se evalua.
Modelo: p local unilateral p = (1/2) erfc(z/sqrt(2)) y su inversa por biseccion; p global = 1 - (1 - p)^N para N zonas independientes y su significancia equivalente; Monte Carlo del maximo
de N variables normales; posterior bayesiano P(H|datos) = BF prior/(1 - prior + BF prior) y factor de Bayes necesario para alcanzar una probabilidad posterior dada.
Supuestos: zonas independientes y gaussianas bajo la hipotesis nula, un unico factor de Bayes. Validez: ilustrativa.
Tolerancia: p global por Monte Carlo dentro de 4 errores estandar de la formula; inversa de p dentro de 1e-9 en z.
"""
from __future__ import annotations
import math
import platform
import random
import sys


def p_local(z):
    return 0.5 * math.erfc(z / math.sqrt(2))


def z_de_p(p):
    lo, hi = -10.0, 40.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if p_local(mid) > p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'z':>4} {'p local (unilateral)':>22} {'1 en':>14}")
    for z in (1, 2, 3, 4, 5):
        p = p_local(z)
        print(f"{z:4d} {p:22.4e} {1 / p:14.1f}")
        assert abs(z_de_p(p) - z) < 1e-9
    print(f"{'N zonas':>8} {'p global de un 3 sigma local':>30} {'significancia global [sigma]':>30} {'p global de un 5 sigma':>24}")
    for n in (1, 10, 100, 1000):
        pg = 1 - (1 - p_local(3)) ** n
        pg5 = 1 - (1 - p_local(5)) ** n
        print(f"{n:8d} {pg:30.5f} {z_de_p(pg):30.3f} {pg5:24.4e}")
    # Monte Carlo
    rng = random.Random(20261109)
    n, reps = 100, 20000
    cuenta = sum(1 for _ in range(reps) if max(rng.gauss(0, 1) for _ in range(n)) > 3)
    pg = 1 - (1 - p_local(3)) ** n
    err = math.sqrt(pg * (1 - pg) / reps)
    print(f"Monte Carlo con N = {n}: fraccion con maximo > 3 sigma = {cuenta / reps:.5f} ; formula = {pg:.5f} ; desviacion = {abs(cuenta / reps - pg) / err:.2f} errores")
    assert abs(cuenta / reps - pg) < 4 * err
    # bayes
    print(f"{'prior':>8}" + "".join(f"{('BF = ' + format(bf, '.0e')):>14}" for bf in (10, 1e3, 1e6, 1e9)))
    for prior in (1e-3, 1e-6, 1e-9):
        fila = [bf * prior / (1 - prior + bf * prior) for bf in (10, 1e3, 1e6, 1e9)]
        print(f"{prior:8.0e}" + "".join(f"{x:14.4e}" for x in fila))
    for prior in (1e-3, 1e-6, 1e-9):
        bf_necesario = (1 - prior) / prior                     # para P(H|datos) = 1/2
        print(f"prior {prior:.0e}: factor de Bayes para llegar a 50 %: {bf_necesario:.3e}")
        assert abs(bf_necesario * prior / (1 - prior + bf_necesario * prior) - 0.5) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
