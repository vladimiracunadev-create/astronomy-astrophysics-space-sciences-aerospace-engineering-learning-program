#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C01: operaciones fundamentales con datos de la Luna.

Datos PUBLICADOS (NASA NSSDC Moon Fact Sheet, act. 11-ene-2024): semieje mayor
384 400 km y velocidad orbital media 1,022 km/s. Modelo: órbita circular de radio
igual al semieje y rapidez constante. Supuestos: la órbita real es elíptica.
Dominio de validez: estimación de un período medio, no efeméride. Tolerancia:
0,5 % frente al período sidéreo publicado (27,3217 d, misma fuente).
Salida: período calculado y la inexactitud del decimal binario frente a Fraction.
"""
from __future__ import annotations

import math
import platform
from fractions import Fraction

A_KM = 384_400            # semieje mayor [km]
V_KMS = 1.022             # velocidad orbital media [km/s]
T_SIDEREO_D = 27.3217     # período sidéreo publicado [d]
S_POR_DIA = 86_400        # 1 d = 24 h = 86 400 s (SI, tabla 8)


def periodo_dias() -> float:
    longitud = 2 * math.pi * A_KM          # km, perímetro de la órbita
    segundos = longitud / V_KMS            # km / (km/s) = s
    return segundos / S_POR_DIA


def pruebas() -> None:
    assert 2 + 3 * 4 == 14 and (2 + 3) * 4 == 20               # jerarquía de operaciones
    assert Fraction(1, 3) + Fraction(1, 6) == Fraction(1, 2)   # suma exacta
    assert 0.1 + 0.2 != 0.3                                    # el decimal binario no es exacto
    assert Fraction("0.1") + Fraction("0.2") == Fraction("0.3")
    t = periodo_dias()
    assert abs(t - T_SIDEREO_D) / T_SIDEREO_D < 0.005, t       # coincide con lo publicado


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    print(f"Perímetro de la órbita: {2 * math.pi * A_KM:,.0f} km")
    t = periodo_dias()
    print(f"Período calculado: {t:.3f} d (publicado: {T_SIDEREO_D} d)")
    print(f"Diferencia relativa: {abs(t - T_SIDEREO_D) / T_SIDEREO_D * 100:.2f} %")
    print(f"0,1 + 0,2 en float = {0.1 + 0.2!r}; en Fraction = {Fraction('0.1') + Fraction('0.2')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
