#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C17: normas humanitarias y objetos de doble uso: clasificacion bajo incertidumbre con presuncion protectora (SINTETICO, analitico).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera. No es una guia de seleccion de objetivos ni de operaciones.
Texto consultado (2026-11-11, nota de legal.un.org): art. III del Tratado del Espacio Ultraterrestre: las actividades se realizan conforme al derecho internacional, incluida la Carta de las Naciones Unidas.
NO consultado: los Convenios de Ginebra, sus Protocolos, el Manual de Tallin ni la practica de los Estados; cualquier referencia a ellos (distincion, proporcionalidad, precaucion, presuncion de caracter civil
en caso de duda) es conocimiento general NO verificado en esta sesion.
Modelo: poblacion SINTETICA de 100000 objetos de doble uso, 90 % de uso civil y 10 % de uso militar (prior ilustrativo); un indicador observable con distribucion normal:
civil N(0,1), militar N(2,1). Regla: se trata como "uso militar" solo si P(militar | x) >= t. Semilla 119.
Coste ilustrativo de error: tratar como militar un objeto civil (dano a civiles) = 10; no identificar un objeto militar = 1. Umbral optimo de Bayes: t* = c_FP / (c_FP + c_FN).
Tolerancia: umbral optimo numerico == analitico dentro de la rejilla de 0.001.
"""
import json, math, platform, random

PRIOR_M = 0.10
MU_C, MU_M, SD = 0.0, 2.0, 1.0
C_FP, C_FN = 10.0, 1.0
def pdf(x, mu):
    return math.exp(-0.5 * ((x - mu) / SD) ** 2) / (SD * math.sqrt(2 * math.pi))
def post_m(x):
    a = PRIOR_M * pdf(x, MU_M); b = (1 - PRIOR_M) * pdf(x, MU_C)
    return a / (a + b)
t_opt = C_FP / (C_FP + C_FN)
rng = random.Random(119)
N = 100000
datos = []
for _ in range(N):
    militar = rng.random() < PRIOR_M
    x = rng.gauss(MU_M if militar else MU_C, SD)
    datos.append((militar, x))
def evaluar(t):
    tp = fp = fn = tn = 0
    for m, x in datos:
        pred = post_m(x) >= t
        if m and pred: tp += 1
        elif m: fn += 1
        elif pred: fp += 1
        else: tn += 1
    return tp, fp, fn, tn
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Poblacion SINTETICA (10 % militar); art. III consultado (2026-11-11); Convenios de Ginebra y Protocolos NO consultados.")
print(f"Umbral optimo de Bayes t* = c_FP/(c_FP+c_FN) = {t_opt:.4f}")
print("   t      TP     FP     FN      TN    coste total   civiles tratados como militares")
mejor = None
for t in (0.30, 0.50, 0.80, t_opt, 0.95):
    tp, fp, fn, tn = evaluar(t)
    coste = C_FP * fp + C_FN * fn
    print(f"{t:6.3f} {tp:6d} {fp:6d} {fn:6d} {tn:7d} {coste:12.0f} {100 * fp / (fp + tn):10.3f} %")
    if mejor is None or coste < mejor[0]: mejor = (coste, t)
# busqueda numerica en rejilla del umbral
mejor_num = min(((C_FP * evaluar(t)[1] + C_FN * evaluar(t)[2], t) for t in [0.5 + 0.02 * i for i in range(0, 25)]))
print(f"Mejor umbral en rejilla gruesa (0.50 a 0.98): {mejor_num[1]:.2f} con coste {mejor_num[0]:.0f}")
assert abs(mejor_num[1] - t_opt) <= 0.02 + 1e-9
tp, fp, fn, tn = evaluar(t_opt)
prec = tp / (tp + fp); rec = tp / (tp + fn)
print(f"En t*: precision {prec:.3f} ; exhaustividad {rec:.3f} ; falsos positivos {fp}")
print("CLAVES " + json.dumps({"t": "%.4f" % t_opt, "prec": "%.3f" % prec, "rec": "%.3f" % rec, "fp": fp, "fn": fn, "mejor": "%.2f" % mejor_num[1]}))
print("Pruebas superadas.")
