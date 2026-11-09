#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C11: probabilidad de una coincidencia fortuita en tiempo y en el cielo.

Datos: ninguna constante fisica. Contexto: GW170817 se localizo en 31 grados cuadrados (arXiv:1710.05833, resumen); la
coincidencia con GRB 170817A tuvo un retardo de 1.74 +/- 0.05 s y una probabilidad fortuita de 5e-8 (arXiv:1710.05834, resumen,
consultado 2026-11-09). La tasa de destellos (100 por anio), la ventana de +/- 5 s y los parametros del Monte Carlo son
ILUSTRATIVOS (sinteticos) y no reproducen el calculo de esa colaboracion.
Modelo: el numero de destellos independientes en una ventana de +/- T con tasa R es Poisson de media R 2T; cada uno cae dentro de
la region de localizacion con probabilidad f = A/(4 pi) (A el area); P(al menos una coincidencia) = 1 - exp(-R 2T f).
Verificacion por Monte Carlo (semilla fija) con parametros mayores para que la probabilidad sea medible.
Supuestos: destellos isotropos y estacionarios (Poisson). Validez: tasas bajas por ventana.
Tolerancia: 5 % relativo entre el Monte Carlo y la formula (p ~ 0.03, 2e5 ensayos).
"""
from __future__ import annotations
import math
import platform
import random
import sys

ANIO = 365.25 * 86400.0
CIELO_DEG2 = 4 * math.pi * (180 / math.pi) ** 2


def p_fortuita(r_anio, t_ventana_s, area_deg2):
    f = area_deg2 / CIELO_DEG2
    return 1 - math.exp(-(r_anio / ANIO) * 2 * t_ventana_s * f)


def poisson(lam, rng):
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"cielo completo = {CIELO_DEG2:.1f} grados cuadrados")
    print(f"{'R [1/anio]':>10} {'T [s]':>8} {'area [deg2]':>12} {'P fortuita':>12}")
    for r, t, a in ((100.0, 5.0, 31.0), (100.0, 5.0, 300.0), (100.0, 86400.0, 31.0), (300.0, 5.0, 31.0), (100.0, 5.0, 4800.0)):
        print(f"{r:10.0f} {t:8.0f} {a:12.0f} {p_fortuita(r, t, a):12.3e}")
    # inversion: tasa que da 5e-8 con T = 5 s y area = 31 deg2
    f = 31.0 / CIELO_DEG2
    r_inv = -math.log(1 - 5e-8) / (2 * 5.0 * f) * ANIO
    print(f"tasa que daria P = 5e-8 con T = 5 s y 31 deg2: {r_inv:.1f} por anio (ilustrativo, no es el calculo publicado)")
    # Monte Carlo con parametros mayores
    rng = random.Random(20261109)
    r, t, a = 100.0, 86400.0, 2000.0
    lam = r / ANIO * 2 * t
    f = a / CIELO_DEG2
    n = 200000
    hits = 0
    for _ in range(n):
        k = poisson(lam, rng)
        if any(rng.random() < f for _ in range(k)):
            hits += 1
    pm, pa = hits / n, p_fortuita(r, t, a)
    print(f"Monte Carlo (R = {r:.0f}/anio, T = 1 d, area = {a:.0f} deg2, {n} ensayos): P_MC = {pm:.5f} ; P formula = {pa:.5f}")
    assert abs(pm / pa - 1) < 0.05, "coincidencia fortuita"
    # eventos por anio con M busquedas
    for m in (1, 10, 100):
        print(f"{m:3d} eventos por anio con P = {p_fortuita(100.0, 5.0, 31.0):.2e}: coincidencias fortuitas esperadas por anio = {m * p_fortuita(100.0, 5.0, 31.0):.2e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
