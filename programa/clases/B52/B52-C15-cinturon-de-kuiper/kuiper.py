#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C15: resonancias con Neptuno y temperatura de equilibrio en el cinturon de Kuiper.

Datos consultados el 2026-11-09: periodo orbital de Neptuno 59 800 dias y distancia al Sol 4515e6 km (NASA/NSSDC, ficha de planetas; fila
«Distance from Sun»; sin incertidumbres); (GM)_sol y luminosidad nominal L_sol = 3.828e26 W (IAU 2015, Resolucion B3, texto del PDF);
constante de Stefan-Boltzmann 5.670374419e-8 W m^-2 K^-4 (NIST, CODATA 2022). La unidad astronomica (1.495978707e11 m) no se consulto.
Datos ILUSTRATIVOS (sinteticos): albedo de Bond 0.1 y 0.3; excentricidad 0.25 del objeto resonante hipotetico. Sin catalogo de objetos transneptunianos (NO consultado).
Sistema de referencia: heliocentrico, orbitas coplanares; SI.
Via 1: a_res = a_N (p/q)^(2/3) (resonancia exterior p:q: Neptuno da p vueltas por q del objeto, P_obj/P_N = p/q). Via 2: integracion RK4 de una particula de prueba y conteo de revoluciones por periodo de Neptuno.
Temperatura: T = [L (1-A) / (16 pi sigma d^2)]^(1/4) (cuerpo esferico de rotacion rapida) frente a biseccion del balance de energia.
Tolerancias: revoluciones 1e-6 relativo; temperatura 1e-9 relativo.
"""
from __future__ import annotations
import math, platform

GM = 1.3271244e20
L_SOL = 3.828e26
SIGMA = 5.670374419e-8
UA = 1.495978707e11
DIA = 86400.0
P_N = 59800.0 * DIA
A_FICHA = 4515e9
RES = [(3, 2), (2, 1), (5, 3), (4, 3), (5, 2)]


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


def t_equilibrio(d, albedo):
    return (L_SOL * (1.0 - albedo) / (16.0 * math.pi * SIGMA * d ** 2)) ** 0.25


def t_biseccion(d, albedo):
    # balance: potencia absorbida (1-A) L pi R^2/(4 pi d^2) = emitida 4 pi R^2 sigma T^4 ; se resuelve para T con R = 1
    absorbida = (1.0 - albedo) * L_SOL * math.pi / (4.0 * math.pi * d ** 2)
    f = lambda T: 4.0 * math.pi * SIGMA * T ** 4 - absorbida
    a, b = 1.0, 1000.0
    for _ in range(300):
        c = 0.5 * (a + b)
        if f(c) < 0: a = c
        else: b = c
    return 0.5 * (a + b)


def calcular():
    an = a_de_periodo(P_N)
    filas = []
    for p, q in RES:
        a = an * (p / q) ** (2.0 / 3.0)
        filas.append((p, q, a, revoluciones(a, P_N), q / p))
    temps = []
    for d_ua in (1.0, 30.0, 40.0, 48.0):
        for alb in (0.1, 0.3):
            temps.append((d_ua, alb, t_equilibrio(d_ua * UA, alb), t_biseccion(d_ua * UA, alb)))
    a32 = filas[0][2]
    e = 0.25
    return dict(an=an, filas=filas, temps=temps, q_peri=a32 * (1 - e), q_apo=a32 * (1 + e), e=e)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Neptuno: distancia de la ficha = {A_FICHA / UA:.4f} ua ; semieje de Kepler con P = 59 800 d = {r['an'] / UA:.4f} ua ; dif. rel. = {r['an'] / A_FICHA - 1:+.2e}")
    print(f"{'p:q':>5} {'a_res [ua]':>11} {'revol. del objeto por P_N':>24} {'q/p':>8} {'dif. rel.':>10}")
    for p, q, a, rev, pq in r["filas"]:
        print(f"{p}:{q:<3} {a / UA:11.4f} {rev:24.9f} {pq:8.4f} {abs(rev / pq - 1):10.1e}")
    print(f"Objeto hipotetico (ilustrativo) en 3:2 con e = {r['e']}: perihelio = {r['q_peri'] / UA:.3f} ua (< a_N = {r['an'] / UA:.3f} ua: cruza la orbita de Neptuno), afelio = {r['q_apo'] / UA:.3f} ua")
    print(f"{'d [ua]':>7} {'albedo':>7} {'T formula [K]':>14} {'T biseccion [K]':>16}")
    for d, alb, t1, t2 in r["temps"]:
        print(f"{d:7.1f} {alb:7.1f} {t1:14.4f} {t2:16.4f}")
    for p, q, a, rev, pq in r["filas"]:
        assert abs(rev / pq - 1) < 1e-6
    for d, alb, t1, t2 in r["temps"]:
        assert abs(t1 / t2 - 1) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
