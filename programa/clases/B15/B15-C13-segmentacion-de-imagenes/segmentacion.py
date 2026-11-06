#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C13: umbralización de Otsu, regiones conectadas y métricas.

Datos: SINTÉTICOS, semilla fija. Disco solar ficticio de 160 x 160 píxeles
(radio 70 px) con oscurecimiento hacia el borde, I = 1000 (0.4 + 0.6 mu),
mu = sqrt(1 - (r/R)^2), y tres manchas oscuras (0.35 de la intensidad local)
de radios 4, 6 y 3 px; ruido gaussiano de 20 unidades.
Referencias analíticas: (1) para una mezcla 50/50 de N(0,1) y N(4,1) el umbral
óptimo es 2; (2) tres cuadrados separados son 3 regiones y dos píxeles
en diagonal son 2 con conectividad 4 y 1 con conectividad 8; (3) para dos
cuadrados 10 x 10 desplazados 2 columnas, IoU = 80/120 y Dice = 160/200.
Contraste independiente: scipy.ndimage.label.
Supuestos: el disco es conocido; las manchas son más oscuras que la fotosfera.
Tolerancias: 0.05 en Otsu (1); igualdad exacta en conteos y métricas.
"""
import platform
import sys
from collections import deque

import numpy as np
import scipy
from scipy import ndimage


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def otsu(x, bins=256):
    h, e = np.histogram(x, bins=bins)
    c = 0.5 * (e[:-1] + e[1:])
    w0 = np.cumsum(h)
    w1 = w0[-1] - w0
    m0 = np.cumsum(h * c) / np.maximum(w0, 1)
    m1 = (np.sum(h * c) - np.cumsum(h * c)) / np.maximum(w1, 1)
    sb = w0 * w1 * (m0 - m1) ** 2
    return c[np.argmax(sb[:-1])]


def etiquetar(b, conectividad):
    """BFS propio; conectividad 4 u 8. Devuelve etiquetas y número de regiones."""
    H, W = b.shape
    lab = np.zeros((H, W), int)
    vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if conectividad == 8:
        vec += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    n = 0
    for i in range(H):
        for j in range(W):
            if b[i, j] and not lab[i, j]:
                n += 1
                q = deque([(i, j)])
                lab[i, j] = n
                while q:
                    a, c = q.popleft()
                    for da, dc in vec:
                        u, v = a + da, c + dc
                        if 0 <= u < H and 0 <= v < W and b[u, v] and not lab[u, v]:
                            lab[u, v] = n
                            q.append((u, v))
    return lab, n


def iou(a, b):
    return (a & b).sum() / (a | b).sum()


def dice(a, b):
    return 2 * (a & b).sum() / (a.sum() + b.sum())


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "|", platform.system())
rng = np.random.default_rng(15013)

# (1) Otsu en una mezcla con óptimo conocido
m = np.concatenate([rng.normal(0, 1, 100000), rng.normal(4, 1, 100000)])
t = otsu(m)
print(f"(1) Otsu en mezcla N(0,1)/N(4,1): umbral {t:.3f} (óptimo 2)")
prueba(abs(t - 2) < 0.05, "Otsu en la mezcla")

# (2) Conectividad y comparación con SciPy
b = np.zeros((12, 12), bool)
b[1:4, 1:4] = b[1:4, 7:10] = b[7:10, 4:7] = True
_, n4 = etiquetar(b, 4)
d = np.zeros((6, 6), bool)
d[1, 1] = d[2, 2] = True
_, d4 = etiquetar(d, 4)
_, d8 = etiquetar(d, 8)
print(f"(2) tres cuadrados: {n4} regiones; dos píxeles en diagonal: {d4} (c4) y {d8} (c8)")
prueba(n4 == 3 and d4 == 2 and d8 == 1, "conteos de regiones")
aleat = rng.random((60, 60)) < 0.45
for c, st in ((4, None), (8, np.ones((3, 3)))):
    _, na = etiquetar(aleat, c)
    _, nb = ndimage.label(aleat, structure=st)
    print(f"    imagen aleatoria 60x60, conectividad {c}: propio {na}, scipy {nb}")
    prueba(na == nb, f"coincide con scipy (c{c})")

# (3) Métricas
A = np.zeros((30, 30), bool); A[5:15, 5:15] = True
B = np.zeros((30, 30), bool); B[5:15, 7:17] = True
print(f"(3) cuadrados 10x10 desplazados 2 columnas: IoU {iou(A,B):.4f} (80/120 = {80/120:.4f}); Dice {dice(A,B):.4f} (160/200 = 0.8000)")
prueba(abs(iou(A, B) - 80 / 120) < 1e-12 and abs(dice(A, B) - 0.8) < 1e-12, "IoU y Dice")

# (4) Disco solar sintético
N, R = 160, 70
yy, xx = np.mgrid[0:N, 0:N]
r = np.hypot(xx - 80, yy - 80)
disco = r < R
mu = np.sqrt(np.clip(1 - (r / R) ** 2, 0, 1))
foto = 1000 * (0.4 + 0.6 * mu)
manchas = [(50, 70, 4), (95, 55, 6), (112, 100, 3)]
verdad = np.zeros((N, N), bool)
for (cx, cy, rr) in manchas:
    verdad |= np.hypot(xx - cx, yy - cy) < rr
img = np.where(disco, foto * np.where(verdad, 0.35, 1.0), 0.0) + 20 * rng.standard_normal((N, N))
area_disco = disco.sum()
print(f"(4) disco de {area_disco} px; área verdadera de las manchas: {verdad.sum()} px ({100*verdad.sum()/area_disco:.3f} % del disco)")

# 4a: Otsu global sobre el disco
t_raw = otsu(img[disco])
seg_raw = (img < t_raw) & disco
print(f"    Otsu global (umbral {t_raw:.0f}): {seg_raw.sum()} px; IoU {iou(seg_raw, verdad):.3f}; Dice {dice(seg_raw, verdad):.3f}")

# 4b: aplanar con el perfil radial mediano y umbralizar la razón
rb = np.minimum((r // 1).astype(int), N)
perfil = np.array([np.median(img[(rb == k) & disco]) if np.any((rb == k) & disco) else 1.0 for k in range(N)])
plano = perfil[rb]
razon = np.where(disco, img / np.maximum(plano, 1), 1.0)
razon_f = ndimage.uniform_filter(razon, 3)
t_rat = otsu(razon_f[disco])
seg = (razon_f < t_rat) & disco
lab, n = ndimage.label(seg, structure=np.ones((3, 3)))
tam = ndimage.sum(seg, lab, range(1, n + 1))
grandes = [k + 1 for k, s in enumerate(tam) if s >= 10]       # descarta ruido pequeño
seg2 = np.isin(lab, grandes)
print(f"    razón a la fotosfera + suavizado 3x3 (umbral Otsu {t_rat:.3f}): {n} regiones, {len(grandes)} con >= 10 px")
print(f"    tras descartar regiones < 10 px: {seg2.sum()} px; IoU {iou(seg2, verdad):.3f}; Dice {dice(seg2, verdad):.3f}; "
      f"área medida {100*seg2.sum()/area_disco:.3f} % del disco")
prueba(len(grandes) == 3, "se encuentran las tres manchas")
prueba(iou(seg2, verdad) > iou(seg_raw, verdad) + 0.2, "aplanar mejora la segmentación")
print("Pruebas superadas.")
