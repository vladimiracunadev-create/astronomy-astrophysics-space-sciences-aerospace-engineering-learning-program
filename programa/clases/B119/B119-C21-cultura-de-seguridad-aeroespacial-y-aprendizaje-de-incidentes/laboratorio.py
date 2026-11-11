#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C21: cultura de seguridad: curva de aprendizaje de incidentes y subnotificacion (datos SINTETICOS de una organizacion ficticia).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11): art. XI del tratado de 1967 (nota legal.un.org): informar en la mayor medida posible sobre la naturaleza, conduccion, lugares y resultados de las actividades
(parafraseado). NO consultado: ninguna norma de seguridad, informe de investigacion de accidentes ni estudio de cultura de seguridad.
Modelo (relacion de Duane / ley de potencia, no consultada en una fuente concreta; verificada por recuperacion del parametro): tasa verdadera de incidentes por unidad de exposicion
lambda(t) = lambda1 * t**(-b) con lambda1 = 12 y b = 0.30; reportes observados ~ Poisson(exposicion * lambda * r(t)), con fraccion reportada r(t) creciente de 0.35 a 0.90.
Exposicion: 100 unidades por ano, 10 anos. Semilla 119. Ajuste por minimos cuadrados en log-log.
Tolerancia: pendiente ajustada con tasa verdadera (sin ruido) == -b (1e-9); con ruido, a 0.15 de -b.
"""
import json, math, platform, random

rng = random.Random(119)
L1, B = 12.0, 0.30
ANOS = list(range(1, 11))
EXPO = 100.0
def lam(t): return L1 * t ** (-B)
def r(t): return 0.35 + (0.90 - 0.35) * (t - 1) / 9.0
def poisson(l):
    L, k, p = math.exp(-l), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L: return k
        k += 1
def ajuste(xs, ys):
    lx = [math.log(x) for x in xs]; ly = [math.log(y) for y in ys]
    n = len(xs); mx = sum(lx) / n; my = sum(ly) / n
    b = sum((a - mx) * (c - my) for a, c in zip(lx, ly)) / sum((a - mx) ** 2 for a in lx)
    return b, math.exp(my - b * mx)
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Organizacion FICTICIA, datos SINTETICOS; art. XI consultado (2026-11-11); ninguna norma ni estudio de seguridad consultado.")
verd = [EXPO / 100 * lam(t) for t in ANOS]
pend0, _ = ajuste(ANOS, verd)
assert abs(pend0 + B) < 1e-9
obs = []
print(" ano  incidentes verdaderos (esp.)  fraccion reportada  reportes observados")
for t in ANOS:
    esp = EXPO / 100 * lam(t) * 100  # incidentes esperados en el ano
    rep = poisson(esp * r(t))
    obs.append(rep)
    print(f"{t:4d} {esp:20.1f} {r(t):22.2f} {rep:20d}")
# el aprendizaje se ve mal si se mira la serie de reportes
pend_obs, _ = ajuste(ANOS, [max(o, 0.5) for o in obs])
corr = [o / r(t) for o, t in zip(obs, ANOS)]
pend_corr, _ = ajuste(ANOS, [max(c, 0.5) for c in corr])
print(f"Pendiente log-log: verdadera {pend0:.3f} ; de los reportes crudos {pend_obs:.3f} ; de los reportes corregidos por r(t) {pend_corr:.3f}")
assert abs(pend_corr + B) < 0.15
print(f"Reportes del ano 1: {obs[0]} ; del ano 10: {obs[-1]} ; incidentes verdaderos esperados {EXPO * lam(1):.0f} y {EXPO * lam(10):.0f}")
print("CLAVES " + json.dumps({"p0": "%.3f" % pend0, "po": "%.3f" % pend_obs, "pc": "%.3f" % pend_corr, "o1": obs[0], "o10": obs[-1], "v1": "%.0f" % (EXPO * lam(1)), "v10": "%.0f" % (EXPO * lam(10))}))
print("Pruebas superadas.")
