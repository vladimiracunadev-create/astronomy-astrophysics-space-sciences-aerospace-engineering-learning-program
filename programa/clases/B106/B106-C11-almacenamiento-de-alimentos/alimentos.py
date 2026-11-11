#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C11: masa de alimento de una mision y vida util por la regla de Q10.

Consultado (OCHMO-TB-002): ingesta media de 3035 kcal/dia por persona. ILUSTRATIVOS (inventados): densidad energetica del alimento envasado de 3.5 kcal/g, envase del 15 % de la masa,
margen del 10 %, vida util de referencia de 24 meses a 21 C (tiempo hasta retener el 80 % de un nutriente), Q10 = 2. Regla de Q10: t(T) = t_ref Q10^((T_ref - T)/10).
Cinetica de primer orden: retencion = exp(-k t) con k = -ln(0.8)/t_vida. Sin datos de alimentos reales.
Verificacion: a la temperatura de referencia la retencion tras t_vida es 0.80; subir 10 C divide la vida util por Q10.
"""
from __future__ import annotations
import math
import platform
import numpy as np

KCAL, DENS, ENV, MARG = 3035.0, 3.5, 0.15, 0.10
TREF, TVIDA, Q10 = 21.0, 24.0, 2.0  # C, meses, adimensional


def vida(T):
    return TVIDA * Q10 ** ((TREF - T) / 10.0)


def retencion(t_meses, T):
    k = -math.log(0.8) / vida(T)
    return math.exp(-k * t_meses)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: ingesta consultada (3035 kcal/dia); densidad energetica, envase, vida util y Q10 ILUSTRATIVOS; sin datos de alimentos reales")
    R = {}
    g_dia = KCAL / DENS
    m_dia = g_dia / 1000.0 * (1 + ENV)
    R["g_dia"], R["m_dia"] = g_dia, m_dia
    print(f"Alimento por persona y dia: {g_dia:.0f} g de alimento + {100*ENV:.0f} % de envase = {m_dia:.3f} kg")
    print("Misiones (con 10 % de margen):")
    print("   mision               personas  dias   masa total [kg]")
    for nom, c, d in (("orbita baja", 4, 180), ("Luna superficie", 4, 365), ("Marte ida y vuelta", 6, 900)):
        M = c * d * m_dia * (1 + MARG)
        print(f"   {nom:20s} {c:6d}  {d:5d}   {M:12.0f}")
        R[nom] = M
    print(f"Vida util (80 % de retencion) segun la temperatura de almacenamiento (Q10 = {Q10}):")
    print("   T [C]   vida util [meses]   retencion a 12 m   retencion a 36 m")
    for T in (4.0, 21.0, 31.0, 41.0):
        print(f"   {T:5.1f}   {vida(T):15.1f}   {retencion(12, T):14.3f}   {retencion(36, T):14.3f}")
    R["v21"], R["v31"], R["v4"] = vida(21.0), vida(31.0), vida(4.0)
    R["r36_21"], R["r36_31"] = retencion(36, 21.0), retencion(36, 31.0)
    assert abs(retencion(TVIDA, TREF) - 0.80) < 1e-12 and abs(vida(31.0) * Q10 - vida(21.0)) < 1e-12
    # alimento que llega con 24 meses de almacenamiento previo mas 30 meses de mision
    t_tot = 24 + 30
    ret = retencion(t_tot, 21.0)
    R["ret54"] = ret
    print(f"Alimento almacenado 24 meses antes y consumido hasta 30 meses despues ({t_tot} m) a 21 C: retencion {ret:.3f} ({'bajo' if ret<0.8 else 'sobre'} el 80 %)")
    print(f"Alimento a 31 C: retencion a 36 m {R['r36_31']:.3f} frente a {R['r36_21']:.3f} a 21 C")
    assert R["r36_31"] < R["r36_21"]
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
