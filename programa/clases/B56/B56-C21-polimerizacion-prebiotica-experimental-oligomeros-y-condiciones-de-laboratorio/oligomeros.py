#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C21: distribucion de longitudes de oligomeros (Flory) y ciclos humedo-seco.

Datos: SINTETICOS e ILUSTRATIVOS. La probabilidad de enlace por ciclo y el numero de ciclos son
numeros de ejercicio; no reproducen ningun experimento. El contexto bibliografico procede de
los resumenes (Europe PMC, consultados el 2026-11-09) de Simonis et al. (2026, Sci. Rep.,
doi 10.1038/s41598-026-56548-9), que informa la sintesis abiotica de polimeros resistentes a la
RNasa con ciclos humedo-seco, y de Alejandre et al. (2025, Commun. Chem.,
doi 10.1038/s42004-025-01632-w), un MODELO teorico de polimerizacion de ARN en una interfaz arcilla-agua.
Modelo: polimerizacion por pasos de monomeros. Con extension de reaccion p (probabilidad de que
un extremo haya reaccionado), la fraccion en numero de cadenas de longitud n es
(1-p) p^(n-1) y la longitud media en numero es 1/(1-p). Cada ciclo humedo-seco aumenta p segun
p_(k+1) = p_k + (1 - p_k) e, con e la eficiencia por ciclo, y la hidrolisis se desprecia.
Supuestos: reactividad independiente de la longitud; sin hidrolisis ni ciclizacion.
Validez: ilustra la forma de la distribucion. Tolerancia: la simulacion Monte Carlo (semilla
31415, 200 000 monomeros) coincide con la formula a 0,01 en fraccion y a 2 % en longitud media.
"""
from __future__ import annotations
import platform
import random
import sys


def fraccion_n(p, n):
    return (1 - p) * p ** (n - 1)


def longitud_media(p):
    return 1.0 / (1.0 - p)


def p_tras_ciclos(e, k):
    p = 0.0
    for _ in range(k):
        p = p + (1 - p) * e
    return p


def simular(p, monomeros=200000, semilla=31415):
    """Cada monomero tiene un extremo reactivo; con probabilidad p se une al siguiente. Se genera una
    cadena por 'racha' de uniones: longitud geometrica."""
    rng = random.Random(semilla)
    longitudes = []
    restantes = monomeros
    while restantes > 0:
        n = 1
        while n < restantes and rng.random() < p:
            n += 1
        longitudes.append(n)
        restantes -= n
    return longitudes


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    e = 0.30
    for k in (1, 3, 6, 10):
        p = p_tras_ciclos(e, k)
        cierre = 1 - (1 - e) ** k
        assert abs(p - cierre) < 1e-12
        print(f"ciclos = {k:2d}: p = {p:.4f} ; longitud media = {longitud_media(p):6.2f}")
    p = p_tras_ciclos(e, 6)
    cad = simular(p)
    n = len(cad)
    for L in (1, 2, 5, 10):
        obs = sum(1 for c in cad if c == L) / n
        esp = fraccion_n(p, L)
        print(f"n={L:2d}: observada {obs:.4f} ; Flory {esp:.4f}")
        assert abs(obs - esp) < 0.01
    media = sum(cad) / n
    print(f"Longitud media simulada = {media:.3f} ; teorica = {longitud_media(p):.3f}")
    assert abs(media / longitud_media(p) - 1) < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
