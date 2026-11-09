#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B39-C06: descomposicion 3+1 de una metrica, curvatura extrinseca, ligadura hamiltoniana y convergencia de una evolucion.

Datos: ninguna constante fisica ni dato observado. La metrica de Schwarzschild en coordenadas de Painleve-Gullstrand con M = 1 (unidades geometrizadas G = c = 1), el radio de prueba r = 4 M y la onda de prueba son
ILUSTRATIVOS; las comparaciones usan formulas cerradas. No es un codigo de relatividad numerica ni evoluciona la ecuacion de Einstein.
Modelo: g_00 = -alpha^2 + beta_i beta^i, g_0i = beta_i, g_ij = gamma_ij; K_ij = (D_i beta_j + D_j beta_i) / (2 alpha) para una rebanada estacionaria; ligadura hamiltoniana R3 + K^2 - K_ij K^ij = 16 pi rho (= 0 en vacio). Como juguete de evolucion hiperbolica se integra phi_tt = phi_xx en [0, 2 pi) periodico con diferencias centrales de segundo orden y Runge-Kutta 4 (metodo de lineas).
Supuestos: rebanada estacionaria de vacio; onda unidimensional lineal. Validez: ilustrativa.
Tolerancia: alpha y beta frente a la formula cerrada a 1e-12; K a 1e-6 (diferencias finitas); ligadura hamiltoniana a 1e-6; orden de convergencia entre 1,9 y 2,1.
"""
from __future__ import annotations
import math, platform

M = 1.0

def pg(x):
    """Schwarzschild en Painleve-Gullstrand; coordenadas (t, r, theta, phi)."""
    t, r, th, ph = x
    b = math.sqrt(2 * M / r)
    return [[-(1 - 2 * M / r), b, 0, 0], [b, 1, 0, 0], [0, 0, r * r, 0], [0, 0, 0, r * r * math.sin(th) ** 2]]

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

def det(m):
    n = len(m)
    a = [r[:] for r in m]; d = 1.0
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(a[r][i]))
        if p != i:
            a[i], a[p] = a[p], a[i]; d = -d
        d *= a[i][i]
        for r in range(i + 1, n):
            f = a[r][i] / a[i][i]
            a[r] = [vr - f * vi for vr, vi in zip(a[r], a[i])]
    return d

def trescuatro(g4):
    gam = [[g4[i][j] for j in range(1, 4)] for i in range(1, 4)]
    beta_low = [g4[0][i] for i in range(1, 4)]
    gi = inv(gam)
    beta_up = [sum(gi[i][j] * beta_low[j] for j in range(3)) for i in range(3)]
    alpha2 = sum(beta_low[i] * beta_up[i] for i in range(3)) - g4[0][0]
    return math.sqrt(alpha2), beta_low, beta_up, gam

def christoffel(g, x, h=1e-5):
    n = len(x)
    gi = inv(g(x)); dg = []
    for c in range(n):
        xp = list(x); xm = list(x); xp[c] += h; xm[c] -= h
        gp, gm = g(xp), g(xm)
        dg.append([[(gp[a][b] - gm[a][b]) / (2 * h) for b in range(n)] for a in range(n)])
    return [[[0.5 * sum(gi[d][e] * (dg[a][e][b] + dg[b][e][a] - dg[e][a][b]) for e in range(n)) for b in range(n)] for a in range(n)] for d in range(n)]

def ricci_escalar(g, x, h1=1e-4, h2=1e-3):
    n = len(x)
    G = christoffel(g, x, h1); dG = []
    for c in range(n):
        xp = list(x); xm = list(x); xp[c] += h2; xm[c] -= h2
        Gp, Gm = christoffel(g, xp, h1), christoffel(g, xm, h1)
        dG.append([[[(Gp[a][b][d] - Gm[a][b][d]) / (2 * h2) for d in range(n)] for b in range(n)] for a in range(n)])
    gi = inv(g(x)); R = 0.0
    for b in range(n):
        for d in range(n):
            ric = sum(dG[a][a][d][b] - dG[d][a][a][b] + sum(G[a][a][e] * G[e][d][b] - G[a][d][e] * G[e][a][b] for e in range(n)) for a in range(n))
            R += gi[b][d] * ric
    return R

def onda(N, T, cfl=0.25):
    dx = 2 * math.pi / N
    nt = int(math.ceil(T / (cfl * dx))); dt = T / nt
    xs = [i * dx for i in range(N)]
    phi = [math.sin(x) + 0.5 * math.cos(2 * x) for x in xs]
    pi = [-math.cos(x) + math.sin(2 * x) for x in xs]
    def rhs(phi, pi):
        lap = [(phi[(i + 1) % N] - 2 * phi[i] + phi[i - 1]) / dx ** 2 for i in range(N)]
        return pi, lap
    for _ in range(nt):
        k1p, k1q = rhs(phi, pi)
        k2p, k2q = rhs([a + 0.5 * dt * b for a, b in zip(phi, k1p)], [a + 0.5 * dt * b for a, b in zip(pi, k1q)])
        k3p, k3q = rhs([a + 0.5 * dt * b for a, b in zip(phi, k2p)], [a + 0.5 * dt * b for a, b in zip(pi, k2q)])
        k4p, k4q = rhs([a + dt * b for a, b in zip(phi, k3p)], [a + dt * b for a, b in zip(pi, k3q)])
        phi = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(phi, k1p, k2p, k3p, k4p)]
        pi = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(pi, k1q, k2q, k3q, k4q)]
    ex = [math.sin(x - T) + 0.5 * math.cos(2 * (x - T)) for x in xs]
    err = math.sqrt(sum((a - b) ** 2 for a, b in zip(phi, ex)) * dx)
    return err

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = 4.0 * M
    x = [0.0, r, math.pi / 2, 0.3]
    g4 = pg(x)
    alpha, bl, bu, gam = trescuatro(g4)
    b_cerr = math.sqrt(2 * M / r)
    print(f"alpha = {alpha:.12f} (cerrado 1)   beta^r = {bu[0]:.12f} (cerrado sqrt(2M/r) = {b_cerr:.12f})")
    dg = det(g4); dgam = det(gam)
    print(f"det g = {dg:.9f}   -alpha^2 det gamma = {-alpha ** 2 * dgam:.9f}")
    # curvatura extrinseca: K_ij = (D_i beta_j + D_j beta_i) / (2 alpha) en coordenadas esfericas (r, theta, phi)
    gam_f = lambda y: [[1.0, 0, 0], [0, y[0] ** 2, 0], [0, 0, y[0] ** 2 * math.sin(y[1]) ** 2]]
    y = [r, math.pi / 2, 0.3]
    beta_f = lambda y: [math.sqrt(2 * M / y[0]), 0.0, 0.0]  # beta_i (covariante: gamma_rr = 1)
    Gm = christoffel(gam_f, y)
    h = 1e-5
    dbeta = []
    for i in range(3):
        yp = list(y); ym = list(y); yp[i] += h; ym[i] -= h
        bp, bm = beta_f(yp), beta_f(ym)
        dbeta.append([(bp[j] - bm[j]) / (2 * h) for j in range(3)])
    b0 = beta_f(y)
    D = [[dbeta[i][j] - sum(Gm[k][i][j] * b0[k] for k in range(3)) for j in range(3)] for i in range(3)]
    K = [[(D[i][j] + D[j][i]) / (2 * alpha) for j in range(3)] for i in range(3)]
    gi3 = inv(gam_f(y))
    Ktr = sum(gi3[i][j] * K[i][j] for i in range(3) for j in range(3))
    Kup = [[sum(gi3[i][a] * K[a][b] * gi3[b][j] for a in range(3) for b in range(3)) for j in range(3)] for i in range(3)]
    KK = sum(K[i][j] * Kup[i][j] for i in range(3) for j in range(3))
    Ktr_cerr = 1.5 * b_cerr / r
    R3 = ricci_escalar(gam_f, y)
    ham = R3 + Ktr ** 2 - KK
    print(f"traza K = {Ktr:.9f} (cerrada 3/2 sqrt(2M/r)/r = {Ktr_cerr:.9f})")
    print(f"R3 = {R3:.2e}   K^2 = {Ktr ** 2:.9f}   K_ij K^ij = {KK:.9f}   ligadura hamiltoniana = {ham:.2e}")
    # convergencia
    T = 1.0
    errs = {N: onda(N, T) for N in (32, 64, 128, 256)}
    print(f"{'N':>5s} {'error L2':>13s} {'orden':>7s}")
    prev = None; orders = []
    for N, e in errs.items():
        o = math.log2(prev / e) if prev else float("nan")
        if prev:
            orders.append(o)
        print(f"{N:5d} {e:13.4e} {o:7.3f}")
        prev = e
    assert abs(alpha - 1) < 1e-12 and abs(bu[0] - b_cerr) < 1e-12 and abs(dg + alpha ** 2 * dgam) < 1e-10
    assert abs(Ktr - Ktr_cerr) < 1e-6 and abs(ham) < 1e-6
    assert all(1.9 < o < 2.1 for o in orders)
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
