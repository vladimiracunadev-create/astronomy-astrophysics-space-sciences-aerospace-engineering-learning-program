#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C12: constantes exactas, constantes medidas y variables.

Datos PUBLICADOS: constantes definitorias del SI (c, h, k, N_A, Δν_Cs; BIPM SI 9.ª ed.); G de CODATA
2022 = 6,67430e-11 con incertidumbre estándar relativa 2,2e-5 (NIST); (GM)sol nominal =
1,3271244e20 m3 s-2 (IAU 2015 B3, exacto por definición); masa del Sol 1,9884e30 kg (NASA Sun Fact
Sheet). Modelo: M = GM / G. Supuestos: la incertidumbre de M proviene solo de G (GM nominal es
exacto por convención). Validez: ilustra la jerarquía de las constantes. Tolerancia: 0,01 % frente
al valor de la NASA.
"""
from __future__ import annotations

import platform

CONSTANTES_EXACTAS = {
    "c [m/s]": 299_792_458,
    "ΔνCs [Hz]": 9_192_631_770,
    "h [J s]": 6.62607015e-34,
    "k [J/K]": 1.380649e-23,
    "N_A [1/mol]": 6.02214076e23,
}
G, U_REL_G = 6.67430e-11, 2.2e-5
GM_SOL = 1.3271244e20
M_SOL_NASA = 1.9884e30


def masa(gm: float, g: float) -> float:
    return gm / g


def pruebas() -> None:
    assert all(v > 0 for v in CONSTANTES_EXACTAS.values())
    m = masa(GM_SOL, G)
    assert abs(m - M_SOL_NASA) / M_SOL_NASA < 1e-4, m
    # una constante medida con u relativa 2,2e-5 da una masa con la misma incertidumbre relativa
    assert abs(U_REL_G * m - 4.4e25) < 0.1e25
    # GM se conoce mejor que G: GM exacto -> la incertidumbre de M es la de G


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    for nombre, v in CONSTANTES_EXACTAS.items():
        print(f"Constante exacta {nombre:12s} = {v!r}")
    m = masa(GM_SOL, G)
    print(f"M_sol = GM/G = {m:.5e} kg (NASA: {M_SOL_NASA:.4e}); diferencia {abs(m - M_SOL_NASA) / M_SOL_NASA * 100:.4f} %")
    print(f"Incertidumbre estándar de M por G: ±{U_REL_G * m:.2e} kg (relativa {U_REL_G:.1e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
