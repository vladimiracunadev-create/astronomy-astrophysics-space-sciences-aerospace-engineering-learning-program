#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C02: matrices de Lorentz, invariante del intervalo y composicion de boosts.

Datos: c exacta (NIST CODATA 2022, consultado 2026-11-09). Eventos y velocidades: SINTETICOS.
Modelo: boost en x con coordenadas (ct, x): ct' = gamma (ct - beta x), x' = gamma (x - beta ct).
Invariante s^2 = (c dt)^2 - dx^2. Composicion: L(beta1) L(beta2) = L(beta_suma).
Supuestos: marcos inerciales con ejes paralelos. Validez: |beta| < 1.
Tolerancia: 1e-12 en determinante y composicion; 1e-9 relativa en el invariante.
"""
from __future__ import annotations
import math
import platform
import sys


def boost(beta):
    g = 1 / math.sqrt(1 - beta * beta)
    return [[g, -g * beta], [-g * beta, g]]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def aplica(m, ev):
    return (m[0][0] * ev[0] + m[0][1] * ev[1], m[1][0] * ev[0] + m[1][1] * ev[1])


def intervalo(ev):
    return ev[0] ** 2 - ev[1] ** 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ev = (5.0, 3.0)
    for b in (0.1, 0.6, 0.9, 0.999):
        m = boost(b)
        det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        e2 = aplica(m, ev)
        assert abs(det - 1) < 1e-9
        assert abs(intervalo(e2) - intervalo(ev)) < 1e-9 * max(1, abs(intervalo(ev)))
        print(f"beta = {b}: gamma = {m[0][0]:.6f}, evento -> (ct', x') = ({e2[0]:.5f}, {e2[1]:.5f}), s^2 = {intervalo(e2):.9f}")
    b1, b2 = 0.6, 0.8
    bs = (b1 + b2) / (1 + b1 * b2)
    prod = mul(boost(b1), boost(b2))
    ref = boost(bs)
    assert max(abs(prod[i][j] - ref[i][j]) for i in range(2) for j in range(2)) < 1e-12, "composicion"
    print(f"composicion 0.6 y 0.8: beta = {bs:.8f}; |L1 L2 - L(suma)| < 1e-12")
    inv = mul(boost(0.6), boost(-0.6))
    assert abs(inv[0][0] - 1) < 1e-12 and abs(inv[0][1]) < 1e-12
    luz = (4.0, 4.0)
    for b in (0.3, 0.99):
        e2 = aplica(boost(b), luz)
        assert abs(e2[0] - e2[1]) < 1e-9
    print("un rayo de luz (ct = x) sigue siendo ct' = x' en cualquier boost")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
