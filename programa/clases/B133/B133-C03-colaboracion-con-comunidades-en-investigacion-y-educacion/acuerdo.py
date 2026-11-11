#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B133-C03: verificar un acuerdo de colaboracion SINTETICO con una comunidad FICTICIA.

Todo es SINTETICO: las tres comunidades, los acuerdos, las fechas y las duraciones estan inventados; ninguno representa a
un pueblo real. El script NO decide si una colaboracion es respetuosa: comprueba que un documento tenga los elementos que
las fuentes consultadas senalan y que las etapas respeten su orden. Una lista completa no sustituye a la comunidad.
Reglas (cada una con su fuente, ver la clase): consentimiento libre, previo, informado y revocable (Declaracion de la ONU,
art. 32.2 por analogia; marco de Lee et al. 2020); los cuatro ejes CARE (Carroll et al. 2020, solo resumen); portadores del
saber reconocidos y credito acordado; devolucion de resultados; relacion de varios años (Neilson et al. 2019: visitas
unicas no construyen confianza); orden de etapas: consulta < acuerdo < recoleccion < revision comunitaria < publicacion.
Segunda via: el orden de etapas se comprueba con dos algoritmos (Kahn y recorrido en profundidad) sobre el mismo grafo.
Tolerancias: exactitud entera; los hallazgos esperados de cada acuerdo se fijan de antemano (defectos plantados).
"""
from __future__ import annotations
import platform

PRECEDENCIA = [("consulta", "acuerdo"), ("acuerdo", "recoleccion"), ("recoleccion", "revision_comunitaria"),
               ("revision_comunitaria", "publicacion"), ("revision_comunitaria", "devolucion")]

CARE = ("beneficio_colectivo", "autoridad_control", "responsabilidad", "etica")

ACUERDOS = {
    "A (completo)": {
        "consentimiento": {"libre": True, "previo": True, "informado": True, "revocable": True},
        "care": {k: "descrito" for k in CARE},
        "autoria": {"portadores_reconocidos": True, "credito_acordado": True},
        "devolucion": {"resultados_a_comunidad": True, "en_idioma_de_la_comunidad": True},
        "duracion_anios": 3.0,
        "etapas": {"consulta": 0, "acuerdo": 60, "recoleccion": 120, "revision_comunitaria": 400,
                   "publicacion": 500, "devolucion": 450},
    },
    "B (extractivo)": {
        "consentimiento": {"libre": True, "previo": False, "informado": False, "revocable": False},
        "care": {"beneficio_colectivo": None, "autoridad_control": None, "responsabilidad": "descrito", "etica": None},
        "autoria": {"portadores_reconocidos": False, "credito_acordado": False},
        "devolucion": {"resultados_a_comunidad": False, "en_idioma_de_la_comunidad": False},
        "duracion_anios": 0.1,
        "etapas": {"consulta": 0, "acuerdo": 5, "recoleccion": 10, "revision_comunitaria": 30,
                   "publicacion": 40, "devolucion": 35},
    },
    "C (orden roto)": {
        "consentimiento": {"libre": True, "previo": True, "informado": True, "revocable": True},
        "care": {k: "descrito" for k in CARE},
        "autoria": {"portadores_reconocidos": True, "credito_acordado": True},
        "devolucion": {"resultados_a_comunidad": True, "en_idioma_de_la_comunidad": True},
        "duracion_anios": 2.0,
        "etapas": {"consulta": 0, "acuerdo": 60, "recoleccion": 30, "revision_comunitaria": 400,
                   "publicacion": 380, "devolucion": 450},
    },
}

ESPERADO = {
    "A (completo)": set(),
    "B (extractivo)": {"CRIT-previo", "CRIT-informado", "CRIT-revocable", "CRIT-CARE-beneficio_colectivo",
                       "CRIT-CARE-autoridad_control", "CRIT-CARE-etica", "IMP-portadores", "IMP-credito",
                       "IMP-devolucion", "IMP-idioma", "AVISO-duracion"},
    "C (orden roto)": {"CRIT-orden-acuerdo-recoleccion", "CRIT-orden-revision_comunitaria-publicacion"},
}


def hallazgos(a: dict) -> set[str]:
    h: set[str] = set()
    for k in ("libre", "previo", "informado", "revocable"):
        if not a["consentimiento"][k]:
            h.add(f"CRIT-{k}")
    for k in CARE:
        if not a["care"].get(k):
            h.add(f"CRIT-CARE-{k}")
    if not a["autoria"]["portadores_reconocidos"]:
        h.add("IMP-portadores")
    if not a["autoria"]["credito_acordado"]:
        h.add("IMP-credito")
    if not a["devolucion"]["resultados_a_comunidad"]:
        h.add("IMP-devolucion")
    if not a["devolucion"]["en_idioma_de_la_comunidad"]:
        h.add("IMP-idioma")
    if a["duracion_anios"] < 1.0:
        h.add("AVISO-duracion")
    for u, v in PRECEDENCIA:
        if a["etapas"][u] >= a["etapas"][v]:
            h.add(f"CRIT-orden-{u}-{v}")
    return h


def kahn(nodos: list[str], aristas: list[tuple[str, str]]) -> bool:
    ent = {n: 0 for n in nodos}
    for _, v in aristas:
        ent[v] += 1
    cola = [n for n in nodos if ent[n] == 0]
    vistos = 0
    while cola:
        n = cola.pop()
        vistos += 1
        for u, v in aristas:
            if u == n:
                ent[v] -= 1
                if ent[v] == 0:
                    cola.append(v)
    return vistos == len(nodos)


def dfs_aciclico(nodos: list[str], aristas: list[tuple[str, str]]) -> bool:
    color = {n: 0 for n in nodos}

    def visita(n: str) -> bool:
        color[n] = 1
        for u, v in aristas:
            if u == n:
                if color[v] == 1 or (color[v] == 0 and not visita(v)):
                    return False
        color[n] = 2
        return True
    return all(color[n] != 0 or visita(n) for n in nodos)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Comunidades y acuerdos SINTETICOS (ficticios); la lista no decide si una colaboracion es respetuosa.")
    nodos = sorted({x for e in PRECEDENCIA for x in e})
    k, d = kahn(nodos, PRECEDENCIA), dfs_aciclico(nodos, PRECEDENCIA)
    print(f"Grafo de precedencia sin ciclos: Kahn = {k}, profundidad = {d}")
    assert k and d
    for nombre, a in ACUERDOS.items():
        h = hallazgos(a)
        crit = sorted(x for x in h if x.startswith("CRIT"))
        otros = sorted(x for x in h if not x.startswith("CRIT"))
        veredicto = "puede iniciar" if not crit else "NO puede iniciar"
        print(f"\nAcuerdo {nombre}: criticos = {len(crit)}, importantes/avisos = {len(otros)} -> {veredicto}")
        for x in crit + otros:
            print(f"   {x}")
        assert h == ESPERADO[nombre], (nombre, h ^ ESPERADO[nombre])
    # Una prueba negativa: un grafo con ciclo debe detectarse por las dos vias
    ciclo = PRECEDENCIA + [("publicacion", "consulta")]
    print(f"\nGrafo con ciclo agregado: Kahn = {kahn(nodos, ciclo)}, profundidad = {dfs_aciclico(nodos, ciclo)}")
    assert not kahn(nodos, ciclo) and not dfs_aciclico(nodos, ciclo)
    print("Hallazgos obtenidos = hallazgos plantados en los 3 acuerdos (la comprobacion es circular por diseño).")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
