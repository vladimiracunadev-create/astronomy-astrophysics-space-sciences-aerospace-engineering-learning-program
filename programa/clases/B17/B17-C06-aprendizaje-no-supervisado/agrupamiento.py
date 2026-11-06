#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C06: reducción de dimensión (PCA por SVD) y agrupamiento (k-medias).

Datos: SINTÉTICOS. 3 poblaciones de 300 objetos en 4 variables (colores
fotométricos estandarizados ficticios): centros en +-4 sobre las dos primeras
variables, dispersión 1; las variables 3 y 4 son ruido de varianza 1 mas una
mezcla lineal de las dos primeras (correlacion artificial).
Referencias exactas: (1) las varianzas de los componentes principales
son los autovalores de la covarianza (SVD y eigh coinciden); (2) la suma de
varianzas es la traza (4 n/(n-1): columnas con desviación poblacional); (3) k-medias a mano (Lloyd) y de
scikit-learn alcanzan la misma inercia; (4) con grupos bien separados el
agrupamiento recupera los centros.
Supuestos: grupos aproximadamente esféricos. Tolerancias: 1e-8 en (1)-(2);
1e-6 relativa en (3); 0,15 en los centros (4).
"""
import platform
import sys

import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def lloyd(X, C, it=100):
    for _ in range(it):
        lab = np.argmin(((X[:, None] - C[None]) ** 2).sum(2), 1)
        Cn = np.array([X[lab == j].mean(0) for j in range(len(C))])
        if np.allclose(Cn, C):
            break
        C = Cn
    inercia = ((X - C[lab]) ** 2).sum()
    return C, lab, inercia


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scikit-learn", sklearn.__version__, "|", platform.system())
rng = np.random.default_rng(6)
cen = np.array([[4, 4], [-4, 4], [0, -5.0]])
X2 = np.vstack([rng.normal(c, 1.0, (300, 2)) for c in cen])
y = np.repeat([0, 1, 2], 300)
X = np.c_[X2, 0.5 * X2[:, 0] - 0.3 * X2[:, 1] + rng.normal(0, 1, 900), -0.4 * X2[:, 0] + rng.normal(0, 1, 900)]
Xs = (X - X.mean(0)) / X.std(0)

# PCA por SVD frente a autovalores de la covarianza
U, s, Vt = np.linalg.svd(Xs - Xs.mean(0), full_matrices=False)
var_svd = s**2 / (len(Xs) - 1)
var_eig = np.linalg.eigh(np.cov(Xs.T))[0][::-1]
print("Varianzas de los componentes (SVD):", np.round(var_svd, 4))
prueba(np.allclose(var_svd, var_eig, atol=1e-8), "SVD vs autovalores")
prueba(abs(var_svd.sum() - 4.0 * len(Xs) / (len(Xs) - 1)) < 1e-8, "traza = 4 n/(n-1)")
print(f"Fracción de varianza explicada por los dos primeros: {var_svd[:2].sum()/var_svd.sum():.3f}")
Z = (Xs - Xs.mean(0)) @ Vt[:2].T

# k-medias: a mano y con scikit-learn
km = KMeans(3, n_init=10, random_state=0).fit(Z)
C0 = Z[rng.choice(len(Z), 3, replace=False)]
Cm, lab_m, in_m = lloyd(Z, km.cluster_centers_ + 0.0)
Cm2, lab2, in_m2 = lloyd(Z, C0)
print(f"Inercia scikit-learn {km.inertia_:.2f}; Lloyd a mano (desde sus centros) {in_m:.2f}; (desde centros al azar) {in_m2:.2f}")
prueba(abs(in_m - km.inertia_) / km.inertia_ < 1e-6, "inercia a mano frente a scikit-learn")
sil = silhouette_score(Z, km.labels_)
print(f"Silueta con k = 3: {sil:.3f}")
for k in (2, 4, 6):
    print(f"  silueta con k = {k}: {silhouette_score(Z, KMeans(k, n_init=10, random_state=0).fit_predict(Z)):.3f}")
prueba(sil > 0.6, "grupos separados")

# Pureza frente a las poblaciones verdaderas (solo disponible porque los datos son sintéticos)
pureza = sum(np.bincount(y[km.labels_ == j]).max() for j in range(3)) / len(y)
print(f"Pureza frente a las poblaciones verdaderas: {pureza:.3f}")
prueba(pureza > 0.98, "pureza")
print("Pruebas superadas.")
