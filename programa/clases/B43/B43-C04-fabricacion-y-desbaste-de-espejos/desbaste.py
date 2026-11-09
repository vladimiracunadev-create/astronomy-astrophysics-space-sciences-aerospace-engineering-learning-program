#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C04: fabricacion y desbaste de espejos: sagita, esferometro, volumen de vidrio y plan de abrasivos.

Datos: ILUSTRATIVOS (espejo de D = 200 mm, f/6 -> distancia focal 1200 mm, R = 2400 mm; espesor 33 mm; densidad 2230 kg/m^3; tamanos de grano, tasas de arranque y regla de dano subsuperficial ~ 2 x grano son valores
tipicos de orden de magnitud NO consultados en un manual). Sin constantes externas.
Modelo: sagita exacta s = R - sqrt(R^2 - a^2) frente a la aproximacion a^2/(2R); esferometro de tres patas sobre un circulo de radio l: R = (l^2 + h^2)/(2h), contrastado con una biseccion numerica y con la formula por el lado del triangulo R = L^2/(6h) + h/2;
volumen del casquete esferico V = pi s (3 a^2 + s^2)/6 frente a la integral numerica de 2 pi y (s - sag(y)) dy (regla de Simpson);
plan de abrasivos: cada etapa debe retirar al menos el dano de la anterior (2 x grano) y el tiempo es retiro/tasa.
Supuestos: superficie esferica ideal, sin bisel; el plan de abrasivos es un modelo de balance, no un procedimiento de taller. Validez: orden de magnitud.
Tolerancia: casquete analitico frente a numerico, 1e-9 relativo; esferometro, 1e-12 relativo.
"""
from __future__ import annotations
import math, platform

D = 0.200; A = D / 2; R = 2.4; RHO = 2230.0

def sag(y, R=R):
    return R - math.sqrt(R * R - y * y)

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def calc():
    r = {}
    s = sag(A)
    r["sagita_exacta_mm"] = s * 1e3; r["sagita_aprox_mm"] = A * A / (2 * R) * 1e3
    r["sagita_parabola_mm"] = D * D / (16 * (R / 2)) * 1e3
    l = 0.05
    h = sag(l)
    r["h_esferometro_mm"] = h * 1e3
    r["R_esferometro_mm"] = (l * l + h * h) / (2 * h) * 1e3
    lo, hi = 0.5, 10.0  # biseccion independiente: R tal que sag_R(l) = h
    for _ in range(200):
        mid = (lo + hi) / 2
        if sag(l, mid) > h:
            lo = mid
        else:
            hi = mid
    r["R_biseccion_mm"] = (lo + hi) / 2 * 1e3
    side = l * math.sqrt(3)
    r["R_lado_mm"] = (side * side / (6 * h) + h / 2) * 1e3
    V = math.pi * s * (3 * A * A + s * s) / 6
    Vn = simpson(lambda y: 2 * math.pi * y * (s - sag(y)), 0.0, A)
    r["V_analitico_cm3"] = V * 1e6; r["V_numerico_cm3"] = Vn * 1e6
    r["masa_retirada_g"] = V * RHO * 1e3
    r["masa_blanco_g"] = math.pi * A * A * 0.033 * RHO * 1e3
    etapas = [("grano 1", 150.0, 60.0), ("grano 2", 80.0, 30.0), ("grano 3", 40.0, 15.0), ("grano 4", 20.0, 8.0), ("grano 5", 9.0, 4.0)]  # um, tasa um/min ILUSTRATIVA
    tot = 0.0; plan = []
    prev = None
    for n, g, rate in etapas:
        retiro = 2 * (prev if prev else g)  # dano de la etapa anterior
        t = retiro / rate
        plan.append((n, g, retiro, t)); tot += t
        prev = g
    r["plan"] = plan; r["t_total_min"] = tot
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        if k != "plan":
            print(f"{k} = {v:.8g}")
    print("etapa | grano (um) | retiro (um) | tiempo (min)")
    for n, g, ret, t in r["plan"]:
        print(f"{n} | {g:.0f} | {ret:.0f} | {t:.2f}")
    assert abs(r["V_analitico_cm3"] - r["V_numerico_cm3"]) / r["V_analitico_cm3"] < 1e-9
    assert abs(r["R_esferometro_mm"] - 2400.0) / 2400.0 < 1e-12
    assert abs(r["sagita_exacta_mm"] - r["sagita_aprox_mm"]) < 0.01
    assert abs(r["R_biseccion_mm"] - 2400.0) < 1e-6 and abs(r["R_lado_mm"] - 2400.0) < 1e-6
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
