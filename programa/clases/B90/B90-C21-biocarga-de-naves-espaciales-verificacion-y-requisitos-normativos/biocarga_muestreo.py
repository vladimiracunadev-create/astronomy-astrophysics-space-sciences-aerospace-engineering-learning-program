#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C21: verificacion de biocarga por muestreo de superficies (SINTETICO).

Cada hisopo cubre un area a (m2) y tiene eficiencia de recuperacion e. Densidad estimada d = C / (e A) (esporas/m2) con C el total de colonias.
Cota superior de Poisson con confianza CL (P(X <= C | mu) = 1 - CL). Limite de ejemplo: 300 esporas/m2 (la pagina de proteccion planetaria de
NASA cita 300 esporas/m2 para el rover de Marte; aqui es solo un LIMITE DE EJEMPLO). Unidades: UFC, m2, esporas/m2. Cobertura por Monte Carlo.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: 20 hisopos de 0.01 m2 sobre superficies de una unidad de ejemplo")

def cdf(r, mu):
    return sum(math.exp(-mu) * mu**i / math.factorial(i) for i in range(r + 1))

def mu_sup(r, CL):
    lo, hi = 0.0, 200.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if cdf(r, mid) > 1 - CL else (lo, mid)
    return (lo + hi) / 2

a, n = 0.01, 20
e = 0.15
colonias = [0, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
C = sum(colonias)
A = a * n
print(f"Hisopos = {n} ; area total = {A:.2f} m2 ; colonias = {C} ; eficiencia de recuperacion = {e}")
d_obs = C / A
d_est = C / (e * A)
print(f"Densidad observada = {d_obs:.1f} /m2 ; corregida por recuperacion = {d_est:.1f} esporas/m2")
for CL in (0.80, 0.90, 0.95):
    mu = mu_sup(C, CL)
    print(f"   cota superior {CL * 100:.0f} %: {mu:.3f} colonias -> {mu / (e * A):.1f} esporas/m2")
mu95 = mu_sup(C, 0.95)
cota = mu95 / (e * A)
lim = 300.0
print(f"Limite de ejemplo = {lim:.0f} esporas/m2 -> cota 95 % = {cota:.1f} : {'CUMPLE' if cota <= lim else 'NO CUMPLE'} ; estimacion central: {'CUMPLE' if d_est <= lim else 'NO CUMPLE'}")
comprobar(d_est < lim < cota, "el ejemplo debe cumplir con la estimacion central pero no con la cota superior")
need = None
for k in range(1, 400):
    if mu_sup(C, 0.95) / (e * a * k) <= lim:
        need = k
        break
print(f"Hisopos necesarios para que la cota de 95 % cumpla con las mismas {C} colonias: {need} (area {need * a:.2f} m2)")
comprobar(need is not None and need > n, "hacen falta mas hisopos que los 20")

rng = np.random.default_rng(90)
for true_d in (150.0, 300.0):
    mu_v = true_d * e * A
    cubre = 0
    N = 100_000
    tab = {x: mu_sup(x, 0.95) / (e * A) for x in range(0, 60)}
    for x in rng.poisson(mu_v, N):
        cubre += tab[min(int(x), 59)] >= true_d
    print(f"Cobertura de la cota de 95 % con densidad verdadera {true_d:.0f} /m2: {cubre / N:.4f}")
    comprobar(cubre / N >= 0.95 - 0.005, "la cota debe cubrir la densidad verdadera con al menos 95 %")
print("Eficiencia de recuperacion -> densidad corregida [esporas/m2]")
for ee in (0.1, 0.3, 0.5, 1.0):
    print(f"   {ee:3.1f} -> {C / (ee * A):7.1f}")
fin()
