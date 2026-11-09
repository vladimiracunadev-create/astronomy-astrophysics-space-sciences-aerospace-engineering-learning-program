#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C04: red de difraccion, dispersion angular y poder de resolucion.

Datos: ninguna constante externa; red de 600 l/mm, 100 mm de ancho y angulo de incidencia 8,627 grados (Littrow para 500 nm) son valores ILUSTRATIVOS, no de un catalogo.
Modelo: ecuacion de la red m lambda = d (sin alpha + sin beta); dispersion d beta/d lambda = m/(d cos beta); R = m N; patron de N rendijas por suma de fasores.
Supuestos: red ideal de rendijas, aproximacion escalar, sin perdidas ni fantasmas. Validez: orden de magnitud del ancho de linea; no modela la eficiencia de blaze.
Tolerancia: dispersion numerica frente a analitica a 1e-6; caida entre dos lineas separadas lambda/(mN) frente a 8/pi^2 = 0,8106 a 0,01 (N = 400).
"""
from __future__ import annotations
import math, platform, sys

D = 1e-3 / 600
ALPHA = math.asin(500e-9 / (2 * D))
NR = 600 * 100


def beta(lam, m=1, alpha=ALPHA):
    return math.asin(m * lam / D - math.sin(alpha))


def intensidad(phi, N):
    s = math.sin(phi / 2)
    if abs(s) < 1e-12:
        return 1.0
    return (math.sin(N * phi / 2) / (N * s)) ** 2


def calcular():
    r = {}
    r["alpha"] = math.degrees(ALPHA)
    r["d_nm"] = D * 1e9
    r["betas"] = [(l, math.degrees(beta(l * 1e-9))) for l in (400, 450, 500, 550, 600)]
    lam = 500e-9
    h = 1e-12
    num = (beta(lam + h) - beta(lam - h)) / (2 * h)
    ana = 1 / (D * math.cos(beta(lam)))
    r["disp_num"] = num
    r["disp_ana"] = ana
    r["disp_mrad_nm"] = ana * 1e-9 * 1e3
    r["R1"] = NR
    r["R2"] = 2 * NR
    r["dlam_nm"] = lam / NR * 1e9
    r["orden_max"] = int((D / lam) * (1 + math.sin(ALPHA)))
    # dos lineas separadas lambda/(mN) con N = 400 rendijas: suma en el punto medio
    N = 400
    l1 = 500e-9
    l2 = l1 * (1 + 1 / N)
    b1, b2 = beta(l1), beta(l2)
    bm = 0.5 * (b1 + b2)

    def fase(l, b):
        return 2 * math.pi * D * (math.sin(ALPHA) + math.sin(b)) / l

    I1 = intensidad(fase(l1, bm), N)
    I2 = intensidad(fase(l2, bm), N)
    r["valle"] = I1 + I2
    r["valle_ref"] = 8 / math.pi ** 2
    # separadas la mitad: sin resolver (sin valle)
    l3 = l1 * (1 + 0.5 / N)
    b3 = beta(l3)
    bm3 = 0.5 * (b1 + b3)
    r["valle_mitad"] = intensidad(fase(l1, bm3), N) + intensidad(fase(l3, bm3), N)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"d = {r['d_nm']:.2f} nm ; alpha = {r['alpha']:.3f} grados ; orden maximo propagante para 500 nm = {r['orden_max']}")
    for l, b in r["betas"]:
        print(f"lambda {l} nm -> beta = {b:.3f} grados")
    print(f"dispersion angular numerica {r['disp_num']:.6e} rad/m ; analitica {r['disp_ana']:.6e} rad/m ({r['disp_mrad_nm']:.4f} mrad/nm)")
    print(f"R (orden 1) = {r['R1']} ; R (orden 2) = {r['R2']} ; delta lambda a 500 nm = {r['dlam_nm']:.5f} nm")
    print(f"suma de dos lineas en el punto medio: separacion lambda/(mN) -> {r['valle']:.4f} (8/pi^2 = {r['valle_ref']:.4f}) ; mitad -> {r['valle_mitad']:.4f}")
    assert abs(r["disp_num"] / r["disp_ana"] - 1) < 1e-6
    assert abs(r["valle"] - r["valle_ref"]) < 0.01
    assert r["valle_mitad"] > 1.0
    assert r["orden_max"] >= 2
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
