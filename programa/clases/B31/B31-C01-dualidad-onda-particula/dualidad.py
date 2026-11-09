#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C01: longitud de onda de de Broglie y patron de doble rendija por Monte Carlo.

Datos: h, c, e, m_e y m_n (NIST CODATA 2022, tabla allascii.txt), consultados 2026-11-09. La separacion de las rendijas (1 um), el ancho de cada una (0.1 um), la distancia a la pantalla (1 m),
la energia de los electrones (50 keV), la temperatura del neutron termico (293 K) y la pelota (0.145 kg, 40 m/s) son ILUSTRATIVOS (sinteticos).
Modelo: lambda = h/p con p c = sqrt(T^2 + 2 T m c^2) (relativista); intensidad de Fraunhofer I(y) = cos^2(pi d y/(lambda L)) sinc^2(pi a y/(lambda L)); muestreo por rechazo (semilla fija) de
los impactos y espaciado de franjas recuperado del maximo de la transformada de Fourier discreta del histograma; comparacion con lambda L/d.
Supuestos: aproximacion de angulos pequenos, rendijas ideales, coherencia total. Validez: franja central y primeros lobulos.
Tolerancia: lambda sqrt(T) = h/sqrt(2 m e) a 1e-12; espaciado de franjas recuperado dentro del 1.5 % del analitico.
"""
from __future__ import annotations
import math
import platform
import random
import sys

H, C, E, ME, MN, KB = 6.62607015e-34, 299792458.0, 1.602176634e-19, 9.1093837139e-31, 1.67492750056e-27, 1.380649e-23


def lam_rel(t_ev, masa):
    t = t_ev * E
    pc = math.sqrt(t * t + 2 * t * masa * C * C)
    return H * C / pc


def sinc(x):
    return 1.0 if abs(x) < 1e-12 else math.sin(x) / x


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'objeto':<28} {'energia / velocidad':<22} {'lambda [m]':>12}")
    for t in (100.0, 1e3, 1e5):
        print(f"{'electron':<28} {f'{t:g} eV':<22} {lam_rel(t, ME):12.4e}")
    tn = 1.5 * KB * 293 / E
    print(f"{'neutron termico (293 K)':<28} {f'{tn:.4f} eV':<22} {lam_rel(tn, MN):12.4e}")
    ev2 = 2.0
    print(f"{'foton de 2 eV':<28} {'p = E/c':<22} {H * C / (ev2 * E):12.4e}")
    m, v = 0.145, 40.0
    print(f"{'pelota 0.145 kg':<28} {'40 m/s':<22} {H / (m * v):12.4e}")
    c_nr = H / math.sqrt(2 * ME * E)
    assert abs(lam_rel(1e-3, ME) * math.sqrt(1e-3) / c_nr - 1) < 1e-6
    print(f"constante no relativista lambda sqrt(T) = {c_nr * 1e9:.6f} nm eV^(1/2) (12.264 A eV^(1/2))")
    # doble rendija
    t = 50e3
    lam = lam_rel(t, ME)
    d, a, big_l = 1e-6, 0.1e-6, 1.0
    dy = lam * big_l / d
    print(f"electrones de 50 keV: lambda = {lam:.4e} m ; espaciado de franjas lambda L/d = {dy * 1e6:.4f} um ; primer cero de la envolvente en {lam * big_l / a * 1e6:.2f} um")
    rng = random.Random(20261109)
    ymax = 40e-6
    pts = []
    while len(pts) < 120000:
        y = rng.uniform(-ymax, ymax)
        i = math.cos(math.pi * d * y / (lam * big_l)) ** 2 * sinc(math.pi * a * y / (lam * big_l)) ** 2
        if rng.random() < i:
            pts.append(y)
    nb = 800
    hist = [0] * nb
    for y in pts:
        hist[min(nb - 1, int((y + ymax) / (2 * ymax) * nb))] += 1
    mean = sum(hist) / nb
    hist = [x - mean for x in hist]
    best, fbest = 0.0, 0.0
    for k in range(1, 4001):
        f_um = k * 0.0001
        re = sum(h * math.cos(2 * math.pi * f_um * ((j + 0.5) * 2 * ymax / nb * 1e6 - ymax * 1e6)) for j, h in enumerate(hist))
        im = sum(h * math.sin(2 * math.pi * f_um * ((j + 0.5) * 2 * ymax / nb * 1e6 - ymax * 1e6)) for j, h in enumerate(hist))
        p = re * re + im * im
        if p > best:
            best, fbest = p, f_um
    dy_rec = 1.0 / fbest * 1e-6
    print(f"{len(pts)} impactos: frecuencia espacial recuperada = {fbest:.4f} ciclos/um -> espaciado = {dy_rec * 1e6:.4f} um ; analitico = {dy * 1e6:.4f} um ; cociente = {dy_rec / dy:.4f}")
    assert abs(dy_rec / dy - 1) < 0.015, "espaciado de franjas"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
