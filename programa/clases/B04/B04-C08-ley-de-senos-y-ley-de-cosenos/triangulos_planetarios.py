#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C08: ley de cosenos y ley de senos con órbitas planetarias.

Datos (PUBLICADOS; estimados): NASA NSSDC Planetary Fact Sheet - Metric
(actualizada 2025-03-18; consulta 2026-11-05), «Distance from Sun» (10^6 km) y
excentricidad: Venus 108,2 (e 0,007), Tierra 149,6 (e 0,017), Marte 228,0 (e 0,094).
Modelo: órbitas circulares coplanares de radio a (primera aproximación) para
la geometría de triángulo Sol-Tierra-planeta; ley de cosenos
d^2 = a1^2 + a2^2 - 2 a1 a2 cos(phi) y ley de senos a/sen A = b/sen B = c/sen C.
Supuestos: coplanares y circulares; ángulos heliocéntricos conocidos (SINTÉTICOS
en la tabla de ejemplos). Validez: orden de magnitud; la excentricidad solo se usa
para acotar el intervalo posible de distancias.
Tolerancia de las pruebas: 1e-12 relativa (identidades) y 1e-9 (triángulos exactos).
"""
from __future__ import annotations
import math, platform, sys

A_VENUS, A_TIERRA, A_MARTE = 108.2, 149.6, 228.0     # 10^6 km
E_TIERRA, E_MARTE = 0.017, 0.094


def lado_por_cosenos(b, c, angulo_rad):
    """Lado opuesto al ángulo entre b y c (ley de cosenos)."""
    return math.sqrt(b * b + c * c - 2 * b * c * math.cos(angulo_rad))


def angulo_por_cosenos(a, b, c):
    """Ángulo opuesto a `a` conocidos los tres lados."""
    x = (b * b + c * c - a * a) / (2 * b * c)
    return math.acos(max(-1.0, min(1.0, x)))


def angulo_por_senos(a, A, b):
    """Ángulo B opuesto a b, dados a, A (caso ambiguo: devuelve las dos soluciones)."""
    s = b * math.sin(A) / a
    if s > 1:
        return ()
    B1 = math.asin(s)
    B2 = math.pi - B1
    return tuple(B for B in (B1, B2) if B + A < math.pi + 1e-12)


def pruebas():
    assert abs(lado_por_cosenos(3, 4, math.pi / 2) - 5) < 1e-12              # Pitágoras
    assert abs(angulo_por_cosenos(1, 1, 1) - math.pi / 3) < 1e-12            # equilátero
    # Triángulo cualquiera: suma de ángulos = π y consistencia seno/lado
    a, b, c = 7.0, 9.0, 12.0
    A, B, C = (angulo_por_cosenos(a, b, c), angulo_por_cosenos(b, a, c), angulo_por_cosenos(c, a, b))
    assert abs(A + B + C - math.pi) < 1e-12
    assert abs(a / math.sin(A) - b / math.sin(B)) < 1e-9 and abs(b / math.sin(B) - c / math.sin(C)) < 1e-9
    # Caso ambiguo: a=8, b=10, A=30° tiene dos soluciones
    sol = angulo_por_senos(8.0, math.radians(30), 10.0)
    assert len(sol) == 2
    # Sin solución: sen B > 1
    assert angulo_por_senos(3.0, math.radians(30), 10.0) == ()
    # Ley de cosenos con φ = 0 y π
    assert abs(lado_por_cosenos(3, 5, 0) - 2) < 1e-12 and abs(lado_por_cosenos(3, 5, math.pi) - 8) < 1e-12


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (Pitágoras, equilátero, suma de ángulos, consistencia seno/lado, caso ambiguo, φ=0 y π)")
    # Elongación máxima de Venus: triángulo Sol–Tierra–Venus con ángulo recto en Venus
    eps = math.degrees(math.asin(A_VENUS / A_TIERRA))
    print(f"\nElongación máxima de Venus (órbitas circulares): sen ε = a_V/a_T = {A_VENUS/A_TIERRA:.4f} -> ε = {eps:.2f}°")
    print("\nDistancia Tierra–Marte según el ángulo heliocéntrico φ (órbitas circulares; φ sintético):")
    print(f"{'φ (°)':>7}{'d (10^6 km)':>14}{'elongación de Marte (°)':>26}")
    for phi in (0, 30, 60, 90, 120, 150, 180):
        d = lado_por_cosenos(A_TIERRA, A_MARTE, math.radians(phi))
        # ángulo en la Tierra entre Sol y Marte (opuesto a a_Marte): ley de cosenos
        elong = math.degrees(angulo_por_cosenos(A_MARTE, A_TIERRA, d)) if d > 0 else float("nan")
        print(f"{phi:7d}{d:14.1f}{elong:26.1f}")
    # Cota inferior con excentricidades: perihelio de Marte menos afelio de la Tierra
    q_marte = A_MARTE * (1 - E_MARTE)
    Q_tierra = A_TIERRA * (1 + E_TIERRA)
    print(f"\nCota inferior de la distancia mínima (calculada): q_Marte - Q_Tierra = {q_marte:.1f} - {Q_tierra:.1f} = {q_marte - Q_tierra:.1f} ×10^6 km")
    print(f"En oposición con órbitas circulares: {A_MARTE - A_TIERRA:.1f} ×10^6 km")
    # Caso ambiguo
    sol = angulo_por_senos(8.0, math.radians(30), 10.0)
    print("\nCaso ambiguo a=8, A=30°, b=10: B =", " o ".join(f"{math.degrees(x):.2f}°" for x in sol))
    # Retardo de luz en ese intervalo
    c_km_s = 299_792.458
    for etiqueta, d in (("oposición circular", A_MARTE - A_TIERRA), ("conjunción", A_MARTE + A_TIERRA)):
        print(f"Luz Tierra–Marte ({etiqueta}): {d * 1e6 / c_km_s / 60:.2f} min")


if __name__ == "__main__":
    main()
