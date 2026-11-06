#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C08: antiderivadas, condiciones iniciales y potencial.

Datos: perfil de aceleración propia a(t) = a0 + b t SINTÉTICO (a0 = 20 m/s2,
b = 0.5 m/s3), sin gravedad ni arrastre. (GM)_E nominal = 3.986004e14 m3/s2 y
R_eE nominal = 6.3781e6 m (IAU 2015 B3, arXiv:1510.07674; conversión).
Modelo: antiderivada de un polinomio por la regla de la potencia
(int x^n dx = x^(n+1)/(n+1) + C, n != -1; DLMF 1.4(iv)) y comprobación
derivando numéricamente; condiciones v(0) = 0, x(0) = 0 fijan las constantes.
Potencial: Phi(r) = -GM/r es una antiderivada de g(r) = GM/r^2 con Phi(inf) = 0.
Supuestos: movimiento rectilíneo; masa puntual. Validez: r > 0.
Tolerancias: 1e-6 relativa entre F'(x) (cociente central, h = 1e-5) y f(x).
"""
from __future__ import annotations
import math, platform, sys

GM_E, R_E = 3.986004e14, 6.3781e6


def antiderivada(poly):
    """poly: dict exponente -> coeficiente. Devuelve la antiderivada (C = 0)."""
    out = {}
    for n, c in poly.items():
        if n == -1:
            raise ValueError("n = -1 requiere ln|x|")
        out[n + 1] = c / (n + 1)
    return out


def evalua(poly, x):
    return sum(c * x**n for n, c in poly.items())


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    casos = {
        "3x^2 - 4x + 5": {2: 3.0, 1: -4.0, 0: 5.0},
        "x^-3": {-3: 1.0},
        "sqrt(x)": {0.5: 1.0},
        "a(t) = 20 + 0.5 t": {0: 20.0, 1: 0.5},
    }
    h = 1e-5
    for nombre, p in casos.items():
        F = antiderivada(p)
        for x in (0.7, 2.0, 5.0):
            dF = (evalua(F, x + h) - evalua(F, x - h)) / (2 * h)
            prueba(abs(dF - evalua(p, x)) <= 1e-6 * max(1, abs(evalua(p, x))), f"F' = f en {nombre}")
        print(f"int [{nombre}] dx = {F}  (+ C)  -> comprobada")
    # perfil de aceleración -> v y x
    a = {0: 20.0, 1: 0.5}
    v = antiderivada(a)            # v(0) = 0 -> C = 0
    x = antiderivada(v)            # x(0) = 0 -> C = 0
    print("\n  t [s]    a [m/s2]   v [m/s]    x [m]")
    for t in (0, 5, 10):
        print(f"  {t:5d}  {evalua(a,t):9.3f}  {evalua(v,t):9.3f}  {evalua(x,t):9.3f}")
    prueba(abs(evalua(v, 10) - 225.0) < 1e-9 and abs(evalua(x, 10) - 1083.3333333333) < 1e-6, "v(10), x(10)")
    # dos antiderivadas de 2 sin x cos x que difieren en una constante
    f1, f2 = (lambda u: math.sin(u) ** 2), (lambda u: -math.cos(u) ** 2)
    dif = [f1(u) - f2(u) for u in (0.3, 1.1, 2.9)]
    prueba(max(dif) - min(dif) < 1e-12 and abs(dif[0] - 1) < 1e-12, "difieren en la constante 1")
    print(f"\nsin^2 x - (-cos^2 x) = {dif[0]:.12f} para todo x (constante)")
    # potencial
    phi = lambda r: -GM_E / r
    g = lambda r: GM_E / r**2
    r0, h_alt = R_E, 4.0e5
    dphi = (phi(r0 + 1.0) - phi(r0 - 1.0)) / 2.0
    prueba(abs(dphi - g(r0)) / g(r0) < 1e-6, "Phi' = g")
    print(f"\nPhi(R) = {phi(R_E):.4e} J/kg;  Phi(R+400 km) = {phi(R_E+h_alt):.4e} J/kg")
    dP = phi(R_E + h_alt) - phi(R_E)
    print(f"Energía por kg para subir 400 km = {dP:.4e} J/kg;  g(R)*h = {g(R_E)*h_alt:.4e} J/kg")
    # sesgo de un acelerómetro: error de velocidad y posición
    b = 1.0e-3
    print(f"Sesgo {b} m/s2 durante 100 s: error de v = {b*100:.3f} m/s; error de x = {b*100**2/2:.3f} m")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
