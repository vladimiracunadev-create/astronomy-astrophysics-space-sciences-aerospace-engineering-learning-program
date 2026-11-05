#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C06: identidades trigonométricas y aproximación de ángulo pequeño.

Datos (PUBLICADOS): radio medio lunar 1737,4 km y semieje mayor 384 400 km
(NASA NSSDC Moon Fact Sheet, 2024-01-11); radio solar nominal 6,957e8 m (IAU 2015
B3) y 1 au = 149 597 870 700 m (SI/IAU). Los ángulos de prueba son SINTÉTICOS.
Modelo: identidades exactas del círculo unidad y desarrollo sin x ≈ x - x^3/6.
Supuestos: ángulos en radianes; Luna y Sol como esferas vistas a su distancia
media. Validez de sin x ≈ tan x ≈ x: |x| < 0,1 rad para error relativo < 0,5 %.
Tolerancia de las pruebas: 1e-12 (identidades en coma flotante).
"""
from __future__ import annotations
import math, platform, sys

RAD_A_ARCSEC = 648_000.0 / math.pi          # 1 rad en segundos de arco (1° = 3600″, 180° = π rad)


def pruebas():
    n = 0
    for k in range(-400, 401):
        x = k * 0.0173                                   # ≈ -6,9 .. 6,9 rad
        y = 0.9 - k * 0.0051
        assert abs(math.sin(x) ** 2 + math.cos(x) ** 2 - 1) < 1e-12
        assert abs(math.sin(x + y) - (math.sin(x) * math.cos(y) + math.cos(x) * math.sin(y))) < 1e-12
        assert abs(math.cos(x + y) - (math.cos(x) * math.cos(y) - math.sin(x) * math.sin(y))) < 1e-12
        assert abs(math.sin(2 * x) - 2 * math.sin(x) * math.cos(x)) < 1e-12
        assert abs(math.cos(2 * x) - (math.cos(x) ** 2 - math.sin(x) ** 2)) < 1e-12
        if abs(math.cos(x)) > 1e-3:
            assert abs(1 + math.tan(x) ** 2 - 1 / math.cos(x) ** 2) < 1e-6 * (1 + math.tan(x) ** 2)
        n += 1
    assert abs(math.sin(math.pi / 6) - 0.5) < 1e-15 and abs(math.cos(math.pi / 3) - 0.5) < 1e-15
    assert abs(math.sin(math.pi / 4) - math.cos(math.pi / 4)) < 1e-15
    assert abs(RAD_A_ARCSEC - 206264.80624709636) < 1e-8
    assert abs(math.radians(1 / 3600) * RAD_A_ARCSEC - 1.0) < 1e-12
    return n


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    n = pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print(f"Pruebas: OK ({n} ángulos; identidades de Pitágoras, suma, doble ángulo, tan, valores notables, 1 rad en ″)")
    print(f"\n1 rad = {RAD_A_ARCSEC:.5f}″ = {math.degrees(1):.5f}°")
    print("\nAproximación de ángulo pequeño (x en rad): error relativo de x frente a sin x y tan x")
    print(f"{'x (rad)':>10}{'x (°)':>10}{'x/sin x - 1':>14}{'x/tan x - 1':>14}")
    for x in (0.0045, 0.01, 0.1, 0.2, 0.5, 1.0):
        print(f"{x:10.4f}{math.degrees(x):10.3f}{x / math.sin(x) - 1:14.3e}{x / math.tan(x) - 1:14.3e}")
    R_luna, a_luna = 1737.4e3, 384_400e3
    R_sol, au = 6.957e8, 149_597_870_700.0
    for nombre, R, d in (("Luna", R_luna, a_luna), ("Sol", R_sol, au)):
        exacto = 2 * math.atan(R / d)
        aprox = 2 * R / d
        print(f"\n{nombre}: diámetro angular exacto = {exacto:.7f} rad = {math.degrees(exacto):.4f}° = "
              f"{math.degrees(exacto) * 60:.3f}′;  aprox 2R/d = {aprox:.7f} rad;  error relativo = {aprox / exacto - 1:.2e}")
    print(f"\nCociente Sol/Luna (diámetros angulares medios, calculado): "
          f"{(2 * R_sol / au) / (2 * R_luna / a_luna):.4f}")


if __name__ == "__main__":
    main()
