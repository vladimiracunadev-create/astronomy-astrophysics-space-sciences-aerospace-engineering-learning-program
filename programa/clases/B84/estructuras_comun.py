#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Biblioteca comun de los laboratorios de B84 (solo biblioteca estandar de Python).

Contiene algebra lineal densa pequena, autovalores simetricos (Jacobi), problema generalizado K phi = w2 M phi
(via Cholesky), matrices de la viga de Euler-Bernoulli (consistentes) y una FFT radix-2.
Unidades: el llamador elige un sistema coherente (SI: m, kg, s, N, Pa). Tolerancias: cada laboratorio declara las suyas.
"""
from __future__ import annotations
import math, cmath


def zeros(n, m=None):
    m = n if m is None else m
    return [[0.0] * m for _ in range(n)]


def matvec(A, x):
    return [sum(a * b for a, b in zip(fila, x)) for fila in A]


def matmul(A, B):
    Bt = list(zip(*B))
    return [[sum(a * b for a, b in zip(fila, col)) for col in Bt] for fila in A]


def transpose(A):
    return [list(c) for c in zip(*A)]


def solve(A, b):
    """Eliminacion gaussiana con pivoteo parcial. Devuelve x tal que A x = b."""
    n = len(A)
    M = [list(map(float, A[i])) + [float(b[i])] for i in range(n)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(M[i][k]))
        if abs(M[p][k]) < 1e-300:
            raise ValueError("matriz singular")
        M[k], M[p] = M[p], M[k]
        for i in range(k + 1, n):
            f = M[i][k] / M[k][k]
            if f:
                for j in range(k, n + 1):
                    M[i][j] -= f * M[k][j]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x


def jacobi_eig(A, tol=1e-14, max_sweeps=100):
    """Autovalores y autovectores (columnas) de una matriz simetrica; ordenados de menor a mayor."""
    n = len(A)
    a = [list(map(float, f)) for f in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_sweeps):
        off = sum(a[i][j] ** 2 for i in range(n) for j in range(i + 1, n))
        if off < tol ** 2 * max(1e-300, sum(a[i][i] ** 2 for i in range(n)) + off):
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                th = (a[q][q] - a[p][p]) / (2.0 * a[p][q])
                t = (1.0 if th >= 0 else -1.0) / (abs(th) + math.sqrt(th * th + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p], a[k][q] = c * akp - s * akq, s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k], a[q][k] = c * apk - s * aqk, s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = V[k][p], V[k][q]
                    V[k][p], V[k][q] = c * vkp - s * vkq, s * vkp + c * vkq
    idx = sorted(range(n), key=lambda i: a[i][i])
    vals = [a[i][i] for i in idx]
    vecs = [[V[k][i] for i in idx] for k in range(n)]
    return vals, vecs


def cholesky(M):
    n = len(M)
    L = zeros(n)
    for i in range(n):
        for j in range(i + 1):
            s = M[i][j] - sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                if s <= 0:
                    raise ValueError("matriz no definida positiva")
                L[i][i] = math.sqrt(s)
            else:
                L[i][j] = s / L[j][j]
    return L


def gen_eig(K, M):
    """K phi = lambda M phi. Devuelve (lambdas, modos con columnas M-normalizadas: phi^T M phi = 1)."""
    n = len(K)
    L = cholesky(M)
    # C = L^-1 K L^-T
    Y = [solve(L, [K[i][j] for i in range(n)]) for j in range(n)]  # columnas de L^-1 K
    Y = transpose(Y)  # L^-1 K
    C = [solve(L, [Y[i][j] for j in range(n)]) for i in range(n)]  # fila i de (L^-1 K) L^-T
    C = [[0.5 * (C[i][j] + C[j][i]) for j in range(n)] for i in range(n)]
    vals, Z = jacobi_eig(C)
    Lt = transpose(L)
    modos = [[0.0] * n for _ in range(n)]
    for j in range(n):
        col = solve(Lt, [Z[i][j] for i in range(n)])
        for i in range(n):
            modos[i][j] = col[i]
    return vals, modos


def viga_ke(EI, L):
    """Rigidez de elemento de viga Euler-Bernoulli, GDL [w1, th1, w2, th2]."""
    c = EI / L ** 3
    return [[c * v for v in f] for f in (
        (12, 6 * L, -12, 6 * L), (6 * L, 4 * L * L, -6 * L, 2 * L * L),
        (-12, -6 * L, 12, -6 * L), (6 * L, 2 * L * L, -6 * L, 4 * L * L))]


def viga_me(rhoA, L):
    """Masa consistente de elemento de viga Euler-Bernoulli."""
    c = rhoA * L / 420.0
    return [[c * v for v in f] for f in (
        (156, 22 * L, 54, -13 * L), (22 * L, 4 * L * L, 13 * L, -3 * L * L),
        (54, 13 * L, 156, -22 * L), (-13 * L, -3 * L * L, -22 * L, 4 * L * L))]


def ensamblar_viga(n, L, EI, rhoA):
    """Viga de n elementos iguales y longitud total L. Devuelve K, M globales (2(n+1) GDL, sin restricciones)."""
    le = L / n
    N = 2 * (n + 1)
    K, M = zeros(N), zeros(N)
    ke, me = viga_ke(EI, le), viga_me(rhoA, le)
    for e in range(n):
        g = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        for i in range(4):
            for j in range(4):
                K[g[i]][g[j]] += ke[i][j]
                M[g[i]][g[j]] += me[i][j]
    return K, M


def reducir(A, libres):
    return [[A[i][j] for j in libres] for i in libres]


def fft(x):
    """FFT radix-2 recursiva (len(x) potencia de 2)."""
    n = len(x)
    if n == 1:
        return [complex(x[0])]
    par, impar = fft(x[0::2]), fft(x[1::2])
    out = [0j] * n
    for k in range(n // 2):
        t = cmath.exp(-2j * math.pi * k / n) * impar[k]
        out[k], out[k + n // 2] = par[k] + t, par[k] - t
    return out


def asd_grms(puntos):
    """Valor eficaz (g rms) de una ASD lineal a tramos en escala log-log.
    puntos = [(f_Hz, ASD g2/Hz), ...]. Integra analiticamente cada tramo: W = int a f^m df."""
    area = 0.0
    for (f1, a1), (f2, a2) in zip(puntos, puntos[1:]):
        m = math.log(a2 / a1) / math.log(f2 / f1)
        if abs(m + 1.0) < 1e-12:
            area += a1 * f1 * math.log(f2 / f1)
        else:
            area += a1 / f1 ** m * (f2 ** (m + 1) - f1 ** (m + 1)) / (m + 1)
    return math.sqrt(area)
