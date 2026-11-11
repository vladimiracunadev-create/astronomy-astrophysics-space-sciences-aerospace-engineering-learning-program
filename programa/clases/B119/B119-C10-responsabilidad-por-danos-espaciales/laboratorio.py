#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C10: exposicion a danos espaciales: probabilidad de colision, dano esperado y su incertidumbre (SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11, resumen de busqueda de UNOOSA sobre el Convenio de Responsabilidad): el Estado de lanzamiento responde por los danos que cause su objeto
espacial (absoluta en la superficie; por culpa en el espacio). NO consultado: texto completo ni practica de reclamaciones.
Formulas (no consultadas en una fuente concreta; verificadas por Monte Carlo): P(al menos un impacto en T) = 1 - exp(-F A T) con flujo F; para una conjuncion con error
gaussiano isotropico sigma y radio combinado R << sigma: Pc ~ (R^2 / (2 sigma^2)) exp(-d^2 / (2 sigma^2)), d = distancia de paso nominal.
SINTETICO: F = 2e-5 impactos/m2/ano; A = 12 m2; T = 5 anos; dano D = 80 u.m. (unidades monetarias sinteticas); conjuncion R = 10 m, sigma = 50 m, d = 60 m.
Semilla 119; N = 400000. Tolerancia: Monte Carlo a 3 sigma.
"""
import json, math, platform, random

rng = random.Random(119)
F, A, T, D = 2e-5, 12.0, 5.0, 80.0
P = 1 - math.exp(-F * A * T)
E = P * D
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Flujo, area y dano SINTETICOS; Convenio de Responsabilidad solo por resumen de busqueda (2026-11-11).")
print(f"P(impacto en {T:.0f} anos) = {P:.6f} ; dano esperado = {E:.4f} u.m.")
# Monte Carlo de Poisson
N = 400000
lam = F * A * T
def poisson(l):
    L, k, p = math.exp(-l), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1
mc = sum(1 for _ in range(N) if poisson(lam) > 0) / N
sig = math.sqrt(P * (1 - P) / N)
print(f"Monte Carlo: {mc:.6f} (sigma {sig:.6f})")
assert abs(mc - P) < 3 * sig
# Conjuncion
Rr, s, d = 10.0, 50.0, 60.0
Pc = Rr ** 2 / (2 * s ** 2) * math.exp(-d ** 2 / (2 * s ** 2))
cuenta = 0
for _ in range(N):
    x = rng.gauss(d, s); y = rng.gauss(0.0, s)
    if x * x + y * y <= Rr * Rr:
        cuenta += 1
mcc = cuenta / N
sigc = math.sqrt(Pc * (1 - Pc) / N)
print(f"Conjuncion: Pc analitica {Pc:.5f} ; Monte Carlo {mcc:.5f} (sigma {sigc:.5f}) ; dano esperado {Pc * D:.4f} u.m.")
assert abs(mcc - Pc) < 4 * sigc + 2e-4
# Sensibilidad: F varia por un factor 3
for fac in (1 / 3, 1.0, 3.0):
    p = 1 - math.exp(-F * fac * A * T)
    print(f"   flujo x{fac:4.2f}: P = {p:.6f} ; dano esperado = {p * D:.4f} u.m.")
print("CLAVES " + json.dumps({"P": "%.6f" % P, "E": "%.4f" % E, "Pc": "%.5f" % Pc, "Ec": "%.3f" % (Pc * D), "lam": "%.4f" % lam, "mc": "%.5f" % mcc, "p3": "%.6f" % (1 - math.exp(-3 * lam))}))
print("Pruebas superadas.")
