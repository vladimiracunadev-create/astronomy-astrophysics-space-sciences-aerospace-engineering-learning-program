#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C11: valores singulares, rango efectivo y bajo rango.

Datos: SINTETICOS. (1) Matriz de 6 x 3 con una columna casi redundante
(c3 = c1 + c2 + 1e-9 * ruido). (2) "Imagen" de 40 x 40 formada por 3 patrones
separables mas ruido gaussiano de 1e-3 (semilla fija).
Modelo: A = U S V^T. Teorema de Eckart-Young: el mejor aproximante de rango
k en norma 2 tiene error sigma_{k+1}; en norma de Frobenius, raiz de la suma
de sigma_j^2 con j > k.
Supuestos: aritmetica doble. Validez: matrices reales.
Tolerancia: 1e-10 en las identidades.
"""
from __future__ import annotations
import platform
import numpy as np


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    rng = np.random.default_rng(11)
    C = rng.normal(size=(6, 2))
    A = np.column_stack([C, C[:, 0] + C[:, 1] + 1e-9 * rng.normal(size=6)])
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    print("valores singulares de A:", [f"{x:.4e}" for x in s])
    assert np.allclose(U @ np.diag(s) @ Vt, A, atol=1e-12)
    assert np.allclose(U.T @ U, np.eye(3), atol=1e-12) and np.allclose(Vt @ Vt.T, np.eye(3), atol=1e-12)
    rango_efectivo = int(np.sum(s > 1e-6 * s[0]))
    print("rango efectivo (umbral 1e-6 relativo) =", rango_efectivo, "| cond(A) =", f"{s[0] / s[-1]:.3e}")
    assert rango_efectivo == 2
    assert abs(np.linalg.norm(A, "fro") ** 2 - (s ** 2).sum()) < 1e-10
    assert abs(np.linalg.norm(A, 2) - s[0]) < 1e-12

    # cond(A^T A) = cond(A)^2
    B = rng.normal(size=(8, 4))
    sb = np.linalg.svd(B, compute_uv=False)
    cA = sb[0] / sb[-1]
    cAA = np.linalg.cond(B.T @ B)
    print(f"cond(B) = {cA:.4f}; cond(B)^2 = {cA ** 2:.4f}; cond(B^T B) = {cAA:.4f}")
    assert abs(cAA / cA ** 2 - 1) < 1e-6

    # imagen sintetica de bajo rango
    x = np.linspace(0, 1, 40)
    patrones = [np.outer(np.sin(np.pi * (k + 1) * x), np.cos(np.pi * (k + 1) * x)) * (10.0 / (k + 1)) for k in range(3)]
    I = sum(patrones) + 1e-3 * rng.normal(size=(40, 40))
    Ui, si, Vti = np.linalg.svd(I)
    print("primeros 6 valores singulares de la imagen:", [f"{v:.4g}" for v in si[:6]])
    for k in (1, 2, 3, 5):
        Ik = (Ui[:, :k] * si[:k]) @ Vti[:k]
        e2 = np.linalg.norm(I - Ik, 2)
        ef = np.linalg.norm(I - Ik, "fro")
        almacen = k * (40 + 40 + 1)
        print(f"k={k}: error (norma 2) = {e2:.4e} = sigma_(k+1) = {si[k]:.4e}; Frobenius = {ef:.4e}; almacenamiento {almacen}/{40 * 40}")
        assert abs(e2 - si[k]) < 1e-10
        assert abs(ef - np.sqrt((si[k:] ** 2).sum())) < 1e-10
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
