#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C24: fusión de una banda pancromática de alta resolución con
bandas multiespectrales de baja resolución (inyección aditiva de detalle).

Datos: SINTÉTICOS, semilla fija, con VERDAD de alta resolución conocida.
Geometría inspirada en Landsat 8/9: pancromática de 15 m con rango
0.50-0.68 um (USGS; cubre verde y rojo, no el infrarrojo cercano) y bandas
multiespectrales de 30 m (valor supuesto; la página del USGS consultada no lo indica). Verdad: tres bandas (verde, rojo, NIR) de 64 x 64 a
15 m. El detalle fino es común al verde y al rojo e INDEPENDIENTE en el NIR.
La pancromática es la media de verde y rojo; las bandas de 30 m son promedios
de bloques 2 x 2 de la verdad.
Método: F_b = MS_b(replicada a 15 m) + g_b (Pan - Pan_baja), con Pan_baja el
promedio de bloques 2 x 2 de Pan replicado; g_b = 1 o la pendiente de la
regresión de MS_b sobre Pan_baja a baja resolución.
Referencias: (1) consistencia (protocolo de Wald): el promedio de bloques de la
imagen fusionada reproduce la multiespectral original (exacto para inyección
aditiva); (2) el error frente a la verdad baja para las bandas cuyo detalle
comparte la pancromática y NO para el NIR con g = 1.
Tolerancia: 1e-12 en (1).
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def blur(a, s):
    k = np.arange(-int(4 * s) - 1, int(4 * s) + 2)
    g = np.exp(-0.5 * (k / s) ** 2)
    g /= g.sum()
    b = np.apply_along_axis(lambda v: np.convolve(np.pad(v, len(k), mode="wrap"), g, mode="same")[len(k):-len(k)], 0, a)
    return np.apply_along_axis(lambda v: np.convolve(np.pad(v, len(k), mode="wrap"), g, mode="same")[len(k):-len(k)], 1, b)


def bloques(a):
    return a.reshape(a.shape[0] // 2, 2, a.shape[1] // 2, 2).mean(axis=(1, 3))


def replicar(a):
    return np.kron(a, np.ones((2, 2)))


def rmse(a, b):
    return float(np.sqrt(np.mean((a - b) ** 2)))


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15024)
N = 64
def campo(s):
    z = blur(rng.standard_normal((N, N)), s)
    return z / z.std()

lenta = [0.40 + 0.08 * campo(6), 0.30 + 0.07 * campo(6), 0.45 + 0.10 * campo(6)]      # verde, rojo, NIR
d = rng.standard_normal((N, N))
det_comun = blur(d, 0.9) - blur(d, 2.5)
det_comun /= det_comun.std()
det_nir = rng.standard_normal((N, N))
det_nir = blur(det_nir, 0.9) - blur(det_nir, 2.5)
det_nir /= det_nir.std()
verdad = [lenta[0] + 0.04 * det_comun, lenta[1] + 0.04 * det_comun, lenta[2] + 0.04 * det_nir]
nombres = ["verde", "rojo", "NIR"]
pan = 0.5 * (verdad[0] + verdad[1])
ms = [bloques(v) for v in verdad]
pan_baja = replicar(bloques(pan))
detalle = pan - pan_baja

print("Resultados (RMSE frente a la verdad de 15 m; correlación del detalle de alta frecuencia con el verdadero):")
for g_modo in ("g = 1", "g de regresión"):
    print(f"  inyección {g_modo}:")
    for b, nom in enumerate(nombres):
        up = replicar(ms[b])
        if g_modo == "g = 1":
            g = 1.0
        else:
            pl = bloques(pan)
            g = np.cov(ms[b].ravel(), pl.ravel())[0, 1] / pl.var(ddof=1)
        F = up + g * detalle
        # consistencia
        cons = np.max(np.abs(bloques(F) - ms[b]))
        prueba(cons < 1e-12, "consistencia (promedio de bloques de F = MS)")
        hp_v = verdad[b] - replicar(bloques(verdad[b]))
        hp_f = F - replicar(bloques(F))
        corr = np.corrcoef(hp_v.ravel(), hp_f.ravel())[0, 1]
        print(f"    {nom:5s}: g = {g:+.3f}; RMSE sin fusionar {rmse(up, verdad[b]):.5f}; fusionada {rmse(F, verdad[b]):.5f}; "
              f"correlación del detalle {corr:+.3f}; consistencia {cons:.1e}")
        if g_modo == "g = 1":
            if nom in ("verde", "rojo"):
                prueba(rmse(F, verdad[b]) < rmse(up, verdad[b]), f"la fusión mejora {nom}")
            else:
                prueba(rmse(F, verdad[b]) > rmse(up, verdad[b]), "la fusión con g=1 empeora el NIR")
print("Pruebas superadas.")
