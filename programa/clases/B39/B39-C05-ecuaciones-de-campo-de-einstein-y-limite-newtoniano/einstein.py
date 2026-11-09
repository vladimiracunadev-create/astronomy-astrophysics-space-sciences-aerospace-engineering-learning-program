#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B39-C05: tensor de Einstein, limite newtoniano de campo debil e identidad de Bianchi contraida.

Datos: G = 6,674 30e-11 m^3 kg^-1 s^-2 y c = 299 792 458 m/s, NIST CODATA 2022 (tabla allascii, consultada el 2026-11-09). La masa de prueba M (0,1; 0,01; 0,001 en unidades geometrizadas G = c = 1), el radio de suavizado b = 1, el punto de evaluacion y los exponentes n del universo a(t) = t^n son
ILUSTRATIVOS (sinteticos); no describen ningun astro real.
Modelo: G_ab = R_ab - R g_ab / 2 con Riemann por diferencias finitas anidadas (pasos 1e-4 y 1e-3); metrica de campo debil ds^2 = -(1 + 2 Phi) dt^2 + (1 - 2 Phi) dx^2 con Phi = -M / sqrt(r^2 + b^2) (esfera de Plummer), cuya densidad de Poisson es rho = 3 M b^2 / (4 pi (r^2 + b^2)^(5/2)); FLRW plano a = t^n: G_00 = 3 n^2 / t^2.
Supuestos: campo debil estatico (|Phi| << 1) y FLRW plano de fluido perfecto. Validez: ilustrativa.
Tolerancia: G_00 frente a 8 pi rho con desviacion relativa proporcional a |Phi| (los coeficientes de los dos valores menores de M coinciden a 5 %); FLRW a 1e-6; identidad de Bianchi contraida a 1e-3 relativo (derivada temporal por diferencias de paso 0,02).
"""
from __future__ import annotations
import math, platform, itertools

G_SI = 6.67430e-11  # NIST CODATA 2022
C_SI = 299792458.0  # NIST CODATA 2022 (exacta)

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

def einstein(g, x, h1=1e-4, h2=1e-3):
    n = len(x)
    G = christoffel(g, x, h1)
    dG = []
    for c in range(n):
        xp = list(x); xm = list(x); xp[c] += h2; xm[c] -= h2
        Gp, Gm = christoffel(g, xp, h1), christoffel(g, xm, h1)
        dG.append([[[(Gp[a][b][d] - Gm[a][b][d]) / (2 * h2) for d in range(n)] for b in range(n)] for a in range(n)])
    ric = [[0.0] * n for _ in range(n)]
    for b, d in itertools.product(range(n), repeat=2):
        for a in range(n):
            ric[b][d] += (dG[a][a][d][b] - dG[d][a][a][b]
                          + sum(G[a][a][e] * G[e][d][b] - G[a][d][e] * G[e][a][b] for e in range(n)))
    gm = g(x); gi = inv(gm)
    R = sum(gi[b][d] * ric[b][d] for b in range(n) for d in range(n))
    return [[ric[a][b] - 0.5 * R * gm[a][b] for b in range(n)] for a in range(n)], ric, R

B = 1.0
def metrica_debil(M):
    def g(x):
        r2 = x[1] ** 2 + x[2] ** 2 + x[3] ** 2
        phi = -M / math.sqrt(r2 + B * B)
        return [[-(1 + 2 * phi), 0, 0, 0], [0, 1 - 2 * phi, 0, 0], [0, 0, 1 - 2 * phi, 0], [0, 0, 0, 1 - 2 * phi]]
    return g

def flrw(n):
    return lambda x: [[-1, 0, 0, 0], [0, x[0] ** (2 * n), 0, 0], [0, 0, x[0] ** (2 * n), 0], [0, 0, 0, x[0] ** (2 * n)]]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"8 pi G / c^4 = {8 * math.pi * G_SI / C_SI ** 4:.6e} s^2 kg^-1 m^-1 (NIST CODATA 2022)")
    x = [0.0, 0.8, 0.3, 0.4]
    r2 = 0.8 ** 2 + 0.3 ** 2 + 0.4 ** 2
    print(f"{'M':>7s} {'Phi':>11s} {'G_00 numerico':>15s} {'8 pi rho':>13s} {'desv. relativa':>15s} {'desv./|Phi|':>12s}")
    devs = []
    for M in (1e-1, 1e-2, 1e-3):
        Ein, ric, R = einstein(metrica_debil(M), x)
        rho = 3 * M * B * B / (4 * math.pi * (r2 + B * B) ** 2.5)
        phi = -M / math.sqrt(r2 + B * B)
        d = abs(Ein[0][0] / (8 * math.pi * rho) - 1)
        devs.append((M, phi, d))
        print(f"{M:7.0e} {phi:11.3e} {Ein[0][0]:15.6e} {8 * math.pi * rho:13.6e} {d:15.3e} {d / abs(phi):12.3f}")
    # G_00 para metrica FLRW
    print(f"{'n':>6s} {'G_00':>12s} {'3n^2/t^2':>12s} {'G_11/a^2':>12s} {'cerrada':>12s}")
    t0 = 2.0
    for n in (2 / 3, 0.5, 0.8):
        Ein, ric, R = einstein(flrw(n), [t0, 0, 0, 0])
        c00 = 3 * n * n / t0 ** 2
        c11 = -(2 * n * (n - 1) + n * n) / t0 ** 2
        print(f"{n:6.4f} {Ein[0][0]:12.8f} {c00:12.8f} {Ein[1][1] / t0 ** (2 * n):12.8f} {c11:12.8f}")
        assert abs(Ein[0][0] - c00) < 1e-6 and abs(Ein[1][1] / t0 ** (2 * n) - c11) < 1e-6
    # Bianchi contraida: d rho/dt + 3 H (rho + p) = 0 con rho = G_00/(8 pi), p = G_11/(8 pi a^2)
    print(f"{'n':>6s} {'d rho/dt':>13s} {'-3H(rho+p)':>13s} {'dif. relativa':>14s}")
    d_t = 0.02
    for n in (2 / 3, 0.5, 0.8):
        rho_f = lambda t: einstein(flrw(n), [t, 0, 0, 0])[0][0][0] / (8 * math.pi)
        drho = (rho_f(t0 + d_t) - rho_f(t0 - d_t)) / (2 * d_t)
        Ein, ric, R = einstein(flrw(n), [t0, 0, 0, 0])
        rho = Ein[0][0] / (8 * math.pi); p = Ein[1][1] / t0 ** (2 * n) / (8 * math.pi)
        rhs = -3 * (n / t0) * (rho + p)
        dif = abs(drho / rhs - 1)
        print(f"{n:6.4f} {drho:13.6e} {rhs:13.6e} {dif:14.3e}")
        assert dif < 1e-3
    # el limite newtoniano mejora al reducir Phi
    assert devs[0][2] > devs[1][2] > devs[2][2]
    k1, k2 = devs[1][2] / abs(devs[1][1]), devs[2][2] / abs(devs[2][1])
    assert abs(k2 / k1 - 1) < 0.05  # desviacion lineal en Phi
    assert devs[2][2] < 5e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
