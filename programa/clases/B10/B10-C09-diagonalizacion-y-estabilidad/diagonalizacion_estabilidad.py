#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C09: diagonalizacion, exponencial matricial y estabilidad.

Datos: SINTETICOS. Modo de flexion de un panel solar: frecuencia 0.5 Hz
(omega = pi rad/s) y razon de amortiguamiento zeta = 0.02 (valores
didacticos, no de un panel real).
Modelo: x'' + 2 zeta omega x' + omega^2 x = 0, escrito como y' = A y con
y = (x, x'). Solucion y(t) = exp(A t) y0 = V exp(L t) V^-1 y0.
Solucion exacta: x(t) = exp(-zeta omega t)[cos(wd t) + (zeta omega/wd) sin(wd t)]
con x(0)=1, x'(0)=0 y wd = omega sqrt(1 - zeta^2).
Supuestos: sistema lineal e invariante. Validez: pequenas oscilaciones.
Tolerancia: 1e-12 entre exp(At) por diagonalizacion y la solucion exacta.
"""
from __future__ import annotations
import platform
import numpy as np


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    w, z = np.pi, 0.02
    A = np.array([[0.0, 1.0], [-w * w, -2 * z * w]])
    lam, V = np.linalg.eig(A)
    print("autovalores:", np.round(lam, 6))
    wd = w * np.sqrt(1 - z * z)
    esperado = -z * w + 1j * wd
    assert abs(lam[np.argmax(lam.imag)] - esperado) < 1e-12
    assert np.allclose(A @ V, V @ np.diag(lam), atol=1e-12)
    print("traza =", round(float(np.trace(A)), 6), "= suma de autovalores", round(float(lam.sum().real), 6))
    print("det   =", round(float(np.linalg.det(A)), 6), "= producto", round(float((lam[0] * lam[1]).real), 6))

    def expm_diag(t):
        return (V @ np.diag(np.exp(lam * t)) @ np.linalg.inv(V)).real

    def exacta(t):
        return np.exp(-z * w * t) * (np.cos(wd * t) + z * w / wd * np.sin(wd * t))

    y0 = np.array([1.0, 0.0])
    for t in (1.0, 5.0, 10.0, 30.0):
        xd = (expm_diag(t) @ y0)[0]
        print(f"t={t:5.1f} s: x(diag) = {xd: .10f}  x(exacta) = {exacta(t): .10f}")
        assert abs(xd - exacta(t)) < 1e-12
    print(f"vida media de la envolvente: ln2/(zeta omega) = {np.log(2) / (z * w):.3f} s")

    # clasificacion de estabilidad segun la parte real de los autovalores
    for zz in (0.02, 0.0, -0.02):
        Az = np.array([[0.0, 1.0], [-w * w, -2 * zz * w]])
        re = np.linalg.eigvals(Az).real.max()
        print(f"zeta = {zz:+.2f}: max Re(lambda) = {re:+.5f} -> ", "estable" if re < -1e-12 else ("marginal" if abs(re) < 1e-12 else "inestable"))

    # Euler explicito: el sistema continuo es estable, el discreto no
    h = 0.1
    M = np.eye(2) + h * A
    rho = max(abs(np.linalg.eigvals(M)))
    n = 100
    y = y0.copy()
    for _ in range(n):
        y = M @ y
    print(f"Euler explicito h={h}: radio espectral = {rho:.5f}; |x| tras {n} pasos = {abs(y[0]):.3f} (exacta {abs(exacta(n * h)):.4f})")
    assert rho > 1.0 and abs(y[0]) > 10 * abs(exacta(n * h))
    # potencias de matriz por diagonalizacion
    # matriz defectuosa
    D = np.array([[1.0, 1.0], [0.0, 1.0]])
    ld, Vd = np.linalg.eig(D)
    print("defectuosa: cond(V) =", f"{np.linalg.cond(Vd):.2e}", "(autovectores casi paralelos)")
    assert np.linalg.cond(Vd) > 1e8
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
