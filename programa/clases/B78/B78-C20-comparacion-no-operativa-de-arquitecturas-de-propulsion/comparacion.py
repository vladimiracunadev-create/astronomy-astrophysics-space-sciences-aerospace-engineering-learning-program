#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C20: comparacion NO operativa de arquitecturas de propulsion por rangos publicados y frente de Pareto.

Datos CONSULTADOS (2026-11-10): g0 = 9.80665 m/s2 (NIST); rangos de empuje e Isp de la Tabla 4-1 del estado del arte de propulsion de la NASA SSVI
(solo se leyeron los primeros 100000 de 289063 caracteres de la pagina):
 hidracina monopropelente 0.25-28 N, 180-285 s ; mono/bipropelentes alternativos 0.05-22 N, 150-310 s ; gas frio 10 uN-3.6 N, 40-110 s ;
 electrotermico 0.1 mN-1 N, 20-350 s ; electrospray 20 uN-20 mN, 225-3000 s ; ionico de rejillas 0.1-20 mN, 500-3000 s ; Hall 0.25-55 mN, 200-1920 s ;
 pulsado/arco de vacio 4-500 uN, 87-3200 s ; el empuje electrico queda por debajo de ~75 mN/kW.
ILUSTRATIVOS (sinteticos): m0 = 1000 kg, Delta-v = 3000 m/s, potencia disponible 5 kW (solo para los electricos), eficiencia 0.6, y la eleccion de un valor representativo dentro de cada rango:
Isp = media geometrica del rango; empuje = menor entre el maximo del rango, el tope de 75 mN/kW x P y 2 eta P/Ve (para los electricos).
Modelo: propelente m_p = m0 (1 - exp(-dv/Ve)) (empuje impulsivo); tiempo t = m0 dv / F (aproximacion de masa constante); no se incluyen masa del propulsor ni de la planta de potencia.
Se supone UN solo propulsor trabajando al empuje representativo. Esto compara RANGOS, no productos ni misiones; no es una recomendacion operativa.
Segunda via: frente de Pareto por comparacion exhaustiva y por barrido ordenado.
Tolerancia: ambos frentes identicos.
"""
from __future__ import annotations
import math, platform

G0 = 9.80665
M0, DV, P, ETA = 1000.0, 3000.0, 5000.0, 0.6
# nombre: (Fmin, Fmax [N], Ispmin, Ispmax [s], electrico)
ARQ = {
    "hidracina mono": (0.25, 28.0, 180.0, 285.0, False),
    "alternativos mono/bi": (0.05, 22.0, 150.0, 310.0, False),
    "gas frio": (10e-6, 3.6, 40.0, 110.0, False),
    "electrotermico": (0.1e-3, 1.0, 20.0, 350.0, True),
    "electrospray": (20e-6, 20e-3, 225.0, 3000.0, True),
    "ionico de rejillas": (0.1e-3, 20e-3, 500.0, 3000.0, True),
    "Hall": (0.25e-3, 55e-3, 200.0, 1920.0, True),
    "pulsado/arco de vacio": (4e-6, 500e-6, 87.0, 3200.0, True),
}


def evaluar(f_min, f_max, i_min, i_max, el):
    isp = math.sqrt(i_min * i_max)
    ve = isp * G0
    f = f_max
    if el:
        f = min(f, 75e-6 * P, 2 * ETA * P / ve)
    mp = M0 * (1 - math.exp(-DV / ve))
    t = M0 * DV / f
    return isp, f, mp, t


def pareto_exhaustivo(pts):
    r = []
    for i, (a, b) in enumerate(pts):
        dom = any((c <= a and d <= b) and (c < a or d < b) for j, (c, d) in enumerate(pts) if j != i)
        if not dom:
            r.append(i)
    return r


def pareto_barrido(pts):
    orden = sorted(range(len(pts)), key=lambda i: (pts[i][0], pts[i][1]))
    mejor_b = math.inf
    r = []
    for i in orden:
        if pts[i][1] < mejor_b:
            r.append(i)
            mejor_b = pts[i][1]
    return sorted(r)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Comparacion NO operativa por RANGOS publicados: m0 = {M0:.0f} kg, dv = {DV:.0f} m/s, P = {P/1e3:.0f} kW (ILUSTRATIVOS)")
    print(" arquitectura            Isp rep [s]   F rep [N]    m_prop [kg]   t [dias]")
    nombres, pts = [], []
    for n, (fa, fb, ia, ib, el) in ARQ.items():
        isp, f, mp, t = evaluar(fa, fb, ia, ib, el)
        nombres.append(n)
        pts.append((mp, t))
        print(f" {n:<22} {isp:>10.1f} {f:>12.4g} {mp:>14.2f} {t/86400:>10.2f}")
    a, b = pareto_exhaustivo(pts), pareto_barrido(pts)
    assert a == b, (a, b)
    print("Frente de Pareto (menos propelente y menos tiempo; sin masa de planta ni de propulsor):")
    for i in a:
        print(f"  {nombres[i]:<22} m_prop = {pts[i][0]:.2f} kg ; t = {pts[i][1]/86400:.2f} dias")
    print("Dominadas:", ", ".join(nombres[i] for i in range(len(nombres)) if i not in a) or "ninguna")
    # sensibilidad a la potencia
    print("Sensibilidad: tiempo del Hall y del ionico con P = 0.1, 0.5, 1 y 5 kW:")
    for pp in (100.0, 500.0, 1000.0, 5000.0):
        for n in ("Hall", "ionico de rejillas"):
            fa, fb, ia, ib, el = ARQ[n]
            isp = math.sqrt(ia * ib)
            ve = isp * G0
            f = min(fb, 75e-6 * pp, 2 * ETA * pp / ve)
            print(f"  P = {pp/1e3:>5.1f} kW {n:<20} F = {f*1e3:>6.2f} mN ; t = {M0*DV/f/86400:>9.1f} dias")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
