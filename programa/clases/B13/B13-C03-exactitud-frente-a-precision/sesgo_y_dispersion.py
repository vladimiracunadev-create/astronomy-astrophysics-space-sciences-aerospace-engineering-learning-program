#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C03: exactitud (sesgo) frente a precision (dispersion).

Datos: SINTETICOS. Un telemetro laser mide una distancia de referencia de
1000.000 m (verdad conocida por construccion) con cuatro instrumentos
simulados: (A) sesgo 0 y dispersion alta, (B) sesgo alto y dispersion baja,
(C) ambos bajos, (D) ambos altos. Semilla fija.
Modelo: x_i = verdad + sesgo + ruido gaussiano(0, sigma). Se estiman
sesgo = media - verdad, desviacion tipica s (n-1) y error cuadratico medio
RMSE = sqrt(media((x-verdad)^2)).
Identidad exacta: RMSE^2 = sesgo^2 + s_pob^2 con s_pob la desviacion con
divisor n. Supuestos: ruido gaussiano, independiente; verdad conocida.
Tolerancia: 1e-9 en la identidad; el sesgo estimado se acerca al verdadero
con error ~ sigma/sqrt(n).
"""
from __future__ import annotations
import math
import platform
import random
import sys

VERDAD = 1000.000  # m (sintetica)


def estadisticos(x):
    n = len(x)
    media = sum(x) / n
    sesgo = media - VERDAD
    s_pob = math.sqrt(sum((v - media) ** 2 for v in x) / n)
    s = math.sqrt(sum((v - media) ** 2 for v in x) / (n - 1))
    rmse = math.sqrt(sum((v - VERDAD) ** 2 for v in x) / n)
    return media, sesgo, s, s_pob, rmse


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261105)
    casos = {"A": (0.000, 0.050), "B": (0.200, 0.005), "C": (0.003, 0.005), "D": (0.200, 0.050)}
    n = 2000
    print("caso  sesgo_verd  sigma_verd | sesgo_est(m)  s(m)     RMSE(m)")
    for nombre, (b, sg) in casos.items():
        x = [VERDAD + b + rng.gauss(0.0, sg) for _ in range(n)]
        media, sesgo, s, s_pob, rmse = estadisticos(x)
        assert abs(rmse ** 2 - (sesgo ** 2 + s_pob ** 2)) < 1e-9      # identidad exacta
        assert abs(sesgo - b) < 5 * sg / math.sqrt(n) + 1e-12         # 5 errores tipicos
        print(f"  {nombre}    {b:8.3f}   {sg:8.3f}   | {sesgo:9.4f}   {s:8.4f}  {rmse:8.4f}")
    # Prueba determinista: datos sin ruido -> s = 0, RMSE = |sesgo|
    x = [VERDAD + 0.2] * 10
    _, sesgo, s, _, rmse = estadisticos(x)
    assert abs(s) < 1e-12 and abs(rmse - abs(sesgo)) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("FALLO: una prueba no se cumple")
        sys.exit(1)
