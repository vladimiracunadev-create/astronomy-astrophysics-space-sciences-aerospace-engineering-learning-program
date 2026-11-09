#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C02: de un objetivo cientifico a requisitos de un instrumento orbital (apertura, periodo, eclipses y masa).

Datos: GM_Tierra = 3,986004e14 m3/s2 y R_ecuatorial = 6,3781e6 m de la Resolucion B3 de la UAI de 2015 (arXiv:1510.07674, consultada el 2026-11-09).
ILUSTRATIVOS (no son requisitos de ninguna mision): resolucion objetivo 0,1 arcsec a 500 nm, orbita circular a 600 km, formato de detector 4096 x 4096 de 16 bit,
presupuesto de masa de subsistemas y margen del 20 %.
Modelo: (1) apertura minima por difraccion D = 1,028 lambda / theta; (2) periodo kepleriano T = 2 pi sqrt(a^3/GM) contrastado con una integracion numerica RK4 de la orbita;
(3) fraccion de eclipse para beta = 0 con sin(rho) = R/a; (4) volumen de datos por imagen y presupuesto de masa con margen.
Supuestos: orbita circular, Tierra esferica, sombra cilindrica. Validez: dimensionamiento preliminar, no un analisis de mision.
Tolerancia: periodo numerico frente al kepleriano, 1e-6 relativo; suma del presupuesto exacta.
"""
from __future__ import annotations
import math, platform

GM = 3.986004e14
RE = 6.3781e6
ARCSEC = math.pi / 180 / 3600


def periodo_numerico(a, pasos=20000):
    v = math.sqrt(GM / a)
    s = [a, 0.0, 0.0, v]
    t_kep = 2 * math.pi * math.sqrt(a ** 3 / GM)
    dt = t_kep / pasos

    def f(s):
        x, y, vx, vy = s
        r3 = (x * x + y * y) ** 1.5
        return [vx, vy, -GM * x / r3, -GM * y / r3]

    t = 0.0
    prev_y = 0.0
    while True:
        k1 = f(s)
        k2 = f([s[i] + 0.5 * dt * k1[i] for i in range(4)])
        k3 = f([s[i] + 0.5 * dt * k2[i] for i in range(4)])
        k4 = f([s[i] + dt * k3[i] for i in range(4)])
        n = [s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4)]
        if t > 0.5 * t_kep and s[1] < 0 <= n[1]:      # cruce ascendente del eje x
            frac = -s[1] / (n[1] - s[1])
            return t + frac * dt
        s = n
        t += dt


def calc():
    r = {}
    lam, th = 500e-9, 0.1 * ARCSEC
    r["D"] = 1.028 * lam / th
    h = 600e3
    a = RE + h
    r["a"] = a
    r["T_kep"] = 2 * math.pi * math.sqrt(a ** 3 / GM)
    r["T_num"] = periodo_numerico(a)
    rho = math.asin(RE / a)
    r["rho_deg"] = math.degrees(rho)
    r["f_ecl"] = rho / math.pi
    r["t_ecl"] = r["f_ecl"] * r["T_kep"]
    r["ciclos_ano"] = 365.25 * 86400 / r["T_kep"]
    r["bits_img"] = 4096 * 4096 * 16
    r["MB_img"] = r["bits_img"] / 8 / 1e6
    masas = {"estructura": 38.0, "optica": 22.0, "detector y electronica": 9.5, "control de actitud": 14.0, "energia": 21.0, "comunicaciones": 6.5}
    r["masas"] = masas
    r["m_suma"] = sum(masas.values())
    r["m_margen"] = r["m_suma"] * 1.2
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"apertura minima para 0.1 arcsec a 500 nm: D = {r['D']:.3f} m")
    print(f"a = {r['a']/1e3:.1f} km ; periodo kepleriano = {r['T_kep']:.3f} s ; periodo numerico RK4 = {r['T_num']:.3f} s")
    print(f"semiangulo de la Tierra rho = {r['rho_deg']:.3f} grados ; fraccion de eclipse (beta = 0) = {r['f_ecl']:.4f} ({r['t_ecl']/60:.2f} min)")
    print(f"ciclos termicos por anio = {r['ciclos_ano']:.0f}")
    print(f"imagen de 4096 x 4096 x 16 bit = {r['bits_img']} bit = {r['MB_img']:.3f} MB")
    for k, v in r["masas"].items():
        print(f"  {k:24s} {v:6.1f} kg")
    print(f"suma = {r['m_suma']:.1f} kg ; con margen del 20 % = {r['m_margen']:.1f} kg")
    assert abs(r["T_num"] - r["T_kep"]) / r["T_kep"] < 1e-6
    assert abs(r["D"] - 1.0592) < 0.01
    assert abs(r["m_suma"] - 111.0) < 1e-9
    assert 0.3 < r["f_ecl"] < 0.4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
