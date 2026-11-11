#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B107-C05: razon de carga aguda:cronica (ACWR) con media movil y con media exponencial, y un riesgo logistico ILUSTRATIVO.

TODO SINTETICO/ILUSTRATIVO: cargas diarias inventadas en unidades arbitrarias (u.a.); la relacion carga-lesion NO esta validada
y los umbrales (0.8-1.3) son del ejemplo, no de ninguna fuente consultada. Semilla 107.
Definiciones: aguda = media de 7 dias; cronica = media de 28 dias (movil) o EWMA con lambda = 2/(N+1). ACWR = aguda / cronica.
Verificacion: la EWMA recursiva coincide con la suma ponderada explicita; un salto de carga de +60 % en una semana eleva el ACWR por encima de 1.3.
Tolerancias: diferencia EWMA recursiva vs explicita < 1e-9; ACWR en semana de salto > 1.3. Numpy.
"""
from __future__ import annotations
import platform
import numpy as np


def movil(x, n):
    c = np.cumsum(np.insert(x, 0, 0))
    out = np.full(len(x), np.nan)
    for i in range(n - 1, len(x)):
        out[i] = (c[i + 1] - c[i + 1 - n]) / n
    return out


def ewma(x, n):
    lam = 2 / (n + 1)
    y = np.zeros(len(x))
    y[0] = x[0]
    for i in range(1, len(x)):
        y[i] = lam * x[i] + (1 - lam) * y[i - 1]
    return y


def ewma_explicita(x, n, i):
    lam = 2 / (n + 1)
    k = np.arange(i + 1)
    pesos = lam * (1 - lam) ** (i - k)
    pesos[0] = (1 - lam) ** i
    return float(np.sum(pesos * x[: i + 1]))


def main():
    rng = np.random.default_rng(107)
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS E ILUSTRATIVOS (semilla 107): cargas en u.a.; umbrales 0.8-1.3 del ejemplo, sin fuente")
    dias = 70
    carga = rng.normal(100, 8, dias)
    carga[[6, 13, 20, 27, 34, 41, 48, 55, 62, 69]] = 0.0  # descanso semanal
    carga[56:63] *= 1.6  # semana de salto (+60 %)
    ag = movil(carga, 7)
    cr = movil(carga, 28)
    acwr = ag / cr
    ag_e, cr_e = ewma(carga, 7), ewma(carga, 28)
    dif = max(abs(ag_e[i] - ewma_explicita(carga, 7, i)) for i in (10, 30, 69))
    print(f"EWMA recursiva vs suma ponderada explicita: diferencia maxima = {dif:.2e}")
    assert dif < 1e-9
    sem_base = acwr[55]
    sem_salto = acwr[62]
    print(f"ACWR (media movil) al dia 55 = {sem_base:.2f}; al final de la semana de salto (dia 62) = {sem_salto:.2f}")
    print(f"ACWR (EWMA) al dia 55 = {ag_e[55]/cr_e[55]:.2f}; dia 62 = {ag_e[62]/cr_e[62]:.2f}")
    assert sem_salto > 1.3
    marcados = [int(i) for i in range(27, dias) if acwr[i] > 1.3]
    print(f"Dias con ACWR > 1.3 (umbral del ejemplo): {marcados}")
    # riesgo logistico ilustrativo: logit = -3 + 2.5 (ACWR - 1)^2 ... forma en U
    def riesgo(a):
        return 1 / (1 + np.exp(-(-3.0 + 3.0 * (a - 1.0) ** 2)))
    for a in (0.6, 1.0, 1.3, 1.6):
        print(f"Riesgo ilustrativo (forma en U inventada) para ACWR {a:.1f}: {riesgo(a)*100:.1f} %")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
