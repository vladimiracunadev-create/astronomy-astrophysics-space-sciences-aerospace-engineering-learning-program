#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C07: radar de apertura sintetica (SAR): compresion de pulso y resoluciones.

Datos: banda C a 5.405 GHz, altitud 693 km y modo IW de resolucion 5 m x 20 m (SentiWiki Sentinel-1, consultada 2026-11-09).
ILUSTRATIVOS: ancho de banda del chirp 100 MHz, duracion 10 us, antena de 12 m, incidencia 35 grados. El eco es SINTETICO (un blanco puntual).
Modelo: chirp lineal s(t) = exp(j pi K t^2), K = B/tau; filtro adaptado por FFT; ancho a -3 dB de la salida frente a 0.886/B; resolucion en
distancia = c/(2B); resolucion en acimut de un SAR de franja = L/2; apertura sintetica L_s = lambda R / L; Tierra plana para R = H/cos(incidencia).
Validez: blanco puntual, sin ruido, sin migracion de rango. Tolerancia: ancho -3 dB medido frente a 0.886/B < 3 %.
Requiere numpy.
"""
import math, platform
import numpy as np

C = 299792458.0
F0 = 5.405e9
B, TAU, FS = 100e6, 10e-6, 400e6
LANT, H, INC = 12.0, 693e3, math.radians(35.0)


def comprimir():
    n = int(round(TAU * FS))
    t = (np.arange(n) - n / 2) / FS
    K = B / TAU
    chirp = np.exp(1j * math.pi * K * t**2)
    N = 1 << 16
    eco = np.zeros(N, complex)
    eco[1000:1000 + n] = chirp  # blanco puntual
    ref = np.zeros(N, complex)
    ref[:n] = chirp
    out = np.fft.ifft(np.fft.fft(eco) * np.conj(np.fft.fft(ref)))
    mag = np.abs(out)
    ipk = int(np.argmax(mag))
    return mag / mag[ipk], ipk


def ancho_3db(mag, ipk, fs):
    umbral = 10 ** (-3 / 20)
    i = ipk
    while mag[i] > umbral:
        i -= 1
    a = i + (umbral - mag[i]) / (mag[i + 1] - mag[i])
    j = ipk
    while mag[j] > umbral:
        j += 1
    b = j - 1 + (mag[j - 1] - umbral) / (mag[j - 1] - mag[j])
    return (b - a) / fs


def calcular():
    r = {}
    mag, ipk = comprimir()
    w = ancho_3db(mag, ipk, FS)
    r["ancho_t_ns"] = w * 1e9
    r["ancho_teo_ns"] = 0.886 / B * 1e9
    r["razon"] = w / (0.886 / B)
    r["lambda_cm"] = C / F0 * 100
    r["res_rango"] = C / (2 * B)
    r["res_rango_3db"] = w * C / 2
    r["tbp"] = B * TAU
    r["res_ground"] = r["res_rango"] / math.sin(INC)
    r["res_acimut"] = LANT / 2
    R = H / math.cos(INC)
    r["R_km"] = R / 1e3
    r["L_sint_km"] = C / F0 * R / LANT / 1e3
    # lobulo lateral mayor
    m = np.concatenate([mag[ipk - 20:ipk - 4], mag[ipk + 5:ipk + 21]])  # fuera del lobulo principal (nulo a 1/B = 4 muestras)
    r["lobulo_db"] = 20 * math.log10(m.max())
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Longitud de onda = {r['lambda_cm']:.3f} cm ; producto tiempo-ancho de banda = {r['tbp']:.0f}")
    print(f"Ancho a -3 dB de la salida comprimida = {r['ancho_t_ns']:.3f} ns ; teorico 0.886/B = {r['ancho_teo_ns']:.3f} ns ; razon = {r['razon']:.3f}")
    print(f"Resolucion en distancia c/(2B) = {r['res_rango']:.2f} m ; a -3 dB = {r['res_rango_3db']:.2f} m ; sobre el suelo (incidencia 35 grados) = {r['res_ground']:.2f} m")
    print(f"Resolucion en acimut L/2 = {r['res_acimut']:.1f} m ; distancia oblicua = {r['R_km']:.1f} km ; apertura sintetica = {r['L_sint_km']:.2f} km")
    print(f"Mayor lobulo lateral cercano (entre 5 y 20 muestras del pico) = {r['lobulo_db']:.1f} dB")
    assert abs(r["razon"] - 1) < 0.03
    assert r["tbp"] > 100
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
