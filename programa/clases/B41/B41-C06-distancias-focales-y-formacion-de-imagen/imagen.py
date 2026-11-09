#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C06: ecuacion de imagen de lente delgada, aumento lateral, forma de Newton y combinacion de dos lentes.

Datos: sin constantes fisicas. Las focales (200 y 50 mm) y las distancias de objeto son ILUSTRATIVAS.
Modelo: 1/s + 1/s' = 1/f ; m = -s'/s ; forma de Newton x x' = f^2. Segunda via: se trazan dos rayos principales (el paralelo al eje que pasa por el foco y el
que pasa por el centro sin desviarse) y se intersectan; el resultado se compara con la ecuacion. Combinacion de dos lentes separadas d:
1/f = 1/f1 + 1/f2 - d/(f1 f2) frente al producto de matrices ABCD.
Supuestos: lente delgada, rayos paraxiales, aire. Validez: paraxial.
Tolerancia: ecuacion frente a rayos 1e-9 mm; combinacion frente a matrices 1e-12 relativo.
"""
from __future__ import annotations
import math, platform, sys


def imagen(s, f):
    return s * f / (s - f)


def por_rayos(s, f, ho):
    """Objeto de altura ho a distancia s (lente en x = 0). Rayo 1 paralelo al eje -> pasa por el foco; rayo 2 por el centro."""
    # rayo 1: sale de (-s, ho), llega a la lente a altura ho, baja con pendiente -ho/f
    # rayo 2: pendiente -ho/s por el origen
    # y1(x) = ho - ho x / f ; y2(x) = -ho x / s ; igualar
    x = ho / (ho / f - ho / s)
    return x, -ho * x / s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    f = 200.0
    print(f"lente delgada f = {f:.0f} mm, objeto de 10 mm")
    print(f"{'s [mm]':>8} {'s\' [mm]':>9} {'m':>8} {'altura imagen':>14} {'tipo':>10} {'x x\'':>10}")
    for s in (600.0, 400.0, 300.0, 250.0, 100.0):
        sp = imagen(s, f)
        m = -sp / s
        x, y = por_rayos(s, f, 10.0)
        tipo = "real" if sp > 0 else "virtual"
        xx = (s - f) * (sp - f)
        print(f"{s:8.0f} {sp:9.3f} {m:8.4f} {10*m:14.3f} {tipo:>10} {xx:10.1f}")
        assert abs(x - sp) < 1e-9 and abs(y - 10 * m) < 1e-9
        assert abs(xx - f * f) < 1e-6
    # telescopio: objeto en el infinito -> imagen en el foco; escala de imagen
    sp_inf = imagen(1e12, f)
    print(f"objeto a 1e12 mm: s' = {sp_inf:.6f} mm (el foco)")
    assert abs(sp_inf - f) < 1e-6
    # tamano de la imagen de la Luna (0,52 grados, ILUSTRATIVO) con f = 1000 mm
    ang = math.radians(0.52)
    print(f"imagen de un disco de 0,52 deg con f = 1000 mm: diametro = {1000*math.tan(ang):.3f} mm")
    # combinacion de dos lentes
    f1, f2 = 200.0, 50.0
    print("combinacion de dos lentes f1 = 200 mm, f2 = 50 mm")
    for d in (0.0, 50.0, 100.0, 150.0):
        f_c = 1 / (1 / f1 + 1 / f2 - d / (f1 * f2))
        # matrices
        l1 = [[1, 0], [-1 / f1, 1]]
        l2 = [[1, 0], [-1 / f2, 1]]
        t = [[1, d], [0, 1]]
        a = l2
        m = [[a[0][0] * t[0][0] + a[0][1] * t[1][0], a[0][0] * t[0][1] + a[0][1] * t[1][1]], [a[1][0] * t[0][0] + a[1][1] * t[1][0], a[1][0] * t[0][1] + a[1][1] * t[1][1]]]
        mm = [[m[0][0] * l1[0][0] + m[0][1] * l1[1][0], m[0][0] * l1[0][1] + m[0][1] * l1[1][1]], [m[1][0] * l1[0][0] + m[1][1] * l1[1][0], m[1][0] * l1[0][1] + m[1][1] * l1[1][1]]]
        f_m = -1 / mm[1][0]
        print(f"  d = {d:5.0f} mm : f = {f_c:9.3f} mm (formula) ; {f_m:9.3f} mm (matrices)")
        assert abs(f_c - f_m) / abs(f_m) < 1e-12
    # teleobjetivo: f1 = 200, f2 = -100, d = 150 -> focal efectiva 400 mm en solo 250 mm de longitud total
    f1, f2, d = 200.0, -100.0, 150.0
    f_c = 1 / (1 / f1 + 1 / f2 - d / (f1 * f2))
    bfd = f_c * (f1 - d) / f1
    print(f"teleobjetivo f1 = 200, f2 = -100, d = 150 : f = {f_c:.3f} mm ; foco a {bfd:.3f} mm tras la 2a lente ; longitud total = {d + bfd:.3f} mm")
    assert abs(f_c - 400.0) < 1e-9 and abs(bfd - 100.0) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
