#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C07: coronografo, difraccion de Airy, punto de Poisson de un ocultador externo y contraste exigido.

Datos: ninguna constante fisica de una fuente. TODO es ILUSTRATIVO: lambda = 550 nm, disco ocultador de radio a = 0,05 m a z = 1000 m del telescopio (numero de Fresnel 4,5),
brillo coronal relativo de 1e-6 del disco (orden de magnitud de uso general, no consultado en esta clase) y objetivo de supresion.
Modelo: (1) intensidad de Airy I(x) = (2 J1(pi x)/(pi x))^2 con J1 por la integral de Bessel (trapecio periodico), contrastada con la energia encerrada analitica
EE(x) = 1 - J0^2 - J1^2 y con la envolvente asintotica; (2) difraccion de Fresnel de un disco opaco: U(r) = 1 + (i k/z) exp(i k r^2/2z) integral_0^a J0(k r rho/z) exp(i k rho^2/2z) rho drho,
cuya intensidad axial vale exactamente 1 (punto de Poisson); (3) supresion requerida para ver una corona de brillo relativo b con relacion senal/fondo 10.
Supuestos: onda plana, disco perfectamente opaco y circular, aproximacion de Fresnel, sin apodizacion ni etapa de Lyot. Validez: ilustrativa.
Tolerancia: energia encerrada numerica frente a analitica, 1e-6; intensidad axial frente a 1, 1e-6; envolvente asintotica, 5 %.
"""
from __future__ import annotations
import math, cmath, platform


def j_bessel(n, z, m=256):
    s = 0.0
    for k in range(m):
        t = 2 * math.pi * (k + 0.5) / m
        s += math.cos(n * t - z * math.sin(t))
    return s / m


def airy(x):
    if x == 0:
        return 1.0
    z = math.pi * x
    return (2 * j_bessel(1, z) / z) ** 2


def ee_numerica(x, n=20000):
    # energia encerrada = integral de 2 pi x I(x) dx dividida por la potencia total 4/pi (x en unidades de lambda/D)
    h = x / n
    s = 0.0
    for i in range(n + 1):
        xi = i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * airy(xi) * xi
    return s * h / 3 * 2 * math.pi / (4 / math.pi)


def ee_analitica(x):
    z = math.pi * x
    return 1 - j_bessel(0, z) ** 2 - j_bessel(1, z) ** 2


def fresnel_disco(r, lam=550e-9, a=0.05, z=1000.0, n=2000):
    k = 2 * math.pi / lam
    h = a / n
    s = 0j
    for i in range(n + 1):
        rho = i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * j_bessel(0, k * r * rho / z, 64) * cmath.exp(1j * k * rho * rho / (2 * z)) * rho
    s *= h / 3
    return 1 + 1j * k / z * cmath.exp(1j * k * r * r / (2 * z)) * s


def calc():
    r = {}
    r["airy"] = {x: airy(x) for x in (0.0, 1.22, 3.0, 5.0, 10.0)}
    z = math.pi * 10.5
    r["env"] = (airy(10.5), 4 * (2 / (math.pi * z)) * math.cos(z - 3 * math.pi / 4) ** 2 / z ** 2)
    r["ee"] = {x: (ee_numerica(x), ee_analitica(x)) for x in (1.22, 2.23, 5.0)}
    lam, a, zz = 550e-9, 0.05, 1000.0
    r["fresnel_n"] = a * a / (lam * zz)
    r["poisson"] = {}
    for rr in (0.0, 0.01, 0.025, 0.05, 0.1):
        u = fresnel_disco(rr)
        r["poisson"][rr] = abs(u) ** 2
    b = 1e-6
    r["supresion"] = b / 10
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print("Intensidad de Airy normalizada I(x), x en lambda/D:")
    for x, v in r["airy"].items():
        print(f"  x = {x:5.2f}  I = {v:.4e}")
    print(f"envolvente asintotica en x = 10.5: exacta = {r['env'][0]:.4e} ; asintotica = {r['env'][1]:.4e}")
    print(f"{'x':>6} {'EE numerica':>14} {'EE analitica':>14}")
    for x, (a, b) in r["ee"].items():
        print(f"{x:6.2f} {a:14.8f} {b:14.8f}")
        assert abs(a - b) < 1e-6
    print(f"numero de Fresnel N = a^2/(lambda z) = {r['fresnel_n']:.3f}")
    for rr, v in r["poisson"].items():
        print(f"  r = {rr*100:5.1f} cm : |U|^2 = {v:.6f}")
    print(f"supresion requerida para ver brillo 1e-6 con S/N = 10: {r['supresion']:.1e}")
    assert abs(r["poisson"][0.0] - 1) < 1e-6
    assert abs(r["airy"][1.22]) < 2e-3 and abs(r["airy"][0.0] - 1) < 1e-12
    assert abs(r["env"][0] - r["env"][1]) / r["env"][0] < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
