#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C09: integración por sustitución y masa de columna.

Datos: atmósfera isotérmica SINTÉTICA, rho(h) = rho0 exp(-h/H) con
rho0 = 1.2 kg/m3 y H = 8.0 km (parámetros de ejemplo; no son los de una
atmósfera estándar publicada). g_n = 9.80665 m/s2 (exacta; CODATA 2022, NIST).
Modelo: masa de columna por unidad de área sobre la altitud h0,
   Sigma(h0) = int_{h0}^{inf} rho dh = rho0 H exp(-h0/H)
obtenida con la sustitución u = -h/H (du = -dh/H). Presión hidrostática
p = g Sigma (equilibrio, g constante).
Verificación numérica con la regla del trapecio compuesta (se estudia en C11)
contra las primitivas obtenidas por sustitución.
Supuestos: g constante, T constante. Validez: altitudes < ~100 km del modelo.
Tolerancias: 1e-6 relativa en las integrales comprobadas.
"""
from __future__ import annotations
import math, platform, sys

RHO0, H, G_N = 1.2, 8000.0, 9.80665


def trapecio(f, a, b, n=200_000):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b)) + sum(f(a + i * h) for i in range(1, n))
    return s * h


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def cerca(a, b, tol=1e-6):
    return abs(a - b) <= tol * max(1.0, abs(b))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    # integrales definidas por sustitución
    casos = [
        ("int_0^1 (3x+1)^5 dx = (4^6-1)/18", lambda x: (3 * x + 1) ** 5, 0.0, 1.0, (4**6 - 1) / 18),
        ("int_0^2 2x cos(x^2) dx = sin 4", lambda x: 2 * x * math.cos(x * x), 0.0, 2.0, math.sin(4.0)),
        ("int_0^3 x/(1+x^2) dx = ln(10)/2", lambda x: x / (1 + x * x), 0.0, 3.0, 0.5 * math.log(10.0)),
    ]
    for nombre, f, a, b, ex in casos:
        num = trapecio(f, a, b)
        prueba(cerca(num, ex), nombre)
        print(f"{nombre}: exacto = {ex:.8f}; trapecio = {num:.8f}")
    # columna de atmósfera
    print("\n  h0 [km]   Sigma [kg/m2]   fracción sobre h0   p = g Sigma [Pa]")
    sigma0 = RHO0 * H
    for h0_km in (0, 5.545, 10, 20, 50):
        h0 = h0_km * 1000.0
        sig = RHO0 * H * math.exp(-h0 / H)
        # comprobación numérica hasta h0 + 100 km (cola e^-12.5 ~ 4e-6 de la columna)
        num = trapecio(lambda h: RHO0 * math.exp(-h / H), h0, h0 + 100_000.0, 100_000)
        prueba(cerca(num, sig, 1e-4), f"Sigma({h0_km} km)")
        print(f"  {h0_km:7.3f}  {sig:13.2f}  {sig/sigma0:17.4f}  {G_N*sig:15.1f}")
    h_mitad = H * math.log(2.0)
    prueba(cerca(RHO0 * H * math.exp(-h_mitad / H), 0.5 * sigma0, 1e-12), "altitud de la mitad")
    print(f"\nAltitud que deja la mitad de la masa de columna encima = H ln 2 = {h_mitad/1000:.4f} km")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
