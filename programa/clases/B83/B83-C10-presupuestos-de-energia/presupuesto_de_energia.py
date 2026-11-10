#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C10: presupuesto de energia orbital (eclipse, panel, bateria y profundidad de descarga).

Constantes consultadas el 2026-11-10: S0 = 1361.0 W/m2, RE y GM de NASA/NSSDC; eficiencia de celdas multiunion de 27-32 % al
inicio de vida (capitulo de energia de NASA SmallSat, S7; se usa 28 %) y bateria de ion-litio de 150-270 Wh/kg (S7).
SINTETICOS: orbita circular de 550 km, cargas por modo (reposo 45 W, toma 110 W durante 8 min por orbita, comunicaciones 40 W durante
7 min por orbita, ambas a la luz), area de panel 0.60 m2, factor de empaquetado 0.85, factor medio de coseno 0.7, degradacion 2.5 %/ano
durante 3 anos, rendimiento de regulacion 0.95, rendimiento de descarga 0.95, bateria de 150 Wh, DoD maxima 30 %. Sistema: Sol en el
plano definido por el angulo beta; sombra cilindrica. Segunda via: fraccion de eclipse por geometria numerica (paso de 1 s) frente a
la formula analitica; balance de energia por simulacion de 10 orbitas. Tolerancias: fraccion de eclipse a 2e-3.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

ETA_CELDA, EMPAQ, COSENO = 0.28, 0.85, 0.7
DEGRAD = (1 - 0.025) ** 3
AREA = 0.60
ETA_REG, ETA_DES = 0.95, 0.95
BAT_WH, DOD_MAX = 150.0, 0.30
P_REPOSO, P_TOMA, T_TOMA_MIN, P_COM, T_COM_MIN = 45.0, 110.0, 8.0, 40.0, 7.0


def eclipse_numerico(beta_deg):
    a = RE_KM + H_KM; T = periodo_s(); n = 2 * math.pi / T
    t = np.arange(0.0, T, 1.0); u = n * t
    b = math.radians(beta_deg)
    s = np.array([math.cos(b), 0.0, math.sin(b)])
    r = a * np.stack([np.cos(u), np.sin(u), np.zeros_like(u)])
    rs = s @ r
    perp2 = (r ** 2).sum(axis=0) - rs ** 2
    return float(np.mean((rs < 0) & (perp2 < RE_KM ** 2)))


def potencia_panel():
    return S0_WM2 * ETA_CELDA * EMPAQ * COSENO * DEGRAD * AREA


def balance(beta_deg):
    T_min = periodo_s() / 60.0
    fe = fraccion_eclipse(H_KM, beta_deg)
    te, ts = fe * T_min, (1 - fe) * T_min
    e_luz = P_REPOSO * ts + P_TOMA * T_TOMA_MIN + P_COM * T_COM_MIN      # W*min
    e_ecl = P_REPOSO * te
    p_sa = potencia_panel()
    gen = p_sa * ts * ETA_REG
    req = e_luz + e_ecl / (ETA_DES * ETA_REG)
    dod = (e_ecl / 60.0 / ETA_DES) / BAT_WH
    return dict(fe=fe, te=te, ts=ts, gen=gen / 60.0, req=req / 60.0, margen=100 * (gen - req) / req, dod=dod * 100, e_ecl_wh=e_ecl / 60.0)


def soc_10_orbitas(beta_deg):
    dt = 1.0; T = periodo_s(); n = 2 * math.pi / T
    t = np.arange(0.0, 10 * T, dt)
    a = RE_KM + H_KM; b = math.radians(beta_deg)
    s = np.array([math.cos(b), 0.0, math.sin(b)])
    u = n * t
    r = a * np.stack([np.cos(u), np.sin(u), np.zeros_like(u)])
    rs = s @ r
    ecl = (rs < 0) & ((r ** 2).sum(axis=0) - rs ** 2 < RE_KM ** 2)
    fase = (t % T) / 60.0
    carga = np.full_like(t, P_REPOSO)
    carga += np.where((~ecl) & (fase < T_TOMA_MIN), P_TOMA, 0.0)
    carga += np.where((~ecl) & (fase >= T_TOMA_MIN) & (fase < T_TOMA_MIN + T_COM_MIN), P_COM, 0.0)
    p_sa = np.where(ecl, 0.0, potencia_panel() * ETA_REG)
    e = BAT_WH * 3600.0                       # J almacenados
    emin, e0 = e, e
    for p, c in zip(p_sa, carga):
        neto = p - c
        e += neto * dt * (1.0 if neto >= 0 else 1.0 / ETA_DES)
        e = min(e, BAT_WH * 3600.0)
        emin = min(emin, e)
    return 100.0 * (1 - emin / (BAT_WH * 3600.0)), 100.0 * e / (BAT_WH * 3600.0)


def calcular():
    V = dict(T_min=periodo_s() / 60.0, p_sa=potencia_panel())
    for beta in (0, 30, 60, 75):
        b = balance(beta)
        for k, v in b.items(): V[f"{k}_{beta}"] = v
        V[f"fep_{beta}"] = b["fe"] * 100
    V["fe_num0"] = eclipse_numerico(0.0)
    V["fe_num60"] = eclipse_numerico(60.0)
    V["fnum0p"] = V["fe_num0"] * 100
    V["dod_sim0"], V["soc_fin0"] = soc_10_orbitas(0.0)
    V["dod_sim60"], V["soc_fin60"] = soc_10_orbitas(60.0)
    V["e_orbita"] = (P_REPOSO * V["T_min"] + P_TOMA * T_TOMA_MIN + P_COM * T_COM_MIN) / 60.0
    return V


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: orbita 550 km, panel 0.60 m2, bateria 150 Wh; S0, RE, GM de NASA/NSSDC; eficiencia de celda 28 % (rango de S7)")
    print(f"Periodo = {V['T_min']:.2f} min ; potencia del panel al final de vida = {V['p_sa']:.2f} W ; energia de carga por orbita = {V['e_orbita']:.2f} Wh")
    print(f"{'beta':>5s} {'eclipse':>8s} {'t_ecl[min]':>10s} {'gen[Wh]':>9s} {'req[Wh]':>9s} {'margen[%]':>10s} {'DoD[%]':>7s}")
    for b in (0, 30, 60, 75):
        print(f"{b:5d} {V[f'fe_{b}']*100:7.2f}% {V[f'te_{b}']:10.2f} {V[f'gen_{b}']:9.2f} {V[f'req_{b}']:9.2f} {V[f'margen_{b}']:10.2f} {V[f'dod_{b}']:7.2f}")
    print(f"Eclipse por geometria numerica: beta 0 -> {V['fe_num0']*100:.3f} % (analitico {V['fe_0']*100:.3f} %) ; beta 60 -> {V['fe_num60']*100:.3f} % (analitico {V['fe_60']*100:.3f} %)")
    print(f"Simulacion de 10 orbitas, beta 0: DoD maxima = {V['dod_sim0']:.2f} % ; carga final = {V['soc_fin0']:.2f} %")
    comprobar(abs(V["fe_num0"] - V["fe_0"]) < 2e-3 and abs(V["fe_num60"] - V["fe_60"]) < 2e-3, "fraccion de eclipse numerica y analitica")
    comprobar(V["margen_0"] > 20.0, "margen del caso de eclipse maximo mayor que 20 % (regla del ejemplo)")
    comprobar(V["dod_0"] <= DOD_MAX * 100, "DoD analitica dentro del limite")
    comprobar(V["soc_fin0"] > 99.0, "la bateria vuelve a plena carga tras 10 orbitas")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
