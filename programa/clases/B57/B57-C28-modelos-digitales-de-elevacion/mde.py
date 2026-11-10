#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C28: modelos digitales de elevacion: pendiente y orientacion, superficie frente a terreno, efecto de la resolucion.

Datos: Copernicus DEM GLO-30 (rejilla de 1 segundo de arco) y GLO-90 (3 segundos), modelo digital de SUPERFICIE obtenido por TanDEM-X entre 2011 y 2015, exactitud vertical
absoluta < 4 m (LE90) (Copernicus Data Space, consultada 2026-11-09). SINTETICOS: plano inclinado, paraboloide z = a (x^2 + y^2), terreno sinusoidal de 200 m de amplitud y
longitud de onda 2000 m con 15 m de arboles sobre la mitad del dominio. Radio terrestre medio 6371 km (referencia, no consultado).
Modelo: pendiente y orientacion por diferencias finitas de Horn (ventana 3 x 3) ; tamano de la celda de 1 segundo de arco en latitud y longitud; efecto de remuestrear a 3 veces el paso.
Validez: terreno suave a la escala de la celda. Tolerancia: plano exacto a 1e-9 ; paraboloide con error relativo < 1 % ; pendiente maxima subestimada al degradar la resolucion.
Requiere numpy.
"""
import math, platform
import numpy as np

RT = 6371e3


def horn(z, dx, dy):
    a, b, c = z[:-2, :-2], z[:-2, 1:-1], z[:-2, 2:]
    d, f = z[1:-1, :-2], z[1:-1, 2:]
    g, h, i = z[2:, :-2], z[2:, 1:-1], z[2:, 2:]
    dzdx = ((c + 2 * f + i) - (a + 2 * d + g)) / (8 * dx)
    dzdy = ((g + 2 * h + i) - (a + 2 * b + c)) / (8 * dy)
    pend = np.hypot(dzdx, dzdy)
    return dzdx, dzdy, pend


def calcular():
    r = {}
    r["celda_lat_m"] = math.radians(1 / 3600) * RT
    for lat in (0.0, -33.0, -60.0):
        r[f"celda_lon_{int(abs(lat))}"] = r["celda_lat_m"] * math.cos(math.radians(lat))
    dx = dy = 30.0
    y, x = np.mgrid[:101, :101].astype(float) * dx
    plano = 0.2 * x + 0.1 * y
    ex, ey, p = horn(plano, dx, dy)
    r["err_plano"] = float(np.max(np.abs(p - math.hypot(0.2, 0.1))))
    r["pend_plano_deg"] = math.degrees(math.atan(math.hypot(0.2, 0.1)))
    a = 1e-4
    xc, yc = x - 1500, y - 1500
    par = a * (xc**2 + yc**2)
    ex, ey, p = horn(par, dx, dy)
    ana = 2 * a * np.hypot(xc, yc)[1:-1, 1:-1]
    r["err_parab"] = float(np.max(np.abs(p - ana) / np.maximum(ana, 1e-9)[:]) if False else np.max(np.abs(p - ana)[ana > 0.05] / ana[ana > 0.05]))
    # terreno sinusoidal: pendiente maxima con paso 30 m y con paso 90 m
    L, A = 2000.0, 200.0
    yy, xx = np.mgrid[:301, :301].astype(float)
    terr = A * np.sin(2 * math.pi * xx * 10.0 / L)  # malla fina de 10 m
    _, _, p10 = horn(terr, 10.0, 10.0)
    t30 = terr[::3, ::3]
    t90 = terr[::9, ::9]
    _, _, p30 = horn(t30, 30.0, 30.0)
    _, _, p90 = horn(t90, 90.0, 90.0)
    r["pmax_ana"] = 2 * math.pi * A / L
    r["pmax_10"], r["pmax_30"], r["pmax_90"] = float(p10.max()), float(p30.max()), float(p90.max())
    # superficie frente a terreno
    dtm = terr.copy()
    dsm = terr.copy()
    dsm[:, 150:] += 15.0
    r["dif_dsm_dtm"] = float((dsm - dtm).max())
    r["pend_borde"] = float(horn(dsm, 10.0, 10.0)[2].max())
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Celda de 1 segundo de arco: {r['celda_lat_m']:.2f} m en latitud ; en longitud a 0 = {r['celda_lon_0']:.2f} m ; a 33 S = {r['celda_lon_33']:.2f} m ; a 60 S = {r['celda_lon_60']:.2f} m")
    print(f"Plano z = 0.2 x + 0.1 y: pendiente {r['pend_plano_deg']:.3f} grados ; error de Horn = {r['err_plano']:.1e}")
    print(f"Paraboloide: error relativo maximo de la pendiente (donde > 0.05) = {r['err_parab']:.2e}")
    print(f"Terreno sinusoidal (pendiente maxima analitica = {r['pmax_ana']:.4f}): paso 10 m = {r['pmax_10']:.4f} ; paso 30 m = {r['pmax_30']:.4f} ; paso 90 m = {r['pmax_90']:.4f}")
    print(f"Arboles de 15 m en la mitad: diferencia superficie-terreno maxima = {r['dif_dsm_dtm']:.1f} m ; pendiente maxima en el borde del bosque (paso 10 m) = {r['pend_borde']:.3f}")
    assert r["err_plano"] < 1e-9
    assert r["err_parab"] < 0.01
    assert r["pmax_90"] < r["pmax_30"] < r["pmax_10"] <= r["pmax_ana"] * 1.001
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
