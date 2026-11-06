#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C11: desenfoque como convolución y deconvolución de Richardson-Lucy.

Datos: SINTÉTICOS, semilla fija. Imagen de 64 x 64 con fondo 5 y tres fuentes
puntuales: dos de flujo 1000 en (x,y) = (30,32) y (34,32) (separación 4 px) y
una de 500 en (14,14). PSF gaussiana de sigma = 2 px (FWHM = 2.355 sigma =
4.71 px), normalizada (suma 1). Convolución circular por FFT (se declara).
Modelo: d = H * x (+ ruido de Poisson). Richardson-Lucy:
    x_{k+1} = x_k * ( (d / (H * x_k)) correlacionado con H ), x_0 = d.
Referencias analíticas: (a) con PSF normalizada y convolución circular la
suma (flujo total) se conserva en cada iteración; (b) sin ruido el error
disminuye; (c) con ruido hay un número óptimo de iteraciones; (d) el filtro
inverso divide por la función de transferencia, cuyo mínimo es exp(-2 pi^2
sigma^2 f^2) en f = 0.5 (Nyquist).
Supuestos: PSF conocida y uniforme; ruido de Poisson; fuentes positivas.
Tolerancias: 1e-8 en la conservación del flujo.
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


N = 64
sig = 2.0
yy, xx = np.mgrid[0:N, 0:N]


def psf_gauss():
    d2 = (np.minimum(xx, N - xx)) ** 2 + (np.minimum(yy, N - yy)) ** 2   # centrada en (0,0) para FFT circular
    p = np.exp(-0.5 * d2 / sig**2)
    return p / p.sum()


P = psf_gauss()
Hf = np.fft.fft2(P)


def conv(a):
    return np.real(np.fft.ifft2(np.fft.fft2(a) * Hf))


def corr(a):
    return np.real(np.fft.ifft2(np.fft.fft2(a) * np.conj(Hf)))


def rl(d, it, x0=None):
    x = d.copy() if x0 is None else x0
    out = {}
    for k in range(1, it + 1):
        est = conv(x)
        x = x * corr(d / np.maximum(est, 1e-12))
        out[k] = x
    return out


def rms(a, b):
    return float(np.sqrt(np.mean((a - b) ** 2)))


def picos_fila(img, y=32, x0=24, x1=40):
    f = img[y, x0:x1]
    return int(np.sum((f[1:-1] > f[:-2]) & (f[1:-1] > f[2:])))


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15011)
verdad = np.full((N, N), 5.0)
for (x, y, F) in ((30, 32, 1000.0), (34, 32, 1000.0), (14, 14, 500.0)):
    verdad[y, x] += F
borrosa = conv(verdad)
print(f"FWHM = {2.3548*sig:.2f} px; separación de las dos fuentes = 4 px; flujo total = {verdad.sum():.0f}")
print(f"mín |H| = {np.abs(Hf).min():.2e} (teoría en la esquina de Fourier, exp(-2 pi^2 sigma^2 (0.25+0.25)) = {np.exp(-2*np.pi**2*sig**2*0.5):.2e})")

# --- Sin ruido
res = rl(borrosa, 300)
sumas = [res[k].sum() for k in (1, 10, 100, 300)]
print(f"(1) sin ruido: suma de la imagen borrosa {borrosa.sum():.6f}; tras 1/10/100/300 it.: "
      + ", ".join(f"{s:.6f}" for s in sumas))
prueba(all(abs(s - borrosa.sum()) < 1e-8 * borrosa.sum() for s in sumas), "conservación del flujo")
print(f"    máximos locales entre x=24..40 en la fila 32: borrosa {picos_fila(borrosa)}, "
      f"10 it. {picos_fila(res[10])}, 100 it. {picos_fila(res[100])}, 300 it. {picos_fila(res[300])}")
print(f"    error RMS respecto a la verdad: borrosa {rms(borrosa, verdad):.3f}; 10 it. {rms(res[10], verdad):.3f}; "
      f"100 it. {rms(res[100], verdad):.3f}; 300 it. {rms(res[300], verdad):.3f}")
print(f"    valor del píxel de la fuente aislada (14,14): verdad {verdad[14,14]:.0f}; borrosa {borrosa[14,14]:.1f}; "
      f"10 it. {res[10][14,14]:.1f}; 100 it. {res[100][14,14]:.1f}; 300 it. {res[300][14,14]:.1f}")
prueba(picos_fila(borrosa) == 1 and picos_fila(res[100]) == 2, "se resuelven las dos fuentes")
prueba(rms(res[300], verdad) < rms(borrosa, verdad), "el error baja sin ruido")

# --- Con ruido de Poisson
datos = rng.poisson(borrosa).astype(float)
res = rl(datos, 1000)
print("(2) con ruido de Poisson: error RMS respecto a la verdad")
errores = {0: rms(datos, verdad)}
print(f"    datos borrosos y ruidosos: {errores[0]:.3f}")
for k in (5, 10, 20, 50, 100, 200, 500, 1000):
    errores[k] = rms(res[k], verdad)
    print(f"    {k:4d} iteraciones: {errores[k]:.3f}   (máx. {res[k].max():.0f}, mín. {res[k].min():.2f})")
kmin = min(range(1, 1001), key=lambda k: rms(res[k], verdad))
print(f"    mínimo del error en {kmin} iteraciones: {rms(res[kmin], verdad):.3f}")
prueba(errores[1000] > rms(res[kmin], verdad) * 1.1, "demasiadas iteraciones amplifican el ruido")
prueba(rms(res[kmin], verdad) < errores[0], "RL mejora a los datos si se detiene a tiempo")

# --- Filtro inverso
inv = np.real(np.fft.ifft2(np.fft.fft2(datos) / Hf))
print(f"(3) filtro inverso con ruido: error RMS {rms(inv, verdad):.3e} (datos: {errores[0]:.3f})")
prueba(rms(inv, verdad) > 5 * errores[0], "el filtro inverso amplifica el ruido")

# --- Enfoque: el pico normalizado depende de sigma
for s in (1.0, 1.5, 2.0):
    print(f"(4) PSF gaussiana sigma = {s}: FWHM {2.3548*s:.2f} px; valor máximo de la PSF normalizada = {1/(2*np.pi*s*s):.4f}")
print("Pruebas superadas.")
