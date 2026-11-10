#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C04: estado estacionario de H3+ en una nube molecular sintetica, ionizada por rayos cosmicos.

Datos: SINTETICOS / ILUSTRATIVOS (no medidos): tasa de ionizacion por rayos cosmicos zeta = 1e-17 s-1 por molecula de H2, n(H2) = 1e4 cm-3,
n(CO) = 1 cm-3 (abundancia 1e-4 respecto de H2), n(e) = 1e-3 cm-3 fijo, coeficientes k_CO = 1.7e-9 y k_e = 2e-7 cm3 s-1 (orden de magnitud tipico,
NO tomados de una base de datos consultada).
Modelo: dn/dt = zeta n(H2) - (k_CO n(CO) + k_e n(e)) n(H3+); se supone que cada ionizacion de H2 produce un H3+ de inmediato.
Los productos de la destruccion por CO alimentan HCO+. Integracion RK4.
Supuestos: abundancias de H2, CO y e fijas; sin granos ni otras vias. Validez: ilustrativa, solo para ver la estructura del balance.
Tolerancia: estacionario numerico vs analitico 1e-6 relativo; relajacion exponencial 1e-6.
"""
from __future__ import annotations
import math, platform

YR = 3.15576e7

def rk4(f, y0, t_fin, pasos):
    h = t_fin / pasos
    y = y0
    for _ in range(pasos):
        k1 = f(y); k2 = f(y + 0.5 * h * k1); k3 = f(y + 0.5 * h * k2); k4 = f(y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    return y

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    zeta, nH2, nCO, ne = 1.0e-17, 1.0e4, 1.0, 1.0e-3
    kCO, ke = 1.7e-9, 2.0e-7
    P = zeta * nH2
    D = kCO * nCO + ke * ne
    nss = P / D
    tau = 1.0 / D
    print("A. Parametros ILUSTRATIVOS: zeta = 1e-17 s-1 ; n(H2) = 1e4 cm-3 ; n(CO) = 1 cm-3 ; n(e) = 1e-3 cm-3")
    print(f"B. Produccion P = {P:.3e} cm-3 s-1 ; destruccion D = {D:.3e} s-1 ; tau = 1/D = {tau:.3e} s = {tau / YR:.2f} anos")
    print(f"   n(H3+) estacionario analitico = {nss:.6e} cm-3")
    f = lambda n: P - D * n
    n_fin = rk4(f, 0.0, 20.0 * tau, 8000)
    err = abs(n_fin - nss) / nss
    print(f"C. Integracion hasta 20 tau: n = {n_fin:.6e} cm-3 ; error relativo = {err:.2e}")
    assert err < 1e-6
    print("D. Relajacion n(t)/n_ss = 1 - exp(-t/tau): numerica frente a analitica")
    print("t/tau    numerica     analitica")
    for m in (0.5, 1.0, 2.0, 4.0):
        n_t = rk4(f, 0.0, m * tau, 4000)
        a = 1.0 - math.exp(-m)
        print(f"{m:5.1f}   {n_t / nss:.8f}   {a:.8f}")
        assert abs(n_t / nss - a) < 1e-6
    print("E. Escala con zeta (n_ss lineal en zeta) y reparto de la destruccion")
    print("zeta [s-1]   n(H3+) [cm-3]   fraccion por CO")
    for z in (0.5e-17, 1e-17, 2e-17, 5e-17):
        n_s = z * nH2 / D
        print(f"{z:.1e}      {n_s:.4e}     {kCO * nCO / D:.4f}")
    assert abs(2e-17 * nH2 / D - 2 * nss) / nss < 1e-12
    r_hcop = kCO * nCO * nss
    print(f"F. Produccion de HCO+ (flujo H3+ + CO) = {r_hcop:.3e} cm-3 s-1 ; HCO+ acumulado en 1e5 anos si no se destruyera = {r_hcop * 1e5 * YR:.3e} cm-3")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
