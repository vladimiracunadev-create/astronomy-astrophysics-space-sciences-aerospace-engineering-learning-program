#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C03: movimiento rectilíneo uniformemente acelerado y circular.

Datos: SINTÉTICOS para la parte rectilínea; GM y radio de la Tierra de NASA NSSDC
(Earth Fact Sheet) para la parte circular. Modelo: MRUA con a constante y
movimiento circular uniforme. Supuestos: a constante; trayectoria circular de
radio fijo. Dominio de validez: velocidades << c; sin rozamiento. Tolerancia:
1e-9 relativa entre fórmulas cerradas e integración exacta por pasos.
"""
from __future__ import annotations
import math
import sys

GM = 3.9860e14
RE = 6_378_137.0

def mrua(x0: float, v0: float, a: float, t: float) -> tuple[float, float]:
    return x0 + v0 * t + 0.5 * a * t * t, v0 + a * t

def circular(h: float) -> dict[str, float]:
    r = RE + h
    v = math.sqrt(GM / r)
    return {"r": r, "v": v, "T": 2 * math.pi * r / v, "w": v / r, "ac": v * v / r}

def main() -> int:
    # Prueba 1: pasos de MRUA componen igual que un único salto
    x, v = 0.0, 100.0
    for _ in range(10):
        x, v = mrua(x, v, 2.0, 1.0)
    xe, ve = mrua(0.0, 100.0, 2.0, 10.0)
    assert abs(x - xe) < 1e-9 and abs(v - ve) < 1e-9
    # Prueba 2: v² = v0² + 2 a Δx
    assert abs(ve**2 - (100.0**2 + 2 * 2.0 * xe)) < 1e-6
    # Prueba 3: a_c = GM/r² (gravedad local) en la órbita circular
    c = circular(400_000.0)
    assert abs(c["ac"] - GM / c["r"]**2) / c["ac"] < 1e-12
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"MRUA: tras 10 s con a=2 m/s^2 y v0=100 m/s: x = {xe:.1f} m, v = {ve:.1f} m/s")
    print(f"Frenado desde 100 m/s con a=-5 m/s^2: se detiene en t = {100/5:.1f} s, recorre {100**2/(2*5):.1f} m")
    for h in (400e3, 2000e3, 35_786e3):
        c = circular(h)
        print(f"h = {h/1e3:8.0f} km: v = {c['v']:8.1f} m/s, T = {c['T']/3600:7.3f} h, a_c = {c['ac']:.3f} m/s^2")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
