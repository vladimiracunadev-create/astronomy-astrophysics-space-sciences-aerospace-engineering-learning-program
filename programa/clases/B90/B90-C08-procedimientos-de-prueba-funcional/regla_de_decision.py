#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C08: regla de decision con banda de guarda en una prueba funcional SINTETICA.

Producto: tension de salida de un regulador, limite superior de especificacion U_L = 5.25 V. Valor verdadero t ~ N(5.00, 0.08);
medida x = t + e, e ~ N(0, s_m), con incertidumbre expandida U = 2 s_m = 0.02 V (k = 2).
Regla: aceptar si x <= U_L - w. Se estiman por Monte Carlo (semilla fija) y por cuadratura numerica la probabilidad de falsa aceptacion
PFA = P(aceptado y t > U_L) y de falso rechazo PFR = P(rechazado y t <= U_L). Unidades: V. Tolerancia: 4 errores estandar de Monte Carlo.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: regulador de 5 V, limite 5.25 V, produccion N(5.00; 0.08) V, medida con U = 0.02 V (k = 2)")
mu, sd, UL, Uexp = 5.00, 0.08, 5.25, 0.02
sm = Uexp / 2
Phi = np.vectorize(lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2))))

def cuadratura(w):
    t = np.linspace(mu - 8 * sd, mu + 8 * sd, 400001)
    dt = t[1] - t[0]
    f = np.exp(-0.5 * ((t - mu) / sd) ** 2) / (sd * math.sqrt(2 * math.pi))
    p_acepta = Phi((UL - w - t) / sm)
    pfa = float(np.sum(f * p_acepta * (t > UL)) * dt)
    pfr = float(np.sum(f * (1 - p_acepta) * (t <= UL)) * dt)
    return pfa, pfr

rng = np.random.default_rng(90)
N = 4_000_000
t = rng.normal(mu, sd, N)
x = t + rng.normal(0, sm, N)
print(f"Fraccion fuera de especificacion (verdadera) = {np.mean(t > UL) * 100:.4f} %")
print("w [V]   regla         PFA [%]    PFR [%]   (Monte Carlo ; cuadratura)")
res = {}
for w, nombre in ((0.0, "sin guarda"), (Uexp, "guarda U"), (2 * Uexp, "guarda 2U")):
    ac = x <= UL - w
    pfa_mc = float(np.mean(ac & (t > UL)))
    pfr_mc = float(np.mean(~ac & (t <= UL)))
    pfa_q, pfr_q = cuadratura(w)
    res[w] = (pfa_mc, pfr_mc, pfa_q, pfr_q)
    print(f"{w:5.2f}  {nombre:11s} {pfa_mc * 100:9.4f} {pfr_mc * 100:9.4f}   ({pfa_q * 100:.4f} ; {pfr_q * 100:.4f})")
    for mc, q in ((pfa_mc, pfa_q), (pfr_mc, pfr_q)):
        se = math.sqrt(max(q * (1 - q), 1e-12) / N)
        comprobar(abs(mc - q) <= 4 * se + 1e-6, "Monte Carlo y cuadratura deben coincidir")
comprobar(res[0.0][2] > res[Uexp][2] > res[2 * Uexp][2], "la banda de guarda debe reducir la falsa aceptacion")
comprobar(res[0.0][3] < res[Uexp][3] < res[2 * Uexp][3], "la banda de guarda debe aumentar el falso rechazo")

# Procedimiento: pasos con valor esperado, tolerancia y resultado (medidas SINTETICAS)
pasos = [
    ("1", "Tension del riel de 5 V", 5.00, 0.25, 5.07),
    ("2", "Corriente en reposo [mA]", 85.0, 15.0, 92.4),
    ("3", "Respuesta al telecomando de eco [ms]", 120.0, 30.0, 151.0),
    ("4", "Tension de la bateria [V]", 8.20, 0.40, 8.31),
]
print("paso  magnitud                               esperado  tol    medido  |dif|/tol  decision (guarda U = 2 % del valor esperado)")
for pid, nom, esp, tol, med in pasos:
    Ux = 0.02 * abs(esp)
    dif = abs(med - esp)
    dec = "PASA" if dif <= tol - Ux else ("INDETERMINADO" if dif <= tol + Ux else "FALLA")
    print(f"  {pid}   {nom:37s} {esp:8.2f} {tol:5.2f} {med:8.2f}  {dif / tol:8.2f}   {dec}")
comprobar(all(p[4] != p[2] for p in pasos), "las medidas de ejemplo no coinciden exactamente con el valor esperado")
fin()
