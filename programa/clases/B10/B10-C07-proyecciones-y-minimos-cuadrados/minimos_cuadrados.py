#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C07: proyecciones y minimos cuadrados.

Datos: SINTETICOS. Distancia a una estacion r(t) = a + b t + c t^2 con
a = 100 km, b = 2 km/s, c = -0.05 km/s^2, t = 0..10 s (11 puntos), mas ruido
gaussiano de sigma = 0.05 km (semilla fija). No son mediciones reales.
Modelo: minimizar |A x - y|^2; ecuaciones normales A^T A x = A^T y; QR.
Supuestos: ruido independiente, igual varianza, modelo correcto.
Validez: A de rango completo. Tolerancia: 1e-10 en la ortogonalidad del
residuo; coeficientes dentro de 4 sigma de sus incertidumbres.
"""
from __future__ import annotations
import platform
import numpy as np


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    rng = np.random.default_rng(7)
    t = np.linspace(0.0, 10.0, 11)
    verdad = np.array([100.0, 2.0, -0.05])
    A = np.vander(t, 3, increasing=True)
    sigma = 0.05
    y = A @ verdad + rng.normal(0.0, sigma, size=t.size)

    x_ne = np.linalg.solve(A.T @ A, A.T @ y)          # ecuaciones normales
    Q, R = np.linalg.qr(A)
    x_qr = np.linalg.solve(R, Q.T @ y)                # QR
    x_ls = np.linalg.lstsq(A, y, rcond=None)[0]       # biblioteca (SVD)
    print("verdad          :", verdad)
    print("normales        :", x_ne.round(5))
    print("QR              :", x_qr.round(5))
    print("lstsq           :", x_ls.round(5))
    assert np.allclose(x_ne, x_qr, atol=1e-8) and np.allclose(x_qr, x_ls, atol=1e-8)

    res = y - A @ x_qr
    print("A^T residuo (max) =", float(np.abs(A.T @ res).max()))
    assert np.abs(A.T @ res).max() < 1e-10                 # residuo ortogonal a las columnas
    print(f"rms del residuo = {np.sqrt(res @ res / (t.size - 3)):.4f} km (sigma = {sigma})")

    cov = sigma ** 2 * np.linalg.inv(A.T @ A)
    inc = np.sqrt(np.diag(cov))
    print("incertidumbres (1 sigma):", inc.round(5))
    assert np.all(np.abs(x_qr - verdad) < 4 * inc)

    # proyeccion: y_hat es la proyeccion y P es idempotente y simetrica
    P = A @ np.linalg.solve(A.T @ A, A.T)
    assert np.allclose(P @ P, P, atol=1e-10) and np.allclose(P, P.T, atol=1e-12)
    assert np.allclose(P @ y, A @ x_qr, atol=1e-9)
    print("traza de P =", round(float(np.trace(P)), 10), "(= numero de parametros)")

    # grado alto: las ecuaciones normales pierden precision
    t2 = np.linspace(0.0, 1.0, 40)
    A2 = np.vander(t2, 12, increasing=True)
    xv = np.ones(12)
    y2 = A2 @ xv
    e_ne = np.abs(np.linalg.solve(A2.T @ A2, A2.T @ y2) - xv).max()
    Q2, R2 = np.linalg.qr(A2)
    e_qr = np.abs(np.linalg.solve(R2, Q2.T @ y2) - xv).max()
    print(f"grado 11: cond(A) = {np.linalg.cond(A2):.2e}; error normales = {e_ne:.2e}; error QR = {e_qr:.2e}")
    assert e_qr < e_ne
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
