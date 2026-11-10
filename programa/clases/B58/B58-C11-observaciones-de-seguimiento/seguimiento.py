#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C11: observaciones de seguimiento: crecimiento de la incertidumbre de prediccion y probabilidad de recuperar el objeto en el campo.

Datos: SINTETICOS. Movimiento lineal en una coordenada del cielo, 8 observaciones en 3 dias con error de 0.3 arcsec, ajuste de recta; incertidumbre bidimensional de 10 arcmin por eje y campos
de radio 5, 10 y 20 arcmin. Ningun objeto real.
Modelo: (1) prediccion por recta de minimos cuadrados: sigma_pred(t)^2 = sigma^2 (1/N + (t - tm)^2 / Sxx) con tm la media de las fechas y Sxx = sum (t_i - tm)^2, frente a 4000 ajustes Monte
Carlo (semilla 20261109); (2) probabilidad de recuperar un objeto en un campo circular de radio r con error gaussiano de sigma por eje: P = 1 - exp(-r^2 / 2 sigma^2), frente a Monte Carlo (400 000).
Unidades: arcsec, arcmin, dia. Supuestos: movimiento rectilineo uniforme, ruido gaussiano independiente. Validez: ilustrativa; la curvatura real de la orbita se trata en C08.
Tolerancia: sigma_pred analitico frente a Monte Carlo 5 %; probabilidad de campo dentro de 3 errores binomiales.
"""
import math, platform, random

def sigma_pred(ts, sig, t):
    N = len(ts); tm = sum(ts) / N; sxx = sum((x - tm) ** 2 for x in ts)
    return sig * math.sqrt(1.0 / N + (t - tm) ** 2 / sxx)

def ajuste_recta(ts, ys):
    N = len(ts); tm = sum(ts) / N; ym = sum(ys) / N
    sxx = sum((x - tm) ** 2 for x in ts)
    m = sum((x - tm) * (y - ym) for x, y in zip(ts, ys)) / sxx
    return ym - m * tm, m

def calcular():
    sig = 0.3
    ts3 = [3.0 * k / 7 for k in range(8)]
    ts10 = [10.0 * k / 7 for k in range(8)]
    rng = random.Random(20261109)
    filas = []
    for t in (5.0, 10.0, 30.0, 100.0):
        res = []
        for ts in (ts3, ts10):
            ana = sigma_pred(ts, sig, t)
            errs = []
            for _ in range(4000):
                ys = [0.5 * x + rng.gauss(0, sig) for x in ts]
                b0, m = ajuste_recta(ts, ys)
                errs.append(b0 + m * t - 0.5 * t)
            mc = math.sqrt(sum(e * e for e in errs) / len(errs))
            res += [ana, mc]
        filas.append((t,) + tuple(res))
    campo = []
    s = 10.0
    N = 400000
    for rr in (5.0, 10.0, 20.0):
        ana = 1 - math.exp(-rr * rr / (2 * s * s))
        k = sum(1 for _ in range(N) if rng.gauss(0, s) ** 2 + rng.gauss(0, s) ** 2 <= rr * rr)
        campo.append((rr, ana, k / N, math.sqrt(ana * (1 - ana) / N)))
    return {"filas": filas, "campo": campo}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Prediccion a t dias del inicio (error de observacion 0.3 arcsec, 8 observaciones):")
    print("%7s %14s %12s %14s %12s" % ("t[d]", "arco 3 d ana", "MC", "arco 10 d ana", "MC"))
    for f in r["filas"]:
        print("%7.0f %13.2f\" %11.2f\" %13.2f\" %11.2f\"" % f)
    print("Probabilidad de recuperar el objeto en un campo de radio r (sigma = 10 arcmin por eje):")
    for rr, a, m, e in r["campo"]:
        print("  r = %4.0f arcmin : analitica = %.4f ; Monte Carlo = %.4f ; diferencia = %+.2f errores" % (rr, a, m, (m - a) / e))
    for f in r["filas"]:
        assert abs(f[2] / f[1] - 1) < 0.05 and abs(f[4] / f[3] - 1) < 0.05
    for rr, a, m, e in r["campo"]:
        assert abs(m - a) < 3 * e
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
