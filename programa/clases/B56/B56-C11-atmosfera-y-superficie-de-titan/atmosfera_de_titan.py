#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C11: gravedad, altura de escala y parametro de Jeans de Titan.

Datos consultados el 2026-11-09: NASA/NSSDC, hoja de satelites saturninos (actualizada
2025-07-22): masa 1345,5e20 kg, radio medio 2575 km, densidad 1880 kg/m3. La pagina de Titan
de la NASA confirma una atmosfera densa y lagos/mares de hidrocarburos liquidos, pero NO da
cifras de presion ni temperatura. G, k y N_A de NIST (CODATA 2022).
NO CONSULTADOS (ILUSTRATIVOS): presion en superficie 1,5e5 Pa, temperatura de superficie 94 K,
masa molar media 28 g/mol (N2), temperatura de la exobase 150 K, altura de la exobase
1000 km sobre la superficie.
Modelo: g = G M / R^2; H = k T / (m g); P(z) = P0 exp(-z/H) con g constante;
parametro de Jeans lambda = G M m / (k T r) = v_esc^2 / (2 k T / m).
Validez: capa baja isoterma; orden de magnitud. Tolerancia: RK4 de dP/dz con g constante
frente a la exponencial 1e-6; los dos calculos de lambda coinciden a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
K = 1.380649e-23
NA = 6.02214076e23
M, R = 1345.5e20, 2575e3
P0, T0, MU = 1.5e5, 94.0, 28.0e-3


def g_de(r=R):
    return G * M / r ** 2


def altura_escala(T, mu=MU, g=None):
    return K * T / (mu / NA * (g if g is not None else g_de()))


def presion_rk4(z, T=T0, mu=MU, n=2000):
    g = g_de()
    m = mu / NA
    h = z / n
    f = lambda p: -p * m * g / (K * T)
    p = P0
    for _ in range(n):
        k1 = f(p)
        k2 = f(p + h * k1 / 2)
        k3 = f(p + h * k2 / 2)
        k4 = f(p + h * k3)
        p += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return p


def jeans(masa_molar, T, r):
    m = masa_molar / NA
    return G * M * m / (K * T * r)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rho = M / (4 / 3 * math.pi * R ** 3)
    print(f"Densidad desde M y R = {rho:.0f} kg/m3 (hoja: 1880)")
    assert abs(rho / 1880 - 1) < 0.01
    g = g_de()
    H = altura_escala(T0)
    print(f"g = {g:.3f} m/s2 ; H = {H / 1e3:.1f} km (T = 94 K, N2, ilustrativo)")
    z = 100e3
    p_c, p_n = P0 * math.exp(-z / H), presion_rk4(z)
    print(f"P(100 km): exponencial {p_c:.1f} Pa ; RK4 {p_n:.1f} Pa")
    assert abs(p_c / p_n - 1) < 1e-6
    r_ex, t_ex = R + 1000e3, 150.0
    ve = math.sqrt(2 * G * M / r_ex)
    for nombre, mm in (("H2", 2.016e-3), ("CH4", 16.04e-3), ("N2", 28.0e-3)):
        lam = jeans(mm, t_ex, r_ex)
        v_p = math.sqrt(2 * K * t_ex / (mm / NA))
        assert abs(lam / (ve / v_p) ** 2 - 1) < 1e-12
        print(f"{nombre:3s}: lambda de Jeans en la exobase = {lam:7.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
