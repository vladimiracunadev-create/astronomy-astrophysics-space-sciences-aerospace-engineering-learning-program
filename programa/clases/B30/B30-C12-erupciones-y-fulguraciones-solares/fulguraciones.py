#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C12: clases de fulguracion, ley de potencias de los picos, efecto Neupert y energia radiada.

Datos: las clases A, B, C, M y X son los umbrales del flujo de rayos X blandos GOES de 0.1-0.8 nm (1e-8, 1e-7, 1e-6, 1e-5, 1e-4 W/m2) de NOAA (spaceweather.gov,
pagina de escalas, consultada 2026-11-09); 1 au (IERS TN36). Los eventos (indice 2.0, 2000 eventos, piso de B1), el pulso de rayos X duros (gaussiano) y la duracion (600 s)
son ILUSTRATIVOS (sinteticos); no se reproduce ningun catalogo.
Modelo: (1) clasificacion por umbral con numero = flujo/umbral de la clase; (2) muestreo de picos por transformada inversa de una ley de potencias dN/dF ~ F^-alpha con
semilla fija y estimador de maxima verosimilitud alpha = 1 + n/Sum ln(F/F_min) con error (alpha - 1)/sqrt(n); (3) efecto Neupert: el flujo de rayos X blandos es la integral
del flujo de rayos X duros, de modo que d(SXR)/dt recupera el HXR; (4) energia radiada en la banda E = 4 pi d^2 Int F dt (emision isotropa).
Supuestos: eventos independientes, emision isotropa. Validez: ilustrativa.
Tolerancia: alpha estimado dentro de 3 errores del verdadero; derivada del SXR frente al HXR dentro de 1e-3 del maximo; Simpson frente a F_pico sigma sqrt(2 pi) a 1e-6.
"""
from __future__ import annotations
import math
import platform
import random
import sys

AU = 1.49597870700e11
CLASES = (("A", 1e-8), ("B", 1e-7), ("C", 1e-6), ("M", 1e-5), ("X", 1e-4))


def clase(f):
    letra, umbral = CLASES[0]
    for l, u in CLASES:
        if f >= u:
            letra, umbral = l, u
    return f"{letra}{f / umbral:.1f}"


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for f in (5e-9, 3.4e-6, 1.0e-5, 1.2e-4, 2.8e-3):
        print(f"flujo {f:.1e} W/m2 -> clase {clase(f)}")
    assert clase(3.4e-6) == "C3.4" and clase(1.2e-4) == "X1.2" and clase(1e-5) == "M1.0"
    # ley de potencias
    rng = random.Random(20261109)
    alpha, n, fmin = 2.0, 2000, 1e-7
    picos = [fmin * (1 - rng.random()) ** (-1 / (alpha - 1)) for _ in range(n)]
    a_hat = 1 + n / sum(math.log(f / fmin) for f in picos)
    err = (a_hat - 1) / math.sqrt(n)
    print(f"{n} picos con indice verdadero {alpha} y piso B1: indice estimado = {a_hat:.3f} +/- {err:.3f}")
    assert abs(a_hat - alpha) < 3 * err, "indice de la ley de potencias"
    cuentas = {l: 0 for l, _ in CLASES}
    for f in picos:
        cuentas[clase(f)[0]] += 1
    esperado = {}
    umb = [u for _, u in CLASES] + [1e-3]
    for (l, u), u2 in zip(CLASES, umb[1:]):
        esperado[l] = n * ((u / fmin) ** (1 - alpha) - (u2 / fmin) ** (1 - alpha)) if u >= fmin else 0
    print(f"{'clase':>6} {'eventos':>8} {'esperados (ley de potencias)':>30}")
    for l, _ in CLASES:
        print(f"{l:>6} {cuentas[l]:8d} {esperado[l]:30.1f}")
    # Neupert
    dt = 1.0
    t = [i * dt for i in range(0, 1201)]
    mu, sg = 400.0, 60.0
    hxr = [math.exp(-0.5 * ((x - mu) / sg) ** 2) for x in t]
    sxr = [0.0]
    for i in range(1, len(t)):
        sxr.append(sxr[-1] + 0.5 * (hxr[i] + hxr[i - 1]) * dt)
    der = [(sxr[i + 1] - sxr[i - 1]) / (2 * dt) for i in range(1, len(t) - 1)]
    dif = max(abs(der[i - 1] - hxr[i]) for i in range(1, len(t) - 1))
    print(f"efecto Neupert: max |d(SXR)/dt - HXR| = {dif:.2e} (HXR maximo 1); SXR final = {sxr[-1]:.3f} (analitico sigma sqrt(2 pi) = {sg * math.sqrt(2 * math.pi):.3f})")
    assert dif < 1e-3 and abs(sxr[-1] / (sg * math.sqrt(2 * math.pi)) - 1) < 1e-6
    # energia: pulso gaussiano de pico 1e-4 W/m2 (X1) y sigma que da 10 min de ancho completo a media altura
    fpico = 1e-4
    fwhm = 600.0
    sigma = fwhm / (2 * math.sqrt(2 * math.log(2)))
    h = sigma * 10 / 2000
    s = 2 * fpico * math.exp(-12.5)
    for i in range(1, 2000):
        x = -5 * sigma + i * (10 * sigma) / 2000
        s += fpico * math.exp(-0.5 * (x / sigma) ** 2) * (4 if i % 2 else 2)
    simp = s * (10 * sigma / 2000) / 3
    ana = fpico * sigma * math.sqrt(2 * math.pi)
    print(f"pulso X1 con FWHM = 600 s (sigma = {sigma:.1f} s): fluencia por Simpson = {simp:.5f} J/m2 ; F_pico sigma sqrt(2 pi) = {ana:.5f} J/m2")
    assert abs(simp / ana - 1) < 1e-6
    area = 4 * math.pi * AU ** 2
    print(f"energia radiada en 0.1-0.8 nm (isotropa): {ana * area:.3e} J = {ana * area * 1e7:.3e} erg")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
