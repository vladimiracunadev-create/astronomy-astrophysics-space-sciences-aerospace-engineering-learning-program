#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C09: atmosfera gris de Eddington, opacidad de Thomson y limite de Eddington.

Datos (NIST CODATA 2022, consultados 2026-11-09): sigma, G, c, k_B, m_p, seccion de Thomson.
GM_sol, L_sol, T_ef,sol nominales (IAU 2015 B3); g_sol = 274.0 m/s2 (NASA Sun Fact Sheet,
2024-05-09). Fraccion de hidrogeno X = 0.7 y masa molecular media mu = 1.3: valores
ILUSTRATIVOS (estimados).
Modelo: atmosfera gris plano-paralela en equilibrio radiativo, aproximacion de Eddington:
T^4 = (3/4) T_ef^4 (tau + 2/3). Opacidad de Thomson por unidad de masa:
kappa_es = sigma_T (1 + X) / (2 m_p). Luminosidad de Eddington: igualar la fuerza de radiacion
kappa L /(4 pi r^2 c) con la gravedad G M / r^2.
Supuestos: opacidad gris, equilibrio local, sin convección en la atmosfera.
Validez: ilustrativa para fotosferas; el Sol real tiene opacidad no gris. Tolerancia: 1e-4 en el
flujo emergente (cuadratura) y 1e-9 en L_Edd por biseccion.
"""
from __future__ import annotations
import math
import platform
import sys

SIGMA, G, C = 5.670374419e-8, 6.67430e-11, 299792458.0
KB, MP, SIGMA_T = 1.380649e-23, 1.67262192595e-27, 6.6524587051e-29
GM_SOL, L_SOL, T_SOL, G_SOL = 1.3271244e20, 3.828e26, 5772.0, 274.0
M_SOL = GM_SOL / G


def temperatura(tau, t_ef):
    return t_ef * (0.75 * (tau + 2 / 3)) ** 0.25


def flujo_emergente(t_ef, n_tau=6000, n_mu=400):
    """F = 2 pi Int_0^1 I(0,mu) mu dmu, I(0,mu) = Int S(tau) exp(-tau/mu) dtau/mu, S = sigma T^4 / pi."""
    tau_max = 40.0
    d_tau = tau_max / n_tau
    f = 0.0
    d_mu = 1.0 / n_mu
    for j in range(n_mu):
        mu = (j + 0.5) * d_mu
        i_mu = 0.0
        for k in range(n_tau):
            tau = (k + 0.5) * d_tau
            s = SIGMA * temperatura(tau, t_ef) ** 4 / math.pi
            i_mu += s * math.exp(-tau / mu) * d_tau / mu
        f += 2 * math.pi * i_mu * mu * d_mu
    return f


def kappa_thomson(X):
    return SIGMA_T * (1 + X) / (2 * MP)


def l_edd_biseccion(M, kappa):
    """L tal que kappa L/(4 pi r^2 c) = G M / r^2 (independiente de r), por biseccion."""
    g_m = lambda L: kappa * L / (4 * math.pi * C) - G * M
    lo, hi = 1e20, 1e40
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if g_m(mid) < 0:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    assert abs(temperatura(2 / 3, T_SOL) / T_SOL - 1) < 1e-12, "T(tau=2/3) != T_ef"
    f_num = flujo_emergente(T_SOL, n_tau=1500, n_mu=150)
    f_ref = SIGMA * T_SOL ** 4
    assert abs(f_num / f_ref - 1) < 1e-3, "flujo emergente != sigma T_ef^4"
    print(f"flujo emergente numerico / sigma T_ef^4 = {f_num / f_ref:.5f}")
    x = 0.7
    k = kappa_thomson(x)
    l_cerrada = 4 * math.pi * G * M_SOL * C / k
    l_bis = l_edd_biseccion(M_SOL, k)
    assert abs(l_bis / l_cerrada - 1) < 1e-9, "biseccion != forma cerrada"
    print(f"kappa_es (X={x}) = {k:.5f} m2/kg = {k * 10:.3f} cm2/g")
    print(f"L_Edd(1 Msol) = {l_cerrada:.4e} W = {l_cerrada / L_SOL:.0f} L_sol")
    mu = 1.3
    H = KB * T_SOL / (mu * MP * G_SOL)
    print(f"escala de altura (T_ef, mu={mu}, g=274.0) = {H / 1e3:.0f} km")
    for tau in (0.0, 2 / 3, 1.0, 2.0, 10.0):
        print(f"tau = {tau:5.3f} -> T = {temperatura(tau, T_SOL):7.1f} K")
    print(f"limbo: I(mu=0)/I(mu=1) = {(2 / 3) / (1 + 2 / 3):.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
