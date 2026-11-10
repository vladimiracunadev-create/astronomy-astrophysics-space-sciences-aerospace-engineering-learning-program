#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C04: equilibrio termico de hielo de agua en un nucleo cometario y empuje de la presion de radiacion sobre el polvo.

Datos: nucleo SINTETICO (albedo 0.04 y emisividad 0.9 ilustrativos). Luminosidad solar 3.828e26 W (valor nominal IAU 2015), GM del Sol 1.32712440018e20 m^3/s^2 (nominal IAU), c, sigma de
Stefan-Boltzmann, k_B y la unidad astronomica: valores del autor, NO consultados en esta sesion. Presion de vapor del hielo de agua P = 3.56e12 exp(-6141.667/T) Pa y calor latente 2.83e6 J/kg: ajustes
recordados por el autor, NO consultados (se declaran ilustrativos).
Modelo: (1) subsolar, balance (1-A) S = eps sigma T^4 + L Z(T), con Z = P_v sqrt(m/(2 pi k T)) y bisecion; (2) beta = F_rad/F_grav = 3 L Q_pr / (16 pi c GM rho s) con Q_pr = 1;
(3) desplazamiento relativo del polvo y del cometa en 1 dia, integrado con RK4, frente a (1/2) beta g t^2. Unidades: SI.
Supuestos: sin conduccion hacia el interior, sin rotacion, polvo esferico y de eficiencia unitaria. Validez: ilustrativa; no describe un cometa real.
Tolerancia: residuo del balance < 1e-9 relativo; beta(rho = 1000, s = 1 um) = 0.574 +- 0.002; desplazamiento integrado frente a analitico 1e-3 relativo.
"""
import math, platform

L_SOL = 3.828e26
GMS = 1.32712440018e20
C = 299792458.0
SIGMA = 5.670374419e-8
KB = 1.380649e-23
UA = 1.495978707e11
M_H2O = 18.015 * 1.66053907e-27
L_SUB = 2.83e6
A, EPS = 0.04, 0.9

def flujo(r_au):
    return L_SOL / (4 * math.pi * (r_au * UA) ** 2)

def Z(T):
    Pv = 3.56e12 * math.exp(-6141.667 / T)
    return Pv * math.sqrt(M_H2O / (2 * math.pi * KB * T))

def balance(T, S):
    return (1 - A) * S - EPS * SIGMA * T ** 4 - L_SUB * Z(T)

def temperatura(r_au):
    S = flujo(r_au)
    lo, hi = 50.0, 500.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if balance(mid, S) > 0:
            lo = mid
        else:
            hi = mid
    T = 0.5 * (lo + hi)
    return T, Z(T), balance(T, S) / ((1 - A) * S)

def beta(rho, s):
    return 3 * L_SOL / (16 * math.pi * C * GMS * rho * s)

def desplazamiento(b, t_final=86400.0, dt=60.0):
    """Separacion radial entre polvo (gravedad efectiva (1-b)GM/r^2) y cometa (GM/r^2), ambos en reposo en r = 1 au al inicio."""
    r0 = UA
    def f(y, g):
        r, v = y
        return (v, -g * GMS / r ** 2)
    def paso(y, g):
        k1 = f(y, g); k2 = f((y[0] + dt / 2 * k1[0], y[1] + dt / 2 * k1[1]), g)
        k3 = f((y[0] + dt / 2 * k2[0], y[1] + dt / 2 * k2[1]), g); k4 = f((y[0] + dt * k3[0], y[1] + dt * k3[1]), g)
        return (y[0] + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), y[1] + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))
    yd, yc = (r0, 0.0), (r0, 0.0)
    for _ in range(int(round(t_final / dt))):
        yd, yc = paso(yd, 1 - b), paso(yc, 1.0)
    return yd[0] - yc[0], 0.5 * b * GMS / r0 ** 2 * t_final ** 2

def calcular():
    filas = []
    for r in [1.0, 1.5, 2.0, 3.0, 5.0]:
        T, z, res = temperatura(r)
        Tbb = ((1 - A) * flujo(r) / (EPS * SIGMA)) ** 0.25
        frac = L_SUB * z / ((1 - A) * flujo(r))
        filas.append((r, T, Tbb, z, frac, res))
    betas = [(s, beta(1000.0, s)) for s in (0.1e-6, 1e-6, 10e-6)]
    b1 = beta(1000.0, 1e-6)
    dx, dxa = desplazamiento(b1)
    return {"filas": filas, "betas": betas, "b1": b1, "dx": dx, "dxa": dxa, "err": abs(dx / dxa - 1)}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("%6s %9s %12s %14s %14s %11s" % ("r[au]", "T[K]", "T sin subl.", "Z[kg/m2/s]", "E a sublim.", "residuo"))
    for f in r["filas"]:
        print("%6.1f %9.2f %12.2f %14.3e %14.4f %11.1e" % f)
    for s, b in r["betas"]:
        print("beta(rho = 1000 kg/m3, s = %.1f um) = %.4f" % (s * 1e6, b))
    print("Desplazamiento en 1 dia: integrado = %.4e m ; (1/2) beta g t^2 = %.4e m ; diferencia relativa = %.2e" % (r["dx"], r["dxa"], r["err"]))
    for f in r["filas"]:
        assert abs(f[5]) < 1e-9
    assert abs(r["b1"] - 0.574) < 0.002
    assert r["err"] < 1e-3
    assert r["filas"][0][4] > 0.9 and r["filas"][-1][4] < 0.2      # a 1 au domina; a 5 au aun gasta una fraccion apreciable
    assert all(r["filas"][i][4] > r["filas"][i + 1][4] for i in range(len(r["filas"]) - 1))
    assert all(r["filas"][i][1] > r["filas"][i + 1][1] for i in range(len(r["filas"]) - 1))
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
