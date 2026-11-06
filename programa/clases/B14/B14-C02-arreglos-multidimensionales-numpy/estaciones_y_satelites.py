#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C02: arreglos NumPy y difusión (broadcasting).

Datos: SINTÉTICOS. Cinco estaciones en la superficie de una Tierra esférica de
radio 6378.137 km (radio ecuatorial, NASA NSSDC Earth Fact Sheet 2024) y seis
satélites en una órbita circular de 7000 km, con posiciones definidas en el
propio script (longitudes y latitudes de ejemplo; no son estaciones reales).
Modelo: posiciones cartesianas x = r cos(lat) cos(lon), y = r cos(lat) sin(lon),
z = r sin(lat) en un sistema fijo a la Tierra (ejes: x hacia lon 0, z al polo
norte). Distancia = norma euclídea de la diferencia.
Supuestos: Tierra esférica, sin rotación, geometría estática.
Validez: demostración de formas, tipos y difusión; no es geodesia.
Tolerancia: 1e-9 relativa contra el bucle puro y contra casos exactos
(antípodas: distancia 2R; mismo punto: 0).
"""
from __future__ import annotations
import math, platform, sys
import numpy as np

R_T = 6378.137  # km


def a_cartesianas(r, lat_deg, lon_deg):
    lat, lon = np.radians(lat_deg), np.radians(lon_deg)
    return np.stack([r * np.cos(lat) * np.cos(lon),
                     r * np.cos(lat) * np.sin(lon),
                     r * np.sin(lat) * np.ones_like(lon)], axis=-1)


def distancias_difusion(sat, est):
    """sat (S,3), est (E,3) -> (S,E) sin bucles: sat[:,None,:] - est[None,:,:]."""
    return np.linalg.norm(sat[:, None, :] - est[None, :, :], axis=-1)


def distancias_bucle(sat, est):
    out = np.empty((len(sat), len(est)))
    for i, s in enumerate(sat):
        for j, e in enumerate(est):
            out[i, j] = math.sqrt(sum((s[k] - e[k]) ** 2 for k in range(3)))
    return out


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}")
    est = a_cartesianas(R_T, np.array([0., 45., -30., 60., 10.]),
                        np.array([0., 90., 180., -60., 30.]))
    sat = a_cartesianas(7000.0, np.array([0., 20., 40., -20., 10., 0.]),
                        np.array([0., 60., 120., 180., -120., -60.]))
    print(f"est.shape={est.shape} sat.shape={sat.shape} dtype={est.dtype} "
          f"strides={est.strides} nbytes={est.nbytes}")
    print(f"sat[:,None,:].shape={sat[:, None, :].shape}  est[None,:,:].shape={est[None, :, :].shape}")

    d = distancias_difusion(sat, est)
    print(f"d.shape={d.shape}  mínimo={d.min():.1f} km  máximo={d.max():.1f} km")
    prueba(d.shape == (6, 5), "forma del resultado")
    prueba(np.allclose(d, distancias_bucle(sat, est), rtol=1e-9), "difusión = bucle")

    # casos exactos
    a = a_cartesianas(R_T, np.array([30.]), np.array([40.]))
    b = a_cartesianas(R_T, np.array([-30.]), np.array([220.]))      # antípoda
    prueba(abs(distancias_difusion(a, b)[0, 0] - 2 * R_T) < 1e-6, "antípodas = 2R")
    prueba(distancias_difusion(a, a)[0, 0] == 0.0, "mismo punto = 0")
    # el satélite no puede estar más cerca que 7000-R_T ni más lejos que 7000+R_T
    prueba(d.min() >= 7000 - R_T - 1e-9 and d.max() <= 7000 + R_T + 1e-9, "cotas triangulares")
    print("antípodas = 2R, mismo punto = 0, cotas triangulares: correctos")

    # vistas frente a copias
    v = est[:, :2]
    prueba(np.shares_memory(v, est), "una rebanada es vista")
    c = est[[0, 1]]
    prueba(not np.shares_memory(c, est), "indexar con lista copia")
    print("rebanada comparte memoria (vista); indexación con lista copia")

    # un error de forma explícito
    try:
        np.zeros((4, 3)) + np.zeros(4)
    except ValueError as e:
        print(f"difusión incompatible: {e}")

    # acumulación float32 vs float64
    x = np.full(10_000_000, 0.1, dtype=np.float32)
    s32, s64 = x.sum(dtype=np.float32), x.sum(dtype=np.float64)
    print(f"suma 1e7 x 0.1: float32={s32:.1f}  float64={s64:.1f}  valor ideal={0.1*1e7:.1f}")
    prueba(abs(s64 - 1e6) / 1e6 < 1e-4, "suma float64")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
