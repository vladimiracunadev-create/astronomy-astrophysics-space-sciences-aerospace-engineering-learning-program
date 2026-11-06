#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B22-C01: problema directo, problema inverso y mal condicionamiento.

Datos: SINTETICOS (no son observaciones). Un perfil de brillo x(s) en n = 40
posiciones, 0 <= s <= 1 (unidades arbitrarias), se emborrona con un nucleo
gaussiano de ancho w = 0.05 (modelo del telescopio) y se le suma ruido
gaussiano de desviacion tipica 1e-3 (semilla fija).
Modelo directo: b = A x, A[i, j] = h * exp(-(s_i - s_j)^2 / (2 w^2)) / (w sqrt(2 pi)),
con h = 1/(n - 1) (regla del rectangulo); ruido solo en b.
Supuestos: nucleo conocido y exacto, invariante por desplazamiento, ruido blanco.
Validez: n = 40; los valores numericos de cond(A) dependen de n y w.
Tolerancias: caso analitico 2x2 a 1e-9 (relativa); cota de propagacion exacta;
recuperacion sin ruido con error relativo < 1e-3 (limitado por cond(A) * 2.2e-16).
"""
from __future__ import annotations
import platform
import numpy as np


def condicion_2x2_analitica(eps: float) -> float:
    """cond_2 de A = [[1, 1], [1, 1 + eps]] (simetrica definida positiva).
    Autovalores: ((2 + eps) +- sqrt(eps^2 + 4)) / 2; cond = lambda_max / lambda_min."""
    r = np.sqrt(eps ** 2 + 4.0)
    return ((2.0 + eps) + r) / ((2.0 + eps) - r)


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)

    # 1) Prueba analitica del numero de condicion
    for eps in (1e-1, 1e-3):
        A2 = np.array([[1.0, 1.0], [1.0, 1.0 + eps]])
        sv = np.linalg.svd(A2, compute_uv=False)
        c_svd, c_ana = sv[0] / sv[-1], condicion_2x2_analitica(eps)
        print(f"2x2 eps={eps:g}: cond SVD = {c_svd:.6f}, cond analitica = {c_ana:.6f}")
        assert abs(c_svd - c_ana) / c_ana < 1e-9

    # 2) Problema directo: emborronar un perfil
    n, w, sigma = 40, 0.05, 1e-3
    s = np.linspace(0.0, 1.0, n)
    h = 1.0 / (n - 1)
    A = h * np.exp(-((s[:, None] - s[None, :]) ** 2) / (2 * w ** 2)) / (w * np.sqrt(2 * np.pi))
    x_ver = np.exp(-((s - 0.3) ** 2) / (2 * 0.04 ** 2)) + 0.6 * np.exp(-((s - 0.7) ** 2) / (2 * 0.06 ** 2))
    b_limpio = A @ x_ver
    rng = np.random.default_rng(22)
    ruido = rng.normal(0.0, sigma, size=n)
    b = b_limpio + ruido

    sv = np.linalg.svd(A, compute_uv=False)
    cond = sv[0] / sv[-1]
    assert np.isclose(cond, np.linalg.cond(A), rtol=1e-6)
    print(f"valores singulares: sigma_1 = {sv[0]:.3e}, sigma_10 = {sv[9]:.3e}, "
          f"sigma_20 = {sv[19]:.3e}, sigma_40 = {sv[-1]:.3e}")
    print(f"cond(A) = {cond:.3e}")

    # 3) Problema inverso ingenuo
    rel = lambda a, b_: np.linalg.norm(a - b_) / np.linalg.norm(b_)
    x_sin = np.linalg.solve(A, b_limpio)
    x_con = np.linalg.solve(A, b)
    e_sin, e_con = rel(x_sin, x_ver), rel(x_con, x_ver)
    print(f"error relativo sin ruido (solo redondeo): {e_sin:.3e}")
    print(f"error relativo con ruido sigma = {sigma:g}: {e_con:.3e}")
    print(f"error relativo de los datos ||ruido||/||b||: {np.linalg.norm(ruido)/np.linalg.norm(b):.3e}")
    assert e_sin < 1e-3                    # sin ruido se recupera casi exacto
    assert e_con > 10.0                    # con ruido, la inversion ingenua es inservible

    # 4) Cota de propagacion: ||dx||/||x|| <= cond * ||db||/||b||  (siempre se cumple)
    cota = cond * np.linalg.norm(ruido) / np.linalg.norm(b_limpio)
    print(f"cota cond*||db||/||b|| = {cota:.3e} (>= error {e_con:.3e})")
    assert e_con <= cota

    # 5) No unicidad: 2 datos (sumas de a pares), 3 incognitas -> espacio nulo
    B = np.array([[1.0, 1.0, 0.0], [0.0, 1.0, 1.0]])
    v_nulo = np.array([1.0, -1.0, 1.0])
    x1 = np.array([1.0, 2.0, 3.0])
    x2 = x1 + 2.5 * v_nulo
    print("B x1 =", B @ x1, "| B x2 =", B @ x2, "(mismos datos, soluciones distintas)")
    assert np.allclose(B @ v_nulo, 0.0) and np.allclose(B @ x1, B @ x2)
    assert np.linalg.matrix_rank(B) == 2   # rango 2 < 3 incognitas
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
