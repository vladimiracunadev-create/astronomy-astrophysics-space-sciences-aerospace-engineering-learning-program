#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C09: circunferencias y elipses aplicadas a órbitas.

Datos (PUBLICADOS; estimados): cometa 1P/Halley, NASA/JPL SBDB (solución del
2025-11-21; consulta 2026-11-05): a = 17,92863504856923 au, e = 0,9679359956953211;
excentricidades de la Tierra (0,017) y Marte (0,094) y semiejes (149,6 y 228,0
millones de km) de la NASA NSSDC Planetary Fact Sheet (2025-03-18).
Modelo: elipse x²/a² + y²/b² = 1 con b = a·sqrt(1-e²), focos en (±ae, 0).
Supuestos: órbita kepleriana plana (sin perturbaciones). Validez: 0 ≤ e < 1.
Tolerancia de las pruebas: 1e-12 (identidades), 1e-9 (perímetro numérico contra
la fórmula exacta del círculo), 1e-4 relativa (Ramanujan frente a Simpson).
"""
from __future__ import annotations
import math, platform, sys


def semieje_menor(a, e):
    return a * math.sqrt(1 - e * e)


def perimetro_simpson(a, b, n=20000):
    """Longitud de la elipse por Simpson de ∫ sqrt(a² sen² t + b² cos² t) dt, t en [0, 2π]."""
    f = lambda t: math.sqrt((a * math.sin(t)) ** 2 + (b * math.cos(t)) ** 2)
    h = 2 * math.pi / n
    s = f(0) + f(2 * math.pi)
    for k in range(1, n):
        s += (4 if k % 2 else 2) * f(k * h)
    return s * h / 3


def perimetro_ramanujan(a, b):
    h = ((a - b) / (a + b)) ** 2
    return math.pi * (a + b) * (1 + 3 * h / (10 + math.sqrt(4 - 3 * h)))


def pruebas():
    # Circunferencia: e = 0 → b = a, perímetro 2πa
    assert semieje_menor(3.0, 0.0) == 3.0
    assert abs(perimetro_simpson(3.0, 3.0) - 2 * math.pi * 3.0) < 1e-9 * 6 * math.pi
    # Propiedad de los focos: d1 + d2 = 2a para puntos de la elipse
    a, e = 5.0, 0.6
    b, c = semieje_menor(a, e), a * e
    assert abs(b - 4.0) < 1e-12 and abs(c - 3.0) < 1e-12              # 3-4-5
    for k in range(0, 360, 7):
        t = math.radians(k)
        x, y = a * math.cos(t), b * math.sin(t)
        assert abs(x * x / a ** 2 + y * y / b ** 2 - 1) < 1e-12
        d1, d2 = math.hypot(x - c, y), math.hypot(x + c, y)
        assert abs(d1 + d2 - 2 * a) < 1e-12
    # Perímetro de la elipse 5×3: valor conocido 25,52699886...
    assert abs(perimetro_simpson(5.0, 3.0) - 25.52699886) < 1e-6
    assert abs(perimetro_ramanujan(5.0, 3.0) / perimetro_simpson(5.0, 3.0) - 1) < 1e-4
    # Distancias extremas
    assert abs(a * (1 - e) + a * (1 + e) - 2 * a) < 1e-12


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (círculo, 3-4-5, d1+d2=2a en 52 puntos, perímetro 5×3, extremos)")
    casos = (("Halley (JPL)", 17.92863504856923, 0.9679359956953211, "au"),
             ("Tierra (NASA)", 149.6, 0.017, "10^6 km"),
             ("Marte (NASA)", 228.0, 0.094, "10^6 km"))
    print(f"\n{'Cuerpo':<15}{'a':>9}{'e':>8}{'b':>10}{'c=ae':>10}{'q':>10}{'Q':>10}{'b/a':>9}  unidad")
    for n, a, e, u in casos:
        b = semieje_menor(a, e)
        print(f"{n:<15}{a:9.3f}{e:8.4f}{b:10.3f}{a * e:10.3f}{a * (1 - e):10.3f}{a * (1 + e):10.3f}{b / a:9.5f}  {u}")
    a, e = casos[0][1], casos[0][2]
    b = semieje_menor(a, e)
    print(f"\nHalley: área = π a b = {math.pi * a * b:.2f} au²; perímetro (Simpson) = {perimetro_simpson(a, b):.3f} au; "
          f"Ramanujan = {perimetro_ramanujan(a, b):.3f} au; 2πa = {2 * math.pi * a:.3f} au")
    print(f"Halley: 2a = {2 * a:.3f} au = q + Q = {a * (1 - e) + a * (1 + e):.3f} au")
    print(f"Tierra: la diferencia entre q y Q es {(1.017 - 0.983) * 149.6:.1f} ×10^6 km ({(1.017 - 0.983) * 100:.1f} % de a)")


if __name__ == "__main__":
    main()
