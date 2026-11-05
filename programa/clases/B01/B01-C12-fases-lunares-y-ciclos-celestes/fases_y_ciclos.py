#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C12: predecir fases lunares y comparar ciclos de calendario.

Datos PUBLICADOS (NASA Moon Fact Sheet y Earth Fact Sheet): período sinódico 29,53 d,
inclinación orbital 5,145°, semieje 384 400 km, año trópico 365,242 d. La fecha de la
luna llena de partida (2026-09-26 00:00) es HIPOTÉTICA: dato de ejemplo, no efeméride.
Modelo: el ciclo de fases es periódico con período P; fracción iluminada
f = (1 − cos(2π·edad/P))/2 (disco iluminado visto desde la Tierra, geometría de esfera).
Supuestos: P constante; órbita circular a efectos de fase. Dominio de validez: unos pocos
ciclos; el error acumulado por redondear P es ≈ n·0,005 d. Tolerancias: casos analíticos
f(0)=0, f(P/2)=1, f(P/4)=0,5 a 1e-12.
"""

from __future__ import annotations

import datetime as dt
import math
import platform
import sys

P_SINODICO = 29.53         # d (NASA)
INCLINACION = 5.145        # grados (NASA)
SEMIEJE_KM = 384_400       # km (NASA)
ANIO_TROPICO = 365.242     # d (NASA)
LLENA_0 = dt.datetime(2026, 9, 26, 0, 0)   # hipotética


def fraccion_iluminada(edad: float, p: float = P_SINODICO) -> float:
    return (1 - math.cos(2 * math.pi * edad / p)) / 2


def pruebas() -> None:
    assert abs(fraccion_iluminada(0.0)) < 1e-12                       # luna nueva
    assert abs(fraccion_iluminada(P_SINODICO / 2) - 1.0) < 1e-12      # luna llena
    assert abs(fraccion_iluminada(P_SINODICO / 4) - 0.5) < 1e-12      # cuarto
    assert abs(235 * P_SINODICO - 19 * ANIO_TROPICO - (-0.05)) < 0.02  # coincidencia 235 meses ≈ 19 años (calc. a mano: 6939,55 − 6939,598)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    print("Lunas llenas predichas (partida hipotética 2026-09-26):")
    for n in range(0, 5):
        f = LLENA_0 + dt.timedelta(days=n * P_SINODICO)
        print(f"  n={n}: {f:%Y-%m-%d %H:%M}  (error acumulado por redondeo ≤ {n * 0.005:.3f} d)")
    for edad in (0, 3.7, 7.4, 11.1, 14.8, 22.1):
        print(f"edad {edad:5.1f} d -> fracción iluminada {fraccion_iluminada(edad):.2f}")
    doce = 12 * P_SINODICO
    print(f"12 meses sinódicos = {doce:.2f} d ; año trópico = {ANIO_TROPICO} d ; falta {ANIO_TROPICO - doce:.2f} d")
    print(f"235 meses sinódicos = {235 * P_SINODICO:.2f} d ; 19 años trópicos = {19 * ANIO_TROPICO:.2f} d ; dif = {235 * P_SINODICO - 19 * ANIO_TROPICO:+.2f} d")
    desvio = SEMIEJE_KM * math.sin(math.radians(INCLINACION))
    print(f"Desvío vertical máximo de la Luna respecto del plano de la órbita terrestre ≈ {desvio:,.0f} km")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
