#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C10: estabilidad de apuntamiento, densidad espectral de potencia, RMS de jitter y degradacion de la imagen.

Datos: ninguna constante fisica de una fuente. TODO es ILUSTRATIVO (no es la estabilidad de ninguna mision): ruido de actitud con RMS 0,010 arcsec y frecuencia de corte 0,5 Hz,
tono de una rueda de reaccion de 0,004 arcsec de amplitud a 40 Hz, telescopio de 0,5 m a 550 nm (FWHM de difraccion 0,2332 arcsec), muestreo 20 Hz.
Modelo: (1) PSD unilateral de un proceso de Ornstein-Uhlenbeck S(f) = 4 sigma^2 tau/(1 + (2 pi f tau)^2) con tau = 1/(2 pi fc), cuya integral es sigma^2; integral numerica frente a la
integral analitica truncada S0 fc atan(F/fc); (2) serie temporal simulada (semilla 20261109) con x[n+1] = a x[n] + sigma sqrt(1 - a^2) w, a = exp(-2 pi fc dt): varianza y
autocorrelacion en retardo 1 frente a sigma^2 y a; (3) RMS total con el tono, sqrt(sigma^2 + A^2/2); (4) ensanchamiento gaussiano de la imagen y sigma maximo para perder 10 % de pico.
Supuestos: jitter gaussiano e independiente en cada eje, PSF de difraccion aproximada por una gaussiana de igual FWHM. Validez: ilustrativa.
Tolerancia: integral numerica frente a analitica, 1e-6 relativo; varianza simulada, 3 %; autocorrelacion, 0,01 absoluto.
"""
from __future__ import annotations
import math, platform, random

SIG, FC = 0.010, 0.5
A_RW, F_RW = 0.004, 40.0
FWHM_D = 0.2332
FWHM_K = 2 * math.sqrt(2 * math.log(2))
DT = 0.05


def psd(f):
    tau = 1 / (2 * math.pi * FC)
    return 4 * SIG ** 2 * tau / (1 + (2 * math.pi * f * tau) ** 2)


def integral_psd(fmax, n=400000):
    h = fmax / n
    s = 0.0
    for i in range(n + 1):
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * psd(i * h)
    return s * h / 3


def calc():
    r = {}
    s0 = psd(0.0)
    r["S0"] = s0
    r["int"] = {}
    for fmax in (2.0, 10.0, 100.0):
        r["int"][fmax] = (integral_psd(fmax), s0 * FC * math.atan(fmax / FC))
    r["sigma2"] = SIG ** 2
    a = math.exp(-2 * math.pi * FC * DT)
    rng = random.Random(20261109)
    n = 200000
    x = rng.gauss(0, SIG)
    xs = []
    b = SIG * math.sqrt(1 - a * a)
    for _ in range(n):
        x = a * x + b * rng.gauss(0, 1)
        xs.append(x)
    m = sum(xs) / n
    var = sum((v - m) ** 2 for v in xs) / (n - 1)
    ac1 = sum((xs[i] - m) * (xs[i + 1] - m) for i in range(n - 1)) / ((n - 1) * var)
    r["a"], r["var_mc"], r["ac1"] = a, var, ac1
    r["rms_total"] = math.sqrt(SIG ** 2 + A_RW ** 2 / 2)
    r["pico"] = {}
    for s in (0.005, 0.010, 0.020, 0.033, 0.050):
        tot = math.sqrt(FWHM_D ** 2 + (FWHM_K * s) ** 2)
        r["pico"][s] = (tot, (FWHM_D / tot) ** 2)
    r["sig_max"] = FWHM_D * math.sqrt(1 / 0.9 - 1) / FWHM_K
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"S0 = {r['S0']:.6e} arcsec^2/Hz ; sigma^2 = {r['sigma2']:.6e} arcsec^2")
    for f, (a, b) in r["int"].items():
        print(f"integral de la PSD hasta {f:6.1f} Hz: numerica = {a:.8e} ; analitica = {b:.8e}")
        assert abs(a - b) / b < 1e-6
    print(f"a = {r['a']:.6f} ; varianza simulada = {r['var_mc']:.6e} (esperada {r['sigma2']:.6e}) ; autocorrelacion lag 1 = {r['ac1']:.4f}")
    print(f"RMS total con el tono de la rueda = {r['rms_total']:.5f} arcsec")
    print(f"{'sigma [arcsec]':>15} {'FWHM total':>12} {'pico relativo':>14}")
    for s, (t, p) in r["pico"].items():
        print(f"{s:15.4f} {t:12.4f} {p:14.4f}")
    print(f"sigma maximo para perder 10 % de pico = {r['sig_max']:.5f} arcsec")
    assert abs(r["var_mc"] - r["sigma2"]) / r["sigma2"] < 0.03
    assert abs(r["ac1"] - r["a"]) < 0.01
    assert abs(r["pico"][0.033][1] - 0.9) < 0.002
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
