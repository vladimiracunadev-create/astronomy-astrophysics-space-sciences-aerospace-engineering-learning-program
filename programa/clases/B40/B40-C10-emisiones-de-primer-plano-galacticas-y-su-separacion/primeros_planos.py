#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C10: primeros planos galacticos y combinacion lineal interna (ILC) en un cielo sintetico.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): h = 6,62607015e-34 J s, k_B = 1,380649e-23 J/K. Del resumen de Planck 2018 IV (arXiv:1807.06208, solo resumen, consultado el
2026-11-09): indice espectral medio del polvo polarizado beta_d = 1,55 +- 0,05 y del sincrotron polarizado beta_s = -3,1 +- 0,1; ese articulo usa Commander, NILC, SEVEM y SMICA (no se leyo su
metodologia). Son ILUSTRATIVOS: la temperatura del polvo T_d = 19,6 K, las amplitudes (CMB 100 uK_CMB; sincrotron 1500 a 30 GHz y polvo 1000 a 353 GHz, como una region cercana al plano), los ruidos por canal, las siete frecuencias
(30 a 353 GHz, elegidas por analogia con las bandas de Planck, no tomadas de una tabla) y el cielo de 40 000 pixeles independientes (semilla 20261109).
Modelo: la senal por canal es CMB (espectro plano en uK_CMB) + sincrotron (ley de potencias en temperatura RJ, convertida) + polvo (cuerpo gris modificado nu^beta B_nu(T_d), convertido con dB/dT)
+ ruido; la ILC usa pesos w = C^-1 a / (a^T C^-1 a) con a = (1,...,1), que minimizan la varianza con suma de pesos 1.
Supuestos: pixeles independientes, componentes sin correlacion entre si ni con el CMB. Validez: ilustrativa; el CMB real y los primeros planos tienen correlacion espacial y entre componentes.
Tolerancia: suma de pesos = 1 a 1e-12; pesos empiricos frente a los exactos a 0,12 (la covarianza empirica con tres componentes casi degeneradas es ruidosa) ; rms residual simulado entre 1 y 1,15 veces el teorico (el sesgo ILC de la muestra finita lo aumenta).
"""
from __future__ import annotations
import math, platform, random, sys

H = 6.62607015e-34
KB = 1.380649e-23
T0 = 2.7255
FREQ = [30, 44, 70, 100, 143, 217, 353]
SIG_N = [8.0, 8.0, 6.0, 3.0, 2.5, 4.0, 12.0]       # uK_CMB por pixel, ilustrativo
S_CMB, S_SYN, S_DUST = 100.0, 1500.0, 1000.0
BETA_S, BETA_D, TD = -3.1, 1.55, 19.6

def x_of(nu_ghz, t=T0):
    return H * nu_ghz * 1e9 / (KB * t)

def rj_a_cmb(nu):            # factor K_RJ -> K_CMB
    x = x_of(nu)
    return (math.exp(x) - 1) ** 2 / (x * x * math.exp(x))

def planck(nu, t):
    x = H * nu * 1e9 / (KB * t)
    return 2 * H * (nu * 1e9) ** 3 / 299792458.0 ** 2 / (math.exp(x) - 1)

def dbdt(nu):
    h = 1e-4
    return (planck(nu, T0 + h) - planck(nu, T0 - h)) / (2 * h)

def sed_sync():
    r = [(nu / 30.0) ** BETA_S * rj_a_cmb(nu) for nu in FREQ]
    return [v / r[0] for v in r]                # 1 a 30 GHz

def sed_dust():
    r = [(nu / 353.0) ** BETA_D * planck(nu, TD) / dbdt(nu) for nu in FREQ]
    return [v / r[-1] for v in r]               # 1 a 353 GHz

def inv(m):
    n = len(m)
    a = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(m)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(a[r][c]))
        a[c], a[p] = a[p], a[c]
        d = a[c][c]
        a[c] = [v / d for v in a[c]]
        for r in range(n):
            if r != c:
                f = a[r][c]
                a[r] = [v - f * w for v, w in zip(a[r], a[c])]
    return [row[n:] for row in a]

def pesos(cov):
    ci = inv(cov)
    num = [sum(ci[i]) for i in range(len(cov))]
    den = sum(num)
    return [v / den for v in num]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ss, sd = sed_sync(), sed_dust()
    print(f"{'GHz':>5} {'sincrotron':>11} {'polvo':>11} {'ruido [uK]':>11}")
    for nu, a, b, n in zip(FREQ, ss, sd, SIG_N):
        print(f"{nu:5d} {a:11.4e} {b:11.4e} {n:11.1f}")
    assert 1.0 < rj_a_cmb(30) < 1.1 and rj_a_cmb(353) > 5
    m = len(FREQ)
    true = [[S_CMB ** 2 + S_SYN ** 2 * ss[i] * ss[j] + S_DUST ** 2 * sd[i] * sd[j] + (SIG_N[i] ** 2 if i == j else 0.0) for j in range(m)] for i in range(m)]
    wt = pesos(true)
    fg = [[true[i][j] - S_CMB ** 2 for j in range(m)] for i in range(m)]
    res_teo = math.sqrt(sum(wt[i] * fg[i][j] * wt[j] for i in range(m) for j in range(m)))
    rng = random.Random(20261109)
    npix = 40000
    cmb, mapas = [], []
    for _ in range(npix):
        c = rng.gauss(0, S_CMB); s = rng.gauss(0, S_SYN); d = rng.gauss(0, S_DUST)
        cmb.append(c)
        mapas.append([c + s * ss[i] + d * sd[i] + rng.gauss(0, SIG_N[i]) for i in range(m)])
    med = [sum(p[i] for p in mapas) / npix for i in range(m)]
    cov = [[sum((p[i] - med[i]) * (p[j] - med[j]) for p in mapas) / (npix - 1) for j in range(m)] for i in range(m)]
    we = pesos(cov)
    print(f"{'GHz':>5} {'peso exacto':>12} {'peso empirico':>14}")
    for nu, a, b in zip(FREQ, wt, we):
        print(f"{nu:5d} {a:12.4f} {b:14.4f}")
    suma = sum(we)
    res = math.sqrt(sum((sum(w * v for w, v in zip(we, p)) - c) ** 2 for p, c in zip(mapas, cmb)) / npix)
    res143 = math.sqrt(sum((p[4] - c) ** 2 for p, c in zip(mapas, cmb)) / npix)
    print(f"suma de pesos = {suma:.12f} ; residuo rms ILC = {res:.2f} uK ; teorico = {res_teo:.2f} uK ; solo el canal de 143 GHz = {res143:.2f} uK (rms del CMB = {S_CMB:.0f} uK)")
    assert abs(suma - 1) < 1e-12
    assert max(abs(a - b) for a, b in zip(wt, we)) < 0.12
    assert 1.0 <= res / res_teo < 1.15
    assert res < res143 / 2
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
