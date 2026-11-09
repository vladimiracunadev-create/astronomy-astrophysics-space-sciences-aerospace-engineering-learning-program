#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B35-C08: balance de presiones en una lamina de Harris, flujo isotermo estacionario en un tubo de area variable y distancia de la magnetopausa.

Datos: mu_0, k_B y m_p (NIST CODATA 2022, tabla allascii.txt, consultados 2026-11-09). El campo de la lamina (10 nT), su espesor (100 km), la densidad (1e6 m^-3), el campo ecuatorial terrestre
(31 000 nT), el radio terrestre (6378 km), la densidad (5 cm^-3) y la velocidad (400 km/s) del viento son ILUSTRATIVOS (valores de orden de magnitud recordados, no consultados ni medidos).
Modelo: (1) Harris B = B0 tanh(z/L), p = p0 sech^2(z/L) con p0 = B0^2/(2 mu0): presion total constante y fuerza j x B = grad p comprobadas por diferencias finitas; (2) flujo isotermo
(1 - M^2) dln v = -dln A integrado con Runge-Kutta y comparado con la relacion de Mach-area A/A* = exp((M^2-1)/2)/M; ademas la integral de Bernoulli v^2/2 + cs^2 ln(rho) = constante con rho obtenida de la conservacion del flujo masico;
(3) magnetopausa: (2 B0 (R_E/R)^3)^2/(2 mu0) = rho v^2 (el campo se duplica en la frontera comprimida; coeficiente de presion 1: orden de magnitud) con R/R_E = (2 B0^2/(mu0 rho v^2))^(1/6).
Supuestos: MHD ideal, 1D (1) y (2); dipolo y estancamiento simplificados (3). Validez: ilustrativa, no es un modelo de magnetopausa.
Tolerancia: presion total constante a 1e-12 relativo; fuerza j x B frente a grad p con error < 1e-3; Mach integrado frente a la relacion cerrada con error < 1e-6; cierre del balance en R a 1e-9.
"""
from __future__ import annotations
import math, platform, sys

MU0 = 1.25663706127e-6
K_B = 1.380649e-23
M_P = 1.67262192595e-27

def lnA_de_M(M):
    return (M * M - 1) / 2 - math.log(M)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # (1) Harris
    B0, L, n0 = 10e-9, 100e3, 1e6
    p0 = B0 ** 2 / (2 * MU0)
    T = p0 / (n0 * K_B)  # p = n k (Ti + Te) -> T_total = Ti + Te
    print(f"(1) Harris: p0 = {p0:.4e} Pa ; (Ti+Te) = {T:.3e} K ; beta(centro) = {p0/(B0**2/(2*MU0)):.3f}")
    print(f"{'z/L':>5} {'B [nT]':>8} {'p [nPa]':>9} {'p+B^2/2mu0 [nPa]':>18} {'jxB [pN/m3]':>12} {'dp/dz [pN/m3]':>14}")
    h = 1.0
    mx = 0.0
    for zl in (-2.0, -1.0, 0.0, 0.5, 1.0, 2.0):
        z = zl * L
        B = B0 * math.tanh(z / L); p = p0 / math.cosh(z / L) ** 2
        ptot = p + B * B / (2 * MU0)
        dB = (B0 * math.tanh((z + h) / L) - B0 * math.tanh((z - h) / L)) / (2 * h)
        dp = (p0 / math.cosh((z + h) / L) ** 2 - p0 / math.cosh((z - h) / L) ** 2) / (2 * h)
        j = dB / MU0
        fz = -j * B  # (j x B)_z con j en y y B en x: (j y)(B x) -> -j B para el signo de la fuerza hacia el centro
        print(f"{zl:5.1f} {B*1e9:8.3f} {p*1e9:9.4f} {ptot*1e9:18.6f} {fz*1e12:12.5f} {dp*1e12:14.5f}")
        assert abs(ptot / p0 - 1) < 1e-12
        if abs(dp) > 1e-20:
            mx = max(mx, abs(fz / dp - 1))
    assert mx < 1e-3
    # (2) flujo isotermo
    print(f"(2) tobera isoterma: {'M':>6} {'A/A*':>8}")
    for M in (0.2, 0.5, 0.8, 1.0, 1.5, 2.0):
        print(f"    {'':14}{M:6.2f} {math.exp(lnA_de_M(M)):8.4f}")
    # integracion independiente de dln v/dlnA = -1/(1-M^2), con M = v/cs (cs constante) y dlnA lado a lado
    def integra(M0, M1, n=2000):
        lnA0, lnA1 = lnA_de_M(M0), lnA_de_M(M1)
        # variable independiente s = ln A; y = ln M ; dy/ds = -1/(1 - exp(2y))
        f = lambda y: -1.0 / (1.0 - math.exp(2 * y))
        y = math.log(M0); hs = (lnA1 - lnA0) / n
        for _ in range(n):
            k1 = f(y); k2 = f(y + 0.5 * hs * k1); k3 = f(y + 0.5 * hs * k2); k4 = f(y + hs * k3)
            y += hs * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return math.exp(y)
    for M0, M1 in ((0.2, 0.8), (2.0, 1.4)):
        Mf = integra(M0, M1)
        print(f"    integracion RK4 de M = {M0} a la area de M = {M1}: M final = {Mf:.8f}")
        assert abs(Mf - M1) < 1e-6
    # Bernoulli: rho sale de la conservacion del flujo masico (rho* = 1, v* = cs = 1): rho = 1/(M A/A*)
    print(f"    {'M':>6} {'rho/rho*':>10} {'M^2/2 + ln(rho)':>16}")
    for M in (0.2, 0.5, 0.8, 1.5, 2.0):
        rho = 1.0 / (M * math.exp(lnA_de_M(M)))
        Bn = M * M / 2 + math.log(rho)
        print(f"    {M:6.2f} {rho:10.5f} {Bn:16.12f}")
        assert abs(Bn - 0.5) < 1e-12
    # (3) magnetopausa
    BE, RE, n, v = 31000e-9, 6378e3, 5e6, 400e3
    rho_sw = n * M_P
    Pd = rho_sw * v * v
    R = RE * (2 * BE ** 2 / (MU0 * Pd)) ** (1 / 6)
    cierre = (2 * BE * (RE / R) ** 3) ** 2 / (2 * MU0)
    R2 = RE * (2 * BE ** 2 / (MU0 * 2 * Pd)) ** (1 / 6)
    print(f"(3) presion dinamica = {Pd*1e9:.4f} nPa ; R/R_E = {R/RE:.3f} ; presion magnetica comprimida = {cierre*1e9:.4f} nPa ; al duplicar Pd: R/R_E = {R2/RE:.3f} (cociente {R2/R:.5f}, 2^(-1/6) = {2**(-1/6):.5f})")
    assert abs(cierre / Pd - 1) < 1e-9 and abs(R2 / R - 2 ** (-1 / 6)) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
