#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C23: convergencia y reproducibilidad de cadenas MCMC.

Datos: SINTETICOS. (a) Cadenas AR(1) con coeficiente rho = 0.9 (tiempo de
autocorrelacion integrado exacto (1+rho)/(1-rho) = 19). (b) Cuatro cadenas de
Metropolis sobre la posterior Gamma(38, 10.1) de C12-C13 con inicios
dispersos (1, 3, 8, 15).
Modelo: R-hat clasico dividiendo cada cadena en dos mitades (version
"split"); tamano muestral efectivo ESS = N / tau_int con tau_int = 1 + 2 sum rho_t
hasta la primera autocorrelacion no positiva; hash SHA-256 de la cadena para
verificar reproducibilidad.
Supuestos: cadenas independientes entre si; estacionarias tras el calentamiento.
Validez: R-hat bajo no prueba convergencia (cadenas que no exploran un modo);
version clasica, no la basada en rangos (arXiv:1903.08008).
Tolerancia: tau_int estimado dentro de 10 % del exacto; R-hat de cadenas
iid < 1.01; R-hat con inicios dispersos y 60 pasos > 1.1; con 20 000 pasos
(tras descartar la mitad) < 1.01; hashes iguales con la misma semilla.
Las pruebas detienen la ejecucion si fallan.
"""
import hashlib
import math
import platform

import numpy as np
import scipy

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")


def split_rhat(chains):
    """chains: (m, n). Divide cada cadena en dos mitades y calcula R-hat clasico."""
    m, n = chains.shape
    h = n // 2
    sp = np.concatenate([chains[:, :h], chains[:, h : 2 * h]], axis=0)
    mm, nn = sp.shape
    means = sp.mean(axis=1)
    W = sp.var(axis=1, ddof=1).mean()
    B = nn * means.var(ddof=1)
    var_plus = (nn - 1) / nn * W + B / nn
    return math.sqrt(var_plus / W)


def tau_int(x):
    x = x - x.mean()
    n = len(x)
    f = np.fft.rfft(x, 2 * n)
    acf = np.fft.irfft(f * np.conj(f))[:n]
    acf /= acf[0]
    tau = 1.0
    for t in range(1, n):
        if acf[t] <= 0:
            break
        tau += 2 * acf[t]
    return tau


def ar1(rho, n, rng):
    e = rng.standard_normal(n) * math.sqrt(1 - rho**2)
    x = np.empty(n)
    x[0] = rng.standard_normal()
    for i in range(1, n):
        x[i] = rho * x[i - 1] + e[i]
    return x


rng = np.random.default_rng(2323)
rho = 0.9
exacto = (1 + rho) / (1 - rho)
x = ar1(rho, 200_000, rng)
tau = tau_int(x)
print(f"AR(1) rho=0.9: tau_int estimado = {tau:.2f}; exacto = {exacto:.2f}; ESS = {len(x)/tau:,.0f} de {len(x):,}")
assert abs(tau / exacto - 1) < 0.10

iid = rng.standard_normal((4, 2000))
r_iid = split_rhat(iid)
print(f"R-hat de 4 cadenas iid = {r_iid:.4f}")
assert r_iid < 1.01

# cadenas de Metropolis con inicios dispersos
a_post, b_post = 38.0, 10.1


def metropolis(x0, n, seed, step=0.8):
    r = np.random.default_rng(seed)
    z = r.standard_normal(n)
    ul = np.log(r.random(n))
    x, lp = x0, (a_post - 1) * math.log(x0) - b_post * x0
    out = np.empty(n)
    for i in range(n):
        y = x + step * z[i]
        if y > 0:
            lpy = (a_post - 1) * math.log(y) - b_post * y
            if ul[i] < lpy - lp:
                x, lp = y, lpy
        out[i] = x
    return out


starts = (1.0, 3.0, 8.0, 15.0)
short = np.array([metropolis(x0, 60, 100 + i) for i, x0 in enumerate(starts)])
r_short = split_rhat(short)
print(f"R-hat con inicios dispersos y 60 pasos = {r_short:.3f}  -> NO convergio")
assert r_short > 1.1
long_ = np.array([metropolis(x0, 40_000, 100 + i) for i, x0 in enumerate(starts)])
kept = long_[:, 20_000:]
r_long = split_rhat(kept)
ess = sum(kept.shape[1] / tau_int(c) for c in kept)
print(f"R-hat con 40 000 pasos (se descarta la mitad) = {r_long:.4f}; ESS total = {ess:,.0f} de {kept.size:,}")
print(f"media posterior = {kept.mean():.4f} (exacta {a_post/b_post:.4f}); error de Monte Carlo = {kept.std()/math.sqrt(ess):.4f}")
assert r_long < 1.01 and abs(kept.mean() - a_post / b_post) < 4 * kept.std() / math.sqrt(ess)

# reproducibilidad
h1 = hashlib.sha256(metropolis(8.0, 5000, 7).tobytes()).hexdigest()
h2 = hashlib.sha256(metropolis(8.0, 5000, 7).tobytes()).hexdigest()
h3 = hashlib.sha256(metropolis(8.0, 5000, 8).tobytes()).hexdigest()
print(f"SHA-256 misma semilla: {h1[:16]} / {h2[:16]} (iguales: {h1 == h2}); otra semilla: {h3[:16]}")
assert h1 == h2 and h1 != h3
print("Pruebas superadas.")
