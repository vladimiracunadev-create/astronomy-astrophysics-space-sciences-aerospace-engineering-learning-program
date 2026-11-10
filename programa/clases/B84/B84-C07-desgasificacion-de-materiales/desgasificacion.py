#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C07: TML, RML, WVR y CVCM de un ensayo tipo ASTM E595 y difusion de un volatil desde una lamina.

El GEVS (GSFC-STD-7000B, 2021-04-28, leido el 2026-11-10) nombra ASTM E595 como cribado de estabilidad al vacio que debe imponerse como minimo; la
pagina de la base de datos de desgasificacion del NASA/GSFC (consultada 2026-11-10) nombra TML, WVR y CVCM como campos. NO se consultaron los limites
numericos ni las condiciones de ensayo de ASTM E595 (se usan como criterios ILUSTRATIVOS: TML <= 1,0 % y CVCM <= 0,10 %, ensayo a 125 C y 24 h).
DATOS SINTETICOS (pesadas inventadas, en mg): masa inicial m_i, masa final en vacio m_f, masa tras reacondicionar con humedad m_h,
ganancia de masa del colector dc. TML = (m_i - m_f)/m_i; WVR = (m_h - m_f)/m_i; RML = TML - WVR; CVCM = dc/m_i (todo en %).
Difusion: lamina de espesor L = 2 mm con desorcion por una cara (la otra es impermeable); fraccion remanente
  F(t) = sum_k 8/((2k+1)^2 pi^2) exp(-(2k+1)^2 pi^2 D t/(4 L^2)), D(T) = D0 exp(-Ea/(R T)) con D0 = 1e-3 m2/s, Ea = 60 kJ/mol (ILUSTRATIVOS).
Segunda via: diferencias finitas explicitas (condicion Fo <= 0,5). Tolerancia: serie frente a diferencias finitas < 5e-3 absoluto en F.
"""
from __future__ import annotations
import math, platform

R = 8.314462618  # J/(mol K) (CODATA 2018; no consultado en esta sesion)
MUESTRAS = {  # mi, mf, mh, dc [mg]
    "Epoxi A (SINTETICO)": (500.00, 497.10, 498.25, 0.20),
    "Silicona B (SINTETICO)": (500.00, 495.40, 495.65, 0.95),
    "Adhesivo C (SINTETICO)": (500.00, 498.90, 499.40, 0.15),
    "Cinta D (SINTETICO)": (500.00, 489.50, 493.00, 1.80),
}
TML_MAX, CVCM_MAX = 1.0, 0.10  # criterios ILUSTRATIVOS (no consultados)


def serie(Fo, terminos=200):
    return sum(8 / ((2 * k + 1) ** 2 * math.pi ** 2) * math.exp(-((2 * k + 1) ** 2) * math.pi ** 2 * Fo / 4) for k in range(terminos))


def fd(Fo_final, n=40):
    """Placa 0 < x < 1, c = 1 inicial, c(1) = 0 (cara abierta), flujo nulo en x = 0. Devuelve la media de c."""
    dx = 1.0 / n
    dt = 0.4 * dx * dx
    c = [1.0] * (n + 1)
    c[n] = 0.0
    t = 0.0
    while t < Fo_final - 1e-15:
        h = min(dt, Fo_final - t)
        nuevo = c[:]
        nuevo[0] = c[0] + 2 * h / dx ** 2 * (c[1] - c[0])
        for i in range(1, n):
            nuevo[i] = c[i] + h / dx ** 2 * (c[i + 1] - 2 * c[i] + c[i - 1])
        nuevo[n] = 0.0
        c = nuevo
        t += h
    # media por trapecio
    return (sum(c[1:n]) + 0.5 * (c[0] + c[n])) * dx


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Cribado tipo E595 con pesadas SINTETICAS (criterios ILUSTRATIVOS: TML <= 1,0 %, CVCM <= 0,10 %):")
    print(f"{'muestra':24s} {'TML %':>7s} {'WVR %':>7s} {'RML %':>7s} {'CVCM %':>7s}  veredicto")
    for n, (mi, mf, mh, dc) in MUESTRAS.items():
        tml = (mi - mf) / mi * 100
        wvr = (mh - mf) / mi * 100
        rml = tml - wvr
        cv = dc / mi * 100
        ok = tml <= TML_MAX and cv <= CVCM_MAX
        print(f"{n:24s} {tml:7.3f} {wvr:7.3f} {rml:7.3f} {cv:7.3f}  {'pasa' if ok else 'NO pasa'}")
    L = 2e-3
    print(f"Difusion en lamina de L = {L * 1e3:.0f} mm, D0 = 1e-3 m2/s, Ea = 60 kJ/mol (ILUSTRATIVOS):")
    print(f"{'T [C]':>6s} {'D [m2/s]':>11s} {'tau=L2/D [h]':>13s} {'F(24 h)':>9s} {'t(99 %) [dias]':>15s}")
    for Tc in (20.0, 60.0, 125.0):
        T = Tc + 273.15
        D = 1e-3 * math.exp(-60e3 / (R * T))
        tau = L * L / D
        F24 = serie(D * 86400 / L ** 2)
        # tiempo para F = 0,01
        lo, hi = 1e-6, 1e4
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            if serie(mid) > 0.01:
                lo = mid
            else:
                hi = mid
        t99 = math.sqrt(lo * hi) * L * L / D / 86400
        print(f"{Tc:6.0f} {D:11.3e} {tau / 3600:13.3e} {F24:9.4f} {t99:15.3e}")
    # Comprobacion por diferencias finitas
    dif = 0.0
    for Fo in (0.05, 0.2, 0.5, 1.0):
        a = serie(Fo)
        b = fd(Fo)
        dif = max(dif, abs(a - b))
        print(f"Fo = {Fo:4.2f}: serie = {a:.5f}  diferencias finitas = {b:.5f}")
    print(f"Diferencia maxima serie - diferencias finitas = {dif:.1e}")
    assert dif < 5e-3
    assert abs(serie(0.0) - 1.0) < 2e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
