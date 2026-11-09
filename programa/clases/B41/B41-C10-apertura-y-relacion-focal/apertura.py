#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C10: relacion focal, captacion de luz, brillo superficial y tiempo de exposicion.

Datos: sin constantes fisicas. Aperturas de 80 a 400 mm, focales y la pupila del ojo de 7 mm son ILUSTRATIVAS.
Modelo: N = F/D. Flujo de una fuente puntual proporcional a D^2; irradiancia de la imagen de un objeto extenso proporcional a 1/N^2. Segunda via: la
irradiancia se calcula integrando numericamente el angulo solido del cono de luz (regla del trapecio de sen t cos t dt) y se compara con sen^2(theta) y con 1/(4N^2).
Ganancia en magnitudes de una fuente puntual: 5 log10(D2/D1), igual a 2,5 log10 del cociente de areas.
Supuestos: objeto en el infinito, transmision unitaria. Validez: geometrica; el cociente ideal es 1/(4N^2) solo para N grandes.
Tolerancia: integral frente a sen^2 1e-9; cociente de exposiciones frente a (N2/N1)^2 1e-12.
"""
from __future__ import annotations
import math, platform, sys


def irradiancia_rel(N, pasos=20000):
    """Integral de sen t cos t dt de 0 a theta, con tan(theta) = D/(2F) = 1/(2N): da sen^2(theta)/2."""
    th = math.atan(1 / (2 * N))
    h = th / pasos
    acc = 0.0
    for i in range(pasos):
        a, b = i * h, (i + 1) * h
        acc += 0.5 * h * (math.sin(a) * math.cos(a) + math.sin(b) * math.cos(b))
    return 2 * acc, th


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'D [mm]':>7} {'F [mm]':>7} {'N':>6} {'area rel.':>10} {'2,5 log10 area':>15} {'brillo sup. rel.':>17}")
    base = (80.0, 400.0)
    for D, F in ((80.0, 400.0), (150.0, 750.0), (200.0, 1000.0), (200.0, 2000.0), (400.0, 1600.0)):
        N = F / D
        area = (D / base[0]) ** 2
        mag = 2.5 * math.log10(area)
        brillo = (base[1] / base[0] / N) ** 2
        print(f"{D:7.0f} {F:7.0f} {N:6.1f} {area:10.3f} {mag:15.3f} {brillo:17.3f}")
    # irradiancia: integral frente a formulas
    print(f"{'N':>5} {'theta [deg]':>12} {'integral':>10} {'sen^2':>10} {'1/(4N^2)':>10} {'error rel. 1/(4N^2)':>20}")
    for N in (1.0, 2.0, 5.0, 10.0, 30.0):
        I, th = irradiancia_rel(N)
        s2 = math.sin(th) ** 2
        p = 1 / (4 * N * N)
        print(f"{N:5.1f} {math.degrees(th):12.4f} {I:10.6f} {s2:10.6f} {p:10.6f} {abs(I-p)/p:20.3e}")
        assert abs(I - s2) < 1e-9
    assert abs(irradiancia_rel(30.0)[0] - 1 / (4 * 900)) / (1 / (4 * 900)) < 1e-3
    # exposicion: mismo objeto extenso, dos relaciones focales
    t1, N1, N2 = 1 / 60, 5.0, 10.0
    t2 = t1 * (N2 / N1) ** 2
    print(f"misma imagen de brillo: f/{N1:.0f} con 1/60 s equivale a f/{N2:.0f} con {t2:.4f} s (= 4 veces)")
    assert abs(t2 / t1 - 4.0) < 1e-12
    # fuente puntual: tiempo ~ 1/D^2 (sin fondo)
    print("fuente puntual: duplicar la apertura reduce el tiempo 4 veces y gana", round(5 * math.log10(2), 3), "magnitudes limite")
    # magnitud limite visual orientativa con la pupila del ojo (7 mm) -> telescopio de D
    for D in (80.0, 200.0, 400.0):
        gan = 5 * math.log10(D / 7.0)
        print(f"  telescopio de {D:.0f} mm frente a un ojo de 7 mm: ganancia = {gan:.2f} magnitudes (solo captacion, ideal)")
    assert abs(5 * math.log10(2) - 1.505) < 1e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
