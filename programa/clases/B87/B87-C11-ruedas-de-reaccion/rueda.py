#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C11: maniobra rest-to-rest de un eje con una rueda de reaccion; conservacion del momento angular total,
limites de par y de momento. Satelite SINTETICO I = diag(0.35, 0.40, 0.30) kg m^2; rueda de ejemplo: par maximo 0.01 N m,
momento maximo 0.05 N m s, inercia 5e-5 kg m^2. Maniobra alrededor de z (RK4, dt = 0.001 s). Perfil: triangular si el momento
pico cabe, trapezoidal si no. Todo SINTETICO."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

TAU, HMAX, IW = 0.01, 0.05, 5e-5


def perfil(theta):
    """Tiempos de aceleracion, crucero y frenado para un giro rest-to-rest alrededor de z (Iz = 0.30)."""
    Iz = 0.30
    al = TAU / Iz
    w_tri = math.sqrt(theta * al)
    if Iz * w_tri <= HMAX:
        return w_tri / al, 0.0, w_tri
    wmax = HMAX / Iz
    ta = wmax / al
    tc = (theta - wmax * ta) / wmax
    return ta, tc, wmax


def simular(theta_deg):
    I = inertia_example()
    th = theta_deg * D2R
    ta, tc, wpk = perfil(th)
    T = 2 * ta + tc
    q = np.array([0, 0, 0, 1.0]); w = np.zeros(3); h = np.zeros(3)
    dt = 0.001
    Hi0 = np.zeros(3)
    pico_h = 0.0; dH = 0.0; peak_w = 0.0
    for k in range(int(round(T / dt))):
        t = k * dt
        u = np.array([0.0, 0.0, -TAU if t < ta else (0.0 if t < ta + tc else TAU)])   # par sobre la rueda
        q, w, h = step(q, w, h, u, np.zeros(3), I, dt)
        Hi = A_of_q(q).T @ (I @ w + h)
        dH = max(dH, np.linalg.norm(Hi - Hi0))
        pico_h = max(pico_h, np.linalg.norm(h)); peak_w = max(peak_w, abs(w[2]))
    qt = q_from_axis_angle([0, 0, 1], -th)       # convencion: u<0 sobre la rueda gira el cuerpo en +z ; se compara el modulo
    ang = ang_between(q, q_from_axis_angle([0, 0, 1], th)) * R2D
    ang2 = ang_between(q, qt) * R2D
    return dict(T=T, ta=ta, tc=tc, pico_h=pico_h, peak_w=peak_w, dH=dH, ang=min(ang, ang2), h_fin=float(np.linalg.norm(h)), w_fin=float(np.linalg.norm(w)))


def calcular():
    r30 = simular(30.0); r90 = simular(90.0); r180 = simular(180.0)
    rpm = r30['pico_h'] / IW * 60 / (2 * math.pi)
    return dict(r30=r30, r90=r90, r180=r180, rpm30=rpm, al=TAU / 0.30, Iw=IW)


def main():
    banner("B87-C11 rueda de reaccion | SINTETICO: I = diag(0.35, 0.40, 0.30) kg m^2; par max 0.01 N m, momento max 0.05 N m s, I_rueda = 5e-5 kg m^2")
    d = calcular()
    print(f"aceleracion angular maxima del cuerpo = par/Iz = {d['al']:.5f} rad/s^2")
    print("giro   tiempo [s]  acel [s]  crucero [s]  w pico [deg/s]  h pico [N m s]  deriva H [N m s]  error angular [deg]  w final [rad/s]")
    for nombre, r in (("30 deg", d['r30']), ("90 deg", d['r90']), ("180 deg", d['r180'])):
        print(f"{nombre:6s} {r['T']:10.3f} {r['ta']:9.3f} {r['tc']:12.3f} {r['peak_w']*R2D:15.3f} {r['pico_h']:14.4f} {r['dH']:17.2e} {r['ang']:20.2e} {r['w_fin']:15.2e}")
    print(f"velocidad de la rueda a 30 deg (h pico / I_rueda) = {d['rpm30']:.0f} rpm")
    for r in (d['r30'], d['r90'], d['r180']):
        assert r['dH'] < 1e-10 and r['ang'] < 0.05 and r['pico_h'] <= HMAX * 1.002
    assert d['r30']['tc'] == 0 and d['r90']['tc'] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
