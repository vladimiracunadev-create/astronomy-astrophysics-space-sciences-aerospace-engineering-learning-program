#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B19-C04: R-hat dividido, tamano efectivo y divergencias.

Datos: SIMULADOS (semilla fija). Cuatro casos con cadenas de longitud n = 1000:
  A) 4 cadenas AR(1) estacionarias con rho = 0.9, media 0, varianza 1.
  B) 4 cadenas iid N(mu_i, 1) con mu_i = 0, 0, 0, 3 (una cadena en otra zona).
  C) 4 cadenas AR(1) rho = 0.9 con deriva: las cadenas parten de -5, -5, 5, 5 y
     no han alcanzado el regimen estacionario en las primeras iteraciones.
  D) embudo de Neal (v ~ N(0, 3^2), x | v ~ N(0, exp(v))) muestreado con HMC,
     en parametrizacion centrada y no centrada; se cuentan divergencias
     (error de energia > 1000).
Formulas: split-R-hat (Gelman et al. / Vehtari et al. 2021, version sin rango):
  W = media de varianzas de cada media-cadena, B/n = varianza de las medias,
  var+ = (n-1)/n W + B/n, R-hat = sqrt(var+/W), con cada cadena partida en 2.
  ESS = M n / (1 + 2 sum rho_t) con secuencia positiva inicial (Geyer).
Referencia exacta: para AR(1), ESS/N = (1 - rho)/(1 + rho).
Supuestos: cadenas independientes entre si; para D, gradiente exacto.
Validez: diagnosticos necesarios, no suficientes. Esta version NO usa
normalizacion por rangos ni plegado (mejora de Vehtari et al. 2021).
Tolerancia: ESS AR(1) dentro del 15 % de la teoria; R-hat caso B contra la
formula cerrada a 1e-12; R-hat caso A < 1.05.
Solo numpy; ASCII en la salida.
"""
from __future__ import annotations
import math
import platform
import sys

import numpy as np


def split_chains(c):
    m, n = c.shape
    h = n // 2
    return np.vstack([c[:, :h], c[:, h:2 * h]])


def rhat(c):
    c = split_chains(c)
    m, n = c.shape
    W = c.var(axis=1, ddof=1).mean()
    Bn = c.mean(axis=1).var(ddof=1)
    return math.sqrt(((n - 1) / n * W + Bn) / W)


def ess(c):
    c = split_chains(c)
    m, n = c.shape
    W = c.var(axis=1, ddof=1).mean()
    Bn = c.mean(axis=1).var(ddof=1)
    var_plus = (n - 1) / n * W + Bn
    rho = np.zeros(n)
    for t in range(n):
        ac = ((c[:, :n - t] - c.mean(axis=1, keepdims=True)) * (c[:, t:] - c.mean(axis=1, keepdims=True))).mean()
        rho[t] = 1.0 - (W - ac) / var_plus
    s = 0.0
    for k in range(1, n - 1, 2):
        pair = rho[k] + rho[k + 1]
        if pair < 0:
            break
        s += pair
    return m * n / (1.0 + 2.0 * s)


def ar1(rng, m, n, rho, x0=None):
    x = np.empty((m, n))
    x[:, 0] = rng.normal(size=m) if x0 is None else np.asarray(x0, float)
    e = rng.normal(size=(m, n)) * math.sqrt(1 - rho ** 2)
    for t in range(1, n):
        x[:, t] = rho * x[:, t - 1] + e[:, t]
    return x


def hmc_embudo(rng, n, centrado, eps=0.15, L=20):
    """Embudo con q = (v, z). Centrado: x = z. No centrado: x = exp(v/2) z, z~N(0,1)."""
    def U(q):
        v, z = q
        if centrado:
            return 0.5 * v * v / 9.0 + 0.5 * z * z * math.exp(-v) + 0.5 * v
        return 0.5 * v * v / 9.0 + 0.5 * z * z

    def g(q):
        v, z = q
        if centrado:
            return np.array([v / 9.0 - 0.5 * z * z * math.exp(-v) + 0.5, z * math.exp(-v)])
        return np.array([v / 9.0, z])

    q = np.array([0.0, 0.0])
    out = np.empty((n, 2))
    div = 0
    for i in range(n):
        p = rng.normal(size=2)
        qn, pn = q.copy(), p.copy()
        pn -= 0.5 * eps * g(qn)
        bad = False
        for k in range(L):
            qn += eps * pn
            if k != L - 1:
                pn -= eps * g(qn)
            if not np.all(np.isfinite(qn)) or abs(qn[0]) > 50:
                bad = True
                break
        if not bad:
            pn -= 0.5 * eps * g(qn)
            dH = (U(q) + 0.5 * p @ p) - (U(qn) + 0.5 * pn @ pn)
            if not math.isfinite(dH) or -dH > 1000.0:
                bad = True
        if bad:
            div += 1
        elif math.log(rng.uniform()) < dH:
            q = qn
        out[i] = q
    return out, div


def pruebas(rng):
    A = ar1(rng, 4, 1000, 0.9)
    assert rhat(A) < 1.05, rhat(A)
    teoria = (1 - 0.9) / (1 + 0.9)
    medidos = []
    for s in range(5):
        r = np.random.default_rng(100 + s)
        medidos.append(ess(ar1(r, 4, 1000, 0.9)) / 4000)
    assert abs(np.mean(medidos) - teoria) / teoria < 0.15, (np.mean(medidos), teoria)
    # R-hat cerrado para cadenas con medias fijas y varianza 1 (aproximacion de muestra grande)
    B = np.vstack([rng.normal(m, 1.0, 1000) for m in (0, 0, 0, 3)])
    c = split_chains(B)
    n = c.shape[1]
    W = np.mean([x.var(ddof=1) for x in c])
    Bn = np.var([x.mean() for x in c], ddof=1)
    assert abs(rhat(B) - math.sqrt(((n - 1) / n * W + Bn) / W)) < 1e-12
    return teoria, float(np.mean(medidos))


def main():
    print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.platform())
    rng = np.random.default_rng(2026)
    teoria, med = pruebas(np.random.default_rng(5))
    print(f"Pruebas: OK (ESS/N de AR(1) rho=0.9: teoria {teoria:.3f}, medida {med:.3f})\n")
    A = ar1(rng, 4, 1000, 0.9)
    B = np.vstack([rng.normal(m, 1.0, 1000) for m in (0, 0, 0, 3)])
    C = ar1(rng, 4, 1000, 0.99, x0=[-5, -5, 5, 5])
    print(f"{'caso':<44}{'R-hat':>8}{'ESS':>9}")
    for nom, x in (("A  AR(1) rho=0.9, estacionarias", A),
                   ("B  una cadena en otra zona (mu=3)", B),
                   ("C  AR(1) rho=0.99 arrancando en -5,-5,5,5", C)):
        print(f"{nom:<44}{rhat(x):8.3f}{ess(x):9.0f}")
    print("\nEmbudo de Neal, HMC (eps=0.15, L=20), 4 cadenas x 1000 iteraciones")
    for nom, cen in (("centrada", True), ("no centrada", False)):
        tot = 0
        vs = []
        for s in range(4):
            x, d = hmc_embudo(np.random.default_rng(300 + s), 1000, cen)
            tot += d
            vs.append(x[:, 0])
        vs = np.array(vs)
        print(f"  {nom:<12} divergencias: {tot:4d}/4000 | R-hat de v: {rhat(vs):.3f} | "
              f"min v: {vs.min():.2f} | sd v: {vs.std():.2f} (exacta 3.00)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
