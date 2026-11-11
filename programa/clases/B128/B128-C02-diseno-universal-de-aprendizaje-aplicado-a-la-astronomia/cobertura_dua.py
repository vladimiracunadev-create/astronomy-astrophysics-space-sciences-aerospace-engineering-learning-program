#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C02: cobertura de las pautas DUA 3.0 en un plan de clase SINTETICO.

Consultado (2026-11-11): CAST, UDL Guidelines 3.0 (2024): tres principios y nueve pautas (nombres abajo).
SINTETICO (inventado): el plan de clase «Las fases de la Luna» (8 actividades) y su etiquetado con pautas.
Que una actividad «cubra» una pauta es un juicio del autor del plan, no una medicion: el script solo cuenta.
Unidades: numero de actividades, minutos. Sin sistema de referencia astronomico.
Segunda via: cobertura por union de conjuntos frente a cobertura por matriz de incidencia (deben coincidir).
Tolerancia: igualdad exacta (enteros).
"""
from __future__ import annotations
import platform

PRINCIPIOS = {
    "Implicacion": {7: "Dar la bienvenida a intereses e identidades", 8: "Sostener el esfuerzo y la persistencia", 9: "Capacidad emocional"},
    "Representacion": {1: "Percepcion", 2: "Lenguaje y simbolos", 3: "Construccion de conocimiento"},
    "Accion y expresion": {4: "Interaccion", 5: "Expresion y comunicacion", 6: "Desarrollo de estrategias"},
}
# (actividad, minutos, pautas que declara cubrir) - SINTETICO
PLAN = [
    ("Pregunta de entrada: que Luna vieron anoche", 10, {7}),
    ("Lectura breve con glosario y dibujo descrito", 15, {1, 2}),
    ("Modelo con pelota y lampara (vista y tacto)", 20, {1, 3, 4}),
    ("Tabla de fases con porcentaje iluminado", 10, {2, 3}),
    ("Eleccion de formato de entrega (dibujo, audio o texto)", 15, {5}),
    ("Lista de pasos para planificar la observacion", 10, {6}),
    ("Cierre: que me costo y que me ayudo", 10, set()),
]
ESPERADAS = {7, 8, 9, 1, 2, 3, 4, 5, 6}


def cobertura_union(plan):
    s = set()
    for _, _, p in plan:
        s |= p
    return s


def cobertura_matriz(plan):
    return {g for g in ESPERADAS if sum(1 for _, _, p in plan if g in p) > 0}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Plan SINTETICO; pautas segun CAST UDL 3.0 (consultado 2026-11-11). Cubrir = juicio del autor, no medicion.")
    u, m = cobertura_union(PLAN), cobertura_matriz(PLAN)
    assert u == m, (u, m)
    print(f"Minutos totales: {sum(t for _, t, _ in PLAN)}")
    indice = {}
    for pr, pautas in PRINCIPIOS.items():
        cub = [g for g in pautas if g in u]
        indice[pr] = len(cub) / len(pautas)
        print(f"{pr:20s}: {len(cub)} de {len(pautas)} pautas ({indice[pr]*100:5.1f} %)  sin cubrir: {[g for g in pautas if g not in u]}")
    total = len(u & ESPERADAS)
    print(f"Cobertura total: {total} de {len(ESPERADAS)} pautas ({total/len(ESPERADAS)*100:.1f} %)")
    print("Minutos por pauta:")
    for g in sorted(ESPERADAS):
        mins = sum(t for _, t, p in PLAN if g in p)
        print(f"  pauta {g}: {mins:3d} min")
    peor = min(indice, key=indice.get)
    print(f"Principio con menor cobertura: {peor}")
    # actividad sin ninguna pauta: candidata a revisar
    print("Actividades sin pauta declarada:", [a for a, _, p in PLAN if not p])
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
