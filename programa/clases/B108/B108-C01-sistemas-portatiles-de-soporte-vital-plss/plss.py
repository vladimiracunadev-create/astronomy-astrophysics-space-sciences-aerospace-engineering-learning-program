#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B108-C01: balance de consumibles de un sistema portatil de soporte vital (PLSS) en una EVA SINTETICA.

CONSULTADOS (2026-11-10): NASA JSC (NTRS 20170004971): presion de operacion del EMU 4.3 psi = 29.6 kPa.
Watts et al. (NTRS 20120007410, PLSS 1.0): inyeccion de CO2 28-280 g/h, agua 35-89 g/h, fuga del traje 2.1-4.2 g/h,
cargas metabolicas de prueba 469 W y maximo 700 W, rechazo de diseno del SWME 810 W, presion de suministro 25.86 -> 1.72 MPa.
ILUSTRATIVOS (sinteticos, no medidos): perfil de la EVA (segmentos y potencias), reserva (30 min a 700 W), temperatura del gas 293.15 K.
RELACIONES ESTANDAR NO CONSULTADAS EN FUENTE CONCRETA: 20.1 kJ por litro de O2 (STP), RQ = 0.85, densidades STP O2 1.429 g/L y
CO2 1.977 g/L, calor latente 2.43 MJ/kg, R = 8.314462618 J/(mol K), gas ideal (Z = 1).
Modelo: calor a rechazar = potencia metabolica (sin perdidas por el traje); volumen de O2 = W t / 20.1 kJ/L.
Segunda via: integral trapezoidal numerica con paso fino frente a la forma cerrada. Tolerancia: 1e-9 relativa.
Unidades: W, s, g, L (STP), Pa, K, m3. Sistema de referencia: no aplica (balance escalar).
"""
from __future__ import annotations
import platform

E_O2 = 20.1e3      # J por litro de O2 (STP)
RQ = 0.85
RHO_O2, RHO_CO2 = 1.429, 1.977   # g/L (STP)
H_FG = 2.43e6      # J/kg
R_GAS, T_GAS, M_O2 = 8.314462618, 293.15, 31.998e-3
P_FULL, P_MIN = 25.86e6, 1.72e6   # Pa (consultado)
PERFIL = [("egreso", 0.5, 300.0), ("traslado", 0.75, 450.0), ("trabajo", 3.5, 469.0),
          ("trabajo intenso", 1.0, 700.0), ("retorno", 0.75, 450.0), ("ingreso", 0.5, 300.0)]
FUGA_GH = 4.2      # g/h, extremo alto del rango consultado
RESERVA_S, RESERVA_W = 1800.0, 700.0   # ILUSTRATIVO


def o2_litros(w, s):
    return w * s / E_O2


def tasas(w):
    """g/h de O2 y CO2 y de agua evaporada [g/h] a potencia metabolica w."""
    lo2 = w * 3600.0 / E_O2
    return lo2 * RHO_O2, RQ * lo2 * RHO_CO2, w / H_FG * 3600.0 * 1e3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("EVA SINTETICA (perfil ilustrativo); presion de traje 29.6 kPa (consultada)")
    print(" segmento           t [h]   W    O2 [g]  CO2 [g]  agua [g]")
    to2 = tco2 = tag = tj = ts = 0.0
    for n, h, w in PERFIL:
        s = h * 3600.0
        o2, co2, ag = o2_litros(w, s) * RHO_O2, RQ * o2_litros(w, s) * RHO_CO2, w * s / H_FG * 1e3
        to2, tco2, tag, tj, ts = to2 + o2, tco2 + co2, tag + ag, tj + w * s, ts + s
        print(f" {n:<16}  {h:5.2f}  {w:5.0f}  {o2:7.1f}  {co2:7.1f}  {ag:7.1f}")
    fuga = FUGA_GH * ts / 3600.0
    print(f" TOTAL              {ts/3600:5.2f}        {to2:7.1f}  {tco2:7.1f}  {tag:7.1f}")
    print(f"Energia metabolica total = {tj/3.6e6:.3f} kWh; potencia media = {tj/ts:.1f} W")
    print(f"Fuga del traje (4.2 g/h x {ts/3600:.1f} h) = {fuga:.1f} g")
    # segunda via: trapecio numerico
    dt, t, acum = 1.0, 0.0, 0.0
    for _, h, w in PERFIL:
        for _ in range(int(h * 3600 / dt)):
            acum += o2_litros(w, dt) * RHO_O2
    dif = abs(acum - to2) / to2
    print(f"Diferencia relativa forma cerrada frente a suma numerica (dt = 1 s) = {dif:.2e}")
    # rangos consultados
    print("Contraste con rangos de ajuste de PLSS 1.0 (no es validacion):")
    for w in (469.0, 700.0):
        o2, co2, ag = tasas(w)
        print(f"  {w:.0f} W: CO2 {co2:6.1f} g/h (rango 28-280: {'dentro' if 28 <= co2 <= 280 else 'FUERA'}), "
              f"agua evaporada {ag:6.1f} g/h, O2 {o2:6.1f} g/h")
    print(f"Margen frente al rechazo de diseno del SWME: 810 - 700 = {810.0 - 700.0:.0f} W")
    # reserva y tanque
    res = o2_litros(RESERVA_W, RESERVA_S) * RHO_O2
    req = to2 + fuga + res
    n_mol = req / (M_O2 * 1e3)
    frac = (P_FULL - P_MIN) / P_FULL
    v_tanque = n_mol * R_GAS * T_GAS / (P_FULL * frac)
    print(f"Reserva ilustrativa (30 min a 700 W) = {res:.1f} g; O2 total requerido = {req:.1f} g = {n_mol:.2f} mol")
    print(f"Fraccion util de la presion (25.86 -> 1.72 MPa) = {frac:.4f}; volumen de tanque (gas ideal, 293.15 K) = {v_tanque*1e3:.2f} L")
    ok = dif < 1e-9 and abs(tj / ts - sum(w * h for _, h, w in PERFIL) / sum(h for _, h, _ in PERFIL)) < 1e-9
    assert ok and 28 <= tasas(469.0)[1] <= 280 and 28 <= tasas(700.0)[1] <= 280
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
