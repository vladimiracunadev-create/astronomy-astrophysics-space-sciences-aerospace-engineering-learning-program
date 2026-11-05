#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C01: niveles de energía del hidrógeno y líneas de Balmer.

Datos PUBLICADOS: CODATA 2022 (NIST) para R_inf, h, c, e (exactos desde 2019)
y la razón m_p/m_e; longitudes de onda observadas en aire y energía de ionización de la NIST
Atomic Spectra Database v5.12 (rango de las componentes de estructura fina).
Modelo: fórmula de Rydberg con masa reducida del núcleo (modelo de Bohr).
Supuestos: átomo de un electrón, sin estructura fina ni efecto Lamb;
índice de refracción del aire constante n = 1,000277 (aproximación).
Dominio de validez: líneas Balmer H-alfa a H-delta, átomo aislado.
Tolerancia: 0,02 nm respecto del rango observado en aire (la aproximación
del índice de aire domina el residuo).
"""

from __future__ import annotations

import sys

R_INF = 10_973_731.568157      # m^-1, CODATA 2022
MP_ME = 1836.152673426         # CODATA 2022
H = 6.62607015e-34             # J s, exacto
C = 299_792_458                # m/s, exacto
E = 1.602176634e-19            # C (J/eV), exacto
N_AIRE = 1.000277              # aproximación para ~400-700 nm

R_H = R_INF / (1 + 1 / MP_ME)  # constante de Rydberg del hidrógeno [m^-1]

# NIST ASD v5.12: rango (mín, máx) de componentes en aire [nm]
ASD_AIRE = {3: (656.270970, 656.290944), 4: (486.1278624, 486.1374864),
            5: (434.0426937, 434.0499857), 6: (410.1702284, 410.1765915)}


def energia_nivel_ev(n: int) -> float:
    """Energía del nivel n medida desde el límite de ionización [eV] (negativa)."""
    return -(H * C * R_INF / E) / n**2


def lambda_vacio_nm(n_alto: int, n_bajo: int = 2, rydberg: float = R_H) -> float:
    return 1e9 / (rydberg * (1 / n_bajo**2 - 1 / n_alto**2))


def pruebas() -> None:
    # 1) hc R_inf debe coincidir con el valor CODATA publicado de 13,605 693 122 990 eV
    assert abs(-energia_nivel_ev(1) - 13.605693122990) < 1e-6
    # 2) la serie de Lyman converge a 1/R_inf = 91,1267 nm (límite analítico)
    assert abs(1e9 / R_INF - 91.126705) < 1e-4
    # 3) la energía de ionización con masa reducida coincide con la de la NIST ASD (13,598 4346 eV)
    # dentro de 2e-4 eV (el resto es retroceso relativista y desplazamiento de Lamb)
    assert abs(-energia_nivel_ev(1) / (1 + 1 / MP_ME) - 13.598434599702) < 2e-4
    # 4) las líneas calculadas en aire caen a menos de 0,02 nm del rango observado
    for n, (lo, hi) in ASD_AIRE.items():
        aire = lambda_vacio_nm(n) / N_AIRE
        assert lo - 0.02 <= aire <= hi + 0.02, (n, aire)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Niveles (E_n = -13,6057/n^2 eV):")
    for n in range(1, 5):
        print(f"  n={n}: {energia_nivel_ev(n):9.4f} eV")
    print("Balmer: n_alto | vacío [nm] | aire calculado [nm] | rango ASD en aire [nm]")
    for n, (lo, hi) in ASD_AIRE.items():
        lv = lambda_vacio_nm(n)
        print(f"  {n}  {lv:9.4f}  {lv / N_AIRE:9.4f}   {lo:.4f}-{hi:.4f}")
    e_ha = 1e9 * H * C / E / lambda_vacio_nm(3)
    print(f"Ionización con masa reducida: {-energia_nivel_ev(1) / (1 + 1 / MP_ME):.4f} eV (NIST ASD: 13.5984 eV)")
    print(f"Fotón H-alfa: {e_ha:.4f} eV  (= E3 - E2 = {energia_nivel_ev(3) - energia_nivel_ev(2):.4f} eV en valor absoluto)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
