#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C11: efecto Sunyaev-Zeldovich termico y cinematico de un cumulo ilustrativo.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): seccion eficaz de Thomson sigma_T = 6,6524587051e-29 m^2, m_e c^2 (de m_e = 9,1093837139e-31 kg y c), k_B, h.
T_0 = 2,7255 K (Fixsen 2009, solo resumen). Mpc = 648000/pi x 10^6 au con au = 149597870700 m. Del resumen de Planck 2015 XXII (arXiv:1502.01596, solo resumen, consultado el 2026-11-09): el
mapa y esta dominado por la senal termica en multipolos 20 a 600. Son ILUSTRATIVOS el cumulo (n_e = 1e-2 cm^-3 uniforme, k T_e = 5 keV, longitud 1 Mpc, v_r = 500 km/s) y las frecuencias.
Modelo: Delta T/T = y (x coth(x/2) - 4), y = (sigma_T/m_e c^2) integral de n_e k T_e dl ; efecto cinematico Delta T/T = -tau v_r/c (tau = sigma_T integral de n_e dl).
Verificacion independiente: el operador de Kompaneets en el limite T_e >> T_gamma, Delta n = y x^-2 d/dx [x^4 dn_0/dx], evaluado por diferencias finitas sobre n_0 = 1/(e^x - 1), frente a la forma cerrada.
Supuestos: sin correcciones relativistas (k T_e/m_e c^2 ~ 1 %), cumulo isotermo y uniforme, dispersion unica. Validez: ilustrativa.
Tolerancia: forma cerrada frente a diferencias finitas, 1e-4 relativo; nulo del efecto termico a 217,5 GHz +- 0,5.
"""
from __future__ import annotations
import math, platform, sys

KB = 1.380649e-23; H = 6.62607015e-34; C = 299792458.0
SIGMA_T = 6.6524587051e-29
MEC2 = 9.1093837139e-31 * C ** 2
EV = 1.602176634e-19
AU = 149597870700.0
MPC = AU * 648000 / math.pi * 1e6
T0 = 2.7255

def n0(x):
    return 1.0 / math.expm1(x)

def g_tsz(x):
    return x / math.tanh(x / 2) - 4

def dn_cerrado(x):
    return x * math.exp(x) / math.expm1(x) ** 2 * g_tsz(x)

def dn_kompaneets(x, h=1e-3):
    def flujo(u):
        d = (n0(u + 1e-4) - n0(u - 1e-4)) / 2e-4
        return u ** 4 * d
    return (flujo(x + h) - flujo(x - h)) / (2 * h) / x ** 2

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'x':>6} {'forma cerrada':>16} {'Kompaneets (dif. finitas)':>27} {'dif. relativa':>14}")
    for x in (0.5, 1.0, 2.0, 3.0, 5.0, 8.0):
        a, b = dn_cerrado(x), dn_kompaneets(x)
        print(f"{x:6.1f} {a:16.8e} {b:27.8e} {abs(a - b) / abs(a):14.2e}")
        assert abs(a - b) / abs(a) < 1e-4
    lo, hi = 2.0, 5.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if g_tsz(lo) * g_tsz(mid) <= 0:
            hi = mid
        else:
            lo = mid
    x0 = 0.5 * (lo + hi)
    nu0 = x0 * KB * T0 / H / 1e9
    print(f"nulo de x coth(x/2) - 4: x0 = {x0:.5f} -> nu0 = {nu0:.2f} GHz (T_0 = {T0} K)")
    assert abs(nu0 - 217.5) < 0.5
    ne = 1e-2 * 1e6                       # m^-3
    kt = 5e3 * EV                         # J
    L = 1.0 * MPC
    tau = SIGMA_T * ne * L
    y = SIGMA_T * ne * kt * L / MEC2
    vr = 500e3
    ksz = -tau * vr / C
    print(f"tau = sigma_T n_e L = {tau:.4e} ; y = {y:.4e} ; k T_e/m_e c^2 = {kt / MEC2:.4e} ; kSZ Delta T/T = {ksz:.4e}")
    print(f"{'nu [GHz]':>9} {'x':>7} {'g(x)':>9} {'tSZ [uK]':>10} {'kSZ [uK]':>10}")
    for nu in (30, 100, 143, 217.5, 353):
        x = H * nu * 1e9 / (KB * T0)
        print(f"{nu:9.1f} {x:7.3f} {g_tsz(x):9.4f} {T0 * 1e6 * y * g_tsz(x):10.2f} {T0 * 1e6 * ksz:10.2f}")
    # limites: Rayleigh-Jeans g -> -2 ; Wien g ~ x - 4
    print(f"limites: g(0,01) = {g_tsz(0.01):.4f} (Rayleigh-Jeans: -2) ; g(30) = {g_tsz(30):.3f} (Wien: x - 4 = {30 - 4})")
    assert abs(g_tsz(0.01) + 2) < 1e-3 and abs(g_tsz(30) - 26) < 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
