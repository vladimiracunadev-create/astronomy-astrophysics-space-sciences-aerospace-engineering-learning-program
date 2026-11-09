#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B64-C05: fuerza protonmotriz y atrapamiento de un acido debil en acidofilos y alcalofilos.

Datos: SINTETICOS/ILUSTRATIVOS. pH interno y externo, potencial de membrana y pKa son propuestos. Apoyo cualitativo
(resumen consultado el 2026-11-09, Europe PMC): Baker-Austin y Dopson 2007 -- los acidofilos (optimo bajo pH 3) mantienen
un gradiente de pH de varias unidades, con potencial de membrana invertido (positivo dentro) y membranas poco permeables.
Constantes (CODATA 2022, NIST, consultado 2026-11-09): R = 8.314462618 J/(mol K), F = 96485.33212 C/mol.
Modelo 1: fuerza protonmotriz  dp = dpsi - (2.303 R T / F) dpH, con dpsi = psi_in - psi_out [mV] y dpH = pH_in - pH_out.
Modelo 2: un acido debil HA con pKa; solo la forma neutra HA atraviesa la membrana. En equilibrio [HA]_in = [HA]_out, de modo que
 total_in/total_out = (1 + 10^(pH_in - pKa)) / (1 + 10^(pH_out - pKa)).
Segunda via: integracion temporal (Euler, paso pequeno) de la permeacion de HA hasta el equilibrio, con conservacion de masa.
Supuestos: 298.15 K, volumenes iguales dentro y fuera (para el balance de masa), pH constante (amortiguado). Validez: ilustrativa.
Tolerancias: pendiente de Nernst 59.16 mV/unidad a 1e-3 relativo; cociente de atrapamiento frente a simulacion 1e-3.
"""
from __future__ import annotations
import math, platform

R, F, T = 8.314462618, 96485.33212, 298.15
PKA = 4.76    # ilustrativo (acido debil tipo acetico)


def nernst_mv():
    return 1000 * math.log(10) * R * T / F


def dp(dpsi_mv, phin, phout):
    return dpsi_mv - nernst_mv() * (phin - phout)


def razon_atrapamiento(phin, phout, pka=PKA):
    return (1 + 10 ** (phin - pka)) / (1 + 10 ** (phout - pka))


def simular(phin, phout, pka=PKA, pasos=400000, dt=5e-3):
    """Dos compartimentos de volumen 1; total inicial = 1 mM fuera, 0 dentro; solo HA permea con k = 100 /unidad de tiempo."""
    fin = 1 / (1 + 10 ** (phin - pka))   # fraccion neutra dentro
    fout = 1 / (1 + 10 ** (phout - pka))
    Tin, Tout = 0.0, 1.0
    for _ in range(pasos):
        flujo = (fout * Tout - fin * Tin) * dt * 100.0
        Tin += flujo
        Tout -= flujo
    return Tin / Tout, Tin + Tout


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ns = nernst_mv()
    print(f"2.303 R T / F = {ns:.3f} mV por unidad de pH (298.15 K)")
    assert abs(ns - 59.16) / 59.16 < 1e-3
    print("Datos SINTETICOS: ")
    print(f"{'caso':<28} {'pH out':>6} {'pH in':>6} {'dpsi [mV]':>10} {'dp [mV]':>9}")
    casos = [("neutrofilo", 7.0, 7.5, -140.0), ("acidofilo (psi invertido)", 1.5, 6.0, +20.0),
             ("acidofilo moderado", 3.0, 6.5, -20.0), ("alcalofilo", 10.0, 8.5, -60.0)]
    for nom, po, pi, ps in casos:
        print(f"{nom:<28} {po:6.1f} {pi:6.1f} {ps:10.1f} {dp(ps, pi, po):9.1f}")
    print("\nAtrapamiento de un acido debil (pKa ilustrativo 4.76):")
    print(f"{'caso':<28} {'total in/out analitico':>24} {'simulado':>10}")
    for nom, po, pi, ps in casos:
        a = razon_atrapamiento(pi, po)
        s, masa = simular(pi, po)
        print(f"{nom:<28} {a:24.4f} {s:10.4f}")
        assert abs(s - a) / a < 1e-3, (nom, s, a)
        assert abs(masa - 1.0) < 1e-9
    print("Nota: una razon > 1 significa que el acido debil se acumula dentro (atrapamiento); es grande en los acidofilos, con interior mucho menos acido que el exterior, y menor que 1 en el alcalofilo, con interior mas acido que el exterior.")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
