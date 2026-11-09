#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C23: significancia estadistica de las tensiones de H0 y de S8 con valores publicados.

Datos (PUBLICADOS en resumenes, consultados 2026-11-09): H0 = 67.4 +/- 0.5 km/s/Mpc, sigma8 = 0.811 +/- 0.006,
Omega_m = 0.315 +/- 0.007 (Planck 2018, arXiv:1807.06209); H0 = 74.03 +/- 1.42 (Riess et al. 2019,
arXiv:1903.07603); H0 = 73.2 +/- 1.3 (SH0ES R20, citado en Di Valentino et al., arXiv:2103.01183); S8 = 0.776 +/- 0.017
(DES Y3, 3x2pt, LCDM; arXiv:2105.13549). S8 = sigma8 sqrt(Om/0.3); el valor de S8 de Planck se DERIVA aqui por
propagacion lineal ignorando la correlacion sigma8-Omega_m: es una estimacion gruesa, no el valor publicado.
Modelo: n sigma = |a - b|/sqrt(s_a^2 + s_b^2); p bilateral = erfc(n/sqrt 2). Comprobaciones: la cola normal por
integracion numerica y por Monte Carlo (1e6 muestras, semilla fija).
Supuestos: gaussianidad e independencia; no se corrige por "mirar en muchos sitios". Validez: ilustrativa.
Tolerancia: 1e-7 entre erfc y la integral; 4 sigma estadisticos en el Monte Carlo.
"""
from __future__ import annotations
import math
import platform
import random
import sys


def nsigma(a, sa, b, sb):
    return abs(a - b) / math.hypot(sa, sb)


def p_bilateral(n):
    return math.erfc(n / math.sqrt(2))


def p_integral(n, hi=12.0, pasos=200000):
    h = (hi - n) / pasos
    f = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
    s = f(n) + f(hi)
    for i in range(1, pasos):
        s += (4 if i % 2 else 2) * f(n + i * h)
    return 2 * s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for n in (1.0, 2.0, 3.0, 4.4, 5.0):
        a, b = p_bilateral(n), p_integral(n)
        assert abs(a - b) < 1e-7 * max(1, 1 / a) * a + 1e-12, f"p(n={n})"
        print(f"n = {n:3.1f} sigma: p bilateral = {a:.3e} (erfc) = {b:.3e} (integral)")
    rng = random.Random(23)
    N = 1000000
    cuenta = sum(1 for _ in range(N) if abs(rng.gauss(0, 1)) > 3.0)
    esp = N * p_bilateral(3.0)
    assert abs(cuenta - esp) < 4 * math.sqrt(esp), "Monte Carlo fuera de 4 sigma"
    print(f"Monte Carlo: {cuenta} de {N} con |x| > 3 (esperado {esp:.0f} +/- {math.sqrt(esp):.0f})")
    print("--- tension de H0 ---")
    for nom, h, s in (("Riess et al. 2019", 74.03, 1.42), ("SH0ES R20 (Di Valentino)", 73.2, 1.3)):
        n = nsigma(67.4, 0.5, h, s)
        print(f"Planck 67.4 +/- 0.5 vs {nom} {h} +/- {s}: diferencia = {h - 67.4:.2f} ; {n:.2f} sigma ; p = {p_bilateral(n):.2e}")
    assert abs(nsigma(67.4, 0.5, 74.03, 1.42) - 4.4) < 0.05
    print("--- tension de S8 (estimacion gruesa) ---")
    sig8, d_sig8, om, d_om = 0.811, 0.006, 0.315, 0.007
    s8 = sig8 * math.sqrt(om / 0.3)
    d_s8 = math.hypot(d_sig8 * math.sqrt(om / 0.3), sig8 * 0.5 / math.sqrt(0.3 * om) * d_om)
    n = nsigma(s8, d_s8, 0.776, 0.017)
    print(f"S8 derivado de Planck = {s8:.4f} +/- {d_s8:.4f} (sin correlacion) ; DES Y3 = 0.776 +/- 0.017 ; {n:.2f} sigma ; p = {p_bilateral(n):.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
