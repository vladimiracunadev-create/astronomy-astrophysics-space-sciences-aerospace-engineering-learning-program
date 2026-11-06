#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C02: bases, coordenadas, rango y dimension.

Datos: SINTETICOS. Plano orbital con inclinacion i = 50 grados (didactica).
Modelo: coordenadas c = B^-1 v; rango por valores singulares; teorema
rango + nulidad = n. Supuestos: aritmetica de coma flotante doble.
Validez: rango numerico con umbral relativo 1e-10.
Tolerancia: 1e-12 en reconstrucciones.
"""
from __future__ import annotations
import platform
import numpy as np


def rango(A, tol=1e-10):
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s > tol * s[0])) if s[0] > 0 else 0


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    i = np.radians(50.0)
    P = np.array([1.0, 0.0, 0.0])
    Q = np.array([0.0, np.cos(i), np.sin(i)])
    W = np.array([0.0, -np.sin(i), np.cos(i)])
    B = np.column_stack([P, Q, W])
    assert np.allclose(B.T @ B, np.eye(3), atol=1e-12)
    v = np.array([3.0, 2.0, 1.0])
    c = B.T @ v
    print("coordenadas de v en la base orbital:", np.round(c, 6))
    assert np.allclose(B @ c, v, atol=1e-12)

    B2 = np.array([[1.0, 1.0, 0.0], [0.0, 1.0, 1.0], [0.0, 0.0, 1.0]])
    c2 = np.linalg.solve(B2, v)
    print("coordenadas en base no ortogonal   :", np.round(c2, 6))
    assert np.allclose(B2 @ c2, v, atol=1e-12)

    S = np.column_stack([[1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1]]).astype(float)
    r = rango(S)
    print("rango de 4 vectores en R^3 =", r, "| nulidad =", S.shape[1] - r)
    assert r == 3 and S.shape[1] - r == 1
    assert rango(np.column_stack([[1, 0, 0], [0, 1, 0], [1, 1, 0]]).astype(float)) == 2
    assert np.allclose(S @ np.array([1.0, 1.0, -1.0, 0.0]), 0)
    x = np.linspace(-1, 1, 9)
    V = np.vander(x, 4, increasing=True)
    print("rango de {1,x,x^2,x^3} evaluados en 9 puntos =", rango(V))
    assert rango(V) == 4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
