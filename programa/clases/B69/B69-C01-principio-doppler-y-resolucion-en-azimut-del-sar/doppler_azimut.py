#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B69-C01: principio Doppler y resolucion en azimut de un SAR (sensor SINTETICO tipo banda C).

Datos: ningun dato observado. Parametros ILUSTRATIVOS (no son los de un satelite real): lambda = 0.0555 m, v = 7100 m/s, R0 = 850 km, antena de L = 12 m, PRF = 1700 Hz.
Sistema de referencia: ejes del sensor; x = direccion de vuelo (azimut, m), tiempo lento t en s con t = 0 en el punto de maxima aproximacion; R0 = distancia oblicua minima (m).
Modelo: blanco puntual; distancia R(t) = sqrt(R0^2 + (v t)^2); fase de ida y vuelta phi(t) = -4 pi R(t)/lambda (rad); frecuencia Doppler f_D = -(1/2pi) dphi/dt = 2 v^2 t/(lambda R(t)).
Aproximacion parabolica: f_D ~ +Ka t con Ka = 2 v^2/(lambda R0) en Hz/s (positivo despues de la maxima aproximacion: el blanco se aleja). Haz de ancho theta = lambda/L; tiempo de iluminacion T = lambda R0/(L v).
Supuestos: sin migracion de celda en alcance, antena uniforme, sin ruido. Validez: T v << R0.
Tolerancias: Ka numerico frente al analitico 1 %; ancho a -3 dB frente a 0.886 v/Ba 3 %; resolucion frente a L/2 3 %.
"""
from __future__ import annotations
import platform
import numpy as np

lam, v, R0, L, PRF = 0.0555, 7100.0, 850e3, 12.0, 1700.0
T = lam * R0 / (L * v)            # s, tiempo de iluminacion
Ka = 2 * v**2 / (lam * R0)        # Hz/s
Ba = Ka * T                       # Hz, ancho de banda Doppler
res_teo = L / 2                   # m, resolucion de azimut teorica (limite de la apertura)

def check(cond, msg):
    if not cond:
        raise SystemExit("FALLA: " + msg)

print(f"Python {platform.python_version()} ; numpy {np.__version__}")
print(f"T = {T:.4f} s ; Ka = {Ka:.2f} Hz/s ; Ba = {Ba:.1f} Hz ; 2v/L = {2*v/L:.1f} Hz ; PRF = {PRF:.0f} Hz")

# Fase exacta y frecuencia Doppler por diferencia finita
fs = 8 * PRF                      # muestreo denso para derivar
t = np.arange(-T / 2, T / 2, 1 / fs)
R = np.sqrt(R0**2 + (v * t) ** 2)
phi = -4 * np.pi * R / lam
fD = -np.gradient(phi, t) / (2 * np.pi)
ka_num = np.polyfit(t, fD, 1)[0]
check(abs(ka_num / Ka - 1) < 0.01, "Ka numerico")
print(f"Ka numerico = {ka_num:.2f} Hz/s (error {100*(ka_num/Ka-1):+.3f} %)")
print(f"Doppler en los bordes del haz: {fD[0]:.1f} y {fD[-1]:.1f} Hz (ancho {fD[-1]-fD[0]:+.1f} Hz)")
check(abs(abs(fD[-1] - fD[0]) / Ba - 1) < 0.01, "ancho de banda Doppler")

# Muestreo en azimut: PRF >= Ba
check(PRF >= Ba, "PRF insuficiente (aliasing)")
print(f"PRF/Ba = {PRF/Ba:.2f} (>1: sin aliasing)")

# Compresion en azimut: filtro adaptado sobre el eco de un blanco
ts = np.arange(-T / 2, T / 2, 1 / PRF)
Rs = np.sqrt(R0**2 + (v * ts) ** 2)
eco = np.exp(-1j * 4 * np.pi * Rs / lam)
N = 1 << 16
H = np.fft.fft(eco, N)
P = np.fft.fftshift(np.abs(H) ** 2)      # espectro de potencia (la salida es su transformada inversa)
UP = 32                                   # interpolacion de Fourier de la salida (UP veces mas fina)
Pp = np.zeros(N * UP)
Pp[(N * UP - N) // 2:(N * UP + N) // 2] = P
y = np.abs(np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(Pp))))
y /= y.max()
dt = 1 / (PRF * UP)
k0 = int(np.argmax(y))
mitad = np.where(y[k0:] < 10 ** (-3 / 20))[0][0]          # -3 dB (potencia 1/2, amplitud 0.708)
a, b = y[k0 + mitad - 1], y[k0 + mitad]
x3 = (mitad - 1) + (a - 10 ** (-3 / 20)) / (a - b)
ancho_t = 2 * x3 * dt                    # s
ancho_m = ancho_t * v                    # m (azimut en tierra ~ v t)
teo = 0.886 * v / Ba
print(f"Ancho a -3 dB = {ancho_m:.3f} m ; teorico 0.886 v/Ba = {teo:.3f} m ; L/2 = {res_teo:.2f} m")
check(abs(ancho_m / teo - 1) < 0.03, "ancho -3 dB")
check(abs(v / Ba / res_teo - 1) < 0.01, "v/Ba = L/2")

# La resolucion no depende de la distancia ni de la longitud de onda
for R0b in (400e3, 850e3, 1200e3):
    Tb = lam * R0b / (L * v)
    Bab = (2 * v**2 / (lam * R0b)) * Tb
    print(f"R0 = {R0b/1e3:6.0f} km -> T = {Tb:.3f} s ; Ba = {Bab:.1f} Hz ; v/Ba = {v/Bab:.3f} m")
    check(abs(v / Bab / res_teo - 1) < 1e-9, "independencia de R0")

# Comparacion con apertura real: longitud de antena necesaria para 6 m a R0
L_real = lam * R0 / res_teo
print(f"Apertura real equivalente para {res_teo:.1f} m a {R0/1e3:.0f} km: {L_real:.0f} m ; apertura sintetica v T = {v*T:.0f} m")
check(abs(v * T - lam * R0 / L) < 1e-6, "apertura sintetica")
print("Pruebas superadas.")
