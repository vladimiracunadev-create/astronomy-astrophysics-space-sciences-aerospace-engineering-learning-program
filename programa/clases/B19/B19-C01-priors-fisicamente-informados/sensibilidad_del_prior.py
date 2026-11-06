#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B19-C01: sensibilidad del prior en una tasa de conteo.

Datos: SINTETICOS. Un contador de particulas de un CubeSat registra n eventos
en T horas. Se usan tres conjuntos con la misma tasa observada n/T = 3 /h:
(n, T) = (3, 1), (30, 10), (300, 100).
Modelo: n | lambda ~ Poisson(lambda*T); lambda [eventos/h] > 0.
Priors: Gamma(a, b) con b = tasa (1/h). Posterior conjugada exacta:
Gamma(a + n, b + T). Priors comparados:
  uniforme (a=1, b=0), Jeffreys (a=0.5, b=0), informado Gamma(4, 1)
  (media 4 /h, desviacion 2 /h: fondo esperado "de laboratorio", sintetico).
Supuestos: eventos independientes, tasa constante, sin tiempo muerto.
Validez: lambda*T moderado; sin saturacion del detector.
Tolerancia: la rejilla numerica reproduce la media y la varianza Gamma exactas
a 1e-4 relativa; la predictiva a priori suma 1 a 1e-9.
Solo numpy; ASCII en la salida.
"""
from __future__ import annotations
import math
import platform
import sys

import numpy as np

LAM = np.linspace(1e-6, 60.0, 600_001)      # rejilla de lambda [1/h]
DL = LAM[1] - LAM[0]


def log_gamma_pdf(lam, a, b):
    if b == 0.0:                              # prior impropio: constante * lam^(a-1)
        return (a - 1.0) * np.log(lam)
    return a * math.log(b) - math.lgamma(a) + (a - 1.0) * np.log(lam) - b * lam


def posterior_rejilla(n, T, a, b):
    logp = log_gamma_pdf(LAM, a, b) + n * np.log(LAM * T) - LAM * T
    p = np.exp(logp - logp.max())
    return p / (p.sum() * DL)


def media_y_intervalo(p, nivel=0.90):
    m = float((LAM * p).sum() * DL)
    c = np.cumsum(p) * DL
    lo = float(LAM[np.searchsorted(c, (1 - nivel) / 2)])
    hi = float(LAM[np.searchsorted(c, 1 - (1 - nivel) / 2)])
    return m, lo, hi


def pruebas():
    # 1) rejilla vs Gamma exacta (media y varianza)
    n, T, a, b = 30, 10.0, 4.0, 1.0
    p = posterior_rejilla(n, T, a, b)
    A, B = a + n, b + T
    m = (LAM * p).sum() * DL
    v = ((LAM - m) ** 2 * p).sum() * DL
    assert abs(m - A / B) / (A / B) < 1e-4, (m, A / B)
    assert abs(v - A / B ** 2) / (A / B ** 2) < 1e-4, (v, A / B ** 2)
    # 2) predictiva a priori Gamma(4,1), T = 1 h: binomial negativa exacta
    k = np.arange(0, 400)
    lognb = (np.array([math.lgamma(x + a) - math.lgamma(x + 1) - math.lgamma(a) for x in k])
             + a * math.log(b / (b + 1.0)) + k * math.log(1.0 / (b + 1.0)))
    assert abs(np.exp(lognb).sum() - 1.0) < 1e-9
    # 3) datos abundantes: el prior deja de importar
    medias = [media_y_intervalo(posterior_rejilla(300, 100.0, *pr))[0]
              for pr in [(1.0, 0.0), (0.5, 0.0), (4.0, 1.0)]]
    assert max(medias) - min(medias) < 0.05, medias


def main():
    print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.platform())
    pruebas()
    print("Pruebas: OK\n")
    priors = {"uniforme(1,0)": (1.0, 0.0), "Jeffreys(0.5,0)": (0.5, 0.0), "informado(4,1)": (4.0, 1.0)}
    datos = [(3, 1.0), (30, 10.0), (300, 100.0)]
    print("Posterior de lambda [1/h]: media [intervalo central 90 %]  (tasa observada n/T = 3.00)")
    print(f"{'prior':<18}" + "".join(f"n={n},T={int(T):<8}" for n, T in datos))
    for nom, (a, b) in priors.items():
        fila = f"{nom:<18}"
        for n, T in datos:
            m, lo, hi = media_y_intervalo(posterior_rejilla(n, T, a, b))
            fila += f"{m:5.2f} [{lo:4.2f},{hi:5.2f}]  "
        print(fila)
    # conflicto prior-datos
    n, T = 60, 2.0
    m, lo, hi = media_y_intervalo(posterior_rejilla(n, T, 4.0, 1.0))
    print(f"\nConflicto: Gamma(4,1) con n={n}, T={T:g} h (n/T = {n/T:.1f}/h): "
          f"media posterior {m:.2f} (exacta {(4+n)/(1+T):.2f}), 90 % [{lo:.2f}, {hi:.2f}]")
    # prior truncado por saturacion fisica lambda <= 20 /h
    p = posterior_rejilla(30, 10.0, 4.0, 1.0)
    pt = np.where(LAM <= 20.0, p, 0.0)
    pt /= pt.sum() * DL
    print("Truncar el prior en 20 /h con (30,10): media", f"{(LAM*pt).sum()*DL:.4f}",
          "vs sin truncar", f"{(LAM*p).sum()*DL:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
