#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B127-C02: prima anual en orbita de un satelite SINTETICO con tasa de fallo Weibull.

CONTENIDO EDUCATIVO: no es una cotizacion ni asesoria financiera, legal o de seguros.
Consultado (2026-11-11): Gallagher, Space insurance market update Q1 2026 (10-04-2026): el loss ratio de suscripcion de 2025
pasa de ~15 % a ~75 % por un siniestro confirmado (SpainSat NG-2, asegurado por mas de 400 MUSD). Solo ilustra la volatilidad
de la clase; ningun parametro de este laboratorio sale de ahi.
ILUSTRATIVOS: forma beta y escala eta de Weibull, valor asegurado inicial, depreciacion, recargo.
Modelo: S(t) = exp(-(t/eta)^beta); probabilidad condicional de fallo en el anio k (t en anios): q_k = 1 - S(k+1)/S(k).
Valor asegurado del anio k: V_k = V0 * max(0, 1 - d*k). Prima del anio k (condicional a seguir vivo) = q_k * V_k * (1 + recargo); perdida esperada total = sum S(k) q_k V_k.
Unidades: anios, MUSD ficticios. Tolerancias: Monte Carlo (100000 satelites, semilla 127) frente a la formula: S(5) dentro de 0.005.
"""
from __future__ import annotations
import math, platform, random

BETA, ETA = 0.7, 120.0  # beta < 1: mortalidad infantil
V0, DEP, RECARGO = 150.0, 0.08, 0.30
ANIOS = 15


def S(t):
    return math.exp(-((t / ETA) ** BETA))


def q(k):
    return 1.0 - S(k + 1) / S(k) if k > 0 else 1.0 - S(1)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS; solo el contexto de volatilidad de mercado (Gallagher Q1 2026) es consultado.")
    print(f"Weibull beta = {BETA}, eta = {ETA} anios ; V0 = {V0} MUSD ; depreciacion {DEP:.0%}/anio ; recargo {RECARGO:.0%}")
    print(" anio  q_k(fallo)  S(fin)  V_k[MUSD]  prima[MUSD]  tasa comercial")
    total_pura = total_com = 0.0
    for k in range(ANIOS):
        vk = V0 * max(0.0, 1 - DEP * k)
        pura = q(k) * vk
        com = pura * (1 + RECARGO)
        total_pura += S(k) * pura  # ponderada por P(vivo al inicio del anio k)
        total_com += S(k) * com
        print(f" {k + 1:4d}  {q(k):9.5f}  {S(k + 1):7.4f}  {vk:9.2f}  {com:10.4f}  {com / vk if vk else 0:10.4%}")
    print(f"Perdida esperada total (ponderada por supervivencia) = {total_pura:.3f} MUSD ; con recargo = {total_com:.3f} MUSD")
    # Monte Carlo: tiempo de fallo ~ Weibull por inversion
    rng = random.Random(127)
    n = 100000
    vivos5, perdida_pura = 0, 0.0
    for _ in range(n):
        t = ETA * (-math.log(1 - rng.random())) ** (1 / BETA)
        if t > 5:
            vivos5 += 1
        k = int(t)
        if k < ANIOS:
            perdida_pura += V0 * max(0.0, 1 - DEP * k)
    mc5 = vivos5 / n
    print(f"S(5) analitica = {S(5):.4f} ; Monte Carlo = {mc5:.4f} ; diferencia = {abs(S(5) - mc5):.4f}")
    print(f"Perdida media 15 anios: analitica = {total_pura:.3f} ; Monte Carlo = {perdida_pura / n:.3f} MUSD")
    # primer anio frente a anio 10 (mortalidad infantil)
    print(f"Razon de tasa pura anio 1 / anio 10 = {q(0) / q(9):.2f}")
    assert abs(S(5) - mc5) < 0.005
    assert abs(total_pura - perdida_pura / n) / total_pura < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
