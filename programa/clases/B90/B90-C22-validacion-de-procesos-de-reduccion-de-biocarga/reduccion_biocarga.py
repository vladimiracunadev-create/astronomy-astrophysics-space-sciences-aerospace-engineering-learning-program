#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C22: reduccion logaritmica de biocarga con cinetica de primer orden (SINTETICO).

N(t) = N0 10^(-t/D); D(T) = D_ref 10^((T_ref - T)/z). Tiempo para n logaritmos: t = n D. Probabilidad de al menos un sobreviviente cuando
quedan en promedio mu = N0 10^(-t/D): 1 - exp(-mu). Los valores D_ref = 60 min a 125 C y z = 20 C son SINTETICOS (no de una norma ni de un material).
Comprobacion por Monte Carlo de sobrevivientes binomiales (semilla fija). Unidades: min, C, esporas.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: N0 = 10000 esporas; D = 60 min a 125 C; z = 20 C")
N0, Dref, Tref, z = 1.0e4, 60.0, 125.0, 20.0
D = lambda T: Dref * 10 ** ((Tref - T) / z)
print("T [C]   D [min]   t para 4 logaritmos [min]")
for T in (105, 115, 125, 135, 145):
    print(f"{T:5d}  {D(T):9.2f}  {4 * D(T):10.1f}")
comprobar(abs(D(Tref + z) - Dref / 10) < 1e-12, "aumentar z grados divide D por 10")
print("Exposicion a 125 C [min] -> esporas esperadas -> reduccion [log] -> P(al menos una sobreviviente)")
rng = np.random.default_rng(90)
for t in (120, 240, 360, 480, 600):
    mu = N0 * 10 ** (-t / Dref)
    sob = rng.binomial(int(N0), mu / N0, 1_000_000)
    p_mc = float(np.mean(sob >= 1))
    p_t = 1 - math.exp(-mu)
    print(f"{t:6d}   {mu:10.4g}   {math.log10(N0 / mu):5.1f}   {p_t:8.5f} (MC {p_mc:8.5f})")
    se = math.sqrt(max(p_t * (1 - p_t), 1e-12) / 1_000_000)
    comprobar(abs(p_mc - p_t) < 4 * se + 1e-4, "Monte Carlo y Poisson deben coincidir")
objetivo = 1e-3
t_req = Dref * math.log10(N0 / (-math.log(1 - objetivo)))
print(f"Tiempo para que P(sobreviviente) <= {objetivo}: {t_req:.0f} min a 125 C = {t_req / Dref:.2f} D ({math.log10(N0 / -math.log(1 - objetivo)):.2f} log)")
comprobar(1 - math.exp(-N0 * 10 ** (-t_req / Dref)) <= objetivo * (1 + 1e-9), "el tiempo calculado debe cumplir el objetivo")
t_marg = 2 * t_req
print(f"Con margen de 2 x el tiempo (practica de ejemplo): {t_marg:.0f} min -> P = {1 - math.exp(-N0 * 10 ** (-t_marg / Dref)):.2e}")
print("Tiempo equivalente a otra temperatura para igual letalidad (a 115 y 135 C) [min]")
for T in (115, 135):
    print(f"   {T} C: {t_req * D(T) / Dref:.0f}")
fin()
