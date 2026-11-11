#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C26: tratamiento de aguas grises: biorreactor de mezcla completa, filtracion y desinfeccion por concentracion por tiempo.

Consultado (pagina de la NASA sobre el ECLSS): el agua pasa por lechos de filtracion de varias etapas y un oxidador catalitico, y sensores de conductividad electrica verifican su pureza.
TODO lo numerico es ILUSTRATIVO: 20 L/dia de agua gris por persona y 4 personas, demanda de carga organica de entrada de 300 mg/L, constante de remocion de 0.5 1/h, constante de Chick-Watson
de 0.5 L/(mg min) para una desinfeccion de log10(N0/N) = k C t, eficiencia de filtro de 99 %. Biorreactor de mezcla completa: S = S0/(1 + k tau); flujo piston: S = S0 exp(-k tau);
N tanques en serie: S = S0/(1 + k tau/N)^N. Sin datos de ningun tratamiento real.
Verificacion: la integracion numerica del tanque llega al estacionario; la remocion de N tanques tiende a la del flujo piston al crecer N; el volumen escala con el caudal.
"""
from __future__ import annotations
import math
import platform
import numpy as np

S0, K = 300.0, 0.5
F_DIA = 4 * 20.0  # L/dia
F_H = F_DIA / 24.0


def s_cstr(tau):
    return S0 / (1 + K * tau)


def s_pfr(tau):
    return S0 * math.exp(-K * tau)


def s_serie(tau, n):
    return S0 / (1 + K * tau / n) ** n


def tau_objetivo(rem, f):
    return f(rem)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: parametros ILUSTRATIVOS; sin datos de un tratamiento real; la filtracion multietapa y la verificacion por conductividad son las de la pagina de la NASA (consultada)")
    R = {}
    print(f"Caudal de aguas grises: {F_DIA:.0f} L/dia = {F_H:.2f} L/h; DBO de entrada {S0:.0f} mg/L; k = {K} 1/h")
    print("Remocion objetivo y volumen necesario (V = F tau):")
    print("   remocion   tau mezcla completa [h]   V [L]   tau piston [h]   V [L]   3 tanques: tau [h]   V [L]")
    for rem in (0.80, 0.90, 0.99):
        t_c = rem / ((1 - rem) * K)
        t_p = -math.log(1 - rem) / K
        # 3 tanques en serie: (1 + K tau/3)^3 = 1/(1-rem)
        t_3 = 3 * ((1 / (1 - rem)) ** (1 / 3) - 1) / K
        print(f"   {rem:8.2f}   {t_c:21.1f}   {t_c*F_H:5.0f}   {t_p:14.1f}   {t_p*F_H:5.0f}   {t_3:18.1f}   {t_3*F_H:5.0f}")
        R[rem] = (t_c, t_c * F_H, t_p, t_p * F_H, t_3, t_3 * F_H)
        assert abs(s_cstr(t_c) - S0 * (1 - rem)) < 1e-9 and abs(s_pfr(t_p) - S0 * (1 - rem)) < 1e-9 and abs(s_serie(t_3, 3) - S0 * (1 - rem)) < 1e-9
    assert R[0.90][1] > R[0.90][5] > R[0.90][3]
    tau = 18.0
    v = F_H * tau
    s, t, dt = S0, 0.0, 0.01
    # tanque: V dS/dt = F (S0 - S) - k S V
    for _ in range(int(400 / dt)):
        s += dt * (F_H / v * (S0 - s) - K * s)
    R["s_sim"], R["s_f"], R["v18"] = s, s_cstr(tau), v
    print(f"Control: tanque de {v:.0f} L con tau = {tau:.0f} h: integracion {s:.3f} mg/L frente a {s_cstr(tau):.3f} mg/L por formula")
    assert abs(s - s_cstr(tau)) < 1e-3
    print("Remocion de N tanques en serie con el mismo tau total de 18 h:")
    for n in (1, 2, 3, 6, 20):
        print(f"   N = {n:2d}: S = {s_serie(18.0, n):7.4f} mg/L ({100*(1-s_serie(18.0, n)/S0):7.4f} % de remocion)")
    R["s1"], R["s3"], R["s20"], R["spfr"] = s_serie(18, 1), s_serie(18, 3), s_serie(18, 20), s_pfr(18)
    assert R["s1"] > R["s3"] > R["s20"] > R["spfr"]
    print(f"   flujo piston (N infinito): S = {R['spfr']:.4f} mg/L")
    print("Desinfeccion de Chick-Watson: log10(N0/N) = k C t, k = 0.5 L/(mg min):")
    print("   C [mg/L]   t para 4 log [min]   CT [mg min/L]")
    for C in (0.5, 1.0, 2.0):
        t4 = 4 / (0.5 * C)
        print(f"   {C:8.1f}   {t4:17.1f}   {C*t4:13.1f}")
    R["ct4"] = 4 / 0.5
    lrv_f = -math.log10(1 - 0.99)
    R["lrv_f"], R["lrv_tot"] = lrv_f, lrv_f + 4
    print(f"Tren: filtro de 99 % ({lrv_f:.1f} log) + desinfeccion de 4 log = {lrv_f+4:.1f} log de reduccion total")
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
