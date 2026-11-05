#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C12: vectores, componentes y velocidad orbital terrestre.

Datos (PUBLICADOS; estimados): NASA NSSDC Planetary Fact Sheet (2025-03-18; consulta
2026-11-05): distancia al Sol de la Tierra 149,6 millones de km y periodo 365,2 d;
c = 299 792 458 m/s exacta (BIPM SI, 9.ª ed.). Sondas y ángulos de ejemplo: SINTÉTICOS.
Modelo: órbita circular uniforme en el plano xy con el Sol en el origen:
posición r = a (cos θ, sen θ), velocidad v = (2πa/P)(-sen θ, cos θ).
Supuestos: circular, plana; la excentricidad real (0,017) cambia v en ~1,7 %.
Validez: primera aproximación. Tolerancia: 1e-12 (identidades), 1 % frente al
orden de magnitud de referencia de 29,8 km/s (calculado aquí con a y P publicados).
"""
from __future__ import annotations
import math, platform, sys

A_KM = 149.6e6
P_S = 365.2 * 86400.0
C_KMS = 299_792.458


def suma(u, v):
    return tuple(a + b for a, b in zip(u, v))


def esc(k, u):
    return tuple(k * a for a in u)


def mod(u):
    return math.sqrt(sum(a * a for a in u))


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def pruebas():
    u, v = (3.0, 4.0), (-1.0, 2.0)
    assert mod(u) == 5.0
    assert suma(u, v) == suma(v, u) == (2.0, 6.0)
    assert esc(2.0, u) == (6.0, 8.0)
    # descomposición radial/tangencial: w = vr r̂ + vt t̂
    th = 0.7
    r_hat, t_hat = (math.cos(th), math.sin(th)), (-math.sin(th), math.cos(th))
    w = (1.3, -2.1)
    vr, vt = dot(w, r_hat), dot(w, t_hat)
    rec = suma(esc(vr, r_hat), esc(vt, t_hat))
    assert abs(rec[0] - w[0]) < 1e-12 and abs(rec[1] - w[1]) < 1e-12
    assert abs(mod(w) ** 2 - (vr ** 2 + vt ** 2)) < 1e-12
    v0 = 2 * math.pi * A_KM / P_S
    assert abs(v0 - 29.8) / 29.8 < 1e-2


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (módulo, suma conmutativa, producto por escalar, descomposición radial/tangencial)")
    v0 = 2 * math.pi * A_KM / P_S
    print(f"\nRapidez orbital media (calculada) v = 2πa/P = {v0:.3f} km/s")
    print(f"{'θ (°)':>6}{'x (10^6 km)':>13}{'y (10^6 km)':>13}{'vx (km/s)':>11}{'vy (km/s)':>11}{'|v|':>9}")
    for deg in (0, 90, 180, 270):
        th = math.radians(deg)
        x, y = A_KM / 1e6 * math.cos(th), A_KM / 1e6 * math.sin(th)
        vx, vy = -v0 * math.sin(th), v0 * math.cos(th)
        print(f"{deg:6d}{x:13.2f}{y:13.2f}{vx:11.3f}{vy:11.3f}{mod((vx, vy)):9.3f}")
    th = 0.0
    v_t = (-v0 * math.sin(th), v0 * math.cos(th))
    v_s = suma(v_t, (0.0, 3.0))
    print(f"\nSonda sintética: v_Tierra = ({v_t[0]:.3f}, {v_t[1]:.3f}) km/s; v_rel = (0, 3) km/s; "
          f"v_heliocéntrica = ({v_s[0]:.3f}, {v_s[1]:.3f}), módulo {mod(v_s):.3f} km/s")
    v_s2 = suma(v_t, (0.0, -3.0))
    print(f"En sentido opuesto (v_rel = (0, -3)): módulo {mod(v_s2):.3f} km/s")
    v_s3 = suma(v_t, (3.0, 0.0))
    print(f"Con v_rel = (3, 0) km/s (radial): v = ({v_s3[0]:.3f}, {v_s3[1]:.3f}), módulo {mod(v_s3):.3f} km/s")
    ab = v0 / C_KMS
    print(f"\nv/c = {ab:.4e} rad = {ab * 206264.806:.2f}″ (orden de magnitud del desplazamiento aparente de una estrella)")
    r_hat, t_hat = (1.0, 0.0), (0.0, 1.0)
    print(f"Componentes de v_s3 en θ=0: radial = {dot(v_s3, r_hat):.3f}, tangencial = {dot(v_s3, t_hat):.3f} km/s")


if __name__ == "__main__":
    main()
