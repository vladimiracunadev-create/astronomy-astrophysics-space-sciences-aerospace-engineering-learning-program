#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C18: fiabilidad exponencial, redundancia k de n, causa comun y repuestos, verificados por Monte Carlo.

Modelo propio (no consultado en una fuente concreta). Valores ILUSTRATIVOS: tasa de falla de 1e-5 por hora (MTBF 100 000 h) de una unidad, mision de 900 dias (21 600 h),
fraccion de causa comun beta = 0.1, conmutador de espera con fiabilidad 0.95, flota de 12 unidades identicas. Monte Carlo con semilla 106 y 200 000 repeticiones.
Verificacion: las formulas coinciden con el Monte Carlo (cuatro desviaciones tipicas); la fiabilidad de 1 de 2 supera a la de 1 y la de 2 de 3 es menor que la de 1 de 3.
"""
from __future__ import annotations
import math
import platform
import numpy as np

LAM, T, BETA, SW, NFLOTA = 1e-5, 900 * 24.0, 0.1, 0.95, 12


def r1(t=T, lam=LAM):
    return math.exp(-lam * t)


def k_de_n(k, n, r):
    return sum(math.comb(n, j) * r ** j * (1 - r) ** (n - j) for j in range(k, n + 1))


def uno_de_dos_cc(t=T):
    lam_i, lam_c = (1 - BETA) * LAM, BETA * LAM
    ri = math.exp(-lam_i * t)
    return math.exp(-lam_c * t) * (1 - (1 - ri) ** 2)


def poisson_cdf(k, mu):
    return sum(math.exp(-mu) * mu ** j / math.factorial(j) for j in range(k + 1))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: tasa de falla, beta y conmutador ILUSTRATIVOS; Monte Carlo SINTETICO (semilla 106); sin datos de componentes reales")
    R = {}
    r = r1()
    cold = r * (1 + LAM * T) * 1.0
    cold_sw = r + SW * LAM * T * r
    cfg = {
        "1 unidad": r,
        "1 de 2 (calor)": k_de_n(1, 2, r),
        "1 de 3 (calor)": k_de_n(1, 3, r),
        "2 de 3 (votacion)": k_de_n(2, 3, r),
        "1 de 2 con causa comun": uno_de_dos_cc(),
        "espera fria (conm. perfecto)": cold,
        "espera fria (conm. 0.95)": cold_sw,
    }
    print(f"Mision de {T:.0f} h con lambda = {LAM:.0e}/h: lambda t = {LAM*T:.3f}")
    print("   configuracion                      fiabilidad")
    for k, v in cfg.items():
        print(f"   {k:32s}   {v:.5f}")
    R["cfg"] = cfg
    assert cfg["1 de 2 (calor)"] > cfg["1 unidad"] and cfg["2 de 3 (votacion)"] < cfg["1 de 3 (calor)"] and cfg["1 de 2 con causa comun"] < cfg["1 de 2 (calor)"]
    rng = np.random.default_rng(106)
    N = 200000
    x = rng.exponential(1 / LAM, (N, 3))
    mc = {"1 unidad": np.mean(x[:, 0] > T), "1 de 2 (calor)": np.mean((x[:, :2] > T).sum(1) >= 1), "2 de 3 (votacion)": np.mean((x > T).sum(1) >= 2)}
    print("Monte Carlo frente a formula:")
    for k, v in mc.items():
        sd = math.sqrt(v * (1 - v) / N)
        print(f"   {k:20s} MC {v:.5f} +- {sd:.5f}; formula {cfg[k]:.5f}")
        assert abs(v - cfg[k]) < 4 * sd
    mu = NFLOTA * LAM * T
    s = 0
    while poisson_cdf(s, mu) < 0.95:
        s += 1
    R["mu"], R["spares95"] = mu, s
    s99 = 0
    while poisson_cdf(s99, mu) < 0.99:
        s99 += 1
    R["spares99"] = s99
    print(f"Flota de {NFLOTA} unidades: fallas esperadas {mu:.2f}; repuestos para 95 %: {s} (P = {poisson_cdf(s, mu):.4f}); para 99 %: {s99} (P = {poisson_cdf(s99, mu):.4f})")
    print(f"Sin repuestos, P(ninguna falla en la flota) = {math.exp(-mu):.4f}")
    R["p_ningun"] = math.exp(-mu)
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
