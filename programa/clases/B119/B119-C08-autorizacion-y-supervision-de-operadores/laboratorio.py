#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C08: autorizacion y supervision de operadores: tiempo de tramite como cola M/M/1 y supervision por muestreo (SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11, nota de legal.un.org y resumen de busqueda de UNOOSA): art. VI del Tratado del Espacio Ultraterrestre: las actividades de entidades no
gubernamentales requieren autorizacion y supervision continua del Estado parte pertinente; el Estado responde internacionalmente.
NO consultado: ninguna ley nacional de licencias ni requisitos concretos.
SINTETICO: tasa de llegada de solicitudes lambda = 3 por mes; tasa de tramitacion mu = 4 por mes; cola M/M/1 (supuesto: llegadas de Poisson, servicio exponencial).
Formulas M/M/1: rho = lambda/mu; tiempo medio en el sistema W = 1/(mu - lambda); en cola Wq = rho/(mu - lambda). Simulacion con semilla 119, N = 200000 solicitudes.
Supervision: n operadores, inspeccion aleatoria de k por periodo; P(operador no inspeccionado en m periodos) = (1 - k/n)^m.
Tolerancia: tiempo medio simulado vs analitico dentro del 3 % (en estado estacionario).
"""
import json, platform, random

lam, mu = 3.0, 4.0
rho = lam / mu
W = 1 / (mu - lam)
Wq = rho / (mu - lam)
rng = random.Random(119)
N = 200000
t_llegada = 0.0
libre = 0.0
suma_sist = suma_cola = 0.0
warm = 5000
cont = 0
for i in range(N):
    t_llegada += rng.expovariate(lam)
    inicio = max(t_llegada, libre)
    fin = inicio + rng.expovariate(mu)
    libre = fin
    if i >= warm:
        suma_sist += fin - t_llegada
        suma_cola += inicio - t_llegada
        cont += 1
W_sim, Wq_sim = suma_sist / cont, suma_cola / cont
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Tramite SINTETICO M/M/1 (lambda = 3, mu = 4 solicitudes/mes); art. VI consultado 2026-11-11; ninguna ley nacional consultada.")
print(f"rho = {rho:.2f} ; W analitico = {W:.3f} mes ; simulado {W_sim:.3f} ; Wq analitico = {Wq:.3f} ; simulado {Wq_sim:.3f}")
assert abs(W_sim - W) / W < 0.03 and abs(Wq_sim - Wq) / Wq < 0.05
print("Efecto de reforzar el servicio (mu): ")
for m in (3.5, 4.0, 5.0, 6.0):
    print(f"   mu = {m:3.1f}  W = {1 / (m - lam):6.3f} mes  ({30 / (m - lam):6.1f} dias)")
n_op, k = 60, 12
for m in (1, 3, 5):
    print(f"Supervision: {k} de {n_op} operadores por periodo; P(no inspeccionado en {m} periodos) = {(1 - k / n_op) ** m:.4f}")
pm5 = (1 - k / n_op) ** 5
print("CLAVES " + json.dumps({"rho": "%.2f" % rho, "W": "%.3f" % W, "Wq": "%.3f" % Wq, "dias": "%.0f" % (30 * W), "W5": "%.3f" % (1 / (5 - lam)), "pm5": "%.4f" % pm5, "pm1": "%.2f" % (1 - k / n_op), "Wsim": "%.3f" % W_sim}))
print("Pruebas superadas.")
