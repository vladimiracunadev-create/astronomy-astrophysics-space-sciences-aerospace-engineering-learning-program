#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B100-C06: red logistica cislunar con ecuacion del cohete, con y sin deposito de reabastecimiento.

CONSULTADO (2026-11-10): distancia media Tierra-Luna 384 400 km (ficha de la Luna, NASA/NSSDC); ecuacion ideal del cohete (NASA Glenn);
la pagina de Gateway de la NASA confirma que Gateway usa una orbita casi rectilinea de halo (NRHO) y no da periodo ni distancias.
Valores EXACTOS del SI no consultados: g0 = 9.80665 m/s2, c = 299 792 458 m/s.
ILUSTRATIVOS (no consultados, no medidos): Delta-v de los tramos LEO->NRHO 3.5, NRHO->superficie 2.7 y superficie->NRHO 2.7 km/s;
Isp quimico 450 s con fraccion estructural 0.10; carga a la superficie 1000 kg; sin retorno de carga.
Escenario A (directo): etapas quimicas desechables LEO->NRHO y NRHO->superficie.
Escenario B (con deposito en NRHO): un aterrizador reutilizable (500 kg secos) baja con la carga y sube vacio; la carga y el propelente de cada
viaje se entregan al deposito desde LEO, con etapas quimicas o con un remolcador electrico ILUSTRATIVO (Isp 1800 s, fraccion estructural 0.20,
Delta-v 6.0 km/s, viaje mas lento).
Segunda via: con fraccion estructural nula la masa total es el producto de los factores exp(dv/ve) de cada tramo. Tolerancia 1e-9.
"""
from __future__ import annotations
import math
import platform

G0, C = 9.80665, 299_792_458.0
ISP, EPS = 450.0, 0.10
VE = ISP * G0
DV = {"LEO->NRHO": 3500.0, "NRHO->sup": 2700.0, "sup->NRHO": 2700.0}


def m0_etapa(carga, dv, isp=ISP, eps=EPS):
    ve = isp * G0
    r = math.exp(dv / ve)
    den = 1.0 - eps * (r - 1.0)
    if den <= 0:
        raise ValueError("inalcanzable")
    return r * carga / den


def propelente_aterrizador(carga, seca):
    """Propelente para bajar con carga y subir vacio (masa seca fija)."""
    m_ini_sub = seca * math.exp(DV["sup->NRHO"] / VE)
    p_sub = m_ini_sub - seca
    m_fin_desc = seca + carga + p_sub
    m_ini_desc = m_fin_desc * math.exp(DV["NRHO->sup"] / VE)
    return (m_ini_desc - m_fin_desc) + p_sub


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos ILUSTRATIVOS: Delta-v por tramo, Isp, fracciones estructurales y masas; consultados: distancia Tierra-Luna y ecuacion del cohete")
    print(f"Velocidad efectiva quimica ve = {VE:.1f} m/s ; retardo de luz Tierra-Luna = {384_400e3 / C:.4f} s")
    carga, seca = 1000.0, 500.0
    m_nrho = m0_etapa(carga, DV["NRHO->sup"])
    m_leo_a = m0_etapa(m_nrho, DV["LEO->NRHO"])
    print(f"A directo (etapas quimicas desechables): masa en NRHO {m_nrho:.1f} kg ; en LEO {m_leo_a:.1f} kg ; razon LEO/carga = {m_leo_a / carga:.3f}")
    prop = propelente_aterrizador(carga, seca)
    print(f"B: aterrizador reutilizable de {seca:.0f} kg secos; propelente por viaje {prop:.1f} kg")
    m_quim = m0_etapa(carga + prop, DV["LEO->NRHO"]) + m0_etapa(seca, DV["LEO->NRHO"]) / 10.0
    print(f"B con transporte quimico a NRHO (10 viajes): LEO {m_quim:.1f} kg ; razon = {m_quim / carga:.3f}")
    isp_t, eps_t, dv_t = 1800.0, 0.20, 6000.0
    print(f"B con remolcador electrico ILUSTRATIVO (Isp {isp_t:.0f} s, fraccion estructural {eps_t}, Delta-v {dv_t / 1000:.1f} km/s, mas lento):")
    print(" viajes   LEO [kg]   razon LEO/carga")

    def leo_b(n):
        return m0_etapa(carga + prop, dv_t, isp_t, eps_t) + m0_etapa(seca, dv_t, isp_t, eps_t) / n

    for n in (1, 3, 5, 10, 20):
        print(f"  {n:5d}  {leo_b(n):9.1f}  {leo_b(n) / carga:12.3f}")
    n_eq = next((n for n in range(1, 500) if leo_b(n) < m_leo_a), None)
    print(f"Viajes del aterrizador para que B con remolcador electrico supere a A: {n_eq}")
    f_prod = math.exp(DV["LEO->NRHO"] / VE) * math.exp(DV["NRHO->sup"] / VE)
    f_unico = m0_etapa(1.0, DV["LEO->NRHO"] + DV["NRHO->sup"], eps=0.0)
    print(f"Con estructura nula: producto {f_prod:.6f} ; tramo unico {f_unico:.6f}")
    assert abs(f_prod - f_unico) / f_unico < 1e-9
    assert m_quim > m_leo_a
    assert n_eq is not None
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
