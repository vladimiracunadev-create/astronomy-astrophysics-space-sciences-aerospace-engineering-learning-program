#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C01: masa interior desde la rotacion y disco exponencial.

Datos: G = 6.67430e-11 m3 kg-1 s-2 (NIST, CODATA 2022, consultado 2026-11-09);
GM_sol = 1.3271244e20 m3/s2 (IAU 2015 B3). R0 = 8.2 kpc, Theta0 = 238 km/s, Omega0 = 29.0
km/s/kpc, R_d = 2.6 kpc y Sigma_estelar(R0) = 38 Msol/pc2 proceden de Bland-Hawthorn y
Gerhard (2016), arXiv:1602.07702 (texto del PDF, consultado 2026-11-09): son valores
OBSERVADOS/ESTIMADOS con incertidumbre; aqui se usan sin ella.
1 pc = 648000/pi ua, 1 ua = 149 597 870 700 m (conversion de unidades).
Modelo: (a) curva plana con simetria esferica: M(<R) = Theta^2 R / G; (b) disco delgado con
densidad superficial Sigma(R) = Sigma_0 exp(-R/R_d).
Supuestos: orbita circular, sin bulbo ni barra ni halo en (b); el halo se trata solo como
masa esferica efectiva en (a).
Validez: orden de magnitud (10 %) del interior de R0. Tolerancias: 1e-9 en identidades
algebraicas, 1e-6 en la cuadratura y 2 % en la consistencia Theta0 = Omega0 R0.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
AU = 149_597_870_700.0
PC = 648000.0 / math.pi * AU
KPC = 1e3 * PC
YR = 365.25 * 86400.0
R0, THETA0, OMEGA0, RD, SIG_R0 = 8.2, 238.0, 29.0, 2.6, 38.0


def masa_interior(theta_kms, r_kpc):
    """M(<R) = Theta^2 R / G en Msol."""
    return (theta_kms * 1e3) ** 2 * r_kpc * KPC / G / M_SOL


def periodo_myr(theta_kms, r_kpc):
    return 2 * math.pi * r_kpc * KPC / (theta_kms * 1e3) / YR / 1e6


def fraccion_disco(r, rd):
    """Fraccion de masa de un disco exponencial dentro de r: 1 - (1 + x) e^-x."""
    x = r / rd
    return 1 - (1 + x) * math.exp(-x)


def fraccion_cuadratura(r, rd, n=4000):
    """Integral de Simpson de 2 pi R Sigma dR / masa total, con Sigma = e^-R/Rd."""
    h = r / n
    f = lambda x: x * math.exp(-x / rd)
    s = f(0) + f(r)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(i * h)
    return (s * h / 3) / (rd ** 2)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: consistencia Theta0 = Omega0 * R0
    th_om = OMEGA0 * R0
    assert abs(th_om / THETA0 - 1) < 0.02, "Theta0 no es consistente con Omega0 R0"
    # Prueba 2: cuadratura frente a la forma cerrada del disco exponencial
    for r in (2.0, R0, 20.0):
        assert abs(fraccion_cuadratura(r, RD) - fraccion_disco(r, RD)) < 1e-6
    # Prueba 3: caso analitico de masa interior: un punto de masa M a r da v^2 = GM/r
    v = math.sqrt(GM_SOL / 1.495978707e11)
    assert abs(v / 29784.7 - 1) < 1e-3, "velocidad orbital de la Tierra fuera de 0,1 %"
    m_in = masa_interior(THETA0, R0)
    p = periodo_myr(THETA0, R0)
    sig0 = SIG_R0 * math.exp(R0 / RD)
    m_disco = 2 * math.pi * (RD * 1e3) ** 2 * sig0
    print(f"M(<R0) por rotacion = {m_in:.3e} Msol ; periodo solar = {p:.0f} Myr")
    print(f"Omega0 R0 = {th_om:.1f} km/s (Theta0 = {THETA0:.0f}) ; v_Tierra = {v:.0f} m/s")
    print(f"Sigma_0 = {sig0:.0f} Msol/pc2 ; M_disco = {m_disco:.3e} Msol")
    print(f"fraccion del disco dentro de R0 = {fraccion_disco(R0, RD):.4f}")
    print(f"fraccion dentro de 2 R_d = {fraccion_disco(2 * RD, RD):.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
