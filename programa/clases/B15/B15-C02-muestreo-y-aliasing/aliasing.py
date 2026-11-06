#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C02: muestreo, frecuencia de Nyquist y aliasing.

Datos: SINTÉTICOS. Cadencias nominales de TESS (MAST): 2 min para objetivos y
unos 30 min para imágenes completas (valor del texto de MAST).
Modelo: una senoide de frecuencia f muestreada cada dt aparece en la
frecuencia f_alias = |f - m*fs| con m entero que la deja en [0, fs/2].
Supuestos: señal estacionaria, sin filtro antialias previo.
Validez: señal de banda única. Tolerancia: 1 bin de la FFT (1/(N dt)).
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def alias(f, fs):
    r = f % fs
    return min(r, fs - r)


def pico(x, dt):
    X = np.abs(np.fft.rfft(x - x.mean()))
    f = np.fft.rfftfreq(x.size, dt)
    return f[np.argmax(X)], f[1]


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
casos = [("2 min", 120.0, 400.0), ("2 min", 120.0, 200.0), ("30 min", 1800.0, 30.0), ("30 min", 1800.0, 10.0)]
for nom, dt, f_cd in casos:               # f en ciclos/día
    fs = 86400.0 / dt                     # ciclos/día
    N = 4096
    t = np.arange(N) * dt / 86400.0       # d
    x = np.sin(2 * np.pi * f_cd * t + 0.3)
    fp, bin_ = pico(x, dt / 86400.0)
    fa = alias(f_cd, fs)
    print(f"cadencia {nom}: fs = {fs:.0f} c/d, Nyquist = {fs/2:.0f} c/d; verdadera {f_cd:.0f} c/d -> "
          f"pico en {fp:.2f} c/d; predicción {fa:.0f} c/d")
    prueba(abs(fp - fa) <= bin_, f"alias en {nom}, f={f_cd}")
# Muestreo en cuasi-resonancia: 1 muestra por día de una señal de 1,02 d
fs = 1.0
fa = alias(1 / 1.02, fs)
print(f"muestreo diario de periodo 1,02 d: alias con periodo {1/fa:.1f} d")
prueba(abs(1 / fa - 51.0) < 0.5, "periodo aparente 51 d")
print("Pruebas superadas.")
