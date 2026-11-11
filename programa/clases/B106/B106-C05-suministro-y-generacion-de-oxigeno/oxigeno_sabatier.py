#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C05: estequiometria de la electrolisis del agua y de la reaccion de Sabatier para una persona.

Consultado (NASA, pagina del ECLSS): el conjunto de generacion de oxigeno electroliza agua en O2 (a la cabina) e H2; el reactor Sabatier combina ese H2 con el
CO2 exhalado para dar metano y agua. Valores de manual NO consultados en una fuente concreta: masas molares y la entalpia de formacion del agua liquida
(285.83 kJ/mol) y la energia libre (237.1 kJ/mol). El rendimiento de celda y el consumo electrico de un equipo real NO se usan.
Datos de la tripulacion: C01 (0.771 kg de O2 y 0.85 de RQ por persona y dia). Verificacion: conservacion de C, H y O en ambas reacciones.
"""
from __future__ import annotations
import platform
import numpy as np

M = {"H2": 2.016e-3, "O2": 31.998e-3, "H2O": 18.015e-3, "CO2": 44.01e-3, "CH4": 16.043e-3}
DH, DG = 285.83e3, 237.1e3  # J/mol H2O


def balance(m_o2, rq=0.85):
    n_o2 = m_o2 / M["O2"]
    n_h2o_el = 2 * n_o2
    n_h2 = 2 * n_o2
    n_co2 = rq * n_o2
    n_co2_red = min(n_co2, n_h2 / 4)
    n_h2o_sab = 2 * n_co2_red
    return dict(n_o2=n_o2, n_h2o_el=n_h2o_el, n_h2=n_h2, n_co2=n_co2, n_co2_red=n_co2_red, n_h2o_sab=n_h2o_sab, n_ch4=n_co2_red)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: estequiometria propia con valores de manual NO consultados; sin datos de un equipo real")
    R = {}
    print("Por kg de O2 producido por electrolisis (2 H2O -> 2 H2 + O2):")
    n = 1.0 / M["O2"]
    m_h2o, m_h2 = 2 * n * M["H2O"], 2 * n * M["H2"]
    e_h = 2 * n * DH
    e_g = 2 * n * DG
    R.update(m_h2o=m_h2o, m_h2=m_h2, kwh_h=e_h / 3.6e6, kwh_g=e_g / 3.6e6)
    print(f"   agua consumida {m_h2o:.4f} kg; H2 producido {m_h2:.4f} kg; energia minima (entalpia) {e_h/1e6:.2f} MJ = {e_h/3.6e6:.3f} kWh; (energia libre) {e_g/3.6e6:.3f} kWh")
    assert abs(1.0 + m_h2 - m_h2o) < 1e-3  # masa
    b = balance(0.771)
    R["b"] = b
    print("Por persona y dia (O2 = 0.771 kg, RQ 0.85):")
    print(f"   O2: {b['n_o2']:.2f} mol; H2O electrolizada: {b['n_h2o_el']*M['H2O']:.3f} kg; H2 producido: {b['n_h2']:.2f} mol = {b['n_h2']*M['H2']:.4f} kg")
    print(f"   CO2 exhalado: {b['n_co2']:.2f} mol = {b['n_co2']*M['CO2']:.3f} kg; el H2 alcanza para reducir {b['n_co2_red']:.2f} mol ({100*b['n_co2_red']/b['n_co2']:.1f} %)")
    print(f"   Sabatier: CH4 {b['n_ch4']*M['CH4']*1e3:.1f} g; agua recuperada {b['n_h2o_sab']*M['H2O']:.3f} kg; agua neta consumida {(b['n_h2o_el']-b['n_h2o_sab'])*M['H2O']:.3f} kg (sin Sabatier: {b['n_h2o_el']*M['H2O']:.3f} kg)")
    R["frac"] = b["n_co2_red"] / b["n_co2"]
    R["neta"] = (b["n_h2o_el"] - b["n_h2o_sab"]) * M["H2O"]
    R["bruta"] = b["n_h2o_el"] * M["H2O"]
    R["P_ideal"] = 0.771 * (e_h / 3.6e6) * 1000 / 24
    print(f"   Potencia electrica minima continua (entalpia): {R['P_ideal']:.0f} W por persona; para 4 personas {4*R['P_ideal']/1e3:.2f} kW")
    # conservacion de elementos
    C_in = b["n_co2_red"]; C_out = b["n_ch4"]
    H_in = 4 * b["n_co2_red"] * 2; H_out = b["n_ch4"] * 4 + b["n_h2o_sab"] * 2
    O_in = b["n_co2_red"] * 2; O_out = b["n_h2o_sab"]
    print(f"Control Sabatier (C, H, O entran/salen mol): C {C_in:.3f}/{C_out:.3f}; H {H_in:.3f}/{H_out:.3f}; O {O_in:.3f}/{O_out:.3f}")
    assert abs(C_in - C_out) < 1e-9 and abs(H_in - H_out) < 1e-9 and abs(O_in - O_out) < 1e-9
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
