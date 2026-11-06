#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C13: matrices de rotacion tridimensional.

Datos: SINTETICOS (angulos y vectores inventados).
Modelo: rotaciones elementales activas Rx, Ry, Rz (mano derecha); formula de
Rodrigues R = I + sin(t) K + (1 - cos t) K^2 con K la matriz antisimetrica del
eje; extraccion de eje y angulo; matriz de transformacion de marco
M = R^T (filas = ejes del marco nuevo expresados en el marco viejo), que es
la convencion de rotacion de coordenadas de SPICE.
Supuestos: aritmetica doble. Validez: angulos en (0, pi) para la extraccion.
Tolerancia: 1e-12 en ortogonalidad y Rodrigues; deriva informada.
"""
from __future__ import annotations
import platform
import numpy as np
from scipy.linalg import expm


def Rx(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])


def Ry(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])


def Rz(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def skew(u):
    return np.array([[0, -u[2], u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]])


def rodrigues(u, t):
    u = np.asarray(u, float) / np.linalg.norm(u)
    K = skew(u)
    return np.eye(3) + np.sin(t) * K + (1 - np.cos(t)) * K @ K


def eje_angulo(R):
    t = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    w = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]])
    return w / np.linalg.norm(w), t


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    a, b = np.radians(90), np.radians(90)
    for R in (Rx(a), Ry(a), Rz(a), Rz(a) @ Rx(b)):
        assert np.allclose(R.T @ R, np.eye(3), atol=1e-12) and abs(np.linalg.det(R) - 1) < 1e-12
    A, B = Rz(a) @ Rx(b), Rx(b) @ Rz(a)
    print("Rz(90)Rx(90) =\n", A.round(12))
    print("Rx(90)Rz(90) =\n", B.round(12))
    assert not np.allclose(A, B)
    u, t = eje_angulo(A)
    print("eje-angulo de Rz(90)Rx(90): eje =", u.round(6), "angulo =", round(float(np.degrees(t)), 6), "grados")
    assert abs(np.degrees(t) - 120.0) < 1e-9 and np.allclose(np.abs(u), 1 / np.sqrt(3), atol=1e-9)
    # Rodrigues frente a la exponencial matricial
    for ax, ang in (([0, 0, 1], 0.7), ([1, 2, 3], 2.1), ([-1, 0.5, 2], 3.0)):
        ax = np.array(ax, float) / np.linalg.norm(ax)
        assert np.allclose(rodrigues(ax, ang), expm(ang * skew(ax)), atol=1e-12)
    assert np.allclose(rodrigues([0, 0, 1], 0.9), Rz(0.9), atol=1e-12)
    # vector activo y marco (SPICE): M = R^T
    w = np.radians(30)
    M = Rz(w).T
    print("filas de M = ejes del marco nuevo en el viejo:", M[0].round(6), M[1].round(6), M[2].round(6))
    assert np.allclose(M[0], [np.cos(w), np.sin(w), 0], atol=1e-12)
    v = np.array([1.0, 0.0, 0.0])
    print("v en el marco nuevo (M v) =", (M @ v).round(6), "| vector rotado -w (Rz(-w) v) =", (Rz(-w) @ v).round(6))
    assert np.allclose(M @ v, Rz(-w) @ v, atol=1e-12)
    # composicion de marcos: M_total = M2 M1
    M1, M2 = Rz(0.3).T, Rx(0.5).T
    v0 = np.array([0.2, -0.4, 0.9])
    assert np.allclose(M2 @ (M1 @ v0), (M2 @ M1) @ v0, atol=1e-12)
    # deriva numerica al componer muchas rotaciones pequenas
    R = np.eye(3)
    paso = rodrigues([1, 1, 1], 1e-3)
    for _ in range(1_000_000):
        R = paso @ R
    err = np.abs(R.T @ R - np.eye(3)).max()
    U, _, Vt = np.linalg.svd(R)
    Rn = U @ Vt
    print(f"tras 1e6 productos: |R^T R - I| = {err:.2e}; tras re-ortonormalizar: {np.abs(Rn.T @ Rn - np.eye(3)).max():.2e}; det = {np.linalg.det(Rn):.12f}")
    assert np.abs(Rn.T @ Rn - np.eye(3)).max() < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
