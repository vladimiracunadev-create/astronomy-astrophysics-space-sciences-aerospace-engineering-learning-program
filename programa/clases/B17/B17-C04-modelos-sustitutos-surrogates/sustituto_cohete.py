#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C04: un modelo sustituto (proceso gaussiano) de un simulador.

Datos: SIMULADOS. Simulador: ascenso vertical de un cohete sonda en vuelo
libre (sin empuje) con gravedad constante g = 9,80665 m/s^2 (valor estándar,
NIST) y arrastre cuadrático, deceleración total g + k v^2, integrado con
solve_ivp. Salida: altura máxima h_max (m) en función de v0 (m/s) y k (1/m).
Referencia exacta: h_max = ln(1 + k v0^2 / g) / (2 k)  (y v0^2/(2g) si k -> 0).
Sustituto: GaussianProcessRegressor (núcleo RBF anisótropo + ruido blanco
mínimo) entrenado con 64 puntos de muestreo Sobol (scipy.stats.qmc) sobre
v0 en [200, 1000] m/s y log10 k en [-4.5, -3.0], y evaluado en 500 puntos
distintos del mismo dominio y en puntos FUERA del dominio.
Supuestos: g constante, densidad del aire constante (k fijo), sin viento.
Validez: dentro del dominio de entrenamiento. Tolerancia: simulador vs.
fórmula 1e-4 m; sustituto, error relativo máximo < 2 % dentro del dominio.
"""
import platform
import sys
import warnings

import numpy as np
import scipy
import sklearn
from scipy.integrate import solve_ivp
from scipy.stats import qmc
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, ConstantKernel as C

G0 = 9.80665


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def exacta(v0, k):
    return np.log1p(k * v0**2 / G0) / (2 * k)


def simulador(v0, k):
    def f(t, s):
        h, v = s
        return [v, -G0 - k * v * abs(v)]
    ev = lambda t, s: s[1]            # noqa: E731  (velocidad vertical = 0)
    ev.terminal = True
    ev.direction = -1
    sol = solve_ivp(f, [0, 200], [0.0, v0], events=ev, rtol=1e-11, atol=1e-9)
    return sol.y_events[0][0][0]


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "| scikit-learn", sklearn.__version__, "|", platform.system())

# 1) Verificar el simulador contra la fórmula exacta
casos = [(300.0, 1e-4), (600.0, 5e-4), (900.0, 2e-5)]
peor = 0.0
for v0, k in casos:
    d = abs(simulador(v0, k) - exacta(v0, k))
    peor = max(peor, d)
    print(f"v0 = {v0:.0f} m/s, k = {k:.0e} 1/m: simulador {simulador(v0, k):.4f} m, exacta {exacta(v0, k):.4f} m, |dif| = {d:.1e} m")
prueba(peor < 1e-4, "simulador contra fórmula")
prueba(abs(exacta(500.0, 1e-9) - 500.0**2 / (2 * G0)) < 1.0, "límite sin arrastre")

# 2) Entrenar el sustituto
def a_fisico(u):
    return np.c_[200 + 800 * u[:, 0], 10 ** (-4.5 + 1.5 * u[:, 1])]

sob = qmc.Sobol(2, scramble=True, seed=7)
Xe = a_fisico(sob.random(64))
ye = np.array([simulador(v, k) for v, k in Xe])
def normaliza(X):
    return np.c_[(X[:, 0] - 200) / 800, (np.log10(X[:, 1]) + 4.5) / 1.5]
ker = C(1.0) * RBF([0.5, 0.5], (0.05, 20)) + WhiteKernel(1e-8, (1e-12, 1e-4))
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    gp = GaussianProcessRegressor(ker, normalize_y=True, n_restarts_optimizer=5, random_state=0)
    gp.fit(normaliza(Xe), ye)
print("Núcleo ajustado:", gp.kernel_)

# 3) Evaluar dentro del dominio
Xt = a_fisico(np.random.default_rng(11).random((500, 2)))
yt = exacta(Xt[:, 0], Xt[:, 1])
mu, sd = gp.predict(normaliza(Xt), return_std=True)
rel = np.abs(mu - yt) / yt
cobertura = np.mean(np.abs(mu - yt) <= 2 * sd)
print(f"Dentro del dominio: error relativo medio {rel.mean():.2e}, máximo {rel.max():.2e}; "
      f"la banda ±2 sigma cubre el {100*cobertura:.1f} % de los puntos")
prueba(rel.max() < 0.02, "error dentro del dominio")

# 4) Fuera del dominio: v0 = 1100-1500 m/s
Xf = np.c_[np.linspace(1100, 1500, 5), np.full(5, 10 ** -3.75)]
muf, sdf = gp.predict(normaliza(Xf), return_std=True)
relf = np.abs(muf - exacta(Xf[:, 0], Xf[:, 1])) / exacta(Xf[:, 0], Xf[:, 1])
for v, r, s in zip(Xf[:, 0], relf, sdf):
    print(f"  v0 = {v:.0f} m/s (fuera del dominio): error relativo {r:.2%}, sigma predicha {s:.0f} m")
prueba(relf[-1] > 10 * rel.max(), "fuera del dominio el sustituto debe degradarse")
print("Pruebas superadas.")
