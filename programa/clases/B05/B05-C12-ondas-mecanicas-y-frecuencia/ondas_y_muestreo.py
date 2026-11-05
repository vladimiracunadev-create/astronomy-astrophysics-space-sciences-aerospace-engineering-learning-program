#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C12: frecuencia, longitud de onda, muestreo y aliasing.

Datos: SINTÉTICOS (señales generadas). Velocidad del sonido en aire: a = sqrt(gamma R T) con
gamma = 1,4 (supuesto de gas diatómico ideal; no consultado, ver clase), R = 8,314 462 618 J/(mol K)
(NIST CODATA 2022), masa molar 0,028 965 kg/mol (SUPUESTO sin fuente consultada). Modelo: onda
senoidal v = f * lambda; transformada discreta de Fourier (DFT) para estimar la frecuencia.
Supuestos: señal estacionaria, ruido nulo. Dominio de validez: f < fs/2 (Nyquist).
Tolerancias: 0,5 Hz en la frecuencia estimada; el aliasing debe aparecer exactamente en |f - fs|.
"""
from __future__ import annotations
import cmath
import math
import sys

R_GAS = 8.314462618
GAMMA = 1.4
M_AIRE = 0.028965

def v_sonido(T_k: float) -> float:
    return math.sqrt(GAMMA * R_GAS * T_k / M_AIRE)

def dft_pico(x: list[float], fs: float) -> float:
    n = len(x)
    mejor, kmax = 0.0, 0
    for k in range(1, n // 2 + 1):
        s = sum(x[j] * cmath.exp(-2j * math.pi * k * j / n) for j in range(n))
        if abs(s) > mejor:
            mejor, kmax = abs(s), k
    return kmax * fs / n

def senal(f: float, fs: float, n: int) -> list[float]:
    return [math.sin(2 * math.pi * f * j / fs) for j in range(n)]

def main() -> int:
    fs, n = 1000.0, 1000
    f_est = dft_pico(senal(50.0, fs, n), fs)
    assert abs(f_est - 50.0) < 0.5, f_est
    fs_bajo, n_bajo = 100.0, 100
    f_alias = dft_pico(senal(130.0, fs_bajo, n_bajo), fs_bajo)
    assert abs(f_alias - 30.0) < 0.5, f_alias       # |130 - 100| = 30 Hz
    assert abs(v_sonido(288.15) - 340.0) < 5.0      # NASA Glenn: ~761 mph = 340 m/s a nivel del mar, día estándar (15 °C)
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Señal de 50 Hz muestreada a {fs:.0f} Hz: frecuencia estimada = {f_est:.2f} Hz")
    print(f"Señal de 130 Hz muestreada a {fs_bajo:.0f} Hz (Nyquist = {fs_bajo/2:.0f} Hz): aparece en {f_alias:.2f} Hz")
    for T in (233.15, 273.15, 288.15, 293.15):
        print(f"  Velocidad del sonido en aire a {T-273.15:6.1f} °C: {v_sonido(T):.1f} m/s")
    v = v_sonido(293.15)
    for f in (20.0, 440.0, 20_000.0):
        print(f"  f = {f:8.1f} Hz -> longitud de onda = {v/f:.4f} m")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
