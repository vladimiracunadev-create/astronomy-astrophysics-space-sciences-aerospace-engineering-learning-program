#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C19: masas formulares de silicatos e hielos y estabilidad del hielo de CO2.

Datos PUBLICADOS: pesos atómicos NIST (puntos medios de intervalos: H 1,007975, C 12,0106,
N 14,006855, O 15,9994, Mg 24,3055, Si 28,085; valores: Fe 55,845, Ca 40,078); NIST WebBook:
CO2 punto triple 216,58 K y 5,185 bar, Delta_sub H = 26,1 kJ/mol (25,2-27,2), masas
molares CO2 44,0095 y H2O 18,0153; Asplund et al. 2009: A(Mg) = 7,60 y A(Si) = 7,51.
Las fórmulas de olivino (Mg,Fe)2SiO4 y piroxeno MgSiO3 son fórmulas de manual; la mezcla
olivino + piroxeno para reproducir Mg/Si solar es un MODELO ILUSTRATIVO (sintético).
Modelo: masa formular = suma de pesos atómicos; Clausius-Clapeyron para CO2(s)<->CO2(g).
Supuestos: composición ideal, Delta H constante. Dominio de validez: ilustración.
Tolerancias: 5e-4 g/mol frente a los valores del WebBook; 1e-9 en la regla de mezcla.
"""

from __future__ import annotations

import math
import re
import sys

A = {"H": 1.007975, "C": 12.0106, "N": 14.006855, "O": 15.9994, "Mg": 24.3055,
     "Si": 28.085, "Fe": 55.845, "Ca": 40.078}
R = 8.314462618
TTP, PTP, DH = 216.58, 5.185e5, 26_100.0


def masa(formula: str) -> float:
    return sum(A[e] * (int(n) if n else 1) for e, n in re.findall(r"([A-Z][a-z]?)(\d*)", formula))


def masa_olivino(fo: float) -> float:
    """Olivino (Mg_fo Fe_(1-fo))2 SiO4 como mezcla lineal de forsterita y fayalita."""
    return fo * masa("Mg2SiO4") + (1 - fo) * masa("Fe2SiO4")


def fraccion_olivino_para_mg_si(mg_si: float) -> float:
    """Fracción de Si en olivino (Mg/Si = 2) frente a piroxeno (Mg/Si = 1) para un Mg/Si dado."""
    return mg_si - 1.0


def presion_estabilidad_co2(T: float, dh: float = DH) -> float:
    return PTP * math.exp(-dh / R * (1 / T - 1 / TTP))


def pruebas() -> None:
    assert abs(masa("CO2") - 44.0095) < 5e-4 and abs(masa("H2O") - 18.0153) < 5e-4
    assert abs(masa_olivino(1.0) - masa("Mg2SiO4")) < 1e-12 and abs(masa_olivino(0.0) - masa("Fe2SiO4")) < 1e-12
    assert masa("Mg2SiO4") < masa_olivino(0.9) < masa("Fe2SiO4")
    # con Mg/Si = 1 (solo piroxeno) no hay olivino; con Mg/Si = 2 todo es olivino
    assert fraccion_olivino_para_mg_si(1.0) == 0.0 and fraccion_olivino_para_mg_si(2.0) == 1.0
    f = fraccion_olivino_para_mg_si(10 ** (7.60 - 7.51))
    mg = 2 * f + 1 * (1 - f)
    si = f + (1 - f)
    assert abs(mg / si - 10 ** 0.09) < 1e-12
    # la presión de estabilidad en el punto triple es la del punto triple
    assert abs(presion_estabilidad_co2(TTP) - PTP) < 1e-6


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    for f in ("H2O", "CO2", "NH3", "Mg2SiO4", "Fe2SiO4", "MgSiO3", "CaCO3"):
        print(f"  M({f}) = {masa(f):.4f} g/mol")
    print(f"Olivino Fo90: {masa_olivino(0.9):.4f} g/mol")
    mg_si = 10 ** (7.60 - 7.51)
    f = fraccion_olivino_para_mg_si(mg_si)
    print(f"Mg/Si solar = {mg_si:.3f} -> fracción de Si en olivino (modelo) = {f:.3f}")
    print(f"Mg en forsterita: {2 * A['Mg'] / masa('Mg2SiO4'):.2%} en masa")
    for T in (150.0, 170.0, 194.7):
        print(f"CO2(s) estable por encima de {presion_estabilidad_co2(T):.4g} Pa a {T} K")
    kt = 8.617333262e-5 * 176.0
    print(f"kT a 176 K (eutéctico NH3-H2O, Glavin et al.) = {kt * 1000:.2f} meV")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
