#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B102-C03: estimacion del patinaje de una rueda con odometria y una referencia independiente.

Datos consultados (2026-11-10): la pagina «Rover Components» de la mision Mars 2020 (NASA, science.nasa.gov) da un diametro de
rueda de 52.5 cm y una velocidad maxima de 152 m/h; aqui solo fijan la ESCALA del ejemplo (radio 0.2625 m, velocidad ~0.05 m/s).
ILUSTRATIVOS (sinteticos, no medidos): velocidad angular 0.2 rad/s, epoca de 20 s, ruido de la referencia visual sigma_v = 0.02 m
por epoca, patinaje verdadero como paseo aleatorio con q = (0.004)^2 por epoca desde 0.10; semilla 20261110.
Modelo: patinaje s = 1 - d_ref / d_odo con d_odo = r w dt; estimador crudo s_k = 1 - d_vo / d_odo; filtro de Kalman escalar (paseo
aleatorio) con R = (sigma_v/d_odo)^2. Sistema: distancias en m a lo largo del avance; patinaje adimensional.
Tolerancias: sin ruido el estimador recupera s con error < 1e-12; desviacion tipica cruda frente a sigma_v/d_odo dentro del 5 %;
varianza del filtro frente a la de regimen estacionario de Riccati dentro del 10 %.
"""
from __future__ import annotations
import math, platform, random

RADIO, W, DT = 0.2625, 0.2, 20.0
D_ODO = RADIO * W * DT
SIG_V = 0.02
Q = 0.004**2


def riccati_estacionaria(q, r):
    p = 1.0
    for _ in range(10000):
        pm = p + q
        p = pm * r / (pm + r)
    return p


def simula(n, rng, ruido=True):
    s = 0.10
    verdad, crudo = [], []
    for _ in range(n):
        s += rng.gauss(0.0, math.sqrt(Q))
        d_vo = D_ODO * (1.0 - s) + (rng.gauss(0.0, SIG_V) if ruido else 0.0)
        verdad.append(s)
        crudo.append(1.0 - d_vo / D_ODO)
    return verdad, crudo


def kalman(medidas, r):
    x, p = medidas[0], r
    salida = [x]
    for z in medidas[1:]:
        pm = p + Q
        k = pm / (pm + r)
        x = x + k * (z - x)
        p = (1 - k) * pm
        salida.append(x)
    return salida


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = (SIG_V / D_ODO) ** 2
    print(f"Datos SINTETICOS: d_odo por epoca = {D_ODO:.4f} m; sigma_s cruda esperada = sigma_v/d_odo = {SIG_V / D_ODO:.4f}; semilla 20261110")
    rng = random.Random(20261110)
    n = 300
    verdad, crudo = simula(n, rng)
    filtrado = kalman(crudo, r)
    # distancia recorrida
    d_true = sum(D_ODO * (1 - s) for s in verdad)
    d_odo_tot = D_ODO * n
    d_corr_crudo = sum(D_ODO * (1 - s) for s in crudo)
    d_corr_kal = sum(D_ODO * (1 - s) for s in filtrado)
    print(f"Distancia en {n} epocas: odometria sin corregir = {d_odo_tot:.2f} m ; verdadera = {d_true:.2f} m")
    print(f"  error odometria sin corregir = {d_odo_tot - d_true:+.3f} m")
    print(f"  error con patinaje crudo     = {d_corr_crudo - d_true:+.3f} m")
    print(f"  error con patinaje filtrado  = {d_corr_kal - d_true:+.3f} m")
    # Monte Carlo
    nrep, nn = 20, 2000
    se_c = se_k = 0.0
    cnt = 0
    for i in range(nrep):
        rr = random.Random(1000 + i)
        v, c = simula(nn, rr)
        k = kalman(c, r)
        for j in range(200, nn):
            se_c += (c[j] - v[j]) ** 2
            se_k += (k[j] - v[j]) ** 2
            cnt += 1
    sd_c = math.sqrt(se_c / cnt)
    mse_k = se_k / cnt
    p_ss = riccati_estacionaria(Q, r)
    print(f"Monte Carlo ({nrep} x {nn} epocas): desviacion cruda = {sd_c:.5f} ; teorica = {SIG_V / D_ODO:.5f}")
    print(f"  varianza filtrada = {mse_k:.3e} ; Riccati estacionaria = {p_ss:.3e} ; cociente = {mse_k / p_ss:.3f}")
    print(f"  mejora del error de patinaje (desviacion): {sd_c / math.sqrt(mse_k):.2f} veces")
    # sin ruido
    v0, c0 = simula(50, random.Random(7), ruido=False)
    err0 = max(abs(a - b) for a, b in zip(v0, c0))
    print(f"Sin ruido: error maximo del estimador = {err0:.2e}")
    assert err0 < 1e-12
    assert abs(sd_c / (SIG_V / D_ODO) - 1) < 0.05
    assert abs(mse_k / p_ss - 1) < 0.10
    assert abs(d_corr_kal - d_true) < abs(d_odo_tot - d_true)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
