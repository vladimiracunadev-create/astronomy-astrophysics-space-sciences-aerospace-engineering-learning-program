#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C24: recubrimientos antirreflectantes de capas multiples por matrices de transferencia.

Datos: ILUSTRATIVOS. Indices constantes (sin dispersion): aire 1,00, sustrato 1,52, capa de bajo indice 1,38 (tipo fluoruro de magnesio), capa intermedia 1,70 y capa de alto indice 2,10 (valores de orden de magnitud
no consultados en una hoja de fabricante); longitud de diseno 550 nm. Sin datos medidos.
Modelo: matriz caracteristica de cada capa M = [[cos d, i sin d/n],[i n sin d, cos d]], d = 2 pi n t/lambda; incidencia normal; R = |(1 - Y)/(1 + Y)|^2 con Y = C/B; T = 4 n_s/|B + C|^2.
Casos: sustrato desnudo; una capa de cuarto de onda (R_min = ((n_s - n_1^2)/(n_s + n_1^2))^2); dos capas de cuarto de onda con n_2 = n_1 sqrt(n_s) (R = 0 en lambda_0); tres capas cuarto-media-cuarto.
Verificacion independiente: formulas cerradas en lambda_0 frente a la matriz de transferencia; conservacion de la energia R + T = 1 sin absorcion.
Supuestos: capas homogeneas, sin absorcion, sin dispersion, incidencia normal. Validez: ilustrativa.
Tolerancia: cerrada frente a TMM, 1e-12; R + T - 1, 1e-12.
"""
from __future__ import annotations
import cmath, math, platform

NS = 1.52; L0 = 550.0

def RT(capas, lam, ns=NS):
    # capas: [(n, espesor nm)] de aire hacia sustrato
    B, C = 1 + 0j, complex(ns)
    for n, t in reversed(capas):
        d = 2 * math.pi * n * t / lam
        c, s = math.cos(d), math.sin(d)
        B, C = c * B + 1j * s / n * C, 1j * n * s * B + c * C
    Y = C / B
    R = abs((1 - Y) / (1 + Y)) ** 2
    T = 4 * ns / abs(B + C) ** 2
    return R, T

def qw(n): return (n, L0 / (4 * n))
def hw(n): return (n, L0 / (2 * n))

def calc():
    r = {}
    n1 = 1.38; n2 = n1 * math.sqrt(NS); nh = 2.10; nm = 1.70
    sust = []
    una = [qw(n1)]
    dos = [qw(n1), qw(n2)]
    tres = [qw(n1), hw(nh), qw(nm)]
    r["n2_V"] = n2
    r["R0_desnudo"] = RT(sust, L0)[0]
    r["R0_una"] = RT(una, L0)[0]
    r["R0_una_cerrada"] = ((NS - n1 ** 2) / (NS + n1 ** 2)) ** 2
    r["R0_dos"] = RT(dos, L0)[0]
    r["R0_tres"] = RT(tres, L0)[0]
    r["max_energia"] = max(abs(sum(RT(c, l)) - 1) for c in (sust, una, dos, tres) for l in (400, 450, 550, 650, 800))
    lams = [400 + 10 * i for i in range(31)]
    filas = []
    for l in (450, 500, 550, 600, 650, 700):
        filas.append((l, RT(sust, l)[0], RT(una, l)[0], RT(dos, l)[0], RT(tres, l)[0]))
    r["filas"] = filas
    lv = [l for l in lams if 450 <= l <= 700]
    for nm_, c in (("desnudo", sust), ("una", una), ("dos", dos), ("tres", tres)):
        r["media_" + nm_] = sum(RT(c, l)[0] for l in lv) / len(lv)
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        if k != "filas":
            print(f"{k} = {v:.6g}")
    print("lambda (nm) | desnudo | 1 capa | 2 capas | 3 capas")
    for f in r["filas"]:
        print(f"{f[0]} | {f[1]:.5f} | {f[2]:.5f} | {f[3]:.5f} | {f[4]:.5f}")
    assert abs(r["R0_una"] - r["R0_una_cerrada"]) < 1e-12
    assert r["R0_dos"] < 1e-12 and r["max_energia"] < 1e-12
    assert r["media_tres"] < r["media_una"] < r["media_desnudo"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
