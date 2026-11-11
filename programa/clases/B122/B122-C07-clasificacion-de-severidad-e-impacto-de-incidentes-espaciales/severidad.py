#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B122-C07: clasificacion de severidad de incidentes SINTETICOS con una escala ponderada ILUSTRATIVA.

CONTENIDO EDUCATIVO Y DEFENSIVO: no es asesoria legal, regulatoria ni de seguridad. La escala es de este curso (no es una escala oficial
ni de ningun organismo); datos SINTETICOS. Marco conceptual (solo ficha y resumen consultados el 2026-11-11): NIST SP 800-61 Rev. 3 (2025).
Puntaje S = suma(w_k x puntaje_k) con criterios 0..4: servicio, alcance, datos, seguridad de las personas y reputacion; pesos suman 1.
Niveles (ilustrativos): S < 1 -> N0 Informativo; < 2 -> N1 Bajo; < 3 -> N2 Medio; >= 3 -> N3 Alto; ademas una regla de escalada:
si seguridad de las personas = 4, el nivel es N3 siempre. Unidades: puntajes adimensionales. Sistema de referencia: ninguno.
Tolerancias: pesos suman 1 (1e-12); estabilidad: Monte Carlo con pesos perturbados +-20 % (50000, semilla 122), fraccion informada.
"""
from __future__ import annotations
import platform, random

PESOS = {"servicio": 0.35, "alcance": 0.25, "datos": 0.15, "personas": 0.15, "reputacion": 0.10}
INCIDENTES = {  # id -> (servicio, alcance, datos, personas, reputacion) 0..4 ; sinteticos
    "I-01": (4, 3, 1, 0, 2), "I-02": (1, 1, 0, 0, 0), "I-03": (2, 2, 4, 0, 3), "I-04": (3, 2, 0, 4, 1),
    "I-05": (0, 1, 1, 0, 0), "I-06": (2, 1, 1, 0, 1), "I-07": (4, 4, 3, 1, 4), "I-08": (3, 3, 2, 0, 2),
}
EDAD_H = {"I-01": 2, "I-02": 30, "I-03": 5, "I-04": 1, "I-05": 48, "I-06": 10, "I-07": 3, "I-08": 8}


def puntaje(v, pesos=PESOS):
    return sum(w * x for w, x in zip(pesos.values(), v))


def nivel(v, s):
    if v[3] == 4:
        return 3
    return 0 if s < 1 else 1 if s < 2 else 2 if s < 3 else 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS: incidentes y puntajes inventados; la escala es ilustrativa, no oficial.")
    assert abs(sum(PESOS.values()) - 1) < 1e-12
    filas = []
    for k, v in INCIDENTES.items():
        s = puntaje(v)
        filas.append((k, s, nivel(v, s)))
    print(" id     S    nivel  edad[h]")
    for k, s, n in filas:
        print(f" {k}  {s:5.2f}  N{n}   {EDAD_H[k]:4d}")
    cola = sorted(filas, key=lambda f: (-f[2], -f[1], -EDAD_H[f[0]]))
    print("Cola de atencion (nivel, puntaje, antiguedad):", [f[0] for f in cola])
    # I-04: S bajo pero personas=4 -> escalada
    s4 = puntaje(INCIDENTES["I-04"])
    print(f"I-04: puntaje {s4:.2f} (N2 por puntaje) pero se escala a N3 por la regla de seguridad de las personas")
    assert s4 < 3 and nivel(INCIDENTES["I-04"], s4) == 3
    # monotonia: subir un criterio nunca baja el puntaje
    base = list(INCIDENTES["I-06"])
    for i in range(5):
        v2 = base.copy(); v2[i] = min(4, v2[i] + 1)
        assert puntaje(v2) >= puntaje(base)
    # estabilidad frente a pesos
    rng = random.Random(122)
    est = {k: 0 for k in INCIDENTES}
    n = 50000
    base_nivel = {k: nivel(v, puntaje(v)) for k, v in INCIDENTES.items()}
    for _ in range(n):
        w = [x * (1 + rng.uniform(-0.2, 0.2)) for x in PESOS.values()]
        tot = sum(w)
        pw = dict(zip(PESOS, [x / tot for x in w]))
        for k, v in INCIDENTES.items():
            if nivel(v, puntaje(v, pw)) == base_nivel[k]:
                est[k] += 1
    print("Fraccion de simulaciones con el mismo nivel al perturbar los pesos +-20 %:")
    for k in INCIDENTES:
        print(f"  {k}: {est[k] / n:.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
