#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C06: patron de Airy, ventana angular y contrastes planeta-estrella (luz reflejada y emision termica).

Datos: h, c, k_B (NIST CODATA 2022); R_sol, R_J(eq), R_E(eq), T_eff = 5772 K (IAU 2015 B3); 1 au (IERS TN36), consultados 2026-11-09. Contexto: la
imagen directa con optica adaptativa y coronografos detecta planetas gigantes autoluminosos (Bowler, arXiv:1605.02731, resumen, consultado 2026-11-09).
Las albedos (0.5 y 0.3), el diametro del telescopio (8 m), las longitudes de onda (1.6 y 10 um), la distancia (10 pc) y las temperaturas planetarias
(125 y 255 K) son ILUSTRATIVOS.
Modelo: patron de Airy I(x)/I0 = [2 J1(x)/x]^2, x = pi D theta/lambda, J1(x) = (1/pi) Int_0^pi cos(tau - x sen tau) dtau (cuadratura numerica);
primer anillo oscuro en la primera raiz de J1 (biseccion) ~ 3.8317 -> theta = 1.2197 lambda/D. Contraste reflejado C = A_g (Rp/a)^2 (fase de Lambert para
alfa = 90 grados: 1/pi); contraste termico (Rp/Rs)^2 B(lambda, Tp)/B(lambda, T*).
Supuestos: disco estelar sin resolver, planeta esferico, albedo geometrico constante. Validez: orientativa.
Tolerancia: raiz de J1 en 3.8317 +/- 1e-4; J1 numerica frente a la serie de potencias a 1e-9.
"""
from __future__ import annotations
import math
import platform
import sys

H, C, KB = 6.62607015e-34, 299792458.0, 1.380649e-23
R_SOL, R_JUP, R_EAR, T_SOL = 6.957e8, 7.1492e7, 6.3781e6, 5772.0
AU = 1.49597870700e11
PC = 648000 / math.pi * AU


def j1(x, n=2000):
    h = math.pi / n
    s = math.cos(0 - x * math.sin(0)) + math.cos(math.pi - x * math.sin(math.pi))
    for i in range(1, n):
        t = i * h
        s += (4 if i % 2 else 2) * math.cos(t - x * math.sin(t))
    return s * h / 3 / math.pi


def j1_serie(x, terminos=40):
    s = 0.0
    for k in range(terminos):
        s += (-1) ** k * (x / 2) ** (2 * k + 1) / (math.factorial(k) * math.factorial(k + 1))
    return s


def airy(x):
    return 1.0 if x == 0 else (2 * j1(x) / x) ** 2


def planck(lam, t):
    return 2 * H * C ** 2 / lam ** 5 / math.expm1(H * C / (lam * KB * t))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for x in (0.5, 2.0, 5.0, 10.0):
        assert abs(j1(x) - j1_serie(x)) < 1e-9, "J1 numerica frente a la serie"
    lo, hi = 3.0, 5.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if j1(lo) * j1(mid) <= 0:
            hi = mid
        else:
            lo = mid
    x0 = 0.5 * (lo + hi)
    assert abs(x0 - 3.8317) < 1e-4
    print(f"primera raiz de J1 = {x0:.5f} -> primer anillo oscuro en theta = {x0 / math.pi:.4f} lambda/D (1.22 lambda/D es el criterio de Rayleigh)")
    print(f"{'x':>6} {'I/I0':>12}")
    for x in (0.0, 1.0, 2.0, 3.0, x0, 5.0, 5.14, 7.0):
        print(f"{x:6.3f} {airy(x):12.5e}")
    # ventana angular de un telescopio de 8 m
    d_t, lam, dist = 8.0, 1.6e-6, 10 * PC
    th = 1.22 * lam / d_t
    print(f"D = {d_t} m, lambda = 1.6 um: 1.22 lambda/D = {th:.4e} rad = {th * 206264.806:.4f} arcsec -> separacion fisica a 10 pc = {th * dist / AU:.3f} au")
    # contrastes reflejados
    print(f"{'planeta':<9} {'a [au]':>7} {'albedo':>7} {'C reflejado (alfa = 90)':>24}")
    for nombre, rp, a, ag in (("Jupiter", R_JUP, 5.2012, 0.5), ("Tierra", R_EAR, 1.0, 0.3)):
        c = ag * (rp / (a * AU)) ** 2 / math.pi
        print(f"{nombre:<9} {a:7.4f} {ag:7.2f} {c:24.4e}")
    # contraste termico
    print(f"{'planeta':<9} {'T [K]':>6} {'lambda [um]':>12} {'C termico':>12}")
    for nombre, rp, tp in (("Jupiter", R_JUP, 125.0), ("Tierra", R_EAR, 255.0)):
        for lam_um in (1.6, 10.0):
            lam_m = lam_um * 1e-6
            c = (rp / R_SOL) ** 2 * planck(lam_m, tp) / planck(lam_m, T_SOL)
            print(f"{nombre:<9} {tp:6.0f} {lam_um:12.1f} {c:12.4e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
