#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C03: matrices como operadores lineales.

Datos: omega = 7.292115e-5 rad/s (IERS, TN36, tabla 1.2, GRS80, valor
nominal); radio ecuatorial 6378.137 km y periodo sideral 23.9345 h (NASA,
ficha de la Tierra). Modelo: la matriz de un operador en una base;
composicion = producto. Supuestos: Tierra rigida con rotacion uniforme; sin
precesion ni movimiento polar (simplificacion didactica). Validez: horas.
Tolerancia: 1e-12 en identidades; 1e-3 h frente al periodo de la ficha.
"""
from __future__ import annotations
import platform
import numpy as np

OMEGA = 7.292115e-5       # rad/s


def Rz(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s], [s, c]])


def matriz_derivada(n):
    """Matriz de d/dx sobre polinomios {1, x, ..., x^n} (n+1 x n+1)."""
    D = np.zeros((n + 1, n + 1))
    for k in range(1, n + 1):
        D[k - 1, k] = k
    return D


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    est0 = np.array([6378.137, 0.0])
    t = 3600.0
    est = Rz(OMEGA * t) @ est0
    print(f"giro en 1 h = {np.degrees(OMEGA * t):.4f} grados; estacion -> {est.round(3)} km")
    assert abs(np.linalg.norm(est) - 6378.137) < 1e-9
    T = 2 * np.pi / OMEGA
    print(f"periodo = {T:.2f} s = {T / 3600:.5f} h (ficha NASA: 23.9345 h)")
    assert abs(T / 3600 - 23.9345) < 1e-3
    assert np.allclose(Rz(OMEGA * T), np.eye(2), atol=1e-12)

    A = Rz(np.radians(30))
    S = np.diag([2.0, 1.0])
    print("A S - S A =\n", (A @ S - S @ A).round(6))
    assert not np.allclose(A @ S, S @ A)
    assert np.allclose(Rz(1.0) @ Rz(0.5), Rz(1.5), atol=1e-12)

    M = np.random.default_rng(3).normal(size=(3, 3))
    x, y = np.random.default_rng(4).normal(size=(2, 3))
    a, b = 2.0, -3.0
    assert np.allclose(M @ (a * x + b * y), a * (M @ x) + b * (M @ y), atol=1e-12)
    f = lambda z: np.linalg.norm(z) * np.ones(3)
    assert not np.allclose(f(a * x + b * y), a * f(x) + b * f(y))

    D = matriz_derivada(3)
    p = np.array([2.0, 3.0, 0.0, -1.0])
    print("D p =", D @ p)
    assert np.allclose(D @ p, [3.0, 0.0, -3.0, 0.0])
    assert np.allclose(np.linalg.matrix_power(D, 4), 0)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
