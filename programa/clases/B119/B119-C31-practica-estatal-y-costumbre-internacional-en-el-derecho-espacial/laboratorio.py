#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C31: practica estatal y costumbre: difusion de una practica entre Estados genericos y tiempo hasta una aceptacion amplia (SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no determina si existe una norma consuetudinaria.
Texto consultado (2026-11-11): la pagina de UNOOSA del Acuerdo sobre la Luna (art. 12) y la nota de legal.un.org muestran principios cuyo alcance a Estados no partes es objeto de debate jurisprudencial y doctrinal;
esto NO se consulto. NO consultado: el Estatuto de la Corte Internacional de Justicia (art. 38), sentencias, la practica de los Estados ni la doctrina sobre costumbre; los dos elementos de la costumbre
(practica general y aceptacion como derecho, opinio juris) se mencionan como CONOCIMIENTO GENERAL no verificado en esta sesion.
Modelo (difusion tipo Bass, no consultado en una fuente concreta; verificado por comparacion estocastico vs determinista): 190 Estados genericos; un no adoptante adopta en cada periodo (ano sintetico)
con probabilidad alfa + beta f_t, donde f_t es la fraccion de adoptantes. alfa = 0.01, beta = 0.25, f_0 = 0.0. Recurrencia determinista f_{t+1} = f_t + (1 - f_t)(alfa + beta f_t).
Umbral ILUSTRATIVO de "practica general": f >= 0.75. Semilla 119; 400 corridas. Tolerancia: media estocastica de f a t = 15 anos == determinista a 0.02.
"""
import json, platform, random

N, ALFA, BETA = 190, 0.01, 0.25
UMBRAL = 0.75
def determinista(T):
    f = 0.0; out = [f]
    for _ in range(T):
        f = f + (1 - f) * (ALFA + BETA * f)
        out.append(f)
    return out
def estocastico(T, rng):
    ad = 0; out = [0.0]
    for _ in range(T):
        f = ad / N
        p = ALFA + BETA * f
        ad += sum(1 for _ in range(N - ad) if rng.random() < p)
        out.append(ad / N)
    return out
T = 30
det = determinista(T)
rng = random.Random(119)
corr = [estocastico(T, rng) for _ in range(400)]
media = [sum(c[t] for c in corr) / len(corr) for t in range(T + 1)]
print("Python", platform.python_version(), "(biblioteca estandar)")
print("190 Estados GENERICOS; practica y umbral ILUSTRATIVOS; Estatuto de la CIJ, jurisprudencia y practica estatal NO consultados (notas de UNOOSA y legal.un.org consultadas 2026-11-11).")
print(" ano   f determinista   f media (400 corridas)")
for t in (0, 5, 10, 15, 20, 30):
    print(f"{t:4d} {det[t]:14.4f} {media[t]:14.4f}")
assert abs(media[15] - det[15]) < 0.02
t_det = next(t for t, f in enumerate(det) if f >= UMBRAL)
t_sim = [next((t for t, f in enumerate(c) if f >= UMBRAL), None) for c in corr]
t_sim = [t for t in t_sim if t is not None]
t_med = sum(t_sim) / len(t_sim)
print(f"Tiempo hasta f >= {UMBRAL}: determinista {t_det} anos ; media estocastica {t_med:.2f} anos (dispersion {max(t_sim) - min(t_sim)} anos)")
# sensibilidad al efecto de imitacion beta
def tiempo(beta):
    f = 0.0
    for t in range(1, 500):
        f = f + (1 - f) * (ALFA + beta * f)
        if f >= UMBRAL: return t
    return None
for b in (0.05, 0.15, 0.25, 0.40):
    print(f"   beta = {b:.2f}: anos hasta f >= {UMBRAL}: {tiempo(b)}")
assert abs(t_med - t_det) < 1.5
print("CLAVES " + json.dumps({"td": t_det, "ts": "%.2f" % t_med, "f15": "%.4f" % det[15], "m15": "%.4f" % media[15], "t05": tiempo(0.05), "t40": tiempo(0.40), "f30": "%.4f" % det[30]}))
print("Pruebas superadas.")
