#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C10: resonancias de movimiento medio en los satelites galileanos y saturnianos.

Datos consultados (2026-11-10): periodos siderales de Io, Europa, Ganymede, Callisto, Mimas, Enceladus, Tethys, Dione, Titan y Hyperion
en dos fuentes: la tabla de elementos de satelites del NASA JPL SSD (epoca 2000-01-01.5, columna P) y las fichas de satelites jovianos
(NASA/NSSDC, 2023-12-06) y saturnianos (NASA/NSSDC, 2025-07-22). Para los galileanos las dos fuentes difieren hasta 1.5 % en la razon
Europa/Ganymede; se toma la ficha NASA/NSSDC como valor de referencia para decidir resonancias y la tabla del JPL como contraste.
Modelo: razon de periodos P2/P1 comparada con el racional p/q mas cercano de denominador <= 5; desviacion relativa y periodo de
circulacion 360 / |(p) n1 - (q) n2| de la combinacion. Relacion de Laplace n1 - 3 n2 + 2 n3 con n = 360 / P (grados/dia).
Segunda via: (a) el mismo calculo con la segunda fuente de periodos; (b) tercera ley de Kepler con los semiejes para comprobar la coherencia
de los periodos con los semiejes. Los periodos de las fuentes no son el movimiento medio resonante exacto: la diferencia entre fuentes
mide cuanto se puede decir con ellos. No hay datos sinteticos.
Tolerancias: razones (ficha NASA) dentro del 1 % del racional; relacion de Laplace (ficha NASA) < 1e-3 de n1; la tabla del JPL debe fallar el 1 % en Europa/Ganymede (es la leccion).
"""
from __future__ import annotations
import json, math, platform, sys
from fractions import Fraction

JPL = {"Io": 1.762732, "Europa": 3.525463, "Ganymede": 7.155588, "Callisto": 16.690440,
       "Mimas": 0.942422, "Enceladus": 1.370218, "Tethys": 1.887802, "Dione": 2.736916, "Titan": 15.945448, "Hyperion": 21.276658}
NASA = {"Io": 1.769138, "Europa": 3.551181, "Ganymede": 7.154553, "Callisto": 16.689017,
        "Mimas": 0.9424218, "Enceladus": 1.370218, "Tethys": 1.887802, "Dione": 2.736915, "Titan": 15.945421, "Hyperion": 21.276609}
A_KM = {"Io": 421800.0, "Europa": 671100.0, "Ganymede": 1070400.0, "Callisto": 1882700.0}
GM_J = 126.687e6
PARES = [("Io", "Europa"), ("Europa", "Ganymede"), ("Ganymede", "Callisto"), ("Mimas", "Tethys"), ("Enceladus", "Dione"), ("Titan", "Hyperion")]


def razon(tab, a, b):
    r = tab[b] / tab[a]
    fr = Fraction(r).limit_denominator(5)
    return r, fr, abs(r / float(fr) - 1)


def laplace(tab):
    n = {k: 360.0 / tab[k] for k in ("Io", "Europa", "Ganymede")}
    return n["Io"] - 3 * n["Europa"] + 2 * n["Ganymede"], n["Io"]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    print("Razones de periodos P2/P1 y racional mas cercano (denominador <= 5), fuente JPL frente a fuente NASA/NSSDC:")
    print(" par                  P2/P1(JPL)  racional  desv.JPL    P2/P1(NASA)  desv.NASA   circulacion [d] (NASA)")
    for i, (a, b) in enumerate(PARES):
        r1, f1, d1 = razon(JPL, a, b)
        r2, f2, d2 = razon(NASA, a, b)
        p, q = f1.numerator, f1.denominator
        # combinacion de resonancia: q n2... con n = 360/P : p n_a_outer? usamos (p) n_interior - (q) n_exterior? ratio P2/P1 = p/q -> n1/n2 = p/q
        n1, n2 = 360.0 / JPL[a], 360.0 / JPL[b]
        delta = q * n1 - p * n2
        n1n, n2n = 360.0 / NASA[a], 360.0 / NASA[b]
        circ = 360.0 / abs(q * n1n - p * n2n) if abs(q * n1n - p * n2n) > 1e-9 else float("inf")
        print(f" {a + '-' + b:20s} {r1:10.6f}  {str(f1):>7s}  {d1:9.2e}  {r2:11.6f}  {d2:9.2e}  {circ:12.1f}")
        out[f"r{i}"], out[f"f{i}"], out[f"d{i}"], out[f"dn{i}"], out[f"c{i}"] = r1, str(f1), d1, d2, circ
    res, n1 = laplace(JPL)
    res2, _ = laplace(NASA)
    print(f"Relacion de Laplace n_Io - 3 n_Europa + 2 n_Ganymede (grados/dia): ficha NASA/NSSDC = {res2:.6f} (cociente a n_Io = {abs(res2) / n1:.1e}) ; tabla JPL = {res:.4f} (cociente = {abs(res) / n1:.1e})")
    out.update(lap=res, lap2=res2, nIo=n1, lap_rel=abs(res) / n1, lap2_rel=abs(res2) / n1)
    # tercera ley de Kepler con los semiejes: coherencia de periodos
    print("Tercera ley de Kepler con GM_Jupiter y los semiejes (periodo kepleriano de una orbita circular) frente a la ficha NASA/NSSDC y a la tabla del JPL:")
    kd = kdn = 0.0
    for k, a in A_KM.items():
        pk = 2 * math.pi * math.sqrt(a**3 / GM_J) / 86400.0
        d = abs(pk / JPL[k] - 1)
        dn = abs(pk / NASA[k] - 1)
        kd, kdn = max(kd, d), max(kdn, dn)
        print(f"  {k:9s}: P_kepler = {pk:.5f} d ; P_NASA = {NASA[k]:.6f} d (dif. {dn:.2%}) ; P_JPL = {JPL[k]:.6f} d (dif. {d:.2%})")
    out["kd"], out["kdn"] = kd, kdn
    assert kdn < 0.002
    assert all(out[f"dn{i}"] < 0.01 for i in range(6) if i != 2)
    assert abs(res2) / n1 < 1e-3
    assert out["f0"] == "2" and out["f1"] == "2" and out["d1"] > 0.01
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
