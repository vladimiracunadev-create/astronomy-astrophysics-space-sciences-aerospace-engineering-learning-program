#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C20: dimensionado preliminar de la estructura de una plataforma de microsatelite de 100 kg.

Datos CONSULTADOS (2026-11-10): GEVS (GSFC-STD-7000B), Tabla 2.2-3 (metalico estatico: fluencia 1,25 y ultima 1,4) y gn = 9,80665 m/s2 (NIST).
DATOS ILUSTRATIVOS (no consultados): masa total 100 kg, cuerpo cuadrado de lado a = 0,60 m y altura L = 0,50 m; cuatro paneles laterales sandwich de aluminio
(pieles de 0,5 mm, nucleo de panal de 20 mm y 50 kg/m3; E = 69 GPa, nu = 0,33, rho = 2700 kg/m3; resistencia de piel 275 MPa fluencia, 310 MPa ultima);
ANILLO/tubo central de aluminio: caja delgada de lado 0,30 m y espesor 2,0 mm; carga de diseno cuasiestatica 30 g (inventada, NO de un lanzador);
requisito ILUSTRATIVO de frecuencia fundamental lateral >= 25 Hz y de panel >= 100 Hz.
Modelo: (1) panel sandwich simplemente apoyado: D = E t_f d^2/(2(1-nu^2)) con d = h + t_f; masa por area m'' = 2 t_f rho + h rho_n; f11 = (pi/2) sqrt(D/m'')(1/a^2 + 1/b^2).
(2) tension de piel bajo presion equivalente q = m_eq N g/a^2: M = 0,0479 q a^2 (placa cuadrada simplemente apoyada, centro) y sigma = M/(t_f d).
(3) frecuencia lateral del cuerpo: voladizo con masa en el extremo: f = (1/2pi) sqrt(3 E I/((m + 0,2357 m_t) L^3)), I = (2/3) t a_t^3 (tubo de caja delgada).
(4) balance de masa. Segunda via de (1): f11 de la formula de la placa de Navier comparada con el modelo de viga de ancho unitario (misma D y masa): f = (pi/2) sqrt(D/m'')(2/a^2) para a = b.
Tolerancia: las dos expresiones de f11 deben coincidir a 1e-12 (son la misma formula para a = b; es un control de codigo).
"""
from __future__ import annotations
import math, platform

G = 9.80665
E, NU, RHO = 69e9, 0.33, 2700.0
TF, H, RN = 0.5e-3, 20e-3, 50.0
A_PAN = 0.60
FSY, FSU = 1.25, 1.4
SY, SU = 275e6, 310e6
N_G = 30.0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    d = H + TF
    Dr = E * TF * d ** 2 / (2 * (1 - NU ** 2))
    mpp = 2 * TF * RHO + H * RN
    f11 = math.pi / 2 * math.sqrt(Dr / mpp) * (2 / A_PAN ** 2)
    f11_b = math.pi / 2 * math.sqrt(Dr / mpp) * (1 / A_PAN ** 2 + 1 / A_PAN ** 2)
    print("Panel sandwich ILUSTRATIVO 0,60 x 0,60 m: pieles 0,5 mm, nucleo 20 mm")
    print(f"Rigidez a flexion D = {Dr:.1f} N m ; masa por area = {mpp:.3f} kg/m2 ; masa del panel = {mpp * A_PAN ** 2:.3f} kg")
    print(f"Frecuencia fundamental del panel simplemente apoyado f11 = {f11:.1f} Hz (requisito ilustrativo >= 100 Hz: {'cumple' if f11 >= 100 else 'NO cumple'})")
    # tension de piel con 8 kg de equipo distribuido (ilustrativo)
    m_eq = 8.0
    q = (m_eq + mpp * A_PAN ** 2) * N_G * G / A_PAN ** 2
    M = 0.0479 * q * A_PAN ** 2
    sig = M / (TF * d)
    ms_y = SY / (FSY * sig) - 1
    ms_u = SU / (FSU * sig) - 1
    print(f"Presion equivalente a {N_G:.0f} g con 8 kg de equipo: q = {q:.0f} Pa ; M = {M:.2f} N m/m ; tension de piel = {sig / 1e6:.2f} MPa")
    print(f"Margenes de piel: fluencia = {SY / 1e6:.0f}/({FSY} x {sig / 1e6:.2f}) - 1 = {ms_y:.2f} ; ultima = {ms_u:.2f}")
    # cuerpo
    at, tt = 0.30, 2.0e-3
    L = 0.50
    I = 2 / 3 * tt * at ** 3
    m_tubo = 4 * at * L * tt * RHO
    m_paneles = 4 * mpp * A_PAN * L
    m_tot = 100.0
    m_vivo = m_tot - m_tubo - m_paneles
    f_lat = math.sqrt(3 * E * I / ((m_tot - 0.2357 * m_tubo) * L ** 3)) / (2 * math.pi)
    print(f"Tubo central caja 0,30 m x 2 mm, L = 0,50 m: I = {I * 1e8:.2f} cm4 ; masa = {m_tubo:.2f} kg")
    print(f"Paneles laterales (4 de 0,60 x 0,50 m): masa = {m_paneles:.2f} kg")
    print(f"Balance de masa: estructura = {m_tubo + m_paneles:.2f} kg ({(m_tubo + m_paneles) / m_tot * 100:.1f} % de 100 kg) ; resto = {m_vivo:.2f} kg")
    print(f"Frecuencia lateral del cuerpo (voladizo con masa en el extremo): f = {f_lat:.1f} Hz (requisito ilustrativo >= 25 Hz: {'cumple' if f_lat >= 25 else 'NO cumple'})")
    # Barrido del espesor de piel
    print("Barrido del espesor de piel del panel:")
    for t in (0.3e-3, 0.5e-3, 0.8e-3, 1.0e-3):
        dd = H + t
        D2 = E * t * dd ** 2 / (2 * (1 - NU ** 2))
        m2 = 2 * t * RHO + H * RN
        ff = math.pi / 2 * math.sqrt(D2 / m2) * (2 / A_PAN ** 2)
        print(f"  t_f = {t * 1e3:.1f} mm  m'' = {m2:.3f} kg/m2  f11 = {ff:6.1f} Hz")
    assert abs(f11 - f11_b) < 1e-12
    assert ms_y > 0 and ms_u > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
