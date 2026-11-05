#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C10: coordenadas polares y cartesianas con una órbita.

Datos (PUBLICADOS; estimados): cometa 1P/Halley, NASA/JPL SBDB (solución del
2025-11-21; consulta 2026-11-05): a = 17,92863504856923 au, e = 0,9679359956953211.
Modelo: r(θ) = a(1-e²)/(1+e cos θ), con el foco (Sol) en el origen y θ medido desde
el perihelio (anomalía verdadera), en el plano orbital.
Supuestos: órbita kepleriana plana. Los puntos de prueba de conversión son SINTÉTICOS.
Validez: 0 ≤ e < 1, ángulos en radianes. Tolerancia: 1e-12 relativa en ida y vuelta,
1e-9 en la comprobación de la elipse.
"""
from __future__ import annotations
import math, platform, sys

A_H, E_H = 17.92863504856923, 0.9679359956953211


def a_polares(x, y):
    return math.hypot(x, y), math.atan2(y, x)


def a_cartesianas(r, th):
    return r * math.cos(th), r * math.sin(th)


def r_orbita(th, a=A_H, e=E_H):
    return a * (1 - e * e) / (1 + e * math.cos(th))


def pruebas():
    for x, y in ((3, 4), (-3, 4), (-3, -4), (3, -4), (0, 2), (-2, 0), (1e-3, -1e3)):
        r, th = a_polares(x, y)
        x2, y2 = a_cartesianas(r, th)
        assert abs(x2 - x) < 1e-12 * max(1, abs(x)) and abs(y2 - y) < 1e-12 * max(1, abs(y))
    # El cuadrante: atan(y/x) falla en x<0, atan2 no
    assert abs(math.atan2(4, -3) - (math.pi - math.atan(4 / 3))) < 1e-15
    assert math.atan(4 / -3) < 0 < math.atan2(4, -3)
    assert abs(r_orbita(0.0) - A_H * (1 - E_H)) < 1e-12                  # perihelio
    assert abs(r_orbita(math.pi) - A_H * (1 + E_H)) < 1e-9                # afelio
    b = A_H * math.sqrt(1 - E_H ** 2)
    for k in range(0, 360, 5):
        th = math.radians(k)
        x, y = a_cartesianas(r_orbita(th), th)
        # centro de la elipse en (-ae, 0)
        assert abs(((x + A_H * E_H) / A_H) ** 2 + (y / b) ** 2 - 1) < 1e-9
    # Órbita circular: r constante
    assert all(abs(r_orbita(t / 10, 1.0, 0.0) - 1.0) < 1e-15 for t in range(63))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (ida y vuelta, cuadrantes, atan2, perihelio, afelio, ecuación de la elipse, círculo)")
    print("\nConversión (puntos sintéticos):")
    for x, y in ((3, 4), (-3, 4), (-3, -4), (3, -4)):
        r, th = a_polares(x, y)
        print(f"  (x, y) = ({x:+d}, {y:+d})  ->  r = {r:.4f}, θ = {math.degrees(th):8.3f}°, atan(y/x) = {math.degrees(math.atan(y / x)):8.3f}°")
    print("\nÓrbita de Halley en polares (θ desde el perihelio):")
    print(f"{'θ (°)':>7}{'r (au)':>10}{'x (au)':>10}{'y (au)':>10}")
    for deg in (0, 30, 60, 90, 120, 150, 180):
        th = math.radians(deg)
        r = r_orbita(th)
        x, y = a_cartesianas(r, th)
        print(f"{deg:7d}{r:10.4f}{x:10.4f}{y:10.4f}")
    print(f"\nq = {r_orbita(0):.6f} au (JPL: 0.574864); Q = {r_orbita(math.pi):.5f} au (JPL: 35.28241)")
    th90 = math.radians(90)
    print(f"En θ = 90° se cumple r = semilado recto p = a(1-e²) = {A_H*(1-E_H**2):.4f} au (calculado: {r_orbita(th90):.4f})")


if __name__ == "__main__":
    main()
