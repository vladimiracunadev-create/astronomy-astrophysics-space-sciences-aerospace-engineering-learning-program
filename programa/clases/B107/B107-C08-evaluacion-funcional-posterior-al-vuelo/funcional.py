#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B107-C08: bateria funcional posterior al vuelo con datos SINTETICOS: puntuacion compuesta, concordancia entre evaluadores y MDC.

TODO SINTETICO: 15 tripulantes inventados y tres pruebas con tiempos en segundos (menor es mejor): levantarse de una silla 5 veces (media previa 9.0 s),
recorrido con obstaculos (media previa 14.0 s) y marcha en tandem de 3 m (media previa 6.0 s). Dia de retorno R+1: el tiempo se multiplica por un factor
de deficit (1.45, 1.30 y 1.60 de media). No son datos de astronautas ni de ninguna mision. Semilla 107.
Definiciones: % del valor previo = 100 * previo/posterior (100 = igual que antes; menor = peor). Compuesto = media geometrica de los tres %.
Concordancia de dos evaluadores: sesgo y limites de acuerdo de Bland-Altman (media +- 1.96 s de las diferencias). SEM = s_dif/sqrt(2); MDC95 = 1.96 sqrt(2) SEM.
Verificacion: la media geometrica coincide con exp(media de logaritmos); la MDC95 es igual a 1.96 s_dif; el 95 % de las diferencias cae dentro de los limites
de acuerdo (+-3 puntos porcentuales). Numpy.
"""
from __future__ import annotations
import platform
import numpy as np

PRUEBAS = ["silla x5", "obstaculos", "tandem 3 m"]
PREV = np.array([9.0, 14.0, 6.0])
DEF = np.array([1.45, 1.30, 1.60])


def main():
    rng = np.random.default_rng(107)
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 107): 15 tripulantes inventados, 3 pruebas; factores de deficit 1.45, 1.30 y 1.60")
    n = 15
    ind = rng.lognormal(0, 0.10, (n, 3))  # variabilidad individual
    previo = PREV * ind
    post = previo * DEF * rng.lognormal(0, 0.08, (n, 3))
    pct = 100 * previo / post
    comp = np.exp(np.mean(np.log(pct), axis=1))
    comp2 = pct.prod(axis=1) ** (1 / 3)
    assert np.allclose(comp, comp2)
    for j, p in enumerate(PRUEBAS):
        print(f"{p}: previo = {previo[:, j].mean():.2f} s; R+1 = {post[:, j].mean():.2f} s; % del previo = {pct[:, j].mean():.1f} +- {pct[:, j].std(ddof=1):.1f}")
    print(f"Compuesto (media geometrica) R+1: media = {comp.mean():.1f} %; minimo = {comp.min():.1f} %; maximo = {comp.max():.1f} %")
    # dos evaluadores sobre el compuesto: el evaluador B tiene un sesgo de +1.5 puntos y ruido 2.5
    a = comp + rng.normal(0, 2.0, n)
    b = comp + 1.5 + rng.normal(0, 2.5, n)
    d = b - a
    sesgo, sd = d.mean(), d.std(ddof=1)
    lo, hi = sesgo - 1.96 * sd, sesgo + 1.96 * sd
    dentro = float(np.mean((d >= lo) & (d <= hi)) * 100)
    print(f"Bland-Altman (B - A): sesgo = {sesgo:.2f} puntos; s = {sd:.2f}; limites de acuerdo = [{lo:.2f}; {hi:.2f}]; dentro = {dentro:.0f} %")
    sem = sd / np.sqrt(2)
    mdc = 1.96 * np.sqrt(2) * sem
    print(f"SEM = {sem:.2f}; MDC95 = {mdc:.2f} puntos (= 1.96 s_dif = {1.96*sd:.2f})")
    assert abs(mdc - 1.96 * sd) < 1e-9 and dentro >= 90
    # una mejoria de 5 puntos entre R+1 y R+5 es mayor que la MDC?
    print(f"Una mejora de 5 puntos {'supera' if 5 > mdc else 'NO supera'} la MDC95 ({mdc:.2f}): {'es distinguible del error' if 5 > mdc else 'no es distinguible del error de medida'}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
