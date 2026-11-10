#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C01: dinamica de cuerpo rigido sin par (RK4), conservacion de H y T, inestabilidad del eje intermedio.
Unidades SI. Cuerpo SINTETICO I = diag(0.35, 0.40, 0.30) kg m^2 (ejes principales). Sin datos medidos."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *


def correr(w0, T_s=60.0, dt=0.01):
    I = inertia_example()
    q = np.array([0, 0, 0, 1.0]); w = np.array(w0, float); h = np.zeros(3)
    H0 = np.linalg.norm(I @ w); T0 = 0.5 * w @ I @ w
    Hi0 = A_of_q(q).T @ (I @ w)
    ts, wp, dH, dT = [], [], 0.0, 0.0
    for k in range(int(T_s / dt)):
        q, w, h = step(q, w, h, np.zeros(3), np.zeros(3), I, dt)
        Hi = A_of_q(q).T @ (I @ w)
        dH = max(dH, np.linalg.norm(Hi - Hi0) / H0)
        dT = max(dT, abs(0.5 * w @ I @ w - T0) / T0)
        ts.append((k + 1) * dt); wp.append(w.copy())
    return np.array(ts), np.array(wp), dH, dT, np.linalg.norm(q), H0, T0


def calcular():
    I = np.diag(inertia_example())
    Om = 1.0
    lam_teo = Om * math.sqrt((I[1] - I[0]) * (I[0] - I[2]) / (I[1] * I[2]))
    # eje intermedio (x): perturbacion pequena en y
    ts, wp, dH, dT, qn, H0, T0 = correr([Om, 1e-4, 0.0], 60.0)
    # tasa de crecimiento: perturbacion de 1e-7 rad/s (regimen lineal), ajuste entre 20 y 45 s
    ts3, wp3, _, _, _, _, _ = correr([Om, 1e-7, 0.0], 45.0)
    t_fit = (ts3 > 20) & (ts3 < 45)
    lam_num = np.polyfit(ts3[t_fit], np.log(np.abs(wp3[t_fit, 1])), 1)[0]
    # eje mayor (y): estable
    ts2, wp2, dH2, dT2, qn2, _, _ = correr([1e-4, Om, 0.0], 60.0)
    return dict(lam_teo=lam_teo, lam_num=lam_num, dH=dH, dT=dT, qn=abs(qn - 1), H0=H0, T0=T0,
                maxy_int=float(np.max(np.abs(wp[:, 1]))), maxx_est=float(np.max(np.abs(wp2[:, 0]))),
                dH_est=dH2, dT_est=dT2, I1=I[0], I2=I[1], I3=I[2], t_e=math.log(10) / lam_teo)


def main():
    banner("B87-C01 cuerpo rigido sin par | cuerpo SINTETICO I = diag(0.35, 0.40, 0.30) kg m^2")
    d = calcular()
    print(f"Giro de 1 rad/s sobre el eje intermedio con perturbacion de 1e-4 rad/s (tasa: 1e-7 rad/s); RK4, dt = 0.01 s, 60 s")
    print(f"H0 = {d['H0']:.5f} kg m^2/s ; T0 = {d['T0']:.5f} J")
    print(f"deriva maxima: |dH|/H = {d['dH']:.2e} ; |dT|/T = {d['dT']:.2e} ; |norma(q)-1| = {d['qn']:.2e}")
    print(f"tasa de crecimiento teorica = {d['lam_teo']:.5f} 1/s ; ajustada = {d['lam_num']:.5f} 1/s")
    print(f"tiempo teorico de x10 = {d['t_e']:.2f} s")
    print(f"eje intermedio: max |w_y| = {d['maxy_int']:.4f} rad/s (parte de 1e-4)")
    print(f"eje mayor (estable): max |w_x| = {d['maxx_est']:.2e} rad/s ; dH = {d['dH_est']:.1e} ; dT = {d['dT_est']:.1e}")
    assert d['dH'] < 1e-9 and d['dT'] < 1e-9 and d['qn'] < 1e-12
    assert abs(d['lam_num'] - d['lam_teo']) / d['lam_teo'] < 0.02
    assert d['maxy_int'] > 0.1 and d['maxx_est'] < 1e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
