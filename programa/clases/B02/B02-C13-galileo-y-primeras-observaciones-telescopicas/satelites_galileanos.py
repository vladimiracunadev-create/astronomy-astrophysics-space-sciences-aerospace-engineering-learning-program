#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B02-C13: los cuatro satélites de Júpiter que vio Galileo en enero de 1610.

Datos PUBLICADOS (NASA NSSDC Jovian Satellite Fact Sheet, act. 6-dic-2023, consultada el
2026-11-05): semiejes mayores [10^3 km] y períodos orbitales [d] de Ío, Europa, Ganimedes y
Calisto. Fechas de la observación (Galileo Project, Universidad Rice): del 7 al 15 de enero de 1610.
Modelo: órbitas circulares con período constante. Supuestos: valores medios.
Validez: ilustra cuántas vueltas ocurren en una semana; no reconstruye las posiciones
observadas por Galileo. Tolerancia: T²/a³ constante dentro de 0,5 % (Kepler, C14).
"""

from __future__ import annotations

import sys

# nombre: (semieje mayor [10^3 km], período [d])
SATELITES = {
    "Ío": (421.8, 1.769138),
    "Europa": (671.1, 3.551181),
    "Ganimedes": (1070.4, 7.154553),
    "Calisto": (1882.7, 16.689017),
}
DIAS_OBSERVACION = 8.0   # del 7 al 15 de enero de 1610 (Rice)


def pruebas() -> None:
    k = [t**2 / a**3 for a, t in SATELITES.values()]
    assert max(k) / min(k) - 1 < 0.005, k            # tercera ley: constante dentro de 0,5 %
    assert abs(SATELITES["Europa"][1] / SATELITES["Ío"][1] - 2.0) < 0.05
    assert abs(SATELITES["Ganimedes"][1] / SATELITES["Europa"][1] - 2.0) < 0.05


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"{'Satélite':10s} {'a [10^3 km]':>12s} {'T [d]':>10s} {'T²/a³ [d²/(10^3 km)³]':>24s} {'vueltas en 8 d':>15s}")
    for nombre, (a, t) in SATELITES.items():
        print(f"{nombre:10s} {a:12.1f} {t:10.6f} {t**2 / a**3:24.4e} {DIAS_OBSERVACION / t:15.2f}")
    print(f"T(Europa)/T(Ío) = {SATELITES['Europa'][1] / SATELITES['Ío'][1]:.4f}; "
          f"T(Ganimedes)/T(Europa) = {SATELITES['Ganimedes'][1] / SATELITES['Europa'][1]:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
