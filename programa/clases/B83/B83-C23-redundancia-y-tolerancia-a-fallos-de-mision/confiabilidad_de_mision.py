#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C23: confiabilidad de mision con redundancia activa, fria, k-de-n y asignacion de redundancia bajo presupuesto de masa.

Datos: SINTETICOS (cuatro unidades en serie de ESTRELLA-S con tasa de falla en FIT y masa inventadas; mision de 5 anos = 43800 h).
Modelo: vida exponencial R(t) = exp(-lambda t), fallas independientes. Configuraciones de una unidad: simple; paralelo activo de 2:
2R - R^2; redundancia fria de 2 con conmutador de confiabilidad Rs: R = exp(-x)(1 + Rs x) con x = lambda t; 2-de-3 con votador perfecto:
3R^2 - 2R^3. Asignacion: elegir que unidades duplicar (paralelo activo) para maximizar la confiabilidad en serie con un presupuesto de
masa de 3.0 kg. Metodo 1: voraz por ganancia de ln R por kg. Segunda via: enumeracion de los 16 subconjuntos y Monte Carlo (200000
vidas, semilla 83023) de las configuraciones de una unidad. Tolerancia Monte Carlo: 0.3 puntos porcentuales. Sin constantes fisicas.
"""
import itertools
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

T_H = 5 * 8760.0
UNIDADES = [("Computadora de a bordo", 5000.0, 1.8), ("Radio", 4000.0, 2.4), ("Rueda de reaccion", 8000.0, 1.5), ("Controlador de bateria", 2000.0, 0.6)]
RS = 0.98
PRESUPUESTO_KG = 3.0


def r_simple(x): return math.exp(-x)
def r_activo(x): r = math.exp(-x); return 2 * r - r * r
def r_frio(x, rs=RS): return math.exp(-x) * (1 + rs * x)
def r_2de3(x): r = math.exp(-x); return 3 * r * r - 2 * r ** 3


def montecarlo(x_lambda, n=200000):
    rng = np.random.default_rng(83023)
    t1 = rng.exponential(1.0 / x_lambda, n); t2 = rng.exponential(1.0 / x_lambda, n); t3 = rng.exponential(1.0 / x_lambda, n)
    mision = 1.0
    simple = (t1 > mision).mean()
    activo = (np.maximum(t1, t2) > mision).mean()
    # fria: la segunda unidad arranca al fallar la primera si el conmutador funciona (prob RS)
    conm = rng.random(n) < RS
    frio = ((t1 > mision) | (conm & (t1 + t2 > mision))).mean()
    dosde3 = ((np.sort(np.stack([t1, t2, t3]), axis=0)[1]) > mision).mean()
    return simple, activo, frio, dosde3


def asignacion():
    xs = [lam * 1e-9 * T_H for _, lam, _ in UNIDADES]
    base = math.prod(r_simple(x) for x in xs)
    # voraz
    ganancia = sorted(range(len(UNIDADES)), key=lambda i: -(math.log(r_activo(xs[i])) - math.log(r_simple(xs[i]))) / UNIDADES[i][2])
    elegidas, masa = [], 0.0
    for i in ganancia:
        if masa + UNIDADES[i][2] <= PRESUPUESTO_KG: elegidas.append(i); masa += UNIDADES[i][2]
    r_vor = math.prod(r_activo(xs[i]) if i in elegidas else r_simple(xs[i]) for i in range(len(xs)))
    # enumeracion
    mejor, mejor_s = -1.0, None
    for bits in itertools.product([0, 1], repeat=len(UNIDADES)):
        m = sum(UNIDADES[i][2] for i in range(len(bits)) if bits[i])
        if m > PRESUPUESTO_KG: continue
        r = math.prod(r_activo(xs[i]) if bits[i] else r_simple(xs[i]) for i in range(len(xs)))
        if r > mejor: mejor, mejor_s = r, bits
    return base, r_vor, [UNIDADES[i][0] for i in elegidas], masa, mejor, [UNIDADES[i][0] for i, b in enumerate(mejor_s) if b]


def calcular():
    V = {}
    lam = 8000.0; x = lam * 1e-9 * T_H
    V["x"] = x
    for k, f in (("simple", r_simple), ("activo", r_activo), ("frio", r_frio), ("dosde3", r_2de3)): V[f"R_{k}"] = 100 * f(x)
    mc = montecarlo(x)
    for k, v in zip(("simple", "activo", "frio", "dosde3"), mc): V[f"mc_{k}"] = 100 * v
    V["dif_mc"] = max(abs(V[f"R_{k}"] - V[f"mc_{k}"]) for k in ("simple", "activo", "frio", "dosde3"))
    base, r_vor, elegidas, masa, mejor, elegidas_enum = asignacion()
    V.update(R_serie=100 * base, R_vor=100 * r_vor, R_enum=100 * mejor, elegidas=elegidas, masa=masa, elegidas_enum=elegidas_enum,
             mismo=sorted(elegidas) == sorted(elegidas_enum), mejora=100 * (r_vor - base))
    # punto de cruce: 2-de-3 frente a simple (R=0.5 en x = ln 2 ... ) y rs critico para frio = activo
    V["frio_vs_activo"] = V["R_frio"] - V["R_activo"]
    V["R_simple_unidades"] = [(n, 100 * r_simple(l * 1e-9 * T_H)) for n, l, _ in UNIDADES]
    return V


def main():
    V = calcular()
    print(cabecera())
    print(f"Datos SINTETICOS: mision de 5 anos = {T_H:.0f} h ; unidad de ejemplo lambda = 8000 FIT -> x = lambda t = {V['x']:.4f} ; Rs = {RS}")
    print(f"{'configuracion':22s} {'R analitica [%]':>16s} {'R Monte Carlo [%]':>18s}")
    for k, n in (("simple", "simple"), ("activo", "paralelo activo 2"), ("frio", "fria 2 (Rs = 0.98)"), ("dosde3", "2-de-3 (votador perfecto)")):
        print(f"{n:22s} {V[f'R_{k}']:16.3f} {V[f'mc_{k}']:18.3f}")
    print("Cadena en serie de 4 unidades (R de cada una sin redundancia): " + ", ".join(f"{n} {r:.2f} %" for n, r in V["R_simple_unidades"]))
    print(f"Serie sin redundancia = {V['R_serie']:.3f} % ; con redundancia voraz (presupuesto {PRESUPUESTO_KG} kg): {V['R_vor']:.3f} % duplicando {', '.join(V['elegidas'])} ({V['masa']:.1f} kg)")
    print(f"Enumeracion exacta: {V['R_enum']:.3f} % duplicando {', '.join(V['elegidas_enum'])} ; misma eleccion: {V['mismo']} ; mejora = {V['mejora']:.3f} puntos")
    comprobar(V["dif_mc"] < 0.3, "Monte Carlo y formulas")
    comprobar(abs(V["R_vor"] - V["R_enum"]) < 1e-9 or V["R_vor"] <= V["R_enum"], "la enumeracion no es peor que el voraz")
    comprobar(V["R_activo"] > V["R_simple"] and V["R_dosde3"] > V["R_simple"], "la redundancia mejora a la simple en este rango")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
