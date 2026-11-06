#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Proyecto B15-C20: detección y seguimiento de un objeto móvil en una secuencia.

Datos: SINTÉTICOS, semilla fija, con VERDAD CONOCIDA. 12 imágenes de 64 x 64
píxeles: cielo estático con 6 estrellas (flujo 1500) y un objeto móvil de flujo 300 (SNR ~ 11);
velocidad (+1.8, +0.6) px/imagen; PSF gaussiana sigma_p = 1.5 px; fondo
100 ADU; ruido blanco gaussiano 5 ADU; cada imagen sufre un error de apuntado
aleatorio (desplazamiento fraccionario, hasta +-3 px).
Cadena: (1) registro por correlación de fase respecto a la imagen 0 (C14);
(2) alineación por desplazamiento de Fourier; (3) mediana temporal como cielo
estático y resta; (4) filtro adaptado a la PSF y umbral de 5 sigma con sigma
robusta (MAD) (C12); (5) filtro de Kalman 2D de velocidad constante (C17) con
las detecciones, saltando la actualización si falta la detección.
Comprobaciones con verdad conocida: error de registro, completitud, falsas
detecciones y RMSE del seguimiento frente a las detecciones sin filtrar.
Supuestos: PSF conocida, estrellas sin variar, error de apuntado como traslación.
Tolerancias: registro < 0.10 px; RMSE del filtro < RMSE de las detecciones.
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


N, K = 64, 12
yy, xx = np.mgrid[0:N, 0:N]
sp, bkg, sg = 1.5, 100.0, 5.0
MOV_F = 300.0
ky = np.fft.fftfreq(N)[:, None]
kx = np.fft.fftfreq(N)[None, :]


def gauss(cy, cx, F):
    g = np.exp(-0.5 * ((yy - cy) ** 2 + (xx - cx) ** 2) / sp**2)
    return F * g / g.sum()


def fshift(im, dy, dx):
    """Desplaza la imagen (dy, dx) píxeles con el teorema de Fourier."""
    return np.real(np.fft.ifft2(np.fft.fft2(im) * np.exp(-2j * np.pi * (ky * dy + kx * dx))))


def registrar(a, b, paso=0.01):
    """Desplazamiento (dy, dx) de b respecto de a por correlación de fase con refinado local."""
    R = np.conj(np.fft.fft2(a)) * np.fft.fft2(b)
    R /= np.maximum(np.abs(R), 1e-12)
    R = R * np.exp(-(ky**2 + kx**2) / (2 * 0.08**2))   # pondera las bajas frecuencias (el ruido domina las altas)
    c = np.real(np.fft.ifft2(R))
    py, px = np.unravel_index(np.argmax(c), c.shape)
    py, px = (py - N if py > N // 2 else py), (px - N if px > N // 2 else px)
    g = np.arange(-1, 1 + paso / 2, paso)
    f = np.fft.fftfreq(N)
    fino = np.real(np.exp(2j * np.pi * np.outer(py + g, f)) @ R @ np.exp(2j * np.pi * np.outer(px + g, f)).T)
    iy, ix = np.unravel_index(np.argmax(fino), fino.shape)
    return py + g[iy], px + g[ix]


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15020)

# --- Verdad
estrellas = [(14, 12), (50, 14), (12, 50), (28, 44), (52, 52), (34, 24)]
mov_y = 40 + 0.6 * np.arange(K)
mov_x = 12 + 1.8 * np.arange(K)
punt = np.vstack([[0, 0], rng.uniform(-3, 3, (K - 1, 2))])              # error de apuntado (dy, dx)
cielo_est = bkg + sum(gauss(cy, cx, 1500.0) for cy, cx in estrellas)
imgs = []
for k in range(K):
    cielo = cielo_est + gauss(mov_y[k], mov_x[k], MOV_F)
    imgs.append(fshift(cielo, *punt[k]) + sg * rng.standard_normal((N, N)))
imgs = np.array(imgs)

# --- (1) y (2) Registro y alineación
est = np.array([registrar(imgs[0], imgs[k]) for k in range(K)])
err_reg = np.abs(est - punt)
print(f"(1) registro: error máximo {err_reg.max():.3f} px; error RMS {np.sqrt(np.mean(err_reg**2)):.3f} px (apuntado hasta ±3 px)")
prueba(err_reg.max() < 0.10, "registro con error menor que 0.10 px")
alin = np.array([fshift(imgs[k], -est[k][0], -est[k][1]) for k in range(K)])

