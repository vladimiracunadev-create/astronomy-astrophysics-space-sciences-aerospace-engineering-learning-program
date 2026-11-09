#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C03: oscilaciones de neutrinos y razon de sabores en la Tierra.

Datos: hbar c (NIST CODATA 2022), consultado 2026-11-09. Los angulos de mezcla (sen^2 th12 = 0.307, sen^2 th13 = 0.022,
sen^2 th23 = 0.55), los Delta m^2 y la fase de violacion CP nula son ILUSTRATIVOS (sinteticos). Contexto: IceCube-170922A,
neutrino de ~290 TeV (arXiv:1807.08816, resumen).
Modelo: dos sabores P = sen^2(2 th) sen^2(phi), phi = Delta m^2 c^4 L/(4 hbar c E) = 1.267 Delta m^2[eV^2] L[km]/E[GeV]
(la constante se calcula aqui desde hbar c). Tres sabores con matriz PMNS real: probabilidad media
P_ab = Sum_i |U_ai|^2 |U_bi|^2 (distancias astrofisicas); razon de sabores en la Tierra = phi_fuente x P.
Supuestos: vacio, sin efecto de materia, sin fase CP. Validez: L/E astrofisico (oscilaciones promediadas).
Tolerancia: 1e-12 en la unitariedad de filas y columnas; 5 % de desviacion de 1:1:1 en la razon de sabores.
"""
from __future__ import annotations
import math
import platform
import sys

HBARC_EV_M = 1.973269804e-7       # eV m (NIST: 197.3269804 MeV fm)


def constante_fase():
    """phi = K * dm2[eV2] * L[km] / E[GeV], con K = 1e3/(4 hbarc[eV m] * 1e9)."""
    return 1e3 / (4 * HBARC_EV_M * 1e9)


def pmns(s12sq, s13sq, s23sq):
    s12, c12 = math.sqrt(s12sq), math.sqrt(1 - s12sq)
    s13, c13 = math.sqrt(s13sq), math.sqrt(1 - s13sq)
    s23, c23 = math.sqrt(s23sq), math.sqrt(1 - s23sq)
    return [[c12 * c13, s12 * c13, s13],
            [-s12 * c23 - c12 * s23 * s13, c12 * c23 - s12 * s23 * s13, s23 * c13],
            [s12 * s23 - c12 * c23 * s13, -c12 * s23 - s12 * c23 * s13, c23 * c13]]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    k = constante_fase()
    assert abs(k / 1.267 - 1) < 1e-3, "constante 1.267"
    print(f"constante de fase K = {k:.5f} (eV^-2 km^-1 GeV)")
    dm2, s2th = 2.5e-3, 1.0
    for e_gev in (1.0, 10.0):
        l_max = math.pi / (2 * k * dm2 / e_gev)
        p = s2th * math.sin(k * dm2 * l_max / e_gev) ** 2
        print(f"E = {e_gev:4.1f} GeV, dm2 = {dm2} eV2: primer maximo de oscilacion en L = {l_max:.1f} km (P = {p:.3f})")
    u = pmns(0.307, 0.022, 0.55)
    for i in range(3):
        assert abs(sum(u[i][j] ** 2 for j in range(3)) - 1) < 1e-12, "fila"
        assert abs(sum(u[j][i] ** 2 for j in range(3)) - 1) < 1e-12, "columna"
    pm = [[sum(u[a][i] ** 2 * u[b][i] ** 2 for i in range(3)) for b in range(3)] for a in range(3)]
    for a in range(3):
        assert abs(sum(pm[a]) - 1) < 1e-12, "unitariedad de P"
    print("P_ab promediada (filas: sabor inicial e, mu, tau; columnas: final):")
    for a in range(3):
        print("   " + "  ".join(f"{pm[a][b]:.4f}" for b in range(3)))
    fuente = (1.0, 2.0, 0.0)
    tierra = [sum(fuente[a] * pm[a][b] for a in range(3)) for b in range(3)]
    tot = sum(tierra)
    rel = [3 * v / tot for v in tierra]
    print(f"razon de sabores en la fuente 1:2:0 -> en la Tierra {rel[0]:.4f}:{rel[1]:.4f}:{rel[2]:.4f}")
    assert all(abs(v - 1) < 0.05 for v in rel), "razon cercana a 1:1:1"
    # promedio justificado: fase para L = 1 Gpc, E = 290 TeV
    l_km = 1e9 * 648000 / math.pi * 1.495978707e11 / 1e3 / 1e0 * 1e0
    l_km = 1e9 * (648000 / math.pi * 1.495978707e11) / 1e3
    phi = k * 7.4e-5 * l_km / 290e3
    print(f"fase de oscilacion solar para L = 1 Gpc y E = 290 TeV (dm2 = 7.4e-5 eV2): {phi:.3e} rad (>> 1: se promedia)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
