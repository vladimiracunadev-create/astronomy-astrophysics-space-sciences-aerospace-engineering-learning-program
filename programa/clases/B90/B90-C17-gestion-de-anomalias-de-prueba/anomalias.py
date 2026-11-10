#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C17: registro de anomalias de prueba SINTETICO, cota de confianza de Poisson y regla de disposicion.

Cota superior de la tasa de fallas con r fallas en T horas y confianza CL: lambda_U tal que P(X <= r | lambda_U T) = 1 - CL, X ~ Poisson.
Para r = 0: lambda_U = -ln(1 - CL)/T (comprobacion cerrada). Cobertura por Monte Carlo (semilla fija). Disposicion por severidad y repeticion
(regla DE EJEMPLO). Unidades: fallas/hora, horas. Tolerancias: cerrada 1e-9; cobertura >= CL - 0.01.
"""
import math
import sys
from collections import Counter
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: 12 anomalias de una campana de ensayos de una unidad de ejemplo")

def cdf(r, mu):
    return sum(math.exp(-mu) * mu**i / math.factorial(i) for i in range(r + 1))

def mu_sup(r, CL):
    lo, hi = 0.0, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if cdf(r, mid) > 1 - CL:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

CL = 0.90
print("r   mu_U (x T) con CL = 90 %")
for r in range(0, 6):
    print(f"{r:2d}   {mu_sup(r, CL):8.4f}")
comprobar(abs(mu_sup(0, CL) + math.log(1 - CL)) < 1e-9, "para r = 0 la cota es -ln(1 - CL)")
T = 500.0
lamU = mu_sup(1, CL) / T
print(f"Con 1 falla en {T:.0f} h: tasa superior = {lamU:.4e} /h ; MTBF inferior = {1 / lamU:.1f} h")

rng = np.random.default_rng(90)
N = 200_000
lam_v = 0.012
tabla = {x: mu_sup(x, CL) / T for x in range(0, 40)}
cubre = sum(1 for x in rng.poisson(lam_v * T, N) if tabla[min(int(x), 39)] >= lam_v)
print(f"Cobertura por Monte Carlo ({N} campanas, tasa verdadera {lam_v}/h): {cubre / N:.4f} (debe ser >= {CL})")
comprobar(cubre / N >= CL - 0.01, "la cota debe cubrir la tasa verdadera con la confianza nominal")

registro = [
    ("A01", "Vibracion", "S2", 1), ("A02", "Funcional", "S3", 1), ("A03", "Termovacio", "S1", 1), ("A04", "Funcional", "S3", 2),
    ("A05", "EMC", "S2", 1), ("A06", "Funcional", "S3", 3), ("A07", "Vibracion", "S1", 1), ("A08", "Despliegue", "S1", 1),
    ("A09", "Termovacio", "S3", 1), ("A10", "EMC", "S2", 2), ("A11", "Funcional", "S3", 4), ("A12", "Despliegue", "S2", 1),
]
def disposicion(sev, rep):
    if sev == "S1":
        return "detener, abrir no conformidad y revisar con el comite"
    if sev == "S2":
        return "analizar causa raiz antes de continuar" if rep == 1 else "detener y corregir"
    return "registrar y continuar" if rep < 3 else "analizar causa raiz (recurrente)"
print("id   ensayo       sev rep  disposicion")
for i, e, s, r in registro:
    print(f"{i}  {e:11s}  {s}  {r}   {disposicion(s, r)}")
por_ens = Counter(e for _, e, _, _ in registro)
print("Pareto por ensayo:", ", ".join(f"{k} {v}" for k, v in por_ens.most_common()))
sev = Counter(s for _, _, s, _ in registro)
print("Por severidad:", ", ".join(f"{k} {v}" for k, v in sorted(sev.items())))
comprobar(sum(por_ens.values()) == len(registro) == 12, "el registro debe tener 12 anomalias")
comprobar(por_ens.most_common(1)[0] == ("Funcional", 4), "el Pareto de ejemplo debe dar 4 anomalias funcionales")
fin()
