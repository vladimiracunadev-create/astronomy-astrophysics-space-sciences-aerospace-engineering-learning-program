#!/usr/bin/env python3
"""B53-C15: penacho SINTETICO. SI. G = 6.67430e-11 (NIST). R = 252 km, rho = 1600 (ilustrativos). Velocidades Maxwell
sigma = 100 m/s por componente. Semilla 20261109. Tolerancias: altura 1e-4 relativa; fraccion 4 errores tipicos."""
import math, platform, random

G, R, RHO, SIG = 6.67430e-11, 252e3, 1600.0, 100.0
M = 4 / 3 * math.pi * RHO * R ** 3
GM = G * M
VESC = math.sqrt(2 * GM / R)

def f_ana(x):
    return math.erfc(x / math.sqrt(2)) + math.sqrt(2 / math.pi) * x * math.exp(-x * x / 2)

def h_ana(v):
    return R / (2 * GM / (R * v * v) - 1)

def h_num(v, dt=0.05):
    r, vr = R, v
    rmax = r
    a = -GM / r ** 2
    while vr > 0 or r > R:
        vr += 0.5 * dt * a
        r += dt * vr
        a = -GM / r ** 2
        vr += 0.5 * dt * a
        rmax = max(rmax, r)
        if vr < 0 and r <= R:
            break
    return rmax - R

def compute():
    rng = random.Random(20261109)
    n = 200000
    k = sum(1 for _ in range(n) if math.sqrt(sum(rng.gauss(0, SIG) ** 2 for _ in range(3))) > VESC)
    f_mc = k / n
    x = VESC / SIG
    fa = f_ana(x)
    return dict(M=M, vesc=VESC, x=x, f_ana=fa, f_mc=f_mc, f_se=math.sqrt(fa * (1 - fa) / n),
                h_ana=h_ana(150.0) / 1e3, h_num=h_num(150.0) / 1e3, h100=h_ana(100.0) / 1e3)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"M = {r['M']:.4e} kg ; v_esc = {r['vesc']:.3f} m/s ; x = v_esc/sigma = {r['x']:.4f}")
    print(f"fraccion que escapa: analitica {r['f_ana']:.5f} ; Monte Carlo {r['f_mc']:.5f} (error tipico {r['f_se']:.1e})")
    print(f"altura a 150 m/s: analitica {r['h_ana']:.4f} km ; leapfrog {r['h_num']:.4f} km")
    assert abs(r["f_mc"] - r["f_ana"]) < 4 * r["f_se"] and abs(r["h_num"] / r["h_ana"] - 1) < 1e-4
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
