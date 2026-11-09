#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C12: Doppler clasico y relativista, velocidad orbital terrestre y correlacion cruzada con ruido.

Datos: c = 299792458 m/s y 1 au = 149597870700 m (exactas; NIST CODATA 2022 y definicion UAI, consultadas el 2026-11-09 solo para c). El ano juliano de 31 557 600 s es una convencion de libro.
El espectro es SINTETICO: 40 lineas de absorcion gaussianas (profundidad 0,1 a 0,4, posiciones aleatorias con semilla 20261109) entre 500 y 510 nm, R = 50 000 y tres pixeles por FWHM; no es un espectro estelar real.
Modelo: z = lambda_obs/lambda_rep - 1; relativista 1 + z = sqrt((1+b)/(1-b)); correlacion cruzada con la plantilla desplazada en pixeles enteros de 2 km/s y maximo por parabola.
Supuestos: ruido gaussiano blanco por pixel, plantilla sin ruido, linea de base normalizada. Validez: sin variaciones del perfil, sin telúricas, sin correccion baricentrica real.
Tolerancia: velocidad sin ruido a 0,15 km/s de la inyectada (el sesgo de la interpolacion parabolica es real y se informa); el cociente de dispersiones entre S/N = 50 y 200 dentro de 30 % de 4.
"""
from __future__ import annotations
import math, platform, random, sys

C = 299792458.0
AU = 149597870700.0
YR = 31557600.0
SEMILLA = 20261109
R = 50000.0
DLN = 1 / (3 * R)                       # paso en ln(lambda): 3 pixeles por FWHM
V_PIX = C * DLN / 1000.0                # km/s por pixel
LAM_A, LAM_B = 500.0, 510.0


def espectro_modelo(rnd):
    sig = 1 / R / math.sqrt(8 * math.log(2))      # sigma en ln(lambda)
    lineas = [(rnd.uniform(math.log(LAM_A) + 0.0005, math.log(LAM_B) - 0.0005), rnd.uniform(0.1, 0.4)) for _ in range(40)]
    n = int((math.log(LAM_B) - math.log(LAM_A)) / DLN)
    return sig, lineas, n


def flujo(sig, lineas, n, desp_ln=0.0):
    out = []
    for i in range(n):
        x = math.log(LAM_A) + i * DLN - desp_ln
        v = 1.0
        for c, d in lineas:
            if abs(x - c) < 6 * sig:
                v -= d * math.exp(-0.5 * ((x - c) / sig) ** 2)
        out.append(v)
    return out


def ccf(obs, plant, k):
    n = len(obs)
    a = max(0, k)
    b = min(n, n + k)
    s = sum((obs[i] - 1) * (plant[i - k] - 1) for i in range(a, b))
    return s


def velocidad(obs, plant, kmax=20):
    ks = list(range(-kmax, kmax + 1))
    vals = [ccf(obs, plant, k) for k in ks]
    j = max(range(len(vals)), key=lambda i: vals[i])
    if 0 < j < len(vals) - 1:
        y0, y1, y2 = vals[j - 1], vals[j], vals[j + 1]
        d = 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2)
    else:
        d = 0.0
    return (ks[j] + d) * V_PIX


def calcular():
    r = {}
    r["v_orb"] = 2 * math.pi * AU / YR / 1000.0
    r["filas"] = []
    for v in (30e3, 3e6, 3e7, 0.1 * C, 0.5 * C):
        b = v / C
        z_cl = b
        z_rel = math.sqrt((1 + b) / (1 - b)) - 1
        r["filas"].append((v / 1000, z_cl, z_rel, (z_rel - z_cl) / z_rel))
    r["z_inv"] = ((1 + 0.1) ** 2 - 1) / ((1 + 0.1) ** 2 + 1)         # beta para z = 0,1
    rnd = random.Random(SEMILLA)
    sig, lineas, n = espectro_modelo(rnd)
    plant = flujo(sig, lineas, n)
    v_true = 7.3                                                       # km/s, ILUSTRATIVO
    desp = v_true * 1000 / C                                           # ~ ln(1+z) pequeno
    obs0 = flujo(sig, lineas, n, desp)
    r["v_sin_ruido"] = velocidad(obs0, plant)
    r["n_pix"] = n
    r["v_pix"] = V_PIX
    for snr in (50, 200):
        est = []
        for _ in range(60):
            obs = [o + rnd.gauss(0, 1 / snr) for o in obs0]
            est.append(velocidad(obs, plant))
        m = sum(est) / len(est)
        sd = math.sqrt(sum((a - m) ** 2 for a in est) / (len(est) - 1))
        r[f"m_{snr}"], r[f"sd_{snr}"] = m, sd
    r["razon_sd"] = r["sd_50"] / r["sd_200"]
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"velocidad orbital de la Tierra (orbita circular, 1 au, 1 ano juliano) = {r['v_orb']:.3f} km/s")
    print(f"{'v (km/s)':>12} {'z clasico':>12} {'z relativista':>14} {'diferencia rel.':>16}")
    for v, a, b, d in r["filas"]:
        print(f"{v:12.1f} {a:12.6f} {b:14.6f} {d:16.4f}")
    print(f"velocidad/c para z = 0,1: {r['z_inv']:.6f}")
    print(f"{r['n_pix']} pixeles, {r['v_pix']:.3f} km/s por pixel ; v inyectada 7.3 km/s ; sin ruido: {r['v_sin_ruido']:.3f} km/s")
    for snr in (50, 200):
        print(f"S/N = {snr}: media {r[f'm_{snr}']:.3f} km/s ; dispersion {r[f'sd_{snr}']:.3f} km/s ; error estandar de la media {r[f'sd_{snr}']/math.sqrt(60):.3f}")
    print(f"cociente de dispersiones S/N 50 frente a 200 = {r['razon_sd']:.2f} (esperado 4)")
    assert abs(r["v_orb"] - 29.785) < 0.01
    assert abs(r["z_inv"] - 0.21 / 2.21) < 1e-12
    assert abs(r["v_sin_ruido"] - 7.3) < 0.15
    assert abs(r["m_50"] - 7.3) < 3 * r["sd_50"] / math.sqrt(60) + 0.15
    assert abs(r["razon_sd"] / 4 - 1) < 0.30
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
