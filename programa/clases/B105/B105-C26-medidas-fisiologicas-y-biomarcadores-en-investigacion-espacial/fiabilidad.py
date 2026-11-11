#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C26: fiabilidad test-retest, error estandar de medida y cambio minimo detectable (datos SINTETICOS).

Modelo: valor medido y_ij = mu_i + e_ij, con mu_i ~ N(100, 10) (variacion entre individuos) y e_ij ~ N(0, 4) (variacion intra + analitica) para el individuo i y la sesion j.
ICC(1,1) por ANOVA de una via: ICC = (MSB - MSW)/(MSB + (k - 1) MSW), k = numero de sesiones. SEM = SD sqrt(1 - ICC); MDC95 = 1.96 sqrt(2) SEM. Verdad: ICC = 100/(100 + 16) = 0.862;
SEM = 4; MDC95 = 11.1. Bland-Altman: sesgo y limites de acuerdo = d_media +- 1.96 SD(d). Semilla 105. Intervalo del ICC por bootstrap de individuos. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

MU, SB, SW = 100.0, 10.0, 4.0


def icc11(y):
    n, k = y.shape
    gm = y.mean()
    msb = k * np.sum((y.mean(axis=1) - gm) ** 2) / (n - 1)
    msw = np.sum((y - y.mean(axis=1, keepdims=True)) ** 2) / (n * (k - 1))
    return (msb - msw) / (msb + (k - 1) * msw), msb, msw


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): mu_i ~ N(100, 10); e ~ N(0, 4); verdad ICC = 0.862, SEM = 4.0, MDC95 = 11.1")
    rng = np.random.default_rng(105)
    icc_v = SB ** 2 / (SB ** 2 + SW ** 2)
    sem_v = SW
    mdc_v = 1.96 * np.sqrt(2) * sem_v
    print(f"Verdad: ICC = {icc_v:.3f}; SEM = {sem_v:.2f}; MDC95 = {mdc_v:.2f}")
    print("n individuos | ICC estimado (media de 2000 repeticiones) [DE] | SEM medio | MDC95 medio | cobertura bootstrap 95 % del ICC (200 rep.)")
    res = {}
    for n in (6, 10, 20, 50, 100):
        iccs, sems, mdcs = [], [], []
        for _ in range(2000):
            mu = rng.normal(MU, SB, n)
            y = mu[:, None] + rng.normal(0, SW, (n, 2))
            i, _, msw = icc11(y)
            iccs.append(i)
            sd = y.std(ddof=1)
            sem = sd * np.sqrt(max(0.0, 1 - i))
            sems.append(sem); mdcs.append(1.96 * np.sqrt(2) * sem)
        # cobertura bootstrap en 200 repeticiones
        cub = 0
        for _ in range(200):
            mu = rng.normal(MU, SB, n)
            y = mu[:, None] + rng.normal(0, SW, (n, 2))
            bs = [icc11(y[rng.integers(0, n, n)])[0] for _ in range(300)]
            lo, hi = np.percentile(bs, [2.5, 97.5])
            cub += (lo <= icc_v <= hi)
        res[n] = (np.mean(iccs), np.std(iccs), np.mean(sems), np.mean(mdcs), cub / 200)
        print(f"   {n:4d}      | {np.mean(iccs):.3f} [{np.std(iccs):.3f}]                              | {np.mean(sems):5.2f}     | {np.mean(mdcs):6.2f}      | {cub / 200:.3f}")
    # Bland-Altman con n = 50
    mu = rng.normal(MU, SB, 50)
    y = mu[:, None] + rng.normal(0, SW, (50, 2)) + np.array([0.0, 1.5])  # sesgo sistematico de +1.5 en la sesion 2
    d = y[:, 1] - y[:, 0]
    print(f"Bland-Altman (n = 50, sesgo sistematico sintetico +1.5): sesgo = {d.mean():.2f}; limites de acuerdo = {d.mean() - 1.96 * d.std(ddof=1):.2f} a {d.mean() + 1.96 * d.std(ddof=1):.2f} (esperado +-{mdc_v:.1f} alrededor de 1.5)")
    # efecto de promediar k sesiones
    for k in (1, 2, 4):
        sem_k = SW / np.sqrt(k)
        print(f"Promedio de {k} sesion(es): SEM = {sem_k:.2f}; MDC95 de la media = {1.96 * np.sqrt(2) * sem_k:.2f}")
    assert abs(res[100][0] - icc_v) < 0.03
    assert res[6][1] > res[100][1]
    assert abs(res[100][3] - mdc_v) < 1.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
