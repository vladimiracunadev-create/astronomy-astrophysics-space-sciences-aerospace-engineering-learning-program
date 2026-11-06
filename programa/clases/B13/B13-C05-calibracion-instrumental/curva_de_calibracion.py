#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C05: curva de calibracion lineal con incertidumbre.

Datos: SINTETICOS. Un fotodiodo de un sensor solar entrega cuentas digitales
(DN) al ser iluminado por una lampara patron con irradiancias conocidas
x = 100, 250, 400, 550, 700, 850, 1000 W/m2 (se suponen sin error frente al
ruido del instrumento). Verdad simulada: y = a + b x con a = 50 DN,
b = 2.50 DN/(W/m2), ruido gaussiano sigma = 8 DN. Semilla fija.
Modelo: minimos cuadrados ordinarios. Con Sxx = sum((x-xm)^2):
  b^ = Sxy/Sxx, a^ = ym - b^ xm, s^2 = sum(r^2)/(n-2),
  u(b^) = s/sqrt(Sxx), u(a^) = s sqrt(1/n + xm^2/Sxx).
Inversion: para m lecturas medias y0 de una fuente desconocida,
  x0 = (y0 - a^)/b^, u(x0) = (s/|b^|) sqrt(1/m + 1/n + (x0-xm)^2/Sxx)
(formula clasica de la calibracion lineal inversa).
Supuestos: relacion lineal, ruido homocedastico, independiente, patrones sin
error. Validez: solo dentro del intervalo de calibracion [100, 1000].
Tolerancia: recta exacta recuperada a 1e-9 sin ruido; u(b) simulada dentro
del 10 % de la teorica (R = 3000 repeticiones).
"""
from __future__ import annotations
import math
import platform
import random
import sys

X = [100.0, 250.0, 400.0, 550.0, 700.0, 850.0, 1000.0]
A_V, B_V, SIGMA = 50.0, 2.50, 8.0


def mco(x, y):
    n = len(x)
    xm, ym = sum(x) / n, sum(y) / n
    sxx = sum((v - xm) ** 2 for v in x)
    sxy = sum((u - xm) * (v - ym) for u, v in zip(x, y))
    b = sxy / sxx
    a = ym - b * xm
    s = math.sqrt(sum((v - (a + b * u)) ** 2 for u, v in zip(x, y)) / (n - 2)) if n > 2 else 0.0
    ub = s / math.sqrt(sxx)
    ua = s * math.sqrt(1 / n + xm * xm / sxx)
    return a, b, s, ua, ub, xm, sxx


def invertir(y0, m, a, b, s, xm, sxx, n):
    x0 = (y0 - a) / b
    u = (s / abs(b)) * math.sqrt(1 / m + 1 / n + (x0 - xm) ** 2 / sxx)
    return x0, u


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: sin ruido la recta se recupera exactamente
    y0 = [A_V + B_V * v for v in X]
    a, b, s, *_ = mco(X, y0)
    assert abs(a - A_V) < 1e-9 and abs(b - B_V) < 1e-9 and s < 1e-9
    # Calibracion con ruido
    rng = random.Random(11)
    y = [A_V + B_V * v + rng.gauss(0, SIGMA) for v in X]
    a, b, s, ua, ub, xm, sxx = mco(X, y)
    print(f"a = {a:.2f} +/- {ua:.2f} DN ; b = {b:.4f} +/- {ub:.4f} DN/(W/m2) ; s = {s:.2f} DN")
    # Prueba 2: dispersion simulada de la pendiente vs teorica
    R = 3000
    pend = []
    for _ in range(R):
        yy = [A_V + B_V * v + rng.gauss(0, SIGMA) for v in X]
        pend.append(mco(X, yy)[1])
    mb = sum(pend) / R
    sd = math.sqrt(sum((v - mb) ** 2 for v in pend) / (R - 1))
    teor = SIGMA / math.sqrt(sxx)
    print(f"u(b) simulada = {sd:.5f} ; teorica = {teor:.5f}")
    assert abs(sd - teor) / teor < 0.10
    # Inversion: una lectura media y0 con m = 5 repeticiones
    y_obs = A_V + B_V * 620.0   # fuente real de 620 W/m2, sin ruido, para ver el sesgo del metodo
    x0, u = invertir(y_obs, 5, a, b, s, xm, sxx, len(X))
    print(f"x0 = {x0:.1f} W/m2 +/- {u:.1f} (verdadero 620.0)")
    assert abs(x0 - 620.0) < 4 * u
    # Prueba 3: u(x0) crece al alejarse del centro de calibracion
    u_c = invertir(a + b * xm, 5, a, b, s, xm, sxx, len(X))[1]
    u_e = invertir(a + b * 1000.0, 5, a, b, s, xm, sxx, len(X))[1]
    print(f"u(x0) en el centro = {u_c:.2f} ; en el extremo (1000) = {u_e:.2f} W/m2")
    assert u_e > u_c
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("FALLO: una prueba no se cumple")
        sys.exit(1)
