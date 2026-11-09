#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C13: regresion de un indice de actividad sobre una funcion de acoplamiento y destreza del pronostico por umbral.

Datos: ninguna constante fisica. La funcion de acoplamiento de prueba v^(4/3) B_T^(2/3) sen^(8/3)(theta/2) (forma funcional ILUSTRATIVA, sin contrastar con la literatura), las distribuciones de v (400 +/- 80 km/s),
de B_T (5 +/- 3 nT) y de theta, el modelo lineal Kp = a + b log10(acoplamiento) + ruido (a = -5, b = 2.2, ruido 0.7) y la semilla fija son ILUSTRATIVOS (sinteticos).
Modelo: 3000 intervalos sinteticos; ajuste de minimos cuadrados de Kp sobre log10 del acoplamiento; R^2 y error de prediccion; pronostico binario de Kp >= 5 con umbral sobre el acoplamiento,
tabla de contingencia y puntuacion de Heidke; barrido del umbral para el mejor Heidke.
Supuestos: relacion lineal en el logaritmo con ruido gaussiano. Validez: ilustrativa; no es el indice real.
Tolerancia: pendiente recuperada dentro de 4 errores estandar de 2.2; Heidke maximo positivo.
"""
from __future__ import annotations
import math, platform, random, sys

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    n = 3000
    xs, ys = [], []
    for _ in range(n):
        v = max(250.0, rng.gauss(400, 80))
        bt = abs(rng.gauss(5, 3)) + 0.5
        th = rng.uniform(0, math.pi)
        c = v ** (4 / 3) * bt ** (2 / 3) * math.sin(th / 2) ** (8 / 3)
        xs.append(math.log10(c + 1e-9))
        ys.append(-5 + 2.2 * xs[-1] + rng.gauss(0, 0.7))
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    a = my - b * mx
    res = [y - (a + b * x) for x, y in zip(xs, ys)]
    s2 = sum(r * r for r in res) / (n - 2)
    errb = math.sqrt(s2 / sxx)
    r2 = 1 - sum(r * r for r in res) / sum((y - my) ** 2 for y in ys)
    print(f"ajuste: a = {a:.3f}, b = {b:.3f} +/- {errb:.3f} (verdadero a = -5, b = 2.2) ; R^2 = {r2:.3f} ; error residual = {math.sqrt(s2):.3f}")
    assert abs(b - 2.2) < 4 * errb
    print(f"{'umbral log10(c)':>16} {'a':>5} {'b':>5} {'c':>5} {'d':>6} {'POD':>6} {'FAR':>6} {'Heidke':>7}")
    mejor = (-1, 0)
    for u in [x / 10 for x in range(int(min(xs) * 10), int(max(xs) * 10), 1)]:
        A = sum(1 for x, y in zip(xs, ys) if x >= u and y >= 5)
        B = sum(1 for x, y in zip(xs, ys) if x >= u and y < 5)
        Cc = sum(1 for x, y in zip(xs, ys) if x < u and y >= 5)
        D = n - A - B - Cc
        den = (A + Cc) * (Cc + D) + (A + B) * (B + D)
        if den == 0 or A + B == 0 or A + Cc == 0:
            continue
        h = 2 * (A * D - B * Cc) / den
        if h > mejor[0]:
            mejor = (h, u, A, B, Cc, D)
        if abs(u * 10 - round(u * 10 / 5) * 5) < 1e-9:
            print(f"{u:16.2f} {A:5d} {B:5d} {Cc:5d} {D:6d} {A / (A + Cc):6.3f} {B / (A + B):6.3f} {h:7.3f}")
    h, u, A, B, Cc, D = mejor
    print(f"mejor umbral = {u:.2f} (en log10 del acoplamiento): a = {A}, b = {B}, c = {Cc}, d = {D} ; POD = {A / (A + Cc):.3f} ; FAR = {B / (A + B):.3f} ; Heidke = {h:.3f}")
    assert h > 0
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
