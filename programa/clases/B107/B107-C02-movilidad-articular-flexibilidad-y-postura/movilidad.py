#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B107-C02: rango articular, alcance de un brazo plano de dos segmentos y par resistivo de un traje.

TODO SINTETICO/ILUSTRATIVO: longitudes y rigideces inventadas, no medidas de personas ni de trajes reales.
Sistema: plano sagital, origen en el hombro, x hacia delante, y hacia arriba; angulos en grados (hombro: 0 = brazo colgando
hacia abajo, positivo = flexion hacia delante; codo: 0 = extendido, positivo = flexion). Segmentos: 0.30 m (brazo), 0.27 m (antebrazo+mano
hasta el punto de agarre). Rangos libres: hombro -40..170 deg, codo 0..145 deg.
Traje ilustrativo: par resistivo tau = k * theta_rel con k = 0.5 N m/deg en el hombro y 0.3 N m/deg en el codo, de modo que, con un
par maximo disponible de 25 N m (hombro) y 15 N m (codo), el rango util es theta <= tau_max / k.
Verificacion: area del espacio de trabajo por malla fina frente a Monte Carlo (semilla 107); alcance maximo analitico L1+L2.
Tolerancias: area malla vs Monte Carlo <= 3 %; alcance maximo = 0.57 m +- 1e-9. Numpy.
"""
from __future__ import annotations
import platform
import numpy as np

L1, L2 = 0.30, 0.27


def punto(h, c):
    """h, c en grados -> (x, y) del punto de agarre. Brazo colgando (h=0) apunta a -y."""
    h = np.radians(h)
    c = np.radians(c)
    x1, y1 = L1 * np.sin(h), -L1 * np.cos(h)
    x2, y2 = x1 + L2 * np.sin(h + c), y1 - L2 * np.cos(h + c)
    return x2, y2


def area_malla(hmin, hmax, cmin, cmax, n=721):
    h = np.linspace(hmin, hmax, n)
    c = np.linspace(cmin, cmax, n)
    H, C = np.meshgrid(h, c)
    x, y = punto(H, C)
    celda = 0.01  # m
    ix = np.floor(x / celda).astype(int)
    iy = np.floor(y / celda).astype(int)
    return len(set(zip(ix.ravel().tolist(), iy.ravel().tolist()))) * celda**2


def area_mc(hmin, hmax, cmin, cmax, rng, n=400000):
    h = rng.uniform(hmin, hmax, n)
    c = rng.uniform(cmin, cmax, n)
    x, y = punto(h, c)
    celda = 0.01
    ix = np.floor(x / celda).astype(int)
    iy = np.floor(y / celda).astype(int)
    return len(set(zip(ix.tolist(), iy.tolist()))) * celda**2


def main():
    rng = np.random.default_rng(107)
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS E ILUSTRATIVOS (semilla 107): brazo plano L1 = 0.30 m, L2 = 0.27 m; traje inventado")
    ar = {
        "libre (hombro -40..170, codo 0..145)": (-40, 170, 0, 145),
    }
    kh, kc, th, tc = 0.5, 0.3, 25.0, 15.0
    hmax_traje = th / kh  # 50 deg
    cmax_traje = tc / kc  # 50 deg
    ar["traje (par max 25 y 15 N m; hombro 0..50, codo 0..50)"] = (0, hmax_traje, 0, cmax_traje)
    ar["traje + hombro recuperado a 90 deg (movilidad entrenada)"] = (0, 90, 0, cmax_traje)
    res = {}
    for nombre, (a, b, c, d) in ar.items():
        am = area_malla(a, b, c, d)
        amc = area_mc(a, b, c, d, rng)
        dif = abs(am - amc) / am * 100
        res[nombre] = am
        print(f"{nombre}: area malla = {am:.3f} m2; Monte Carlo = {amc:.3f} m2; diferencia = {dif:.2f} %")
        assert dif <= 3.0
    alc = float(np.hypot(*punto(0, 0)))
    print(f"Alcance maximo con brazo extendido hacia abajo: {alc:.4f} m (analitico L1+L2 = {L1+L2:.4f} m)")
    assert abs(alc - (L1 + L2)) < 1e-9
    libre, traje = list(res.values())[0], list(res.values())[1]
    print(f"Reduccion del espacio de trabajo por el traje: {100*(1-traje/libre):.1f} % (area {libre:.3f} -> {traje:.3f} m2)")
    # par resistivo en una tarea: elevar la mano a 60 deg de hombro con traje
    print(f"Par resistivo del hombro a 60 deg: {kh*60:.1f} N m (> par disponible {th:.0f} N m: el rango util termina en {hmax_traje:.0f} deg)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
