#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C05: suma de fuerzas por componentes y equilibrio.

Datos: SINTÉTICOS (masas, ángulos y empujes inventados para enseñanza); g_n = 9,806 65 m/s²
(NIST CODATA 2022). Modelo: partícula en 2D, marco inercial; x horizontal, y vertical
hacia arriba. Supuestos: fuerzas concurrentes en un punto, cuerpo rígido sin giro.
Dominio de validez: estática y dinámica de partícula con fuerzas constantes.
Tolerancia: 1e-9 relativa en equilibrio; 1e-12 en componentes.
"""
from __future__ import annotations
import math
import sys

GN = 9.80665

def comp(modulo: float, angulo_deg: float) -> tuple[float, float]:
    a = math.radians(angulo_deg)
    return modulo * math.cos(a), modulo * math.sin(a)

def suma(fuerzas):
    return sum(f[0] for f in fuerzas), sum(f[1] for f in fuerzas)

def cables_simetricos(m: float, theta_deg: float) -> float:
    """Tensión de cada cable (ángulo theta sobre la horizontal) que sostiene m en equilibrio."""
    return m * GN / (2 * math.sin(math.radians(theta_deg)))

def main() -> int:
    # Prueba 1: cuatro fuerzas iguales a 0°, 90°, 180° y 270° se anulan
    assert max(abs(c) for c in suma([comp(10, a) for a in (0, 90, 180, 270)])) < 1e-12
    # Prueba 2: cables simétricos con carga m: 2 T sin(theta) = m g
    m, th = 200.0, 30.0
    T = cables_simetricos(m, th)
    f = [comp(T, th), comp(T, 180 - th), (0.0, -m * GN)]
    sx, sy = suma(f)
    assert abs(sx) < 1e-9 * m * GN and abs(sy) < 1e-9 * m * GN, (sx, sy)
    # Prueba 3: con theta = 30° la tensión es igual al peso
    assert abs(T - m * GN) < 1e-9 * m * GN
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Cables a 30°: T = {T:.1f} N para m = {m:.0f} kg (peso {m*GN:.1f} N)")
    for th in (60, 30, 10, 5):
        t = cables_simetricos(m, th)
        print(f"  theta = {th:2d}°: T = {t:9.1f} N = {t/(m*GN):.2f} pesos")
    # Cohete sintético en plataforma: m = 5,0e5 kg, empuje 7,0e6 N vertical
    m, E = 5.0e5, 7.0e6
    a = (E - m * GN) / m
    print(f"Cohete sintético en plataforma: peso = {m*GN:.0f} N; a = {a:.3f} m/s² ({a/GN:.3f} g_n)")
    # Satélite: gravedad 8675,9 N hacia -x y empuje tangencial de 50 N en +y
    F = [(-8675.9, 0.0), comp(50.0, 90.0)]
    sx, sy = suma(F)
    print(f"Satélite (1000 kg): suma de fuerzas = ({sx:.1f}, {sy:.1f}) N; a = ({sx/1000:.4f}, {sy/1000:.4f}) m/s²")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
