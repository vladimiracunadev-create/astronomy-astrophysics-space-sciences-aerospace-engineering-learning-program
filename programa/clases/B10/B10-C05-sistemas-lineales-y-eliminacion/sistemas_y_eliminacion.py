#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C05: eliminacion gaussiana con pivoteo y trilateracion plana.

Datos: SINTETICOS. Estaciones en (0,0), (1000,200) y (300,1000) km; objeto
en (400,600) km (verdad conocida); distancias exactas (sin ruido).
Modelo: |P - s_k|^2 = r_k^2; restando la primera ecuacion a las demas se
obtiene el sistema lineal 2 (s_k - s_1) . P = |s_k|^2 - |s_1|^2 - (r_k^2 - r_1^2).
Supuestos: plano, distancias exactas. Validez: estaciones no colineales.
Tolerancia: 1e-9 km en la posicion; 1e-12 en residuos relativos.
"""
from __future__ import annotations
import platform
import numpy as np


def eliminar(A, b, pivoteo=True):
    """Eliminacion gaussiana con pivoteo parcial y sustitucion hacia atras."""
    A = np.array(A, float)
    b = np.array(b, float)
    n = len(b)
    for k in range(n - 1):
        if pivoteo:
            p = k + int(np.argmax(np.abs(A[k:, k])))
            if p != k:
                A[[k, p]] = A[[p, k]]
                b[[k, p]] = b[[p, k]]
        if A[k, k] == 0.0:
            raise ZeroDivisionError("pivote nulo: matriz singular")
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]
    if A[n - 1, n - 1] == 0.0:
        raise ZeroDivisionError("pivote nulo: matriz singular")
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - A[i, i + 1:] @ x[i + 1:]) / A[i, i]
    return x


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    # 1. Sistema 3x3 de mano
    A = [[1, 1, 1], [2, -1, 1], [1, 2, -1]]
    b = [6, 3, 2]
    x = eliminar(A, b)
    print("sistema 3x3 ->", x.round(12))
    assert np.allclose(x, [1, 2, 3], atol=1e-12)

    # 2. Pivoteo: pivote diminuto
    Ap = [[1e-20, 1.0], [1.0, 1.0]]
    bp = [1.0, 2.0]
    sin = eliminar(Ap, bp, pivoteo=False)
    con = eliminar(Ap, bp, pivoteo=True)
    print("sin pivoteo:", sin, "| con pivoteo:", con, "| exacta ~ (1, 1)")
    assert abs(con[0] - 1) < 1e-12 and abs(sin[0] - 1) > 0.5

    # 3. Trilateracion
    S = np.array([[0.0, 0.0], [1000.0, 200.0], [300.0, 1000.0]])
    P = np.array([400.0, 600.0])
    r = np.linalg.norm(S - P, axis=1)
    M = 2 * (S[1:] - S[0])
    rhs = (S[1:] ** 2).sum(1) - (S[0] ** 2).sum() - (r[1:] ** 2 - r[0] ** 2)
    est = eliminar(M, rhs)
    print("distancias (km):", r.round(4))
    print("posicion estimada (km):", est.round(9), "| error:", float(np.linalg.norm(est - P)))
    assert np.linalg.norm(est - P) < 1e-9
    print("cond(M) =", round(float(np.linalg.cond(M)), 3))
    # estaciones casi colineales
    S2 = np.array([[0.0, 0.0], [500.0, 1e-3], [1000.0, 2.5e-3]])
    r2 = np.linalg.norm(S2 - P, axis=1)
    M2 = 2 * (S2[1:] - S2[0])
    print("cond(M) estaciones casi colineales =", f"{np.linalg.cond(M2):.3e}")

    # 4. Matriz de Hilbert: mal condicionada
    for n in (4, 8, 12):
        H = 1.0 / (np.arange(1, n + 1)[:, None] + np.arange(n)[None, :])
        xe = np.ones(n)
        xh = eliminar(H, H @ xe)
        print(f"Hilbert n={n:2d}: cond = {np.linalg.cond(H):.2e}, error max = {np.max(np.abs(xh - xe)):.2e}")
    # 5. Comparacion con la biblioteca
    rng = np.random.default_rng(5)
    A5 = rng.normal(size=(30, 30))
    b5 = rng.normal(size=30)
    assert np.allclose(eliminar(A5, b5), np.linalg.solve(A5, b5), atol=1e-9)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
