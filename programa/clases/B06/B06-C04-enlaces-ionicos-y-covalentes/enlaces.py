#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C04: energía de Coulomb entre iones y conteo de electrones de valencia.

Datos PUBLICADOS: CODATA 2022 (NIST): e y c exactas, epsilon_0 = 8,854 187 8188e-12 F/m,
Ry*hc = 13,605 693 122 990 eV, radio de Bohr 5,291 772 105 44e-11 m.
Las distancias entre iones (0,25 y 0,30 nm) son SINTÉTICAS (ilustrativas), no datos
de un compuesto concreto. Electrones de valencia: número de grupo (C02).
Modelo: dos cargas puntuales en el vacío, E = q1 q2 / (4 pi eps0 r); conteo de
Lewis: pares = (suma de valencias)/2. Supuestos: sin apantallamiento por el
medio, sin repulsión de corto alcance. Dominio de validez: estimación de orden
de magnitud. Tolerancia: 1e-4 en la prueba de la energía de Hartree.
"""

from __future__ import annotations

import math
import sys

E = 1.602176634e-19            # C, exacto
EPS0 = 8.8541878188e-12        # F/m, CODATA 2022
KB_EV = 1.380649e-23 / E       # eV/K (k exacta / e)
RY_EV = 13.605693122990        # eV, CODATA 2022
A0_M = 5.29177210544e-11       # m, CODATA 2022

VALENCIA = {"H": 1, "C": 4, "N": 5, "O": 6, "Cl": 7}   # por número de grupo (C02)


def coulomb_ev(q1: int, q2: int, r_nm: float) -> float:
    """Energía de interacción entre cargas q1 y q2 (en unidades de e) a r [nm], en eV."""
    return q1 * q2 * E / (4 * math.pi * EPS0 * r_nm * 1e-9)


def electrones_valencia(formula: dict[str, int], carga: int = 0) -> int:
    return sum(VALENCIA[a] * n for a, n in formula.items()) - carga


def pruebas() -> None:
    # La energía de Coulomb a un radio de Bohr debe ser 1 Hartree = 2 Ry (relación analítica)
    hartree = coulomb_ev(1, 1, A0_M * 1e9)
    assert abs(hartree - 2 * RY_EV) / (2 * RY_EV) < 1e-4, hartree
    # Cargas opuestas atraen (energía negativa) e iguales repelen
    assert coulomb_ev(1, -1, 0.3) < 0 < coulomb_ev(1, 1, 0.3)
    # La energía escala como 1/r y como q1 q2
    assert abs(coulomb_ev(1, -1, 0.2) / coulomb_ev(1, -1, 0.4) - 2) < 1e-12
    assert abs(coulomb_ev(2, -2, 0.3) / coulomb_ev(1, -1, 0.3) - 4) < 1e-12
    # Conteos de Lewis conocidos
    assert electrones_valencia({"H": 2, "O": 1}) == 8
    assert electrones_valencia({"N": 1, "H": 3}) == 8
    assert electrones_valencia({"C": 1, "O": 2}) == 16
    assert electrones_valencia({"N": 1, "H": 4}, carga=+1) == 8


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"e^2/(4 pi eps0) = {coulomb_ev(1, 1, 1.0):.5f} eV nm")
    print(f"Hartree (r = a0): {coulomb_ev(1, 1, A0_M * 1e9):.4f} eV (2 Ry = {2 * RY_EV:.4f} eV)")
    for r in (0.25, 0.30):
        print(f"Par +1/-1 a {r:.2f} nm (sintético): {coulomb_ev(1, -1, r):+.3f} eV")
    print(f"Par +2/-2 a 0.25 nm (sintético): {coulomb_ev(2, -2, 0.25):+.3f} eV")
    for T in (176, 300):
        print(f"kT a {T} K = {KB_EV * T * 1000:.2f} meV")
    for nombre, f, c in (("H2O", {"H": 2, "O": 1}, 0), ("NH3", {"N": 1, "H": 3}, 0),
                         ("CO2", {"C": 1, "O": 2}, 0), ("NH4+", {"N": 1, "H": 4}, 1)):
        ev = electrones_valencia(f, c)
        print(f"{nombre}: {ev} electrones de valencia = {ev // 2} pares")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
