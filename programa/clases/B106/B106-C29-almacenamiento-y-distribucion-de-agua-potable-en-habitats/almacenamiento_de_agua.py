#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C29: almacenamiento y distribucion de agua potable: volumen de reserva, caida de presion en una linea y vida util del biocida residual.

Consultado (OCHMO-TB-002): el agua minima para beber es de 2.5 L/dia por persona (V2 6109); el resumen lista requisitos de calidad (V2 6026), de temperatura (V2 6110) y de caudal e incrementos
de dispensacion de agua potable (V2 6039 y 6040). ILUSTRATIVOS: demanda total de 10 kg/dia por persona (C06), reserva de 3 dias de operacion sin reciclaje, margen del 10 %, linea de 10 m de
diametro interior 10 mm, caudal de 0.01 L/s, agua a 20 C (viscosidad 1.0e-3 Pa s, densidad 998 kg/m3), biocida residual inicial de 2 mg/L con decaimiento de primer orden de 0.05 1/dia y
residual minimo de 0.1 mg/L, tanque con membrana de gas de 30 L precargado a 200 kPa con 10 L de gas.
Verificacion: Poiseuille es valido con Re < 2000 y el laboratorio lo comprueba; la presion en el tanque sigue la ley isoterma; la vida del biocida cumple C(t) = C_min.
"""
from __future__ import annotations
import math
import platform
import numpy as np

MU, RHO = 1.0e-3, 998.0


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: demanda de bebida consultada (2.5 L/dia); resto ILUSTRATIVO; sin datos de un sistema real")
    R = {}
    crew, d_tot, dias, marg = 4, 10.0, 3, 0.10
    vol_bebida = crew * 2.5 * dias
    vol_total = crew * d_tot * dias * (1 + marg)
    R.update(vol_bebida=vol_bebida, vol_total=vol_total)
    print(f"Reserva de {dias} dias para {crew} personas: solo bebida {vol_bebida:.0f} L (2.5 L/dia); demanda total con {100*marg:.0f} % de margen {vol_total:.0f} L (masa {vol_total*RHO/1000:.0f} kg)")
    print("Reserva segun los dias de operacion sin reciclaje:")
    for d in (1, 3, 7, 14):
        print(f"   {d:2d} dias: {crew*d_tot*d*(1+marg):6.0f} L")
    d_m, L, Q = 10e-3, 10.0, 0.01e-3
    A = math.pi * d_m ** 2 / 4
    v = Q / A
    re = RHO * v * d_m / MU
    dp = 128 * MU * L * Q / (math.pi * d_m ** 4)
    R.update(v=v, re=re, dp=dp, P_hid=dp * Q)
    print(f"Linea de {L:.0f} m y {d_m*1e3:.0f} mm con {Q*1e3:.2f} L/s: velocidad {v:.3f} m/s; Re = {re:.0f} ({'laminar' if re < 2000 else 'NO laminar'}); caida de presion (Poiseuille) {dp:.0f} Pa = {dp/1e3:.2f} kPa; potencia hidraulica {dp*Q*1e3:.2f} mW")
    assert re < 2000
    print("Regimen segun el caudal (Poiseuille si Re < 2000; Blasius f = 0.316 Re^-0.25 si Re > 4000; entre ambos, transicion):")
    for qq in (0.005e-3, 0.01e-3, 0.02e-3, 0.05e-3):
        vv = qq / A
        rr = RHO * vv * d_m / MU
        if rr < 2000:
            d_p, reg = 128 * MU * L * qq / (math.pi * d_m ** 4), "laminar"
        elif rr > 4000:
            d_p, reg = 0.316 * rr ** -0.25 * (L / d_m) * RHO * vv * vv / 2, "turbulento"
        else:
            d_p, reg = float("nan"), "transicion"
        print(f"   {qq*1e3:5.3f} L/s: Re = {rr:6.0f} ({reg}); " + (f"caida {d_p/1e3:7.3f} kPa" if d_p == d_p else "caida no definida por estas formulas"))
    R["dp50"] = 0.316 * (RHO * 0.05e-3 / A * d_m / MU) ** -0.25 * (L / d_m) * RHO * (0.05e-3 / A) ** 2 / 2
    for dd in (8e-3, 10e-3, 12e-3):
        print(f"   diametro {dd*1e3:4.0f} mm: caida {128*MU*L*Q/(math.pi*dd**4)/1e3:7.2f} kPa (escala con d^-4)")
    assert abs(128 * MU * L * Q / (math.pi * (5e-3) ** 4) / dp - 16) < 1e-9
    R["dp8"] = 128 * MU * L * Q / (math.pi * (8e-3) ** 4)
    # tanque con membrana: gas isotermo
    Vt, Vg0, P0 = 30.0, 10.0, 200.0
    print("Tanque con membrana de gas (30 L, gas de 10 L a 200 kPa): presion de entrega al extraer agua")
    for ext in (0.0, 5.0, 10.0, 15.0):
        vg = Vg0 + ext
        p = P0 * Vg0 / vg
        print(f"   agua extraida {ext:4.1f} L: gas {vg:5.1f} L, presion {p:6.1f} kPa")
    R["p15"] = P0 * Vg0 / (Vg0 + 15.0)
    R["util"] = Vt - Vg0
    assert abs(P0 * Vg0 / (Vg0 + 10.0) - 100.0) < 1e-12
    c0, cmin, k = 2.0, 0.1, 0.05
    t_max = math.log(c0 / cmin) / k
    R["t_max"] = t_max
    print(f"Biocida: {c0} mg/L con k = {k} 1/dia llega a {cmin} mg/L en {t_max:.1f} dias; a los 30 dias queda {c0*math.exp(-k*30):.3f} mg/L; a los 90, {c0*math.exp(-k*90):.4f} mg/L")
    assert abs(c0 * math.exp(-k * t_max) - cmin) < 1e-12
    R["c30"], R["c90"] = c0 * math.exp(-k * 30), c0 * math.exp(-k * 90)
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
