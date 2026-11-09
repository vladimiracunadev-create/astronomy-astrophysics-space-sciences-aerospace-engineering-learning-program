#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C06: campo geoelectrico inducido en un semiespacio uniforme y corriente en una linea.

Datos: mu_0 (NIST CODATA 2022), consultado 2026-11-09. La conductividad del suelo (1e-3 S/m), las amplitudes y periodos del campo magnetico (50 nT a 100 s, 20 nT a 300 s, 10 nT a 1000 s), la longitud de la linea
(100 km) y las resistencias (5 + 2 x 0.5 ohm) son ILUSTRATIVOS (sinteticos); no se modela ninguna region.
Modelo: onda plana sobre un semiespacio de conductividad sigma: E(omega) = Z B(omega)/mu_0 con Z = sqrt(i omega mu_0/sigma), es decir |E| = sqrt(omega/(mu_0 sigma)) |B| con adelanto de fase de pi/4;
calculo en el dominio de la frecuencia (por componentes) y en el tiempo (transformada discreta directa e inversa de una serie de 1024 muestras); corriente I = E L/(R_linea + 2 R_tierra).
Supuestos: semiespacio uniforme, incidencia vertical, campo uniforme sobre la linea. Validez: orientativa.
Tolerancia: E(t) del dominio de frecuencia frente a la suma analitica por componentes a 1e-6 del maximo.
"""
from __future__ import annotations
import cmath, math, platform, sys
MU0 = 1.25663706127e-6

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    sigma = 1e-3
    comp = ((50e-9, 100.0), (20e-9, 300.0), (10e-9, 1000.0))
    print(f"{'T [s]':>7} {'B [nT]':>8} {'|E| [mV/km]':>12} {'Z/mu0 [m/s]':>13}")
    for b, per in comp:
        w = 2 * math.pi / per
        z = math.sqrt(w / (MU0 * sigma))
        print(f"{per:7.0f} {b * 1e9:8.1f} {z * b * 1e6:12.4f} {z:13.3e}")
    n, dt = 1024, 4.0
    ts = [i * dt for i in range(n)]
    # periodos elegidos como multiplos enteros de la frecuencia fundamental para evitar fuga espectral
    f0 = 1 / (n * dt)
    comp2 = []
    for b, per in comp:
        k = round(1 / (per * f0))
        comp2.append((b, k))
    bt = [sum(b * math.sin(2 * math.pi * k * f0 * t) for b, k in comp2) for t in ts]
    spec = [sum(bt[i] * cmath.exp(-2j * math.pi * k * i / n) for i in range(n)) for k in range(n // 2 + 1)]
    et = [0.0] * n
    for k in range(1, n // 2):
        w = 2 * math.pi * k * f0
        z = cmath.sqrt(1j * w * MU0 / sigma) / MU0
        ek = spec[k] * z
        for i in range(n):
            et[i] += 2 * (ek * cmath.exp(2j * math.pi * k * i / n)).real / n
    ana = [sum(b * math.sqrt(2 * math.pi * k * f0 / (MU0 * sigma)) * math.sin(2 * math.pi * k * f0 * t + math.pi / 4) for b, k in comp2) for t in ts]
    dif = max(abs(a - e) for a, e in zip(ana, et))
    print(f"E(t) maximo = {max(abs(x) for x in ana) * 1e3 * 1e3:.3f} mV/km ; diferencia maxima entre dominio de frecuencia y suma analitica = {dif / max(abs(x) for x in ana):.2e} del maximo")
    assert dif < 1e-6 * max(abs(x) for x in ana)
    emax = max(abs(x) for x in ana) * 1e3      # V/km
    i = emax * 100 / (5 + 2 * 0.5)
    print(f"|E| maximo = {emax:.4f} V/km ; en una linea de 100 km con 6 ohm: I = {i:.3f} A")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
