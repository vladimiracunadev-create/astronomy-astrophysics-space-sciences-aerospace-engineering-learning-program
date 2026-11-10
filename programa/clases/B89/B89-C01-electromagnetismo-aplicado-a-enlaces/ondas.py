#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C01. Electromagnetismo aplicado a enlaces: longitud de onda, densidad de flujo y polarizacion.
Datos SINTETICOS (potencia, ganancia, distancia). c es la constante exacta de NIST CODATA 2022 (consultada)."""
import math, sys

C = 299_792_458.0  # m/s, exacta (NIST CODATA 2022)

def lam(f_hz):
    return C / f_hz

def flujo(p_w, g_lin, r_m):
    """Densidad de flujo de potencia S = P G / (4 pi r^2) en W/m2 (campo lejano, vacio)."""
    return p_w * g_lin / (4 * math.pi * r_m ** 2)

def plf_lineal(psi_rad):
    """Factor de perdida por polarizacion entre dos lineales desalineadas psi."""
    return math.cos(psi_rad) ** 2

def a_db(x):
    return 10 * math.log10(x)

def calcular():
    R = {}
    bandas = {"UHF 401 MHz": 401e6, "S 2.2 GHz": 2.2e9, "X 8.4 GHz": 8.4e9, "Ka 32 GHz": 32e9}
    R["lam"] = {k: lam(v) for k, v in bandas.items()}
    p, g, r = 20.0, 10 ** (30 / 10), 1_000e3  # 20 W, 30 dBi, 1000 km (SINTETICO)
    R["S"] = flujo(p, g, r)
    R["S_dBWm2"] = a_db(R["S"])
    R["S_2r"] = flujo(p, g, 2 * r)
    R["razon_2r"] = R["S"] / R["S_2r"]
    R["plf"] = {a: plf_lineal(math.radians(a)) for a in (0, 30, 45, 60, 85)}
    R["plf_db"] = {a: a_db(max(v, 1e-12)) for a, v in R["plf"].items()}
    R["circ_lin_db"] = a_db(0.5)
    # verificacion independiente: f lambda = c y la ley 1/r^2 por integracion de la esfera
    R["chk_flam"] = max(abs(lam(f) * f - C) / C for f in bandas.values())
    R["chk_esfera"] = abs(R["S"] * 4 * math.pi * r ** 2 - p * g) / (p * g)
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("Longitud de onda lambda = c/f (c = 299 792 458 m/s):")
    for k, v in R["lam"].items():
        print(f"  {k:12s} lambda = {v*100:9.3f} cm")
    print("SINTETICO: P = 20 W, G = 30 dBi, r = 1000 km")
    print(f"  S = {R['S']:.4e} W/m2 = {R['S_dBWm2']:.2f} dBW/m2")
    print(f"  S(r)/S(2r) = {R['razon_2r']:.4f}")
    print("Perdida por polarizacion lineal-lineal desalineada:")
    for a in R["plf"]:
        print(f"  psi = {a:2d} grados  PLF = {R['plf'][a]:.4f}  ({R['plf_db'][a]:7.2f} dB)")
    print(f"Circular -> lineal: {R['circ_lin_db']:.2f} dB")
    assert R["chk_flam"] < 1e-12 and R["chk_esfera"] < 1e-12
    assert abs(R["razon_2r"] - 4.0) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
