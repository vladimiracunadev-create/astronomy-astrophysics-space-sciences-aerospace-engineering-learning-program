#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C17: ley de Planck y calibracion radiometrica con cuerpo negro.

Datos: h, c, k EXACTAS del SI (CODATA 2022/BIPM, consultadas 2026-11-05);
sigma = 5.670374419e-8 W m-2 K-4 (CODATA). Sol: T_ef = 5772 K, R = 695 700 km
(NASA/NSSDC Sun Fact Sheet 2024-05-09), 1 au = 1.495978707e11 m (IERS TN36).
Camara infrarroja y fuente de cuerpo negro SINTETICAS: ganancia 0.80 DN por
(W m-2 sr-1) en la banda 8-12 um, desplazamiento 120 DN, ruido 2 DN.
Modelo: L_lambda(T) = 2 h c^2 / lambda^5 / (exp(h c / (lambda k T)) - 1)
[W m-2 sr-1 m-1]. Radiancia espectral integrada en toda la banda:
pi * integral(L_lambda dlambda) = sigma T^4 (ley de Stefan-Boltzmann).
Calibracion: DN = a + G * L_banda con L_banda integrada en 8-12 um; ajuste
lineal por minimos cuadrados con fuentes a distintas T.
Supuestos: emisividad 1 (cuerpo negro ideal), banda rectangular, sin
atmosfera. Tolerancia: integral numerica de Planck vs sigma T^4 a 1e-5
relativa; recta exacta sin ruido a 1e-9.
"""
from __future__ import annotations
import math
import platform
import random
import sys

H, C, K = 6.62607015e-34, 299792458.0, 1.380649e-23
SIGMA = 5.670374419e-8
AU = 1.495978707e11


def planck(lam, T):
    x = H * C / (lam * K * T)
    if x > 700:
        return 0.0
    return 2 * H * C ** 2 / lam ** 5 / math.expm1(x)


def integra(f, a, b, n=200000):
    """Regla de Simpson en escala logaritmica de lambda."""
    la, lb = math.log(a), math.log(b)
    h = (lb - la) / n
    s = 0.0
    for i in range(n + 1):
        lam = math.exp(la + i * h)
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * f(lam) * lam
    return s * h / 3


def l_banda(T, a=8e-6, b=12e-6):
    return integra(lambda l: planck(l, T), a, b, 4000)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1) Planck integrada vs Stefan-Boltzmann
    for T in (300.0, 1000.0, 5772.0):
        tot = math.pi * integra(lambda l: planck(l, T), 1e-8, 1e-2)
        rel = abs(tot - SIGMA * T ** 4) / (SIGMA * T ** 4)
        print(f"T = {T:6.0f} K: pi*int L = {tot:.6e} ; sigma T^4 = {SIGMA*T**4:.6e} ; rel = {rel:.1e}")
        assert rel < 1e-5
    # 2) Maximo espectral (Wien) por biseccion en x = h c/(lambda k T)
    lo, hi = 4.0, 6.0
    f = lambda x: x - 5.0 * (1.0 - math.exp(-x))
    for _ in range(80):
        m = 0.5 * (lo + hi)
        lo, hi = (m, hi) if f(m) < 0 else (lo, m)
    x = 0.5 * (lo + hi)
    b = H * C / (K * x)
    print(f"x = {x:.9f} ; b = lambda_max T = {b*1e3:.6f} mm K ; lambda_max(5772 K) = {b/5772*1e9:.1f} nm ; lambda_max(300 K) = {b/300*1e6:.2f} um")
    # el maximo de L_lambda en 5772 K esta en lambda = b/T
    lm = b / 5772.0
    assert planck(lm, 5772.0) > planck(lm * 0.99, 5772.0) and planck(lm, 5772.0) > planck(lm * 1.01, 5772.0)
    # 3) Irradiancia solar a 1 au
    s = SIGMA * 5772.0 ** 4 * (695700e3 / AU) ** 2
    print(f"sigma T^4 (Sol) = {SIGMA*5772.0**4:.4e} W/m2 ; irradiancia a 1 au = {s:.2f} W/m2")
    # 4) Calibracion radiometrica con cuerpo negro
    temps = [280.0, 300.0, 320.0, 340.0, 360.0, 380.0]
    Lb = [l_banda(T) for T in temps]
    print("T (K): " + ", ".join(f"{T:.0f}" for T in temps))
    print("L_banda 8-12 um (W m-2 sr-1): " + ", ".join(f"{v:.3f}" for v in Lb))
    G, A = 0.80, 120.0
    dn_exacto = [A + G * v for v in Lb]
    n = len(Lb)
    xm, ym = sum(Lb) / n, sum(dn_exacto) / n
    g_hat = sum((a - xm) * (b_ - ym) for a, b_ in zip(Lb, dn_exacto)) / sum((a - xm) ** 2 for a in Lb)
    a_hat = ym - g_hat * xm
    assert abs(g_hat - G) < 1e-9 and abs(a_hat - A) < 1e-6
    rng = random.Random(17)
    dn = [v + rng.gauss(0, 2.0) for v in dn_exacto]
    ym = sum(dn) / n
    g2 = sum((a - xm) * (b_ - ym) for a, b_ in zip(Lb, dn)) / sum((a - xm) ** 2 for a in Lb)
    a2 = ym - g2 * xm
    res = math.sqrt(sum((d - (a2 + g2 * l)) ** 2 for d, l in zip(dn, Lb)) / (n - 2))
    ug = res / math.sqrt(sum((a - xm) ** 2 for a in Lb))
    print(f"ganancia = {g2:.4f} +/- {ug:.4f} DN/(W m-2 sr-1) (verdadera {G}) ; desplazamiento = {a2:.1f} DN (verdadero {A})")
    assert abs(g2 - G) < 4 * ug
    # 5) Inversion: radiancia desde 250 DN y temperatura de brillo
    L0 = (250.0 - a2) / g2
    lo_t, hi_t = 200.0, 500.0
    for _ in range(60):
        m = 0.5 * (lo_t + hi_t)
        lo_t, hi_t = (m, hi_t) if l_banda(m) < L0 else (lo_t, m)
    print(f"250 DN -> L = {L0:.3f} W m-2 sr-1 -> temperatura de brillo = {0.5*(lo_t+hi_t):.2f} K")
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
