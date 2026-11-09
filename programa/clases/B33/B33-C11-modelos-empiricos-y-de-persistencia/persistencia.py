#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C11: pronostico de persistencia y de recurrencia de 27 dias frente a la climatologia.

Datos: ninguna constante fisica. La serie diaria sintetica (media 4, componente recurrente de periodo 27 dias y amplitud 1.5, AR(1) de coeficiente 0.6 y ruido 0.8), los 3000 dias y la semilla fija son
ILUSTRATIVOS (sinteticos); la recurrencia de 27 dias es una suposicion del generador y no se contrasta con datos.
Modelo: pronosticos a 1 dia por persistencia, a 27 dias por recurrencia (valor de hace 27 dias) y por climatologia (media); errores cuadraticos medios, destreza MSSS = 1 - MSE/MSE_clim y correlacion;
barrido de pronosticos de recurrencia con desfases de 20 a 34 dias para mostrar el maximo en 27.
Supuestos: serie estacionaria con componente periodico. Validez: ilustrativa.
Tolerancia: el desfase de mayor correlacion es 27 dias; la persistencia a 1 dia supera a la climatologia.
"""
from __future__ import annotations
import math, platform, random, sys

def pearson(a, b):
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    n = 3000
    ar = 0.0
    y = []
    for t in range(n):
        ar = 0.6 * ar + rng.gauss(0, 0.8)
        y.append(4.0 + 1.5 * math.sin(2 * math.pi * t / 27) + ar)
    clim = sum(y) / n
    def mse(pr, ob):
        return sum((a - b) ** 2 for a, b in zip(pr, ob)) / len(ob)
    base = mse([clim] * n, y)
    print(f"{'metodo':<26} {'MSE':>8} {'MSSS':>8} {'correlacion':>12}")
    for nombre, lag in (("climatologia", None), ("persistencia 1 dia", 1), ("recurrencia 27 dias", 27), ("persistencia 14 dias", 14)):
        if lag is None:
            pr, ob = [clim] * n, y
        else:
            pr, ob = y[:-lag], y[lag:]
        m = mse(pr, ob)
        c = pearson(pr, ob) if lag else float("nan")
        print(f"{nombre:<26} {m:8.3f} {1 - m / base:8.3f} {c:12.3f}")
    cs = {lag: pearson(y[:-lag], y[lag:]) for lag in range(20, 35)}
    mejor = max(cs, key=cs.get)
    print("correlacion por desfase: " + ", ".join(f"{k}:{v:.3f}" for k, v in cs.items() if k in (20, 24, 26, 27, 28, 30, 34)))
    print(f"desfase de mayor correlacion = {mejor} dias")
    assert mejor == 27
    assert 1 - mse(y[:-1], y[1:]) / base > 0
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
