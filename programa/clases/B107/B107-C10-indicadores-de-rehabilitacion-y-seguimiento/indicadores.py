#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B107-C10: indicadores de rehabilitacion: tiempo hasta el criterio con censura (Kaplan-Meier) y control CUSUM de estancamiento.

TODO SINTETICO/ILUSTRATIVO: una cohorte de 40 tripulantes inventados. Tiempo hasta el criterio ~ exponencial de media 30 dias; seguimiento
maximo de 45 dias (los que no alcanzan el criterio quedan CENSURADOS). Semilla 107.
Indicadores: (1) % de recuperacion = 100 (x - x_R1)/(x_previo - x_R1) donde x es una medida y x_R1 la del dia 1; (2) tiempo hasta el criterio; (3) CUSUM de
la pendiente semanal para detectar estancamiento.
Verificacion: (a) el estimador Kaplan-Meier se compara con el conteo directo en tiempos sin censura previa y con la forma cerrada exp(-t/30) (tolerancia +-0.12 por
muestra pequena); (b) el CUSUM, con parametros k = 0.5 y h = 4 (en desviaciones), detecta un estancamiento introducido el dia 28 y la tasa de falsas alarmas sin
estancamiento es < 10 % en 300 simulaciones. Numpy.
"""
from __future__ import annotations
import platform
import numpy as np


def kaplan_meier(t, evento):
    orden = np.argsort(t)
    t, evento = t[orden], evento[orden]
    s, riesgo, curva = 1.0, len(t), []
    for u in np.unique(t[evento == 1]):
        n_riesgo = int(np.sum(t >= u))
        d = int(np.sum((t == u) & (evento == 1)))
        s *= 1 - d / n_riesgo
        curva.append((float(u), s, n_riesgo))
    return curva


def S_en(curva, tt):
    s = 1.0
    for u, v, _ in curva:
        if u <= tt:
            s = v
    return s


def cusum_bajo(x, mu0, sd, k=0.5, h=4.0):
    c = 0.0
    for i, v in enumerate(x):
        z = (mu0 - v) / sd  # desviacion hacia abajo respecto de lo esperado
        c = max(0.0, c + z - k)
        if c > h:
            return i
    return None


def main():
    rng = np.random.default_rng(107)
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS E ILUSTRATIVOS (semilla 107): cohorte de 40; tiempo al criterio exp(media 30 d); seguimiento 45 d")
    n = 40
    tt = rng.exponential(30.0, n)
    evento = (tt <= 45.0).astype(int)
    obs = np.minimum(tt, 45.0)
    print(f"Alcanzan el criterio: {evento.sum()} de {n}; censurados en el dia 45: {n - evento.sum()}")
    curva = kaplan_meier(obs, evento)
    for t0 in (15.0, 30.0, 45.0):
        km = S_en(curva, t0)
        # conteo directo (sin censura antes de 45): proporcion que aun no alcanza
        directo = float(np.mean(obs > t0)) if t0 < 45 else float(np.mean(obs >= 45.0))
        print(f"t = {t0:4.0f} d: KM S = {km:.3f}; conteo directo = {directo:.3f}; teorico exp(-t/30) = {np.exp(-t0/30):.3f}")
        assert abs(km - directo) < 1e-9 or t0 == 45.0
        assert abs(km - np.exp(-t0 / 30)) <= 0.12
    # mediana
    med = next((u for u, s, _ in curva if s <= 0.5), None)
    print(f"Mediana de tiempo al criterio (KM) = {med:.1f} d (teorica {30*np.log(2):.1f} d)")
    # CUSUM
    esp = 5.0  # mejora esperada por semana (puntos de %), ilustrativa
    sdm = 3.0
    dias_det = []
    fa = 0
    for _ in range(300):
        x = rng.normal(esp, sdm, 12)
        if cusum_bajo(x, esp, sdm) is not None:
            fa += 1
    ret = []
    for _ in range(300):
        x = rng.normal(esp, sdm, 12)
        x[4:] = rng.normal(0.5, sdm, 8)
        d = cusum_bajo(x, esp, sdm)
        if d is not None:
            ret.append(d - 4)
    print(f"CUSUM (k = 0.5, h = 4): falsas alarmas sin estancamiento = {fa/3:.1f} % de 300; con estancamiento desde la semana 5 se detecta en {len(ret)/3:.1f} % de 300 corridas, con {np.mean(ret):.1f} semanas de retraso tras la primera semana estancada (indice base 0)")
    assert fa / 300 < 0.10 and len(ret) / 300 > 0.8
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
