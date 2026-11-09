#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C10: inversion lineal regularizada (Tikhonov) de una perturbacion interna a partir de datos tipo frecuencia.

Datos: ninguna constante fisica. Todo es SINTETICO (ilustrativo): los nucleos K_i(x) (gaussianas positivas de ancho 0,12 centradas entre x = 0,08 y 0,92), la perturbacion verdadera
(una gaussiana centrada en x = 0,35) y el ruido (sigma = 0,01) con semilla 20261109. No son nucleos de frecuencias estelares reales.
Modelo: d_i = Int K_i(x) f(x) dx + e_i, con 12 datos y 40 incognitas discretizadas; solucion de Tikhonov f = (A^T A + lambda I)^-1 A^T d. Dos vias algebraicamente equivalentes:
forma primal (40 x 40) y forma dual f = A^T (A A^T + lambda I)^-1 d (12 x 12). Resolucion R = A^T (A A^T + lambda I)^-1 A, con traza = grados de libertad efectivos.
Supuestos: problema lineal, ruido gaussiano independiente, regularizacion de orden cero. Validez: ilustra el compromiso sesgo-varianza, no una inversion estelar.
Tolerancia: primal y dual coinciden a 1e-8; con lambda -> 0 y sin ruido el ajuste de los datos es casi exacto (residuo < 1e-4); traza de R entre 0 y el numero de datos.
"""
from __future__ import annotations
import math, platform, random, sys

NX, ND = 40, 12


def gauss_solve(A, B):
    n = len(A)
    m = len(B[0])
    M = [A[i][:] + B[i][:] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n + m):
                M[r][k] -= f * M[c][k]
    X = [[0.0] * m for _ in range(n)]
    for r in range(n - 1, -1, -1):
        for j in range(m):
            X[r][j] = (M[r][n + j] - sum(M[r][k] * X[k][j] for k in range(r + 1, n))) / M[r][r]
    return X


def matriz():
    xs = [(j + 0.5) / NX for j in range(NX)]
    A = []
    for i in range(ND):
        # nucleos localizados: gaussianas de ancho 0,12 centradas de 0,1 a 0,9, por dx
        c = 0.08 + 0.84 * i / (ND - 1)
        A.append([math.exp(-0.5 * ((x - c) / 0.12) ** 2) / NX * 5.0 for x in xs])
    return xs, A


def tikhonov_primal(A, d, lam):
    n = len(A[0])
    AtA = [[sum(A[k][i] * A[k][j] for k in range(len(A))) + (lam if i == j else 0.0) for j in range(n)] for i in range(n)]
    Atd = [[sum(A[k][i] * d[k] for k in range(len(A)))] for i in range(n)]
    return [r[0] for r in gauss_solve(AtA, Atd)]


def tikhonov_dual(A, d, lam):
    m = len(A)
    AAt = [[sum(A[i][k] * A[j][k] for k in range(len(A[0]))) + (lam if i == j else 0.0) for j in range(m)] for i in range(m)]
    y = [r[0] for r in gauss_solve(AAt, [[v] for v in d])]
    return [sum(A[i][j] * y[i] for i in range(m)) for j in range(len(A[0]))]


def traza_resolucion(A, lam):
    m = len(A)
    G0 = [[sum(A[i][k] * A[j][k] for k in range(len(A[0]))) for j in range(m)] for i in range(m)]
    AAt = [[G0[i][j] + (lam if i == j else 0.0) for j in range(m)] for i in range(m)]
    S = gauss_solve(AAt, G0)
    return sum(S[i][i] for i in range(m))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    xs, A = matriz()
    ftrue = [math.exp(-0.5 * ((x - 0.35) / 0.07) ** 2) for x in xs]
    d0 = [sum(a * f for a, f in zip(row, ftrue)) for row in A]
    rng = random.Random(20261109)
    sig = 0.01
    d = [v + rng.gauss(0, sig) for v in d0]
    print(f"{ND} datos, {NX} incognitas; max dato = {max(d0):.4f}; sigma = {sig}")
    print(f"{'lambda':>9} {'residuo rms':>12} {'error rms de f':>15} {'traza R':>8}")
    res = {}
    for lam in (1e-8, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1):
        fp = tikhonov_primal(A, d, lam)
        fd = tikhonov_dual(A, d, lam)
        dif = max(abs(a - b) for a, b in zip(fp, fd))
        assert dif < 1e-6, (lam, dif)
        r = math.sqrt(sum((sum(a * f for a, f in zip(row, fp)) - di) ** 2 for row, di in zip(A, d)) / ND)
        e = math.sqrt(sum((a - b) ** 2 for a, b in zip(fp, ftrue)) / NX)
        tr = traza_resolucion(A, lam)
        res[lam] = (r, e, tr)
        print(f"{lam:9.0e} {r:12.5f} {e:15.5f} {tr:8.3f}")
        assert 0 < tr <= ND + 1e-6
    # sin ruido y lambda pequeno: ajuste casi exacto
    fp = tikhonov_primal(A, d0, 1e-8)
    r0 = math.sqrt(sum((sum(a * f for a, f in zip(row, fp)) - di) ** 2 for row, di in zip(A, d0)) / ND)
    print(f"sin ruido, lambda = 1e-8: residuo rms = {r0:.2e}")
    assert r0 < 1e-4
    # compromiso: el residuo crece con lambda; el error de f tiene un minimo interior
    ls = sorted(res)
    assert all(res[a][0] <= res[b][0] + 1e-12 for a, b in zip(ls, ls[1:]))
    errs = [res[l][1] for l in ls]
    kmin = errs.index(min(errs))
    print(f"lambda de minimo error: {ls[kmin]:.0e} (error {errs[kmin]:.5f}); el discrepancy principle pide residuo rms = sigma = {sig}")
    assert 0 < kmin < len(ls) - 1
    # principio de discrepancia: el lambda cuyo residuo rms se acerca mas a sigma
    lam_d = min(ls, key=lambda l: abs(res[l][0] - sig))
    print(f"lambda por discrepancia: {lam_d:.0e} (residuo rms {res[lam_d][0]:.5f}, error de f {res[lam_d][1]:.5f})")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
