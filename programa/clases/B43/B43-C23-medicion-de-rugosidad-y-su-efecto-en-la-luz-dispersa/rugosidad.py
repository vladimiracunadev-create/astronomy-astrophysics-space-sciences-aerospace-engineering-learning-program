#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C23: medicion de rugosidad y su efecto en la luz dispersa total (TIS).

Datos: SINTETICOS. Perfil 1D de 4096 puntos con paso de 0,25 um (longitud 1,024 mm) construido con una densidad espectral de potencia (PSD) A/f^2 entre 1 y 1800 mm^-1 y fases aleatorias (semilla 20261109);
A = 1 nm^2 mm^-1; por la banda efectiva (modos k = 2 a 1842 de la ventana) la rugosidad RMS resulta de unos 0,81 nm. lambda = 550 nm. No son mediciones de ninguna superficie real.
Modelo: sigma^2 = integral de PSD df; luz dispersa total a incidencia normal TIS = (4 pi sigma cos(theta)/lambda)^2 (aproximacion escalar, superficie lisa frente a lambda); reflectancia especular R = R_0 exp(-TIS).
Verificacion independiente: sigma del perfil medido directamente (raiz del promedio de h^2) frente a sigma de la integral de la PSD estimada con la DFT del perfil (identidad de Parseval).
Supuestos: perfil 1D como sustituto de una superficie 2D isotropa, estadistica gaussiana, banda 1-1800 mm^-1 (periodos mayores que lambda). Validez: sigma << lambda.
Tolerancia: sigma del perfil frente a la integral continua de la PSD en la misma banda (regla del punto medio), 5 %; Parseval, 1e-9 relativo.
"""
from __future__ import annotations
import cmath, math, platform, random

N = 4096; DX = 0.25e-3  # mm
LAM = 550.0

def dft_potencia(h):
    n = len(h)
    # DFT directa solo para los modos de la banda construida (k = 1..K) mas comprobacion de Parseval con FFT recursiva
    return fft(h)

def fft(x):
    n = len(x)
    if n == 1:
        return x
    p = fft(x[0::2]); q = fft(x[1::2])
    out = [0j] * n
    for k in range(n // 2):
        t = cmath.exp(-2j * math.pi * k / n) * q[k]
        out[k] = p[k] + t; out[k + n // 2] = p[k] - t
    return out

def calc():
    rng = random.Random(20261109)
    L = N * DX; df = 1.0 / L
    f1, f2 = 1.0, 1800.0
    A = 1.0  # nm^2 mm^-1
    kmin = int(math.ceil(f1 / df)); kmax = int(math.floor(f2 / df))
    h = [0.0] * N
    amps = []
    for k in range(kmin, kmax + 1):
        a = math.sqrt(2 * A / (k * df) ** 2 * df); ph = rng.uniform(0, 2 * math.pi)
        amps.append(a)
        for i in range(N):
            h[i] += a * math.cos(2 * math.pi * k * df * i * DX + ph)
    r = {}
    r["modos"] = kmax - kmin + 1
    sig2_psd = sum(a * a / 2 for a in amps)
    r["sigma_psd_nm"] = math.sqrt(sig2_psd)
    r["sigma_cont_nm"] = math.sqrt(A * (1 / ((kmin - 0.5) * df) - 1 / ((kmax + 0.5) * df)))
    m = sum(h) / N
    r["sigma_perfil_nm"] = math.sqrt(sum((v - m) ** 2 for v in h) / N)
    X = fft([complex(v - m) for v in h])
    par = sum(abs(c) ** 2 for c in X) / N / N
    r["parseval_rel"] = abs(par - r["sigma_perfil_nm"] ** 2) / par
    r["TIS_cont"] = (4 * math.pi * r["sigma_cont_nm"] / LAM) ** 2
    r["TIS_perfil"] = (4 * math.pi * r["sigma_perfil_nm"] / LAM) ** 2
    r["TIS_45"] = (4 * math.pi * r["sigma_cont_nm"] * math.cos(math.radians(45)) / LAM) ** 2
    r["R_espec"] = 0.92 * math.exp(-r["TIS_perfil"])
    filas = []
    for s in (0.5, 1.0, 2.0, 5.0):
        filas.append((s, (4 * math.pi * s / LAM) ** 2))
    r["filas"] = filas
    r["TIS_lambda_ratio"] = ((4 * math.pi * 1.0 / 400.0) ** 2) / ((4 * math.pi * 1.0 / 800.0) ** 2)
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        if k != "filas":
            print(f"{k} = {v:.6g}")
    print("sigma (nm) | TIS")
    for s, t in r["filas"]:
        print(f"{s} | {t:.3e}")
    assert abs(r["sigma_perfil_nm"] / r["sigma_cont_nm"] - 1) < 0.05
    assert r["parseval_rel"] < 1e-9
    assert abs(r["TIS_lambda_ratio"] - 4.0) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
