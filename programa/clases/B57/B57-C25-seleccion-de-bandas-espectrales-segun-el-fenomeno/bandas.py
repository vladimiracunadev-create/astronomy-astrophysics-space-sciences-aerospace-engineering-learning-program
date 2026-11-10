#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C25: seleccion de bandas segun el fenomeno: separabilidad de clases y busqueda de subconjuntos.

Datos: SINTETICOS. Cuatro clases (agua, vegetacion, suelo desnudo, ceniza/quemado) con reflectancias medias en 8 bandas candidatas y desviacion de 0.02 por banda
(ILUSTRATIVAS). Los centros de las ocho bandas candidatas (0.45, 0.55, 0.66, 0.74, 0.86, 1.24, 1.61, 2.20 um) siguen el reparto de las bandas de un sensor multiespectral
generico y no son los de ningun sensor concreto.
Modelo: distancia de Bhattacharyya para gaussianas de igual covarianza diagonal B = d^2/8 con d^2 = sum (m_i - m_j)^2 / sigma^2 ; distancia de Jeffries-Matusita JM = 2 (1 - exp(-B)) en [0, 2] ;
objetivo = minimo JM entre pares de clases; busqueda exhaustiva de los subconjuntos de k bandas frente a la busqueda voraz hacia adelante.
Validez: gaussianas de igual covarianza diagonal. Tolerancia: JM analitica = JM calculada a 1e-12; el optimo exhaustivo debe ser >= al voraz.
"""
import itertools, math, platform

BANDAS = [0.45, 0.55, 0.66, 0.74, 0.86, 1.24, 1.61, 2.20]
SIG = 0.02
CLASES = {
    "agua":        [0.06, 0.07, 0.04, 0.02, 0.01, 0.01, 0.00, 0.00],
    "vegetacion":  [0.04, 0.09, 0.05, 0.25, 0.45, 0.40, 0.22, 0.10],
    "suelo":       [0.10, 0.14, 0.20, 0.24, 0.28, 0.33, 0.38, 0.36],
    "quemado":     [0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.11, 0.09],
}
NOM = list(CLASES)


def jm(a, b, idx):
    d2 = sum((a[i] - b[i]) ** 2 for i in idx) / SIG**2
    return 2 * (1 - math.exp(-d2 / 8.0))


def objetivo(idx):
    return min(jm(CLASES[x], CLASES[y], idx) for x, y in itertools.combinations(NOM, 2))


def calcular():
    r = {}
    todas = list(range(len(BANDAS)))
    r["jm_todas"] = objetivo(todas)
    r["jm_rgb"] = objetivo([1, 2, 4])  # verde, rojo, NIR
    mejores = {}
    voraz = {}
    sel = []
    for k in (1, 2, 3, 4):
        best = max(itertools.combinations(todas, k), key=objetivo)
        mejores[k] = (best, objetivo(best))
        cand = max((i for i in todas if i not in sel), key=lambda i: objetivo(sel + [i]))
        sel = sel + [cand]
        voraz[k] = (list(sel), objetivo(sel))
    r["mejores"], r["voraz"] = mejores, voraz
    r["par_dificil"] = min(itertools.combinations(NOM, 2), key=lambda p: jm(CLASES[p[0]], CLASES[p[1]], todas))
    r["jm_par_dificil"] = jm(CLASES[r["par_dificil"][0]], CLASES[r["par_dificil"][1]], todas)
    r["jm_par_dificil_nir"] = jm(CLASES[r["par_dificil"][0]], CLASES[r["par_dificil"][1]], [4])
    for k in (1, 2, 3, 4):
        r[f"mejores_k{k}"] = ", ".join(str(BANDAS[i]).replace(".", ",") for i in mejores[k][0])
        r[f"voraz_k{k}"] = ", ".join(str(BANDAS[i]).replace(".", ",") for i in voraz[k][0])
        r[f"jm_e{k}"], r[f"jm_v{k}"] = mejores[k][1], voraz[k][1]
    r["dif_k3"] = mejores[3][1] - voraz[3][1]
    r["nombres_k3"] = ", ".join(str(BANDAS[i]) for i in mejores[3][0])
    r["nombres_vor3"] = ", ".join(str(BANDAS[i]) for i in voraz[3][0])
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"JM minimo entre pares con las 8 bandas = {r['jm_todas']:.4f} ; con verde-rojo-NIR (0.55, 0.66, 0.86) = {r['jm_rgb']:.4f}")
    print(f"Par mas dificil: {r['par_dificil'][0]} - {r['par_dificil'][1]} ; JM con 8 bandas = {r['jm_par_dificil']:.4f} ; solo NIR 0.86 = {r['jm_par_dificil_nir']:.4f}")
    for k in (1, 2, 3, 4):
        be, vo = r["mejores"][k], r["voraz"][k]
        print(f"k = {k}: exhaustivo {[BANDAS[i] for i in be[0]]} JM = {be[1]:.4f} ; voraz {[BANDAS[i] for i in vo[0]]} JM = {vo[1]:.4f}")
    a, b = CLASES["agua"], CLASES["vegetacion"]
    d2 = sum((x - y) ** 2 for x, y in zip(a, b)) / SIG**2
    assert abs(jm(a, b, range(8)) - 2 * (1 - math.exp(-d2 / 8))) < 1e-12
    for k in (1, 2, 3, 4):
        assert r["mejores"][k][1] >= r["voraz"][k][1] - 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
