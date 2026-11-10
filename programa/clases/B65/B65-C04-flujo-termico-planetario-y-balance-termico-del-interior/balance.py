#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B65-C04: flujo termico, geotermo con produccion radiactiva, enfriamiento de la litosfera y balance de Urey.

Datos consultados: flujo total de la Tierra 47 +/- 2 TW (Davies y Davies 2010, Solid Earth 1, 5-24, solo el resumen); radio volumetrico medio 6371.000 km
(NASA/GSFC NSSDC, Earth Fact Sheet, actualizada 2024-11-15); consultas del 2026-11-09.
Datos ILUSTRATIVOS (sinteticos; no son medidas): k = 3.0 W m^-1 K^-1, kappa = 1e-6 m^2 s^-1, A = 1.0e-6 W m^-3, espesor de la capa radiactiva 30 km, T_m - T_s = 1300 K,
T_s = 273 K, calor radiactivo total del manto + corteza H = 20 TW, capacidad termica efectiva C = 7e27 J K^-1.
Modelo: (1) flujo medio = Q / (4 pi R^2); (2) geotermo estacionario k T'' = -A: solucion cerrada contra diferencias finitas (Dirichlet en ambos extremos) y flujo superficial;
(3) semiespacio que se enfria: flujo q = k dT / sqrt(pi kappa t) contra diferencias finitas explicitas; (4) razon de Urey y tasa de enfriamiento secular.
Sistema de referencia: z hacia abajo desde la superficie [m]. Supuestos: conduccion 1D, propiedades constantes. Validez: ilustrativa.
Tolerancia: flujo superficial FD frente a cerrado < 1e-6 relativo; flujo del semiespacio < 1 %.
"""
from __future__ import annotations
import math, platform

R_TIERRA, Q_TOTAL = 6.371e6, 47.0e12      # m, W (consultados)
K, KAPPA, A_RAD, L_RAD = 3.0, 1.0e-6, 1.0e-6, 30.0e3
TS, DT_MANTO = 273.0, 1300.0
H_RAD, C_TERM = 20.0e12, 7.0e27
ANIO = 3.15576e7

def geotermo_cerrado(z, q0):
    return TS + q0 * z / K - A_RAD * z * z / (2 * K)

def solve_bvp(N, T_L):
    """k T'' = -A con T(0)=TS, T(L)=T_L en N intervalos; devuelve (T, flujo en superficie con diferencia de 2.o orden)."""
    h = L_RAD / N
    a = [0.0] + [1.0] * (N - 1)
    b = [1.0] + [-2.0] * (N - 1)
    c = [0.0] + [1.0] * (N - 1)
    d = [TS] + [-A_RAD * h * h / K] * (N - 1)
    # Thomas para el sistema interno con T_N conocido
    d[N - 1] -= T_L
    n = N                        # incognitas 0..N-1 (indice 0 es el contorno)
    cp, dp = [0.0] * n, [0.0] * n
    cp[0], dp[0] = c[0] / b[0], d[0] / b[0]
    for i in range(1, n):
        m = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / m if i < n - 1 else 0.0
        dp[i] = (d[i] - a[i] * dp[i - 1]) / m
    T = [0.0] * n
    T[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        T[i] = dp[i] - cp[i] * T[i + 1]
    T.append(T_L)
    q = K * (-3 * T[0] + 4 * T[1] - T[2]) / (2 * h)
    return T, q

def semiespacio_fd(t_fin, N=400, zmax=300.0e3):
    h = zmax / N
    dt = 0.2 * h * h / KAPPA
    T = [TS + DT_MANTO] * (N + 1)
    T[0] = TS
    t = 0.0
    while t < t_fin:
        paso = min(dt, t_fin - t)
        Tn = T[:]
        for i in range(1, N):
            Tn[i] = T[i] + paso * KAPPA * (T[i + 1] - 2 * T[i] + T[i - 1]) / (h * h)
        T = Tn
        t += paso
    return K * (-3 * T[0] + 4 * T[1] - T[2]) / (2 * h)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    area = 4 * math.pi * R_TIERRA**2
    print(f"Flujo medio de la Tierra = 47 TW / (4 pi R^2) = {Q_TOTAL/area*1e3:.2f} mW/m^2 (area = {area:.4e} m^2) ; +/- 2 TW -> +/- {2e12/area*1e3:.2f} mW/m^2")
    # geotermo
    q0_ana_obj = 0.065                                  # W/m^2, flujo superficial ilustrativo
    T_L = geotermo_cerrado(L_RAD, q0_ana_obj)
    T, q_fd = solve_bvp(300, T_L)
    err = abs(q_fd - q0_ana_obj) / q0_ana_obj
    print(f"Geotermo: q0 = {q0_ana_obj*1e3:.1f} mW/m^2, A = {A_RAD*1e6:.1f} uW/m^3 -> T(30 km) = {T_L:.2f} K ; flujo FD = {q_fd*1e3:.4f} mW/m^2 ; error relativo = {err:.2e}")
    print(f"  Flujo en la base de la capa = q0 - A L = {(q0_ana_obj - A_RAD*L_RAD)*1e3:.1f} mW/m^2 (la capa aporta {A_RAD*L_RAD*1e3:.1f} mW/m^2)")
    # semiespacio
    print("Litosfera oceanica que se enfria (semiespacio, ilustrativa):")
    peor = 0.0
    for t_ma in (10, 50, 100):
        t = t_ma * 1e6 * ANIO
        q_ana = K * DT_MANTO / math.sqrt(math.pi * KAPPA * t)
        q_fd2 = semiespacio_fd(t)
        e = abs(q_fd2 - q_ana) / q_ana
        peor = max(peor, e)
        print(f"  t = {t_ma:3d} Ma: q analitico = {q_ana*1e3:7.2f} mW/m^2 ; q FD = {q_fd2*1e3:7.2f} mW/m^2 ; error = {e:.2e}")
    # Urey
    urey = H_RAD / Q_TOTAL
    cool = (Q_TOTAL - H_RAD) / C_TERM * ANIO * 1e9
    print(f"Balance: H = {H_RAD/1e12:.0f} TW (ilustrativo) -> razon de Urey = {urey:.3f} ; enfriamiento secular = {(Q_TOTAL-H_RAD)/1e12:.0f} TW -> dT/dt = -{cool:.0f} K/Ga")
    assert err < 1e-6 and peor < 1e-2
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
