#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C06: periodograma, ventana de Hann, Welch y Lomb-Scargle.

Datos: SINTÉTICOS, semilla fija. Modelos y referencias analíticas:
 (1) con ventana de Hann periódica w[n] = 0.5 - 0.5 cos(2 pi n/N), suma(w) = N/2;
     un coseno de amplitud A en un bin entero da |X[k0]| = A * suma(w)/2 = A N/4;
 (2) el periodograma P[k] = |X[k]|^2/N de ruido blanco de varianza s^2 tiene
     media s^2 y distribución exponencial (desviación relativa 1); promediar K
     segmentos independientes la reduce a ~1/sqrt(K);
 (3) umbral de falsa alarma: P(P > z s^2) = exp(-z) por bin; con M bins
     independientes, FAP = 1 - (1 - exp(-z))^M;
 (4) Lomb-Scargle (scipy.signal.lombscargle, frecuencias angulares) recupera
     la frecuencia de una senoide con muestreo irregular.
Supuestos: ruido gaussiano blanco, señal estacionaria. Validez: N grande.
Tolerancias: 1e-9 en (1); 15 % en (2); intervalo estadístico en (3);
0.05 c/d (1/T = 0.037 c/d) en (4).
"""
import platform
import sys

import numpy as np
import scipy
from scipy.signal import lombscargle


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "|", platform.system())
rng = np.random.default_rng(15006)

# (1) Ventana de Hann y amplitud
N, k0, A = 1024, 64, 2.0
n = np.arange(N)
w = 0.5 - 0.5 * np.cos(2 * np.pi * n / N)
x = A * np.cos(2 * np.pi * k0 * n / N)
Xr = np.abs(np.fft.rfft(x))
Xh = np.abs(np.fft.rfft(x * w))
print(f"(1) |X[{k0}]| sin ventana = {Xr[k0]:.6f} (A N/2 = {A*N/2}); con Hann = {Xh[k0]:.6f} (A N/4 = {A*N/4})")
prueba(abs(Xr[k0] - A * N / 2) < 1e-9 and abs(Xh[k0] - A * N / 4) < 1e-9, "amplitudes con y sin Hann")

# Fuga con frecuencia fuera de bin
x2 = A * np.cos(2 * np.pi * 64.5 * n / N)
for nom, v in (("rectangular", x2), ("Hann", x2 * w)):
    X = np.abs(np.fft.rfft(v))
    pico = X.max()
    lejos = X[64 + 30:64 + 40].max()
    print(f"    {nom:12s}: pico {pico:.1f}; nivel a 30 bins del pico = {20*np.log10(lejos/pico):.1f} dB")
Xr2 = np.abs(np.fft.rfft(x2)); Xh2 = np.abs(np.fft.rfft(x2 * w))
dbr = 20 * np.log10(Xr2[94:104].max() / Xr2.max())
dbh = 20 * np.log10(Xh2[94:104].max() / Xh2.max())
prueba(dbh < dbr - 20, "Hann reduce la fuga lejana en más de 20 dB")

# (2) Varianza del periodograma y promedio de segmentos
L = 16384
z = rng.standard_normal(L)
P = np.abs(np.fft.rfft(z)[1:-1]) ** 2 / L
rel1 = P.std() / P.mean()
K = 16
seg = z.reshape(K, L // K)
Ps = (np.abs(np.fft.rfft(seg, axis=1)[:, 1:-1]) ** 2 / (L // K)).mean(axis=0)
relK = Ps.std() / Ps.mean()
print(f"(2) desviación relativa del periodograma: 1 segmento {rel1:.3f} (teoría 1); {K} segmentos {relK:.3f} (teoría {1/np.sqrt(K):.3f})")
prueba(abs(rel1 - 1) < 0.15 and abs(relK - 1 / np.sqrt(K)) < 0.15 * (1 / np.sqrt(K)), "varianza del periodograma")

# (3) Falsa alarma
M, Nn, reps = 1023, 2048, 3000
zumbral = np.log(M / 0.01)
cuenta = 0
for _ in range(reps):
    zz = rng.standard_normal(Nn)
    Pz = np.abs(np.fft.rfft(zz)[1:-1]) ** 2 / Nn
    cuenta += Pz.max() > zumbral
fap_teo = 1 - (1 - np.exp(-zumbral)) ** M
print(f"(3) umbral z = {zumbral:.2f} sigma^2; FAP teórica {fap_teo:.4f}; observada {cuenta/reps:.4f} ({cuenta}/{reps})")
esperado = fap_teo * reps
prueba(abs(cuenta - esperado) < 4 * np.sqrt(esperado), "tasa de falsa alarma")

# (4) Lomb-Scargle con muestreo irregular
T = 27.0
t = np.sort(rng.uniform(0, T, 300))
t = t[(t < 10) | (t > 12)]                 # hueco de 2 d
f_true, amp = 3.7, 0.5
y = amp * np.sin(2 * np.pi * f_true * t + 0.4) + 0.5 * rng.standard_normal(t.size)
f = np.linspace(0.05, 20, 4000)           # c/d
pgram = lombscargle(t, y - y.mean(), 2 * np.pi * f)
fp = f[np.argmax(pgram)]
print(f"(4) {t.size} puntos irregulares en {T:.0f} d; pico de Lomb-Scargle en {fp:.3f} c/d (verdadera {f_true}); 1/T = {1/T:.3f} c/d")
prueba(abs(fp - f_true) < 0.05, "Lomb-Scargle recupera la frecuencia")
print("Pruebas superadas.")
