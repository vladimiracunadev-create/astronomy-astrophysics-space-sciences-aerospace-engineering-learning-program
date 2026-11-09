#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C10: leyes de conservacion en reacciones de particulas con numeros cuanticos.

Datos: ninguna constante fisica. Las cargas de los quarks (+2/3 para u, -1/3 para d), el numero barionico (1/3 por quark) y los numeros leptonicos de las particulas son valores estandar del modelo
estandar NO consultados en esta sesion; las reacciones propuestas (permitidas y prohibidas) son ejemplos ILUSTRATIVOS elegidos para el laboratorio.
Modelo: cada particula tiene (carga Q, numero barionico B, numeros leptonicos L_e, L_mu, L_tau) con fracciones exactas (modulo fractions); una reaccion es permitida por las reglas
de conservacion si la suma de cada numero se conserva; se construyen protones, neutrones y piones a partir de quarks y se comprueba su carga y su numero barionico.
Supuestos: solo las leyes de conservacion de la carga, el numero barionico y los numeros leptonicos; se ignoran la energia disponible, el espin y la paridad. Validez: filtro necesario, no suficiente.
Tolerancia: aritmetica exacta con fracciones; la clasificacion de cada reaccion debe coincidir con la esperada.
"""
from __future__ import annotations
import platform
import sys
from fractions import Fraction as F

# (Q, B, Le, Lmu, Ltau)
P = {
    "p": (1, 1, 0, 0, 0), "n": (0, 1, 0, 0, 0), "pbar": (-1, -1, 0, 0, 0),
    "e-": (-1, 0, 1, 0, 0), "e+": (1, 0, -1, 0, 0), "nue": (0, 0, 1, 0, 0), "nuebar": (0, 0, -1, 0, 0),
    "mu-": (-1, 0, 0, 1, 0), "mu+": (1, 0, 0, -1, 0), "numu": (0, 0, 0, 1, 0), "numubar": (0, 0, 0, -1, 0),
    "gamma": (0, 0, 0, 0, 0), "pi+": (1, 0, 0, 0, 0), "pi-": (-1, 0, 0, 0, 0), "pi0": (0, 0, 0, 0, 0),
}
NOMBRES = ["Q", "B", "L_e", "L_mu", "L_tau"]
Q_QUARK = {"u": F(2, 3), "d": F(-1, 3), "ubar": F(-2, 3), "dbar": F(1, 3)}


def total(lista):
    s = [F(0)] * 5
    for x in lista:
        for i, v in enumerate(P[x]):
            s[i] += v
    return s


def clasifica(ini, fin):
    ti, tf = total(ini), total(fin)
    violadas = [NOMBRES[i] for i in range(5) if ti[i] != tf[i]]
    return violadas


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # quarks
    print(f"{'hadron':<8} {'quarks':<12} {'Q':>5} {'B':>5}")
    for nombre, qs in (("p", ["u", "u", "d"]), ("n", ["u", "d", "d"]), ("pi+", ["u", "dbar"]), ("pi-", ["d", "ubar"])):
        q = sum(Q_QUARK[x] for x in qs)
        b = sum((F(1, 3) if not x.endswith("bar") else F(-1, 3)) for x in qs)
        print(f"{nombre:<8} {'+'.join(qs):<12} {str(q):>5} {str(b):>5}")
        assert q == P[nombre][0] and b == P[nombre][1], nombre
    reacciones = [
        (["n"], ["p", "e-", "nuebar"], True),
        (["pi+"], ["mu+", "numu"], True),
        (["e-", "e+"], ["gamma", "gamma"], True),
        (["p", "p"], ["p", "p", "p", "pbar"], True),
        (["mu-"], ["e-", "nue", "numu"], False),
        (["mu-"], ["e-", "nuebar", "numu"], True),
        (["mu-"], ["e-", "gamma"], False),
        (["p"], ["e+", "pi0"], False),
        (["e-"], ["nue", "gamma"], False),
        (["pi0"], ["gamma", "gamma"], True),
        (["n"], ["p", "e-"], False),
    ]
    print(f"{'reaccion':<38} {'permitida':>9} {'leyes violadas':<20}")
    for ini, fin, esperado in reacciones:
        v = clasifica(ini, fin)
        print(f"{' + '.join(ini) + ' -> ' + ' + '.join(fin):<38} {str(not v):>9} {', '.join(v) if v else '-':<20}")
        assert (not v) == esperado, (ini, fin)
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
