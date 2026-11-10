#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C06: relacion masa-impulso (empuje, gasto masico, impulso total, Isp).

Datos consultados (2026-11-10): Isp y V_eq = Isp g0 (NASA Glenn, Ideal Rocket Equation); g0 = 9.80665 m/s2 (NIST CODATA 2022).
ILUSTRATIVOS (sinteticos): perfil de empuje trapezoidal (rampa del 10 %, meseta, rampa final del 10 %) con pico F0 = 2.0 MN, Isp = 300 s, masa de propelente 60 000 kg;
coeficientes estructurales 0.06 a 0.14; Isp 250..450 s.
Sistema: magnitudes escalares, SI.
Modelo: F = mdot Isp g0; impulso total I = integral F dt = m_p Isp g0; fraccion de carga util de una etapa pi = (exp(-dv/c) - eps)/(1-eps);
dv maximo con carga nula: dv_max = c ln(1/eps).
Segunda via: integracion trapezoidal de F(t) sobre un perfil dado frente a m_p Isp g0.
Tolerancias: impulso integrado frente a m_p Isp g0 1e-9 relativa.
"""
import math, platform

G0 = 9.80665
ISP, MP, F0 = 300.0, 60000.0, 2.0e6


def mdot_perfil(t, tb):
    """Perfil trapezoidal normalizado del gasto: sube en 10 % de tb, meseta, baja en el ultimo 10 %."""
    x = t / tb
    if x < 0.1:
        return x / 0.1
    if x > 0.9:
        return (1 - x) / 0.1
    return 1.0


def calcular():
    c = ISP * G0
    r = {"c": c}
    r["I_ana"] = MP * c
    r["mdot_nom"] = F0 / c
    r["tb_nom"] = MP / r["mdot_nom"]
    # perfil trapezoidal con la misma masa de propelente: la integral de mdot_perfil vale 0.9 tb
    tb = MP / (r["mdot_nom"] * 0.9)
    n = 200000
    dt = tb / n
    imp, masa = 0.0, 0.0
    f_prev = m_prev = 0.0
    for i in range(1, n + 1):
        t = i * dt
        md = r["mdot_nom"] * mdot_perfil(t, tb)
        f = md * c
        imp += 0.5 * (f_prev + f) * dt
        masa += 0.5 * (m_prev + md) * dt
        f_prev, m_prev = f, md
    r["tb_perfil"], r["I_num"], r["m_num"] = tb, imp, masa
    r["err_I"] = abs(imp - r["I_ana"]) / r["I_ana"]
    r["err_m"] = abs(masa - MP) / MP
    r["F_pico"] = F0
    r["F_media"] = r["I_ana"] / tb
    r["tw"] = [(m0, F0 / (m0 * G0)) for m0 in (80000.0, 120000.0, 160000.0)]
    r["pi_tabla"] = []
    for isp in (250.0, 300.0, 350.0, 450.0):
        fila = []
        for eps in (0.06, 0.10, 0.14):
            cc = isp * G0
            dvmax = cc * math.log(1 / eps)
            fila.append(dvmax)
        r["pi_tabla"].append((isp, fila))
    r["pi_ej"] = (math.exp(-4000.0 / c) - 0.10) / 0.90
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Motor SINTETICO: Isp = {ISP} s (c = {r['c']:.2f} m/s), F0 = {F0/1e6} MN, m_prop = {MP:.0f} kg")
    print(f"Gasto nominal = {r['mdot_nom']:.2f} kg/s; tb nominal = {r['tb_nom']:.2f} s; impulso total analitico = {r['I_ana']/1e6:.3f} MN s")
    print(f"Perfil trapezoidal: tb = {r['tb_perfil']:.2f} s; impulso integrado = {r['I_num']/1e6:.3f} MN s; masa quemada = {r['m_num']:.3f} kg")
    print(f"Errores relativos: impulso {r['err_I']:.2e}; masa {r['err_m']:.2e}; empuje medio = {r['F_media']/1e6:.3f} MN")
    print("T/W de despegue segun masa inicial: " + "; ".join(f"{m:.0f} kg -> {t:.3f}" for m, t in r["tw"]))
    print("DV maximo con carga nula (c ln(1/eps)) [m/s]:")
    print("  Isp [s]   eps=0.06   eps=0.10   eps=0.14")
    for isp, fila in r["pi_tabla"]:
        print(f"  {isp:6.0f}   " + "   ".join(f"{d:8.0f}" for d in fila))
    print(f"Razon de carga util pi para dv = 4000 m/s, Isp = 300 s, eps = 0.10: {r['pi_ej']:.4f}")
    assert r["err_I"] < 1e-9 and r["err_m"] < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
