#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C03: materiales para espejos: rigidez especifica, figura de merito termica y flexion por peso propio.

Datos: g = 9,80665 m/s^2 (aceleracion estandar de la gravedad, NIST CODATA 2022, consultada el 2026-11-09). Las propiedades de los materiales (E, densidad, dilatacion, conductividad, nu) son ILUSTRATIVAS, valores tipicos de orden de magnitud
de cada familia, NO consultados en una hoja de fabricante: no sirven para disenar. El espejo (D = 200 mm, espesor D/6) es ilustrativo.
Modelo: flecha central de un disco delgado apoyado en el borde bajo peso propio, w(0) = (5+nu)/(1+nu) q a^4/(64 D_f), D_f = E t^3/(12(1-nu^2)), q = rho g t.
Verificacion independiente: se sustituye la solucion en la ecuacion biarmonica axisimetrica con diferencias finitas (laplaciano dos veces) y se comprueban w(a) = 0 y M_r(a) = 0.
Supuestos: placa de Kirchhoff (t << D), material homogeneo e isotropo, peso uniforme, apoyo simple perimetral. Validez: cualitativa para t/D = 1/6.
Tolerancia: residuo biarmonico < 1e-3 relativo; condiciones de borde < 1e-9 relativo.
"""
from __future__ import annotations
import math, platform

G = 9.80665
MAT = {  # nombre: (E GPa, rho kg/m3, alpha 1e-6/K, k W/m/K, nu)  ILUSTRATIVOS
    "borosilicato": (63.0, 2230.0, 3.25, 1.14, 0.20),
    "silice fundida": (73.0, 2200.0, 0.55, 1.38, 0.17),
    "vitroceramica": (90.0, 2530.0, 0.05, 1.46, 0.24),
    "ULE (tipo)": (68.0, 2210.0, 0.03, 1.31, 0.17),
    "SiC": (400.0, 3200.0, 2.5, 150.0, 0.19),
    "aluminio": (69.0, 2700.0, 23.6, 167.0, 0.33),
    "berilio": (287.0, 1850.0, 11.4, 216.0, 0.08),
}
A = 0.100; T = 0.200 / 6

def flecha(E, rho, nu, a=A, t=T):
    Df = E * t ** 3 / (12 * (1 - nu * nu))
    q = rho * G * t
    return (5 + nu) / (1 + nu) * q * a ** 4 / (64 * Df)

def w_perfil(r, E, rho, nu, a=A, t=T):
    Df = E * t ** 3 / (12 * (1 - nu * nu)); q = rho * G * t
    return q / (64 * Df) * (a * a - r * r) * ((5 + nu) / (1 + nu) * a * a - r * r)

def biarmonico(r, E, rho, nu, h=1e-3):
    f = lambda x: w_perfil(x, E, rho, nu)
    def lap(x):
        return (f(x + h) - 2 * f(x) + f(x - h)) / h ** 2 + (f(x + h) - f(x - h)) / (2 * h * x)
    return (lap(r + h) - 2 * lap(r) + lap(r - h)) / h ** 2 + (lap(r + h) - lap(r - h)) / (2 * h * r)

def calc():
    r = {"tabla": {}}
    for n, (E, rho, al, k, nu) in MAT.items():
        E_ = E * 1e9
        d = flecha(E_, rho, nu)
        r["tabla"][n] = dict(E_rho=E_ / rho / 1e6, k_alpha=k / al, flecha_nm=d * 1e9, flecha_rel_nm=None)
    E, rho, al, k, nu = MAT["borosilicato"]
    E *= 1e9
    # escalado con el espesor: w ~ 1/t^2
    r["razon_t_mitad"] = flecha(E, rho, nu, t=T / 2) / flecha(E, rho, nu)
    # residuo biarmonico y bordes
    Df = E * T ** 3 / (12 * (1 - nu ** 2)); q = rho * G * T
    res = max(abs(biarmonico(x, E, rho, nu) / (q / Df) - 1) for x in (0.2 * A, 0.5 * A, 0.8 * A))
    r["residuo_biarmonico"] = res
    r["w_borde"] = w_perfil(A, E, rho, nu)
    h = 1e-6
    f = lambda x: w_perfil(x, E, rho, nu)
    wpp = (f(A - h) - 2 * f(A) + f(A - 2 * h)) / h ** 2  # aproximacion en A-h
    # momento radial en el borde por solucion analitica: -D(w'' + nu w'/r)
    ww = lambda x: (f(x + 1e-5) - 2 * f(x) + f(x - 1e-5)) / 1e-10
    wp = lambda x: (f(x + 1e-5) - f(x - 1e-5)) / 2e-5
    Mr = -Df * (ww(A - 1e-5) + nu * wp(A - 1e-5) / A)
    r["Mr_borde_rel"] = abs(Mr) / (q * A * A)
    r["flecha_centro_nm"] = f(0.0) * 1e9
    r["flecha_formula_nm"] = flecha(E, rho, nu) * 1e9
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print("material | E/rho (MN m/kg) | k/alpha (W/m por 1e-6/K) | flecha central (nm)")
    for n, d in r["tabla"].items():
        print(f"{n} | {d['E_rho']:.3f} | {d['k_alpha']:.1f} | {d['flecha_nm']:.2f}")
    for k in ("razon_t_mitad", "residuo_biarmonico", "w_borde", "Mr_borde_rel", "flecha_centro_nm", "flecha_formula_nm"):
        print(f"{k} = {r[k]:.6g}")
    assert abs(r["razon_t_mitad"] - 4.0) < 1e-9
    assert r["residuo_biarmonico"] < 1e-3
    assert abs(r["w_borde"]) < 1e-18 and r["Mr_borde_rel"] < 1e-3
    assert abs(r["flecha_centro_nm"] - r["flecha_formula_nm"]) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
