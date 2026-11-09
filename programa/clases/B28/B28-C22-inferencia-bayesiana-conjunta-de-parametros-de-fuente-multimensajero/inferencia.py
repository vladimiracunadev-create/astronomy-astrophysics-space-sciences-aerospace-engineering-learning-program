#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C22: inferencia bayesiana conjunta de distancia e inclinacion (ondas gravitacionales + medida electromagnetica).

Datos: ninguna constante fisica. Contexto: GW170817 se observo a 40 (+8, -8) Mpc con una contrapartida identificada (arXiv:1710.05833,
resumen) y su distancia permitio una medicion de la constante de Hubble como sirena estandar (arXiv:1710.05835, resumen, consultados
2026-11-09). Todos los numeros del laboratorio (distancia verdadera de 40 Mpc, inclinacion de 0.4 rad, errores del 10 % en la amplitud y de
0.1 rad en la inclinacion, rangos y rejillas) son ILUSTRATIVOS (sinteticos); no se usa ningun valor de la constante de Hubble.
Modelo: la amplitud gravitacional observada es A = A0 F(iota)/d con F(iota) = sqrt(((1 + c^2)/2)^2 + c^2)/sqrt(2), c = cos(iota) (F = 1 de
frente, 0.354 de canto); verosimilitud gaussiana en A con error relativo del 10 %; la medida electromagnetica de la inclinacion es
gaussiana (iota_obs, 0.1 rad). Priors: p(d) ~ d^2 en [10, 100] Mpc y cos(iota) uniforme en [0, 1]. Posterior sobre rejilla (d, cos iota).
Verificaciones: (1) normalizacion y convergencia al duplicar la rejilla; (2) calibracion: en 300 ensayos con verdad extraida del prior, el
intervalo creible central del 68 % de la distancia contiene la verdad el 68 % de las veces (con y sin la medida electromagnetica).
Supuestos: amplitud unica, errores gaussianos conocidos, sin correlaciones con otros parametros. Validez: ilustrativa.
Tolerancia: mediana de d estable a 1 % al duplicar la rejilla; cobertura entre 0.60 y 0.76.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

A0 = 1.0


def F(c):
    return math.sqrt(((1 + c * c) / 2) ** 2 + c * c) / math.sqrt(2)


def rejilla(nd, nc):
    ds = [10 + 90 * (i + 0.5) / nd for i in range(nd)]
    cs = [(j + 0.5) / nc for j in range(nc)]
    return ds, cs


def posterior(a_obs, iota_obs, usar_em, ds, cs, sig_rel=0.1, sig_i=0.1):
    p = []
    for d in ds:
        fila = []
        for c in cs:
            a_mod = A0 * F(c) / d
            ll = -0.5 * ((a_obs - a_mod) / (sig_rel * a_obs)) ** 2
            if usar_em:
                ll += -0.5 * ((math.acos(c) - iota_obs) / sig_i) ** 2
            fila.append(d * d * math.exp(ll))
        p.append(fila)
    s = sum(sum(f) for f in p)
    return [[x / s for x in f] for f in p]


def marginal_d(p):
    return [sum(f) for f in p]


def cuantil(ds, m, q):
    acum = 0.0
    for d, w in zip(ds, m):
        acum += w
        if acum >= q:
            return d
    return ds[-1]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"F(0) = {F(1.0):.4f} (de frente) ; F(90 grados) = {F(0.0):.4f} (de canto) ; cociente de amplitudes = {F(1.0) / F(0.0):.3f}")
    d_v, i_v = 40.0, 0.4
    a_obs = A0 * F(math.cos(i_v)) / d_v
    ds, cs = rejilla(300, 300)
    for etiqueta, em in (("solo ondas gravitacionales", False), ("ondas gravitacionales + inclinacion electromagnetica", True)):
        p = posterior(a_obs, i_v, em, ds, cs)
        assert abs(sum(sum(f) for f in p) - 1) < 1e-12, "normalizacion"
        m = marginal_d(p)
        med, lo, hi = cuantil(ds, m, 0.5), cuantil(ds, m, 0.16), cuantil(ds, m, 0.84)
        ds2, cs2 = rejilla(600, 600)
        m2 = marginal_d(posterior(a_obs, i_v, em, ds2, cs2))
        med2 = cuantil(ds2, m2, 0.5)
        assert abs(med / med2 - 1) < 0.01, "convergencia de la rejilla"
        print(f"{etiqueta}: d = {med:.1f} (+{hi - med:.1f}, -{med - lo:.1f}) Mpc ; intervalo 68 % de ancho relativo {(hi - lo) / med / 2 * 100:.1f} % (rejilla doble: {med2:.1f})")
    # calibracion
    rng = random.Random(20261109)
    ds, cs = rejilla(120, 120)
    cob = {False: 0, True: 0}
    anchos = {False: [], True: []}
    n = 300
    for _ in range(n):
        d_t = (10 ** 3 + (100 ** 3 - 10 ** 3) * rng.random()) ** (1 / 3)      # p(d) ~ d^2 en [10, 100]
        c_t = rng.random()
        a_t = A0 * F(c_t) / d_t
        a_o = a_t * (1 + 0.1 * rng.gauss(0, 1))
        i_o = math.acos(c_t) + 0.1 * rng.gauss(0, 1)
        for em in (False, True):
            m = marginal_d(posterior(a_o, i_o, em, ds, cs))
            lo, hi = cuantil(ds, m, 0.16), cuantil(ds, m, 0.84)
            anchos[em].append(hi - lo)
            if lo <= d_t <= hi:
                cob[em] += 1
    for em, nombre in ((False, "solo GW"), (True, "GW + EM")):
        c = cob[em] / n
        print(f"calibracion {nombre}: el intervalo central del 68 % contiene la verdad el {c * 100:.1f} % de las veces ({n} ensayos) ; ancho mediano = {statistics.median(anchos[em]):.1f} Mpc")
        assert 0.60 <= c <= 0.76, f"cobertura {nombre}"
    print(f"mejora del ancho mediano con la medida electromagnetica: {statistics.median(anchos[False]) / statistics.median(anchos[True]):.2f} veces")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
