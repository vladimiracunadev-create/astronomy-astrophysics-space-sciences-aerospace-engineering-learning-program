#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C07: detectar y medir el cambio de distribución.

Datos: SINTÉTICOS. Una característica estandarizada x. Entrenamiento
("objetos brillantes"): clase 0 ~ N(-1, 1), clase 1 ~ N(+1, 1). Despliegue
("objetos débiles"): el ruido de medida crece, x ~ N(+-1, 1,6) y la clase 1
es menos frecuente (prevalencia 0,3).
Referencias exactas (dos poblaciones normales N(0,1) y N(d,1), d = 1):
  estadístico de Kolmogorov-Smirnov = 2 Phi(d/2) - 1 = 0,3829
  AUC de un clasificador de dominio óptimo   = Phi(d/sqrt(2)) = 0,7602
Modelo: prueba KS de dos muestras (scipy), clasificador de dominio (regresión
logística con validación cruzada) y degradación de exactitud.
Supuestos: sólo cambio de covariables y prevalencia. Tolerancia: 0,02 en KS y AUC.
"""
import platform
import sys
from math import erf, sqrt

import numpy as np
import scipy
import sklearn
from scipy.stats import ks_2samp
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import roc_auc_score


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


Phi = lambda x: 0.5 * (1 + erf(x / sqrt(2)))  # noqa: E731


def auc_dominio(a, b):
    X = np.r_[a, b].reshape(-1, 1)
    d = np.r_[np.zeros(len(a)), np.ones(len(b))]
    p = cross_val_predict(LogisticRegression(), X, d, cv=StratifiedKFold(5, shuffle=True, random_state=0), method="predict_proba")[:, 1]
    return roc_auc_score(d, p)


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "| scikit-learn", sklearn.__version__, "|", platform.system())
rng = np.random.default_rng(8)
n = 20000
a, b = rng.normal(0, 1, n), rng.normal(1, 1, n)
ks_t, ks_o = 2 * Phi(0.5) - 1, ks_2samp(a, b).statistic
print(f"KS: teoría {ks_t:.4f}, medido {ks_o:.4f}")
prueba(abs(ks_o - ks_t) < 0.02, "KS")
auc_t, auc_o = Phi(1 / sqrt(2)), auc_dominio(a, b)
print(f"AUC de dominio: teoría {auc_t:.4f}, medido {auc_o:.4f}")
prueba(abs(auc_o - auc_t) < 0.02, "AUC de dominio")
a2 = rng.normal(0, 1, n)
auc_0 = auc_dominio(a, a2)
print(f"Sin cambio (misma distribución): AUC de dominio {auc_0:.4f} (esperado 0,5), p-valor KS {ks_2samp(a, a2).pvalue:.3f}")
prueba(abs(auc_0 - 0.5) < 0.02, "sin cambio")

# Degradación de un clasificador entrenado en 'brillantes'
yt = rng.integers(0, 2, n)
xt = rng.normal(np.where(yt == 1, 1.0, -1.0), 1.0).reshape(-1, 1)
modelo = LogisticRegression().fit(xt, yt)
yv = (rng.random(n) < 0.3).astype(int)
xv = rng.normal(np.where(yv == 1, 1.0, -1.0), 1.6).reshape(-1, 1)
yb = rng.integers(0, 2, n)
xb = rng.normal(np.where(yb == 1, 1.0, -1.0), 1.0).reshape(-1, 1)
acc_b, acc_v = modelo.score(xb, yb), modelo.score(xv, yv)
teo_b = Phi(1.0)
print(f"Exactitud en brillantes nuevos {acc_b:.4f} (teoría {teo_b:.4f}); en débiles {acc_v:.4f}")
prueba(abs(acc_b - teo_b) < 0.01 and acc_v < acc_b - 0.03, "degradación")
# Detección por el cambio de covariables: KS y dominio entre entrenamiento y despliegue
print(f"Entrenamiento vs. despliegue: KS {ks_2samp(xt.ravel(), xv.ravel()).statistic:.3f}, AUC de dominio {auc_dominio(xt.ravel(), xv.ravel()):.3f}")
# Referencia: exactitud sin etiquetas = confianza máxima media (softmax) como alarma
conf_b = modelo.predict_proba(xb).max(1).mean()
conf_v = modelo.predict_proba(xv).max(1).mean()
print(f"Confianza media: brillantes {conf_b:.3f}, débiles {conf_v:.3f} (la confianza declarada no cae como la exactitud)")
print("Pruebas superadas.")
