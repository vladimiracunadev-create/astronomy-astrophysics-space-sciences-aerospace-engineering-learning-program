#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C20: respuesta institucional a un incidente espacial SINTETICO: simulacion de tiempos por etapa, secuencial y con etapas en paralelo.

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11): art. XI del tratado de 1967 (nota legal.un.org): informar a la ONU, al publico y a la comunidad cientifica en la mayor medida posible; Convenio de Registro (UNOOSA),
art. VI: ayuda para identificar objetos causantes de dano. NO consultado: ningun protocolo institucional real.
SINTETICO: cinco etapas con tiempos exponenciales (medias en horas): deteccion 2, notificacion interna 1, coordinacion 6, decision 3, comunicacion 1 (media total 13 h).
Variante paralela: la coordinacion (media 6 h) y la evaluacion juridica (media 5 h) se hacen a la vez; el tiempo de la fase es el maximo de ambas.
Formulas: E[suma] = suma de medias; para dos exponenciales de medias a y b, E[max] = a + b - ab/(a+b). Semilla 119; N = 200000; tolerancia: 3 errores estandar.
"""
import json, math, platform, random, statistics

rng = random.Random(119)
N = 200000
MEDIAS = {"deteccion": 2.0, "notificacion": 1.0, "coordinacion": 6.0, "decision": 3.0, "comunicacion": 1.0}
JUR = 5.0
def exp_(m): return rng.expovariate(1.0 / m)
sec, par = [], []
for _ in range(N):
    base = exp_(2.0) + exp_(1.0)
    fin = exp_(3.0) + exp_(1.0)
    c, j = exp_(6.0), exp_(JUR)
    sec.append(base + c + j + fin)           # secuencial: coordinacion y luego evaluacion juridica
    par.append(base + max(c, j) + fin)
def resumen(x):
    x = sorted(x)
    return statistics.mean(x), x[int(0.5 * len(x))], x[int(0.9 * len(x))], x[int(0.95 * len(x))]
rs, rp = resumen(sec), resumen(par)
esp_sec = sum(MEDIAS.values()) + JUR
esp_par = 2 + 1 + (6 + JUR - 6 * JUR / (6 + JUR)) + 3 + 1
se_s = statistics.stdev(sec) / math.sqrt(N); se_p = statistics.stdev(par) / math.sqrt(N)
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Etapas SINTETICAS con tiempos exponenciales; art. XI y art. VI (Registro) consultados 2026-11-11; ningun protocolo real consultado.")
print("               media [h]  mediana  p90    p95   media analitica")
print(f"secuencial    {rs[0]:8.2f} {rs[1]:8.2f} {rs[2]:6.2f} {rs[3]:6.2f}   {esp_sec:8.2f}")
print(f"en paralelo   {rp[0]:8.2f} {rp[1]:8.2f} {rp[2]:6.2f} {rp[3]:6.2f}   {esp_par:8.2f}")
assert abs(rs[0] - esp_sec) < 3 * se_s and abs(rp[0] - esp_par) < 3 * se_p
ahorro = rs[0] - rp[0]
print(f"Ahorro medio por paralelizar la evaluacion juridica: {ahorro:.2f} h ({100 * ahorro / rs[0]:.1f} %)")
# probabilidad de comunicar dentro de 24 h
p24s = sum(1 for t in sec if t <= 24) / N; p24p = sum(1 for t in par if t <= 24) / N
print(f"P(comunicar en 24 h): secuencial {p24s:.4f} ; paralelo {p24p:.4f}")
print("CLAVES " + json.dumps({"ms": "%.2f" % rs[0], "mp": "%.2f" % rp[0], "p95s": "%.1f" % rs[3], "p95p": "%.1f" % rp[3], "ah": "%.2f" % ahorro, "ahp": "%.1f" % (100 * ahorro / rs[0]), "a24s": "%.3f" % p24s, "a24p": "%.3f" % p24p, "es": "%.2f" % esp_sec, "ep": "%.2f" % esp_par}))
print("Pruebas superadas.")
