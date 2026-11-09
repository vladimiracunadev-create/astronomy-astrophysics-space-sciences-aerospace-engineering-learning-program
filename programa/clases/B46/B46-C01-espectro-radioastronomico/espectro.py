#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C01: ley de Planck, aproximacion de Rayleigh-Jeans y temperatura de brillo.

Datos: h, k y c de NIST CODATA 2022 (tabla allascii.txt, consultada 2026-11-09). Las temperaturas y frecuencias de la tabla
(10 K; 1,4 a 1000 GHz) y el valor 2,7255 K para el fondo cosmico son ILUSTRATIVOS (este ultimo no se consulto en esta clase).
Modelo: B_nu(T) = 2 h nu^3 / c^2 / (exp(h nu / k T) - 1); T_B de Rayleigh-Jeans = B c^2 / (2 k nu^2); T_B de Planck inversa.
Supuestos: cuerpo negro, sin polarizacion ni absorcion. Validez: orientativa.
Tolerancia: error relativo de la aproximacion RJ igual a x/2 dentro del 1 % para x <= 0,01; inversion exacta a 1e-9.
"""
from __future__ import annotations
import math, platform
H, K, C = 6.62607015e-34, 1.380649e-23, 299792458.0

def planck(nu, T):
    return 2 * H * nu ** 3 / C ** 2 / math.expm1(H * nu / (K * T))

def rj(nu, T):
    return 2 * K * T * nu ** 2 / C ** 2

def tb_rj(B, nu):
    return B * C ** 2 / (2 * K * nu ** 2)

def tb_planck(B, nu):
    return H * nu / K / math.log1p(2 * H * nu ** 3 / C ** 2 / B)

def calc():
    T = 10.0
    filas = []
    for nu in (1.4e9, 10e9, 100e9, 1000e9):
        x = H * nu / (K * T)
        b = planck(nu, T)
        filas.append(dict(nu=nu, x=x, err=rj(nu, T) / b - 1, tbrj=tb_rj(b, nu), tbp=tb_planck(b, nu)))
    cmb = {}
    for nu in (1.4e9, 100e9):
        b = planck(nu, 2.7255)
        cmb[nu] = (tb_rj(b, nu), tb_planck(b, nu))
    return dict(filas=filas, cmb=cmb, lam21=C / 1.420405751768e9, wien=5.878925757e10 * 10.0)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'nu [GHz]':>9} {'x=h nu/kT':>10} {'RJ/Planck-1':>12} {'T_B RJ [K]':>11} {'T_B Planck [K]':>15}")
    for f in r["filas"]:
        print(f"{f['nu']/1e9:9.1f} {f['x']:10.5f} {f['err']:12.5f} {f['tbrj']:11.4f} {f['tbp']:15.6f}")
    for nu, (a, b) in r["cmb"].items():
        print(f"fondo de 2.7255 K a {nu/1e9:.1f} GHz: T_B(RJ) = {a:.4f} K ; T_B(Planck) = {b:.6f} K")
    print(f"lambda(1420.405751768 MHz) = {r['lam21']*100:.3f} cm ; pico de B_nu a 10 K en {r['wien']/1e9:.1f} GHz")
    f0 = r["filas"][0]
    assert abs(f0["err"] / (f0["x"] / 2) - 1) < 0.01
    for f in r["filas"]:
        assert abs(f["tbp"] - 10.0) < 1e-9
    assert r["filas"][-1]["err"] > 4
    assert abs(r["lam21"] * 100 - 21.106) < 0.001
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
