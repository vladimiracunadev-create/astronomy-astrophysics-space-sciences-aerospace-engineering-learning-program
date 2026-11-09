#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C12: error del pronostico de llegada de CME con parametros de arrastre mal especificados.

Datos: R_sol (UAI 2015 B3) y 1 au (IERS TN36), consultados 2026-11-09. Los eventos sinteticos (velocidades iniciales de 500 a 2500 km/s), el viento (400 km/s), el arrastre verdadero (2e-8 km^-1) y los
modelos (arrastre 1e-8, 2e-8 y 4e-8; sin arrastre), la ventana de acierto (+/- 6 h) y la semilla fija son ILUSTRATIVOS (sinteticos).
Modelo: tiempo de transito del modelo de arrastre (biseccion) para 200 eventos; error medio (sesgo), error absoluto medio (MAE), raiz del error cuadratico medio y fraccion dentro de +/- 6 h para cada modelo.
Supuestos: los eventos se generan con el modelo de arrastre y gamma verdadero. Validez: ilustrativa.
Tolerancia: el modelo con gamma verdadero tiene error cero; el modelo sin arrastre tiene sesgo negativo (llega antes).
"""
from __future__ import annotations
import math, platform, random, sys
R_SOL, AU = 6.957e5, 1.49597870700e8

def transito(v0, w, g, r0=20 * R_SOL):
    if g == 0:
        return (AU - r0) / v0 / 3600
    lo, hi = 0.0, 1e7
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if r0 + w * mid + math.log(1 + g * (v0 - w) * mid) / g < AU:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi) / 3600

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    w, gv = 400.0, 2e-8
    vs = [rng.uniform(500, 2500) for _ in range(200)]
    real = [transito(v, w, gv) for v in vs]
    print(f"{'modelo':<20} {'sesgo [h]':>10} {'MAE [h]':>8} {'RMSE [h]':>9} {'dentro de +/- 6 h':>18}")
    res = {}
    for nombre, g in (("gamma verdadero", 2e-8), ("gamma / 2", 1e-8), ("gamma x 2", 4e-8), ("sin arrastre", 0.0)):
        err = [transito(v, w, g) - t for v, t in zip(vs, real)]
        sesgo = sum(err) / len(err)
        mae = sum(abs(e) for e in err) / len(err)
        rmse = math.sqrt(sum(e * e for e in err) / len(err))
        dentro = sum(1 for e in err if abs(e) <= 6) / len(err)
        res[nombre] = (sesgo, mae, rmse, dentro)
        print(f"{nombre:<20} {sesgo:10.2f} {mae:8.2f} {rmse:9.2f} {dentro:18.3f}")
    assert res["gamma verdadero"][1] < 1e-9
    assert res["sin arrastre"][0] < 0
    assert res["gamma / 2"][0] < 0 < res["gamma x 2"][0]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
