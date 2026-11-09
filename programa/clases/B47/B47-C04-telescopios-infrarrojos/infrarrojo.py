#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C04: ley de Planck, desplazamiento de Wien y fondo termico de un telescopio infrarrojo.

Datos: h, c, k_B, constante de Stefan-Boltzmann (5,670374419e-8 W m-2 K-4) y constante de desplazamiento de Wien (2,897771955e-3 m K) de NIST CODATA 2022
(allascii.txt, consultada el 2026-11-09). ILUSTRATIVOS (no son valores de ningun telescopio): area colectora A = pi (0,5)^2 m2, emisividad efectiva 0,05,
transmision 0,5, pixel de 0,1 arcsec, banda 9-11 micrometros y corriente de oscuridad 1 e-/s.
Modelo: (1) integral numerica de pi B_lambda frente a sigma T^4; (2) maximo de B_lambda hallado por busqueda frente a b/T; (3) tasa de fotones termicos por pixel
N = eps eta A Omega integral B_lambda lambda/(hc) dlambda para varias temperaturas y la temperatura en que iguala la corriente de oscuridad (biseccion).
Supuestos: emision de cuerpo gris, sin fondo zodiacal ni emision de la atmosfera residual. Validez: ilustrativa.
Tolerancia: integral de Planck frente a sigma T^4, 1e-6 relativo; maximo de Wien, 1e-5 relativo.
"""
from __future__ import annotations
import math, platform

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
SIGMA = 5.670374419e-8
WIEN = 2.897771955e-3
ARCSEC = math.pi / 180 / 3600


def planck(lam, t):
    x = H * C / (lam * KB * t)
    if x > 700:
        return 0.0
    return 2 * H * C ** 2 / lam ** 5 / math.expm1(x)


def integral_planck(t, n=200000):
    # integral de pi*B_lambda dlambda con cambio u = ln(lambda), regla del trapecio
    lo = math.log(2.898e-3 / t * 0.05)
    hi = math.log(2.898e-3 / t * 400)
    h = (hi - lo) / n
    s = 0.0
    for k in range(n + 1):
        lam = math.exp(lo + k * h)
        w = 0.5 if k in (0, n) else 1.0
        s += w * planck(lam, t) * lam
    return math.pi * s * h


def pico(t):
    a, b = 0.2 * WIEN / t, 5 * WIEN / t
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        c1, d1 = b - g * (b - a), a + g * (b - a)
        if planck(c1, t) > planck(d1, t):
            b = d1
        else:
            a = c1
    return 0.5 * (a + b)


def fotones_pixel(t, l1=9e-6, l2=11e-6, eps=0.05, eta=0.5, area=math.pi * 0.5 ** 2, pix=0.1, n=2000):
    omega = (pix * ARCSEC) ** 2
    h = (l2 - l1) / n
    s = 0.0
    for k in range(n + 1):
        lam = l1 + k * h
        w = 1 if k in (0, n) else (4 if k % 2 else 2)
        s += w * planck(lam, t) * lam / (H * C)
    return eps * eta * area * omega * s * h / 3


def calc():
    r = {}
    r["sigma_h"] = 2 * math.pi ** 5 * KB ** 4 / (15 * H ** 3 * C ** 2)
    r["int"] = {}
    for t in (3, 40, 290, 5772):
        r["int"][t] = (integral_planck(t), SIGMA * t ** 4)
    r["pico"] = {t: (pico(t), WIEN / t) for t in (40, 80, 290)}
    r["foton"] = {t: fotones_pixel(t) for t in (290, 150, 80, 40)}
    a, b = 20.0, 290.0
    for _ in range(80):
        m = 0.5 * (a + b)
        if fotones_pixel(m) > 1.0:
            b = m
        else:
            a = m
    r["t_oscuridad"] = 0.5 * (a + b)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"sigma desde h, c, k_B = {r['sigma_h']:.9e} W m-2 K-4 ; NIST = {SIGMA:.9e}")
    print(f"{'T [K]':>8} {'integral pi*B':>16} {'sigma T^4':>16}")
    for t, (a, b) in r["int"].items():
        print(f"{t:8d} {a:16.6e} {b:16.6e}")
        assert abs(a - b) / b < 1e-6
    for t, (a, b) in r["pico"].items():
        print(f"T = {t} K: maximo de B_lambda en {a*1e6:.4f} um ; Wien b/T = {b*1e6:.4f} um")
        assert abs(a - b) / b < 1e-5
    for t, n in r["foton"].items():
        print(f"fondo termico 9-11 um por pixel a {t} K: {n:.4e} fotones/s")
    print(f"temperatura donde el fondo iguala 1 e-/s: {r['t_oscuridad']:.2f} K")
    assert abs(r["sigma_h"] - SIGMA) / SIGMA < 1e-8
    assert r["foton"][290] > r["foton"][150] > r["foton"][80] > r["foton"][40]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
