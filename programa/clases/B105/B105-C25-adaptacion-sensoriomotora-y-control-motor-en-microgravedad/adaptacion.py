#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C25: adaptacion sensoriomotora con un modelo de estado-espacio de una tasa (datos SINTETICOS).

Modelo: x_{n+1} = A x_n + B e_n con error e_n = p_n - x_n (p = perturbacion, x = estado de la adaptacion, en grados). Entonces x_{n+1} = (A - B) x_n + B p. Tasa de aprendizaje
lambda = A - B por ensayo; estado estacionario x* = B p/(1 - A + B). Valores ILUSTRATIVOS: A = 0.95 (retencion), B = 0.20 (sensibilidad al error), p = 30 grados durante
40 ensayos y luego 0 (lavado, 40 ensayos). Observaciones: y_n = x_n + ruido N(0, 2 grados) (SINTETICAS, semilla 105). Ajuste de A y B por rejilla de minimos cuadrados.
Interpretacion: p representa una perturbacion de la relacion movimiento-visual o de la gravedad; no se uso ningun dato de microgravedad. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np


def simular(a, b, p_vec):
    x = 0.0
    xs = []
    for p in p_vec:
        xs.append(x)
        e = p - x
        x = a * x + b * e
    return np.array(xs)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): A = 0.95, B = 0.20, perturbacion 30 grados x 40 ensayos, luego lavado de 40; ruido 2 grados")
    a, b = 0.95, 0.20
    p = np.concatenate([np.full(40, 30.0), np.zeros(40)])
    x = simular(a, b, p)
    xstar = b * 30 / (1 - a + b)
    lam = a - b
    print(f"Tasa lambda = A - B = {lam:.2f} por ensayo; estado estacionario x* = {xstar:.1f} grados ({100 * xstar / 30:.0f} % de la perturbacion); constante de tiempo = {-1 / np.log(lam):.2f} ensayos")
    print("Ensayo: " + " ".join(f"{i:5d}" for i in (0, 1, 2, 5, 10, 20, 39, 40, 41, 45, 60, 79)))
    print("x [gr]: " + " ".join(f"{x[i]:5.1f}" for i in (0, 1, 2, 5, 10, 20, 39, 40, 41, 45, 60, 79)))
    print(f"Error al inicio = 30.0 grados; error en el ensayo 10 = {30 - x[10]:.1f}; en el 39 = {30 - x[39]:.1f}")
    print(f"Postefecto al retirar la perturbacion (ensayo 40): x = {x[40]:.1f} grados, es decir error de {-x[40]:.1f} grados; vuelve a menos de 1 grado en el ensayo {int(np.argmax(np.abs(x[40:]) < 1.0)) + 40}")
    rng = np.random.default_rng(105)
    y = x + rng.normal(0, 2.0, x.size)
    mejor = (1e18, 0, 0)
    for aa in np.linspace(0.80, 1.0, 201):
        for bb in np.linspace(0.02, 0.50, 241):
            e = np.sum((y - simular(aa, bb, p)) ** 2)
            if e < mejor[0]:
                mejor = (e, aa, bb)
    print(f"Ajuste por rejilla a 80 observaciones ruidosas: A = {mejor[1]:.3f} (verdad {a}), B = {mejor[2]:.3f} (verdad {b}); SSE = {mejor[0]:.1f}; lambda ajustada = {mejor[1] - mejor[2]:.3f}")
    # ahorro: segunda exposicion con B mayor tras experiencia
    x2 = simular(0.95, 0.30, p)
    print(f"Segunda exposicion con B = 0.30 (mas sensibilidad al error): x en el ensayo 10 = {x2[10]:.1f} grados frente a {x[10]:.1f}; ahorro = {x2[10] - x[10]:.1f} grados")
    # error de aprendizaje con ruido: cuantos ensayos para reducir el error a la mitad
    n_med = np.log(0.5) / np.log(lam)
    print(f"Ensayos para reducir a la mitad la distancia al estado estacionario = {n_med:.2f}")
    assert abs(xstar - 24.0) < 1e-9
    assert abs(x[39] - xstar) < 1.0
    assert abs(mejor[1] - a) < 0.05 and abs(mejor[2] - b) < 0.1
    assert x2[10] > x[10]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
