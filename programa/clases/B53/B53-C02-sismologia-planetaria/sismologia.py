#!/usr/bin/env python3
"""B53-C02: sismologia planetaria SINTETICA. Unidades: km, s, rad. Esfera homogenea R=3000 km.
Semilla 20261109. Tolerancias: integral 1e-7 relativa; Monte Carlo dentro de 3 errores tipicos."""
import math, platform, random

R, V, VP, VS, SIG = 3000.0, 8.0, 8.0, 4.5, 0.5

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def compute():
    rmin = 800.0
    smax = math.acosh(R / rmin)
    D_num = 2 * simpson(lambda s: 1 / math.cosh(s), 0, smax)
    D_ana = 2 * math.acos(rmin / R)
    t_num = (2 / V) * simpson(lambda s: rmin * math.cosh(s), 0, smax)
    t_ana = 2 * math.sqrt(R * R - rmin * rmin) / V
    d_true = 1200.0
    k = 1 / VS - 1 / VP
    dt_sp = d_true * k
    rng = random.Random(20261109)
    ests = []
    for _ in range(20000):
        tp = d_true / VP + rng.gauss(0, SIG)
        ts = d_true / VS + rng.gauss(0, SIG)
        ests.append((ts - tp) / k)
    mu = sum(ests) / len(ests)
    sd = math.sqrt(sum((e - mu) ** 2 for e in ests) / (len(ests) - 1))
    sd_ana = math.sqrt(2) * SIG / k
    return dict(rmin=rmin, D_num=D_num, D_ana=D_ana, t_num=t_num, t_ana=t_ana, d_true=d_true, dt_sp=dt_sp,
                d_mean=mu, d_sd_mc=sd, d_sd_ana=sd_ana, bias=mu - d_true, se=sd / math.sqrt(len(ests)))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"rayo con r_min = {r['rmin']:.0f} km: Delta numerica {r['D_num']:.8f} rad ; geometrica {r['D_ana']:.8f} rad")
    print(f"tiempo de viaje: numerico {r['t_num']:.5f} s ; geometrico {r['t_ana']:.5f} s")
    print(f"evento a {r['d_true']:.0f} km: retraso S-P exacto = {r['dt_sp']:.3f} s")
    print(f"Monte Carlo (20000): distancia = {r['d_mean']:.2f} +- {r['d_sd_mc']:.2f} km ; sigma analitica = {r['d_sd_ana']:.2f} km ; sesgo = {r['bias']:.3f} km")
    assert abs(r["D_num"] - r["D_ana"]) / r["D_ana"] < 1e-7 and abs(r["t_num"] - r["t_ana"]) / r["t_ana"] < 1e-7
    assert abs(r["bias"]) < 3 * r["se"] and abs(r["d_sd_mc"] / r["d_sd_ana"] - 1) < 0.03
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
