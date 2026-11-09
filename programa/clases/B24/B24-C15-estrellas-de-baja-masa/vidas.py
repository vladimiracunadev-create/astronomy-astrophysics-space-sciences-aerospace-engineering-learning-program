#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C15: vida en secuencia principal de estrellas de baja masa.

Datos: GM_sol y L_sol nominales (IAU 2015 B3); energia por kg de H de la fusion calculada en
B24-C06 con masas NIST (epsilon c^2 = 6.3978e14 J/kg). La relacion masa-luminosidad por tramos
es ILUSTRATIVA (sintetica): L = 0.23 M^2.3 (M < 0.43), L = M^4 (0.43 <= M < 2), L = 1.4 M^3.5
(M >= 2), con M y L en unidades solares; NO es la relacion de ninguna publicacion consultada.
La fraccion de hidrogeno quemado f = 0.1 (M >= 0.35, nucleo radiativo) y f = 1 (M < 0.35,
completamente convectiva) y X = 0.7 son valores ILUSTRATIVOS (estimados).
Modelo: t = f X M epsilon c^2 / L.
Supuestos: L constante; sin evolucion de L en la secuencia principal. Validez: orden de magnitud.
Tolerancia: pendiente log-log de un tramo = 1 - alfa a 1e-9; continuidad de L entre tramos 10 %.
"""
from __future__ import annotations
import math
import platform
import sys

GM_SOL, L_SOL, G = 1.3271244e20, 3.828e26, 6.67430e-11
M_SOL_KG = GM_SOL / G
EPS_C2 = 6.3978e14
YR = 365.25 * 86400.0
X = 0.7


def lum(m):
    if m < 0.43:
        return 0.23 * m ** 2.3
    if m < 2.0:
        return m ** 4
    return 1.4 * m ** 3.5


def f_quemada(m):
    return 1.0 if m < 0.35 else 0.1


def t_ms_gyr(m):
    return f_quemada(m) * X * m * M_SOL_KG * EPS_C2 / (lum(m) * L_SOL) / YR / 1e9


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # continuidad de la relacion ilustrativa
    for mb in (0.43, 2.0):
        lo, hi = lum(mb * (1 - 1e-9)), lum(mb)
        assert abs(hi / lo - 1) < 0.1, f"discontinuidad en {mb}"
    # pendiente log-log dentro de un tramo: t ~ M^(1-alfa) cuando f es constante
    m1, m2 = 0.6, 1.2
    pend = (math.log(t_ms_gyr(m2)) - math.log(t_ms_gyr(m1))) / (math.log(m2) - math.log(m1))
    assert abs(pend - (1 - 4)) < 1e-9, "pendiente != 1 - alfa"
    t1 = t_ms_gyr(1.0)
    print(f"t_MS(1 Msol) = {t1:.2f} Gyr (X=0.7, f=0.1)")
    print(f"{'M/Msol':>7} {'L/Lsol':>9} {'f':>4} {'t_MS [Gyr]':>14}")
    for m in (0.1, 0.2, 0.35, 0.5, 0.8, 1.0, 1.5, 2.0, 5.0, 10.0):
        print(f"{m:7.2f} {lum(m):9.4g} {f_quemada(m):4.1f} {t_ms_gyr(m):14.4g}")
    print(f"pendiente log-log (0.6 -> 1.2 Msol) = {pend:.6f} (esperada {1 - 4})")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
