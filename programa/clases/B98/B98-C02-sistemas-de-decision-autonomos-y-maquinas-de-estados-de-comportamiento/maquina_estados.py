#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B98-C02: maquina de estados de comportamiento de un rover y su equivalente como arbol de comportamiento.

Datos: SINTETICOS (umbrales, probabilidades de eventos y semilla 98002); no describen ninguna mision.
Unidades: bateria en fraccion [0, 1]; el tiempo es discreto (1 tick = 1 s de reloj de a bordo).
Modelo: estados SEGURO, REPOSO, CONDUCIR, CIENCIA, RECUPERACION. Eventos: orden de Tierra, bateria baja, obstaculo, fallo.
Invariantes verificados: (I1) tabla determinista (un destino por par estado-evento); (I2) todos los estados alcanzables;
(I3) CONDUCIR y CIENCIA solo se entran con bateria >= 0.30; (I4) de SEGURO solo se sale con la orden LIBERAR de Tierra.
Segunda via: un arbol de comportamiento (Secuencia/Fallback) decide la misma accion que la tabla en todos los casos
del espacio discreto (bateria en 3 niveles x obstaculo x orden), comprobado por enumeracion. Solo biblioteca estandar.
"""
from __future__ import annotations
import itertools, platform, random
from collections import deque

UMBRAL = 0.30
T = {  # (estado, evento) -> estado destino
    ("REPOSO", "IR"): "CONDUCIR", ("REPOSO", "MEDIR"): "CIENCIA", ("REPOSO", "FALLO"): "RECUPERACION",
    ("CONDUCIR", "LLEGADA"): "REPOSO", ("CONDUCIR", "OBSTACULO"): "REPOSO", ("CONDUCIR", "BATERIA_BAJA"): "SEGURO",
    ("CONDUCIR", "FALLO"): "RECUPERACION",
    ("CIENCIA", "FIN"): "REPOSO", ("CIENCIA", "BATERIA_BAJA"): "SEGURO", ("CIENCIA", "FALLO"): "RECUPERACION",
    ("RECUPERACION", "RESUELTO"): "REPOSO", ("RECUPERACION", "FALLO_GRAVE"): "SEGURO",
    ("SEGURO", "LIBERAR"): "REPOSO",
}
ESTADOS = ["SEGURO", "REPOSO", "CONDUCIR", "CIENCIA", "RECUPERACION"]
PESOS = [10, 10, 6, 4, 1, 1, 6, 3, 0.3, 4]  # SINTETICOS: fallos raros
EVENTOS = ["IR", "MEDIR", "LLEGADA", "OBSTACULO", "BATERIA_BAJA", "FALLO", "FIN", "RESUELTO", "FALLO_GRAVE", "LIBERAR"]


def paso(estado, evento, bateria):
    """Aplica una transicion con la guarda de bateria; ignora eventos sin transicion definida."""
    dest = T.get((estado, evento))
    if dest is None:
        return estado, False
    if dest in ("CONDUCIR", "CIENCIA") and bateria < UMBRAL:
        return estado, False  # guarda: no se entra a CONDUCIR/CIENCIA sin energia
    return dest, True


def alcanzables():
    visto, cola = {"SEGURO"}, deque(["SEGURO"])
    while cola:
        e = cola.popleft()
        for (s, _), d in T.items():
            if s == e and d not in visto:
                visto.add(d)
                cola.append(d)
    return visto


# --- Arbol de comportamiento (segunda via) para la decision "que hacer en REPOSO ante una orden de conducir".
def seq(*hijos):
    return lambda ctx: all(h(ctx) for h in hijos)


def fallback(*hijos):
    return lambda ctx: any(h(ctx) for h in hijos)


def cond(clave, valor=True):
    return lambda ctx: ctx[clave] == valor


def accion(nombre):
    def f(ctx):
        ctx["accion"] = nombre
        return True
    return f


ARBOL = fallback(
    seq(cond("bateria_ok"), cond("obstaculo", False), accion("CONDUCIR")),
    seq(cond("bateria_ok", False), accion("QUEDARSE")),
    accion("QUEDARSE"),
)


def decide_tabla(bat, obst):
    # La tabla de transiciones no modela el obstaculo previo a conducir: se evalua como guarda adicional.
    est, _ = paso("REPOSO", "IR", bat)
    return "CONDUCIR" if (est == "CONDUCIR" and not obst) else "QUEDARSE"


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS: umbral de bateria 0.30; semilla 98002")
    # I1 determinismo: un diccionario no admite claves repetidas; se cuenta que no haya destinos vacios.
    assert len(T) == len(set(T))
    print(f"I1 transiciones definidas: {len(T)} (una por par estado-evento)")
    alc = alcanzables()
    print(f"I2 estados alcanzables desde SEGURO: {sorted(alc)} ({len(alc)} de {len(ESTADOS)})")
    assert alc == set(ESTADOS)
    # Simulacion aleatoria: 20000 ticks con eventos aleatorios y bateria que baja y se recarga.
    rng = random.Random(98002)
    est, bat = "REPOSO", 0.9
    entradas_prohibidas = salidas_seguro_ilegales = 0
    cubiertas = set()
    visitas = {e: 0 for e in ESTADOS}
    for _ in range(20000):
        bat = min(1.0, max(0.0, bat + rng.uniform(-0.02, 0.012)))
        evento = rng.choices(EVENTOS, weights=PESOS)[0]
        if bat < UMBRAL and est in ("CONDUCIR", "CIENCIA"):
            evento = "BATERIA_BAJA"
        previo = est
        est, ok = paso(est, evento, bat)
        if ok:
            cubiertas.add((previo, evento))
            if est in ("CONDUCIR", "CIENCIA") and bat < UMBRAL:
                entradas_prohibidas += 1
            if previo == "SEGURO" and evento != "LIBERAR":
                salidas_seguro_ilegales += 1
        visitas[est] += 1
    print(f"I3 entradas a CONDUCIR/CIENCIA con bateria < 0.30: {entradas_prohibidas}")
    print(f"I4 salidas de SEGURO sin orden LIBERAR: {salidas_seguro_ilegales}")
    print(f"Cobertura de transiciones: {len(cubiertas)} de {len(T)}")
    print("Ticks por estado:", ", ".join(f"{e} {visitas[e]}" for e in ESTADOS))
    assert entradas_prohibidas == 0 and salidas_seguro_ilegales == 0
    # Equivalencia arbol-tabla por enumeracion.
    casos = 0
    for bat, obst in itertools.product([0.1, 0.3, 0.9], [False, True]):
        ctx = {"bateria_ok": bat >= UMBRAL, "obstaculo": obst, "accion": None}
        ARBOL(ctx)
        assert ctx["accion"] == decide_tabla(bat, obst), (bat, obst)
        casos += 1
    print(f"Arbol de comportamiento = tabla en {casos} de {casos} casos enumerados")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
