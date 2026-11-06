#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C12: precisión, exhaustividad y falsos positivos de un sistema de alertas.

Datos: SINTÉTICOS. Puntuaciones de un clasificador de candidatos: los
negativos ~ N(0, 1) y los positivos ~ N(2, 1) (separación d = 2). Prevalencia
de positivos: 1 % en una muestra de 200 000 objetos.
Referencias exactas: con umbral t, TPR = 1 - Phi(t - 2); FPR = 1 - Phi(t);
precisión = pi TPR/(pi TPR + (1-pi) FPR); AUC ROC = Phi(d/sqrt(2)).
Caso de referencia de scikit-learn (documentación): y = [0,0,0,1,1,1,1,1],
pred = [0,1,0,1,0,1,0,1] da (tn, fp, fn, tp) = (2, 1, 2, 3); y = [0,0,1,1],
puntuaciones [0,1; 0,4; 0,35; 0,8] dan precisión promedio 0,83.
Tolerancias: 0,01 en TPR/FPR/precisión a n = 200 000; 1e-9 en casos pequeños.
"""
import platform
import sys
from math import erf, sqrt

import numpy as np
import sklearn
from sklearn.metrics import average_precision_score, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


Phi = lambda x: 0.5 * (1 + erf(x / sqrt(2)))  # noqa: E731
print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scikit-learn", sklearn.__version__, "|", platform.system())

# Caso pequeño de la documentación
yt = [0, 0, 0, 1, 1, 1, 1, 1]; yp = [0, 1, 0, 1, 0, 1, 0, 1]
tn, fp, fn, tp = confusion_matrix(yt, yp).ravel().tolist()
P, R = tp / (tp + fp), tp / (tp + fn)
F1 = 2 * P * R / (P + R)
print(f"Matriz de confusión (tn, fp, fn, tp) = {(tn, fp, fn, tp)}; precisión {P:.4f}, exhaustividad {R:.4f}, F1 {F1:.4f}")
prueba((tn, fp, fn, tp) == (2, 1, 2, 3), "matriz de confusión")
prueba(abs(P - precision_score(yt, yp)) < 1e-12 and abs(R - recall_score(yt, yp)) < 1e-12 and abs(F1 - f1_score(yt, yp)) < 1e-12, "P, R, F1 frente a scikit-learn")
ap = average_precision_score([0, 0, 1, 1], [0.1, 0.4, 0.35, 0.8])
print(f"Precisión promedio del caso de referencia: {ap:.4f} (documentación: 0,83)")
prueba(abs(ap - 5 / 6) < 1e-12, "precisión promedio")

# Alertas con prevalencia 1 %
rng = np.random.default_rng(12)
n, pi = 200000, 0.01
y = (rng.random(n) < pi).astype(int)
s = rng.normal(2.0 * y, 1.0)
print(f"Muestra: {n} objetos, {y.sum()} positivos ({100*y.mean():.2f} %)")
for t in (1.0, 2.0, 3.0):
    pred = s > t
    tpr, fpr = pred[y == 1].mean(), pred[y == 0].mean()
    prec = y[pred].mean()
    teo_t, teo_f = 1 - Phi(t - 2), 1 - Phi(t)
    teo_p = pi * teo_t / (pi * teo_t + (1 - pi) * teo_f)
    print(f"  umbral {t:.0f}: exhaustividad {tpr:.3f} (teoría {teo_t:.3f}) | tasa de falsos positivos {fpr:.4f} (teoría {teo_f:.4f}) | precisión {prec:.3f} (teoría {teo_p:.3f}) | alertas {pred.sum()}")
    prueba(abs(tpr - teo_t) < 0.03 and abs(fpr - teo_f) < 0.003 and abs(prec - teo_p) < 0.03, f"umbral {t}")
auc, auc_t = roc_auc_score(y, s), Phi(2 / sqrt(2))
apn = average_precision_score(y, s)
print(f"AUC ROC {auc:.4f} (teoría {auc_t:.4f}) | precisión promedio {apn:.4f} (azar = prevalencia {pi:.2f})")
prueba(abs(auc - auc_t) < 0.01 and apn < 0.5, "AUC y precisión promedio")

# Elección de umbral por costo: un falso positivo cuesta 1, un positivo perdido cuesta 50
mejor = None
for t in np.arange(0.0, 4.01, 0.25):
    pred = s > t
    costo = ((pred == 1) & (y == 0)).sum() * 1 + ((pred == 0) & (y == 1)).sum() * 50
    if mejor is None or costo < mejor[1]:
        mejor = (t, costo)
print(f"Umbral de mínimo costo (FP = 1, FN = 50): {mejor[0]:.2f}, costo {mejor[1]}")
print("Pruebas superadas.")
