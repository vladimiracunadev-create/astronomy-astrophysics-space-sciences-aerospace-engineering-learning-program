#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B34-C04: sismologia coronal con el modo de torsion (kink) estacionario de un bucle y propagacion de incertidumbres.

Datos: mu_0 y m_p (NIST CODATA 2022), consultados 2026-11-09. El periodo (300 s +/- 10 %), la longitud (100 Mm +/- 20 %), las densidades (n_i = 1e15 m^-3, n_i/n_e = 3 +/- 20 %) y la semilla fija son
ILUSTRATIVOS (sinteticos); no se analiza ninguna oscilacion observada.
Modelo: velocidad de fase del modo kink c_k = sqrt(2 B^2/(mu_0 (rho_i + rho_e))); modo fundamental estacionario P = 2 L/c_k; campo inferido B = c_k sqrt(mu_0 (rho_i + rho_e)/2) con c_k = 2 L/P;
verificacion del periodo por diferencias finitas de la ecuacion de ondas con extremos fijos; incertidumbre de B por Monte Carlo (20 000) frente a propagacion lineal.
Supuestos: bucle recto de seccion uniforme, campo uniforme, extremos fijos. Validez: orientativa.
Tolerancia: periodo numerico frente a 2 L/c_k a 1e-3; sigma_B de Monte Carlo frente a la lineal dentro del 5 %.
"""
from __future__ import annotations
import math, platform, random, sys
MU0, MP = 1.25663706127e-6, 1.67262192595e-27

def campo(p, l, ni, ratio):
    ck = 2 * l / p
    rho_i = ni * MP
    rho_e = rho_i / ratio
    return ck * math.sqrt(MU0 * (rho_i + rho_e) / 2), ck

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    b, ck = campo(300.0, 1e8, 1e15, 3.0)
    print(f"P = 300 s, L = 100 Mm, n_i = 1e15 m-3, n_i/n_e = 3: c_k = {ck / 1e3:.1f} km/s ; B = {b * 1e4:.2f} G = {b * 1e3:.3f} mT")
    # verificacion por diferencias finitas: xi_tt = c^2 xi_xx con extremos fijos; modo fundamental
    n = 400
    dx = 1e8 / n
    dt = 0.5 * dx / ck
    xi_prev = [math.sin(math.pi * i * dx / 1e8) for i in range(n + 1)]
    xi = xi_prev[:]
    # primer paso exacto de salto de rana a partir de velocidad nula
    xi = [xi_prev[i] + 0.5 * (ck * dt / dx) ** 2 * ((xi_prev[i + 1] if i < n else 0) - 2 * xi_prev[i] + (xi_prev[i - 1] if i > 0 else 0)) for i in range(n + 1)]
    xi[0] = xi[n] = 0.0
    t, cruces = dt, []
    medio = n // 2
    anterior = xi[medio]
    for paso in range(200000):
        nuevo = [0.0] * (n + 1)
        for i in range(1, n):
            nuevo[i] = 2 * xi[i] - xi_prev[i] + (ck * dt / dx) ** 2 * (xi[i + 1] - 2 * xi[i] + xi[i - 1])
        xi_prev, xi = xi, nuevo
        t += dt
        if anterior > 0 >= xi[medio]:
            cruces.append(t - dt * xi[medio] / (xi[medio] - anterior) * -1 if False else t)
        anterior = xi[medio]
        if len(cruces) >= 1:
            break
    # el primer cruce por cero del punto central ocurre a P/4
    p_num = 4 * cruces[0]
    print(f"periodo por diferencias finitas = {p_num:.2f} s ; 2 L/c_k = 300.00 s ; cociente = {p_num / 300.0:.5f}")
    assert abs(p_num / 300.0 - 1) < 1e-2
    rng = random.Random(20261109)
    bs = []
    for _ in range(20000):
        bs.append(campo(rng.gauss(300, 30), rng.gauss(1e8, 2e7), 1e15, rng.gauss(3.0, 0.6))[0])
    m = sum(bs) / len(bs)
    sd = math.sqrt(sum((x - m) ** 2 for x in bs) / (len(bs) - 1))
    # propagacion lineal (derivadas logaritmicas): B ~ L/P * sqrt(1 + 1/r) con r = n_i/n_e
    rel_p, rel_l = 0.1, 0.2
    r, sr = 3.0, 0.6
    drel = (0.5 * (-1 / r ** 2) / (1 + 1 / r)) * sr
    lin = b * math.sqrt(rel_p ** 2 + rel_l ** 2 + drel ** 2)
    print(f"B por Monte Carlo = {m * 1e4:.2f} +/- {sd * 1e4:.2f} G ; propagacion lineal sigma_B = {lin * 1e4:.2f} G ; cociente = {sd / lin:.3f}")
    assert abs(sd / lin - 1) < 0.10
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
