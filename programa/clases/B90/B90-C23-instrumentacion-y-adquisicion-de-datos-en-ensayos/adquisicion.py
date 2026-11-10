#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C23: muestreo, aliasing, cuantizacion y sensibilidad de un acelerometro en un ensayo (SINTETICO).

Una senal senoidal de f0 muestreada a fs aparece en f_alias = |f0 - round(f0/fs) fs|. SNR ideal de un cuantizador de N bits con senoide a plena escala:
6.02 N + 1.76 dB, comprobada con una senoide cuantizada. Acelerometro: V = S a (S en mV/g). Unidades: Hz, g, mV, V, bits. Tolerancias: FFT a 1 bin; SNR 0.5 dB.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: ensayo de vibracion con banda de interes de 20 a 2000 Hz")
fs_bueno, fs_malo = 8192.0, 2048.0
f0 = 1500.0
dur = 1.0

def pico_fft(fs, f0):
    t = np.arange(int(fs * dur)) / fs
    x = np.sin(2 * math.pi * f0 * t)
    X = np.abs(np.fft.rfft(x * np.hanning(len(x))))
    return np.fft.rfftfreq(len(x), 1 / fs)[int(np.argmax(X))]

for fs in (fs_bueno, fs_malo, 2000.0):
    ap = pico_fft(fs, f0)
    esp = abs(f0 - round(f0 / fs) * fs)
    print(f"fs = {fs:7.0f} Hz ; tono de {f0:.0f} Hz aparece en {ap:7.1f} Hz (esperado {esp:7.1f} Hz) ; Nyquist = {fs / 2:.0f} Hz")
    comprobar(abs(ap - esp) <= 1.0 / dur, "la frecuencia aparente debe coincidir con la de aliasing")
print("Regla: fs >= 2 x banda; con filtro antialias de orden 4 y corte 2000 Hz, atenuacion en f:")
for f in (2000, 3000, 4000, 6144):
    h = 1 / math.sqrt(1 + (f / 2000.0) ** 8)
    print(f"   {f} Hz: {20 * math.log10(h):6.1f} dB")
print("Resolucion: N bits -> SNR ideal [dB] ; medida con senoide cuantizada")
for N in (8, 12, 16, 24):
    t = np.arange(65536) / 65536.0
    x = 0.999 * np.sin(2 * math.pi * 1013 * t)
    q = 2.0 / 2**N
    xq = np.round(x / q) * q
    snr = 10 * math.log10(np.mean(x**2) / np.mean((xq - x) ** 2))
    print(f"   {N:2d} -> {6.02 * N + 1.76:6.2f} ; {snr:6.2f}")
    comprobar(abs(snr - (6.02 * N + 1.76)) < 0.5, "la SNR medida debe seguir 6.02 N + 1.76")
S = 10.0                       # mV/g
rango_g, rango_V = 50.0, 5.0
print(f"Acelerometro: S = {S} mV/g ; 5 g rms -> {S * 5:.1f} mV ; plena escala del ADC {rango_V} V corresponde a {rango_V * 1000 / S:.0f} g")
for N in (12, 16):
    q_V = 2 * rango_V / 2**N
    print(f"   LSB con {N} bits en +-{rango_V} V = {q_V * 1000:.4f} mV = {q_V * 1000 / S * 1000:.2f} mg")
g_rms_min = 0.5
print(f"Ruido de cuantizacion con 16 bits: {q_V / math.sqrt(12) * 1000 / S * 1000:.3f} mg rms frente a {g_rms_min * 1000:.0f} mg de la senal minima")
comprobar(q_V / math.sqrt(12) * 1000 / S < 0.01 * g_rms_min, "el ruido de cuantizacion debe ser menor que 1 % de la senal minima")
fin()
