#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C20: clasificador de galaxias por concentracion y evaluacion con metricas.

Datos: ninguno observado. Poblacion SINTETICA (semilla fija): 50 % discos con indice de Sersic n ~ Normal(1,0; 0,25)
recortado a [0,5; 2] y 50 % esferoides con n ~ Normal(4,0; 0,7) recortado a [2,5; 6]; la mitad de las galaxias
son 'brillantes' (ruido de la concentracion 0,3) y la mitad 'tenues' (ruido 4,0). Valores ILUSTRATIVOS.
Modelo: concentracion C = R80/R20 de un perfil de Sersic (C09): C = (x80/x20)^n con P(2n, x_p) = p y P la gamma
incompleta regularizada; regla: esferoide si C > C_umbral (punto medio entre C(n=1) y C(n=4)).
Metricas: matriz de confusion, exactitud, precision, exhaustividad (recall) y F1.
Supuestos: perfil de Sersic puro, ruido gaussiano en C, sin polvo ni inclinacion.
Validez: demostracion de ingenieria; la clasificacion real usa imagenes y ejemplos etiquetados.
Tolerancias: 1e-9 (casos analiticos n = 1/2 y n = 1; metricas de un caso a mano), 3 sigma (estadistica).
"""
from __future__ import annotations
import math
import platform
import random
import sys


def gamma_p(a, x):
    if x <= 0:
        return 0.0
    term = 1.0 / a
    s = term
    k = 1
    while term > 1e-17 * s and k < 10000:
        term *= x / (a + k)
        s += term
        k += 1
    return s * math.exp(-x + a * math.log(x) - math.lgamma(a))


def x_p(n, p):
    lo, hi = 1e-12, 80.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if gamma_p(2 * n, mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def concentracion(n):
    return (x_p(n, 0.8) / x_p(n, 0.2)) ** n


def metricas(tp, fn, fp, tn):
    prec = tp / (tp + fp)
    rec = tp / (tp + fn)
    return {"exactitud": (tp + tn) / (tp + fn + fp + tn), "precision": prec, "recall": rec,
            "f1": 2 * prec * rec / (prec + rec)}


def evalua(muestra, umbral):
    tp = fn = fp = tn = 0
    for real, c_med in muestra:
        pred = c_med > umbral
        if real and pred:
            tp += 1
        elif real and not pred:
            fn += 1
        elif not real and pred:
            fp += 1
        else:
            tn += 1
    return tp, fn, fp, tn


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: n = 1/2 -> C = sqrt(ln 5 / ln 1,25) exacto
    assert abs(concentracion(0.5) - math.sqrt(math.log(5) / math.log(1.25))) < 1e-9
    # Prueba 2: n = 1, raices de 1 - (1+x) e^-x = p por biseccion independiente
    def raiz(p):
        lo, hi = 0.0, 40.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if 1 - (1 + mid) * math.exp(-mid) < p:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    assert abs(concentracion(1.0) - raiz(0.8) / raiz(0.2)) < 1e-9
    # Prueba 3: metricas de un caso a mano: TP = 40, FN = 10, FP = 5, TN = 45
    m = metricas(40, 10, 5, 45)
    assert abs(m["exactitud"] - 0.85) < 1e-12 and abs(m["precision"] - 40 / 45) < 1e-12 and abs(m["recall"] - 0.8) < 1e-12
    assert abs(m["f1"] - 2 * (40 / 45) * 0.8 / (40 / 45 + 0.8)) < 1e-12
    c1, c4 = concentracion(1.0), concentracion(4.0)
    umbral = 0.5 * (c1 + c4)
    rng = random.Random(2026)
    brill, tenue = [], []
    for k in range(4000):
        esf = k % 2 == 1
        if esf:
            n = min(6.0, max(2.5, rng.gauss(4.0, 0.7)))
        else:
            n = min(2.0, max(0.5, rng.gauss(1.0, 0.25)))
        bright = (k // 2) % 2 == 0
        c_med = concentracion(n) + rng.gauss(0, 0.3 if bright else 4.0)
        (brill if bright else tenue).append((esf, c_med))
    todo = brill + tenue
    r_b, r_t, r_a = metricas(*evalua(brill, umbral)), metricas(*evalua(tenue, umbral)), metricas(*evalua(todo, umbral))
    # Prueba 4: la exactitud sobre la muestra brillante sobreestima la global (sesgo de seleccion)
    assert r_b["exactitud"] > r_a["exactitud"] > r_t["exactitud"]
    n_b = len(brill)
    err = math.sqrt(r_b["exactitud"] * (1 - r_b["exactitud"]) / n_b)
    assert r_b["exactitud"] - r_a["exactitud"] > 3 * err
    print(f"C(n = 0.5) = {concentracion(0.5):.4f} ; C(n = 1) = {c1:.4f} ; C(n = 2) = {concentracion(2.0):.4f} ; C(n = 4) = {c4:.4f}")
    print(f"umbral = {umbral:.4f} ; N = {len(todo)} (brillantes {len(brill)}, tenues {len(tenue)})")
    for nombre, r, mx in (("brillantes", r_b, evalua(brill, umbral)), ("tenues", r_t, evalua(tenue, umbral)), ("todas", r_a, evalua(todo, umbral))):
        print(f"{nombre:10s}: TP={mx[0]:4d} FN={mx[1]:4d} FP={mx[2]:4d} TN={mx[3]:4d} | exactitud {r['exactitud']:.3f} precision {r['precision']:.3f} recall {r['recall']:.3f} F1 {r['f1']:.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
