#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B107-C09: criterios de progresion y de alta con umbrales, requisito de confirmacion y error de medida.

TODO SINTETICO/ILUSTRATIVO: cuatro indicadores de un tripulante inventado, cada uno en % del valor previo al vuelo; trayectorias exponenciales
con deficit y constante de tiempo inventados; umbrales (95 % para todos) y la regla de «2 evaluaciones consecutivas» son del ejemplo, no de ninguna
mision ni norma. Semilla 107. Evaluaciones en los dias 5, 10, 15, ..., 90 (cada 5 dias). Ruido de medida gaussiano de 2.0 puntos.
Regla: alta cuando TODOS los indicadores >= 95 % en k evaluaciones consecutivas (k = 1 o 2).
Verificacion: (a) sin ruido, el dia de alta analitico es max_i(tau_i ln(D_i/5)) redondeado a la siguiente evaluacion (+ k - 1 evaluaciones);
(b) con ruido, la probabilidad de un «pase falso» (todos >= 95 con el verdadero valor por debajo) se compara con el producto de normales;
(c) k = 2 reduce los pases falsos. Tolerancias: dia analitico = dia sin ruido; pase falso simulado vs teorico +-1 punto (30000 repeticiones). Numpy y math.
"""
from __future__ import annotations
import math
import platform
import numpy as np

D = np.array([22.0, 15.0, 30.0, 12.0])
TAU = np.array([20.0, 14.0, 28.0, 10.0])
NOM = ["fuerza", "equilibrio", "resistencia", "marcha"]
UMBRAL, SIG = 95.0, 2.0
DIAS = np.arange(5, 95, 5)


def verd(t):
    return 100 - D[None, :] * np.exp(-t[:, None] / TAU[None, :])


def dia_alta(med, k):
    ok = np.all(med >= UMBRAL, axis=1)
    for i in range(len(DIAS) - k + 1):
        if ok[i : i + k].all():
            return int(DIAS[i + k - 1])
    return None


def fi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def main():
    rng = np.random.default_rng(107)
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS E ILUSTRATIVOS (semilla 107): 4 indicadores; umbral 95 %; ruido 2.0 puntos; reglas del ejemplo")
    tcruce = TAU * np.log(D / (100 - UMBRAL))
    print("Dia en que cada indicador verdadero cruza el 95 %: " + ", ".join(f"{n} {t:.1f}" for n, t in zip(NOM, tcruce)))
    t_ana = float(tcruce.max())
    sig = verd(DIAS.astype(float))
    d1 = dia_alta(sig, 1)
    d2 = dia_alta(sig, 2)
    sig_dia = int(DIAS[np.argmax(DIAS >= t_ana)])
    print(f"Sin ruido: dia de alta con k = 1: {d1}; con k = 2: {d2}; analitico (primera evaluacion >= {t_ana:.1f} d) = {sig_dia}")
    assert d1 == sig_dia
    # pase falso: en una evaluacion cuando el verdadero esta bajo el umbral
    t_ev = 40.0
    vv = verd(np.array([t_ev]))[0]
    por_debajo = vv < UMBRAL
    print(f"Evaluacion del dia {t_ev:.0f}: verdaderos = " + ", ".join(f"{n} {v:.1f}" for n, v in zip(NOM, vv)))
    p_teo = 1.0
    for v in vv:
        p_teo *= 1 - fi((UMBRAL - v) / SIG)
    N = 30000
    med = vv[None, :] + rng.normal(0, SIG, (N, 4))
    p_sim = float(np.mean(np.all(med >= UMBRAL, axis=1)))
    print(f"Probabilidad de que una sola evaluacion en el dia {t_ev:.0f} cumpla todos los umbrales (pase falso si algun verdadero esta bajo): teorica = {p_teo*100:.2f} %; simulada = {p_sim*100:.2f} %")
    assert abs(p_sim - p_teo) * 100 <= 1.0 and por_debajo.any()
    # dia de alta simulado (distribucion) para k = 1 y 2
    res = {1: [], 2: []}
    for _ in range(4000):
        med = sig + rng.normal(0, SIG, sig.shape)
        for k in (1, 2):
            res[k].append(dia_alta(med, k) or 95)
    for k in (1, 2):
        r = np.array(res[k])
        print(f"k = {k}: dia de alta simulado: mediana = {np.median(r):.0f}; P10-P90 = {np.percentile(r,10):.0f}-{np.percentile(r,90):.0f}; altas antes del dia analitico {sig_dia} = {np.mean(r < sig_dia)*100:.1f} %")
    a1 = float(np.mean(np.array(res[1]) < sig_dia))
    a2 = float(np.mean(np.array(res[2]) < sig_dia))
    assert a2 < a1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
