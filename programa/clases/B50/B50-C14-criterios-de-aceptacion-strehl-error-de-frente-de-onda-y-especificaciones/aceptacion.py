#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C14: criterios de aceptacion (razon de Strehl, error de frente de onda RMS y banda de guarda).

Datos: ninguna constante fisica consultada. Las aberraciones (esferica y desenfoque), la poblacion de unidades (RMS verdadero normal de media 0.040 y desviacion 0.010 ondas), la incertidumbre
de medida de 0.005 ondas y el limite de 0.050 ondas RMS son ILUSTRATIVOS (sinteticos); no corresponden a ninguna especificacion real.
Modelo: pupila circular unidad; Strehl exacto de la intensidad central S = |media de exp(i 2 pi W)|^2 sobre una malla de 401 x 401; aproximacion de Marechal exp(-(2 pi sigma)^2) y su
version truncada 1 - (2 pi sigma)^2; caso analitico del desenfoque puro S = (sin(pi a)/(pi a))^2 con a el valor pico a valle; criterio de Rayleigh (lambda/4 PV de esferica con mejor enfoque).
Aceptacion con banda de guarda: se acepta si el RMS medido <= L - k u; riesgos del consumidor y del productor por Monte Carlo (semilla 20261109) y por cuadratura determinista.
Supuestos: aberracion pequena y simetrica (el maximo esta en el centro), poblacion normal. Validez: ilustrativa.
Tolerancia: desenfoque numerico frente a la formula 3e-4; Marechal frente a exacto 1.5 % hasta sigma 0.1; riesgos Monte Carlo frente a cuadratura dentro de 3 errores binomiales.
"""
from __future__ import annotations
import math, platform, random

NG = 401


def malla():
    pts = []
    for i in range(NG):
        for j in range(NG):
            x = -1.0 + 2.0 * (i + 0.5) / NG
            y = -1.0 + 2.0 * (j + 0.5) / NG
            r2 = x * x + y * y
            if r2 <= 1.0:
                pts.append(r2)
    return pts


def strehl(w):
    c = sum(math.cos(2 * math.pi * x) for x in w)
    s = sum(math.sin(2 * math.pi * x) for x in w)
    n = len(w)
    return (c * c + s * s) / (n * n)


def rms(w):
    m = sum(w) / len(w)
    return math.sqrt(sum((x - m) ** 2 for x in w) / len(w))


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def calcular():
    P = malla()
    z40 = [math.sqrt(5.0) * (6 * r2 * r2 - 6 * r2 + 1) for r2 in P]
    tabla = []
    for sg in (0.025, 0.05, 0.075, 0.10, 0.15, 0.20):
        w = [sg * z for z in z40]
        sr = rms(w)
        tabla.append((sg, sr, strehl(w), math.exp(-(2 * math.pi * sr) ** 2), 1 - (2 * math.pi * sr) ** 2))
    # desenfoque puro
    des = []
    for a in (0.1, 0.25, 0.5):
        w = [a * r2 for r2 in P]
        des.append((a, strehl(w), (math.sin(math.pi * a) / (math.pi * a)) ** 2, rms(w), a / (2 * math.sqrt(3.0))))
    # Rayleigh: esferica de una onda con el mejor enfoque
    w = [1.0 * (r2 * r2 - r2) for r2 in P]
    ray = (max(w) - min(w), rms(w), strehl(w), math.exp(-(2 * math.pi * rms(w)) ** 2))
    # aceptacion
    L, U, mu, sd = 0.050, 0.005, 0.040, 0.010
    rng = random.Random(20261109)
    N = 200000
    datos = []
    for _ in range(N):
        t = max(0.0, rng.gauss(mu, sd))
        datos.append((t, t + rng.gauss(0.0, U)))
    riesgos = []
    for k in (0.0, 1.0, 1.645):
        lim = L - k * U
        cons = sum(1 for t, m in datos if m <= lim and t > L) / N
        prod = sum(1 for t, m in datos if m > lim and t <= L) / N
        # cuadratura determinista (sobre la normal sin truncar; el recorte en 0 es despreciable)
        cons_q = prod_q = 0.0
        M = 4000
        lo, hi = mu - 6 * sd, mu + 6 * sd
        dt = (hi - lo) / M
        for i in range(M):
            t = lo + (i + 0.5) * dt
            dens = math.exp(-0.5 * ((t - mu) / sd) ** 2) / (sd * math.sqrt(2 * math.pi))
            pa = phi((lim - t) / U)
            if t > L:
                cons_q += dens * pa * dt
            else:
                prod_q += dens * (1 - pa) * dt
        riesgos.append((k, lim, cons, cons_q, prod, prod_q))
    p_malo = sum(1 for t, m in datos if t > L) / N
    return dict(tabla=tabla, des=des, ray=ray, riesgos=riesgos, p_malo=p_malo, N=N, L=L)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print("Esferica de Zernike Z(4,0): Strehl exacto (intensidad central) frente a la aproximacion de Marechal")
    print(f"{'RMS [ondas]':>11} {'S exacto':>9} {'exp(-(2 pi s)^2)':>17} {'1-(2 pi s)^2':>13}")
    for sg, sr, s, m, t in r["tabla"]:
        print(f"{sr:11.4f} {s:9.4f} {m:17.4f} {t:13.4f}")
    print("Desenfoque puro: numerico frente a (sin(pi a)/(pi a))^2")
    for a, s, f, sr, sa in r["des"]:
        print(f"  a = {a:4.2f} ondas PV: S numerico = {s:.6f} ; formula = {f:.6f} ; RMS = {sr:.5f} (a / (2 raiz 3) = {sa:.5f})")
    print(f"Rayleigh: esferica de 1 onda con el mejor enfoque: PV = {r['ray'][0]:.4f} ondas ; RMS = {r['ray'][1]:.4f} ; S exacto = {r['ray'][2]:.4f} ; Marechal = {r['ray'][3]:.4f}")
    print(f"Aceptacion con limite L = {r['L']} ondas RMS, incertidumbre u = 0.005 ; fraccion verdaderamente fuera de especificacion = {r['p_malo']:.4f}")
    print(f"{'k':>6} {'limite de medida':>17} {'consumidor MC':>14} {'consumidor Q':>13} {'productor MC':>13} {'productor Q':>12}")
    for k, lim, c, cq, p, pq in r["riesgos"]:
        print(f"{k:6.3f} {lim:17.5f} {c:14.5f} {cq:13.5f} {p:13.5f} {pq:12.5f}")
    for sg, sr, s, m, t in r["tabla"]:
        if sr <= 0.10:
            assert abs(m - s) / s < 0.015
    for a, s, f, sr, sa in r["des"]:
        assert abs(s - f) < 3e-4 and abs(sr - sa) < 1e-3
    assert abs(r["ray"][0] - 0.25) < 0.01 and abs(r["ray"][2] - 0.80) < 0.02
    for k, lim, c, cq, p, pq in r["riesgos"]:
        for mc, q in ((c, cq), (p, pq)):
            e = math.sqrt(max(q, 1e-9) * (1 - q) / r["N"])
            assert abs(mc - q) < 3 * e + 1e-4
    assert r["riesgos"][2][2] < r["riesgos"][0][2] and r["riesgos"][2][4] > r["riesgos"][0][4]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
