#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C02: ecuaciones lineales y cuadráticas con datos lunares.

Datos (PUBLICADOS, observados/estimados): NASA NSSDC Moon Fact Sheet
(actualizada 2024-01-11, consulta 2026-11-05): gravedad superficial 1,62 m/s²,
semieje mayor 384 400 km; velocidad de la luz c = 299 792 458 m/s exacta (SI).
Modelo: caída con aceleración constante  y = y0 + v0 t + (1/2) g t² (eje hacia
abajo) y propagación de la luz  d = c t. Supuestos: g uniforme, sin atmósfera,
sin rotación ni relieve. Validez: alturas pequeñas frente al radio lunar.
Tolerancia de las pruebas: 1e-12 relativa en sustitución; 1e-9 en raíces exactas.
"""
from __future__ import annotations
import math, platform, sys

G_LUNA = 1.62          # m/s^2, NASA Moon Fact Sheet
A_LUNA = 384_400e3     # m, semieje mayor
C = 299_792_458.0      # m/s, exacto


def lineal(a, b):
    """Resuelve a x + b = 0 (a != 0)."""
    if a == 0:
        raise ValueError("a = 0: no es una ecuación lineal")
    return -b / a


def cuadratica(a, b, c):
    """Raíces reales de a x^2 + b x + c = 0 con fórmula estable.
    Evita restar números casi iguales: calcula primero la raíz de mayor módulo
    y obtiene la otra con x1 * x2 = c / a."""
    disc = b * b - 4 * a * c
    if disc < 0:
        return ()
    s = math.sqrt(disc)
    q = -0.5 * (b + math.copysign(s, b))
    x1 = q / a
    x2 = c / q if q != 0 else x1
    return tuple(sorted((x1, x2)))


def pruebas():
    assert lineal(2, -6) == 3.0
    r = cuadratica(1, -5, 6)
    assert all(abs(x - y) < 1e-9 for x, y in zip(r, (2.0, 3.0))), r
    assert cuadratica(1, 0, 1) == ()                     # discriminante negativo
    # Cancelación: x^2 - 1e8 x + 1 = 0  ->  raíces ~1e8 y ~1e-8 (producto = 1)
    pequena, grande = cuadratica(1, -1e8, 1)
    assert abs(pequena * grande - 1.0) < 1e-9
    ingenua = (1e8 - math.sqrt(1e16 - 4)) / 2           # fórmula directa, inestable
    assert abs(pequena - 1e-8) / 1e-8 < 1e-12            # estable: exacta
    assert abs(ingenua - 1e-8) / 1e-8 > 1e-9             # ingenua: pierde cifras
    # sustitución de la solución en la ecuación (caída)
    t = cuadratica(0.5 * G_LUNA, 1.0, -2.0)[-1]
    assert abs(0.5 * G_LUNA * t * t + 1.0 * t - 2.0) < 1e-12


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (lineal, cuadrática, discriminante<0, cancelación, sustitución)")
    h = 2.0
    t0 = math.sqrt(2 * h / G_LUNA)
    print(f"\nSoltar desde {h} m en la Luna (v0 = 0): t = sqrt(2h/g) = {t0:.4f} s")
    t1 = cuadratica(0.5 * G_LUNA, 1.0, -h)[-1]
    print(f"Lanzar hacia abajo a 1,0 m/s desde {h} m: t = {t1:.4f} s")
    print(f"Con g terrestre 9,81 (referencia): t = {math.sqrt(2*h/9.81):.4f} s")
    print(f"Velocidad al llegar (v0 = 0): {G_LUNA*t0:.4f} m/s")
    tl = A_LUNA / C
    print(f"\nLuz Tierra–Luna (semieje mayor): t = d/c = {tl:.4f} s")
    d_ida_vuelta = C * 2.5
    print(f"Un eco de 2,5 s corresponde a d = c t/2 = {d_ida_vuelta/2/1e3:.0f} km")
    print("\nCancelación numérica con x^2 - 1e8 x + 1 = 0:")
    pq, gr = cuadratica(1, -1e8, 1)
    ing = (1e8 - math.sqrt(1e16 - 4)) / 2
    print(f"  estable : raíz pequeña = {pq:.6e}")
    print(f"  ingenua : raíz pequeña = {ing:.6e}")


if __name__ == "__main__":
    main()
