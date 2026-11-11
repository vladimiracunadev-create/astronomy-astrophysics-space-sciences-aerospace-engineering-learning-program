#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B116-C01: frecuencia cardiaca desde una senal optica (PPG) SINTETICA con artefacto de movimiento.

Todo es sintetico (semilla 116) y NO procede de ninguna persona ni de ningun dispositivo real. La senal PPG se genera como suma de
armonicos de la frecuencia cardiaca verdadera (referencia, como si fuera un ECG), mas un artefacto de movimiento sinusoidal a la
cadencia del ejercicio (2,0 Hz = 120 ciclos/min) y ruido blanco. El estimador toma el pico del espectro (FFT con relleno de ceros)
en la banda de 40 a 200 latidos/min. Unidades: tiempo en s, frecuencia en Hz, frecuencia cardiaca en latidos/min (lpm).
Se calcula: error por nivel de movimiento, resolucion espectral, sesgo y limites de acuerdo (Bland-Altman: sesgo +/- 1,96 DE de las
diferencias) y efecto de la ventana. Verificacion: sin movimiento ni ruido el error es menor que 1 lpm; la resolucion natural
es 60/T lpm; el error crece con el movimiento. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

FS = 25.0  # Hz, frecuencia de muestreo
CADENCIA = 2.0  # Hz, artefacto de movimiento (120 ciclos/min)


def ppg(hr_lpm, t, mov_amp, ruido, rng):
    f = hr_lpm / 60.0
    ph = rng.uniform(0, 2 * np.pi)
    s = np.sin(2 * np.pi * f * t + ph) + 0.35 * np.sin(2 * np.pi * 2 * f * t + 2 * ph)
    s = s + mov_amp * np.sin(2 * np.pi * CADENCIA * t + rng.uniform(0, 2 * np.pi))
    return s + rng.normal(0, ruido, t.size)


def estimar(x, fs=FS, nfft_factor=16, mascara_cadencia=False):
    x = x - x.mean()
    x = x * np.hanning(x.size)
    n = x.size * nfft_factor
    esp = np.abs(np.fft.rfft(x, n))
    fr = np.fft.rfftfreq(n, 1 / fs) * 60.0
    m = (fr >= 40) & (fr <= 200)
    if mascara_cadencia:  # el acelerometro (referencia) informa de la cadencia: se excluye +/- 6 lpm
        m = m & (np.abs(fr - CADENCIA * 60.0) > 6.0)
    return float(fr[m][np.argmax(esp[m])])


def ensayo(mov_amp, ventana_s, rng, n=200, ruido=0.1, mascara=False):
    t = np.arange(0, ventana_s, 1 / FS)
    ref = rng.uniform(55, 95, n)
    est = np.array([estimar(ppg(r, t, mov_amp, ruido, rng), mascara_cadencia=mascara) for r in ref])
    return ref, est


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 116): senal PPG simulada; ninguna cifra procede de una persona ni de un dispositivo real")
    rng = np.random.default_rng(116)
    # control 1: sin movimiento ni ruido
    t = np.arange(0, 30, 1 / FS)
    ctrl = [abs(estimar(ppg(hr, t, 0.0, 0.0, rng)) - hr) for hr in (50, 62.3, 75, 88.8, 101)]
    print(f"Control sin movimiento ni ruido: error maximo = {max(ctrl):.2f} lpm (ventana 30 s)")
    assert max(ctrl) < 1.0
    for T in (8, 15, 30, 60):
        print(f"Resolucion espectral natural 60/T con T = {T:2d} s: {60 / T:5.2f} lpm")
    print("Error segun el nivel de movimiento (ventana 30 s, 200 ensayos, FC verdadera 55-95 lpm):")
    print("  amp. mov/amp. pulso   sesgo [lpm]   DE dif [lpm]   limites de acuerdo [lpm]   |error|>5 lpm   con acelerometro")
    medias = []
    for a in (0.0, 0.3, 0.6, 0.8, 1.0, 1.5):
        ref, est = ensayo(a, 30, rng)
        d = est - ref
        sesgo, de = d.mean(), d.std(ddof=1)
        frac = float(np.mean(np.abs(d) > 5))
        medias.append(frac)
        ref2, est2 = ensayo(a, 30, rng, mascara=True)
        frac2 = float(np.mean(np.abs(est2 - ref2) > 5))
        print(f"        {a:3.1f}            {sesgo:7.2f}       {de:7.2f}        [{sesgo - 1.96 * de:7.1f}, {sesgo + 1.96 * de:6.1f}]          {100 * frac:5.1f} %           {100 * frac2:5.1f} %")
    assert medias[-1] > medias[0]
    assert frac2 < medias[-1]
    print("Efecto de la ventana con movimiento 1.5 (200 ensayos):")
    print("  ventana [s]   |error| medio [lpm]   fraccion con |error| > 5 lpm")
    for T in (8, 15, 30, 60):
        ref, est = ensayo(1.5, T, rng)
        d = np.abs(est - ref)
        print(f"     {T:3d}            {d.mean():6.2f}                {100 * np.mean(d > 5):5.1f} %")
    print("Caso de captura del artefacto: FC verdadera 118 lpm con movimiento a 120 ciclos/min y amplitud 2.5:")
    t = np.arange(0, 30, 1 / FS)
    e = [estimar(ppg(118, t, 2.5, 0.1, rng)) for _ in range(50)]
    print(f"  estimacion media = {np.mean(e):.1f} lpm (el estimador se engancha a la cadencia, no al pulso)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
