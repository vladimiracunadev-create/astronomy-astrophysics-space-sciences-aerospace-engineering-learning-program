#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C09: presupuesto de perdidas, frecuencia optima y temperatura de union de un reductor SINTETICO.

Datos consultados (2026-11-10): ficha del estandar ECSS-E-ST-20C Rev.2 (solo existencia, fecha y alcance; no se leyo su texto) y tensiones de bus de 12, 28 y 50 V
con convertidores GaN del capitulo de potencia de la NASA (contexto).
ILUSTRATIVOS (sinteticos, no medidos): Vin = 28 V, Vo = 5 V, Io = 2 A, L = 22 uH, MOSFET superior Ron = 0.04 ohm, inferior Ron = 0.03 ohm, resistencia de bobina 0.03 ohm,
diodo Schottky Vf = 0.4 V, diodo de cuerpo Vf = 0.7 V, tiempo muerto 20 ns, tr = tf = 10 ns, Qg = 5 nC a 5 V, Coss = 100 pF, perdida de nucleo
0.03 W (dI/1 A)^2 (f/200 kHz)^1.5, resistencia termica union-placa 25 K/W, placa a 50 C, Tj maxima nominal 150 C y limite de derating 110 C (limite ilustrativo, NO de una norma).
Modelo: P_total(f) = P_cond + P_cond_rizado + P_sw + P_puerta + P_nucleo (+ P_diodo o P_tiempo_muerto); D de entrada ideal Vo/Vin.
Segunda via: minimo de P_total(f) por seccion aurea frente a un barrido en rejilla de 1 kHz.
Tolerancia: frecuencia optima de las dos vias con diferencia < 1 kHz.
"""
from __future__ import annotations
import math, platform

VIN, VO, IO, L = 28.0, 5.0, 2.0, 22e-6
RHS, RLS, RL, VFD, VFB = 0.04, 0.03, 0.03, 0.4, 0.7
TD, TRF, QG, VG, COSS, KCORE = 20e-9, 20e-9, 5e-9, 5.0, 100e-12, 0.03
RTH, TPLACA, TJMAX, TJDER = 25.0, 50.0, 150.0, 110.0
D = VO / VIN


def perdidas(f, sync):
    di = (VIN - VO) * D / (L * f)
    irms2 = IO ** 2 + di ** 2 / 12.0
    p_hs_cond = D * RHS * irms2
    p_ls_cond = (1.0 - D) * RLS * irms2 if sync else 0.0
    p_diodo = 0.0 if sync else (1.0 - D) * VFD * IO
    p_bobina = RL * irms2
    p_sw = 0.5 * VIN * IO * TRF * f + 0.5 * COSS * VIN ** 2 * f
    p_puerta = QG * VG * f * (2.0 if sync else 1.0)
    p_td = 2.0 * VFB * IO * TD * f if sync else 0.0
    p_nucleo = KCORE * di ** 2 * (f / 200e3) ** 1.5
    tot = p_hs_cond + p_ls_cond + p_diodo + p_bobina + p_sw + p_puerta + p_td + p_nucleo
    return dict(hs_cond=p_hs_cond, ls_cond=p_ls_cond, diodo=p_diodo, bobina=p_bobina, sw=p_sw, puerta=p_puerta, td=p_td, nucleo=p_nucleo,
                total=tot, hs=p_hs_cond + p_sw + QG * VG * f, di=di)


def aurea(fun, a, b):
    g = (math.sqrt(5.0) - 1.0) / 2.0
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(200):
        if fun(c) < fun(d):
            b = d
        else:
            a = c
        c, d = b - g * (b - a), a + g * (b - a)
    return 0.5 * (a + b)


def resultados():
    r = {}
    for nombre, sync in (("as", False), ("sy", True)):
        p = perdidas(200e3, sync)
        pout = VO * IO
        r[f"P_{nombre}"] = p
        r[f"eta_{nombre}"] = pout / (pout + p["total"])
        r[f"eta_{nombre}_pct"] = 100.0 * r[f"eta_{nombre}"]
        r[f"Tj_{nombre}"] = TPLACA + RTH * p["hs"]
    f_opt = aurea(lambda f: perdidas(f, True)["total"], 50e3, 1.0e6)
    mejor = min(range(50, 1001), key=lambda k: perdidas(k * 1e3, True)["total"])
    r["f_opt"] = f_opt
    r["f_rej"] = mejor * 1e3
    r["df"] = abs(f_opt - mejor * 1e3)
    r["P_opt"] = perdidas(f_opt, True)["total"]
    r["eta_opt_pct"] = 100.0 * VO * IO / (VO * IO + r["P_opt"])
    r["P100"], r["P500"], r["P1000"] = (perdidas(k, True)["total"] for k in (100e3, 500e3, 1e6))
    r["margen_Tj"] = TJDER - r["Tj_sy"]
    r["Tj_der"] = TJDER
    r["f_opt_kHz"] = f_opt / 1e3
    r["f_rej_kHz"] = r["f_rej"] / 1e3
    r["Pas"], r["Psy"] = r["P_as"]["total"], r["P_sy"]["total"]
    m = dict(hs="hs_cond", ls="ls_cond", dio="diodo", bob="bobina", sw="sw", pue="puerta", td="td", nuc="nucleo")
    for pre, key in (("as", "P_as"), ("sy", "P_sy")):
        for a, b in m.items():
            r[f"{pre}_{a}"] = r[key][b]
    r["D"] = D
    r["uno_menos_d"] = 1.0 - D
    r["ahorro"] = r["P_as"]["total"] - r["P_sy"]["total"]
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Reductor SINTETICO 28 V -> 5 V, 2 A, f = 200 kHz: D = {D:.4f}")
    print(" perdida [W]          asincrono   sincrono")
    for k, n in (("hs_cond", "conduccion MOSFET sup."), ("ls_cond", "conduccion MOSFET inf."), ("diodo", "diodo Schottky"), ("bobina", "resistencia bobina"),
                 ("sw", "conmutacion"), ("puerta", "puerta"), ("td", "tiempo muerto"), ("nucleo", "nucleo")):
        print(f" {n:<22} {r['P_as'][k]:9.4f}   {r['P_sy'][k]:9.4f}")
    print(f" {'TOTAL':<22} {r['P_as']['total']:9.4f}   {r['P_sy']['total']:9.4f}")
    print(f"Eficiencia: asincrono = {r['eta_as_pct']:.2f} % ; sincrono = {r['eta_sy_pct']:.2f} % ; ahorro = {r['ahorro']:.4f} W")
    print(f"Temperatura de union del MOSFET superior: asincrono = {r['Tj_as']:.2f} C ; sincrono = {r['Tj_sy']:.2f} C (limite de derating ilustrativo {TJDER:.0f} C ; nominal {TJMAX:.0f} C)")
    print(f"Frecuencia optima (sincrono): seccion aurea = {r['f_opt']/1e3:.2f} kHz ; rejilla = {r['f_rej']/1e3:.0f} kHz ; diferencia = {r['df']:.1f} Hz")
    print(f"Perdida total a 100 kHz = {r['P100']:.4f} W ; a 500 kHz = {r['P500']:.4f} W ; a 1 MHz = {r['P1000']:.4f} W ; en el optimo = {r['P_opt']:.4f} W ({r['eta_opt_pct']:.2f} %)")
    assert r["df"] < 1000.0
    assert r["P_sy"]["total"] < r["P_as"]["total"]
    assert r["Tj_sy"] < TJDER
    assert r["P_opt"] <= min(r["P100"], r["P500"], r["P1000"]) + 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
