#!/usr/bin/env python3
"""B53-C27: evidencia de un oceano SUBSUPERFICIAL con parametros ILUSTRATIVOS. SI. sigma = 2.5 S/m, periodos 9.925 h y 85.228 h
(uso comun, no consultados), mu0 = 4 pi e-7, R = 1560 km, capa t = 100 km. Simpson 2000 intervalos. Tolerancia 1e-9 relativa."""
import math, platform

MU0, SIGMA, R, T = 4e-7 * math.pi, 2.5, 1560e3, 100e3

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def frac_inercia_num(t):
    # momento de inercia de la capa exterior / total, densidad uniforme: integral de r^4 dr
    return simpson(lambda r: r ** 4, R - t, R) / simpson(lambda r: r ** 4, 0.0, R)

def compute():
    tsyn = 1 / abs(1 / 9.925 - 1 / 85.228)
    omega = 2 * math.pi / (tsyn * 3600)
    delta = math.sqrt(2 / (MU0 * SIGMA * omega))
    r = dict(Tsyn_h=tsyn, omega=omega, delta_km=delta / 1e3)
    for k in (1, 10, 100):
        r[f"att{k}"] = math.exp(-k * 1e3 / delta)
    r["fC_num"] = frac_inercia_num(T)
    r["fC_ana"] = 1 - (1 - T / R) ** 5
    r["amp"] = 1 / r["fC_num"]
    r["fC50"] = 1 - (1 - 50e3 / R) ** 5
    r["amp50"] = 1 / r["fC50"]
    r["err"] = abs(r["fC_num"] - r["fC_ana"]) / r["fC_ana"]
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"T_sinodico = {r['Tsyn_h']:.4f} h ; omega = {r['omega']:.4e} rad/s ; profundidad de piel = {r['delta_km']:.3f} km")
    print(f"atenuacion de amplitud: 1 km {r['att1']:.4f} ; 10 km {r['att10']:.4f} ; 100 km {r['att100']:.4f}")
    print(f"fraccion de inercia de la capa (t = 100 km): Simpson {r['fC_num']:.6f} ; formula {r['fC_ana']:.6f} ; error relativo {r['err']:.2e}")
    print(f"amplificacion de la libracion C/C_capa = {r['amp']:.3f} (t = 50 km: {r['amp50']:.3f})")
    assert r["err"] < 1e-9 and r["amp"] > 1
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
