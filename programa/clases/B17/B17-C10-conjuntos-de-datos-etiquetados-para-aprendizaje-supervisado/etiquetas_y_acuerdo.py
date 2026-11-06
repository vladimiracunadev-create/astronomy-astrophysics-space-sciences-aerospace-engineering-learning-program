#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C10: calidad de las etiquetas, acuerdo entre anotadores y ruido.

Datos: SINTÉTICOS. 20 000 objetos con clase verdadera binaria equiprobable
(p. ej. «espiral» / «elíptica») y tres anotadores que aciertan cada uno con
probabilidad p = 0,8, con errores independientes.
Referencias exactas:
 (1) acuerdo observado entre dos anotadores: p^2 + (1-p)^2 = 0,68;
 (2) kappa de Cohen con clases equiprobables: (0,68 - 0,5)/(1 - 0,5) = 0,36;
 (3) exactitud del voto mayoritario de 3: p^3 + 3 p^2 (1-p) = 0,896;
 (4) exactitud medida de un clasificador de exactitud verdadera A contra
     etiquetas con ruido simétrico eta: A (1-eta) + (1-A) eta.
Modelo: regresión logística sobre una característica gaussiana (clases +-1,
sigma 1; exactitud máxima Phi(1) = 0,8413). Tolerancias: 0,01.
"""
import platform
import sys
from math import erf, sqrt

import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import cohen_kappa_score


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


Phi = lambda x: 0.5 * (1 + erf(x / sqrt(2)))  # noqa: E731
print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scikit-learn", sklearn.__version__, "|", platform.system())
rng = np.random.default_rng(10)
n, p = 20000, 0.8
y = rng.integers(0, 2, n)
an = np.array([np.where(rng.random(n) < p, y, 1 - y) for _ in range(3)])

acu = (an[0] == an[1]).mean()
kap = cohen_kappa_score(an[0], an[1])
print(f"Acuerdo entre dos anotadores: {acu:.4f} (teoría {p*p + (1-p)**2:.4f}); kappa {kap:.4f} (teoría 0,3600)")
prueba(abs(acu - 0.68) < 0.01 and abs(kap - 0.36) < 0.02, "acuerdo y kappa")
voto = (an.sum(0) >= 2).astype(int)
av = (voto == y).mean()
print(f"Exactitud del voto mayoritario de 3: {av:.4f} (teoría {p**3 + 3*p*p*(1-p):.4f}); un anotador solo: {(an[0]==y).mean():.4f}")
prueba(abs(av - 0.896) < 0.01, "voto mayoritario")

# Característica física y ruido de etiquetas
x = rng.normal(np.where(y == 1, 1.0, -1.0), 1.0).reshape(-1, 1)
A = Phi(1.0)
tr, te = slice(0, 10000), slice(10000, n)
m_limpio = LogisticRegression().fit(x[tr], y[tr])
m_ruido = LogisticRegression().fit(x[tr], an[0][tr])
acc_limpia = m_limpio.score(x[te], y[te])
acc_cr = m_ruido.score(x[te], y[te])
print(f"Entrenado con etiquetas limpias, evaluado limpio: {acc_limpia:.4f} (techo {A:.4f}); entrenado con etiquetas con 20 % de ruido, evaluado limpio: {acc_cr:.4f}")
eta = 0.2
medida = m_limpio.score(x[te], an[0][te])
print(f"Mismo modelo limpio evaluado contra etiquetas ruidosas: {medida:.4f} (teoría {A*(1-eta) + (1-A)*eta:.4f})")
prueba(abs(medida - (A * (1 - eta) + (1 - A) * eta)) < 0.01, "ruido de evaluación")
prueba(abs(acc_cr - acc_limpia) < 0.01, "ruido simétrico apenas afecta al entrenamiento")
print("Pruebas superadas.")
