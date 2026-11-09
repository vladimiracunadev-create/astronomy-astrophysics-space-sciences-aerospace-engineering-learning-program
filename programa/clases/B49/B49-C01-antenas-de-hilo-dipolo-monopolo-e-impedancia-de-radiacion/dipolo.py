#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C01: resistencia de radiacion, directividad y longitud de un dipolo y de un monopolo de hilo delgado.

Datos: la impedancia caracteristica del vacio eta = 376.730313412 ohm y c = 299792458 m/s (NIST, CODATA 2022, tabla allascii.txt, consultada el 2026-11-09). Las longitudes de antena (L/lambda) y la
frecuencia de 150 MHz del ejemplo son ILUSTRATIVAS; no describen ninguna antena real.
Modelo: hilo delgado con corriente sinusoidal I(z) = I0 sin(k(h-|z|)); campo lejano F(theta) = [cos(kh cos theta) - cos(kh)]/sin theta; potencia radiada por integracion numerica de [cos(kh cos theta) - cos(kh)]^2/sin theta
(regla del punto medio, 20000 puntos) y R_pico = eta/(2 pi) * integral, referida a la corriente maxima I0. Verificacion independiente con la serie de la funcion Cin: R(media onda) = eta/(4 pi) Cin(2 pi).
Supuestos: hilo de radio nulo, sin perdidas, en el espacio libre; el monopolo es la mitad del dipolo sobre un plano conductor infinito y perfecto. Validez: L/lambda <= 1,5; la reactancia no se calcula.
Tolerancia: integral numerica frente a la serie Cin a 1e-6 relativo; dipolo corto (R_in, referida a la corriente de alimentacion) frente a la formula 20 pi^2 (L/lambda)^2 a 2 % para L/lambda = 0,02.
"""
from __future__ import annotations
import math, platform

ETA = 376.730313412      # ohm, NIST
C = 299792458.0          # m/s, NIST


def integral_f2(kh, n=20000):
    """Integral de [cos(kh cos th) - cos(kh)]^2 / sin(th) sobre [0, pi] por punto medio."""
    s = 0.0
    for i in range(n):
        th = (i + 0.5) * math.pi / n
        f = math.cos(kh * math.cos(th)) - math.cos(kh)
        s += f * f / math.sin(th)
    return s * math.pi / n


def directividad(kh, n=20000):
    """D = 2 F_max^2 / integral(F^2 sin theta) (campo F con corriente maxima; hilo en el eje z)."""
    num = 0.0
    fmax = 0.0
    for i in range(n):
        th = (i + 0.5) * math.pi / n
        f = (math.cos(kh * math.cos(th)) - math.cos(kh)) / math.sin(th)
        num += f * f * math.sin(th)
        fmax = max(fmax, abs(f))
    num *= math.pi / n
    return 2.0 * fmax * fmax / num


def cin(x):
    """Cin(x) = suma_{k>=1} (-1)^(k+1) x^(2k) / (2k (2k)!)."""
    s = 0.0
    t = 1.0
    for k in range(1, 60):
        t *= x * x / ((2 * k - 1) * (2 * k))
        s += (-1) ** (k + 1) * t / (2 * k)
    return s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"eta = {ETA} ohm (NIST) ; 120 pi = {120 * math.pi:.6f} ohm")
    print("Dipolo de longitud total L (h = L/2, k h = pi L / lambda):")
    print(f"{'L/lambda':>9} {'R_pico (ohm)':>13} {'D':>7} {'D (dBi)':>8} {'R_in (ohm)':>11}")
    filas = {}
    for lr in (0.02, 0.1, 0.25, 0.5, 0.75, 1.25):
        kh = math.pi * lr
        r = ETA / (2 * math.pi) * integral_f2(kh)
        d = directividad(kh)
        sn = math.sin(kh)
        rin = r / (sn * sn) if abs(sn) > 1e-3 else float("inf")
        filas[lr] = (r, d)
        print(f"{lr:9.2f} {r:13.4f} {d:7.4f} {10 * math.log10(d):8.3f} {rin:11.4f}")
    r_half = filas[0.5][0]
    r_cin = ETA / (4 * math.pi) * cin(2 * math.pi)
    r_120 = 30.0 * cin(2 * math.pi)
    print(f"Media onda: integral numerica = {r_half:.5f} ohm ; serie Cin = {r_cin:.5f} ohm ; con 120 pi = {r_120:.5f} ohm")
    assert abs(r_half / r_cin - 1) < 1e-6
    r_short = filas[0.02][0] / math.sin(math.pi * 0.02) ** 2
    r_formula = 20 * math.pi ** 2 * 0.02 ** 2 * (ETA / (120 * math.pi))
    print(f"Dipolo corto L = 0,02 lambda (referido a la corriente de alimentacion): numerico = {r_short:.5f} ohm ; formula 20 pi^2 (L/lambda)^2 = {r_formula:.5f} ohm ; dif = {abs(r_short / r_formula - 1) * 100:.3f} %")
    assert abs(r_short / r_formula - 1) < 0.02
    assert abs(filas[0.5][1] - 1.6410) < 5e-3
    print("Monopolo sobre plano perfecto (mitad del dipolo): longitud h = L/2")
    r_mono = r_half / 2
    d_mono = 2 * filas[0.5][1]
    print(f"  cuarto de onda: R = {r_mono:.4f} ohm ; D = {d_mono:.4f} ({10 * math.log10(d_mono):.3f} dBi)")
    assert abs(r_mono - r_half / 2) < 1e-12
    f_hz = 150e6
    lam = C / f_hz
    print(f"A 150 MHz: lambda = {lam:.5f} m ; dipolo de media onda L = {lam / 2:.5f} m ; monopolo L = {lam / 4:.5f} m")
    assert abs(lam - 1.99861638667) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
