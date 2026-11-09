#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C11: busqueda de franjas VLBI (retardo y tasa) con una transformada de Fourier bidimensional.

Datos: ninguna constante fisica. Matriz de visibilidades de 64 canales (1 MHz) por 64 tiempos (1 s), retardo verdadero de 337 ns y tasa verdadera de 0,0137 Hz, amplitud 0,35 por
muestra con ruido de 1,0 por componente: todo SINTETICO e ILUSTRATIVO (semilla 20261109).
Modelo: V[c,t] = A exp(2 pi i (tau nu_c + r t)) + ruido; el pico del modulo de la FFT 2D (con relleno de ceros a 256) da retardo y tasa; el refinamiento usa la parabola en cada eje.
Segunda via: SNR del pico frente a A sqrt(N) / (sigma sqrt 2); la probabilidad de falsa deteccion del maximo de M celdas independientes, P = 1 - (1 - exp(-T))^M, frente a un Monte Carlo
solo con ruido (32 x 32 sin relleno, donde las celdas son exactamente independientes).
Supuestos: ruido blanco gaussiano, una sola fuente, sin variacion de la amplitud en la banda ni en el tiempo. Validez: ilustrativa.
Tolerancia: retardo dentro de 0,25 de celda sin relleno (15,6 ns) y tasa dentro de 0,0035 Hz; falsas alarmas Monte Carlo dentro de 3 sigma binomiales de la prediccion.
"""
from __future__ import annotations
import cmath, math, platform, random, sys

def fft(a):
    n = len(a)
    if n == 1:
        return list(a)
    e = fft(a[0::2]); o = fft(a[1::2])
    t = [cmath.exp(-2j * math.pi * k / n) * o[k] for k in range(n // 2)]
    return [e[k] + t[k] for k in range(n // 2)] + [e[k] - t[k] for k in range(n // 2)]

def fft2(m, nf, nt):
    rows = [fft(r + [0j] * (nt - len(r))) for r in m]
    rows += [[0j] * nt for _ in range(nf - len(m))]
    cols = [fft([rows[i][j] for i in range(nf)]) for j in range(nt)]
    return [[cols[j][i] for j in range(nt)] for i in range(nf)]

def parab(ym, y0, yp):
    return 0.5 * (ym - yp) / (ym - 2 * y0 + yp)

def compute():
    rng = random.Random(20261109)
    nc = nt = 64
    dnu, dt = 1.0e6, 1.0
    tau0, r0, A, sg = 337e-9, 0.0137, 0.35, 1.0
    V = [[A * cmath.exp(2j * math.pi * (tau0 * c * dnu + r0 * t * dt)) + complex(rng.gauss(0, sg), rng.gauss(0, sg)) for t in range(nt)] for c in range(nc)]
    pad = 256
    F = fft2(V, pad, pad)
    mag = [[abs(v) for v in row] for row in F]
    pi, pj = max(((i, j) for i in range(pad) for j in range(pad)), key=lambda p: mag[p[0]][p[1]])
    di = pi if pi <= pad // 2 else pi - pad
    dj = pj if pj <= pad // 2 else pj - pad
    fi = parab(mag[(pi - 1) % pad][pj], mag[pi][pj], mag[(pi + 1) % pad][pj])
    fj = parab(mag[pi][(pj - 1) % pad], mag[pi][pj], mag[pi][(pj + 1) % pad])
    tau_est = (di + fi) / (pad * dnu)
    r_est = (dj + fj) / (pad * dt)
    R = dict(nc=nc, nt=nt, A=A, sg=sg, tau0=tau0, r0=r0, tau_est=tau_est, r_est=r_est, cell_tau=1 / (nc * dnu), cell_r=1 / (nt * dt))
    N = nc * nt
    R["snr_pred"] = A * math.sqrt(N) / (sg * math.sqrt(2))
    F0 = fft2(V, nc, nt)
    d1 = tau0 / R["cell_tau"]; d2 = r0 / R["cell_r"]
    d1 -= round(d1); d2 -= round(d2)
    sc = lambda x: 1.0 if x == 0 else math.sin(math.pi * x) / (math.pi * x)
    R["scal"] = abs(sc(d1) * sc(d2)); R["d1"] = d1; R["d2"] = d2
    R["snr_obs"] = max(abs(v) for row in F0 for v in row) / (sg * math.sqrt(2 * N))
    # falsas detecciones
    n2 = 32
    M = n2 * n2
    T = 6.0
    thr = math.sqrt(T)
    p_pred = 1 - (1 - math.exp(-T)) ** M
    cnt = 0; ntr = 1500
    for _ in range(ntr):
        W = [[complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(n2)] for _ in range(n2)]
        G = fft2(W, n2, n2)
        mx = max(abs(v) for row in G for v in row) / math.sqrt(2 * M)
        cnt += mx > thr
    R.update(M=M, T=T, p_pred=p_pred, p_obs=cnt / ntr, ntr=ntr)
    T1 = -math.log(1 - 0.99 ** (1 / M))
    R["T_1pct"] = T1
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"celdas sin relleno: retardo {R['cell_tau'] * 1e9:.2f} ns, tasa {R['cell_r']:.5f} Hz")
    print(f"retardo verdadero = {R['tau0'] * 1e9:.2f} ns ; estimado = {R['tau_est'] * 1e9:.2f} ns")
    print(f"tasa verdadera = {R['r0']:.5f} Hz ; estimada = {R['r_est']:.5f} Hz")
    assert abs(R["tau_est"] - R["tau0"]) < 0.25 * R["cell_tau"] and abs(R["r_est"] - R["r0"]) < 0.0035
    print(f"SNR del pico: A sqrt(N)/(sigma sqrt2) = {R['snr_pred']:.2f} ; perdida por celda (desfases {R['d1']:+.2f} y {R['d2']:+.2f} celdas) = {R['scal']:.3f} -> {R['snr_pred'] * R['scal']:.2f} ; observada = {R['snr_obs']:.2f}")
    assert abs(R["snr_obs"] / (R["snr_pred"] * R["scal"]) - 1) < 0.15
    print(f"falsa deteccion con umbral |z|^2 > {R['T']} sobre M = {R['M']} celdas: prediccion = {R['p_pred']:.4f} ; Monte Carlo ({R['ntr']}) = {R['p_obs']:.4f}")
    sd = math.sqrt(R["p_pred"] * (1 - R["p_pred"]) / R["ntr"])
    assert abs(R["p_obs"] - R["p_pred"]) < 3 * sd
    print(f"umbral |z|^2 para 1 % de falsas detecciones con M = {R['M']}: {R['T_1pct']:.3f} (|z| = {math.sqrt(R['T_1pct']):.3f})")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
