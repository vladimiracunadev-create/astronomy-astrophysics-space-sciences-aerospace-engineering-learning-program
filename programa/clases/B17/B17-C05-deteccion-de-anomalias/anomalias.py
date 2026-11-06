#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C05: detección de anomalías con Mahalanobis e Isolation Forest.

Datos: SINTÉTICOS. Telemetría de dos variables estandarizadas (temperatura y
corriente de un subsistema) con distribución normal bivariada, correlación
0,8, n = 5000 normales; 25 anomalías inyectadas (desplazadas 5 desviaciones a lo largo de la dirección de menor varianza
(ninguna variable por separado se ve extrema)).
Referencia exacta: para datos normales bivariados, la distancia de Mahalanobis
al cuadrado sigue chi-cuadrado con 2 grados de libertad; el umbral del
cuantil 0,99 debe marcar ~1 % de los normales (falsas alarmas).
Modelo: Mahalanobis con media y covarianza de entrenamiento; IsolationForest
(scikit-learn, 300 árboles). Supuestos: normales gaussianos, entrenamiento
solo con datos normales. Tolerancia: tasa de falsas alarmas 1 % +- 0,5 puntos.
"""
import platform
import sys

import numpy as np
import sklearn
from scipy.stats import chi2
from sklearn.ensemble import IsolationForest
from sklearn.metrics import roc_auc_score


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scikit-learn", sklearn.__version__, "|", platform.system())
rng = np.random.default_rng(5)
S = np.array([[1, 0.8], [0.8, 1]])
Xtr = rng.multivariate_normal([0, 0], S, 5000)
Xn = rng.multivariate_normal([0, 0], S, 5000)          # normales nuevos
w, V = np.linalg.eigh(S)
dir_malo = V[:, 0]                                      # menor varianza
signo = rng.choice([-1.0, 1.0], 25)[:, None]
Xa = rng.multivariate_normal([0, 0], S, 25) * 0.5 + 5 * np.sqrt(w[0]) * signo * dir_malo

mu = Xtr.mean(0)
Si = np.linalg.inv(np.cov(Xtr.T))
d2 = lambda X: np.einsum("ij,jk,ik->i", X - mu, Si, X - mu)  # noqa: E731
umbral = chi2.ppf(0.99, 2)
fa = (d2(Xn) > umbral).mean()
rec = (d2(Xa) > umbral).mean()
print(f"Umbral chi2(2, 0,99) = {umbral:.3f}: falsas alarmas {100*fa:.2f} % (teoría 1 %), recuperación de anomalías {100*rec:.0f} %")
prueba(abs(fa - 0.01) < 0.005, "falsas alarmas vs. chi-cuadrado")

X_ev = np.vstack([Xn, Xa])
y = np.r_[np.zeros(len(Xn)), np.ones(len(Xa))]
iso = IsolationForest(n_estimators=300, random_state=0).fit(Xtr)
auc_i = roc_auc_score(y, -iso.score_samples(X_ev))
auc_m = roc_auc_score(y, d2(X_ev))
print(f"AUC ROC: Mahalanobis {auc_m:.3f} | Isolation Forest {auc_i:.3f}")
prueba(auc_m > 0.95 and auc_i > 0.85, "ambos deben detectar las anomalías inyectadas")

# Una variable por separado no ve la anomalía de correlación
z = (X_ev - mu) / Xtr.std(0)
auc_1 = roc_auc_score(y, np.abs(z).max(1))
print(f"AUC con |z| máximo por variable (ignora la correlación): {auc_1:.3f}")
prueba(auc_m > auc_1, "Mahalanobis debe superar al criterio por variable")
print("Pruebas superadas.")
