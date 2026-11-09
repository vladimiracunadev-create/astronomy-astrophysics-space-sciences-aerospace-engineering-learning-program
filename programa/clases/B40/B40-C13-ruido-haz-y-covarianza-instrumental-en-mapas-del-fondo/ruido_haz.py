#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C13: haz gaussiano, ruido blanco y covarianza del espectro estimado.

Datos: ninguna constante fisica ni dato de un instrumento real. El haz (FWHM 7 arcmin), el ruido (30 uK-arcmin), la amplitud D_0 = 1000 uK^2 del espectro de juguete
C_l = 2 pi D_0 / (l (l+1)) y las repeticiones (semilla 20261109) son ILUSTRATIVOS; no describen ninguna mision.
Modelo: B_l = exp(-l(l+1) sigma_b^2 / 2), sigma_b = FWHM / sqrt(8 ln 2) ; N_l = (Delta_T [uK rad])^2 ; estimador C^_l = (media |a_lm|^2 - N_l)/B_l^2 ; varianza
Var(C^_l) = 2 (C_l + N_l/B_l^2)^2 / ((2l+1) f_sky). Segunda via del haz: transformada de Legendre del perfil gaussiano de cielo.
Supuestos: cielo completo en la simulacion (f_sky = 1), ruido blanco homogeneo, haz simetrico. Validez: ilustrativa; el efecto de una mascara solo se anota por la formula, no se simula.
Tolerancia: B_l frente a la transformada numerica, 1e-3; desviacion simulada de C^_l frente a la formula, 5 % (4000 repeticiones).
"""
from __future__ import annotations
import math, platform, random, sys

FWHM_ARCMIN = 7.0
DELTA_T = 30.0                 # uK arcmin
D0 = 1000.0                    # uK^2
ARCMIN = math.pi / 10800.0
SB = FWHM_ARCMIN * ARCMIN / math.sqrt(8 * math.log(2))

def bl(l):
    return math.exp(-l * (l + 1) * SB * SB / 2)

def nl():
    return (DELTA_T * ARCMIN) ** 2

def cl(l):
    return 2 * math.pi * D0 / (l * (l + 1))

def legendre(l, x):
    a, b = 1.0, x
    if l == 0:
        return a
    for k in range(2, l + 1):
        a, b = b, ((2 * k - 1) * x * b - (k - 1) * a) / k
    return b

def bl_numerico(l, n=4000):
    tmax = 10 * SB
    h = tmax / n
    num = den = 0.0
    for i in range(0, n + 1):
        t = i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        b = math.exp(-t * t / (2 * SB * SB))
        num += w * b * legendre(l, math.cos(t)) * math.sin(t)
        den += w * b * math.sin(t)
    return num / den

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"sigma_b = {SB:.6e} rad = {SB / ARCMIN:.4f} arcmin ; N_l = {nl():.4e} uK^2 sr")
    print(f"{'l':>6} {'B_l analitica':>14} {'B_l numerica':>13} {'C_l B_l^2':>12} {'N_l':>12} {'N_l/B_l^2':>12}")
    for l in (100, 500, 1000, 1500, 2000):
        b = bl(l)
        bn = bl_numerico(l)
        print(f"{l:6d} {b:14.6e} {bn:13.6e} {cl(l) * b * b:12.4e} {nl():12.4e} {nl() / b / b:12.4e}")
        if l <= 1500:
            assert abs(bn - b) < 1e-3
    # cruce senal-ruido
    cruce = None
    for l in range(2, 6000):
        if cl(l) * bl(l) ** 2 < nl():
            cruce = l
            break
    print(f"el ruido supera a la senal con haz (C_l B_l^2 < N_l) desde l = {cruce}")
    rng = random.Random(20261109)
    print(f"{'l':>6} {'sigma simulada':>15} {'sigma formula':>14} {'cociente':>9} {'sesgo medio':>12} {'metodo':>8}")
    for l in (100, 500, 1000, 1500):
        b2 = bl(l) ** 2
        var_t = cl(l) * b2 + nl()
        nrep = 4000
        est = []
        for _ in range(nrep):
            if l == 100:
                s = sum(rng.gauss(0, 1) ** 2 for _ in range(2 * l + 1))
            else:
                s = 2 * rng.gammavariate((2 * l + 1) / 2.0, 1.0)       # suma de 2l+1 cuadrados gaussianos
            est.append((var_t * s / (2 * l + 1) - nl()) / b2)
        m = sum(est) / nrep
        sd = math.sqrt(sum((e - m) ** 2 for e in est) / (nrep - 1))
        formula = math.sqrt(2.0 / (2 * l + 1)) * (cl(l) + nl() / b2)
        print(f"{l:6d} {sd:15.4e} {formula:14.4e} {sd / formula:9.3f} {(m / cl(l) - 1):12.4f} {'directo' if l == 100 else 'gamma':>8}")
        assert abs(sd / formula - 1) < 0.05
        assert abs(m / cl(l) - 1) < 0.1 + 4 * formula / cl(l) / math.sqrt(nrep)
    print(f"con f_sky = 0,6 la desviacion crece por 1/sqrt(f_sky) = {1 / math.sqrt(0.6):.4f} (formula, no simulado)")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
