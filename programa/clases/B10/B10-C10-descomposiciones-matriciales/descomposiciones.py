#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C10: LU con pivoteo, QR y Cholesky.

Datos: SINTETICOS. Covarianza de error de posicion (km^2) de un objeto:
P = [[4, 1, 0.5], [1, 3, 0.2], [0.5, 0.2, 2]] (simetrica definida positiva).
Modelo: P A = L U (Doolittle con pivoteo parcial); A = Q R; P = L L^T.
Supuestos: aritmetica doble. Validez: matrices cuadradas regulares (LU) y
simetricas definidas positivas (Cholesky).
Tolerancia: 1e-12 en las reconstrucciones; 2 % en la covarianza muestral
(semilla fija, 400 000 muestras).
"""
from __future__ import annotations
import platform
import numpy as np


def lu_pivoteo(A):
    A = np.array(A, float)
    n = A.shape[0]
    P = np.eye(n)
    L = np.zeros((n, n))
    U = A.copy()
    for k in range(n - 1):
        p = k + int(np.argmax(np.abs(U[k:, k])))
        if p != k:
            U[[k, p]] = U[[p, k]]
            P[[k, p]] = P[[p, k]]
            L[[k, p], :k] = L[[p, k], :k]
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]
    L += np.eye(n)
    return P, L, U


def cholesky(A):
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)
    for j in range(n):
        s = A[j, j] - L[j, :j] @ L[j, :j]
        if s <= 0:
            raise ValueError("la matriz no es definida positiva")
        L[j, j] = np.sqrt(s)
        for i in range(j + 1, n):
            L[i, j] = (A[i, j] - L[i, :j] @ L[j, :j]) / L[j, j]
    return L


def resolver_lu(P, L, U, b):
    y = np.linalg.solve(np.tril(L), P @ b)       # sustitucion hacia adelante
    return np.linalg.solve(np.triu(U), y)        # sustitucion hacia atras


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    A = np.array([[2.0, 1.0, 1.0], [4.0, -6.0, 0.0], [-2.0, 7.0, 2.0]])
    P, L, U = lu_pivoteo(A)
    print("P A - L U (max) =", float(np.abs(P @ A - L @ U).max()))
    assert np.allclose(P @ A, L @ U, atol=1e-12)
    det_lu = np.linalg.det(P) * np.prod(np.diag(U))
    print("det por LU =", round(float(det_lu), 9), "| det directo =", round(float(np.linalg.det(A)), 9))
    assert abs(det_lu - np.linalg.det(A)) < 1e-9
    b = np.array([5.0, -2.0, 9.0])
    x = resolver_lu(P, L, U, b)
    print("A x = b ->", x.round(12))
    assert np.allclose(A @ x, b, atol=1e-12)

    Q, R = np.linalg.qr(A)
    assert np.allclose(Q @ R, A, atol=1e-12) and np.allclose(Q.T @ Q, np.eye(3), atol=1e-12)
    print("QR: |A - QR| max =", float(np.abs(A - Q @ R).max()), "| |Q^T Q - I| max =", float(np.abs(Q.T @ Q - np.eye(3)).max()))

    Pc = np.array([[4.0, 1.0, 0.5], [1.0, 3.0, 0.2], [0.5, 0.2, 2.0]])
    Lc = cholesky(Pc)
    print("Cholesky L =\n", Lc.round(6))
    assert np.allclose(Lc @ Lc.T, Pc, atol=1e-12) and np.allclose(Lc, np.linalg.cholesky(Pc), atol=1e-12)
    try:
        cholesky(np.array([[1.0, 2.0], [2.0, 1.0]]))
        raise AssertionError("debia fallar")
    except ValueError as e:
        print("[[1,2],[2,1]]:", e)

    rng = np.random.default_rng(12)
    w = rng.normal(size=(3, 400_000))
    muestras = Lc @ w
    cov = np.cov(muestras)
    err = np.abs(cov - Pc).max() / np.abs(Pc).max()
    print("covarianza muestral - P (max relativo) =", f"{err:.4f}")
    assert err < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
