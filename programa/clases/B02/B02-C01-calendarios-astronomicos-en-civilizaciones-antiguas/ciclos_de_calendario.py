#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B02-C01: cuánto se desajusta un calendario respecto del cielo.

Datos PUBLICADOS: año trópico 365,242 d y mes sinódico 29,53 d (NASA NSSDC Earth y
Moon Fact Sheets, consultadas el 2026-11-05). Los ciclos de 260 y 365 días del
calendario maya y la regla gregoriana (97 años bisiestos cada 400) son
CONVENCIONES aritméticas: se calculan, no se miden.
Modelo: razones entre ciclos medios constantes. Supuestos: valores medios.
Validez: órdenes de magnitud de la deriva; no sirve para fechar eventos reales.
Tolerancia: 0,3 d en la comparación metónica (limitada por las 4 cifras del mes sinódico).
"""

from __future__ import annotations

import math
import sys

ANIO_TROPICO = 365.242      # d, NASA NSSDC Earth Fact Sheet
MES_SINODICO = 29.53        # d, NASA NSSDC Moon Fact Sheet


def pruebas() -> None:
    assert math.lcm(260, 365) == 18_980                 # caso analítico: mcm exacto
    assert 18_980 // 365 == 52 and 18_980 // 260 == 73  # 52 vueltas de 365 y 73 de 260
    assert abs((97 * 366 + 303 * 365) / 400 - 365.2425) < 1e-12   # regla gregoriana
    assert abs(19 * ANIO_TROPICO - 235 * MES_SINODICO) < 0.3       # ciclo de Metón


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    for nombre, largo in (("Civil de 365 d", 365.0), ("Juliano", 365.25), ("Gregoriano", 365.2425)):
        deriva = ANIO_TROPICO - largo        # días de deriva por año calendario
        if abs(deriva) < 1e-9:
            print(f"{nombre}: sin deriva")
            continue
        anios = 1.0 / abs(deriva)
        print(f"{nombre}: {largo} d/año; deriva {deriva:+.4f} d/año; 1 día cada {anios:,.0f} años")
    print(f"Año civil de 365 d: vuelta completa de las estaciones (365 d vs 365,25 d): {365 / 0.25:,.0f} años")
    print(f"Calendario circular maya: mcm(260,365) = {math.lcm(260, 365):,} d = 52 años de 365 d")
    print(f"19 años trópicos = {19 * ANIO_TROPICO:.2f} d; 235 meses sinódicos = {235 * MES_SINODICO:.2f} d;"
          f" diferencia {19 * ANIO_TROPICO - 235 * MES_SINODICO:+.2f} d")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
