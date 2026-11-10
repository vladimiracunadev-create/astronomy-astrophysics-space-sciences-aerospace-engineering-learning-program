#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C24: diseno PD del control de actitud por vector de empuje (TVC) de un lanzador SINTETICO.

Datos consultados (2026-11-10): criterio de estabilidad (NASA Glenn, Rocket Stability): un par restaurador estabiliza, un par desestabilizador amplifica el desplazamiento.
La literatura de control de lanzadores NO se consulto.
SINTETICOS / ILUSTRATIVOS (inventados): los del lanzador de C23 (mu_a = 0.9277 1/s2 con el centro de presion delante del de gravedad, mu_c = 21.333 1/s2),
actuador ideal salvo limites: deflexion maxima 0.6 grados y velocidad maxima de 3 grados/s (limites inventados y pequenos para que la saturacion aparezca) en el caso 'con limites'; especificacion: wn = 1.5 rad/s y zeta = 0.7.
Sistema: plano de cabeceo, theta = actitud (rad); comando theta_c; delta = deflexion de la tobera; coeficientes congelados; SI.
Modelo: theta'' = mu_a theta + mu_c delta; delta = Kp (theta_c - theta) - Kd theta'. Lazo cerrado: theta'' + mu_c Kd theta' + (mu_c Kp - mu_a) theta = mu_c Kp theta_c.
Diseno: Kp = (wn^2 + mu_a)/mu_c; Kd = 2 zeta wn/mu_c.
Segunda via: sobreimpulso y tiempo de pico de un sistema de segundo orden respecto del valor final: exp(-pi zeta/sqrt(1-zeta^2)) y pi/(wn sqrt(1-zeta^2)).
Tolerancias: sobreimpulso 2e-2 (relativo), tiempo de pico 5e-3 (relativo), valor final 1e-4.
"""
import math, platform

MU_A, MU_C = 0.9277, 21.333
WN, ZETA = 1.5, 0.7
DMAX, DRATE = math.radians(0.6), math.radians(3.0)


def disenio(wn, zeta):
    return (wn ** 2 + MU_A) / MU_C, 2 * zeta * wn / MU_C


def simula(kp, kd, tc, limites, t_fin=15.0, dt=0.001):
    th, w, d = 0.0, 0.0, 0.0
    reg = []
    t = 0.0
    sat = False
    while t < t_fin:
        d_cmd = kp * (tc - th) - kd * w
        if limites:
            if abs(d_cmd) > DMAX:
                sat = True
            d_cmd = max(-DMAX, min(DMAX, d_cmd))
            paso = DRATE * dt
            d += max(-paso, min(paso, d_cmd - d))
        else:
            d = d_cmd
        # integracion semi-implicita (la deflexion se mantiene constante en el paso)
        k1 = (w, MU_A * th + MU_C * d)
        k2 = (w + dt / 2 * k1[1], MU_A * (th + dt / 2 * k1[0]) + MU_C * d)
        th += dt * k2[0]
        w += dt * k2[1]
        t += dt
        reg.append((t, th, d))
    return reg, sat


def metricas(reg, tc):
    final = reg[-1][1]
    pico = max(reg, key=lambda x: x[1])
    return final, pico[0], (pico[1] - final) / final, max(abs(x[2]) for x in reg)


def calcular():
    r = {}
    kp, kd = disenio(WN, ZETA)
    r["kp"], r["kd"] = kp, kd
    r["wn_cl"] = math.sqrt(MU_C * kp - MU_A)
    r["z_cl"] = MU_C * kd / (2 * r["wn_cl"])
    r["dc"] = MU_C * kp / (MU_C * kp - MU_A)
    tc = math.radians(1.0)
    reg, _ = simula(kp, kd, tc, False)
    fin, tp, os_, dmax = metricas(reg, tc)
    r["lin"] = dict(final=fin, tp=tp, os=os_, dmax=dmax)
    r["os_ana"] = math.exp(-math.pi * ZETA / math.sqrt(1 - ZETA ** 2))
    r["tp_ana"] = math.pi / (WN * math.sqrt(1 - ZETA ** 2))
    r["final_ana"] = r["dc"] * tc
    r["err_os"] = abs(os_ - r["os_ana"]) / r["os_ana"]
    r["err_tp"] = abs(tp - r["tp_ana"]) / r["tp_ana"]
    r["err_final"] = abs(fin - r["final_ana"]) / r["final_ana"]
    filas = []
    for grados in (1.0, 5.0, 10.0):
        tc = math.radians(grados)
        reg_l, _ = simula(kp, kd, tc, False)
        reg_s, sat = simula(kp, kd, tc, True)
        fl, tpl, osl, dml = metricas(reg_l, tc)
        fs, tps, oss, dms = metricas(reg_s, tc)
        filas.append(dict(cmd=grados, d_lin=math.degrees(dml), d_sat=math.degrees(dms), sat=sat, os_lin=osl, os_sat=(oss if abs(math.degrees(fs)) < 1000 else float("nan")), fin_sat=math.degrees(fs), estable=abs(fs - fl) < 0.05 * abs(fl)))
    r["filas"] = filas
    # ganancias bajo el minimo: lazo inestable
    r["kp_min"] = MU_A / MU_C
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Planta SINTETICA: mu_a = {MU_A} 1/s2 (inestable), mu_c = {MU_C} 1/s2; especificacion wn = {WN} rad/s, zeta = {ZETA}")
    print(f"Ganancias: Kp = {r['kp']:.5f} (minimo {r['kp_min']:.5f}), Kd = {r['kd']:.5f}; lazo cerrado verificado: wn = {r['wn_cl']:.4f}, zeta = {r['z_cl']:.4f}; ganancia estatica = {r['dc']:.4f}")
    l = r["lin"]
    print(f"Escalon de 1 grado (lineal): valor final = {math.degrees(l['final']):.4f} grados (analitico {math.degrees(r['final_ana']):.4f}; error {r['err_final']:.1e}); sobreimpulso = {l['os']*100:.3f} % (analitico {r['os_ana']*100:.3f} %; error {r['err_os']:.1e}); tiempo de pico = {l['tp']:.3f} s (analitico {r['tp_ana']:.3f} s; error {r['err_tp']:.1e})")
    print(" comando  tobera pico lineal  tobera pico con limites  sobreimp. lineal  sobreimp. con limites  final con limites  satura  respuesta estable")
    for f in r["filas"]:
        print(f"  {f['cmd']:4.1f}   {f['d_lin']:12.3f}      {f['d_sat']:14.3f}         {f['os_lin']*100:8.2f} %      {('%10.2f' % (f['os_sat']*100)) if f['os_sat'] == f['os_sat'] else '       n/d'} %        {('%8.3f' % f['fin_sat']) if abs(f['fin_sat']) < 1000 else ' diverge'}      {'si' if f['sat'] else 'no'}     {'si' if f['estable'] else 'NO'}")
    assert r["err_os"] < 2e-2 and r["err_tp"] < 5e-3 and r["err_final"] < 1e-4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
