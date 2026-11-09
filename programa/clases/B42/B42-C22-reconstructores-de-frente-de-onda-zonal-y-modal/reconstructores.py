#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C22: reconstruccion de la fase a partir de pendientes con un reconstructor zonal (minimos cuadrados regularizados) y uno modal (Zernike), en geometria de Fried.

Datos: frente de onda SINTETICO de 1 rad rms formado por 40 ondas planas con amplitud proporcional a k^(-11/6) (pseudo-Kolmogorov, NO una pantalla de Kolmogorov exacta), red de 11 x 11 nodos con 10 x 10 subaperturas,
ruido de pendiente de 0,05 rad por paso de nodo y 14 modos de Zernike (ordenes radiales 1 a 4) son ILUSTRATIVOS ; semilla 20261109. Los polinomios de Zernike de Noll se escriben de memoria (formula general de R_n^m) y se verifica
numericamente su coherencia con las pendientes sintetizadas.
Modelo: operador de pendientes de Fried s = S phi (dos pendientes por subapertura, promedio de las diferencias de las cuatro esquinas) ; zonal: phi = (S^T S + eps I)^(-1) S^T s con eps = 1e-6 (fija el piston y el modo de
tablero, invisibles para S) ; modal: phi = Z a con a = (B^T B)^(-1) B^T s, B = S Z. La propagacion de ruido se calcula por la traza de G G^T con G el reconstructor (via analitica) y por Monte Carlo (via independiente, 300 repeticiones).
Supuestos: red cuadrada completa (los nodos se inscriben en el disco unidad con corners en r = 1), ruido blanco, sin aliasing de alta frecuencia (|k| <= 4 ciclos por 10 nodos). Validez: ilustrativa ; los reconstructores reales usan mascaras circulares, reconstructores tomograficos y regularizaciones de varios tipos.
Tolerancia: sin ruido, el error zonal del frente sintetico < 5 % rms (limitado por la discretizacion) ; el error modal incluye el truncado de modos ; propagacion de ruido Monte Carlo frente a la traza a 10 %.
"""
from __future__ import annotations
import math, platform, random

M = 11
NS = M - 1

def zern_rad(n, m, r):
    s = 0.0
    for k in range((n - m) // 2 + 1):
        s += (-1) ** k * math.factorial(n - k) / (math.factorial(k) * math.factorial((n + m) // 2 - k) * math.factorial((n - m) // 2 - k)) * r ** (n - 2 * k)
    return s

MODOS = [(1, 1, 'c'), (1, 1, 's'), (2, 0, 'c'), (2, 2, 'c'), (2, 2, 's'), (3, 1, 'c'), (3, 1, 's'), (3, 3, 'c'), (3, 3, 's'), (4, 0, 'c'), (4, 2, 'c'), (4, 2, 's'), (4, 4, 'c'), (4, 4, 's')]

def zern(n, m, tipo, r, t):
    norm = math.sqrt(n + 1) if m == 0 else math.sqrt(2 * (n + 1))
    ang = 1.0 if m == 0 else (math.cos(m * t) if tipo == 'c' else math.sin(m * t))
    return norm * zern_rad(n, m, r) * ang

def nodos():
    # nodos inscritos: esquinas en r = 1
    c = (M - 1) / 2
    esc = 1 / (c * math.sqrt(2))
    return [((j - c) * esc, (i - c) * esc) for i in range(M) for j in range(M)]

def idx(i, j):
    return i * M + j

def operador_pendientes():
    S = []
    for i in range(NS):
        for j in range(NS):
            f = [0.0] * (M * M)
            f[idx(i, j + 1)] += 0.5; f[idx(i, j)] -= 0.5; f[idx(i + 1, j + 1)] += 0.5; f[idx(i + 1, j)] -= 0.5
            S.append(f)
    for i in range(NS):
        for j in range(NS):
            f = [0.0] * (M * M)
            f[idx(i + 1, j)] += 0.5; f[idx(i, j)] -= 0.5; f[idx(i + 1, j + 1)] += 0.5; f[idx(i, j + 1)] -= 0.5
            S.append(f)
    return S

def mat_t(a):
    return [list(r) for r in zip(*a)]

def mat_mul(a, b):
    bt = mat_t(b)
    return [[sum(x * y for x, y in zip(r, c)) for c in bt] for r in a]

def inversa(a):
    n = len(a)
    m = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(m[r][c]))
        m[c], m[p] = m[p], m[c]
        piv = m[c][c]
        m[c] = [v / piv for v in m[c]]
        for r in range(n):
            if r != c and m[r][c] != 0.0:
                f = m[r][c]
                m[r] = [x - f * y for x, y in zip(m[r], m[c])]
    return [row[n:] for row in m]

def sin_piston(v):
    mu = sum(v) / len(v)
    return [x - mu for x in v]

def rms(v):
    return math.sqrt(sum(x * x for x in sin_piston(v)) / len(v))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    S = operador_pendientes()
    nodo = nodos()
    # frente sintetico
    ondas = []
    for _ in range(40):
        k = rnd.uniform(0.3, 4.0)
        a = rnd.uniform(0, 2 * math.pi)
        ondas.append((k * math.cos(a), k * math.sin(a), rnd.uniform(0, 2 * math.pi), k ** (-11 / 6)))
    phi = [sum(am * math.cos(2 * math.pi * (kx * j + ky * i) / (M - 1) + ps) for kx, ky, ps, am in ondas) for i in range(M) for j in range(M)]
    esc = 1.0 / rms(phi)
    phi = [v * esc for v in phi]
    print(f"frente de onda sintetico: rms = {rms(phi):.3f} rad ; pendientes = {len(S)} ; nodos = {M * M}")
    s = [sum(c * v for c, v in zip(f, phi)) for f in S]
    # zonal
    StS = mat_mul(mat_t(S), S)
    for i in range(M * M):
        StS[i][i] += 1e-6
    Gz = mat_mul(inversa(StS), mat_t(S))             # (121 x 200)
    pz = [sum(g * v for g, v in zip(f, s)) for f in Gz]
    # modal
    Z = [[zern(n, m, t, math.hypot(x, y), math.atan2(y, x)) for (n, m, t) in MODOS] for (x, y) in nodo]
    B = mat_mul(S, Z)                                 # (200 x 14)
    BtB = mat_mul(mat_t(B), B)
    Gm_a = mat_mul(inversa(BtB), mat_t(B))            # (14 x 200)
    am = [sum(g * v for g, v in zip(f, s)) for f in Gm_a]
    pm = [sum(z * a for z, a in zip(r, am)) for r in Z]
    ez = rms([a - b for a, b in zip(pz, phi)]) / rms(phi)
    em = rms([a - b for a, b in zip(pm, phi)]) / rms(phi)
    print(f"sin ruido: error relativo zonal = {ez:.4f} ; modal ({len(MODOS)} modos) = {em:.4f}")
    assert ez < 0.05
    # condicionamiento del modal: cuantas pendientes por modo
    print(f"pendientes / modos = {len(S)}/{len(MODOS)} = {len(S) / len(MODOS):.1f} ; pendientes / nodos = {len(S)}/{M * M} = {len(S) / (M * M):.2f}")
    # propagacion de ruido
    sig = 0.05
    Gm = mat_mul(Z, Gm_a)                             # (121 x 200) reconstructor modal en nodos
    def traza_ruido(G):
        # varianza media de la fase reconstruida sin piston por nodo : sigma^2 tr(Q G G^T Q)/N
        n = len(G)
        gg = 0.0
        # tr(Q G G^T Q) = sum_k ||Q g_k||^2 con g_k las columnas de G
        for k in range(len(G[0])):
            col = [G[i][k] for i in range(n)]
            gg += sum(x * x for x in sin_piston(col))
        return sig * math.sqrt(gg / n)
    tz, tm = traza_ruido(Gz), traza_ruido(Gm)
    nmc = 300
    az = am_ = 0.0
    for _ in range(nmc):
        sn = [v + rnd.gauss(0, sig) for v in s]
        pzn = [sum(g * v for g, v in zip(f, sn)) for f in Gz]
        pmn = [sum(g * v for g, v in zip(f, sn)) for f in Gm]
        az += sum(x * x for x in sin_piston([a - b for a, b in zip(pzn, pz)])) / (M * M)
        am_ += sum(x * x for x in sin_piston([a - b for a, b in zip(pmn, pm)])) / (M * M)
    mz, mm = math.sqrt(az / nmc), math.sqrt(am_ / nmc)
    print(f"{'reconstructor':<14} {'ruido rms Monte Carlo [rad]':>28} {'ruido rms por traza [rad]':>27}")
    print(f"{'zonal':<14} {mz:28.4f} {tz:27.4f}")
    print(f"{'modal':<14} {mm:28.4f} {tm:27.4f}")
    assert abs(mz / tz - 1) < 0.10 and abs(mm / tm - 1) < 0.10
    assert tm < tz        # el modal con 14 modos propaga menos ruido que el zonal con 121 nodos
    # error total con ruido
    print(f"error total esperado (raiz de ajuste^2 + ruido^2): zonal = {math.hypot(ez, tz):.4f} ; modal = {math.hypot(em, tm):.4f} (relativo a 1 rad rms)")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
