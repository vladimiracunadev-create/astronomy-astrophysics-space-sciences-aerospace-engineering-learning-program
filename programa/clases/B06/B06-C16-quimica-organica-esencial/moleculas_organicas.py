#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C16: masa molar y grado de insaturación de moléculas orgánicas.

Datos PUBLICADOS: pesos atómicos NIST (puntos medios de intervalos: H 1,007975,
C 12,0106, N 14,006855, O 15,9994); masas molares de referencia del NIST
WebBook: CH4 16,0425, H2O 18,0153, CO2 44,0095 g/mol; Glavin et al. 2025
(Bennu, extracto en agua caliente, nmol/g): ácido fórmico 4106, ácido acético
1436, metilamina 914, etilamina 121; carbono total de la muestra 4,5-4,7 % en masa.
Modelo: M = suma(n_i M_i) ; grado de insaturación = (2C + 2 + N - H) / 2 (halógenos
y otros elementos no tratados). Supuestos: fórmula molecular conocida, moléculas
neutras. Dominio de validez: compuestos de C, H, N, O.
Tolerancias: 5e-4 g/mol frente al WebBook; grados de insaturación exactos.
"""

from __future__ import annotations

import re
import sys

A = {"H": 1.007975, "C": 12.0106, "N": 14.006855, "O": 15.9994}


def parsear(formula: str) -> dict[str, int]:
    cuenta: dict[str, int] = {}
    for el, n in re.findall(r"([A-Z][a-z]?)(\d*)", formula):
        cuenta[el] = cuenta.get(el, 0) + (int(n) if n else 1)
    return cuenta


def masa_molar(formula: str) -> float:
    return sum(A[e] * n for e, n in parsear(formula).items())


def insaturacion(formula: str) -> float:
    c = parsear(formula)
    return (2 * c.get("C", 0) + 2 + c.get("N", 0) - c.get("H", 0)) / 2


def pruebas() -> None:
    assert abs(masa_molar("CH4") - 16.0425) < 5e-4
    assert abs(masa_molar("H2O") - 18.0153) < 5e-4
    assert abs(masa_molar("CO2") - 44.0095) < 5e-4
    assert insaturacion("CH4") == 0 and insaturacion("C2H4") == 1
    assert insaturacion("C6H6") == 4 and insaturacion("CH2O2") == 1
    assert insaturacion("C2H5NO2") == 1                # glicina
    assert parsear("C2H5NO2") == {"C": 2, "H": 5, "N": 1, "O": 2}


MOLECULAS = {  # nombre: (fórmula, nmol/g en el extracto de Bennu)
    "ácido fórmico": ("CH2O2", 4106), "ácido acético": ("C2H4O2", 1436),
    "metilamina": ("CH5N", 914), "etilamina": ("C2H7N", 121),
}


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    tot_ug, tot_c = 0.0, 0.0
    print("Molécula | fórmula | M [g/mol] | insat. | nmol/g | ug/g | ug C/g")
    for nombre, (f, nmol) in MOLECULAS.items():
        m = masa_molar(f)
        ug = nmol * m / 1000
        ugc = nmol * parsear(f)["C"] * A["C"] / 1000
        tot_ug, tot_c = tot_ug + ug, tot_c + ugc
        print(f"  {nombre:14s} {f:7s} {m:8.4f}  {insaturacion(f):4.0f}  {nmol:6d}  {ug:7.2f}  {ugc:7.2f}")
    print(f"Total de las cuatro: {tot_ug:.1f} ug/g ({tot_ug / 1e4:.4f} % en masa) ; carbono: {tot_c:.1f} ug C/g")
    for pct in (4.5, 4.7):
        print(f"  frente a C total {pct} %: {100 * tot_c / (pct * 1e4):.2f} % del carbono")
    for f in ("C2H6O", "C6H6", "C10H8", "C2H5NO2"):
        print(f"{f}: M = {masa_molar(f):.4f} g/mol ; insaturación = {insaturacion(f):.0f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
