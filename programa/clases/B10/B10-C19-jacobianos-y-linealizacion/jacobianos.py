#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C19: jacobianos, linealizacion y propagacion de errores.

Datos: SINTETICOS. Medida de una estacion: distancia r = 1000 km, azimut
30 grados, elevacion 40 grados; incertidumbres sigma_r = 0.1 km,
sigma_az = sigma_el = 1e-4 rad (inventadas).
Modelo: x = r cos(el) cos(az), y = r cos(el) sin(az), z = r sin(el).
Jacobiano analitico contrastado con diferencias centrales; det J = r^2 cos(el).
Propagacion lineal: C_x = J C J^T. Contraste con Monte Carlo (semilla fija).
Supuestos: errores gaussianos independientes y pequenos. Tolerancia: 1e-7
relativa en el jacobiano; 3 % en la covarianza lineal frente a Monte Carlo.
"""
from __future__ import annotations
import platform
import numpy as np


def f(p):
    r, az, el = p
    return np.array([r * np.cos(el) * np.cos(az), r * np.cos(el) * np.sin(az), r * np.sin(el)])


def J_analitico(p):
    r, az, el = p
    ca, sa, ce, se = np.cos(az), np.sin(az), np.cos(el), np.sin(el)
    return np.array([[ce * ca, -r * ce * sa, -r * se * ca],
                     [ce * sa, r * ce * ca, -r * se * sa],
                     [se, 0.0, r * ce]])


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    p0 = np.array([1000.0, np.radians(30), np.radians(40)])
    J = J_analitico(p0)
    Jn = np.zeros((3, 3))
    for j in range(3):
        h = 1e-6 * max(1.0, abs(p0[j]))
        e = np.zeros(3); e[j] = h
        Jn[:, j] = (f(p0 + e) - f(p0 - e)) / (2 * h)
    err = np.abs(J - Jn).max() / np.abs(J).max()
    print("J =\n", J.round(6))
    print(f"error relativo vs diferencias centrales = {err:.2e}")
    assert err < 1e-7
    d = np.linalg.det(J)
    print(f"det J = {d:.6f} | r^2 cos(el) = {p0[0] ** 2 * np.cos(p0[2]):.6f}")
    assert abs(d - p0[0] ** 2 * np.cos(p0[2])) < 1e-6
    # linealizacion: error frente al desplazamiento
    dirn = np.array([1.0, 1.0, 1.0]) / np.sqrt(3)
    print("escala del paso   error de la linealizacion (km)")
    prev = None
    for s in (1e-1, 1e-2, 1e-3):
        dp = s * dirn * np.array([1000.0, 1.0, 1.0])
        exacto = f(p0 + dp) - f(p0)
        lineal = J @ dp
        e = np.linalg.norm(exacto - lineal)
        print(f"{s:10.0e}   {e:.4e}   (|dx| = {np.linalg.norm(exacto):.4e} km)")
        if prev is not None:
            assert e < prev / 50          # cuadratico: x10 en el paso => ~x100 en el error
        prev = e
    # propagacion de errores
    C = np.diag([0.1 ** 2, 1e-8, 1e-8])
    Cx = J @ C @ J.T
    rng = np.random.default_rng(19)
    muestras = rng.multivariate_normal(p0, C, size=400_000)
    X = np.array([f(q) for q in muestras[:100_000]])
    Cmc = np.cov(X.T)
    print("sigma lineal (km) =", np.sqrt(np.diag(Cx)).round(6))
    print("sigma Monte Carlo (km) =", np.sqrt(np.diag(Cmc)).round(6))
    assert np.abs(Cmc - Cx).max() / np.abs(Cx).max() < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
