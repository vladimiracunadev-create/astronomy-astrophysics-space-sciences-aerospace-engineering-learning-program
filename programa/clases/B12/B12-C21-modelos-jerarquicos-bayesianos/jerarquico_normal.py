#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C21: modelo jerarquico normal-normal (agrupacion parcial).

Datos: SINTETICOS e ILUSTRATIVOS. Ocho sensores del mismo tipo miden un mismo
desfase de calibracion con diferentes errores; lecturas y_j (um) y errores
tipicos conocidos s_j (um).
Modelo: y_j ~ N(theta_j, s_j^2); theta_j ~ N(mu, tau^2); prior plano en mu y
uniforme en tau sobre [0, 6] um. Marginal: y_j ~ N(mu, s_j^2 + tau^2).
Posterior de tau (rejilla): p(tau|y) ∝ V_mu^(1/2) prod (s_j^2+tau^2)^(-1/2)
exp(-(y_j - mu_hat)^2 / (2 (s_j^2+tau^2))), con mu_hat = sum w_j y_j / sum w_j,
w_j = 1/(s_j^2+tau^2), V_mu = 1/sum w_j. Condicional: media de theta_j dado
(tau, y) = (1 - B_j) y_j + B_j mu_hat, B_j = s_j^2/(s_j^2+tau^2).
Supuestos: normalidad, s_j conocidos, intercambiabilidad de los sensores.
Validez: pocos grupos hacen la posterior de tau muy ancha.
Tolerancia: la verosimilitud marginal en tau por la formula cerrada coincide
con integracion numerica en mu (J = 3) a 1e-8 relativo; limites tau->0 (media
ponderada) y tau->inf (sin agrupacion) a 1e-3; media posterior de theta_j por
rejilla y por muestreo directo a 0.02 um (M = 400 000). Detienen la ejecucion.
"""
import platform

import numpy as np
import scipy
from scipy import stats

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")
y = np.array([4.1, 1.2, 2.8, 0.4, 3.3, 5.6, 1.9, 2.5])
s = np.array([1.0, 0.8, 1.5, 1.2, 0.9, 1.4, 1.1, 1.6])
J = len(y)


def stats_tau(tau, y, s):
    w = 1.0 / (s**2 + tau**2)
    mu_hat = np.sum(w * y) / np.sum(w)
    V = 1.0 / np.sum(w)
    logp = 0.5 * np.log(V) - 0.5 * np.sum(np.log(s**2 + tau**2)) - 0.5 * np.sum(w * (y - mu_hat) ** 2)
    return logp, mu_hat, V


# comprobacion independiente: integrar mu numericamente para J = 3
y3, s3, tau0 = y[:3], s[:3], 1.3
mus = np.linspace(-40, 40, 400_001)
lik = np.ones_like(mus)
for yj, sj in zip(y3, s3):
    lik *= stats.norm.pdf(yj, mus, np.sqrt(sj**2 + tau0**2))
num = np.trapezoid(lik, mus)
lp, _, _ = stats_tau(tau0, y3, s3)
w3 = 1.0 / (s3**2 + tau0**2)
# formula cerrada: integral = exp(lp) * (2 pi)^(-(J-1)/2)
closed = np.exp(lp) * (2 * np.pi) ** (-(len(y3) - 1) / 2)
print(f"verosimilitud marginal en tau=1.3 (J=3): cerrada = {closed:.8e}; integracion numerica = {num:.8e}")
assert abs(closed / num - 1) < 1e-8

# posterior de tau en rejilla
taus = np.linspace(1e-4, 6.0, 6000)
lps = np.array([stats_tau(t, y, s)[0] for t in taus])
pt = np.exp(lps - lps.max())
pt /= pt.sum()
cdf = np.cumsum(pt)
q = lambda a: taus[np.searchsorted(cdf, a)]
print(f"posterior de tau: media = {np.sum(taus*pt):.3f} um; mediana = {q(0.5):.3f}; IC 95 % = [{q(0.025):.3f}, {q(0.975):.3f}]")
print(f"P(tau < 0.5 um | y) = {pt[taus < 0.5].sum():.3f}  (la posterior no excluye tau pequeno)")

# limites
mu_pool = np.sum(y / s**2) / np.sum(1 / s**2)
_, mu_small, _ = stats_tau(1e-6, y, s)
B_small = s**2 / (s**2 + 1e-6)
assert abs(mu_small - mu_pool) < 1e-3 and np.all(np.abs((1 - B_small) * y + B_small * mu_small - mu_pool) < 1e-3)
B_big = s**2 / (s**2 + 1e6)
assert np.all(np.abs((1 - B_big) * y + B_big * 0 - y) < 1e-3 * (1 + np.abs(y)))
print(f"tau -> 0: todos los theta_j = media ponderada {mu_pool:.4f}; tau -> inf: theta_j = y_j")

# media posterior de theta_j: rejilla (Rao-Blackwell) vs muestreo directo
mu_hats = np.array([stats_tau(t, y, s)[1] for t in taus])
B = s[None, :] ** 2 / (s[None, :] ** 2 + taus[:, None] ** 2)
cond_mean = (1 - B) * y[None, :] + B * mu_hats[:, None]
post_mean_grid = pt @ cond_mean
rng = np.random.default_rng(2121)
M = 400_000
idx = rng.choice(len(taus), size=M, p=pt)
tt = taus[idx]
w = 1.0 / (s[None, :] ** 2 + tt[:, None] ** 2)
mh = (w * y).sum(axis=1) / w.sum(axis=1)
Vm = 1.0 / w.sum(axis=1)
mu = rng.normal(mh, np.sqrt(Vm))
Vj = 1.0 / (1.0 / s[None, :] ** 2 + 1.0 / tt[:, None] ** 2)
mj = Vj * (y[None, :] / s[None, :] ** 2 + mu[:, None] / tt[:, None] ** 2)
theta = rng.normal(mj, np.sqrt(Vj))
post_mean_mc = theta.mean(axis=0)
print("sensor    y_j     s_j   sin agrupar   agrupacion parcial (rejilla)   (muestreo)   reduccion de s")
for j in range(J):
    print(f"{j+1:4d}   {y[j]:6.2f}  {s[j]:5.2f}     {y[j]:6.2f}          {post_mean_grid[j]:6.3f}                  {post_mean_mc[j]:6.3f}       {100*(1-theta[:, j].std()/s[j]):5.1f} %")
assert np.max(np.abs(post_mean_grid - post_mean_mc)) < 0.02
print(f"media global mu: {mu.mean():.3f} +/- {mu.std():.3f} um;  media ponderada sin jerarquia: {mu_pool:.3f}")
print("Pruebas superadas.")
