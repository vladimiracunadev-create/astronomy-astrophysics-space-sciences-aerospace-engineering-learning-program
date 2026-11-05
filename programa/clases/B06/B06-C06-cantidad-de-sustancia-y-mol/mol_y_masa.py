#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C06: del gramo al mol y al número de átomos.

Datos PUBLICADOS: CODATA 2022 (NIST): N_A = 6,022 140 76e23 /mol (exacta), u =
1,660 539 068 92e-27 kg; pesos atómicos NIST (C 12,0106 y N 14,006855, puntos
medios de los intervalos; H 1,007975; O 15,9994); Glavin et al. 2025: muestra
total de Bennu 121,6 g; C = 4,5-4,7 % y N = 0,23-0,25 % en masa (análisis de
laboratorio sobre alícuotas). Aplicar esos porcentajes a los 121,6 g es una
HIPÓTESIS de la clase (ESTIMADO), no una medida de la muestra completa.
Modelo: n = m/M ; N = n N_A. Dominio de validez: muestras homogéneas.
Tolerancia: 1e-8 relativo entre N_A*u y 1 g/mol (relación entre dos constantes).
"""

from __future__ import annotations

import sys

NA = 6.02214076e23          # 1/mol, exacta
U_KG = 1.66053906892e-27    # kg, CODATA 2022
M = {"H": 1.007975, "C": 12.0106, "N": 14.006855, "O": 15.9994}   # g/mol


def moles(masa_g: float, molar_g_mol: float) -> float:
    return masa_g / molar_g_mol


def numero(n_mol: float) -> float:
    return n_mol * NA


def pruebas() -> None:
    # N_A * u debe ser 1 g/mol dentro de 1e-8 (dos constantes independientes en CODATA)
    assert abs(NA * U_KG * 1e3 - 1.0) < 1e-8
    # 1 mol de agua: 18,0153 g (NIST WebBook) con los pesos de la clase
    agua = 2 * M["H"] + M["O"]
    assert abs(agua - 18.0153) < 5e-4
    # Ida y vuelta masa -> mol -> masa
    assert abs(moles(100.0, 12.0106) * 12.0106 - 100.0) < 1e-12


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"N_A * u = {NA * U_KG * 1e3:.10f} g/mol")
    m_tot = 121.6
    for el, lo, hi in (("C", 4.5, 4.7), ("N", 0.23, 0.25)):
        n_lo, n_hi = moles(m_tot * lo / 100, M[el]), moles(m_tot * hi / 100, M[el])
        print(f"{el}: {m_tot * lo / 100:.3f}-{m_tot * hi / 100:.3f} g -> {n_lo:.4f}-{n_hi:.4f} mol -> "
              f"{numero(n_lo):.3e}-{numero(n_hi):.3e} átomos")
    c_n = (4.6 / M["C"]) / (0.24 / M["N"])
    print(f"Razón atómica C/N con valores centrales: {c_n:.1f}")
    kg = 1000.0
    n_agua = moles(kg, 2 * M["H"] + M["O"])
    print(f"1 kg de agua: {n_agua:.2f} mol = {numero(n_agua):.3e} moléculas")
    print(f"Masa de un átomo de C-12: {12 * U_KG:.5e} kg")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
