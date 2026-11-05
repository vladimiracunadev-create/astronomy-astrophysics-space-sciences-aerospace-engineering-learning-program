#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B02-C16: las líneas de Balmer del hidrógeno a partir de la constante de Rydberg.

Datos PUBLICADOS (consultados el 2026-11-05): constante de Rydberg R_inf = 10 973 731,568 157 1/m y
razón de masas protón/electrón 1 836,152 673 426 (NIST, CODATA 2022); longitudes de onda en AIRE
de las líneas H-alfa, H-beta, H-gamma, H-delta (NIST, tabla «Strong Lines of Hydrogen»).
Modelo: Bohr con masa reducida, 1/lambda_vac = R_H (1/4 - 1/n^2), R_H = R_inf/(1 + me/mp).
Conversión vacío -> aire con la fórmula de dispersión de Edlén (1966), escrita de memoria y
VALIDADA aquí contra NIST (no es una fuente consultada). Supuestos: hidrógeno ligero, sin estructura fina.
Validez: líneas visibles de Balmer; tolerancia 5e-5 en longitud de onda relativa respecto de NIST.
"""

from __future__ import annotations

import sys

R_INF = 10_973_731.568157          # 1/m, CODATA 2022 (NIST)
MP_ME = 1836.152673426             # CODATA 2022 (NIST)
# NIST (aire), valor central de cada línea: H-alfa, H-beta, H-gamma, H-delta
NIST_AIRE_NM = {3: 656.2711, 4: 486.1279, 5: 434.0462, 6: 410.1739}
NOMBRE = {3: "Hα", 4: "Hβ", 5: "Hγ", 6: "Hδ"}


def lambda_vacio_nm(n: int) -> float:
    r_h = R_INF / (1.0 + 1.0 / MP_ME)
    return 1e9 / (r_h * (0.25 - 1.0 / n**2))


def indice_aire(lam_vac_nm: float) -> float:
    s2 = (1e3 / lam_vac_nm) ** 2        # sigma^2 en 1/µm²
    return 1.0 + 1e-8 * (8342.13 + 2406030.0 / (130.0 - s2) + 15997.0 / (38.9 - s2))


def lambda_aire_nm(n: int) -> float:
    lv = lambda_vacio_nm(n)
    return lv / indice_aire(lv)


def pruebas() -> None:
    assert abs(lambda_vacio_nm(3) - 656.47) < 0.02                  # valor en vacío conocido de H-alfa (~656,47 nm)
    for n, ref in NIST_AIRE_NM.items():
        assert abs(lambda_aire_nm(n) / ref - 1.0) < 5e-5, (n, lambda_aire_nm(n), ref)
    assert lambda_vacio_nm(3) > lambda_vacio_nm(4) > lambda_vacio_nm(5) > lambda_vacio_nm(6)   # serie convergente


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"{'Línea':6s} {'λ vacío [nm]':>14s} {'λ aire calc. [nm]':>19s} {'NIST aire [nm]':>16s} {'dif. relativa':>14s}")
    for n in (3, 4, 5, 6):
        la, ref = lambda_aire_nm(n), NIST_AIRE_NM[n]
        print(f"{NOMBRE[n]:6s} {lambda_vacio_nm(n):14.4f} {la:19.4f} {ref:16.4f} {la / ref - 1:14.2e}")
    limite = 1e9 / ((R_INF / (1 + 1 / MP_ME)) * 0.25)
    print(f"Límite de la serie (n→∞), vacío: {limite:.3f} nm")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
