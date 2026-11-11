#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C21: depuracion de un contaminante traza: balance de cabina, ruptura de un lecho de carbon y conversion de un catalizador.

Consultado (pagina de la NASA sobre el ECLSS): los contaminantes traza se retiran con carbon activado, un oxidador catalitico y un lecho de hidroxido de litio; el resumen OCHMO-TB-002
lista el monitoreo de trazas y el limite de contaminacion atmosferica como requisitos (V2 6023 y V2 6050), sin dar valores. TODO lo numerico es ILUSTRATIVO: contaminante generico de masa
molar indefinida, generacion de 5 mg/h en 100 m3, caudal por el lecho de 0.01 m3/s con eficiencia 0.95, lecho de 5 kg con capacidad de 0.05 g/g, constante de Yoon-Nelson de 2e-6 1/s,
catalizador con A = 1e9 1/s, Ea = 60 kJ/mol y tiempo de residencia de 0.5 s. Modelo de Yoon-Nelson: C/C0 = 1/(1 + exp(k (tau - t))), tau = W q/(Q C0).
Verificacion: el estacionario G/(eta Q) coincide con la integracion; la ruptura vale 0.5 en t = tau; la conversion es 1 - exp(-k t_res).
"""
from __future__ import annotations
import math
import platform
import numpy as np

V, G_MG_H, Q, ETA = 100.0, 5.0, 0.01, 0.95
RG = 8.314462


def integrar(g, k, t_end, dt=60.0):
    c, t = 0.0, 0.0
    for _ in range(int(t_end / dt)):
        c += dt * (g / V - k * c)
    return c


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: contaminante generico y parametros ILUSTRATIVOS; los metodos de depuracion son los de la pagina de la NASA (consultada)")
    R = {}
    g = G_MG_H / 3600.0  # mg/s
    k = ETA * Q / V
    c_ss = g / (ETA * Q)
    c_int = integrar(g, k, 14 * 86400)
    R["c_ss"], R["c_int"] = c_ss, c_int
    print(f"Balance de cabina: G = {G_MG_H} mg/h, caudal {Q*1e3:.0f} L/s, eficiencia {ETA}: estacionario {c_ss:.3f} mg/m3 (integracion a 14 dias: {c_int:.3f})")
    assert abs(c_int - c_ss) / c_ss < 0.01
    print(f"Tiempo de respuesta V/(eta Q) = {V/(ETA*Q)/3600:.1f} h")
    R["t_resp"] = V / (ETA * Q) / 3600
    print("Vida del lecho (balance de masa: tau = W q / (Q C0)), W = 5 kg, q = 0.05 g/g = 250 g de capacidad:")
    print("   C0 [mg/m3]   tau [dias]   t10 % [dias]   t90 % [dias]")
    W, qcap, kyn = 5000.0, 0.05, 2e-6
    res = {}
    for C0 in (0.1, 1.0, 10.0):
        tau = W * qcap * 1000.0 / (Q * C0) / 86400.0  # mg / (m3/s * mg/m3) = s -> dias
        d = math.log(9) / kyn / 86400.0
        res[C0] = (tau, tau - d, tau + d)
        print(f"   {C0:10.1f}   {tau:10.1f}   {tau-d:12.1f}   {tau+d:12.1f}")
    R["tau1"], R["t10_1"], R["tau10"] = res[1.0][0], res[1.0][1], res[10.0][0]
    tau = res[1.0][0] * 86400.0
    assert abs(1 / (1 + math.exp(kyn * (tau - tau))) - 0.5) < 1e-12
    assert res[10.0][0] < res[1.0][0] < res[0.1][0]
    print("Catalizador (conversion X = 1 - exp(-k t_res), k = A exp(-Ea/(R T)), t_res = 0.5 s):")
    print("   T [K]    k [1/s]    conversion")
    xs = {}
    for T in (330.0, 350.0, 380.0, 400.0):
        kk = 1e9 * math.exp(-60e3 / (RG * T))
        xs[T] = 1 - math.exp(-kk * 0.5)
        print(f"   {T:5.0f}   {kk:9.3f}   {xs[T]:9.5f}")
    R["x330"], R["x350"], R["x380"], R["x400"] = xs[330.0], xs[350.0], xs[380.0], xs[400.0]
    assert xs[330.0] < xs[350.0] < xs[380.0] < xs[400.0]
    # tren: lecho (eta 0.95) + catalizador a 350 K
    eta_tot = 1 - (1 - ETA) * (1 - xs[350.0])
    R["eta_tot"] = eta_tot
    print(f"Tren lecho + catalizador a 350 K: eficiencia combinada {eta_tot:.5f}; estacionario {g/(eta_tot*Q):.3f} mg/m3")
    R["c_ss_tren"] = g / (eta_tot * Q)
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
