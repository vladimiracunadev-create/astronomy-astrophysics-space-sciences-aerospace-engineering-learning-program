#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C13: relacion periodo-luminosidad con cefeidas SINTETICAS y escala de pulsacion.

Datos: ninguno observado. Muestra de 60 "cefeidas" SINTETICAS: M = a + b (log10 P - 1) con
a = -4.0, b = -2.5, dispersion 0.15 mag, a un modulo de distancia verdadero mu = 18.50 mag
(valores ilustrativos, no la calibracion de ninguna publicacion). GM_sol, R_sol nominales
(IAU 2015 B3) para la escala dinamica.
Modelo: m = M + mu; ajuste lineal por minimos cuadrados m = A + b log10 P; mu = A - a - ... se
recupera con a conocido (calibracion externa). Distancia d = 10^((mu+5)/5) pc. Escala de
pulsacion: P ~ 2 pi sqrt(R^3 / G M).
Supuestos: sin extincion, sin dispersion intrinseca de la franja de inestabilidad mas alla de la
declarada. Validez: ilustrativa. Tolerancia: 1e-9 sin ruido; 3 sigma con ruido (semilla fija).
"""
from __future__ import annotations
import math
import platform
import random
import sys

GM_SOL, R_SOL = 1.3271244e20, 6.957e8
A_VERD, B_VERD, MU_VERD, SIG = -4.0, -2.5, 18.50, 0.15


def ajuste(x, y):
    n = len(x)
    sx, sy = sum(x), sum(y)
    sxx = sum(v * v for v in x)
    sxy = sum(a * b for a, b in zip(x, y))
    d = n * sxx - sx * sx
    b = (n * sxy - sx * sy) / d
    a = (sy - b * sx) / n
    return a, b


def errores(x, y, a, b):
    n = len(x)
    res = [yi - (a + b * xi) for xi, yi in zip(x, y)]
    s2 = sum(r * r for r in res) / (n - 2)
    xm = sum(x) / n
    sxx = sum((xi - xm) ** 2 for xi in x)
    return math.sqrt(s2 / sxx), math.sqrt(s2 * (1 / n + xm * xm / sxx)), math.sqrt(s2)


def muestra(n, ruido, rng):
    lp = [rng.uniform(0.4, 1.8) for _ in range(n)]          # log10 P, P de 2.5 a 63 d
    m = [A_VERD + B_VERD * (v - 1) + MU_VERD + (rng.gauss(0, SIG) if ruido else 0.0) for v in lp]
    return lp, m


def distancia_pc(mu):
    return 10 ** ((mu + 5) / 5)


def periodo_dinamico_d(M_sol, R_sol):
    return 2 * math.pi * math.sqrt((R_sol * R_SOL) ** 3 / (GM_SOL * M_sol)) / 86400.0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(13)
    lp, m = muestra(60, False, rng)
    a, b = ajuste(lp, m)
    assert abs(b - B_VERD) < 1e-9 and abs(a - (A_VERD - B_VERD + MU_VERD)) < 1e-9, "sin ruido debe ser exacto"
    lp, m = muestra(60, True, rng)
    a, b = ajuste(lp, m)
    sb, sa, s = errores(lp, m, a, b)
    mu_rec = a + b * 1.0 - A_VERD  # m(logP=1) = a + b*1 ; M(logP=1) = A_VERD
    assert abs(b - B_VERD) < 3 * sb, "pendiente fuera de 3 sigma"
    assert abs(mu_rec - MU_VERD) < 3 * math.sqrt(sa ** 2 + 0.0) + 0.05
    print(f"pendiente recuperada = {b:.3f} +/- {sb:.3f} (verdadera {B_VERD})")
    print(f"dispersion residual = {s:.3f} mag (inyectada {SIG})")
    print(f"mu recuperado = {mu_rec:.3f} mag (verdadero {MU_VERD}) -> d = {distancia_pc(mu_rec) / 1e3:.2f} kpc "
          f"(verdadera {distancia_pc(MU_VERD) / 1e3:.2f} kpc)")
    print(f"periodo dinamico Sol = {periodo_dinamico_d(1, 1) * 24:.2f} h ; "
          f"(M=5, R=50) = {periodo_dinamico_d(5, 50):.1f} d")
    assert abs(periodo_dinamico_d(4, 1) / periodo_dinamico_d(1, 1) - 0.5) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
