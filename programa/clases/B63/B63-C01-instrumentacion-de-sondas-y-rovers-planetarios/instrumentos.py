#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B63-C01: escala de pixel, ruido de fotones y localizacion sismica con una estacion.

Datos: SINTETICOS e ILUSTRATIVOS. La camara (f = 34 mm, paso de pixel 7.4 um), el numero de fotoelectrones y las
velocidades sismicas (vp = 5.0 km/s, vs = 2.9 km/s) son valores propuestos para el ejemplo; no son medidos y no
corresponden a ningun instrumento ni cuerpo real.
Modelo: (1) tamano de pixel en el suelo GSD = p * d / f (optica de orificio, objeto lejano); (2) SNR de fotones
= N / sqrt(N + sigma_lectura^2), contrastada con una simulacion Monte Carlo (semilla fija); (3) distancia al
epicentro con una estacion, d = dt_SP * vp * vs / (vp - vs).
Sistema de referencia: distancias a lo largo de la visual (m) y sobre el terreno (km). Medio homogeneo.
Validez: ilustrativa; ignora distorsion, inclinacion de la visual, ruido de fondo y medios estratificados.
Tolerancias: GSD < 1e-12 relativo; SNR Monte Carlo dentro del 1 % del analitico; distancia sismica < 1e-9 km.
Versiones: se imprimen al ejecutar (solo biblioteca estandar).
"""
from __future__ import annotations
import math, platform, random

F_MM, PITCH_UM = 34.0, 7.4          # ilustrativos
VP, VS = 5.0, 2.9                   # km/s, ilustrativos


def gsd_m(rango_m: float, f_mm: float = F_MM, p_um: float = PITCH_UM) -> float:
    return (p_um * 1e-6) * rango_m / (f_mm * 1e-3)


def snr_analitico(n_e: float, lectura_e: float) -> float:
    return n_e / math.sqrt(n_e + lectura_e ** 2)


def poisson(rng: random.Random, lam: float) -> int:
    # Para lam grande: aproximacion normal con redondeo (suficiente para el contraste de la tolerancia).
    return max(0, int(round(rng.gauss(lam, math.sqrt(lam)))))


def snr_montecarlo(n_e: float, lectura_e: float, n: int = 200000, semilla: int = 63) -> float:
    rng = random.Random(semilla)
    xs = [poisson(rng, n_e) + rng.gauss(0.0, lectura_e) for _ in range(n)]
    m = sum(xs) / n
    v = sum((x - m) ** 2 for x in xs) / (n - 1)
    return m / math.sqrt(v)


def distancia_sismica_km(dt_sp_s: float, vp: float = VP, vs: float = VS) -> float:
    return dt_sp_s * vp * vs / (vp - vs)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Camara ilustrativa: f = {F_MM} mm, paso = {PITCH_UM} um")
    print(" rango [m]   GSD [mm/pix]")
    for d in (2.0, 10.0, 50.0, 100.0):
        print(f"{d:9.1f}   {gsd_m(d) * 1e3:10.4f}")
    # prueba analitica: GSD escala lineal con el rango
    assert abs(gsd_m(100.0) / gsd_m(10.0) - 10.0) < 1e-12
    assert abs(gsd_m(10.0) - 7.4e-6 * 10.0 / 0.034) < 1e-15
    print("Escala lineal con el rango comprobada.")
    print("SNR de fotones (lectura = 10 e-):")
    print("  N [e-]   SNR analitico   SNR Monte Carlo   dif relativa")
    peor = 0.0
    for n_e in (100.0, 1000.0, 10000.0):
        a, mc = snr_analitico(n_e, 10.0), snr_montecarlo(n_e, 10.0)
        peor = max(peor, abs(mc / a - 1))
        print(f"{n_e:8.0f}   {a:12.3f}   {mc:14.3f}   {abs(mc / a - 1):10.4f}")
    assert peor < 0.01, peor
    print(f"Diferencia maxima Monte Carlo/analitico = {peor:.4f} (< 0.01).")
    print(f"Sismica (vp = {VP} km/s, vs = {VS} km/s):")
    for dt in (10.0, 30.0, 60.0):
        print(f"  S-P = {dt:5.1f} s  ->  distancia = {distancia_sismica_km(dt):8.2f} km")
    d = distancia_sismica_km(30.0)
    # prueba de ida y vuelta: tiempos de llegada recalculados reproducen el retardo
    assert abs(d / VS - d / VP - 30.0) < 1e-9
    print("Ida y vuelta de tiempos de llegada comprobada (< 1e-9 s).")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
