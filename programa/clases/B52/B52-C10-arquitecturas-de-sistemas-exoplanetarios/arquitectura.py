#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C10: espaciado en radios de Hill mutuos y razones de periodos del Sistema Solar y de un sistema sintetico.

Datos consultados el 2026-11-09 (NASA/NSSDC, ficha de planetas, tabla metrica; la fila se rotula en la ficha «Distance from Sun»):
masa (1e24 kg), distancia al Sol (1e6 km) y periodo orbital (dias) de Mercurio a Neptuno:
Mercurio 0.330, 57.9, 88.0 ; Venus 4.87, 108.2, 224.7 ; Tierra 5.97, 149.6, 365.2 ; Marte 0.642, 228.0, 687.0 ;
Jupiter 1898, 778.5, 4331 ; Saturno 568, 1432.0, 10747 ; Urano 86.8, 2867.0, 30589 ; Neptuno 102, 4515.0, 59800.
(GM)_sol nominal de la IAU 2015 (Resolucion B3) y G de NIST (CODATA 2022), consultados el 2026-11-09.
Sistema SINTETICO (no observado): 5 planetas de 5 masas terrestres alrededor de 0.9 M_sol con espaciado constante de 12 radios de Hill mutuos,
primer semieje 0.05 ua. La ficha no da incertidumbres: se rotula.
Sistema de referencia: orbitas circulares coplanares aproximadas; SI.
Modelo: R_H,m = ((m1+m2)/(3 M*))^(1/3) (a1+a2)/2 ; Delta = (a2-a1)/R_H,m. Via 2: semieje de Kepler a partir del periodo con (GM)_sol frente a la distancia de la ficha.
Tolerancias: semieje de Kepler frente a la ficha < 1 %; recurrencia del sistema sintetico: espaciado reconstruido igual a 12 con 1e-9.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
GM = 1.3271244e20
MSOL = GM / G
UA = 1.495978707e11
DIA = 86400.0
PLANETAS = [("Mercurio", 0.330, 57.9, 88.0), ("Venus", 4.87, 108.2, 224.7), ("Tierra", 5.97, 149.6, 365.2), ("Marte", 0.642, 228.0, 687.0),
            ("Jupiter", 1898.0, 778.5, 4331.0), ("Saturno", 568.0, 1432.0, 10747.0), ("Urano", 86.8, 2867.0, 30589.0), ("Neptuno", 102.0, 4515.0, 59800.0)]
M_TIERRA = 5.97e24


def r_hill_mutuo(m1, m2, a1, a2, M):
    return ((m1 + m2) / (3.0 * M)) ** (1.0 / 3.0) * 0.5 * (a1 + a2)


def delta(m1, m2, a1, a2, M):
    return (a2 - a1) / r_hill_mutuo(m1, m2, a1, a2, M)


def calcular():
    kepler = []
    for nm, m, d, p in PLANETAS:
        a = (GM * (p * DIA) ** 2 / (4 * math.pi ** 2)) ** (1.0 / 3.0)
        kepler.append((nm, d * 1e9, a, a / (d * 1e9) - 1.0))
    pares = []
    for i in range(len(PLANETAS) - 1):
        n1, m1, d1, p1 = PLANETAS[i]
        n2, m2, d2, p2 = PLANETAS[i + 1]
        pares.append((n1, n2, delta(m1 * 1e24, m2 * 1e24, d1 * 1e9, d2 * 1e9, MSOL), p2 / p1))
    # sistema sintetico: se construye a_{k+1} a partir de Delta = 12 resolviendo (a2 - a1) = 12 R_H,m con biseccion
    Ms, m = 0.9 * MSOL, 5.0 * M_TIERRA
    a = [0.05 * UA]
    for _ in range(4):
        lo, hi = a[-1], a[-1] * 10
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if delta(m, m, a[-1], mid, Ms) < 12.0:
                lo = mid
            else:
                hi = mid
        a.append(0.5 * (lo + hi))
    per = [2 * math.pi * math.sqrt(x ** 3 / (G * Ms)) / DIA for x in a]
    recon = [delta(m, m, a[i], a[i + 1], Ms) for i in range(4)]
    return dict(kepler=kepler, pares=pares, sa=a, sp=per, sd=recon, razon=[per[i + 1] / per[i] for i in range(4)])


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print("Sistema Solar (ficha NASA/NSSDC, consulta 2026-11-09; sin incertidumbres en la ficha)")
    print(f"{'planeta':>9} {'dist. ficha [ua]':>17} {'a Kepler [ua]':>14} {'dif.':>9}")
    for nm, d, a, dd in r["kepler"]:
        print(f"{nm:>9} {d / UA:17.4f} {a / UA:14.4f} {dd:9.2e}")
    print(f"{'par':>20} {'Delta (R_H mutuos)':>19} {'P2/P1':>8}")
    for n1, n2, dl, rp in r["pares"]:
        print(f"{n1 + '-' + n2:>20} {dl:19.2f} {rp:8.3f}")
    print("Sistema SINTETICO (no observado): 5 planetas de 5 M_Tierra, 0.9 M_sol, Delta = 12")
    print("semiejes [ua]: " + " ".join(f"{x / UA:.5f}" for x in r["sa"]))
    print("periodos [d]: " + " ".join(f"{x:.3f}" for x in r["sp"]))
    print("razones de periodos: " + " ".join(f"{x:.4f}" for x in r["razon"]) + " ; Delta reconstruido: " + " ".join(f"{x:.9f}" for x in r["sd"]))
    assert all(abs(dd) < 0.01 for _, _, _, dd in r["kepler"])
    assert all(abs(x - 12.0) < 1e-9 for x in r["sd"])
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
