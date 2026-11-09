#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B64-C01: supervivencia a la radiacion ionizante con un modelo de roturas de doble cadena (DSB).

Datos: SINTETICOS e ILUSTRATIVOS. Ningun valor corresponde a una cepa medida: rendimiento de DSB por gray y por Mpb (y),
tamano de genoma (G) y capacidad de reparacion (n_rep) son propuestos para el ejemplo. La unica afirmacion cualitativa
apoyada en una fuente consultada (Cox y Battista 2005, resumen) es que D. radiodurans tolera dosis que causan cientos de DSB.
Modelo: el numero de DSB por genoma tras una dosis D [Gy] es Poisson con media lam = y*G*D. La celula sobrevive si
DSB <= n_rep (cuantas roturas puede reparar con fidelidad). S(D) = P(Poisson(lam) <= n_rep).
Supuestos: DSB independientes, dosis aguda, sin efecto de la tasa de dosis ni del medio. Validez: ilustrativa.
Unidades: dosis [Gy = J/kg]; y [DSB Gy^-1 Mpb^-1]; G [Mpb]. Sistema de referencia: poblacion de celulas de un cultivo.
Tolerancias: S(D) analitica frente a Monte Carlo 0.01 absoluto (N=40 000); caso n_rep=0 frente a exp(-lam) a 1e-12;
D10 por biseccion frente a barrido fino 1 %.
"""
from __future__ import annotations
import math, platform, random

Y = 0.005          # DSB / (Gy * Mpb)  (ilustrativo)
G = 3.2            # Mpb (ilustrativo)
ORG = {"sensible (n_rep=2)": 2, "tolerante (n_rep=150)": 150}


def lam(D):
    return Y * G * D


def poisson_cdf(k, mu):
    """P(X<=k) para Poisson(mu), sumando en escala logaritmica."""
    s = 0.0
    for j in range(k + 1):
        s += math.exp(j * math.log(mu) - mu - math.lgamma(j + 1)) if mu > 0 else (1.0 if j == 0 else 0.0)
    return min(s, 1.0)


def S(D, n):
    return poisson_cdf(n, lam(D))


def d10(n):
    lo, hi = 0.0, 1e5
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if S(mid, n) > 0.1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def poisson_sample(rng, mu):
    # Knuth para mu pequeno, aproximacion por sumas de Poisson parciales para mu grande
    if mu < 30:
        L, k, p = math.exp(-mu), 0, 1.0
        while True:
            p *= rng.random()
            if p <= L:
                return k
            k += 1
    return sum(poisson_sample(rng, 20.0) for _ in range(int(mu // 20))) + poisson_sample(rng, mu - 20.0 * int(mu // 20))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: y = {Y} DSB/(Gy*Mpb), G = {G} Mpb -> {lam(1):.4f} DSB por Gy y por genoma")
    dosis = [10, 100, 500, 1000, 3000, 5000, 8000]
    print(f"{'D [Gy]':>8} {'DSB medio':>10} " + " ".join(f"{k:>24}" for k in ORG))
    for D in dosis:
        print(f"{D:8d} {lam(D):10.1f} " + " ".join(f"{S(D, n):24.4g}" for n in ORG.values()))
    for k, n in ORG.items():
        print(f"D10 {k}: {d10(n):.1f} Gy ; DSB medio en D10: {lam(d10(n)):.1f}")
    # pruebas
    for D in (0.0, 50.0, 400.0):
        assert abs(S(D, 0) - math.exp(-lam(D))) < 1e-12, "n_rep=0 debe dar exp(-lam)"
    rng = random.Random(20261109)
    N = 40000
    for D, n in ((100.0, 2), (800.0, 10), (4000.0, 60)):
        mc = sum(1 for _ in range(N) if poisson_sample(rng, lam(D)) <= n) / N
        print(f"Prueba D={D:.0f} Gy n_rep={n}: analitica {S(D, n):.4f} ; Monte Carlo {mc:.4f}")
        assert abs(mc - S(D, n)) < 0.01
    for n in ORG.values():
        d = d10(n)
        fino = min((abs(S(x, n) - 0.1), x) for x in [i * 0.5 for i in range(1, int(4 * d))])[1]
        assert abs(fino - d) / d < 0.01, (fino, d)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
