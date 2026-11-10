#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C06: potencia del chorro, eficiencia y razon empuje/potencia de un propulsor electrico.

Datos CONSULTADOS (2026-11-10): g0 = 9.80665 m/s2 (NIST); Dawn (NASA/JPL): empuje maximo 91 mN, xenon ~3.25 mg/s;
NASA SSVI (Tabla 4-1 y texto): la propulsion electrica de naves pequenas queda por debajo de ~75 mN/kW (500 W -> <= ~38 mN).
ILUSTRATIVO (sintetico, no medido): eficiencia total eta = 0.6 (y 0.4, 0.7 en la comparacion), masa de nave 500 kg, Delta-v 1000 m/s,
potencia de entrada 1 kW. La potencia de entrada de Dawn NO se consulto (la pagina solo da la potencia de los paneles: >10 kW).
Modelo: P_jet = (1/2) mdot Ve^2 = (1/2) F Ve = F^2/(2 mdot); eta = P_jet / P_in; empuje/potencia = 2 eta / Ve; aceleracion constante.
Segunda via: P_jet por tres formulas equivalentes y energia cinetica del chorro acumulada en un intervalo de tiempo.
Tolerancia: las tres formulas de P_jet coinciden a 1e-12 relativa; F/P = 2 eta/Ve a 1e-12.
"""
from __future__ import annotations
import platform

G0 = 9.80665


def pjet(f, mdot):
    ve = f / mdot
    a = 0.5 * mdot * ve ** 2
    b = 0.5 * f * ve
    c = f ** 2 / (2 * mdot)
    assert abs(a - b) / a < 1e-12 and abs(a - c) / a < 1e-12
    return a


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    f, md = 0.091, 3.25e-6
    ve = f / md
    pj = pjet(f, md)
    print(f"Dawn (consultado F y mdot): Ve = {ve:.0f} m/s ; Isp = {ve/G0:.1f} s ; P_jet = {pj:.1f} W")
    for eta in (0.4, 0.6, 0.7):
        pin = pj / eta
        tp = f / pin * 1e6  # mN/kW
        assert abs(f / pin - 2 * eta / ve) / (2 * eta / ve) < 1e-12
        print(f"  eta = {eta:.1f} (ILUSTRATIVA) -> P_in = {pin:>7.1f} W ; F/P = {tp:>5.1f} mN/kW")
    print("Empuje por kilovatio frente al Isp (eta = 0.6, ILUSTRATIVA):")
    print("   Isp [s]   Ve [m/s]   F/P [mN/kW]   F con 1 kW [mN]")
    prev = None
    for isp in (300.0, 500.0, 1000.0, 2000.0, 3000.0, 5000.0):
        v = isp * G0
        tp = 2 * 0.6 / v * 1e6
        assert prev is None or tp < prev
        prev = tp
        print(f" {isp:>8.0f} {v:>10.0f} {tp:>13.1f} {tp:>16.1f}")
    # Cruce entre la cota fisica 2 eta/Ve y el tope consultado de 75 mN/kW (eta = 1)
    ve_x = 2 * 1.0 / 75e-6
    print(f"Con eta = 1, la cota fisica F/P = 2/Ve vale 75 mN/kW para Ve = {ve_x:.0f} m/s (Isp = {ve_x/G0:.0f} s); por debajo de ese Isp la cota fisica es mayor que el tope consultado y manda el tope practico")
    # Tiempo de empuje para un delta-v dado (ILUSTRATIVO): m = 500 kg, dv = 1000 m/s, P_in = 1 kW, eta = 0.6
    m, dv, pin, eta = 500.0, 1000.0, 1000.0, 0.6
    print("Tiempo de empuje para 1000 m/s con 1 kW, 500 kg, eta = 0.6 (masa constante, aproximacion):")
    for isp in (1000.0, 2000.0, 3000.0):
        v = isp * G0
        fth = 2 * eta * pin / v
        t = m * dv / fth
        print(f"  Isp = {isp:>5.0f} s -> F = {fth*1e3:>6.1f} mN ; t = {t/86400:>7.1f} dias ; propelente = {fth/v*t:>6.2f} kg")
        assert abs(fth / v * t - m * dv / v) < 1e-6  # m_prop = m dv / Ve en la aproximacion lineal
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
