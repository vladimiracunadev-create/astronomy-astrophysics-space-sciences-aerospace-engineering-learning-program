#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C04: ciclos astronómicos y escalas de tiempo.

Datos PUBLICADOS (NASA NSSDC Earth y Moon Fact Sheets; SI 9.ª ed.). Salidas:
cálculos derivados. Supuestos: períodos medios constantes. Dominio de validez:
valores medios, no efemérides. Tolerancias: 0,01 d en el período sinódico y
exactitud entera en las constantes exactas.
"""

from __future__ import annotations

import sys

C = 299_792_458                   # m/s, exacto (SI)
CS_HZ = 9_192_631_770             # Hz, exacto (SI): cesio-133

# NASA Earth Fact Sheet (act. 15-nov-2024)
DIA_SIDEREO_H = 23.9345           # rotación sidérea [h]
DIA_SOLAR_H = 24.0                # día solar medio [h]
ANIO_SIDEREO_D = 365.256          # período orbital sidéreo [d]
ANIO_TROPICO_D = 365.242          # período orbital trópico [d]
# NASA Moon Fact Sheet (act. 11-ene-2024)
LUNA_SIDEREA_D = 27.3217          # revolución sidérea [d]
LUNA_SINODICA_D = 29.53           # período sinódico publicado [d]


def pruebas() -> None:
    assert abs(C * 1e-9 - 0.299792458) < 1e-12                       # distancia de la luz en 1 ns [m]
    assert CS_HZ * 86_400 == 794_243_384_928_000           # períodos de cesio en 86 400 s
    sinodica = 1.0 / (1.0 / LUNA_SIDEREA_D - 1.0 / ANIO_SIDEREO_D)
    assert abs(sinodica - LUNA_SINODICA_D) < 0.01, sinodica   # coincide con el valor publicado
    dias_siderios = ANIO_SIDEREO_D * DIA_SOLAR_H / DIA_SIDEREO_H
    assert abs(dias_siderios - (ANIO_SIDEREO_D + 1.0)) < 0.01, dias_siderios  # 1 día sidéreo extra por año


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    dif_min = (DIA_SOLAR_H - DIA_SIDEREO_H) * 60
    print(f"Día solar − día sidéreo: {dif_min:.2f} min")
    print(f"Días sidéreos por año sidéreo: {ANIO_SIDEREO_D * DIA_SOLAR_H / DIA_SIDEREO_H:.2f}")
    sinodica = 1.0 / (1.0 / LUNA_SIDEREA_D - 1.0 / ANIO_SIDEREO_D)
    print(f"Período sinódico calculado: {sinodica:.3f} d (publicado: {LUNA_SINODICA_D} d)")
    dif = (ANIO_SIDEREO_D - ANIO_TROPICO_D)
    print(f"Año sidéreo − año trópico: {dif:.3f} d = {dif * 1440:.1f} min")
    print(f"Períodos de cesio en un día de 86 400 s: {CS_HZ * 86_400:.4e}")
    print(f"Distancia de la luz en 1 ns: {C * 1e-9:.4f} m")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
