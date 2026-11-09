#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B39-C03: tensores de Riemann y Ricci y curvatura escalar por diferencias finitas anidadas.

Datos: ninguna constante fisica ni dato observado. Las metricas (2-esfera de radio 2, Schwarzschild con M = 1 en unidades geometrizadas G = c = 1) y los puntos de evaluacion son
ILUSTRATIVOS; las comparaciones usan formulas cerradas.
Modelo: R^a_bcd = d_c Gamma^a_db - d_d Gamma^a_cb + Gamma^a_ce Gamma^e_db - Gamma^a_de Gamma^e_cb; Ricci R_bd = R^a_bad; R = g^bd R_bd; escalar de Kretschmann K = R_abcd R^abcd. Christoffel con paso 1e-4 y su derivada con paso 1e-3.
Supuestos: conexion de Levi-Civita; derivadas centrales. Validez: ilustrativa.
Tolerancia: R de la esfera a 1e-6; Ricci de Schwarzschild nulo a 1e-6; Kretschmann frente a 48 M^2/r^6 a 1e-6 relativo; antisimetria (cd) y primera identidad de Bianchi a 1e-8; antisimetria (ab) a 1e-5 de la componente maxima (error de diferencias finitas).
"""
from __future__ import annotations
import math, platform, itertools

def inv(m):
    n = len(m)
    a = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(m)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(a[r][i]))
        a[i], a[p] = a[p], a[i]
        d = a[i][i]
        a[i] = [v / d for v in a[i]]
        for r in range(n):
            if r != i:
                f = a[r][i]
                a[r] = [vr - f * vi for vr, vi in zip(a[r], a[i])]
    return [row[n:] for row in a]

def christoffel(g, x, h=1e-4):
    n = len(x)
    gi = inv(g(x)); dg = []
    for c in range(n):
        xp = list(x); xm = list(x); xp[c] += h; xm[c] -= h
        gp, gm = g(xp), g(xm)
        dg.append([[(gp[a][b] - gm[a][b]) / (2 * h) for b in range(n)] for a in range(n)])
    return [[[0.5 * sum(gi[d][e] * (dg[a][e][b] + dg[b][e][a] - dg[e][a][b]) for e in range(n)) for b in range(n)] for a in range(n)] for d in range(n)]

def riemann(g, x, h1=1e-4, h2=1e-3):
    """R[a][b][c][d] = R^a_bcd."""
    n = len(x)
    G = christoffel(g, x, h1)
    dG = []
    for c in range(n):
        xp = list(x); xm = list(x); xp[c] += h2; xm[c] -= h2
        Gp, Gm = christoffel(g, xp, h1), christoffel(g, xm, h1)
        dG.append([[[ (Gp[a][b][d] - Gm[a][b][d]) / (2 * h2) for d in range(n)] for b in range(n)] for a in range(n)])
    R = [[[[0.0] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a, b, c, d in itertools.product(range(n), repeat=4):
        R[a][b][c][d] = (dG[c][a][d][b] - dG[d][a][c][b]
                         + sum(G[a][c][e] * G[e][d][b] - G[a][d][e] * G[e][c][b] for e in range(n)))
    return R

def ricci(R):
    n = len(R)
    return [[sum(R[a][b][a][d] for a in range(n)) for d in range(n)] for b in range(n)]

def escalar(Ric, gi):
    n = len(Ric)
    return sum(gi[b][d] * Ric[b][d] for b in range(n) for d in range(n))

A = 2.0
def esfera(x):
    return [[A * A, 0.0], [0.0, A * A * math.sin(x[0]) ** 2]]

M = 1.0
def schw(x):
    t, r, th, ph = x
    f = 1 - 2 * M / r
    return [[-f, 0, 0, 0], [0, 1 / f, 0, 0], [0, 0, r * r, 0], [0, 0, 0, r * r * math.sin(th) ** 2]]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    x = [1.1, 0.5]
    R2 = riemann(esfera, x); Ric2 = ricci(R2); g2 = esfera(x)
    Rs = escalar(Ric2, inv(g2))
    print(f"2-esfera (a = {A}): R numerica {Rs:.8f}  cerrada 2/a^2 = {2 / A ** 2:.8f}")
    print(f"  Ricci - (R/2) g: maximo {max(abs(Ric2[i][j] - 0.5 * Rs * g2[i][j]) for i in range(2) for j in range(2)):.2e}")
    # Schwarzschild
    r = 6.0
    xs = [0.0, r, math.pi / 2, 0.0]
    R4 = riemann(schw, xs); Ric4 = ricci(R4); g4 = schw(xs); gi = inv(g4)
    ric_max = max(abs(Ric4[i][j]) for i in range(4) for j in range(4))
    print(f"Schwarzschild (M = {M}, r = {r}): maximo |R_ab| = {ric_max:.2e} (vacio: debe ser 0)")
    n = 4
    # bajar el primer indice y subir los otros para el escalar de Kretschmann
    Rl = [[[[sum(g4[a][e] * R4[e][b][c][d] for e in range(n)) for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Ru = [[[[sum(gi[b][f] * gi[c][g_] * gi[d][h_] * R4[a][f][g_][h_] for f in range(n) for g_ in range(n) for h_ in range(n)) for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    # R_abcd R^abcd con R^abcd = g^bf g^cg g^dh R^a_fgh (a ya esta arriba)
    K = sum(Rl[a][b][c][d] * Ru[a][b][c][d] for a in range(n) for b in range(n) for c in range(n) for d in range(n))
    K_cerr = 48 * M * M / r ** 6
    print(f"Kretschmann numerico {K:.9e}  cerrado 48 M^2/r^6 = {K_cerr:.9e}")
    # simetrias
    anti = max(abs(Rl[a][b][c][d] + Rl[b][a][c][d]) for a, b, c, d in itertools.product(range(n), repeat=4))
    antic = max(abs(Rl[a][b][c][d] + Rl[a][b][d][c]) for a, b, c, d in itertools.product(range(n), repeat=4))
    bianchi1 = max(abs(Rl[a][b][c][d] + Rl[a][c][d][b] + Rl[a][d][b][c]) for a, b, c, d in itertools.product(range(n), repeat=4))
    escala = max(abs(Rl[a][b][c][d]) for a, b, c, d in itertools.product(range(n), repeat=4))
    print(f"componente covariante maxima |R_abcd| = {escala:.4f}")
    print(f"antisimetria (ab): {anti:.2e}   antisimetria (cd): {antic:.2e}   primera identidad de Bianchi: {bianchi1:.2e}")
    # componente tipica de Schwarzschild: R^t_rtr = -2M/(r^3 (1-2M/r))... se compara R_trtr = -2M/r^3
    print(f"R_trtr numerico {Rl[0][1][0][1]:.9f}  cerrado -2M/r^3 = {-2 * M / r ** 3:.9f}")
    assert abs(Rs - 2 / A ** 2) < 1e-6
    assert ric_max < 1e-6
    assert abs(K / K_cerr - 1) < 1e-6
    assert anti < 1e-5 * escala and antic < 1e-8 and bianchi1 < 1e-8
    assert abs(Rl[0][1][0][1] + 2 * M / r ** 3) < 1e-8
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
