#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C01: empuje e impulso especifico.

Datos CONSULTADOS (2026-11-10):
  - g0 = 9.80665 m/s2 exacta (NIST CODATA).
  - Dawn (NASA/JPL, pagina de propulsion ionica): empuje maximo 91 mN por motor; xenon ~3.25 mg/s a empuje maximo.
  - Ecuacion de empuje F = mdot*Ve + Ae*(pe - p0) y definicion Isp = F/(mdot*g0) (NASA Glenn).
ILUSTRATIVO (sintetico, no medido): la tobera quimica (mdot = 100 kg/s, Ve = 3000 m/s, Ae = 2.0 m2, pe = 60 kPa) y las presiones ambiente.
Modelo: empuje unidimensional estacionario. Isp se define con el empuje total (velocidad equivalente Veq = F/mdot).
Segunda via: Isp = Veq/g0 y total de impulso por integracion numerica (regla del trapecio) frente a F*t.
Tolerancia: coincidencia relativa < 1e-9 entre las dos vias de Isp; integral numerica < 1e-9 frente al producto.
"""
from __future__ import annotations
import platform

G0 = 9.80665  # m/s2, exacta (NIST)


def empuje(mdot, ve, ae, pe, p0):
    return mdot * ve + ae * (pe - p0)


def isp(f, mdot):
    return f / (mdot * G0)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1) Dawn (consultado): F y mdot publicados -> Veq e Isp (NO es una medicion propia)
    f, md = 0.091, 3.25e-6
    veq = f / md
    print(f"Dawn (consultado): F = {f*1e3:.0f} mN, mdot = {md*1e6:.2f} mg/s -> Veq = {veq:.0f} m/s ; Isp = {isp(f, md):.1f} s")
    assert abs(isp(f, md) - veq / G0) / isp(f, md) < 1e-9
    # 2) Tobera quimica ILUSTRATIVA: efecto de la presion ambiente
    print("Tobera ILUSTRATIVA (mdot = 100 kg/s, Ve = 3000 m/s, Ae = 2.0 m2, pe = 60 kPa):")
    print(" ambiente        p0 [kPa]    F [kN]   Isp [s]")
    for nombre, p0 in (("nivel del mar", 101.325), ("alta atmosfera", 20.0), ("vacio", 0.0)):
        ff = empuje(100.0, 3000.0, 2.0, 60e3, p0 * 1e3)
        print(f" {nombre:<14} {p0:>9.3f} {ff/1e3:>9.1f} {isp(ff, 100.0):>9.1f}")
        assert abs(isp(ff, 100.0) - (ff / 100.0) / G0) < 1e-9
    # 3) Impulso total: integral numerica de un empuje constante frente a F*t
    ff = empuje(100.0, 3000.0, 2.0, 60e3, 0.0)
    n, t = 1000, 120.0
    dt = t / n
    # empuje que sube linealmente de 50 % a 100 % (ILUSTRATIVO): analitico = 0.75*ff*t
    fs = [ff * (0.5 + 0.5 * i / n) for i in range(n + 1)]
    integral = sum(0.5 * (fs[i] + fs[i + 1]) * dt for i in range(n))
    print(f"Impulso total (vacio, {t:.0f} s, rampa 50-100 %): numerico = {integral/1e6:.3f} MN s ; analitico 0.75*F*t = {0.75*ff*t/1e6:.3f} MN s")
    assert abs(integral - 0.75 * ff * t) / (0.75 * ff * t) < 1e-9
    # 4) Masa de propelente consumida y verificacion Isp -> mdot
    m_prop = 100.0 * t
    print(f"Propelente consumido en {t:.0f} s: {m_prop:.0f} kg ; mdot desde Isp = {ff/(isp(ff,100.0)*G0):.3f} kg/s")
    # 5) Dawn: xenon en un dia de empuje maximo
    print(f"Dawn: xenon por dia a empuje maximo = {md*86400*1e3:.1f} g ; impulso por dia = {f*86400:.0f} N s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
