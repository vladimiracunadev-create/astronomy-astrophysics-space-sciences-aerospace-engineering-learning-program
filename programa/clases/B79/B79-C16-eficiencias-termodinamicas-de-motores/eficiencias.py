#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C16: eficiencias termica, propulsiva y global de un turborreactor ideal y con perdidas.

Consultado (2026-11-10): NASA Glenn, Brayton (estaciones), primera ley y segunda ley (S_f > S_i si irreversible). La pagina de eficiencia termica de NASA devolvio 404: NO consultada.
ESTANDAR (no consultado): empuje especifico F/m = (1+f) Ve - V0 (presion de salida igual a la ambiente); f = (cp_h T4t - cp_c T3t)/(eta_b Q_R - cp_h T4t);
eta_term = [ (1+f) Ve^2/2 - V0^2/2 ] / (f Q_R); eta_prop = F V0 / (m [ (1+f) Ve^2/2 - V0^2/2 ]); eta_global = eta_term eta_prop = F V0 / (m_comb Q_R);
consumo especifico TSFC = f / (F/m).
ILUSTRATIVOS (sinteticos, no medidos): aire ambiente T0 = 220 K, p0 = 23000 Pa; M0 = 0.8; relacion de presiones del compresor 15; T4t = 1500 K; poder calorifico Q_R = 43 MJ/kg;
eta_b = 0.99; lado frio cp = 1004.675, gamma = 1.4; lado caliente cp = 1148, gamma = 1.333 (de texto, no consultados); R_frio = 287.05 J/(kg K).
Caso ideal: toma, compresor, turbina y tobera isentropicos, quemador sin caida de presion. Caso con perdidas: pi_d = 0.97, eta_c = 0.85, eta_t = 0.88, pi_b = 0.96, eta_n = 0.98.
Via 2: eta_global calculada por F V0/(m_comb Q_R) frente al producto eta_term eta_prop; balance de energia cinetica.
Tolerancias: producto frente a directo < 1e-12 relativa.
"""
import math, platform

T0, P0 = 220.0, 23000.0
CP_C, G_C, R_C = 1004.675, 1.4, 287.05
CP_H, G_H = 1148.0, 1.333
QR, ETA_B = 43e6, 0.99
T4T = 1500.0


def motor(M0, r, ideal):
    pi_d, eta_c, eta_t, pi_b, eta_n = (1.0, 1.0, 1.0, 1.0, 1.0) if ideal else (0.97, 0.85, 0.88, 0.96, 0.98)
    a0 = math.sqrt(G_C * R_C * T0)
    v0 = M0 * a0
    t0t = T0 * (1 + 0.5 * (G_C - 1) * M0 * M0)
    p0t = P0 * (t0t / T0) ** (G_C / (G_C - 1)) * pi_d
    kc = (G_C - 1) / G_C
    kh = (G_H - 1) / G_H
    t3t = t0t * (1 + (r ** kc - 1) / eta_c)
    p3t = p0t * r
    w_c = CP_C * (t3t - t0t)
    f = (CP_H * T4T - CP_C * t3t) / (ETA_B * QR - CP_H * T4T)
    p4t = p3t * pi_b
    w_t = w_c / (1 + f)
    t5t = T4T - w_t / CP_H
    t5ts = T4T - (T4T - t5t) / eta_t
    p5t = p4t * (t5ts / T4T) ** (1 / kh)
    if p5t <= P0:
        return None
    ve = math.sqrt(2 * eta_n * CP_H * t5t * (1 - (P0 / p5t) ** kh))
    fe = (1 + f) * ve - v0
    ek = 0.5 * (1 + f) * ve ** 2 - 0.5 * v0 ** 2
    eta_th = ek / (f * QR)
    eta_p = fe * v0 / ek
    eta_o = fe * v0 / (f * QR)
    tsfc = f / fe
    return dict(v0=v0, f=f, ve=ve, fe=fe, eth=eta_th, ep=eta_p, eo=eta_o, tsfc=tsfc, t3t=t3t, t5t=t5t, p5t=p5t)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Turborreactor ILUSTRATIVO: T0 = {T0} K, p0 = {P0:.0f} Pa, r = 15, T4t = {T4T} K, Q_R = {QR / 1e6:.0f} MJ/kg")
    peor = 0.0
    print("Caso               M0     V0 [m/s]  f        Ve [m/s]   F/m [N s/kg]  eta_term  eta_prop  eta_global  TSFC [mg/(N s)]")
    for ideal in (True, False):
        for M0 in (0.0, 0.5, 0.8, 1.2, 2.0):
            d = motor(M0, 15.0, ideal)
            peor = max(peor, abs(d["eth"] * d["ep"] - d["eo"]))
            nombre = "ideal" if ideal else "con perdidas"
            tsfc = f"{d['tsfc'] * 1e6:10.2f}" if d["v0"] > 0 else "       n/a"
            print(f"{nombre:13s}   {M0:4.1f}   {d['v0']:7.1f}  {d['f']:.5f}  {d['ve']:8.1f}   {d['fe']:9.1f}    {d['eth']:.4f}    {d['ep']:.4f}    {d['eo']:.4f}    {tsfc}")
    print(f"Diferencia maxima |eta_term eta_prop - eta_global| = {peor:.2e}")
    # barrido de r a M0 = 0.8 con perdidas
    print("Barrido de r (M0 = 0.8, con perdidas)")
    print("    r    F/m [N s/kg]  TSFC [mg/(N s)]  eta_term  eta_global")
    mejor_f, r_f, mejor_s, r_s = -1.0, 0.0, 1e9, 0.0
    r = 4.0
    while r <= 40.0:
        d = motor(0.8, r, False)
        if d is not None:
            if d["fe"] > mejor_f:
                mejor_f, r_f = d["fe"], r
            if d["tsfc"] < mejor_s:
                mejor_s, r_s = d["tsfc"], r
        r += 0.05
    for r in (5.0, 10.0, 15.0, 25.0, 35.0):
        d = motor(0.8, r, False)
        print(f" {r:4.0f}    {d['fe']:9.1f}      {d['tsfc'] * 1e6:8.2f}        {d['eth']:.4f}    {d['eo']:.4f}")
    print(f"Empuje especifico maximo {mejor_f:.1f} N s/kg en r = {r_f:.2f} ; TSFC minimo del barrido {mejor_s * 1e6:.2f} mg/(N s) en r = {r_s:.2f} (borde del barrido)")
    # relacion de la eficiencia propulsiva con Ve/V0 (jet simple, f -> 0): eta_p = 2/(1 + Ve/V0)
    d = motor(0.8, 15.0, True)
    ep_s = 2 * d["v0"] / (d["ve"] + d["v0"])
    print(f"Aproximacion eta_prop = 2 V0/(Ve + V0) (f -> 0), ideal M0 = 0.8: {ep_s:.4f} frente a {d['ep']:.4f}")
    assert peor < 1e-12
    assert 0.0 < motor(0.8, 15.0, False)["eo"] < motor(0.8, 15.0, True)["eo"] < 1.0
    assert abs(ep_s - d["ep"]) < 0.01
    print("Pruebas superadas.")


main()
