#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B38-C01: funcion de luminosidad sintetica y estimador 1/Vmax.

Datos: M_bol,sol = 4,74 (convencion de uso comun; la resolucion de la UAI que la fija no se consulto). La funcion inicial de masa (Salpeter, indice 2,35),
la relacion masa-luminosidad L ~ M^3,5, el radio de 1000 pc, el limite m = 10 y la semilla 20261109 son ILUSTRATIVOS (sinteticos); no se usa ningun catalogo.
Modelo: estrellas con densidad uniforme en una esfera; M_bol = 4,74 - 2,5 log10(L/Lsol); d_max = 10^((m_lim - M + 5)/5) pc; V_max = 4/3 pi min(d_max, R)^3.
Phi_j = sum(1/V_max)/dM en cada intervalo de magnitud; el valor verdadero se obtiene de forma analitica (dos vias independientes).
Supuestos: sin extincion, densidad uniforme, estrellas aisladas. Validez: ilustrativa.
Tolerancia: el cociente 1/Vmax / verdadero debe estar entre 0,9 y 1,1 en los intervalos con mas de 200 estrellas; el recuento crudo debe estar sesgado.
"""
from __future__ import annotations
import math, platform, random, sys

MBOL_SOL = 4.74
ALPHA = 2.35
MMIN, MMAX = 0.5, 20.0
R_PC = 1000.0
M_LIM = 10.0
N = 400000

def mbol(m):
    return MBOL_SOL - 2.5 * 3.5 * math.log10(m)

def masa_de_mbol(mb):
    return 10 ** ((MBOL_SOL - mb) / 8.75)

def sample_mass(rng):
    a = 1 - ALPHA
    u = rng.random()
    return (MMIN ** a + u * (MMAX ** a - MMIN ** a)) ** (1 / a)

def frac_verdadera(m1, m2):
    a = 1 - ALPHA
    return (m2 ** a - m1 ** a) / (MMAX ** a - MMIN ** a)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    v_total = 4 / 3 * math.pi * R_PC ** 3
    dens = N / v_total
    edges = [mbol(MMAX) + 1.5 * k for k in range(0, 10)]
    ncrudo = [0] * 9
    suma_w = [0.0] * 9
    nobs = 0
    for _ in range(N):
        m = sample_mass(rng)
        mb = mbol(m)
        d = R_PC * rng.random() ** (1 / 3)
        mag_ap = mb + 5 * math.log10(d / 10.0) if d > 0 else -99
        if mag_ap > M_LIM:
            continue
        nobs += 1
        j = int((mb - edges[0]) // 1.5)
        if not (0 <= j < 9):
            continue
        dmax = 10 ** ((M_LIM - mb + 5) / 5)
        vmax = 4 / 3 * math.pi * min(dmax, R_PC) ** 3
        ncrudo[j] += 1
        suma_w[j] += 1 / vmax
    def fv(j):
        hi = min(masa_de_mbol(edges[j]), MMAX)
        lo = max(masa_de_mbol(edges[j + 1]), MMIN)
        return frac_verdadera(lo, hi)
    print(f"estrellas generadas {N}, observadas {nobs} ({nobs / N:.4f})")
    print(f"{'M_bol':>12} {'n_obs':>7} {'crudo/verd':>11} {'1/Vmax/verd':>12}")
    ok = 0
    for j in range(9):
        mb1, mb2 = edges[j], edges[j + 1]
        verd_n = N * fv(j)
        verd_phi = verd_n / v_total
        est_phi = suma_w[j]
        crudo = ncrudo[j] / v_total
        r_crudo = ncrudo[j] / (verd_n) if verd_n > 0 else float("nan")
        r_est = est_phi / verd_phi if verd_phi > 0 else float("nan")
        print(f"{mb1:5.1f}..{mb2:5.1f} {ncrudo[j]:7d} {r_crudo:11.4f} {r_est:12.4f}")
        if ncrudo[j] > 200:
            assert 0.9 < r_est < 1.1, (j, r_est)
            ok += 1
    assert ok >= 5
    # el recuento crudo esta sesgado hacia lo brillante: la fraccion observada crece con la luminosidad
    frac_obs_brillante = ncrudo[0] / (N * fv(0))
    frac_obs_debil = ncrudo[8] / (N * fv(8))
    print(f"fraccion observada: brillante {frac_obs_brillante:.4f}, debil {frac_obs_debil:.4f}")
    assert frac_obs_brillante > frac_obs_debil
    print(f"densidad media {dens * 1e9:.4f} estrellas por kpc^3 (n = {dens:.3e} pc^-3)")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
