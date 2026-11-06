#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B19-C06: distribucion predictiva posterior y chequeo predictivo.

Datos: SINTETICOS. Conteos de eventos en 12 intervalos de 1 h de un contador
de particulas de un CubeSat, en dos conjuntos:
  BIEN  = 2 1 4 2 0 3 2 5 1 2 3 1          (compatible con tasa constante)
  RAFAGA= 1 0 2 1 9 0 1 2 0 8 1 0          (dos intervalos con rafagas)
Modelo: y_i | lambda ~ Poisson(lambda) (1 h); lambda ~ Gamma(a=2, b=1) [1/h].
Posterior exacta: Gamma(a + sum y, b + 12).
Predictiva exacta para un conteo futuro en t horas: binomial negativa,
  P(Y=k) = Gamma(k+a')/(k! Gamma(a')) * p^a' * (1-p)^k,  a' = a + sum y, p = b'/(b'+t).
Chequeo predictivo posterior: estadistico T(y) = varianza/media (indice de
dispersion); valor p predictivo posterior = P(T(y_rep) >= T(y) | y) por simulacion
(si T es indefinido porque la media es 0 se descarta esa replica).
Supuestos: eventos independientes, tasa constante.
Validez: conteos moderados. Tolerancia: la simulacion reproduce la predictiva
binomial negativa con diferencia maxima por casilla < 0.004 (200 000 sorteos).
Solo numpy; ASCII en la salida.
"""
from __future__ import annotations
import math
import platform
import sys

import numpy as np

BIEN = np.array([2, 1, 4, 2, 0, 3, 2, 5, 1, 2, 3, 1])
RAFAGA = np.array([1, 0, 2, 1, 9, 0, 1, 2, 0, 8, 1, 0])
A0, B0 = 2.0, 1.0


def nb_pmf(k, a, p):
    return math.exp(math.lgamma(k + a) - math.lgamma(k + 1) - math.lgamma(a) + a * math.log(p) + k * math.log(1 - p))


def dispersion(y):
    m = y.mean(axis=-1)
    v = y.var(axis=-1, ddof=1)
    return np.where(m > 0, v / np.where(m > 0, m, 1), np.nan)


def ppc(y, rng, R=20_000):
    a1, b1 = A0 + y.sum(), B0 + len(y)
    lam = rng.gamma(a1, 1.0 / b1, size=R)
    rep = rng.poisson(lam[:, None], size=(R, len(y)))
    t = dispersion(rep)
    ok = ~np.isnan(t)
    return float((t[ok] >= dispersion(y)).mean()), float(dispersion(y)), float(np.nanmean(t))


def main():
    print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.platform())
    rng = np.random.default_rng(2026)
    # --- prueba: simulacion vs binomial negativa exacta
    a1, b1 = A0 + BIEN.sum(), B0 + len(BIEN)
    for t in (1.0, 3.0):
        lam = rng.gamma(a1, 1.0 / b1, size=200_000)
        y = rng.poisson(lam * t)
        p = b1 / (b1 + t)
        ks = np.arange(0, 15)
        emp = np.array([(y == k).mean() for k in ks])
        ex = np.array([nb_pmf(k, a1, p) for k in ks])
        assert np.max(np.abs(emp - ex)) < 0.004, (t, np.max(np.abs(emp - ex)))
    assert abs(sum(nb_pmf(k, a1, b1 / (b1 + 1)) for k in range(400)) - 1) < 1e-9
    print("Pruebas: OK\n")
    for nom, y in (("BIEN", BIEN), ("RAFAGA", RAFAGA)):
        a1, b1 = A0 + y.sum(), B0 + len(y)
        media_post = a1 / b1
        p = b1 / (b1 + 1.0)
        pmf = np.array([nb_pmf(k, a1, p) for k in range(0, 40)])
        c = np.cumsum(pmf)
        q = lambda x: int(np.searchsorted(c, x))
        pv, tobs, tmed = ppc(y, np.random.default_rng(11))
        print(f"{nom}: sum y = {y.sum()}, media {y.mean():.2f}, T(y) = var/media = {tobs:.2f}")
        print(f"   posterior de lambda: Gamma({a1:g}, {b1:g}); media {media_post:.3f} /h; sd {math.sqrt(a1)/b1:.3f}")
        print(f"   predictiva de 1 conteo en 1 h: media {media_post:.3f}; sd {math.sqrt(a1*(1-p))/p:.3f}; "
              f"mediana {q(0.5)}, 90 % central [{q(0.05)}, {q(0.95)}]; P(Y=0) = {pmf[0]:.3f}")
        print(f"   chequeo: T medio replicado {tmed:.2f}; valor p predictivo posterior = {pv:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
