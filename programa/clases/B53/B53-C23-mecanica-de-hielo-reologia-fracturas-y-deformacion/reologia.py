#!/usr/bin/env python3
"""B53-C23: reologia del hielo con coeficientes de USO COMUN, NO CONSULTADOS: n = 3, A(273 K) = 2.4e-24 Pa^-3 s^-1, Q = 60 kJ/mol.
Lamina H = 100 m, alfa = 2 grados, rho = 917. SI; ano = 3.156e7 s. Tolerancia 1e-9 relativa."""
import math, platform

N, A0, Q, R_GAS, RHO, H, ALFA, ANO = 3, 2.4e-24, 60000.0, 8.314462618, 917.0, 100.0, math.radians(2.0), 3.156e7

def A(T):
    return A0 * math.exp(-(Q / R_GAS) * (1 / T - 1 / 273.0))

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def us_ana(g, T=270.0):
    return 2 * A(T) / (N + 1) * (RHO * g * math.sin(ALFA)) ** N * H ** (N + 1) * ANO

def us_num(g, T=270.0):
    return simpson(lambda z: 2 * A(T) * (RHO * g * math.sin(ALFA) * (H - z)) ** N, 0, H) * ANO

def compute():
    g1, g2 = 9.81, 1.3
    r = dict(us_ana=us_ana(g1), us_num=us_num(g1), us_eur=us_ana(g2), ratio_g=us_ana(g2) / us_ana(g1), QR=Q / R_GAS,
             A270=A(270.0), A200=A(200.0), A100=A(100.0), ratio_T=A(270.0) / A(100.0), r200=A(200.0) / A(270.0),
             tau_b=RHO * g1 * math.sin(ALFA) * H)
    r["d_nye"] = 2 / (RHO * g1) * (1e-10 / A(270.0)) ** (1 / 3)
    r["err"] = abs(r["us_num"] - r["us_ana"]) / r["us_ana"]
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"u_s (g = 9.81): formula {r['us_ana']:.6f} m/ano ; Simpson {r['us_num']:.6f} m/ano ; error relativo {r['err']:.2e}")
    print(f"u_s (g = 1.3) = {r['us_eur']:.4e} m/ano ; razon = {r['ratio_g']:.5f} ; (1.3/9.81)^3 = {(1.3 / 9.81) ** 3:.5f}")
    print(f"A(270) = {r['A270']:.3e} ; A(200) = {r['A200']:.3e} ; A(100) = {r['A100']:.3e} Pa^-3 s^-1 ; cociente 270/100 = {r['ratio_T']:.3e}")
    print(f"profundidad de Nye (1e-10 /s, 270 K) = {r['d_nye']:.3f} m")
    assert r["err"] < 1e-9 and abs(r["ratio_g"] - (1.3 / 9.81) ** 3) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
