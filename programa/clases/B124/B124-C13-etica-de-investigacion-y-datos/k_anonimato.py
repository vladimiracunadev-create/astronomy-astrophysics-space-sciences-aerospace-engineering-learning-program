#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C13: riesgo de reidentificacion con k-anonimato sobre un conjunto de datos SINTETICO de participantes.

CONTENIDO EDUCATIVO: no es asesoria juridica ni de proteccion de datos. Los 300 participantes son SINTETICOS (no son personas reales).
Cuasi-identificadores: edad, codigo postal (5 digitos), tipo de equipo. Atributo sensible: banda de ingresos (bajo/medio/alto), inventada.
Generalizacion: edad: 0 exacta, 1 banda de 10 anios, 2 banda de 20 anios, 3 suprimida; postal: 0 cinco digitos, 1 tres digitos, 2 un digito, 3 suprimido;
equipo: 0 exacto, 1 suprimido. El reticulado tiene 4 x 4 x 2 = 32 nodos.
k de un nodo = tamano del grupo mas pequeno. Se permite suprimir hasta el 5 % de los registros (los de grupos menores que K_OBJETIVO = 5).
Perdida de informacion: metrica de discernibilidad DM = suma de (tamano del grupo)^2 + supresiones x N.
Busqueda: exhaustiva sobre los 32 nodos y voraz (sube el nivel del atributo que mas reduce los grupos pequenos); ambas deben ser validas, la exhaustiva no peor.
Conteo: dos implementaciones (Counter y orden con agrupacion) deben coincidir. Semilla 124.
Tolerancias: igualdad exacta de conteos; riesgo medio = grupos / N.
"""
import itertools, platform, random
from collections import Counter

N, K_OBJ, MAX_SUPR = 300, 5, 0.05
ZONAS = ["80", "81", "82", "83", "84", "85"]
EQUIPOS = ["binocular", "refractor", "reflector"]
INGRESOS = ["bajo", "medio", "alto"]


def datos():
    rng = random.Random(124)
    out = []
    for _ in range(N):
        edad = int(min(80, max(18, rng.gauss(45, 15))))
        cp = rng.choice(ZONAS) + "".join(rng.choice("0123456789") for _ in range(3))
        out.append((edad, cp, rng.choice(EQUIPOS), rng.choice(INGRESOS)))
    return out


def gen_edad(e, n):
    return [e, e // 10, e // 20, 0][n]


def gen_cp(c, n):
    return [c, c[:3], c[:1], ""][n]


def gen_eq(q, n):
    return [q, ""][n]


def llave(r, nodo):
    return (gen_edad(r[0], nodo[0]), gen_cp(r[1], nodo[1]), gen_eq(r[2], nodo[2]))


def grupos_counter(d, nodo):
    return Counter(llave(r, nodo) for r in d)


def grupos_orden(d, nodo):
    ks = sorted(llave(r, nodo) for r in d)
    res = {}
    for k, g in itertools.groupby(ks):
        res[k] = len(list(g))
    return res


def evaluar(d, nodo):
    g = grupos_counter(d, nodo)
    assert dict(g) == grupos_orden(d, nodo)
    pequenos = sum(c for c in g.values() if c < K_OBJ)
    quedan = {k: c for k, c in g.items() if c >= K_OBJ}
    valido = pequenos <= MAX_SUPR * len(d)
    k = min(quedan.values()) if quedan else 0
    dm = sum(c * c for c in quedan.values()) + pequenos * len(d)
    return dict(nodo=nodo, valido=valido, k=k, dm=dm, supr=pequenos, grupos=len(quedan), g=g)


def exhaustiva(d):
    nodos = [(a, b, c) for a in range(4) for b in range(4) for c in range(2)]
    ev = [evaluar(d, n) for n in nodos]
    validos = [e for e in ev if e["valido"]]
    return min(validos, key=lambda e: e["dm"]), len(validos), ev


def voraz(d):
    nodo = [0, 0, 0]
    tope = [3, 3, 1]
    while True:
        e = evaluar(d, tuple(nodo))
        if e["valido"]:
            return e
        mejor, mp = None, None
        for i in range(3):
            if nodo[i] < tope[i]:
                n2 = nodo[:]
                n2[i] += 1
                p = evaluar(d, tuple(n2))["supr"]
                if mp is None or p < mp:
                    mejor, mp = i, p
        nodo[mejor] += 1


def run():
    d = datos()
    g0 = grupos_counter(d, (0, 0, 0))
    unicos = sum(1 for c in g0.values() if c == 1)
    best, n_validos, _ = exhaustiva(d)
    vor = voraz(d)
    sens = {}
    for r in d:
        sens.setdefault(llave(r, best["nodo"]), set()).add(r[3])
    l_min = min(len(sens[k]) for k, c in best["g"].items() if c >= K_OBJ)
    R = {"unicos": unicos, "pct_unicos": unicos / N, "n_validos": n_validos, "best_a": best["nodo"][0], "best_p": best["nodo"][1], "best_e": best["nodo"][2],
         "best_k": best["k"], "best_dm": best["dm"], "best_supr": best["supr"], "best_grupos": best["grupos"], "riesgo_max": 1 / best["k"],
         "riesgo_med": best["grupos"] / (N - best["supr"]), "vor_a": vor["nodo"][0], "vor_p": vor["nodo"][1], "vor_e": vor["nodo"][2], "vor_dm": vor["dm"],
         "vor_valido": 1 if vor["valido"] else 0, "l_min": l_min, "dm0": evaluar(d, (0, 0, 0))["dm"], "grupos0": len(g0), "k0": min(g0.values())}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"{N} participantes SINTETICOS; cuasi-identificadores: edad, codigo postal, equipo ; sensible: ingresos ; k objetivo = {K_OBJ} ; supresion maxima = {100 * MAX_SUPR:.0f} %")
    print(f"Sin generalizar: {R['grupos0']} grupos ; k = {R['k0']} ; registros unicos = {R['unicos']} ({100 * R['pct_unicos']:.1f} %) -> riesgo de reidentificacion 100 % para ellos")
    print(f"Nodos validos del reticulado (de 32): {R['n_validos']}")
    print(f"Optimo exhaustivo: edad nivel {R['best_a']}, postal nivel {R['best_p']}, equipo nivel {R['best_e']} ; k = {R['best_k']} ; supresiones = {R['best_supr']} ; grupos = {R['best_grupos']} ; DM = {R['best_dm']}")
    print(f"  riesgo maximo 1/k = {R['riesgo_max']:.3f} ; riesgo medio = {R['riesgo_med']:.4f} ; diversidad minima de ingresos por grupo = {R['l_min']}")
    print(f"Voraz: edad {R['vor_a']}, postal {R['vor_p']}, equipo {R['vor_e']} ; DM = {R['vor_dm']} ; valido = {bool(R['vor_valido'])}")
    assert R["vor_valido"] == 1 and R["best_dm"] <= R["vor_dm"] and R["best_k"] >= K_OBJ
    print("Conteos Counter y por orden: iguales en los 32 nodos.")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
