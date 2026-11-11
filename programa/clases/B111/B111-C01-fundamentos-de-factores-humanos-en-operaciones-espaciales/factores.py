#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B111-C01: capacidades y limites humanos con la ley de Fitts y la ley de Hick-Hyman.

Modelos (relaciones estandar, no consultadas en una fuente concreta; Fitts 1954 solo en metadatos):
  Fitts (formulacion de Shannon): ID = log2(D/W + 1) [bit]; MT = a + b * ID [s].
  Hick-Hyman: TR = c + d * log2(n + 1) [s], n opciones equiprobables.
Parametros SINTETICOS (ilustrativos, no medidos en personas): a = 0.20 s, b = 0.15 s/bit, c = 0.25 s, d = 0.18 s/bit.
Guante: SINTETICO, reduce el ancho efectivo del objetivo W a 0.7 W. Distancias D en mm, anchos W en mm.
Segunda via: se generan 200 pares (ID, MT) con ruido gaussiano (semilla 111, sigma = 0.03 s) y se recuperan a y b por
minimos cuadrados; tolerancia: |a_est - a| < 0.02 s y |b_est - b| < 0.01 s/bit.
Supuestos: movimiento apuntado en una dimension, sin errores, usuario entrenado, sin microgravedad modelada.
"""
from __future__ import annotations
import math, platform, random

A, B, C, D_H = 0.20, 0.15, 0.25, 0.18
GUANTE = 0.7


def indice(d, w):
    return math.log2(d / w + 1.0)


def mt(d, w):
    return A + B * indice(d, w)


def hick(n):
    return C + D_H * math.log2(n + 1.0)


def minimos_cuadrados(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Fitts SINTETICO: MT = 0.20 + 0.15 ID [s]; guante: W_eff = 0.7 W")
    print("  D [mm]  W [mm]  ID sin guante [bit]  MT sin guante [s]  ID guante [bit]  MT guante [s]  aumento [%]")
    for d in (50.0, 100.0, 200.0):
        for w in (10.0, 20.0):
            i0, i1 = indice(d, w), indice(d, w * GUANTE)
            print(f"  {d:6.0f}  {w:6.0f}  {i0:18.4f}  {mt(d, w):17.4f}  {i1:15.4f}  {mt(d, w * GUANTE):13.4f}  {100 * (mt(d, w * GUANTE) / mt(d, w) - 1):10.2f}")
    print("Hick-Hyman SINTETICO: TR = 0.25 + 0.18 log2(n+1) [s]")
    print("  n opciones  TR [s]  incremento frente a n-1 [s]")
    previo = None
    for n in (1, 2, 4, 8, 16):
        t = hick(n)
        print(f"  {n:10d}  {t:6.4f}  {'-' if previo is None else format(t - previo, '.4f'):>8s}")
        previo = t
    rng = random.Random(111)
    xs, ys = [], []
    for _ in range(200):
        d = rng.uniform(30.0, 300.0)
        w = rng.uniform(5.0, 30.0)
        x = indice(d, w)
        xs.append(x)
        ys.append(A + B * x + rng.gauss(0.0, 0.03))
    a_est, b_est = minimos_cuadrados(xs, ys)
    print(f"Segunda via (ajuste de 200 datos sinteticos, semilla 111): a_est = {a_est:.4f} s ; b_est = {b_est:.4f} s/bit")
    print(f"  errores: |a_est - a| = {abs(a_est - A):.4f} s ; |b_est - b| = {abs(b_est - B):.4f} s/bit")
    cap = indice(100.0, 20.0) / mt(100.0, 20.0)
    print(f"Capacidad aparente (D = 100 mm, W = 20 mm) = ID/MT = {cap:.3f} bit/s")
    assert abs(a_est - A) < 0.02 and abs(b_est - B) < 0.01
    assert mt(100.0, 20.0 * GUANTE) > mt(100.0, 20.0)
    assert abs(indice(100.0, 20.0) - math.log2(6.0)) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
