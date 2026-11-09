#!/usr/bin/env python3
"""B53-C14: capa de hielo conductiva ILUSTRATIVA. SI. k = a/T (a = 567 W/m, uso comun, no consultado), Ts = 100 K, Tb = 273 K.
rho = 920, g = 1.3, alpha = 1.6e-4, kappa = 1e-6, eta = 1e14 (ilustrativos). Tolerancia 1e-9 relativa."""
import math, platform

A, TS, TB, RHO, G, ALPHA, KAPPA, ETA = 567.0, 100.0, 273.0, 920.0, 1.3, 1.6e-4, 1.0e-6, 1.0e14

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def H_ana(q):
    return A / q * math.log(TB / TS)

def H_num(q):
    # dz = k dT / q con k = A/T
    return simpson(lambda T: A / T / q, TS, TB)

def compute():
    r = {"ln": math.log(TB / TS)}
    for qm in (10, 20, 50):
        q = qm / 1000
        h = H_ana(q)
        r[f"H{qm}"] = h / 1e3
        r[f"H{qm}n"] = H_num(q) / 1e3
        r[f"Ra{qm}"] = RHO * G * ALPHA * (TB - TS) * h ** 3 / (KAPPA * ETA)
        r[f"pb{qm}"] = RHO * G * h / 1e6
    r["H40"] = H_ana(0.04) / 1e3
    r["q5"] = A * math.log(TB / TS) / 5000.0
    r["err"] = max(abs(r[f"H{qm}n"] - r[f"H{qm}"]) / r[f"H{qm}"] for qm in (10, 20, 50))
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    for qm in (10, 20, 50):
        print(f"q = {qm} mW/m2: H = {r['H%d' % qm]:.3f} km (Simpson {r['H%dn' % qm]:.3f}) ; Ra = {r['Ra%d' % qm]:.3e} ; presion basal = {r['pb%d' % qm]:.2f} MPa")
    print(f"error relativo maximo de la integracion = {r['err']:.2e}")
    assert r["err"] < 1e-9 and r["H10"] > r["H20"] > r["H50"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
