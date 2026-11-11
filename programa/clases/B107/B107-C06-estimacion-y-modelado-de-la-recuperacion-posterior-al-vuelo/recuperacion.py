#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B107-C06: modelo exponencial de recuperacion, ajuste por minimos cuadrados e incertidumbre por remuestreo.

TODO SINTETICO/ILUSTRATIVO: una funcion (por ejemplo, fuerza de una prueba) de un tripulante INVENTADO; no son datos de astronautas.
Modelo: S(t) = S_pre - D exp(-t/tau), t en dias desde el retorno, S en % del valor previo al vuelo (S_pre = 100 %).
Parametros verdaderos ilustrativos: D = 18 % (deficit inicial), tau = 25 d. Ruido gaussiano de medida de 1.5 puntos. Mediciones en los dias
1, 3, 7, 14, 21, 30, 45, 60. Tiempo para recuperar el 95 % del deficit: t95 = tau ln(20) (ln(1/0.05)).
Ajuste: para cada tau de una malla se resuelve D por minimos cuadrados lineales; se toma el tau de menor residuo. Incertidumbre: 1000 remuestreos
parametricos (semilla 107). Verificacion: tau y D recuperados dentro de 2 desviaciones remuestreadas; t95 analitico. Numpy.
"""
from __future__ import annotations
import platform
import numpy as np

T = np.array([1, 3, 7, 14, 21, 30, 45, 60], float)


def ajusta(y, T=T):
    mejor = (1e99, None, None)
    for tau in np.linspace(5, 80, 301):
        x = -np.exp(-T / tau)
        # y - 100 = D x  -> D por minimos cuadrados
        D = float(np.sum((y - 100) * x) / np.sum(x * x))
        r = float(np.sum((y - 100 - D * x) ** 2))
        if r < mejor[0]:
            mejor = (r, tau, D)
    return mejor[1], mejor[2], mejor[0]


def main():
    rng = np.random.default_rng(107)
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS E ILUSTRATIVOS (semilla 107): un tripulante inventado; D = 18 %, tau = 25 d, ruido 1.5 puntos")
    D0, TAU0, SIG = 18.0, 25.0, 1.5
    y = 100 - D0 * np.exp(-T / TAU0) + rng.normal(0, SIG, len(T))
    tau, D, r = ajusta(y)
    print("Datos (dia: % del previo): " + ", ".join(f"{int(t)}: {v:.1f}" for t, v in zip(T, y)))
    print(f"Ajuste: tau = {tau:.1f} d; D = {D:.1f} %; residuo cuadratico = {r:.2f}")
    taus, Ds = [], []
    for _ in range(1000):
        yb = 100 - D * np.exp(-T / tau) + rng.normal(0, SIG, len(T))
        a, b, _ = ajusta(yb)
        taus.append(a)
        Ds.append(b)
    taus, Ds = np.array(taus), np.array(Ds)
    print(f"Remuestreo: tau = {taus.mean():.1f} +- {taus.std():.1f} d (IC 95 %: {np.percentile(taus,2.5):.1f}-{np.percentile(taus,97.5):.1f}); D = {Ds.mean():.1f} +- {Ds.std():.1f} %")
    assert abs(tau - TAU0) <= 2 * taus.std() and abs(D - D0) <= 2 * Ds.std()
    t95 = tau * np.log(20)
    print(f"t95 estimado = {t95:.1f} d (IC 95 %: {np.percentile(taus*np.log(20),2.5):.1f}-{np.percentile(taus*np.log(20),97.5):.1f}); t95 verdadero = {TAU0*np.log(20):.1f} d")
    # efecto de pocos datos: solo los dias 1-14 (4 puntos)
    T4 = T[:4]
    t4 = []
    for _ in range(300):
        yb = 100 - D0 * np.exp(-T4 / TAU0) + rng.normal(0, SIG, 4)
        t4.append(ajusta(yb, T4)[0])
    t4 = np.array(t4)
    print(f"Solo con los dias 1-14: tau remuestreado = {t4.mean():.1f} +- {t4.std():.1f} d (frente a +- {taus.std():.1f} d con 8 puntos hasta el dia 60)")
    assert t4.std() > taus.std()
    assert t95 > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
