#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C02: funcion de transferencia, forma del espectro de materia y normalizacion con sigma8.

Datos: Omega_m = 0.315, h = 0.674, Omega_b h^2 = 0.0224, n_s = 0.965 y sigma8 = 0.811 (resumen de Planck 2018, arXiv:1807.06209, consultado 2026-11-09).
La FORMA de la funcion de transferencia (ajuste tipo BBKS con el parametro de forma Gamma = Omega_m h exp[-Omega_b(1 + sqrt(2h)/Omega_m)]) es una formula
de la literatura que NO se consulto: es un modelo ILUSTRATIVO, no el espectro de un codigo de Boltzmann.
Modelo: P(k) = A k^n_s T(k)^2, k en h/Mpc, P en (Mpc/h)^3; sigma_R^2 = 1/(2 pi^2) Int k^2 P(k) W(kR)^2 dk con W de sombrero de copa (esfera).
Segunda via: la integral se calcula con Simpson en ln k y con la regla del punto medio en k lineal por tramos; deben coincidir.
Supuestos: sin neutrinos masivos, sin oscilaciones acusticas, ajuste suave. Validez: forma aproximada a pocos por ciento.
Tolerancia: dos integrales dentro de 1e-4 relativo; sigma8 recuperado dentro de 1e-9 por construccion.
"""
from __future__ import annotations
import math, platform

OM, H, OBH2, NS, S8 = 0.315, 0.674, 0.0224, 0.965, 0.811
OB = OBH2 / H ** 2
GAMMA = OM * H * math.exp(-OB * (1 + math.sqrt(2 * H) / OM))


def T(k):
    q = k / GAMMA
    if q < 1e-8:
        return 1.0
    return math.log(1 + 2.34 * q) / (2.34 * q) * (1 + 3.89 * q + (16.1 * q) ** 2 + (5.46 * q) ** 3 + (6.71 * q) ** 4) ** -0.25


def P0(k):
    return k ** NS * T(k) ** 2


def W(x):
    if x < 1e-3:
        return 1 - x * x / 10
    return 3 * (math.sin(x) - x * math.cos(x)) / x ** 3


def sig2_simpson(R, f=P0, lo=1e-5, hi=1e3, n=20000):
    a, b = math.log(lo), math.log(hi)
    h = (b - a) / n
    g = lambda l: math.exp(l) ** 3 * f(math.exp(l)) * W(math.exp(l) * R) ** 2 / (2 * math.pi ** 2)
    s = g(a) + g(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * g(a + i * h)
    return s * h / 3


def sig2_medio(R, f=P0, lo=1e-5, hi=1e3):
    # punto medio en k lineal por tramos geometricos (otra malla y otra variable)
    s = 0.0
    edges = [lo * (hi / lo) ** (j / 60) for j in range(61)]
    for u, v in zip(edges[:-1], edges[1:]):
        m = 400
        d = (v - u) / m
        for i in range(m):
            k = u + (i + 0.5) * d
            s += k * k * f(k) * W(k * R) ** 2 / (2 * math.pi ** 2) * d
    return s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Gamma = {GAMMA:.4f} h/Mpc ; Omega_b = {OB:.4f}")
    a = sig2_simpson(8.0)
    b = sig2_medio(8.0)
    rel = abs(a - b) / a
    print(f"sigma_8^2 sin normalizar: Simpson ln k = {a:.6e} ; punto medio = {b:.6e} ; dif. relativa = {rel:.2e}")
    A = S8 ** 2 / a
    print(f"amplitud A = {A:.4e} (Mpc/h)^3 para sigma8 = {S8}")
    P = lambda k: A * P0(k)
    s8 = math.sqrt(sig2_simpson(8.0, P))
    print(f"sigma8 recuperado = {s8:.6f}")
    print(f"{'k [h/Mpc]':>10} {'T(k)':>8} {'P(k) [(Mpc/h)^3]':>18} {'Delta^2':>10} {'d ln P/d ln k':>14}")
    for k in (1e-3, 1e-2, 3e-2, 1e-1, 1.0, 10.0):
        e = 1e-3
        pend = (math.log(P(k * (1 + e))) - math.log(P(k * (1 - e)))) / (math.log(1 + e) - math.log(1 - e))
        print(f"{k:10.3g} {T(k):8.4f} {P(k):18.4e} {k ** 3 * P(k) / (2 * math.pi ** 2):10.4e} {pend:14.3f}")
    # maximo del espectro
    ks = [10 ** (-3 + 3 * i / 3000) for i in range(3001)]
    kpk = max(ks, key=P)
    print(f"maximo de P(k) en k = {kpk:.4f} h/Mpc (Gamma = {GAMMA:.4f})")
    print(f"{'R [Mpc/h]':>10} {'sigma(R)':>10}")
    sR = {}
    for R in (1.0, 4.0, 8.0, 16.0, 32.0):
        sR[R] = math.sqrt(sig2_simpson(R, P))
        print(f"{R:10.1f} {sR[R]:10.4f}")
    # sensibilidad a Gamma
    amp = {}
    for fac in (0.9, 1.0, 1.1):
        g = GAMMA * fac
        Tg = lambda k, g=g: (math.log(1 + 2.34 * k / g) / (2.34 * k / g) * (1 + 3.89 * k / g + (16.1 * k / g) ** 2 + (5.46 * k / g) ** 3 + (6.71 * k / g) ** 4) ** -0.25)
        Pg = lambda k, Tg=Tg: A * k ** NS * Tg(k) ** 2
        amp[fac] = math.sqrt(sig2_simpson(8.0, Pg))
    print(f"sigma8 con A fija y Gamma x0.9, x1.0, x1.1: {amp[0.9]:.4f}, {amp[1.0]:.4f}, {amp[1.1]:.4f}")
    assert rel < 1e-4
    assert abs(s8 - S8) < 1e-9
    assert abs(T(1e-6) - 1) < 1e-4
    assert all(sR[x] > sR[y] for x, y in ((1.0, 4.0), (4.0, 8.0), (8.0, 16.0), (16.0, 32.0)))
    assert 0.005 < kpk < 0.05
    assert amp[0.9] < amp[1.0] < amp[1.1]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
