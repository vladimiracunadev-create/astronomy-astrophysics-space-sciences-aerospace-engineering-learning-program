#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C04: producto de incertidumbres de un paquete gaussiano y de una particula en una caja.

Datos: hbar = h/(2 pi), m_e y e (NIST CODATA 2022), consultados 2026-11-09. La anchura del paquete (sigma_x = 1, unidades con hbar = 1), la malla (512 puntos, 40 unidades), el ancho de
la caja y el confinamiento de 0.1 nm son ILUSTRATIVOS (sinteticos).
Modelo: (1) paquete gaussiano psi(x) ~ exp(-x^2/(4 sigma^2)); la transformada de Fourier discreta (O(N^2), sin bibliotecas) da la distribucion de momentos y sigma_p; producto sigma_x sigma_p
frente a hbar/2; (2) particula en una caja con psi_n = sqrt(2/L) sen(n pi x/L): sigma_x^2 = <x^2> - <x>^2 y sigma_p^2 = <p^2> por integracion de Simpson, frente a la forma cerrada
sigma_x sigma_p = hbar sqrt(n^2 pi^2/12 - 1/2); (3) confinamiento de un electron en 0.1 nm: cota hbar/(2 Delta x) y energia cinetica asociada.
Supuestos: funciones de onda reales y normalizadas, 1D. Validez: exacta para el modelo.
Tolerancia: paquete gaussiano a 1e-3; caja a 1e-6.
"""
from __future__ import annotations
import cmath
import math
import platform
import sys

H, E, ME = 6.62607015e-34, 1.602176634e-19, 9.1093837139e-31
HBAR = H / (2 * math.pi)


def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # paquete gaussiano
    n, big_l = 512, 40.0
    dx = big_l / n
    sig = 1.0
    xs = [(i - n // 2) * dx for i in range(n)]
    psi = [math.exp(-x * x / (4 * sig * sig)) for x in xs]
    nrm = math.sqrt(sum(abs(p) ** 2 for p in psi) * dx)
    psi = [p / nrm for p in psi]
    sx = math.sqrt(sum(x * x * abs(p) ** 2 for x, p in zip(xs, psi)) * dx)
    # DFT: psi~(k) = sum psi(x) exp(-i k x) dx ; k_j = 2 pi (j - n/2)/L
    ks = [2 * math.pi * (j - n // 2) / big_l for j in range(n)]
    phi = [sum(psi[i] * cmath.exp(-1j * ks[j] * xs[i]) for i in range(n)) * dx for j in range(n)]
    nk = sum(abs(p) ** 2 for p in phi) * (2 * math.pi / big_l)
    sk = math.sqrt(sum(k * k * abs(p) ** 2 for k, p in zip(ks, phi)) * (2 * math.pi / big_l) / nk)
    print(f"paquete gaussiano (hbar = 1): sigma_x = {sx:.5f} ; sigma_p = {sk:.5f} ; producto = {sx * sk:.5f} ; hbar/2 = 0.50000")
    assert abs(sx * sk / 0.5 - 1) < 1e-3
    # caja
    print(f"{'n':>2} {'sigma_x/L':>10} {'sigma_p L/hbar':>15} {'producto/hbar numerico':>23} {'sqrt(n^2 pi^2/12 - 1/2)':>25}")
    for nn in (1, 2, 3):
        f = lambda x: 2 * math.sin(nn * math.pi * x) ** 2          # |psi|^2 en unidades de L = 1
        mx = simpson(lambda x: x * f(x), 0, 1)
        mx2 = simpson(lambda x: x * x * f(x), 0, 1)
        sxn = math.sqrt(mx2 - mx * mx)
        p2 = simpson(lambda x: 2 * (nn * math.pi * math.cos(nn * math.pi * x)) ** 2, 0, 1)   # <p^2> hbar^-2 L^2 = int |psi'|^2
        spn = math.sqrt(p2)
        ana = math.sqrt(nn * nn * math.pi ** 2 / 12 - 0.5)
        print(f"{nn:2d} {sxn:10.5f} {spn:15.5f} {sxn * spn:23.6f} {ana:25.6f}")
        assert abs(sxn * spn / ana - 1) < 1e-6, f"caja n={nn}"
    # confinamiento
    dxc = 0.1e-9
    dp = HBAR / (2 * dxc)
    print(f"electron confinado en Delta x = 0.1 nm: Delta p >= {dp:.4e} kg m/s ; velocidad tipica {dp / ME:.4e} m/s ; energia cinetica minima (Delta p)^2/(2 m) = {dp ** 2 / (2 * ME) / E:.4f} eV")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
