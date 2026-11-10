#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C01: estructura vertical de una atmosfera (temperatura y presion por capas).

Datos: constantes de NIST CODATA 2022 (k, N_A) y gravedad media terrestre de la ficha NASA/NSSDC (9.820 m/s^2, consulta 2026-11-09).
Los espesores de capa y gradientes de temperatura (perfil por tramos tipo "atmosfera estandar") son PARAMETROS DEL MODELO
introducidos por la clase (ilustrativos); no se verificaron contra el texto de la U.S. Standard Atmosphere 1976 (solo se consulto su resumen).
Modelo: equilibrio hidrostatico dP/dz = -rho g con gas ideal; T(z) lineal a trozos. Integracion numerica (RK4) frente a la solucion analitica por capa.
Supuestos: aire seco de masa molar 28.9647 g/mol (valor ilustrativo), g constante. Validez: z < 85 km, sin humedad.
Tolerancia: presion numerica frente a analitica < 1e-6 relativo.
"""
import math, platform

K_B = 1.380649e-23        # J/K (NIST CODATA 2022, exacta)
N_A = 6.02214076e23       # 1/mol (NIST CODATA 2022, exacta)
R = K_B * N_A             # J/(mol K)
G0, M = 9.820, 0.0289647  # m/s^2 (NASA/NSSDC), kg/mol
P0, T0 = 101325.0, 288.15  # Pa, K (ilustrativos)
# (base z [m], gradiente dT/dz [K/m]) -- parametros ilustrativos
CAPAS = [(0.0, -6.5e-3), (11000.0, 0.0), (20000.0, 1.0e-3), (32000.0, 2.8e-3), (47000.0, 0.0), (51000.0, -2.8e-3), (71000.0, -2.0e-3)]


def perfil_analitico(zs):
    """Presion y temperatura analiticas por capas."""
    out, z_b, T_b, P_b = [], 0.0, T0, P0
    bases = [c[0] for c in CAPAS] + [86000.0]
    caps = []
    for i, (zb, L) in enumerate(CAPAS):
        zt = bases[i + 1]
        caps.append((zb, zt, L, T_b, P_b))
        dz = zt - zb
        T_t = T_b + L * dz
        P_b = P_b * (T_t / T_b) ** (-G0 * M / (R * L)) if L != 0 else P_b * math.exp(-G0 * M * dz / (R * T_b))
        T_b = T_t
    for z in zs:
        for zb, zt, L, Tb, Pb in caps:
            if zb <= z <= zt:
                dz = z - zb
                T = Tb + L * dz
                P = Pb * (T / Tb) ** (-G0 * M / (R * L)) if L != 0 else Pb * math.exp(-G0 * M * dz / (R * Tb))
                out.append((z, T, P)); break
    return out


def T_de_z(z):
    T, z_prev = T0, 0.0
    bases = [c[0] for c in CAPAS] + [1e9]
    for i, (zb, L) in enumerate(CAPAS):
        if z <= bases[i + 1]:
            return T + L * (z - zb)
        T += L * (bases[i + 1] - zb)


def integra_rk4(z_fin, n=20000):
    f = lambda z, P: -P * G0 * M / (R * T_de_z(z))
    h, z, P = z_fin / n, 0.0, P0
    for _ in range(n):
        k1 = f(z, P); k2 = f(z + h / 2, P + h * k1 / 2); k3 = f(z + h / 2, P + h * k2 / 2); k4 = f(z + h, P + h * k3)
        P += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6; z += h
    return P


print(f"Python {platform.python_version()} (biblioteca estandar)")
print(f"R = k N_A = {R:.6f} J/(mol K) ; H(288.15 K) = {R*T0/(M*G0)/1000:.3f} km")
zs = [0, 5000, 11000, 20000, 32000, 47000, 51000, 71000, 85000]
print(" z [km]   T [K]    P analitica [Pa]   P RK4 [Pa]   dif. rel.")
peor = 0.0
for z, T, P in perfil_analitico(zs):
    Pn = integra_rk4(z) if z > 0 else P0
    d = abs(Pn - P) / P; peor = max(peor, d)
    print(f"{z/1000:7.1f} {T:8.2f} {P:16.4f} {Pn:14.4f}  {d:.1e}")
assert peor < 1e-6, "la integracion numerica no coincide con la solucion analitica"
T11, P11 = perfil_analitico([11000])[0][1:]
print(f"Tropopausa modelo (11 km): T = {T11:.2f} K ; P = {P11:.1f} Pa")
# mesopausa: minimo de T
zmin = min((z for z in range(0, 85001, 1000)), key=T_de_z)
print(f"Minimo de T en la mesopausa del modelo: z = {zmin/1000:.0f} km ; T = {T_de_z(zmin):.2f} K")
print("Pruebas superadas.")
