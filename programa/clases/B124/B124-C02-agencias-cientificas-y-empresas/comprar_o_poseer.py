#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C02: comprar un servicio frente a poseer el sistema (agencia frente a empresa).

CONTENIDO EDUCATIVO: no es asesoria financiera ni de contratacion.
CONSULTADOS (2026-11-11), NASA Office of Inspector General, informe IG-20-005 (noviembre de 2019): desde 2006 la NASA compro 70 asientos
Soyuz por unos 3 900 millones de USD, incluidos 5 asientos comprados a Boeing por 373,5 millones de USD (74,7 millones por asiento);
el costo medio informado por la OIG fue 55,4 millones de USD por asiento; tras 2017, 12 asientos por unos 1 000 millones de USD, con una media
informada de 79,7 millones por asiento. Las cifras del informe son aproximadas.
SINTETICOS (ilustrativos): capex K de un sistema propio, costo marginal c, precio de servicio p, numero de asientos N, dispersion sigma.
Modelo: costo propio = K + c N ; costo de comprar = p N ; punto de equilibrio N* = K / (p - c).
Con K ~ lognormal (mediana K0, sigma): P(propio mas barato) = P(K < N (p - c)) = Phi(ln(N (p - c) / K0) / sigma).
Unidades: millones de USD (MUSD) en los datos consultados; en el modelo, MUSD sinteticos.
Tolerancias: recalculo frente al valor informado dentro del 5 %; Monte Carlo (200000 muestras, semilla 124) frente a analitico < 0.005.
"""
import math, platform, random

# consultados (OIG IG-20-005)
TOTAL_70 = 3900.0
N_70 = 70
BOEING_TOTAL, BOEING_N, BOEING_INFORMADO = 373.5, 5, 74.7
MEDIA_INFORMADA = 55.4
POST2017_TOTAL, POST2017_N, POST2017_INFORMADO = 1000.0, 12, 79.7
# sinteticos
K0, SIGMA, C, P, N = 2000.0, 0.35, 20.0, 55.0, 70


def phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def run():
    r70 = TOTAL_70 / N_70
    rb = BOEING_TOTAL / BOEING_N
    r12 = POST2017_TOTAL / POST2017_N
    nstar = K0 / (P - C)
    p_an = phi(math.log(N * (P - C) / K0) / SIGMA)
    rng = random.Random(124)
    mu = math.log(K0)
    n_mc = 200000
    ok = sum(1 for _ in range(n_mc) if math.exp(rng.gauss(mu, SIGMA)) < N * (P - C))
    p_mc = ok / n_mc
    return {"r70": r70, "e70": abs(r70 - MEDIA_INFORMADA) / MEDIA_INFORMADA, "rb": rb, "eb": abs(rb - BOEING_INFORMADO) / BOEING_INFORMADO,
            "r12": r12, "e12": abs(r12 - POST2017_INFORMADO) / POST2017_INFORMADO, "nstar": nstar, "p_an": p_an, "p_mc": p_mc,
            "dif": abs(p_an - p_mc), "costo_comprar": P * N, "costo_propio": K0 + C * N, "ahorro": P * N - (K0 + C * N), "mi": MEDIA_INFORMADA, "m12": POST2017_INFORMADO, "p_comp": 1 - p_an}


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Parte 1: precios por asiento recalculados desde NASA OIG IG-20-005 (consultado 2026-11-11; cifras aproximadas)")
    print(f"  70 asientos: {TOTAL_70:.0f} MUSD / 70 = {R['r70']:.2f} MUSD ; informado {MEDIA_INFORMADA} ; diferencia relativa {100 * R['e70']:.1f} %")
    print(f"  5 asientos Boeing: {BOEING_TOTAL} / 5 = {R['rb']:.2f} MUSD ; informado {BOEING_INFORMADO} ; diferencia relativa {100 * R['eb']:.1f} %")
    print(f"  12 asientos tras 2017: {POST2017_TOTAL:.0f} / 12 = {R['r12']:.2f} MUSD ; informado {POST2017_INFORMADO} ; diferencia relativa {100 * R['e12']:.1f} %")
    print("Parte 2: modelo SINTETICO comprar frente a poseer (MUSD sinteticos)")
    print(f"  K0 = {K0:.0f}, c = {C:.0f}, p = {P:.0f}, N = {N}, sigma = {SIGMA}")
    print(f"  costo de comprar = {R['costo_comprar']:.0f} ; costo de poseer (K0 + cN) = {R['costo_propio']:.0f} ; ahorro de poseer = {R['ahorro']:.0f}")
    print(f"  punto de equilibrio N* = {R['nstar']:.2f} asientos")
    print(f"  P(poseer mas barato) analitico = {R['p_an']:.4f} ; Monte Carlo = {R['p_mc']:.4f} ; diferencia = {R['dif']:.4f}")
    assert R["e70"] < 0.05 and R["eb"] < 0.05 and R["e12"] < 0.05
    assert R["dif"] < 0.005
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
