#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B02-C08: de la orientación medida a la declinación astronómica.

Datos: SINTÉTICOS (sitio imaginario a latitud −10°; azimuts inventados para ilustrar).
Constante PUBLICADA: oblicuidad de la Tierra 23,44° (NASA NSSDC Earth Fact Sheet,
consultada el 2026-11-05). Modelo: geometría esférica sin refracción ni semidiámetro
solar; horizonte con altura h conocida. Supuestos: Tierra esférica, declinación constante
durante el día. Validez: declinaciones de orden de 0,5°; no sustituye una efeméride.
Tolerancia de las pruebas: 1e-9 grados en casos analíticos.
Fórmula: sin(dec) = sin(lat)·sin(h) + cos(lat)·cos(h)·cos(A), con A azimut desde el norte.
"""

from __future__ import annotations

import math
import sys

OBLICUIDAD = 23.44   # grados, NASA NSSDC Earth Fact Sheet


def declinacion(lat: float, azimut: float, altura: float = 0.0) -> float:
    la, a, h = map(math.radians, (lat, azimut, altura))
    s = math.sin(la) * math.sin(h) + math.cos(la) * math.cos(h) * math.cos(a)
    return math.degrees(math.asin(max(-1.0, min(1.0, s))))


def azimut_de_salida(lat: float, dec: float) -> float:
    """Azimut (desde el norte, hacia el este) de la salida geométrica de un astro con declinación `dec`."""
    c = math.sin(math.radians(dec)) / math.cos(math.radians(lat))
    return math.degrees(math.acos(c))


def pruebas() -> None:
    assert abs(declinacion(-33.0, 90.0)) < 1e-9                        # este verdadero: equinoccio
    assert abs(declinacion(-30.0, 0.0) - 60.0) < 1e-9                  # norte, horizonte plano: 90 − |lat|
    assert abs(azimut_de_salida(0.0, OBLICUIDAD) - (90.0 - OBLICUIDAD)) < 1e-9   # ecuador, solsticio
    lat = -10.0
    assert abs(declinacion(lat, azimut_de_salida(lat, 17.5)) - 17.5) < 1e-9       # ida y vuelta


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    lat = -10.0
    print(f"Sitio SINTÉTICO a latitud {lat}°, horizonte plano")
    for nombre, dec in (("solsticio de junio", OBLICUIDAD), ("equinoccio", 0.0), ("solsticio de diciembre", -OBLICUIDAD)):
        print(f"  {nombre}: salida geométrica en azimut {azimut_de_salida(lat, dec):.2f}° (desde el norte)")
    print("Orientaciones SINTÉTICAS → declinación (lat −10°):")
    for az, h in ((66.2, 0.0), (66.2, 1.0), (90.0, 0.0), (113.8, 0.0)):
        print(f"  azimut {az:6.1f}°, altura horizonte {h:3.1f}° → declinación {declinacion(lat, az, h):+.2f}°")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
