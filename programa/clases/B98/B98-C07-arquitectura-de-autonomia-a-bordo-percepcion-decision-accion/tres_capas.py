#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B98-C07: presupuesto de tiempos de una arquitectura de tres capas (reactiva, ejecutiva, deliberativa).

Datos: TODOS SINTETICOS (no medidos; no describen ninguna mision; semilla 98007). Unidades: segundos de reloj de a bordo.
Conjunto de tareas periodicas con prioridad por tasa (menor periodo = mayor prioridad): (C = tiempo de calculo en el peor caso,
T = periodo = plazo): percepcion C=0.020 T=0.100; reflejo (capa reactiva) C=0.010 T=0.100; ejecutivo C=0.150 T=1.000;
telemetria C=0.100 T=2.000. La capa deliberativa (planificador) corre en segundo plano con tiempo de calculo
lognormal (mediana 45 s, sigma log 0.5) y debe terminar antes de 120 s para que el plan llegue a tiempo.
Comprobaciones: (1) utilizacion U = sum C/T frente a la cota de Liu-Layland n(2^(1/n)-1) (condicion suficiente);
(2) analisis exacto del tiempo de respuesta R_i = C_i + sum_{j de mayor prioridad} ceil(R_i/T_j) C_j (iteracion de punto fijo);
(3) latencia peor caso percepcion -> orden de reflejo, acotada por R_percepcion + R_reflejo, frente al presupuesto de 0.5 s; (4) Monte Carlo del planificador: fraccion de planes que superan los 120 s.
Solo biblioteca estandar.
"""
from __future__ import annotations
import math, platform, random

TAREAS = [  # nombre, C, T
    ("percepcion", 0.020, 0.100),
    ("reflejo", 0.010, 0.100),
    ("ejecutivo", 0.150, 1.000),
    ("telemetria", 0.100, 2.000),
]
PRESUPUESTO_REFLEJO = 0.5  # s, SINTETICO
PLAZO_PLAN = 120.0


def prioridad(tareas):
    return sorted(tareas, key=lambda t: t[2])


def tiempo_respuesta(i, tareas):
    _, c, t = tareas[i]
    r = c
    for _ in range(1000):
        nuevo = c + sum(math.ceil(r / tj) * cj for _, cj, tj in tareas[:i])
        if abs(nuevo - r) < 1e-12:
            return nuevo
        if nuevo > t:
            return nuevo
        r = nuevo
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS; semilla 98007")
    ts = prioridad(TAREAS)
    u = sum(c / t for _, c, t in ts)
    cota = len(ts) * (2 ** (1 / len(ts)) - 1)
    print(f"Utilizacion U = {u:.4f}; cota de Liu-Layland para n = {len(ts)}: {cota:.4f} ({'cumple' if u <= cota else 'no basta'})")
    print(f"{'tarea':12s} {'C [s]':>7s} {'T [s]':>7s} {'R [s]':>8s} {'holgura [s]':>12s}")
    resp = {}
    for i, (n, c, t) in enumerate(ts):
        r = tiempo_respuesta(i, ts)
        resp[n] = r
        print(f"{n:12s} {c:7.3f} {t:7.3f} {r:8.3f} {t - r:12.3f}")
        assert r <= t
    lat = resp["percepcion"] + resp["reflejo"]
    print(f"Latencia peor caso percepcion -> reflejo (R_p + R_r, acotada por las dos respuestas): {lat:.3f} s (presupuesto {PRESUPUESTO_REFLEJO} s)")
    print(f"Latencia peor caso hasta el ejecutivo, incluyendo el periodo de muestreo: {resp['percepcion'] + 1.0 + resp['ejecutivo']:.3f} s")
    assert lat <= PRESUPUESTO_REFLEJO
    assert u <= cota
    rng = random.Random(98007)
    n, mu, sg = 20000, math.log(45.0), 0.5
    tarde = sum(1 for _ in range(n) if rng.lognormvariate(mu, sg) > PLAZO_PLAN)
    p_exacta = 0.5 * math.erfc((math.log(PLAZO_PLAN) - mu) / (sg * math.sqrt(2)))
    print(f"Planificador: P(tiempo > {PLAZO_PLAN:.0f} s) Monte Carlo = {tarde / n:.4f}; formula lognormal = {p_exacta:.4f}")
    assert abs(tarde / n - p_exacta) < 0.005
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
