#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C04: matriz multicriterio de propuesta de valor y estabilidad del ranking, con datos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria financiera ni de negocios. Opciones, criterios, pesos y puntajes son SINTETICOS.
Modelo: puntaje_i = sum_k w_k s_ik, con sum(w) = 1 y s_ik en [1, 5] (1 = peor, 5 = mejor).
Sensibilidad por peso: se cambia w_k = t y los demas se reescalan proporcionalmente a (1 - t); el cruce entre dos opciones se resuelve
de forma analitica y se contrasta con un barrido de t en pasos de 0.0001.
Estabilidad: 20000 vectores de pesos Dirichlet (concentracion 20 alrededor de los pesos base, semilla 124); se cuenta cuantas veces gana cada opcion.
Tolerancias: cruce analitico frente a barrido < 2e-4; suma de frecuencias = 1 dentro de 1e-12; puntaje por producto matricial = por bucle (< 1e-12).
"""
import platform, random

OPCIONES = ["A imagen mensual", "B alerta en 24 h", "C indice de cultivo", "D datos abiertos", "E consultoria a medida"]
CRIT = ["necesidad del usuario", "calidad de dato", "plazo de entrega", "costo para el usuario", "diferenciacion"]
W = [0.30, 0.25, 0.15, 0.15, 0.15]
S = [  # filas: opciones; columnas: criterios (1-5)
    [3, 4, 3, 4, 2],
    [5, 3, 5, 2, 4],
    [4, 4, 3, 3, 4],
    [3, 5, 2, 5, 2],
    [4, 3, 1, 1, 5],
]


def puntajes(w):
    return [sum(wk * sk for wk, sk in zip(w, fila)) for fila in S]


def puntajes_matriz(w):
    cols = list(zip(*S))
    # segunda forma de calcular: por columnas
    total = [0.0] * len(S)
    for k, col in enumerate(cols):
        for i, v in enumerate(col):
            total[i] += w[k] * v
    return total


def con_peso(k, t):
    resto = sum(W) - W[k]
    return [t if j == k else W[j] * (1 - t) / resto for j in range(len(W))]


def cruce_analitico(i, j, k):
    # f(t) = puntaje_i - puntaje_j es lineal en t: f(0) y f(1) determinan la raiz
    f0 = puntajes(con_peso(k, 0.0))
    f1 = puntajes(con_peso(k, 1.0))
    d0, d1 = f0[i] - f0[j], f1[i] - f1[j]
    if d0 == d1:
        return None
    t = d0 / (d0 - d1)
    return t if 0 <= t <= 1 else None


def cruce_barrido(i, j, k):
    ant = None
    for n in range(0, 10001):
        t = n / 10000
        p = puntajes(con_peso(k, t))
        d = p[i] - p[j]
        if ant is not None and (ant > 0) != (d > 0):
            return t
        ant = d
    return None


def run():
    p = puntajes(W)
    pm = puntajes_matriz(W)
    ord_ = sorted(range(len(p)), key=lambda i: -p[i])
    rng = random.Random(124)
    gan = [0] * len(S)
    n = 20000
    for _ in range(n):
        g = [rng.gammavariate(20 * w, 1.0) for w in W]
        tot = sum(g)
        wr = [x / tot for x in g]
        pr = puntajes(wr)
        gan[max(range(len(pr)), key=lambda i: pr[i])] += 1
    frec = [g / n for g in gan]
    i1, i2 = ord_[0], ord_[1]
    k = 0  # criterio cuyo peso se mueve
    ta = cruce_analitico(i1, i2, k)
    tb = cruce_barrido(i1, i2, k)
    R = {"lider": ord_[0], "segundo": ord_[1], "p_lider": p[ord_[0]], "p_segundo": p[ord_[1]], "dif_mat": max(abs(a - b) for a, b in zip(p, pm)),
         "frec_suma": sum(frec), "t_an": ta if ta is not None else -1.0, "t_ba": tb if tb is not None else -1.0, "peso_base": W[k],
         "dif_cruce": abs(ta - tb) if (ta is not None and tb is not None) else 0.0}
    for i in range(len(S)):
        R[f"p{i}"] = p[i]
        R[f"f{i}"] = frec[i]
    R["ord"] = ord_
    R["frec"] = frec
    R["nlider"] = OPCIONES[ord_[0]]
    R["nsegundo"] = OPCIONES[ord_[1]]
    R["f_lider"] = frec[ord_[0]]
    R["f_segundo"] = frec[ord_[1]]
    R["f_ultimo"] = frec[ord_[-1]]
    R["dif_lider"] = p[ord_[0]] - p[ord_[1]]
    return R


def main():
    R = run()
    ord_, frec = R['ord'], R['frec']
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Propuestas de valor SINTETICAS; puntajes 1-5; pesos base:", ", ".join(f"{c}={w}" for c, w in zip(CRIT, W)))
    print(" opcion                    puntaje   P(gana) con pesos Dirichlet")
    for i in ord_:
        print(f" {OPCIONES[i]:<24} {R[f'p{i}']:8.3f}   {frec[i]:.4f}")
    print(f"Lider = {OPCIONES[R['lider']]} ; segundo = {OPCIONES[R['segundo']]}")
    print(f"El primero deja de liderar al subir/bajar el peso de '{CRIT[0]}' desde {R['peso_base']} hasta t = {R['t_an']:.4f} (analitico) ; barrido {R['t_ba']:.4f} ; diferencia {R['dif_cruce']:.1e}")
    print(f"Puntaje por filas frente a por columnas (error) = {R['dif_mat']:.1e} ; suma de frecuencias = {R['frec_suma']:.6f}")
    assert R["dif_mat"] < 1e-12 and abs(R["frec_suma"] - 1) < 1e-12
    assert R["dif_cruce"] < 2e-4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
