#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C03: maximos anuales sinteticos, ajuste de Gumbel y periodos de retorno.

Datos: ninguna constante fisica. Los parametros de la distribucion de Gumbel (mu = 100, beta = 30), la longitud del registro (60 anios), las repeticiones (500) y la semilla fija son
ILUSTRATIVOS (sinteticos); no se reproduce ninguna serie historica ni el evento de Carrington.
Modelo: F(x) = exp(-exp(-(x - mu)/beta)); nivel de retorno x_T = mu - beta ln(-ln(1 - 1/T)); ajuste por momentos (beta = s sqrt(6)/pi, mu = media - 0.5772 beta) y por maxima verosimilitud
(iteracion de punto fijo); probabilidad de al menos un evento en N anios 1 - exp(-N/T); intervalo del nivel de 100 anios por 500 registros de 60 anios.
Supuestos: maximos anuales independientes y de Gumbel. Validez: ilustrativa.
Tolerancia: x_T numerico frente al cerrado a 1e-9; el valor verdadero cae en el intervalo 5-95 %.
"""
from __future__ import annotations
import math, platform, random, sys
EULER = 0.5772156649015329

def x_t(mu, beta, t):
    return mu - beta * math.log(-math.log(1 - 1 / t))

def mle(xs):
    n = len(xs)
    m = sum(xs) / n
    s = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    beta = s * math.sqrt(6) / math.pi
    for _ in range(200):
        w = [math.exp(-x / beta) for x in xs]
        nb = m - sum(x * wi for x, wi in zip(xs, w)) / sum(w)
        if abs(nb - beta) < 1e-12:
            break
        beta = nb
    mu = -beta * math.log(sum(math.exp(-x / beta) for x in xs) / n)
    return mu, beta

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    mu, beta = 100.0, 30.0
    print(f"{'T [anios]':>10} {'x_T':>9} {'P(al menos 1 en 10 anios)':>27}")
    for t in (2, 10, 50, 100, 500):
        p = 1 - math.exp(-10 / t)
        print(f"{t:10d} {x_t(mu, beta, t):9.2f} {p:27.4f}")
        F = math.exp(-math.exp(-(x_t(mu, beta, t) - mu) / beta))
        assert abs(F - (1 - 1 / t)) < 1e-9
    rng = random.Random(20261109)
    est_m, est_l = [], []
    for _ in range(500):
        xs = [mu - beta * math.log(-math.log(rng.random())) for _ in range(60)]
        m = sum(xs) / 60
        s = math.sqrt(sum((x - m) ** 2 for x in xs) / 59)
        b1 = s * math.sqrt(6) / math.pi
        est_m.append(x_t(m - EULER * b1, b1, 100))
        mm, bb = mle(xs)
        est_l.append(x_t(mm, bb, 100))
    est_m.sort(); est_l.sort()
    ver = x_t(mu, beta, 100)
    print(f"nivel de 100 anios verdadero = {ver:.2f}")
    print(f"momentos: mediana {est_m[250]:.2f}, 5-95 % [{est_m[25]:.2f}, {est_m[475]:.2f}] ; maxima verosimilitud: mediana {est_l[250]:.2f}, 5-95 % [{est_l[25]:.2f}, {est_l[475]:.2f}]")
    assert est_m[25] < ver < est_m[475] and est_l[25] < ver < est_l[475]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
