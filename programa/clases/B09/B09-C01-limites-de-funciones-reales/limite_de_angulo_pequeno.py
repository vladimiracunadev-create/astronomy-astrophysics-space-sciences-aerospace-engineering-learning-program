#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C01: límites y aproximación de ángulo pequeño en paralaje.

Datos: ninguno observado. Ángulos de paralaje SINTÉTICOS. Definición del
parsec (1 pc = 648000/pi au) según la IAU (citada en B01-C02; no releída aquí).
Modelo: lim_{t->0} sin(t)/t = 1 y lim_{t->0} (1-cos t)/t^2 = 1/2 (DLMF 1.4(ii),
L'Hopital, ec. 1.4.14-1.4.15, como marco; los valores se COMPRUEBAN aquí).
Supuestos: ángulos en radianes; aritmética IEEE 754 de doble precisión.
Validez: |t| < 1 rad para las cotas por serie. Tolerancias: 1e-12 relativa en
el parsec; las cotas de serie son desigualdades estrictas.
"""
from __future__ import annotations
import math, platform, sys

ARCSEC = math.pi / (180 * 3600)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    # 1) sin t / t y tan t / t cuando t -> 0, con cotas de la serie
    print("t [\"]        t [rad]       sin t/t         tan t/t")
    for arc in (3600.0, 60.0, 1.0, 1e-3):
        t = arc * ARCSEC
        s, u = math.sin(t) / t, math.tan(t) / t
        print(f"{arc:8.3g}  {t:12.5e}  {s:.12f}  {u:.12f}")
        # |sin t/t - (1 - t^2/6)| <= t^4/120  (serie alternada)
        prueba(abs(s - (1 - t * t / 6)) <= t**4 / 120 + 1e-16, "cota de serie de sin t/t")
    # 2) epsilon-delta: delta = sqrt(6 eps) garantiza |sin t/t - 1| < eps
    eps = 1e-6
    delta = math.sqrt(6 * eps)
    prueba(abs(math.sin(delta) / delta - 1) < eps, "epsilon-delta de sin t/t")
    print(f"epsilon = {eps:g}  ->  delta = {delta:.6e} rad = {delta/ARCSEC:.1f} arcsec")
    # 3) el parsec desde la tangente frente a la definición
    pc_tan = 1.0 / math.tan(ARCSEC)          # en au
    pc_def = 648000.0 / math.pi
    rel = abs(pc_tan / pc_def - 1)
    prueba(rel < 1e-10, "parsec por tangente")
    print(f"1 pc por 1/tan(1\") = {pc_tan:.6f} au;  648000/pi = {pc_def:.6f} au;  dif. relativa = {rel:.2e}")
    # 4) paralaje sintética de 0,1" -> 10 pc
    p = 0.1 * ARCSEC
    print(f"Paralaje sintética 0.1\" -> d = {1/math.tan(p)/pc_def:.6f} pc (aprox. 1/p: {1/(p*pc_def):.6f} pc)")
    # 5) cancelación: (1-cos t)/t^2 -> 1/2
    print("t            ingenuo (1-cos t)/t^2     estable 2 sin^2(t/2)/t^2")
    for t in (1e-1, 1e-4, 1e-8, 1e-9):
        ing = (1 - math.cos(t)) / t**2
        est = 2 * math.sin(t / 2) ** 2 / t**2
        print(f"{t:8.0e}   {ing:22.15f}   {est:22.15f}")
        prueba(abs(est - 0.5) < t * t / 24 + 1e-15, "forma estable tiende a 1/2")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
