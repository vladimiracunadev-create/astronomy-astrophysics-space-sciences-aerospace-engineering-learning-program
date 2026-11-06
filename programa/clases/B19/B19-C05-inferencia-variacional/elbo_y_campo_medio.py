#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B19-C05: ELBO y aproximacion de campo medio.

Parte 1 (exacta). Modelo normal-normal: theta ~ N(m0, s0^2); y_i | theta ~ N(theta, s^2),
i = 1..n. La posterior es normal y la evidencia log p(y) tiene forma cerrada.
Con q = N(mq, sq^2) el ELBO es
  ELBO = E_q[log p(y|theta)] + E_q[log p(theta)] - E_q[log q(theta)]
y ELBO = log p(y) - KL(q || p(theta|y)); si q es la posterior exacta, ELBO = log p(y).
Datos: SINTETICOS: y = (9.8, 10.4, 10.1, 9.6, 10.6), s = 0.5, m0 = 10, s0 = 2 (unidades arbitrarias).
Parte 2 (exacta). Objetivo gaussiano bidimensional;
se usa covarianza [[1, r],[r, 1]], r = 0.9.
CAVI de campo medio converge a q_i = N(mu_i, 1/Lambda_ii): subestima la varianza
marginal por el factor 1 - r^2 (resultado clasico; Blei, Kucukelbir y McAuliffe 2017).
Parte 3 (numerica). Tasa de Poisson con parametrizacion eta = log(lambda), prior
eta ~ N(1, 1) y datos n = 7 eventos en T = 2 h (SINTETICOS). q = N(m, s^2) en eta;
el ELBO se evalua con cuadratura de Gauss-Hermite (40 nodos) y se maximiza con
Nelder-Mead de scipy; se compara con la posterior exacta por rejilla.
Supuestos: familia gaussiana (partes 1 y 3) y factorizada (parte 2).
Validez: ilustrativa; ADVI y VI de gran escala no se implementan.
Tolerancia: ELBO exacto = log p(y) a 1e-10; CAVI frente a la teoria a 1e-8;
VI gaussiana frente a rejilla: media de eta a 0.05 y sd a 0.05.
"""
from __future__ import annotations
import math
import platform
import sys

import numpy as np
import scipy
from scipy.optimize import minimize

Y = np.array([9.8, 10.4, 10.1, 9.6, 10.6])
S, M0, S0 = 0.5, 10.0, 2.0


def log_evidencia(y):
    n = len(y)
    cov = S ** 2 * np.eye(n) + S0 ** 2 * np.ones((n, n))
    d = y - M0
    sign, logdet = np.linalg.slogdet(cov)
    return -0.5 * (n * math.log(2 * math.pi) + logdet + d @ np.linalg.solve(cov, d))


def posterior_exacta(y):
    n = len(y)
    prec = 1 / S0 ** 2 + n / S ** 2
    mean = (M0 / S0 ** 2 + y.sum() / S ** 2) / prec
    return mean, 1 / math.sqrt(prec)


def elbo_normal(y, mq, sq):
    n = len(y)
    e_loglik = -0.5 * n * math.log(2 * math.pi * S ** 2) - ((y - mq) ** 2).sum() / (2 * S ** 2) - n * sq ** 2 / (2 * S ** 2)
    e_logprior = -0.5 * math.log(2 * math.pi * S0 ** 2) - ((mq - M0) ** 2 + sq ** 2) / (2 * S0 ** 2)
    entropia = 0.5 * math.log(2 * math.pi * math.e * sq ** 2)
    return e_loglik + e_logprior + entropia


def cavi_2d(r, mu=(0.0, 0.0), it=200):
    cov = np.array([[1.0, r], [r, 1.0]])
    L = np.linalg.inv(cov)
    m = np.array([3.0, -2.0])                      # arranque arbitrario
    mu = np.asarray(mu, float)
    for _ in range(it):
        m[0] = mu[0] - L[0, 1] / L[0, 0] * (m[1] - mu[1])
        m[1] = mu[1] - L[1, 0] / L[1, 1] * (m[0] - mu[0])
    return m, 1.0 / np.sqrt(np.diag(L))


GH_X, GH_W = np.polynomial.hermite.hermgauss(40)
N_EV, T_EV, M_PR, S_PR = 7, 2.0, 1.0, 1.0


def elbo_poisson(par):
    m, ls = par
    s = math.exp(ls)
    eta = m + math.sqrt(2.0) * s * GH_X
    f = N_EV * eta - T_EV * np.exp(eta) - 0.5 * ((eta - M_PR) / S_PR) ** 2
    esperanza = (GH_W * f).sum() / math.sqrt(math.pi)
    return esperanza + 0.5 * math.log(2 * math.pi * math.e * s ** 2)    # constantes omitidas


def main():
    print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "|", platform.platform())
    # --- Parte 1
    mean, sd = posterior_exacta(Y)
    logZ = log_evidencia(Y)
    e_ex = elbo_normal(Y, mean, sd)
    assert abs(e_ex - logZ) < 1e-10, (e_ex, logZ)
    e_mal = elbo_normal(Y, mean + 0.3, sd * 1.5)
    assert e_mal < logZ
    # --- Parte 2
    m2, s2 = cavi_2d(0.9)
    assert np.allclose(m2, 0.0, atol=1e-8) and np.allclose(s2, math.sqrt(1 - 0.81), atol=1e-8)
    # --- Parte 3
    res = minimize(lambda p: -elbo_poisson(p), x0=[0.0, 0.0], method="Nelder-Mead",
                   options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 2000})
    mv, sv = res.x[0], math.exp(res.x[1])
    eta = np.linspace(-6.0, 6.0, 120001)
    d = eta[1] - eta[0]
    lp = N_EV * eta - T_EV * np.exp(eta) - 0.5 * ((eta - M_PR) / S_PR) ** 2
    p = np.exp(lp - lp.max())
    p /= p.sum() * d
    me = (eta * p).sum() * d
    se = math.sqrt(((eta - me) ** 2 * p).sum() * d)
    assert abs(mv - me) < 0.05 and abs(sv - se) < 0.05, (mv, me, sv, se)
    print("Pruebas: OK\n")
    print(f"Parte 1: log p(y) = {logZ:.6f}; posterior exacta N({mean:.4f}, {sd:.4f}^2)")
    print(f"         ELBO con q exacta = {e_ex:.6f}; ELBO con q desplazada y ancha = {e_mal:.6f} (< log p(y))")
    print(f"         brecha = KL(q||p) = {logZ - e_mal:.6f}")
    print(f"Parte 2: CAVI r=0.9 -> medias {np.round(m2, 6)}, sd de q {np.round(s2, 4)} "
          f"(sd marginal exacta 1.0000; cociente {s2[0]:.4f} = sqrt(1-r^2))")
    print(f"Parte 3: VI gaussiana en eta=log(lambda): m = {mv:.4f}, s = {sv:.4f}")
    print(f"         posterior exacta (rejilla):     m = {me:.4f}, s = {se:.4f}")
    print(f"         lambda aprox. exp(m) = {math.exp(mv):.3f} /h (MLE n/T = {N_EV/T_EV:.2f} /h)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
