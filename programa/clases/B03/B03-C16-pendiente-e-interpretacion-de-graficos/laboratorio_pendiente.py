#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C16: pendiente de una recta y ajuste de mínimos cuadrados.

Datos PUBLICADOS (NASA Planetary Fact Sheets: semiejes en 1e6 km y períodos en días); 1 au =
149 597 870,7 km; año de la Tierra 365,256 d. Datos SINTÉTICOS: una recta exacta y(x) = 3x + 2 y un
movimiento uniforme (50 km/s desde 100 km) para validar el código. Modelo: y = m x + b ajustada por
mínimos cuadrados, m = Sxy/Sxx. Aplicado a log10(T) frente a log10(a). Supuestos: errores solo en y,
puntos independientes. Validez: la pendiente de Kepler, no incertidumbres. Tolerancia: 1e-12 con
datos exactos; la pendiente de Kepler debe estar a menos de 0,01 de 1,5.
"""
from __future__ import annotations

import math
import platform

AU_KM = 149_597_870.7
ANIO_D = 365.256
DATOS = {"Mercurio": (57.909, 87.969), "Venus": (108.210, 224.701), "Tierra": (149.598, 365.256),
         "Marte": (227.956, 686.980), "Júpiter": (778.479, 4332.589), "Saturno": (1432.041, 10755.699),
         "Urano": (2867.043, 30685.400), "Neptuno": (4514.953, 60189.018)}


def pendiente_dos_puntos(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def ajuste(xs: list[float], ys: list[float]) -> tuple[float, float]:
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    m = sxy / sxx
    return m, my - m * mx


def pruebas() -> None:
    xs = [0.0, 1.0, 2.0, 5.0, 9.0]
    m, b = ajuste(xs, [3 * x + 2 for x in xs])
    assert abs(m - 3) < 1e-12 and abs(b - 2) < 1e-12
    tiempos = [0.0, 10.0, 20.0, 40.0]
    m2, b2 = ajuste(tiempos, [100 + 50 * t for t in tiempos])        # movimiento uniforme sintético
    assert abs(m2 - 50) < 1e-9 and abs(b2 - 100) < 1e-9
    assert pendiente_dos_puntos((1, 2), (3, 8)) == 3.0
    lx = [math.log10(a * 1e6 / AU_KM) for a, _ in DATOS.values()]
    ly = [math.log10(t / ANIO_D) for _, t in DATOS.values()]
    mk, bk = ajuste(lx, ly)
    assert abs(mk - 1.5) < 0.01, mk
    assert abs(bk) < 0.02, bk


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    lx = [math.log10(a * 1e6 / AU_KM) for a, _ in DATOS.values()]
    ly = [math.log10(t / ANIO_D) for _, t in DATOS.values()]
    m, b = ajuste(lx, ly)
    print(f"Ajuste log10(T) = m log10(a) + b: m = {m:.4f}, b = {b:.4f} (esperado 1,5 y 0)")
    p = pendiente_dos_puntos((lx[0], ly[0]), (lx[-1], ly[-1]))
    print(f"Pendiente entre Mercurio y Neptuno: {p:.4f}")
    a1, t1 = DATOS["Tierra"]
    a2, t2 = DATOS["Marte"]
    print(f"Pendiente lineal T-a entre Tierra y Marte: {(t2 - t1) / ANIO_D / ((a2 - a1) * 1e6 / AU_KM):.4f} años/au")
    a3, t3 = DATOS["Neptuno"]
    a4, t4 = DATOS["Urano"]
    print(f"Pendiente lineal T-a entre Urano y Neptuno: {(t3 - t4) / ANIO_D / ((a3 - a4) * 1e6 / AU_KM):.4f} años/au")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
