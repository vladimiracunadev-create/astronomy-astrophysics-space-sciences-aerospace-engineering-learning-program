#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C13: ley de Wien, pico en lambda y en nu, y ajuste de temperatura a flujos con ruido.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): h, c, k_B y sigma exactas; constante de desplazamiento de Wien en longitud de onda b = 2,897771955e-3 m K y en frecuencia
5,878925757e10 Hz/K. Los cinco flujos en bandas son SINTETICOS (T verdadera 6500 K, ruido gaussiano relativo del 2 %, semilla 20261109), con bandas rectangulares ILUSTRATIVAS de 50 nm.
Modelo: B_lambda(T) y B_nu(T) de Planck; maximo por biseccion de x = 5(1 - e^-x) y x = 3(1 - e^-x); ajuste de T por busqueda en rejilla de chi cuadrado con amplitud analitica.
Supuestos: cuerpo negro puro, sin extincion, bandas estrechas. Validez: una estrella real se aparta del cuerpo negro (lineas, opacidad).
Tolerancia: b calculada frente a NIST a 1e-9 relativo; T recuperada dentro de 3 errores del ajuste (error por curvatura de chi cuadrado).
"""
from __future__ import annotations
import math, platform, random, sys

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
SIGMA = 5.670374419e-8
B_NIST = 2.897771955e-3
BNU_NIST = 5.878925757e10
SEMILLA = 20261109


def raiz(f, a, b):
    for _ in range(200):
        m = 0.5 * (a + b)
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)


def planck(l, T):
    return 2 * H * C ** 2 / l ** 5 / math.expm1(H * C / (l * KB * T))


def banda(l0, T, ancho=50e-9, n=40):
    h = ancho / n
    return sum(planck(l0 - ancho / 2 + (i + 0.5) * h, T) for i in range(n)) * h


def calcular():
    r = {}
    x5 = raiz(lambda x: x - 5 * (1 - math.exp(-x)), 1.0, 10.0)
    x3 = raiz(lambda x: x - 3 * (1 - math.exp(-x)), 1.0, 10.0)
    r["x5"], r["x3"] = x5, x3
    r["b_calc"] = H * C / (KB * x5)
    r["bnu_calc"] = x3 * KB / H
    T = 5772.0
    r["lam_pico_nm"] = r["b_calc"] / T * 1e9
    r["nu_pico_THz"] = r["bnu_calc"] * T / 1e12
    r["lam_de_nu_pico_nm"] = C / (r["bnu_calc"] * T) * 1e9
    r["tabla"] = [(Tx, r["b_calc"] / Tx * 1e9) for Tx in (3000.0, 5772.0, 10000.0, 30000.0)]
    r["sb_ratio"] = (2 * math.pi ** 5 * KB ** 4 / (15 * H ** 3 * C ** 2)) / SIGMA
    # ajuste de T: cinco bandas sinteticas
    rnd = random.Random(SEMILLA)
    centros = [400e-9, 500e-9, 600e-9, 700e-9, 800e-9]
    T_true = 6500.0
    A_true = 1.0
    datos = [A_true * banda(c, T_true) * (1 + rnd.gauss(0, 0.02)) for c in centros]
    sig = [0.02 * d for d in datos]
    mejor = None
    cadena = []
    for i in range(3000, 12001, 10):
        Tg = float(i)
        m = [banda(c, Tg) for c in centros]
        A = sum(d * mm / s ** 2 for d, mm, s in zip(datos, m, sig)) / sum(mm * mm / s ** 2 for mm, s in zip(m, sig))
        chi2 = sum(((d - A * mm) / s) ** 2 for d, mm, s in zip(datos, m, sig))
        cadena.append((Tg, chi2, A))
        if mejor is None or chi2 < mejor[1]:
            mejor = (Tg, chi2, A)
    r["T_fit"], r["chi2"], r["A_fit"] = mejor
    # error por Delta chi2 = 1 (perfil con amplitud optima en cada T)
    dentro = [t for t, c, a in cadena if c <= mejor[1] + 1.0]
    r["T_lo"], r["T_hi"] = min(dentro), max(dentro)
    r["sigma_T"] = 0.5 * (r["T_hi"] - r["T_lo"])
    # temperatura de color por razon de dos bandas (400 y 700 nm) sin ruido
    r1 = banda(400e-9, 6500.0) / banda(700e-9, 6500.0)
    lo, hi = 3000.0, 20000.0
    f = lambda Tx: banda(400e-9, Tx) / banda(700e-9, Tx) - r1
    r["T_color"] = raiz(f, lo, hi)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"raices: x = {r['x5']:.9f} (lambda) ; x = {r['x3']:.9f} (nu)")
    print(f"b = {r['b_calc']:.9e} m K (NIST 2,897771955e-3) ; b_nu = {r['bnu_calc']:.9e} Hz/K (NIST 5,878925757e10)")
    print(f"T = 5772 K: pico en lambda {r['lam_pico_nm']:.2f} nm ; pico en nu {r['nu_pico_THz']:.2f} THz = {r['lam_de_nu_pico_nm']:.2f} nm")
    for T, l in r["tabla"]:
        print(f"  T = {T:7.0f} K -> lambda_max = {l:8.2f} nm")
    print(f"sigma calculada / NIST = {r['sb_ratio']:.12f}")
    print(f"ajuste a 5 bandas: T = {r['T_fit']:.0f} K (verdadera 6500) ; chi2 = {r['chi2']:.2f} para 3 grados de libertad ; intervalo delta chi2 = 1: {r['T_lo']:.0f} a {r['T_hi']:.0f} K ; amplitud = {r['A_fit']:.4f}")
    print(f"temperatura de color sin ruido por razon 400/700 nm = {r['T_color']:.2f} K")
    assert abs(r["b_calc"] / B_NIST - 1) < 1e-9
    assert abs(r["bnu_calc"] / BNU_NIST - 1) < 1e-9
    assert abs(r["sb_ratio"] - 1) < 1e-9
    assert abs(r["T_fit"] - 6500) < 3 * r["sigma_T"]
    assert abs(r["T_color"] - 6500) < 0.01
    assert r["lam_de_nu_pico_nm"] > 1.5 * r["lam_pico_nm"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
