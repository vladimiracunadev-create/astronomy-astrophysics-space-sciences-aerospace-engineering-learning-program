#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B98-C01: seleccion de objetivos a bordo con presupuesto de energia y ventanas de tiempo.

Datos: TODOS SINTETICOS (ilustrativos, no medidos; no describen ninguna mision). Unidades: utilidad adimensional,
energia en Wh, tiempos en minutos desde el inicio de la jornada (t = 0). Sistema de referencia temporal: reloj de a bordo.
Modelo: cada objetivo tiene utilidad, energia, duracion y ventana [inicio, fin]. Un plan es factible si, ejecutado en
algun orden y sin solaparse, cada objetivo empieza no antes de su inicio de ventana y termina antes del fin, y la
energia total no supera el presupuesto. Se compara un planificador voraz (utilidad/energia) con la busqueda exhaustiva
(optimo, 2^8 subconjuntos x permutaciones). Replanificacion: un fallo de bateria quita energia a mitad de jornada.
Tolerancia: factibilidad exacta (enteros); voraz <= optimo; plan replanificado factible. Python 3, solo biblioteca estandar.
"""
from __future__ import annotations
import itertools, platform

# id, utilidad, energia [Wh], duracion [min], inicio de ventana, fin de ventana  (SINTETICOS)
OBJ = [
    ("G1 imagen panoramica", 10, 18, 20, 0, 90),
    ("G2 espectro A", 14, 30, 35, 10, 120),
    ("G3 espectro B", 12, 26, 30, 40, 160),
    ("G4 perforacion superficial", 20, 55, 60, 30, 200),
    ("G5 calibracion", 6, 8, 10, 0, 240),
    ("G6 desplazamiento a sitio 2", 8, 22, 40, 60, 180),
    ("G7 meteorologia", 5, 10, 25, 100, 240),
    ("G8 imagen alta resolucion", 11, 20, 25, 120, 240),
]
ENERGIA = 150.0   # Wh (sintetico)
T_FALLO = 100.0   # min
PERDIDA = 35.0    # Wh perdidos por el fallo de bateria (sintetico)


def horario(orden, t0):
    """Devuelve la lista (objetivo, inicio, fin) si el orden cumple las ventanas; si no, None."""
    t, res = t0, []
    for o in orden:
        ini = max(t, o[4])
        fin = ini + o[3]
        if fin > o[5]:
            return None
        res.append((o, ini, fin))
        t = fin
    return res


def mejor_orden(subconjunto, t0):
    for perm in itertools.permutations(subconjunto):
        h = horario(perm, t0)
        if h is not None:
            return h
    return None


def optimo(objs, t0, energia):
    mejor = (0.0, [])
    for k in range(len(objs) + 1):
        for sub in itertools.combinations(objs, k):
            if sum(o[2] for o in sub) > energia:
                continue
            u = sum(o[1] for o in sub)
            if u <= mejor[0]:
                continue
            h = mejor_orden(sub, t0)
            if h is not None:
                mejor = (u, h)
    return mejor


def voraz(objs, t0, energia):
    elegidos, usada = [], 0.0
    for o in sorted(objs, key=lambda o: o[1] / o[2], reverse=True):
        if usada + o[2] > energia:
            continue
        h = mejor_orden(elegidos + [o], t0)
        if h is not None:
            elegidos.append(o)
            usada += o[2]
    h = mejor_orden(elegidos, t0) or []
    return (sum(o[1] for o in elegidos), h)


def mostrar(titulo, plan):
    u, h = plan
    e = sum(o[2] for o, _, _ in h)
    print(f"{titulo}: utilidad {u:.0f}, energia {e:.0f} Wh, objetivos {len(h)}")
    for o, a, b in h:
        print(f"   {o[0]:28s} {a:6.1f} -> {b:6.1f} min  ({o[2]} Wh)")
    return e


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"DATOS SINTETICOS: {len(OBJ)} objetivos, presupuesto {ENERGIA:.0f} Wh, jornada 240 min")
    pv = voraz(OBJ, 0.0, ENERGIA)
    po = optimo(OBJ, 0.0, ENERGIA)
    ev = mostrar("Plan voraz", pv)
    eo = mostrar("Plan optimo", po)
    print(f"Razon voraz/optimo = {pv[0] / po[0]:.3f}")
    # Ejecucion hasta T_FALLO: se conservan los objetivos terminados; el resto se replanifica.
    hechos = [(o, a, b) for o, a, b in po[1] if b <= T_FALLO]
    ids_hechos = {o[0] for o, _, _ in hechos}
    gastada = sum(o[2] for o, _, _ in hechos)
    restante = ENERGIA - gastada - PERDIDA
    pendientes = [o for o in OBJ if o[0] not in ids_hechos]
    print(f"Fallo de bateria en t = {T_FALLO:.0f} min: terminados {len(hechos)} objetivos ({gastada:.0f} Wh); "
          f"energia restante tras perder {PERDIDA:.0f} Wh = {restante:.0f} Wh")
    pr = optimo(pendientes, T_FALLO, restante)
    er = mostrar("Plan de contingencia (replanificado)", pr)
    u_total = sum(o[1] for o, _, _ in hechos) + pr[0]
    print(f"Utilidad total con fallo = {u_total:.0f} (sin fallo, optimo = {po[0]:.0f})")
    assert ev <= ENERGIA and eo <= ENERGIA
    assert pv[0] <= po[0]
    for plan in (pv, po):
        assert horario([o for o, _, _ in plan[1]], 0.0) is not None
    assert er <= restante + 1e-9
    assert all(a >= T_FALLO - 1e-9 for _, a, _ in pr[1])
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
