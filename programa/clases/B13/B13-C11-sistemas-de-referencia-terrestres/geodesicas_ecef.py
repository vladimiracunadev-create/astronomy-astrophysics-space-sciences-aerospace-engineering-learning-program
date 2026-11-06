#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C11: coordenadas geodesicas <-> cartesianas terrestres.

Datos: elipsoide GRS80 (IERS Conventions 2010, TN36, Tabla 1.2, consultada
2026-11-05): a = 6378137 m, 1/f = 298.257222101, omega = 7.292115e-5 rad/s.
Estacion de ejemplo SINTETICA: latitud -24.6 grados, longitud -70.4 grados,
altura elipsoidal 2500 m (zona de desierto de Atacama; coordenadas
aproximadas de ejemplo, no de un instrumento concreto).
Modelo: N = a / sqrt(1 - e2 sin^2 phi); X = (N+h) cos phi cos lam;
Y = (N+h) cos phi sin lam; Z = (N (1-e2) + h) sin phi. Inversa por
iteracion de punto fijo sobre la latitud. e2 = f (2 - f).
Supuestos: marco ECEF del elipsoide GRS80 sin movimiento de placas ni mareas;
altura elipsoidal (no ortometrica). Validez: |h| << a.
Tolerancia: ida y vuelta < 1e-9 m en posicion y 1e-12 grados en angulos.
"""
from __future__ import annotations
import math
import platform
import sys

A = 6378137.0
F = 1.0 / 298.257222101
E2 = F * (2.0 - F)
B = A * (1.0 - F)
OMEGA = 7.292115e-5


def a_ecef(lat_deg, lon_deg, h):
    p, l = math.radians(lat_deg), math.radians(lon_deg)
    n = A / math.sqrt(1.0 - E2 * math.sin(p) ** 2)
    return ((n + h) * math.cos(p) * math.cos(l),
            (n + h) * math.cos(p) * math.sin(l),
            (n * (1.0 - E2) + h) * math.sin(p))


def a_geodesicas(x, y, z):
    lon = math.atan2(y, x)
    p = math.hypot(x, y)
    lat = math.atan2(z, p * (1.0 - E2))
    for _ in range(20):
        n = A / math.sqrt(1.0 - E2 * math.sin(lat) ** 2)
        h = p / math.cos(lat) - n if abs(lat) < 1.3 else z / math.sin(lat) - n * (1.0 - E2)
        nueva = math.atan2(z, p * (1.0 - E2 * n / (n + h)))
        if abs(nueva - lat) < 1e-15:
            lat = nueva
            break
        lat = nueva
    n = A / math.sqrt(1.0 - E2 * math.sin(lat) ** 2)
    h = p / math.cos(lat) - n if abs(lat) < 1.3 else z / math.sin(lat) - n * (1.0 - E2)
    return math.degrees(lat), math.degrees(lon), h


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"b = a(1-f) = {B:.4f} m ; e2 = {E2:.12f}")
    # Casos con respuesta conocida
    assert a_ecef(0, 0, 0) == (A, 0.0, 0.0)
    x, y, z = a_ecef(90, 0, 0)
    assert abs(z - B) < 1e-6 and abs(x) < 1e-6
    # Un punto de superficie cumple la ecuacion del elipsoide
    for lat in (-80, -45, -24.6, 0, 33, 61):
        x, y, z = a_ecef(lat, 17.0, 0.0)
        assert abs((x * x + y * y) / A ** 2 + z * z / B ** 2 - 1.0) < 1e-12
    # Ida y vuelta en una malla amplia
    peor = 0.0
    for lat in range(-89, 90, 7):
        for lon in range(-180, 181, 15):
            for h in (-400.0, 0.0, 2500.0, 700000.0):
                x, y, z = a_ecef(lat, lon, h)
                la, lo, hh = a_geodesicas(x, y, z)
                err = max(abs(la - lat) * 111000, abs(((lo - lon + 180) % 360) - 180) * 111000 * math.cos(math.radians(lat)), abs(hh - h))
                peor = max(peor, err)
    print(f"peor error de ida y vuelta (malla) = {peor:.2e} m")
    assert peor < 1e-6
    # Estacion de ejemplo
    x, y, z = a_ecef(-24.6, -70.4, 2500.0)
    print(f"estacion: X = {x:.3f} m, Y = {y:.3f} m, Z = {z:.3f} m")
    la, lo, hh = a_geodesicas(x, y, z)
    print(f"inversa: lat = {la:.9f}, lon = {lo:.9f}, h = {hh:.4f} m")
    assert abs(la + 24.6) < 1e-9 and abs(lo + 70.4) < 1e-9 and abs(hh - 2500) < 1e-6
    # Latitud geocentrica frente a geodesica a 45 grados
    x, y, z = a_ecef(45, 0, 0)
    geoc = math.degrees(math.atan2(z, math.hypot(x, y)))
    print(f"lat geodesica 45 -> geocentrica {geoc:.6f} (diferencia {45 - geoc:.4f} grados)")
    # Velocidad de rotacion en el ecuador y en la estacion
    print(f"velocidad por rotacion: ecuador {OMEGA*A:.3f} m/s ; estacion {OMEGA*math.hypot(*a_ecef(-24.6,-70.4,2500.0)[:2]):.3f} m/s")
    assert abs(OMEGA * A - 465.10) < 0.01
    # Distancia entre dos estaciones (cuerda)
    p1, p2 = a_ecef(-24.6, -70.4, 2500.0), a_ecef(-33.45, -70.67, 520.0)
    cuerda = math.dist(p1, p2)
    print(f"cuerda entre dos puntos de Chile (ejemplo) = {cuerda/1000:.3f} km")
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
