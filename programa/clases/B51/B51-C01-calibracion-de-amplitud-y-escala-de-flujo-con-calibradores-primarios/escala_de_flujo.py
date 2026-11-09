#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C01: escala de flujo y bootstrap desde un calibrador primario hasta una fuente secundaria.

Datos: constantes de NIST CODATA 2022 (k_B y c, exactas; consultadas el 2026-11-09). El calibrador primario (10,0 Jy a 1,4 GHz, indice espectral -0,7), la fuente secundaria
(2,50 Jy), las ganancias de 8 antenas y el ruido son SINTETICOS e ILUSTRATIVOS; no son valores de ninguna escala publicada.
Modelo: |V_ij| = g_i g_j S + ruido. Con el primario se resuelven las ganancias de amplitud por minimos cuadrados en logaritmos; con ellas se escala la fuente secundaria (bootstrap).
Segunda via: caso sin ruido (analitico: recuperacion exacta) y Monte Carlo con semilla 20261109. Temperatura de brillo de una fuente gaussiana por Rayleigh-Jeans y vuelta.
Supuestos: ganancias constantes entre los dos barridos, amplitud pura (sin fase), ruido gaussiano en la amplitud. Validez: ilustrativa.
Tolerancia: recuperacion sin ruido 1e-9 relativo; sesgo Monte Carlo menor que 3 errores estandar; ida y vuelta de T_b 1e-12.
"""
from __future__ import annotations
import math, platform, random, sys

KB = 1.380649e-23      # J/K, exacta (NIST CODATA 2022)
C = 299792458.0        # m/s, exacta
JY = 1e-26             # W m-2 Hz-1, definicion

def solve(a, b):
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[p] = m[p], m[i]
        for r in range(i + 1, n):
            f = m[r][i] / m[i][i]
            for c in range(i, n + 1):
                m[r][c] -= f * m[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x

def gains_from_amplitudes(n, amps, s_cal):
    ata = [[0.0] * n for _ in range(n)]
    atb = [0.0] * n
    for (i, j), a in amps.items():
        y = math.log(a / s_cal)
        atb[i] += y; atb[j] += y
        ata[i][i] += 1; ata[j][j] += 1; ata[i][j] += 1; ata[j][i] += 1
    return [math.exp(v) for v in solve(ata, atb)]

def trial(rng, g, s_p, s_s, sig, n):
    base = [(i, j) for i in range(n) for j in range(i + 1, n)]
    ap = {b: g[b[0]] * g[b[1]] * s_p + rng.gauss(0, sig) for b in base}
    asec = {b: g[b[0]] * g[b[1]] * s_s + rng.gauss(0, sig) for b in base}
    gh = gains_from_amplitudes(n, ap, s_p)
    return sum(asec[b] / (gh[b[0]] * gh[b[1]]) for b in base) / len(base)

def compute():
    n, s_p, s_s, sig = 8, 10.0, 2.5, 0.05
    rng = random.Random(20261109)
    g = [math.exp(rng.gauss(0, 0.1)) for _ in range(n)]
    R = dict(n=n, s_p=s_s * 0 + s_p, s_s=s_s, sig=sig, nbase=n * (n - 1) // 2)
    R["est0"] = trial(rng, g, s_p, s_s, 0.0, n)
    ests = [trial(rng, g, s_p, s_s, sig, n) for _ in range(2000)]
    mu = sum(ests) / len(ests)
    sd = math.sqrt(sum((e - mu) ** 2 for e in ests) / (len(ests) - 1))
    R.update(mu=mu, sd=sd, se=sd / math.sqrt(len(ests)), ntr=len(ests))
    alfa, nu0 = -0.7, 1.4
    R["ley"] = [(nu, s_p * (nu / nu0) ** alfa) for nu in (1.4, 2.0, 5.0)]
    nu, fwhm = 1.4e9, math.radians(1 / 3600)
    omega = math.pi * fwhm ** 2 / (4 * math.log(2))
    tb = s_p * JY * C ** 2 / (2 * KB * nu ** 2 * omega)
    R.update(omega=omega, tb=tb, s_back=2 * KB * nu ** 2 * omega * tb / C ** 2 / JY)
    R["dbl"] = s_p * (2.8 / nu0) ** alfa - s_p * 2 ** alfa
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"sin ruido: S_secundaria recuperada = {R['est0']:.9f} Jy (verdadera {R['s_s']})")
    assert abs(R["est0"] - R["s_s"]) / R["s_s"] < 1e-9
    print(f"Monte Carlo ({R['ntr']} ensayos, ruido {R['sig']} Jy por base): media = {R['mu']:.4f} Jy, desviacion = {R['sd']:.4f} Jy ({100 * R['sd'] / R['s_s']:.2f} %), error estandar = {R['se']:.4f} Jy")
    print(f"sesgo = {R['mu'] - R['s_s']:+.4f} Jy = {(R['mu'] - R['s_s']) / R['se']:+.2f} errores estandar")
    assert abs(R["mu"] - R["s_s"]) < 3 * R["se"] + 0.004
    print("S(nu) del primario con indice -0,7:")
    for nu, s in R["ley"]:
        print(f"  nu = {nu:.1f} GHz: S = {s:.4f} Jy")
    assert abs(R["dbl"]) < 1e-12
    print(f"Omega = {R['omega']:.4e} sr ; T_b (FWHM 1 arcsec, 10 Jy, 1,4 GHz) = {R['tb']:.4e} K ; S de vuelta = {R['s_back']:.6f} Jy")
    assert abs(R["s_back"] - R["s_p"]) / R["s_p"] < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
