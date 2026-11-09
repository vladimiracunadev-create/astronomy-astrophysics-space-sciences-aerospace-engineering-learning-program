#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B64-C02: curva de crecimiento frente a la temperatura y presion para mantener agua liquida.

Datos: SINTETICOS. Las tasas de crecimiento de un hipertermofilo hipotetico se generan con el modelo cardinal de Ratkowsky
(Tmin, Tmax, b, c ilustrativos) y ruido gaussiano de semilla fija. No son datos de ninguna cepa. Cita cualitativa consultada:
Kashefi y Lovley 2003 (solo el registro bibliografico; su resumen no se obtuvo) y Bloechl et al. 1997 (Pyrolobus fumarii, crecimiento entre 90 y 113 C con optimo cercano a 106 C, resumen consultado el 2026-11-09 en Europe PMC).
Constantes: R = 8.314462618 J/(mol K) (CODATA 2022, NIST, consultado 2026-11-09); T[K] = T[C] + 273.15.
Modelo 1 (Arrhenius): ln k = ln A - Ea/(R T), valido en la rama ascendente. Se ajusta por minimos cuadrados cerrados y se
compara con un ajuste por descenso de gradiente (via independiente).
Modelo 2 (Ratkowsky): sqrt(r) = b (T-Tmin)(1-exp(c (T-Tmax))). Temperatura optima por seccion aurea frente a barrido fino.
Modelo 3 (Clausius-Clapeyron, DH_vap = 40.66 kJ/mol constante, ILUSTRATIVO): presion de saturacion del agua entre 100 y 121 C,
integracion numerica RK4 frente a forma cerrada p = p0 exp(-DH/R (1/T - 1/T0)), con p0 = 101325 Pa a 373.15 K.
Es una aproximacion: el DH_vap real decrece con T; no sustituye a una tabla de vapor.
Supuestos: crecimiento exponencial balanceado, sin lisis. Validez: ilustrativa. Tolerancias: Ea recuperada a 3 %;
Topt seccion aurea vs barrido 0.05 K; RK4 vs cerrada 1e-6 relativo.
"""
from __future__ import annotations
import math, platform, random

R = 8.314462618
TMIN, TMAX, B, C = 60.0, 112.0, 0.045, 0.30   # ilustrativos (C, C, adim., 1/K)


def ratkowsky(Tc):
    if Tc <= TMIN or Tc >= TMAX:
        return 0.0
    return (B * (Tc - TMIN) * (1.0 - math.exp(C * (Tc - TMAX)))) ** 2   # 1/h


def ajuste_lineal(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    m = sxy / sxx
    return m, my - m * mx


def ajuste_gradiente(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    sx = math.sqrt(sum((a - mx) ** 2 for a in x) / len(x))
    xs = [(a - mx) / sx for a in x]
    m = b = 0.0
    for _ in range(20000):
        gm = sum(2 * (m * a + b - c) * a for a, c in zip(xs, y)) / len(xs)
        gb = sum(2 * (m * a + b - c) for a, c in zip(xs, y)) / len(xs)
        m -= 0.1 * gm
        b -= 0.1 * gb
    m_orig = m / sx
    return m_orig, b - m_orig * mx


def seccion_aurea(f, a, b, tol=1e-6):
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    while b - a > tol:
        if f(c) > f(d):
            b, d = d, c
            c = b - g * (b - a)
        else:
            a, c = c, d
            d = a + g * (b - a)
    return 0.5 * (a + b)


def clausius_rk4(T_final, DH=40660.0, p0=101325.0, T0=373.15, n=2000):
    h = (T_final - T0) / n
    f = lambda T, p: p * DH / (R * T * T)
    T, p = T0, p0
    for _ in range(n):
        k1 = f(T, p); k2 = f(T + h / 2, p + h * k1 / 2); k3 = f(T + h / 2, p + h * k2 / 2); k4 = f(T + h, p + h * k3)
        p += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        T += h
    return p


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: Tmin={TMIN} C, Tmax={TMAX} C, b={B}, c={C}")
    # rama ascendente con ruido
    rng = random.Random(20261109)
    temps = [62 + 2.5 * i for i in range(14)]  # 62 ... 94.5 C
    tasas = [ratkowsky(t) * (1 + rng.gauss(0, 0.01)) for t in temps]
    xs = [1.0 / (t + 273.15) for t in temps]
    ys = [math.log(k) for k in tasas]
    m1, b1 = ajuste_lineal(xs, ys)
    m2, b2 = ajuste_gradiente(xs, ys)
    Ea1, Ea2 = -m1 * R / 1000, -m2 * R / 1000
    print(f"Ea aparente (rama 62-94.5 C): minimos cuadrados cerrados {Ea1:.1f} kJ/mol ; descenso de gradiente {Ea2:.1f} kJ/mol")
    assert abs(Ea1 - Ea2) / Ea1 < 0.03
    # Ea de referencia: pendiente local del modelo sin ruido
    xs0 = [1.0 / (t + 273.15) for t in temps]
    ys0 = [math.log(ratkowsky(t)) for t in temps]
    Ea0 = -ajuste_lineal(xs0, ys0)[0] * R / 1000
    print(f"Ea aparente del modelo sin ruido: {Ea0:.1f} kJ/mol (el ruido del 1 % la perturba poco)")
    assert abs(Ea1 - Ea0) / Ea0 < 0.03
    # temperatura optima
    Topt = seccion_aurea(ratkowsky, TMIN + 1, TMAX - 0.01)
    barrido = max((ratkowsky(60 + 0.01 * i), 60 + 0.01 * i) for i in range(1, 5200))[1]
    print(f"Topt: seccion aurea {Topt:.3f} C ; barrido fino {barrido:.2f} C ; tasa maxima {ratkowsky(Topt):.4f} 1/h")
    assert abs(Topt - barrido) < 0.05
    print(f"Tiempo de duplicacion en Topt: {math.log(2) / ratkowsky(Topt):.2f} h ; a 100 C: {math.log(2) / ratkowsky(100):.2f} h")
    # presion de saturacion
    print(f"{'T [C]':>7} {'p cerrada [kPa]':>16} {'p RK4 [kPa]':>12}")
    for Tc in (100.0, 105.0, 113.0, 121.0):
        T = Tc + 273.15
        cerr = 101325.0 * math.exp(-40660.0 / R * (1 / T - 1 / 373.15))
        num = clausius_rk4(T)
        print(f"{Tc:7.1f} {cerr / 1000:16.2f} {num / 1000:12.2f}")
        assert abs(cerr - num) / cerr < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
