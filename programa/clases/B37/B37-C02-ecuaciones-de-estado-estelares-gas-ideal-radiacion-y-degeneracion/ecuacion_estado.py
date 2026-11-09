#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C02: ecuacion de estado estelar con gas ideal, radiacion y electrones degenerados.

Datos: constantes h, k_B, m_e, m_u, sigma_SB y c de NIST CODATA 2022, consultada el 2026-11-09. Las composiciones (mu, mu_e) y los estados (rho, T) son ILUSTRATIVOS (sinteticos).
Modelo: P_gas = rho k T/(mu m_u); P_rad = a T^4/3 con a = 4 sigma/c. Electrones: n_e = (4 pi/h^3)(2 m_e k T)^(3/2) F_1/2(eta) (integral de Fermi-Dirac no relativista, Simpson)
y P_e = (2/3) n_e k T F_3/2(eta)/F_1/2(eta); eta se halla por biseccion para n_e = rho/(mu_e m_u).
Contraste: limite no degenerado (P_e -> n_e k T) y limite de temperatura nula P_e = (3 pi^2)^(2/3) hbar^2 n^(5/3)/(5 m_e), con hbar = h/(2 pi).
Supuestos: electrones no relativistas, iones ideales, sin correcciones coulombianas ni ionizacion parcial. Validez: orientativa (se viola a alta densidad relativista).
Tolerancia: limites dentro del 1 % en los casos extremos; integral de Fermi dentro de 1e-10 frente a su valor analitico en eta = -20.
"""
from __future__ import annotations
import math, platform, sys

H = 6.62607015e-34
KB = 1.380649e-23
ME = 9.1093837139e-31
MU = 1.66053906892e-27
SB = 5.670374419e-8
C = 299792458.0
A_RAD = 4 * SB / C
HBAR = H / (2 * math.pi)


def fermi(j, eta, n=4000):
    xmax = max(eta, 0.0) + 60.0
    h = xmax / n
    f = lambda x: x**j / (1.0 + math.exp(min(x - eta, 700.0)))
    s = f(0.0) + f(xmax)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(i * h)
    return s * h / 3.0


def n_e_de_eta(eta, T):
    return 4 * math.pi / H**3 * (2 * ME * KB * T) ** 1.5 * fermi(0.5, eta)


def eta_de_n(n, T):
    lo, hi = -40.0, 400.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if n_e_de_eta(mid, T) < n:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def presiones(rho, T, mu, mue):
    n = rho / (mue * MU)
    eta = eta_de_n(n, T)
    pe = (2.0 / 3.0) * n * KB * T * fermi(1.5, eta) / fermi(0.5, eta)
    pideal = n * KB * T
    p0 = (3 * math.pi**2) ** (2 / 3) * HBAR**2 * n ** (5 / 3) / (5 * ME)
    pion = rho * KB * T / (mu * MU) - pideal if mu else 0.0
    return n, eta, pe, pideal, p0, pion


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1. integral de Fermi frente al limite analitico no degenerado
    eta = -20.0
    ref = math.sqrt(math.pi) / 2 * math.exp(eta)
    err = abs(fermi(0.5, eta) / ref - 1)
    print(f"F_1/2(-20) / (sqrt(pi)/2 exp(-20)) - 1 = {err:.2e}")
    assert err < 1e-3
    # 2. mezcla gas ideal + radiacion en un centro de tipo solar (ilustrativo)
    rho, T, mu = 1.5e5, 1.57e7, 0.85
    pg = rho * KB * T / (mu * MU)
    pr = A_RAD * T**4 / 3
    print(f"centro tipo Sol: P_gas = {pg:.3e} Pa ; P_rad = {pr:.3e} Pa ; beta = {pg / (pg + pr):.4f}")
    assert 0.99 < pg / (pg + pr) < 1.0
    # 3. grado de degeneracion de los electrones en tres estados
    print(f"{'estado':<20} {'rho [kg/m3]':>12} {'T [K]':>9} {'eta':>9} {'Pe/(n k T)':>11} {'Pe/P(T=0)':>10}")
    casos = (("tipo Sol", 1.5e5, 1.57e7, 0.85, 1.17), ("enana blanca", 1e9, 1e7, 1.3, 2.0), ("intermedio", 1e7, 1e7, 1.3, 2.0), ("gas diluido", 1e2, 1e7, 0.6, 1.17))
    res = {}
    for nombre, r, t, m, me in casos:
        n, eta, pe, pid, p0, _ = presiones(r, t, m, me)
        res[nombre] = (eta, pe / pid, pe / p0)
        print(f"{nombre:<20} {r:12.2e} {t:9.2e} {eta:9.3f} {pe / pid:11.4f} {pe / p0:10.4f}")
    assert 1.0 < res["tipo Sol"][1] < 1.10
    assert abs(res["gas diluido"][1] - 1) < 0.001
    assert abs(res["enana blanca"][2] - 1) < 0.01
    assert res["intermedio"][1] > 1.01
    # 4. la presion degenerada casi no depende de T; la ideal si
    p1 = presiones(1e9, 1e7, 1.3, 2.0)[2]
    p2 = presiones(1e9, 2e7, 1.3, 2.0)[2]
    print(f"enana blanca: P_e(T = 2e7)/P_e(T = 1e7) = {p2 / p1:.4f} (gas ideal daria 2,0000)")
    assert p2 / p1 < 1.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
