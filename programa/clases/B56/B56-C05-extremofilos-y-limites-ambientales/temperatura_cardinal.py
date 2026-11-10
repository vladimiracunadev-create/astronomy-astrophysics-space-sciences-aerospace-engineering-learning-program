#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C05: modelo de temperatura cardinal y cotejo con los limites de COSPAR.

Datos: (1) limites de replicacion de la politica COSPAR 2026 (Space Research Today n. 224):
actividad del agua minima 0,5 y temperatura minima -28 C (texto completo consultado el
2026-11-09). (2) Tasas de crecimiento SINTETICAS generadas aqui con semilla 7: no son
mediciones de ningun organismo. (3) Los ambientes de la tabla final son ILUSTRATIVOS.
Modelo (Ratkowsky, rama fria): sqrt(r) = b (T - T_min), T < T_opt; ajuste por minimos
cuadrados lineales sobre sqrt(r). Dos metodos independientes: formulas cerradas y
ecuaciones normales resueltas por Cramer.
Supuestos: ruido gaussiano multiplicativo pequeno; solo rama fria. Validez: T entre T_min y
T_opt del organismo sintetico. Tolerancia: coinciden los dos metodos a 1e-9 y el T_min
recuperado dista < 1 K del verdadero.
"""
from __future__ import annotations
import platform
import random
import sys

LLT_C = -28.0
LLAW = 0.5


def generar(b=0.05, tmin=-10.0, temps=None, sd=0.002, semilla=7):
    rng = random.Random(semilla)
    temps = temps or [-5, 0, 5, 10, 15, 20, 25]
    return [(t, b * (t - tmin) + rng.gauss(0, sd)) for t in temps]


def ajuste_cerrado(datos):
    n = len(datos)
    sx = sum(t for t, _ in datos)
    sy = sum(y for _, y in datos)
    sxx = sum(t * t for t, _ in datos)
    sxy = sum(t * y for t, y in datos)
    b = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    a = (sy - b * sx) / n
    return b, -a / b


def ajuste_cramer(datos):
    n = len(datos)
    sx = sum(t for t, _ in datos)
    sy = sum(y for _, y in datos)
    sxx = sum(t * t for t, _ in datos)
    sxy = sum(t * y for t, y in datos)
    det = sxx * n - sx * sx
    a = (sy * sxx - sx * sxy) / det
    b = (n * sxy - sx * sy) / det
    return b, -a / b


def dentro_de_limites(t_c, aw):
    return t_c >= LLT_C and aw >= LLAW


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    datos = generar()
    b1, tm1 = ajuste_cerrado(datos)
    b2, tm2 = ajuste_cramer(datos)
    assert abs(b1 - b2) < 1e-9 and abs(tm1 - tm2) < 1e-9
    assert abs(tm1 - (-10.0)) < 1.0, "T_min recuperado lejos del verdadero"
    print(f"Ajuste: b = {b1:.4f} ; T_min = {tm1:.2f} C (verdadero: 0.0500 y -10.00)")
    ambientes = [
        ("Salmuera hipersalina fria (sintetico)", -20.0, 0.60),
        ("Suelo seco polar (sintetico)", -40.0, 0.30),
        ("Fuente termal (sintetico)", 70.0, 0.98),
        ("Sal casi seca (sintetico)", 20.0, 0.40),
    ]
    for nombre, t, aw in ambientes:
        print(f"{nombre:40s} T={t:6.1f} C, aw={aw:.2f} -> {'dentro' if dentro_de_limites(t, aw) else 'fuera'}")
    assert dentro_de_limites(-28.0, 0.5) and not dentro_de_limites(-28.1, 0.5)
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
