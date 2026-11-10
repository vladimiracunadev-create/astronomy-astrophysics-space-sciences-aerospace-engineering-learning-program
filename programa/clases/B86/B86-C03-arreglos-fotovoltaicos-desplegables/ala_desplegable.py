#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C03: dimensionamiento de un ala solar desplegable SINTETICA (2 alas de 2 paneles).

Datos consultados (2026-11-10): irradiancia solar 1361.0 W/m2 (NASA/NSSDC); eficiencia BOL de celda 29.5 % (tabla de celdas del estado del
arte de la NASA, como valor tipico).
ILUSTRATIVOS (sinteticos): paneles de 0.50 m x 0.60 m, 2 paneles por ala y 2 alas, factor de empaquetado 0.85, densidad de area 2.2 kg/m2,
espesor de panel plegado 25 mm con holgura de 5 mm, rigidez a flexion EI = 120 N m2 por ala (viga en voladizo, uniforme).
Modelo: P = G A f_emp eta cos(theta); frecuencia de flexion f1 = (x1^2 / (2 pi L^2)) sqrt(EI / m'), con x1 raiz de cosh(x) cos(x) = -1.
Segunda via: x1 por biseccion frente a 1.8751040687 (valor de tablas de la viga de Euler-Bernoulli) y cociente de Rayleigh con la forma
estatica phi = 3 xi^2 - xi^3 (cota superior de f1).
Tolerancia: x1 numerico frente al tabulado < 1e-8; el cociente de Rayleigh debe quedar entre 0 % y 2 % por encima de f1.
"""
from __future__ import annotations
import math, platform

G, ETA, EMP = 1361.0, 0.295, 0.85
W, LP, NP, NA = 0.50, 0.60, 2, 2            # ancho, largo de panel [m], paneles por ala, alas
RHO_A, EI = 2.2, 120.0                      # kg/m2, N m2 por ala
ESP, HOLG = 0.025, 0.005                    # m


def raiz_viga():
    f = lambda x: math.cosh(x) * math.cos(x) + 1.0
    lo, hi = 1.5, 2.5
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if f(lo) * f(m) <= 0.0:
            hi = m
        else:
            lo = m
    return 0.5 * (lo + hi)


def rayleigh(L, ei, mlin, n=20000):
    h = 1.0 / n
    num = den = 0.0
    for k in range(n + 1):
        xi = k * h
        c = 1.0 if k in (0, n) else (4.0 if k % 2 else 2.0)
        d2 = 6.0 - 6.0 * xi            # phi'' de phi = 3 xi^2 - xi^3 (con xi = x/L)
        phi = 3.0 * xi ** 2 - xi ** 3
        num += c * ei * d2 ** 2 / L ** 4
        den += c * mlin * phi ** 2
    num *= h / 3.0 * L
    den *= h / 3.0 * L
    return math.sqrt(num / den) / (2.0 * math.pi)


def resultados():
    a_ala = W * LP * NP * NA
    p_bol = G * a_ala * EMP * ETA
    L = LP * NP
    mlin = RHO_A * W
    x1 = raiz_viga()
    f1 = x1 ** 2 / (2.0 * math.pi * L ** 2) * math.sqrt(EI / mlin)
    fr = rayleigh(L, EI, mlin)
    masa = RHO_A * a_ala
    return dict(A=a_ala, Pbol=p_bol, L=L, mlin=mlin, x1=x1, x1_tab=1.8751040687, dx1=abs(x1 - 1.8751040687), f1=f1, fR=fr,
                errR=(fr - f1) / f1 * 100.0, masa=masa, Wsp=p_bol / masa,
                P30=p_bol * math.cos(math.radians(30)), P60=p_bol * math.cos(math.radians(60)),
                hstow=NP * (ESP + HOLG) + ESP, hpanel_t=NP * (ESP + HOLG), P45=p_bol * math.cos(math.radians(45)), Wsp3=p_bol / (3.0 * a_ala),
                f1x2=2.0 * f1, f1c=f1 / 4.0, A300=300.0 / (G * EMP * ETA), cos45=math.cos(math.radians(45)))


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Ala SINTETICA: {NA} alas x {NP} paneles de {W} m x {LP} m; area total = {r['A']:.3f} m2 ; masa = {r['masa']:.2f} kg")
    print(f"Potencia BOL normal al Sol = {r['Pbol']:.2f} W ; potencia especifica = {r['Wsp']:.1f} W/kg")
    print(f"Con el Sol a 30 grados = {r['P30']:.2f} W ; a 60 grados = {r['P60']:.2f} W")
    print(f"Altura plegada por ala = {r['hstow']*1000:.0f} mm (paneles de {ESP*1000:.0f} mm con holgura de {HOLG*1000:.0f} mm)")
    print(f"Viga en voladizo L = {r['L']:.2f} m, masa lineal = {r['mlin']:.2f} kg/m, EI = {EI:.0f} N m2")
    print(f"x1 numerico = {r['x1']:.10f} ; tabulado = {r['x1_tab']:.10f} ; diferencia = {r['dx1']:.1e}")
    print(f"f1 = {r['f1']:.4f} Hz ; cociente de Rayleigh = {r['fR']:.4f} Hz ({r['errR']:+.3f} %)")
    assert r["dx1"] < 1e-8
    assert 0.0 <= r["errR"] < 2.0
    assert abs(r["P60"] - 0.5 * r["Pbol"]) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
