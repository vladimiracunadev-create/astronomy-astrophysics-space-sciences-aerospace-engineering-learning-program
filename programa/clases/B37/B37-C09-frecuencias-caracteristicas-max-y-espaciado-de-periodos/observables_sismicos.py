#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C09: Delta nu, nu_max y espaciado de periodos: relaciones de escala, inversion a masa y radio y extraccion desde frecuencias sinteticas.

Datos: constante G de NIST CODATA 2022 y valores nominales solares de la UAI 2015 B3 (GM, R, T_ef = 5772 K), consultados el 2026-11-09 (solo resumen de la UAI). Los valores solares de
referencia Delta nu_sol = 135,1 uHz y nu_max,sol = 3090 uHz son valores de referencia ADOPTADOS (ilustrativos, no consultados). Las estrellas, los ruidos (0,10 uHz) y los espaciados
(Delta Pi_1 = 80 s) son SINTETICOS; la relacion de escala de nu_max se cita solo por el resumen de Belkacem et al. (2011, arXiv:1104.0630), consultado el 2026-11-09.
Modelo: Delta nu = Delta nu_sol sqrt(M/M_sol) (R/R_sol)^-3/2 ; nu_max = nu_max,sol (M/M_sol)(R/R_sol)^-2 (T_ef/T_sol)^-1/2 ; inversion directa a M y R. Frecuencias asintoticas
nu_{n,l} = Delta nu (n + l/2 + eps) - l(l+1) D0 ; Delta nu se extrae por regresion lineal de nu_{n,0} contra n con ruido gaussiano (semilla 20261109) y se compara con el valor impuesto.
Modos g: Pi_{n,l} = Delta Pi_l (n + alpha) con Delta Pi_l = Pi_0/sqrt(l(l+1)); cociente Delta Pi_1/Delta Pi_2 = sqrt(3).
Supuestos: relaciones de escala validas para estrellas de tipo solar; asintotica de orden alto. Validez: orientativa.
Tolerancia: inversion exacta a 1e-12; Delta nu extraido dentro de 3 sigma del valor impuesto; Delta nu / sqrt(GM/R^3) casi constante entre estrellas sinteticas (dentro de 1e-12).
"""
from __future__ import annotations
import math, platform, random, sys

G = 6.67430e-11
GM_SOL, R_SOL, TEF_SOL = 1.3271244e20, 6.957e8, 5772.0
DNU_SOL, NUMAX_SOL = 135.1, 3090.0  # uHz, adoptados


def dnu(M, R):
    return DNU_SOL * math.sqrt(M) * R**-1.5


def numax(M, R, Teff):
    return NUMAX_SOL * M * R**-2 * (Teff / TEF_SOL) ** -0.5


def invertir(dn, nm, Teff):
    # R = (numax/numax_sol)(dnu/dnu_sol)^-2 (T/Tsol)^1/2 ; M = (numax/numax_sol)^3 (dnu/dnu_sol)^-4 (T/Tsol)^3/2
    x, y = nm / NUMAX_SOL, dn / DNU_SOL
    th = Teff / TEF_SOL
    return x**3 * y**-4 * th**1.5, x * y**-2 * th**0.5


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'M':>5} {'R':>5} {'T_ef':>6} {'dnu [uHz]':>10} {'numax [uHz]':>12} {'M inv':>7} {'R inv':>7} {'dnu/nu_din':>11}")
    estrellas = ((1.0, 1.0, 5772.0), (1.2, 1.5, 6200.0), (0.9, 0.85, 5300.0), (1.3, 3.0, 5000.0))
    cs = []
    for M, R, T in estrellas:
        d, n = dnu(M, R), numax(M, R, T)
        Mi, Ri = invertir(d, n, T)
        nu_din = math.sqrt(GM_SOL * M / (R_SOL * R) ** 3) / (2 * math.pi) * 1e6
        cs.append(d / nu_din)
        print(f"{M:5.2f} {R:5.2f} {T:6.0f} {d:10.3f} {n:12.2f} {Mi:7.3f} {Ri:7.3f} {d / nu_din:11.4f}")
        assert abs(Mi - M) < 1e-12 and abs(Ri - R) < 1e-12
    assert max(cs) - min(cs) < 1e-12
    print(f"nu_dinamica sol = sqrt(GM/R^3)/(2 pi) = {math.sqrt(GM_SOL / R_SOL**3) / (2 * math.pi) * 1e6:.2f} uHz ; razon dnu/nu_din = {cs[0]:.4f} (constante por la escala)")
    # extraccion de Delta nu desde frecuencias sinteticas (estrella 2)
    M, R, T = estrellas[1]
    d0 = dnu(M, R)
    eps, D0 = 1.4, 0.8
    rng = random.Random(20261109)
    nus, ns = [], []
    nmax = numax(M, R, T)
    n0 = int(nmax / d0)
    for n in range(n0 - 4, n0 + 5):
        nus.append(d0 * (n + eps) + rng.gauss(0, 0.10))
        ns.append(n)
    nm_ = sum(ns) / len(ns)
    sxx = sum((n - nm_) ** 2 for n in ns)
    pend = sum((n - nm_) * (v - sum(nus) / len(nus)) for n, v in zip(ns, nus)) / sxx
    sig = 0.10 / math.sqrt(sxx)
    print(f"radiales n = {ns[0]}..{ns[-1]}: Delta nu extraido = {pend:.4f} +/- {sig:.4f} uHz ; impuesto = {d0:.4f} uHz ; desviacion = {(pend - d0) / sig:.2f} sigma")
    assert abs(pend - d0) < 3 * sig
    # propagacion a M y R con 2 % en numax y 0,5 % en dnu (1 % en T no entra)
    sM = math.sqrt((3 * 0.02) ** 2 + (4 * 0.005) ** 2)
    sR = math.sqrt((0.02) ** 2 + (2 * 0.005) ** 2)
    print(f"incertidumbres relativas: sigma(M)/M = {sM * 100:.2f} % ; sigma(R)/R = {sR * 100:.2f} % (2 % en numax y 0,5 % en dnu, sin T_ef)")
    # espaciado de periodos de modos g
    Pi0 = 80.0 * math.sqrt(2)  # s, de modo que Delta Pi_1 = 80 s
    dP1, dP2 = Pi0 / math.sqrt(2), Pi0 / math.sqrt(6)
    print(f"Delta Pi_1 = {dP1:.3f} s ; Delta Pi_2 = {dP2:.3f} s ; cociente = {dP1 / dP2:.4f} (sqrt 3 = {math.sqrt(3):.4f})")
    assert abs(dP1 / dP2 - math.sqrt(3)) < 1e-12
    # regresion lineal de periodos de l = 1 con ruido de 0,2 s
    ps = [dP1 * (n + 0.25) + rng.gauss(0, 0.2) for n in range(20, 40)]
    ns2 = list(range(20, 40))
    m2 = sum(ns2) / 20
    sxx2 = sum((n - m2) ** 2 for n in ns2)
    p2 = sum((n - m2) * (v - sum(ps) / 20) for n, v in zip(ns2, ps)) / sxx2
    s2 = 0.2 / math.sqrt(sxx2)
    print(f"regresion de 20 periodos: Delta Pi_1 = {p2:.3f} +/- {s2:.3f} s (impuesto 80,000)")
    assert abs(p2 - 80.0) < 3 * s2
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
