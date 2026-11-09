#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C03: antena parabolica de apertura uniforme: geometria, haz de Airy y directividad.

Datos: c de NIST CODATA 2022 (consultada 2026-11-09). El diametro (25 m), la distancia focal (9 m), la frecuencia (1,4 GHz) y la eficiencia (0,6)
son ILUSTRATIVOS; no describen una antena real.
Modelo: paraboloide z = r^2/(4 f); patron de apertura circular uniforme F(x) = 2 J1(x)/x con x = pi D sin(theta)/lambda (J1 por serie);
directividad por integracion numerica del patron frente a (pi D/lambda)^2.
Supuestos: apertura uniforme, campo lejano, sin bloqueo. Validez: orientativa.
Tolerancia: directividad numerica dentro del 0,1 % de la analitica; ancho a media potencia 1,029 lambda/D dentro del 1 %.
"""
from __future__ import annotations
import math, platform
C = 299792458.0

def j1(x):
    if x < 12:
        s, t, k = 0.0, x / 2, 0
        while True:
            term = (-1) ** k * (x / 2) ** (2 * k + 1) / (math.factorial(k) * math.factorial(k + 1))
            s += term
            k += 1
            if abs(term) < 1e-18 and k > 5:
                return s
    # asintotica de Hankel
    mu = 4.0
    p = 1 - (mu - 1) * (mu - 9) / (2 * (8 * x) ** 2)
    q = (mu - 1) / (8 * x) - (mu - 1) * (mu - 9) * (mu - 25) / (6 * (8 * x) ** 3)
    ch = x - 3 * math.pi / 4
    return math.sqrt(2 / (math.pi * x)) * (p * math.cos(ch) - q * math.sin(ch))

def F(x):
    return 1.0 if x == 0 else 2 * j1(x) / x

def calc():
    D, f, nu, eta = 25.0, 9.0, 1.4e9, 0.6
    lam = C / nu
    prof = D ** 2 / (16 * f)
    fD = f / D
    # ancho a media potencia: F^2 = 1/2
    lo, hi = 0.5, 3.0
    for _ in range(80):
        m = 0.5 * (lo + hi)
        if F(m) ** 2 > 0.5:
            lo = m
        else:
            hi = m
    x_half = 0.5 * (lo + hi)
    hpbw = 2 * x_half * lam / (math.pi * D)
    # directividad: Omega = 2 pi/k^2 * int F^2 x dx ; D = 4 pi / Omega = 2 k^2 / int F^2 x dX
    X, n = 600.0, 600000
    h = X / n
    s = 0.0
    for i in range(n):
        x = (i + 0.5) * h
        s += F(x) ** 2 * x
    s *= h
    s += 4 / (math.pi * X)        # cola: promedio de 4 J1^2/x -> 4/(pi x^2)
    k = math.pi * D / lam
    dir_num = 2 * k ** 2 / s
    dir_ana = k ** 2
    return dict(lam=lam, prof=prof, fD=fD, hpbw=hpbw, hpbw_lam=hpbw * D / lam, dir_num=dir_num, dir_ana=dir_ana, eta=eta,
                G_dB=10 * math.log10(eta * dir_ana), Ae=eta * math.pi * D ** 2 / 4, x_half=x_half, s=s, D=D)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"lambda = {r['lam']*100:.3f} cm ; f/D = {r['fD']:.3f} ; profundidad del plato = {r['prof']:.3f} m")
    print(f"x_1/2 = {r['x_half']:.5f} ; HPBW = {math.degrees(r['hpbw'])*60:.2f} arcmin = {r['hpbw_lam']:.4f} lambda/D")
    print(f"integral de F^2 x dx = {r['s']:.5f} (analitica 2.00000)")
    print(f"directividad numerica = {r['dir_num']:.1f} ; analitica (pi D/lambda)^2 = {r['dir_ana']:.1f}")
    print(f"con eta = {r['eta']}: G = {r['G_dB']:.2f} dBi ; A_e = {r['Ae']:.1f} m^2")
    assert abs(r["dir_num"] / r["dir_ana"] - 1) < 1e-3
    assert abs(r["hpbw_lam"] / 1.029 - 1) < 0.01
    assert abs(r["prof"] - 25 ** 2 / 144) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
