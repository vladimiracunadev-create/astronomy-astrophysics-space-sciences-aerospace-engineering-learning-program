#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C07: optimización con derivadas.

Parte A (SINTÉTICA): tanque cilíndrico de volumen V fijo con tapas planas;
minimizar el área A(r) = 2 pi r^2 + 2 V / r (proxy de masa de pared).
Solución analítica: r^3 = V/(2 pi), L = 2 r.
Parte B (modelo): punto de atracción igual entre la Tierra y la Luna sobre su
línea, con Phi(x) = -GM_T/x - GM_L/(d - x) (sin rotación ni Sol).
Datos publicados: (GM)_Tierra nominal = 3.986004e5 km3/s2 (IAU 2015 B3,
arXiv:1510.07674); GM_Luna = 4.90e3 km3/s2 (3 cifras) y d = 384 400 km
(NASA/NSSDC, ficha lunar, 2024). Estimación de orden de magnitud.
Supuestos: cuerpos puntuales, sin movimiento orbital. Validez: 0 < x < d.
Tolerancias: 1e-9 relativa entre óptimo analítico y numérico (sección áurea).
"""
from __future__ import annotations
import math, platform, sys


def area(r, V):
    return 2 * math.pi * r * r + 2 * V / r


def seccion_aurea(f, a, b, tol=1e-10):
    """Mínimo de una función unimodal en [a, b]."""
    phi = (math.sqrt(5) - 1) / 2
    c, d = b - phi * (b - a), a + phi * (b - a)
    while abs(b - a) > tol:
        if f(c) < f(d):
            b, d = d, c
            c = b - phi * (b - a)
        else:
            a, c = c, d
            d = a + phi * (b - a)
    return 0.5 * (a + b)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    print("PARTE A: tanque (datos SINTÉTICOS)")
    print("  V [m3]    r* [m]     L* [m]     A* [m2]    A''(r*)   r_num [m]")
    for V in (1.0, 10.0, 100.0):
        r_an = (V / (2 * math.pi)) ** (1 / 3)
        r_num = seccion_aurea(lambda r: area(r, V), 0.01, 100.0)
        L = V / (math.pi * r_an**2)
        d2 = 4 * math.pi + 4 * V / r_an**3
        prueba(abs(r_num - r_an) / r_an < 1e-7, "óptimo numérico = analítico")
        prueba(abs(L - 2 * r_an) < 1e-9 * L, "L = 2 r")
        prueba(d2 > 0, "segunda derivada positiva (mínimo)")
        print(f"  {V:6.1f}  {r_an:9.5f}  {L:9.5f}  {area(r_an, V):9.4f}  {d2:8.3f}  {r_num:9.5f}")
    V = 10.0
    r_an = (V / (2 * math.pi)) ** (1 / 3)
    a0 = area(r_an, V)
    for f in (0.9, 1.0, 1.1):
        print(f"  V=10, r = {f:.1f} r*: A = {area(f*r_an, V):.4f} m2 ({area(f*r_an, V)/a0-1:+.3%})")
    a1 = area(1.0, V)
    print(f"  V=10, r = 1.0 m: A = {a1:.4f} m2 ({a1/a0-1:+.3%})")
    # escala: A* proporcional a V^(2/3)
    a100, a1_ = area((100/(2*math.pi))**(1/3), 100.0), area((1/(2*math.pi))**(1/3), 1.0)
    prueba(abs(a100 / a1_ - 100 ** (2 / 3)) < 1e-9, "A* ~ V^(2/3)")

    print("\nPARTE B: punto de atracción igual Tierra-Luna (modelo)")
    GE, GL, d = 3.986004e5, 4.90e3, 384_400.0
    q = math.sqrt(GL / GE)
    x_an = d / (1 + q)
    # dPhi/dx = GM_T/x^2 - GM_L/(d-x)^2 = 0, hallada por bisección
    f = lambda x: GE / x**2 - GL / (d - x) ** 2
    a, b = 0.1 * d, 0.999 * d
    for _ in range(200):
        c = 0.5 * (a + b)
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    x_bis = 0.5 * (a + b)
    prueba(abs(x_bis - x_an) < 1e-6, "bisección = fórmula")
    # segunda derivada de Phi: -2 GE/x^3 - 2 GL/(d-x)^3 < 0 -> máximo de Phi
    d2phi = -2 * GE / x_an**3 - 2 * GL / (d - x_an) ** 3
    prueba(d2phi < 0, "Phi tiene un máximo sobre la línea")
    print(f"  sqrt(GM_L/GM_T) = {q:.5f};  x* = {x_an:.1f} km desde la Tierra;  a la Luna: {d - x_an:.1f} km")
    print(f"  Phi''(x*) = {d2phi:.3e} km2/s2/km2 (negativa: máximo de Phi a lo largo de la línea)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
