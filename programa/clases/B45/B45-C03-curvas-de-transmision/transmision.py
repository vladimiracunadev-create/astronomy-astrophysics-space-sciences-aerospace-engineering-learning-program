#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C03: curvas de transmision, producto de elementos, longitud de onda efectiva y fugas.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): h, c y k_B exactas. Todas las curvas (filtro gaussiano de pico 0,9, centro 550 nm y sigma 40 nm; eficiencia cuantica
lineal; atmosfera) son ILUSTRATIVAS, no medidas de un instrumento.
Modelo: T_total(lambda) = producto de curvas; ancho equivalente W = integral de T; lambda_efectiva = integral(lambda T S)/integral(T S); lambda_pivote^2 = integral(T lambda)/integral(T/lambda).
Supuestos: fuente continua de Planck, integracion en energia. Validez: la longitud de onda efectiva depende de la fuente; la de pivote no.
Tolerancia: ancho equivalente gaussiano frente a A sigma sqrt(2 pi) a 1e-6; pivote por debajo de la efectiva (fuente plana) en menos de 2 nm.
"""
from __future__ import annotations
import math, platform, sys

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23


def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


def planck(l, T):
    return 2 * H * C ** 2 / l ** 5 / math.expm1(H * C / (l * KB * T))


def filtro(l):
    return 0.9 * math.exp(-0.5 * ((l - 550e-9) / 40e-9) ** 2)


def qe(l):
    return max(0.0, min(0.9, 0.9 - (l - 400e-9) / (1000e-9 - 400e-9) * 0.7))


def atm(l):
    return math.exp(-0.1 * (550e-9 / l) ** 4)        # solo dispersion de Rayleigh ilustrativa


def fuga(l):
    return filtro(l) + (1e-3 if l > 700e-9 else 0.0)


A, B = 300e-9, 1000e-9


def efectiva(T, S=None):
    if S is None:
        S = lambda l: 1.0
    num = simpson(lambda l: l * T(l) * S(l), A, B)
    den = simpson(lambda l: T(l) * S(l), A, B)
    return num / den


def calcular():
    r = {}
    r["W"] = simpson(filtro, A, B)
    r["W_anal"] = 0.9 * 40e-9 * math.sqrt(2 * math.pi)
    tot = lambda l: filtro(l) * qe(l) * atm(l)
    r["pico_filtro"] = filtro(550e-9)
    r["pico_total"] = tot(550e-9)
    r["W_tot"] = simpson(tot, A, B)
    r["eff_plana"] = efectiva(tot)
    r["pivote"] = math.sqrt(simpson(lambda l: tot(l) * l, A, B) / simpson(lambda l: tot(l) / l, A, B))
    for T in (3000.0, 6000.0, 10000.0):
        r[f"eff_{int(T)}"] = efectiva(tot, lambda l, T=T: planck(l, T))
    for T in (3000.0, 10000.0):
        sin = simpson(lambda l: filtro(l) * planck(l, T), A, B)
        con = simpson(lambda l: fuga(l) * planck(l, T), A, B)
        r[f"fuga_{int(T)}"] = con / sin - 1
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"ancho equivalente del filtro = {r['W']*1e9:.4f} nm ; analitico = {r['W_anal']*1e9:.4f} nm")
    print(f"pico del filtro = {r['pico_filtro']:.3f} ; pico del producto = {r['pico_total']:.4f} ; ancho equivalente total = {r['W_tot']*1e9:.3f} nm")
    print(f"lambda efectiva (fuente plana) = {r['eff_plana']*1e9:.3f} nm ; lambda de pivote = {r['pivote']*1e9:.3f} nm")
    for T in (3000, 6000, 10000):
        print(f"lambda efectiva con Planck {T} K = {r[f'eff_{T}']*1e9:.3f} nm")
    print(f"aumento de flujo por una fuga de 1e-3 sobre 700 nm: 3000 K {r['fuga_3000']*100:.3f} % ; 10000 K {r['fuga_10000']*100:.4f} %")
    assert abs(r["W"] / r["W_anal"] - 1) < 1e-6
    assert r["eff_3000"] > r["eff_6000"] > r["eff_10000"]
    assert 0 < r["eff_plana"] - r["pivote"] < 2e-9
    assert r["fuga_3000"] > 5 * r["fuga_10000"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
