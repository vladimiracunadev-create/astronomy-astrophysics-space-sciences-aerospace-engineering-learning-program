#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C14: eventos medicos de una mision como proceso de Poisson y consumo de recursos (datos SINTETICOS).

Tasa de eventos lambda = 0.5 por persona-anio (SINTETICA, no es una estadistica de vuelo). Tripulacion de 6, mision de 180 dias. Gravedad por evento:
leve 80 %, moderado 18 %, grave 2 % (SINTETICA) con consumo de 1, 3 y 8 unidades de recursos (kits, tiempo de tripulacion; unidades arbitrarias).
Reserva de 20 unidades. Probabilidad analitica de al menos un evento: 1 - exp(-lambda n T). Simulacion de 100000 misiones, semilla 105.
Contenido educativo: no define criterios de evacuacion, triaje ni tratamiento; solo ejercita probabilidades. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np
from math import exp, factorial

LAM, N, DIAS = 0.5, 6, 180
P_G = np.array([0.80, 0.18, 0.02]); COSTE = np.array([1, 3, 8]); RESERVA = 20


def pois(k, mu):
    return exp(-mu) * mu ** k / factorial(k)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): tasa 0.5/persona-anio; gravedad 80/18/2 %; costes 1/3/8 unidades; reserva 20; sin estadisticas reales")
    mu = LAM * N * DIAS / 365.25
    print(f"Eventos esperados en la mision mu = {mu:.3f}; P(0) = {pois(0, mu):.4f}; P(>=1) = {1 - exp(-mu):.4f}; P(>=3) = {1 - sum(pois(k, mu) for k in range(3)):.4f}")
    rng = np.random.default_rng(105)
    m = 100000
    n_ev = rng.poisson(mu, m)
    gasto = np.zeros(m)
    graves = np.zeros(m, dtype=int)
    for i in np.nonzero(n_ev)[0]:
        g = rng.choice(3, size=n_ev[i], p=P_G)
        gasto[i] = COSTE[g].sum(); graves[i] = (g == 2).sum()
    print(f"Simulacion: media de eventos = {n_ev.mean():.3f}; P(>=1) = {np.mean(n_ev >= 1):.4f}; P(>=3) = {np.mean(n_ev >= 3):.4f}")
    print(f"Consumo de recursos: media {gasto.mean():.2f}, p95 = {np.percentile(gasto, 95):.0f}; P(consumo > reserva de {RESERVA}) = {np.mean(gasto > RESERVA):.5f}")
    print(f"P(al menos un evento grave) = {np.mean(graves >= 1):.4f} (analitica {1 - exp(-mu * P_G[2]):.4f})")
    for lam in (0.25, 0.5, 1.0, 2.0):
        mu2 = lam * N * DIAS / 365.25
        print(f"  lambda = {lam:4.2f}/persona-anio: mu = {mu2:5.2f}; P(>=1) = {1 - exp(-mu2):.3f}")
    # la reserva necesaria para cubrir el 99 % de las misiones
    q99 = np.percentile(gasto, 99)
    print(f"Reserva que cubre el 99 % de las misiones simuladas = {q99:.0f} unidades")
    assert abs(np.mean(n_ev >= 1) - (1 - exp(-mu))) < 0.005
    assert abs(n_ev.mean() - mu) < 0.02
    assert abs(np.mean(graves >= 1) - (1 - exp(-mu * P_G[2]))) < 0.002
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
