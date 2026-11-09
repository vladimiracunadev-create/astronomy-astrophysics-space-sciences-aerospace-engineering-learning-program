#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C06: ensanchamiento termico, microturbulencia y macroturbulencia gaussiana.

Datos: k_B, m_p, u y c (NIST CODATA 2022), consultados 2026-11-09. La linea de Fe I (525 nm, masa 55.845 u como valor estandar NO consultado), T = 5772 K (UAI 2015 B3), la microturbulencia
(1.0 km/s) y la macroturbulencia (3.0 km/s) son ILUSTRATIVAS (sinteticas).
Modelo: ancho Doppler total xi_tot^2 = 2kT/m + xi_micro^2; la macroturbulencia gaussiana se convoluciona con el perfil: sigma^2 = sigma_1^2 + sigma_2^2 (convolucion numerica discreta frente a la suma
en cuadratura); conservacion del ancho equivalente (area) en la convolucion.
Supuestos: perfiles gaussianos. Validez: ilustrativa.
Tolerancia: sigma de la convolucion frente a la cuadratura a 1e-4; area conservada a 1e-6.
"""
from __future__ import annotations
import math, platform, sys
KB, U, C = 1.380649e-23, 1.66053906892e-27, 299792458.0

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m = 55.845 * U
    vt = math.sqrt(2 * KB * 5772 / m)
    xi, ma = 1.0e3, 3.0e3
    vtot = math.sqrt(vt ** 2 + xi ** 2)
    lam = 525e-9
    print(f"velocidad termica del Fe a 5772 K = {vt / 1e3:.4f} km/s ; con microturbulencia de 1 km/s: {vtot / 1e3:.4f} km/s")
    print(f"Delta lambda_D termico = {lam / C * vt * 1e12:.3f} pm ; total = {lam / C * vtot * 1e12:.3f} pm ; con macroturbulencia (cuadratura) = {lam / C * math.sqrt(vtot ** 2 + ma ** 2) * 1e12:.3f} pm")
    # convolucion numerica en unidades de km/s
    s1, s2 = vtot / math.sqrt(2) / 1e3, ma / math.sqrt(2) / 1e3          # sigma de cada gaussiana exp(-v^2/ (2 sigma^2))
    h = 0.02
    xs = [(-12 + i * h) for i in range(int(24 / h) + 1)]
    g1 = [math.exp(-x * x / (2 * s1 * s1)) / (s1 * math.sqrt(2 * math.pi)) for x in xs]
    g2 = [math.exp(-x * x / (2 * s2 * s2)) / (s2 * math.sqrt(2 * math.pi)) for x in xs]
    n = len(xs)
    conv = [sum(g1[j] * g2[i - j + n // 2] for j in range(n) if 0 <= i - j + n // 2 < n) * h for i in range(n)]
    area = sum(conv) * h
    var = sum(x * x * c for x, c in zip(xs, conv)) * h / area
    sig = math.sqrt(var)
    esp = math.sqrt(s1 ** 2 + s2 ** 2)
    print(f"sigma_1 = {s1:.4f} km/s ; sigma_2 = {s2:.4f} km/s ; sigma convolucion = {sig:.5f} ; cuadratura = {esp:.5f} km/s ; area = {area:.6f}")
    assert abs(sig / esp - 1) < 1e-4 and abs(area - 1) < 1e-6
    print(f"fraccion del ensanchamiento debida a cada efecto (en varianza): termico {vt ** 2 / (vtot ** 2 + ma ** 2) * 100:.1f} %, micro {xi ** 2 / (vtot ** 2 + ma ** 2) * 100:.1f} %, macro {ma ** 2 / (vtot ** 2 + ma ** 2) * 100:.1f} %")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
