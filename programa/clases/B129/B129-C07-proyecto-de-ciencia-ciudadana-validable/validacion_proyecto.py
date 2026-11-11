#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B129-C07: validacion de un proyecto SINTETICO de clasificacion ciudadana contra una referencia experta.

Todo SINTETICO: 1000 objetos con etiqueta experta binaria ("espiral"/"no espiral", prevalencia 0.30); voluntarios que aciertan cada voto con
probabilidad p (homogeneo p = 0.80 o heterogeneo uniforme en [0.65, 0.95], media 0.80). Los votos son independientes salvo en el escenario
con objetos DIFICILES: 10 % de los objetos engañan a todos y se acierta con probabilidad 0.50.
Voto mayoritario con n votos impares: P(correcto) = sum_{k>n/2} C(n,k) p^k (1-p)^(n-k) (via analitica). Segunda via: Monte Carlo (semilla 129).
Acuerdo con la referencia: kappa de Cohen = (po - pe)/(1 - pe) con pe calculado de las marginales; via analitica de po = P(correcto).
Tolerancias: |analitico - MC| <= 4 sigma binomial. Se resuelve el menor n impar con P >= 0.95.
Lista de comprobacion con los diez principios de la ECSA (2015): estado de un plan SINTETICO, declarado por el usuario; no se verifica automaticamente.
La semejanza con Galaxy Zoo es solo de forma: no se usan sus datos ni se afirma ningun resultado suyo.
"""
from __future__ import annotations
import math, platform, random

N_OBJ = 1000
PREV = 0.30


def p_mayoria(n, p):
    return sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n // 2 + 1, n + 1))


def kappa(po, y_exp, y_vol):
    n = len(y_exp)
    pe = 0.0
    for c in (0, 1):
        pe += (sum(1 for a in y_exp if a == c) / n) * (sum(1 for a in y_vol if a == c) / n)
    return (po - pe) / (1 - pe)


def simular(rng, y, n_votos, modo):
    """modo: 'homog', 'heter' o 'dificil'. Devuelve las etiquetas por mayoria."""
    dificil = [rng.random() < 0.10 for _ in y] if modo == "dificil" else [False] * len(y)
    out = []
    for yi, dif in zip(y, dificil):
        ok = 0
        for _ in range(n_votos):
            if modo == "heter":
                p = rng.uniform(0.65, 0.95)
            elif modo == "dificil":
                p = 0.50 if dif else 0.80
            else:
                p = 0.80
            ok += rng.random() < p
        correcto = ok > n_votos // 2
        out.append(yi if correcto else 1 - yi)
    return out


ECSA = [
    "1 participacion real", "2 resultado cientifico genuino", "3 beneficio para ambas partes", "4 participacion en varias etapas",
    "5 retroalimentacion a los participantes", "6 limites y sesgos considerados", "7 datos y metadatos abiertos (salvo privacidad)",
    "8 reconocimiento de los participantes", "9 evaluacion del programa", "10 cuestiones legales y eticas",
]


def main():
    rng = random.Random(129)
    print(f"Python {platform.python_version()} (biblioteca estandar); semilla 129")
    y = [1 if rng.random() < PREV else 0 for _ in range(N_OBJ)]
    print(f"DATOS SINTETICOS: {N_OBJ} objetos, prevalencia {sum(y) / N_OBJ:.3f}; votos independientes")
    print("1) Exactitud del voto mayoritario con p = 0.80 por voto")
    print("   n votos   P anal   P MC (homog)  dif/sigma   kappa MC   P MC (heterog)  P MC (10 % dificiles)")
    peor = 0.0
    previo = 0.0
    for n in (1, 3, 5, 7, 9, 11, 15):
        pa = p_mayoria(n, 0.80)
        yh = simular(rng, y, n, "homog")
        pm = sum(a == b for a, b in zip(y, yh)) / N_OBJ
        sig = math.sqrt(pa * (1 - pa) / N_OBJ)
        z = abs(pa - pm) / max(sig, 1e-9)
        peor = max(peor, z)
        kp = kappa(pm, y, yh)
        ye = simular(rng, y, n, "heter")
        pe = sum(a == b for a, b in zip(y, ye)) / N_OBJ
        yd = simular(rng, y, n, "dificil")
        pd = sum(a == b for a, b in zip(y, yd)) / N_OBJ
        print(f"   {n:7d}   {pa:.4f}   {pm:.3f}        {z:7.2f}     {kp:.3f}     {pe:.3f}           {pd:.3f}")
        assert z <= 4.0
        assert pa >= previo
        previo = pa
    # menor n con P >= 0.95
    n_min = next(n for n in range(1, 99, 2) if p_mayoria(n, 0.80) >= 0.95)
    print(f"2) Menor n impar con P(correcto) >= 0.95 y p = 0.80: n = {n_min} (P = {p_mayoria(n_min, 0.80):.4f})")
    # techo con objetos dificiles: P_inf = 0.9*1 + 0.1*0.5 en el limite de n -> infinito
    techo = 0.9 * 1.0 + 0.1 * 0.5
    print(f"   Con 10 % de objetos dificiles (p = 0.50) la exactitud no pasa de {techo:.3f} por muchos votos que se pidan")
    assert abs(p_mayoria(101, 0.80) - 1.0) < 1e-6
    # kappa analitico para n = 5, homogeneo
    pa5 = p_mayoria(5, 0.80)
    pe5 = PREV * PREV + (1 - PREV) * (1 - PREV)  # marginales iguales en el limite
    # marginales de voluntarios: P(vol=1) = PREV*pa + (1-PREV)*(1-pa)
    pv1 = PREV * pa5 + (1 - PREV) * (1 - pa5)
    pe5 = PREV * pv1 + (1 - PREV) * (1 - pv1)
    print(f"3) kappa analitico con n = 5: po = {pa5:.4f}, pe = {pe5:.4f}, kappa = {(pa5 - pe5) / (1 - pe5):.4f}")
    # 4) lista ECSA de un plan sintetico (estado declarado)
    plan = {0: True, 1: True, 2: True, 3: False, 4: True, 5: True, 6: True, 7: True, 8: False, 9: True}
    print("4) Lista de comprobacion ECSA (2015) del plan SINTETICO (estado declarado por quien disena, no verificado):")
    for i, nombre in enumerate(ECSA):
        print(f"   [{'x' if plan[i] else ' '}] {nombre}")
    print(f"   Cumplidos: {sum(plan.values())}/10; pendientes: " + ", ".join(ECSA[i] for i, v in plan.items() if not v))
    print(f"Maxima desviacion MC-analitico = {peor:.2f} sigma. Pruebas superadas.")


if __name__ == "__main__":
    main()
