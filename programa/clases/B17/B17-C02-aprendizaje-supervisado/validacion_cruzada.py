#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C02: aprendizaje supervisado y validación cruzada.

Datos: SINTÉTICOS. Dos clases gaussianas en una dimensión (una variable
física estandarizada), medias -1 y +1, desviación 1, clases equiprobables.
Modelo: regresión logística; validación cruzada estratificada de 5 pliegues
(escrita a mano y comparada con scikit-learn).
Referencia exacta: la exactitud máxima posible (error de Bayes) es
Phi(d/2) con d = separación de medias / sigma = 2  ->  Phi(1) = 0,8413.
Supuestos: clases gaussianas con igual varianza. Validez: este caso.
Tolerancia: 0,01 sobre n = 20 000 (error estándar ~ 0,0026).
"""
import platform
import sys
from math import erf, sqrt

import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def phi(x):
    return 0.5 * (1 + erf(x / sqrt(2)))


def pliegues_estratificados(y, k, semilla):
    """k pliegues que conservan la proporción de clases (versión simple)."""
    rng = np.random.default_rng(semilla)
    pl = np.empty(len(y), dtype=int)
    for c in np.unique(y):
        idx = rng.permutation(np.where(y == c)[0])
        pl[idx] = np.arange(len(idx)) % k
    return pl


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scikit-learn", sklearn.__version__, "|", platform.system())
rng = np.random.default_rng(2)
n = 20000
y = rng.integers(0, 2, n)
x = rng.normal(np.where(y == 1, 1.0, -1.0), 1.0).reshape(-1, 1)

bayes = phi(1.0)
print(f"Exactitud máxima posible (Bayes) = Phi(1) = {bayes:.4f}")

# Validación cruzada a mano
k = 5
pl = pliegues_estratificados(y, k, 0)
ac = []
for j in range(k):
    ent, val = pl != j, pl == j
    m = LogisticRegression().fit(x[ent], y[ent])
    ac.append((m.predict(x[val]) == y[val]).mean())
ac = np.array(ac)
print("Exactitud por pliegue (a mano):", np.round(ac, 4), f"| media {ac.mean():.4f} ± {ac.std(ddof=1):.4f}")
prueba(abs(ac.mean() - bayes) < 0.01, "la validación cruzada debe acercarse a Bayes")

# Comparación con scikit-learn
sk = cross_val_score(LogisticRegression(), x, y, cv=StratifiedKFold(5, shuffle=True, random_state=0))
print(f"scikit-learn StratifiedKFold: media {sk.mean():.4f}")
prueba(abs(sk.mean() - ac.mean()) < 0.01, "ambas implementaciones deben coincidir")

# Prueba de cordura: etiquetas aleatorias => exactitud ~ 0,5
y_ruido = rng.integers(0, 2, n)
r = cross_val_score(LogisticRegression(), x, y_ruido, cv=StratifiedKFold(5, shuffle=True, random_state=0)).mean()
print(f"Etiquetas aleatorias: exactitud {r:.4f} (esperado ~0,5)")
prueba(abs(r - 0.5) < 0.02, "con etiquetas aleatorias no debe haber aprendizaje")

# Evaluar en los datos de entrenamiento con un modelo flexible engaña
from sklearn.neighbors import KNeighborsClassifier
m1 = KNeighborsClassifier(1).fit(x[:2000], y[:2000])
tr = m1.score(x[:2000], y[:2000])
te = m1.score(x[2000:], y[2000:])
print(f"1-vecino: exactitud en entrenamiento {tr:.3f}, en datos nuevos {te:.3f}")
prueba(tr == 1.0 and te < bayes - 0.05, "el sobreajuste debe verse")

# Regresión: mínimos cuadrados = solución exacta de las ecuaciones normales
xa = rng.uniform(0, 10, 200)
ya = 2.0 + 0.5 * xa + rng.normal(0, 0.3, 200)
A = np.c_[np.ones_like(xa), xa]
beta = np.linalg.solve(A.T @ A, A.T @ ya)
beta2 = np.linalg.lstsq(A, ya, rcond=None)[0]
print(f"Regresión lineal: ecuaciones normales {np.round(beta,4)}, lstsq {np.round(beta2,4)} (verdad 2,0 y 0,5)")
prueba(np.allclose(beta, beta2, atol=1e-8) and abs(beta[1] - 0.5) < 0.02, "regresión")
print("Pruebas superadas.")
