#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C19: riesgo de rango a nivel conceptual (victimas esperadas) con datos SINTETICOS.

Datos consultados (2026-11-10): 14 CFR 450.101 (copia del Legal Information Institute, resumen leido): para lanzamientos, el numero esperado de victimas del publico
no debe exceder 1e-4 y la probabilidad de victima de cualquier miembro del publico, 1e-6 por lanzamiento (valores citados solo como orden de magnitud de referencia,
no como evaluacion de cumplimiento).
SINTETICOS / ILUSTRATIVOS (inventados, no corresponden a ningun lugar ni vehiculo): probabilidad de falla por lanzamiento p_f = 0.02; en una falla, el punto de impacto
de los escombros sigue una gaussiana 2D con sigma_x = 15 km (a lo largo de la trayectoria) y sigma_y = 5 km (transversal), centrada en el origen; el area de victima por impacto
A_c = 10 m2 efectivos por 'paquete' de escombros y 50 paquetes independientes por falla (NF); poblacion: fondo rural de 5 personas/km2 y una ciudad gaussiana (pico 500 personas/km2, sigma 3 km x 3 km) centrada en (40, 8) km.
Sistema: plano horizontal local (x a lo largo de la trayectoria, y transversal), km, SI para areas (1 km2 = 1e6 m2).
Modelo: E_c = p_f * N_escombros * A_c * integral f(x,y) rho(x,y) dx dy, con NF = 50 paquetes; riesgo individual en el centro de la ciudad P_c = p_f * f(x_c, y_c) * A_c.
Tres vias: (1) cerrada (producto de gaussianas), (2) cuadratura numerica en malla, (3) Monte Carlo con semilla 5 (N = 500 000).
Tolerancias: malla frente a cerrada 1e-4 relativa; Monte Carlo frente a cerrada: dentro de 4 errores estandar.
"""
import math, platform, random

PF, SX, SY, AC, NF = 0.02, 15.0, 5.0, 10.0 / 1e6, 50  # AC en km2
RURAL, PICO, SC, XC, YC = 5.0, 500.0, 3.0, 40.0, 8.0


def f_impacto(x, y):
    return math.exp(-0.5 * (x / SX) ** 2 - 0.5 * (y / SY) ** 2) / (2 * math.pi * SX * SY)


def rho(x, y):
    return RURAL + PICO * math.exp(-0.5 * ((x - XC) / SC) ** 2 - 0.5 * ((y - YC) / SC) ** 2)


def integral_cerrada():
    # rural: 5 * 1 ; ciudad: PICO * 2 pi SC^2 * N(XC,YC; 0, diag(SX^2 + SC^2, SY^2 + SC^2))
    vx, vy = SX ** 2 + SC ** 2, SY ** 2 + SC ** 2
    n = math.exp(-0.5 * (XC ** 2 / vx + YC ** 2 / vy)) / (2 * math.pi * math.sqrt(vx * vy))
    return RURAL + PICO * 2 * math.pi * SC ** 2 * n


def integral_malla(paso=0.25, lim=(-90.0, 90.0, -45.0, 45.0)):
    x0, x1, y0, y1 = lim
    nx, ny = int((x1 - x0) / paso), int((y1 - y0) / paso)
    s = 0.0
    for i in range(nx):
        x = x0 + (i + 0.5) * paso
        for j in range(ny):
            y = y0 + (j + 0.5) * paso
            s += f_impacto(x, y) * rho(x, y)
    return s * paso * paso


def montecarlo(n=500000, semilla=5):
    rnd = random.Random(semilla)
    s = s2 = 0.0
    for _ in range(n):
        x, y = rnd.gauss(0, SX), rnd.gauss(0, SY)
        v = rho(x, y)
        s += v
        s2 += v * v
    m = s / n
    sd = math.sqrt(s2 / n - m * m)
    return m, sd / math.sqrt(n)


def calcular():
    global XC
    r = {}
    r["I_cerr"] = integral_cerrada()
    r["I_malla"] = integral_malla()
    r["I_mc"], r["I_mc_err"] = montecarlo()
    r["err_malla"] = abs(r["I_malla"] - r["I_cerr"]) / r["I_cerr"]
    r["sigmas_mc"] = abs(r["I_mc"] - r["I_cerr"]) / r["I_mc_err"]
    r["Ec"] = PF * NF * AC * r["I_cerr"]
    r["Ec_rural"] = PF * NF * AC * RURAL
    r["Ec_ciudad"] = r["Ec"] - r["Ec_rural"]
    r["Pc_ciudad"] = PF * NF * f_impacto(XC, YC) * AC
    # sensibilidad: mover la ciudad a 80 km (mas lejos) y a 0 km (bajo la trayectoria)
    r["sens"] = []
    x_orig = XC
    for xc in (0.0, 20.0, 40.0, 80.0):
        XC = xc
        r["sens"].append((xc, PF * NF * AC * integral_cerrada()))
    XC = x_orig
    r["lim_Ec"], r["lim_Pc"] = 1e-4, 1e-6
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Escenario SINTETICO: p_fallo = {PF}, impacto gaussiano sigma = ({SX:.0f}, {SY:.0f}) km, A_victima = {AC*1e6:.0f} m2 x {NF} paquetes, ciudad en ({XC:.0f}, {YC:.0f}) km (pico {PICO:.0f}/km2), fondo {RURAL:.0f}/km2")
    print(f"Integral de f*rho [personas/km2]: cerrada = {r['I_cerr']:.6f}; malla = {r['I_malla']:.6f} (error {r['err_malla']:.1e}); Monte Carlo = {r['I_mc']:.4f} +- {r['I_mc_err']:.4f} ({r['sigmas_mc']:.2f} sigma de la cerrada)")
    print(f"Victimas esperadas E_c = {r['Ec']:.3e} (rural {r['Ec_rural']:.3e}; ciudad {r['Ec_ciudad']:.3e}); referencia de 14 CFR 450.101 = {r['lim_Ec']:.0e} -> cociente {r['Ec']/r['lim_Ec']:.2f}")
    print(f"Riesgo individual en el centro de la ciudad P_c = {r['Pc_ciudad']:.3e}; referencia = {r['lim_Pc']:.0e} -> cociente {r['Pc_ciudad']/r['lim_Pc']:.3f}")
    print("Sensibilidad a la posicion de la ciudad (x_c en km -> E_c): " + "; ".join(f"{x:.0f} -> {e:.3e}" for x, e in r["sens"]))
    assert r["err_malla"] < 1e-4 and r["sigmas_mc"] < 4.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
