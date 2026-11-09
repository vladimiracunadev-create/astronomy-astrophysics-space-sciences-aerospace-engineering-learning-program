#!/usr/bin/env python3
"""B53-C13: estabilidad del hielo de agua (equilibrio de vapor). SI. Constantes de uso comun, NO consultadas:
L = 2.83e6 J/kg, punto triple 611.657 Pa a 273.16 K, M = 0.018015 kg/mol, rho = 917 kg/m3. R exacta (SI).
Tolerancia: pendiente numerica dentro de 1e-6 relativa."""
import math, platform

R_GAS, M, L, PT, TT, RHO, ANO = 8.314462618, 0.018015, 2.83e6, 611.657, 273.16, 917.0, 3.156e7
RV = R_GAS / M

def p_vapor(T):
    return PT * math.exp(L / RV * (1 / TT - 1 / T))

def flujo(T):
    return p_vapor(T) * math.sqrt(M / (2 * math.pi * R_GAS * T))

def compute():
    r = {"Rv": RV}
    for T in (100, 150, 200, 250):
        r[f"p{T}"] = p_vapor(T)
        r[f"j{T}"] = flujo(T)
        r[f"y{T}"] = RHO / flujo(T) / ANO
    t1, t2 = 199.0, 201.0
    r["sl_num"] = (math.log(p_vapor(t2)) - math.log(p_vapor(t1))) / (1 / t2 - 1 / t1)
    r["sl_ana"] = -L / RV
    r["razon"] = r["y250"] / r["y100"]
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"R_v = {r['Rv']:.3f} J/(kg K) ; pendiente de ln p frente a 1/T: numerica {r['sl_num']:.4f} K ; analitica {r['sl_ana']:.4f} K")
    for T in (100, 150, 200, 250):
        print(f"T = {T} K: p = {r['p%d' % T]:.3e} Pa ; J = {r['j%d' % T]:.3e} kg/m2/s ; anos por metro = {r['y%d' % T]:.3e}")
    print(f"cociente de vidas 250 K / 100 K = {r['razon']:.3e}")
    assert abs(r["sl_num"] / r["sl_ana"] - 1) < 1e-6 and r["y100"] > r["y150"] > r["y200"] > r["y250"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
