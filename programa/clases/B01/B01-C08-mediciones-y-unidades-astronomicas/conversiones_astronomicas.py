#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C08: hoja de conversiones astronómicas con análisis dimensional.

Datos: constantes DEFINIDAS (BIPM SI 9.ª ed.: c, 1 au; año juliano = 365,25 d por
convención) y la distancia de ejemplo de la galaxia de Hα de C01 (43 Mpc, valor
ESTIMADO para docencia). El parsec se toma como (648 000/π) au (definición IAU, citada en C02)
y se contrasta con la geometría 1 au / tan(1″). Supuestos: valores exactos por definición; sin
incertidumbre en las conversiones. Dominio de validez: conversiones de longitud y tiempo.
Tolerancia: igualdad exacta en enteros; 1e-10 relativa pc frente a la geometría; 1e-6 absoluta en el tiempo de luz. Las pruebas se
detienen si alguna falla.
"""

from __future__ import annotations

import math
import platform
import sys

C = 299_792_458                      # m/s, exacto (SI)
AU = 149_597_870_700                 # m, exacto (SI/IAU)
ANIO_JULIANO_S = 365.25 * 86_400     # s, convención
SEG_ARCO_RAD = math.pi / (180 * 3600)  # rad por segundo de arco

LY = C * 31_557_600                  # m (entero, exacto con el año juliano)
PC = AU * 648_000 / math.pi          # m, definición IAU: (648 000/π) au


def pruebas() -> None:
    assert LY == 9_460_730_472_580_800                         # entero conocido por definición
    geometrico = AU / math.tan(SEG_ARCO_RAD)                  # referencia independiente: 1 au subtiende 1″
    assert abs(PC - geometrico) / PC < 1e-10                  # difieren ~8e-12 por tan(x) ≈ x
    assert abs(AU / C - 499.0047838) < 1e-6                    # tiempo de luz de 1 au [s]
    assert abs(PC / LY - 3.2615637771) < 1e-9                  # pc en años luz
    # análisis dimensional: v [km/s] / H0 [km/s/Mpc] = d [Mpc]
    v, h0 = 3015.0, 70.0
    assert abs(v / h0 - 43.07) < 0.01


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    print(f"1 au = {AU} m ; tiempo de luz de 1 au = {AU / C:.4f} s = {AU / C / 60:.4f} min")
    print(f"1 ly = {LY} m = {LY / AU:.1f} au")
    print(f"1 pc = {PC:.6e} m = {PC / AU:.3f} au = {PC / LY:.4f} ly")
    d_mpc = 43.0
    d_m = d_mpc * 1e6 * PC
    print(f"43 Mpc = {d_m:.4e} m = {d_mpc * 1e6 * PC / LY:.4e} ly = {d_mpc * 1e6 * PC / AU:.4e} au")
    print(f"Tiempo de luz de 43 Mpc = {d_m / C / ANIO_JULIANO_S:.4e} años julianos")
    print(f"Radio solar nominal / 1 au = {6.957e8 / AU:.5f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
