#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C15: difusion orbital en el mapa estandar; coeficiente D(K) frente a la teoria cuasi-lineal.

Datos: TODOS SINTETICOS (adimensionales). Mapa con momento sin envolver: p' = p + K sin(theta), theta' = theta + p' (theta modulo 2 pi).
Conjunto de 1000 particulas (semilla 73) con theta0 y p0 uniformes en [0, 2 pi); se mide <(p_n - p_0)^2> para n = 100..1000
y se ajusta D por regresion lineal por el origen: <(Delta p)^2> = D n. Errores estandar a partir de 5 submuestras de 200.
Teoria cuasi-lineal (fases aleatorias): D_ql = K^2 / 2. Correccion de primer orden por correlaciones: D / D_ql ~ 1 - 2 J_2(K) (J_2 por serie); no consultada.
Segunda via: el mapa de fases aleatorias (theta sorteado en cada paso) debe dar D = K^2/2 dentro del error estadistico: valida la maquinaria de Monte Carlo.
Exponente de transporte alfa: <(Dp)^2> ~ n^alfa entre n = 100 y 1000 (alfa = 1 es difusion normal; alfa = 2, balistico).
Tiempo de difusion para recorrer 2 pi en momento: tau = (2 pi)^2 / D.
Tolerancias: mapa de fases aleatorias dentro de 3 errores estandar de K^2/2 ; K = 5 y 10 con D/D_ql entre 0.4 y 1.6 y alfa entre 0.9 y 1.1; K = 6.5 con alfa > 1.3 (anomalo).
"""
from __future__ import annotations
import json, math, platform, random, sys

TWO_PI = 2 * math.pi
M = 1000
NMAX = 1000
CHECK = (100, 200, 400, 700, 1000)


def J2(x, terms=40):
    s = 0.0
    for m in range(terms):
        s += (-1) ** m / (math.factorial(m) * math.factorial(m + 2)) * (x / 2) ** (2 * m + 2)
    return s


def ensemble(K, rnd, azar):
    th = [rnd.uniform(0, TWO_PI) for _ in range(M)]
    p = [rnd.uniform(0, TWO_PI) for _ in range(M)]
    p0 = list(p)
    msd = {}
    for n in range(1, NMAX + 1):
        for i in range(M):
            if azar:
                th[i] = rnd.uniform(0, TWO_PI)
            p[i] += K * math.sin(th[i])
            th[i] = (th[i] + p[i]) % TWO_PI
        if n in CHECK:
            msd[n] = [(p[i] - p0[i]) ** 2 for i in range(M)]
    return msd


def ajustar(msd, idx):
    num = sum(n * (sum(msd[n][i] for i in idx) / len(idx)) for n in CHECK)
    den = sum(n * n for n in CHECK)
    return num / den


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    print(f"{M} particulas sinteticas (semilla 73), hasta {NMAX} iteraciones; D = <(Dp)^2>/n por regresion por el origen")
    print("    K       D medido   error est.   D_ql=K^2/2   D/D_ql    1-2 J2(K)   alfa   tau [iter] = (2 pi)^2/D")
    rnd = random.Random(73)
    for K, tag in ((1.0, "k1"), (3.0, "k3"), (5.0, "k5"), (6.5, "k65"), (10.0, "k10")):
        msd = ensemble(K, rnd, False)
        D = ajustar(msd, range(M))
        subs = [ajustar(msd, range(j * 200, (j + 1) * 200)) for j in range(5)]
        mu = sum(subs) / 5
        se = math.sqrt(sum((s - mu) ** 2 for s in subs) / 4 / 5)
        Dql = K * K / 2
        alfa = math.log(sum(msd[1000]) / sum(msd[100])) / math.log(10)
        print(f" {K:5.1f}   {D:10.4f}   {se:9.4f}   {Dql:10.4f}   {D / Dql:7.3f}   {1 - 2 * J2(K):9.3f}   {alfa:6.2f}   {(TWO_PI) ** 2 / D:14.1f}")
        out[f"al_{tag}"] = alfa
        out[f"D_{tag}"], out[f"se_{tag}"], out[f"r_{tag}"], out[f"rw_{tag}"], out[f"tau_{tag}"] = D, se, D / Dql, 1 - 2 * J2(K), TWO_PI**2 / D
    # fases aleatorias
    K = 5.0
    msd = ensemble(K, rnd, True)
    D = ajustar(msd, range(M))
    subs = [ajustar(msd, range(j * 200, (j + 1) * 200)) for j in range(5)]
    mu = sum(subs) / 5
    se = math.sqrt(sum((s - mu) ** 2 for s in subs) / 4 / 5)
    print(f"Mapa de fases aleatorias (K = 5): D = {D:.4f} +- {se:.4f} ; K^2/2 = {K * K / 2:.4f} ; diferencia = {abs(D - K * K / 2) / se:.2f} errores estandar")
    out.update(D_az=D, se_az=se, z_az=abs(D - K * K / 2) / se)
    assert abs(D - K * K / 2) < 3 * se
    assert 0.4 < out["r_k5"] < 1.6 and 0.4 < out["r_k10"] < 1.6
    assert 0.9 < out["al_k5"] < 1.1 and 0.9 < out["al_k10"] < 1.1 and out["al_k65"] > 1.3
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
