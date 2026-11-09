#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C19: corriente geomagneticamente inducida en una linea y niveles de retorno de eventos extremos.

Datos: ninguna constante fisica. El campo electrico geomagnetico (1 V/km), la longitud de linea (100 km), las resistencias (linea 5 ohm, toma a tierra 0.5 ohm en cada extremo),
la tasa de eventos (10 por anio por encima del umbral), el indice de la cola (alpha = 2.5), el registro (60 anios) y las repeticiones (500, semilla fija) son ILUSTRATIVOS (sinteticos).
Modelo: (1) circuito de corriente continua con fuente V = E L en serie con R_linea y dos tomas a tierra: I = E L/(R_linea + 2 R_tierra); (2) cola de potencias P(X > x) = (x/x_min)^-(alpha - 1)
con N eventos por anio por encima de x_min; nivel de retorno x_T = x_min (N T)^(1/(alpha - 1)); estimacion de alpha por maxima verosimilitud sobre un registro sintetico de 60 anios y
propagacion de la incertidumbre al nivel de 100 anios con 500 repeticiones.
Supuestos: campo uniforme, linea sin transformadores saturables, eventos independientes con cola de potencias. Validez: ilustrativa.
Tolerancia: nivel de retorno verdadero y el estimado dentro del intervalo del 5-95 % de las repeticiones.
"""
from __future__ import annotations
import math
import platform
import random
import sys


def gic(e_vkm, l_km, r_lin, r_tie):
    return e_vkm * l_km / (r_lin + 2 * r_tie)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'E [V/km]':>9} {'L [km]':>7} {'V = E L [V]':>12} {'R total [ohm]':>14} {'I [A]':>8}")
    for e, l in ((1, 100), (2, 100), (1, 200), (5, 100), (5, 400)):
        print(f"{e:9.1f} {l:7.0f} {e * l:12.0f} {5 + 2 * 0.5:14.1f} {gic(e, l, 5.0, 0.5):8.2f}")
    assert abs(gic(1, 100, 5.0, 0.5) - 100 / 6) < 1e-12
    # niveles de retorno
    alpha, lam, anios, rep = 2.5, 10.0, 60, 500
    verdad = (lam * 100) ** (1 / (alpha - 1))
    print(f"cola con alpha = {alpha}, {lam:.0f} eventos/anio: nivel de 100 anios verdadero = {verdad:.2f} x_min ; de 10 anios = {(lam * 10) ** (1 / (alpha - 1)):.2f} x_min ; de 1 anio = {lam ** (1 / (alpha - 1)):.2f} x_min")
    rng = random.Random(20261109)
    estimaciones, alfas = [], []
    for _ in range(rep):
        n = max(2, int(rng.gauss(lam * anios, math.sqrt(lam * anios))))
        xs = [(1 - rng.random()) ** (-1 / (alpha - 1)) for _ in range(n)]
        a_hat = 1 + n / sum(math.log(x) for x in xs)
        # mu = N T con N estimado por n/anios
        estimaciones.append(((n / anios) * 100) ** (1 / (a_hat - 1)))
        alfas.append(a_hat)
    estimaciones.sort()
    alfas.sort()
    q = lambda v, p: v[int(p * (len(v) - 1))]
    print(f"{rep} registros de {anios} anios: alpha estimado: mediana {q(alfas, 0.5):.3f}, intervalo 5-95 % [{q(alfas, 0.05):.3f}, {q(alfas, 0.95):.3f}] (verdadero {alpha})")
    print(f"nivel de 100 anios estimado: mediana {q(estimaciones, 0.5):.2f}, intervalo 5-95 % [{q(estimaciones, 0.05):.2f}, {q(estimaciones, 0.95):.2f}] x_min (verdadero {verdad:.2f})")
    assert q(estimaciones, 0.05) < verdad < q(estimaciones, 0.95)
    print(f"cociente del intervalo 95/5 % para el nivel de 100 anios: {q(estimaciones, 0.95) / q(estimaciones, 0.05):.2f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
