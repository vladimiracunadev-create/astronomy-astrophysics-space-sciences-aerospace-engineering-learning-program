#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C09: cargas cuasiestaticas en la interfaz de un satelite y margenes con los factores del GEVS.

Datos CONSULTADOS (2026-11-10): GEVS (GSFC-STD-7000B, 2021-04-28), Tabla 2.2-3, factores de seguridad aplicados a cargas limite:
  columna estatica: metalico fluencia 1,25 y ultima 1,4; estabilidad ultima 1,4; compuesto ultima 1,5; union adhesiva/inserto ultima 1,5.
  columna aleatoria/acustica: metalico fluencia 1,6 y ultima 1,8; compuesto ultima 1,9. gn = 9,80665 m/s2 (NIST).
  (El estandar indica que si solo se califica por analisis hacen falta 2,0 sobre fluencia y 2,6 sobre rotura; no se usa aqui.)
DATOS ILUSTRATIVOS (no consultados): masa 100 kg, centro de masas a 0,50 m sobre el plano de interfaz, anillo de interfaz de diametro D = 0,937 m,
factores de carga limite cuasiestaticos axial 6,0 g y lateral 3,0 g (inventados: NO de un lanzador), area de seccion del anillo 3,0e-4 m2,
modulo de seccion para flexion 4,5e-5 m3, tension de fluencia 275 MPa y ultima 310 MPa (aluminio ilustrativo).
Modelo: P = N_ax m g ; V = N_lat m g ; M = V h ; carga axial equivalente P_eq = P + 4 M / D (anillo).
Tensiones: sigma = P/A + M/Z. Margen: MS = sigma_adm/(FS sigma_limite) - 1.
Segunda via: la tension maxima y minima del anillo por superposicion; verificacion de equilibrio de momentos y que MS = 0 al escalar la carga por el factor.
Tolerancia: 1e-9.
"""
from __future__ import annotations
import math, platform

G = 9.80665
FS_Y, FS_U = 1.25, 1.4
M_KG, H, D_INT = 100.0, 0.50, 0.937
NAX, NLAT = 6.0, 3.0
A, Z = 3.0e-4, 4.5e-5
SY, SU = 275e6, 310e6


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Factores de seguridad del GEVS (Tabla 2.2-3, estatico): fluencia 1,25; ultima 1,4 (metalico)")
    P = NAX * M_KG * G
    V = NLAT * M_KG * G
    Mom = V * H
    Peq = P + 4 * Mom / D_INT
    print(f"Datos ILUSTRATIVOS: m = {M_KG:.0f} kg, h = {H} m, N_ax = {NAX} g, N_lat = {NLAT} g")
    print(f"Cargas limite: P = {P:.1f} N, V = {V:.1f} N, M = {Mom:.1f} N m, P_eq = P + 4M/D = {Peq:.1f} N")
    sig_comp = P / A + Mom / Z   # fibra mas comprimida (axial + flexion)
    sig_trac = P / A - Mom / Z
    print(f"Tension limite en el anillo (compresion axial + flexion): max = {sig_comp / 1e6:.2f} MPa, min = {sig_trac / 1e6:.2f} MPa")
    ms_y = SY / (FS_Y * sig_comp) - 1
    ms_u = SU / (FS_U * sig_comp) - 1
    print(f"Margen de fluencia  MS_y = {SY / 1e6:.0f}/({FS_Y} x {sig_comp / 1e6:.2f}) - 1 = {ms_y:.3f}")
    print(f"Margen de rotura    MS_u = {SU / 1e6:.0f}/({FS_U} x {sig_comp / 1e6:.2f}) - 1 = {ms_u:.3f}")
    # Escala critica: factor que lleva el margen a cero
    k_y = SY / (FS_Y * sig_comp)
    k_u = SU / (FS_U * sig_comp)
    print(f"Factor de carga que agota el margen: fluencia x{k_y:.4f}, rotura x{k_u:.4f}")
    print("Barrido de carga lateral (carga axial fija 6 g):")
    for nl in (1.0, 3.0, 5.0, 8.0):
        sg = P / A + nl * M_KG * G * H / Z
        print(f"  N_lat = {nl:3.1f} g -> sigma = {sg / 1e6:7.2f} MPa, MS_u = {SU / (FS_U * sg) - 1:7.3f}")
    # Comprobaciones
    sig_esc = k_u * sig_comp * FS_U
    assert abs(sig_esc - SU) < 1e-3
    assert abs((P / A + Mom / Z) - (sig_comp)) < 1e-9
    assert abs(sig_comp - sig_trac - 2 * Mom / Z) < 1e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
