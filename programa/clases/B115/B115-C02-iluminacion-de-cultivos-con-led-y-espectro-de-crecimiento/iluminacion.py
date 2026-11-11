#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B115-C02: iluminacion LED de un cultivo: fotones, integral diaria de luz, eficacia, potencia y calor.

Datos CONSULTADOS (2026-11-10): eficacias de paquete LED a 25 C (rojo 4.5, azul 3.5, blanco 2.9 umol/J) y de luminaria
(blanco 2.7, rojo+blanco 3.4, azul+rojo 4.1 umol/J) de Kusuma et al. (2020); 200 umol m-2 s-1, 16 h de luz y relacion
12 rojo (630 nm) : 3 azul (455 nm) : 1 verde (530 nm) de Veggie en Khodadad et al. (2020); tabla de area por persona de
Wheeler (NASA/KSC, diapositivas): PPF 500 umol m-2 s-1, DLI 28.8 mol m-2 d-1, RUE 0.75 g/mol -> 31.5 m2.
ILUSTRATIVO: el rendimiento y la fraccion de PAR absorbida. Unidades: umol, mol, J, W, m2, h. Solo numpy y estandar.
Verificacion: la DLI se compara con la tabla de Wheeler; las eficacias de mezcla se comparan con las de luminaria de
Kusuma (el cociente luminaria/paquete debe estar entre 0.90 y 1.00).
"""
from __future__ import annotations
import platform
import numpy as np

NA, H_PLANCK, C_LUZ = 6.02214076e23, 6.62607015e-34, 299792458.0   # CODATA, exactos desde 2019 (no consultados aqui)


def energia_mol_fotones(lambda_nm):
    """Energia de un mol de fotones en kJ/mol."""
    return NA * H_PLANCK * C_LUZ / (lambda_nm * 1e-9) / 1000.0


def dli(ppfd, horas):
    return ppfd * horas * 3600.0 / 1e6


def eficacia_mezcla(fracciones, eficacias):
    """Eficacia de una mezcla por fotones: 1 / sum(f_i / eta_i), con f_i fraccion de fotones."""
    f = np.array(fracciones, float)
    f = f / f.sum()
    return 1.0 / float(np.sum(f / np.array(eficacias, float)))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: eficacias de Kusuma et al. (2020), luz de Veggie de Khodadad et al. (2020), tabla de Wheeler (NASA/KSC)")
    print("Energia de un mol de fotones")
    for nom, lam in (("azul 455 nm", 455), ("verde 530 nm", 530), ("rojo 630 nm", 630), ("rojo lejano 730 nm", 730)):
        print(f"   {nom:20s} {energia_mol_fotones(lam):7.1f} kJ/mol")

    d_wheeler = dli(500, 16)
    d_veggie = dli(200, 16)
    print(f"DLI con 500 umol/m2/s y 16 h = {d_wheeler:.2f} mol/m2/d (tabla de Wheeler: 28.8)")
    print(f"DLI con 200 umol/m2/s y 16 h = {d_veggie:.2f} mol/m2/d (Veggie segun Khodadad)")
    assert abs(d_wheeler - 28.8) < 1e-9

    print("Eficacia de mezcla (paquete) frente a luminaria publicada")
    casos = (("90 % rojo + 10 % azul (fotones)", (0.9, 0.1), (4.5, 3.5), 4.1),
             ("100 % blanco", (1.0,), (2.9,), 2.7),
             ("50 % rojo + 50 % blanco", (0.5, 0.5), (4.5, 2.9), 3.4))
    for nom, f, e, lum in casos:
        m = eficacia_mezcla(f, e)
        print(f"   {nom:34s} paquete = {m:.3f}  luminaria Kusuma = {lum:.1f}  cociente = {lum/m:.3f}")
        assert 0.90 <= lum / m <= 1.0
    mezcla_veggie = eficacia_mezcla((12, 3), (4.5, 3.5))
    print(f"   Rojo:azul 12:3 (sin el verde, cuya eficacia no se verifico) paquete = {mezcla_veggie:.3f} umol/J")

    print("Potencia electrica y calor para 1 m2 con PPFD de 200 y de 500 umol/m2/s (eficacia de luminaria 3.4 umol/J)")
    for ppfd in (200, 500):
        p_el = ppfd / 3.4
        e_dia = p_el * 16 / 1000
        e_mol = (12 * energia_mol_fotones(630) + 3 * energia_mol_fotones(455)) / 15   # kJ/mol, mezcla 12:3
        p_rad = ppfd * 1e-6 * e_mol * 1000                                         # W/m2 de energia radiante PAR
        almacenada = 0.75 * 15.6 / e_mol                                           # RUE 0.75 g/mol * 15.6 kJ/g (CH2O, ilustrativo)
        print(f"   PPFD {ppfd:3d}: potencia electrica = {p_el:6.1f} W/m2; PAR radiante = {p_rad:5.1f} W/m2 "
              f"({p_rad/p_el*100:.0f} % de la electrica); energia = {e_dia:.2f} kWh/m2/d; "
              f"fraccion de la PAR guardada en biomasa = {almacenada*100:.1f} %")
    print("   El resto (casi toda la potencia electrica) acaba como calor que el habitat debe evacuar.")

    print("Area y potencia para el oxigeno de una persona (tabla de Wheeler: 31.5 m2 con RUE 0.75, PPF 500, 16 h)")
    area_w = 31.5
    p_total = area_w * 500 / 3.4
    print(f"   Potencia de luminaria con 3.4 umol/J = {p_total/1000:.2f} kW mientras esta encendida; {p_total*16/1000:.1f} kWh/dia")
    biomasa_wheeler = area_w * 0.75 * d_wheeler
    biomasa_ch2o = 830 / 32.0 * 30.0
    print(f"   Biomasa implicita en la tabla = {biomasa_wheeler:.0f} g/d = {biomasa_wheeler/(830/32.0):.1f} g por mol de O2; "
          f"con CH2O (30 g/mol) serian {biomasa_ch2o:.0f} g/d")
    print("Sensibilidad: efecto de la eficacia en la potencia del modulo de 31.5 m2")
    for e in (2.0, 3.0, 3.4, 4.1):
        print(f"   eficacia {e:.1f} umol/J -> {area_w*500/e/1000:6.2f} kW")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
