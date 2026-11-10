#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C17: supervivencia de un compuesto organico a la radiolisis y exceso enantiomerico con incertidumbre (SINTETICOS).

Datos: SINTETICOS / ILUSTRATIVOS. Tasa de dosis 1.0e-3 Gy por ano, dosis caracteristica de destruccion D0 = 1.0e6 Gy, tiempos de 1e6 a 4.5e9 anos; fracciones L y D de un aminoacido hipotetico con p_L = 0.55.
Ningun valor procede de una medicion ni de una fuente consultada; la bibliografia sobre aminoacidos y nucleobases en meteoritos (p. ej. Callahan et al. 2011) NO se consulto con exito y no se usa.
Modelo: S = exp(-D/D0) con D = tasa_dosis * t ; exceso enantiomerico ee = (L - D)/(L + D) con L ~ Binomial(N, p) y desviacion analitica sigma_ee = sqrt((1 - ee^2)/N) para N moleculas contadas.
Supuestos: destruccion de primer orden en la dosis; sin produccion simultanea; conteo independiente. Validez: ilustrativa.
Tolerancia: sigma_ee Monte Carlo vs analitica a 5 %; ee medio Monte Carlo vs verdadero a 3 sigma.
"""
from __future__ import annotations
import math, platform, random

TASA = 1.0e-3     # Gy/ano
D0 = 1.0e6        # Gy

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("A. Supervivencia S = exp(-D/D0) (tasa 1e-3 Gy/ano, D0 = 1e6 Gy; ILUSTRATIVOS)")
    print("t [anos]    dosis [Gy]    S")
    for t in (1e6, 1e8, 1e9, 4.5e9):
        D = TASA * t
        print(f"{t:8.1e}    {D:9.3e}   {math.exp(-D / D0):.6f}")
    t_half = D0 * math.log(2.0) / TASA
    print(f"B. Tiempo para que sobreviva la mitad = D0 ln2 / tasa = {t_half:.4e} anos")
    assert abs(math.exp(-TASA * t_half / D0) - 0.5) < 1e-12
    # dosis necesaria para S = 1 %
    D01 = D0 * math.log(100.0)
    print(f"   dosis para S = 1 % : {D01:.4e} Gy ; tiempo = {D01 / TASA:.4e} anos")
    # exceso enantiomerico
    p = 0.55
    ee_v = 2 * p - 1
    print(f"C. Exceso enantiomerico verdadero ee = (L-D)/(L+D) = 2p - 1 = {ee_v:.3f} (p_L = 0.55 SINTETICO)")
    print("N molec.   ee medio MC   sigma MC     sigma analitica   ee/sigma")
    rng = random.Random(1789)
    for N in (100, 1000, 10000):
        ees = []
        for _ in range(2000):
            L = sum(1 for _ in range(N) if rng.random() < p) if N <= 1000 else int(round(rng.gauss(N * p, math.sqrt(N * p * (1 - p)))))
            ees.append((2 * L - N) / N)
        m = sum(ees) / len(ees)
        sd = math.sqrt(sum((x - m) ** 2 for x in ees) / (len(ees) - 1))
        sa = math.sqrt((1 - ee_v ** 2) / N)
        print(f"{N:8d}   {m:9.4f}   {sd:9.4f}   {sa:12.4f}      {ee_v / sa:6.2f}")
        assert abs(sd - sa) / sa < 0.05, (N, sd, sa)
        assert abs(m - ee_v) < 3 * sa / math.sqrt(len(ees)) + 1e-3
    print("D. Con ee = 0.10 y N = 100 el cociente ee/sigma es", round(0.10 / math.sqrt((1 - 0.1 ** 2) / 100), 2), "(no distinguible de 0 a 3 sigma)")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
