#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C12: teorema fundamental del cálculo y velocidad de escape.

Datos (PUBLICADOS): (GM)_E nominal = 3.986004e14 m3/s2 y R_eE nominal =
6.3781e6 m (IAU 2015 B3, arXiv:1510.07674; conversión). Radio medio
volumétrico = 6371.000 km y velocidad de escape = 11.186 km/s (NASA/NSSDC,
Earth Fact Sheet, actualizada 2024-11-15) como referencia independiente.
Modelo: trabajo por unidad de masa para llevar un cuerpo de R a r_max:
W = int_R^rmax GM/r^2 dr = GM (1/R - 1/rmax)  (teorema fundamental, parte 1);
G(x) = int_R^x g dr cumple G'(x) = g(x)  (parte 2). Escape: (1/2) v^2 = GM/R.
Supuestos: Tierra esférica, masa puntual, sin rotación, sin atmósfera.
Validez: r >= R. Tolerancias: Simpson n = 4000 a 1e-9 relativa;
v_esc con R medio dentro de 1e-3 relativa del valor NASA.
"""
from __future__ import annotations
import math, platform, sys

GM, R = 3.986004e14, 6.3781e6
R_MEDIO, V_ESC_NASA = 6.371e6, 11186.0


def g(r):
    return GM / r**2


def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 2 * sum(f(a + i * h) for i in range(2, n, 2))
    return s * h / 3


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    # parte 1: F(b) - F(a)
    print("r_max/R    W numérico [J/kg]   W analítico [J/kg]   fracción de GM/R")
    for k in (2, 10, 100, 1000):
        # se integra en escala logarítmica por tramos para cubrir varios órdenes
        tramos = [(R * 10 ** i, R * min(10 ** (i + 1), k)) for i in range(0, 4) if 10 ** i < k]
        num = sum(simpson(g, a, b) for a, b in tramos) if k > 10 else simpson(g, R, k * R)
        ana = GM * (1 / R - 1 / (k * R))
        prueba(abs(num - ana) / ana < 1e-9, f"F(b)-F(a) con k = {k}")
        print(f"{k:7d}   {num:17.6e}   {ana:17.6e}   {ana/(GM/R):10.4f}")
    # parte 2: derivada de la función acumulada
    G = lambda x: simpson(g, R, x)
    x0, h = 2 * R, 1e-5 * R
    dG = (G(x0 + h) - G(x0 - h)) / (2 * h)
    prueba(abs(dG - g(x0)) / g(x0) < 1e-8, "G' = g")
    print(f"\nG'(2R) = {dG:.8f} m/s2;  g(2R) = {g(x0):.8f} m/s2")
    # valor medio de g sobre [R, 2R]
    media = simpson(g, R, 2 * R) / R
    prueba(abs(media - g(R) / 2) / g(R) < 1e-9, "valor medio = g(R)/2")
    print(f"Valor medio de g entre R y 2R = {media:.6f} m/s2 = g(R)/2 = {g(R)/2:.6f}")
    # escape
    e_esc = GM / R
    v_nom = math.sqrt(2 * e_esc)
    v_med = math.sqrt(2 * GM / R_MEDIO)
    print(f"\nEnergía de escape GM/R = {e_esc:.5e} J/kg")
    print(f"v_esc (R nominal ecuatorial)  = {v_nom:.2f} m/s")
    print(f"v_esc (R medio 6371.000 km)   = {v_med:.2f} m/s;  NASA = {V_ESC_NASA:.0f} m/s;  dif. = {(v_med/V_ESC_NASA-1):+.2e}")
    prueba(abs(v_med / V_ESC_NASA - 1) < 1e-3, "v_esc contra NASA")
    # órbita circular baja
    r_leo = R + 4.0e5
    vc = math.sqrt(GM / r_leo)
    ve = math.sqrt(2) * vc
    print(f"\nA 400 km: v_circular = {vc:.1f} m/s; v_escape = {ve:.1f} m/s; Delta v para escapar = {ve-vc:.1f} m/s")
    # el teorema exige continuidad: 1/x^2 en [-1, 1]
    print("Aviso: int_-1^1 dx/x^2 NO es [-1/x] = -2 (el integrando no es continuo en 0).")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
