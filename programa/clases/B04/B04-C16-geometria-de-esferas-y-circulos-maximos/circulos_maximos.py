#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C16: distancias sobre la esfera y círculos máximos.

Datos (PUBLICADOS): USGS, Snyder, Map Projections - A Working Manual (PP 1395, 1987),
ecuaciones (5-3), (5-3a) y (5-4b) para la distancia de círculo máximo y el acimut;
radios nominales de la Tierra de IAU 2015 B3: R_e = 6,3781e6 m, R_p = 6,3568e6 m. Radio
medio de la esfera de la clase: (2 R_e + R_p)/3 (cálculo propio). Estrellas: NASA Exoplanet
Archive (2026-11-05; ra y dec, marco y época no verificados). Puntos terrestres: SINTÉTICOS.
Modelo: esfera de radio R; longitud λ hacia el este y latitud φ al norte.
Supuestos: Tierra esférica (error de forma hasta ~0,3 % en distancias); sin relieve.
Validez: toda la esfera con (5-3a); (5-3) pierde cifras para c pequeño.
Tolerancia de las pruebas: 1e-9 rad (casos exactos) y 1e-12 (coincidencia entre fórmulas).
"""
from __future__ import annotations
import math, platform, sys

RE, RP = 6.3781e6, 6.3568e6
R = (2 * RE + RP) / 3

ESTRELLAS = {
    "Proxima Cen": (217.3934657, -62.6761821),
    "tau Cet": (26.0093029, -15.9337987),
    "eps Eri": (53.2284306, -9.4581715),
}


def c_coseno(p1, l1, p2, l2):
    """Snyder (5-3): cos c = sen φ1 sen φ2 + cos φ1 cos φ2 cos Δλ  (ángulos en grados)."""
    p1, l1, p2, l2 = map(math.radians, (p1, l1, p2, l2))
    x = math.sin(p1) * math.sin(p2) + math.cos(p1) * math.cos(p2) * math.cos(l2 - l1)
    return math.acos(max(-1.0, min(1.0, x)))


def c_haversine(p1, l1, p2, l2):
    """Snyder (5-3a): sen(c/2) = sqrt(sen²(Δφ/2) + cos φ1 cos φ2 sen²(Δλ/2))."""
    p1, l1, p2, l2 = map(math.radians, (p1, l1, p2, l2))
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin((l2 - l1) / 2) ** 2
    return 2 * math.asin(min(1.0, math.sqrt(h)))


def acimut(p1, l1, p2, l2):
    """Snyder (5-4b): tan Az = cos φ2 sen Δλ / (cos φ1 sen φ2 − sen φ1 cos φ2 cos Δλ); Az desde el norte hacia el este."""
    p1, l1, p2, l2 = map(math.radians, (p1, l1, p2, l2))
    y = math.cos(p2) * math.sin(l2 - l1)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(l2 - l1)
    return math.degrees(math.atan2(y, x)) % 360.0


def pruebas():
    assert abs(c_haversine(0, 0, 90, 0) - math.pi / 2) < 1e-9             # ecuador → polo
    assert abs(c_haversine(0, 0, 0, 180) - math.pi) < 1e-9                # antípodas
    assert c_haversine(10, 20, 10, 20) == 0.0
    assert abs(c_haversine(0, 0, 0, 90) - math.pi / 2) < 1e-12            # un cuarto del ecuador
    for (a, b, c, d) in ((10, 20, 30, 140), (-45, 10, 60, -170), (80, 0, -80, 179)):
        assert abs(c_coseno(a, b, c, d) - c_haversine(a, b, c, d)) < 1e-9
        assert abs(c_haversine(a, b, c, d) - c_haversine(c, d, a, b)) < 1e-15   # simetría
    # Desigualdad triangular
    A, B, C = (10, 20), (30, 140), (-20, -60)
    assert c_haversine(*A, *C) <= c_haversine(*A, *B) + c_haversine(*B, *C) + 1e-12
    # Acimutes notables
    assert abs(acimut(0, 0, 10, 0) - 0.0) < 1e-9 and abs(acimut(0, 0, 0, 10) - 90.0) < 1e-9
    assert abs(acimut(0, 0, -10, 0) - 180.0) < 1e-9
    # Pérdida de cifras de (5-3) para c pequeño (1e-8 rad ≈ 0,002″): (5-3a) sigue exacta
    g = 1e-8
    assert abs(c_haversine(0, 0, 0, math.degrees(g)) - g) / g < 1e-9
    assert abs(c_coseno(0, 0, 0, math.degrees(g)) - g) / g > 1e-4


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (polo, antípodas, cuarto de ecuador, (5-3)=(5-3a), simetría, triangular, acimutes, c pequeño)")
    print(f"\nRadio de la esfera de la clase R = (2 Re + Rp)/3 = {R / 1e3:.2f} km")
    print(f"Un grado de círculo máximo = {R * math.pi / 180 / 1e3:.3f} km; cuarto de meridiano = {R * math.pi / 2 / 1e3:.1f} km")
    # Puntos terrestres sintéticos
    puntos = (("A (0°N, 0°E)", 0.0, 0.0), ("B (45°N, 90°E)", 45.0, 90.0), ("C (60°N, 10°E)", 60.0, 10.0),
              ("D (60°N, 170°E)", 60.0, 170.0))
    print("\nPuntos terrestres sintéticos")
    pares = ((0, 1), (2, 3), (0, 3))
    for i, j in pares:
        (n1, p1, l1), (n2, p2, l2) = puntos[i], puntos[j]
        c = c_haversine(p1, l1, p2, l2)
        print(f"  {n1} → {n2}: c = {math.degrees(c):8.4f}° ; d = {c * R / 1e3:9.1f} km ; acimut inicial = {acimut(p1, l1, p2, l2):7.3f}°")
    # Comparación con «plano»: C y D a 60°N con Δλ = 160°
    c = c_haversine(60, 10, 60, 170)
    plano = math.cos(math.radians(60)) * math.radians(160) * R   # arco del paralelo
    print(f"  Paralelo 60°N entre C y D: arco del paralelo = {plano / 1e3:.1f} km frente al círculo máximo {c * R / 1e3:.1f} km ({(plano / (c * R) - 1) * 100:.1f} % más largo)")
    # Estrellas: separación angular
    print("\nSeparación angular de estrellas (ra, dec como λ, φ), grados")
    nom = list(ESTRELLAS)
    for i in range(len(nom)):
        for j in range(i + 1, len(nom)):
            (a1, d1), (a2, d2) = ESTRELLAS[nom[i]], ESTRELLAS[nom[j]]
            print(f"  {nom[i]} – {nom[j]}: {math.degrees(c_haversine(d1, a1, d2, a2)):.4f}° (5-3a), {math.degrees(c_coseno(d1, a1, d2, a2)):.4f}° (5-3)")
    # Efecto de la forma: R_e frente a R_p
    print(f"\nCuarto de meridiano con R_e = {RE * math.pi / 2 / 1e3:.1f} km y con R_p = {RP * math.pi / 2 / 1e3:.1f} km: "
          f"diferencia {(RE / RP - 1) * 100:.2f} %")
    # c pequeño
    g = 1e-8
    print(f"\nc = {math.degrees(g) * 3600:.4f}″: (5-3a) = {c_haversine(0, 0, 0, math.degrees(g)):.6e} rad; (5-3) = {c_coseno(0, 0, 0, math.degrees(g)):.6e} rad; exacto {g:.6e}")


if __name__ == "__main__":
    main()
