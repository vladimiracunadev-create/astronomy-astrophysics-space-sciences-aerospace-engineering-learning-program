#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C03: ventanas de lanzamiento Tierra-Marte y Tierra-Venus desde las longitudes medias (modelo circular y coplanar).

Datos consultados (2026-11-10): longitudes medias a J2000 de la tabla de posiciones aproximadas del JPL (baricentro Tierra-Luna 100.46457166 grados,
Marte -4.55343205, Venus 181.97909950) y periodos siderales de las fichas NASA/NSSDC (Tierra 365.256 d, Marte 686.980 d, Venus 224.701 d).
Semiejes de las fichas; GM_sol = 1.32712440e11 km3/s2 (valor estandar, no consultado en la pagina).
Modelo: longitud media L(t) = L0 + 360 t / P; ventana cuando L_destino - L_Tierra = fase de salida (C02). Se ignoran la excentricidad (Marte 0.0935)
y la inclinacion; por eso las fechas son orientativas (decenas de dias) y NO se comparan con fechas reales de lanzamiento (no consultadas).
Pruebas: (1) en cada ventana la separacion angular iguala la fase de salida (tol. 1e-6 grados); (2) el intervalo entre ventanas iguala el periodo sinodico (tol. 1e-6 d).
"""
import math, platform, datetime as dt
MU = 1.32712440e11
A = {"Venus": 108.210e6, "Tierra": 149.598e6, "Marte": 227.956e6}
P = {"Venus": 224.701, "Tierra": 365.256, "Marte": 686.980}
L0 = {"Venus": 181.97909950, "Tierra": 100.46457166, "Marte": -4.55343205}
J2000 = dt.datetime(2000, 1, 1, 12, 0, 0)


def ventanas(dest, n):
    tof = math.pi * math.sqrt((0.5 * (A["Tierra"] + A[dest])) ** 3 / MU) / 86400
    phi = 180.0 - 360.0 * tof / P[dest]
    syn = 1.0 / abs(1.0 / P["Tierra"] - 1.0 / P[dest])
    rate = 360.0 / P[dest] - 360.0 / P["Tierra"]
    s0 = L0[dest] - L0["Tierra"]
    t = (phi - s0) / rate
    while t < 0: t += syn
    while t - syn >= 0: t -= syn
    out = []
    for _ in range(n):
        out.append(t); t += syn
    return out, phi, rate, s0, syn


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for dest, n in (("Marte", 6), ("Venus", 6)):
        ts, phi, rate, s0, syn = ventanas(dest, n)
        print(f"{dest}: fase de salida = {phi:.3f} grados ; periodo sinodico = {syn:.3f} d ({syn/365.256:.3f} anios)")
        for t in ts:
            fecha = (J2000 + dt.timedelta(days=t)).strftime("%Y-%m-%d")
            sep = (s0 + rate * t - phi) % 360.0
            sep = min(sep, 360.0 - sep)
            assert sep < 1e-6, sep
            print(f"   salida (modelo) {fecha}  t = {t:9.2f} d desde J2000")
        gaps = [b - a for a, b in zip(ts, ts[1:])]
        assert all(abs(g - syn) < 1e-6 for g in gaps)
    print("Intervalos entre ventanas = periodo sinodico del modelo. Pruebas superadas.")


if __name__ == "__main__":
    main()
