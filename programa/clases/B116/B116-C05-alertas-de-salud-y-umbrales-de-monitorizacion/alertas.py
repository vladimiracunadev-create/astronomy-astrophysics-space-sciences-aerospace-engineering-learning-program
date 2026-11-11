#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B116-C05: politicas de alerta (umbral, persistencia, histeresis) sobre una serie SINTETICA de 30 dias.

Todo es sintetico (semilla 120) y NO describe a ninguna persona. Serie de frecuencia cardiaca [lpm] a 1 muestra/min durante 30 dias
(43 200 muestras): base 70 lpm + ritmo circadiano de +/-5 lpm (periodo 24 h) + ruido gaussiano de 8 lpm + artefactos de movimiento
aislados (0,3 % de las muestras, +40 lpm) + 8 eventos verdaderos (+45 lpm durante 20 min, con instantes aleatorios). Politicas:
A) umbral simple: alarma en cada cruce ascendente de 100 lpm; B) persistencia: alarma cuando 5 muestras consecutivas superan 100 lpm;
C) histeresis + persistencia: alarma como B, pero queda latcheada hasta que la serie baja de 90 lpm durante 5 min (sin nuevas alarmas
mientras tanto). Una alarma es verdadera si ocurre en la ventana de un evento (inicio -2 min a fin +5 min). Resultados: alarmas/dia,
falsas alarmas/dia, eventos detectados y retardo medio de deteccion respecto al inicio del evento. De la alerta 50 de la Joint
Commission (2013; consultada 2026-11-10 solo mediante un resumen de resultados de busqueda) se cita unicamente el orden de magnitud
(85 %-99 % de las senales no requieren intervencion clinica); no se usa en el calculo. Los umbrales son ilustrativos, no clinicos. Numpy.
"""
from __future__ import annotations
import platform
import numpy as np

N = 30 * 24 * 60


def serie(rng):
    t = np.arange(N)
    x = 70 + 5 * np.sin(2 * np.pi * t / 1440) + rng.normal(0, 8, N)
    art = rng.uniform(size=N) < 0.003
    x = x + 40 * art
    inicios = np.sort(rng.choice(np.arange(500, N - 500, 20), size=8, replace=False))
    while np.any(np.diff(inicios) < 200):
        inicios = np.sort(rng.choice(np.arange(500, N - 500, 20), size=8, replace=False))
    for i in inicios:
        x[i:i + 20] += 45
    return x, inicios, int(art.sum())


def pol_a(x, umbral=100):
    s = x > umbral
    return [i for i in range(1, N) if s[i] and not s[i - 1]]


def pol_b(x, umbral=100, m=5):
    s = x > umbral
    out, run = [], 0
    for i in range(N):
        run = run + 1 if s[i] else 0
        if run == m:
            out.append(i)
    return out


def pol_c(x, hi=100, lo=90, m=5):
    s = x > hi
    out, run, lat, bajo = [], 0, False, 0
    for i in range(N):
        run = run + 1 if s[i] else 0
        if not lat and run == m:
            out.append(i)
            lat, bajo = True, 0
        elif lat:
            bajo = bajo + 1 if x[i] < lo else 0
            if bajo >= m:
                lat = False
    return out


def evaluar(alarmas, inicios):
    ventanas = [(i - 2, i + 20 + 5) for i in inicios]
    verd, falsas, retardos, detect = 0, 0, [], set()
    for a in alarmas:
        k = next((j for j, (v0, v1) in enumerate(ventanas) if v0 <= a <= v1), None)
        if k is None:
            falsas += 1
        else:
            verd += 1
            if k not in detect:
                detect.add(k)
                retardos.append(a - inicios[k])
    return len(alarmas), falsas, len(detect), (float(np.mean(retardos)) if retardos else float("nan"))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 120): serie de 30 dias simulada; los umbrales son ilustrativos, no clinicos")
    rng = np.random.default_rng(120)
    x, ini, nart = serie(rng)
    print(f"Muestras = {N}; artefactos = {nart}; eventos verdaderos = {len(ini)} (+45 lpm, 20 min)")
    print("Politica                                  alarmas  falsas  falsas/dia  eventos detectados  retardo medio [min]")
    res = {}
    for nombre, f in (("A umbral simple (>100)", pol_a), ("B persistencia 5 min", pol_b), ("C persistencia + histeresis (90)", pol_c)):
        a = f(x)
        n, fa, det, ret = evaluar(a, ini)
        res[nombre[0]] = (n, fa, det, ret)
        print(f"{nombre:40s}  {n:5d}   {fa:5d}    {fa / 30:7.2f}         {det} de 8            {ret:6.1f}")
    assert res["B"][1] < res["A"][1] and res["C"][0] <= res["B"][0]
    # control sin ruido ni artefactos: todas las politicas detectan los 8 eventos y no hay falsas alarmas
    x0 = np.full(N, 70.0)
    for i in ini:
        x0[i:i + 20] += 45
    for f in (pol_a, pol_b, pol_c):
        n, fa, det, ret = evaluar(f(x0), ini)
        assert det == 8 and fa == 0
    print("Control sin ruido ni artefactos: las tres politicas detectan 8 de 8 y 0 falsas alarmas (el retardo de B y C es de 4 min por la persistencia)")
    print("Barrido del umbral de la politica B (persistencia 5 min):")
    print("  umbral [lpm]   alarmas  falsas/dia  eventos detectados")
    for u in (90, 95, 100, 105, 110):
        n, fa, det, ret = evaluar(pol_b(x, umbral=u), ini)
        print(f"     {u:3d}        {n:5d}     {fa / 30:7.2f}        {det} de 8")
    print("Barrido de la persistencia m con umbral 100 lpm:")
    print("  m [min]   alarmas  falsas/dia  eventos detectados  retardo medio [min]")
    for m in (1, 3, 5, 8, 12):
        n, fa, det, ret = evaluar(pol_b(x, m=m), ini)
        print(f"   {m:3d}      {n:5d}     {fa / 30:7.2f}        {det} de 8            {ret:6.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
