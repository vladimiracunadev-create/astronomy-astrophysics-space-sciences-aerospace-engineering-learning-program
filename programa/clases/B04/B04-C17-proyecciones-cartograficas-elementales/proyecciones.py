#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C17: proyecciones Mercator y ortográfica sobre la esfera.

Datos (PUBLICADOS): USGS, Snyder, Map Projections - A Working Manual (PP 1395, 1987):
Mercator esférica: x = R(λ-λ0), y = R ln tan(π/4 + φ/2), h = k = sec φ, escala de área
k² = sec² φ, inversa φ = arctan(sinh(y/R)) (cap. 7, ec. 7-3 a 7-5); tabla 7 (esfera, R = 1):
y(45°) = 0,88137, y(60°) = 1,31696, y(75°) = 2,02759, y(85°) = 3,13130. Ortográfica oblicua:
x = R cos φ sen(λ-λ0), y = R[cos φ1 sen φ - sen φ1 cos φ cos(λ-λ0)], h' = cos c, k' = 1
(cap. 20, ec. 20-3 a 20-5). Radio de la esfera: 6371,0 km (cálculo propio, C16). Puntos de
los ejemplos: SINTÉTICOS.
Modelo: esfera de radio R. Supuestos: sin elipsoide. Validez: Mercator, |φ| < 90°;
ortográfica, puntos con cos c >= 0 (hemisferio visible).
Tolerancia de las pruebas: 1e-5 frente a la tabla impresa (5 decimales) y 1e-12 en identidades.
"""
from __future__ import annotations
import math, platform, sys

R = 6371.0


def merc(phi_deg, lam_deg, lam0_deg=0.0, radio=1.0):
    phi, d = math.radians(phi_deg), math.radians(lam_deg - lam0_deg)
    return radio * d, radio * math.log(math.tan(math.pi / 4 + phi / 2))


def merc_inv(x, y, radio=1.0, lam0_deg=0.0):
    return math.degrees(math.atan(math.sinh(y / radio))), math.degrees(x / radio) + lam0_deg


def k_merc(phi_deg):
    return 1.0 / math.cos(math.radians(phi_deg))


def orto(phi_deg, lam_deg, phi1_deg, lam0_deg, radio=1.0):
    p, p1, d = math.radians(phi_deg), math.radians(phi1_deg), math.radians(lam_deg - lam0_deg)
    x = radio * math.cos(p) * math.sin(d)
    y = radio * (math.cos(p1) * math.sin(p) - math.sin(p1) * math.cos(p) * math.cos(d))
    cosc = math.sin(p1) * math.sin(p) + math.cos(p1) * math.cos(p) * math.cos(d)
    return x, y, cosc


def pruebas():
    # Tabla 7 de Snyder (esfera, R = 1)
    for phi, ref in ((45, 0.88137), (60, 1.31696), (75, 2.02759), (85, 3.13130)):
        assert abs(merc(phi, 0)[1] - ref) < 1e-5, (phi, merc(phi, 0)[1])
    assert all(abs(c) < 1e-15 for c in merc(0, 0))                     # el origen cae en (0, 0)
    for phi, lam in ((10, 20), (-45, 170), (70, -120), (0, 0)):         # ida y vuelta
        p2, l2 = merc_inv(*merc(phi, lam))
        assert abs(p2 - phi) < 1e-10 and abs(l2 - lam) < 1e-10
    assert abs(k_merc(60) - 2.0) < 1e-12 and abs(k_merc(10) - 1.0154266) < 1e-6   # 1,5 % a 10° (Snyder)
    # Mercator: la escala local k = dy/dφ en el plano coincide con sec φ (diferencia finita)
    h = 1e-6
    for phi in (10, 40, 70):
        dy = (merc(phi + h, 0)[1] - merc(phi - h, 0)[1]) / (math.radians(2 * h))
        assert abs(dy - k_merc(phi)) < 1e-6
    # Ortográfica: distancia al centro = R sen c; centro en el origen
    x, y, cosc = orto(30, 40, 30, 40)
    assert abs(x) < 1e-12 and abs(y) < 1e-12 and abs(cosc - 1) < 1e-12
    for (phi, lam) in ((0, 30), (30, 0), (45, 45)):
        x, y, cosc = orto(phi, lam, 0.0, 0.0)
        assert abs(math.hypot(x, y) - math.sqrt(1 - cosc ** 2)) < 1e-12
    x, y, cosc = orto(0, 90, 0, 0)
    assert abs(cosc) < 1e-12 and abs(math.hypot(x, y) - 1.0) < 1e-12   # el límite del mapa es una circunferencia de radio R


def gran_circulo_medio(p1, l1, p2, l2):
    def v(p, l):
        p, l = math.radians(p), math.radians(l)
        return (math.cos(p) * math.cos(l), math.cos(p) * math.sin(l), math.sin(p))
    a, b = v(p1, l1), v(p2, l2)
    m = tuple(x + y for x, y in zip(a, b))
    n = math.sqrt(sum(c * c for c in m))
    m = tuple(c / n for c in m)
    return math.degrees(math.asin(m[2])), math.degrees(math.atan2(m[1], m[0]))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (tabla 7 de Snyder, ida y vuelta, k = sec φ, ortográfica: r = R sen c y límite R)")
    print("\nMercator: factor de escala k = sec φ y de área k² (R = 6371,0 km; y en km)")
    print(f"{'φ (°)':>7}{'y (km)':>11}{'k':>9}{'k² (área)':>12}")
    for phi in (0, 15, 30, 45, 60, 75, 80, 85):
        x, y = merc(phi, 0, radio=R)
        print(f"{phi:7d}{(0.0 if abs(y) < 0.5 else y):11.0f}{k_merc(phi):9.4f}{k_merc(phi) ** 2:12.3f}")
    print("\nOrtográfica con centro en (0°, 0°): escala radial h' = cos c")
    print(f"{'c (°)':>7}{'x (km)':>10}{'y (km)':>10}{'h = cos c':>11}{'r = R sen c':>13}")
    for phi in (0, 30, 60, 80, 90):
        x, y, cosc = orto(phi, 0, 0, 0, radio=R)
        print(f"{phi:7d}{x:10.0f}{y:10.0f}{cosc:11.4f}{R * math.sqrt(1 - cosc ** 2):13.0f}")
    # Camino de círculo máximo C→D (sintético) en Mercator: el punto medio queda más al norte que la recta
    phi_m, lam_m = gran_circulo_medio(60, 10, 60, 170)
    x1, y1 = merc(60, 10, 0, 1.0)
    x2, y2 = merc(60, 170, 0, 1.0)
    xm, ym = merc(phi_m, lam_m, 0, 1.0)
    print(f"\nTrayecto C(60°N,10°E)→D(60°N,170°E): punto medio del círculo máximo = ({phi_m:.2f}°N, {lam_m:.1f}°E);")
    print(f"  en Mercator la recta C–D está en y = {y1:.4f} y el punto medio del círculo máximo en y = {ym:.4f}: no es una recta")
    print(f"Área aparente de una región a 60°N frente a una igual en el ecuador: ×{k_merc(60) ** 2:.1f}")


if __name__ == "__main__":
    main()
