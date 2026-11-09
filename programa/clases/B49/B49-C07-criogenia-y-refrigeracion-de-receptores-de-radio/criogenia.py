#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C07: ruido de Johnson, temperatura de un receptor enfriado y balance termico de un criostato.

Datos: k = 1.380649e-23 J/K, h = 6.62607015e-34 J s, c = 299792458 m/s y sigma = 5.670374419e-8 W m^-2 K^-4 (NIST, CODATA 2022, tabla allascii.txt, consultada el 2026-11-09). Todo lo demas es ILUSTRATIVO
y no describe ningun criostato, amplificador ni refrigerador real: la ley T_LNA = 4 K + 0,15 T_fisica, la perdida de alimentador de 0,3 dB, los 2,2 K del resto de la cadena, las areas, emisividades, capas
de aislante y conductividad de los soportes, y las capacidades de la cabeza fria.
Modelo: ruido termico disponible P = k T B (densidad -173,98 dBm/Hz a 290 K) y tension cuadratica media 4 k T R B; temperatura del receptor T_rec = (L-1) T_f + L (T_LNA(T_f) + T_resto) con L la perdida del
alimentador a la temperatura T_f; carga por radiacion Q = sigma eps A (T_c^4 - T_f^4)/(N+1) con N capas de aislante multicapa; carga por conduccion Q = n k A (T_c - T_f)/l con conductividad media constante; potencia
minima de Carnot W = Q (T_c - T_f)/T_f. Comprobacion independiente de sigma: 2 pi^5 k^4/(15 h^3 c^2).
Supuestos: conductividad constante (en la realidad depende de T), contacto termico perfecto, sin carga de cableado ni de ventana. Validez: orden de magnitud para dimensionar; no sustituye al calculo de diseno.
Tolerancia: sigma calculada frente a la de NIST a 1e-9 relativo; densidad de ruido a 290 K frente a -173,98 dBm/Hz a 0,01 dB; margen de potencia frigorifica positivo en ambas etapas.
"""
from __future__ import annotations
import math, platform

K = 1.380649e-23
H = 6.62607015e-34
C = 299792458.0
SIG_NIST = 5.670374419e-8


def db(x):
    return 10 ** (x / 10)


def t_lna(tf):
    return 4.0 + 0.15 * tf


def t_rec(tf, perdida_db=0.3, resto=2.2):
    L = db(perdida_db)
    return (L - 1) * tf + L * (t_lna(tf) + resto)


def rad(eps, area, tc, tf, capas):
    return SIG_NIST * eps * area * (tc ** 4 - tf ** 4) / (capas + 1)


def cond(n, kk, area, long, tc, tf):
    return n * kk * area * (tc - tf) / long


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    sig = 2 * math.pi ** 5 * K ** 4 / (15 * H ** 3 * C ** 2)
    print(f"sigma calculada = {sig:.9e} W m^-2 K^-4 ; NIST = {SIG_NIST:.9e} ; dif relativa = {abs(sig / SIG_NIST - 1):.1e}")
    assert abs(sig / SIG_NIST - 1) < 1e-9
    dens = 10 * math.log10(K * 290 * 1000)
    print(f"Densidad de ruido disponible k T a 290 K = {K * 290:.4e} W/Hz = {dens:.3f} dBm/Hz")
    assert abs(dens + 173.98) < 0.01
    R, B = 50.0, 100e6
    for T in (290.0, 77.0, 15.0):
        print(f"  T = {T:5.0f} K: tension rms de Johnson (R = 50 ohm, B = 100 MHz) = {math.sqrt(4 * K * T * R * B) * 1e6:.3f} microvoltios ; k T B = {K * T * B:.3e} W")
    print(f"{'T fisica (K)':>13} {'T_LNA (K)':>10} {'T_rec (K)':>10} {'mejora':>8}")
    base = t_rec(290.0)
    for tf in (290.0, 77.0, 40.0, 15.0, 4.0):
        tr = t_rec(tf)
        print(f"{tf:13.0f} {t_lna(tf):10.2f} {tr:10.2f} {base / tr:8.2f}")
    assert t_rec(15.0) < t_rec(77.0) < t_rec(290.0)
    # balance termico: etapa de 40 K y etapa de 15 K
    q1_rad = rad(0.05, 0.5, 300.0, 40.0, 10)
    q1_cond = cond(4, 0.4, 2e-4, 0.1, 300.0, 40.0)
    q2_rad = rad(0.05, 0.3, 40.0, 15.0, 10)
    q2_cond = cond(4, 0.4, 2e-4, 0.1, 40.0, 15.0)
    q1 = q1_rad + q1_cond + 2.0     # 2 W de disipacion ilustrativa de electronica en la etapa de 40 K
    q2 = q2_rad + q2_cond + 0.5     # 0,5 W de disipacion del LNA y cableado en la etapa de 15 K
    cap1, cap2 = 40.0, 1.0
    print(f"Etapa de 40 K: radiacion {q1_rad:.3f} W + conduccion {q1_cond:.3f} W + electronica 2,000 W = {q1:.3f} W ; capacidad {cap1} W ; margen {cap1 - q1:.3f} W")
    print(f"Etapa de 15 K: radiacion {q2_rad:.5f} W + conduccion {q2_cond:.3f} W + electronica 0,500 W = {q2:.3f} W ; capacidad {cap2} W ; margen {cap2 - q2:.3f} W")
    assert cap1 - q1 > 0 and cap2 - q2 > 0
    print("Capas de aislante multicapa y radiacion de la etapa de 40 K:")
    for n in (0, 5, 10, 30):
        print(f"  N = {n:2d}: {rad(0.05, 0.5, 300.0, 40.0, n):.4f} W")
    for tf, q in ((40.0, q1), (15.0, q2)):
        print(f"Carnot para extraer {q:.3f} W a {tf:.0f} K desde 300 K: W_min = {q * (300 - tf) / tf:.2f} W")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
