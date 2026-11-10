#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C24: arbol de fallos: conjuntos minimos de corte, probabilidad del evento superior por tres vias e importancia.

Datos: SINTETICOS. Evento superior: «perdida de control de actitud» de ESTRELLA-S. Siete eventos basicos independientes con
probabilidad en la mision inventada (B1 sensor solar 0.02, B2 magnetometro 0.03, B3 rueda 0.06, B4 magnetopar 0.01, B5 error de
software 0.01, B6 latch-up sin recuperacion 0.02, B7 fallo de alimentacion 0.005). Estructura: TOP = G1 O G2 O G3; G1 = (B1 Y B2) O B7;
G2 = B3 Y B4; G3 = B5 O (B6 Y B7). B7 aparece dos veces (evento repetido). Metodo 1: conjuntos minimos de corte (MOCUS con absorcion)
y aproximaciones de evento raro y de cota superior de cortes minimos. Segunda via: enumeracion exacta de los 2^7 estados. Tercera via:
Monte Carlo (400000, semilla 83024). Importancia: Birnbaum y Fussell-Vesely (FV = (P - P|p_i = 0)/P). Tolerancias: exacto frente
a la formula de cortes (inclusion-exclusion) a 1e-12; Monte Carlo a 1.2e-3 (4 sigma). Sin constantes fisicas.
"""
import itertools
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

P = {"B1": 0.02, "B2": 0.03, "B3": 0.06, "B4": 0.01, "B5": 0.01, "B6": 0.02, "B7": 0.005}
ARBOL = ("OR", [("OR", [("AND", ["B1", "B2"]), "B7"]), ("AND", ["B3", "B4"]), ("OR", ["B5", ("AND", ["B6", "B7"])])])


def evalua(nodo, estado):
    if isinstance(nodo, str): return estado[nodo]
    op, hijos = nodo
    v = [evalua(h, estado) for h in hijos]
    return all(v) if op == "AND" else any(v)


def cortes(nodo):
    """Conjuntos de corte por expansion (MOCUS): lista de frozensets."""
    if isinstance(nodo, str): return [frozenset([nodo])]
    op, hijos = nodo
    sub = [cortes(h) for h in hijos]
    if op == "OR": return [c for s in sub for c in s]
    res = [frozenset()]
    for s in sub: res = [a | b for a in res for b in s]
    return res


def minimos(cs):
    cs = sorted(set(cs), key=len)
    out = []
    for c in cs:
        if not any(m <= c for m in out): out.append(c)
    return out


def prob_cs(c, p): return float(np.prod([p[x] for x in c]))


def exacta(p):
    ev = list(p); tot = 0.0
    for bits in itertools.product([0, 1], repeat=len(ev)):
        est = {e: bool(b) for e, b in zip(ev, bits)}
        if evalua(ARBOL, est):
            tot += float(np.prod([p[e] if est[e] else 1 - p[e] for e in ev]))
    return tot


def inclusion_exclusion(mcs, p):
    tot = 0.0
    for k in range(1, len(mcs) + 1):
        for sub in itertools.combinations(mcs, k):
            tot += (-1) ** (k + 1) * prob_cs(frozenset().union(*sub), p)
    return tot


def calcular():
    mcs = minimos(cortes(ARBOL))
    pc = [prob_cs(c, P) for c in mcs]
    ex = exacta(P)
    ie = inclusion_exclusion(mcs, P)
    rara = sum(pc)
    cota = 1 - float(np.prod([1 - x for x in pc]))
    rng = np.random.default_rng(83024)
    N = 400000
    est = {e: rng.random(N) < P[e] for e in P}
    top = (est["B1"] & est["B2"]) | est["B7"] | (est["B3"] & est["B4"]) | est["B5"] | (est["B6"] & est["B7"])
    mc = float(top.mean())
    imp = {}
    for e in P:
        p0 = dict(P); p0[e] = 0.0; p1 = dict(P); p1[e] = 1.0
        imp[e] = dict(birn=exacta(p1) - exacta(p0), fv=(ex - exacta(p0)) / ex)
    mayor_fv = max(imp, key=lambda e: imp[e]["fv"])
    V = dict(mcs=[sorted(c) for c in mcs], pc=pc, n_mcs=len(mcs), n_unit=sum(1 for c in mcs if len(c) == 1), ex=ex, ie=ie, rara=rara, cota=cota, mc=mc,
             dif_ie=abs(ex - ie), dif_mc=abs(ex - mc), err_rara=100 * (rara - ex) / ex, imp=imp, mayor_fv=mayor_fv, fv_mayor=imp[mayor_fv]["fv"],
             n_estados=2 ** len(P), sin_absorcion=len(cortes(ARBOL)))
    return V


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 7 eventos basicos; TOP = (B1 Y B2) O B7 O (B3 Y B4) O B5 O (B6 Y B7)")
    print(f"Conjuntos de corte antes de la absorcion: {V['sin_absorcion']} ; minimos: {V['n_mcs']} ({V['n_unit']} de un solo evento)")
    for c, x in zip(V["mcs"], V["pc"]): print(f"  {{{', '.join(c)}}}  P = {x:.3e}")
    print(f"P(TOP) exacta por enumeracion de {V['n_estados']} estados = {V['ex']:.8f}")
    print(f"P(TOP) por inclusion-exclusion de cortes = {V['ie']:.8f} ; diferencia {V['dif_ie']:.1e}")
    print(f"Aproximacion de evento raro = {V['rara']:.8f} (error {V['err_rara']:.3f} %) ; cota de cortes minimos = {V['cota']:.8f}")
    print(f"Monte Carlo (400000, semilla 83024) = {V['mc']:.6f} ; diferencia con la exacta {V['dif_mc']:.1e}")
    print("Importancia: " + ", ".join(f"{e} FV {v['fv']:.3f} B {v['birn']:.4f}" for e, v in V["imp"].items()))
    print(f"Mayor contribuyente (Fussell-Vesely): {V['mayor_fv']} ({V['fv_mayor']:.3f})")
    comprobar(V["dif_ie"] < 1e-12, "exacta e inclusion-exclusion")
    comprobar(V["dif_mc"] < 1.2e-3, "Monte Carlo cerca de la exacta")
    comprobar(V["rara"] >= V["ex"] and V["cota"] >= V["ex"], "las dos aproximaciones son cotas superiores")
    comprobar(V["n_mcs"] == 4 and V["sin_absorcion"] == 5, "cortes minimos esperados")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
