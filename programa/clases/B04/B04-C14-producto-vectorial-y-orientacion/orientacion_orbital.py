#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C14: producto vectorial y orientación de órbitas.

Datos (PUBLICADOS; estimados): cometa 1P/Halley, NASA/JPL SBDB (solución del
2025-11-21; consulta 2026-11-05): inclinación i = 162,1905300439129°, longitud del
nodo ascendente Ω = 59,09894720612437°, excentricidad e = 0,9679359956953211,
semieje a = 17,92863504856923 au. El plano de referencia de la solución no se verificó
en la consulta (en SBDB suele ser la eclíptica J2000; aquí se trata como «plano de
referencia» sin más). Tierra: a = 149,6e6 km y P = 365,2 d (NASA NSSDC, 2025-03-18).
Modelo: la normal a la órbita es ĥ = (sen i sen Ω, −sen i cos Ω, cos i), que sale de
rotar el eje z del plano de referencia; ĥ ∝ r × v. Supuestos: órbita kepleriana, ángulos
en el sentido estándar de los elementos orbitales. Validez: 0 ≤ i ≤ 180°.
Tolerancia de las pruebas: 1e-12.
"""
from __future__ import annotations
import math, platform, sys

I_H, OM_H = 162.1905300439129, 59.09894720612437


def cruz(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norma(u):
    return math.sqrt(dot(u, u))


def normal_orbita(i_deg, om_deg):
    i, om = math.radians(i_deg), math.radians(om_deg)
    return (math.sin(i) * math.sin(om), -math.sin(i) * math.cos(om), math.cos(i))


def pruebas():
    x, y, z = (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)
    assert cruz(x, y) == z and cruz(y, z) == x and cruz(z, x) == y          # mano derecha
    assert cruz(y, x) == (0.0, 0.0, -1.0)                                    # anticonmutativa
    assert cruz(x, x) == (0.0, 0.0, 0.0)
    u, v = (2.0, -1.0, 0.5), (0.3, 0.8, -1.2)
    w = cruz(u, v)
    assert abs(dot(w, u)) < 1e-12 and abs(dot(w, v)) < 1e-12                  # perpendicular a ambos
    gam = math.acos(dot(u, v) / (norma(u) * norma(v)))
    assert abs(norma(w) - norma(u) * norma(v) * math.sin(gam)) < 1e-12        # |u×v| = |u||v| sen γ
    assert abs(norma(cruz(u, v)) ** 2 + dot(u, v) ** 2 - dot(u, u) * dot(v, v)) < 1e-12   # Lagrange
    assert abs(norma(normal_orbita(I_H, OM_H)) - 1) < 1e-12
    assert abs(math.degrees(math.acos(normal_orbita(I_H, OM_H)[2])) - I_H) < 1e-9   # ángulo con el eje z = i
    assert normal_orbita(0.0, 0.0) == (0.0, 0.0, 1.0)                         # órbita en el plano: normal = z


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (mano derecha, anticonmutativa, perpendicular, |u×v|, identidad de Lagrange, normal de Halley)")
    # Tierra: r × v constante en el modelo circular
    a_km, P = 149.6e6, 365.2 * 86400
    v0 = 2 * math.pi * a_km / P
    print(f"\nTierra (circular): v0 = {v0:.3f} km/s; |r×v| esperado = a·v0 = {a_km * v0:.4e} km²/s")
    for deg in (0, 45, 90, 200):
        t = math.radians(deg)
        r = (a_km * math.cos(t), a_km * math.sin(t), 0.0)
        v = (-v0 * math.sin(t), v0 * math.cos(t), 0.0)
        h = cruz(r, v)
        print(f"  θ = {deg:3d}°: r×v = ({h[0]:.1f}, {h[1]:.1f}, {h[2]:.4e}) km²/s  -> sentido +z (órbita directa)")
    hH = normal_orbita(I_H, OM_H)
    print(f"\nHalley: ĥ = ({hH[0]:.5f}, {hH[1]:.5f}, {hH[2]:.5f}); |ĥ| = {norma(hH):.12f}")
    print(f"  Ángulo entre ĥ de Halley y ĥ del plano de referencia = {math.degrees(math.acos(dot(hH, (0.0, 0.0, 1.0)))):.4f}° (= i)")
    print(f"  Componente z de ĥ = {hH[2]:.5f} < 0 -> órbita retrógrada (i > 90°)")
    # Área del paralelogramo / triángulo con vectores sintéticos
    u, v = (3.0, 0.0, 0.0), (1.0, 2.0, 0.0)
    print(f"\nÁrea (sintético): |u×v| = {norma(cruz(u, v)):.3f} (paralelogramo), triángulo = {norma(cruz(u, v)) / 2:.3f}")
    # Línea de nodos: ẑ × ĥ
    nodo = cruz((0.0, 0.0, 1.0), hH)
    n = norma(nodo)
    print(f"Línea de nodos ∝ ẑ × ĥ = ({nodo[0] / n:.5f}, {nodo[1] / n:.5f}, 0): ángulo desde x = {math.degrees(math.atan2(nodo[1], nodo[0])) % 360:.4f}° (Ω = {OM_H:.4f}°)")


if __name__ == "__main__":
    main()
