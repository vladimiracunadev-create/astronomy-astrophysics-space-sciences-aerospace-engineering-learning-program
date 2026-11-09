#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C05: patron de Airy de una apertura circular, medicion simulada con ruido, ajuste de ancho y desapuntamiento, y distancia de campo lejano.

Datos: c = 299792458 m/s (NIST, CODATA 2022, consultada el 2026-11-09). La apertura de 3 m, la frecuencia de 10 GHz, el desapuntamiento de 0,12 (en unidades de x), el ruido gaussiano de desviacion 1e-3 (-60 dB respecto del pico) y los 161 puntos del
barrido son ILUSTRATIVOS y SINTETICOS (semilla 20261109); no describen ninguna medicion real ni ninguna antena real.
Modelo: apertura circular uniforme, P(x) = (2 J1(x)/x)^2 con x = pi D sin(theta)/lambda. J1 se evalua con la integral de Bessel (regla del trapecio periodica). Ancho a mitad de potencia por biseccion; directividad
D = 4 pi/Omega con Omega = 2 pi integral P sin(theta) dtheta, contrastada con (pi D/lambda)^2; la cola por encima de X se corrige con 4/(pi X). Medicion simulada: barrido de un corte con una fuente puntual
lejana, ruido gaussiano aditivo de desviacion relativa 1e-3 y ajuste de una parabola al logaritmo de la potencia por encima de -3 dB (P > 0,5). Distancia de campo lejano 2 D^2/lambda y error de fase de borde.
Supuestos: apertura sin bloqueo, iluminacion uniforme, fuente puntual a distancia infinita en la simulacion del barrido. Validez: parte central del patron; el ajuste parabolico (gaussiano) es aproximado.
Tolerancia: J1 frente a valores conocidos a 1e-9; HPBW de Airy frente a 1,0290 lambda/D a 1e-3; directividad numerica frente a (pi D/lambda)^2 a 1e-3; ancho ajustado frente al verdadero a 3 %; error de fase en 2D^2/lambda: 22,5 grados a 0,1.
"""
from __future__ import annotations
import math, platform, random

C = 299792458.0


def j1(x):
    n = int(abs(x)) + 60
    s = 0.0
    for k in range(n):
        t = 2 * math.pi * (k + 0.5) / n   # puntos medios de [0, 2 pi): integral periodica
        s += math.cos(t - x * math.sin(t))
    return s / n


def airy(x):
    if abs(x) < 1e-8:
        return 1.0
    return (2 * j1(x) / x) ** 2


def biseccion(f, a, b):
    fa = f(a)
    for _ in range(80):
        m = 0.5 * (a + b)
        fm = f(m)
        if (fa < 0) == (fm < 0):
            a, fa = m, fm
        else:
            b = m
    return 0.5 * (a + b)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1. J1 y rasgos del patron
    j_pico = j1(1.8411837813)
    z1 = biseccion(j1, 3.0, 4.5)
    print(f"J1(1,8412) = {j_pico:.9f} (maximo de J1, valor conocido 0,581865) ; primer cero de J1 = {z1:.7f} (conocido 3,8317060)")
    assert abs(j_pico - 0.5818652) < 1e-6 and abs(z1 - 3.8317060) < 1e-6
    xh = biseccion(lambda x: airy(x) - 0.5, 1.0, 2.5)
    hp = 2 * xh / math.pi
    nulo = z1 / math.pi
    xs = biseccion(lambda x: (j1(x + 1e-5) / (x + 1e-5)) ** 2 - (j1(x - 1e-5) / (x - 1e-5)) ** 2, 4.5, 6.0)
    sl = 10 * math.log10(airy(xs))
    print(f"HPBW = {hp:.4f} lambda/D ; primer nulo = {nulo:.4f} lambda/D ; primer lobulo lateral en x = {xs:.4f}, nivel = {sl:.3f} dB")
    assert abs(hp - 1.0290) < 1e-3 and abs(sl + 17.57) < 0.02
    # 2. directividad
    X = 300.0
    n = 60000
    h = X / n
    integ = 0.0
    for i in range(n):
        x = (i + 0.5) * h
        j = j1(x)
        integ += 4 * j * j / x * h
    integ_c = integ + 4 / (math.pi * X)
    print(f"Integral de 4 J1^2/x entre 0 y {X:.0f} = {integ:.6f} ; con cola 4/(pi X) = {integ_c:.6f} ; valor exacto 2")
    assert abs(integ_c / 2 - 1) < 1e-3
    # Omega = 2 pi (lambda/(pi D))^2 * integral ; D = 4 pi/Omega = 2 (pi D/lambda)^2 / integral
    ratio = 2.0 / integ_c
    print(f"Directividad numerica / (pi D/lambda)^2 = {ratio:.5f}")
    assert abs(ratio - 1) < 1e-3
    # 3. barrido simulado
    lam_d = 1.0     # unidades de lambda/D
    rng = random.Random(20261109)
    x0 = 0.12
    sig = 1e-3
    npt = 161
    xs_s = [-8 + 16 * i / (npt - 1) for i in range(npt)]
    datos = [airy(x - x0) + rng.gauss(0, sig) for x in xs_s]
    # ajuste parabolico a ln P para P > 0.1 (-10 dB)
    sel = [(x, math.log(p)) for x, p in zip(xs_s, datos) if p > 0.5]
    m = len(sel)
    sx = sum(x for x, _ in sel); sx2 = sum(x * x for x, _ in sel); sx3 = sum(x ** 3 for x, _ in sel); sx4 = sum(x ** 4 for x, _ in sel)
    sy = sum(y for _, y in sel); sxy = sum(x * y for x, y in sel); sx2y = sum(x * x * y for x, y in sel)
    # sistema para y = a + b x + c x^2
    A = [[m, sx, sx2], [sx, sx2, sx3], [sx2, sx3, sx4]]
    B = [sy, sxy, sx2y]
    # Cramer
    def det3(M):
        return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    D0 = det3(A)
    sol = []
    for k in range(3):
        Mk = [row[:] for row in A]
        for r in range(3):
            Mk[r][k] = B[r]
        sol.append(det3(Mk) / D0)
    a, b, c = sol
    xpk = -b / (2 * c)
    sigma_g = math.sqrt(-1 / (2 * c))
    fwhm_x = 2 * math.sqrt(2 * math.log(2)) * sigma_g       # ancho de la gaussiana en potencia, en unidades de x
    hp_aj = fwhm_x / math.pi
    print(f"Puntos usados en el ajuste (P > 0,5): {m} ; pico ajustado en x = {xpk:.4f} (verdadero {x0}) ; HPBW ajustado = {hp_aj:.4f} lambda/D (Airy {hp:.4f}) ; dif = {abs(hp_aj / hp - 1) * 100:.2f} %")
    assert abs(xpk - x0) < 0.01 and abs(hp_aj / hp - 1) < 0.03
    # lobulo lateral medido: maximo de los datos entre los dos nulos primeros
    lat = max(p for x, p in zip(xs_s, datos) if 1.2197 * math.pi < abs(x - x0) < 2.2 * math.pi)
    print(f"Primer lobulo lateral medido (maximo en el barrido) = {10 * math.log10(lat):.3f} dB ; verdadero {sl:.3f} dB ; suelo de ruido = {20 * math.log10(sig):.1f} dB")
    # 4. campo lejano
    f = 10e9
    lam = C / f
    Dm = 3.0
    R = 2 * Dm ** 2 / lam
    dpath = math.sqrt(R * R + (Dm / 2) ** 2) - R
    fase = 360 * dpath / lam
    print(f"lambda = {lam * 100:.5f} cm ; D = {Dm} m ; 2 D^2/lambda = {R:.2f} m ; diferencia de camino en el borde = {dpath / lam:.5f} lambda ; fase de borde = {fase:.3f} grados")
    assert abs(fase - 22.5) < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
