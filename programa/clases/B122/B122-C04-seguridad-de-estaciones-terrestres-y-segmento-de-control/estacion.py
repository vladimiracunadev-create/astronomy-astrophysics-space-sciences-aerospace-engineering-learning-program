#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B122-C04: defensa por capas de una estacion terrestre SINTETICA (condicion detectar-antes-que-retardo).

CONTENIDO EDUCATIVO Y DEFENSIVO: no es asesoria legal, regulatoria ni de seguridad; no describe como vulnerar una estacion.
Datos SINTETICOS (inventados). Marco conceptual (solo ficha y resumen consultados el 2026-11-11): NIST IR 8401 (2022).
Modelo: las capas se cruzan en orden; cada capa i tiene eficacia e_i (prob. de detener) y retardo d_i [min]; la deteccion ocurre en
la capa de sensor con tiempo t_det [min] desde el inicio del evento. Hay respuesta efectiva si t_det + t_resp <= suma de retardos
restantes tras la deteccion. Prob. de que una accion indebida cruce todas las capas: P = prod(1 - e_i) (capas independientes: supuesto).
Unidades: minutos, probabilidades. Sistema de referencia: tiempo desde el inicio del evento. Tolerancias: Monte Carlo (200000, semilla 122) vs
producto < 0.002; aritmetica de retardos exacta.
"""
from __future__ import annotations
import platform, random

CAPAS = [  # (nombre, tipo, eficacia, retardo_min)
    ("Perimetro y control de acceso", "fisica", 0.60, 3.0),
    ("Sala de control con registro de entradas", "fisica", 0.50, 2.0),
    ("Segmentacion de red de operaciones", "logica", 0.70, 4.0),
    ("Autenticacion fuerte en el segmento de control", "logica", 0.80, 5.0),
    ("Autorizacion de telecomandos (doble confirmacion)", "logica", 0.90, 6.0),
]
T_DET = {"sin sensores": None, "alarma en capa 2": 3.0, "alarma en capa 4": 9.0}  # min desde el inicio (ilustrativo)
T_RESP = 5.0  # min de respuesta humana (ilustrativo)


def p_cruce():
    p = 1.0
    for _, _, e, _ in CAPAS:
        p *= 1 - e
    return p


def retardo_restante(t_det):
    """Retardo acumulado desde t_det hasta cruzar todas las capas."""
    acum, restante = 0.0, 0.0
    for _, _, _, d in CAPAS:
        fin = acum + d
        if fin > t_det:
            restante += fin - max(acum, t_det)
        acum = fin
    return restante


def mc_cruce(n, seed):
    rng = random.Random(seed)
    ok = 0
    for _ in range(n):
        if all(rng.random() >= e for _, _, e, _ in CAPAS):
            ok += 1
    return ok / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS: capas, eficacias y tiempos son inventados; no describen ninguna estacion real.")
    for nom, tipo, e, d in CAPAS:
        print(f"  capa {tipo:6s} e={e:.2f} retardo={d:3.1f} min : {nom}")
    pc = p_cruce()
    mc = mc_cruce(200000, 122)
    print(f"Prob. de cruzar todas las capas: producto = {pc:.5f} ; Monte Carlo = {mc:.5f} ; dif = {abs(pc - mc):.5f}")
    assert abs(pc - mc) < 0.002
    total = sum(d for *_, d in CAPAS)
    print(f"Retardo total = {total} min ; tiempo de respuesta = {T_RESP} min")
    for k, t in T_DET.items():
        if t is None:
            print(f"  {k}: no hay deteccion -> respuesta efectiva: False")
            continue
        rest = retardo_restante(t)
        print(f"  {k}: t_det = {t} min ; retardo restante = {rest:.1f} min ; respuesta efectiva (t_resp <= restante): {T_RESP <= rest}")
    assert retardo_restante(0.0) == total
    # sin una capa logica
    sin = 1.0
    for i, (_, _, e, _) in enumerate(CAPAS):
        if i != 3:
            sin *= 1 - e
    print(f"Sin la autenticacion fuerte (capa 4): prob. de cruce = {sin:.5f} ({sin / pc:.1f} veces mayor)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
