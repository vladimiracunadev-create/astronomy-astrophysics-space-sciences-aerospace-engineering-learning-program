#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B69-C02: formacion de una imagen SAR (compresion en alcance y en azimut) con tres blancos puntuales SINTETICOS.

Datos: ningun dato observado. Parametros ILUSTRATIVOS tipo banda C: lambda = 0.0555 m, v = 7100 m/s, R0 = 850 km, L = 12 m, PRF = 1700 Hz,
chirp de alcance de ancho de banda B = 56 MHz, duracion tau = 10 us, muestreo fs = 64 MHz, c = 299 792 458 m/s (definicion SI).
Sistema de referencia: alcance oblicuo r (m) respecto del inicio de la ventana; azimut x = v t (m) respecto del instante central del bloque.
Modelo (con correccion de migracion de celda, RCMC, en el dominio alcance-Doppler: dR = lambda^2 R0 fD^2/(8 v^2), y comparacion con la imagen sin ella): eco crudo = suma de blancos con amplitud A_k, retardo 2 R_k(t)/c y fase -4 pi R_k(t)/lambda; compresion en alcance con filtro adaptado por FFT y compresion
en azimut con filtro adaptado en cada celda de alcance (se calcula la migracion de celda y se compara con la celda).
Supuestos: sin ruido, antena uniforme (envolvente rectangular en azimut), sin ventana espectral. Validez: migracion de celda de ~1 celda; se corrige con RCMC.
Tolerancias: amplitudes relativas 6 %; posicion del pico dentro de 1 pixel; anchura a -3 dB frente a 0.886/B (alcance) y 0.886 v/Ba (azimut) 5 %; PSLR de un sinc sin ventana -13.26 dB +- 0.7 dB.
"""
from __future__ import annotations
import platform
import numpy as np

c = 299_792_458.0
lam, v, R0, L, PRF = 0.0555, 7100.0, 850e3, 12.0, 1700.0
B, tau, fs = 56e6, 10e-6, 64e6
T = lam * R0 / (L * v)
Ka = 2 * v**2 / (lam * R0)
Ba = Ka * T

def check(cond, msg):
    if not cond:
        raise SystemExit("FALLA: " + msg)

print(f"Python {platform.python_version()} ; numpy {np.__version__}")
# Migracion de celda en alcance a lo largo de la apertura
dR = np.sqrt(R0**2 + (v * T / 2) ** 2) - R0
res_r = c / (2 * B)
print(f"Migracion de celda = {dR:.3f} m ; celda de alcance c/2B = {res_r:.3f} m ; cociente = {dR/res_r:.2f}")
check(dR < res_r, "migracion de celda mayor que la celda")

# Rejillas
Nr, Na = 1024, 2048
ts = (np.arange(Na) - Na // 2) / PRF            # tiempo lento
tr = np.arange(Nr) / fs                          # tiempo rapido (relativo al retardo de referencia)
kr = B / tau                                     # tasa del chirp (Hz/s)
# Blancos: (alcance relativo en m, azimut en m, amplitud)
blancos = [(300.0, 0.0, 1.0), (600.0, 150.0, 0.7), (450.0, -200.0, 0.5)]
raw = np.zeros((Na, Nr), dtype=complex)
for rk, xk, ak in blancos:
    tk = ts - xk / v                             # el blanco esta en maxima aproximacion en t = xk/v
    Rt = np.sqrt(R0**2 + (v * tk) ** 2) - R0     # distancia relativa a R0 (m)
    ill = np.abs(tk) <= T / 2                    # iluminado por el haz
    retardo = 2 * (rk + Rt) / c                  # s
    for i in np.where(ill)[0]:
        u = tr - retardo[i]
        env = (np.abs(u - tau / 2) <= tau / 2)
        raw[i] += ak * env * np.exp(1j * np.pi * kr * (u - tau / 2) ** 2) * np.exp(-1j * 4 * np.pi * (R0 + rk + Rt[i]) / lam)

# Compresion en alcance (filtro adaptado en la frecuencia)
ref = (np.abs(tr - tau / 2) <= tau / 2) * np.exp(1j * np.pi * kr * (tr - tau / 2) ** 2)
Href = np.conj(np.fft.fft(ref))
rc = np.fft.ifft(np.fft.fft(raw, axis=1) * Href[None, :], axis=1)
# Compresion en azimut, con o sin correccion de la migracion de celda (RCMC) en el dominio alcance-Doppler
Tref = np.arange(-T / 2, T / 2, 1 / PRF)
fD = np.fft.fftfreq(Na, 1 / PRF)                 # Hz
fr = np.fft.fftfreq(Nr, 1 / fs)                  # Hz
dR_fD = lam**2 * R0 * fD**2 / (8 * v**2)         # m, migracion en funcion del Doppler

def azimut(rcmc):
    RC = np.fft.fft(rc, axis=0)
    if rcmc:
        RCr = np.fft.fft(RC, axis=1) * np.exp(1j * 2 * np.pi * fr[None, :] * (2 * dR_fD[:, None] / c))
        RC = np.fft.ifft(RCr, axis=1)
    out = np.empty_like(rc)
    for ir in range(Nr):
        Rcel = R0 + c * ir / (2 * fs)
        Ha = np.conj(np.fft.fft(np.exp(-1j * 4 * np.pi * (np.sqrt(Rcel**2 + (v * Tref) ** 2) - Rcel) / lam), Na))
        out[:, ir] = np.fft.ifft(RC[:, ir] * Ha)
    return out

img_sin = azimut(False)
img = azimut(True)
mag = np.abs(img)

dr_pix = c / (2 * fs)                            # m por muestra de alcance
dx_pix = v / PRF                                 # m por muestra de azimut
print(f"Pixel de alcance = {dr_pix:.3f} m ; pixel de azimut = {dx_pix:.3f} m")

# Se busca el maximo global y los demas por separado, enmascarando alrededor
m = mag.copy()
picos = []
for _ in range(3):
    j = np.unravel_index(np.argmax(m), m.shape)
    picos.append((j[0], j[1], mag[j]))
    m[max(j[0] - 30, 0):j[0] + 30, max(j[1] - 60, 0):j[1] + 60] = 0
picos.sort(key=lambda p: -p[2])
print("Picos (indice azimut, indice alcance, amplitud relativa al maximo):")
for ia, ir, a in picos:
    print(f"  ({ia:4d}, {ir:4d})  {a/picos[0][2]:.3f}")
# Amplitud con interpolacion de Fourier en azimut (evita la perdida por pico entre muestras)
def _perfil(vec, UP=16):
    n = len(vec)
    F = np.fft.fftshift(np.fft.fft(vec))
    Fp = np.zeros(n * UP, dtype=complex)
    Fp[(n * UP - n) // 2:(n * UP + n) // 2] = F
    return np.abs(np.fft.ifft(np.fft.ifftshift(Fp)))
amp = [_perfil(np.take(img[:, ir_], np.arange(ia_ - 64, ia_ + 64), mode="wrap")).max() for ia_, ir_, _ in picos]
print("Amplitudes interpoladas relativas:", ", ".join(f"{a/amp[0]:.3f}" for a in amp))
rel = sorted([a / amp[0] for a in amp], reverse=True)
check(all(abs(r / e - 1) < 0.06 for r, e in zip(rel, (1.0, 0.7, 0.5))), "amplitudes relativas (tolerancia 6 %: rejilla de muestreo)")
# Separaciones entre picos frente a las geometricas (en pixeles)
ia0, ir0 = picos[0][0], picos[0][1]
esp = [(0, 0), ((150.0 - 0.0) / dx_pix, (600 - 300) * 2 / c * fs), ((-200.0 - 0.0) / dx_pix, (450 - 300) * 2 / c * fs)]
for k in (1, 2):
    da = picos[k][0] - ia0
    da = (da + Na // 2) % Na - Na // 2
    dr = picos[k][1] - ir0
    print(f"  separacion del pico {k+1}: azimut {da:+d} pix (esperado {esp[k][0]:+.1f}) ; alcance {dr:+d} pix (esperado {esp[k][1]:+.1f})")
    check(abs(da - esp[k][0]) <= 1.0 and abs(dr - esp[k][1]) <= 1.0, f"posicion del pico {k+1}")

# Anchura a -3 dB y PSLR del blanco principal (interpolacion de Fourier x16 en cada eje)
def perfil(vec, UP=16):
    n = len(vec)
    F = np.fft.fftshift(np.fft.fft(vec))
    Fp = np.zeros(n * UP, dtype=complex)
    Fp[(n * UP - n) // 2:(n * UP + n) // 2] = F
    return np.abs(np.fft.ifft(np.fft.ifftshift(Fp)))

def anchura(p, paso):
    k = int(np.argmax(p)); p = p / p[k]
    d = np.where(p[k:] < 10 ** (-3 / 20))[0][0]
    i = np.where(p[k::-1] < 10 ** (-3 / 20))[0][0]
    a = (d - 1) + (p[k + d - 1] - 10 ** (-3 / 20)) / (p[k + d - 1] - p[k + d])
    b = (i - 1) + (p[k - i + 1] - 10 ** (-3 / 20)) / (p[k - i + 1] - p[k - i])
    return (a + b) * paso

def pslr(p):
    k = int(np.argmax(p)); p = p / p[k]
    # primer minimo a la derecha, luego el maximo del lobulo lateral
    d = k
    while p[d + 1] < p[d]:
        d += 1
    lat = p[d:d + 16 * 40].max()
    return 20 * np.log10(lat)

ia, ir = picos[0][0], picos[0][1]
cut_r = np.roll(img[ia, :], 0)[ir - 64:ir + 64] if ir >= 64 else img[ia, :128]
cut_a = np.take(img[:, ir], np.arange(ia - 64, ia + 64), mode="wrap")
pr_ = perfil(cut_r); pa_ = perfil(cut_a)
w_r = anchura(pr_, dr_pix / 16)
w_a = anchura(pa_, dx_pix / 16)
t_r, t_a = 0.886 * c / (2 * B), 0.886 * v / Ba
print(f"Anchura a -3 dB en alcance = {w_r:.3f} m (teorica 0.886 c/2B = {t_r:.3f} m)")
print(f"Anchura a -3 dB en azimut  = {w_a:.3f} m (teorica 0.886 v/Ba = {t_a:.3f} m)")
# Ancho de azimut sin RCMC (mismo blanco principal)
mag_sin = np.abs(img_sin)
ia_s, ir_s = np.unravel_index(np.argmax(mag_sin), mag_sin.shape)
w_a_sin = anchura(perfil(np.take(img_sin[:, ir_s], np.arange(ia_s - 64, ia_s + 64), mode="wrap")), dx_pix / 16)
print(f"Anchura de azimut SIN correccion de migracion = {w_a_sin:.3f} m ; CON correccion = {w_a:.3f} m")
check(w_a_sin > 1.1 * w_a, "la migracion sin corregir deberia ensanchar")
check(abs(w_r / t_r - 1) < 0.05, "anchura de alcance")
check(abs(w_a / t_a - 1) < 0.05, "anchura de azimut")
ps_r, ps_a = pslr(pr_), pslr(pa_)
print(f"PSLR alcance = {ps_r:.2f} dB ; azimut = {ps_a:.2f} dB (sinc teorico -13.26 dB)")
check(abs(ps_r + 13.26) < 0.7 and abs(ps_a + 13.26) < 0.7, "PSLR")
print("Pruebas superadas.")
