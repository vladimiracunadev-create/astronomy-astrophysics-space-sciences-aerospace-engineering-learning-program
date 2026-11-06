#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C12: detección de fuentes con filtro adaptado y umbral.

Datos: SINTÉTICOS, semilla fija. Imagen de 200 x 200 con fondo 100 ADU, ruido
gaussiano blanco de sigma = 5 ADU y fuentes puntuales con PSF gaussiana
normalizada de sigma_p = 1.5 px (Sum p = 1).
Modelo: imagen filtrada T = p (correlación) (d - fondo). Para ruido blanco,
std(T) = sigma sqrt(Sum p^2). Una fuente de flujo F centrada en un píxel da
T = F Sum p^2 en ese píxel, es decir una relación señal-ruido
SNR = F sqrt(Sum p^2)/sigma. Con umbral T > k std(T), la probabilidad de
detectar es Phi(SNR - k) y la de falsa alarma por píxel es 1 - Phi(k).
Supuestos: ruido gaussiano blanco conocido; PSF conocida; fuentes aisladas.
Tolerancias: 3 % en std(T); 3 desviaciones binomiales en las tasas.
"""
import math
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def Phi(z):
    return 0.5 * math.erfc(-z / math.sqrt(2))


def corr_fft(img, ker):
    """Correlación circular con un núcleo simétrico mediante FFT."""
    n = img.shape[0]
    k = np.zeros_like(img)
    h = ker.shape[0] // 2
    for i in range(ker.shape[0]):
        for j in range(ker.shape[1]):
            k[(i - h) % n, (j - h) % n] = ker[i, j]
    return np.real(np.fft.ifft2(np.fft.fft2(img) * np.conj(np.fft.fft2(k))))


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15012)
N, bkg, sg, sp = 200, 100.0, 5.0, 1.5
y, x = np.mgrid[-7:8, -7:8]
p = np.exp(-0.5 * (x**2 + y**2) / sp**2)
p /= p.sum()
S2 = (p**2).sum()
print(f"Sum p^2 = {S2:.5f} (aprox. continua 1/(4 pi sigma_p^2) = {1/(4*np.pi*sp**2):.5f}); "
      f"std(T) esperada = {sg*math.sqrt(S2):.4f} ADU")

# (1) Ruido del filtrado
sT = sg * math.sqrt(S2)
medidas = []
for _ in range(10):
    ruido = bkg + sg * rng.standard_normal((N, N))
    medidas.append(corr_fft(ruido - bkg, p).std())
print(f"(1) std(T) medida = {np.mean(medidas):.4f} (esperada {sT:.4f})")
prueba(abs(np.mean(medidas) / sT - 1) < 0.03, "ruido del filtro adaptado")

# (2) Falsas alarmas por píxel
k = 4.0
cuentas = 0
reps = 100
for _ in range(reps):
    T = corr_fft(sg * rng.standard_normal((N, N)), p)
    cuentas += int(np.sum(T > k * sT))
esp = N * N * reps * (1 - Phi(k))
print(f"(2) píxeles sobre {k:.0f} sigma en {reps} imágenes de ruido: {cuentas} (esperados {esp:.0f})")
prueba(abs(cuentas - esp) < 0.4 * esp, "tasa de falsa alarma por píxel")

# (3) Completitud
print("(3) completitud con umbral 4 sigma (fuentes centradas en un píxel):")
paso = 20
centros = [(i, j) for i in range(10, N, paso) for j in range(10, N, paso)]
for snr in (3, 4, 5, 6, 7):
    F = snr * sg / math.sqrt(S2)
    det = tot = 0
    for _ in range(40):
        d = sg * rng.standard_normal((N, N))
        for (i, j) in centros:
            d[i - 7:i + 8, j - 7:j + 8] += F * p
        T = corr_fft(d, p)
        for (i, j) in centros:
            det += T[i, j] > k * sT
            tot += 1
    f = det / tot
    teo = Phi(snr - k)
    print(f"    SNR = {snr}: flujo {F:6.1f} ADU; detectadas {f:.3f}; teórico {teo:.3f}")
    prueba(abs(f - teo) < 3 * math.sqrt(teo * (1 - teo) / tot) + 0.01, f"completitud SNR={snr}")

# (4) Fondo robusto
d = bkg + sg * rng.standard_normal((N, N))
for (i, j) in centros:
    d[i - 7:i + 8, j - 7:j + 8] += 1000.0 * p
med = np.median(d)
mad = 1.4826 * np.median(np.abs(d - med))
m, s_ = d.mean(), d.std()
for _ in range(10):                      # recorte iterativo a 3 sigma
    sel = np.abs(d - m) < 3 * s_
    m, s_ = d[sel].mean(), d[sel].std()
print(f"(4) con {len(centros)} fuentes brillantes (fondo real {bkg}, sigma real {sg}):")
print(f"    media {d.mean():.2f}; mediana {med:.2f}; media con recorte a 3 sigma {m:.2f}")
print(f"    sigma: desviación global {d.std():.2f}; robusta (MAD) {mad:.2f}; con recorte {s_:.2f}")
prueba(abs(d.mean() - bkg) > abs(med - bkg) > abs(m - bkg), "mejor orden de sesgos: media, mediana, recorte")
prueba(abs(m - bkg) < 0.6 and abs(s_ - sg) < 0.3, "el recorte acerca fondo y sigma")
print("Pruebas superadas.")
