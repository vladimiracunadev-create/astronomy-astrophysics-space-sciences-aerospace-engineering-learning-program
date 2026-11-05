#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C05: notación científica y órdenes de magnitud.

Datos PUBLICADOS (NASA NSSDC Fact Sheets: masas en 1e24 kg; semieje de Neptuno 4514,953e6 km;
distancia Tierra-Luna 0,3844e6 km; au = 149 597 870 700 m, SI tabla 8). Modelo: x = m x 10^e con
1 <= |m| < 10; el orden de magnitud de x es e (aquí: floor(log10|x|)). Supuestos: valores
tal como se publican. Validez: x distinto de cero. Tolerancia: 1e-12 relativa en las pruebas.
"""
from __future__ import annotations

import math
import platform

MASAS_KG = {"Luna": 0.07346e24, "Marte": 0.64169e24, "Tierra": 5.9722e24,
            "Neptuno": 102.409e24, "Júpiter": 1898.13e24, "Sol": 1988400e24}
DIST_M = {"Tierra-Luna": 0.3844e9, "1 au": 149_597_870_700.0, "Neptuno-Sol": 4514.953e9}


def a_cientifica(x: float) -> tuple[float, int]:
    """Devuelve (mantisa, exponente) con 1 <= |mantisa| < 10."""
    if x == 0:
        raise ValueError("el cero no tiene notación científica normalizada")
    e = math.floor(math.log10(abs(x)))
    m = x / 10 ** e
    if abs(m) >= 10:        # corrección por redondeo en el borde
        m, e = m / 10, e + 1
    return m, e


def pruebas() -> None:
    for x in (1.0, 9.99, 10.0, 0.001, 384_400e3, -2.5e-7, 1.9884e30):
        m, e = a_cientifica(x)
        assert 1 <= abs(m) < 10, (x, m)
        assert abs(m * 10 ** e - x) <= 1e-12 * abs(x), x
    assert a_cientifica(86_400.0) == (8.64, 4)
    assert abs((2e5) * (3e-3) - 6e2) < 1e-9              # (2x10^5)(3x10^-3) = 6x10^2
    assert abs(math.log10(1e6) - 6) < 1e-12
    assert a_cientifica(0.5)[1] == -1


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    for nombre, kg in MASAS_KG.items():
        m, e = a_cientifica(kg)
        print(f"Masa {nombre:8s}: {m:.4f} x 10^{e} kg")
    for nombre, d in DIST_M.items():
        m, e = a_cientifica(d)
        print(f"Dist {nombre:11s}: {m:.4f} x 10^{e} m")
    r = MASAS_KG["Sol"] / MASAS_KG["Tierra"]
    print(f"Sol/Tierra en masa: {r:.4g} -> {math.log10(r):.2f} órdenes de magnitud")
    r2 = MASAS_KG["Tierra"] / MASAS_KG["Luna"]
    print(f"Tierra/Luna en masa: {r2:.4g} -> {math.log10(r2):.2f} órdenes de magnitud")
    r3 = DIST_M["Neptuno-Sol"] / DIST_M["Tierra-Luna"]
    print(f"Neptuno-Sol / Tierra-Luna: {r3:.4g} -> {math.log10(r3):.2f} órdenes de magnitud")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
