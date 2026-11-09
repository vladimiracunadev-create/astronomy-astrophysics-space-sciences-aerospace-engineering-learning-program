#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C08: frecuencia de plasma, relacion de dispersion y retardo de grupo.

Datos: e, m_e, epsilon_0, c, k_B y 1 au (NIST CODATA 2022 e IERS TN36), consultados 2026-11-09; 1 pc = 648000/pi au. Las densidades (1e14-1e16 m^-3 en la corona, 5e6 m^-3 en el viento solar),
el campo del viento solar (5 nT), la temperatura (1e5 K) y el camino (1 au con n = 5e6 m^-3, 1e7 Hz de contraste) son ILUSTRATIVOS.
Modelo: f_p = (1/2 pi) sqrt(n e^2/(epsilon_0 m_e)) (comprobacion del coeficiente 8.98 kHz sqrt(n[cm^-3])); girofrecuencia f_c = e B/(2 pi m_e); onda electromagnetica
omega^2 = omega_p^2 + k^2 c^2, v_g = c sqrt(1 - omega_p^2/omega^2); retardo respecto de la luz Dt = Int ds (1/v_g - 1/c) por cuadratura numerica frente a la aproximacion
(L/c) omega_p^2/(2 omega^2) = e^2 N/(8 pi^2 epsilon_0 m_e c f^2) (misma constante de dispersion que B28-C01); Bohm-Gross omega^2 = omega_p^2 + 3 k^2 v_th^2.
Supuestos: plasma frio uniforme para la onda electromagnetica, no relativista. Validez: omega > omega_p.
Tolerancia: coeficiente 8.98 kHz dentro del 0.1 %; retardo por cuadratura frente a la aproximacion dentro de 1e-4 para f = 100 MHz.
"""
from __future__ import annotations
import math
import platform
import sys

E, ME, EPS0, C, KB = 1.602176634e-19, 9.1093837139e-31, 8.8541878188e-12, 299792458.0, 1.380649e-23
AU = 1.49597870700e11


def fp(n):
    return math.sqrt(n * E ** 2 / (EPS0 * ME)) / (2 * math.pi)


def retardo_cuadratura(n, long, f, pasos=2000):
    wp = 2 * math.pi * fp(n)
    w = 2 * math.pi * f
    vg = C * math.sqrt(1 - (wp / w) ** 2)
    # medio uniforme: la integral es L (1/vg - 1/c); la cuadratura de Simpson verifica la implementacion con densidad variable n(s) = n (1 + 0.5 sen(2 pi s/L))
    h = long / pasos
    def integrando(s):
        ns = n * (1 + 0.5 * math.sin(2 * math.pi * s / long))
        wps = 2 * math.pi * fp(ns)
        return 1 / (C * math.sqrt(1 - (wps / w) ** 2)) - 1 / C
    tot = integrando(0) + integrando(long)
    for i in range(1, pasos):
        tot += (4 if i % 2 else 2) * integrando(i * h)
    return tot * h / 3, long * (1 / vg - 1 / C)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    coef = fp(1e6) / math.sqrt(1.0)       # n = 1 cm^-3 = 1e6 m^-3
    print(f"f_p para n = 1 cm^-3: {coef:.2f} Hz -> coeficiente 8.98 kHz sqrt(n[cm^-3]) ({coef / 1e3:.4f} kHz)")
    assert abs(coef / 8.98e3 - 1) < 1e-3
    print(f"{'entorno (ilustrativo)':<26} {'n [m-3]':>9} {'f_p':>14}")
    for nombre, n in (("corona alta", 1e14), ("corona baja", 1e15), ("cromosfera superior", 1e16), ("viento solar a 1 au", 5e6), ("ionosfera F", 1e12)):
        f = fp(n)
        etiqueta = f"{f / 1e6:.3f} MHz" if f >= 1e6 else f"{f / 1e3:.3f} kHz"
        print(f"{nombre:<26} {n:9.1e} {etiqueta:>14}")
    b = 5e-9
    fc = E * b / (2 * math.pi * ME)
    print(f"girofrecuencia electronica en el viento solar (B = 5 nT): f_c = {fc:.1f} Hz")
    # relacion de dispersion EM y velocidad de grupo
    n = 1e15
    wp = 2 * math.pi * fp(n)
    print(f"{'f/f_p':>7} {'v_g/c':>10} {'v_f/c':>10} {'v_g v_f/c^2':>12}")
    for r in (1.01, 1.5, 2.0, 5.0, 20.0):
        w = r * wp
        k = math.sqrt(w ** 2 - wp ** 2) / C
        vg, vf = C * math.sqrt(1 - 1 / r ** 2), w / k
        assert abs(vg * vf / C ** 2 - 1) < 1e-12, "v_g v_f = c^2"
        print(f"{r:7.2f} {vg / C:10.5f} {vf / C:10.5f} {vg * vf / C ** 2:12.8f}")
    # retardo de grupo
    n0, long, f = 5e6, AU, 100e6
    num, ap = retardo_cuadratura(n0, long, f)
    const = E ** 2 / (8 * math.pi ** 2 * EPS0 * ME * C)
    dm_col = n0 * long                       # columna uniforme (el seno integra a cero)
    formula = const * dm_col / f ** 2
    print(f"retardo a 100 MHz por 1 au con n = {n0:.0e} m-3 (con modulacion senoidal de 50 %): por cuadratura = {num * 1e6:.4f} us ; por columna e^2 N/(8 pi^2 eps0 m c f^2) = {formula * 1e6:.4f} us ; (medio uniforme exacto: {ap * 1e6:.4f} us)")
    assert abs(num / formula - 1) < 1e-4, "retardo por cuadratura"
    # Bohm-Gross
    t = 1e5
    vth = math.sqrt(KB * t / ME)
    ld = math.sqrt(EPS0 * KB * t / (5e6 * E ** 2))
    print(f"velocidad termica electronica = {vth / 1e3:.1f} km/s ; longitud de Debye = {ld:.2f} m")
    print(f"{'k lambda_D':>11} {'omega/omega_p (Bohm-Gross)':>28}")
    for kl in (0.05, 0.1, 0.3, 1.0):
        k = kl / ld
        w_bg = math.sqrt(1 + 3 * (k * vth / (2 * math.pi * fp(5e6))) ** 2 / (1.0))
        print(f"{kl:11.2f} {w_bg:28.5f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
