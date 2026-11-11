#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C04: otolitos como acelerometro y canales semicirculares como filtro pasa-altos (modelo DIDACTICO, SINTETICO).

Otolitos: miden la fuerza especifica f = a - g (aceleracion de la cabeza menos la gravedad). En la Tierra (g = 9.81 m/s2) una inclinacion
lateral theta da una componente g sin(theta) indistinguible de una traslacion a = g sin(theta): ambiguedad inclinacion-traslacion.
En orbita (caida libre) el termino de gravedad desaparece de f: la inclinacion no produce senal otolitica, solo la traslacion.
Canales: velocidad angular percibida w_p con tau dw_p/dt = -w_p + tau dw/dt (pasa-altos), tau = 5 s (ILUSTRATIVO). Rotacion constante w = 60 grados/s
desde t = 0: w_p = w exp(-t/tau). Integracion numerica de Euler con paso 0.01 s. Sin datos medidos. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

G = 9.81


def fuerza_especifica_lateral(theta_grados, a_lat, g):
    return a_lat - g * np.sin(np.radians(theta_grados))


def canal_correcto(w, dt, tau):
    wp = np.zeros_like(w)
    for i in range(1, len(w)):
        wp[i] = wp[i - 1] - dt / tau * wp[i - 1] + (w[i] - w[i - 1])
    return wp


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS/ILUSTRATIVOS: no hay mediciones; tau = 5 s y los angulos son de ensenanza")
    print("Fuerza especifica lateral f = a - g sin(theta) [m/s2]:")
    print("  caso                         Tierra (g = 9.81)   Orbita (g efectiva = 0)")
    for nombre, th, a in (("inclinacion 10 grados, a = 0", 10, 0.0), ("traslacion a = 1.70, sin inclinar", 0, 1.70), ("inclinacion 30 grados, a = 0", 30, 0.0)):
        print(f"  {nombre:30s} {fuerza_especifica_lateral(th, a, G):8.3f}            {fuerza_especifica_lateral(th, a, 0.0):8.3f}")
    th_eq = np.degrees(np.arcsin(1.70 / G))
    print(f"Ambiguedad: una traslacion de 1.70 m/s2 equivale en la Tierra a una inclinacion de {th_eq:.2f} grados")
    dt, tau = 0.01, 5.0
    t = np.arange(0, 30 + dt / 2, dt)
    w = np.full_like(t, 60.0)
    w[0] = 0.0
    wp = canal_correcto(w, dt, tau)
    for ts in (0.0, 5.0, 10.0, 15.0, 30.0):
        i = int(round(ts / dt))
        print(f"  t = {ts:4.1f} s: velocidad angular percibida = {wp[i]:6.2f} grados/s (verdad 60) ; analitica {60 * np.exp(-ts / tau):6.2f}")
    t10 = tau * np.log(10)
    print(f"Tiempo hasta que la percepcion cae al 10 % de la velocidad real = {t10:.2f} s")
    assert abs(fuerza_especifica_lateral(10, 0, G) + 1.703) < 0.01
    assert fuerza_especifica_lateral(10, 0, 0.0) == 0.0
    assert abs(th_eq - 9.98) < 0.05
    assert abs(wp[int(10 / dt)] - 60 * np.exp(-2)) < 0.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
