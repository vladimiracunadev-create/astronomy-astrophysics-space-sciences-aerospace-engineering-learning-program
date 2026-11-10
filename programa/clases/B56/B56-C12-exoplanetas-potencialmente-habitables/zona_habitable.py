#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C12: borde de la zona habitable segun la parametrizacion de Kopparapu et al.

Datos consultados el 2026-11-09: resumen de Kopparapu et al. (2013), arXiv:1301.6674: para el
Sol, perdida de agua a 0,99 UA y maximo invernadero de CO2 a 1,70 UA; modelo para estrellas
F, G, K y M con T_ef de 2600 a 7200 K. LOS COEFICIENTES NUMERICOS de la tabla del articulo NO
SE CONSULTARON (solo el resumen): se tomaron de la memoria del autor del script y aqui solo
se comprueba que reproducen las dos cifras del resumen. Cualquier otro valor que se calcule con
ellos es ILUSTRATIVO hasta cotejarlo con el articulo. Estrellas y planetas: SINTETICOS.
Modelo: S_ef(T) = S0 + a T* + b T*^2 + c T*^3 + d T*^4 con T* = T_ef - 5780 K;
distancia limite d = sqrt(L / S_ef) con L en L_sol y d en UA.
Supuestos: planeta de 1 masa terrestre, atmosfera de N2-CO2-H2O; sin nubes ni rotacion.
Validez: 2600 K <= T_ef <= 7200 K. Tolerancia: 0,01 UA frente a las cifras del resumen.
"""
from __future__ import annotations
import math
import platform
import sys

COEF = {
    "perdida de agua": (1.0140, 8.1774e-5, 1.7063e-9, -4.3241e-12, -6.6462e-16),
    "maximo invernadero": (0.3438, 5.8942e-5, 1.6558e-9, -3.0045e-12, -5.2983e-16),
}


def s_ef(nombre, t_ef):
    s0, a, b, c, d = COEF[nombre]
    t = t_ef - 5780.0
    return s0 + a * t + b * t ** 2 + c * t ** 3 + d * t ** 4


def borde(nombre, t_ef, luminosidad):
    return math.sqrt(luminosidad / s_ef(nombre, t_ef))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ri, ro = borde("perdida de agua", 5780, 1.0), borde("maximo invernadero", 5780, 1.0)
    print(f"Sol (T_ef = 5780 K, L = 1): borde interno {ri:.3f} UA ; borde externo {ro:.3f} UA")
    assert abs(ri - 0.99) < 0.01 and abs(ro - 1.70) < 0.01
    estrellas = [
        ("tipo G sintetica", 5780.0, 1.0),
        ("tipo K sintetica", 4500.0, 0.20),
        ("tipo M sintetica", 3300.0, 0.0015),
    ]
    for nombre, t, lum in estrellas:
        ri, ro = borde("perdida de agua", t, lum), borde("maximo invernadero", t, lum)
        assert ri < ro
        print(f"{nombre:18s} T_ef={t:6.0f} K L={lum:7.4f}: HZ = {ri:.3f} a {ro:.3f} UA")
    # Un planeta sintetico a 0,06 UA de la estrella M: flujo en unidades de S_tierra
    a_pl, lum = 0.06, 0.0015
    flujo = lum / a_pl ** 2
    print(f"Planeta sintetico a {a_pl} UA de la M: flujo = {flujo:.2f} S_Tierra ; limites: "
          f"{s_ef('maximo invernadero', 3300.0):.3f} a {s_ef('perdida de agua', 3300.0):.3f}")
    assert s_ef("maximo invernadero", 3300.0) < flujo < s_ef("perdida de agua", 3300.0)
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
