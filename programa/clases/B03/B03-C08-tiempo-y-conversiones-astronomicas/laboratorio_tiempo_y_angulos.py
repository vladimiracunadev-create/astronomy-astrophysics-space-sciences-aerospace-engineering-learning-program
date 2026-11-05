#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C08: conversiones de tiempo y de ángulo.

Datos: definiciones del SI (1 min = 60 s; 1 h = 3600 s; 1 d = 86 400 s; 1° = π/180 rad;
1″ = π/648 000 rad; BIPM SI 9.ª ed., tabla 8) y valores PUBLICADOS de la NASA (períodos sidéreos
de Mercurio 87,969 d y Neptuno 60 189,018 d; rotación sidérea terrestre 23,9345 h). El año de
365,25 d es una CONVENCIÓN del programa (año juliano), no una medición. Modelo: factores
exactos. Validez: conversiones, no escalas de tiempo (UTC, TT) ni efemérides. Tolerancia: 1e-12.
"""
from __future__ import annotations

import math
import platform

S_DIA = 86_400
ANIO_JULIANO_D = 365.25


def hms_a_segundos(h: int, m: int, s: float) -> float:
    return h * 3600 + m * 60 + s


def segundos_a_hms(t: float) -> tuple[int, int, float]:
    h, resto = divmod(t, 3600)
    m, s = divmod(resto, 60)
    return int(h), int(m), s


def grados_a_arcseg(deg: float) -> float:
    return deg * 3600


def horas_a_grados(h: float) -> float:
    """Una vuelta (360°) en 24 h: 15° por hora de ascensión recta."""
    return h * 360 / 24


def pruebas() -> None:
    assert segundos_a_hms(hms_a_segundos(11, 51, 41.0)) == (11, 51, 41.0)
    assert hms_a_segundos(0, 8, 19) == 499
    assert horas_a_grados(1) == 15.0 and horas_a_grados(24) == 360.0
    assert abs(grados_a_arcseg(1) - 3600) < 1e-12
    assert abs(math.radians(1 / 3600) - math.pi / 648_000) < 1e-15      # 1″ en rad
    assert abs(87.969 / ANIO_JULIANO_D * ANIO_JULIANO_D - 87.969) < 1e-12   # ida y vuelta


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    for nombre, d in (("Mercurio", 87.969), ("Neptuno", 60_189.018)):
        print(f"{nombre}: {d} d = {d * S_DIA:.4e} s = {d / ANIO_JULIANO_D:.4f} años julianos (convención)")
    print(f"1″ = {math.pi / 648_000:.4e} rad; 1° = {math.pi / 180:.6f} rad")
    w = 360 / 23.9345
    print(f"Rotación sidérea de la Tierra: {w:.4f} °/h = {w * 3600 / 3600 / 60:.4f} ′/s")
    print(f"Luz 1 au: {149_597_870_700 / 299_792_458:.3f} s = {segundos_a_hms(149_597_870_700 / 299_792_458)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
