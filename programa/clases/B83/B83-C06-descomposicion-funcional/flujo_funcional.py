#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C06: descomposicion funcional, asignacion a subsistemas y ruta critica del flujo funcional.

Datos: SINTETICOS (once funciones de la secuencia «tomar y entregar una imagen» de la mision de ejemplo ESTRELLA-S, con
duraciones en segundos y asignacion a subsistemas inventadas). Modelo: grafo aciclico de dependencias; ruta critica = camino
mas largo. Metodo 1: programacion dinamica en orden topologico (con holguras). Segunda via: enumeracion de todos los caminos
por busqueda en profundidad. Tolerancia: ambas duraciones criticas iguales. Sin constantes fisicas.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

# id: (nombre, duracion s, subsistema, predecesoras)
F = {
    "F1": ("Recibir comando de toma", 2, "C&DH", []),
    "F2": ("Apuntar la plataforma", 120, "ADCS", []),
    "F3": ("Estabilizar", 30, "ADCS", ["F2"]),
    "F4": ("Calentar el detector", 60, "Carga util", ["F1"]),
    "F5": ("Capturar la imagen", 10, "Carga util", ["F3", "F4"]),
    "F6": ("Comprimir", 45, "C&DH", ["F5"]),
    "F7": ("Almacenar", 20, "C&DH", ["F6"]),
    "F8": ("Bajar los datos", 400, "Comunicaciones", ["F7"]),
    "F9": ("Verificar integridad en tierra", 30, "Segmento terreno", ["F8"]),
    "F10": ("Generar y distribuir potencia", 0, "EPS", []),
    "F11": ("Controlar la temperatura", 0, "Termico", []),
}
GRUPOS = {"Adquirir imagen": ["F1", "F2", "F3", "F4", "F5"], "Procesar y almacenar": ["F6", "F7"],
          "Entregar datos": ["F8", "F9"], "Soportar la plataforma": ["F10", "F11"]}


def orden():
    pend, res = dict(F), []
    while pend:
        listos = [k for k, v in pend.items() if all(p in res for p in v[3])]
        assert listos, "ciclo"
        res.append(listos[0]); pend.pop(listos[0])
    return res


def calcular():
    o = orden()
    ef = {}
    for k in o:
        ef[k] = max([ef[p] for p in F[k][3]], default=0) + F[k][1]
    fin = max(ef.values())
    sucs = {k: [j for j in F if k in F[j][3]] for k in F}
    # LF(k) = min LS(sucesor); LS(k) = LF(k) - dur
    lf, lsx = {}, {}
    for k in reversed(o):
        lf[k] = min([lsx[s] for s in sucs[k]], default=fin)
        lsx[k] = lf[k] - F[k][1]
    holgura = {k: lsx[k] - (ef[k] - F[k][1]) for k in F}
    critica = [k for k in o if holgura[k] == 0 and F[k][1] > 0]
    # segunda via: todos los caminos
    def caminos(k):
        if not sucs[k]: return [[k]]
        return [[k] + c for s in sucs[k] for c in caminos(s)]
    sin_pred = [k for k in F if not F[k][3]]
    todos = [c for k in sin_pred for c in caminos(k)]
    dur_c = lambda c: sum(F[x][1] for x in c)
    mejor = max(todos, key=dur_c)
    # acoplamiento entre subsistemas: flujos entre funciones de subsistemas distintos
    cruces = {}
    for k in F:
        for p in F[k][3]:
            a, b = sorted([F[p][2], F[k][2]])
            if a != b: cruces[(a, b)] = cruces.get((a, b), 0) + 1
    subs = sorted({v[2] for v in F.values()})
    acopl = {s: sum(n for (a, b), n in cruces.items() if s in (a, b)) for s in subs}
    mas = max(acopl, key=acopl.get)
    return dict(n_f=len(F), n_sub=len(subs), t_crit=fin, critica=critica, t_via2=dur_c(mejor), via2=[x for x in mejor if F[x][1] > 0],
                holg_f4=holgura["F4"], holg_f1=holgura["F1"], n_cruces=sum(cruces.values()), cruces=cruces, acopl=acopl, mas=mas,
                n_caminos=len(todos), ef=ef, holgura=holgura)


def main():
    V = calcular()
    print(cabecera())
    print(f"Datos SINTETICOS: {V['n_f']} funciones, {V['n_sub']} subsistemas, duraciones en segundos")
    for g, fs in GRUPOS.items():
        print(f"  {g}: " + ", ".join(f"{f} {F[f][0]} [{F[f][2]}]" for f in fs))
    print(f"Duracion de la ruta critica = {V['t_crit']} s ; ruta critica = {' -> '.join(V['critica'])}")
    print(f"Segunda via (enumeracion de {V['n_caminos']} caminos): {V['t_via2']} s ; {' -> '.join(V['via2'])}")
    print(f"Holgura de F1 = {V['holg_f1']} s ; holgura de F4 = {V['holg_f4']} s")
    print(f"Flujos entre subsistemas distintos = {V['n_cruces']}")
    for (a, b), n in sorted(V["cruces"].items()):
        print(f"  {a} - {b}: {n}")
    print("Acoplamiento por subsistema: " + ", ".join(f"{s} {n}" for s, n in V["acopl"].items()) + f" ; mas acoplado: {V['mas']}")
    comprobar(V["t_crit"] == V["t_via2"], "ruta critica por DP y por enumeracion")
    comprobar(V["critica"] == V["via2"], "misma ruta critica")
    comprobar(all(h >= 0 for h in V["holgura"].values()), "holguras no negativas")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
