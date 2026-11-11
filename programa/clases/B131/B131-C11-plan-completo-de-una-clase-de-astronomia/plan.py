#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C11: validacion de coherencia de un plan de clase de 90 minutos sobre las fases de la Luna.

CONTENIDO EDUCATIVO. Sin datos consultados para la validacion: el plan, las reglas y los tiempos son ILUSTRATIVOS (propuesta del curso).
Estandar NO consultado: mes sinodico 29.530589 d; fraccion iluminada k = (1 + cos i)/2 con i el angulo de fase (Sol-Luna-Tierra),
verificada aqui por simetria k(i) + k(180 - i) = 1 y por un conteo independiente de puntos del disco (semilla 131).
Reglas de coherencia (ilustrativas): (1) los tiempos suman 90 min; (2) cada resultado de aprendizaje tiene al menos una actividad y un item de
evaluacion; (3) la evaluacion formativa ocupa al menos 10 % del tiempo; (4) ningun bloque de exposicion pasa de 15 min seguidos;
(5) toda actividad que mencione el Sol o la luz solar lleva la precaucion 'filtro certificado o proyeccion indirecta supervisada'
o declara 'sin observacion del Sol'.
Tolerancias: simetria de k a 1e-12; conteo de puntos del disco dentro de 3e-3.
"""
from __future__ import annotations
import math, platform, random

PLAN = {
    "resultados": {
        "R1": "Explicar con un diagrama por que se ve una fase lunar segun el angulo Sol-Luna-Tierra",
        "R2": "Calcular la fraccion iluminada de la Luna para un angulo de fase dado",
        "R3": "Justificar por que la sombra de la Tierra no causa las fases",
    },
    "bloques": [
        {"id": "B1", "min": 10, "tipo": "diagnostico", "texto": "Pregunta inicial con distractores sobre la causa de las fases", "res": ["R3"], "item": True, "seguridad": "sin observacion del Sol"},
        {"id": "B2", "min": 12, "tipo": "exposicion", "texto": "Geometria Sol-Tierra-Luna con modelo de linterna y esfera", "res": ["R1"], "item": False, "seguridad": "sin observacion del Sol"},
        {"id": "B3", "min": 25, "tipo": "actividad", "texto": "Parejas ordenan fases con la maqueta y dibujan el angulo de fase", "res": ["R1"], "item": True, "seguridad": "sin observacion del Sol"},
        {"id": "B4", "min": 10, "tipo": "exposicion", "texto": "Formula k = (1 + cos i)/2 y tabla de valores", "res": ["R2"], "item": False, "seguridad": "sin observacion del Sol"},
        {"id": "B5", "min": 18, "tipo": "actividad", "texto": "Problemas de calculo de k en cinco angulos con verificacion por simetria", "res": ["R2"], "item": True, "seguridad": "sin observacion del Sol"},
        {"id": "B6", "min": 10, "tipo": "evaluacion", "texto": "Ticket de salida: dibuja la fase para i = 90 y explica por que no es una sombra", "res": ["R1", "R3"], "item": True, "seguridad": "sin observacion del Sol"},
        {"id": "B7", "min": 5, "tipo": "cierre", "texto": "Sintesis y tarea: bitacora de la Luna", "res": [], "item": False, "seguridad": "sin observacion del Sol"},
    ],
}

PLAN_DEFECTUOSO = {
    "resultados": {"R1": "Explicar las fases", "R2": "Calcular k", "R3": "Comprender la sombra"},
    "bloques": [
        {"id": "X1", "min": 20, "tipo": "exposicion", "texto": "Clase magistral sobre las fases", "res": ["R1"], "item": False, "seguridad": ""},
        {"id": "X2", "min": 30, "tipo": "actividad", "texto": "Observar el Sol con binoculares para ver su disco", "res": ["R1"], "item": False, "seguridad": ""},
        {"id": "X3", "min": 20, "tipo": "actividad", "texto": "Calculos de k", "res": ["R2"], "item": True, "seguridad": "sin observacion del Sol"},
        {"id": "X4", "min": 25, "tipo": "evaluacion", "texto": "Examen final", "res": ["R2"], "item": True, "seguridad": "sin observacion del Sol"},
    ],
}


def validar(plan, total=90):
    fallos = []
    bl = plan["bloques"]
    s = sum(b["min"] for b in bl)
    if s != total:
        fallos.append(f"(1) tiempos suman {s} min, no {total}")
    for r in plan["resultados"]:
        if not any(r in b["res"] and b["tipo"] in ("actividad", "diagnostico", "exposicion") for b in bl):
            fallos.append(f"(2) {r} sin actividad")
        if not any(r in b["res"] and b["item"] for b in bl):
            fallos.append(f"(2) {r} sin item de evaluacion")
    form = sum(b["min"] for b in bl if b["tipo"] in ("diagnostico", "evaluacion"))
    if form < 0.10 * total:
        fallos.append(f"(3) evaluacion formativa {form} min < 10 %")
    run = 0
    for b in bl:
        run = run + b["min"] if b["tipo"] == "exposicion" else 0
        if run > 15:
            fallos.append(f"(4) exposicion de {run} min seguidos en {b['id']}")
    for b in bl:
        t = b["texto"].lower()
        if ("sol " in t + " " or "solar" in t) and "sin observacion del sol" not in b["seguridad"] and "filtro certificado" not in b["seguridad"]:
            fallos.append(f"(5) {b['id']} menciona el Sol sin precaucion de seguridad")
    return fallos


def tabla_fases():
    print("Fases (modelo circular uniforme, ILUSTRATIVO): dia, angulo de fase i, fraccion iluminada k")
    nombres = ["nueva", "creciente", "cuarto creciente", "gibosa creciente", "llena", "gibosa menguante", "cuarto menguante", "menguante"]
    peor = 0.0
    for n, nom in enumerate(nombres):
        dia = n * 29.530589 / 8
        i = 180 - 360 * dia / 29.530589
        k = (1 + math.cos(math.radians(i))) / 2
        peor = max(peor, abs(k + (1 + math.cos(math.radians(180 - i))) / 2 - 1))
        print(f"  {nom:18s} dia {dia:5.2f}   i = {i % 360:6.1f}   k = {k:.3f}")
    return peor


def conteo_disco(i_deg, n=200000, seed=131):
    rng = random.Random(seed)
    i = math.radians(i_deg)
    s = (math.sin(i), math.cos(i))
    tot = lit = 0
    while tot < n:
        x, y = rng.uniform(-1, 1), rng.uniform(-1, 1)
        if x * x + y * y > 1:
            continue
        tot += 1
        if x * s[0] + math.sqrt(1 - x * x - y * y) * s[1] > 0:
            lit += 1
    return lit / tot


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Plan, reglas y tiempos ILUSTRATIVOS; mes sinodico y formula de k estandar NO consultados; ningun dato de estudiantes reales.")
    peor = tabla_fases()
    k90 = conteo_disco(90.0)
    print(f"Simetria k(i) + k(180 - i) - 1: maximo {peor:.1e} ; conteo independiente del disco a i = 90: {k90:.4f} (esperado 0.5000)")
    for nombre, plan in (("Plan propuesto", PLAN), ("Plan defectuoso", PLAN_DEFECTUOSO)):
        fallos = validar(plan)
        tot = sum(b["min"] for b in plan["bloques"])
        print(f"\n{nombre}: {len(plan['bloques'])} bloques, {tot} min, {len(plan['resultados'])} resultados")
        form = sum(b["min"] for b in plan["bloques"] if b["tipo"] in ("diagnostico", "evaluacion"))
        print(f"  evaluacion formativa (diagnostico + evaluacion): {form} min = {100 * form / tot:.0f} %")
        print(f"  fallos: {len(fallos)}")
        for f in fallos:
            print("   - " + f)
    assert not validar(PLAN)
    assert len(validar(PLAN_DEFECTUOSO)) >= 5
    assert peor < 1e-12 and abs(k90 - 0.5) < 3e-3
    print("\nPruebas superadas.")


if __name__ == "__main__":
    main()
