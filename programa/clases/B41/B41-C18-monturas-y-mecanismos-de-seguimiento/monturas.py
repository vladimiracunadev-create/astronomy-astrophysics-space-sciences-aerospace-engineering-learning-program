#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C18: rotacion de campo de una montura altazimutal y error periodico de un tornillo sinfin.

Datos: sin constantes del NIST. La velocidad sideral, 360 grados / 86164,0905 s = 15,0411 arcsec/s, usa el dia sideral de libro (NO consultado; ilustrativo).
Latitud -30 grados, estrella de declinacion -20 grados, periodo del sinfin de 479 s, amplitud periodica de 15 arcsec y exposiciones de 1 a 600 s son ILUSTRATIVOS.
Modelo: (1) rotacion de campo en una montura altazimutal: dq/dt = Omega cos(phi) cos(A)/cos(h) (formula de libro) comparada con la derivada numerica del angulo
paralactico q = atan2(sen H, tan(phi) cos(dec) - sen(dec) cos H), calculado desde el vector de la estrella en el sistema del horizonte (altitud h, azimut A desde el norte).
(2) Error periodico e(t) = A sen(2 pi t/P + f): la deriva maxima en una exposicion T es 2 A sen(pi T/P) (T <= P/2), comparada con una simulacion con semilla 20261109.
Supuestos: refraccion y flexiones despreciadas, rotacion terrestre uniforme. Validez: geometria esferica.
Tolerancia: modulo de la formula frente al de la derivada numerica 1e-4 relativo (el signo depende del hemisferio y del convenio); deriva de la simulacion frente a la analitica 1 %.
"""
from __future__ import annotations
import math, platform, random, sys

OMEGA = 360 * 3600 / 86164.0905          # arcsec por segundo


def horizonte(H, dec, lat):
    x = -math.cos(dec) * math.sin(H)
    y = math.sin(dec) * math.cos(lat) - math.cos(dec) * math.sin(lat) * math.cos(H)
    z = math.sin(dec) * math.sin(lat) + math.cos(dec) * math.cos(lat) * math.cos(H)
    return math.atan2(x, y), math.asin(z)


def paralactico(H, dec, lat):
    return math.atan2(math.sin(H), math.tan(lat) * math.cos(dec) - math.sin(dec) * math.cos(H))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"velocidad sideral = {OMEGA:.4f} arcsec/s")
    lat, dec = math.radians(-30.0), math.radians(-20.0)
    print(f"latitud -30 deg, declinacion -20 deg")
    print(f"{'H [h]':>6} {'alt [deg]':>10} {'az [deg]':>9} {'formula [arcsec/s]':>19} {'numerica (modulo) [arcsec/s]':>29}")
    for Hh in (-3.0, -1.0, -0.5, 0.5, 1.0, 3.0):
        H = math.radians(Hh * 15.0)
        A, h = horizonte(H, dec, lat)
        form = OMEGA * math.cos(lat) * math.cos(A) / math.cos(h)
        dH = math.radians(1e-4)
        q1, q0 = paralactico(H + dH, dec, lat), paralactico(H - dH, dec, lat)
        dq = (q1 - q0 + math.pi) % (2 * math.pi) - math.pi
        num = math.degrees(dq) / math.degrees(2 * dH) * OMEGA
        print(f"{Hh:6.1f} {math.degrees(h):10.3f} {math.degrees(A):9.3f} {form:19.4f} {abs(num):29.4f}")
        assert abs(abs(num) - abs(form)) / abs(form) < 1e-4
    # cerca del cenit
    dec2 = math.radians(-29.5)
    print("paso casi cenital (dec -29,5 deg): la rotacion crece sin limite")
    for Hm in (-20.0, -5.0, -1.0, 1.0):
        H = math.radians(Hm / 60.0 * 15.0)
        A, h = horizonte(H, dec2, lat)
        form = OMEGA * math.cos(lat) * math.cos(A) / math.cos(h)
        print(f"  H = {Hm:6.1f} min : alt = {math.degrees(h):8.3f} deg ; rotacion = {form:10.3f} arcsec/s")
    # error periodico
    P, A0 = 479.0, 15.0
    rng = random.Random(20261109)
    print(f"error periodico: P = {P:.0f} s, A = {A0:.0f} arcsec")
    print(f"{'T [s]':>6} {'analitica [arcsec]':>19} {'simulacion [arcsec]':>20}")
    for T in (1.0, 5.0, 20.0, 60.0, 120.0, 239.5):
        ana = 2 * A0 * math.sin(math.pi * T / P)
        mx = 0.0
        for _ in range(4000):
            f0 = rng.uniform(0, 2 * math.pi)
            t0 = 0.0
            # deriva = e(T) - e(0); su maximo sobre la fase es la analitica
            e = A0 * (math.sin(2 * math.pi * T / P + f0) - math.sin(f0))
            mx = max(mx, abs(e))
        print(f"{T:6.1f} {ana:19.4f} {mx:20.4f}")
        assert abs(mx - ana) / ana < 0.01
    T1 = P / math.pi * math.asin(1.0 / (2 * A0))
    print(f"exposicion maxima sin guiado para derivar menos de 1 arcsec = {T1:.2f} s")
    assert abs(T1 - 5.08) < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
