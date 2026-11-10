#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C08: calibracion de un magnetometro (sesgo + factor de escala por eje) por minimos cuadrados no lineales (Gauss-Newton)
y del sesgo de un giroscopio con el satelite en reposo. Datos SINTETICOS (semilla 20260518): campo uniforme de 34 uT visto desde
un cuerpo que gira por muchas orientaciones; sesgo (3000, -2000, 1000) nT y escalas (1.03, 0.97, 1.01); ruido de 100 nT."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

B_T = 34e-6
S_TRUE = np.array([1.03, 0.97, 1.01])
O_TRUE = np.array([3000e-9, -2000e-9, 1000e-9])


def gauss_newton(m, B, it=30):
    s = np.ones(3); o = np.zeros(3)
    hist = []
    for _ in range(it):
        y = (m - o) / s
        ny = np.linalg.norm(y, axis=1)
        r = ny - B
        J = np.hstack([-(y ** 2) / (s * ny[:, None]), -y / (s * ny[:, None])])   # columnas: s1..s3, o1..o3
        dp = np.linalg.lstsq(J, -r, rcond=None)[0]
        s = s + dp[:3]; o = o + dp[3:]
        hist.append(math.sqrt(np.mean(r ** 2)))
        if np.linalg.norm(dp) < 1e-14:
            break
    return s, o, hist


def calcular():
    rng = np.random.default_rng(20260518)
    n = 600
    Bb = np.array([unit(rng.standard_normal(3)) * B_T for _ in range(n)])     # campo visto en el cuerpo
    m = S_TRUE * Bb + O_TRUE + 100e-9 * rng.standard_normal((n, 3))
    s, o, hist = gauss_newton(m, B_T)
    res_antes = math.sqrt(np.mean((np.linalg.norm(m, axis=1) - B_T) ** 2))
    mc = (m - o) / s
    res_desp = math.sqrt(np.mean((np.linalg.norm(mc, axis=1) - B_T) ** 2))
    dir_antes = math.sqrt(np.mean([math.acos(min(1, unit(a) @ unit(b))) ** 2 for a, b in zip(m, Bb)])) * R2D
    dir_desp = math.sqrt(np.mean([math.acos(min(1, unit(a) @ unit(b))) ** 2 for a, b in zip(mc, Bb)])) * R2D
    # giroscopio en reposo: sesgo = media; incertidumbre = sigma/sqrt(N)
    fs = 10.0; T = 60.0; sg = 5.8178e-5 / math.sqrt(1 / fs)  # ARW 0.2 deg/sqrt(h) a 10 Hz
    bias_true = 0.05 * D2R / 1.0   # rad/s (0.05 deg/s)
    w = bias_true + sg * rng.standard_normal(int(T * fs))
    b_est = w.mean()
    return dict(s=s, o=o, hist=hist, res_antes=res_antes, res_desp=res_desp, dir_antes=dir_antes, dir_desp=dir_desp,
                bias_true=bias_true, b_est=b_est, b_sig=sg / math.sqrt(T * fs), sg=sg)


def main():
    banner("B87-C08 calibracion | magnetometro y giroscopio SINTETICOS (semilla 20260518)")
    d = calcular()
    print(f"verdad: escalas = {S_TRUE} ; sesgo = {O_TRUE*1e9} nT")
    print(f"estimado: escalas = {np.round(d['s'],5)} ; sesgo = {np.round(d['o']*1e9,1)} nT")
    print(f"iteraciones Gauss-Newton = {len(d['hist'])} ; rms de |m|-B: " + " -> ".join(f"{h*1e9:.1f}" for h in d['hist'][:5]) + " nT")
    print(f"residuo rms de |m| - B: antes = {d['res_antes']*1e9:.1f} nT ; despues = {d['res_desp']*1e9:.1f} nT (ruido = 100 nT por eje)")
    print(f"error de direccion rms: antes = {d['dir_antes']:.3f} deg ; despues = {d['dir_desp']:.3f} deg")
    print(f"giroscopio en reposo 60 s: sesgo verdadero = {d['bias_true']*R2D:.4f} deg/s ; estimado = {d['b_est']*R2D:.4f} deg/s ; sigma de la media = {d['b_sig']*R2D*3600:.2f} deg/h")
    assert np.abs(d['s'] - S_TRUE).max() < 0.002 and np.abs(d['o'] - O_TRUE).max() < 100e-9
    assert d['res_desp'] < d['res_antes'] / 5 and d['dir_desp'] < d['dir_antes'] / 3
    assert abs(d['b_est'] - d['bias_true']) < 5 * d['b_sig']
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
