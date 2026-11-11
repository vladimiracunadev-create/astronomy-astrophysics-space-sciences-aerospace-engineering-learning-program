#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C27: negociacion estilizada entre dos Estados tras un incidente espacial sintetico: solucion de Nash y ofertas alternadas de Rubinstein.

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no representa ninguna negociacion real.
Texto consultado (2026-11-11): art. IX del Tratado del Espacio Ultraterrestre (nota legal.un.org): cooperacion y asistencia mutua considerando los intereses de las demas partes, y consultas
cuando una actividad pueda causar interferencia perjudicial; Convenio de Registro (UNOOSA), art. VI: ayuda para identificar objetos. NO consultado: ninguna practica diplomatica ni arbitraje.
Modelo (teoria de juegos, no consultada en una fuente concreta; verificada por induccion hacia atras y enumeracion): excedente a repartir = 100 u.u. (unidades de utilidad sinteticas);
puntos de desacuerdo d1 = 10 y d2 = 20. Nash: x1 = d1 + (S - d1 - d2)/2 con S = 100. Rubinstein con factores de descuento d1f = 0.90 y d2f = 0.80:
parte del primer proponente = (1 - d2f) / (1 - d1f d2f) (limite de horizonte infinito); se verifica con induccion hacia atras en 400 rondas.
Tolerancia: induccion hacia atras vs formula cerrada < 1e-9.
"""
import json, platform

S = 100.0
d1, d2 = 10.0, 20.0
x1_nash = d1 + (S - d1 - d2) / 2.0
x2_nash = S - x1_nash
# enumeracion: maximizar (x1 - d1)(x2 - d2)
mejor = max(((i / 100.0 - d1) * (S - i / 100.0 - d2), i / 100.0) for i in range(int(d1 * 100), int((S - d2) * 100) + 1))
assert abs(mejor[1] - x1_nash) < 0.011
del1, del2 = 0.90, 0.80
cerrado = (1 - del2) / (1 - del1 * del2)
def induccion(T, d1f, d2f):
    """Parte del jugador 1 (proponente en rondas impares) por induccion hacia atras en T rondas."""
    v = 1.0                                   # ronda T: el proponente se queda con todo
    for t in range(T - 1, 0, -1):             # t = T-1, ..., 1
        d_resp = d2f if t % 2 == 1 else d1f   # en rondas impares responde el jugador 2
        v = 1.0 - d_resp * v
    return v if T % 2 == 1 else None
v401 = induccion(401, del1, del2)
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Negociacion ESTILIZADA con utilidades SINTETICAS; art. IX y art. VI (Registro) consultados 2026-11-11; practica diplomatica NO consultada.")
print(f"Nash: excedente {S - d1 - d2:.0f}; parte del Estado 1 = {x1_nash:.1f} ; del Estado 2 = {x2_nash:.1f}")
print(f"Rubinstein (descuentos {del1}/{del2}): parte del primer proponente en horizonte infinito = {cerrado:.4f}")
print(f"Induccion hacia atras con 401 rondas: {v401:.6f}")
assert abs(v401 - cerrado) < 1e-9
# sensibilidad: si el Estado 2 es mas impaciente
for dd in (0.6, 0.8, 0.95):
    print(f"   descuento del Estado 2 = {dd:.2f}: parte del primer proponente = {(1 - dd) / (1 - del1 * dd):.4f}")
print("CLAVES " + json.dumps({"n1": "%.1f" % x1_nash, "n2": "%.1f" % x2_nash, "rub": "%.4f" % cerrado, "rub2": "%.3f" % (1 - cerrado), "s6": "%.4f" % ((1 - 0.6) / (1 - del1 * 0.6)), "s95": "%.4f" % ((1 - 0.95) / (1 - del1 * 0.95))}))
print("Pruebas superadas.")
