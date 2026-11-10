#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C02: Delta-v de una etapa quimica (ecuacion del cohete) como sistema con masas.

Datos CONSULTADOS (2026-11-10): g0 = 9.80665 m/s2 (NIST); rangos de Isp de la Tabla 4-1 del estado del arte de propulsion
para naves pequenas (NASA SSVI): hidracina monopropelente 180-285 s (clase de 1 N: ~200-235 s).
ILUSTRATIVO (sintetico): fraccion de tanques = 12 % de la masa de propelente,
masa fija de motor y valvulas = 20 kg, carga util 150 kg, Isp = 220 s (dentro del rango consultado).
Modelo: Tsiolkovsky dv = Isp g0 ln(m0/mf), empuje impulsivo, sin perdidas gravitatorias ni de direccion.
Segunda via: integracion numerica de dv = Ve * dm/m con pasos finitos.
Tolerancia: integral numerica frente a la formula analitica < 1e-6 relativa con 200000 pasos.
"""
from __future__ import annotations
import math, platform

G0 = 9.80665


def dv(isp, m0, mf):
    return isp * G0 * math.log(m0 / mf)


def dv_numerico(isp, m0, mf, n=200000):
    ve = isp * G0
    m = m0
    dm = (m0 - mf) / n
    v = 0.0
    for _ in range(n):
        v += ve * dm / (m - 0.5 * dm)  # punto medio
        m -= dm
    return v


def masas(m_prop, m_util=150.0, m_motor=20.0, k_tanque=0.12):
    m_tanque = k_tanque * m_prop
    mf = m_util + m_motor + m_tanque
    return mf + m_prop, mf, m_tanque


def propelente_para(dv_obj, isp, m_util=150.0, m_motor=20.0, k_tanque=0.12):
    # m0/mf = exp(dv/ve); m0 = mf + mp; mf = fijo + k mp  -> mp = (R-1) fijo / (1 - k (R-1))
    r = math.exp(dv_obj / (isp * G0))
    fijo = m_util + m_motor
    den = 1.0 - k_tanque * (r - 1.0)
    if den <= 0:
        raise ValueError("Delta-v inalcanzable con esta fraccion de tanques")
    return (r - 1.0) * fijo / den


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    isp = 220.0
    print(f"Etapa ILUSTRATIVA: Isp = {isp:.0f} s (rango consultado 180-285 s), carga util 150 kg, motor 20 kg, tanques 12 % del propelente")
    print(" m_prop [kg]   m0 [kg]   mf [kg]   m0/mf    dv [m/s]  dv numerico [m/s]")
    for mp in (100.0, 300.0, 600.0, 1000.0):
        m0, mf, _ = masas(mp)
        a, b = dv(isp, m0, mf), dv_numerico(isp, m0, mf)
        print(f" {mp:>10.0f} {m0:>9.1f} {mf:>9.1f} {m0/mf:>8.4f} {a:>11.2f} {b:>11.2f}")
        assert abs(a - b) / a < 1e-6
    print("Propelente necesario para un delta-v objetivo (misma etapa):")
    for obj in (500.0, 1000.0, 1500.0, 2000.0):
        mp = propelente_para(obj, isp)
        m0, mf, _ = masas(mp)
        assert abs(dv(isp, m0, mf) - obj) < 1e-6
        print(f"  dv = {obj:>6.0f} m/s -> m_prop = {mp:>8.2f} kg ; m0 = {m0:>8.2f} kg ; fraccion de propelente = {mp/m0:.3f}")
    # Cota: con tanques de 12 % el delta-v maximo para cualquier cantidad de propelente
    ve = isp * G0
    cota = ve * math.log(1.12 / 0.12)
    print(f"Cota con tanques de 12 %: dv < Ve ln((1+k)/k) = {cota:.1f} m/s (aunque m_prop -> infinito)")
    try:
        propelente_para(cota * 1.01, isp)
    except ValueError:
        print("Un objetivo 1 % por encima de la cota se rechaza (inalcanzable).")
    # Sensibilidad al Isp dentro del rango consultado
    for i in (180.0, 220.0, 285.0):
        print(f"  Isp = {i:>5.0f} s -> propelente para 1000 m/s = {propelente_para(1000.0, i):.2f} kg")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
