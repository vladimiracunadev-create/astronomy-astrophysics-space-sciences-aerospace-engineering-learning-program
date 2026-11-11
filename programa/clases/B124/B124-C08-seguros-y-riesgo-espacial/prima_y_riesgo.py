#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C08: prima, pérdida esperada y cola de pérdidas de una cartera de seguros SINTETICA, con y sin fallas en grupo.

CONTENIDO EDUCATIVO: no es asesoria de seguros, financiera ni legal. Probabilidades, valores asegurados y recargos son SINTETICOS.
Consultado (2026-11-11), texto de la ONU (UNOOSA, STSPACE11E): Tratado del Espacio de 1967, art. VII (el Estado que lanza o hace lanzar un objeto
espacial, o desde cuyo territorio se lanza, es internacionalmente responsable por el dano que cause) y Convenio sobre responsabilidad de 1972,
art. II (responsabilidad absoluta por dano en la superficie de la Tierra o a aeronaves en vuelo) y art. III (por culpa en otros casos).
Modelo: 20 satelites con valor asegurado V = 300 um cada uno; falla total con probabilidad p = 0.04 (sintetica). Prima por satelite = p V (1 + L), L = 0.35.
Caso independiente: perdida = V K, K ~ Binomial(20, p). Caso en grupo: 5 lanzamientos con 4 satelites cada uno; falla de lanzamiento con probabilidad p;
perdida = 4 V K_l, K_l ~ Binomial(5, p). Capital del asegurador = 400 um. Ruina si perdida > primas + capital.
Unidades: um (unidades monetarias sinteticas). Tolerancias: Monte Carlo (200000 carteras, semilla 124) frente a binomial exacta < 0.005 en cada probabilidad.
"""
import math, platform, random

N_SAT, V, P, LOAD, CAP = 20, 300.0, 0.04, 0.35, 400.0
N_LANZ, POR_LANZ = 5, 4


def binom_pmf(k, n, p):
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def cola(n, p, unidad, umbral):
    """P(unidad * K > umbral) exacta."""
    return sum(binom_pmf(k, n, p) for k in range(n + 1) if unidad * k > umbral)


def var99(n, p, unidad):
    acum = 0.0
    for k in range(n + 1):
        acum += binom_pmf(k, n, p)
        if acum >= 0.99:
            return unidad * k
    return unidad * n


def simular(n, p, unidad, umbral, rng, reps=200000):
    sobre, perd = 0, []
    for _ in range(reps):
        k = sum(1 for _ in range(n) if rng.random() < p)
        if unidad * k > umbral:
            sobre += 1
        perd.append(unidad * k)
    perd.sort()
    return sobre / reps, perd[int(0.99 * reps) - 1]


def run():
    prima_sat = P * V * (1 + LOAD)
    primas = N_SAT * prima_sat
    umbral = primas + CAP
    perdida_esp = N_SAT * P * V
    ruina_ind = cola(N_SAT, P, V, umbral)
    ruina_gr = cola(N_LANZ, P, POR_LANZ * V, umbral)
    rng = random.Random(124)
    mc_ind, q_ind = simular(N_SAT, P, V, umbral, rng)
    mc_gr, q_gr = simular(N_LANZ, P, POR_LANZ * V, umbral, rng)
    return {"prima_sat": prima_sat, "primas": primas, "umbral": umbral, "perdida_esp": perdida_esp, "ganancia": primas - perdida_esp,
            "ruina_ind": ruina_ind, "ruina_gr": ruina_gr, "mc_ind": mc_ind, "mc_gr": mc_gr, "dif_ind": abs(ruina_ind - mc_ind), "dif_gr": abs(ruina_gr - mc_gr),
            "var_ind": var99(N_SAT, P, V), "var_gr": var99(N_LANZ, P, POR_LANZ * V), "q_ind": q_ind, "q_gr": q_gr,
            "razon": ruina_gr / ruina_ind, "esp_gr": N_LANZ * P * POR_LANZ * V}


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Cartera SINTETICA: 20 satelites, V = 300 um, p = 0.04, recargo L = 0.35, capital = 400 um")
    print(f"Prima por satelite = {R['prima_sat']:.2f} um ; primas totales = {R['primas']:.1f} ; perdida esperada = {R['perdida_esp']:.1f} ; ganancia esperada = {R['ganancia']:.1f}")
    print(f"Ruina si perdida > primas + capital = {R['umbral']:.1f} um")
    print(f"  fallas independientes: P(ruina) exacta = {R['ruina_ind']:.4f} ; Monte Carlo = {R['mc_ind']:.4f} ; diferencia = {R['dif_ind']:.4f} ; VaR 99 % = {R['var_ind']:.0f} (MC {R['q_ind']:.0f})")
    print(f"  fallas en grupo (5 lanzamientos x 4): perdida esperada = {R['esp_gr']:.1f} ; P(ruina) exacta = {R['ruina_gr']:.4f} ; Monte Carlo = {R['mc_gr']:.4f} ; diferencia = {R['dif_gr']:.4f} ; VaR 99 % = {R['var_gr']:.0f} (MC {R['q_gr']:.0f})")
    print(f"  razon de ruina en grupo / independiente = {R['razon']:.2f}")
    assert abs(R["esp_gr"] - R["perdida_esp"]) < 1e-9
    assert R["dif_ind"] < 0.005 and R["dif_gr"] < 0.005
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
