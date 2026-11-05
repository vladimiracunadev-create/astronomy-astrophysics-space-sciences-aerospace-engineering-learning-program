#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C07: masa molar media de una atmósfera y composición porcentual.

Datos PUBLICADOS (observados): NASA NSSDC Fact Sheets de Marte (act. 19-may-2025),
Venus (11-ene-2024) y Tierra (15-nov-2024): composición en volumen (fracción molar
de gas ideal) y peso molecular medio de referencia: Marte 43,49; Venus 43,45;
Tierra 28,97 g/mol. Pesos atómicos NIST (puntos medios de los intervalos).
Modelo: M_media = suma(y_i M_i) / suma(y_i) (se normaliza porque las fichas
redondean). Supuestos: gas ideal, mezcla homogénea, solo los componentes listados
(Venus: CO2 y N2; omite trazas de 150 ppm de SO2 y menos). Tolerancia: 0,05 g/mol.
"""

from __future__ import annotations

import sys

A = {"H": 1.007975, "C": 12.0106, "N": 14.006855, "O": 15.9994, "Ar": 39.948}


def masa_molar(formula: dict[str, int]) -> float:
    return sum(A[e] * n for e, n in formula.items())


MOL = {
    "CO2": masa_molar({"C": 1, "O": 2}), "N2": masa_molar({"N": 2}),
    "O2": masa_molar({"O": 2}), "Ar": A["Ar"], "CO": masa_molar({"C": 1, "O": 1}),
}
ATM = {  # % en volumen (NASA)
    "Marte": ({"CO2": 95.1, "N2": 2.59, "Ar": 1.94, "O2": 0.16, "CO": 0.06}, 43.49),
    "Venus": ({"CO2": 96.5, "N2": 3.5}, 43.45),
    "Tierra (seca)": ({"N2": 78.08, "O2": 20.95, "Ar": 0.934, "CO2": 0.042}, 28.97),
}


def masa_media(comp: dict[str, float]) -> float:
    total = sum(comp.values())
    return sum(y * MOL[g] for g, y in comp.items()) / total


def pruebas() -> None:
    assert abs(MOL["CO2"] - 44.0095) < 5e-4                  # NIST WebBook
    for nombre, (comp, ref) in ATM.items():
        assert abs(masa_media(comp) - ref) < 0.05, (nombre, masa_media(comp))
    # composición porcentual del agua: 2 H / M(H2O)
    agua_h = 2 * A["H"] / masa_molar({"H": 2, "O": 1})
    assert abs(agua_h - 0.1119) < 1e-3


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    for nombre, (comp, ref) in ATM.items():
        print(f"{nombre}: M calculada = {masa_media(comp):.3f} g/mol (NASA: {ref}) ; suma % = {sum(comp.values()):.3f}")
    co2 = masa_molar({"C": 1, "O": 2})
    print(f"CO2: C = {A['C'] / co2:.2%} ; O = {2 * A['O'] / co2:.2%} en masa")
    h2o = masa_molar({"H": 2, "O": 1})
    print(f"H2O: H = {2 * A['H'] / h2o:.2%} ; O = {A['O'] / h2o:.2%} en masa")
    # fórmula empírica a partir de 27,29 % C y 72,71 % O
    nc, no = 27.29 / A["C"], 72.71 / A["O"]
    print(f"Fórmula empírica de 27,29 % C / 72,71 % O: C{nc / nc:.2f} O{no / nc:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
