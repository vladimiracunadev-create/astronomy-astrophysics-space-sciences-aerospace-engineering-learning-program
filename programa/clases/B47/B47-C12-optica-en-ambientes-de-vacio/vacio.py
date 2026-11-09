#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C12: optica en vacio, camino libre medio, flujo de Hertz-Knudsen, tiempo de monocapa y pelicula contaminante sobre un espejo.

Datos: k_B = 1,380649e-23 J/K y u = 1,66053906892e-27 kg de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09); 1 Torr = 101325/760 Pa (definicion).
ILUSTRATIVOS (no medidos): diametro molecular de N2 3,7e-10 m, contaminante de 100 u a 293 K, presion parcial 1e-8 Pa, densidad superficial de monocapa 1e19 m-2, espejo de aluminio con
n = 0,96 + 6,69 i a 550 nm (valor de uso general, no consultado aqui), pelicula con indice 1,5 e indice del aire 1,000277.
Modelo: (1) camino libre medio lambda = k T/(sqrt 2 pi d^2 p); (2) flujo de Hertz-Knudsen Phi = p/sqrt(2 pi m k T), contrastado con n <v>/4 y <v> integrado numericamente de la
distribucion de Maxwell; (3) reflectancia normal de una pelicula delgada sobre metal por la formula de Airy y por la matriz de transferencia; (4) longitud de onda en aire frente a vacio.
Supuestos: coeficiente de adherencia 1, incidencia normal, pelicula homogenea y transparente. Validez: ilustrativa.
Tolerancia: flujo de dos vias, 1e-6 relativo; reflectancia de dos vias, 1e-12; limite de 1 langmuir cerca de un segundo.
"""
from __future__ import annotations
import math, cmath, platform

KB = 1.380649e-23
U = 1.66053906892e-27
TORR = 101325 / 760
T = 293.0


def camino_libre(p, d=3.7e-10, t=T):
    return KB * t / (math.sqrt(2) * math.pi * d * d * p)


def flujo_hk(p, mu, t=T):
    return p / math.sqrt(2 * math.pi * mu * U * KB * t)


def vmedia_numerica(mu, t=T, n=200000):
    m = mu * U
    a = m / (2 * KB * t)
    vmax = 12 / math.sqrt(a)
    h = vmax / n
    s = 0.0
    for i in range(n + 1):
        v = i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * v * (4 * math.pi * (a / math.pi) ** 1.5 * v * v * math.exp(-a * v * v))
    return s * h / 3


def r_airy(n0, n1, n2, d, lam):
    r01 = (n0 - n1) / (n0 + n1)
    r12 = (n1 - n2) / (n1 + n2)
    e = cmath.exp(2j * 2 * math.pi * n1 * d / lam)
    r = (r01 + r12 * e) / (1 + r01 * r12 * e)
    return abs(r) ** 2


def r_matriz(n0, n1, n2, d, lam):
    dl = 2 * math.pi * n1 * d / lam
    m11, m12, m21, m22 = cmath.cos(dl), -1j * cmath.sin(dl) / n1, -1j * n1 * cmath.sin(dl), cmath.cos(dl)
    r = (n0 * (m11 + m12 * n2) - (m21 + m22 * n2)) / (n0 * (m11 + m12 * n2) + (m21 + m22 * n2))
    return abs(r) ** 2


def calc():
    r = {}
    r["mfp"] = {p: camino_libre(p) for p in (101325.0, 1.0, 1e-3, 1e-6)}
    r["fh"] = {}
    for mu in (28.0, 100.0):
        p = 1e-8
        a = flujo_hk(p, mu)
        vm = vmedia_numerica(mu)
        b = p / (KB * T) * vm / 4
        r["fh"][mu] = (a, b)
    ns = 1e19
    r["t_mono"] = ns / flujo_hk(1e-8, 100.0)
    r["t_mono_dias"] = r["t_mono"] / 86400
    r["langmuir"] = ns / flujo_hk(1e-6 * TORR, 28.0)
    n0, n2, lam = 1.0, 0.96 + 6.69j, 550e-9
    r["refl"] = {}
    for d in (0, 10e-9, 50e-9, 100e-9, 200e-9):
        r["refl"][d] = (r_airy(n0, 1.5, n2, d, lam), r_matriz(n0, 1.5, n2, d, lam))
    r["dl_aire"] = lam * (1 - 1 / 1.000277)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for p, v in r["mfp"].items():
        print(f"p = {p:10.3e} Pa : camino libre medio = {v:.4e} m")
    for mu, (a, b) in r["fh"].items():
        print(f"M = {mu:5.1f} u a 1e-8 Pa: Hertz-Knudsen = {a:.6e} m-2 s-1 ; n<v>/4 con <v> numerica = {b:.6e}")
        assert abs(a - b) / a < 1e-6
    print(f"tiempo de monocapa del contaminante (100 u, 1e-8 Pa): {r['t_mono']:.3e} s = {r['t_mono_dias']:.2f} dias")
    print(f"tiempo de monocapa de N2 a 1e-6 Torr: {r['langmuir']:.2f} s")
    print(f"{'d [nm]':>8} {'R Airy':>12} {'R matriz':>12}")
    for d, (a, b) in r["refl"].items():
        print(f"{d*1e9:8.0f} {a:12.8f} {b:12.8f}")
        assert abs(a - b) < 1e-12
    print(f"diferencia de longitud de onda aire-vacio a 550 nm: {r['dl_aire']*1e9:.4f} nm")
    assert 0.5 < r["langmuir"] < 10
    assert r["refl"][0][0] > r["refl"][100e-9][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
