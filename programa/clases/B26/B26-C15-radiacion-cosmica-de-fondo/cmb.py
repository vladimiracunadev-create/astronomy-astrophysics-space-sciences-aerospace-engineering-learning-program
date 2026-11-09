#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C15: la radiacion cosmica de fondo como cuerpo negro a T0.

Datos: T0 = 2.72548 +/- 0.00057 K (Fixsen, arXiv:0911.1955, resumen, consultado 2026-11-09). Constantes de NIST
(CODATA 2022, consultadas 2026-11-09): h, c, k_B, constante de desplazamiento de Wien en frecuencia
(5.878925757e10 Hz/K), eV. Omega_b h^2 = 0.0224 +/- 0.0001 y H0 = 67.4 (Planck 2018, arXiv:1807.06209, resumen).
Modelo: espectro de Planck B_nu(T); densidad numerica de fotones n = (2 zeta(3)/pi^2)(kT/(hbar c))^3
(zeta(3) por serie); energia media por foton = 2.701 kT; maximo de B_nu en nu = 5.8789e10 T Hz;
razon barion/foton eta = n_b/n_gamma con n_b = Omega_b rho_c/m_p.
Supuestos: cuerpo negro perfecto e isotropo, desprecia anisotropias (~1e-5). Validez: orden de magnitud y
proporciones. Tolerancia: 1e-6 entre integrales numericas y formas cerradas.
"""
from __future__ import annotations
import math
import platform
import sys

H, C, KB, EV, G = 6.62607015e-34, 299792458.0, 1.380649e-23, 1.602176634e-19, 6.67430e-11
HBAR = H / (2 * math.pi)
NU_WIEN = 5.878925757e10          # Hz/K
T0, DT0 = 2.72548, 0.00057
OBH2, H0_KMS = 0.0224, 67.4
AU = 1.49597870700e11
MPC_M = 1e6 * (648000 / math.pi) * AU
MP = 1.67262192595e-27


def zeta3(n=200000):
    return sum(1.0 / k ** 3 for k in range(1, n + 1)) + 1.0 / (2 * n * n)


def n_gamma_cerrada(T):
    return 2 * zeta3() / math.pi ** 2 * (KB * T / (HBAR * C)) ** 3


def n_gamma_integral(T, n=40000):
    xmax = 60.0
    dx = xmax / n
    s = sum((i * dx) ** 2 / math.expm1(i * dx) * dx for i in range(1, n))
    return (8 * math.pi / (H * C) ** 3) * (KB * T) ** 3 * s


def bnu(nu, T):
    return 2 * H * nu ** 3 / C ** 2 / math.expm1(H * nu / (KB * T))


def pico_bnu(T):
    a, b = 1e9, 1e12
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(300):
        if bnu(c, T) > bnu(d, T):
            b = d
        else:
            a = c
        c, d = b - g * (b - a), a + g * (b - a)
    return (a + b) / 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ng_c, ng_i = n_gamma_cerrada(T0), n_gamma_integral(T0)
    assert abs(ng_i / ng_c - 1) < 1e-6, "n_gamma: integral != cerrada"
    print(f"n_gamma = {ng_c * 1e-6:.2f} cm^-3 (cerrada) ; {ng_i * 1e-6:.2f} cm^-3 (integral)")
    nu_p = pico_bnu(T0)
    assert abs(nu_p / (NU_WIEN * T0) - 1) < 1e-6, "maximo de B_nu != constante de Wien"
    print(f"maximo de B_nu: {nu_p / 1e9:.3f} GHz (numerico) = {NU_WIEN * T0 / 1e9:.3f} GHz (Wien-NIST) ; lambda = {C / nu_p * 1e3:.3f} mm")
    # energia media por foton
    u = 4 * 5.670374419e-8 / C * T0 ** 4
    emed = u / ng_c
    print(f"energia media por foton = {emed / EV * 1e3:.4f} meV = {emed / (KB * T0):.4f} kT (2.701 esperado)")
    assert abs(emed / (KB * T0) - 2.701) < 1e-3
    rho_c = 3 * (H0_KMS * 1e3 / MPC_M) ** 2 / (8 * math.pi * G)
    h = H0_KMS / 100
    n_b = OBH2 / h ** 2 * rho_c / MP
    eta = n_b / ng_c
    print(f"n_b = {n_b:.4f} m^-3 ; eta = n_b/n_gamma = {eta:.3e}")
    # incertidumbre de T0 -> n_gamma (proporcional a T^3)
    print(f"incertidumbre relativa de T0 = {DT0 / T0:.2e} -> de n_gamma = {3 * DT0 / T0:.2e}")
    print(f"temperatura a z = 1089 : {T0 * 1090:.0f} K")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
