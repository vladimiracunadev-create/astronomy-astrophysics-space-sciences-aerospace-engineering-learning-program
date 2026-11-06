#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C04: determinantes, invertibilidad y regla de Cramer.

Datos: SINTETICOS. Dos estaciones en (0,0) y (1000,0) km miden la direccion
hacia un objeto situado (verdad conocida) en (400, 600) km.
Modelo: P = s_k + t_k d_k; el cruce de las dos visuales resuelve
[d1  -d2][t1 t2]^T = s2 - s1; det = -(d1 x d2) = -sen(angulo entre visuales).
Supuestos: plano, sin ruido. Validez: angulo entre visuales no nulo.
Tolerancia: 1e-9 en la posicion recuperada; det = 0 detectado con 1e-12.
"""
from __future__ import annotations
import platform
import numpy as np


def det_cofactores(A):
    """Determinante por expansion en la primera fila (DLMF 1.3.4)."""
    A = np.asarray(A, float)
    n = A.shape[0]
    if n == 1:
        return A[0, 0]
    tot = 0.0
    for j in range(n):
        menor = np.delete(np.delete(A, 0, 0), j, 1)
        tot += (-1) ** j * A[0, j] * det_cofactores(menor)
    return tot


def cramer2(A, b):
    d = det_cofactores(A)
    if abs(d) < 1e-12:
        raise ZeroDivisionError("det = 0: sin solucion unica")
    x1 = det_cofactores(np.column_stack([b, A[:, 1]])) / d
    x2 = det_cofactores(np.column_stack([A[:, 0], b])) / d
    return np.array([x1, x2]), d


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    rng = np.random.default_rng(1)
    for n in (2, 3, 4, 5):
        A = rng.normal(size=(n, n))
        assert abs(det_cofactores(A) - np.linalg.det(A)) < 1e-9
    A, B = rng.normal(size=(2, 4, 4))
    assert abs(np.linalg.det(A @ B) - np.linalg.det(A) * np.linalg.det(B)) < 1e-9
    u, v = np.array([3.0, 0.0]), np.array([1.0, 2.0])
    print("area del paralelogramo =", det_cofactores(np.column_stack([u, v])))
    assert abs(det_cofactores(np.column_stack([u, v])) - 6.0) < 1e-12
    M = np.diag([1.0, 2.0, 3.0])
    assert abs(det_cofactores(M) - 6.0) < 1e-12

    s1, s2, P = np.array([0.0, 0.0]), np.array([1000.0, 0.0]), np.array([400.0, 600.0])
    d1 = (P - s1) / np.linalg.norm(P - s1)
    d2 = (P - s2) / np.linalg.norm(P - s2)
    A2 = np.column_stack([d1, -d2])
    t, d = cramer2(A2, s2 - s1)
    Prec = s1 + t[0] * d1
    print(f"det = {d:.6f}  posicion recuperada = {Prec.round(6)} km")
    assert np.allclose(Prec, P, atol=1e-9)
    for lejos in (1e3, 1e5, 1e7):
        Pl = np.array([400.0, lejos])
        e1 = (Pl - s1) / np.linalg.norm(Pl - s1)
        e2 = (Pl - s2) / np.linalg.norm(Pl - s2)
        Al = np.column_stack([e1, -e2])
        print(f"objeto a {lejos:9.0f} km: |det| = {abs(det_cofactores(Al)):.3e}  cond = {np.linalg.cond(Al):.3e}")
    try:
        cramer2(np.column_stack([d1, -d1]), s2 - s1)
        raise AssertionError("debia fallar")
    except ZeroDivisionError as e:
        print("visuales paralelas:", e)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
