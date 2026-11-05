#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C02: qué estrellas nunca se ponen y cuántas horas está arriba cada una.

Datos: SIMULADOS (calculados) para latitudes -30,0 (valle del Elqui, redondeada), 0 y -90.
Modelo: esfera celeste sin refracción ni paralaje; el arco diurno vale 2*H0 con
cos(H0) = -tan(lat) tan(dec). Dominio: estrellas (paralaje despreciable). Tolerancia: 0,05 h.
Prueba independiente: se cuenta el tiempo sobre el horizonte barriendo el ángulo horario
con la altura calculada por astrolib_b08.altaz (método distinto del cierre analítico).
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import D2R, altaz, pruebas_biblioteca  # noqa: E402


def clasificar(dec: float, lat: float) -> str:
    colat = 90.0 - abs(lat)
    sur = lat < 0
    d = -dec if sur else dec          # espejo al hemisferio norte
    if d >= colat - 1e-9:
        return "circumpolar (nunca se pone)"
    if d < -colat:
        return "nunca sale"
    return "sale y se pone"


def horas_sobre_horizonte(dec: float, lat: float) -> float:
    """Horas sidéreas sobre el horizonte geométrico (altura 0), por cierre analítico."""
    x = -math.tan(lat * D2R) * math.tan(dec * D2R)
    if x <= -1.0:
        return 24.0
    if x >= 1.0:
        return 0.0
    return 2.0 * math.degrees(math.acos(x)) / 15.0


def horas_barrido(dec: float, lat: float) -> float:
    """Mismo dato por barrido numérico del ángulo horario (cada 0,01 h)."""
    n = 0
    pasos = 2400
    for i in range(pasos):
        h = i * 360.0 / pasos
        alt, _ = altaz(0.0, dec, lat, h)   # RA=0, LST=h -> ángulo horario h
        if alt > 0.0:
            n += 1
    return 24.0 * n / pasos


def pruebas() -> None:
    pruebas_biblioteca()
    for dec in (-80, -60.5, -30, 0, 30, 59.5):
        a, b = horas_sobre_horizonte(dec, -30.0), horas_barrido(dec, -30.0)
        assert abs(a - b) < 0.05, (dec, a, b)
    assert abs(horas_sobre_horizonte(0.0, -30.0) - 12.0) < 1e-9      # el ecuador celeste: 12 h en cualquier latitud
    assert abs(horas_sobre_horizonte(25.0, 0.0) - 12.0) < 1e-9       # en el ecuador terrestre, toda estrella está 12 h
    assert clasificar(-65.0, -30.0).startswith("circumpolar")
    assert clasificar(65.0, -30.0) == "nunca sale"


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Latitud -30,0 (datos SIMULADOS). dec | clasificacion | horas sobre el horizonte")
    for dec in (-85, -65, -60, -45, -30, 0, 30, 45, 59, 65):
        print(f"{dec:+4d} | {clasificar(dec, -30.0):28s} | {horas_sobre_horizonte(dec, -30.0):5.2f} h")
    print(f"Altura del polo sur celeste en lat -30,0: {abs(-30.0):.1f} grados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
