#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C08: convertidor reductor (buck) SINTETICO de 28 V a 5 V, simulado por conmutacion.

Datos consultados (2026-11-10): bus de bateria de 8.2 V con salidas reguladas de 5.0 y 3.3 V, y tensiones de 12, 28 y 50 V con convertidores GaN
(capitulo de potencia del estado del arte de naves pequenas de la NASA; solo como contexto de tensiones).
ILUSTRATIVOS (sinteticos, no medidos): Vin = 28 V, Iout = 2 A (carga resistiva 2.5 ohm), fsw = 200 kHz, L = 22 uH, C = 47 uF, Ron = 0.05 ohm,
resistencia de bobina 0.03 ohm, diodo Schottky Vf = 0.4 V, tiempos de conmutacion tr = tf = 10 ns, carga de puerta y consumo propio 0.05 W.
Modelo: CCM ideal D = Vo/Vin; dI = (Vin - Vo) D / (L f); dV = dI / (8 f C). Con perdidas resistivas Vo = D Vin - I [D Ron + (1 - D) 0 + RL] - (1 - D) Vf.
Segunda via: simulacion en el tiempo de la conmutacion (Euler semi-implicito, 1000 pasos por periodo, 800 periodos) comparada con las formulas.
Tolerancia: rizado de corriente simulado frente al analitico < 3 %; Vo simulado frente al predicho < 0.5 %.
"""
from __future__ import annotations
import math, platform

VIN, F, L, C = 28.0, 200e3, 22e-6, 47e-6
RON, RL, VF = 0.05, 0.03, 0.4
RC, TR, TF, PQ = 2.5, 10e-9, 10e-9, 0.05          # carga [ohm], tr, tf [s], consumo propio [W]


def simular(d, periodos=800, pasos=1000):
    dt = 1.0 / (F * pasos)
    il, vc = 0.0, 0.0
    log_i, log_v, i_on = [], [], 0.0
    for k in range(periodos * pasos):
        on = (k % pasos) < d * pasos
        if on:
            vl = VIN - il * (RON + RL) - vc
        else:
            vl = -VF - il * RL - vc
        il += vl / L * dt
        if not on and il < 0.0:
            il = 0.0
        vc += (il - vc / RC) / C * dt
        if k >= (periodos - 40) * pasos:
            log_i.append(il)
            log_v.append(vc)
            if on:
                i_on += il
    n = len(log_i)
    return dict(i_pp=max(log_i) - min(log_i), v_pp=max(log_v) - min(log_v), v_med=sum(log_v) / n, i_med=sum(log_i) / n, i_on=i_on / n)


def vo_predicho(d, i):
    return d * VIN - i * d * RON - i * RL - (1.0 - d) * VF


def resultados():
    vo, io = 5.0, 2.0
    d_ideal = vo / VIN
    # D que da 5 V con perdidas (iteracion de punto fijo: la corriente depende de Vo)
    d = d_ideal
    for _ in range(100):
        i = vo / RC
        d = (vo + i * RL + VF) / (VIN - i * RON + VF)
    i = vo / RC
    d_ideal_di = (VIN - vo) * d_ideal / (L * F)
    di_ana = (VIN - vo) * d / (L * F)
    dv_ana = di_ana / (8.0 * F * C)
    s = simular(d)
    vo_pred = vo_predicho(d, s["i_med"])
    vo_pred_i = vo_predicho(d, s["v_med"] / RC)
    # perdidas
    i_rms2 = s["i_med"] ** 2 + di_ana ** 2 / 12.0
    p_cond = d * RON * i_rms2 + RL * i_rms2
    p_diodo = (1.0 - d) * VF * s["i_med"]
    p_sw = 0.5 * VIN * s["i_med"] * (TR + TF) * F
    p_out = s["v_med"] * s["i_med"]
    p_loss = p_cond + p_diodo + p_sw + PQ
    eta = p_out / (p_out + p_loss)
    l_crit = (1.0 - d) * RC / (2.0 * F)
    return dict(D_ideal=d_ideal, D=d, dI_ana=di_ana, dI_sim=s["i_pp"], err_dI=abs(s["i_pp"] - di_ana) / di_ana * 100.0,
                dV_ana=dv_ana, dV_sim=s["v_pp"], Vo_sim=s["v_med"], Vo_pred=vo_pred_i, err_Vo=abs(s["v_med"] - vo_pred_i) / vo_pred_i * 100.0,
                Io_sim=s["i_med"], Pout=p_out, Pcond=p_cond, Pdiodo=p_diodo, Psw=p_sw, Pq=PQ, Ploss=p_loss, eta=eta, eta_pct=eta * 100.0,
                Lcrit_uH=l_crit * 1e6, dV_mV=dv_ana * 1e3, dV_sim_mV=s['v_pp'] * 1e3, dt_on_us=d / F * 1e6, dI_med=di_ana / 2.0,
                dV_med=dv_ana * 1e3 / 2.0, dI_dobl=2.0 * di_ana, Lc20=(1.0 - d) * 20.0 / (2.0 * F) * 1e6, Lcrit=l_crit, dI_ideal=d_ideal_di, Vin=VIN, Vo_ideal=d * VIN)


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Reductor SINTETICO: Vin = {VIN} V, Vo = 5 V, carga {RC} ohm, fsw = {F/1e3:.0f} kHz, L = {L*1e6:.0f} uH, C = {C*1e6:.0f} uF")
    print(f"Ciclo de trabajo ideal D = Vo/Vin = {r['D_ideal']:.4f} ; con perdidas D = {r['D']:.4f}")
    print(f"Rizado de corriente en L: analitico = {r['dI_ana']:.4f} A ; simulado = {r['dI_sim']:.4f} A ; diferencia = {r['err_dI']:.2f} %")
    print(f"Rizado de tension: analitico = {r['dV_ana']*1000:.3f} mV ; simulado = {r['dV_sim']*1000:.3f} mV")
    print(f"Tension de salida media simulada = {r['Vo_sim']:.4f} V ; predicha con perdidas = {r['Vo_pred']:.4f} V ; diferencia = {r['err_Vo']:.3f} %")
    print(f"Inductancia critica CCM/DCM = {r['Lcrit_uH']:.2f} uH (L = {L*1e6:.0f} uH: conduccion continua)")
    print(f"Perdidas: conduccion = {r['Pcond']:.4f} W ; diodo = {r['Pdiodo']:.4f} W ; conmutacion = {r['Psw']:.4f} W ; propio = {r['Pq']:.4f} W ; total = {r['Ploss']:.4f} W")
    print(f"Potencia de salida = {r['Pout']:.4f} W ; eficiencia = {r['eta_pct']:.2f} %")
    assert r["err_dI"] < 3.0
    assert r["err_Vo"] < 0.5
    assert L > r["Lcrit"]
    assert 0.8 < r["eta"] < 0.97
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
