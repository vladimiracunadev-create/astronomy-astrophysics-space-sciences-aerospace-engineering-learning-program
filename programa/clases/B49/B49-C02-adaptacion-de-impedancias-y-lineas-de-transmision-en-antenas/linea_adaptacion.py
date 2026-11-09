#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C02: coeficiente de reflexion, ROE, perdida por desadaptacion y transformador de cuarto de onda en una linea sin perdidas.

Datos: ninguna constante fisica. La carga de 73,08 ohm (resistencia de un dipolo de media onda calculada en B49-C01 con el valor de NIST de la impedancia del vacio, consultado el 2026-11-09), la linea de
50 ohm, la frecuencia central de 150 MHz y el factor de velocidad 0,66 son ILUSTRATIVOS; no describen ningun cable ni antena real.
Modelo: linea sin perdidas de impedancia Z0; Gamma = (ZL - Z0)/(ZL + Z0); ROE = (1 + |Gamma|)/(1 - |Gamma|); perdida por desadaptacion = -10 log10(1 - |Gamma|^2). Impedancia de entrada por dos vias
independientes: la formula con tangente y la rotacion de Gamma en la carta de Smith, Z = Z0 (1 + Gamma e^{-2 j beta l})/(1 - Gamma e^{-2 j beta l}). El patron de ondas estacionarias se muestrea
a lo largo de la linea. Transformador de cuarto de onda con Z_T = sqrt(Z0 ZL) y su ancho de banda.
Supuestos: linea sin perdidas, uniforme, modo TEM, carga independiente de la frecuencia (la antena real no lo es). Validez: banda estrecha alrededor de la frecuencia de diseno.
Tolerancia: las dos formas de la impedancia de entrada coinciden a 1e-9 relativo; ROE muestreada frente a la analitica a 1e-3; cuarto de onda adapta a |Gamma| < 1e-7 a la frecuencia central.
"""
from __future__ import annotations
import cmath, math, platform

Z0 = 50.0
C = 299792458.0


def gamma(zl, z0=Z0):
    return (zl - z0) / (zl + z0)


def roe(g):
    return (1 + abs(g)) / (1 - abs(g))


def zin_tan(zl, z0, bl):
    t = math.tan(bl)
    return z0 * (zl + 1j * z0 * t) / (z0 + 1j * zl * t)


def zin_smith(zl, z0, bl):
    g = gamma(zl, z0) * cmath.exp(-2j * bl)
    return z0 * (1 + g) / (1 - g)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'ZL (ohm)':>16} {'|Gamma|':>8} {'ROE':>8} {'RL (dB)':>8} {'perdida (dB)':>13} {'potencia reflejada %':>21}")
    for zl in (50.0, 73.08, 100.0, 25.0, 10.0, 50 + 50j, 200.0):
        g = gamma(zl)
        rl = -20 * math.log10(abs(g)) if abs(g) > 0 else float("inf")
        ml = -10 * math.log10(1 - abs(g) ** 2) + 0.0
        print(f"{str(zl):>16} {abs(g):8.4f} {roe(g):8.4f} {rl:8.3f} {ml:13.5f} {100 * abs(g) ** 2:21.3f}")
    zl = 73.08
    g = gamma(zl)
    assert abs(roe(g) - zl / Z0) < 1e-12
    print("Impedancia de entrada de una linea de 50 ohm cargada con 73,08 + j20 ohm segun la longitud electrica:")
    zc = 73.08 + 20j
    print(f"{'l/lambda':>9} {'Zin tangente':>24} {'Zin Smith':>24} {'dif relativa':>13}")
    for lr in (0.0, 0.05, 0.125, 0.25, 0.3, 0.5):
        bl = 2 * math.pi * lr
        a = zin_tan(zc, Z0, bl) if abs(math.tan(bl)) < 1e12 else None
        if lr == 0.25:
            a = Z0 ** 2 / zc
        b = zin_smith(zc, Z0, bl)
        dif = abs(a - b) / abs(b)
        print(f"{lr:9.3f} {a.real:11.4f}{a.imag:+10.4f}j {b.real:11.4f}{b.imag:+10.4f}j {dif:13.2e}")
        assert dif < 1e-9
    # patron de ondas estacionarias: |V(d)| = |1 + Gamma e^{-2 j beta d}| (d distancia a la carga)
    gc = gamma(zc)
    vals = [abs(1 + gc * cmath.exp(-2j * 2 * math.pi * (k / 2000.0))) for k in range(2001)]
    roe_m = max(vals) / min(vals)
    print(f"Carga 73,08 + j20: |Gamma| = {abs(gc):.5f} ; ROE analitica = {roe(gc):.5f} ; ROE muestreada = {roe_m:.5f}")
    assert abs(roe_m / roe(gc) - 1) < 1e-3
    # transformador de cuarto de onda
    zt = math.sqrt(Z0 * zl)
    print(f"Transformador de cuarto de onda entre 50 y 73,08 ohm: Z_T = sqrt(50 x 73,08) = {zt:.4f} ohm")
    vf = 0.66
    f0 = 150e6
    lq = vf * C / f0 / 4
    print(f"A 150 MHz con factor de velocidad {vf}: longitud electrica de cuarto de onda = {lq:.5f} m")
    print(f"{'f/f0':>6} {'|Gamma| directo':>16} {'|Gamma| con transf.':>20} {'RL con transf. (dB)':>20}")
    anchos = []
    for k in range(0, 21):
        x = 0.5 + 0.05 * k
        bl = (math.pi / 2) * x
        zi = zin_tan(zl, zt, bl) if abs(math.cos(bl)) > 1e-9 else zt ** 2 / zl
        gi = abs(gamma(zi, Z0))
        rl = -20 * math.log10(gi) if gi > 1e-15 else float("inf")
        if k % 2 == 0:
            print(f"{x:6.2f} {abs(g):16.5f} {gi:20.6f} {rl:20.3f}")
        anchos.append((x, rl))
    gcen = abs(gamma(zin_tan(zl, zt, math.pi / 2 - 1e-9), Z0))
    assert gcen < 1e-7
    # ancho de banda donde la perdida de retorno supera 20 dB (busqueda fina)
    ok = []
    for k in range(0, 4001):
        x = 0.5 + k * 0.0005
        bl = (math.pi / 2) * x
        zi = zin_tan(zl, zt, bl)
        if -20 * math.log10(abs(gamma(zi, Z0)) + 1e-300) >= 20:
            ok.append(x)
    print(f"RL >= 20 dB para f/f0 entre {min(ok):.4f} y {max(ok):.4f} (ancho fraccional {max(ok) - min(ok):.4f})")
    assert min(ok) < 1 < max(ok)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
