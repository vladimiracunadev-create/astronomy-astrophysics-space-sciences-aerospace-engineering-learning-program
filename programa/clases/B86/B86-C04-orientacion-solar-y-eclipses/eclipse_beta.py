#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C04: eclipse y orientacion solar de un satelite SINTETICO en orbita circular de 600 km.

Datos consultados (2026-11-10): GM = 0.39860e6 km3/s2 y radio medio 6371.000 km de la Tierra (NASA/NSSDC, Earth Fact Sheet).
ILUSTRATIVOS (sinteticos): altitud 600 km; angulos beta de 0, 30, 50 y 70 grados; tres estrategias de orientacion del ala
(fija con normal al cenit, un eje que sigue al Sol, dos ejes).
Modelo: orbita circular, sombra cilindrica (sin penumbra), Sol a distancia infinita con vector s = (cos beta, 0, sin beta), orbita en el plano xy.
Formula cerrada: f(beta) = acos( sqrt(h^2 + 2 R h) / ((R + h) cos beta) ) / pi para |beta| < beta* = asin(R/(R + h)).
Segunda via: muestreo geometrico de la orbita (1e6 puntos) con la prueba de sombra cilindrica.
Tolerancia: fraccion de eclipse numerica frente a la cerrada < 1e-5.
"""
from __future__ import annotations
import math, platform

MU, RE, H = 398600.0, 6371.0, 600.0
A = RE + H
T = 2.0 * math.pi * math.sqrt(A ** 3 / MU)
BSTAR = math.asin(RE / A)


def frac_cerrada(beta):
    if abs(beta) >= BSTAR:
        return 0.0
    return math.acos(math.sqrt(H * H + 2.0 * RE * H) / (A * math.cos(beta))) / math.pi


def frac_numerica(beta, n=1_000_000):
    s = (math.cos(beta), 0.0, math.sin(beta))
    cnt = 0
    for k in range(n):
        u = 2.0 * math.pi * (k + 0.5) / n
        x, y = A * math.cos(u), A * math.sin(u)
        d = x * s[0]                       # r . s (z = 0)
        if d < 0.0:
            p2 = x * x + y * y - d * d     # distancia al eje del cilindro al cuadrado
            if p2 < RE * RE:
                cnt += 1
    return cnt / n


def cos_medios(beta, n=200000):
    """Medias sobre una orbita completa de cos(incidencia) para tres orientaciones; cero en eclipse."""
    fija = uno = dos = 0.0
    s = (math.cos(beta), 0.0, math.sin(beta))
    for k in range(n):
        u = 2.0 * math.pi * (k + 0.5) / n
        x, y = A * math.cos(u), A * math.sin(u)
        d = x * s[0]
        if d < 0.0 and (x * x + y * y - d * d) < RE * RE:
            continue
        zenit = (x * s[0]) / A               # r_hat . s con r_hat = (cos u, sin u, 0)
        fija += max(0.0, zenit)
        uno += math.cos(beta)
        dos += 1.0
    return fija / n, uno / n, dos / n


def resultados():
    r = dict(T=T, bstar=math.degrees(BSTAR))
    for b in (0, 30, 50, 70):
        br = math.radians(b)
        r[f"f{b}"] = frac_cerrada(br)
        r[f"te{b}"] = frac_cerrada(br) * T
    r["fn0"] = frac_numerica(0.0)
    r["fn50"] = frac_numerica(math.radians(50))
    r["d0"] = abs(r["fn0"] - r["f0"])
    r["d50"] = abs(r["fn50"] - r["f50"])
    c = cos_medios(0.0)
    r["cfija0"], r["cuno0"], r["cdos0"] = c
    c = cos_medios(math.radians(50))
    r["cfija50"], r["cuno50"], r["cdos50"] = c
    r["pct0"] = r["f0"] * 100.0
    r["pct50"] = r["f50"] * 100.0
    r["bstar_rad"] = BSTAR
    r["f30_pct"] = r["f30"] * 100.0
    r["ra"] = RE / A
    r["rel_dos"] = (1.0 - r["f0"]) / (1.0 - r["f50"])
    r["rel_uno"] = r["cuno50"] / r["cuno0"]
    r["b25"] = math.degrees(math.acos(math.sqrt(H * H + 2.0 * RE * H) / A / math.cos(math.pi / 4.0)))
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Orbita SINTETICA h = {H:.0f} km: T = {T:.1f} s ; beta critico = {r['bstar']:.3f} grados")
    print(" beta [gr]  eclipse [%]  eclipse [s]")
    for b in (0, 30, 50, 70):
        print(f" {b:8d}  {r[f'f{b}']*100:11.3f}  {r[f'te{b}']:11.1f}")
    print(f"Fraccion de eclipse beta = 0: cerrada {r['f0']:.6f} ; muestreo {r['fn0']:.6f} ; diferencia {r['d0']:.1e}")
    print(f"Fraccion de eclipse beta = 50: cerrada {r['f50']:.6f} ; muestreo {r['fn50']:.6f} ; diferencia {r['d50']:.1e}")
    print("Cosenos medios por orbita (incluye el eclipse como cero):")
    print(f"  beta = 0 : fija al cenit {r['cfija0']:.4f} ; un eje {r['cuno0']:.4f} ; dos ejes {r['cdos0']:.4f}")
    print(f"  beta = 50: fija al cenit {r['cfija50']:.4f} ; un eje {r['cuno50']:.4f} ; dos ejes {r['cdos50']:.4f}")
    assert r["d0"] < 1e-5 and r["d50"] < 1e-5
    assert abs(r["cdos0"] - (1.0 - r["f0"])) < 1e-4
    assert r["f70"] == 0.0
    assert r["f0"] > r["f30"] > r["f50"] > 0.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
