#!/usr/bin/env python3
"""B53-C04: figura de equilibrio SINTETICA (esferoide de Maclaurin) y ondulacion del geoide.
SI. G = 6.67430e-11 (NIST CODATA 2022). Cuerpo homogeneo rho=5500 kg/m3, periodo 24 h, R=6.0e6 m (ilustrativos).
Tolerancias: biseccion 1e-12; Bruns vs equipotencial 1e-3 relativa."""
import math, platform

G = 6.67430e-11

def biseccion(f, a, b, tol=1e-12):
    fa = f(a)
    for _ in range(200):
        c = 0.5 * (a + b)
        fc = f(c)
        if (fa < 0) == (fc < 0):
            a, fa = c, fc
        else:
            b = c
        if b - a < tol:
            break
    return 0.5 * (a + b)

def maclaurin(e):
    return (2 * math.sqrt(1 - e * e) / e ** 3) * (3 - 2 * e * e) * math.asin(e) - 6 * (1 - e * e) / (e * e)

def compute():
    rho, T, Rm = 5500.0, 86400.0, 6.0e6
    w = 2 * math.pi / T
    x = w * w / (math.pi * G * rho)
    e = biseccion(lambda e: maclaurin(e) - x, 1e-2, 0.8)
    f = 1 - math.sqrt(1 - e * e)
    q = 3 * w * w / (4 * math.pi * G * rho)
    f_lin = 1.25 * q
    GM = G * rho * 4 / 3 * math.pi * Rm ** 3
    g = GM / Rm ** 2
    dm, d = 1.0e16, 1.0e4
    Tp = G * dm / d
    n_bruns = Tp / g
    n_num = biseccion(lambda h: -GM / (Rm + h) - G * dm / (d + h) + GM / Rm, -100.0, 100.0)
    return dict(w=w, x=x, e=e, f=f, inv_f=1 / f, f_lin=f_lin, dif=abs(f - f_lin) / f, g=g, N_bruns=n_bruns, N_num=n_num)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"omega = {r['w']:.5e} rad/s ; x = w^2/(pi G rho) = {r['x']:.7f}")
    print(f"Maclaurin: e = {r['e']:.7f} ; f = {r['f']:.8f} (1/{r['inv_f']:.2f}) ; aproximacion 5q/4 = {r['f_lin']:.8f} ; dif. relativa = {r['dif']:.3e}")
    print(f"g = {r['g']:.4f} m/s2 ; N Bruns = {r['N_bruns']:.5f} m ; N equipotencial = {r['N_num']:.5f} m")
    assert r["dif"] < 0.01 and abs(r["N_bruns"] - r["N_num"]) / r["N_num"] < 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
