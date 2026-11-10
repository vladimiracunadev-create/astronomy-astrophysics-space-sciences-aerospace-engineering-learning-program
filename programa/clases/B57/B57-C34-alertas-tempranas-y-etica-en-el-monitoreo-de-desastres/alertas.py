#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C34: alertas tempranas y etica: umbral de decision, falsas alarmas y valor predictivo.

Datos: SINTETICOS / ILUSTRATIVOS. Una puntuacion de deteccion distribuida N(0,1) sin evento y N(d',1) con evento (d' = 3.0), probabilidad a priori del evento por ventana de
decision 0.01, costo de una falsa alarma 1 y de una omision 100 (unidades arbitrarias), 200 000 ventanas simuladas con semilla fija 57. No describe ningun sistema de alerta real.
Modelo: regla de decision por umbral t; tasa de falsas alarmas FPR = 1 - Phi(t), tasa de deteccion TPR = 1 - Phi(t - d') ; costo esperado C(t) = c_fa (1-pi) FPR + c_om pi (1-TPR) ;
umbral optimo t* = d'/2 + ln(c_fa (1-pi)/(c_om pi))/d' ; valor predictivo positivo PPV = pi TPR/(pi TPR + (1-pi) FPR).
Validez: dos gaussianas de igual varianza. Tolerancia: umbral optimo numerico frente a analitico < 0.01 ; PPV simulado frente al analitico < 5 % relativo.
Requiere numpy.
"""
import math, platform
import numpy as np

D, PI, C_FA, C_OM = 3.0, 0.01, 1.0, 100.0


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def tasas(t):
    return 1 - phi(t), 1 - phi(t - D)  # FPR, TPR


def costo(t):
    fpr, tpr = tasas(t)
    return C_FA * (1 - PI) * fpr + C_OM * PI * (1 - tpr)


def ppv(t):
    fpr, tpr = tasas(t)
    return PI * tpr / (PI * tpr + (1 - PI) * fpr)


def calcular():
    r = {}
    r["t_ana"] = D / 2 + math.log(C_FA * (1 - PI) / (C_OM * PI)) / D
    ts = np.linspace(-1, 4, 50001)
    cs = np.array([costo(t) for t in ts])
    r["t_num"] = float(ts[np.argmin(cs)])
    r["costo_min"] = float(cs.min())
    r["t_equilibrio"] = D / 2
    for nombre, t in (("opt", r["t_ana"]), ("eq", r["t_equilibrio"]), ("alto", 2.5)):
        fpr, tpr = tasas(t)
        r[f"fpr_{nombre}"], r[f"tpr_{nombre}"], r[f"ppv_{nombre}"], r[f"costo_{nombre}"] = fpr, tpr, ppv(t), costo(t)
    rng = np.random.default_rng(57)
    n = 200000
    ev = rng.uniform(size=n) < PI
    s = np.where(ev, D, 0.0) + rng.standard_normal(n)
    alerta = s > r["t_ana"]
    r["ppv_sim"] = float((alerta & ev).sum() / alerta.sum())
    r["falsas_sim_por_ventana"] = float((alerta & ~ev).sum() / n)
    r["razon_falsas_verdaderas"] = float((alerta & ~ev).sum() / max((alerta & ev).sum(), 1))
    r["ppv_err"] = abs(r["ppv_sim"] / r["ppv_opt"] - 1)
    # alertas falsas por anio con una ventana diaria en 100 sitios
    r["falsas_anio_100"] = r["fpr_opt"] * (1 - PI) * 365 * 100
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Umbral optimo: analitico = {r['t_ana']:.4f} ; numerico = {r['t_num']:.4f} ; umbral de igual error (d'/2) = {r['t_equilibrio']:.2f}")
    for n, nombre in (("opt", "optimo"), ("eq", "d'/2"), ("alto", "2.5")):
        print(f"Umbral {nombre}: FPR = {r['fpr_'+n]*100:.3f} % ; TPR = {r['tpr_'+n]*100:.2f} % ; PPV = {r['ppv_'+n]*100:.1f} % ; costo esperado = {r['costo_'+n]:.4f}")
    print(f"Simulacion de 200000 ventanas con el umbral optimo: PPV = {r['ppv_sim']*100:.1f} % (error relativo {r['ppv_err']:.1%}) ; falsas alarmas por 1000 ventanas = {r['falsas_sim_por_ventana']*1000:.2f} ; falsas por cada alerta verdadera = {r['razon_falsas_verdaderas']:.2f}")
    print(f"Con 100 sitios y una ventana diaria: {r['falsas_anio_100']:.0f} falsas alarmas por anio con el umbral optimo")
    assert abs(r["t_num"] - r["t_ana"]) < 0.01
    assert r["ppv_err"] < 0.05
    assert r["ppv_eq"] < 0.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
