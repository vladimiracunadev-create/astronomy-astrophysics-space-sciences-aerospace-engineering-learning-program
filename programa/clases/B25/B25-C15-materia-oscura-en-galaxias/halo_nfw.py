#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C15: halo de materia oscura tipo NFW para una galaxia como la Via Lactea.

Datos: G (NIST, CODATA 2022, 2026-11-09); GM_sol (IAU 2015 B3); H0 = 67,4 km/s/Mpc, Omega_c h^2 = 0,120,
Omega_b h^2 = 0,0224 (Planck 2018 VI, arXiv:1807.06209, resumen consultado 2026-11-09).
Via Lactea: M_vir = 1,3e12 Msol y concentracion c = 16 de un halo NFW de Bland-Hawthorn y Gerhard
(2016, arXiv:1602.07702, texto del PDF consultado 2026-11-09); aqui se usan como M_200 (SIMPLIFICACION
de esta clase: su definicion de masa virial no se reconstruyo); densidad local de materia oscura
0,013 +- 0,003 Msol/pc3 (misma fuente, que cita a McKee et al. 2015). R0 = 8,2 kpc, Theta0 = 238 km/s.
Modelo: rho(r) = rho_s / [(r/r_s)(1 + r/r_s)^2]; M(<r) = 4 pi rho_s r_s^3 [ln(1+x) - x/(1+x)], x = r/r_s;
M_200 = (4 pi/3) 200 rho_crit r_200^3, rho_crit = 3 H0^2/(8 pi G).
Supuestos: halo esferico sin contraccion adiabatica por los barriones, sin subestructura.
Validez: orden de magnitud. Referencia: rho_crit = 2,775e11 h^2 Msol/Mpc3 (valor clasico, no consultado en esta sesion; se usa solo como cota
de coherencia con tolerancia 1e-3). Tolerancias: 1e-6 (masa por cuadratura), 1e-3 (maximo de v_c).
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
PC = 3.0856776e16
KPC = 1e3 * PC
MPC = 1e6 * PC


def m_nfw(x):
    return math.log(1 + x) - x / (1 + x)


def simpson(f, a, b, n=40000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def max_aureo(f, lo, hi):
    g = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(200):
        if f(c) > f(d):
            b, d = d, c
            c = b - g * (b - a)
        else:
            a, c = c, d
            d = a + g * (b - a)
    return 0.5 * (a + b)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    h0 = 67.4e3 / MPC
    rho_crit = 3 * h0 ** 2 / (8 * math.pi * G)
    m200, c = 1.3e12 * M_SOL, 16.0
    r200 = (3 * m200 / (4 * math.pi * 200 * rho_crit)) ** (1 / 3)
    rs = r200 / c
    rho_s = m200 / (4 * math.pi * rs ** 3 * m_nfw(c))
    rho = lambda r: rho_s / ((r / rs) * (1 + r / rs) ** 2)
    # Prueba 1: la masa por cuadratura en ln r coincide con la forma cerrada
    for x in (0.5, 4.0, c):
        f = lambda u: 4 * math.pi * rho(math.exp(u)) * math.exp(3 * u)
        num = simpson(f, math.log(1e-8 * rs), math.log(x * rs))
        assert abs(num / (4 * math.pi * rho_s * rs ** 3 * m_nfw(x)) - 1) < 1e-6, "masa NFW"
    # Prueba 2: v_c^2 = G M/r es maximo en x = 2,1626
    vc2 = lambda x: m_nfw(x) / x
    xm = max_aureo(vc2, 0.5, 10.0)
    assert abs(xm - 2.1626) < 1e-3
    # Prueba 3: rho_crit = 2,775e11 h^2 Msol/Mpc^3 (referencia clasica con h = H0/100), tolerancia 1e-3
    rc_msol_mpc3 = rho_crit * MPC ** 3 / M_SOL
    assert abs(rc_msol_mpc3 / (2.775e11 * 0.674 ** 2) - 1) < 1e-3, "rho_crit en Msol/Mpc3"
    r0 = 8.2 * KPC
    x0 = r0 / rs
    vc0 = math.sqrt(G * 4 * math.pi * rho_s * rs ** 3 * m_nfw(x0) / r0)
    rho0 = rho(r0) * PC ** 3 / M_SOL
    print(f"rho_crit = {rho_crit:.3e} kg/m3 = {rc_msol_mpc3:.3e} Msol/Mpc3")
    print(f"r_200 = {r200 / KPC:.0f} kpc ; r_s = {rs / KPC:.1f} kpc ; r_max = {xm * rs / KPC:.1f} kpc")
    print(f"v_c(R0) del halo = {vc0 / 1e3:.0f} km/s ; fraccion de Theta0^2 = {(vc0 / 238e3) ** 2:.2f}")
    print(f"rho_halo(R0) = {rho0:.4f} Msol/pc3 (densidad local medida: 0.013 +- 0.003)")
    print(f"M(<R0) del halo = {4 * math.pi * rho_s * rs ** 3 * m_nfw(x0) / M_SOL:.3e} Msol")
    print(f"Omega_c/Omega_b = {0.120 / 0.0224:.2f} (Planck 2018, resumen)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
