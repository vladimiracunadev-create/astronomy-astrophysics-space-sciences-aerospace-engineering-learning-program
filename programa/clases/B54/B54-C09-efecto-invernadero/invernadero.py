#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C09: efecto invernadero en una atmosfera gris.

Datos: S, albedo de Bond, T de superficie de las fichas NASA/NSSDC (Venus, Tierra, Marte) y sigma de NIST CODATA 2022 (consulta 2026-11-09).
Modelo: atmosfera gris en equilibrio radiativo, T_s^4 = T_e^4 (1 + 3 tau/4), con tau la profundidad optica infrarroja vertical (aproximacion de dos corrientes);
una capa isoterma perfectamente absorbente en el IR da T_s = 2^(1/4) T_e. Se INVIERTE tau a partir de T_s observada.
Supuestos: sin conveccion ni nubes ni conveccion; el "tau" resultante es una medida EQUIVALENTE, no una medicion espectral. Tolerancia: reconstruccion de T_s 1e-9 K.
"""
import math, platform
SIG = 5.670374419e-8
F = {"Venus": (2601.3, 0.77, 737.0), "Tierra": (1361.0, 0.294, 288.0), "Marte": (586.2, 0.250, 214.0)}
print(f"Python {platform.python_version()} (biblioteca estandar)")
print("planeta   Te [K]   Ts obs [K]   Ts/Te   tau equivalente   flujo de superficie sigma Ts^4 [W/m2]")
for n, (S, A, Ts) in F.items():
    Te = (S * (1 - A) / (4 * SIG)) ** 0.25
    tau = (4 / 3) * ((Ts / Te) ** 4 - 1)
    Ts2 = Te * (1 + 0.75 * tau) ** 0.25
    assert abs(Ts2 - Ts) < 1e-9
    print(f"{n:8s} {Te:7.2f} {Ts:10.1f} {Ts/Te:7.3f} {tau:14.2f} {SIG*Ts**4:30.1f}")
# casos limite analiticos
Te = 255.0
assert math.isclose(Te * (1 + 0.75 * 0.0) ** 0.25, Te)
Ts_capa = 2 ** 0.25 * Te
print(f"Una capa isoterma opaca al IR: Ts = {Ts_capa:.2f} K (2^(1/4) Te = {2**0.25:.4f} Te)")
# balance de dos capas: flujos (modelo de una capa con emisividad eps) -> Ts^4 = Te^4 * 2/(2 - eps)
for eps in (0.0, 0.5, 0.78, 1.0):
    Ts = Te * (2 / (2 - eps)) ** 0.25
    print(f"  una capa con emisividad IR {eps:4.2f}: Ts = {Ts:7.2f} K  (Delta = {Ts-Te:5.1f} K)")
assert math.isclose(Te * (2 / (2 - 1.0)) ** 0.25, Ts_capa)
# eps necesaria para la Tierra con una sola capa
S, A, Ts = F["Tierra"]; Te_t = (S * (1 - A) / (4 * SIG)) ** 0.25
eps_t = 2 - 2 * (Te_t / Ts) ** 4
print(f"Tierra: emisividad de la capa que reproduce Ts = {Ts} K: {eps_t:.3f}")
# forzamiento por un cambio de tau: dTs = Ts * (3/16) dtau/(1 + 0.75 tau)
tau = (4 / 3) * ((288.0 / Te_t) ** 4 - 1)
dTs = 288.0 * 0.75 * 0.01 / (4 * (1 + 0.75 * tau))
Ts_b = Te_t * (1 + 0.75 * (tau + 0.01)) ** 0.25
print(f"+0.01 en tau: dTs analitico = {dTs:.4f} K ; exacto = {Ts_b-288.0:.4f} K")
assert abs(dTs - (Ts_b - 288.0)) < 1e-3
print("Pruebas superadas.")
