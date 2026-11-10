#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C32: vibracion aleatoria: sintesis de una senal gaussiana desde una ASD, estimacion espectral (Welch), valor eficaz, picos 3 sigma y curtosis.

Datos CONSULTADOS (2026-11-10): GEVS (GSFC-STD-7000B, 2021-04-28), Tabla 2.4-4 (minimo de mano de obra, componentes de 45,4 kg o menos): 20 Hz 0,01 g2/Hz; +3 dB/oct hasta 80 Hz;
0,04 g2/Hz de 80 a 500 Hz; -3 dB/oct hasta 2000 Hz con 0,01 g2/Hz; total publicado 6,8 g rms.
SENAL SINTETICA (no medida): fs = 8192 Hz, N = 2^15 muestras (4 s), semilla 84032. Sintesis espectral: coeficientes de Fourier con amplitud sqrt(G(f) df N fs/2...) y fase uniforme.
En concreto X_k = sqrt(G(f_k) fs N/2) e^{i phi_k} para 0 < f_k < 2000 Hz (G en g2/Hz); x = parte real de la transformada inversa con la normalizacion de modo que var(x) = int G df.
Estimacion: periodograma de Welch con segmentos de 2048 muestras, ventana de Hann y 50 % de solape (promedio de 15 segmentos); densidad G_est = 2|X|^2/(fs sum(w^2)).
Tolerancias: g rms temporal frente a la integral de la ASD < 3 %; g rms de la ASD estimada frente a la teorica < 3 %; curtosis entre 2,7 y 3,3.
"""
from __future__ import annotations
import math, platform, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import fft, asd_grms

FS, N = 8192.0, 2 ** 15


def asd(f):
    if f < 20 or f > 2000:
        return 0.0
    if f <= 80:
        return 0.01 * (f / 20)
    if f <= 500:
        return 0.04
    return 0.04 * (500 / f)


def sintetizar(rng):
    df = FS / N
    X = [0j] * N
    for k in range(1, N // 2):
        f = k * df
        g = asd(f)
        if g > 0:
            amp = math.sqrt(g * df / 2) * N  # E[x^2] por componente = amp^2 * 2 / N^2 = g df
            ph = 2 * math.pi * rng.random()
            X[k] = amp * complex(math.cos(ph), math.sin(ph))
            X[N - k] = X[k].conjugate()
    # x[n] = (1/N) sum X_k e^{+2 pi i k n/N} -> usar FFT de la conjugada: x = conj(FFT(conj(X)))/N; la senal es real
    xc = fft([v.conjugate() for v in X])
    return [(v.conjugate()).real / N for v in xc]


def welch(x, nseg=2048):
    w = [0.5 - 0.5 * math.cos(2 * math.pi * i / nseg) for i in range(nseg)]
    sw = sum(v * v for v in w)
    paso = nseg // 2
    acc = [0.0] * (nseg // 2 + 1)
    cuenta = 0
    for s in range(0, len(x) - nseg + 1, paso):
        seg = [x[s + i] * w[i] for i in range(nseg)]
        X = fft(seg)
        for k in range(nseg // 2 + 1):
            acc[k] += abs(X[k]) ** 2
        cuenta += 1
    freqs = [k * FS / nseg for k in range(nseg // 2 + 1)]
    gest = [2 * a / (FS * sw * cuenta) for a in acc]
    gest[0] /= 2
    gest[-1] /= 2
    return freqs, gest, cuenta


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    perfil = [(20.0, 0.01), (80.0, 0.04), (500.0, 0.04), (2000.0, 0.01)]
    teorico = asd_grms(perfil)
    print(f"ASD de mano de obra minima (GEVS, Tabla 2.4-4): g rms teorico = {teorico:.4f} (publicado 6,8)")
    rng = random.Random(84032)
    x = sintetizar(rng)
    media = sum(x) / N
    var = sum((v - media) ** 2 for v in x) / N
    sd = math.sqrt(var)
    curt = sum((v - media) ** 4 for v in x) / N / var ** 2
    print(f"Senal SINTETICA de {N} muestras a {FS:.0f} Hz: media = {media:.4f} g, g rms = {sd:.4f} g (diferencia con el teorico {abs(sd - teorico) / teorico * 100:.2f} %)")
    pico = max(abs(v) for v in x)
    f3 = sum(1 for v in x if abs(v - media) > 3 * sd) / N
    print(f"Curtosis = {curt:.3f} (gaussiana: 3) ; pico absoluto = {pico:.3f} g = {pico / sd:.2f} sigma ; fraccion de muestras fuera de 3 sigma = {f3 * 100:.3f} % (gaussiana: 0,270 %)")
    fr, ge, nseg = welch(x)
    df = fr[1] - fr[0]
    grms_est = math.sqrt(sum(g * df for g in ge))
    print(f"Estimacion de Welch con {nseg} segmentos de 2048 muestras (resolucion {df:.1f} Hz): g rms de la ASD estimada = {grms_est:.4f}")
    print("ASD estimada frente a teorica en bandas (promedio por banda):")
    for f1, f2 in ((20, 80), (80, 200), (200, 500), (500, 1000), (1000, 2000)):
        ii = [k for k, f in enumerate(fr) if f1 <= f < f2]
        est = sum(ge[k] for k in ii) / len(ii)
        teo = sum(asd(fr[k]) for k in ii) / len(ii)
        print(f"  {f1:4d}-{f2:4d} Hz: estimada = {est:.5f}  teorica = {teo:.5f}  cociente = {est / teo:.3f}")
    # Incertidumbre estadistica: coeficiente de variacion de un bin ~ 1/sqrt(nseg_eff)
    print(f"Con {nseg} segmentos solapados el error aleatorio de cada bin es del orden de 1/sqrt({nseg}) = {1 / math.sqrt(nseg) * 100:.0f} % (mas por el solape)")
    assert abs(sd - teorico) / teorico < 0.03, sd
    assert abs(grms_est - teorico) / teorico < 0.03
    assert 2.7 < curt < 3.3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
