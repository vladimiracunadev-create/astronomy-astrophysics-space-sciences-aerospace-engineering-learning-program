#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B70-C05: contraste térmico de una lava reciente sobre la superficie de Venus a 1,02 micrometros.

Datos: temperatura superficial media de Venus 737 K (hoja de datos NASA/NSSDC, consultada 2026-11-09). Constantes SI definidas: h = 6,62607015e-34 J s,
k = 1,380649e-23 J/K, c = 299792458 m/s. Temperatura de la lava (1000 K), longitud de onda (1,02 um, ventana de emision de la superficie) y fracciones
de pixel: ILUSTRATIVOS (sinteticos). No se modela ninguna imagen real ni se reproduce ninguna medida.
Modelo: radiancia de Planck B(lambda, T) = 2 h c^2 / lambda^5 / (exp(h c / (lambda k T)) - 1) [W m^-2 sr^-1 m^-1], emisividad 1 (cuerpo negro).
Un pixel con fraccion f a temperatura T_l y el resto a T_s tiene B_pix = (1-f) B_s + f B_l; el aumento relativo es f (B_l/B_s - 1).
Pruebas: (1) integral numerica de B sobre todo lambda = sigma T^4 / pi con sigma = 2 pi^5 k^4/(15 h^3 c^2); (2) limite de Wien en
lambda T pequeño; (3) fraccion minima de pixel detectable para un aumento dado, ida y vuelta.
Supuestos: cuerpo negro, sin atmosfera ni nubes (el cociente real se ve afectado), emisividad 1. Validez: ilustrativa.
Tolerancia: 1e-6 relativo en la integral de Stefan-Boltzmann; 1e-4 en Wien.
"""
from __future__ import annotations
import math, platform

H, K, C = 6.62607015e-34, 1.380649e-23, 299792458.0
SIGMA = 2 * math.pi**5 * K**4 / (15 * H**3 * C**2)

def planck(lam, T):
    x = H * C / (lam * K * T)
    if x > 700:
        return 0.0
    return 2 * H * C**2 / lam**5 / math.expm1(x)

def integral_planck(T, n=200000):
    # integral en x = h c/(lam k T) de 0 a 60: lam = h c/(x k T); dlam = -h c/(k T x^2) dx
    xmax = 60.0
    h = xmax / n
    s = 0.0
    for i in range(1, n + 1):
        x = (i - 0.5) * h
        lam = H * C / (x * K * T)
        s += planck(lam, T) * H * C / (K * T * x * x) * h
    return s

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"sigma calculada = {SIGMA:.6e} W m^-2 K^-4")
    for T in (737.0, 1000.0):
        I = integral_planck(T)
        ref = SIGMA * T**4 / math.pi
        assert abs(I - ref) / ref < 1e-6, "integral de Planck no coincide con Stefan-Boltzmann"
        print(f"  T = {T:6.1f} K: integral numerica = {I:.6e} ; sigma T^4/pi = {ref:.6e} W m^-2 sr^-1")
    lam, Ts, Tl = 1.02e-6, 737.0, 1000.0
    for T in (300.0,):
        w = 2 * H * C**2 / lam**5 * math.exp(-H * C / (lam * K * T))
        assert abs(planck(lam, T) - w) / w < 1e-4
    print("Limite de Wien a 300 K superado.")
    Bs, Bl = planck(lam, Ts), planck(lam, Tl)
    print(f"B(1,02 um, 737 K) = {Bs:.4e} ; B(1,02 um, 1000 K) = {Bl:.4e} W m^-2 sr^-1 m^-1 ; cociente = {Bl/Bs:.2f}")
    print("Aumento relativo del pixel segun la fraccion f de lava a 1000 K (ilustrativa):")
    for f in (0.001, 0.01, 0.05, 0.1):
        print(f"  f = {f:5.3f}: aumento = {f*(Bl/Bs-1)*100:7.2f} %")
    for umbral in (0.05, 0.20):
        f = umbral / (Bl / Bs - 1)
        assert abs(f * (Bl / Bs - 1) - umbral) < 1e-12
        print(f"Fraccion minima para un aumento de {umbral*100:.0f} %: f = {f:.4f}")
    print("Cociente de radiancias segun la temperatura de la lava (1,02 um, fondo 737 K):")
    for T in (800.0, 900.0, 1000.0, 1200.0):
        print(f"  T_lava = {T:6.1f} K: B_l/B_s = {planck(lam, T)/Bs:8.2f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
