#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C04: linealizacion en L1 y L2 del CR3BP y frecuencias de las familias halo.

Datos CONSULTADOS (2026-11-10): GM_T, GM_L (JPL, DE440), a_L (NASA/NSSDC). Modelo: CR3BP circular, ejes sinodicos adimensionales.
Con gamma = distancia al punto, c2 = [mu + (1-mu) gamma^3/(1+gamma)^3]/gamma^3 (L2) y
c2 = [mu + (1-mu) gamma^3/(1-gamma)^3]/gamma^3 (L1). Linealizacion plana: lambda^4 + (2-c2) lambda^2 + (1+2c2)(1-c2) = 0;
frecuencia vertical nu = sqrt(c2). Segunda via: Uxx numerica por diferencias finitas de la aceleracion (paso 1e-6).
Tolerancia: Uxx numerica frente a 1+2c2 < 1e-6 relativa.
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *


def modos(punto):
    l1, l2, _ = colineales()
    if punto == "L1":
        g = 1 - MU - l1
        c2 = (MU + (1 - MU) * g ** 3 / (1 - g) ** 3) / g ** 3
        x = l1
    else:
        g = l2 - (1 - MU)
        c2 = (MU + (1 - MU) * g ** 3 / (1 + g) ** 3) / g ** 3
        x = l2
    b1, b2 = 2 - c2, (1 + 2 * c2) * (1 - c2)
    disc = math.sqrt(b1 * b1 - 4 * b2)
    lam = math.sqrt((-b1 + disc) / 2)
    om = math.sqrt((b1 + disc) / 2)
    nu = math.sqrt(c2)
    h = 1e-6
    ax = lambda xx: rhs((xx, 0, 0, 0, 0, 0))[3]
    uxx = (ax(x + h) - ax(x - h)) / (2 * h)
    cj = omega2(x)
    return dict(x=x, gamma=g, c2=c2, lam=lam, om=om, nu=nu, uxx=uxx, uxx_th=1 + 2 * c2, cj=cj,
                t_lam=1 / (lam * N_L) / DIA, t_om=2 * math.pi / om * T_U / DIA, t_nu=2 * math.pi / nu * T_U / DIA)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for p in ("L1", "L2"):
        m = modos(p)
        print(f"{p}: x = {m['x']:.6f} ; gamma = {m['gamma']:.6f} ({m['gamma'] * A_L:.0f} km) ; c2 = {m['c2']:.5f} ; C = {m['cj']:.6f}")
        print(f"    lambda = {m['lam']:.5f} (e-pliegue {m['t_lam']:.3f} d) ; omega = {m['om']:.5f} (P = {m['t_om']:.3f} d) ; nu = {m['nu']:.5f} (P = {m['t_nu']:.3f} d)")
        print(f"    Uxx numerica = {m['uxx']:.6f} ; teorica 1+2c2 = {m['uxx_th']:.6f} ; omega/nu = {m['om'] / m['nu']:.4f}")
        assert abs(m['uxx'] - m['uxx_th']) / m['uxx_th'] < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
