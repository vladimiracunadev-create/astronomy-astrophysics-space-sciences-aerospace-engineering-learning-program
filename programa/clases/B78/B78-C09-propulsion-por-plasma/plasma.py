#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C09: parametros de un plasma de propulsion y expansion en una tobera magnetica (conceptual).

Datos CONSULTADOS (2026-11-10): e, eps0 = 8.8541878188e-12 F/m, m_e = 9.1093837139e-31 kg, u = 1.66053906892e-27 kg, g0 (NIST CODATA);
rango de los propulsores de plasma pulsados y de arco de vacio de naves pequenas: 4-500 uN y 87-3200 s (NASA SSVI, Tabla 4-1).
NO CONSULTADO: masa atomica del xenon 131.293.
ILUSTRATIVOS (sinteticos, no de un dispositivo real): densidad n = 1e18 m^-3, temperatura electronica Te = 5 eV (iones frios),
longitud del plasma 0.1 m, cociente de densidades en la tobera 1e-3, caudal de iones 1 mg/s.
Modelo: plasma de un solo ion (Xe+), electrones isotermos; longitud de Debye, frecuencia de plasma; velocidad de Bohm cs = sqrt(e Te/m_i);
en la tobera: (1/2) m v^2 = (1/2) m cs^2 + e Te ln(n0/n) con flujo conservado n v A = const.
Segunda via: cota adiabatica (sin aporte de calor) de conversion total de la entalpia electronica, (1/2) m v^2 = (5/2) e Te; integracion numerica de dv/dn.
Tolerancia: velocidad analitica frente a la integral numerica < 1e-6 relativa.
"""
from __future__ import annotations
import math, platform

E = 1.602176634e-19
EPS0 = 8.8541878188e-12
ME = 9.1093837139e-31
U = 1.66053906892e-27
G0 = 9.80665
MI = 131.293 * U


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n, te, L = 1e18, 5.0, 0.1
    kte = E * te
    debye = math.sqrt(EPS0 * kte / (n * E ** 2))
    wpe = math.sqrt(n * E ** 2 / (EPS0 * ME))
    wpi = math.sqrt(n * E ** 2 / (EPS0 * MI))
    nd = n * (4 / 3) * math.pi * debye ** 3
    cs = math.sqrt(kte / MI)
    print(f"Plasma ILUSTRATIVO: n = {n:.0e} m^-3, Te = {te:.0f} eV")
    print(f"  longitud de Debye = {debye*1e6:.2f} um ; N_D (particulas en la esfera de Debye) = {nd:.0f} ; L/lambda_D = {L/debye:.0f}")
    print(f"  frecuencia de plasma electronica = {wpe:.3e} rad/s ; ionica = {wpi:.3e} rad/s ; cociente = {wpe/wpi:.1f}")
    assert abs(wpe / wpi - math.sqrt(MI / ME)) < 1e-9 * wpe / wpi
    assert debye < L / 100 and nd > 1
    print(f"  velocidad de Bohm cs = {cs:.0f} m/s")
    # Tobera magnetica isoterma
    razon = 1e-3
    v_an = cs * math.sqrt(1 + 2 * math.log(1 / razon))
    # integral numerica de v dv = -cs^2 dn/n  -> v^2/2 - cs^2/2 = cs^2 ln(n0/n)
    pasos = 200000
    v2 = cs ** 2
    ln_total = math.log(1 / razon)
    d = ln_total / pasos
    for _ in range(pasos):
        v2 += 2 * cs ** 2 * d
    v_num = math.sqrt(v2)
    assert abs(v_an - v_num) / v_an < 1e-6
    print(f"Tobera magnetica isoterma, n/n0 = {razon:.0e}: v = {v_an:.0f} m/s ({v_an/G0:.0f} s) ; numerica = {v_num:.0f} m/s")
    mach = v_an / cs
    area = (1 / razon) * (1 / mach)  # n v A = n0 cs A0
    print(f"  Mach ionico = {mach:.2f} ; razon de areas A/A0 = n0 cs/(n v) = {area:.1f}")
    cota = math.sqrt(5 * kte / MI)
    print(f"Cota ADIABATICA (sin aporte de calor): conversion total de la entalpia electronica, v = sqrt(5 e Te/m_i) = {cota:.0f} m/s ({cota/G0:.0f} s)")
    print(f"La expansion isoterma supera esa cota en un factor {v_an/cota:.3f} porque supone que los electrones reciben calor de un reservorio: es una idealizacion optimista")
    assert v_an > cota
    mdot = 1e-6
    F = mdot * v_an
    P = 0.5 * mdot * v_an ** 2
    print(f"Con 1 mg/s de iones ILUSTRATIVO: F = {F*1e3:.2f} mN ; potencia del chorro = {P:.1f} W")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
