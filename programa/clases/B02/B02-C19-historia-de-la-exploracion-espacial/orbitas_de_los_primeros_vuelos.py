#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B02-C19: órbitas de los primeros vuelos con la tercera ley de Kepler.

Datos PUBLICADOS (consultados el 2026-11-05): período de Sputnik 1, «unos 98 minutos» (NASA History);
semieje mayor de la Luna 384,4x10^3 km y período sidéreo 27,3217 d (NASA Moon Fact Sheet);
radio ecuatorial terrestre 6 378,137 km y rotación sidérea 23,9345 h (NASA Earth Fact Sheet).
Modelo: tercera ley con el mismo cuerpo central (Tierra): a = a_Luna * (T / T_Luna)^(2/3), órbita circular.
Supuestos: masa de la Luna despreciable frente a la de la Tierra; órbita circular. Validez: altitud media
de una órbita de período dado, con ~1 %; NO reproduce perigeo ni apogeo.
Tolerancia: 0,6 % en la comprobación con la órbita geoestacionaria (la masa de la Luna, ~1 % de la terrestre,
explica una diferencia de unos 0,4 %).
"""

from __future__ import annotations

import math
import sys

A_LUNA = 384_400.0            # km
T_LUNA_MIN = 27.3217 * 1440.0   # min
R_EQ = 6378.137               # km
ROT_SIDEREA_MIN = 23.9345 * 60.0   # min


def semieje_km(periodo_min: float) -> float:
    return A_LUNA * (periodo_min / T_LUNA_MIN) ** (2.0 / 3.0)


def pruebas() -> None:
    assert abs(semieje_km(T_LUNA_MIN) - A_LUNA) < 1e-9                 # caso analítico: la propia Luna
    a_geo = semieje_km(ROT_SIDEREA_MIN)
    alt_geo = a_geo - R_EQ
    assert abs(alt_geo / 35_786.0 - 1.0) < 0.006, alt_geo               # referencia independiente (memoria): ~35 786 km
    assert abs(semieje_km(2 * T_LUNA_MIN) / A_LUNA - 2 ** (2 / 3)) < 1e-12   # escalado T^(2/3)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    t = 98.0
    a = semieje_km(t)
    v = 2 * math.pi * a / (t * 60.0)
    print(f"Sputnik 1 (~98 min): a = {a:,.0f} km; altitud media sobre el ecuador ≈ {a - R_EQ:,.0f} km; velocidad media ≈ {v:.2f} km/s")
    print("Vostok 1: los 108 min son la duración del VUELO (ascenso, una vuelta y descenso), no el período orbital → no se usa")
    a_geo = semieje_km(ROT_SIDEREA_MIN)
    print(f"Comprobación: período = rotación sidérea → a = {a_geo:,.0f} km; altitud ≈ {a_geo - R_EQ:,.0f} km (referencia ~35 786 km)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
