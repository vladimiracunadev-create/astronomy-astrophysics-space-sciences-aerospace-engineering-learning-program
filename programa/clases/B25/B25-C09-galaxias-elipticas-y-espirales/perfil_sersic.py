#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C09: perfil de Sersic, radio efectivo y fraccion de luz.

Datos: ninguna medida; galaxias SINTETICAS: una eliptica (n = 4, R_e = 5 kpc) y un disco (n = 1,
R_d = 2,6 kpc, el de C01 por Bland-Hawthorn y Gerhard 2016, arXiv:1602.07702, PDF consultado
2026-11-09). Perfil: I(R) = I_e exp(-b_n [(R/R_e)^(1/n) - 1]), con b_n tal que la mitad de la luz
cae dentro de R_e, es decir P(2n, b_n) = 1/2 (P = gamma incompleta regularizada inferior).
Modelo: simetria circular proyectada, sin elipticidad ni isofotas.
Supuestos: perfil de una sola componente, sin polvo.
Validez: ilustrativa; los perfiles reales tienen varias componentes. Tolerancias: 1e-9 (casos
analiticos n = 1/2 y n = 1) y 1e-6 (cuadratura de la luz total).
Referencias independientes: n = 1/2 da P(1, x) = 1 - e^-x, luego b = ln 2; n = 1 da
P(2, x) = 1 - (1 + x) e^-x (la fraccion del disco exponencial de C01), luego b_1 = 1,67835.
"""
from __future__ import annotations
import math
import platform
import sys


def gamma_p(a, x):
    """Gamma incompleta regularizada inferior por serie (valida para todo x > 0)."""
    if x <= 0:
        return 0.0
    term = 1.0 / a
    s = term
    k = 1
    while term > 1e-17 * s:
        term *= x / (a + k)
        s += term
        k += 1
        if k > 10000:
            break
    return s * math.exp(-x + a * math.log(x) - math.lgamma(a))


def b_n(n):
    lo, hi = 1e-9, 60.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if gamma_p(2 * n, mid) < 0.5:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def frac_dentro(x_re, n):
    """Fraccion de luz dentro de R = x_re R_e."""
    return gamma_p(2 * n, b_n(n) * x_re ** (1.0 / n))


def luz_total(n, ie=1.0, re=1.0):
    b = b_n(n)
    return 2 * math.pi * n * math.exp(b) * b ** (-2 * n) * math.gamma(2 * n) * ie * re * re


def luz_numerica(n, u_max=40.0, N=200000):
    """int 2 pi R I dR con el cambio u = (R/Re)^(1/n): R = u^n, dR = n u^(n-1) du (integrando suave)."""
    b = b_n(n)
    f = lambda u: 2 * math.pi * u ** n * math.exp(-b * (u - 1)) * n * u ** (n - 1)
    h = u_max / N
    s = f(0.0) + f(u_max)
    for i in range(1, N):
        s += (4 if i % 2 else 2) * f(i * h)
    return s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: n = 1/2 -> b = ln 2 (caso analitico exacto)
    assert abs(b_n(0.5) - math.log(2)) < 1e-9
    # Prueba 2: n = 1 -> raiz de 1 - (1+x) e^-x = 1/2 por biseccion independiente
    lo, hi = 0.0, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if 1 - (1 + mid) * math.exp(-mid) < 0.5:
            lo = mid
        else:
            hi = mid
    assert abs(b_n(1.0) - 0.5 * (lo + hi)) < 1e-9
    # Prueba 3: luz total cerrada frente a cuadratura (en la variable suave u = (R/Re)^(1/n))
    for n in (1.0, 4.0):
        assert abs(luz_numerica(n) / luz_total(n) - 1) < 1e-6, f"luz total n={n}"
    for n in (1.0, 2.0, 4.0):
        print(f"n = {n:.0f}: b_n = {b_n(n):.5f} ; L(<0.1 Re)/L = {frac_dentro(0.1, n):.4f} ; L(<Re)/L = {frac_dentro(1.0, n):.4f} ; L(<3 Re)/L = {frac_dentro(3.0, n):.4f}")
    print(f"n = 1: R_e / R_d = b_1 = {b_n(1.0):.5f}  (R_d = 2.6 kpc -> R_e = {b_n(1.0) * 2.6:.2f} kpc)")
    print(f"I(0)/I_e: n = 1 -> {math.exp(b_n(1.0)):.2f} ; n = 4 -> {math.exp(b_n(4.0)):.0f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
