#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C13: propulsores de actitud (gas frio): par de un par de toberas, impulso minimo, consumo por Isp y ciclo limite de
banda muerta en un eje. Satelite SINTETICO Iz = 0.30 kg m^2; toberas de ejemplo F = 0.05 N a d = 0.1 m del eje (par = 2 F d = 0.01 N m),
Isp de ejemplo 60 s, tiempo minimo de encendido 0.02 s, banda muerta +-0.5 deg. g0 = 9.80665 m/s^2 (valor convencional). Todo SINTETICO."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

F, DB, ISP, TMIN, IZ, G0 = 0.05, 0.1, 60.0, 0.02, 0.30, 9.80665


def consumo_detumble(w0_deg):
    dH = IZ * w0_deg * D2R                       # momento angular a eliminar
    imp = 2 * dH / DB                            # impulso total de las dos toberas (N s)
    return dH, imp, imp / (ISP * G0)


def ciclo_limite(T=2000.0, dt=0.002, theta_db_deg=0.5):
    tau = 2 * F * DB
    al = tau / IZ
    dw = al * TMIN                               # salto de velocidad por pulso minimo
    tdb = theta_db_deg * D2R
    th, w = tdb * 1.0001, 0.0
    quedan = 0; pulsos = 0; cruces = []; a_cmd = 0.0
    npul = int(round(TMIN / dt))                  # pasos por pulso minimo
    signo_prev = np.sign(th)
    wth = dw / 2
    k_end = int(T / dt)
    for k in range(k_end):
        if quedan == 0:
            if th > tdb and w > -wth:
                a_cmd = -al; quedan = npul; pulsos += 1
            elif th < -tdb and w < wth:
                a_cmd = al; quedan = npul; pulsos += 1
        a = a_cmd if quedan > 0 else 0.0
        if quedan > 0:
            quedan -= 1
        w += a * dt
        th += w * dt
        s = np.sign(th)
        if s != signo_prev and s != 0:
            cruces.append(k * dt); signo_prev = s
    per = 2 * np.mean(np.diff(cruces)) if len(cruces) > 3 else float('nan')
    masa = pulsos * 2 * F * TMIN / (ISP * G0)
    return dict(dw=dw, per=per, pulsos=pulsos, masa=masa, per_teo=4 * tdb / dw, th_max=float(abs(th)), T=T)


def calcular():
    dH, imp, m = consumo_detumble(5.0)
    lc = ciclo_limite()
    return dict(tau=2 * F * DB, al=2 * F * DB / IZ, dw_bit=lc['dw'], dth_bit_deg=lc['dw'] * R2D, ibit=2 * F * TMIN, Hbit=2 * F * DB * TMIN,
                dH=dH, imp=imp, masa=m, lc=lc, masa_h=lc['masa'] / lc['T'] * 3600)


def main():
    banner("B87-C13 propulsores | SINTETICO: F = 0.05 N por tobera, brazo 0.1 m, Isp 60 s, impulso minimo de 0.02 s, Iz = 0.30 kg m^2")
    d = calcular(); lc = d['lc']
    print(f"par = 2 F d = {d['tau']:.4f} N m ; aceleracion angular = {d['al']:.5f} rad/s^2")
    print(f"impulso minimo por tobera F t_min = {d['ibit']*1e3:.2f} mN s ; momento angular por pulso = {d['Hbit']*1e6:.0f} uN m s ; salto de velocidad = {d['dw_bit']:.3e} rad/s ({d['dth_bit_deg']:.4f} deg/s)")
    print(f"detumbling de 5 deg/s: momento a eliminar = {d['dH']:.5f} N m s ; impulso total = {d['imp']:.4f} N s ; propergol = {d['masa']*1e3:.3f} g")
    print(f"ciclo limite (banda muerta +-0.5 deg, {lc['T']:.0f} s): periodo medido = {lc['per']:.1f} s ; teoria 4 theta_db/dw = {lc['per_teo']:.1f} s")
    print(f"pulsos = {lc['pulsos']} ; propergol = {lc['masa']*1e3:.3f} g en {lc['T']:.0f} s = {d['masa_h']*1e3:.2f} g/h")
    assert abs(lc['per'] - lc['per_teo']) / lc['per_teo'] < 0.1 and lc['th_max'] < 0.6 * D2R
    assert abs(d['masa'] - 2 * d['dH'] / DB / (ISP * G0)) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
