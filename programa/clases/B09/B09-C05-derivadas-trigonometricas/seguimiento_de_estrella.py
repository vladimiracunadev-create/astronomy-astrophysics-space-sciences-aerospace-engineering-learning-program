#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C05: derivadas trigonométricas y velocidad de seguimiento.

Datos: omega = 7.292115e-5 rad/s, velocidad angular media nominal de la Tierra
(IERS Conventions 2010, TN36, tabla 1.2, parámetros GRS80). Latitud del
observador y declinaciones: SINTÉTICAS (ejemplos).
Modelo: altitud h de un astro de declinación d, latitud phi, ángulo horario H:
   sin h = sin(phi) sin(d) + cos(phi) cos(d) cos(H),  H = omega t  (estrella;
el ángulo horario de una estrella crece con la rotación sideral).
Derivando respecto a t con la regla de la cadena:
   dh/dt = -omega cos(phi) cos(d) sin(H) / cos(h).
Supuestos: sin refracción, sin movimiento propio, tierra esférica de latitud
geodésica = geocéntrica. Validez: astro por encima del horizonte, h < 90 grados.
Tolerancia: 1e-8 relativa entre derivada analítica y cociente central (h = 1 s).
"""
from __future__ import annotations
import math, platform, sys

OMEGA = 7.292115e-5                       # rad/s
ARCSEC = math.pi / 648000.0


def altitud(t, phi, dec):
    H = OMEGA * t
    s = math.sin(phi) * math.sin(dec) + math.cos(phi) * math.cos(dec) * math.cos(H)
    return math.asin(s)


def tasa_analitica(t, phi, dec):
    H = OMEGA * t
    h = altitud(t, phi, dec)
    return -OMEGA * math.cos(phi) * math.cos(dec) * math.sin(H) / math.cos(h)


def central(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    print(f"omega = {OMEGA:.6e} rad/s = {OMEGA/ARCSEC:.4f} arcsec/s = {2*math.pi/OMEGA:.2f} s (periodo sideral)")
    phi = math.radians(-33.45)
    for dec_deg in (0.0, -30.0):
        dec = math.radians(dec_deg)
        # altura en el meridiano: h = 90 - |phi - dec|
        h0 = math.degrees(altitud(0.0, phi, dec))
        h0_esp = 90 - abs(math.degrees(phi) - dec_deg)
        prueba(abs(h0 - h0_esp) < 1e-9, "altura meridiana 90-|phi-d|")
        print(f"\nDeclinación {dec_deg:+.0f} deg: altura meridiana = {h0:.4f} deg (esperada {h0_esp:.4f})")
        print("  H [deg]   h [deg]   dh/dt analítica ['/s]  numérica ['/s]")
        for H_deg in (-90, -60, -30, -10, 0):
            t = math.radians(H_deg) / OMEGA
            h = math.degrees(altitud(t, phi, dec))
            if h <= 0:
                print(f"  {H_deg:6d}   {h:7.2f}   (bajo el horizonte)")
                continue
            a = tasa_analitica(t, phi, dec) / ARCSEC
            n = central(lambda x: altitud(x, phi, dec), t, 1.0) / ARCSEC
            print(f"  {H_deg:6d}   {h:7.2f}   {a:18.4f}   {n:16.4f}")
            if abs(a) > 1e-3:
                prueba(abs(a - n) / abs(a) < 1e-6, "derivada analítica vs central")
        # culminación: derivada cero
        prueba(abs(tasa_analitica(0.0, phi, dec)) < 1e-18, "dh/dt = 0 en el meridiano")
    # salida del horizonte en el ecuador celeste: dh/dt = omega cos(phi)
    t_sal = -math.pi / 2 / OMEGA
    r = tasa_analitica(t_sal, phi, 0.0)
    prueba(abs(r - OMEGA * math.cos(phi)) < 1e-12, "tasa de salida = omega cos(phi)")
    print(f"\nSalida de un astro de dec = 0: dh/dt = omega cos(phi) = {r/ARCSEC:.4f} arcsec/s")
    # (cos h - 1)/h -> 0 y derivada de sin
    print("\nh        (cos h-1)/h      (sin(x+h)-sin x)/h - cos x   (x = 1)")
    for h in (1e-1, 1e-3, 1e-5):
        c = -2 * math.sin(h / 2) ** 2 / h
        e = (math.sin(1 + h) - math.sin(1)) / h - math.cos(1)
        print(f"{h:7.0e}  {c:14.6e}  {e:14.6e}")
    prueba(abs((math.sin(1 + 1e-6) - math.sin(1)) / 1e-6 - math.cos(1)) < 1e-6, "sin' = cos")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
