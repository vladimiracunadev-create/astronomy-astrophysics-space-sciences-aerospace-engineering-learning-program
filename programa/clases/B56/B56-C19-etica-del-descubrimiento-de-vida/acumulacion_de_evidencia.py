#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C19: acumulacion de evidencia en log-odds y umbrales de comunicacion.

Datos: SINTETICOS e ILUSTRATIVOS. La probabilidad previa, las razones de verosimilitud de cada
linea de evidencia y los umbrales de comunicacion (0,5; 0,9; 0,99) son numeros de ejercicio,
no una escala adoptada por ninguna agencia. El contexto normativo (la politica COSPAR 2026
obliga a mantener contenida una muestra devuelta si se detecta una entidad replicante
no terrestre, y trata los "falsos positivos") procede de las secciones 4.5 y 6.5 del texto
completo consultado el 2026-11-09.
Modelo: log-odds posterior = log-odds previo + suma de ln(razon de verosimilitud de cada linea
independiente). Probabilidad = 1/(1+exp(-L)).
Supuestos: lineas condicionalmente independientes (rara vez cierto). Validez: ilustra la
logica de la acumulacion. Tolerancia: igualdad con fracciones exactas entre la forma
secuencial y la del producto de razones.
"""
from __future__ import annotations
import math
import platform
import sys
from fractions import Fraction as F

UMBRALES = (0.5, 0.9, 0.99)


def prob_de_odds(o):
    return o / (1 + o)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    previa = F(1, 1000)
    lineas = [("compuesto candidato", F(20)), ("patron isotopico", F(5)), ("contexto geologico excluye origen abiotico", F(3)),
              ("replica independiente", F(10))]
    odds = previa / (1 - previa)
    L = math.log(float(odds))
    print(f"Previa {float(previa):.4f} -> odds {float(odds):.5f}")
    for nombre, lr in lineas:
        odds *= lr
        L += math.log(float(lr))
        p = prob_de_odds(odds)
        # Dos vias independientes: producto exacto y suma de logaritmos
        p_log = 1 / (1 + math.exp(-L))
        assert abs(float(p) - p_log) < 1e-12
        sup = [u for u in UMBRALES if float(p) >= u]
        print(f"+ {nombre:44s} LR={float(lr):4.0f} -> P = {float(p):.4f} ; umbrales superados: {sup if sup else 'ninguno'}")
    total = F(1)
    for _, lr in lineas:
        total *= lr
    assert odds == previa / (1 - previa) * total
    # Una linea falsa (LR=1/20) deshace la evidencia de la primera
    assert prob_de_odds(previa / (1 - previa) * 20 / 20) == previa
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
