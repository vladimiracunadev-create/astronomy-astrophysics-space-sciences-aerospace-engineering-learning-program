#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B127-C05: modelo de frecuencia y severidad, prima pura y perdida agregada de una cartera SINTETICA.

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de seguros, ni un calculo actuarial profesional.
Consultado (2026-11-11): Gallagher, Space insurance market update Q1 2026 (10-04-2026): definicion de loss ratio como
siniestros / primas y el salto de ~15 % a ~75 % en 2025 por un siniestro. Ningun parametro sale de ahi.
ILUSTRATIVOS: tasa verdadera de siniestros, severidad lognormal, tamano de la cartera, recargo, historia simulada.
Modelo: N ~ Poisson(lambda * n_sat) por anio; severidades X_i ~ Lognormal(mu, s); S = sum X_i (Poisson compuesto).
E[S] = lam E[X]; Var[S] = lam E[X^2]; E[X] = exp(mu + s^2/2); E[X^2] = exp(2 mu + 2 s^2).
Estimacion: lam_hat = siniestros / satelite-anio; intervalo normal 95 % lam_hat +- 1.96 sqrt(lam_hat / exposicion).
Unidades: siniestros por satelite-anio, MUSD ficticios. Tolerancias: media de S de Monte Carlo (20000 anios, semilla 127)
frente a la formula: error relativo < 2 %; varianza < 8 %.
"""
from __future__ import annotations
import math, platform, random

LAM_VERDADERA = 0.06  # siniestros por satelite-anio (sintetico)
MU, S = 2.5, 1.3  # severidad ln(MUSD)
N_SAT = 40
RECARGO_K = 0.5  # principio de desviacion estandar


def poisson(rng, lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS; solo la definicion de loss ratio (Gallagher Q1 2026) es consultada.")
    ex = math.exp(MU + S * S / 2)
    ex2 = math.exp(2 * MU + 2 * S * S)
    print(f"Severidad: media = {ex:.3f} MUSD ; desviacion = {math.sqrt(ex2 - ex * ex):.3f} MUSD (cola pesada: CV = {math.sqrt(ex2 - ex * ex) / ex:.2f})")
    rng = random.Random(127)
    # historia simulada de 200 satelite-anios
    exposicion = 200
    cuenta = poisson(rng, LAM_VERDADERA * exposicion)
    lam_hat = cuenta / exposicion
    ee = math.sqrt(lam_hat / exposicion)
    print(f"Historia SIMULADA: {cuenta} siniestros en {exposicion} satelite-anios ; lam_hat = {lam_hat:.4f} (verdadera {LAM_VERDADERA})")
    print(f"Intervalo 95 % = [{lam_hat - 1.96 * ee:.4f}, {lam_hat + 1.96 * ee:.4f}] ; ancho relativo = {3.92 * ee / lam_hat:.0%}")
    prima_pura_sat = LAM_VERDADERA * ex
    print(f"Prima pura por satelite-anio = lam * E[X] = {prima_pura_sat:.4f} MUSD")
    lam = LAM_VERDADERA * N_SAT
    media_S, var_S = lam * ex, lam * ex2
    sd_S = math.sqrt(var_S)
    print(f"Cartera de {N_SAT} satelites: E[S] = {media_S:.3f} ; sd[S] = {sd_S:.3f} MUSD ; CV = {sd_S / media_S:.2f}")
    prima_sd = media_S + RECARGO_K * sd_S
    print(f"Prima por principio de desviacion estandar (k = {RECARGO_K}) = {prima_sd:.3f} MUSD ; recargo = {prima_sd / media_S - 1:.1%}")
    # Monte Carlo de la perdida agregada anual
    n = 20000
    tot = []
    for _ in range(n):
        k = poisson(rng, lam)
        tot.append(sum(rng.lognormvariate(MU, S) for _ in range(k)))
    tot.sort()
    m = sum(tot) / n
    v = sum((x - m) ** 2 for x in tot) / (n - 1)
    print(f"Monte Carlo ({n} anios): media = {m:.3f} ; sd = {math.sqrt(v):.3f} ; error media = {abs(m - media_S) / media_S:.2%} ; error varianza = {abs(v - var_S) / var_S:.2%}")
    print(f"Cuantil 95 % = {tot[int(0.95 * n)]:.2f} ; cuantil 99 % = {tot[int(0.99 * n)]:.2f} MUSD ; P(S = 0) = {sum(1 for x in tot if x == 0) / n:.4f} (teorica {math.exp(-lam):.4f})")
    lr = [x / prima_sd for x in tot]
    print(f"Loss ratio con la prima {prima_sd:.2f}: mediana = {lr[n // 2]:.0%} ; P(loss ratio > 100 %) = {sum(1 for x in lr if x > 1) / n:.3f}")
    assert abs(m - media_S) / media_S < 0.02
    assert abs(v - var_S) / var_S < 0.08
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
