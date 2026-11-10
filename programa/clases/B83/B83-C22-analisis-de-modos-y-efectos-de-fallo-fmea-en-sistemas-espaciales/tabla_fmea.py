#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C22: FMEA de cinco componentes de ESTRELLA-S: RPN, probabilidad de cada modo en la mision y reevaluacion.

Datos: SINTETICOS (diez modos de fallo con severidad S, ocurrencia O y deteccion D de 1 a 10; tasas de falla de componente en FIT
(fallas por 1e9 h) y fraccion de cada modo alfa, todo inventado). Modelo: RPN = S x O x D (escala de ejemplo, no de una norma);
probabilidad de un modo en la mision p = 1 - exp(-lambda alfa t) con t = 3 anos = 26280 h. Mitigacion del ejemplo: mejorar la deteccion
D en 2 puntos en los tres modos de mayor RPN. Segunda via: RPN y probabilidades con numpy frente a bucles y serie de Taylor de
1 - exp(-x). Tolerancia: 1e-12. Sin constantes fisicas.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

T_H = 3 * 8760.0
# componente, modo, efecto, S, O, D, lambda del componente (FIT), alfa
FMEA = [("Bateria", "Cortocircuito de celda", "Perdida de bus de energia", 9, 3, 5, 2000, 0.30),
        ("Bateria", "Perdida de capacidad", "Menos energia en eclipse", 6, 5, 4, 2000, 0.70),
        ("Panel solar", "Falla de despliegue", "Potencia reducida a la mitad", 8, 3, 2, 500, 0.40),
        ("Panel solar", "Degradacion acelerada", "Margen de energia menor", 5, 4, 6, 500, 0.60),
        ("Computadora", "Latch-up por radiacion", "Perdida de control hasta reinicio", 9, 4, 3, 3000, 0.25),
        ("Computadora", "Reinicio espurio", "Interrupcion breve de la mision", 4, 6, 2, 3000, 0.75),
        ("Radio", "Falla del amplificador", "Sin bajada de datos", 7, 3, 2, 1500, 1.00),
        ("Rueda de reaccion", "Friccion creciente", "Apuntamiento degradado", 6, 5, 5, 4000, 0.60),
        ("Rueda de reaccion", "Bloqueo", "Perdida de un eje de control", 8, 2, 4, 4000, 0.40),
        ("Sensor solar", "Deriva de calibracion", "Error de actitud en modo seguro", 5, 4, 7, 800, 1.00)]


def prob(lam_fit, alfa): return 1.0 - math.exp(-lam_fit * 1e-9 * alfa * T_H)


def taylor(x, n=12):
    return sum((-1) ** (k + 1) * x ** k / math.factorial(k) for k in range(1, n + 1))


def calcular():
    rpn = [s * o * d for _, _, _, s, o, d, _, _ in FMEA]
    rpn_np = (np.array([r[3] for r in FMEA]) * np.array([r[4] for r in FMEA]) * np.array([r[5] for r in FMEA])).tolist()
    p = [prob(r[6], r[7]) for r in FMEA]
    p_t = [taylor(r[6] * 1e-9 * r[7] * T_H) for r in FMEA]
    orden = sorted(range(len(FMEA)), key=lambda i: -rpn[i])
    acum = np.cumsum([rpn[i] for i in orden]) / sum(rpn)
    n80 = int(np.searchsorted(acum, 0.8) + 1)
    top3 = orden[:3]
    rpn2 = [(s * o * max(1, d - 2) if i in top3 else s * o * d) for i, (_, _, _, s, o, d, _, _) in enumerate(FMEA)]
    sumas = {}
    for r in FMEA: sumas[r[0]] = sumas.get(r[0], 0.0) + r[7]
    alta_sev = [(FMEA[i][0] + ": " + FMEA[i][1]) for i in range(len(FMEA)) if FMEA[i][3] >= 8]
    V = dict(rpn=rpn, rpn2=rpn2, p=p, orden=orden, n=len(FMEA), rpn_total=sum(rpn), rpn_total2=sum(rpn2), n80=n80,
             mayor=f"{FMEA[orden[0]][0]}: {FMEA[orden[0]][1]}", rpn_max=rpn[orden[0]], top3=[f"{FMEA[i][0]}: {FMEA[i][1]}" for i in top3],
             dif_rpn=max(abs(a - b) for a, b in zip(rpn, rpn_np)), dif_p=max(abs(a - b) for a, b in zip(p, p_t)),
             alfa_ok=all(abs(v - 1.0) < 1e-12 for v in sumas.values()), reduccion=100 * (1 - sum(rpn2) / sum(rpn)),
             p_max=max(p) * 100, p_sev8=sum(p[i] for i in range(len(FMEA)) if FMEA[i][3] >= 8) * 100, n_sev8=len(alta_sev), sev8=alta_sev,
             p_mayor_rpn=p[orden[0]] * 100, n_rpn100=sum(1 for r in rpn if r >= 100))
    return V


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 10 modos de fallo; RPN = S x O x D; p = 1 - exp(-lambda alfa t), t = 26280 h (3 anos)")
    print(f"{'#':>2s} {'componente':18s} {'modo':26s} {'S':>2s} {'O':>2s} {'D':>2s} {'RPN':>4s} {'p [%]':>7s}")
    for i, (r, rp, p) in enumerate(zip(FMEA, V["rpn"], V["p"]), 1):
        print(f"{i:2d} {r[0]:18s} {r[1]:26s} {r[3]:2d} {r[4]:2d} {r[5]:2d} {rp:4d} {p*100:7.3f}")
    print(f"RPN total = {V['rpn_total']} ; mayor RPN = {V['rpn_max']} ({V['mayor']}) ; modos con RPN >= 100: {V['n_rpn100']}")
    print(f"Modos que suman el 80 % del RPN: {V['n80']} de {V['n']}")
    print(f"Mitigacion (D - 2 en {', '.join(V['top3'])}): RPN total {V['rpn_total']} -> {V['rpn_total2']} ({V['reduccion']:.1f} % menos)")
    print(f"Modos de severidad >= 8: {V['n_sev8']} ; suma de sus probabilidades = {V['p_sev8']:.3f} % ; probabilidad maxima = {V['p_max']:.3f} %")
    print(f"Diferencias entre vias: RPN {V['dif_rpn']:.1e} ; probabilidad {V['dif_p']:.1e}")
    comprobar(V["dif_rpn"] == 0 and V["dif_p"] < 1e-12, "dos vias de RPN y de probabilidad")
    comprobar(V["alfa_ok"], "las fracciones de modo suman 1 por componente")
    comprobar(V["rpn_total2"] < V["rpn_total"], "mitigar reduce el RPN total")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
