#!/usr/bin/env python3
"""B53-C16: gravedad efectiva en un asteroide ILUSTRATIVO esferico. SI. G = 6.67430e-11 (NIST). R = 250 m, rho = 1190.
Tolerancia: periodo limite por biseccion dentro de 1e-9 relativa de sqrt(3 pi/(G rho))."""
import math, platform

G, R, RHO = 6.67430e-11, 250.0, 1190.0
M = 4 / 3 * math.pi * RHO * R ** 3
G0 = G * M / R ** 2

def geff(P):
    w = 2 * math.pi / P
    return G0 - w * w * R

def compute():
    r = {"M": M, "g0": G0, "vesc": math.sqrt(2 * G * M / R)}
    for h in (24, 8, 4):
        r[f"geff{h}"] = geff(h * 3600.0)
        r[f"pct{h}"] = 100 * geff(h * 3600.0) / G0
    a, b = 3600.0, 24 * 3600.0
    for _ in range(200):
        c = 0.5 * (a + b)
        if geff(c) > 0:
            b = c
        else:
            a = c
    r["Pc_h"] = 0.5 * (a + b) / 3600
    r["Pc_ana_h"] = math.sqrt(3 * math.pi / (G * RHO)) / 3600
    r["w2r4"] = (2 * math.pi / 14400.0) ** 2 * R
    r["v_eq"] = 2 * math.pi / 14400.0 * R
    r["rv"] = r["v_eq"] / r["vesc"]
    r["vesc_cm"] = r["vesc"] * 100
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"M = {r['M']:.4e} kg ; g estatica = {r['g0']:.4e} m/s2 ; v_esc = {r['vesc']:.4f} m/s")
    for h in (24, 8, 4):
        print(f"P = {h:2d} h: g_eff = {r['geff%d' % h]:.4e} m/s2 ({r['pct%d' % h]:.1f} % de la estatica)")
    print(f"periodo limite: biseccion {r['Pc_h']:.6f} h ; formula {r['Pc_ana_h']:.6f} h")
    print(f"v_ecuador (4 h) = {r['v_eq']:.4f} m/s = {r['rv']:.3f} v_esc")
    assert abs(r["Pc_h"] / r["Pc_ana_h"] - 1) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
