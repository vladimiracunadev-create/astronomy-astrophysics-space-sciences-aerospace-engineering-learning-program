#!/usr/bin/env python3
"""B53-C10: escalamiento de impactos con coeficientes ILUSTRATIVOS (no consultados). SI. Semilla 20261109.
D_tc = CD a (rho_i/rho_t)^(1/3) (g a / v^2)^(-beta), CD = 1.0, beta = 0.22. Hugoniot Us = c + s up con c = 2600 m/s, s = 1.5.
Tolerancia: pendiente dentro de 3 errores tipicos de 0.22."""
import math, platform, random

A, V, RHO_I, RHO_T = 100.0, 20000.0, 3000.0, 2700.0
CD, BETA, C_H, S_H = 1.0, 0.22, 2600.0, 1.5
MT = 4.184e15

def d_tc(g, a=A, v=V):
    return CD * a * (RHO_I / RHO_T) ** (1 / 3) * (g * a / v ** 2) ** (-BETA)

def presion(v):
    up = v / 2
    return RHO_T * (C_H + S_H * up) * up

def compute():
    m = 4 / 3 * math.pi * RHO_I * A ** 3
    E = 0.5 * m * V ** 2
    dl, dm, dt = d_tc(1.62), d_tc(3.71), d_tc(9.81)
    rng = random.Random(20261109)
    xs, ys = [], []
    for _ in range(200):
        a = math.exp(rng.uniform(math.log(10), math.log(1000)))
        g = rng.uniform(1.0, 10.0)
        v = rng.uniform(5000, 30000)
        xs.append(math.log(g * a / v ** 2))
        ys.append(math.log(d_tc(g, a, v) / a) + rng.gauss(0, 0.05))
    n = len(xs); mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    res = [y - (my + sl * (x - mx)) for x, y in zip(xs, ys)]
    se = math.sqrt(sum(e * e for e in res) / (n - 2) / sxx)
    return dict(m=m, E=E, E_mt=E / MT, D_luna=dl, D_marte=dm, D_tierra=dt, r_marte=dm / dl, r_tierra=dt / dl,
                r_marte_th=(1.62 / 3.71) ** BETA, P_choque=presion(V) / 1e9, P10=presion(10000.0) / 1e9, beta=-sl, beta_se=se)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"masa = {r['m']:.4e} kg ; energia = {r['E']:.4e} J = {r['E_mt']:.2f} Mt TNT")
    print(f"D_tc: Luna {r['D_luna']:.1f} m ; Marte {r['D_marte']:.1f} m ; Tierra {r['D_tierra']:.1f} m")
    print(f"razon Marte/Luna = {r['r_marte']:.4f} (teorica {r['r_marte_th']:.4f}) ; Tierra/Luna = {r['r_tierra']:.4f}")
    print(f"presion de choque = {r['P_choque']:.1f} GPa (v = 20 km/s) ; {r['P10']:.1f} GPa (v = 10 km/s)")
    print(f"regresion log-log (200 experimentos sinteticos): beta = {r['beta']:.4f} +- {r['beta_se']:.4f} (verdadero {BETA})")
    assert abs(r["beta"] - BETA) < 3 * r["beta_se"] and abs(r["r_marte"] / r["r_marte_th"] - 1) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
