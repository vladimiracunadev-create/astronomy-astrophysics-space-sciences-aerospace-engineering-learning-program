#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C07: comparacion de arquitecturas con jerarquia analitica (AHP) y sensibilidad.

Datos: SINTETICOS (tres arquitecturas candidatas para la mision de ejemplo ESTRELLA-S y comparaciones por pares en la escala 1-9
inventadas para el ejemplo). Modelo: vector propio principal de cada matriz de comparaciones; razon de consistencia CR = CI/RI,
con RI = 0.58 (n = 3) y 0.90 (n = 4): indices aleatorios tabulados estandar, NO consultados en una fuente concreta.
Segunda via: iteracion de potencias frente a numpy.linalg.eig. Tolerancia: pesos entre metodos a 1e-9. Sin constantes fisicas.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

ARQ = ["A Un satelite de 80 kg", "B Tres microsatelites", "C Carga alojada en plataforma ajena"]
CRIT = ["Costo", "Desempeno", "Riesgo", "Calendario"]
M_CRIT = np.array([[1, 1 / 3, 2, 3], [3, 1, 4, 5], [1 / 2, 1 / 4, 1, 2], [1 / 3, 1 / 5, 1 / 2, 1]])
M_ALT = [np.array([[1, 3, 1 / 2], [1 / 3, 1, 1 / 5], [2, 5, 1]]),
         np.array([[1, 1 / 2, 3], [2, 1, 5], [1 / 3, 1 / 5, 1]]),
         np.array([[1, 2, 1 / 2], [1 / 2, 1, 1 / 4], [2, 4, 1]]),
         np.array([[1, 4, 1 / 2], [1 / 4, 1, 1 / 5], [2, 5, 1]])]
RI = {3: 0.58, 4: 0.90}


def pesos_eig(M):
    w, v = np.linalg.eig(M)
    k = int(np.argmax(w.real))
    p = np.abs(v[:, k].real); return p / p.sum(), float(w[k].real)


def pesos_pot(M, it=500):
    x = np.ones(len(M)) / len(M)
    for _ in range(it):
        x = M @ x; x /= x.sum()
    return x


def cr(M):
    n = len(M); _, lam = pesos_eig(M)
    return (lam - n) / (n - 1) / RI[n]


def globales(wc):
    L = np.array([pesos_eig(M)[0] for M in M_ALT])   # criterios x alternativas
    return wc @ L


def calcular():
    wc, lam = pesos_eig(M_CRIT)
    wc2 = pesos_pot(M_CRIT)
    g = globales(wc)
    crs = [cr(M_CRIT)] + [cr(M) for M in M_ALT]
    # sensibilidad: peso del desempeno de 0 a 1, resto proporcional
    cruce = None; prev = None
    barrido = []
    for p in np.linspace(0, 1, 1001):
        w = np.array([(1 - p) * wc[i] / (1 - wc[1]) if i != 1 else p for i in range(4)])
        gg = globales(w); k = int(np.argmax(gg)); barrido.append(k)
        if prev is not None and k != prev and cruce is None: cruce = p
        prev = k
    return dict(wc=wc, wc2=wc2, lam=lam, g=g, k=int(np.argmax(g)), ganador=ARQ[int(np.argmax(g))], cr_crit=crs[0], cr_max=max(crs),
                crs=crs, cruce=cruce if cruce is not None else -1.0, w_perf=wc[1], gA=g[0], gB=g[1], gC=g[2],
                w1=wc[0], w2=wc[1], w3=wc[2], w4=wc[3], gana_p0=ARQ[barrido[0]], gana_p1=ARQ[barrido[-1]])


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 3 arquitecturas, 4 criterios, escala de comparacion 1-9; RI tabulado (no consultado)")
    print("Pesos de criterios: " + ", ".join(f"{c} {w:.4f}" for c, w in zip(CRIT, V["wc"])) + f" ; lambda_max = {V['lam']:.4f} ; CR = {V['cr_crit']:.4f}")
    print("CR de las matrices de alternativas: " + ", ".join(f"{c} {x:.4f}" for c, x in zip(CRIT, V["crs"][1:])))
    print("Puntaje global: " + ", ".join(f"{a[:1]} {x:.4f}" for a, x in zip(ARQ, V["g"])))
    print(f"Ganadora: {V['ganador']}")
    print(f"Sensibilidad al peso del desempeno: con peso 0 gana {V['gana_p0']} ; con peso 1 gana {V['gana_p1']} ; cruce en p = {V['cruce']:.3f}")
    comprobar(np.allclose(V["wc"], V["wc2"], atol=1e-9), "pesos por eig y por potencias")
    comprobar(V["cr_max"] < 0.10, "todas las matrices son consistentes (CR < 0.10)")
    comprobar(abs(V["g"].sum() - 1) < 1e-9, "puntajes globales suman 1")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
