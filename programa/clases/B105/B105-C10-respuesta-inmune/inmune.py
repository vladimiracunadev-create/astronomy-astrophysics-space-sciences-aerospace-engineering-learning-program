#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C10: reactivacion viral y muestreo periodico: cuantos episodios se detectan (datos SINTETICOS).

Modelo: cada persona sufre episodios de reactivacion (p. ej. de un virus latente) como proceso de Poisson de tasa lambda = 0.02 por dia (ILUSTRATIVA);
cada episodio es detectable en muestras durante una ventana de d = 3 dias (ILUSTRATIVA); se toma una muestra cada s dias con sensibilidad del ensayo
q = 0.90. Probabilidad de detectar un episodio con muestreo periodico en fase aleatoria: p = q min(1, d/s) (analitica). Mision de 180 dias, tripulacion
de 6, semilla 105, 20000 misiones simuladas. No se consultaron datos de inmunologia espacial; esto es un ejercicio de muestreo. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

LAM, D, Q, DIAS, N = 0.02, 3.0, 0.90, 180.0, 6


def p_detecta(s):
    return Q * min(1.0, D / s)


def simular(s, rng, misiones=20000):
    total = rng.poisson(LAM * DIAS * N, misiones)
    det = np.zeros(misiones, dtype=int)
    for i in range(misiones):
        inicios = rng.uniform(0, DIAS, total[i])
        fase = rng.uniform(0, s)
        # hay una muestra en fase + k s; el episodio es detectable en [inicio, inicio + D)
        k = np.ceil((inicios - fase) / s)
        t_muestra = fase + k * s
        visible = t_muestra < inicios + D
        det[i] = np.sum(visible & (rng.uniform(size=total[i]) < Q))
    return total, det


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): lambda 0.02/dia, ventana 3 dias, sensibilidad 0.90; tripulacion de 6; mision de 180 dias; sin datos reales")
    print(f"Episodios esperados por mision = {LAM * DIAS * N:.2f}; por persona = {LAM * DIAS:.2f}; P(persona sin episodios) = {np.exp(-LAM * DIAS):.4f}")
    rng = np.random.default_rng(105)
    print("intervalo s [d] | p analitica | fraccion detectada (sim.) | detectados por mision | P(ningun detectado | hubo episodios)")
    sim = {}
    for s in (1, 3, 7, 14, 30):
        tot, det = simular(s, rng)
        frac = det.sum() / max(tot.sum(), 1)
        hubo = tot > 0
        p0 = np.mean(det[hubo] == 0)
        sim[s] = frac
        print(f"   {s:3d}          |   {p_detecta(s):.3f}     |   {frac:.3f}                  |   {det.mean():5.2f}                |   {p0:.3f}")
    print(f"Con s = 7: se pierden en media {100 * (1 - sim[7]):.1f} % de los episodios; con s = 1: {100 * (1 - sim[1]):.1f} % (solo por la sensibilidad)")
    s_necesario = D * Q / 0.5
    print(f"Intervalo maximo para detectar al menos el 50 % de los episodios = {s_necesario:.1f} dias (q min(1,d/s) = 0.5)")
    assert abs(sim[1] - 0.90) < 0.01
    assert abs(sim[7] - 0.90 * 3 / 7) < 0.02
    assert sim[1] > sim[3] > sim[7] > sim[14] > sim[30]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