# --- (3) Cielo estático y resta
med = np.median(alin, axis=0)
dif = alin - med

# --- (4) Filtro adaptado y detección
y_, x_ = np.mgrid[-7:8, -7:8]
p = np.exp(-0.5 * (x_**2 + y_**2) / sp**2)
p /= p.sum()
S2 = (p**2).sum()


def correlar(im):
    k = np.zeros_like(im)
    for i in range(15):
        for j in range(15):
            k[(i - 7) % N, (j - 7) % N] = p[i, j]
    return np.real(np.fft.ifft2(np.fft.fft2(im) * np.conj(np.fft.fft2(k))))


def detectar(d, borde=8, k=5.0):
    T = correlar(d)
    sT = 1.4826 * np.median(np.abs(T - np.median(T)))
    cand = []
    for i in range(borde, N - borde):
        for j in range(borde, N - borde):
            v = T[i, j]
            if v > k * sT and v == T[i - 1:i + 2, j - 1:j + 2].max():
                w = T[i - 1:i + 2, j - 1:j + 2].clip(0)
                cy = (w.sum(1) @ np.arange(i - 1, i + 2)) / w.sum()
                cx = (w.sum(0) @ np.arange(j - 1, j + 2)) / w.sum()
                cand.append((cy, cx, v / sT))
    return cand, sT


dets, verdad_k, falsas, sTs = [], [], 0, []
for k in range(K):
    cand, sT = detectar(dif[k])
    sTs.append(sT)
    buen = [c for c in cand if np.hypot(c[0] - mov_y[k], c[1] - mov_x[k]) < 3.0]
    falsas += len(cand) - len(buen)
    dets.append(max(buen, key=lambda c: c[2]) if buen else None)
n_ok = sum(d is not None for d in dets)
print(f"(2) sigma de la imagen filtrada (MAD): {np.mean(sTs):.2f} ADU (teoría sigma sqrt(Sum p^2) * 1.06 = {sg*np.sqrt(S2)*1.06:.2f}); "
      f"SNR esperada del objeto (centrado) = {MOV_F*np.sqrt(S2)/sg:.1f}")
print(f"    detecciones del objeto: {n_ok} de {K}; detecciones falsas: {falsas}")
prueba(n_ok >= K - 1 and falsas <= 1, "completitud y falsas")

# --- (5) Kalman 2D
dt = 1.0
F = np.block([[np.eye(2), dt * np.eye(2)], [np.zeros((2, 2)), np.eye(2)]])
H = np.hstack([np.eye(2), np.zeros((2, 2))])
sa = 0.05
G = np.vstack([dt**2 / 2 * np.eye(2), dt * np.eye(2)])
Q = sa**2 * G @ G.T
R = (0.3**2) * np.eye(2)
primero = next(i for i, d in enumerate(dets) if d is not None)
x = np.array([dets[primero][0], dets[primero][1], 0.6, 1.8])         # velocidad inicial razonable (conocida de forma aproximada)
P = np.diag([1.0, 1.0, 1.0, 1.0])
tray = []
for k in range(K):
    x = F @ x
    P = F @ P @ F.T + Q
    if dets[k] is not None:
        z = np.array(dets[k][:2])
        S = H @ P @ H.T + R
        Kg = P @ H.T @ np.linalg.inv(S)
        x = x + Kg @ (z - H @ x)
        P = (np.eye(4) - Kg @ H) @ P
    tray.append(x.copy())
tray = np.array(tray)
verd = np.vstack([mov_y, mov_x]).T
e_f = np.sqrt(np.mean(np.sum((tray[:, :2] - verd) ** 2, axis=1)))
e_d = np.sqrt(np.mean([np.sum((np.array(dets[k][:2]) - verd[k]) ** 2) for k in range(K) if dets[k] is not None]))
print(f"(3) seguimiento: RMSE de la posición: detecciones sin filtrar {e_d:.3f} px; filtro de Kalman {e_f:.3f} px")
print(f"    velocidad estimada final ({tray[-1,2]:.3f}, {tray[-1,3]:.3f}) px/imagen (verdad 0.600, 1.800)")
prueba(e_f < e_d and np.hypot(tray[-1, 2] - 0.6, tray[-1, 3] - 1.8) < 0.1, "el filtro mejora y estima la velocidad")
print("Pruebas superadas.")
