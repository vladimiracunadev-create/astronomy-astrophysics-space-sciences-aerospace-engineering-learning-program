#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C11: oscilador armónico, resonancia y péndulo.

Datos: SINTÉTICOS (masa 50 kg y rigidez 2,0e5 N/m de un mástil de enseñanza; no corresponden
a ninguna nave real); g_n = 9,806 65 m/s² (NIST CODATA 2022). Modelo: masa-resorte lineal,
x'' = -(k/m) x, integrado con velocity-Verlet, frente a la solución analítica
x = A cos(w t); péndulo simple con período exacto por la media aritmético-geométrica (AGM).
Supuestos: sin amortiguamiento (salvo la parte indicada), pequeñas deformaciones.
Dominio de validez: resorte lineal. Tolerancias: 1e-6 en amplitud tras 10 períodos; 1e-5 en deriva de energía; 1e-6
entre el período por AGM y la serie en ángulo pequeño con 1e-3 rad.
"""
from __future__ import annotations
import math
import sys

GN = 9.80665

def resorte(m: float, k: float, a0: float, n_periodos: int = 10, pasos: int = 2000):
    w = math.sqrt(k / m)
    T = 2 * math.pi / w
    dt = T / pasos
    x, v = a0, 0.0
    a = -w * w * x
    emax = 0.0
    e0 = 0.5 * m * v * v + 0.5 * k * x * x
    for _ in range(n_periodos * pasos):
        v += 0.5 * a * dt
        x += v * dt
        a = -w * w * x
        v += 0.5 * a * dt
        emax = max(emax, abs(0.5 * m * v * v + 0.5 * k * x * x - e0) / e0)
    return x, v, w, T, emax

def periodo_pendulo(longitud: float, theta0_rad: float) -> float:
    """Período exacto T = 4 K(sin(theta0/2)) sqrt(L/g) usando la AGM."""
    k = math.sin(theta0_rad / 2)
    a, b = 1.0, math.sqrt(1 - k * k)
    for _ in range(40):
        a, b = 0.5 * (a + b), math.sqrt(a * b)
    K = math.pi / (2 * a)
    return 4 * K * math.sqrt(longitud / GN)

def amplitud_forzada(w: float, w0: float, zeta: float) -> float:
    """Factor de amplificación dinámico de un oscilador amortiguado forzado."""
    r = w / w0
    return 1.0 / math.sqrt((1 - r * r) ** 2 + (2 * zeta * r) ** 2)

def main() -> int:
    m, k, a0 = 50.0, 2.0e5, 0.01
    x, v, w, T, emax = resorte(m, k, a0)
    assert abs(x - a0 * math.cos(w * 10 * T)) < 1e-6 * a0 + 1e-9, x
    assert emax < 1e-5, emax
    t0 = 2 * math.pi * math.sqrt(1.0 / GN)
    assert abs(periodo_pendulo(1.0, 1e-3) - t0) / t0 < 1e-6
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Mástil sintético: w = {w:.3f} rad/s, f = {w/(2*math.pi):.3f} Hz, T = {T*1e3:.2f} ms; tras 10 períodos x = {x*1e3:.4f} mm; deriva de energía máx = {emax:.1e}")
    print(f"Péndulo de 1,00 m: T(ángulo pequeño) = {t0:.4f} s")
    for deg in (5, 30, 60, 90):
        t = periodo_pendulo(1.0, math.radians(deg))
        print(f"  theta0 = {deg:2d}°: T = {t:.4f} s (T/T0 = {t/t0:.4f})")
    for zeta in (0.01, 0.05, 0.2):
        print(f"Factor de amplificación en resonancia (zeta = {zeta}): {amplitud_forzada(w, w, zeta):.1f}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
