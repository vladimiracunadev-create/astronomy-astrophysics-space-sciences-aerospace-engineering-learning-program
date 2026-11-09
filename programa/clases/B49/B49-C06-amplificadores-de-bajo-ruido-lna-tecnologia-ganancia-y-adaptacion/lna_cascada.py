#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C06: temperatura de ruido de una cascada con la formula de Friis, cifra de ruido, efecto de las perdidas antes del LNA, desadaptacion y metodo del factor Y.

Datos: constante de Boltzmann k = 1.380649e-23 J/K (exacta, NIST CODATA 2022, tabla allascii.txt, consultada el 2026-11-09). Las temperaturas y ganancias de los cuatro bloques (LNA 10 K y 30 dB, filtro 1 dB,
mezclador 7 dB, amplificador de FI 100 K y 25 dB), la temperatura de referencia de 290 K, el ancho de banda de 100 MHz, las cargas caliente (300 K) y fria (77 K) y la semilla 20261109 son ILUSTRATIVOS;
no describen ningun componente ni receptor real.
Modelo: Friis, T_cas = T1 + T2/G1 + T3/(G1 G2) + ...; cifra de ruido F = 1 + T/T0, NF = 10 log10 F; un elemento pasivo con perdida L a temperatura fisica T_f tiene T_e = (L - 1) T_f y ganancia 1/L. Segunda via:
metodo del factor Y simulado con muestras gaussianas de potencia proporcional a k B (T_carga + T_rec); T_rec = (T_h - Y T_c)/(Y - 1) con Y = P_h/P_c.
Supuestos: etapas lineales, adaptadas, ruido blanco, ganancias independientes de la frecuencia en la banda. Validez: banda estrecha. La desadaptacion usa la aproximacion T_rec/(1 - |Gamma|^2).
Tolerancia: Friis frente al calculo etapa a etapa con factores de ruido a 1e-9; temperatura del receptor recuperada con el factor Y frente a la de Friis a 5 % (1,2 millones de muestras por carga; la dispersion estadistica esperada es de unos 1,6 %).
"""
from __future__ import annotations
import math, platform, random

K = 1.380649e-23
T0 = 290.0


def db(x):
    return 10 ** (x / 10)


def friis(etapas):
    """etapas: lista de (Te, G lineal). Devuelve temperatura en la entrada."""
    t = 0.0
    g = 1.0
    for te, ga in etapas:
        t += te / g
        g *= ga
    return t


def friis_f(etapas):
    f = 0.0
    g = 1.0
    for i, (te, ga) in enumerate(etapas):
        fi = 1 + te / T0
        f += fi if i == 0 else (fi - 1) / g
        g *= ga
    return f


def pasivo(perdida_db, tf=T0):
    L = db(perdida_db)
    return ((L - 1) * tf, 1 / L)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    lna = (10.0, db(30))
    filt = pasivo(1.0)
    mez = pasivo(7.0)
    fi = (100.0, db(25))
    cadena = [lna, filt, mez, fi]
    t_f = friis(cadena)
    f_f = friis_f(cadena)
    print(f"Bloques (Te, G): LNA {lna[0]} K, 30 dB ; filtro {filt[0]:.2f} K, -1 dB ; mezclador {mez[0]:.1f} K, -7 dB ; FI {fi[0]} K, 25 dB")
    print(f"Friis: T_cas = {t_f:.4f} K ; F = 1 + T/T0 = {1 + t_f / T0:.5f} ; NF = {10 * math.log10(1 + t_f / T0):.4f} dB")
    print(f"Friis con factores de ruido: F_cas = {f_f:.5f} ; T = (F - 1) T0 = {(f_f - 1) * T0:.4f} K")
    assert abs((f_f - 1) * T0 / t_f - 1) < 1e-9
    print(f"{'etapa':>10} {'aporte a T_cas (K)':>20} {'porcentaje':>11}")
    g = 1.0
    nombres = ["LNA", "filtro", "mezclador", "FI"]
    for nom, (te, ga) in zip(nombres, cadena):
        ap = te / g
        print(f"{nom:>10} {ap:20.4f} {100 * ap / t_f:11.3f}")
        g *= ga
    # perdida antes del LNA
    print("Perdida pasiva (a 290 K) colocada ANTES del LNA:")
    print(f"{'perdida (dB)':>13} {'T_cas (K)':>10} {'NF (dB)':>8}")
    base = [lna, filt, mez, fi]
    for ld in (0.0, 0.1, 0.5, 1.0):
        cad = ([pasivo(ld)] if ld > 0 else []) + base
        t = friis(cad)
        print(f"{ld:13.1f} {t:10.3f} {10 * math.log10(1 + t / T0):8.3f}")
    t_ant = friis([pasivo(0.5)] + base)
    assert abs(t_ant - (friis([pasivo(0.5)]) + (1 / (1 / db(0.5))) * 0 + db(0.5) * t_f)) < 1e-9
    # desadaptacion
    print("Desadaptacion de entrada del LNA (T_rec/(1 - |Gamma|^2), aproximacion):")
    for gm in (0.0, 0.1, 0.3, 0.5):
        print(f"  |Gamma| = {gm:.1f} -> T_rec = {t_f / (1 - gm * gm):.3f} K")
    # factor Y
    rng = random.Random(20261109)
    th, tc = 300.0, 77.0
    B = 100e6
    n = 1_200_000
    def potencia(tcarga):
        var = tcarga + t_f
        s = 0.0
        for _ in range(n):
            x = rng.gauss(0, 1)
            s += x * x
        return var * s / n
    ph, pc = potencia(th), potencia(tc)
    y = ph / pc
    trec = (th - y * tc) / (y - 1)
    print(f"Factor Y: Y = {y:.5f} ; T_rec recuperada = {trec:.3f} K ; Friis = {t_f:.3f} K ; dif = {abs(trec / t_f - 1) * 100:.2f} % ; potencia de ruido k B T_cas = {K * B * t_f:.3e} W")
    assert abs(trec / t_f - 1) < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
