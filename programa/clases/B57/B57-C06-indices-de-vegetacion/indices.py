#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C06: indices de vegetacion (NDVI y SAVI) y su saturacion.

Datos: SINTETICOS. Modelo de dosel simplificado ILUSTRATIVO: R(LAI) = R_suelo exp(-k LAI) + R_dosel (1 - exp(-k LAI)), con
rojo: suelo 0.20, dosel 0.04, k = 0.8 ; infrarrojo cercano (NIR): suelo 0.30, dosel 0.50, k = 0.5. Suelo oscuro: rojo 0.10, NIR 0.15.
Definicion NDVI = (NIR - rojo)/(NIR + rojo) (NASA Earth Observatory, consultada 2026-11-09); en Landsat 8 equivale a (B5 - B4)/(B5 + B4)
con las bandas descritas por USGS (consultada 2026-11-09). SAVI = (1 + L)(NIR - rojo)/(NIR + rojo + L) con L = 0.5 (formula conocida, NO CONSULTADA).
Modelo: NDVI y SAVI en funcion del indice de area foliar (LAI) y del suelo de fondo. Validez: ilustrativa, no es un modelo de transferencia radiativa.
Tolerancia: derivada numerica frente a analitica < 1e-6 relativa; NDVI siempre en [-1, 1].
Requiere numpy.
"""
import platform
import numpy as np

ROJO = dict(suelo=0.20, dosel=0.04, k=0.8)
NIR = dict(suelo=0.30, dosel=0.50, k=0.5)
ROJO_OSC = dict(suelo=0.10, dosel=0.04, k=0.8)
NIR_OSC = dict(suelo=0.15, dosel=0.50, k=0.5)


def refl(p, lai):
    e = np.exp(-p["k"] * lai)
    return p["suelo"] * e + p["dosel"] * (1 - e)


def ndvi(nir, rojo):
    return (nir - rojo) / (nir + rojo)


def savi(nir, rojo, L=0.5):
    return (1 + L) * (nir - rojo) / (nir + rojo + L)


def calcular():
    r = {}
    lai = np.linspace(0, 8, 801)
    n = ndvi(refl(NIR, lai), refl(ROJO, lai))
    r["ndvi_0"], r["ndvi_2"], r["ndvi_4"], r["ndvi_6"], r["ndvi_8"] = (float(n[int(x * 100)]) for x in (0, 2, 4, 6, 8))
    r["ndvi_lim"] = (NIR["dosel"] - ROJO["dosel"]) / (NIR["dosel"] + ROJO["dosel"])
    r["lai_06"] = float(lai[np.argmax(n >= 0.6)])
    r["gan_0_2"] = r["ndvi_2"] - r["ndvi_0"]
    r["gan_4_6"] = r["ndvi_6"] - r["ndvi_4"]
    # suelo de fondo con LAI = 1
    n_cl = float(ndvi(refl(NIR, 1.0), refl(ROJO, 1.0)))
    n_os = float(ndvi(refl(NIR_OSC, 1.0), refl(ROJO_OSC, 1.0)))
    s_cl = float(savi(refl(NIR, 1.0), refl(ROJO, 1.0)))
    s_os = float(savi(refl(NIR_OSC, 1.0), refl(ROJO_OSC, 1.0)))
    r["ndvi_suelo_claro"], r["ndvi_suelo_oscuro"] = n_cl, n_os
    r["savi_suelo_claro"], r["savi_suelo_oscuro"] = s_cl, s_os
    r["dif_ndvi"], r["dif_savi"] = abs(n_cl - n_os), abs(s_cl - s_os)
    # derivada analitica dNDVI/dNIR = 2 rojo / (NIR + rojo)^2 frente a diferencia finita
    nir0, rojo0, h = 0.45, 0.05, 1e-6
    num = (ndvi(nir0 + h, rojo0) - ndvi(nir0 - h, rojo0)) / (2 * h)
    ana = 2 * rojo0 / (nir0 + rojo0) ** 2
    r["err_deriv"] = abs(num / ana - 1)
    r["ndvi_min"], r["ndvi_max"] = float(n.min()), float(n.max())
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print("NDVI sintetico segun LAI: " + " ; ".join(f"LAI {l}: {r['ndvi_'+str(l)]:.3f}" for l in (0, 2, 4, 6, 8)))
    print(f"Limite NDVI del dosel puro = {r['ndvi_lim']:.3f} ; LAI en que NDVI llega a 0.6 = {r['lai_06']:.2f}")
    print(f"Ganancia de NDVI entre LAI 0 y 2 = {r['gan_0_2']:.3f} ; entre LAI 4 y 6 = {r['gan_4_6']:.3f}")
    print(f"LAI = 1: NDVI suelo claro = {r['ndvi_suelo_claro']:.3f} ; suelo oscuro = {r['ndvi_suelo_oscuro']:.3f} ; diferencia = {r['dif_ndvi']:.3f}")
    print(f"LAI = 1: SAVI suelo claro = {r['savi_suelo_claro']:.3f} ; suelo oscuro = {r['savi_suelo_oscuro']:.3f} ; diferencia = {r['dif_savi']:.3f}")
    print(f"Error relativo de la derivada numerica = {r['err_deriv']:.2e}")
    assert -1 <= r["ndvi_min"] and r["ndvi_max"] <= 1
    assert r["err_deriv"] < 1e-6
    assert r["gan_4_6"] < 0.2 * r["gan_0_2"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
