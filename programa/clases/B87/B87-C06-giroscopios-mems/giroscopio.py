#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C06: giroscopio MEMS de un eje: ruido de paseo angular (ARW) y de paseo de tasa (RRW), varianza de Allan.
Datos SINTETICOS (semilla 20260516): fs = 10 Hz, 4 h. ARW N = 0.2 deg/sqrt(h); RRW K = 2 deg/h/sqrt(h). Unidades SI en el codigo (rad, s)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

N_DEG_RTH = 0.2          # deg / sqrt(h)
K_DEG_H_RTH = 2.0        # (deg/h) / sqrt(h)
N_SI = N_DEG_RTH * D2R / 60.0                       # rad / sqrt(s)  (1 sqrt(h) = 60 sqrt(s))
K_SI = K_DEG_H_RTH * D2R / 3600.0 / 60.0            # (rad/s) / sqrt(s)


def simular(T, fs, rng):
    dt = 1.0 / fs
    n = int(T * fs)
    blanco = N_SI / math.sqrt(dt) * rng.standard_normal(n)
    sesgo = np.cumsum(K_SI * math.sqrt(dt) * rng.standard_normal(n))
    return blanco + sesgo


def allan(y, fs, ms):
    """Desviacion de Allan (no solapada) de una serie de tasas y (rad/s)."""
    out = []
    for m in ms:
        k = len(y) // m
        if k < 3:
            continue
        ym = y[:k * m].reshape(k, m).mean(axis=1)
        av = 0.5 * np.mean(np.diff(ym) ** 2)
        out.append((m / fs, math.sqrt(av)))
    return np.array(out)


def calcular():
    fs = 10.0
    rng = np.random.default_rng(20260516)
    y = simular(4 * 3600.0, fs, rng)
    ms = np.unique(np.round(np.logspace(0, 4.3, 45)).astype(int))
    ad = allan(y, fs, ms)
    taus, sig = ad[:, 0], ad[:, 1]
    A = np.column_stack([1.0 / taus, taus / 3.0])
    coef = np.linalg.lstsq(A, sig ** 2, rcond=None)[0]
    N_est = math.sqrt(max(coef[0], 0)); K_est = math.sqrt(max(coef[1], 0))
    # error de angulo al integrar solo el giroscopio (ARW + RRW): Monte Carlo a 600 s
    t_int = 600.0
    angs = []
    for _ in range(300):
        yy = simular(t_int, fs, rng)
        angs.append(np.sum(yy) / fs)
    sig_ang_mc = float(np.std(angs))
    sig_ang_teo = math.sqrt(N_SI ** 2 * t_int + K_SI ** 2 * t_int ** 3 / 3.0)
    # sesgo de 0.1 deg/s sin calibrar: angulo a 600 s
    return dict(N_est=N_est, K_est=K_est, taus=taus, sig=sig, N_SI=N_SI, K_SI=K_SI, sig_ang_mc=sig_ang_mc, sig_ang_teo=sig_ang_teo,
                tau_min=float(taus[np.argmin(sig)]), sig_min=float(sig.min()), fs=fs, t_int=t_int)


def main():
    banner("B87-C06 giroscopio MEMS | serie SINTETICA de 4 h a 10 Hz (semilla 20260516)")
    d = calcular()
    print(f"parametros verdaderos: N = {N_DEG_RTH} deg/sqrt(h) = {d['N_SI']:.4e} rad/sqrt(s) ; K = {K_DEG_H_RTH} deg/h/sqrt(h) = {d['K_SI']:.4e} rad/s/sqrt(s)")
    print("tau [s]   sigma_Allan [deg/h]")
    for tau, s in list(zip(d['taus'], d['sig']))[::4]:
        print(f"{tau:8.1f}   {s*R2D*3600:10.3f}")
    print(f"minimo de la curva: {d['sig_min']*R2D*3600:.3f} deg/h en tau = {d['tau_min']:.1f} s")
    print(f"ajuste AVAR = N^2/tau + K^2 tau/3: N = {d['N_est']*R2D*60:.4f} deg/sqrt(h) ; K = {d['K_est']*R2D*3600*60:.4f} deg/h/sqrt(h)")
    print(f"error de angulo integrando solo el giroscopio a {d['t_int']:.0f} s: Monte Carlo = {d['sig_ang_mc']*R2D*3600:.2f} arcsec ; teoria = {d['sig_ang_teo']*R2D*3600:.2f} arcsec")
    assert abs(d['N_est'] - d['N_SI']) / d['N_SI'] < 0.1
    assert abs(d['K_est'] - d['K_SI']) / d['K_SI'] < 0.35
    assert abs(d['sig_ang_mc'] - d['sig_ang_teo']) / d['sig_ang_teo'] < 0.15
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
