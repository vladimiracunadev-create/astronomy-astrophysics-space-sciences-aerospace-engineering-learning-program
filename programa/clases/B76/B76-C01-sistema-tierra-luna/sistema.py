#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C01: escalas del sistema Tierra-Luna y puntos de Lagrange colineales.

Datos CONSULTADOS (2026-11-10): GM de la Tierra y de la Luna (JPL SSD, DE440), a = 384400 km (NASA/NSSDC),
radios de la Tierra (NASA/NSSDC) y de la Luna (JPL SSD). Ver cislunar_lib.py.
Modelo: CR3BP circular y plano; mu = GM_L/(GM_T+GM_L). Radio de Hill ~ a (mu/3)^(1/3) (aproximacion);
esfera de influencia de Laplace a (m/M)^(2/5). Los puntos L1-L3 se resuelven por biseccion.
Tolerancias: residuo de dOmega/dx < 1e-12; baricentro dentro de la Tierra (comprobacion).
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *


def calcular():
    l1, l2, l3 = colineales()
    r_hill = A_L * (MU / 3) ** (1 / 3)
    r_lap = A_L * (GM_L / GM_T) ** 0.4
    bary = A_L * MU

    def res(x):
        return x - (1 - MU) * (x + MU) / abs(x + MU) ** 3 - MU * (x - 1 + MU) / abs(x - 1 + MU) ** 3
    return dict(mu=MU, razon=GM_T / GM_L, bary=bary, bary_frac=bary / R_T_MED, r_hill=r_hill, r_lap=r_lap,
                d_l1=(1 - MU - l1) * A_L, d_l2=(l2 - (1 - MU)) * A_L, d_l3=(-MU - l3) * A_L,
                x=(l1, l2, l3), resid=max(abs(res(l1)), abs(res(l2)), abs(res(l3))),
                n=N_L, t_u=T_U / DIA, v_u=A_L * N_L)


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"mu = GM_L/(GM_T+GM_L) = {r['mu']:.8f} ; GM_T/GM_L = {r['razon']:.4f}")
    print(f"Baricentro a {r['bary']:.1f} km del centro de la Tierra = {r['bary_frac']:.4f} radios medios terrestres")
    print(f"Radio de Hill de la Luna ~ {r['r_hill']:.0f} km ; esfera de Laplace ~ {r['r_lap']:.0f} km")
    print(f"L1 a {r['d_l1']:.0f} km de la Luna ; L2 a {r['d_l2']:.0f} km ; L3 a {r['d_l3']:.0f} km de la Tierra, en el lado opuesto a la Luna")
    print(f"x adimensional: L1 = {r['x'][0]:.6f} ; L2 = {r['x'][1]:.6f} ; L3 = {r['x'][2]:.6f}")
    print(f"Residuo maximo de dOmega/dx = {r['resid']:.2e}")
    print(f"n = {r['n']:.6e} rad/s ; unidad de tiempo = {r['t_u']:.4f} d ; unidad de velocidad = {r['v_u']:.5f} km/s")
    assert r['resid'] < 1e-12
    assert r['bary'] < R_T_MED
    assert abs(r['d_l1'] - r['r_hill']) / r['r_hill'] < 0.1 and abs(r['d_l2'] - r['r_hill']) / r['r_hill'] < 0.15
    assert 81.2 < r['razon'] < 81.4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
