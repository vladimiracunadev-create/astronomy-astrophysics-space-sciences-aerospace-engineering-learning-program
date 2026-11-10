#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C15: apuntamiento fino de un eje: lazo PD con medida de actitud ruidosa (20 arcsec, 10 Hz) y giroscopio (2e-5 rad/s),
par perturbador constante de 2 uN m + ruido de par (jitter) blanco; indices de error (media, desviacion, error de apuntamiento
absoluto 99.7 %, error relativo en ventanas de 10 s). Iz = 0.30 kg m^2 SINTETICO; semilla 20260521; dt = 0.01 s, 600 s."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

IZ = 0.30
ARC = D2R / 3600.0


def correr(wn, zeta=0.7, T=600.0, dt=0.01, seed=20260521):
    rng = np.random.default_rng(seed)
    kp, kd = IZ * wn ** 2, 2 * zeta * wn * IZ
    th, w = 0.0, 0.0
    err = []
    th_m = 0.0
    for k in range(int(T / dt)):
        if k % 10 == 0:
            th_m = th + 20 * ARC * rng.standard_normal()
        w_m = w + 2e-5 * rng.standard_normal()
        u = -kp * th_m - kd * w_m
        td = 2e-6 + 3e-7 * rng.standard_normal()
        w += (u + td) / IZ * dt
        th += w * dt
        err.append(th)
    e = np.array(err)[int(100 / dt):]               # se descarta el transitorio de 100 s
    ape_mean = float(e.mean())
    sd = float(e.std())
    p997 = float(np.percentile(np.abs(e), 99.7))
    nv = int(10 / dt)
    rpe = float(np.mean([e[i:i + nv].std() for i in range(0, len(e) - nv, nv)]))
    return dict(kp=kp, kd=kd, mean=ape_mean / ARC, sd=sd / ARC, p997=p997 / ARC, rpe=rpe / ARC, teo_bias=2e-6 / kp / ARC)


def calcular():
    return {wn: correr(wn) for wn in (0.1, 0.3, 1.0)}


def main():
    banner("B87-C15 apuntamiento fino de un eje | SINTETICO (semilla 20260521): medida 20 arcsec a 10 Hz, par constante 2 uN m + jitter")
    d = calcular()
    print("wn [rad/s]  Kp [N m/rad]  Kd [N m s/rad]  media [arcsec]  desv. [arcsec]  APE 99.7% [arcsec]  RPE 10 s [arcsec]  sesgo teorico tau/Kp [arcsec]")
    for wn, r in d.items():
        print(f"{wn:10.1f}  {r['kp']:12.4f}  {r['kd']:14.4f}  {r['mean']:14.2f}  {r['sd']:14.2f}  {r['p997']:18.2f}  {r['rpe']:16.2f}  {r['teo_bias']:26.2f}")
    for wn, r in d.items():
        assert abs(r['mean'] - r['teo_bias']) < 0.15 * r['teo_bias'] + 3 * r['sd'] / 40
    assert d[0.1]['mean'] > d[1.0]['mean'] and d[1.0]['sd'] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
