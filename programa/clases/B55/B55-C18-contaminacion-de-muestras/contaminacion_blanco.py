#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C18: sustraccion de blanco, limite de deteccion y sedimentacion de particulas (Stokes) para una muestra SINTETICA.

Datos: SINTETICOS / ILUSTRATIVOS. Blancos de procedimiento (6 replicas) con media 2.0 y desviacion 0.5 ng; muestra medida 5.0 ng con incertidumbre 0.4 ng; viscosidad del aire 1.8e-5 Pa s,
densidad de particula 2000 kg m-3, g = 9.80665 m s-2 (valor convencional), radios de 1 a 10 um. Ningun valor procede de una medicion. La pagina institucional del COSPAR sobre proteccion planetaria
(consultada el 2026-11-09) se cita como contexto normativo: la politica 2026 existe y distingue requisitos segun el cuerpo y la mision; no se leyeron sus categorias.
Modelo: neta = medida - media del blanco ; sigma_neta = sqrt(sigma_med^2 + s_blanco^2 / n) ; LOD = 3 s_blanco ; LOQ = 10 s_blanco ; velocidad de Stokes v = 2 r^2 (rho_p - rho_a) g / (9 eta).
Supuestos: blanco estable y aditivo; particulas esfericas en regimen de Stokes (Reynolds << 1). Validez: ilustrativa.
Tolerancia: propagacion analitica vs Monte Carlo a 3 %; Stokes: numero de Reynolds < 0.1 para los radios usados.
"""
from __future__ import annotations
import math, platform, random

ETA, RHO_P, RHO_A, G = 1.8e-5, 2000.0, 1.2, 9.80665

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n, b, s = 6, 2.0, 0.5
    med, s_med = 5.0, 0.4
    neta = med - b
    s_neta = math.sqrt(s_med ** 2 + s ** 2 / n)
    lod, loq = 3 * s, 10 * s
    print("A. Muestra SINTETICA: blanco de 6 replicas (media 2.0 ng, desviacion 0.5 ng) ; medida 5.0 +- 0.4 ng")
    print(f"B. Senal neta = {neta:.3f} ng ; incertidumbre = {s_neta:.4f} ng ; LOD = 3 s = {lod:.2f} ng ; LOQ = 10 s = {loq:.2f} ng")
    print(f"   Neta/LOD = {neta / lod:.2f} ; Neta/LOQ = {neta / loq:.2f}  => {'por encima' if neta > lod else 'por debajo'} del LOD y {'por encima' if neta > loq else 'por debajo'} del LOQ")
    # Monte Carlo
    rng = random.Random(2468)
    vals = []
    for _ in range(100000):
        bl = [rng.gauss(b, s) for _ in range(n)]
        m_b = sum(bl) / n
        vals.append(rng.gauss(med, s_med) - m_b)
    mm = sum(vals) / len(vals)
    sd = math.sqrt(sum((v - mm) ** 2 for v in vals) / (len(vals) - 1))
    print(f"C. Monte Carlo (100000, semilla 2468): neta = {mm:.4f} ng ; desviacion = {sd:.4f} ng ; analitica {s_neta:.4f} ng")
    assert abs(sd - s_neta) / s_neta < 0.03
    assert abs(mm - neta) < 0.01
    print("D. Efecto de la incertidumbre del blanco sobre la neta (la muestra no cambia)")
    print("s_blanco [ng]   sigma_neta [ng]   LOD [ng]   neta/LOD")
    for sb in (0.1, 0.25, 0.5, 1.0):
        print(f"{sb:12.2f}   {math.sqrt(s_med ** 2 + sb ** 2 / n):14.4f}   {3 * sb:8.2f}   {neta / (3 * sb):8.2f}")
    print("E. Sedimentacion por Stokes en aire (rho_p = 2000 kg/m3, eta = 1.8e-5 Pa s)")
    print("radio [um]   v [mm/s]   tiempo para caer 1 m [h]   Reynolds")
    for r_um in (1.0, 2.0, 5.0, 10.0):
        r = r_um * 1e-6
        v = 2 * r * r * (RHO_P - RHO_A) * G / (9 * ETA)
        re = RHO_A * v * 2 * r / ETA
        print(f"{r_um:8.1f}   {v * 1e3:9.4f}   {1.0 / v / 3600:14.3f}   {re:9.2e}")
        assert re < 0.1, (r_um, re)
    v1 = 2 * (1e-6) ** 2 * (RHO_P - RHO_A) * G / (9 * ETA)
    v10 = 2 * (1e-5) ** 2 * (RHO_P - RHO_A) * G / (9 * ETA)
    assert abs(v10 / v1 - 100.0) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
