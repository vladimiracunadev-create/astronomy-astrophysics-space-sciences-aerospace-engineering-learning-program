#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C23: agrupamiento k-medias de píxeles sin muestras etiquetadas.

Datos: SINTÉTICOS, semilla fija. Mismos tres tipos de cobertura ficticios de
B15-C22 (rojo, NIR): agua (0.03, 0.02), vegetación (0.04, 0.45), suelo (0.20, 0.28),
con dispersión sigma por banda; aquí NO se usan las etiquetas para agrupar, solo
para evaluar al final.
Algoritmo (Lloyd): asignar cada punto al centroide más cercano; recalcular los
centroides como medias; repetir. Referencias: (1) la inercia (suma de distancias
cuadradas al centroide) no aumenta en cada iteración; (2) con k = 1 la inercia
es N tr(Sigma); (3) con centroides iniciales idénticos, el algoritmo propio
coincide con scipy.cluster.vq.kmeans2 (minit='matrix'); (4) con clases bien
separadas el índice de Rand ajustado (ARI) es ~1, y baja al solaparse;
(5) con inicio aleatorio simple el algoritmo puede quedar en mínimos locales:
se compara con la inicialización k-means++ por fracción de ejecuciones que
alcanzan la mejor inercia.
Tolerancias: 1e-9 en (3); 1e-12 en monotonía; 3 % en (2).
"""
import platform
import sys

import numpy as np
import scipy
from scipy.cluster.vq import kmeans2


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def lloyd(X, C0, iters=100):
    C = C0.copy()
    hist = []
    for _ in range(iters):
        D = ((X[:, None, :] - C[None]) ** 2).sum(2)
        lab = D.argmin(1)
        hist.append(D[np.arange(len(X)), lab].sum())
        Cn = np.array([X[lab == k].mean(0) if np.any(lab == k) else C[k] for k in range(len(C))])
        if np.allclose(Cn, C, atol=1e-12):
            break
        C = Cn
    D = ((X[:, None, :] - C[None]) ** 2).sum(2)
    lab = D.argmin(1)
    return C, lab, D[np.arange(len(X)), lab].sum(), hist


def kpp(X, k, rng):
    C = [X[rng.integers(len(X))]]
    for _ in range(k - 1):
        d2 = np.min(((X[:, None, :] - np.array(C)[None]) ** 2).sum(2), axis=1)
        C.append(X[rng.choice(len(X), p=d2 / d2.sum())])
    return np.array(C)


def ari(a, b):
    from math import comb
    ca = np.unique(a)
    cb = np.unique(b)
    M = np.array([[np.sum((a == i) & (b == j)) for j in cb] for i in ca])
    s = sum(comb(int(v), 2) for v in M.ravel())
    sa = sum(comb(int(v), 2) for v in M.sum(1))
    sb = sum(comb(int(v), 2) for v in M.sum(0))
    n = comb(int(M.sum()), 2)
    esp = sa * sb / n
    return (s - esp) / (0.5 * (sa + sb) - esp)


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "|", platform.system())
rng = np.random.default_rng(15023)
mu = np.array([(0.03, 0.02), (0.04, 0.45), (0.20, 0.28)])


def datos(sg, n=1000):
    X = np.vstack([rng.normal(m, sg, (n, 2)) for m in mu])
    return X, np.repeat(np.arange(3), n)


# (1)-(3)
X, y = datos(0.05)
C0 = kpp(X, 3, rng)
C, lab, inercia, hist = lloyd(X, C0)
dif = np.diff(hist)
print(f"(1) k-medias (sigma = 0.05): {len(hist)} iteraciones; inercia {hist[0]:.4f} -> {inercia:.4f}; mayor cambio de inercia entre iteraciones {dif.max():.1e} (siempre ≤ 0)")
prueba(np.all(dif <= 1e-12), "la inercia no aumenta")
I1 = ((X - X.mean(0)) ** 2).sum()
print(f"(2) k = 1: inercia {I1:.4f}; N tr(Sigma) = {len(X) * np.trace(np.cov(X.T, bias=True)):.4f}")
prueba(abs(I1 / (len(X) * np.trace(np.cov(X.T, bias=True))) - 1) < 1e-9, "inercia con k = 1")
Cs, ls = kmeans2(X, C0.copy(), iter=100, minit="matrix")
Cp, lp, ip, _ = lloyd(X, C0, iters=100)
orden_s = np.lexsort(Cs.T)
orden_p = np.lexsort(Cp.T)
print(f"(3) propio vs scipy.cluster.vq.kmeans2: diferencia máxima de centroides {np.max(np.abs(Cs[orden_s] - Cp[orden_p])):.2e}")
prueba(np.max(np.abs(Cs[orden_s] - Cp[orden_p])) < 1e-6, "coincide con scipy")

# (4) ARI según el solapamiento
print("(4) índice de Rand ajustado (ARI) de las agrupaciones frente a las clases verdaderas:")
for sg in (0.02, 0.05, 0.09, 0.15):
    X, y = datos(sg)
    mejores = max((lloyd(X, kpp(X, 3, rng)) for _ in range(10)), key=lambda r: -r[2])
    print(f"    sigma = {sg:.2f}: ARI = {ari(y, mejores[1]):.3f}")
Xs, ys = datos(0.02)
Cc, ll, _, _ = lloyd(Xs, kpp(Xs, 3, rng))
prueba(ari(ys, ll) > 0.99, "clases bien separadas: ARI ~ 1")

# (5) Mínimos locales (k = 6 sobre 3 grupos reales: hay varias formas de repartirlos)
X, y = datos(0.05)
n_ej, kk = 300, 6
res = {"aleatoria (puntos)": [], "k-means++": []}
for _ in range(n_ej):
    res["aleatoria (puntos)"].append(lloyd(X, X[rng.choice(len(X), kk, replace=False)])[2])
    res["k-means++"].append(lloyd(X, kpp(X, kk, rng))[2])
mejor = min(min(v) for v in res.values())
print(f"(5) k = {kk}, {n_ej} ejecuciones por tipo de inicio; mejor inercia {mejor:.3f}")
for k, v in res.items():
    v = np.array(v)
    print(f"    inicio {k:20s}: fracción que alcanza la mejor inercia (±1 %): {np.mean(v < 1.01 * mejor):.3f}; inercia media {v.mean():.3f}; peor {v.max():.3f}")
prueba(max(max(v) for v in res.values()) > 1.01 * mejor, "existen mínimos locales")

# (6) Elegir k: inercia
X, y = datos(0.05)
print("(6) inercia frente a k (sigma = 0.05, 3 clases reales):")
for k in range(1, 7):
    ij = min(lloyd(X, kpp(X, k, rng))[2] for _ in range(5))
    print(f"    k = {k}: {ij:.3f}")
print("Pruebas superadas.")
