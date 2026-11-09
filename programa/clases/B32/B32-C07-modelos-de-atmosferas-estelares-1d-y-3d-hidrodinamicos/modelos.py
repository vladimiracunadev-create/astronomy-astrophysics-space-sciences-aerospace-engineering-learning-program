#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C07: modelo 1D hidrostatico y efecto de las fluctuaciones de temperatura (comparacion 1D/3D de juguete).

Datos: k_B, u, sigma_SB (NIST CODATA 2022) y T_eff = 5772 K (UAI 2015 B3), consultados 2026-11-09. La gravedad (274.2 m/s^2), kappa = 0.03 m^2/kg, la masa molecular media (1.3), la dispersion de la
temperatura (10 %) y la semilla fija son ILUSTRATIVAS (sinteticas); no se simula ninguna atmosfera real.
Modelo: (1) 1D: P(tau) = g tau/kappa; rho = mu u P/(k T) con T de Eddington; escala de altura H = kT/(mu u g); (2) juguete 3D: temperaturas T_i = <T>(1 + eps_i), eps gaussiano de
sigma 10 %; el flujo medio sigma <T^4> supera a sigma <T>^4 en un factor <(1 + eps)^4> = 1 + 6 s^2 + 3 s^4; temperatura equivalente <T^4>^(1/4) > <T>.
Supuestos: capas planas, sin conveccion explicita. Validez: ilustrativa.
Tolerancia: factor de <T^4> frente a 1 + 6 s^2 + 3 s^4 dentro de 4 errores estandar.
"""
from __future__ import annotations
import math, platform, random, sys
KB, U, SIG = 1.380649e-23, 1.66053906892e-27, 5.670374419e-8
TEFF, G, KAPPA, MU = 5772.0, 274.2, 0.03, 1.3

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'tau':>6} {'T [K]':>8} {'P [Pa]':>11} {'rho [kg/m3]':>12} {'H [km]':>8}")
    for tau in (0.01, 0.1, 2 / 3, 1.0, 3.0):
        t = TEFF * (0.75 * (tau + 2 / 3)) ** 0.25
        p = G * tau / KAPPA
        rho = MU * U * p / (KB * t)
        print(f"{tau:6.3f} {t:8.1f} {p:11.2f} {rho:12.4e} {KB * t / (MU * U * G) / 1e3:8.1f}")
    rng = random.Random(20261109)
    s = 0.10
    n = 400000
    acum4 = acum1 = 0.0
    for _ in range(n):
        e = rng.gauss(0, s)
        acum4 += (1 + e) ** 4
        acum1 += 1 + e
    m4, m1 = acum4 / n, acum1 / n
    ana = 1 + 6 * s * s + 3 * s ** 4
    err = math.sqrt((4 * 6 * s * s) / n) * 1.5
    print(f"<(1 + eps)^4> = {m4:.5f} ; 1 + 6 s^2 + 3 s^4 = {ana:.5f} ; <(1 + eps)> = {m1:.5f}")
    print(f"flujo medio / flujo de la temperatura media = {m4 / m1 ** 4:.5f} ; temperatura equivalente / <T> = {(m4 ** 0.25) / m1:.5f}")
    assert abs(m4 - ana) < 4 * err + 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
