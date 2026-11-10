#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C07: separacion de etapas a nivel conceptual (numero de etapas y conservacion de la cantidad de movimiento).

Datos consultados (2026-11-10): ecuacion de cohete ideal (NASA Glenn); g0 = 9.80665 m/s2 (NIST CODATA 2022).
ILUSTRATIVOS (sinteticos): DV total 9400 m/s, Isp = 330 s en todas las etapas, eps = 0.08, carga util 1000 kg; separacion de dos cuerpos de 5000 kg
(etapa gastada) y 8000 kg (resto) con energia de resorte de 3000 J, sobre un eje 1D en el marco inercial del vehiculo antes de separar.
Sistema: velocidades en el marco del centro de masa antes de la separacion (inercial), SI.
Modelo: N etapas iguales con DV/N cada una: masa de despegue = PL/pi^N con pi = (exp(-DV/(N c)) - eps)/(1-eps).
Separacion: conservacion de la cantidad de movimiento m1 v1 + m2 v2 = 0 y de la energia del resorte (1/2)m1 v1^2 + (1/2)m2 v2^2 = E.
Segunda via: se recalcula la energia cinetica con las velocidades obtenidas y la cantidad de movimiento total.
Tolerancias: cantidad de movimiento y energia 1e-12 relativa.
"""
import math, platform

G0, DV, ISP, EPS, PL = 9.80665, 9400.0, 330.0, 0.08, 1000.0


def glow(n):
    c = ISP * G0
    pi = (math.exp(-DV / (n * c)) - EPS) / (1.0 - EPS)
    return None if pi <= 0 else PL / pi ** n, pi


def separacion(m1, m2, e):
    # v1 = -(m2/m1) v2 ; E = 0.5 m1 v1^2 + 0.5 m2 v2^2 = 0.5 m2 v2^2 (1 + m2/m1)
    v2 = math.sqrt(2 * e / (m2 * (1 + m2 / m1)))
    v1 = -m2 / m1 * v2
    return v1, v2


def calcular():
    r = {"etapas": []}
    for n in (1, 2, 3, 4, 6):
        g = glow(n)
        r["etapas"].append((n, None if g is None else g[0], None if g is None else g[1]))
    m1, m2, e = 5000.0, 8000.0, 3000.0
    v1, v2 = separacion(m1, m2, e)
    r["v1"], r["v2"], r["vrel"] = v1, v2, v2 - v1
    r["p_tot"] = m1 * v1 + m2 * v2
    r["e_tot"] = 0.5 * m1 * v1 ** 2 + 0.5 * m2 * v2 ** 2
    r["err_e"] = abs(r["e_tot"] - e) / e
    r["err_p"] = abs(r["p_tot"]) / (m1 * abs(v1))
    # el decremento de masa por etapa extra
    validas = [x for x in r["etapas"] if x[1] is not None]
    r["mejora"] = [(validas[i][0], validas[i + 1][0], validas[i][1] - validas[i + 1][1]) for i in range(len(validas) - 1)]
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Lanzador SINTETICO: DV = {DV:.0f} m/s, Isp = {ISP} s, eps = {EPS}, carga util = {PL:.0f} kg")
    print(" N etapas   pi por etapa   masa de despegue [kg]")
    for n, g, pi in r["etapas"]:
        if g is None:
            print(f"  {n:6d}   inalcanzable (pi <= 0)")
        else:
            print(f"  {n:6d}   {pi:12.4f}   {g:14.1f}")
    print("Ahorro al anadir una etapa (kg): " + "; ".join(f"{a}->{b}: {d:.0f}" for a, b, d in r["mejora"]))
    print(f"Separacion 1D (5000 kg y 8000 kg, resorte 3000 J): v1 = {r['v1']:.4f} m/s, v2 = {r['v2']:.4f} m/s, v relativa = {r['vrel']:.4f} m/s")
    print(f"Cantidad de movimiento total = {r['p_tot']:.2e} kg m/s (error relativo {r['err_p']:.1e}); energia = {r['e_tot']:.6f} J (error relativo {r['err_e']:.1e})")
    assert r["err_e"] < 1e-12 and r["err_p"] < 1e-12
    assert r["etapas"][0][1] is None or r["etapas"][0][1] > r["etapas"][1][1]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
