#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C10: capa de Chapman, tasa de fotolisis y vida fotoquimica.

Datos: k y N_A de NIST CODATA 2022 (consulta 2026-11-09). Seccion eficaz de absorcion, flujo fotonico, densidad de la base y altura de escala son
SINTETICOS e ILUSTRATIVOS (no corresponden a una especie ni a una banda medida).
Modelo: atmosfera isoterma n(z) = n0 exp(-z/H); absorbente de seccion sigma; profundidad optica tau(z) = sigma n(z) H / cos(chi);
tasa de produccion q(z) = sigma F n(z) exp(-tau). Maximo analitico en tau = 1: z_m = H ln(sigma n0 H / cos chi); q_m = F cos(chi)/(e H).
Supuestos: haz monocromatico, plano-paralelo (chi < 70 grados), sin dispersion. Tolerancia: maximo numerico frente al analitico, 0.5 % de H; q_m 1e-4 relativo.
"""
import math, platform
print(f"Python {platform.python_version()} (biblioteca estandar)")
H, n0, sigma, F = 7.0e3, 2.5e25, 1.0e-23, 1.0e18   # m, 1/m3, m2 (sintetico), fotones m^-2 s^-1 (sintetico)
print("chi [grados]   z_m analitico [km]   z_m numerico [km]   q_m analitico [m^-3 s^-1]   q_m numerico")
for chi in (0.0, 30.0, 60.0, 70.0):
    c = math.cos(math.radians(chi))
    zm = H * math.log(sigma * n0 * H / c)
    qm = F * c / (math.e * H)
    best, qb = 0.0, 0.0
    for i in range(0, 150001):
        z = i
        n = n0 * math.exp(-z / H)
        q = sigma * F * n * math.exp(-sigma * n * H / c)
        if q > qb: qb, best = q, z
    print(f"{chi:11.1f} {zm/1e3:19.3f} {best/1e3:19.3f} {qm:27.4e} {qb:16.4e}")
    assert abs(best - zm) < 0.005 * H and abs(qb - qm) / qm < 1e-4
# la capa sube en altura de unos H ln(1/cos chi) al aumentar el angulo cenital
print(f"Desplazamiento de la capa entre chi=0 y 70 grados: {H*math.log(1/math.cos(math.radians(70)))/1e3:.2f} km")
# tasa de fotolisis J(z) = sigma F exp(-tau) y vida fotoquimica 1/J
print("z [km]   tau (chi=0)   J [1/s]   vida 1/J [h]")
for z in (60e3, 80e3, 100e3, 120e3):
    n = n0 * math.exp(-z / H); tau = sigma * n * H
    J = sigma * F * math.exp(-tau)
    print(f"{z/1e3:6.0f} {tau:12.3e} {J:10.3e} {1/J/3600:12.3e}")
J_top = sigma * F
assert math.isclose(J_top, 1.0e-5, rel_tol=1e-12)
# equilibrio fotoquimico sencillo: dn/dt = P - L n con P y L constantes; solucion exacta n(t) = n_eq + (n_0 - n_eq) exp(-L t)
P_, L_ = 2.0e9, 1.0e-4; n_eq = P_ / L_
n, dt = 0.0, 10.0
for _ in range(int(5 / L_ / dt)):
    n += dt * (P_ - L_ * n)
ex = n_eq * (1 - math.exp(-5.0))
print(f"Equilibrio: n tras 5 vidas = {n:.4e} ; exacto = {ex:.4e} ; n_eq = {n_eq:.4e} m^-3")
assert abs(n - ex) / ex < 1e-3
print("Pruebas superadas.")
