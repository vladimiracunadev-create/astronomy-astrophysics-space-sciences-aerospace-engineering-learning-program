#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C19: verificacion de una ley de control de un eje: margenes de ganancia y fase con retardo, simulacion en el dominio del
tiempo y Monte Carlo (inercia +-20 %, ruido de medida 20 arcsec). L(s) = (Kd s + Kp) exp(-s Td) / (I s^2); PD de wn = 0.2 rad/s,
zeta = 0.7 con I nominal 0.30 kg m^2 SINTETICO. Requisito de ejemplo: giro de 10 deg, asentamiento al 2 % < 60 s, sobreimpulso < 20 %.
Semilla 20260523; dt = 0.01 s."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

I0, WN, Z = 0.30, 0.2, 0.7
KP, KD = I0 * WN ** 2, 2 * Z * WN * I0


def margenes(Td, I=I0):
    w = np.logspace(-3, 2, 200000)
    s = 1j * w
    L = (KD * s + KP) * np.exp(-s * Td) / (I * s ** 2)
    mag = np.abs(L); fase = np.unwrap(np.angle(L)) * R2D
    i = np.where(np.diff(np.sign(mag - 1)) != 0)[0]
    wc = w[i[0]] if len(i) else float('nan')
    pm = 180 + fase[i[0]] if len(i) else float('nan')
    j = np.where(np.diff(np.sign(fase + 180)) != 0)[0]
    gm = -20 * math.log10(mag[j[0]]) if len(j) else float('inf')
    return wc, pm, gm


def sim(I_real, Td, sigma_arcsec=0.0, T=200.0, dt=0.01, rng=None, ang=10.0):
    nd = int(round(Td / dt))
    buf = [0.0] * (nd + 1)
    th, w = 0.0, 0.0
    ref = ang * D2R
    traj = []
    for k in range(int(T / dt)):
        thm = th + (sigma_arcsec * D2R / 3600 * rng.standard_normal() if sigma_arcsec > 0 else 0.0)
        u = -KP * (thm - ref) - KD * w
        buf.append(u); ui = buf.pop(0)
        w += ui / I_real * dt
        th += w * dt
        traj.append(th)
    tr = np.array(traj) / ref
    over = max(0.0, tr.max() - 1) * 100
    fuera = np.where(np.abs(tr - 1) > 0.02)[0]
    ts = (fuera[-1] + 1) * dt if len(fuera) else 0.0
    return ts, over, bool(np.abs(tr[-1] - 1) < 0.02)


def calcular():
    out = {}
    for Td in (0.0, 0.5, 1.0, 2.0, 5.0):
        out[Td] = margenes(Td)
    rng = np.random.default_rng(20260523)
    ok = 0; n = 200; tss = []; ovs = []
    for _ in range(n):
        Ir = I0 * rng.uniform(0.8, 1.2)
        ts, ov, est = sim(Ir, 0.2, 20.0, rng=rng, T=120.0)
        tss.append(ts); ovs.append(ov)
        ok += int(est and ts < 60 and ov < 20)
    nom = sim(I0, 0.0, 0.0, rng=rng, T=120.0)
    inest = sim(I0, 5.0, 0.0, rng=rng, T=300.0)
    return dict(marg=out, tasa=ok / n, ts_med=float(np.mean(tss)), ts_max=float(np.max(tss)), ov_med=float(np.mean(ovs)), ov_max=float(np.max(ovs)),
                nom=nom, inest=inest, n=n)


def main():
    banner("B87-C19 verificacion | SINTETICO: PD wn = 0.2, zeta = 0.7, I = 0.30 kg m^2 +-20 %, retardo y ruido; Monte Carlo semilla 20260523")
    d = calcular()
    print("retardo [s]  frecuencia de cruce [rad/s]  margen de fase [deg]  margen de ganancia [dB]")
    for Td, (wc, pm, gm) in d['marg'].items():
        print(f"{Td:11.1f}  {wc:27.4f}  {pm:20.1f}  {gm:22.1f}")
    print(f"simulacion nominal (sin retardo): asentamiento = {d['nom'][0]:.1f} s ; sobreimpulso = {d['nom'][1]:.1f} % ; estable = {d['nom'][2]}")
    print(f"simulacion con retardo de 5 s: estable = {d['inest'][2]} ; sobreimpulso = {'diverge' if d['inest'][1] > 1000 else format(d['inest'][1], '.0f') + ' %'}")
    print(f"Monte Carlo ({d['n']} casos, retardo 0.2 s, I +-20 %, ruido 20 arcsec): cumple {d['tasa']*100:.1f} % ; asentamiento medio = {d['ts_med']:.1f} s (max {d['ts_max']:.1f}) ; sobreimpulso medio = {d['ov_med']:.1f} % (max {d['ov_max']:.1f})")
    assert d['marg'][0.0][1] > 60 and d['marg'][5.0][1] < 0 and d['marg'][0.5][1] > d['marg'][1.0][1] > d['marg'][2.0][1]
    assert d['nom'][2] and not d['inest'][2]
    assert d['tasa'] >= 0.9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
