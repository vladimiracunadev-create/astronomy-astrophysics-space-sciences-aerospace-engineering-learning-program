#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C26: lectura sistematica de doctrinas declaradas publicamente: codificacion de textos y acuerdo entre codificadores (kappa de Cohen). Textos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no analiza la doctrina de ningun Estado real.
Texto consultado (2026-11-11, nota de legal.un.org): art. IV (armas de destruccion masiva y usos pacificos) y art. XI (informar en la mayor medida posible) del tratado de 1967 como marco contra el cual
se lee una doctrina. NO consultado: ninguna doctrina, politica ni estrategia espacial publicada por ningun Estado.
Modelo: 40 "declaraciones" SINTETICAS, cada una con un tema verdadero oculto entre cuatro categorias (cooperacion, disuasion, defensa, comercio); dos codificadores sinteticos ven cada declaracion
y acierta cada uno con probabilidad 0.85 (si falla, elige otra categoria al azar). Semilla 119.
kappa = (po - pe) / (1 - pe), con po = acuerdo observado y pe = acuerdo esperado por azar segun las marginales. Verificacion: kappa tambien = 1 - (1 - po)/(1 - pe).
Intervalo por bootstrap (2000 remuestras, semilla 120).
"""
import json, platform, random

CAT = ["cooperacion", "disuasion", "defensa", "comercio"]
rng = random.Random(119)
N = 40
verdad = [rng.choice(CAT) for _ in range(N)]
def codificar(p):
    out = []
    for v in verdad:
        if rng.random() < p: out.append(v)
        else: out.append(rng.choice([c for c in CAT if c != v]))
    return out
a, b = codificar(0.85), codificar(0.85)
def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in CAT)
    k1 = (po - pe) / (1 - pe)
    k2 = 1 - (1 - po) / (1 - pe)
    assert abs(k1 - k2) < 1e-12
    return po, pe, k1
po, pe, k = kappa(a, b)
print("Python", platform.python_version(), "(biblioteca estandar)")
print("40 declaraciones SINTETICAS con tema oculto; art. IV y XI consultados (2026-11-11); ninguna doctrina real consultada.")
print("Matriz de confusion entre codificadores (filas A, columnas B):")
print("              " + "".join(f"{c[:6]:>9s}" for c in CAT))
for ca in CAT:
    print(f"{ca:12s}  " + "".join(f"{sum(1 for x, y in zip(a, b) if x == ca and y == cb):9d}" for cb in CAT))
print(f"Acuerdo observado po = {po:.3f} ; esperado por azar pe = {pe:.3f} ; kappa = {k:.3f}")
# kappa respecto de la verdad
_, _, ka = kappa(a, verdad); _, _, kb = kappa(b, verdad)
print(f"kappa de cada codificador frente a la verdad oculta: {ka:.3f} y {kb:.3f}")
# bootstrap
rb = random.Random(120)
ks = []
for _ in range(2000):
    idx = [rb.randrange(N) for _ in range(N)]
    aa = [a[i] for i in idx]; bb = [b[i] for i in idx]
    try:
        ks.append(kappa(aa, bb)[2])
    except ZeroDivisionError:
        pass
ks.sort()
lo, hi = ks[int(0.025 * len(ks))], ks[int(0.975 * len(ks))]
print(f"Intervalo bootstrap del 95 % para kappa: [{lo:.3f}, {hi:.3f}]")
assert lo <= k <= hi
# caso limite: acuerdo perfecto
assert abs(kappa(verdad, verdad)[2] - 1) < 1e-12
print("CLAVES " + json.dumps({"po": "%.3f" % po, "pe": "%.3f" % pe, "k": "%.3f" % k, "lo": "%.3f" % lo, "hi": "%.3f" % hi, "ka": "%.3f" % ka, "kb": "%.3f" % kb}))
print("Pruebas superadas.")
