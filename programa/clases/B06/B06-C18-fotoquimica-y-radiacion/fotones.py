#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C18: energía del fotón, energía por mol de fotones y umbrales.

Datos PUBLICADOS: CODATA 2022 (NIST): h, c, e, N_A exactas y R_inf, m_p/m_e;
NIST ASD v5.12: energía de ionización de H I = 13,598 434 599 702 eV;
NIST WebBook: Delta_vap H(H2O) = 44,004 kJ/mol (derivado, C12) y Delta_sub H(CO2) =
26,1 kJ/mol. La barrera de 50 kJ/mol es SINTÉTICA (la de C14). Las fronteras
UV/visible/IR (400 y 700 nm) son una convención de la clase.
Modelo: E = h c / lambda ; E_mol = N_A E ; lambda_umbral = h c / E_umbral.
Supuestos: un fotón actúa sobre una partícula; el umbral energético es necesario,
no suficiente (también hace falta que la partícula absorba). Dominio de validez:
orden de magnitud. Tolerancias: 1e-6 relativo en h c ; 2e-3 nm entre dos rutas
independientes para el límite de Lyman.
"""

from __future__ import annotations

import sys

H, C, E, NA = 6.62607015e-34, 299_792_458, 1.602176634e-19, 6.02214076e23
HC_EV_NM = H * C / E * 1e9            # eV nm
R_INF, MP_ME = 10_973_731.568157, 1836.152673426
R_H = R_INF / (1 + 1 / MP_ME)
IE_H_EV = 13.598434599702            # NIST ASD
DH_VAP_EV = 44_004.0 / (NA * E)
DH_SUB_CO2_EV = 26_100.0 / (NA * E)
BARRERA_SINT_EV = 50_000.0 / (NA * E)


def energia_ev(lambda_nm: float) -> float:
    return HC_EV_NM / lambda_nm


def energia_kj_mol(lambda_nm: float) -> float:
    return energia_ev(lambda_nm) * E * NA / 1000


def lambda_umbral_nm(e_ev: float) -> float:
    return HC_EV_NM / e_ev


def banda(lambda_nm: float) -> str:
    return "ultravioleta" if lambda_nm < 400 else ("visible" if lambda_nm <= 700 else "infrarrojo")


def pruebas() -> None:
    assert abs(HC_EV_NM - 1239.84198) < 1e-4
    # límite de Lyman por dos rutas independientes: 1/R_H y h c / IE (NIST ASD)
    assert abs(1e9 / R_H - lambda_umbral_nm(IE_H_EV)) < 2e-3
    assert abs(energia_ev(121.567) - 10.1988) < 1e-3
    assert banda(121.567) == "ultravioleta" and banda(656.3) == "visible" and banda(2718) == "infrarrojo"
    assert abs(energia_kj_mol(1239.84198) - 96.4853) < 1e-3      # 1 eV = 96,485 kJ/mol


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"h c = {HC_EV_NM:.5f} eV nm ; 1 eV = {E * NA / 1000:.4f} kJ/mol")
    print("lambda [nm] | banda | E [eV] | E [kJ/mol de fotones]")
    for lam in (91.176, 121.567, 250.0, 400.0, 656.47, 1000.0, 2718.0):
        print(f"  {lam:8.3f}  {banda(lam):12s} {energia_ev(lam):8.4f}  {energia_kj_mol(lam):9.2f}")
    print(f"Umbral de ionización del H (fundamental): {lambda_umbral_nm(IE_H_EV):.3f} nm (1/R_H = {1e9 / R_H:.3f} nm)")
    print(f"Ionizar desde n=2 (3.4 eV): {lambda_umbral_nm(IE_H_EV / 4):.2f} nm")
    print(f"Umbral para 0.4561 eV (Delta_vap H del agua): {lambda_umbral_nm(DH_VAP_EV):.0f} nm ; "
          f"CO2 sublimación: {lambda_umbral_nm(DH_SUB_CO2_EV):.0f} nm ; barrera sintética 50 kJ/mol: {lambda_umbral_nm(BARRERA_SINT_EV):.0f} nm")
    print(f"Fotones de Lyman-alfa en 1 J: {1 / (energia_ev(121.567) * E):.3e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
