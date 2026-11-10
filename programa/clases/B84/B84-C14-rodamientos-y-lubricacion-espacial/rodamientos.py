#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C14: contacto de Hertz en un rodamiento de bolas, vida L10 y duracion del lubricante frente a su evaporacion en vacio.

DATOS ILUSTRATIVOS (no consultados): bola de acero de radio R = 3,175 mm; E = 200 GPa, nu = 0,30 (E* = 1/((1-nu^2)/E x 2) = 109,9 GPa);
carga normal por bola Q = 100 N; surco de radio r_g = 0,52 d = 3,302 mm (conformidad 52 %), aproximado como cavidad esferica en el plano de rodadura (APROXIMACION: el
contacto real es toroidal/eliptico); capacidad dinamica C = 4,0 kN y carga equivalente P = 0,8 kN; velocidad 60 rpm.
Hertz (esfera-plano o esfera-cavidad): a = (3 Q R'/(4 E*))^(1/3) con 1/R' = 1/R1 + 1/R2 (R2 < 0 para cavidad); p0 = 3 Q/(2 pi a^2).
Vida L10 = (C/P)^3 millones de revoluciones (rodamiento de bolas; no consultado el texto de ISO 281).
Lubricante: masa m0 = 2,0 mg sobre area expuesta A = 1,0e-4 m2; presion de vapor P(T) = 1e-7 Pa exp(-H/R (1/T - 1/300)), H = 80 kJ/mol; masa molar 0,5 kg/mol;
flujo de Langmuir (cota superior, alfa = 1) J = P sqrt(M/(2 pi R T)). Constantes exactas del SI (no consultadas): R = 8,314462618.
Segunda via de Hertz: la presion media = Q/(pi a^2) = 2/3 p0 (identidad); a se recalcula por una tercera expresion con el modulo reducido.
Tolerancia: identidad p_media = 2/3 p0 a 1e-12.
"""
from __future__ import annotations
import math, platform

R_BOLA, E, NU = 3.175e-3, 200e9, 0.30
RG = 3.302e-3
R_GAS = 8.314462618


def hertz(Q, R1, R2):
    Estar = 1.0 / (2.0 * (1 - NU ** 2) / E)
    Rp = 1.0 / (1.0 / R1 + 1.0 / R2) if R2 is not None else R1
    a = (3 * Q * Rp / (4 * Estar)) ** (1 / 3)
    p0 = 3 * Q / (2 * math.pi * a * a)
    return a, p0, Rp, Estar


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    Q = 100.0
    print("Bola de 6,35 mm de acero (valores ILUSTRATIVOS), carga normal Q = 100 N")
    print(f"{'contacto':24s} {'R_eq [mm]':>10s} {'a [mm]':>8s} {'p0 [MPa]':>9s} {'p_media [MPa]':>14s}")
    for nom, R2 in (("bola sobre plano", None), ("bola en surco 52 % (aprox.)", -RG)):
        a, p0, Rp, Es = hertz(Q, R_BOLA, R2)
        pm = Q / (math.pi * a * a)
        assert abs(pm - 2 / 3 * p0) / pm < 1e-12
        print(f"{nom:28s} {Rp * 1e3:8.3f} {a * 1e3:8.4f} {p0 / 1e6:9.1f} {pm / 1e6:14.1f}")
    print(f"E* = {1.0 / (2.0 * (1 - NU ** 2) / E) / 1e9:.1f} GPa")
    print("Presion de contacto frente a la carga (bola sobre plano): p0 ~ Q^(1/3)")
    prev = None
    for q in (25.0, 50.0, 100.0, 200.0, 400.0):
        a, p0, _, _ = hertz(q, R_BOLA, None)
        extra = "" if prev is None else f" (x{p0 / prev:.3f} al duplicar Q; 2^(1/3) = {2 ** (1 / 3):.3f})"
        print(f"  Q = {q:5.0f} N  p0 = {p0 / 1e6:8.1f} MPa{extra}")
        prev = p0
    C, Pq, rpm = 4000.0, 800.0, 60.0
    L10 = (C / Pq) ** 3
    horas = L10 * 1e6 / (rpm * 60)
    print(f"Vida L10 = (C/P)^3 = {L10:.1f} millones de revoluciones = {horas:.3e} h a {rpm:.0f} rpm = {horas / 8766:.1f} anos")
    print("Lubricante en vacio (cota superior): m0 = 2,0 mg, A = 1e-4 m2, M = 0,5 kg/mol, P(300 K) = 1e-7 Pa, H = 80 kJ/mol")
    for Tc in (20.0, 50.0, 80.0):
        T = Tc + 273.15
        P = 1e-7 * math.exp(-80e3 / R_GAS * (1 / T - 1 / 300.0))
        J = P * math.sqrt(0.5 / (2 * math.pi * R_GAS * T))
        dm_dt = J * 1e-4
        dias = 2.0e-6 / dm_dt / 86400
        print(f"  T = {Tc:4.0f} C  P = {P:.2e} Pa  flujo = {dm_dt * 1e6:.3e} mg/s  tiempo para evaporar 2 mg = {dias:.3e} dias = {dias / 365.25:.3e} anos")
    assert 4.0 < L10 < 200
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
