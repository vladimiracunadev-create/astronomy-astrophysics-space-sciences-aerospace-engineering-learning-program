#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C17: geometria de una estrella guia laser: efecto cono (anisoplanatismo focal) y elongacion de la mancha en el sensor.

Datos: altitud de la capa de sodio de 90 km con 10 km de espesor, altitud Rayleigh de 10 km, apertura de 8 m (R = 4 m), perfil de Cn^2 de la clase C12 (ILUSTRATIVO), subapertura
a 8 m del lanzador, lambda = 500 nm y altura de escala de 8 km son valores ILUSTRATIVOS tomados de la memoria de orden de magnitud, NO consultados en fuentes ; los coeficientes 6,88 y 0,423 son de libro de texto
(no consultados). Semilla 20261109. Sin datos de un observatorio.
Modelo: (1) la estrella guia a altitud H ve la turbulencia en una huella conica de radio R (1 - h/H) en la capa h ; extrapolar a la pupila completa produce un error de fase por pares
E[(phi(r) - phi(s r))^2] = D_phi((1 - s) r) con s = 1 - h/H. Con D_phi(r) = 6,88 (r/r0,h)^(5/3) y la media sobre el disco <rho^(5/3)> = (6/11) R^(5/3), el error cuadratico medio SIN quitar pistón ni
inclinacion es sigma^2 = 6,88 (6/11) 0,423 k^2 R^(5/3) int Cn^2(h) (h/H)^(5/3) dh (cota superior). (2) elongacion: angulo entre los rayos desde una subapertura a distancia x del lanzador a la base y a la cima de la capa.
Vias independientes: media sobre el disco por Monte Carlo (2 millones de puntos) frente a 6/11 ; angulo exacto (arctan) frente a la aproximacion x Delta / H^2.
Supuestos: turbulencia de capas finas, sin escala externa, sin correcciones de pistón e inclinacion, geometria sin atmosfera refractiva. Validez: orden de magnitud ; NO es un procedimiento de operacion de laser
(la operacion real exige coordinacion con la autoridad aeronautica y clasificacion de seguridad laser, temas fuera de esta clase).
Tolerancia: media del disco a 2e-3 ; elongacion exacta frente a la aproximada a 1 %.
"""
from __future__ import annotations
import math, platform, random

ARCSEC = 206264.806247

def cn2(h):
    return 4.0e-16 * math.exp(-h / 1000.0) + 1.0e-17 * math.exp(-((h - 8000.0) / 1500.0) ** 2)

def simpson(f, a, b, n=6000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3

def sigma2_cono(R, H, lam=500e-9, hmax=None):
    k = 2 * math.pi / lam
    hmax = min(H, 30000.0) if hmax is None else hmax
    integ = simpson(lambda h: cn2(h) * (h / H) ** (5 / 3), 0.0, hmax)
    return 6.88 * (6 / 11) * 0.423 * k * k * R ** (5 / 3) * integ

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    # media sobre el disco de rho^(5/3)
    n = 2_000_000
    s = 0.0
    for _ in range(n):
        r = math.sqrt(rnd.random())      # distribucion uniforme en el disco unidad
        s += r ** (5 / 3)
    media = s / n
    print(f"<rho^(5/3)> sobre el disco unidad: Monte Carlo = {media:.5f} ; 6/11 = {6 / 11:.5f}")
    assert abs(media - 6 / 11) < 2e-3
    R = 4.0
    print(f"{'estrella guia':<22} {'H [km]':>7} {'sigma^2 [rad^2]':>16} {'sigma [rad]':>12} {'sigma/lambda*500nm [nm]':>24}")
    res = {}
    for nombre, H in (("Rayleigh", 10e3), ("sodio", 90e3), ("estrella natural", 1e12)):
        s2 = sigma2_cono(R, H)
        res[nombre] = s2
        print(f"{nombre:<22} {H / 1e3:7.0f} {s2:16.4f} {math.sqrt(s2):12.4f} {math.sqrt(s2) * 500 / (2 * math.pi):24.1f}")
    assert res["Rayleigh"] > res["sodio"] > res["estrella natural"]
    assert res["estrella natural"] < 1e-9
    # escala con la apertura: (R)^(5/3)
    s_a = sigma2_cono(2.0, 90e3)
    s_b = sigma2_cono(4.0, 90e3)
    print(f"R = 2 m -> {s_a:.4f} rad^2 ; R = 4 m -> {s_b:.4f} rad^2 ; cociente = {s_b / s_a:.4f} (2^(5/3) = {2 ** (5 / 3):.4f})")
    assert abs(s_b / s_a - 2 ** (5 / 3)) < 1e-9
    # escala con la altitud: 1/H^(5/3) mientras la turbulencia este por debajo de H
    r_h = sigma2_cono(R, 10e3) / sigma2_cono(R, 90e3)
    print(f"cociente Rayleigh(10 km)/sodio(90 km) = {r_h:.2f} (limite (90/10)^(5/3) = {9 ** (5 / 3):.1f} para turbulencia muy baja ; menor porque parte de la turbulencia esta sobre 10 km y se trunca)")
    # elongacion
    print(f"{'x [m]':>6} {'elongacion exacta [arcsec]':>27} {'x Delta/H^2 [arcsec]':>22}")
    H0, Delta = 90e3, 10e3
    for x in (0.0, 2.0, 4.0, 8.0, 12.0):
        a_base = math.atan2(x, H0 - Delta / 2)
        a_cima = math.atan2(x, H0 + Delta / 2)
        exacta = (a_base - a_cima) * ARCSEC
        aprox = x * Delta / H0 ** 2 * ARCSEC
        print(f"{x:6.1f} {exacta:27.4f} {aprox:22.4f}")
        if x > 0:
            assert abs(exacta / aprox - 1) < 0.01
    # retrodispersion Rayleigh: densidad y lambda^-4
    dens = math.exp(-10.0 / 8.0)
    print(f"densidad relativa a 10 km con altura de escala 8 km = {dens:.4f} ; factor de seccion eficaz (532/355)^-4 = {(532 / 355) ** -4:.4f} (el ultravioleta dispersa {(532 / 355) ** 4:.2f} veces mas)")
    assert abs((532 / 355) ** 4 - 5.04) < 0.05
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
