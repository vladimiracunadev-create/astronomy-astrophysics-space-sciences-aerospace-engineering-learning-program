#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C05: poblacion SINTETICA de granos de polvo con distribucion de tamanos en ley de potencias.

Datos: ILUSTRATIVOS. n(a) da = K a^(-3.5) da entre a_min = 0.005 um y a_max = 0.25 um (exponente y limites de tipo clasico, no leidos en la fuente;
Draine 2003 se consulto solo por su resumen); densidad del material 3.0 g cm-3; cociente de masa polvo/hidrogeno 0.01 (ilustrativo).
Constante de Boltzmann 1.380649e-23 J/K (NIST, CODATA 2022, consultada el 2026-11-09); masa del proton 1.67262192595e-27 kg (NIST, CODATA 2022)
usada como masa del atomo de H.
Modelo: K se fija por la masa total de polvo; seccion eficaz y area por atomo de H por integracion analitica y numerica (regla del trapecio en malla logaritmica).
Tasa de adsorcion de un atomo de H sobre los granos: k_ads = n_gr(H)*sigma * v_med * S, con v_med = sqrt(8 k T / (pi m)) y probabilidad de pegado S = 1 (ilustrativa).
Supuestos: granos esfericos, un solo material, sin carga; geometria, no Mie. Validez: ilustrativa.
Tolerancia: integrales numericas vs analiticas 1e-6 relativo.
"""
from __future__ import annotations
import math, platform

K_B = 1.380649e-23       # J/K
M_H = 1.67262192595e-27  # kg
UM = 1.0e-4              # cm por um
Q = 3.5                  # exponente
A_MIN, A_MAX = 0.005 * UM, 0.25 * UM     # cm
RHO = 3.0                # g cm-3
RATIO = 0.01             # M_polvo / M_H
M_H_G = M_H * 1.0e3      # g

def integral_analitica(p, a1, a2):
    """integral de a^p da (p != -1)."""
    return (a2 ** (p + 1) - a1 ** (p + 1)) / (p + 1)

def integral_numerica(p, a1, a2, n=200000):
    """regla del trapecio en ln a: integral de a^(p+1) d(ln a)."""
    la1, la2 = math.log(a1), math.log(a2)
    h = (la2 - la1) / n
    s = 0.0
    for i in range(n + 1):
        w = 0.5 if i in (0, n) else 1.0
        s += w * math.exp((p + 1) * (la1 + i * h))
    return s * h

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # K por la masa: (4/3) pi rho K int a^(3-Q) da = RATIO * m_H   (por atomo de H)
    I_m = integral_analitica(3 - Q, A_MIN, A_MAX)
    K = RATIO * M_H_G / ((4.0 / 3.0) * math.pi * RHO * I_m)
    print("A. Poblacion ILUSTRATIVA: n(a) = K a^-3.5 ; a en [0.005, 0.25] um ; rho = 3 g cm-3 ; M_polvo/M_H = 0.01")
    print(f"K = {K:.4e} cm^2.5 por atomo de H")
    I_n = integral_analitica(-Q, A_MIN, A_MAX)
    I_s = integral_analitica(2 - Q, A_MIN, A_MAX)
    n_gr = K * I_n
    sigma = math.pi * K * I_s
    area = 4.0 * math.pi * K * I_s
    a_med = I_s / I_n
    print(f"B. Granos por atomo de H = {n_gr:.4e} ; seccion eficaz geometrica por H = {sigma:.4e} cm2 ; area superficial por H = {area:.4e} cm2")
    # prueba numerica
    for nombre, p in (("numero", -Q), ("seccion", 2 - Q), ("masa", 3 - Q)):
        a = integral_analitica(p, A_MIN, A_MAX); b = integral_numerica(p, A_MIN, A_MAX)
        err = abs(a - b) / a
        assert err < 1e-6, (nombre, err)
    print("C. Integrales analiticas frente a numericas (trapecio en ln a): superadas a 1e-6 relativo")
    # fraccion de la superficie en granos pequenos
    a_corte = 0.01 * UM
    f_sup = integral_analitica(2 - Q, A_MIN, a_corte) / I_s
    f_num = integral_analitica(-Q, A_MIN, a_corte) / I_n
    f_mas = integral_analitica(3 - Q, A_MIN, a_corte) / I_m
    print(f"D. Granos con a < 0.01 um: {100 * f_num:.2f} % del numero ; {100 * f_sup:.2f} % de la superficie ; {100 * f_mas:.2f} % de la masa")
    assert f_num > f_sup > f_mas
    # adsorcion
    print("E. Tasa de adsorcion de H por grano-superficie (S = 1) para n_H = 1e4 cm-3")
    print("T [K]   v_med [cm/s]   k_ads por atomo [s-1]   tiempo hasta adsorberse [anos]")
    nH = 1.0e4
    for T in (10.0, 20.0, 50.0, 100.0):
        v = math.sqrt(8.0 * K_B * T / (math.pi * M_H)) * 100.0
        k_ads = nH * sigma * v
        print(f"{T:5.0f}   {v:11.4e}   {k_ads:.4e}          {1.0 / k_ads / 3.15576e7:.4e}")
    v10 = math.sqrt(8.0 * K_B * 10.0 / (math.pi * M_H)) * 100.0
    v40 = math.sqrt(8.0 * K_B * 40.0 / (math.pi * M_H)) * 100.0
    assert abs(v40 / v10 - 2.0) < 1e-12
    print(f"F. Radio efectivo <a^3>/<a^2> = {integral_analitica(3 - Q, A_MIN, A_MAX) / I_s / UM:.5f} um ; razon area/masa = {area / (RATIO * M_H_G):.4e} cm2 g-1")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
