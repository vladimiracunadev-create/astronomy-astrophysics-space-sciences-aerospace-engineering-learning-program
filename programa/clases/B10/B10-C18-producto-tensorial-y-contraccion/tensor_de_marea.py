#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C18: producto tensorial, contraccion y tensor de marea.

Datos: GM de la Tierra = 3.986005e14 m3/s2 (IERS, TN36, tabla 1.2, GRS80).
Satelite SINTETICO a r = 7000 km del centro.
Modelo: g(x) = -GM x/|x|^3; su gradiente es T_ij = dg_i/dx_j =
(GM/r^3)(3 n_i n_j - delta_ij), n = x/|x| (tensor de marea de dos cuerpos).
Supuestos: masa puntual central. Validez: desplazamientos << r.
Tolerancia: 1e-6 relativa frente a la diferencia finita; traza 1e-18 s^-2.
"""
from __future__ import annotations
import platform
import numpy as np

GM = 3.986005e14


def g(x):
    return -GM * x / np.linalg.norm(x) ** 3


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    a, b = np.array([1.0, 2.0, 3.0]), np.array([4.0, 5.0, 6.0])
    O = np.einsum("i,j->ij", a, b)
    assert np.allclose(O, np.outer(a, b)) and np.linalg.matrix_rank(O) == 1
    assert abs(np.einsum("ii", O) - a @ b) < 1e-12           # contraccion = producto escalar
    assert np.allclose(np.einsum("ij,j->i", O, b), a * (b @ b))
    print("traza(a (x) b) =", np.trace(O), "= a.b =", a @ b)

    r = 7.0e6
    x0 = np.array([r, 0.0, 0.0])
    n = x0 / r
    T = GM / r ** 3 * (3 * np.outer(n, n) - np.eye(3))
    print("GM/r^3 =", f"{GM / r ** 3:.6e}", "s^-2")
    print("T (s^-2) =\n", T)
    print("autovalores =", np.linalg.eigvalsh(T))
    assert abs(np.trace(T)) < 1e-15
    assert np.allclose(np.linalg.eigvalsh(T) / (GM / r ** 3), [-1, -1, 2], atol=1e-12)
    # diferencia finita del gradiente de g
    h = 1.0
    J = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(3); e[j] = h
        J[:, j] = (g(x0 + e) - g(x0 - e)) / (2 * h)
    err = np.abs(J - T).max() / np.abs(T).max()
    print(f"gradiente por diferencias centrales: error relativo = {err:.2e}")
    assert err < 1e-6
    # contraccion con un desplazamiento: aceleracion diferencial para 1 m radial y 1 m transversal
    dr = np.array([1.0, 0.0, 0.0]); dt = np.array([0.0, 1.0, 0.0])
    print("da (radial 1 m)      =", np.einsum("ij,j->i", T, dr), "m/s2")
    print("da (transversal 1 m) =", np.einsum("ij,j->i", T, dt), "m/s2")
    # el producto tensorial T = k (3 n(x)n - I) bajo rotacion
    c, s = np.cos(0.7), np.sin(0.7)
    R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    n2 = R @ n
    T2 = GM / r ** 3 * (3 * np.outer(n2, n2) - np.eye(3))
    assert np.allclose(T2, R @ T @ R.T, atol=1e-18)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
