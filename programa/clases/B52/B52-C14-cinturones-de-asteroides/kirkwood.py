#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C14: posiciones de las resonancias de movimiento medio con Jupiter en el cinturon de asteroides.

Datos consultados el 2026-11-09: periodo orbital de Jupiter 4331 dias y distancia al Sol 778.5e6 km (NASA/NSSDC, ficha de planetas; fila
«Distance from Sun»; sin incertidumbres); (GM)_sol nominal de la IAU 2015 (Resolucion B3); la unidad astronomica (1.495978707e11 m) no se consulto.
No se usan datos de asteroides: las posiciones se calculan, no se comparan con un catalogo (NO consultado). El intervalo 2.0-3.3 ua del cinturon principal es
ILUSTRATIVO (no consultado).
Sistema de referencia: heliocentrico, orbitas circulares coplanares; SI.
Via 1: a_res = a_J (q/p)^(2/3) con la tercera ley de Kepler para el periodo de Jupiter de la ficha. Via 2: integracion RK4 de una particula de prueba
en a_res (movimiento kepleriano alrededor del Sol, sin Jupiter) y medida del angulo recorrido en un periodo de Jupiter: debe ser 2 pi p/q.
Tolerancias: razon de revoluciones numerica frente a p/q 1e-6.
"""
from __future__ import annotations
import math, platform

GM = 1.3271244e20
UA = 1.495978707e11
DIA = 86400.0
P_J = 4331.0 * DIA
A_FICHA = 778.5e9
RES = [(4, 1), (3, 1), (5, 2), (7, 3), (2, 1), (3, 2), (1, 1)]  # p:q = revoluciones del asteroide por q de Jupiter


def a_de_periodo(p):
    return (GM * p ** 2 / (4 * math.pi ** 2)) ** (1.0 / 3.0)


def rk4(f, y, h):
    k1 = f(y); k2 = f([a + 0.5 * h * b for a, b in zip(y, k1)]); k3 = f([a + 0.5 * h * b for a, b in zip(y, k2)]); k4 = f([a + h * b for a, b in zip(y, k3)])
    return [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(y, k1, k2, k3, k4)]


def revoluciones(a, T, n=4000):
    f = lambda y: [y[2], y[3], -GM * y[0] / (y[0] ** 2 + y[1] ** 2) ** 1.5, -GM * y[1] / (y[0] ** 2 + y[1] ** 2) ** 1.5]
    y = [a, 0.0, 0.0, math.sqrt(GM / a)]
    ang, prev, h = 0.0, 0.0, T / n
    for _ in range(n):
        y = rk4(f, y, h)
        th = math.atan2(y[1], y[0])
        d = th - prev
        if d < -math.pi: d += 2 * math.pi
        if d > math.pi: d -= 2 * math.pi
        ang += d
        prev = th
    return ang / (2 * math.pi)


def calcular():
    aj = a_de_periodo(P_J)
    filas = []
    for p, q in RES:
        a = aj * (q / p) ** (2.0 / 3.0)
        rev = revoluciones(a, P_J)
        filas.append((p, q, a, rev, p / q))
    return dict(aj=aj, filas=filas)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Jupiter: distancia de la ficha = {A_FICHA / UA:.4f} ua ; semieje de Kepler con P = 4331 d = {r['aj'] / UA:.4f} ua ; dif. rel. = {r['aj'] / A_FICHA - 1:+.2e}")
    print(f"{'p:q':>5} {'a_res [ua]':>11} {'revol. numericas en P_J':>24} {'p/q':>8} {'dif. rel.':>10} {'en 2.0-3.3 ua':>14}")
    for p, q, a, rev, pq in r["filas"]:
        print(f"{p}:{q:<3} {a / UA:11.4f} {rev:24.9f} {pq:8.4f} {abs(rev / pq - 1):10.1e} {'si' if 2.0 <= a / UA <= 3.3 else 'no':>14}")
    for p, q, a, rev, pq in r["filas"]:
        assert abs(rev / pq - 1) < 1e-6
    assert abs(r["aj"] / A_FICHA - 1) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
