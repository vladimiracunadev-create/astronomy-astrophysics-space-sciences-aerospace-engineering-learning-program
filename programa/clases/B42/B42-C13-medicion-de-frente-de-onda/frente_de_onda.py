#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C13: medicion de un frente de onda por pendientes y por fase interferometrica, con ajuste modal de Zernike.

Datos: coeficientes verdaderos (nm rms), ruido de pendientes (1 nm por unidad de radio de pupila) y ruido de fase (0,005 rad a 633 nm) son ILUSTRATIVOS ; semilla 20261109.
Los polinomios de Zernike con normalizacion de Noll (rms unitario sobre el disco) se escriben aqui de memoria y se VERIFICAN numericamente (ortonormalidad) en la propia ejecucion.
Modelo: W(x,y) = sum a_j Z_j. Via A (tipo Hartmann): pendientes por diferencias centradas de W en 24 x 24 puntos de pupila, ajuste por minimos cuadrados de las 8 coeficientes a las
pendientes. Via B (interferometria de cuatro pasos, C09): fase phi = 2 pi W / lambda con ruido, ajuste directo de W. Para cada via la covarianza prevista de los coeficientes es
sigma^2 (A^T A)^(-1) y se compara con la dispersion de 400 repeticiones Monte Carlo.
Supuestos: ruido blanco gaussiano independiente, modos conocidos, sin desenrollado de fase (|phi| < pi). Validez: ilustrativa de la teoria lineal de estimacion.
Tolerancia: sin ruido, coeficientes a 1e-3 nm ; dispersion Monte Carlo frente a la prevista a 12 %.
"""
from __future__ import annotations
import math, platform, random

M = 24
LAM = 633.0

def zern(j, r, t):
    if j == 0: return 2 * r * math.cos(t)
    if j == 1: return 2 * r * math.sin(t)
    if j == 2: return math.sqrt(3) * (2 * r * r - 1)
    if j == 3: return math.sqrt(6) * r * r * math.sin(2 * t)
    if j == 4: return math.sqrt(6) * r * r * math.cos(2 * t)
    if j == 5: return math.sqrt(8) * (3 * r ** 3 - 2 * r) * math.sin(t)
    if j == 6: return math.sqrt(8) * (3 * r ** 3 - 2 * r) * math.cos(t)
    return math.sqrt(5) * (6 * r ** 4 - 6 * r * r + 1)

NOMBRES = ["inclinacion x", "inclinacion y", "desenfoque", "astigmatismo 45", "astigmatismo 0", "coma y", "coma x", "esferica"]

def modo(j, x, y):
    return zern(j, math.hypot(x, y), math.atan2(y, x))

def puntos():
    out = []
    for i in range(M):
        for k in range(M):
            x = -1 + (2 * k + 1) / M
            y = -1 + (2 * i + 1) / M
            if math.hypot(x, y) <= 1:
                out.append((x, y))
    return out

def resolver(a, b):
    n = len(a)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(m[r][c]))
        m[c], m[p] = m[p], m[c]
        for r in range(n):
            if r != c:
                f = m[r][c] / m[c][c]
                for k in range(c, n + 1):
                    m[r][k] -= f * m[c][k]
    return [m[i][n] / m[i][i] for i in range(n)]

def inversa(a):
    n = len(a)
    return [resolver(a, [1.0 if i == j else 0.0 for i in range(n)]) for j in range(n)]

def ata(A):
    n = len(A[0])
    return [[sum(r[i] * r[j] for r in A) for j in range(n)] for i in range(n)]

def atb(A, b):
    return [sum(r[i] * v for r, v in zip(A, b)) for i in range(len(A[0]))]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    P = puntos()
    n = len(P)
    # ortonormalidad numerica
    G = [[sum(modo(i, x, y) * modo(j, x, y) for x, y in P) / n for j in range(8)] for i in range(8)]
    ort = max(abs(G[i][j] - (1.0 if i == j else 0.0)) for i in range(8) for j in range(8))
    print(f"puntos en la pupila = {n} ; maxima desviacion de la ortonormalidad (malla {M}x{M}) = {ort:.3f}")
    assert ort < 0.06
    a_ver = [30.0, -20.0, 60.0, 25.0, -15.0, 20.0, -12.0, 18.0]
    W = lambda x, y: sum(a * modo(j, x, y) for j, a in enumerate(a_ver))
    # via B: matriz de diseno de fase
    Ab = [[modo(j, x, y) for j in range(8)] for x, y in P]
    # via A: pendientes (dW/dx, dW/dy) por diferencias centradas, paso h
    h = 1e-5
    As = []
    for x, y in P:
        As.append([(modo(j, x + h, y) - modo(j, x - h, y)) / (2 * h) for j in range(8)])
    for x, y in P:
        As.append([(modo(j, x, y + h) - modo(j, x, y - h)) / (2 * h) for j in range(8)])
    pend = [(W(x + h, y) - W(x - h, y)) / (2 * h) for x, y in P] + [(W(x, y + h) - W(x, y - h)) / (2 * h) for x, y in P]
    iA = inversa(ata(As))
    iB = inversa(ata(Ab))
    ca = [sum(iA[i][k] * v for k, v in enumerate(atb(As, pend))) for i in range(8)]
    wb = [W(x, y) for x, y in P]
    cb = [sum(iB[i][k] * v for k, v in enumerate(atb(Ab, wb))) for i in range(8)]
    err_a = max(abs(c - t) for c, t in zip(ca, a_ver))
    err_b = max(abs(c - t) for c, t in zip(cb, a_ver))
    print(f"sin ruido: error maximo via pendientes = {err_a:.2e} nm ; via fase = {err_b:.2e} nm")
    assert err_a < 1e-3 and err_b < 1e-3
    wrms = math.sqrt(sum(a * a for a in a_ver))
    print(f"rms del frente de onda verdadero = {wrms:.3f} nm (suma cuadratica de los 8 coeficientes)")
    # Monte Carlo con ruido
    sig_s = 1.0                              # nm por unidad de radio
    sig_phi = 0.005                          # rad
    sig_w = sig_phi * LAM / (2 * math.pi)    # nm
    print(f"ruido de fase 0,005 rad a {LAM:.0f} nm = {sig_w:.4f} nm de frente de onda por punto")
    nmc = 400
    sa = [[0.0, 0.0] for _ in range(8)]
    sb = [[0.0, 0.0] for _ in range(8)]
    for _ in range(nmc):
        pn = [v + rnd.gauss(0, sig_s) for v in pend]
        wn = [v + rnd.gauss(0, sig_w) for v in wb]
        xa = atb(As, pn); xb = atb(Ab, wn)
        for i in range(8):
            va = sum(iA[i][k] * xa[k] for k in range(8)) - a_ver[i]
            vb = sum(iB[i][k] * xb[k] for k in range(8)) - a_ver[i]
            sa[i][0] += va; sa[i][1] += va * va
            sb[i][0] += vb; sb[i][1] += vb * vb
    print(f"{'modo':<18} {'sigma A MC':>10} {'sigma A teo':>11} {'sigma B MC':>10} {'sigma B teo':>11}")
    for i in range(8):
        ma = math.sqrt(sa[i][1] / nmc); ta = sig_s * math.sqrt(iA[i][i])
        mb = math.sqrt(sb[i][1] / nmc); tb = sig_w * math.sqrt(iB[i][i])
        print(f"{NOMBRES[i]:<18} {ma:10.4f} {ta:11.4f} {mb:10.4f} {tb:11.4f}")
        assert abs(ma / ta - 1) < 0.12 and abs(mb / tb - 1) < 0.12, (i, ma, ta, mb, tb)
    ra = math.sqrt(sum(sig_s ** 2 * iA[i][i] for i in range(8)))
    rb = math.sqrt(sum(sig_w ** 2 * iB[i][i] for i in range(8)))
    print(f"error total del frente de onda reconstruido (rms, 8 modos): via pendientes = {ra:.3f} nm ; via fase = {rb:.3f} nm")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
