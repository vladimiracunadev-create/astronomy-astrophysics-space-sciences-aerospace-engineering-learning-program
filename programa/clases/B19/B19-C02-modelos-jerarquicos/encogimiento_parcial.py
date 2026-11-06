#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B19-C02: encogimiento parcial en un modelo normal jerarquico.

Datos: SINTETICOS (inventados para la clase). Seis sensores de temperatura de
un satelite miden un desvio de calibracion y_j [mK] con incertidumbre
conocida sigma_j [mK]:
  y     = 12.1  9.4 15.8  7.2 10.9 18.3
  sigma =  2.0  3.5  4.0  2.5  3.0  5.0
Modelo: y_j | theta_j ~ N(theta_j, sigma_j^2); theta_j | mu, tau ~ N(mu, tau^2);
prior plano en mu y plano en tau sobre [0, 60] mK.
Exacto: p(tau | y) ∝ prod_j N(y_j | mu^(tau), sigma_j^2 + tau^2) * V_mu(tau)^(1/2),
con w_j = 1/(sigma_j^2+tau^2), mu^ = sum(w y)/sum(w), V_mu = 1/sum(w).
Supuestos: normalidad, sigma_j conocidas, intercambiabilidad de los sensores.
Validez: J pequeno; la posterior de tau depende de su prior (se discute en clase).
Tolerancia: pruebas analiticas 1e-9; Monte Carlo (200 000 sorteos) a 0.05 mK.
Solo numpy; ASCII en la salida.
"""
from __future__ import annotations
import platform
import sys

import numpy as np

Y = np.array([12.1, 9.4, 15.8, 7.2, 10.9, 18.3])
S = np.array([2.0, 3.5, 4.0, 2.5, 3.0, 5.0])
TAU = np.linspace(0.0, 60.0, 6001)
DT = TAU[1] - TAU[0]


def condicional(tau):
    """mu^, V_mu y media/varianza de theta_j dado tau (marginalizando mu)."""
    w = 1.0 / (S ** 2 + tau ** 2)
    mu_hat = (w * Y).sum() / w.sum()
    v_mu = 1.0 / w.sum()
    if tau == 0.0:
        return mu_hat, v_mu, np.full_like(Y, mu_hat), np.full_like(Y, v_mu)
    prec = 1.0 / S ** 2 + 1.0 / tau ** 2
    th_hat = (Y / S ** 2 + mu_hat / tau ** 2) / prec
    v_th = 1.0 / prec + ((1.0 / tau ** 2) / prec) ** 2 * v_mu
    return mu_hat, v_mu, th_hat, v_th


def log_post_tau(tau):
    w = 1.0 / (S ** 2 + tau ** 2)
    mu_hat = (w * Y).sum() / w.sum()
    return -0.5 * np.sum(np.log(S ** 2 + tau ** 2) + w * (Y - mu_hat) ** 2) - 0.5 * np.log(w.sum())


def posterior_tau():
    lp = np.array([log_post_tau(t) for t in TAU])
    p = np.exp(lp - lp.max())
    return p / (p.sum() * DT)


def main():
    print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.platform())
    p = posterior_tau()
    # --- pruebas ---
    assert abs(p.sum() * DT - 1.0) < 1e-9
    w0 = 1.0 / S ** 2
    pooled = (w0 * Y).sum() / w0.sum()
    _, _, th0, _ = condicional(0.0)
    assert np.allclose(th0, pooled, atol=1e-12)            # tau -> 0: agrupacion completa
    _, _, th_big, _ = condicional(1e6)
    assert np.allclose(th_big, Y, atol=1e-6)               # tau -> inf: sin agrupar
    # media posterior de theta_j: cuadratura vs Monte Carlo
    Eth = np.zeros_like(Y)
    for t, pt in zip(TAU, p):
        Eth += pt * DT * condicional(t)[2]
    rng = np.random.default_rng(2026)
    N = 200_000
    taus = rng.choice(TAU, size=N, p=p * DT / (p * DT).sum())
    th = np.empty((N, len(Y)))
    for i, t in enumerate(np.unique(taus)):                # agrupa por valor de tau
        idx = np.where(taus == t)[0]
        mu_hat, v_mu, _, _ = condicional(t)
        mu = rng.normal(mu_hat, np.sqrt(v_mu), size=idx.size)
        if t == 0.0:
            th[idx] = mu[:, None]
        else:
            prec = 1.0 / S ** 2 + 1.0 / t ** 2
            m = (Y / S ** 2 + mu[:, None] / t ** 2) / prec
            th[idx] = m + rng.normal(size=(idx.size, len(Y))) / np.sqrt(prec)
    assert np.max(np.abs(th.mean(axis=0) - Eth)) < 0.05, (th.mean(axis=0), Eth)
    print("Pruebas: OK")
    # --- resultados ---
    c = np.cumsum(p) * DT
    q = lambda x: TAU[np.searchsorted(c, x)]
    print(f"\nposterior de tau [mK]: mediana {q(0.5):.2f}, 90 % [{q(0.05):.2f}, {q(0.95):.2f}]; "
          f"moda {TAU[np.argmax(p)]:.2f}; masa en tau>50: {p[TAU > 50].sum()*DT:.2e}")
    print(f"media agrupada completa (tau=0): {pooled:.2f} mK")
    print(f"{'j':<3}{'y':>7}{'sigma':>7}{'agrup.':>9}{'parcial':>9}{'sd':>7}{'sin agrupar':>13}{'factor B':>10}")
    sd = th.std(axis=0)
    tau_m = q(0.5)
    for j in range(len(Y)):
        B = S[j] ** 2 / (S[j] ** 2 + tau_m ** 2)
        print(f"{j+1:<3}{Y[j]:7.1f}{S[j]:7.1f}{pooled:9.2f}{Eth[j]:9.2f}{sd[j]:7.2f}{Y[j]:13.1f}{B:10.2f}")
    print("(factor B = sigma^2/(sigma^2+tau^2) evaluado en la mediana de tau)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
