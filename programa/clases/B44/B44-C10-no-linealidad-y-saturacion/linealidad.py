#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C10: no linealidad, desviacion respecto de la recta y umbral de saturacion.

Datos: ninguna constante fisica. La respuesta cuadratica (coeficiente b = 1,5e-6 por ADU), la ganancia (1,0 ADU/e-), el pozo (60 000 ADU) y el ruido de lectura son
ILUSTRATIVOS (sinteticos); no describen una camara real.
Modelo: salida = x (1 - b x) con x el flujo lineal en ADU (el termino cuadratico comprime), saturacion dura en 60 000 ADU. Se hace un barrido de exposicion, un ajuste lineal
a los puntos bajos (x <= 3000), se mide la desviacion porcentual y se halla el umbral de 1 % analitico (x = 0,01/b) frente al numerico. Semilla 20261109 para el ruido.
Supuestos: no linealidad cuadratica pura y ruido gaussiano de 3 ADU. Validez: ilustrativa.
Tolerancia: umbral numerico a dos pasos (2000 ADU) del analitico (el ruido de 3 ADU mueve el primer cruce); coeficiente cuadratico recuperado dentro de 5 %.
"""
from __future__ import annotations
import math, platform, random, sys

B, SAT = 1.5e-6, 60000.0

def resp(x):
    return min(SAT, x * (1 - B * x))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    xs = [1000.0 * k for k in range(1, 61)]                  # flujo lineal ideal 1000..60000 ADU (exposiciones crecientes)
    ys = [resp(x) + rng.gauss(0, 3.0) for x in xs]
    bajos = [(x, y) for x, y in zip(xs, ys) if x <= 3000]
    n = len(bajos)
    mx = sum(x for x, _ in bajos) / n
    my = sum(y for _, y in bajos) / n
    a = sum((x - mx) * (y - my) for x, y in bajos) / sum((x - mx) ** 2 for x, _ in bajos)
    c = my - a * mx
    print(f"ajuste lineal a x <= 3000: pendiente {a:.5f}, ordenada {c:.2f} ADU")
    print(f"{'x ideal':>8} {'salida':>9} {'dev. ideal [%]':>15} {'dev. ajuste [%]':>16}")
    umb_n = None
    for x, y in zip(xs, ys):
        pred = a * x + c
        dev_aj = 100 * (y - pred) / pred
        dev = 100 * (y - x) / x            # frente al flujo ideal, conocido en la simulacion
        if x in (5000, 10000, 20000, 30000, 40000, 50000, 60000):
            print(f"{x:8.0f} {y:9.1f} {dev:15.3f} {dev_aj:16.3f}")
        if umb_n is None and dev < -1.0:
            umb_n = x
    umb_a = 0.01 / B
    print(f"umbral de 1 % frente al flujo ideal: analitico x = {umb_a:.0f} ADU ; numerico (primer punto fuera) x = {umb_n:.0f} ADU")
    assert abs(umb_n - umb_a) <= 2000.0
    # coeficiente b recuperado por regresion de y/x frente a x sobre todos los puntos no saturados
    pts = [(x, y / x) for x, y in zip(xs, ys) if resp(x) < SAT]
    m = len(pts)
    mx2 = sum(p[0] for p in pts) / m
    my2 = sum(p[1] for p in pts) / m
    sl = sum((p[0] - mx2) * (p[1] - my2) for p in pts) / sum((p[0] - mx2) ** 2 for p in pts)
    print(f"coeficiente cuadratico recuperado: {-sl:.3e} (verdadero {B:.3e})")
    assert abs(-sl / B - 1) < 0.05
    sat = [x for x in xs if x * (1 - B * x) >= SAT]
    print(f"puntos saturados: {len(sat)} (el flujo ideal ya no mide)")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
