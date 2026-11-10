#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C16: consecuencias geofisicas de un impacto: magnitud sismica equivalente y radio de la onda de choque (Sedov-Taylor).

Datos: cuatro impactores SINTETICOS (20, 50, 140 y 470 m; 2600-3000 kg/m^3; 15-20 km/s) de C10. Relaciones recordadas del autor y NO consultadas: M = 0.67 log10(k E_J) - 5.87 con eficiencia sismica
k = 1e-4 (ILUSTRATIVA, de la literatura de efectos de impacto) y solucion de Sedov-Taylor R = xi (E t^2 / rho0)^(1/5) con xi = 1.033 para gamma = 1.4; relacion de Rankine-Hugoniot de choque fuerte
p2/p0 = (2 gamma M^2 - (gamma - 1)) / (gamma + 1) (estandar). Aire: rho0 = 1.2 kg/m^3, c0 = 340 m/s (ilustrativos). Fraccion de energia en la onda: 0.5 (ILUSTRATIVA). 1 Mt = 4.184e15 J.
Modelo: R(t) de Sedov para una explosion puntual en atmosfera uniforme; se busca el radio donde el frente tiene Mach 2 (R_dot = 2 c0, R_dot = 0.4 R / t); p2/p0 = 4.5 en ese punto.
Supuestos: sin altura ni fragmentacion, aire uniforme, onda de choque fuerte (Mach 2 es el limite inferior de validez aproximada). Validez: ilustrativa.
Tolerancia: derivada numerica de R(t) frente a 0.4 R/t con 1e-6; R(Mach 2) escala como E^(1/3) con 1e-9; p2/p0 = 1 para M = 1 y 4.5 para M = 2 con 1e-12.
"""
import math, platform

MT = 4.184e15
XI, RHO0, C0, GAMMA = 1.033, 1.2, 340.0, 1.4

def energia_j(D, rho, v_kms):
    return 0.5 * rho * math.pi * D ** 3 / 6 * (v_kms * 1e3) ** 2

def magnitud(E_J, k=1e-4):
    return 0.67 * math.log10(k * E_J) - 5.87

def radio(E, t):
    return XI * (E * t * t / RHO0) ** 0.2

def radio_mach(E, M=2.0):
    # R_dot = 0.4 xi (E/rho0)^0.2 t^-0.6 = M c0
    t = (0.4 * XI * (E / RHO0) ** 0.2 / (M * C0)) ** (1 / 0.6)
    return radio(E, t), t

def p_ratio(M, g=GAMMA):
    return (2 * g * M * M - (g - 1)) / (g + 1)

def calcular():
    casos = [("SINT-4", 20.0, 3000.0, 18.0), ("SINT-2", 50.0, 2600.0, 15.0), ("SINT-1", 140.0, 2600.0, 20.0), ("SINT-3", 470.0, 2600.0, 20.0)]
    filas = []
    for n, D, rho, v in casos:
        E = energia_j(D, rho, v)
        Eb = 0.5 * E
        R2, t2 = radio_mach(Eb)
        filas.append((n, D, E / MT, magnitud(E), R2 / 1e3, t2))
    E0 = 0.5 * energia_j(140.0, 2600.0, 20.0)
    R, t = radio_mach(E0)
    h = 1e-6 * t
    dRdt = (radio(E0, t + h) - radio(E0, t - h)) / (2 * h)
    return {"filas": filas, "dRdt": dRdt, "dRdt_a": 0.4 * R / t, "c0": C0, "e_scal": radio_mach(8 * E0)[0] / radio_mach(E0)[0],
            "p1": p_ratio(1.0), "p2": p_ratio(2.0)}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("%-7s %7s %12s %11s %17s %9s" % ("caso", "D[m]", "E[Mt]", "M sismica", "R(Mach 2) [km]", "t [s]"))
    for f in r["filas"]:
        print("%-7s %7.0f %12.4g %11.2f %17.3f %9.2f" % f)
    print("Velocidad del frente en el punto Mach 2 (caso 140 m): numerica = %.6f m/s ; 0.4 R/t = %.6f m/s ; 2 c0 = %.1f m/s" % (r["dRdt"], r["dRdt_a"], 2 * r["c0"]))
    print("R(Mach 2) al multiplicar E por 8: factor %.9f (8^(1/3) = 2)" % r["e_scal"])
    print("Rankine-Hugoniot p2/p0: M = 1 -> %.12f ; M = 2 -> %.12f" % (r["p1"], r["p2"]))
    assert abs(r["dRdt"] / r["dRdt_a"] - 1) < 1e-6
    assert abs(r["e_scal"] - 2.0) < 1e-9
    assert abs(r["p1"] - 1.0) < 1e-12 and abs(r["p2"] - 4.5) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
