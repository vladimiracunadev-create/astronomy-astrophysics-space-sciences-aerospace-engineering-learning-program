#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C11: estimar primero, redondear al final.

Datos PUBLICADOS: 1 au = 149 597 870 700 m y c = 299 792 458 m/s (SI); radio medio de la Tierra
6371 km y semieje lunar 384 400 km (NASA). Modelo: estimación de Fermi con una cifra
(1,5e11 m / 3e8 m/s) frente al valor exacto; redondeo a n cifras significativas con Decimal
(mitad hacia arriba). Supuestos: valores como se publican. Validez: orden de magnitud y
cifras. Tolerancia: la estimación debe quedar a menos de un factor 1,5 (aquí, a menos del 1 %).
"""
from __future__ import annotations

import math
import platform
from decimal import ROUND_HALF_UP, Decimal

AU = 149_597_870_700
C = 299_792_458


def cifras(x: float, n: int) -> float:
    """Redondea x a n cifras significativas (mitad hacia arriba)."""
    if x == 0:
        return 0.0
    d = Decimal(repr(x))
    exp = d.adjusted()
    cuantum = Decimal(1).scaleb(exp - n + 1)
    return float(d.quantize(cuantum, rounding=ROUND_HALF_UP))


def pruebas() -> None:
    assert cifras(27.3217, 3) == 27.3 and cifras(0.0012345, 2) == 0.0012
    assert cifras(2.5, 1) == 3.0 and cifras(149_597_870_700, 4) == 149_600_000_000
    est = 1.5e11 / 3e8
    exacto = AU / C
    assert abs(est - exacto) / exacto < 0.01, (est, exacto)
    assert 0.5 < (384_400 / (2 * 6_371)) / 30 < 2          # Fermi: ~30 Tierras entre la Tierra y la Luna
    # redondear antes de operar acumula error más que redondear al final
    a, b = 1.44, 2.44
    assert abs(cifras(a, 2) + cifras(b, 2) - (a + b)) > abs(cifras(a + b, 2) - (a + b))


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    est, exacto = 1.5e11 / 3e8, AU / C
    print(f"Tiempo de luz Sol-Tierra: estimado {est:.0f} s; exacto {exacto:.3f} s; error {abs(est - exacto) / exacto * 100:.2f} %")
    n = 384_400 / (2 * 6_371)
    print(f"Diámetros terrestres entre Tierra y Luna: {n:.1f} (estimación mental: 30)")
    for k in (6, 4, 3, 2):
        print(f"1 au en m con {k} cifras: {cifras(AU, k):.6e}")
    a, b = 1.44, 2.44
    print(f"Redondeo previo: {cifras(a, 2) + cifras(b, 2):.1f}; redondeo al final: {cifras(a + b, 2):.1f}; exacto: {a + b:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
