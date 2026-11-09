#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C09: asignacion de tolerancias que minimiza el costo para un presupuesto de frente de onda.

Datos: ninguna constante fisica consultada. Las sensibilidades (ondas RMS por unidad de tolerancia), los coeficientes de costo (a/delta) y el objetivo de 0.05 ondas RMS son ILUSTRATIVOS
(sinteticos); no corresponden a ningun instrumento ni proveedor.
Modelo: el error de frente de onda del parametro i, con tolerancia uniforme +-delta_i, tiene RMS s_i delta_i / sqrt(3); el total es la suma cuadratica. Costo C = sum a_i / delta_i.
Minimizacion con restriccion por multiplicadores de Lagrange: delta_i proporcional a (a_i / s_i^2)^(1/3). Segunda via: busqueda aleatoria con semilla 20261109 por transferencias de presupuesto.
Comprobacion del RMS resultante con Monte Carlo (200 000 ensayos).
Supuestos: respuesta lineal y errores independientes de media cero. Validez: ilustrativa.
Tolerancia: optimo analitico frente a la busqueda 1e-3 relativo; igualdad de a_i / (s_i^2 delta_i^3) a 1e-9; RMS de Monte Carlo a 0.5 %.
"""
from __future__ import annotations
import math, platform, random

NOMBRES = ["descentramiento de L1 [mm]", "inclinacion de L2 [mrad]", "espesor de L1 [mm]", "separacion L1-L2 [mm]", "radio de la cara 3 [franjas]"]
S = [2.0, 0.5, 1.2, 0.25, 0.8]   # ondas RMS por unidad (ilustrativo)
A = [1.0, 4.0, 2.0, 0.5, 3.0]    # costo * unidad (ilustrativo)
W0 = 0.05                        # ondas RMS objetivo


def rms_total(d):
    return math.sqrt(sum((s * x / math.sqrt(3.0)) ** 2 for s, x in zip(S, d)))


def costo(d):
    return sum(a / x for a, x in zip(A, d))


def reescalar(d):
    k = W0 / rms_total(d)
    return [x * k for x in d]


def calcular():
    n = len(S)
    # asignacion igual: cada parametro aporta W0 / sqrt(n)
    d_eq = [W0 / math.sqrt(n) * math.sqrt(3.0) / s for s in S]
    # Lagrange
    d_op = reescalar([(a / s**2) ** (1.0 / 3.0) for a, s in zip(A, S)])
    invariante = [a / (s**2 * x**3) for a, s, x in zip(A, S, d_op)]
    # busqueda aleatoria por transferencias (segunda via)
    rng = random.Random(20261109)
    d = d_eq[:]
    c = costo(d)
    paso = 0.2
    for it in range(60000):
        i, j = rng.randrange(n), rng.randrange(n)
        if i == j:
            continue
        q = d[:]
        q[i] *= 1 + paso * rng.uniform(-1, 1)
        q = reescalar(q)
        cq = costo(q)
        if cq < c:
            d, c = q, cq
        if it % 15000 == 14999:
            paso *= 0.3
    # Monte Carlo del RMS realizado
    N = 200000
    acc = 0.0
    for _ in range(N):
        w = sum(s * rng.uniform(-x, x) for s, x in zip(S, d_op))
        acc += w * w
    rms_mc = math.sqrt(acc / N)
    return dict(d_eq=d_eq, d_op=d_op, c_eq=costo(d_eq), c_op=costo(d_op), c_busq=c, inv=invariante, rms_mc=rms_mc, d_busq=d)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Objetivo: {W0} ondas RMS (suma cuadratica); costo C = suma de a_i / delta_i")
    print(f"{'parametro':>30} {'s_i':>6} {'a_i':>6} {'delta igual':>12} {'delta optima':>13}")
    for nm, s, a, de, do in zip(NOMBRES, S, A, r["d_eq"], r["d_op"]):
        print(f"{nm:>30} {s:6.2f} {a:6.2f} {de:12.5f} {do:13.5f}")
    print(f"RMS con asignacion igual = {rms_total(r['d_eq']):.5f} ; con la optima = {rms_total(r['d_op']):.5f} ondas")
    print(f"Costo con asignacion igual = {r['c_eq']:.4f} ; optimo analitico = {r['c_op']:.4f} ; busqueda aleatoria = {r['c_busq']:.4f}")
    print(f"Ahorro del optimo frente a la asignacion igual = {100 * (1 - r['c_op'] / r['c_eq']):.2f} %")
    print("Invariante de Lagrange a_i / (s_i^2 delta_i^3): " + " ; ".join(f"{x:.6f}" for x in r["inv"]))
    print(f"RMS por Monte Carlo (200 000 ensayos, uniformes) = {r['rms_mc']:.5f} ondas")
    assert abs(rms_total(r["d_op"]) - W0) < 1e-12
    assert max(r["inv"]) - min(r["inv"]) < 1e-9
    assert r["c_op"] < r["c_eq"]
    assert abs(r["c_busq"] - r["c_op"]) / r["c_op"] < 1e-3 and r["c_busq"] >= r["c_op"] - 1e-9
    assert abs(r["rms_mc"] / W0 - 1.0) < 0.005
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
