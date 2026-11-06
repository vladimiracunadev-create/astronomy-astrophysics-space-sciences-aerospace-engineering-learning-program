#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B22-C05: pruebas de inversion con datos sinteticos y el "crimen inverso".

Datos: SINTETICOS (no son observaciones). Perfil verdadero con bordes: x(s) = 1 para
0.31 < s < 0.62 y 0.4 para 0.75 < s < 0.85, en 0 <= s <= 1 (unidades arbitrarias).
Modelo directo continuo: b(s_i) = integral G(s_i - u) x(u) du, G gaussiana de ancho
w = 0.05, calculado con una rejilla FINA de 1000 puntos (regla del punto medio).
Inversion: rejilla GRUESA de n = 30 incognitas con 30 datos; Tikhonov (L = I) con
lam elegido por el principio de discrepancia ||A x - b|| = sigma sqrt(n).
Dos experimentos: (1) CRIMEN INVERSO: datos fabricados con el mismo modelo grueso
que luego se usa para invertir; (2) PRUEBA HONESTA: datos fabricados con el modelo fino.
Ruido gaussiano de desviacion tipica sigma (se barre de 1e-6 a 1e-2), semilla 5.
Mas: prueba de cobertura (regresion lineal bien planteada, 1-sigma debe cubrir ~68 %).
Supuestos: sigma conocida; ruido blanco; nucleo conocido.
Tolerancias: modelo grueso vs fino coinciden a 1e-2 en el caso suave de prueba (verifica
la discretizacion); cobertura 1-sigma entre 66 % y 70 % con 4000 repeticiones.
"""
from __future__ import annotations
import platform
import numpy as np

W = 0.05


def nucleo(si, sj_matriz_u):
    return np.exp(-((si[:, None] - sj_matriz_u[None, :]) ** 2) / (2 * W ** 2)) / (W * np.sqrt(2 * np.pi))


def operador(s_datos, n_inc):
    """Matriz (len(s_datos) x n_inc) con la regla del punto medio en n_inc celdas de [0,1]."""
    u = (np.arange(n_inc) + 0.5) / n_inc
    return nucleo(s_datos, u) / n_inc, u


def perfil(u):
    return np.where((u > 0.31) & (u < 0.62), 1.0, 0.0) + np.where((u > 0.75) & (u < 0.85), 0.4, 0.0)


def tikhonov_discrepancia(A, b, sigma):
    U, sv, Vt = np.linalg.svd(A)
    beta = U.T @ b
    lams = np.logspace(-8, 1, 181)
    n = len(b)
    mejor = None
    for lam in lams:
        f = sv ** 2 / (sv ** 2 + lam ** 2)
        x = Vt.T @ (f * beta / sv)
        r = np.linalg.norm(A @ x - b)
        if mejor is None or abs(r - sigma * np.sqrt(n)) < mejor[0]:
            mejor = (abs(r - sigma * np.sqrt(n)), lam, x)
    return mejor[2], mejor[1]


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    n = 30
    s_dat = (np.arange(n) + 0.5) / n          # 30 datos en los centros de las celdas gruesas
    A_c, u_c = operador(s_dat, n)             # modelo grueso (el del inversor)
    A_f, u_f = operador(s_dat, 1000)          # modelo fino (la "realidad" simulada)
    x_fino = perfil(u_f)
    x_grueso = perfil(u_c)
    b_fino = A_f @ x_fino                     # dato honesto sin ruido
    b_crimen = A_c @ x_grueso                 # dato del crimen inverso sin ruido

    # Prueba de la discretizacion con un perfil suave: modelo grueso ~ fino
    suave = lambda u: np.exp(-((u - 0.5) / 0.15) ** 2)
    dif = np.abs(A_c @ suave(u_c) - A_f @ suave(u_f)).max() / np.abs(A_f @ suave(u_f)).max()
    print(f"discretizacion (perfil suave): diferencia relativa grueso-fino = {dif:.2e}")
    assert dif < 1e-2
    disc = np.abs(b_crimen - b_fino).max() / np.abs(b_fino).max()
    print(f"discrepancia de modelo con el perfil con bordes: {disc:.2e} (relativa al maximo del dato)")

    rel = lambda x: np.linalg.norm(x - x_grueso) / np.linalg.norm(x_grueso)
    print("  sigma      error crimen   error honesto   lam crimen  lam honesto")
    filas = []
    for sigma in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2):
        rng = np.random.default_rng(5)
        ruido = rng.normal(0.0, sigma, n)
        xc, lc = tikhonov_discrepancia(A_c, b_crimen + ruido, sigma)
        xh, lh = tikhonov_discrepancia(A_c, b_fino + ruido, sigma)
        filas.append((sigma, rel(xc), rel(xh)))
        print(f"  {sigma:7.0e}    {rel(xc):10.3e}    {rel(xh):10.3e}    {lc:9.2e}  {lh:9.2e}")
    # el crimen subestima el error en el regimen de poco ruido
    assert filas[0][1] < filas[0][2]
    assert filas[1][1] < filas[1][2]

    # Cobertura: regresion lineal y = a + b t (problema BIEN planteado), sigma conocida
    rng = np.random.default_rng(5)
    t = np.linspace(0.0, 10.0, 20)
    Al = np.column_stack([np.ones_like(t), t])
    sig = 0.2
    cov = sig ** 2 * np.linalg.inv(Al.T @ Al)
    ver = np.array([2.0, 0.5])
    cubre = np.zeros(2)
    N = 4000
    for _ in range(N):
        yy = Al @ ver + rng.normal(0, sig, t.size)
        est = np.linalg.lstsq(Al, yy, rcond=None)[0]
        cubre += np.abs(est - ver) < np.sqrt(np.diag(cov))
    cob = cubre / N
    print(f"cobertura 1-sigma de (a, b): {cob.round(4)} (esperado 0.6827)")
    assert np.all((cob > 0.66) & (cob < 0.70))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
