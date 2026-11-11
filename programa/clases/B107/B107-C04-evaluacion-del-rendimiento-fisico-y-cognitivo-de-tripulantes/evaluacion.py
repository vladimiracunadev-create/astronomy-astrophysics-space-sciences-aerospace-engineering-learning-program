#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B107-C04: fiabilidad test-retest, error tipico, cambio fiable (RCI) y deteccion de un descenso en una bateria.

TODO SINTETICO: 12 tripulantes inventados, una prueba con media poblacional 100 y desviacion 15 (puntuacion estandar, sin unidad), semilla 107.
Modelo: puntuacion observada = verdadera + error; fiabilidad r = var_verdadera / var_total. Error tipico de medida SEM = s sqrt(1 - r).
Cambio fiable (indice de cambio fiable, Jacobson-Truax) RCI = (x2 - x1) / (sqrt(2) SEM); |RCI| > 1.96 marca un cambio mas alla del error al 95 %.
Verificacion: (a) r y SEM estimados con 2000 individuos simulados frente a los verdaderos; (b) tasa de falsas alarmas del RCI sin cambio
real frente a 5 %; (c) potencia para detectar un descenso real de 10 puntos frente a la formula normal.
Tolerancias: r estimado +-0.02; falsas alarmas 5 % +-1 punto; potencia +-2 puntos. Numpy y math.
"""
from __future__ import annotations
import math
import platform
import numpy as np


def fi(z):  # CDF normal
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def main():
    rng = np.random.default_rng(107)
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 107): media 100, s total 15, fiabilidad verdadera 0.85; no son datos de astronautas")
    s_tot, r_true = 15.0, 0.85
    s_ver = s_tot * math.sqrt(r_true)
    s_err = s_tot * math.sqrt(1 - r_true)
    n = 2000
    ver = rng.normal(100, s_ver, n)
    x1 = ver + rng.normal(0, s_err, n)
    x2 = ver + rng.normal(0, s_err, n)
    r_est = float(np.corrcoef(x1, x2)[0, 1])
    s_est = float(np.std(np.concatenate([x1, x2]), ddof=1))
    sem = s_est * math.sqrt(1 - r_est)
    print(f"Fiabilidad test-retest estimada = {r_est:.3f} (verdadera {r_true}); SEM estimado = {sem:.2f} (verdadero {s_err:.2f}) puntos")
    assert abs(r_est - r_true) <= 0.02
    sdiff = math.sqrt(2) * sem
    mdc95 = 1.96 * sdiff
    print(f"Desviacion de la diferencia = {sdiff:.2f}; cambio minimo detectable al 95 % (MDC95) = {mdc95:.2f} puntos")
    rci = (x2 - x1) / sdiff
    fa = float(np.mean(np.abs(rci) > 1.96) * 100)
    print(f"Sin cambio real: falsas alarmas del RCI = {fa:.2f} % (nominal 5 %)")
    assert abs(fa - 5) <= 1.0
    # potencia frente a descenso real de 10 puntos
    x3 = ver - 10 + rng.normal(0, s_err, n)
    pot = float(np.mean((x3 - x1) / sdiff < -1.96) * 100)
    pot_teo = fi(-1.96 + 10 / (math.sqrt(2) * s_err)) * 100
    print(f"Descenso real de 10 puntos: deteccion simulada = {pot:.1f} %; formula normal = {pot_teo:.1f} %")
    assert abs(pot - pot_teo) <= 2.0
    # 12 tripulantes: cuantos marcados con un descenso de 10 en 3 de ellos
    tri = rng.normal(100, s_ver, 12)
    base = tri + rng.normal(0, s_err, 12)
    caida = np.zeros(12)
    caida[[2, 5, 9]] = 10
    nueva = tri - caida + rng.normal(0, s_err, 12)
    marcados = np.where((nueva - base) / sdiff < -1.96)[0].tolist()
    print(f"Equipo de 12 (descenso real de 10 puntos en los tripulantes 2, 5 y 9): marcados por RCI = {marcados}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
