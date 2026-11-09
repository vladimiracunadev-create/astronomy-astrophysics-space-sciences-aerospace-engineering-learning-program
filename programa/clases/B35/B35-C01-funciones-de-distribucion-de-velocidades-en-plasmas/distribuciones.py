#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B35-C01: distribuciones de velocidad maxwelliana y kappa, sus momentos y la mala estimacion de la temperatura.

Datos: k_B y m_p (NIST CODATA 2022, tabla allascii.txt, consultados 2026-11-09). La temperatura (1e5 K) y los indices kappa (2, 3, 5, 10, 100) son ILUSTRATIVOS
(sinteticos); no representan una medicion de ninguna nave.
Modelo: distribucion maxwelliana 3D f(v) y kappa 3D f(v) = A (1 + v^2/(kappa th^2))^-(kappa+1) con th^2 = (2 kappa - 3)/kappa * kT/m (de modo que la temperatura cinetica sea T).
Los momentos se obtienen por integracion numerica (regla del trapecio en ln v) y, de forma independiente, por un muestreo Monte Carlo del caso maxwelliano (semilla 20261109).
Supuestos: plasma de protones homogeneo, sin deriva; kappa > 3/2. Validez: ilustrativa.
Tolerancia: normalizacion e integral de v^2 con error relativo < 1e-3; media de la rapidez frente a la formula analitica con error < 1 %.
"""
from __future__ import annotations
import math, platform, random, sys

K_B = 1.380649e-23
M_P = 1.67262192595e-27

def momento(f, n, a=1e-4, b=1e4, N=40000):
    """Integral de 4 pi v^(n+2) f(v) dv con trapecio uniforme en ln v (v en unidades de la rapidez termica)."""
    h = (math.log(b) - math.log(a)) / N
    s = 0.0
    for i in range(N + 1):
        v = math.exp(math.log(a) + i * h)
        w = 0.5 if i in (0, N) else 1.0
        s += w * 4 * math.pi * v ** (n + 3) * f(v)
    return s * h

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    T = 1e5
    vt = math.sqrt(K_B * T / M_P)  # rapidez termica sqrt(kT/m)
    print(f"v_t = sqrt(kT/m) = {vt/1e3:.3f} km/s para T = {T:.0e} K")
    # unidades: v en v_t. Maxwell: f = (2 pi)^(-3/2) exp(-v^2/2)
    fM = lambda v: (2 * math.pi) ** -1.5 * math.exp(-v * v / 2)
    n0 = momento(fM, 0); m2 = momento(fM, 2)
    vm_num = momento(fM, 1)
    vm_an = math.sqrt(8 / math.pi)
    print(f"Maxwell: n = {n0:.6f} ; <v^2> = {m2:.6f} (esperado 3) ; <v> = {vm_num:.6f} (analitico {vm_an:.6f})")
    assert abs(n0 - 1) < 1e-3 and abs(m2 - 3) < 3e-3 and abs(vm_num - vm_an) < 1e-3
    # Monte Carlo independiente
    rng = random.Random(20261109)
    N = 200000
    s1 = s2 = 0.0
    for _ in range(N):
        x, y, z = rng.gauss(0, 1), rng.gauss(0, 1), rng.gauss(0, 1)
        r2 = x * x + y * y + z * z
        s2 += r2; s1 += math.sqrt(r2)
    print(f"Monte Carlo (N = {N}): <v> = {s1/N:.4f} ; <v^2> = {s2/N:.4f}")
    assert abs(s1 / N - vm_an) / vm_an < 0.01 and abs(s2 / N - 3) / 3 < 0.01
    print(f"{'kappa':>6} {'n':>9} {'<v^2>/3':>9} {'f(5 vt)/fM(5 vt)':>17} {'T_ajuste/T':>11}")
    resultados = {}
    for kap in (2.0, 3.0, 5.0, 10.0, 100.0):
        th2 = (2 * kap - 3) / kap
        A = (math.gamma(kap + 1) / (kap ** 1.5 * math.gamma(kap - 0.5))) / (math.pi ** 1.5 * th2 ** 1.5)
        fK = lambda v, A=A, th2=th2, kap=kap: A * (1 + v * v / (kap * th2)) ** (-(kap + 1))
        nk = momento(fK, 0, b=1e6, N=60000)
        mk = momento(fK, 2, b=1e6, N=60000) / 3 if kap > 2.5 else float("nan")
        cola = fK(5.0) / fM(5.0)
        # temperatura de un ajuste maxwelliano que iguala el valor central: T_aj/T = (f0_M/f0_K)^(2/3)
        taj = (fM(0.0) / fK(0.0)) ** (2.0 / 3.0)
        resultados[kap] = (nk, mk, cola, taj)
        print(f"{kap:6.0f} {nk:9.5f} {mk:9.5f} {cola:17.4g} {taj:11.4f}")
    # kappa grande -> Maxwell
    assert abs(resultados[100.0][0] - 1) < 2e-3 and abs(resultados[100.0][3] - 1) < 0.02
    # normalizacion de todas
    for kap in (3.0, 5.0, 10.0):
        assert abs(resultados[kap][0] - 1) < 2e-3
    # temperatura cinetica = T (momento 2) para kappa >= 3
    for kap in (5.0, 10.0):
        assert abs(resultados[kap][1] - 1) < 5e-3
    # la cola kappa excede a la maxwelliana y crece al bajar kappa
    assert resultados[3.0][2] > resultados[5.0][2] > resultados[10.0][2] > 1
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
