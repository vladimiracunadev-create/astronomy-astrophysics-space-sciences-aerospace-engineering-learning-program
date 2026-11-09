#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C01: cuatro mensajeros y como se distinguen (deflexion, dispersion y retardos).

Datos: c, e, m_e, epsilon_0 (NIST CODATA 2022) y 1 au (IERS TN36), consultados 2026-11-09. El campo magnetico galactico
de 3 microgauss, las distancias, las energias y la masa del neutrino de 0.1 eV son ILUSTRATIVOS (sinteticos). Contexto
de GW170817: distancia de 40 Mpc (arXiv:1710.05833, resumen).
Modelo: (1) radio de Larmor r_L = E/(Z e B c) (E en eV: r_L = E_eV/(Z B c)); (2) un rayo cosmico recorre un arco de
circunferencia de radio r_L entre dos puntos a distancia d: s = r_L phi con phi = 2 asin(d/(2 r_L)); exceso s - d ~ d^3/(24 r_L^2);
(3) retardo por dispersion del plasma dt = [e^2/(8 pi^2 epsilon_0 m_e c)] DM / nu^2; (4) retardo de un neutrino con masa
(d/c)(1 - beta)/beta con 1 - beta = (mc^2/E)^2/(1 + beta).
Supuestos: campo uniforme, trayectoria sin perdida de energia, plasma frio. Validez: orientativa.
Tolerancia: 1 % entre exceso exacto y aproximado para d/r_L < 0.3; constante de dispersion dentro del 0.5 % de 4.149e3.
"""
from __future__ import annotations
import math
import platform
import sys

C, E, ME, EPS0 = 299792458.0, 1.602176634e-19, 9.1093837139e-31, 8.8541878188e-12
AU = 1.49597870700e11
PC = 648000 / math.pi * AU


def larmor(e_ev, z, b):
    return e_ev / (z * b * C)


def exceso_arco(d, r):
    phi = 2 * math.asin(d / (2 * r))
    return r * phi - d


def retraso_nu(d, mc2_ev, e_ev):
    beta = math.sqrt(1 - (mc2_ev / e_ev) ** 2)
    return d / C * ((mc2_ev / e_ev) ** 2 / (1 + beta)) / beta


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    b = 3e-10   # 3 microgauss
    print(f"B = {b * 1e10:.0f} microgauss = {b:.1e} T ; 1 pc = {PC:.6e} m")
    print(f"{'E [eV]':>9} {'Z':>3} {'r_L [pc]':>12} {'r_L [kpc]':>10}")
    for e_ev, z in ((1e15, 1), (1e18, 1), (1e18, 26), (1e20, 1)):
        r = larmor(e_ev, z, b)
        print(f"{e_ev:9.0e} {z:3d} {r / PC:12.4e} {r / PC / 1e3:10.4f}")
    # exceso de camino de un protón de 1e19 eV en 1 kpc
    r = larmor(1e19, 1, b)
    d = 1e3 * PC
    ex, ap = exceso_arco(d, r), d ** 3 / (24 * r ** 2)
    assert d / r < 0.3 and abs(ex / ap - 1) < 0.01, "exceso de camino"
    print(f"proton de 1e19 eV, d = 1 kpc, r_L = {r / PC / 1e3:.3f} kpc: exceso de camino = {ex / PC:.4f} pc (aprox {ap / PC:.4f}) ; retardo = {ex / C / (365.25 * 86400):.2f} anios")
    # constante de dispersión
    k_si = E ** 2 / (8 * math.pi ** 2 * EPS0 * ME * C)       # s m^2 Hz^2 ... dt = k_si * N_e / nu^2 (N_e en m^-2)
    dm_unit = PC * 1e6                                        # 1 pc cm^-3 en m^-2
    k_dm = k_si * dm_unit / 1e12                              # en s MHz^2 pc^-1 cm^3
    assert abs(k_dm / 4.149e3 - 1) < 0.005, "constante de dispersion"
    print(f"constante de dispersion = {k_dm:.2f} s MHz^2 cm^3/pc")
    for nu_ghz, dm in ((1.4, 100.0), (0.4, 100.0)):
        dt = k_si * dm * dm_unit / (nu_ghz * 1e9) ** 2
        print(f"DM = {dm:.0f} pc/cm3, nu = {nu_ghz} GHz: retardo = {dt:.4f} s")
    # retardos a 40 Mpc
    d40 = 40e6 * PC
    print(f"40 Mpc = {d40:.4e} m ; luz/ondas gravitacionales: {d40 / C:.4e} s")
    for e_mev in (10.0, 1e6):
        print(f"neutrino de {e_mev:.0e} MeV con mc2 = 0.1 eV: retraso = {retraso_nu(d40, 0.1, e_mev * 1e6):.4e} s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
