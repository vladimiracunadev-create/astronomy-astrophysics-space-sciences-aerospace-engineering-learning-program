#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B22-C03: identificabilidad estructural y practica.

Datos: SINTETICOS (no son observaciones). Caida de brillo de un transitorio
y(t) = A1 exp(-k1 t) + A2 exp(-k2 t), t en dias (30 puntos entre 0 y 10),
brillo en unidades arbitrarias, ruido gaussiano sigma = 0.01 (semilla fija 3).
Parametros p = (A1, k1, A2, k2). Caso A (ritmos separados): (1.0, 0.2, 0.8, 2.0) 1/dia.
Caso B (ritmos proximos): (1.0, 0.8, 0.8, 1.0) 1/dia.
Modelo: minimos cuadrados con ruido blanco de sigma conocida. Matriz de
informacion de Fisher F = J^T J / sigma^2; cota de Cramer-Rao: cov >= F^-1.
Supuestos: modelo correcto; ruido gaussiano independiente; linealizacion local.
Validez: cerca de la verdad; el perfil de verosimilitud no la requiere.
Tolerancias: Jacobiano analitico vs diferencias finitas 1e-6; desviacion
tipica empirica (Monte Carlo, 4000 repeticiones) vs cota en el caso lineal 5 %.
"""
from __future__ import annotations
import platform
import numpy as np
from scipy.optimize import least_squares
import scipy

T = np.linspace(0.0, 10.0, 30)
SIGMA = 0.01


def modelo(p, t=T):
    A1, k1, A2, k2 = p
    return A1 * np.exp(-k1 * t) + A2 * np.exp(-k2 * t)


def jacobiano(p, t=T):
    A1, k1, A2, k2 = p
    e1, e2 = np.exp(-k1 * t), np.exp(-k2 * t)
    return np.column_stack([e1, -A1 * t * e1, e2, -A2 * t * e2])


def jac_numerico(p, h=1e-6):
    cols = []
    for i in range(len(p)):
        d = np.zeros(len(p)); d[i] = h
        cols.append((modelo(p + d) - modelo(p - d)) / (2 * h))
    return np.column_stack(cols)


def perfil_k2(y, p0, k2_grid):
    """chi^2 minimo sobre (A1, k1, A2) para cada k2 fijo (verosimilitud de perfil).
    Se recorre la rejilla desde el k2 mas cercano a p0[3] hacia cada extremo,
    usando como arranque la solucion del punto anterior (evita minimos locales).
    Se impone k1 = u * k2 con 0 <= u <= 1 (k1 <= k2) para eliminar la simetria de
    etiquetas: intercambiar (A1, k1) con (A2, k2) da exactamente el mismo modelo."""
    out = np.empty(len(k2_grid))
    i0 = int(np.argmin(np.abs(k2_grid - p0[3])))
    for sentido in (+1, -1):
        guess = np.array([p0[0], p0[1] / p0[3], p0[2]])
        idx = range(i0, len(k2_grid)) if sentido == 1 else range(i0, -1, -1)
        for i in idx:
            f = lambda q: (modelo(np.array([q[0], q[1] * k2_grid[i], q[2], k2_grid[i]])) - y) / SIGMA
            sol = least_squares(f, guess, bounds=([0, 0, 0], [50, 1, 50]))
            out[i] = 2.0 * sol.cost         # cost = 0.5 * sum(res^2)
            guess = sol.x
    return out


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__, "| scipy", scipy.__version__)

    # 1) Jacobiano analitico = numerico
    pA = np.array([1.0, 0.2, 0.8, 2.0])
    assert np.allclose(jacobiano(pA), jac_numerico(pA), atol=1e-6)

    # 1b) Simetria de etiquetas: intercambiar (A1,k1) con (A2,k2) no cambia el modelo
    assert np.allclose(modelo(np.array([1.0, 0.2, 0.8, 2.0])), modelo(np.array([0.8, 2.0, 1.0, 0.2])))

    # 2) No identificabilidad estructural: y = (th1 + th2) t
    Js = np.column_stack([T, T])
    print("estructural y=(th1+th2)t: rango de J =", np.linalg.matrix_rank(Js), "(2 parametros)")
    assert np.linalg.matrix_rank(Js) == 1
    assert np.allclose(Js @ [3.0, 1.0], Js @ [0.5, 3.5])      # th1 + th2 = 4 en ambos

    # 3) Caso lineal: cota de Cramer-Rao = covarianza empirica
    Al = np.column_stack([np.ones_like(T), T])
    cov_cr = SIGMA ** 2 * np.linalg.inv(Al.T @ Al)
    rng = np.random.default_rng(3)
    verdad_l = np.array([1.0, 0.05])
    est = np.empty((4000, 2))
    for i in range(4000):
        yy = Al @ verdad_l + rng.normal(0, SIGMA, T.size)
        est[i] = np.linalg.lstsq(Al, yy, rcond=None)[0]
    emp, cr = est.std(axis=0, ddof=1), np.sqrt(np.diag(cov_cr))
    print("lineal: desv. tipica empirica", emp, "| cota", cr)
    assert np.all(np.abs(emp / cr - 1) < 0.05)

    # 4) Identificabilidad practica: Fisher en los casos A y B
    pB = np.array([1.0, 0.8, 0.8, 1.0])
    for nombre, p in (("A (k1=0.2, k2=2.0)", pA), ("B (k1=0.8, k2=1.0)", pB)):
        J = jacobiano(p)
        F = J.T @ J / SIGMA ** 2
        sv = np.linalg.svd(J, compute_uv=False)
        cr = np.sqrt(np.diag(np.linalg.inv(F)))
        print(f"caso {nombre}: cond(J) = {sv[0]/sv[-1]:.2e}; cota 1-sigma (A1,k1,A2,k2) = {cr.round(4)}")
        print(f"   cota relativa de k2 = {cr[3]/p[3]*100:.1f} %")

    # 5) Perfil de verosimilitud de k2 con datos sinteticos (misma semilla)
    for nombre, p in (("A", pA), ("B", pB)):
        rng = np.random.default_rng(3)
        y = modelo(p) + rng.normal(0, SIGMA, T.size)
        grid = np.linspace(0.1, 6.0, 119)
        chi = perfil_k2(y, p, grid)
        chi -= chi.min()
        dentro = grid[chi < 1.0]
        dentro3 = grid[chi < 9.0]
        abierto = lambda v: " (toca el borde de la rejilla: intervalo abierto)" if (v.min() <= grid[0] or v.max() >= grid[-1]) else ""
        print(f"caso {nombre}: k2 verdadero = {p[3]}; k2 optimo del perfil = {grid[np.argmin(chi)]:.3f}; "
              f"intervalo 1-sigma [{dentro.min():.3f}, {dentro.max():.3f}]{abierto(dentro)}; "
              f"3-sigma [{dentro3.min():.3f}, {dentro3.max():.3f}]{abierto(dentro3)}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
