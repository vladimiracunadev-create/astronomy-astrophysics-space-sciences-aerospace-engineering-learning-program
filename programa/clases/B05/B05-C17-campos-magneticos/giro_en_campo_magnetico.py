#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C17: partículas cargadas en un campo magnético uniforme y campo de un hilo.

Datos PUBLICADOS (CODATA 2022 / SI 9.ª ed.): e = 1,602 176 634e-19 C (exacta); m_p = 1,672 621 925 95e-27 kg;
m_e = 9,109 383 7139e-31 kg; mu_0 = 1,256 637 061 27e-6 N/A². Intensidad del campo de prueba (50 uT,
dentro del intervalo 20-60 uT que NOAA da para el campo principal en superficie), velocidades y corrientes:
SINTÉTICAS. Modelo: movimiento no relativista en B uniforme con el algoritmo de Boris (rotación exacta
del vector velocidad). Supuestos: sin campo eléctrico, sin radiación. Dominio de validez: v << c.
Tolerancias: radio y período del giro a 1e-3 frente a las fórmulas; rapidez conservada a 1e-12.
"""
from __future__ import annotations
import math
import sys

E = 1.602176634e-19
M_P = 1.67262192595e-27
M_E = 9.1093837139e-31
MU0 = 1.25663706127e-6

def girar(q: float, m: float, v0: float, B: float, pasos_por_periodo: int = 200, periodos: int = 10):
    """Boris con B a lo largo de z y velocidad inicial en x; devuelve (radio medido, período, rapidez final, regreso)."""
    T = 2 * math.pi * m / (abs(q) * B)
    dt = T / pasos_por_periodo
    x, y, vx, vy = 0.0, 0.0, v0, 0.0
    t = (q / m) * B * dt / 2
    s = 2 * t / (1 + t * t)
    xs, ys = [], []
    for _ in range(pasos_por_periodo * periodos):
        vpx, vpy = vx + vy * t, vy - vx * t
        vx, vy = vx + vpy * s, vy - vpx * s
        x += vx * dt
        y += vy * dt
        xs.append(x); ys.append(y)
    # centro estimado: media de las posiciones sobre un número entero de períodos
    cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
    radio = sum(math.hypot(a - cx, b - cy) for a, b in zip(xs, ys)) / len(xs)
    regreso = math.hypot(x, y)
    return radio, T, math.hypot(vx, vy), regreso

def campo_hilo(I: float, r: float) -> float:
    return MU0 * I / (2 * math.pi * r)

def main() -> int:
    B, v = 50e-6, 1.0e6
    r_teo = M_P * v / (E * B)
    radio, T, vf, reg = girar(E, M_P, v, B)
    assert abs(radio - r_teo) / r_teo < 1e-3, (radio, r_teo)
    assert abs(T - 2 * math.pi * r_teo / v) / T < 1e-12
    assert abs(vf - v) / v < 1e-12
    assert reg < 1e-2 * r_teo, reg
    # signo de la carga: un electrón gira en sentido contrario (se comprueba el signo del momento angular)
    rad_e, T_e, _, _ = girar(-E, M_E, 1.0e7, B)
    assert abs(rad_e - M_E * 1.0e7 / (E * B)) / (M_E * 1.0e7 / (E * B)) < 1e-3
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Protón (v = {v:.1e} m/s, B = {B*1e6:.0f} uT): radio teórico = {r_teo:.2f} m, medido = {radio:.2f} m; período = {T*1e3:.3f} ms; f = {1/T:.1f} Hz")
    print(f"Electrón (v = 1,0e7 m/s): radio = {M_E*1.0e7/(E*B):.4f} m; frecuencia de giro = {E*B/(2*math.pi*M_E):.4e} Hz")
    print(f"Cociente de radios protón/electrón a igual rapidez: {M_P/M_E:.1f}")
    for I, r in ((10.0, 0.10), (1.0, 1.0), (100.0, 1.0)):
        print(f"Hilo con {I:5.1f} A a {r:4.2f} m: B = {campo_hilo(I, r)*1e6:.3f} uT")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
