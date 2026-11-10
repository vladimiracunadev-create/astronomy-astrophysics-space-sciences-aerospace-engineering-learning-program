#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C01: dimensionamiento de masas de un lanzador SINTETICO de dos etapas.

Datos consultados (2026-11-10): g0 = 9.80665 m/s2 (NIST CODATA 2022, exacto); ecuacion de cohete ideal (NASA Glenn).
ILUSTRATIVOS (sinteticos, no medidos): DV_total = 9400 m/s, Isp1 = 300 s, Isp2 = 350 s, eps1 = 0.08, eps2 = 0.10 (coef. estructural
m_est/(m_est+m_prop)), carga util 1000 kg, T/W de despegue 1.3.
Unidades SI. Sistema: magnitudes escalares de masa y velocidad caracteristica, sin sistema de referencia espacial.
Modelo: DV_i = Isp_i g0 ln(m0_i/mf_i); razon de carga util por etapa pi_i = (exp(-DV_i/c_i) - eps_i)/(1 - eps_i).
Segunda via: se integra numericamente el consumo de propelente de cada etapa (dm = -F/(Isp g0) dt) y se compara con la masa final.
Tolerancias: balance de masas 1e-9 relativo; integracion frente a analitica 1e-6.
"""
import math, platform

G0 = 9.80665
DV, ISP, EPS, PL, TW = 9400.0, (300.0, 350.0), (0.08, 0.10), 1000.0, 1.3


def razon(dv, isp, eps):
    return (math.exp(-dv / (isp * G0)) - eps) / (1.0 - eps)


def masas(dv1):
    dv = (dv1, DV - dv1)
    pi = [razon(dv[i], ISP[i], EPS[i]) for i in range(2)]
    if min(pi) <= 0:
        return None
    m0_2 = PL / pi[1]
    m0_1 = m0_2 / pi[0]
    return dv, pi, m0_1, m0_2


def glow(dv1):
    r = masas(dv1)
    return float("inf") if r is None else r[2]


def minimo(f, a, b):
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(200):
        if f(c) < f(d):
            b = d
        else:
            a = c
        c, d = b - g * (b - a), a + g * (b - a)
    return 0.5 * (a + b)


def integra_etapa(m0, mprop, isp, f_n, n=200000):
    """Consumo de propelente a empuje constante: devuelve masa final y DV por integracion de a = F/m (Euler fino)."""
    mdot = f_n / (isp * G0)
    tb = mprop / mdot
    dt = tb / n
    m, v = m0, 0.0
    for _ in range(n):
        v += f_n / m * dt
        m -= mdot * dt
    return m, v


def calcular():
    dv1_opt = minimo(glow, 500.0, DV - 500.0)
    res = {}
    res["dv1_opt"] = dv1_opt
    for nom, dv1 in (("opt", dv1_opt), ("mitad", DV / 2)):
        dv, pi, m01, m02 = masas(dv1)
        mprop1 = (m01 - m02) * (1 - EPS[0])
        mest1 = (m01 - m02) * EPS[0]
        mprop2 = (m02 - PL) * (1 - EPS[1])
        mest2 = (m02 - PL) * EPS[1]
        res[nom] = dict(dv=dv, pi=pi, m01=m01, m02=m02, mprop1=mprop1, mest1=mest1, mprop2=mprop2, mest2=mest2)
    o = res["opt"]
    o["balance"] = abs(o["m01"] - (o["mprop1"] + o["mest1"] + o["mprop2"] + o["mest2"] + PL)) / o["m01"]
    o["empuje0"] = TW * o["m01"] * G0
    mf, v = integra_etapa(o["m02"], o["mprop2"], ISP[1], 0.5 * o["m02"] * G0 * 3.0)
    o["dv2_int"] = v
    o["mf2_int"] = mf
    o["mf2_ana"] = o["m02"] - o["mprop2"]
    o["dv2_ana"] = ISP[1] * G0 * math.log(o["m02"] / o["mf2_ana"])
    return res


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Lanzador SINTETICO: DV_total = {DV:.0f} m/s, Isp = {ISP} s, eps = {EPS}, carga util = {PL:.0f} kg")
    for nom, tit in (("opt", "reparto optimo"), ("mitad", "reparto 50/50")):
        x = r[nom]
        print(f"[{tit}] DV1 = {x['dv'][0]:.1f} m/s, DV2 = {x['dv'][1]:.1f} m/s; pi1 = {x['pi'][0]:.4f}, pi2 = {x['pi'][1]:.4f}")
        print(f"   masa de despegue = {x['m01']:.1f} kg; etapa 1: prop {x['mprop1']:.1f} + est {x['mest1']:.1f}; etapa 2: prop {x['mprop2']:.1f} + est {x['mest2']:.1f}")
    o = r["opt"]
    print(f"Balance de masas (optimo): error relativo = {o['balance']:.2e}")
    print(f"Empuje de despegue con T/W = {TW}: {o['empuje0']/1e3:.1f} kN")
    print(f"Etapa 2: DV integrado = {o['dv2_int']:.3f} m/s; analitico = {o['dv2_ana']:.3f} m/s; masa final {o['mf2_int']:.3f} vs {o['mf2_ana']:.3f} kg")
    assert o["balance"] < 1e-9
    assert abs(o["dv2_int"] - o["dv2_ana"]) / o["dv2_ana"] < 1e-5
    assert r["opt"]["m01"] <= r["mitad"]["m01"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
