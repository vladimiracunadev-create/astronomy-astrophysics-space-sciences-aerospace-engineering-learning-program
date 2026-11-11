#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C27: psicometria de un cuestionario SINTETICO: alfa de Cronbach, analisis de items y Spearman-Brown.

Cuestionario sintetico de 10 items tipo Likert (1-5) sobre un constructo latente unico (por ejemplo, un cuestionario inventado de 'bienestar percibido'): respuesta continua
z_ij = lambda_j theta_i + e_ij con theta_i ~ N(0,1), cargas lambda_j de 0.7 (items 1-8) y 0.2 (items 9-10, items DEFECTUOSOS a proposito), ruido e_ij ~ N(0, sqrt(1 - lambda_j^2)); se discretiza a 1-5 con
cortes en -1.2, -0.4, 0.4, 1.2. Alfa de Cronbach = k/(k-1) (1 - sum var_j / var_total). Correlacion item-total corregida; alfa si se elimina el item; IC del alfa por bootstrap
de respondientes; Spearman-Brown: rho_k = k r / (1 + (k - 1) r). Valores propios de la matriz de correlaciones para unidimensionalidad. Semilla 105. NO es un instrumento real ni validado. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

CARGAS = np.array([0.7] * 8 + [0.2] * 2)
CORTES = np.array([-1.2, -0.4, 0.4, 1.2])


def generar(n, rng):
    th = rng.normal(0, 1, n)
    z = CARGAS * th[:, None] + rng.normal(0, 1, (n, CARGAS.size)) * np.sqrt(1 - CARGAS ** 2)
    return np.searchsorted(CORTES, z) + 1


def alfa(x):
    k = x.shape[1]
    with np.errstate(divide="ignore", invalid="ignore"):
        return k / (k - 1) * (1 - x.var(axis=0, ddof=1).sum() / x.sum(axis=1).var(ddof=1))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): 10 items Likert 1-5; items 9 y 10 defectuosos (carga 0.2); no es un instrumento real")
    rng = np.random.default_rng(105)
    x = generar(200, rng)
    print(f"n = 200 respondientes; media de items = {x.mean():.2f}; alfa de Cronbach (10 items) = {alfa(x):.3f}")
    tot = x.sum(axis=1)
    print("item  carga verd.  corr. item-total corregida  alfa si se elimina")
    for j in range(10):
        rest = tot - x[:, j]
        r = np.corrcoef(x[:, j], rest)[0, 1]
        sin = np.delete(x, j, axis=1)
        print(f"  {j + 1:2d}     {CARGAS[j]:.1f}            {r:6.3f}                    {alfa(sin):.3f}")
    buenos = x[:, :8]
    print(f"Alfa con solo los items 1-8 = {alfa(buenos):.3f}")
    rb = []
    for _ in range(2000):
        rb.append(alfa(x[rng.integers(0, 200, 200)]))
    print(f"IC bootstrap 95 % del alfa (10 items, n = 200) = {np.percentile(rb, 2.5):.3f} - {np.percentile(rb, 97.5):.3f}")
    print("Efecto del tamano de la muestra en el IC del alfa (items 1-8):")
    anch = {}
    for n in (6, 20, 50, 200, 1000):
        xs = generar(n, rng)[:, :8]
        bs = []
        for _ in range(1000):
            idx = rng.integers(0, n, n)
            a = alfa(xs[idx])
            bs.append(a)
        lo, hi = np.nanpercentile(bs, [2.5, 97.5])
        anch[n] = hi - lo
        print(f"  n = {n:5d}: alfa = {alfa(xs):.3f}; IC95 = {lo:.3f} - {hi:.3f} (ancho {hi - lo:.3f})")
    # Spearman-Brown: correlacion media entre items buenos
    c = np.corrcoef(buenos.T)
    rbar = (c.sum() - 8) / (8 * 7)
    print(f"Correlacion media entre los items 1-8 = {rbar:.3f}")
    for k in (4, 8, 16):
        print(f"  Spearman-Brown con k = {k:2d} items: confiabilidad = {k * rbar / (1 + (k - 1) * rbar):.3f}")
    ev = np.sort(np.linalg.eigvalsh(np.corrcoef(x.T)))[::-1]
    print("Valores propios de la matriz de correlaciones: " + ", ".join(f"{v:.2f}" for v in ev[:4]) + f"; primero/segundo = {ev[0] / ev[1]:.2f}")
    assert alfa(buenos) > alfa(x)
    assert anch[6] > anch[200]
    assert ev[0] / ev[1] > 2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
