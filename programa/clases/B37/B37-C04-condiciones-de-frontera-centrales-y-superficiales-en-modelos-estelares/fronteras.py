#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C04: condiciones de frontera central y superficial de un modelo estelar (politropo n = 3 y atmosfera gris).

Datos: constantes G, sigma_SB de NIST CODATA 2022 y valores nominales solares de la UAI 2015 B3 (GM = 1,3271244e20 m3/s2, R = 6,957e8 m, T_ef = 5772 K), consultados el 2026-11-09 (solo
resumen de la Resolucion B3). La densidad central, la opacidad constante de la atmosfera y la gravedad superficial usada en la parte 3 son ILUSTRATIVAS (sinteticas).
Modelo: ecuacion de Lane-Emden theta'' + 2 theta'/xi + theta^n = 0 con series centrales theta = 1 - xi^2/6 + n xi^4/120 e integracion RK4 hasta theta = 0. Contraste con n = 1,
cuya solucion analitica es theta = sin(xi)/xi (xi_1 = pi). Atmosfera gris de Eddington T^4 = (3/4) T_ef^4 (tau + 2/3); presion fotosferica por integracion de dP/dtau = g/kappa.
Supuestos: politropo (la estructura se reduce a una sola variable), kappa constante en la atmosfera. Validez: orientativa.
Tolerancia: xi_1 de n = 1 dentro de 1e-6 de pi; n = 3 dentro de 1e-4 de los valores tabulados 6,89685 y 2,01824 (referencia clasica, no consultada); T(tau = 2/3) = T_ef exacta.
"""
from __future__ import annotations
import math, platform, sys

G = 6.67430e-11
SB = 5.670374419e-8
GM_SOL, R_SOL, TEF_SOL = 1.3271244e20, 6.957e8, 5772.0


def lane_emden(n, h=1e-4):
    xi = 1e-3
    th = 1 - xi**2 / 6 + n * xi**4 / 120
    ph = -xi / 3 + n * xi**3 / 30  # theta'

    def f(x, t, p):
        return p, -2 * p / x - (max(t, 0.0)) ** n

    while True:
        k1 = f(xi, th, ph)
        k2 = f(xi + h / 2, th + h / 2 * k1[0], ph + h / 2 * k1[1])
        k3 = f(xi + h / 2, th + h / 2 * k2[0], ph + h / 2 * k2[1])
        k4 = f(xi + h, th + h * k3[0], ph + h * k3[1])
        tn = th + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        pn = ph + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if tn <= 0:
            # interpolacion lineal al cero
            fr = th / (th - tn)
            xi1 = xi + fr * h
            p1 = ph + fr * (pn - ph)
            return xi1, -xi1**2 * p1
        xi, th, ph = xi + h, tn, pn


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    x1, m1 = lane_emden(1.0)
    print(f"n = 1: xi_1 = {x1:.6f} (pi = {math.pi:.6f}) ; -xi^2 theta' = {m1:.6f} (pi = {math.pi:.6f})")
    assert abs(x1 - math.pi) < 1e-6 and abs(m1 - math.pi) < 1e-5
    x3, m3 = lane_emden(3.0)
    rc_rm = x3**3 / (3 * m3)
    print(f"n = 3: xi_1 = {x3:.5f} ; -xi^2 theta' = {m3:.5f} ; rho_c/rho_medio = {rc_rm:.4f}")
    assert abs(x3 - 6.89685) < 1e-4 and abs(m3 - 2.01824) < 1e-4
    # 2. condiciones centrales: P_c y T_c de un politropo de la masa y radio nominales del Sol
    M = GM_SOL / G
    rho_m = M / (4 / 3 * math.pi * R_SOL**3)
    rho_c = rc_rm * rho_m
    Pc = 4 * math.pi * G * rho_c**2 * (R_SOL / x3) ** 2 / (3 + 1)
    print(f"M = {M:.4e} kg ; rho_medio = {rho_m:.1f} kg/m3 ; rho_c = {rho_c:.4e} kg/m3 ; P_c = {Pc:.4e} Pa")
    # contraste del valor de P_c: presion de equilibrio de una esfera uniforme (2 pi/3 G rho^2 R^2) como cota de orden
    Pc_unif = 2 * math.pi / 3 * G * rho_m**2 * R_SOL**2
    print(f"P_c(politropo) / P_c(esfera uniforme) = {Pc / Pc_unif:.3f}")
    assert 50 < Pc / Pc_unif < 150
    # 3. serie central frente a integracion numerica de la masa: m(r) = 4 pi/3 rho_c r^3 (1 - 3 xi^2/10 ...)
    xi_s = 0.05
    th = 1 - xi_s**2 / 6 + 3 * xi_s**4 / 120
    m_serie = 4 * math.pi / 3 * rho_c * (R_SOL / x3 * xi_s) ** 3
    m_num = 0.0
    N = 20000
    a = R_SOL / x3
    for i in range(N):
        r = (i + 0.5) / N * xi_s * a
        xi = r / a
        t = 1 - xi**2 / 6 + 3 * xi**4 / 120
        m_num += 4 * math.pi * r**2 * rho_c * t**3 * (xi_s * a / N)
    print(f"masa interior a xi = {xi_s}: integral numerica = {m_num:.5e} kg ; 4 pi/3 rho_c r^3 = {m_serie:.5e} kg ; cociente = {m_num / m_serie:.5f}")
    assert abs(m_num / m_serie - 1) < 5e-3
    # 4. superficie: atmosfera gris de Eddington
    for tau in (0.0, 2 / 3, 1.0, 10.0):
        T = TEF_SOL * (0.75 * (tau + 2 / 3)) ** 0.25
        print(f"tau = {tau:6.3f} : T = {T:8.1f} K")
    assert abs(TEF_SOL * (0.75 * (2 / 3 + 2 / 3)) ** 0.25 / TEF_SOL - 1) < 1e-12
    g, kappa = GM_SOL / R_SOL**2, 0.05  # kappa ilustrativa [m2/kg]
    n_int, tau_max = 20000, 2 / 3
    P = 0.0
    for i in range(n_int):
        P += g / kappa * tau_max / n_int
    print(f"g = {g:.2f} m/s2 ; P(tau = 2/3) = {P:.3f} Pa (integracion) ; g tau/kappa = {g * tau_max / kappa:.3f} Pa")
    assert abs(P / (g * tau_max / kappa) - 1) < 1e-9
    # 5. L = 4 pi R^2 sigma T_ef^4 como condicion de superficie
    L = 4 * math.pi * R_SOL**2 * SB * TEF_SOL**4
    print(f"L = 4 pi R^2 sigma T_ef^4 = {L:.4e} W")
    assert abs(L / 3.828e26 - 1) < 2e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
