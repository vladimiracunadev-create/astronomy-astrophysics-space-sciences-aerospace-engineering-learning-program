#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B17-C03: red informada por la física para dos EDO.

Datos: SIMULADOS/SINTÉTICOS. Caso A: y' = -k y, y(0)=1, k=1,5 (solución exacta
exp(-k t)). Caso B: y'' + w^2 y = 0, y(0)=1, y'(0)=0, w=2 (solución cos(w t)).
Modelo: red de una capa oculta N(t) = c + sum_i v_i tanh(w_i t + b_i) con
H = 10 neuronas; sus derivadas se calculan en forma analítica:
  N'  = sum v_i w_i (1 - T_i^2),  N'' = sum v_i w_i^2 (-2 T_i (1 - T_i^2)),
con T_i = tanh(w_i t + b_i). Pérdida = suma de residuos^2 de la EDO en 60
puntos de colocación + condiciones iniciales (peso 10). Optimizador:
scipy.optimize.least_squares (método trf, Jacobiano por diferencias finitas).
Supuestos: EDO exacta conocida, dominio t en [0, 3]. Validez: solo ese
dominio. Tolerancias: error máximo < 5e-3 (A) y < 2e-2 (B).
Línea base: la misma red ajustada solo a datos ruidosos en [0, 1] y
evaluada hasta t = 3 (sin la EDO).
"""
import platform
import sys

import numpy as np
import scipy
from scipy.optimize import least_squares

H = 10
T_MAX = 3.0


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def desempaquetar(p):
    return p[:H], p[H:2 * H], p[2 * H:3 * H], p[3 * H]   # v, w, b, c


def red(p, t):
    v, w, b, c = desempaquetar(p)
    T = np.tanh(np.outer(t, w) + b)
    return c + T @ v


def red_d1(p, t):
    v, w, b, _ = desempaquetar(p)
    T = np.tanh(np.outer(t, w) + b)
    return (1 - T**2) @ (v * w)


def red_d2(p, t):
    v, w, b, _ = desempaquetar(p)
    T = np.tanh(np.outer(t, w) + b)
    return (-2 * T * (1 - T**2)) @ (v * w**2)


# Prueba de las derivadas analíticas contra diferencias centradas
rng = np.random.default_rng(3)
p0 = rng.normal(0, 1, 3 * H + 1)
tt = np.linspace(0, 3, 7)
h = 1e-5
d1_fd = (red(p0, tt + h) - red(p0, tt - h)) / (2 * h)
d2_fd = (red(p0, tt + h) - 2 * red(p0, tt) + red(p0, tt - h)) / h**2
prueba(np.allclose(red_d1(p0, tt), d1_fd, atol=1e-6), "primera derivada")
prueba(np.allclose(red_d2(p0, tt), d2_fd, atol=1e-3), "segunda derivada")

tc = np.linspace(0, T_MAX, 60)           # puntos de colocación
tev = np.linspace(0, T_MAX, 301)         # evaluación


def entrenar(res, semilla):
    r = np.random.default_rng(semilla)
    p = np.r_[r.normal(0, 0.5, H), r.normal(0, 1.0, H), r.normal(0, 1.0, H), 0.0]
    return least_squares(res, p, method="trf", max_nfev=1500, ftol=1e-14, xtol=1e-14, gtol=1e-14).x


k = 1.5
res_a = lambda p: np.r_[red_d1(p, tc) + k * red(p, tc), 10 * (red(p, np.array([0.0])) - 1.0)]  # noqa: E731
pa = entrenar(res_a, 1)
err_a = np.max(np.abs(red(pa, tev) - np.exp(-k * tev)))

w0 = 2.0
res_b = lambda p: np.r_[red_d2(p, tc) + w0**2 * red(p, tc),                                    # noqa: E731
                        10 * (red(p, np.array([0.0])) - 1.0), 10 * red_d1(p, np.array([0.0]))]
pb = entrenar(res_b, 2)
err_b = np.max(np.abs(red(pb, tev) - np.cos(w0 * tev)))

# Línea base solo con datos: 8 puntos ruidosos en [0,1], sin EDO
r = np.random.default_rng(4)
td = np.linspace(0, 1, 8)
yd = np.exp(-k * td) + r.normal(0, 0.01, td.size)
pd_ = entrenar(lambda p: red(p, td) - yd, 5)
err_d_dentro = np.max(np.abs(red(pd_, td) - np.exp(-k * td)))
tex = tev[tev > 1.0]
err_d_fuera = np.max(np.abs(red(pd_, tex) - np.exp(-k * tex)))

print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "|", platform.system())
print(f"Caso A (decaimiento, k=1,5): error máximo en [0,3] = {err_a:.2e}")
print(f"Caso B (oscilador, w=2):     error máximo en [0,3] = {err_b:.2e}")
print(f"Solo datos (8 puntos con ruido, [0,1]): error en datos {err_d_dentro:.2e}; extrapolando a [1,3] {err_d_fuera:.2e}")
prueba(err_a < 5e-3, "caso A")
prueba(err_b < 2e-2, "caso B")
prueba(err_d_fuera > 5 * err_a, "la línea base solo con datos debe extrapolar peor")
print("Pruebas superadas.")
