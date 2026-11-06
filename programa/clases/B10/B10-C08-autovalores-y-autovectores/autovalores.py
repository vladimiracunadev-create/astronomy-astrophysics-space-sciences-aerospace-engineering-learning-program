#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C08: autovalores y ejes principales de inercia.

Datos: SINTETICOS. Tensor de inercia de un satelite ficticio, en kg m^2:
I = [[120, -10, 0], [-10, 100, 0], [0, 0, 150]] (simetrico).
Modelo: I v = lambda v; det(I - lambda E) = 0. Los autovalores son los
momentos principales y los autovectores, los ejes principales.
Supuestos: cuerpo rigido; tensor simetrico. Validez: solo este tensor.
Tolerancia: 1e-10 frente a la solucion analitica del bloque 2x2.
"""
from __future__ import annotations
import platform
import numpy as np


def iteracion_potencia(A, it=500):
    v = np.array([1.0, 0.3, 0.2])
    v /= np.linalg.norm(v)
    for _ in range(it):
        w = A @ v
        v = w / np.linalg.norm(w)
    return v @ A @ v, v


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    I = np.array([[120.0, -10.0, 0.0], [-10.0, 100.0, 0.0], [0.0, 0.0, 150.0]])
    w, V = np.linalg.eigh(I)
    print("momentos principales (kg m^2):", w.round(6))
    # solucion analitica del bloque 2x2: 110 +/- sqrt(100 + 100)
    a = np.array([110 - np.sqrt(200), 110 + np.sqrt(200), 150.0])
    assert np.allclose(w, a, atol=1e-10)
    print("traza:", round(float(np.trace(I)), 9), "= suma de autovalores", round(float(w.sum()), 9))
    print("det  :", round(float(np.linalg.det(I)), 6), "= producto", round(float(w.prod()), 6))
    assert abs(np.trace(I) - w.sum()) < 1e-9 and abs(np.linalg.det(I) - w.prod()) < 1e-6
    for k in range(3):
        assert np.allclose(I @ V[:, k], w[k] * V[:, k], atol=1e-10)
    assert np.allclose(V.T @ V, np.eye(3), atol=1e-12)
    # angulo del eje principal mayor del bloque 2x2: tan(2 theta) = 2 Ixy/(Ixx - Iyy)
    th = 0.5 * np.degrees(np.arctan2(2 * -10.0, 120.0 - 100.0))
    print("angulo del eje (tan 2t = 2 Ixy/(Ixx-Iyy)):", round(float(th), 4), "grados")
    v_max = V[:, 1]
    ang = np.degrees(np.arctan2(v_max[1], v_max[0]))
    print("autovector del mayor valor del bloque (grados respecto de x):", round(float(ang), 4))
    # iteracion de la potencia
    lam, v = iteracion_potencia(I)
    print("iteracion de la potencia: lambda mayor =", round(float(lam), 8))
    assert abs(lam - 150.0) < 1e-6
    # no simetrica: autovalores complejos (rotacion)
    R = np.array([[0.0, -1.0], [1.0, 0.0]])
    print("autovalores de R(90 deg):", np.linalg.eigvals(R))
    assert np.allclose(sorted(np.linalg.eigvals(R).imag), [-1.0, 1.0])
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
