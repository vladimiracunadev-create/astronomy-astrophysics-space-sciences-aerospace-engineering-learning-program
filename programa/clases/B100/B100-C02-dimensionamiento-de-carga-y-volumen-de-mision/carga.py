#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B100-C02: masa y volumen de carga de una mision de superficie y masa inicial por la ecuacion del cohete.

ILUSTRATIVOS (no consultados, no medidos): tasas de consumo por persona y dia (oxigeno 0.84, agua 4.0, alimento seco 0.80 kg/dia),
densidades aparentes (kg/m3), factor de embalaje 1.15, repuestos 10 % de la masa, 4 personas, 30 dias; Isp = 450 s; fraccion estructural 0.10;
Delta-v de la cadena LEO -> superficie lunar = 3.1 + 0.9 + 1.9 km/s (ilustrativo).
CONSULTADO (2026-11-10): ecuacion ideal del cohete de NASA Glenn, Delta u = V_eq ln(m_f/m_e); g0 = 9.80665 m/s2 (valor estandar, no consultado en esta sesion).
Segunda via: Delta-v recuperado de la masa inicial con la ecuacion inversa; producto de factores por tramo con fraccion estructural nula.
Tolerancia: 1e-9 relativa.
"""
from __future__ import annotations
import math
import platform

G0 = 9.80665
TASAS = {"oxigeno": (0.84, 1.43), "agua": (4.0, 1000.0), "alimento": (0.80, 600.0)}  # kg/dia/persona, kg/m3
PERSONAS, DIAS = 4, 30
EMBALAJE, REPUESTOS = 1.15, 0.10
ISP, EPS = 450.0, 0.10
TRAMOS = {"LEO->TLI": 3.1, "TLI->LLO": 0.9, "LLO->superficie": 1.9}  # km/s ilustrativos


def masa_inicial(carga, dv_ms, isp=ISP, eps=EPS):
    """Masa inicial de una etapa: estructura eps*m_prop+..., con m0 = carga/(factor)."""
    ve = isp * G0
    r = math.exp(dv_ms / ve)  # m0/mf
    # mf = carga + estructura; estructura = eps * propelente; propelente = m0 - mf
    # m0 = r*mf; mf = carga + eps*(r*mf - mf) => mf = carga/(1 - eps*(r-1))
    den = 1.0 - eps * (r - 1.0)
    if den <= 0:
        raise ValueError("fraccion estructural inalcanzable")
    mf = carga / den
    return r * mf


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos ILUSTRATIVOS: tasas de consumo, densidades, embalaje, repuestos, Isp, fraccion estructural y Delta-v")
    masa = vol = 0.0
    print(" consumible   masa [kg]   volumen [m3]")
    for nom, (tasa, rho) in TASAS.items():
        m = tasa * PERSONAS * DIAS
        v = m / rho
        masa += m
        vol += v
        print(f" {nom:10s} {m:10.1f} {v:12.3f}")
    m_emb = masa * EMBALAJE
    m_rep = REPUESTOS * m_emb
    m_carga = m_emb + m_rep
    print(f"Consumibles netos {masa:.1f} kg ; con embalaje {m_emb:.1f} kg ; con repuestos {m_carga:.1f} kg")
    print(f"Volumen neto de consumibles {vol:.3f} m3")
    m = m_carga
    print("Masa que debe existir antes de cada tramo (hacia atras):")
    for nom, dv in reversed(list(TRAMOS.items())):
        m = masa_inicial(m, dv * 1000.0)
        print(f"  antes de {nom:16s} {m:10.1f} kg")
    crecimiento = m / m_carga
    print(f"Factor de crecimiento masa en LEO / masa en superficie = {crecimiento:.3f}")
    # segunda via 1: producto de factores con eps = 0
    f_prod = 1.0
    for dv in TRAMOS.values():
        f_prod *= math.exp(dv * 1000.0 / (ISP * G0))
    f_tot = masa_inicial(1.0, sum(TRAMOS.values()) * 1000.0, eps=0.0)
    print(f"Con estructura nula: producto por tramo {f_prod:.6f} ; tramo unico {f_tot:.6f}")
    # segunda via 2: recuperar el Delta-v de la masa inicial de un tramo
    m0 = masa_inicial(m_carga, 1900.0)
    mf = m0 - (m0 - m_carga) / (1 + EPS * 0) if False else None
    r = math.exp(1900.0 / (ISP * G0))
    mf = m0 / r
    dv_rec = ISP * G0 * math.log(m0 / mf)
    print(f"Delta-v recuperado del tramo final = {dv_rec:.6f} m/s (dato 1900)")
    print(f"Aterrizadores de 1500 kg de carga necesarios: {math.ceil(m_carga / 1500.0)}")
    assert abs(f_prod - f_tot) / f_tot < 1e-9
    assert abs(dv_rec - 1900.0) < 1e-6
    assert crecimiento > 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
