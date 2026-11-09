#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C08: ley de decaimiento por Monte Carlo, estimacion de la constante de decaimiento y cadena de Bateman.

Datos: ninguna constante fisica externa (se usa ln 2 y el anio de 365.25 dias). Los periodos de semidesintegracion (10 dias y 3 dias), el numero de nucleos (100 000 y 1e15), la semilla
fija y el tiempo de integracion son ILUSTRATIVOS (sinteticos); no corresponden a ningun radionucleido.
Modelo: N(t) = N_0 e^(-lambda t) con lambda = ln 2/T_{1/2}; muestreo de tiempos de decaimiento exponenciales y estimador de maxima verosimilitud lambda_hat = 1/media con error relativo 1/sqrt(N);
vida media tau = T_{1/2}/ln 2; actividad A = lambda N; cadena de dos pasos dN1/dt = -lambda_1 N1, dN2/dt = lambda_1 N1 - lambda_2 N2 integrada con RK4 y comparada con la solucion de Bateman
N2(t) = lambda_1 N1(0)/(lambda_2 - lambda_1) (e^(-lambda_1 t) - e^(-lambda_2 t)) y con el equilibrio transitorio N2/N1 -> lambda_1/(lambda_2 - lambda_1).
Supuestos: decaimientos independientes, constantes de decaimiento fijas. Validez: exacta para el modelo.
Tolerancia: supervivientes dentro de 4 desviaciones tipicas binomiales; lambda_hat dentro de 4/sqrt(N); RK4 frente a Bateman a 1e-8.
"""
from __future__ import annotations
import math
import platform
import random
import sys


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    t_half = 10.0 * 86400.0
    lam = math.log(2) / t_half
    n0 = 100000
    rng = random.Random(20261109)
    tiempos = [rng.expovariate(lam) for _ in range(n0)]
    print(f"T_1/2 = 10 d ; lambda = {lam:.4e} s-1 ; vida media tau = {1 / lam / 86400:.4f} d = {t_half / math.log(2) / t_half:.4f} T_1/2")
    print(f"{'t/T_1/2':>8} {'N esperado':>11} {'N simulado':>11} {'desviacion [sigma]':>19}")
    for k in range(0, 6):
        t = k * t_half
        p = math.exp(-lam * t)
        sup = sum(1 for x in tiempos if x > t)
        sig = math.sqrt(n0 * p * (1 - p)) if 0 < p < 1 else 1.0
        print(f"{k:8d} {n0 * p:11.1f} {sup:11d} {abs(sup - n0 * p) / sig:19.2f}")
        assert abs(sup - n0 * p) < 4 * sig + 1e-9
    lam_hat = n0 / sum(tiempos)
    print(f"estimador de maxima verosimilitud: lambda_hat = {lam_hat:.4e} s-1 ; cociente con lambda = {lam_hat / lam:.5f} ; error relativo esperado 1/sqrt(N) = {1 / math.sqrt(n0):.5f}")
    assert abs(lam_hat / lam - 1) < 4 / math.sqrt(n0)
    n_at = 1e15
    print(f"actividad de {n_at:.0e} nucleos con T_1/2 = 10 d: A = lambda N = {lam * n_at:.4e} Bq")
    # Bateman
    l1, l2 = math.log(2) / (10 * 86400.0), math.log(2) / (3 * 86400.0)
    n1_0 = 1e12
    def f(y):
        return [-l1 * y[0], l1 * y[0] - l2 * y[1]]
    y, t, dt = [n1_0, 0.0], 0.0, 600.0
    print(f"{'t [d]':>6} {'N2 RK4':>14} {'N2 Bateman':>14} {'dif. relativa':>14} {'N2/N1':>9} {'l1/(l2 - l1)':>13}")
    marcas = [5, 10, 20, 40]
    pasos = int(40 * 86400 / dt)
    for i in range(1, pasos + 1):
        k1 = f(y)
        k2 = f([y[j] + 0.5 * dt * k1[j] for j in range(2)])
        k3 = f([y[j] + 0.5 * dt * k2[j] for j in range(2)])
        k4 = f([y[j] + dt * k3[j] for j in range(2)])
        y = [y[j] + dt * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j]) / 6 for j in range(2)]
        t = i * dt
        if any(abs(t - m * 86400) < dt / 2 for m in marcas):
            ana = l1 * n1_0 / (l2 - l1) * (math.exp(-l1 * t) - math.exp(-l2 * t))
            d = abs(y[1] / ana - 1)
            print(f"{t / 86400:6.1f} {y[1]:14.6e} {ana:14.6e} {d:14.2e} {y[1] / y[0]:9.4f} {l1 / (l2 - l1):13.4f}")
            assert d < 1e-8
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
