#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C05: crecimiento de un embrion por acrecion de planetesimales, enfoque gravitacional y masa de aislamiento.

Datos consultados el 2026-11-09: G de NIST (CODATA 2022); (GM)_sol y (GM)_Tierra nominales de la IAU 2015 (Resolucion B3).
La unidad astronomica (1.495978707e11 m) NO se consulto en esta sesion.
Datos ILUSTRATIVOS (sinteticos): a = 1 ua; densidad superficial de solidos Sigma_p = 50 kg/m^2; densidad de los cuerpos 2000 kg/m^3;
velocidad relativa v_rel = 1 m/s (regimen frio) ; ancho de la zona de alimentacion b = 10 R_H (coeficiente no consultado).
Sistema de referencia: orbita circular a 1 ua de una estrella de (GM)_sol; SI.
Modelo: dM/dt = pi R^2 Sigma_p Omega F_g, F_g = 1 + (v_esc/v_rel)^2, R = (3M/(4 pi rho))^(1/3) (coeficiente de orden uno ILUSTRATIVO).
Via 1: soluciones analiticas de los limites (geometrico: M^(1/3) lineal en t; enfoque dominante: M^(-1/3) lineal en t, con explosion en tiempo finito).
Via 2: integracion RK4 con paso adaptativo. Masa de aislamiento: cierre analitico frente a biseccion.
Tolerancias: ODE frente a analitico 1e-5 relativo; masa de aislamiento 1e-9.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
GM = 1.3271244e20
GM_T = 3.986004e14
MSOL, MT = GM / G, GM_T / G
UA = 1.495978707e11
ANIO = 365.25 * 86400.0
A_UA, SIGMA_P, RHO, V_REL, B_H = 1.0, 50.0, 2000.0, 1.0, 10.0
OM = math.sqrt(GM / (A_UA * UA) ** 3)
K_R = (3.0 / (4.0 * math.pi * RHO)) ** (1.0 / 3.0)


def radio(M): return K_R * M ** (1.0 / 3.0)
def v_esc2(M): return 2.0 * G * M / radio(M)


def tasa_geom(M): return math.pi * radio(M) ** 2 * SIGMA_P * OM
def tasa_foco(M): return tasa_geom(M) * v_esc2(M) / V_REL ** 2
def tasa_total(M): return tasa_geom(M) * (1.0 + v_esc2(M) / V_REL ** 2)


def integrar(f, M0, M_fin):
    """RK4 con paso adaptativo h = 1e-3 M/(dM/dt); devuelve el tiempo en que M alcanza M_fin."""
    M, t = M0, 0.0
    while M < M_fin:
        h = 1e-3 * M / f(M)
        k1 = f(M); k2 = f(M + 0.5 * h * k1); k3 = f(M + 0.5 * h * k2); k4 = f(M + h * k3)
        Mn = M + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if Mn >= M_fin:
            t += h * (M_fin - M) / (Mn - M)
            M = M_fin
        else:
            M, t = Mn, t + h
    return t


def masa_aislamiento():
    cerrada = (2.0 * math.pi * (A_UA * UA) ** 2 * SIGMA_P * B_H) ** 1.5 / math.sqrt(3.0 * MSOL)
    f = lambda M: M - 2.0 * math.pi * (A_UA * UA) * SIGMA_P * B_H * (A_UA * UA) * (M / (3.0 * MSOL)) ** (1.0 / 3.0)
    a, b = 1e15, 1e27
    for _ in range(300):
        c = math.sqrt(a * b)
        if f(c) > 0: b = c
        else: a = c
    return cerrada, math.sqrt(a * b)


def calcular():
    M0 = 1e18
    A = math.pi * K_R ** 2 * SIGMA_P * OM
    Mf_g = 1e19
    # geometrico: dM/dt = A M^(2/3) => M^(1/3) = M0^(1/3) + A t / 3
    t_g_an = 3.0 * (Mf_g ** (1 / 3) - M0 ** (1 / 3)) / A
    t_g_num = integrar(tasa_geom, M0, Mf_g)
    # enfoque dominante: dM/dt = C M^(4/3), C = 2 pi G Sigma Omega K_R / v^2
    C = 2.0 * math.pi * G * SIGMA_P * OM * K_R / V_REL ** 2
    Mf_f = 1e24
    t_f_an = 3.0 * (M0 ** (-1 / 3) - Mf_f ** (-1 / 3)) / C
    t_f_num = integrar(tasa_foco, M0, Mf_f)
    t_blow = 3.0 * M0 ** (-1 / 3) / C
    t_tot_num = integrar(tasa_total, M0, Mf_f)
    ci, bi = masa_aislamiento()
    return dict(M0=M0, A=A, C=C, t_g_an=t_g_an, t_g_num=t_g_num, t_f_an=t_f_an, t_f_num=t_f_num, t_blow=t_blow,
                t_tot=t_tot_num, mf_g=Mf_g, mf_f=Mf_f, ciso=ci, biso=bi, fg0=1 + v_esc2(M0) / V_REL ** 2, rM0=radio(M0), ve0=math.sqrt(v_esc2(M0)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Embrion ilustrativo a {A_UA} ua: M0 = {r['M0']:.1e} kg ; R0 = {r['rM0'] / 1e3:.1f} km ; v_esc = {r['ve0']:.1f} m/s ; F_g inicial = {r['fg0']:.0f}")
    print(f"Limite geometrico: t(M0 -> {r['mf_g']:.0e} kg) analitico = {r['t_g_an'] / ANIO:.4f} anios ; RK4 = {r['t_g_num'] / ANIO:.4f} anios ; dif. rel. = {abs(r['t_g_num'] / r['t_g_an'] - 1):.1e}")
    print(f"Limite de enfoque: t(M0 -> {r['mf_f']:.0e} kg) analitico = {r['t_f_an'] / ANIO:.2f} anios ; RK4 = {r['t_f_num'] / ANIO:.2f} anios ; dif. rel. = {abs(r['t_f_num'] / r['t_f_an'] - 1):.1e}")
    print(f"Tiempo de explosion (masa infinita) del limite de enfoque = {r['t_blow'] / ANIO:.2f} anios")
    print(f"Modelo completo (1 + enfoque): t(M0 -> {r['mf_f']:.0e} kg) = {r['t_tot'] / ANIO:.2f} anios")
    print(f"Masa de aislamiento (b = {B_H:.0f} R_H): cerrada = {r['ciso']:.4e} kg = {r['ciso'] / MT:.4f} M_Tierra ; biseccion = {r['biso']:.4e} kg ; dif. rel. = {abs(r['biso'] / r['ciso'] - 1):.1e}")
    assert abs(r["t_g_num"] / r["t_g_an"] - 1) < 1e-5
    assert abs(r["t_f_num"] / r["t_f_an"] - 1) < 1e-5
    assert abs(r["biso"] / r["ciso"] - 1) < 1e-9
    assert r["t_f_an"] < r["t_blow"] and r["t_tot"] <= r["t_f_an"] and r["t_tot"] > 0.98 * r["t_f_an"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
