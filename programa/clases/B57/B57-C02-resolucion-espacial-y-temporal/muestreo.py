#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C02: resolucion espacial (GSD, barrido, aliasing) y temporal (ciclos de repeticion).

Datos: cifras publicadas de Landsat 8 (altitud 705 km, pixel 30 m, barrido 185 km, ciclo de 16 dias con 8 dias de desfase al sumar
Landsat 9; USGS, consultada 2026-11-09) y de Sentinel-2 (barrido 290 km, pixel 10 m; SentiWiki, consultada 2026-11-09).
La escena con una senal de periodo 50 m es SINTETICA (una sinusoide); no hay imagen observada.
Modelo: IFOV = GSD/H en nadir; pixeles por linea = barrido/GSD; GSD en el borde del barrido con Tierra plana (aproximacion);
aliasing: la frecuencia aparente de una sinusoide muestreada a paso g es |f - k/g| con k entero que minimiza.
Sistema de referencia: distancias en el suelo, en metros; angulos desde el nadir.
Validez: Tierra plana, ignora la curvatura (error de segundo orden en el borde de 185 km). Tolerancia: periodo aparente medido por DFT = teorico < 1 %.
"""
import math, platform

H = 705e3
GSD = 30.0
BARRIDO_L8, BARRIDO_S2, GSD_S2 = 185e3, 290e3, 10.0


def dft_pico(muestras, paso):
    """Frecuencia (ciclos/m) del maximo de la DFT directa en (0, Nyquist]."""
    n = len(muestras)
    m = sum(muestras) / n
    x = [v - m for v in muestras]
    mejor, kmax = -1.0, 0
    for k in range(1, n // 2 + 1):
        re = sum(x[i] * math.cos(2 * math.pi * k * i / n) for i in range(n))
        im = sum(x[i] * math.sin(2 * math.pi * k * i / n) for i in range(n))
        p = re * re + im * im
        if p > mejor:
            mejor, kmax = p, k
    return kmax / (n * paso)


def alias_teorico(periodo, g):
    f, fs = 1.0 / periodo, 1.0 / g
    return abs(f - round(f / fs) * fs)


def calcular():
    r = {}
    ifov = GSD / H
    r["ifov_urad"] = ifov * 1e6
    r["px_l8"] = BARRIDO_L8 / GSD
    r["px_s2"] = BARRIDO_S2 / GSD_S2
    th = math.atan((BARRIDO_L8 / 2) / H)
    r["theta_borde"] = math.degrees(th)
    r["gsd_borde"] = GSD / math.cos(th) ** 2
    r["mb_banda"] = (BARRIDO_L8 / GSD) ** 2 * 2 / 1e6
    r["imagenes_anio_1"] = 365.0 / 16
    r["imagenes_anio_2"] = 365.0 / 8
    n, paso = 300, GSD
    for periodo in (50.0, 20.0, 100.0):
        m = [math.sin(2 * math.pi * (i * paso) / periodo) for i in range(n)]
        f = dft_pico(m, paso)
        r[f"alias_{int(periodo)}"] = 1.0 / f
        r[f"alias_t_{int(periodo)}"] = 1.0 / alias_teorico(periodo, paso)
    r["periodo_nyquist"] = 2 * GSD
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"IFOV = GSD/H = {r['ifov_urad']:.3f} urad")
    print(f"Pixeles por linea: Landsat 8 (185 km / 30 m) = {r['px_l8']:.0f} ; Sentinel-2 (290 km / 10 m) = {r['px_s2']:.0f}")
    print(f"Borde del barrido: angulo = {r['theta_borde']:.2f} grados ; GSD cruzado = {r['gsd_borde']:.3f} m (Tierra plana)")
    print(f"Una banda de escena 185 x 185 km a 16 bits = {r['mb_banda']:.1f} MB")
    print(f"Imagenes por anio y punto sin nubes: 16 dias -> {r['imagenes_anio_1']:.1f} ; 8 dias -> {r['imagenes_anio_2']:.1f}")
    print("Aliasing con GSD = 30 m (periodo real -> aparente medido por DFT / teorico):")
    for p in (50, 20, 100):
        print(f"  {p:4d} m -> {r['alias_'+str(p)]:.2f} m / {r['alias_t_'+str(p)]:.2f} m")
    print(f"Periodo de Nyquist (2 GSD) = {r['periodo_nyquist']:.0f} m")
    assert abs(r["ifov_urad"] * 1e-6 * H - GSD) < 1e-9
    for p in (50, 20):
        assert abs(r[f"alias_{p}"] / r[f"alias_t_{p}"] - 1) < 0.01
    assert r["alias_100"] > r["periodo_nyquist"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
