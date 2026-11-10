#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C02: partes interesadas, necesidades ponderadas y estabilidad del orden.

Datos: SINTETICOS (seis partes interesadas de la mision de ejemplo ESTRELLA-S, sus poder/interes 1-5 y la importancia 0-5 que
cada una da a cinco necesidades). Modelo: peso de la parte = poder*interes normalizado; prioridad de la necesidad = suma
ponderada. Estabilidad: 10000 perturbaciones lognormales (sigma = 0.3, semilla 83002). Segunda via: calculo con bucles.
Tolerancia: coincidencia de prioridades a 1e-12. Sin constantes fisicas.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

PARTES = ["Equipo cientifico", "Agencia financiadora", "Operador de estacion", "Proveedor de lanzamiento", "Usuarios de datos", "Regulador de espectro"]
PODER = np.array([3, 5, 2, 4, 2, 5], dtype=float)
INTERES = np.array([5, 4, 3, 2, 5, 2], dtype=float)
NEC = ["N1 Alta resolucion", "N2 Bajo costo", "N3 Entrega rapida de datos", "N4 Cumplir normas de espectro", "N5 Larga vida util"]
IMP = np.array([[5, 2, 3, 1, 4],
                [3, 5, 2, 3, 3],
                [2, 3, 5, 3, 2],
                [1, 4, 1, 3, 1],
                [4, 2, 5, 1, 3],
                [1, 2, 1, 5, 2]], dtype=float)


def clase(p, i):
    return "gestionar de cerca" if p >= 4 and i >= 4 else ("mantener satisfecha" if p >= 4 else ("mantener informada" if i >= 4 else "monitorear"))


def rangos(v):
    o = np.argsort(-v)
    r = np.empty(len(v)); r[o] = np.arange(len(v)); return r


def calcular():
    w = PODER * INTERES; w = w / w.sum()
    prio = w @ IMP
    prio2 = np.array([sum(w[s] * IMP[s, n] for s in range(6)) for n in range(5)])
    rng = np.random.default_rng(83002)
    base = rangos(prio)
    top = 0; rho = 0.0; N = 10000
    for _ in range(N):
        wk = w * np.exp(rng.normal(0, 0.3, 6)); wk /= wk.sum()
        pk = wk @ IMP
        top += int(np.argmax(pk) == np.argmax(prio))
        d = rangos(pk) - base
        rho += 1 - 6 * np.sum(d ** 2) / (5 * (25 - 1))
    conf = int(sum(1 for n in range(5) for a in range(6) for b in range(a + 1, 6) if abs(IMP[a, n] - IMP[b, n]) >= 4))
    cl = [clase(p, i) for p, i in zip(PODER, INTERES)]
    V = dict(w=w, prio=prio, prio2=prio2, n_conf=conf, p_top=100.0 * top / N, rho=rho / N,
             top_need=NEC[int(np.argmax(prio))], n_gest=cl.count("gestionar de cerca"), cl=cl)
    for k in range(5): V[f"p{k+1}"] = prio[k]
    for k in range(6): V[f"w{k+1}"] = w[k] * 100
    return V


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 6 partes interesadas, 5 necesidades (escala 0-5); poder/interes 1-5")
    for i, p in enumerate(PARTES):
        print(f"  {p:26s} poder {PODER[i]:.0f} interes {INTERES[i]:.0f} peso {V['w'][i]*100:5.1f} %  -> {V['cl'][i]}")
    print("Prioridad de las necesidades (suma ponderada):")
    for n, p in zip(NEC, V["prio"]):
        print(f"  {n:32s} {p:.3f}")
    print(f"Necesidad prioritaria: {V['top_need']} ; pares en conflicto (diferencia >= 4): {V['n_conf']}")
    print(f"Estabilidad (10000 perturbaciones, semilla 83002): primera necesidad igual en {V['p_top']:.1f} % ; correlacion de rangos media {V['rho']:.3f}")
    comprobar(np.allclose(V["prio"], V["prio2"], atol=1e-12), "prioridad por producto matricial y por bucles")
    comprobar(abs(V["w"].sum() - 1) < 1e-12, "los pesos suman 1")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
