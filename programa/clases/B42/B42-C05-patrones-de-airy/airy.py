#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C05: patron de Airy de una apertura circular: ceros, FWHM, energia encerrada y criterio de Rayleigh.

Datos: ninguna constante fisica. D = 8 m y lambda = 2,2 um (banda K) son ILUSTRATIVOS; no describen un telescopio concreto.
Modelo: I(x) = [2 J1(x)/x]^2 con x = pi D theta / lambda. J1 se calcula por la integral de Bessel J1(x) = (1/pi) int_0^pi cos(t - x sin t) dt (regla de Simpson, 400 intervalos).
Vias independientes: (a) ceros de J1 por biseccion contra los valores tabulados 3,8317, 7,0156 y 10,1735 (valores de libro, no consultados);
(b) energia encerrada por integracion numerica de 2 pi x I(x) frente a la forma cerrada EE(x) = 1 - J0(x)^2 - J1(x)^2.
Supuestos: pupila circular uniforme sin obstruccion, monocromatica, campo lejano. Validez: telescopio ideal sin aberraciones.
Tolerancia: ceros a 1e-4 ; EE numerica frente a cerrada a 1e-5 ; FWHM = 1,029 lambda/D a 1e-3.
"""
from __future__ import annotations
import math, platform

def bessel(n, x, m=400):
    h = math.pi / m
    s = 0.0
    for i in range(m + 1):
        t = i * h
        f = math.cos(n * t - x * math.sin(t))
        s += f * (1 if i in (0, m) else (4 if i % 2 else 2))
    return s * h / 3 / math.pi

def airy(x):
    return 1.0 if abs(x) < 1e-9 else (2 * bessel(1, x) / x) ** 2

def cero(a, b):
    fa = bessel(1, a)
    for _ in range(60):
        c = 0.5 * (a + b)
        fc = bessel(1, c)
        if fa * fc <= 0:
            b = c
        else:
            a, fa = c, fc
    return 0.5 * (a + b)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    D, lam = 8.0, 2.2e-6
    ldD = lam / D
    print(f"lambda/D = {ldD:.4e} rad = {ldD * 206264.806247:.5f} arcsec")
    tab = (3.8317, 7.0156, 10.1735)
    ceros = [cero(3.0, 4.5), cero(6.0, 7.5), cero(9.5, 11.0)]
    print(f"{'cero':>5} {'x':>10} {'tabla':>8} {'theta/(lambda/D)':>17}")
    for i, (z, t) in enumerate(zip(ceros, tab), 1):
        print(f"{i:5d} {z:10.5f} {t:8.4f} {z / math.pi:17.4f}")
        assert abs(z - t) < 1e-4
    # FWHM
    lo, hi = 0.5, 2.5
    for _ in range(60):
        m = 0.5 * (lo + hi)
        if airy(m) > 0.5:
            lo = m
        else:
            hi = m
    x_half = 0.5 * (lo + hi)
    fwhm = 2 * x_half / math.pi
    print(f"FWHM = {fwhm:.4f} lambda/D (1,029 esperado)")
    assert abs(fwhm - 1.029) < 1e-3
    # energia encerrada
    print(f"{'x':>8} {'EE numerica':>12} {'EE cerrada':>12}")
    peor = 0.0
    for x_e in (ceros[0], ceros[1], ceros[2]):
        n = 2000
        h = x_e / n
        tot = 0.0
        for i in range(n):
            x = (i + 0.5) * h
            tot += airy(x) * x * h
        # normalizacion: la energia total es int_0^inf I x dx = 2 (con I = [2J1/x]^2) => EE = tot / 2
        ee_num = tot / 2
        ee_cer = 1 - bessel(0, x_e) ** 2 - bessel(1, x_e) ** 2
        peor = max(peor, abs(ee_num - ee_cer))
        print(f"{x_e:8.4f} {ee_num:12.6f} {ee_cer:12.6f}")
    assert peor < 1e-5
    ee1 = 1 - bessel(0, ceros[0]) ** 2
    print(f"EE hasta el primer cero = {ee1:.4f} (84 % en el disco de Airy) ; segundo anillo hasta el 2o cero = {1 - bessel(0, ceros[1]) ** 2:.4f}")
    assert abs(ee1 - 0.8378) < 1e-3
    # criterio de Rayleigh: separacion = primer cero
    th_r = 1.21967 * ldD
    x_r = math.pi * th_r / ldD
    print(f"separacion de Rayleigh = {x_r / math.pi:.4f} lambda/D = {th_r * 206264.806247:.5f} arcsec ; primer cero = {ceros[0] / math.pi:.4f} lambda/D")
    assert abs(ceros[0] / math.pi - 1.21967) < 1e-4
    # intensidad en el punto medio de dos fuentes a la separacion de Rayleigh
    mid = 2 * airy(x_r / 2)
    print(f"cociente I(punto medio)/I(pico) a la separacion de Rayleigh = {mid / (1 + airy(x_r)):.4f} (teoria ~ 0,735)")
    assert abs(mid / (1 + airy(x_r)) - 0.735) < 0.01
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
