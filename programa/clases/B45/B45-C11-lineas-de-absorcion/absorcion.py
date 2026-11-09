#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C11: profundidad optica, ancho equivalente y curva de crecimiento de una linea gaussiana.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): radio clasico del electron r_e = 2,8179403205e-15 m. La fuerza de oscilador f = 0,64, la longitud de onda de 589 nm y las
columnas de densidad son ILUSTRATIVAS (no se consultaron valores atomicos de laboratorio).
Modelo: perfil de profundidad optica tau(x) = tau0 exp(-x^2) con x = (lambda - lambda0)/b; W_x = integral (1 - exp(-tau(x))) dx; limite lineal W = sqrt(pi) tau0 b; W = pi r_e N f lambda^2 en el regimen lineal.
Supuestos: ensanchamiento gaussiano puro (sin alas de amortiguamiento), una sola componente, sin ensanchamiento instrumental. Validez: el regimen saturado depende en la realidad de las alas de Voigt.
Tolerancia: W/(sqrt(pi) tau0) = 1 - tau0/(2 sqrt 2) a 1e-4 para tau0 = 0,01 y a 2 % de 1 para tau0 = 0,05; columna recuperada en el regimen lineal a 1 %; limite 2 sqrt(ln tau0) con error relativo menor que 10 % para tau0 = 1e4.
"""
from __future__ import annotations
import math, platform, sys

RE = 2.8179403205e-15
LAM = 589e-9
F_OSC = 0.64


def ancho_x(tau0, xmax=9.0, n=18000):
    h = 2 * xmax / n
    s = 0.0
    for i in range(n + 1):
        x = -xmax + i * h
        v = -math.expm1(-tau0 * math.exp(-x * x))
        s += v * (1 if i in (0, n) else (4 if i % 2 else 2))
    return s * h / 3


def calcular():
    r = {}
    r["tabla"] = []
    for t in (0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0, 100.0, 1000.0, 10000.0):
        w = ancho_x(t)
        lin = math.sqrt(math.pi) * t
        sat = 2 * math.sqrt(math.log(t)) if t > 1 else float("nan")
        r["tabla"].append((t, w, lin, w / lin, sat))
    # doblete 2:1
    r["doblete"] = []
    for t in (0.01, 0.1, 1.0, 10.0, 100.0):
        r["doblete"].append((t, ancho_x(2 * t) / ancho_x(t)))
    r["transm_centro"] = [(t, math.exp(-t)) for t in (0.1, 1.0, 3.0)]
    # columna de densidad desde el regimen lineal
    N_true = 5e15                                    # m^-2 (5e11 cm^-2)
    W = math.pi * RE * N_true * F_OSC * LAM ** 2     # m
    r["W_pm"] = W * 1e12
    r["W_over_lam"] = W / LAM
    N_rec = W / (math.pi * RE * F_OSC * LAM ** 2)
    r["N_ratio"] = N_rec / N_true
    # tau0 equivalente con b = 3 pm (broadening ilustrativo)
    b = 3e-12
    r["tau0"] = W / (math.sqrt(math.pi) * b)
    r["N_critica"] = N_true / r["tau0"]   # columna con tau0 = 1
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"{'tau0':>8} {'W/b':>9} {'lineal sqrt(pi)tau0':>20} {'W/lineal':>9} {'2 sqrt(ln tau0)':>16}")
    for t, w, lin, q, sat in r["tabla"]:
        print(f"{t:8.2f} {w:9.5f} {lin:20.5f} {q:9.4f} {sat:16.4f}")
    print("cociente de anchos del doblete 2:1 (W fuerte / W debil):")
    for t, q in r["doblete"]:
        print(f"  tau0 debil = {t:6.2f} -> {q:.4f}")
    print("transmision en el centro:", ", ".join(f"tau0 {t} -> {v:.4f}" for t, v in r["transm_centro"]))
    print(f"N = 5e15 m^-2 con f = 0,64 a 589 nm: W = {r['W_pm']:.4f} pm (W/lambda = {r['W_over_lam']:.3e}) ; N recuperada/N = {r['N_ratio']:.6f}")
    print(f"con b = 3 pm: tau0 = {r['tau0']:.4f} ; columna para tau0 = 1: {r['N_critica']:.3e} m^-2")
    t = {x[0]: x for x in r["tabla"]}
    assert abs(t[0.01][3] - (1 - 0.01 / (2 * math.sqrt(2)))) < 1e-4 and abs(t[0.05][3] - 1) < 0.02
    assert abs(t[10000.0][1] / t[10000.0][4] - 1) < 0.10
    assert abs(r["doblete"][0][1] - 2) < 0.02 and r["doblete"][-1][1] < 1.3
    assert abs(r["N_ratio"] - 1) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
