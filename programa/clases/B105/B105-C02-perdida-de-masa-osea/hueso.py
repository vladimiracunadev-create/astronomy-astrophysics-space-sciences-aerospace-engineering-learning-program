#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C02: perdida de densidad mineral osea (modelo DIDACTICO, datos SINTETICOS).

Dato consultado (NASA, 'Human body in space', 2026-11-10): los huesos que soportan peso pierden en promedio 1 % a 1.5 % de densidad
mineral por mes en el espacio. Aqui se usa ese INTERVALO como entrada de un modelo exponencial BMD(t) = BMD0 (1 - r)^t (t en meses),
frente a uno lineal BMD0 (1 - r t). BMD0 = 1.00 g/cm2 con DE 0.12 (ilustrativo). Recuperacion posvuelo: la perdida decae como
exp(-k t) con k = ln(2)/6 por mes (semivida de recuperacion de 6 meses, ILUSTRATIVA; la NASA indica que la perdida puede no recuperarse
por completo). Poblacion SINTETICA de 5000 individuos, semilla 105, tasa r ~ N(1.25 %, 0.25 %). Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np


def exponencial(b0, r, t):
    return b0 * (1 - r) ** t


def lineal(b0, r, t):
    return b0 * (1 - r * t)


def recuperacion(perdida, k, t):
    return perdida * np.exp(-k * t)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: tasa 1 %-1.5 % por mes consultada (NASA, 2026-11-10); BMD0, DE y recuperacion SINTETICOS/ILUSTRATIVOS; poblacion semilla 105")
    b0 = 1.0
    print("Perdida acumulada exponencial / lineal [%] por tasa mensual y duracion:")
    for r in (0.010, 0.0125, 0.015):
        fila = []
        for t in (1, 3, 6, 12):
            fila.append(f"{t:2d} m: {100 * (1 - exponencial(b0, r, t) / b0):5.2f}/{100 * (1 - lineal(b0, r, t) / b0):5.2f}")
        print(f"  r = {100 * r:4.2f} %/mes   " + "   ".join(fila))
    rng = np.random.default_rng(105)
    r = rng.normal(0.0125, 0.0025, 5000).clip(0.0, None)
    bmd0 = rng.normal(b0, 0.12, 5000)
    bmd6 = exponencial(bmd0, r, 6)
    perd6 = 100 * (1 - bmd6 / bmd0)
    print(f"Poblacion sintetica a 6 meses: perdida media {perd6.mean():.2f} % (DE {perd6.std():.2f}); percentiles 5/95 = {np.percentile(perd6, 5):.2f}/{np.percentile(perd6, 95):.2f} %")
    print(f"  fraccion con perdida > 10 % a 6 meses = {np.mean(perd6 > 10):.4f}; con perdida > 5 % = {np.mean(perd6 > 5):.3f}")
    k = np.log(2) / 6
    p6 = (1 - exponencial(b0, 0.0125, 6)) * b0
    print(f"Recuperacion ilustrativa (semivida 6 meses) de una perdida de {100 * p6:.2f} % de BMD0 a los 6 meses:")
    for t in (0, 6, 12, 24):
        print(f"  t = {t:2d} meses tras el vuelo: perdida restante {100 * recuperacion(p6, k, t):5.2f} %")
    # tiempo hasta recuperar el 90 % de la perdida
    t90 = np.log(10) / k
    print(f"Tiempo hasta recuperar el 90 % de la perdida (modelo) = {t90:.1f} meses")
    # incertidumbre del T-score didactico: variacion respecto a BMD0 individual en unidades de DE poblacional
    dz = (bmd0 - bmd6).mean() / 0.12
    print(f"Perdida media expresada en DE poblacionales (0.12 g/cm2): {dz:.2f}")
    assert abs(100 * (1 - exponencial(1, 0.01, 6)) - 5.85) < 0.01
    assert all(exponencial(1, 0.0125, t) > lineal(1, 0.0125, t) for t in (3, 6, 12))
    assert 6.5 < perd6.mean() < 8.0
    assert abs(recuperacion(1.0, k, 6) - 0.5) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
