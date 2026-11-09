#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C03: serie sintetica de manchas solares, periodo del ciclo y autocorrelacion.

Datos: ninguna constante fisica. Contexto: el ciclo solar de unos 11 anios se caracteriza por la subida y bajada del numero y del area de las manchas, y otros
indicadores (flujo a 10.7 cm, irradiancia total, campo magnetico, fulguraciones, eyecciones de masa coronal, actividad geomagnetica, flujo de rayos cosmicos
galacticos) varian en asociacion con ellas (Hathaway, arXiv:1502.07020, resumen, consultado 2026-11-09). La forma del ciclo (x^2 e^-x con maximo a 4 anios), las duraciones
(11 +/- 1 anios), las amplitudes (lognormales) y el ruido (15 %) son ILUSTRATIVOS (sinteticos); la serie no reproduce ningun registro historico.
Modelo: suma de ciclos s(t) = A_k ((t - t_k)/tau)^2 exp(-(t - t_k)/tau) con tau = 2 anios, comienzos t_{k+1} - t_k ~ N(11, 1); muestreo mensual durante 130 anios;
periodograma de Lomb-Scargle y funcion de autocorrelacion; Monte Carlo (semilla fija) del periodo recuperado.
Supuestos: ciclos independientes, ruido multiplicativo. Validez: ilustrativa.
Tolerancia: periodo recuperado dentro de 0.4 anios de 11 y media de 50 realizaciones dentro de 3 errores.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

TAU = 2.0


def serie(rng, anios=130.0, paso=1 / 12):
    comienzos = [0.0]
    while comienzos[-1] < anios + 20:
        comienzos.append(comienzos[-1] + rng.gauss(11.0, 1.0))
    amps = [math.exp(rng.gauss(math.log(100.0), 0.35)) for _ in comienzos]
    ts = [i * paso for i in range(int(anios / paso))]
    ys = []
    for t in ts:
        v = 0.0
        for tk, a in zip(comienzos, amps):
            x = (t - tk) / TAU
            if 0 <= x < 12:
                v += a * x * x * math.exp(-x) / (4 * math.exp(-2))
        ys.append(v * (1 + 0.15 * rng.gauss(0, 1)))
    return ts, ys


def ls(ts, ys, f):
    w = 2 * math.pi * f
    s2 = sum(math.sin(2 * w * t) for t in ts)
    c2 = sum(math.cos(2 * w * t) for t in ts)
    tau = math.atan2(s2, c2) / (2 * w)
    cs = [math.cos(w * (t - tau)) for t in ts]
    sn = [math.sin(w * (t - tau)) for t in ts]
    return 0.5 * (sum(y * c for y, c in zip(ys, cs)) ** 2 / sum(c * c for c in cs) + sum(y * s for y, s in zip(ys, sn)) ** 2 / sum(s * s for s in sn))


def autocorr(ys, lag):
    n = len(ys)
    m = sum(ys) / n
    num = sum((ys[i] - m) * (ys[i + lag] - m) for i in range(n - lag))
    den = sum((y - m) ** 2 for y in ys)
    return num / den


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    ts, ys = serie(rng)
    ym = sum(ys) / len(ys)
    yc = [y - ym for y in ys]
    print(f"{len(ts)} valores mensuales en 130 anios ; maximo = {max(ys):.1f} ; media = {ym:.1f} ; fraccion de meses con valor < 10 % del maximo = {sum(1 for y in ys if y < 0.1 * max(ys)) / len(ys):.2f}")
    fs = [0.03 + 0.0005 * i for i in range(400)]
    pot = [ls(ts, yc, f) for f in fs]
    i = max(range(len(fs)), key=lambda j: pot[j])
    print(f"periodograma de Lomb-Scargle: pico en f = {fs[i]:.4f} /anio -> periodo = {1 / fs[i]:.2f} anios")
    lags = {l: autocorr(yc, int(l * 12)) for l in (2, 5.5, 8, 11, 22)}
    print(f"{'lag [anios]':>12} {'autocorrelacion':>16}")
    for l, a in lags.items():
        print(f"{l:12.1f} {a:16.3f}")
    assert lags[11] > lags[5.5] and lags[22] > lags[8], "la autocorrelacion tiene maximos en multiplos del periodo"
    ps = []
    for _ in range(50):
        t2, y2 = serie(rng)
        m2 = sum(y2) / len(y2)
        y2 = [y - m2 for y in y2]
        p2 = [ls(t2, y2, f) for f in fs[::2]]
        j = max(range(len(p2)), key=lambda k: p2[k])
        ps.append(1 / fs[::2][j])
    mm, ss = statistics.mean(ps), statistics.pstdev(ps)
    print(f"50 realizaciones: periodo recuperado = {mm:.3f} +/- {ss:.3f} anios (verdadero 11)")
    assert abs(mm - 11) < 0.4 and abs(mm - 11) < 3 * ss / math.sqrt(50) + 0.15, "periodo medio"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
