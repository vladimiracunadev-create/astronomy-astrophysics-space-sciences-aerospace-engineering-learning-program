#!/usr/bin/env python3
"""B53-C11: colada de lava SINTETICA en una lamina inclinada. SI. h = 2 m, eta = 1e3 Pa s, rho = 2700, alfa = 2 grados,
tau_y = 1e4 Pa, t_c = 3e4 s (todo ilustrativo). g = 9.81, 3.71, 1.62 (redondeos, no consultados). Tolerancia 1e-9."""
import math, platform

RHO, ETA, ALFA, H, TAUY, TC = 2700.0, 1.0e3, math.radians(2.0), 2.0, 1.0e4, 3.0e4
GS = {"tierra": 9.81, "marte": 3.71, "luna": 1.62}

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def u_media_ana(g, h=H):
    return RHO * g * h * h * math.sin(ALFA) / (3 * ETA)

def u_media_num(g, h=H):
    return simpson(lambda z: RHO * g * math.sin(ALFA) / ETA * (h * z - z * z / 2), 0, h) / h

def h_max(g):
    return TAUY / (RHO * g * math.sin(ALFA))

def compute():
    R = {}
    ut = u_media_ana(GS["tierra"])
    for k, g in GS.items():
        R[f"u_{k}"] = u_media_ana(g)
        R[f"h_{k}"] = h_max(g)
        R[f"r_{k}"] = u_media_ana(g) / ut
    R["u_num"] = u_media_num(GS["tierra"])
    R["err"] = abs(R["u_num"] - ut) / ut
    R["L_tierra"] = ut * TC
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"velocidad media (Tierra): analitica {r['u_tierra']:.6f} m/s ; Simpson {r['u_num']:.6f} m/s ; error relativo {r['err']:.2e}")
    for k in GS:
        print(f"{k:7s} g = {GS[k]:5.2f}: u = {r['u_'+k]:.5f} m/s ; razon {r['r_'+k]:.4f} ; h maximo (Bingham) = {r['h_'+k]:.3f} m")
    print(f"largo ilustrativo (u * t_c) = {r['L_tierra']:.0f} m")
    assert r["err"] < 1e-9 and abs(r["r_luna"] - 1.62 / 9.81) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
