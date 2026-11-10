#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C11: presupuesto de micropropulsion de un CubeSat (impulso total, Delta-v y limite por potencia).

Datos CONSULTADOS (2026-11-10): g0 = 9.80665 m/s2 (NIST); NASA SSVI, Tabla 4-1 y texto:
 gas frio 10 uN-3.6 N, 40-110 s; modulo CPOD hasta 186 N s; sistema H2O2-etanol 250 mN, 179 s, impulso total estimado 1400 N s (1.5U) y 2120 N s (2U);
 electrospray 20 uN-20 mN, 225-3000 s; ionico de rejillas 0.1-20 mN, 500-3000 s; Hall 0.25-55 mN, 200-1920 s;
 la propulsion electrica queda por debajo de ~75 mN/kW (500 W -> hasta ~38 mN).
ILUSTRATIVOS (sinteticos, no de una mision): masa del CubeSat 6 kg, potencia disponible para propulsion 20 W, Delta-v requerido 100 m/s,
valores dentro de los rangos consultados para el empuje y el Isp de cada tecnologia (columna 'elegido').
Modelo: Tsiolkovsky con empuje impulsivo, t = m dv / F (masa constante, aproximacion), F <= 75 mN/kW * P para los electricos.
Segunda via: Delta-v = I_total/m (aproximacion de masa constante) frente a Tsiolkovsky con la masa de propelente correspondiente.
Tolerancia: el error relativo de la aproximacion lineal es ~(dv/Ve)/2; se exige menos de 0.6 dv/Ve.
"""
from __future__ import annotations
import math, platform

G0 = 9.80665
M0, P_DISP, DV = 6.0, 20.0, 100.0
# nombre: (F elegido [N], Isp elegido [s], es_electrico)
OPC = {
    "gas frio": (25e-3, 70.0, False),
    "H2O2-etanol": (250e-3, 179.0, False),
    "electrospray": (1.0e-3, 1500.0, True),
    "ionico de rejillas": (1.0e-3, 2000.0, True),
    "Hall": (1.4e-3, 1200.0, True),
}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"CubeSat ILUSTRATIVO: m = {M0:.0f} kg ; potencia para propulsion = {P_DISP:.0f} W ; dv requerido = {DV:.0f} m/s")
    tope = 75e-6 * P_DISP  # N
    print(f"Tope consultado F/P < 75 mN/kW -> F <= {tope*1e3:.2f} mN con {P_DISP:.0f} W")
    print(" tecnologia            F [mN]  Isp [s]  m_prop [kg]  m_prop/m0   t [dias]   cumple tope")
    for n, (f, isp, el) in OPC.items():
        ve = isp * G0
        mp = M0 * (1 - math.exp(-DV / ve))
        mp2 = M0 * DV / ve  # aproximacion lineal
        assert abs(mp - mp2) / mp < 0.6 * DV / ve  # error relativo ~ (dv/ve)/2
        t = M0 * DV / f / 86400
        cumple = (f <= tope) if el else True
        print(f" {n:<20} {f*1e3:>7.2f} {isp:>8.0f} {mp:>11.4f} {mp/M0:>10.4f} {t:>10.2f}   {'si' if cumple else 'NO'}")
        if el:
            assert cumple
    print("Delta-v con los impulsos totales consultados (masa constante de 6 kg):")
    for n, it in (("CPOD (gas frio)", 186.0), ("H2O2-etanol, 1.5U", 1400.0), ("H2O2-etanol, 2U", 2120.0)):
        dv = it / M0
        print(f"  {n:<20} I = {it:>6.0f} N s -> dv ~ {dv:>6.1f} m/s")
    # comprobacion cruzada: I_total = F t = m_prop ve
    f, isp, _ = OPC["H2O2-etanol"]
    ve = isp * G0
    it = 1400.0
    mp_it = it / ve
    print(f"  Propelente equivalente a 1400 N s con Isp 179 s: {mp_it:.3f} kg")
    print("Limite por potencia: tiempo para dv = 100 m/s con 20 W si el propulsor electrico usa todo el tope:")
    for isp in (1500.0, 2000.0, 3000.0):
        ve = isp * G0
        f_tope = min(tope, 2 * 0.5 * P_DISP / ve)  # eficiencia 0.5 ILUSTRATIVA
        t = M0 * DV / f_tope / 86400
        print(f"  Isp = {isp:>5.0f} s -> F = {f_tope*1e3:>5.3f} mN ; t = {t:>6.1f} dias de empuje continuo")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
