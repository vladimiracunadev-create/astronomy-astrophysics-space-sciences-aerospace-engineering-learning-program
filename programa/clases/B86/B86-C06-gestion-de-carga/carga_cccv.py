#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C06: gestion de carga (corriente constante - tension constante) de una bateria SINTETICA 8S3P.

Datos consultados (2026-11-10): GM = 0.39860e6 km3/s2 y radio medio 6371.000 km (NASA/NSSDC) para el periodo y la luz de una orbita de 600 km con beta = 0.
ILUSTRATIVOS (sinteticos, no medidos): paquete 8S3P de celdas de 3.0 Ah (9.0 Ah), OCV por celda 3.3 + 0.8 SOC [V], resistencia 0.05 ohm por celda,
tension maxima por celda 4.1 V, corriente CC de 1.0, 2.0 y 3.0 A, corte de la fase CV a 0.45 A (C/20), DoD inicial 15.54 % (resultado de B86-C05).
Modelo: fase CC hasta V = 32.8 V; fase CV a 32.8 V con I = Np (Vmax/Ns - OCV)/r; cuenta de Coulomb con paso de 1 s.
Segunda via: tiempo de la fase CC en forma cerrada (carga a reponer hasta el SOC de cambio entre la corriente) frente a la simulacion;
balance de carga integral(I dt) = variacion del SOC por la capacidad.
Tolerancia: tiempo CC cerrado frente a simulado < 1 s; balance de carga < 1e-6 Ah.
"""
from __future__ import annotations
import math, platform

NS, NP, CAP, R = 8, 3, 3.0, 0.05
C_PACK = NP * CAP
VMAX = NS * 4.1
ITAPER = 0.05 * C_PACK
SOC0 = 1.0 - 0.1554
MU, RE, H = 398600.0, 6371.0, 600.0
A = RE + H
T = 2.0 * math.pi * math.sqrt(A ** 3 / MU)
TD = T - math.asin(RE / A) / math.pi * T


def ocv(s):
    return 3.3 + 0.8 * s


def cargar(i_cc, dt=1.0, tmax=36000.0):
    s, t = SOC0, 0.0
    q = e = 0.0
    t_cc = None
    fase = "CC"
    while t < tmax:
        if fase == "CC":
            i = i_cc
            v = NS * (ocv(s) + i / NP * R)
            if v >= VMAX:
                fase, t_cc = "CV", t
                continue
        else:
            v = VMAX
            i = NP * (VMAX / NS - ocv(s)) / R
            if i <= ITAPER:
                break
        s += i * dt / (3600.0 * C_PACK)
        q += i * dt / 3600.0
        e += v * i * dt / 3600.0
        t += dt
    return dict(t=t, t_cc=t_cc if t_cc is not None else t, soc=s, q=q, e=e, fase=fase)


def t_cc_cerrado(i_cc):
    # V = NS (3.3 + 0.8 s + i R / NP) = VMAX  ->  s_cv
    s_cv = (VMAX / NS - 3.3 - i_cc * R / NP) / 0.8
    return (s_cv - SOC0) * C_PACK * 3600.0 / i_cc


def resultados():
    r = dict(Td=TD, Q_falta=(1.0 - SOC0) * C_PACK)
    for i in (1.0, 2.0, 3.0):
        c = cargar(i)
        k = int(i)
        r[f"t{k}"], r[f"tcc{k}"], r[f"q{k}"], r[f"e{k}"], r[f"s{k}"] = c["t"], c["t_cc"], c["q"], c["e"], c["soc"]
        r[f"tcc_c{k}"] = t_cc_cerrado(i)
        r[f"dtcc{k}"] = abs(c["t_cc"] - t_cc_cerrado(i))
        r[f"bal{k}"] = abs(c["q"] - (c["soc"] - SOC0) * C_PACK)
        r[f"cabe{k}"] = c["t"] <= TD
    # energia almacenada en la bateria = integral de OCV dq (Wh): NS * C_PACK * integral (3.3 + 0.8 s) ds
    r["E_alm"] = NS * C_PACK * (3.3 * (r["s1"] - SOC0) + 0.4 * (r["s1"] ** 2 - SOC0 ** 2))
    r["eta_e"] = r["E_alm"] / r["e1"]
    r["Itaper"] = ITAPER
    r["Vmax"] = VMAX
    r["frac_cc1"] = r["tcc1"] / r["t1"]
    r["frac_cc1_pct"] = 100.0 * r["frac_cc1"]
    r["eta_pct"] = 100.0 * r["eta_e"]
    r["scv2"] = (VMAX / NS - 3.3 - 2.0 * R / NP) / 0.8
    r["dq2"] = (r["scv2"] - SOC0) * C_PACK
    r["cuantas"] = TD / r["t1"]
    r["Edis"] = r["e1"] - r["E_alm"]
    r["q_restante"] = r["Q_falta"] - r["q1"]
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Paquete SINTETICO 8S3P: {C_PACK:.1f} Ah ; Vmax = {VMAX:.1f} V ; corte CV = {ITAPER:.2f} A ; luz disponible Td = {TD:.1f} s")
    print(f"Carga a reponer desde SOC = {SOC0*100:.2f} % : {r['Q_falta']:.3f} Ah")
    print(" I_CC [A]   t_CC [s]  cerrado [s]   t_total [s]   Q [Ah]   E [Wh]   cabe en la luz")
    for k in (1, 2, 3):
        print(f" {k:8.1f}  {r[f'tcc{k}']:9.1f}  {r[f'tcc_c{k}']:10.1f}  {r[f't{k}']:12.1f}  {r[f'q{k}']:7.3f}  {r[f'e{k}']:7.2f}   {'si' if r[f'cabe{k}'] else 'no'}")
    print(f"Energia almacenada (integral de OCV) con I = 1 A = {r['E_alm']:.2f} Wh ; energia de entrada = {r['e1']:.2f} Wh ; eficiencia = {r['eta_e']*100:.2f} %")
    for k in (1, 2, 3):
        assert r[f"dtcc{k}"] < 1.0, f"tiempo CC {k} A"
        assert r[f"bal{k}"] < 1e-6, f"balance de carga {k} A"
    assert r["t3"] < r["t2"] < r["t1"]
    assert 0.8 < r["eta_e"] < 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
