#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C14: cuadro maestro de flat y no uniformidad residual.

Datos: ninguna constante fisica. La respuesta de pixel (PRNU de 1,5 %), el vineteo (hasta 15 %) y el nivel de 20 000 e- son ILUSTRATIVOS (sinteticos); no describen una camara real.
Modelo: respuesta r(x,y) = (1 + PRNU) (1 - v rho^2); flat = r * L + ruido de fotones (gaussiano); maestro = media de N flats normalizada por su media; calibrado = cuadro / maestro.
El ruido relativo del maestro es sqrt(media(1/(N r L))) y el residuo de un cuadro uniforme calibrado es sqrt(media((1 + 1/N)/(r L))) (el cuadro con su propio ruido de fotones). Semilla 20261109.
Supuestos: sin bias ni dark (ya restados); iluminacion de flat uniforme. Validez: ilustrativa.
Tolerancia: residuo dentro de 4 % del analitico.
"""
from __future__ import annotations
import math, platform, random, sys

W = 48
N = W * W

def std(xs):
    m = sum(xs) / len(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    resp = []
    for y in range(W):
        for x in range(W):
            rho2 = ((x - (W - 1) / 2) ** 2 + (y - (W - 1) / 2) ** 2) / (2 * ((W - 1) / 2) ** 2)
            resp.append((1 + rng.gauss(0, 0.015)) * (1 - 0.15 * rho2))
    L = 20000.0
    print(f"respuesta verdadera: std relativa {std(resp)/ (sum(resp)/N):.4f} (PRNU + vineteo)")
    print(f"{'N flats':>8} {'ruido maestro':>14} {'analitico':>10} {'residuo cuadro':>15} {'analitico':>10}")
    sal = None
    for nf in (5, 20, 80):
        fl = [[r * L + rng.gauss(0, math.sqrt(r * L)) for r in resp] for _ in range(nf)]
        mm = [sum(f[i] for f in fl) / nf for i in range(N)]
        mn = sum(mm) / N
        maestro = [m / mn for m in mm]
        verdadero = [r / (sum(resp) / N) for r in resp]
        ruido_m = std([a / b for a, b in zip(maestro, verdadero)])
        esc = [r * L + rng.gauss(0, math.sqrt(r * L)) for r in resp]  # cuadro de escena uniforme
        cal = [e / m for e, m in zip(esc, maestro)]
        rel = std(cal) / (sum(cal) / N)
        an_m = math.sqrt(sum(1 / (r * L * nf) for r in resp) / N)
        an_c = math.sqrt(sum((1 + 1 / nf) / (r * L) for r in resp) / N)
        print(f"{nf:8d} {ruido_m:14.6f} {an_m:10.6f} {rel:15.6f} {an_c:10.6f}")
        assert abs(ruido_m / an_m - 1) < 0.15
        assert abs(rel / an_c - 1) < 0.04
        if nf == 80:
            sal = rel
    sin = [r * L + rng.gauss(0, math.sqrt(r * L)) for r in resp]
    print(f"sin flat: no uniformidad {std(sin)/(sum(sin)/N):.4f} ; con flat de 80 cuadros: {sal:.5f}")
    assert std(sin) / (sum(sin) / N) > 4 * sal
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
