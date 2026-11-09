#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C12: disco de Airy, criterio de Rayleigh, criterio de Sparrow, regla de Dawes y obstruccion central.

Datos: sin constantes del NIST. D = 200 mm, lambda = 550 nm y obstruccion de razon 0,30 son ILUSTRATIVOS. 206264,806 = 648000/pi (definicion geometrica).
La regla de Dawes, 116/D[mm] segundos de arco, es una relacion empirica de libro NO consultada en esta sesion; aqui solo se compara.
Modelo: I(x) = (2 J1(x)/x)^2 con x = pi D theta / lambda; J0 y J1 por su integral trapezoidal (periodica, espectralmente exacta). Primer cero de J1 por biseccion
(Rayleigh: theta = 3,8317/pi lambda/D). Segunda via: energia encerrada EE(x) = integral numerica de I(x) x dx frente a la forma cerrada 1 - J0^2 - J1^2.
Con obstruccion e: I_e(x) = [2J1(x)/x - e^2 2J1(e x)/(e x)]^2 / (1-e^2)^2.
Supuestos: apertura circular, onda plana monocromatica, campo lejano (Fraunhofer). Validez: difraccion escalar.
Tolerancia: primer cero 3,8317 a 1e-4; EE numerica frente a la forma cerrada 1e-6; punto medio de Rayleigh 0,735 a 2e-3.
"""
from __future__ import annotations
import math, platform, sys

ARCSEC = 648000.0 / math.pi


def Jn(n, x, m=400):
    s = 0.5 * (math.cos(n * 0 - x * 0) + math.cos(n * math.pi - x * 0))
    for i in range(1, m):
        t = math.pi * i / m
        s += math.cos(n * t - x * math.sin(t))
    return s / m


def airy(x):
    return 1.0 if abs(x) < 1e-12 else (2 * Jn(1, x) / x) ** 2


def airy_obs(x, e):
    if abs(x) < 1e-12:
        return 1.0
    a = 2 * Jn(1, x) / x
    b = e * e * 2 * Jn(1, e * x) / (e * x)
    return (a - b) ** 2 / (1 - e * e) ** 2


def cero_j1(a, b):
    for _ in range(100):
        m = 0.5 * (a + b)
        if Jn(1, a) * Jn(1, m) <= 0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)


def ee_numerica(xmax, f=airy, n=4000):
    """Integral de I(x) x dx de 0 a xmax; la total del disco ideal vale 2, asi que EE = integral / 2."""
    h = xmax / n
    s = 0.0
    for i in range(n + 1):
        x = i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * f(x) * x
    return s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    x1 = cero_j1(3.0, 4.5)
    x2 = cero_j1(6.5, 7.5)
    print(f"primeros ceros de J1: {x1:.4f} y {x2:.4f} -> radios de los anillos oscuros {x1/math.pi:.4f} y {x2/math.pi:.4f} lambda/D")
    assert abs(x1 - 3.8317) < 1e-4 and abs(x2 - 7.0156) < 1e-4
    D, lam = 200e-3, 550e-9
    ray = x1 / math.pi * lam / D * ARCSEC
    spar_x = None
    # Sparrow: segunda derivada del punto medio se anula
    def curv(s):
        h = 1e-3
        f = lambda x: airy(x - s / 2) + airy(x + s / 2)
        return (f(h) - 2 * f(0.0) + f(-h)) / (h * h)
    lo, hi = 1.5, 4.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if curv(mid) < 0:
            lo = mid
        else:
            hi = mid
    spar_x = 0.5 * (lo + hi)
    spar = spar_x / math.pi * lam / D * ARCSEC
    dawes = 116.0 / (D * 1e3)
    print(f"D = 200 mm, 550 nm: Rayleigh = {ray:.4f} arcsec ; Sparrow = {spar:.4f} arcsec ({spar_x/math.pi:.4f} lambda/D) ; Dawes (empirica) = {dawes:.4f} arcsec")
    mid_rayleigh = 2 * airy(x1 / 2)
    print(f"intensidad en el punto medio con separacion de Rayleigh = {mid_rayleigh:.4f} del maximo de la suma")
    assert abs(mid_rayleigh - 0.735) < 2e-3
    # energia encerrada
    print(f"{'x':>8} {'EE numerica':>12} {'1-J0^2-J1^2':>12}")
    for x in (1.0, x1, x2, 10.1735):
        num = ee_numerica(x) / 2          # la integral total de I x dx vale 2
        cer = 1 - Jn(0, x) ** 2 - Jn(1, x) ** 2
        print(f"{x:8.4f} {num:12.6f} {cer:12.6f}")
        assert abs(num - cer) < 1e-6
    # obstruccion
    e = 0.30
    print(f"obstruccion e = {e:.2f}")
    print(f"{'':>26} {'sin obstruccion':>16} {'con obstruccion':>16}")
    ee0 = ee_numerica(x1)
    # normalizacion de la EE con obstruccion: energia total = integral hasta infinito; se aproxima con x grande y se normaliza al total del disco
    tot_e = ee_numerica(60.0, lambda x: airy_obs(x, e), n=12000)
    tot_0 = ee_numerica(60.0, airy, n=12000)
    ee1 = ee_numerica(x1, lambda x: airy_obs(x, e)) / tot_e
    ee0n = ee0 / tot_0
    print(f"{'EE hasta x = 3,8317':>26} {ee0n:16.4f} {ee1:16.4f}")
    # primer anillo: intensidad maxima relativa
    pk0 = max(airy(x) for x in [5.0 + 0.001 * i for i in range(1, 1500)])
    pk1 = max(airy_obs(x, e) for x in [4.8 + 0.001 * i for i in range(1, 1500)])
    print(f"{'1er anillo / maximo':>26} {pk0:16.4f} {pk1:16.4f}")
    assert ee1 < ee0n and pk1 > pk0
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
