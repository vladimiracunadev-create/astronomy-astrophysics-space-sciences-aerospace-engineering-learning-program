#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C10: energía térmica kT frente a energía de cohesión por molécula.

Datos PUBLICADOS: CODATA 2022 (k, e, N_A exactas); NIST Chemistry WebBook:
Delta_f H(H2O, gas) = -241,826 kJ/mol y Delta_f H(H2O, líquido) = -285,830 kJ/mol
(Cox, Wagman et al. 1984) => Delta_vap H(298 K) = 44,004 kJ/mol (DERIVADO);
Delta_sub H(CO2) = 26,1 kJ/mol a 207 K (Stephenson y Malanowski 1987, vía WebBook);
NIST ASD v5.12: energía de ionización de H I = 13,598 435 eV; temperaturas de
NASA NSSDC: Marte 214 K, Tierra 288 K, Venus 737 K, fotosfera solar T_ef = 5772 K.
La temperatura de 10 K de una nube densa es ILUSTRATIVA (sintética).
Modelo: comparar epsilon (energía por partícula) con kT; epsilon/kT grande => ligado.
Supuestos: cohesión = entalpía de cambio de fase por molécula, a la T indicada.
Dominio de validez: orden de magnitud; no predice el punto exacto de transición.
Tolerancias: 1e-6 relativo en las relaciones de unidades.
"""

from __future__ import annotations

import sys

K = 1.380649e-23      # J/K, exacta
E = 1.602176634e-19   # C, exacta
NA = 6.02214076e23    # 1/mol, exacta
KB_EV = K / E         # eV/K

DH_FORM_GAS, DH_FORM_LIQ = -241.826, -285.830           # kJ/mol, WebBook
DH_VAP = DH_FORM_GAS - DH_FORM_LIQ                       # kJ/mol a 298 K
DH_SUB_CO2 = 26.1                                        # kJ/mol a 207 K
E_ION_H = 13.598434599702                                # eV, NIST ASD
AMBIENTES = {"Nube densa (10 K, ilustrativo)": 10.0, "Marte (214 K)": 214.0,
             "Tierra (288 K)": 288.0, "Venus (737 K)": 737.0, "Fotosfera solar (5772 K)": 5772.0}


def kj_mol_a_ev(x: float) -> float:
    return x * 1e3 / (NA * E)


def kt_ev(T: float) -> float:
    return KB_EV * T


def pruebas() -> None:
    assert abs(kt_ev(300.0) - 0.025852) < 1e-6                 # 25,85 meV a 300 K (valor conocido)
    assert abs(DH_VAP - 44.004) < 1e-9                         # clausura de Hess con datos NIST
    assert abs(kj_mol_a_ev(96.48533212) - 1.0) < 1e-6          # 1 eV = 96,485 kJ/mol (N_A e)
    assert abs(kj_mol_a_ev(DH_VAP) - 0.4561) < 1e-4
    assert abs(E_ION_H / KB_EV - 157_800) < 100                # T con kT = 13,6 eV


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    eps_agua, eps_co2 = kj_mol_a_ev(DH_VAP), kj_mol_a_ev(DH_SUB_CO2)
    print(f"Delta_vap H(H2O) = {DH_VAP:.3f} kJ/mol = {eps_agua:.4f} eV/molécula ; "
          f"Delta_sub H(CO2) = {DH_SUB_CO2} kJ/mol = {eps_co2:.4f} eV")
    print("Ambiente | kT [meV] | eps_agua/kT | eps_CO2/kT | E_ion(H)/kT")
    for n, T in AMBIENTES.items():
        k = kt_ev(T)
        print(f"  {n:34s} {k * 1000:9.3f}  {eps_agua / k:9.1f}  {eps_co2 / k:9.1f}  {E_ION_H / k:10.1f}")
    print(f"T con kT = eps_agua: {eps_agua / KB_EV:.0f} K ; T con kT = E_ion(H): {E_ION_H / KB_EV:.0f} K")
    print(f"Agua en su punto de ebullición (373,17 K): eps/kT = {eps_agua / kt_ev(373.17):.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
