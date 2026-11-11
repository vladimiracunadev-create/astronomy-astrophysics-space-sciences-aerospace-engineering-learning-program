#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C14: amenazas ciberneticas a satelites, nivel DEFENSIVO: arbol de ataque abstracto y riesgo residual con controles (SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera. No describe tecnicas, vulnerabilidades ni procedimientos de ataque.
Texto consultado (2026-11-11): art. VI del tratado de 1967 (nota legal.un.org): el Estado responde de las actividades nacionales y exige autorizacion y supervision continua;
 NO consultado: ninguna norma de ciberseguridad (p. ej. estandares de CCSDS, NIST, ISO), informe de incidente ni vulnerabilidad real.
Modelo: arbol AND/OR con nodos hoja abstractos ("A: acceso al segmento terreno", "B: acceso al enlace", "C: elusion de autenticacion", "D: error de operador") y probabilidades
anuales SINTETICAS; un control reduce la probabilidad de una hoja por un factor de efectividad. Compuerta OR: 1 - prod(1 - p); AND: prod(p) (supuesto de independencia).
Verificacion: Monte Carlo con semilla 119, N = 400000, a 3 sigma.
"""
import json, math, platform, random

HOJAS = {"A": 0.10, "B": 0.05, "C": 0.20, "D": 0.08}
def or_(*p):
    q = 1.0
    for x in p: q *= 1 - x
    return 1 - q
def and_(*p):
    q = 1.0
    for x in p: q *= x
    return q
def riesgo(h):
    # exito del evento = (A AND C) OR (B AND C) OR D
    return or_(and_(h["A"], h["C"]), and_(h["B"], h["C"]), h["D"])

base = riesgo(HOJAS)
CONTROLES = {"autenticacion_reforzada": ("C", 0.5), "segmentacion_de_red": ("A", 0.5), "formacion_y_doble_verificacion": ("D", 0.5), "cifrado_del_enlace": ("B", 0.5)}
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Arbol DEFENSIVO abstracto con probabilidades SINTETICAS; ninguna norma ni vulnerabilidad real consultada (art. VI consultado 2026-11-11).")
print(f"Riesgo anual base (evento = (A y C) o (B y C) o D): {base:.5f}")
res = {}
for nombre, (hoja, f) in CONTROLES.items():
    h = dict(HOJAS); h[hoja] *= f
    r = riesgo(h)
    res[nombre] = r
    print(f"  control {nombre:32s}: riesgo {r:.5f}  reduccion {100 * (1 - r / base):5.1f} %")
todos = dict(HOJAS)
for hoja, f in CONTROLES.values(): todos[hoja] *= f
r_todos = riesgo(todos)
print(f"Con los cuatro controles: riesgo {r_todos:.5f} ({100 * (1 - r_todos / base):.1f} % menos)")
rng = random.Random(119)
N = 400000
cuenta = 0
for _ in range(N):
    s = {k: rng.random() < v for k, v in HOJAS.items()}
    if (s["A"] and s["C"]) or (s["B"] and s["C"]) or s["D"]:
        cuenta += 1
mc = cuenta / N
sig = math.sqrt(base * (1 - base) / N)
print(f"Monte Carlo del riesgo base: {mc:.5f} (sigma {sig:.5f})")
assert abs(mc - base) < 3 * sig
mejor = min(res, key=res.get)
print(f"Control individual mas eficaz: {mejor}")
assert mejor == "formacion_y_doble_verificacion"
print("CLAVES " + json.dumps({"base": "%.5f" % base, "todos": "%.5f" % r_todos, "mejor": "%.5f" % res[mejor], "red": "%.1f" % (100 * (1 - r_todos / base)), "mc": "%.5f" % mc, "aut": "%.5f" % res["autenticacion_reforzada"]}))
print("Pruebas superadas.")
