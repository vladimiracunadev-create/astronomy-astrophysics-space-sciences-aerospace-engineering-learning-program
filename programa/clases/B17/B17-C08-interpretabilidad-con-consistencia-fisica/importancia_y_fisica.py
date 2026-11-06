#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C08: importancia por permutación y consistencia con la física.

Datos: SINTÉTICOS. Sistemas de un planeta con semieje a (0,3 a 10 au) y masa
estelar M (0,3 a 2 masas solares) distribuidos log-uniformes. Periodo en
años según la tercera ley en unidades solares, P = a^1,5 * M^-0,5 (exacta),
con ruido multiplicativo log-normal de 2 %. Variable espuria: un número
aleatorio sin relación.
Referencias exactas: (1) en un modelo lineal con variables independientes
de varianza s_j^2, el aumento esperado del error cuadrático medio al permutar
la variable j es 2 b_j^2 s_j^2; (2) la ley física impone pendientes 1,5 y -0,5
en log-log.
Modelo: regresión lineal en logaritmos y bosque aleatorio sobre los mismos
datos. Supuestos: ley de Kepler exacta, ruido pequeño. Tolerancias: 5 %
frente a (1); 0,02 frente a (2).
"""
import platform
import sys

import numpy as np
import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LinearRegression


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def perm_mano(modelo, X, y, j, rng, reps=30):
    base = np.mean((modelo.predict(X) - y) ** 2)
    aumentos = []
    for _ in range(reps):
        Xp = X.copy()
        Xp[:, j] = rng.permutation(Xp[:, j])
        aumentos.append(np.mean((modelo.predict(Xp) - y) ** 2) - base)
    return np.mean(aumentos)


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scikit-learn", sklearn.__version__, "|", platform.system())
rng = np.random.default_rng(9)
n = 4000
la = rng.uniform(np.log(0.3), np.log(10), n)
lM = rng.uniform(np.log(0.3), np.log(2.0), n)
esp = rng.normal(0, 1, n)
lP = 1.5 * la - 0.5 * lM + rng.normal(0, 0.02, n)
X = np.c_[la, lM, esp]
tr, te = slice(0, 3000), slice(3000, n)

lin = LinearRegression().fit(X[tr], lP[tr])
print(f"Pendientes ajustadas (a, M, espuria): {np.round(lin.coef_, 4)}  (física: 1,5; -0,5; 0)")
prueba(abs(lin.coef_[0] - 1.5) < 0.02 and abs(lin.coef_[1] + 0.5) < 0.02 and abs(lin.coef_[2]) < 0.02, "pendientes físicas")

# (1) Importancia por permutación: mano vs. sklearn vs. teoría 2 b^2 s^2
r2 = np.random.default_rng(1)
for j, nom in enumerate(["ln a", "ln M", "espuria"]):
    teo = 2 * lin.coef_[j] ** 2 * X[te][:, j].var()
    mano = perm_mano(lin, X[te], lP[te], j, r2)
    print(f"  {nom}: teoría {teo:.4f} | a mano {mano:.4f}")
    if teo > 1e-3:
        prueba(abs(mano - teo) / teo < 0.05, f"permutación frente a teoría ({nom})")
sk = permutation_importance(lin, X[te], lP[te], n_repeats=30, random_state=0, scoring="neg_mean_squared_error")
print("  sklearn (aumento del ECM):", np.round(sk.importances_mean, 4))
prueba(sk.importances_mean[2] < 1e-3 and sk.importances_mean[0] > sk.importances_mean[1] > 0.0, "orden de importancias")

# Bosque aleatorio y variable duplicada
rf = RandomForestRegressor(200, random_state=0, n_jobs=1).fit(X[tr], lP[tr])
imp1 = permutation_importance(rf, X[te], lP[te], n_repeats=20, random_state=0).importances_mean
Xd = np.c_[X, la + rng.normal(0, 0.05, n)]               # copia casi idéntica de ln a
rf2 = RandomForestRegressor(200, random_state=0, n_jobs=1).fit(Xd[tr], lP[tr])
imp2 = permutation_importance(rf2, Xd[te], lP[te], n_repeats=20, random_state=0).importances_mean
print(f"Bosque: importancia de ln a sola = {imp1[0]:.3f}; con una copia correlacionada: ln a = {imp2[0]:.3f}, copia = {imp2[3]:.3f}")
prueba(imp2[0] < imp1[0], "la copia reparte la importancia")

# (2) Consistencia física fuera del dominio: a = 30 au
x0 = np.array([[np.log(30.0), np.log(1.0), 0.0]])
fisica = 1.5 * np.log(30.0)
print(f"ln P predicho en a = 30 au, M = 1 (fuera del entrenamiento): lineal {lin.predict(x0)[0]:.3f}, bosque {rf.predict(x0)[0]:.3f}, ley {fisica:.3f}")
prueba(abs(lin.predict(x0)[0] - fisica) < 0.05 and abs(rf.predict(x0)[0] - fisica) > 0.5, "extrapolación")
print("Pruebas superadas.")
