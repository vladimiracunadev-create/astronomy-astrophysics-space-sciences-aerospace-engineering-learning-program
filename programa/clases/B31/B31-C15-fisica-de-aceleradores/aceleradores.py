#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C15: rigidez magnetica, perdidas por sincrotron y energia en el centro de masas.

Datos: c, e, epsilon_0, masas del electron (0.510 998 950 69 MeV) y del proton (938.272 089 43 MeV) (NIST CODATA 2022), consultados 2026-11-09. El campo (8 T), el radio de curvatura (2800 m),
las energias (100 GeV para el electron, 6.5 TeV para el proton) y la energia del ciclotron (10 MeV) son ILUSTRATIVOS (sinteticos); no se describe ningun acelerador concreto.
Modelo: p = e B rho, con p c [GeV] = 0.299 792 458 B[T] rho[m]; perdida por vuelta de un anillo isomagnetico U_0 = e^2 beta^3 gamma^4/(3 epsilon_0 rho) (en eV: U_0 = e beta^3 gamma^4/(3 epsilon_0 rho));
cociente entre protones y electrones de igual energia (m_e/m_p)^4 (con la correccion beta^3 del proton); frecuencia del ciclotron f = e B/(2 pi gamma m); energia en el centro de masas sqrt(s) = 2E (colisionador) frente a
sqrt(2 m c^2 E + 2 m^2 c^4) (blanco fijo).
Supuestos: campo uniforme, particula relativista (beta ~ 1) para las perdidas, sin aceleracion de radiofrecuencia. Validez: orden de magnitud.
Tolerancia: coeficiente 0.299 792 458 por dos vias a 1e-12; cociente de perdidas dentro de 5e-4 de (m_e/m_p)^4 (diferencia: beta^3 del proton).
"""
from __future__ import annotations
import math
import platform
import sys

C, E, EPS0 = 299792458.0, 1.602176634e-19, 8.8541878188e-12
ME_MEV, MP_MEV = 0.51099895069, 938.27208943


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    coef = C / 1e9
    print(f"coeficiente p c = 0.299 792 458 B rho: c/1e9 = {coef:.9f}")
    b, rho = 8.0, 2800.0
    pc_gev = coef * b * rho
    pc_si = E * b * rho * C / E / 1e9
    assert abs(pc_gev / pc_si - 1) < 1e-12
    print(f"B = {b} T, rho = {rho:.0f} m: p c = {pc_gev:.3f} GeV = {pc_gev / 1e3:.4f} TeV")
    # perdidas
    print(f"{'particula':<9} {'E [GeV]':>9} {'gamma':>12} {'U_0 por vuelta [GeV]':>22}")
    res = {}
    for nombre, m_mev, e_gev, rr in (("electron", ME_MEV, 100.0, 3000.0), ("proton", MP_MEV, 100.0, 3000.0), ("proton", MP_MEV, 6500.0, 2800.0)):
        gam = e_gev * 1e3 / m_mev
        beta = math.sqrt(1 - 1 / gam ** 2)
        u0 = E * beta ** 3 * gam ** 4 / (3 * EPS0 * rr) / 1e9           # GeV por vuelta
        res[(nombre, e_gev)] = u0
        print(f"{nombre:<9} {e_gev:9.1f} {gam:12.4e} {u0:22.4e}")
    ratio = res[("proton", 100.0)] / res[("electron", 100.0)]
    print(f"cociente protones/electrones de igual energia y radio: {ratio:.4e} ; (m_e/m_p)^4 = {(ME_MEV / MP_MEV) ** 4:.4e}")
    assert abs(ratio / (ME_MEV / MP_MEV) ** 4 - 1) < 5e-4       # la diferencia es el factor beta^3 del proton (gamma = 107)
    # ciclotron
    t = 10.0
    gam = 1 + t / MP_MEV
    f0 = E * 1.5 / (2 * math.pi * 1.67262192595e-27)
    f = f0 / gam
    print(f"ciclotron de protones de {t} MeV en 1.5 T: f(no relativista) = {f0 / 1e6:.4f} MHz ; f(relativista) = {f / 1e6:.4f} MHz ; reduccion = {(1 - 1 / gam) * 100:.3f} %")
    # centro de masas
    print(f"{'E del haz [GeV]':>16} {'colisionador sqrt(s) [GeV]':>27} {'blanco fijo sqrt(s) [GeV]':>27}")
    for e in (6500.0,):
        s_col = 2 * e
        s_fix = math.sqrt(2 * (MP_MEV / 1e3) * e + 2 * (MP_MEV / 1e3) ** 2)
        print(f"{e:16.1f} {s_col:27.1f} {s_fix:27.2f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
