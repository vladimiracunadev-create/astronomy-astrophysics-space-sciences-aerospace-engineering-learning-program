#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C03: resolucion radiometrica (cuantizacion) y espectral (respuesta de banda).

Datos: bits y limites de banda publicados por USGS para Landsat 8 (OLI 12 bits; banda 5 infrarrojo cercano 0.85-0.88 um; banda 4 rojo
0.64-0.67 um; consultada 2026-11-09). El rango de radiancia (0-300 W m^-2 sr^-1 um^-1) y los espectros son ILUSTRATIVOS / SINTETICOS.
Modelo: cuantizador uniforme de N bits sobre [-1, 1] aplicado a una sinusoide a plena escala; SQNR teorica = 6.02 N + 1.76 dB.
Respuesta espectral gaussiana con FWHM igual al ancho de la banda; promedio de banda = integral(R(l) S(l)) / integral(S(l)).
Validez: sinusoide de frecuencia incomensurable con el muestreo; ruido de cuantizacion uniforme. Tolerancia: SQNR medida frente a teorica < 0.5 dB.
Requiere numpy (se imprime la version).
"""
import math, platform
import numpy as np


def sqnr(bits, n=1000003):
    t = np.arange(n)
    x = np.sin(2 * math.pi * 0.0618033988749895 * t + 0.3)
    pasos = 2 ** bits
    q = 2.0 / pasos
    xq = (np.floor(x / q) + 0.5) * q
    xq = np.clip(xq, -1 + q / 2, 1 - q / 2)
    ruido = xq - x
    return 10 * math.log10(np.mean(x**2) / np.mean(ruido**2))


def promedio_banda(espectro, centro, fwhm):
    sigma = fwhm / (2 * math.sqrt(2 * math.log(2)))
    lam = np.linspace(centro - 4 * sigma, centro + 4 * sigma, 4001)
    s = np.exp(-0.5 * ((lam - centro) / sigma) ** 2)
    return float(np.sum(espectro(lam) * s) / np.sum(s))


def calcular():
    r = {}
    for b in (8, 12, 16):
        r[f"niveles_{b}"] = 2**b
        r[f"sqnr_{b}"] = sqnr(b)
        r[f"teo_{b}"] = 6.02 * b + 1.76
    r["paso_12"] = 300.0 / 2**12
    r["paso_8"] = 300.0 / 2**8
    lineal = lambda l: 0.2 + 0.5 * (l - 0.8)  # espectro lineal sintetico
    escalon = lambda l: np.where(l < 0.865, 0.1, 0.5)  # escalon sintetico en el centro de la banda
    r["lin_banda"] = promedio_banda(lineal, 0.865, 0.03)
    r["lin_centro"] = float(lineal(0.865))
    r["esc_banda_centrada"] = promedio_banda(escalon, 0.865, 0.03)
    r["esc_banda_corrida"] = promedio_banda(escalon, 0.875, 0.03)
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print("bits  niveles   SQNR medida [dB]  SQNR teorica [dB]")
    for b in (8, 12, 16):
        print(f"{b:4d}  {r['niveles_'+str(b)]:7d}   {r['sqnr_'+str(b)]:16.2f}  {r['teo_'+str(b)]:17.2f}")
    print(f"Paso de cuantizacion para 0-300 W m^-2 sr^-1 um^-1 (ilustrativo): 8 bits = {r['paso_8']:.4f} ; 12 bits = {r['paso_12']:.4f}")
    print(f"Espectro lineal: promedio de banda = {r['lin_banda']:.5f} ; valor en el centro = {r['lin_centro']:.5f}")
    print(f"Espectro con escalon: banda centrada = {r['esc_banda_centrada']:.4f} ; banda corrida 10 nm = {r['esc_banda_corrida']:.4f}")
    for b in (8, 12, 16):
        assert abs(r[f"sqnr_{b}"] - r[f"teo_{b}"]) < 0.5
    assert abs(r["lin_banda"] - r["lin_centro"]) < 1e-6
    assert abs(r["esc_banda_centrada"] - 0.3) < 1e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
