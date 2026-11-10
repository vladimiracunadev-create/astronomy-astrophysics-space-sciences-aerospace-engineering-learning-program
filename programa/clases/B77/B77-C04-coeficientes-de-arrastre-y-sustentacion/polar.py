#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C04: coeficientes de arrastre y sustentacion a partir de datos SINTETICOS de tunel.

Datos consultados (2026-11-10): D = Cd q A, q = rho V^2/2, el area de referencia debe declararse (NASA Glenn, Drag Coefficient).
SINTETICOS (generados aqui con semilla 7, NO medidos en ningun tunel): CL_alfa = 2.4 /rad, CD0 = 0.30, k = 0.8 en la polar CD = CD0 + k CL^2,
ruido gaussiano de sigma 0.003 en CL y CD; q = 20000 Pa; area de referencia A1 = 10 m2; curva Cd(M) por tramos (subsonico 0.30,
pico transonico 0.55 en M = 1.1, 0.40 en M = 2, 0.35 en M = 4) inventada para ilustrar la forma.
Sistema: ejes del viento, SI. Angulos de ataque de -6 a 6 grados.
Modelo: ajuste lineal por minimos cuadrados de CL = a alfa y de CD frente a CL^2 (solo biblioteca estandar).
Segunda via: el ajuste debe recuperar los parametros de entrada dentro de la incertidumbre estadistica; la fuerza D no depende del area elegida.
Tolerancias: parametros recuperados dentro de 3 sigma del ajuste; D invariante bajo cambio de area con 1e-12.
"""
import math, platform, random

CLA, CD0, K, SIG, Q, A1 = 2.4, 0.30, 0.8, 0.003, 20000.0, 10.0
M_TAB = [(0.5, 0.30), (0.9, 0.32), (1.1, 0.55), (2.0, 0.40), (4.0, 0.35)]


def cd_mach(m):
    for (m0, c0), (m1, c1) in zip(M_TAB, M_TAB[1:]):
        if m0 <= m <= m1:
            return c0 + (c1 - c0) * (m - m0) / (m1 - m0)
    raise ValueError("Mach fuera de tabla")


def ajuste(x, y):
    n = len(x)
    sx, sy = sum(x), sum(y)
    sxx, sxy = sum(a * a for a in x), sum(a * b for a, b in zip(x, y))
    b = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    a = (sy - b * sx) / n
    res = sum((yi - (a + b * xi)) ** 2 for xi, yi in zip(x, y))
    s2 = res / (n - 2)
    sb = math.sqrt(s2 * n / (n * sxx - sx * sx))
    sa = math.sqrt(s2 * sxx / (n * sxx - sx * sx))
    return a, b, sa, sb


def calcular():
    rnd = random.Random(7)
    alfas = [math.radians(a) for a in range(-6, 7)]
    cl = [CLA * a + rnd.gauss(0, SIG) for a in alfas]
    cd = [CD0 + K * (CLA * a) ** 2 + rnd.gauss(0, SIG) for a in alfas]
    r = {"n": len(alfas)}
    a0, a1, sa0, sa1 = ajuste(alfas, cl)
    r["cla_fit"], r["cla_sig"] = a1, sa1
    b0, b1, sb0, sb1 = ajuste([c * c for c in cl], cd)
    r["cd0_fit"], r["cd0_sig"], r["k_fit"], r["k_sig"] = b0, sb0, b1, sb1
    r["ok_cla"] = abs(a1 - CLA) < 3 * sa1
    r["ok_cd0"] = abs(b0 - CD0) < 3 * sb0
    r["ok_k"] = abs(b1 - K) < 3 * sb1
    al = math.radians(4.0)
    r["CL4"] = CLA * al
    r["CD4"] = CD0 + K * r["CL4"] ** 2
    r["L4"], r["D4"] = r["CL4"] * Q * A1, r["CD4"] * Q * A1
    r["LD4"] = r["CL4"] / r["CD4"]
    r["LD_max"] = 1.0 / (2.0 * math.sqrt(CD0 * K))
    r["CL_LDmax"] = math.sqrt(CD0 / K)
    # el area de referencia
    A2 = 4.0
    r["Cd_A2"] = r["CD4"] * A1 / A2
    r["D_A2"] = r["Cd_A2"] * Q * A2
    r["dif_area"] = abs(r["D_A2"] - r["D4"]) / r["D4"]
    r["mach"] = [(m, cd_mach(m)) for m in (0.5, 0.9, 1.0, 1.1, 1.5, 2.0, 3.0)]
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Datos SINTETICOS de tunel (semilla 7, {r['n']} puntos, sigma = {SIG}); verdad de entrada CL_alfa = {CLA}, CD0 = {CD0}, k = {K}")
    print(f"Ajuste CL_alfa = {r['cla_fit']:.4f} +- {r['cla_sig']:.4f} /rad")
    print(f"Ajuste CD0 = {r['cd0_fit']:.4f} +- {r['cd0_sig']:.4f}; k = {r['k_fit']:.4f} +- {r['k_sig']:.4f}")
    print(f"A alfa = 4 grados: CL = {r['CL4']:.4f}, CD = {r['CD4']:.4f}, L = {r['L4']/1e3:.2f} kN, D = {r['D4']/1e3:.2f} kN, L/D = {r['LD4']:.3f}")
    print(f"L/D maximo de la polar = {r['LD_max']:.3f} con CL = {r['CL_LDmax']:.4f}")
    print(f"Cambio de area de referencia 10 -> 4 m2: Cd pasa de {r['CD4']:.4f} a {r['Cd_A2']:.4f}; D identica (dif. relativa {r['dif_area']:.1e})")
    print("Cd(M) sintetico: " + ", ".join(f"M{m:.1f}={c:.3f}" for m, c in r["mach"]))
    assert r["ok_cla"] and r["ok_cd0"] and r["ok_k"]
    assert r["dif_area"] < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
