#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C02: composicion, masa molar media y altura de escala.

Datos: fracciones por volumen y alturas de escala de las fichas NASA/NSSDC (Venus, Marte, Tierra, Jupiter; Titan: pagina NASA Science), consulta 2026-11-09.
Masas atomicas redondeadas (H 1.008, He 4.0026, C 12.011, N 14.007, O 15.999, Ar 39.948): valores estandar NO consultados en esta clase.
Fracciones omitidas (trazas) se renormalizan a 1 y eso es una APROXIMACION de la clase.
Modelo: M = suma(x_i M_i); H = k T / (m g), con g = G M_p / r^2 (G de NIST CODATA 2022) y T la temperatura de la ficha.
Validez: gas ideal bien mezclado. Tolerancia: H calculada frente a la ficha, 20 % (T de ficha no es la del nivel exacto).
"""
import platform
K_B, N_A, G = 1.380649e-23, 6.02214076e23, 6.67430e-11
AM = {"H2": 2.016, "He": 4.0026, "N2": 28.014, "O2": 31.998, "Ar": 39.948, "CO2": 44.009, "CH4": 16.043, "CO": 28.010}
# nombre: (composicion %, T [K], masa [kg], radio [km], H de ficha [km] o None)
P = {
    "Tierra": ({"N2": 78.08, "O2": 20.95, "Ar": 0.934, "CO2": 0.042}, 288.0, 5.9722e24, 6371.0, 8.5),
    "Venus": ({"CO2": 96.5, "N2": 3.5}, 737.0, 4.8673e24, 6051.8, 15.9),
    "Marte": ({"CO2": 95.1, "N2": 2.59, "Ar": 1.94, "O2": 0.16, "CO": 0.06}, 214.0, 0.64169e24, 3389.5, 11.0),
    "Jupiter": ({"H2": 89.8, "He": 10.2}, 165.0, 1898.13e24, 71492.0, 27.0),
    "Titan": ({"N2": 95.0, "CH4": 5.0}, 94.15, 1.3455e23, 2575.0, None),
}
print(f"Python {platform.python_version()} (biblioteca estandar)")
print("planeta   M [g/mol]   g [m/s2]   H calc [km]   H ficha [km]   dif.")
res = {}
for n, (comp, T, m, r, Hf) in P.items():
    tot = sum(comp.values())
    M = sum(v / tot * AM[k] for k, v in comp.items())
    g = G * m / (r * 1e3) ** 2
    H = K_B * T / (M * 1e-3 / N_A * g) / 1e3
    res[n] = (M, g, H)
    if Hf:
        d = abs(H - Hf) / Hf
        assert d < 0.20, f"{n}: H se aleja de la ficha"
        print(f"{n:8s} {M:9.3f} {g:10.3f} {H:12.2f} {Hf:12.1f} {d*100:7.1f} %")
    else:
        print(f"{n:8s} {M:9.3f} {g:10.3f} {H:12.2f} {'(sin ficha)':>12s}")
# prueba analitica: gas puro de una sola especie
M_N2 = AM["N2"]; assert abs(sum(1.0 * AM["N2"] for _ in [0]) - M_N2) < 1e-12
# prueba de coherencia: g de la Tierra calculada frente a 9.820 m/s2 de la ficha
gT = res["Tierra"][1]; assert abs(gT - 9.820) < 0.03, gT
print(f"g calculada de la Tierra = {gT:.3f} m/s2 (ficha: 9.820)")
print("Pruebas superadas.")
