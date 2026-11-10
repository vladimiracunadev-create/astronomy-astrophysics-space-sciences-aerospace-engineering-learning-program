#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C17: control PD en cuaterniones de tres ejes: tau = -Kp sign(qe_w) qe_v - Kd w (Wie), con Kp = 2 I_medio wn^2 (escalar), Kd = 2 zeta wn I
(por eje). Maniobra de 60 deg alrededor de (1,2,3)/sqrt(14) desde el reposo; con y sin limite de par (0.004 N m por eje).
Satelite SINTETICO I = diag(0.35, 0.40, 0.30) kg m^2; wn = 0.2 rad/s, zeta = 0.8; RK4 dt = 0.01 s; 150 s."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

WN, ZETA = 0.2, 0.8


def maniobra(limite, ang_deg=60.0, T=150.0, dt=0.01):
    I = inertia_example()
    Id = np.diag(I)
    kp = 2 * Id.mean() * WN ** 2; kd = 2 * ZETA * WN * Id
    qc = q_from_axis_angle([1, 2, 3], ang_deg * D2R)
    q = np.array([0, 0, 0, 1.0]); w = np.zeros(3); h = np.zeros(3)
    th, tmax, sat, V0 = [], 0.0, 0, None
    Vprev = None; Vmono = True
    for k in range(int(T / dt)):
        qe = qmul(q, qconj(qc))
        s = 1.0 if qe[3] >= 0 else -1.0
        tau = -kp * s * qe[:3] - kd * w
        if limite is not None:
            tc = np.clip(tau, -limite, limite)
            sat += int(np.any(tc != tau)); tau = tc
        tmax = max(tmax, float(np.max(np.abs(tau))))
        q, w, h = step(q, w, h, np.zeros(3), tau, I, dt)
        e = ang_between(q, qc) * R2D
        th.append(e)
        qe2 = qmul(q, qconj(qc))
        V = 0.5 * w @ I @ w + 2 * kp * (1 - abs(qe2[3]))
        if limite is None and Vprev is not None and V > Vprev + 1e-12:
            Vmono = False
        Vprev = V
    th = np.array(th)
    ts = np.arange(1, len(th) + 1) * dt
    band = 0.02 * ang_deg
    fuera = np.where(th > band)[0]
    t_s = float(ts[fuera[-1]] + dt) if len(fuera) else 0.0
    return dict(t_s=t_s, tmax=tmax, sat=sat / len(th), efin=float(th[-1]), Vmono=(Vmono if limite is None else 'no evaluada'))


def calcular():
    lin = maniobra(None)
    lim = maniobra(0.004)
    return dict(lin=lin, lim=lim, t_teo=4 / (ZETA * WN))


def main():
    banner("B87-C17 control de tres ejes | SINTETICO: maniobra de 60 deg, wn = 0.2 rad/s, zeta = 0.8, I = diag(0.35, 0.40, 0.30) kg m^2")
    d = calcular()
    for nombre, r in (("sin limite de par", d['lin']), ("limite 0.004 N m por eje", d['lim'])):
        print(f"{nombre}: asentamiento al 2 % = {r['t_s']:.1f} s ; par maximo = {r['tmax']*1e3:.2f} mN m ; saturado {r['sat']*100:.1f} % ; error final = {r['efin']:.2e} deg ; V monotona = {r['Vmono']}")
    print(f"teoria lineal (4/(zeta wn)) = {d['t_teo']:.1f} s")
    assert d['lin']['Vmono'] and d['lin']['efin'] < 1e-3 and d['lim']['efin'] < 1e-3
    assert d['lim']['tmax'] <= 0.004 + 1e-12 and d['lim']['t_s'] > d['lin']['t_s']
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
