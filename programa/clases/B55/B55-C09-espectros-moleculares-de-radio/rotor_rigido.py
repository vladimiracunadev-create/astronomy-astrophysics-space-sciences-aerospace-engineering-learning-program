#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C09: espectro de rotacion de una molecula lineal (rotor rigido y rotor con distorsion centrifuga) frente al catalogo JPL.

Datos (OBSERVADOS en laboratorio, via catalogo JPL; consultados el 2026-11-09): frecuencias de las lineas J+1 -> J del CO (etiqueta 28001, version 4,
ago. 1997, https://spec.jpl.nasa.gov/ftp/pub/catalog/c028001.cat y doc/d028001.cat) y B = 57635.968 MHz de su documentacion; tres componentes hiperfinas de HCN J=1-0
(etiqueta 27001, version 2, ene. 1984). Energias del nivel inferior en cm-1 tomadas de la columna correspondiente del archivo.
Unidades del catalogo: frecuencia en MHz; E_inferior en cm-1. Constantes: h, c y k_B tienen valor exacto en el SI (2019), por lo que hc/k = 1.438776877... cm K es exacto.
Modelo: nu(J+1 -> J) = 2 B (J+1) (rotor rigido) ; nu = 2 B (J+1) - 4 D (J+1)^3 (con distorsion centrifuga, D ajustada por minimos cuadrados con las lineas del catalogo).
Poblacion de Boltzmann del nivel J: g_J exp(-E_J / kT), g_J = 2J+1. Velocidad Doppler: v = c (nu0 - nu)/nu0.
Supuestos: molecula lineal 1 Sigma, sin estructura fina ni hiperfina (salvo HCN); equilibrio termodinamico local. Validez: niveles bajos.
Tolerancia: rotor rigido vs catalogo 1e-3 relativo para J_sup <= 4; con distorsion 1e-6 relativo para J_sup <= 8.
"""
from __future__ import annotations
import math, platform

C_KMS = 299792.458            # km/s, exacto (definicion del metro)
HC_K = 1.438776877            # cm K  (= h c / k_B, SI 2019; 1.438776877...)

# CO (JPL 28001 v4): (J_sup, frecuencia MHz, E_inferior cm-1)
CO = [(1, 115271.2018, 0.0), (2, 230538.0000, 3.8450), (3, 345795.9899, 11.5350), (4, 461040.7682, 23.0695),
      (5, 576267.9305, 38.4481), (6, 691473.0763, 57.6704), (7, 806651.8060, 80.7354), (8, 921799.7000, 107.6424)]
B_CO = 57635.968          # MHz (documentacion JPL 28001)
# HCN J=1-0 hiperfina (JPL 27001 v2): frecuencia MHz y degeneracion
HCN = [(88630.4160, 3), (88631.8470, 5), (88633.9360, 1)]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("A. CO: catalogo JPL (OBSERVADO en laboratorio) frente al rotor rigido 2B J_sup")
    print("J_sup   catalogo [MHz]    rotor rigido [MHz]   dif relativa")
    for j, f, _ in CO:
        rr = 2.0 * B_CO * j
        print(f"{j:5d}   {f:14.4f}    {rr:14.4f}      {abs(rr - f) / f:.3e}")
        if j <= 4:
            assert abs(rr - f) / f < 1e-3
    # ajuste de D por minimos cuadrados: f = 2 B j - 4 D j^3  => (2 B j - f) = 4 D j^3
    num = sum((2 * B_CO * j - f) * 4 * j ** 3 for j, f, _ in CO)
    den = sum((4 * j ** 3) ** 2 for j, f, _ in CO)
    D = num / den
    print(f"B. Ajuste de D (minimos cuadrados con 8 lineas): D = {D * 1e3:.4f} kHz")
    print("J_sup   catalogo [MHz]    2BJ - 4DJ^3 [MHz]   dif relativa")
    for j, f, _ in CO:
        m = 2 * B_CO * j - 4 * D * j ** 3
        e = abs(m - f) / f
        print(f"{j:5d}   {f:14.4f}    {m:14.4f}        {e:.3e}")
        assert e < 1e-6, (j, e)
    # HCN: centro ponderado
    g = sum(w for _, w in HCN)
    fc = sum(f * w for f, w in HCN) / g
    print(f"C. HCN J=1-0: tres componentes hiperfinas {HCN[0][0]:.3f}, {HCN[1][0]:.3f}, {HCN[2][0]:.3f} MHz ; centro ponderado = {fc:.4f} MHz ; separacion total = {HCN[2][0] - HCN[0][0]:.3f} MHz = {(HCN[2][0] - HCN[0][0]) / fc * C_KMS:.2f} km/s")
    # Doppler
    nu0 = CO[0][1]
    print("D. Velocidad Doppler de la linea CO 1-0 para frecuencias observadas (SINTETICAS)")
    print("nu_obs [MHz]    v [km/s]")
    for v in (-10.0, 0.0, 5.0, 30.0):
        nu = nu0 * (1.0 - v / C_KMS)
        v_rec = C_KMS * (nu0 - nu) / nu0
        assert abs(v_rec - v) < 1e-9
        print(f"{nu:12.4f}   {v_rec:8.3f}")
    # Boltzmann: J de mayor poblacion
    print("E. Nivel de rotacion mas poblado del CO segun Boltzmann (g = 2J+1, E = B hc J(J+1), B calculado de la documentacion JPL)")
    b_cm = B_CO * 1e6 / (C_KMS * 1e5)          # B en cm-1 (MHz -> Hz / (cm/s))
    print(f"   B = {b_cm:.5f} cm-1")
    print("T [K]   J mas poblado (numerico)   J analitico sqrt(kT/(2 B hc)) - 1/2")
    for T in (10.0, 30.0, 100.0, 300.0):
        pob = [(2 * j + 1) * math.exp(-b_cm * j * (j + 1) * HC_K / T) for j in range(0, 60)]
        jn = max(range(len(pob)), key=pob.__getitem__)
        ja = math.sqrt(T / (2.0 * b_cm * HC_K)) - 0.5
        print(f"{T:5.0f}   {jn:8d}                {ja:8.2f}")
        assert abs(jn - ja) <= 1.0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
