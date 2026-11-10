#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C15: probabilidad de vida dada una deteccion con falsos positivos.

Datos: SINTETICOS e ILUSTRATIVOS. La probabilidad previa p, la sensibilidad s = P(senal|vida)
y la tasa de falsos positivos f = P(senal|no vida) son numeros de ejercicio, no estimaciones
de la comunidad. El marco conceptual (el oxigeno es una biofirma fuerte pero ambigua; hay
falsos positivos y falsos negativos) procede del resumen de Meadows et al. (2018),
arXiv:1705.07560, consultado el 2026-11-09.
Modelo: teorema de Bayes, P(vida|senal) = s p / (s p + f (1-p)). Dos senales independientes
multiplican las razones de verosimilitud en la razon de probabilidades (odds).
Supuestos: independencia condicional entre senales. Validez: ilustra el razonamiento.
Tolerancia: igualdad EXACTA con fracciones entre Bayes, conteo de poblacion y actualizacion
secuencial.
"""
from __future__ import annotations
import platform
import sys
from fractions import Fraction as F


def posterior(p, s, f):
    return s * p / (s * p + f * (1 - p))


def posterior_por_conteo(p, s, f, poblacion=10 ** 6):
    vida = int(p * poblacion)
    sin = poblacion - vida
    verdaderos = vida * s
    falsos = sin * f
    return F(verdaderos) / (F(verdaderos) + F(falsos))


def odds(x):
    return x / (1 - x)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    s = F(9, 10)
    for p, f in ((F(1, 100), F(1, 100)), (F(1, 100), F(1, 1000)), (F(1, 1000), F(1, 1000)), (F(1, 1000), F(1, 100))):
        pb = posterior(p, s, f)
        pc = posterior_por_conteo(p, s, f)
        assert pb == pc, "Bayes y conteo deben coincidir"
        print(f"previa {float(p):.3f}, sens {float(s):.2f}, falsos pos {float(f):.3f} -> P(vida|senal) = {float(pb):.4f}")
    # Dos senales independientes: secuencial = conjunto
    p, f = F(1, 100), F(1, 20)
    seq = posterior(posterior(p, s, f), s, f)
    conj = posterior(p, s * s, f * f)
    assert seq == conj
    assert odds(seq) == odds(p) * (s / f) ** 2
    print(f"Dos senales independientes: {float(seq):.4f} (secuencial = conjunta = odds multiplicadas)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
