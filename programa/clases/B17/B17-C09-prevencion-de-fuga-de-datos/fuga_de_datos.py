#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C09: tres fugas de datos y su corrección.

Datos: SINTÉTICOS.
 A) Selección de variables con todo el conjunto: 200 objetos, 5000 variables
    gaussianas independientes y etiquetas aleatorias. Exactitud verdadera
    posible = 0,5 (no hay señal). Se elige SelectKBest(k=25).
 B) Dependencia temporal: dos paseos aleatorios independientes (uno es la
    característica, otro define la etiqueta por su signo). No hay relación
    entre característica y etiqueta: exactitud verdadera = 0,5. Clasificador:
    1 vecino.
 C) Dependencia por fuente: 40 fuentes con 25 observaciones; cada fuente
    tiene un desplazamiento propio en la característica y una etiqueta propia
    (la etiqueta es de la fuente, sin relación con la física). Exactitud
    verdadera con fuentes nuevas = 0,5.
Referencia independiente: en los tres casos la exactitud honesta debe estar
en 0,5 +- tolerancia; la fuga la infla.
Tolerancias: A 0,07 (n = 200 -> error estándar 0,035, 2 sigma); C 0,08 y
B 0,15 (promedios de 20 repeticiones; en B los paseos aleatorios no son
estacionarios y la exactitud honesta se dispersa más).
"""
import platform
import sys

import numpy as np
import sklearn
from sklearn.feature_selection import SelectKBest
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold, KFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scikit-learn", sklearn.__version__, "|", platform.system())

# --- A) preprocesamiento con todo el conjunto ---
fugas, honestas, cvp = [], [], []
for s in range(20):
    r = np.random.default_rng(100 + s)
    X, y = r.normal(size=(200, 5000)), r.integers(0, 2, 200)
    Xs = SelectKBest(k=25).fit_transform(X, y)                       # error: ve la etiqueta de la prueba
    a, b, ya, yb = train_test_split(Xs, y, random_state=0)
    fugas.append(LogisticRegression(max_iter=500).fit(a, ya).score(b, yb))
    a, b, ya, yb = train_test_split(X, y, random_state=0)
    pipe = make_pipeline(SelectKBest(k=25), LogisticRegression(max_iter=500)).fit(a, ya)
    honestas.append(pipe.score(b, yb))
    cvp.append(cross_val_score(make_pipeline(SelectKBest(k=25), LogisticRegression(max_iter=500)), X, y, cv=KFold(5, shuffle=True, random_state=0)).mean())
fa, ho, cv = np.mean(fugas), np.mean(honestas), np.mean(cvp)
print(f"A) selección con todo el conjunto: {fa:.3f} | dentro de la partición: {ho:.3f} | Pipeline con validación cruzada: {cv:.3f} (verdad 0,5)")
prueba(fa > 0.65 and abs(ho - 0.5) < 0.07 and abs(cv - 0.5) < 0.07, "fuga A")

# --- B) dependencia temporal ---
al, bl = [], []
for s in range(20):
    r = np.random.default_rng(200 + s)
    n = 1000
    x = np.cumsum(r.normal(size=n)).reshape(-1, 1)
    y = (np.cumsum(r.normal(size=n)) > 0).astype(int)
    knn = KNeighborsClassifier(1)
    al.append(cross_val_score(knn, x, y, cv=KFold(5, shuffle=True, random_state=0)).mean())      # pliegues al azar
    bl.append(cross_val_score(knn, x, y, cv=KFold(5, shuffle=False)).mean())                       # bloques contiguos
ra, bq = np.mean(al), np.mean(bl)
print(f"B) paseos aleatorios: pliegues al azar {ra:.3f} | bloques contiguos {bq:.3f} (verdad 0,5)")
prueba(ra > 0.7 and abs(bq - 0.5) < 0.15 and ra - bq > 0.1, "fuga B")

# --- C) dependencia por fuente ---
sa, sg = [], []
for s in range(20):
    r = np.random.default_rng(300 + s)
    fuente = np.repeat(np.arange(40), 25)
    et = np.repeat(r.integers(0, 2, 40), 25)
    x = (np.repeat(r.normal(0, 3, 40), 25) + r.normal(0, 0.05, 1000)).reshape(-1, 1)
    knn = KNeighborsClassifier(5)
    sa.append(cross_val_score(knn, x, et, cv=KFold(5, shuffle=True, random_state=0)).mean())
    sg.append(cross_val_score(knn, x, et, cv=GroupKFold(5), groups=fuente).mean())
ca, cg = np.mean(sa), np.mean(sg)
print(f"C) 40 fuentes x 25 observaciones: pliegues al azar {ca:.3f} | por fuente (GroupKFold) {cg:.3f} (verdad 0,5)")
prueba(ca > 0.85 and abs(cg - 0.5) < 0.08, "fuga C")
print("Pruebas superadas.")
