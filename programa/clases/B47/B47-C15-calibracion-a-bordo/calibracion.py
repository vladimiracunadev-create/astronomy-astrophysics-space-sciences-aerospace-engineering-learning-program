#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C15: calibracion a bordo, curva de transferencia de fotones (PTC), ganancia, ruido de lectura y correccion de campo plano.

Datos: ninguna constante fisica de una fuente. TODO es SINTETICO (semilla 20261109) y ILUSTRATIVO: ganancia verdadera K = 2,0 e-/DN, ruido de lectura 5,0 e-, nivel de bias 500 DN,
no uniformidad de respuesta pixel a pixel (PRNU) de 1 %, matriz de 4900 pixeles, niveles de iluminacion de 50 a 40000 e-. No es un detector real.
Modelo: (1) cada pixel de un campo plano cuenta Poisson(g_i mu) (aproximacion normal si mu > 200) mas ruido de lectura gaussiano, dividido por K y sumado al bias; (2) par de tramas por nivel:
varianza = var(f1 - f2)/2 y media = media(f1) - bias; (3) recta var = media/K + (sigma_r/K)^2 por minimos cuadrados ponderados con 1/var^2 -> K y sigma_r; (4) mapa de ganancia relativa a partir de
N_f tramas planas promediadas y residuo de la correccion frente a la prediccion sqrt(1/(N_f mu)).
Supuestos: respuesta lineal, sin ruido de patron fijo adicional, sin corriente de oscuridad ni saturacion. Validez: sintetica, solo ejercita el metodo.
Tolerancia: K y sigma_r recuperados a 5 % y 10 % (error estadistico de una varianza con 4900 pixeles: 2 %); residuo de la correccion de campo plano a 10 % de la prediccion.
"""
from __future__ import annotations
import math, platform, random

K_TRUE, RN, BIAS, PRNU = 2.0, 5.0, 500.0, 0.01
NPIX = 4900


def poisson(rng, mu):
    if mu > 200:
        return max(0.0, rng.gauss(mu, math.sqrt(mu)))
    l, k, p = math.exp(-mu), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1


def trama(rng, mu, gains):
    return [BIAS + (poisson(rng, g * mu) + rng.gauss(0, RN)) / K_TRUE for g in gains]


def media(x):
    return sum(x) / len(x)


def var(x):
    m = media(x)
    return sum((v - m) ** 2 for v in x) / (len(x) - 1)


def calc():
    rng = random.Random(20261109)
    gains = [1 + PRNU * rng.gauss(0, 1) for _ in range(NPIX)]
    r = {"ptc": []}
    for mu in (50, 200, 1000, 4000, 10000, 20000, 40000):
        f1, f2 = trama(rng, mu, gains), trama(rng, mu, gains)
        m = media(f1) - BIAS
        v = var([a - b for a, b in zip(f1, f2)]) / 2
        r["ptc"].append((mu, m, v))
    xs = [m for _, m, _ in r["ptc"]]
    ys = [v for _, _, v in r["ptc"]]
    w = [1 / y ** 2 for y in ys]                      # pesos: error relativo igual en cada nivel
    sw = sum(w)
    mx = sum(wi * x for wi, x in zip(w, xs)) / sw
    my = sum(wi * y for wi, y in zip(w, ys)) / sw
    a = sum(wi * (x - mx) * (y - my) for wi, x, y in zip(w, xs, ys)) / sum(wi * (x - mx) ** 2 for wi, x in zip(w, xs))
    b = my - a * mx
    r["pend"], r["orig"] = a, b
    r["K"] = 1 / a
    r["rn"] = (1 / a) * math.sqrt(max(b, 0))
    # campo plano: mapa de ganancias relativo y residuo
    nf, mu_f = 16, 20000
    acum = [0.0] * NPIX
    for _ in range(nf):
        f = trama(rng, mu_f, gains)
        for i, v in enumerate(f):
            acum[i] += (v - BIAS)
    mapa = [v / nf for v in acum]
    mm = media(mapa)
    rel = [v / mm for v in mapa]
    ciencia = trama(rng, mu_f, gains)
    sin = [(v - BIAS) for v in ciencia]
    con = [(v - BIAS) / g for v, g in zip(ciencia, rel)]
    def rms_rel(x):
        return math.sqrt(var(x)) / media(x)
    r["rms_sin"], r["rms_con"] = rms_rel(sin), rms_rel(con)
    mu_dn = mu_f / K_TRUE
    r["foton"] = math.sqrt(1 / mu_f + (RN / K_TRUE / mu_dn) ** 2 / 1.0)
    r["pred"] = math.sqrt(r["foton"] ** 2 * (1 + 1 / nf))
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'mu [e-]':>9} {'media [DN]':>11} {'varianza [DN2]':>15}")
    for mu, m, v in r["ptc"]:
        print(f"{mu:9d} {m:11.2f} {v:15.3f}")
    print(f"pendiente = {r['pend']:.5f} DN-1 ; ordenada = {r['orig']:.4f} DN2")
    print(f"ganancia recuperada K = {r['K']:.4f} e-/DN (verdadera {K_TRUE}) ; ruido de lectura = {r['rn']:.3f} e- (verdadero {RN})")
    print(f"dispersion relativa del campo plano a 20000 e-: sin corregir = {r['rms_sin']*100:.4f} % ; corregida = {r['rms_con']*100:.4f} %")
    print(f"ruido de fotones y lectura esperado (1 trama) = {r['foton']*100:.4f} % ; con ruido del mapa (N_f = 16) = {r['pred']*100:.4f} %")
    assert abs(r["K"] - K_TRUE) / K_TRUE < 0.05
    assert abs(r["rn"] - RN) / RN < 0.10
    assert abs(r["rms_con"] - r["pred"]) / r["pred"] < 0.10
    assert r["rms_con"] < r["rms_sin"] * 0.7
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
