#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B102-C06: calibracion de una celda de carga y medicion de una fuerza de traccion con incertidumbre.

Datos consultados (2026-11-10): aceleracion estandar de la gravedad g_n = 9.80665 m/s2 (NIST, CODATA 2022), usada para convertir masas
patron en fuerza nominal. ILUSTRATIVOS (sinteticos, no de una celda real): alcance 1000 N; sensibilidad verdadera 2.0004 mV/V, cero
0.0031 mV/V, no linealidad cuadratica de 0.02 % del alcance, ruido gaussiano de 0.0008 mV/V por lectura; masas patron 0 a 100 kg en
pasos de 12.5 kg; incertidumbre relativa de la fuerza de referencia (g local y masas) 5.8e-4 (estandar); semilla 20261110.
Modelo: V = a + b F (ajuste lineal por minimos cuadrados, una lectura por punto); medida: media de 4 lecturas; prediccion inversa
F = (V - a)/b; incertidumbre tipo A de ajuste y repeticion, tipo B de la referencia, combinadas en cuadratura (GUM); expandida con k = 2.
Unidades: F en N, V en mV/V. Sistema: eje de la celda alineado con la fuerza; sin efectos de temperatura ni de carga excentrica.
Tolerancias: desviacion tipica Monte Carlo frente a la analitica dentro del 5 %; recuperacion exacta de a y b sin ruido < 1e-9.
"""
from __future__ import annotations
import math, platform, random

GN = 9.80665
ALCANCE = 1000.0
S_V, ZERO, NL, SIG = 2.0004, 0.0031, 2.0e-4, 0.0008
U_REF = 5.8e-4
MASAS = [12.5 * i for i in range(9)]
F_REF = [m * GN for m in MASAS]
N_MED = 4


def salida(f, rng, ruido=True, nl=True):
    v = ZERO + S_V * f / ALCANCE
    if nl:
        v += NL * S_V * (f / ALCANCE) ** 2 * 1.0
    if ruido:
        v += rng.gauss(0.0, SIG)
    return v


def ajuste(x, y):
    n = len(x)
    xb, yb = sum(x) / n, sum(y) / n
    sxx = sum((xi - xb) ** 2 for xi in x)
    b = sum((xi - xb) * (yi - yb) for xi, yi in zip(x, y)) / sxx
    a = yb - b * xb
    res = [yi - (a + b * xi) for xi, yi in zip(x, y)]
    s = math.sqrt(sum(r * r for r in res) / (n - 2))
    return a, b, s, sxx, xb, res


def calibra(rng, ruido=True, nl=True, fuerza_g=1.0):
    y = [salida(f, rng, ruido, nl) for f in F_REF]
    return ajuste([f * fuerza_g for f in F_REF], y)


def medir(rng, f_real, a, b, ruido=True):
    v = sum(salida(f_real, rng, ruido) for _ in range(N_MED)) / N_MED
    return (v - a) / b


def u_analitica(f_hat, b, sig, sxx, xb):
    n = len(F_REF)
    ua = (sig / b) * math.sqrt(1.0 / N_MED + 1.0 / n + (f_hat - xb) ** 2 / sxx)
    ub = f_hat * U_REF
    return ua, ub, math.hypot(ua, ub)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Celda SINTETICA: alcance {ALCANCE:.0f} N; S = {S_V} mV/V; ruido {SIG} mV/V; {len(F_REF)} puntos de calibracion, 0 a {F_REF[-1]:.1f} N (g_n = {GN})")
    rng = random.Random(20261110)
    a, b, s, sxx, xb, res = calibra(rng)
    print(f"Ajuste: V = {a:.5f} + {b * 1000:.5f}e-3 F  [mV/V, N]; sensibilidad {b * ALCANCE:.4f} mV/V a plena escala; residuo tipico = {s:.5f} mV/V")
    print(f"Residuo maximo del ajuste = {max(abs(r) for r in res):.5f} mV/V = {max(abs(r) for r in res) / b:.3f} N")
    a0, b0, *_ = calibra(random.Random(1), ruido=False, nl=False)
    print(f"Sin ruido ni no linealidad: a = {a0:.9f} (verdadero {ZERO}), b*alcance = {b0 * ALCANCE:.9f} (verdadero {S_V})")
    assert abs(a0 - ZERO) < 1e-9 and abs(b0 * ALCANCE - S_V) < 1e-9
    f_real = 176.8
    f_hat = medir(rng, f_real, a, b)
    ua, ub, uc = u_analitica(f_hat, b, s, sxx, xb)
    print(f"Medicion de una traccion de barra SINTETICA de {f_real} N (media de {N_MED} lecturas):")
    print(f"  F = {f_hat:.3f} N ; u_A = {ua:.3f} N ; u_B (referencia) = {ub:.3f} N ; u_c = {uc:.3f} N ; U (k = 2) = {2 * uc:.3f} N")
    print(f"  U relativa = {200 * uc / f_hat:.2f} % de la lectura ; {200 * uc / ALCANCE:.3f} % del alcance")
    # Monte Carlo: recalibrar y medir muchas veces
    nmc = 4000
    errs = []
    for i in range(nmc):
        r = random.Random(50000 + i)
        fg = 1.0 + r.gauss(0.0, U_REF)
        aa, bb, ss, *_ = calibra(r, fuerza_g=fg)
        errs.append(medir(r, f_real, aa, bb) - f_real)
    media = sum(errs) / nmc
    sd = math.sqrt(sum((e - media) ** 2 for e in errs) / (nmc - 1))
    ua2, ub2, uc2 = u_analitica(f_real, b, SIG, sxx, xb)
    print(f"Monte Carlo ({nmc} calibraciones + medidas): sesgo = {media:+.3f} N ; desviacion tipica = {sd:.3f} N")
    print(f"  analitica con el ruido verdadero: u_c = {uc2:.3f} N ; cociente MC/analitica = {sd / uc2:.3f}")
    cobertura = sum(1 for e in errs if abs(e - media) <= 2 * uc2) / nmc
    print(f"  fraccion de errores dentro de +/- 2 u_c (cobertura aproximada) = {cobertura:.3f}")
    assert abs(sd / uc2 - 1) < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
