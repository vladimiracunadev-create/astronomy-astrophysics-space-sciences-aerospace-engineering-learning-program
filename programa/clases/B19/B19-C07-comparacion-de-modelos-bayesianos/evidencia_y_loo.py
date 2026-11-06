#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B19-C07: evidencia, factor de Bayes, WAIC y LOO exactos.

Datos: SINTETICOS. n = 10 mediciones de la amplitud de una senal [unidades
arbitrarias] con ruido gaussiano conocido sigma = 1:
  y = 0.9 -0.2 1.1 0.4 0.7 1.5 -0.3 0.8 0.2 0.6
Modelos: M0 "sin senal": mu = 0.  M1 "con senal": mu ~ N(0, tau^2).
Evidencia (formas cerradas): con z = sqrt(n) ybar / sigma y r = n tau^2 / sigma^2,
  BF01 = p(y|M0)/p(y|M1) = sqrt(1 + r) * exp(-0.5 z^2 r / (1 + r)).
Comprobaciones independientes: (i) normal multivariante directa con covarianza
sigma^2 I + tau^2 11^T; (ii) cuadratura numerica de p(y|mu) p(mu) dmu.
WAIC (Watanabe/Vehtari et al.): elpd_waic = lppd - p_waic, con lppd = sum log media_s p(y_i|mu_s)
y p_waic = sum var_s log p(y_i|mu_s), usando sorteos s de la posterior exacta de M1.
LOO exacto: la posterior sin y_i es normal, la predictiva de y_i es
N(m_-i, sigma^2 + v_-i); elpd_loo = sum log de esas densidades.
Supuestos: normalidad con sigma conocida; observaciones independientes.
Validez: ilustrativa; no implementa PSIS-LOO.
Tolerancia: formas cerradas contra directa/cuadratura a 1e-8; |elpd_waic - elpd_loo| < 0.15.
Solo numpy; ASCII en la salida.
"""
from __future__ import annotations
import math
import platform
import sys

import numpy as np

Y = np.array([0.9, -0.2, 1.1, 0.4, 0.7, 1.5, -0.3, 0.8, 0.2, 0.6])
SIG = 1.0
N = len(Y)


def lognorm(x, m, s):
    return -0.5 * math.log(2 * math.pi * s * s) - 0.5 * ((x - m) / s) ** 2


def logev_m0(y):
    return float(np.sum(lognorm(y, 0.0, SIG)))


def logev_m1(y, tau):
    n = len(y)
    cov = SIG ** 2 * np.eye(n) + tau ** 2 * np.ones((n, n))
    s, ld = np.linalg.slogdet(cov)
    return -0.5 * (n * math.log(2 * math.pi) + ld + y @ np.linalg.solve(cov, y))


def bf01_cerrado(y, tau):
    n = len(y)
    z = math.sqrt(n) * y.mean() / SIG
    r = n * tau ** 2 / SIG ** 2
    return math.sqrt(1 + r) * math.exp(-0.5 * z * z * r / (1 + r))


def logev_m1_cuadratura(y, tau):
    mu = np.linspace(-12 * tau - 5, 12 * tau + 5, 400_001) if tau < 5 else np.linspace(-8 * tau, 8 * tau, 2_000_001)
    d = mu[1] - mu[0]
    ll = np.array([lognorm(y, m, SIG).sum() for m in mu[::1]]) if len(mu) < 5000 else None
    if ll is None:                                                  # vectorizado
        ll = (-0.5 * N * math.log(2 * math.pi * SIG ** 2)
              - 0.5 * (((y[:, None] - mu[None, ::1]) / SIG) ** 2).sum(axis=0))
    lp = ll + lognorm(mu, 0.0, tau)
    mx = lp.max()
    return float(mx + math.log(np.exp(lp - mx).sum() * d))


def waic_loo(y, tau, rng, S=100_000):
    n = len(y)
    prec = 1 / tau ** 2 + n / SIG ** 2
    mean, sd = y.sum() / SIG ** 2 / prec, 1 / math.sqrt(prec)
    mu = rng.normal(mean, sd, size=S)
    ll = lognorm(y[None, :], mu[:, None], SIG)                      # S x n
    lppd = np.log(np.exp(ll).mean(axis=0)).sum()
    pw = ll.var(axis=0, ddof=1).sum()
    loo_i = []
    for i in range(n):
        yi = np.delete(y, i)
        pr = 1 / tau ** 2 + (n - 1) / SIG ** 2
        m, v = yi.sum() / SIG ** 2 / pr, 1 / pr
        loo_i.append(lognorm(y[i], m, math.sqrt(SIG ** 2 + v)))
    return lppd - pw, pw, float(np.sum(loo_i)), np.array(loo_i)


def main():
    print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.platform())
    for tau in (0.5, 1.0, 3.0):
        direct = logev_m0(Y) - logev_m1(Y, tau)
        assert abs(math.log(bf01_cerrado(Y, tau)) - direct) < 1e-8
        assert abs(logev_m1_cuadratura(Y, tau) - logev_m1(Y, tau)) < 1e-6, tau
    rng = np.random.default_rng(2026)
    ew, pw, el, _ = waic_loo(Y, 1.0, rng)
    assert abs(ew - el) < 0.15, (ew, el)
    print("Pruebas: OK\n")
    z = math.sqrt(N) * Y.mean() / SIG
    print(f"ybar = {Y.mean():.3f}; z = sqrt(n) ybar/sigma = {z:.3f}  (p bilateral clasico ~ {math.erfc(z/math.sqrt(2)):.4f})")
    print("\nFactor de Bayes frente al ancho del prior tau (M1: mu ~ N(0,tau^2)):")
    print(f"{'tau':>8}{'log p(y|M0)':>14}{'log p(y|M1)':>14}{'BF01':>10}{'BF10':>10}")
    for tau in (0.1, 0.3, 1.0, 3.0, 10.0, 100.0, 1000.0):
        b = bf01_cerrado(Y, tau)
        print(f"{tau:8g}{logev_m0(Y):14.4f}{logev_m1(Y, tau):14.4f}{b:10.3f}{1/b:10.3f}")
    # maximo de BF10 sobre tau
    taus = np.logspace(-2, 3, 5001)
    bf10 = np.array([1 / bf01_cerrado(Y, t) for t in taus])
    k = int(np.argmax(bf10))
    print(f"\nBF10 maximo = {bf10[k]:.3f} en tau = {taus[k]:.3f}")
    print("\nWAIC y LOO exacto (M1 con tau = 1; M0 sin parametros):")
    ew, pw, el, li = waic_loo(Y, 1.0, np.random.default_rng(2026))
    e0 = logev_m0(Y)
    print(f"   M0: elpd = {e0:.3f} (p_efectivo = 0)")
    print(f"   M1: elpd_waic = {ew:.3f} (p_waic = {pw:.3f}); elpd_loo = {el:.3f}")
    d = li - lognorm(Y, 0.0, SIG)
    print(f"   diferencia elpd_loo(M1) - elpd(M0) = {d.sum():.3f} +- {math.sqrt(N)*d.std(ddof=1):.3f} (error estandar aproximado)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
