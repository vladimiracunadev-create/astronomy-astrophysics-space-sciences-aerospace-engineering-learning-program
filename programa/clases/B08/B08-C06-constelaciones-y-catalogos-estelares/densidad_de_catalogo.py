#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C06: cuántas fuentes de un catálogo caben en un campo de visión.

Datos PUBLICADOS: Gaia DR3 contiene 1 811 709 771 fuentes (ESA, https://www.cosmos.esa.int/web/gaia/dr3,
consultada 2026-11-05); el catálogo estelar por defecto de Stellarium tiene «más de 600 000» estrellas
(https://stellarium.org/, consultada 2026-11-05; se usa 600 000 como cota inferior). Salidas: promedios
CALCULADOS sobre toda la esfera; la densidad real varía mucho (plano galáctico vs polos).
Prueba independiente: el área de la esfera celeste en grados cuadrados, 4*pi*(180/pi)^2, comparada con el
valor analítico 41 252,96 grados cuadrados. Tolerancia: 0,01 grados cuadrados.
"""
from __future__ import annotations

import math
import sys

GAIA_DR3 = 1_811_709_771
STELLARIUM_BASE = 600_000          # cota inferior publicada
AREA_ESFERA_DEG2 = 4.0 * math.pi * (180.0 / math.pi) ** 2


def area_campo_deg2(diametro_deg: float) -> float:
    """Área (grados cuadrados) de un campo circular pequeño, en aproximación plana."""
    return math.pi * (diametro_deg / 2.0) ** 2


def pruebas() -> None:
    assert abs(AREA_ESFERA_DEG2 - 41252.96) < 0.01, AREA_ESFERA_DEG2
    assert abs(area_campo_deg2(2.0) - math.pi) < 1e-12            # campo de 2 grados de diámetro: pi grados cuadrados
    # Semiesfera por casquete exacto: A = 2*pi*(1-cos(theta)) estereorradianes; theta=90 -> media esfera
    assert abs(2 * math.pi * (1 - math.cos(math.pi / 2)) * (180 / math.pi) ** 2 - AREA_ESFERA_DEG2 / 2) < 1e-6


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Area de la esfera celeste: {AREA_ESFERA_DEG2:.2f} grados cuadrados")
    d_gaia = GAIA_DR3 / AREA_ESFERA_DEG2
    d_stel = STELLARIUM_BASE / AREA_ESFERA_DEG2
    print(f"Densidad media Gaia DR3: {d_gaia:,.0f} fuentes por grado cuadrado (CALCULADA; promedio)")
    print(f"Densidad media catalogo base de Stellarium (cota inferior): {d_stel:.1f} por grado cuadrado")
    print(f"Cociente Gaia / Stellarium base: {GAIA_DR3 / STELLARIUM_BASE:,.0f}")
    for nombre, diam in [("campo de ocular de telescopio (0,5 grados)", 0.5), ("binoculares (6,5 grados)", 6.5)]:
        a = area_campo_deg2(diam)
        print(f"{nombre}: area {a:.2f} deg2 -> Gaia medio {a * d_gaia:,.0f}; Stellarium base {a * d_stel:,.0f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
