#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C20: presupuesto de incertidumbre de una velocidad orbital.

Datos: GM = 3.986004e14 m3/s2 y radio ecuatorial nominal 6.3781e6 m (IAU 2015
B3, arXiv:1510.07674, consultado 2026-11-05). Altitud h = 400 000 m con
lecturas SINTETICAS repetidas: n = 9, s = 300 m (ILUSTRATIVO). Tolerancia
del radio de referencia +-500 m rectangular y u_rel(GM) = 1e-9, ambos
ILUSTRATIVOS.
Modelo: v = sqrt(GM/(R + h)). Componentes: A (repeticiones de h, tipo A, nu = 8),
B1 (radio de referencia, tipo B rectangular), B2 (GM, tipo B).
Metodo: ley de propagacion del GUM, formula de Welch-Satterthwaite (G.4.1),
incertidumbre expandida U = k u_c y contraste con Monte Carlo (M = 1e6).
Supuestos: entradas independientes; tipo B con grados de libertad infinitos.
Validez: modelo casi lineal (u/x ~ 1e-4). Tolerancia: u_c de GUM frente a
Monte Carlo (h normal) a menos de 0.5 %; con h ~ t(8) escalada a menos de
10 %. Las pruebas detienen la ejecucion si fallan.
"""
import math
import platform

import numpy as np
import scipy
from scipy import stats

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")
GM, R, h = 3.986004e14, 6.3781e6, 400_000.0
a = R + h
v = math.sqrt(GM / a)
n, s = 9, 300.0
uA = s / math.sqrt(n)
uB1 = 500.0 / math.sqrt(3)
uGM = 1e-9 * GM
c_a = -0.5 * v / a
c_GM = 0.5 * v / GM
comp = {"A  altitud (9 lecturas)": (c_a * uA, 8), "B1 radio de referencia": (c_a * uB1, math.inf), "B2 GM": (c_GM * uGM, math.inf)}
uc = math.sqrt(sum(c**2 for c, _ in comp.values()))
print(f"v = {v:.4f} m/s; coeficientes: c_a = {c_a:.4e} (m/s)/m, c_GM = {c_GM:.4e} (m/s)/(m3/s2)")
print("componente                  u_i(v) [m/s]   % de la varianza   nu")
for name, (c, nu) in comp.items():
    print(f"{name:26s}  {abs(c):.5f}        {100*c**2/uc**2:6.2f}           {nu}")
print(f"u_c(v) = {uc:.5f} m/s;  relativa = {uc/v:.2e}")
assert abs(sum(c**2 for c, _ in comp.values()) / uc**2 - 1) < 1e-12

# Welch-Satterthwaite (G.2a)
den = sum(c**4 / nu for c, nu in comp.values() if math.isfinite(nu))
nu_eff = uc**4 / den
k95 = stats.t.ppf(0.975, nu_eff)
print(f"nu_eff = {nu_eff:.1f}; k(95 %) = {k95:.3f}; U = k u_c = {k95*uc:.4f} m/s")

# Monte Carlo (h normal) y variante con t(8)
rng = np.random.default_rng(2020)
M = 1_000_000
def mc(hs):
    Rr = rng.uniform(R - 500, R + 500, M)
    G = rng.normal(GM, uGM, M)
    return np.sqrt(G / (Rr + hs))
vm = mc(rng.normal(h, uA, M))
print(f"MC (h normal): u = {vm.std():.5f} m/s; IC 95 % = [{np.percentile(vm, 2.5):.4f}, {np.percentile(vm, 97.5):.4f}]")
assert abs(vm.std() / uc - 1) < 0.005
vt = mc(h + uA * rng.standard_t(8, M))
print(f"MC (h ~ t(8) escalada): u = {vt.std():.5f} m/s (la t de 8 gl tiene desviacion sqrt(8/6) = 1.155 veces la normal)")
assert abs(vt.std() / uc - 1) < 0.10

req = 0.25
print(f"requisito u_c <= {req} m/s: {'CUMPLE' if uc <= req else 'NO CUMPLE'}; componente dominante: B1")
assert uc <= req
# informe
print(f"informe: v = {v:.3f} m/s, u_c = {uc:.3f} m/s (k = 1); U = {k95*uc:.3f} m/s (k = {k95:.2f}, ~95 %); u_c/v = {uc/v:.1e}")
# mejora: reducir la tolerancia del radio de referencia a +-100 m
uB1b = 100.0 / math.sqrt(3)
uc2 = math.sqrt((c_a * uA) ** 2 + (c_a * uB1b) ** 2 + (c_GM * uGM) ** 2)
print(f"con tolerancia de +-100 m en el radio: u_c = {uc2:.5f} m/s ({100*(1-uc2/uc):.1f} % menos)")
print("Pruebas superadas.")
