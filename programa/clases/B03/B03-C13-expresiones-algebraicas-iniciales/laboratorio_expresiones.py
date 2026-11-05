#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C13: expresiones algebraicas con distancias Tierra-Marte.

Datos PUBLICADOS: semieje mayor de la Tierra 149,598e6 km y de Marte 227,956e6 km (NASA Planetary
Fact Sheets); c = 299 792,458 km/s (SI). Modelo SIMPLIFICADO: órbitas circulares y coplanares de
radios iguales a los semiejes; distancia mínima d = a2 - a1 y máxima d = a1 + a2. Supuestos: las
órbitas reales son elípticas e inclinadas, así que la distancia mínima real es distinta. Validez:
ilustrar la construcción y evaluación de expresiones, no predecir acercamientos. Tolerancia: 1e-9
en las identidades; 1e-9 relativo en la prueba numérica.
"""
from __future__ import annotations

import platform
import random

A_TIERRA = 149.598e6      # km
A_MARTE = 227.956e6       # km
C_KMS = 299_792.458       # km/s


def d_min(a1: float, a2: float) -> float:
    return a2 - a1


def d_max(a1: float, a2: float) -> float:
    return a1 + a2


def t_luz(d: float) -> float:
    return d / C_KMS


def pruebas() -> None:
    rnd = random.Random(2026)
    for _ in range(1000):
        a, b = rnd.uniform(-50, 50), rnd.uniform(-50, 50)
        assert abs((a + b) ** 2 - (a * a + 2 * a * b + b * b)) < 1e-9          # cuadrado de una suma
        assert abs((a * a - b * b) - (a - b) * (a + b)) < 1e-9                  # diferencia de cuadrados
        assert abs(3 * (a + b) - (3 * a + 3 * b)) < 1e-9                        # propiedad distributiva
    # d_max * d_min = a2^2 - a1^2 (factorización)
    assert abs(d_max(A_TIERRA, A_MARTE) * d_min(A_TIERRA, A_MARTE) - (A_MARTE ** 2 - A_TIERRA ** 2)) < 1e-3 * 1e12
    assert d_max(A_TIERRA, A_MARTE) - d_min(A_TIERRA, A_MARTE) == 2 * A_TIERRA


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    lo, hi = d_min(A_TIERRA, A_MARTE), d_max(A_TIERRA, A_MARTE)
    print(f"Distancia mínima (modelo circular): {lo / 1e6:.3f} x 10^6 km; luz: {t_luz(lo):.1f} s = {t_luz(lo) / 60:.2f} min")
    print(f"Distancia máxima (modelo circular): {hi / 1e6:.3f} x 10^6 km; luz: {t_luz(hi):.1f} s = {t_luz(hi) / 60:.2f} min")
    print(f"Producto d_max*d_min = {lo * hi:.4e} km^2 = a2^2 - a1^2 = {A_MARTE ** 2 - A_TIERRA ** 2:.4e} km^2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
