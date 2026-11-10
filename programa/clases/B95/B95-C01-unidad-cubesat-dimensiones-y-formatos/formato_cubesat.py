#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B95-C01: cumplimiento de una configuracion CubeSat de 1U a 3U.

Datos CONSULTADOS (2026-11-10): CubeSat Design Specification (1U-12U) Rev. 14.1 (Cal Poly), texto completo:
  Tabla 1 (masa maxima tipica): 1U 2.00 kg; 1.5U 3.00; 2U 4.00; 3U 6.00 [kg]
  Tabla 2 (CG respecto del centro geometrico, +/-): 1U (2,2,2) cm; 1.5U (2,2,3); 2U (2,2,4.5); 3U (2,2,7)
  Longitud de la envolvente (historial de cambios): 1U 113.5 mm; 1.5U 170.2; 2U 227.0; 3U 340.5; seccion 100 x 100 mm (1U)
  2.4.4: deployables esperan >= 30 min tras activar el interruptor de despliegue; 2.4.5: sin transmitir antes de 45 min.
  Las dimensiones de 6U y 12U estan en dibujos que NO se consultaron: no se usan.
ILUSTRATIVOS (sinteticos, no medidos): lista de masas y posiciones de un 3U ficticio y la linea de tiempo de eventos.
Sistema de referencia: origen en el centro geometrico del CubeSat, ejes X, Y, Z de la seccion 2.2.1 del CDS; unidades SI salvo mm y cm indicados.
Tolerancias: comprobaciones de aritmetica < 1e-9; el CG es resultado de un promedio ponderado de masas puntuales.
"""
from __future__ import annotations
import platform

MASA_MAX = {"1U": 2.00, "1.5U": 3.00, "2U": 4.00, "3U": 6.00}  # kg, CDS Tabla 1
CG_MAX = {"1U": (2.0, 2.0, 2.0), "1.5U": (2.0, 2.0, 3.0), "2U": (2.0, 2.0, 4.5), "3U": (2.0, 2.0, 7.0)}  # cm, CDS Tabla 2
LARGO = {"1U": 113.5, "1.5U": 170.2, "2U": 227.0, "3U": 340.5}  # mm, CDS historial de cambios
LADO = 100.0  # mm

# 3U ILUSTRATIVO: (nombre, masa kg, x cm, y cm, z cm) respecto del centro geometrico
MASAS = [
    ("estructura", 0.95, 0.0, 0.0, 0.0),
    ("baterias", 0.60, 0.5, -0.3, -9.0),
    ("OBC y EPS", 0.45, -0.4, 0.2, -4.0),
    ("carga util", 1.40, 0.3, 0.4, 5.0),
    ("ADCS", 0.55, 0.0, 0.0, 10.5),
    ("radio y antena", 0.35, -0.2, 0.3, 13.0),
    ("paneles solares", 0.70, 0.0, 0.0, 0.0),
]


def volumen_l(u):
    return LADO * LADO * LARGO[u] * 1e-6  # mm3 -> L


def centro_de_gravedad(masas):
    m = sum(x[1] for x in masas)
    return m, tuple(sum(x[1] * x[k] for x in masas) / m for k in (2, 3, 4))


def centro_de_gravedad_dos_vias(masas):
    """Segunda via: momentos acumulados con aritmetica por separado."""
    m = 0.0
    mom = [0.0, 0.0, 0.0]
    for _, mi, *r in masas:
        m += mi
        for k in range(3):
            mom[k] += mi * r[k]
    return m, tuple(c / m for c in mom)


def cumple(u, masa, cg):
    ok_m = masa <= MASA_MAX[u] + 1e-12
    ok_cg = all(abs(c) <= lim + 1e-12 for c, lim in zip(cg, CG_MAX[u]))
    return ok_m, ok_cg


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Tabla de formatos (CDS Rev. 14.1, consultado) y densidad media maxima:")
    print(" fmt   largo[mm]  vol[L]  masa max[kg]  rho_max[kg/L]  CG(x,y,z)[cm]")
    for u in MASA_MAX:
        v = volumen_l(u)
        print(f"{u:5s} {LARGO[u]:9.1f} {v:7.3f} {MASA_MAX[u]:11.2f} {MASA_MAX[u] / v:13.3f}   {CG_MAX[u]}")
    # comprobacion: el largo de 3U es 3 x 113.5 mm (derivado) frente al publicado
    d3 = abs(3 * LARGO["1U"] - LARGO["3U"])
    print(f"3 x 113.5 - 340.5 = {d3:.3f} mm ; 2 x 113.5 - 227.0 = {abs(2 * LARGO['1U'] - LARGO['2U']):.3f} mm ; 1.5 x 113.5 - 170.2 = {abs(1.5 * LARGO['1U'] - LARGO['1.5U']):.3f} mm")
    print("\n3U ILUSTRATIVO (masas sinteticas, no medidas):")
    m, cg = centro_de_gravedad(MASAS)
    m2, cg2 = centro_de_gravedad_dos_vias(MASAS)
    print(f"  masa total = {m:.3f} kg (limite {MASA_MAX['3U']:.2f} kg) ; margen = {MASA_MAX['3U'] - m:.3f} kg")
    print(f"  CG = ({cg[0]:.3f}, {cg[1]:.3f}, {cg[2]:.3f}) cm ; limites {CG_MAX['3U']}")
    ok_m, ok_cg = cumple("3U", m, cg)
    print(f"  cumple masa: {ok_m} ; cumple CG: {ok_cg}")
    # variante: mover la carga util 2 cm hacia +Z empuja el CG
    var = [(n, mi, x, y, z + (2.0 if n == "carga util" else 0.0)) for n, mi, x, y, z in MASAS]
    mv, cgv = centro_de_gravedad(var)
    print(f"  variante (carga util +2 cm en Z): CG_z = {cgv[2]:.3f} cm ; cumple CG: {cumple('3U', mv, cgv)[1]}")
    # linea de tiempo: eventos tras el interruptor de despliegue [min]
    eventos = [("encendido permitido", 0.0), ("despliegue de antena", 31.0), ("primera transmision", 46.0)]
    print("Linea de tiempo ILUSTRATIVA tras la expulsion (reglas 2.4.4 y 2.4.5):")
    for nombre, t in eventos:
        if "antena" in nombre:
            ok = t >= 30.0
        elif "transmision" in nombre:
            ok = t >= 45.0
        else:
            ok = True
        print(f"  t = {t:5.1f} min  {nombre:22s} {'cumple' if ok else 'INCUMPLE'}")
    assert abs(m - m2) < 1e-12 and max(abs(a - b) for a, b in zip(cg, cg2)) < 1e-9
    assert d3 < 1e-9 and ok_m and ok_cg
    assert not cumple("3U", mv, cgv)[1] or abs(cgv[2]) <= 7.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
