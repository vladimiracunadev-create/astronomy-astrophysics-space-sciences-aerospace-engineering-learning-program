#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C18: limites superiores de Poisson con fondo, intervalo bayesiano y cobertura por Monte Carlo.

Datos: ninguna constante fisica. El fondo esperado (1.2 sucesos), los sucesos observados (0 y 3), el nivel de confianza (90 %), la exposicion (1000 kg dia), la eficiencia (0.5) y la
senal verdadera de la prueba de cobertura (2 sucesos) son ILUSTRATIVOS (sinteticos).
Modelo: limite superior frecuentista clasico s_up tal que P(N <= n_obs | s_up + b) = 1 - CL (biseccion); limite bayesiano con a priori uniforme en s >= 0 (integracion de Simpson de la
verosimilitud, sin tomar el signo del fondo); caso n_obs = 0, b = 0: s_up = -ln(1 - CL) = 2.3026 (analitico, ambos metodos); conversion a una seccion eficaz sigma < s_up/(eficiencia * exposicion);
cobertura: fraccion de experimentos simulados en que el limite supera el valor verdadero (debe ser >= CL).
Supuestos: fondo conocido, conteo de Poisson, sin incertidumbres sistematicas. Validez: ilustrativa.
Tolerancia: caso analitico clasico a 1e-9 y bayesiano a 1e-3; cobertura clasica >= 0.90 - 4 errores estandar.
"""
from __future__ import annotations
import math
import platform
import random
import sys


def p_le(n, mu):
    s, t = 0.0, math.exp(-mu)
    for k in range(n + 1):
        s += t
        t *= mu / (k + 1)
    return s


def lim_clasico(n_obs, b, cl=0.90):
    lo, hi = 0.0, 100.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if p_le(n_obs, mid + b) > 1 - cl:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def lim_bayes(n_obs, b, cl=0.90):
    def lik(s):
        return math.exp(-(s + b)) * (s + b) ** n_obs / math.factorial(n_obs)
    top = 60.0
    n = 6000
    h = top / n
    cum, acum = [0.0], 0.0
    for i in range(n):
        s0, s1 = i * h, (i + 1) * h
        acum += h * (lik(s0) + 4 * lik((s0 + s1) / 2) + lik(s1)) / 6
        cum.append(acum)
    total = cum[-1]
    for i, c in enumerate(cum):
        if c / total >= cl:
            c0 = cum[i - 1] / total
            return (i - 1 + (cl - c0) / (c / total - c0)) * h        # interpolacion lineal dentro del paso
    return top


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'n_obs':>6} {'fondo b':>8} {'limite clasico (90 %)':>22} {'limite bayesiano (90 %)':>24}")
    for n_obs, b in ((0, 0.0), (0, 1.2), (3, 1.2), (1, 1.2), (8, 1.2)):
        print(f"{n_obs:6d} {b:8.1f} {lim_clasico(n_obs, b):22.4f} {lim_bayes(n_obs, b):24.4f}")
    assert abs(lim_clasico(0, 0.0) + math.log(0.1)) < 1e-9
    assert abs(lim_bayes(0, 0.0) + math.log(0.1)) < 1e-3
    print(f"caso analitico n = 0, b = 0: -ln 0.1 = {-math.log(0.1):.6f}")
    expo, efi = 1000.0, 0.5
    s_up = lim_clasico(3, 1.2)
    print(f"con n_obs = 3 y b = 1.2: s_up = {s_up:.3f} sucesos -> sigma < {s_up / (efi * expo):.4e} por kg dia (unidades arbitrarias de la exposicion)")
    # cobertura
    rng = random.Random(20261109)
    s_ver, b = 2.0, 1.2
    n_exp = 20000
    cubre = 0
    memo = {}
    for _ in range(n_exp):
        # muestreo de Poisson por inversion
        u, k, t = rng.random(), 0, math.exp(-(s_ver + b))
        c = t
        while u > c:
            k += 1
            t *= (s_ver + b) / k
            c += t
        if k not in memo:
            memo[k] = lim_clasico(k, b)
        if memo[k] >= s_ver:
            cubre += 1
    cob = cubre / n_exp
    err = math.sqrt(0.9 * 0.1 / n_exp)
    print(f"cobertura del limite clasico con s = {s_ver} y b = {b} en {n_exp} experimentos: {cob:.4f} (nominal 0.90, error estandar {err:.4f})")
    assert cob > 0.90 - 4 * err
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
