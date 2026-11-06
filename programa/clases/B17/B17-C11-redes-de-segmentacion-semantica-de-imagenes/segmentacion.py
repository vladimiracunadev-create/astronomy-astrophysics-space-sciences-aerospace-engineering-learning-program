#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C11: segmentación por píxel con una capa convolucional aprendida.

Datos: SINTÉTICOS. Imágenes de 48 x 48 con un disco brillante (una «mancha»
solar ficticia) de radio entre 7 y 12 píxeles, contraste 1,0 sobre un fondo 0
y ruido gaussiano de desviación 0,9. La máscara verdadera es el disco.
Modelo: una sola capa convolucional lineal de 7 x 7 seguida de una sigmoide
(regresión logística sobre parches 7 x 7), entrenada con 24 imágenes;
evaluada con 12 imágenes distintas. Línea base: umbral por píxel.
Referencias exactas: (1) la convolución escrita a mano coincide con
scipy.signal.correlate2d (modo 'valid'); (2) IoU y Dice de dos cuadrados de
10 x 10 desplazados 5 px: IoU = 1/3 y Dice = 1/2; (3) Dice = 2 IoU/(1+IoU);
(4) tamaño de salida 'valid' = N - k + 1.
Supuestos: ruido blanco gaussiano, una mancha por imagen. Tolerancia: 1e-10
en (1)-(3); el modelo debe superar a la línea base en IoU.
"""
import platform
import sys

import numpy as np
import scipy
import sklearn
from scipy.signal import correlate2d
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import jaccard_score


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def conv_valid(img, k):
    h, w = img.shape
    kh, kw = k.shape
    out = np.zeros((h - kh + 1, w - kw + 1))
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            out[i, j] = (img[i:i + kh, j:j + kw] * k).sum()
    return out


def iou(a, b):
    return (a & b).sum() / (a | b).sum()


def dice(a, b):
    return 2 * (a & b).sum() / (a.sum() + b.sum())


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "| scikit-learn", sklearn.__version__, "|", platform.system())
rng = np.random.default_rng(11)
img = rng.normal(size=(16, 16)); ker = rng.normal(size=(5, 5))
prueba(np.allclose(conv_valid(img, ker), correlate2d(img, ker, mode="valid"), atol=1e-10), "convolución")
print(f"Convolución a mano = scipy.signal.correlate2d; salida {conv_valid(img, ker).shape} = 16 - 5 + 1 = 12")

A = np.zeros((30, 30), bool); A[5:15, 5:15] = True
B = np.zeros((30, 30), bool); B[10:20, 5:15] = True
print(f"Cuadrados 10x10 desplazados 5 px: IoU {iou(A, B):.4f}, Dice {dice(A, B):.4f}")
prueba(abs(iou(A, B) - 1 / 3) < 1e-12 and abs(dice(A, B) - 0.5) < 1e-12, "IoU y Dice exactos")
prueba(abs(dice(A, B) - 2 * iou(A, B) / (1 + iou(A, B))) < 1e-12, "Dice = 2 IoU/(1+IoU)")
prueba(abs(iou(A, B) - jaccard_score(A.ravel(), B.ravel())) < 1e-12, "IoU frente a scikit-learn")


def imagen(r):
    N = 48
    cy, cx = r.integers(18, 30, 2)
    rad = r.integers(7, 13)
    yy, xx = np.mgrid[:N, :N]
    m = (yy - cy) ** 2 + (xx - cx) ** 2 <= rad**2
    return m * 1.0 + r.normal(0, 0.9, (N, N)), m


def parches(im, k=7):
    h = k // 2
    p = np.pad(im, h, mode="reflect")
    return np.lib.stride_tricks.sliding_window_view(p, (k, k)).reshape(-1, k * k)


r = np.random.default_rng(12)
tr = [imagen(r) for _ in range(24)]
te = [imagen(r) for _ in range(12)]
Xtr = np.vstack([parches(i) for i, _ in tr]); ytr = np.concatenate([m.ravel() for _, m in tr])
modelo = LogisticRegression(max_iter=500).fit(Xtr, ytr)

iou_m, iou_b, dice_m = [], [], []
for i, m in te:
    pred = modelo.predict(parches(i)).reshape(m.shape)
    base = i > 0.5
    iou_m.append(iou(pred, m)); dice_m.append(dice(pred, m)); iou_b.append(iou(base, m))
print(f"IoU medio en 12 imágenes nuevas: umbral por píxel {np.mean(iou_b):.3f} | capa convolucional 7x7 aprendida {np.mean(iou_m):.3f} (Dice {np.mean(dice_m):.3f})")
prueba(np.mean(iou_m) > np.mean(iou_b) + 0.1, "el modelo debe superar la línea base")
nucleo = modelo.coef_.reshape(7, 7)
print(f"Núcleo aprendido: suma {nucleo.sum():.3f}; peso central {nucleo[3,3]:.3f}; peso medio de los bordes {np.abs(nucleo[0]).mean():.3f}")
print("Pruebas superadas.")
