#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B68-C02: fotodesorcion de hielos de CO y CO2, vida bajo un flujo UV y separacion de la desorcion y la fotolisis.

Datos publicados (consultados el 2026-11-09, texto completo en PDF):
 - Oberg, van Dishoeck y Linnartz (2009, A&A 496, 281; arXiv:0809.1333), lampara de H2 (7-10,5 eV): Y_CO(T) = 2,7e-3 - (T-15) 1,7e-4 moleculas/foton
   para 15-27 K; Y_N2 < 2e-4; Y_CO2(x) = 1,2e-3 (1 - exp(-x/2,9)) + 1,1e-3 (1 - exp(-x/4,6)), x = espesor en ML, a 15-18 K.
 - Fayolle et al. (2011, ApJ 739, L36; arXiv:1109.0281), Tabla 1, CO de 10 ML a 18 K: rendimientos absolutos a 8,2; 9,2; 10,2 y 11,2 eV =
   2,8e-2 ; 1,3e-2 ; 6,9e-3 ; 9,3e-3 moleculas/foton (incertidumbres 1,7e-2 ; 0,91e-2 ; 2,4e-3 ; 3,4e-3).
SINTETICO / ILUSTRATIVO: los flujos UV (1e3-1e5 fotones cm^-2 s^-1), los pesos espectrales, la curva de espesor frente a fluencia con ruido
(semilla fija) y la hipotesis de errores gaussianos independientes. Convencion: 1 ML = 1e15 moleculas cm^-2.
Modelo: desorcion superficial de orden cero, dN/dFluencia = -Y (fluencia en fotones cm^-2); fotolisis de primer orden en el volumen.
Referencias independientes: la ley lineal de propagacion de la varianza frente a Monte Carlo; la funcion de espesor generadora frente al ajuste.
Tolerancias: rendimiento ajustado dentro de 15 % del verdadero sintetico; desviacion MC frente a analitica < 3 %.
Unidades: rendimiento en moleculas/foton; flujo en fotones cm^-2 s^-1; tiempo en s y anos.
"""
from __future__ import annotations
import math, platform, random

ML = 1e15
SEC_ANIO = 365.25 * 86400.0


def y_co(T: float) -> float:
    """Rendimiento de CO puro [moleculas/foton], valido 15-27 K (Oberg 2009)."""
    return 2.7e-3 - (T - 15.0) * 1.7e-4


def y_co2(x: float) -> float:
    """Rendimiento de CO2 [moleculas/foton] frente al espesor x [ML] (Oberg 2009)."""
    return 1.2e-3 * (1 - math.exp(-x / 2.9)) + 1.1e-3 * (1 - math.exp(-x / 4.6))


def vida_1ml(Y: float, flujo: float) -> float:
    """Tiempo [s] en desorber 1 ML a rendimiento Y y flujo [fotones cm^-2 s^-1]."""
    return ML / (Y * flujo)


def resolver3(A, b):
    """Resuelve 3x3 por eliminacion gaussiana con pivoteo."""
    n = 3
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x


def ajuste_lineal_exp(fl, N):
    """Ajusta N = A - Yp*fl - B (1 - exp(-s fl)) con fl en 1e17 fotones cm^-2; barrido en s y minimos cuadrados lineales."""
    mejor = None
    for k in range(1, 400):
        s = 0.01 * k
        cols = [[1.0 for _ in fl], [-f for f in fl], [-(1 - math.exp(-s * f)) for f in fl]]
        A = [[sum(cols[i][m] * cols[j][m] for m in range(len(fl))) for j in range(3)] for i in range(3)]
        b = [sum(cols[i][m] * N[m] for m in range(len(fl))) for i in range(3)]
        try:
            x = resolver3(A, b)
        except ZeroDivisionError:
            continue
        chi = sum((x[0] * cols[0][m] + x[1] * cols[1][m] + x[2] * cols[2][m] - N[m]) ** 2 for m in range(len(fl)))
        if mejor is None or chi < mejor[0]:
            mejor = (chi, s, x)
    return mejor


def calcular():
    # 1) tablas publicadas
    T_lista = (15.0, 18.0, 21.0, 24.0, 27.0)
    ycoT = [(T, y_co(T)) for T in T_lista]
    x_lista = (1.0, 2.0, 5.0, 10.0, 20.0)
    yco2 = [(x, y_co2(x)) for x in x_lista]
    y_lim = 1.2e-3 + 1.1e-3
    lo, hi = 0.0, 100.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if y_co2(mid) < 0.9 * y_lim:
            lo = mid
        else:
            hi = mid
    x90 = 0.5 * (lo + hi)
    # 2) vida de 1 ML de CO con flujos sinteticos
    vidas = [(F, vida_1ml(y_co(15.0), F) / SEC_ANIO) for F in (1e3, 1e4, 1e5)]
    # 3) promedio espectral con la Tabla 1 de Fayolle (pesos SINTETICOS) y propagacion de errores
    E_eV = (8.2, 9.2, 10.2, 11.2)
    Yf = (2.8e-2, 1.3e-2, 6.9e-3, 9.3e-3)
    sig = (1.7e-2, 0.91e-2, 2.4e-3, 3.4e-3)
    espectros = {"A (sint.: mas fotones a 10-11 eV)": (0.1, 0.2, 0.4, 0.3), "B (sint.: mas fotones a 8-9 eV)": (0.5, 0.3, 0.1, 0.1)}
    medias = {}
    rng = random.Random(20261109)
    for nom, w in espectros.items():
        m = sum(wi * yi for wi, yi in zip(w, Yf))
        s_an = math.sqrt(sum((wi * si) ** 2 for wi, si in zip(w, sig)))
        muestras = []
        for _ in range(200000):
            muestras.append(sum(wi * rng.gauss(yi, si) for wi, yi, si in zip(w, Yf, sig)))
        mm = sum(muestras) / len(muestras)
        sd = math.sqrt(sum((v - mm) ** 2 for v in muestras) / (len(muestras) - 1))
        medias[nom] = (m, s_an, mm, sd)
    # 4) separacion desorcion / fotolisis con curva SINTETICA y ruido
    Y_ver = 2.7e-3
    A0, B1, sigma_f = 10.0, 1.5, 0.35  # ML, ML, (1e17 fotones cm^-2)^-1
    fl = [0.5 * i for i in range(0, 41)]  # fluencia en 1e17 fotones cm^-2
    rng2 = random.Random(7)
    Yp_ver = Y_ver * 1e17 / ML  # ML por 1e17 fotones cm^-2
    N = [A0 - Yp_ver * f - B1 * (1 - math.exp(-sigma_f * f)) + rng2.gauss(0, 0.02) for f in fl]
    chi, s_aj, x = ajuste_lineal_exp(fl, N)
    Y_aj = x[1] * ML / 1e17
    # ajuste ingenuo: solo recta
    n = len(fl); mf = sum(fl) / n; mN = sum(N) / n
    pend = sum((f - mf) * (v - mN) for f, v in zip(fl, N)) / sum((f - mf) ** 2 for f in fl)
    Y_ing = -pend * ML / 1e17
    return dict(ycoT=ycoT, yco2=yco2, y_lim=y_lim, x90=x90, vidas=vidas, E_eV=E_eV, Yf=Yf, medias=medias,
                Y_ver=Y_ver, Y_aj=Y_aj, s_aj=s_aj, Y_ing=Y_ing, B_aj=x[2], A_aj=x[0], sigma_f=sigma_f, B1=B1)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print("CO puro, 15-27 K (Oberg 2009): Y(T) = 2.7e-3 - (T-15) 1.7e-4 moleculas/foton")
    for T, y in r["ycoT"]:
        print(f"  T = {T:4.0f} K -> Y = {y:.3e}")
    print("CO2 (Oberg 2009): Y(x) = 1.2e-3 (1-exp(-x/2.9)) + 1.1e-3 (1-exp(-x/4.6))")
    for x, y in r["yco2"]:
        print(f"  x = {x:5.1f} ML -> Y = {y:.3e}")
    print(f"  limite x -> infinito = {r['y_lim']:.2e} ; 90 % del limite a x = {r['x90']:.2f} ML")
    print("Vida de 1 ML de CO a 15 K (flujos SINTETICOS):")
    for F, t in r["vidas"]:
        print(f"  F = {F:.0e} fotones cm^-2 s^-1 -> {t:.3e} anos")
    print("Fayolle 2011, Tabla 1 (CO 10 ML, 18 K): " + " ; ".join(f"{e} eV -> {y:.1e}" for e, y in zip(r["E_eV"], r["Yf"])))
    for nom, (m, s_an, mm, sd) in r["medias"].items():
        print(f"  Espectro {nom}: Y medio = {m:.3e} ; sigma analitica = {s_an:.3e} ; Monte Carlo media = {mm:.3e}, sigma = {sd:.3e} ; dif. sigma = {abs(sd / s_an - 1) * 100:.2f} %")
    print(f"Curva SINTETICA de espesor: Y verdadero = {r['Y_ver']:.2e} ; ajuste lineal+exp = {r['Y_aj']:.3e} (sigma_f ajustada = {r['s_aj']:.2f}, verdadera {r['sigma_f']:.2f}) ; solo recta = {r['Y_ing']:.3e}")
    # pruebas
    ys = [y for _, y in r["ycoT"]]
    assert all(a > b for a, b in zip(ys, ys[1:]))
    assert abs(r["ycoT"][0][1] - 2.7e-3) < 1e-12
    assert abs(r["y_lim"] - 2.3e-3) < 1e-12
    for nom, (m, s_an, mm, sd) in r["medias"].items():
        assert abs(sd / s_an - 1) < 0.03 and abs(mm - m) < 4 * s_an / math.sqrt(200000) + 1e-9
    assert abs(r["Y_aj"] / r["Y_ver"] - 1) < 0.15
    assert abs(r["Y_ing"] / r["Y_ver"] - 1) > abs(r["Y_aj"] / r["Y_ver"] - 1)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
