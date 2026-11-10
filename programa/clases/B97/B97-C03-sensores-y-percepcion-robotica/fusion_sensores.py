#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C03: fusion de dos sensores de distancia por varianza inversa.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): distancia verdadera 12.0 m; sensor A (lidar) sigma = 0.05 m; sensor B (camara de tiempo de vuelo)
sigma = 0.20 m; sesgo del sensor B de 0.10 m en el caso con sesgo; 200000 muestras con semilla fija.
Modelo: medidas independientes z_i = d + b_i + e_i, e_i ~ N(0, s_i^2). Estimador de varianza minima: d_hat = (z_A/s_A^2 + z_B/s_B^2)/(1/s_A^2 + 1/s_B^2);
varianza teorica 1/(1/s_A^2 + 1/s_B^2). Promedio de N lecturas: s/sqrt(N).
Segunda via: desviacion tipica empirica por Monte Carlo (tolerancia 1% relativa) y sesgo teorico w_B b_B.
Unidades SI. Sin correlacion entre sensores ni ruido no gaussiano.
"""
from __future__ import annotations
import math, platform, random

D, SA, SB, BIAS, N, SEMILLA = 12.0, 0.05, 0.20, 0.10, 200000, 20261110   # ILUSTRATIVOS / SINTETICOS


def calc():
    rng = random.Random(SEMILLA)
    wa, wb = 1 / SA ** 2, 1 / SB ** 2
    sf = 1 / math.sqrt(wa + wb)
    fa, fb = wa / (wa + wb), wb / (wa + wb)
    est, estb = [], []
    for _ in range(N):
        za = D + rng.gauss(0, SA)
        zb = D + rng.gauss(0, SB)
        est.append(fa * za + fb * zb)
        estb.append(fa * za + fb * (zb + BIAS))
    m = sum(est) / N
    s = math.sqrt(sum((e - m) ** 2 for e in est) / (N - 1))
    mb = sum(estb) / N
    return dict(sf=sf, fa=fa, fb=fb, s_emp=s, rel=abs(s - sf) / sf, sesgo=mb - D, sesgo_teo=fb * BIAS, sin_b=m - D,
                n_igual=math.ceil((SA / sf) ** 2), s_prom16=SA / math.sqrt(16), mejora=SA / sf)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: d = {D} m; sigma_A = {SA} m; sigma_B = {SB} m; semilla {SEMILLA}; N = {N}")
    print(f"Pesos: w_A = {r['fa']:.4f}, w_B = {r['fb']:.4f}")
    print(f"sigma fusionada teorica = {r['sf']*1000:.3f} mm; empirica = {r['s_emp']*1000:.3f} mm (diferencia relativa {r['rel']:.2e})")
    print(f"Sesgo sin sesgo de B = {r['sin_b']*1000:.3f} mm; con sesgo de B = {BIAS*1000:.0f} mm -> {r['sesgo']*1000:.3f} mm (teorico {r['sesgo_teo']*1000:.3f} mm)")
    print(f"Promediar 16 lecturas de A da {r['s_prom16']*1000:.2f} mm; mejora de la fusion respecto de A solo = x{r['mejora']:.4f}")
    assert r["rel"] < 0.01 and abs(r["sesgo"] - r["sesgo_teo"]) < 5e-4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
