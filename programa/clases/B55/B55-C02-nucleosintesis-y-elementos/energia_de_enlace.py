#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C02: energia de enlace por nucleon y energia de reacciones de quemado nuclear.

Datos (NIST, consultados el 2026-11-09): masas atomicas relativas de H-1, H-2, He-4, C-12, O-16, Mg-24, Si-28, Ca-40, Fe-56 y Ni-62 (Atomic Weights and
Isotopic Compositions); masa del neutron 1.00866491606 u y equivalente energetico de la unidad de masa atomica 931.49410372 MeV (CODATA 2022).
Modelo: B = Z M(H-1) + N m_n - M(atomo), con masas ATOMICAS (los electrones se cancelan); Q = (suma de masas atomicas iniciales - finales) c^2.
Supuestos: nucleos en reposo y estado fundamental; sin energia de neutrinos (las masas atomicas incluyen todo el balance de H-1 a He-4).
Validez: balance de masa; no da tasas de reaccion. Tolerancia: dos caminos de calculo de B coinciden a 1e-9 MeV; ciclo de Q cerrado a 1e-9 MeV.
"""
from __future__ import annotations
import platform

U_MEV = 931.49410372        # MeV por u (CODATA 2022)
M_N = 1.00866491606         # u (CODATA 2022)
M_H1 = 1.00782503223        # u (NIST)
# nombre: (Z, A, masa atomica en u)  -- NIST
NUCL = {
    "H-2": (1, 2, 2.01410177812),
    "He-4": (2, 4, 4.00260325413),
    "C-12": (6, 12, 12.0),
    "O-16": (8, 16, 15.99491461957),
    "Mg-24": (12, 24, 23.985041697),
    "Si-28": (14, 28, 27.97692653465),
    "Ca-40": (20, 40, 39.962590863),
    "Fe-56": (26, 56, 55.93493633),
    "Ni-62": (28, 62, 61.92834537),
}

def enlace(Z, A, M):
    N = A - Z
    return (Z * M_H1 + N * M_N - M) * U_MEV

def enlace_por_exceso(Z, A, M):
    """Segundo camino: con excesos de masa Delta = M - A (en u)."""
    N = A - Z
    d_h, d_n, d = M_H1 - 1.0, M_N - 1.0, M - A
    return (Z * d_h + N * d_n - d) * U_MEV

def q(entra, sale):
    return (sum(NUCL[x][2] * c for x, c in entra) - sum(NUCL[x][2] * c for x, c in sale)) * U_MEV

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("A. Energia de enlace por nucleon (masas atomicas NIST, constantes CODATA 2022)")
    print("nuclido   B total [MeV]   B/A [MeV]")
    ba = {}
    for k, (Z, A, M) in NUCL.items():
        b = enlace(Z, A, M)
        assert abs(b - enlace_por_exceso(Z, A, M)) < 1e-9
        ba[k] = b / A
        print(f"{k:>7}   {b:12.4f}   {b / A:9.4f}")
    maximo = max(ba, key=ba.get)
    assert maximo in ("Fe-56", "Ni-62") and ba["Fe-56"] > ba["Ca-40"] > ba["C-12"] > ba["H-2"]
    print(f"Maximo de B/A en el conjunto: {maximo} ({ba[maximo]:.4f} MeV)")
    print("B. Energia liberada por reaccion de quemado (Q = masas iniciales - finales)")
    q_h = (4 * M_H1 - NUCL["He-4"][2]) * U_MEV
    q_3a = q([("He-4", 3)], [("C-12", 1)])
    q_ca = q([("C-12", 1), ("He-4", 1)], [("O-16", 1)])
    q_cc = q([("C-12", 2)], [("Mg-24", 1)])
    q_oo = q([("O-16", 2)], [("Si-28", 1), ("He-4", 1)])
    q_dd = q([("H-2", 2)], [("He-4", 1)])
    print(f"4 H-1 -> He-4           Q = {q_h:9.4f} MeV")
    print(f"3 He-4 -> C-12          Q = {q_3a:9.4f} MeV")
    print(f"C-12 + He-4 -> O-16     Q = {q_ca:9.4f} MeV")
    print(f"2 C-12 -> Mg-24         Q = {q_cc:9.4f} MeV")
    print(f"2 O-16 -> Si-28 + He-4  Q = {q_oo:9.4f} MeV")
    print(f"2 H-2 -> He-4           Q = {q_dd:9.4f} MeV")
    # ciclo: 3 a -> C12 -> (+a) O16 equivale a 4 a -> O16
    directo = q([("He-4", 4)], [("O-16", 1)])
    assert abs(q_3a + q_ca - directo) < 1e-9
    print(f"C. Cierre del ciclo: Q(3a)+Q(C12+a) = {q_3a + q_ca:.6f} MeV ; Q(4 a -> O-16) = {directo:.6f} MeV")
    # energia por masa de combustible
    u_kg = 1.66053906892e-27   # kg por u (CODATA 2022)
    mev_j = 1.602176634e-13    # J por MeV (e exacto)
    eps_h = q_h / (4 * M_H1 * U_MEV)
    j_kg_h = q_h * mev_j / (4 * M_H1 * u_kg)
    eps_3a = q_3a / (3 * NUCL["He-4"][2] * U_MEV)
    print(f"D. Fraccion de masa liberada: H->He {eps_h:.5f} ; 3a->C {eps_3a:.5f} ; energia por kg de H: {j_kg_h:.4e} J/kg")
    assert 0.0065 < eps_h < 0.0075
    assert eps_3a < eps_h / 5
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
