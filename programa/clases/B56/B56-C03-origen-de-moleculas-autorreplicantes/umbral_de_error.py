#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C03: umbral de error de Eigen para un replicador de pico unico.

Datos: SINTETICOS e ILUSTRATIVOS (fidelidad por nucleotido q, ventaja selectiva sigma). No
son tasas medidas de ningun replicador real.
Modelo: poblacion de una secuencia maestra (fraccion x) y mutantes. Replicacion de la maestra
con tasa sigma y calidad Q = q^L (probabilidad de copia sin error); los mutantes tienen tasa 1; se ignora la
retromutacion. Con flujo constante phi = media de la tasa, dx/dt = x (sigma Q - phi) y
phi = sigma x + (1 - x) (la maestra produce sigma copias por unidad de tiempo, una fraccion
1-Q de ellas mutada). Estacionario: x* = (sigma Q - 1)/(sigma - 1) si sigma Q > 1.
Longitud maxima aproximada: L_max ~ ln(sigma)/(1-q) (q cercano a 1).
Supuestos: pico unico, sin retromutacion. Validez: orden de magnitud. Tolerancia: 1e-6
entre la integracion RK4 y la forma cerrada.
"""
from __future__ import annotations
import math
import platform
import sys


def x_estacionario(q, L, sigma):
    Q = q ** L
    return max(0.0, (sigma * Q - 1) / (sigma - 1))


def integrar(q, L, sigma, x0=0.5, t_fin=400.0, dt=0.01):
    Q = q ** L

    def f(x):
        phi = sigma * x + (1 - x)
        return x * (sigma * Q - phi)

    x = x0
    for _ in range(int(t_fin / dt)):
        k1 = f(x)
        k2 = f(x + dt * k1 / 2)
        k3 = f(x + dt * k2 / 2)
        k4 = f(x + dt * k3)
        x += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x


def l_max(q, sigma):
    return math.log(sigma) / (1 - q)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    sigma = 10.0
    for q, L in ((0.99, 100), (0.99, 300), (0.999, 1000)):
        xc = x_estacionario(q, L, sigma)
        xn = integrar(q, L, sigma)
        print(f"q={q}, L={L}: Q={q ** L:.4f} ; x* cerrada={xc:.5f} ; RK4={xn:.5f}")
        assert abs(xc - xn) < 1e-6 or (xc == 0 and xn < 1e-6)
    # Prueba 2: en L = ln(sigma)/(-ln q) la maestra se extingue (sigma Q = 1)
    q = 0.99
    L_exacto = math.log(sigma) / (-math.log(q))
    assert abs(sigma * q ** L_exacto - 1) < 1e-12
    print(f"q={q}: L_exacto={L_exacto:.1f} ; aproximacion ln(sigma)/(1-q)={l_max(q, sigma):.1f}")
    assert abs(L_exacto - l_max(q, sigma)) / L_exacto < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
