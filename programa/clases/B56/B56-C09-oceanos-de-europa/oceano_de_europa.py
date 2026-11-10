#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C09: profundidad de un oceano global de Europa a partir de su volumen.

Datos consultados el 2026-11-09: NASA/NSSDC, hoja de satelites galileanos: masa
48,0e21 kg, radio medio 1561 km, densidad 3010 kg/m3, gravedad 1,31 m/s2; pagina de Europa de
la NASA (science.nasa.gov): "un oceano de agua salada bajo la corteza de hielo que contiene
el doble de agua que el oceano global de la Tierra". G de NIST (CODATA 2022).
NO CONSULTADOS (ILUSTRATIVOS): volumen del oceano terrestre 1,335e9 km3; densidad del hielo
920 kg/m3 y del agua salada 1030 kg/m3; espesor del hielo de 15 km (la pagina de la NASA no da
cifra; es un supuesto que se varia en los ejercicios).
Modelo: oceano = cascara esferica entre r1 = R - d_hielo - d_oceano y r2 = R - d_hielo, con
V = 4 pi (r2^3 - r1^3)/3. Presion en el fondo: P = rho_h g d_hielo + rho_a g d_oceano, con g
constante e igual al valor de superficie (sobrestima algo la presion; el interior real tiene
g menor a mayor profundidad).
Validez: orden de magnitud. Tolerancia: la biseccion coincide con la forma cerrada a 1e-9
relativo; la densidad calculada con M y R coincide con la hoja a < 1 %.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
M, R = 48.0e21, 1561e3
V_TIERRA = 1.335e9 * 1e9  # m3 (ilustrativo, no consultado)
RHO_H, RHO_A = 920.0, 1030.0
G_SUP = 1.31


def profundidad_cerrada(V, d_hielo):
    r2 = R - d_hielo
    return r2 - (r2 ** 3 - 3 * V / (4 * math.pi)) ** (1 / 3)


def volumen(d_oceano, d_hielo):
    r2 = R - d_hielo
    r1 = r2 - d_oceano
    return 4 * math.pi / 3 * (r2 ** 3 - r1 ** 3)


def profundidad_biseccion(V, d_hielo):
    lo, hi = 0.0, R - d_hielo
    for _ in range(200):
        mid = (lo + hi) / 2
        if volumen(mid, d_hielo) < V:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rho = M / (4 * math.pi / 3 * R ** 3)
    print(f"Densidad media = {rho:.0f} kg/m3 (hoja: 3010) ; g = {G * M / R ** 2:.3f} m/s2 (hoja: 1,31)")
    assert abs(rho / 3010 - 1) < 0.01
    V = 2 * V_TIERRA
    for d_h in (5e3, 15e3, 30e3):
        d_c = profundidad_cerrada(V, d_h)
        d_b = profundidad_biseccion(V, d_h)
        assert abs(d_c / d_b - 1) < 1e-9
        fino = V / (4 * math.pi * (R - d_h) ** 2)
        p = (RHO_H * d_h + RHO_A * d_c) * G_SUP
        print(f"hielo {d_h / 1e3:4.0f} km -> oceano {d_c / 1e3:6.1f} km (cascara fina: {fino / 1e3:6.1f} km) ; "
              f"P fondo = {p / 1e6:6.1f} MPa")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
