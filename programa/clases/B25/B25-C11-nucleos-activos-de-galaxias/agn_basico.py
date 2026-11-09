#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C11: limite de Eddington, crecimiento de un agujero negro y sombra de M87*.

Datos: G, c, m_p y sigma_T (NIST, CODATA 2022, consultados 2026-11-09); GM_sol (IAU 2015 B3);
M(M87*) = (6,5 +- 0,7)e9 Msol y diametro del anillo 42 +- 3 microsegundos de arco (Event Horizon
Telescope Collaboration, arXiv:1906.11238, resumen consultado 2026-11-09): OBSERVADOS. La eficiencia
radiativa 0,1 y el crecimiento a Eddington son ILUSTRATIVOS; la semilla de 100 Msol es SINTETICA.
Modelo: (a) L_Edd = 4 pi G M m_p c / sigma_T; (b) L = eta Mdot c^2 y e-pliegue t_S = eta/(1-eta) sigma_T c/(4 pi G m_p);
(c) en Schwarzschild (unidades GM/c^2 = 1) la energia especifica de la orbita circular es
E(r) = (1 - 2/r)/sqrt(1 - 3/r), con minimo en r = 6 (ISCO) y eficiencia 1 - E(6) = 1 - sqrt(8/9);
el parametro de impacto critico b(r) = r/sqrt(1 - 2/r) es minimo en r = 3 con b = 3 sqrt(3), de donde el
diametro de la sombra es 2 b = 6 sqrt(3) GM/c^2.
Supuestos: agujero sin rotacion, Eddington con opacidad Thomson de hidrogeno, sin viento.
Validez: ordenes de magnitud; los agujeros reales rotan y la eficiencia depende del espin.
Tolerancias: 1e-9 en identidades, 1e-6 en minimizaciones numericas.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
C = 299_792_458.0
MP = 1.67262192595e-27
ST = 6.6524587051e-29
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
YR = 365.25 * 86400.0
MPC = 3.0856776e22


def l_edd(m_kg):
    return 4 * math.pi * G * m_kg * MP * C / ST


def t_salpeter(eta):
    return eta / (1 - eta) * ST * C / (4 * math.pi * G * MP)


def minimiza(f, lo, hi):
    """Busqueda por seccion aurea del minimo de f en [lo, hi]."""
    g = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(200):
        if f(c) < f(d):
            b, d = d, c
            c = b - g * (b - a)
        else:
            a, c = c, d
            d = a + g * (b - a)
    return 0.5 * (a + b)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: equilibrio de fuerzas en L_Edd: F_rad = L sigma_T/(4 pi r^2 c) = F_grav = G M m_p / r^2
    m, r = 10 * M_SOL, 1e9
    assert abs(l_edd(m) * ST / (4 * math.pi * r * r * C) / (G * m * MP / (r * r)) - 1) < 1e-12
    # Prueba 2: t_S por dos caminos: eta M c^2 / ((1-eta) L_Edd)
    for eta in (0.1, 0.057):
        via2 = eta * M_SOL * C ** 2 / ((1 - eta) * l_edd(M_SOL))
        assert abs(via2 / t_salpeter(eta) - 1) < 1e-12
    # Prueba 3: ISCO y eficiencia de Schwarzschild
    e = lambda r_: (1 - 2 / r_) / math.sqrt(1 - 3 / r_)
    r_isco = minimiza(e, 3.5, 20.0)
    assert abs(r_isco - 6.0) < 1e-6
    eta_isco = 1 - e(6.0)
    assert abs(eta_isco - (1 - math.sqrt(8 / 9))) < 1e-12
    # Prueba 4: sombra, b minimo en r = 3
    b = lambda r_: r_ / math.sqrt(1 - 2 / r_)
    r_ph = minimiza(b, 2.1, 10.0)
    assert abs(r_ph - 3.0) < 1e-6 and abs(b(r_ph) - 3 * math.sqrt(3)) < 1e-6
    print(f"L_Edd(1 Msol) = {l_edd(M_SOL):.3e} W ; L_Edd(6.5e9 Msol) = {l_edd(6.5e9 * M_SOL):.3e} W")
    print(f"t_Salpeter(eta = 0.1) = {t_salpeter(0.1) / YR / 1e6:.1f} Myr ; eta_ISCO = {eta_isco:.4f} -> {t_salpeter(eta_isco) / YR / 1e6:.1f} Myr")
    n_pliegues = math.log(6.5e9 / 100)
    print(f"de 100 Msol a 6.5e9 Msol: {n_pliegues:.2f} e-pliegues = {n_pliegues * t_salpeter(0.1) / YR / 1e9:.2f} Gyr (eta = 0.1, a Eddington)")
    print(f"ISCO en {r_isco:.4f} GM/c2 ; eficiencia = {eta_isco:.4f} (Newton: {1 / 12:.4f})")
    print(f"sombra: diametro = {2 * b(r_ph):.4f} GM/c2 = {b(r_ph):.4f} R_s (R_s = 2GM/c2)")
    gm_c2 = GM_SOL * 6.5e9 / C ** 2
    theta_rad = 42e-6 / 206264.806247
    d = 6 * math.sqrt(3) * gm_c2 / theta_rad
    print(f"M87*: GM/c2 = {gm_c2:.3e} m ; con 42 microarcsec la distancia implicada es {d / MPC:.1f} Mpc")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
