#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C03: la derivada como límite de cocientes de diferencia.

Datos: (GM)_E nominal = 3.986004e14 m3/s2 y R_eE nominal = 6.3781e6 m (IAU 2015
Resolución B3, arXiv:1510.07674; son factores de conversión, no estimaciones).
Lanzamiento vertical SINTÉTICO con v0 = 100 m/s.
Modelo: h(t) = v0 t - g t^2/2 con g = GM/R^2 constante (sin arrastre ni
rotación). Derivada exacta: v(t) = v0 - g t (DLMF 1.4(iii), ec. 1.4.4).
Supuestos: altura << R. Validez: h < 1 % de R (aquí h_max ~ 510 m).
Tolerancias: cociente central exacto a 1e-9 m/s en el cuadrático; error del
cociente progresivo = g*dt/2 a 1e-9 relativo.
"""
from __future__ import annotations
import math, platform, sys

GM_E = 3.986004e14
R_E = 6.3781e6
G = GM_E / R_E**2
V0 = 100.0


def altura(t):
    return V0 * t - 0.5 * G * t * t


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def progresivo(f, x, h):
    return (f(x + h) - f(x)) / h


def central(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    print(f"g = GM/R^2 = {G:.5f} m/s2")
    t0 = 4.0
    v_exacta = V0 - G * t0
    print(f"t = {t0} s: v exacta = {v_exacta:.6f} m/s")
    print("   dt [s]    progresivo   error      central      error")
    for dt in (1.0, 0.1, 0.01, 1e-3, 1e-6, 1e-9, 1e-12):
        p, c = progresivo(altura, t0, dt), central(altura, t0, dt)
        print(f"{dt:9.0e}  {p:11.6f}  {p-v_exacta:10.2e}  {c:11.6f}  {c-v_exacta:10.2e}")
    # pruebas
    prueba(abs(progresivo(altura, t0, 0.01) - v_exacta - (-G * 0.01 / 2)) < 1e-9,
           "error del progresivo = -g dt/2")
    prueba(abs(central(altura, t0, 0.1) - v_exacta) < 1e-9, "central exacto en cuadrática")
    # apogeo: v = 0
    t_ap = V0 / G
    h_max = V0**2 / (2 * G)
    prueba(abs(central(altura, t_ap, 1e-3)) < 1e-6, "v = 0 en el apogeo")
    print(f"Apogeo: t = {t_ap:.4f} s, h = {h_max:.3f} m")
    # función no polinómica: orden de convergencia
    f, df = math.sin, math.cos
    e1 = abs(progresivo(f, 1.0, 1e-3) - df(1.0))
    e2 = abs(progresivo(f, 1.0, 1e-4) - df(1.0))
    c1 = abs(central(f, 1.0, 1e-3) - df(1.0))
    c2 = abs(central(f, 1.0, 1e-2) - df(1.0))
    print(f"sin'(1): razón de errores progresivo 1e-3/1e-4 = {e1/e2:.2f} (orden 1); "
          f"central 1e-2/1e-3 = {c2/c1:.1f} (orden 2)")
    prueba(8 < e1 / e2 < 12, "orden 1")
    prueba(80 < c2 / c1 < 120, "orden 2")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
