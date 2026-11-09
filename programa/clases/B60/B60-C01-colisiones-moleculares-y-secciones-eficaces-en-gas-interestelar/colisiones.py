#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B60-C01: constantes de velocidad a partir de secciones eficaces.

Datos: constantes CODATA 2022 consultadas en NIST el 2026-11-09 (k_B, u, e, eps0). Diametro molecular de 3 A,
polarizabilidad de 0.787 A^3 (H2), masas de 3 u y 2 u y barrera de 500 K son ILUSTRATIVOS (no consultados ni medidos).
Modelo: k(T) = <sigma v> con distribucion de Maxwell-Boltzmann de la velocidad relativa (masa reducida mu).
 - esfera dura: sigma = pi d^2           -> k = sigma sqrt(8 k T / (pi mu))
 - Langevin (ion-neutro): sigma = k_L/v -> k_L = e/(2 eps0) sqrt(alpha/mu), alpha = 4 pi eps0 alpha'
 - lineas de centros con barrera E0: sigma = sigma0 (1 - E0/E) -> k = sigma0 vbar exp(-E0/kT)
Unidades: SI en el calculo; se imprime en cm^3 s^-1. Supuestos: colisiones binarias en gas diluido, sin estructura interna.
Tolerancias: Monte Carlo (semilla 60001, N = 400000) frente a la formula: 1 %; cuadratura frente a cerrada: 1e-6 relativo.
Validez: ilustrativa; no es una seccion eficaz medida ni calculada de ninguna reaccion real.
"""
from __future__ import annotations
import math, platform, random

KB = 1.380649e-23          # J/K (exacto, CODATA 2022, NIST)
U = 1.66053906892e-27      # kg (CODATA 2022, NIST)
E = 1.602176634e-19        # C (exacto, CODATA 2022, NIST)
EPS0 = 8.8541878188e-12    # F/m (CODATA 2022, NIST)


def vbar(T, mu):
    return math.sqrt(8 * KB * T / (math.pi * mu))


def k_dura(T, mu, d):
    return math.pi * d * d * vbar(T, mu)


def k_langevin(mu, alpha_vol):
    alpha = 4 * math.pi * EPS0 * alpha_vol
    return E / (2 * EPS0) * math.sqrt(alpha / mu)


def k_barrera_cerrada(T, mu, sigma0, E0_K):
    return sigma0 * vbar(T, mu) * math.exp(-E0_K / T)


def k_barrera_cuadratura(T, mu, sigma0, E0_K, n=20000):
    """k = sqrt(8/(pi mu)) (kT)^(-3/2) * integral sigma(E) E exp(-E/kT) dE (Simpson)."""
    kT = KB * T
    E0 = E0_K * KB
    a, b = E0, E0 + 60 * kT
    h = (b - a) / n
    f = lambda e: sigma0 * (1 - E0 / e) * e * math.exp(-e / kT)
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    integral = s * h / 3
    return math.sqrt(8 / (math.pi * mu)) * kT ** -1.5 * integral


def monte_carlo(T, mu, d, alpha_vol, N, rng):
    """Promedia sigma*v sobre velocidades relativas muestreadas (cada componente N(0, sqrt(kT/mu)))."""
    s = math.sqrt(KB * T / mu)
    sig_hs = math.pi * d * d
    kL = k_langevin(mu, alpha_vol)
    acc_hs = acc_l = 0.0
    for _ in range(N):
        v = math.sqrt(sum(rng.gauss(0, s) ** 2 for _ in range(3)))
        acc_hs += sig_hs * v
        acc_l += kL / v * v          # sigma_L(v) * v
    return acc_hs / N, acc_l / N


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    cm3 = 1e6
    m1, m2 = 3 * U, 2 * U
    mu = m1 * m2 / (m1 + m2)
    d, alpha_vol = 3.0e-10, 0.787e-30
    kL = k_langevin(mu, alpha_vol)
    print(f"mu = {mu / U:.3f} u ; Langevin k_L = {kL * cm3:.3e} cm^3 s^-1 (independiente de T)")
    print("\nEsfera dura (d = 3 A) frente a Langevin:")
    print("  T [K]   v_media [m/s]   k_dura [cm3/s]   k_L/k_dura")
    for T in (10.0, 50.0, 300.0):
        print(f"  {T:5.0f}   {vbar(T, mu):11.1f}   {k_dura(T, mu, d) * cm3:13.3e}   {kL / k_dura(T, mu, d):9.1f}")
    rng = random.Random(60001)
    T = 10.0
    mh, ml = monte_carlo(T, mu, d, alpha_vol, 400000, rng)
    eh, el = abs(mh / k_dura(T, mu, d) - 1), abs(ml / kL - 1)
    print(f"\nMonte Carlo a {T:.0f} K (N = 400000): esfera dura {mh * cm3:.3e} (error {eh:.2%}) ; Langevin {ml * cm3:.3e} (error {el:.2e})")
    print("\nSeccion con barrera E0/k = 500 K (sigma0 = pi d^2): cuadratura frente a forma cerrada")
    print("  T [K]   k_cuadratura [cm3/s]   k_cerrada [cm3/s]   dif. relativa")
    sigma0 = math.pi * d * d
    peor = 0.0
    for T in (50.0, 100.0, 300.0):
        kq = k_barrera_cuadratura(T, mu, sigma0, 500.0)
        kc = k_barrera_cerrada(T, mu, sigma0, 500.0)
        peor = max(peor, abs(kq / kc - 1))
        print(f"  {T:5.0f}   {kq * cm3:18.4e}   {kc * cm3:15.4e}   {abs(kq / kc - 1):.1e}")
    print(f"  cociente k(300 K)/k(50 K) con barrera = {k_barrera_cerrada(300.0, mu, sigma0, 500.0) / k_barrera_cerrada(50.0, mu, sigma0, 500.0):.1f}")
    assert eh < 0.01 and el < 0.01 and peor < 1e-6
    assert 1.0e-9 < kL * cm3 < 2.5e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
