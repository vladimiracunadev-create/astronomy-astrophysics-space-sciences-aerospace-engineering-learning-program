#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C02: magnitudes de Pogson, sistema AB, suma de magnitudes y color sintetico.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): h, c y k_B exactas. La definicion AB (m_AB = -2,5 log10(f_nu) - 48,60 con f_nu en erg s^-1 cm^-2 Hz^-1, es decir
3631 Jy para m = 0) es conocimiento de libro NO consultado aqui. Los filtros B y V son rectangulos ILUSTRATIVOS (400-500 nm y 500-600 nm), no filtros reales.
Modelo: Pogson m = -2,5 log10(F/F0); color sintetico = -2,5 log10 de la razon de integrales de F_lambda de Planck por cada filtro.
Supuestos: filtros rectangulares, flujo integrado en energia, sin atmosfera. Validez: colores solo comparables entre si; el punto cero de color se fija con T = 10000 K (ilustrativo).
Tolerancia: relacion de Pogson a 1e-12; limite de Rayleigh-Jeans del color frente a la integral analitica de lambda^-4 a 1e-3 mag.
"""
from __future__ import annotations
import math, platform, sys

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


def planck(lam, T):
    x = H * C / (lam * KB * T)
    return 2 * H * C ** 2 / lam ** 5 / math.expm1(x)


def banda(T, a, b):
    return simpson(lambda l: planck(l, T), a, b)


def bv_bruto(T):
    return -2.5 * math.log10(banda(T, 400e-9, 500e-9) / banda(T, 500e-9, 600e-9))


def calcular():
    r = {}
    r["pogson"] = 100 ** 0.2
    r["razon5"] = 10 ** (0.4 * 5)
    f_nu = 3631e-23                       # 3631 Jy en erg s^-1 cm^-2 Hz^-1
    r["m_ab0"] = -2.5 * math.log10(f_nu) - 48.60
    r["m_ab_1jy"] = -2.5 * math.log10(1e-23) - 48.60
    r["suma2"] = -2.5 * math.log10(2.0)
    r["suma_ejemplo"] = -2.5 * math.log10(10 ** (-0.4 * 12.0) + 10 ** (-0.4 * 13.0))
    r["mod_dist"] = 5 * math.log10(100.0 / 10.0)
    r["sig_m"] = 2.5 / math.log(10) * 0.01
    cero = bv_bruto(10000.0)
    temps = [3500.0, 5000.0, 6000.0, 8000.0, 10000.0, 20000.0]
    r["colores"] = [(T, bv_bruto(T) - cero) for T in temps]
    # limite de Rayleigh-Jeans: F_lambda ~ lambda^-4 -> integral analitica (1/3)(a^-3 - b^-3)
    anal = -2.5 * math.log10((400e-9 ** -3 - 500e-9 ** -3) / (500e-9 ** -3 - 600e-9 ** -3))
    r["rj_num"] = bv_bruto(1e7)
    r["rj_anal"] = anal
    r["cero"] = cero
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"100^(1/5) = {r['pogson']:.6f} ; 10^(0,4*5) = {r['razon5']:.3f}")
    print(f"m_AB(3631 Jy) = {r['m_ab0']:.5f} ; m_AB(1 Jy) = {r['m_ab_1jy']:.4f}")
    print(f"dos estrellas iguales: {r['suma2']:+.4f} mag ; 12 + 13 -> {r['suma_ejemplo']:.4f}")
    print(f"modulo de distancia a 100 pc = {r['mod_dist']:.1f} ; sigma_m para 1 % de flujo = {r['sig_m']:.5f}")
    print(f"{'T (K)':>8} {'B-V sintetico':>14}")
    for T, c in r["colores"]:
        print(f"{T:8.0f} {c:14.4f}")
    print(f"limite Rayleigh-Jeans (T=1e7 K) numerico {r['rj_num']:.5f} ; analitico {r['rj_anal']:.5f}")
    assert abs(r["pogson"] ** 5 - 100) < 1e-9
    assert abs(r["razon5"] - 100) < 1e-9
    assert abs(r["m_ab0"]) < 1e-3
    assert abs(r["m_ab_1jy"] - 8.90) < 5e-3
    assert abs(r["suma2"] + 0.7526) < 1e-4
    assert abs(r["rj_num"] - r["rj_anal"]) < 1e-3
    cs = [c for _, c in r["colores"]]
    assert all(cs[i] > cs[i + 1] for i in range(len(cs) - 1))
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
