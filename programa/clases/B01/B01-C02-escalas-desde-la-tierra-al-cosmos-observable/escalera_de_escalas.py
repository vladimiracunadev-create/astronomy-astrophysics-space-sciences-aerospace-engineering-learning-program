#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C02: escalera de escalas desde la Tierra al cosmos observable.

Datos (ver tabla de fuentes de la clase): valores PUBLICADOS (observados o
estimados) tomados de NASA Planetary/Earth/Moon Fact Sheets, IAU 2015 B3,
NASA Exoplanet Archive, Riess et al. 2012, Mei et al. 2007 y del laboratorio de
B01-C01 (modelo, SIMULADO). Salidas: logaritmos decimales y cocientes.

Sistema de referencia: distancias medias, sin tratar excentricidad ni época.
Tolerancia de las pruebas: 1e-9 relativa (constantes exactas) y 1e-3 (cocientes).
"""

from __future__ import annotations

import math

C = 299_792_458.0                     # m/s, exacto (SI)
AU = 149_597_870_700.0                # m, exacto (SI, IAU 2012 B2)
PC = 648_000.0 / math.pi * AU         # m, exacto por definición (IAU 2015 B2, nota 4)
YEAR_S = 365.25 * 86_400.0            # s, año juliano
LY = C * YEAR_S                       # m

ESCALERA = [
    # (nombre, distancia o radio en m, origen del dato)
    ("Radio medio de la Tierra",        6.371e6,        "NASA Earth Fact Sheet (6371 km)"),
    ("Distancia media Tierra–Luna",     3.844e8,        "NASA Moon Fact Sheet (384,4 × 10³ km)"),
    ("Radio nominal del Sol",           6.957e8,        "IAU 2015 B3"),
    ("1 unidad astronómica",            AU,             "SI / IAU 2012 B2"),
    ("Distancia Sol–Neptuno",           4515.0e9,       "NASA Planetary Fact Sheet (4515 × 10⁶ km)"),
    ("Distancia a Próxima Centauri",    1.30119 * PC,   "NASA Exoplanet Archive (1,30119 pc)"),
    ("Distancia a Andrómeda (M31)",     765e3 * PC,     "Riess et al. 2012 (765 ± 28 kpc)"),
    ("Distancia al cúmulo de Virgo",    16.5e6 * PC,    "Mei et al. 2007 (16,5 Mpc)"),
    ("Radio observable (ΛCDM, hoy)",    46.13e9 * LY,   "Laboratorio B01-C01 (modelo)"),
]


def pruebas() -> None:
    assert abs(PC - 3.0856775814913673e16) / PC < 1e-9          # parsec en metros
    assert abs(LY - 9.4607304725808e15) / LY < 1e-9              # año luz en metros
    assert abs(AU / C - 499.00478384) < 1e-6                     # luz del Sol en segundos
    assert abs(PC / LY - 3.261563777) < 1e-6                     # pc en ly
    ratios = {n: d for n, d, _ in ESCALERA}
    assert abs(ratios["Radio nominal del Sol"] / ratios["Radio medio de la Tierra"] - 109.2) < 0.1
    assert abs(ratios["Distancia Sol–Neptuno"] / AU - 30.18) < 0.02


def main() -> int:
    pruebas()
    print("Pruebas de unidades: OK")
    print(f"{'Objeto':<34}{'metros':>12}{'log10':>8}{'en au':>14}{'x anterior':>12}")
    previo = None
    for nombre, d, _ in ESCALERA:
        factor = "" if previo is None else f"{d / previo:12.3g}"
        print(f"{nombre:<34}{d:12.4g}{math.log10(d):8.2f}{d / AU:14.4g}{factor:>12}")
        previo = d
    total = ESCALERA[-1][1] / ESCALERA[0][1]
    print(f"\nDel radio terrestre al radio observable: factor {total:.3g} "
          f"({math.log10(total):.1f} órdenes de magnitud)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
