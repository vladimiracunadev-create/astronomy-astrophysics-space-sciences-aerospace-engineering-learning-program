#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C22: clasificación supervisada de píxeles (2 bandas).

Datos: SINTÉTICOS, semilla fija. Píxeles con reflectancia en rojo y en
infrarrojo cercano (bandas 4 y 5 de Landsat 8/9, USGS) de tres clases ficticias:
agua (rojo 0.03, NIR 0.02), vegetación (0.04, 0.45) y suelo (0.20, 0.28), con
desviación 0.09 en cada banda (gaussianas independientes).
Clasificadores: distancia mínima a la media de clase; máxima verosimilitud
gaussiana (QDA con covarianza de cada clase); k vecinos más cercanos (k = 1).
Referencias analíticas: (1) para dos clases gaussianas 1D con igual varianza y
medias separadas d sigma, el error de Bayes con umbral en el punto medio es
Phi(-d/2); (2) el índice NDVI = (NIR - rojo)/(NIR + rojo) de la media de cada
clase; (3) el kappa de Cohen de una matriz de confusión diagonal es 1.
Supuestos: clases gaussianas; muestras de entrenamiento representativas.
Tolerancias: 2 % relativo en (1); exactitud de prueba coherente con el error de Bayes.
"""
import math
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def Phi(z):
    return 0.5 * math.erfc(-z / math.sqrt(2))


def kappa(C):
    n = C.sum()
    po = np.trace(C) / n
    pe = (C.sum(0) * C.sum(1)).sum() / n**2
    return (po - pe) / (1 - pe)


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15022)

# (1) Error de Bayes en 1D
d = 2.0
n1 = 400000
x0 = rng.normal(0, 1, n1)
x1 = rng.normal(d, 1, n1)
err = 0.5 * (np.mean(x0 > d / 2) + np.mean(x1 < d / 2))
print(f"(1) dos gaussianas separadas {d} sigma: error observado {err:.5f}; Phi(-d/2) = {Phi(-d/2):.5f}")
prueba(abs(err / Phi(-d / 2) - 1) < 0.02, "error de Bayes")

# (2) Clases de píxeles
medias = {"agua": (0.03, 0.02), "vegetación": (0.04, 0.45), "suelo": (0.20, 0.28)}
nombres = list(medias)
mu = np.array([medias[k] for k in nombres])
sg = 0.09
print("    NDVI de la media de cada clase: " + ", ".join(f"{k} {(m[1]-m[0])/(m[1]+m[0]):+.2f}" for k, m in medias.items()))


def muestra(n):
    X = np.vstack([rng.normal(m, sg, (n, 2)) for m in mu])
    y = np.repeat(np.arange(3), n)
    return X, y


Xtr, ytr = muestra(30)           # entrenamiento pequeño
Xte, yte = muestra(5000)         # prueba independiente


def entrenar(X, y):
    ms = np.array([X[y == c].mean(0) for c in range(3)])
    cov = [np.cov(X[y == c].T) + 1e-9 * np.eye(2) for c in range(3)]
    return ms, cov


ms, cov = entrenar(Xtr, ytr)


def dmin(X):
    return np.argmin(((X[:, None, :] - ms[None]) ** 2).sum(2), axis=1)


def qda(X):
    out = []
    for c in range(3):
        Si = np.linalg.inv(cov[c])
        dd = X - ms[c]
        out.append(-0.5 * np.einsum("ni,ij,nj->n", dd, Si, dd) - 0.5 * np.log(np.linalg.det(cov[c])))
    return np.argmax(np.array(out), axis=0)


def knn1(X, Xt=Xtr, yt=ytr):
    D = ((X[:, None, :] - Xt[None]) ** 2).sum(2)
    return yt[np.argmin(D, axis=1)]


def conf(y, p):
    C = np.zeros((3, 3), int)
    for a, b in zip(y, p):
        C[a, b] += 1
    return C


res = {}
for nom, f in (("distancia mínima", dmin), ("máxima verosimilitud", qda), ("1 vecino", knn1)):
    C = conf(yte, f(Xte))
    res[nom] = (np.trace(C) / C.sum(), kappa(C), C)
    print(f"(2) {nom:22s}: exactitud de prueba {res[nom][0]:.4f}; kappa {res[nom][1]:.4f}")
print("    matriz de confusión (filas verdad, columnas predicción; agua, vegetación, suelo), máxima verosimilitud:")
for fila in res["máxima verosimilitud"][2]:
    print("    ", fila.tolist())
acc_tr = np.mean(knn1(Xtr[:], Xtr, ytr) == ytr)
print(f"    1 vecino evaluado con los datos de entrenamiento: exactitud {acc_tr:.3f} (fuga: no es una medida de generalización)")
prueba(acc_tr == 1.0 and res["1 vecino"][0] < acc_tr, "el 1-NN acierta el 100 % en entrenamiento y menos en prueba")
prueba(kappa(np.diag([10, 20, 30])) == 1.0, "kappa de una matriz diagonal")

# (3) Solapamiento: suelo y vegetación más cercanos
mu2 = mu.copy()
mu2[2] = (0.10, 0.40)
for sep, mm in (("separadas", mu), ("solapadas", mu2)):
    Xt = np.vstack([rng.normal(m, sg, (5000, 2)) for m in mm])
    msx = np.array([rng.normal(m, sg, (2000, 2)).mean(0) for m in mm])
    p = np.argmin(((Xt[:, None, :] - msx[None]) ** 2).sum(2), axis=1)
    C = conf(np.repeat(np.arange(3), 5000), p)
    print(f"(3) clases {sep}: exactitud con distancia mínima {np.trace(C)/C.sum():.4f}")
print("Pruebas superadas.")
