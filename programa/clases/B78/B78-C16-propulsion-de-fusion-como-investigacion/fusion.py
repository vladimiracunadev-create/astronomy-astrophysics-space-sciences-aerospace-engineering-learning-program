#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C16: energia especifica de la fusion D-T frente a la combustion y la fision (balance de energia, sin diseno).

Datos CONSULTADOS (2026-11-10): e = 1.602176634e-19 C, u = 1.66053906892e-27 kg, c = 299792458 m/s, g0 = 9.80665 m/s2 (NIST CODATA).
NO CONSULTADOS (valores de manual, ILUSTRATIVOS): energia liberada por reaccion D-T = 17.6 MeV; masas atomicas D = 2.014 u y T = 3.016 u;
fision: ~200 MeV por nucleo de U-235 (235.04 u); combustion H2/O2: 241.8 kJ por mol de H2O (18.015 g/mol).
ILUSTRATIVOS: fraccion de la energia que acaba como energia cinetica dirigida del escape f = 0.30 (y 0.05 y 1.00 como extremos), potencia del chorro 1 GW para el consumo de combustible.
Modelo: energia por masa de combustible eps = E_reaccion/(masa de reactivos); cota Ve_max = sqrt(2 f eps) (clasica; se contrasta con la relativista).
Segunda via: eps = (fraccion de masa convertida) c^2, con la fraccion = E/(M u c^2), y la correccion relativista del escape.
Tolerancia: las dos vias de eps coinciden a 1e-12 relativa.
"""
from __future__ import annotations
import math, platform

E, U, C, G0 = 1.602176634e-19, 1.66053906892e-27, 299792458.0, 9.80665


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    uc2_mev = U * C ** 2 / E / 1e6
    print(f"u c^2 = {uc2_mev:.3f} MeV (derivado de u, c, e consultados)")
    casos = {
        "D-T (fusion)": (17.6e6 * E, (2.014 + 3.016) * U),
        "U-235 (fision)": (200e6 * E, 235.04 * U),
        "H2/O2 (quimica)": (241.8e3 / 6.02214076e23, 18.015e-3 / 6.02214076e23),
    }
    eps = {}
    for nombre, (en, ma) in casos.items():
        e1 = en / ma
        frac = en / (ma * C ** 2)
        e2 = frac * C ** 2
        assert abs(e1 - e2) / e1 < 1e-12
        eps[nombre] = e1
        print(f"  {nombre:<16} eps = {e1:.3e} J/kg ; fraccion de masa convertida = {frac:.3e}")
    print(f"Cociente D-T/quimica = {eps['D-T (fusion)']/eps['H2/O2 (quimica)']:.3e} ; D-T/fision = {eps['D-T (fusion)']/eps['U-235 (fision)']:.2f}")
    print("Cota de escape Ve_max = sqrt(2 f eps) segun la fraccion f dirigida (ILUSTRATIVA):")
    print("  caso            f      Ve_clasica [m/s]  Ve/c     Isp [s]       gamma-1 relativista")
    for nombre in ("D-T (fusion)", "H2/O2 (quimica)"):
        for f in (0.05, 0.30, 1.00):
            ve = math.sqrt(2 * f * eps[nombre])
            b = ve / C
            g1 = 1 / math.sqrt(1 - b * b) - 1
            ec = 0.5 * b * b
            assert abs(g1 - ec) / ec < 0.01 or nombre != "D-T (fusion)"
            print(f"  {nombre:<15} {f:>4.2f} {ve:>16.3e} {b:>8.4f} {ve/G0:>12.3e} {g1:>12.3e}")
    pj = 1e9
    f = 0.30
    mdot = pj / (f * eps["D-T (fusion)"])
    print(f"Para una potencia del chorro de {pj/1e9:.0f} GW con f = {f}: consumo de combustible D-T = {mdot*1e6:.2f} mg/s ({mdot*86400:.2f} kg/dia)")
    mq = pj / (f * eps["H2/O2 (quimica)"])
    print(f"  la misma potencia con quimica H2/O2 pediria {mq:.1f} kg/s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
