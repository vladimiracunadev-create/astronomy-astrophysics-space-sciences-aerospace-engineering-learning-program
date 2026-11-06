#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C17: notacion indicial y tensor de inercia.

Datos: SINTETICOS. Cuatro masas puntuales (kg, m): 2 en (+-1,0,0) y 1 en
(0,+-2,0), giradas 30 grados alrededor de z.
Modelo: I_ij = sum_n m_n (r_n.r_n delta_ij - r_ni r_nj); ley de
transformacion I' = R I R^T; identidad e_ijk e_ilm = d_jl d_km - d_jm d_kl.
Supuestos: cuerpo rigido de masas puntuales. Validez: este conjunto.
Tolerancia: 1e-12.
"""
from __future__ import annotations
import platform
import numpy as np

delta = np.eye(3)
eps = np.zeros((3, 3, 3))
for (i, j, k), s in {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}.items():
    eps[i, j, k] = s


def Rz(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])


def inercia(m, r):
    return sum(mn * (rn @ rn * delta - np.outer(rn, rn)) for mn, rn in zip(m, r))


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    # identidades
    lhs = np.einsum("ijk,ilm->jklm", eps, eps)
    rhs = np.einsum("jl,km->jklm", delta, delta) - np.einsum("jm,kl->jklm", delta, delta)
    assert np.allclose(lhs, rhs, atol=1e-12)
    a, b = np.array([1.0, 2.0, 3.0]), np.array([-1.0, 0.5, 2.0])
    assert np.allclose(np.einsum("ijk,j,k->i", eps, a, b), np.cross(a, b), atol=1e-12)
    print("a x b (indicial) =", np.einsum("ijk,j,k->i", eps, a, b), "| a.b =", np.einsum("i,i", a, b))
    # inercia
    m = np.array([2.0, 2.0, 1.0, 1.0])
    r0 = np.array([[1, 0, 0], [-1, 0, 0], [0, 2, 0], [0, -2, 0]], float)
    I0 = inercia(m, r0)
    print("I0 =\n", I0)
    assert np.allclose(np.diag(I0), [8, 4, 12], atol=1e-12)
    R = Rz(np.radians(30))
    r1 = r0 @ R.T
    I1 = inercia(m, r1)
    print("I (giradas 30 grados) =\n", I1.round(6))
    assert np.allclose(I1, R @ I0 @ R.T, atol=1e-12)
    assert np.allclose(np.einsum("ia,jb,ab->ij", R, R, I0), I1, atol=1e-12)
    w = np.linalg.eigvalsh(I1)
    print("autovalores =", w.round(9), "| traza =", round(float(np.trace(I1)), 9), "| 2*sum m r^2/..: ", round(float(np.einsum('n,ni,ni->', m, r1, r1) * 2), 9))
    assert np.allclose(w, [4, 8, 12], atol=1e-12)
    assert abs(np.trace(I1) - 2 * np.einsum("n,ni,ni->", m, r1, r1)) < 1e-12
    # energia cinetica de rotacion T = 1/2 w_i I_ij w_j frente a suma directa
    om = np.array([0.1, -0.2, 0.3])
    T = 0.5 * np.einsum("i,ij,j", om, I1, om)
    v = np.cross(om, r1)
    T2 = 0.5 * np.einsum("n,ni,ni->", m, v, v)
    print(f"T = {T:.9f} J (indicial) | {T2:.9f} J (directa)")
    assert abs(T - T2) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
