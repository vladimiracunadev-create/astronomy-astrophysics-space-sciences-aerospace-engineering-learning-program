#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C11: oscilacion de neutrinos de dos sabores en el vacio.

Datos: hbar c = 197.326 980 4 MeV fm = 1.973 269 804e-7 eV m, e y c (NIST CODATA 2022), consultados 2026-11-09. El angulo de mezcla (45 grados, sen^2 2 theta = 1), la diferencia de
masas al cuadrado (2.5e-3 eV^2), las energias (0.5 a 2 GeV), las distancias y el numero de neutrinos (100 000, semilla fija) son ILUSTRATIVOS (sinteticos); no se ajusta ningun experimento.
Modelo: P(nu_a -> nu_b) = sen^2(2 theta) sen^2(Delta m^2 c^4 L/(4 hbar c E)); la fase vale 1.267 Delta m^2[eV^2] L[km]/E[GeV] (el coeficiente se calcula con las constantes); probabilidad de
supervivencia = 1 - P; longitud de oscilacion L_osc = 4 pi hbar c E/(Delta m^2 c^4); promedio sobre un espectro de energias uniforme; deteccion Monte Carlo.
Supuestos: dos sabores, vacio, ondas planas con energia bien definida. Validez: ilustrativa; la oscilacion de tres sabores y los efectos de materia no se tratan.
Tolerancia: coeficiente 1.267 dentro de 5e-4; P_aparicion + P_supervivencia = 1 a 1e-15; frecuencia empirica dentro de 4 errores estandar; promedio de energia dentro de 0.02 de sen^2(2 theta)/2.
"""
from __future__ import annotations
import math
import platform
import random
import sys

HBARC_EV_M = 1.973269804e-7


def fase(dm2, l_km, e_gev):
    return dm2 * 1e0 * (l_km * 1e3) / (4 * HBARC_EV_M * e_gev * 1e9)


def prob(s2, dm2, l_km, e_gev):
    return s2 * math.sin(fase(dm2, l_km, e_gev)) ** 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    coef = fase(1.0, 1.0, 1.0)
    print(f"coeficiente de la fase Delta m^2 L/(4 hbar c E) para 1 eV^2, 1 km, 1 GeV = {coef:.5f} (valor habitual 1.267)")
    assert abs(coef / 1.267 - 1) < 5e-4
    s2, dm2 = 1.0, 2.5e-3
    print(f"{'L [km]':>8} {'E [GeV]':>8} {'fase':>8} {'P(aparicion)':>13} {'P(superv.)':>11} {'suma':>6}")
    for l, e in ((100, 1.0), (295, 0.6), (495, 1.0), (1000, 1.0), (2000, 1.0), (500, 0.5), (500, 2.0)):
        p = prob(s2, dm2, l, e)
        print(f"{l:8d} {e:8.1f} {fase(dm2, l, e):8.4f} {p:13.5f} {1 - p:11.5f} {p + (1 - p):6.1f}")
        assert abs(p + (1 - p) - 1) < 1e-15
    losc = lambda e: 4 * math.pi * HBARC_EV_M * e * 1e9 / dm2 / 1e3
    print(f"longitud de oscilacion para E = 1 GeV: L_osc = {losc(1.0):.2f} km ; primer maximo en L_osc/2 = {losc(1.0) / 2:.2f} km")
    assert abs(prob(s2, dm2, losc(1.0) / 2, 1.0) - 1) < 1e-12
    # Monte Carlo
    rng = random.Random(20261109)
    p = prob(s2, dm2, 295, 0.6)
    n = 100000
    k = sum(1 for _ in range(n) if rng.random() < p)
    err = math.sqrt(p * (1 - p) / n)
    print(f"{n} neutrinos a 295 km y 0.6 GeV: P = {p:.5f} ; frecuencia = {k / n:.5f} ; desviacion = {abs(k / n - p) / err:.2f} errores")
    assert abs(k / n - p) < 4 * err
    # promedio en energia
    prom = 0.0
    ne = 20000
    for i in range(ne):
        e = 0.5 + (i + 0.5) * (1.5 / ne)
        prom += prob(s2, dm2, 5000, e)
    prom /= ne
    print(f"promedio de P en L = 5000 km con E uniforme en [0.5, 2] GeV: {prom:.4f} ; limite de oscilaciones rapidas sen^2(2 theta)/2 = {s2 / 2:.4f}")
    assert abs(prom - s2 / 2) < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
