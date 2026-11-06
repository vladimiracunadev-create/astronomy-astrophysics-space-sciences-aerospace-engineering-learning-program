#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C06: producto interno, angulos y Gram-Schmidt.

Datos: SINTETICOS (direcciones del Sol y normales de panel inventadas).
Modelo: <u,v> = sum u_i v_i; cos(theta) = <u,v>/(|u||v|); la fraccion de
flujo que recibe un panel plano es max(0, cos(theta)) entre la normal y la
direccion al Sol. Gram-Schmidt clasico y modificado.
Supuestos: panel plano, sin sombras, sin reflexion. Validez: solo geometria.
Tolerancia: 1e-12 en identidades; la perdida de ortogonalidad se informa.
"""
from __future__ import annotations
import platform
import numpy as np


def angulo(u, v):
    c = (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return np.degrees(np.arccos(np.clip(c, -1.0, 1.0)))


def gs_clasico(A):
    Q = np.zeros_like(A, dtype=float)
    for j in range(A.shape[1]):
        v = A[:, j].astype(float).copy()
        for i in range(j):
            v -= (Q[:, i] @ A[:, j]) * Q[:, i]
        Q[:, j] = v / np.linalg.norm(v)
    return Q


def gs_modificado(A):
    Q = np.zeros_like(A, dtype=float)
    for j in range(A.shape[1]):
        v = A[:, j].astype(float).copy()
        for i in range(j):
            v -= (Q[:, i] @ v) * Q[:, i]
        Q[:, j] = v / np.linalg.norm(v)
    return Q


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    # 1. Angulo Sol-panel
    n = np.array([0.0, 0.0, 1.0])
    for elev in (90, 60, 30, 0, -10):
        s = np.array([np.cos(np.radians(elev)), 0.0, np.sin(np.radians(elev))])
        th = angulo(n, s)
        print(f"elevacion {elev:4d} deg -> angulo con la normal = {th:7.3f} deg, factor = {max(0.0, np.cos(np.radians(th))):.4f}")
    s30 = np.array([np.cos(np.radians(30)), 0.0, np.sin(np.radians(30))])
    assert abs(angulo(n, s30) - 60.0) < 1e-9

    # 2. Cauchy-Schwarz y desigualdad triangular
    rng = np.random.default_rng(6)
    for _ in range(1000):
        u, v = rng.normal(size=(2, 5))
        assert abs(u @ v) <= np.linalg.norm(u) * np.linalg.norm(v) + 1e-12
        assert np.linalg.norm(u + v) <= np.linalg.norm(u) + np.linalg.norm(v) + 1e-12
    # Pitagoras para vectores ortogonales
    u, v = np.array([3.0, 0.0, 0.0]), np.array([0.0, 4.0, 0.0])
    assert abs(np.linalg.norm(u + v) - 5.0) < 1e-12

    # 3. Gram-Schmidt sobre vectores independientes
    A = np.array([[1.0, 1.0, 0.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0]])
    Q = gs_clasico(A)
    print("Q^T Q - I (max) =", float(np.abs(Q.T @ Q - np.eye(3)).max()))
    assert np.allclose(Q.T @ Q, np.eye(3), atol=1e-12)
    # 4. Perdida de ortogonalidad con columnas casi paralelas
    eps = 1e-8
    B = np.array([[1, 1, 1], [eps, 0, 0], [0, eps, 0], [0, 0, eps]], float)
    e_c = np.abs(gs_clasico(B).T @ gs_clasico(B) - np.eye(3)).max()
    e_m = np.abs(gs_modificado(B).T @ gs_modificado(B) - np.eye(3)).max()
    print(f"columnas casi paralelas: |Q^T Q - I| clasico = {e_c:.2e}, modificado = {e_m:.2e}")
    assert e_m < e_c
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
