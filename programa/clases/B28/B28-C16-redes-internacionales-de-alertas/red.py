#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C16: visibilidad de una fuente desde una red de sitios y disponibilidad combinada.

Datos: ninguna constante fisica. Contexto: GW170817 fue seguida por muchos observatorios tras la alerta (arXiv:1710.05833, resumen,
consultado 2026-11-09). Las coordenadas de los seis sitios, la altitud minima de 30 grados, la noche entre las 20 y las 4 h solares
locales y la disponibilidad de 0.7 por sitio son ILUSTRATIVAS (sinteticas); no corresponden a observatorios reales.
Modelo: altura de la fuente sen(a) = sen(phi) sen(delta) + cos(phi) cos(delta) cos(H), H = LST - ra; LST = GMST + longitud;
GMST = 280.46061837 + 360.98564736629 (JD - 2451545.0) grados. Un sitio puede observar si a > 30 grados y es de noche (hora solar media
local = UT + lon/15 entre 20 h y 4 h). Comprobaciones: fuente en el cenit (a = 90) y fraccion del cielo sobre 30 grados = (1 - sen 30)/2 = 0.25
(Monte Carlo con fuentes uniformes en la esfera, semilla fija). Probabilidad de que al menos un sitio pueda observar: Monte Carlo
frente a la formula ingenua de independencia 1 - Prod(1 - p_i).
Supuestos: sin Luna, sin nubes salvo la disponibilidad, noche fija. Validez: ilustrativa.
Tolerancia: 5 desviaciones binomiales en las probabilidades Monte Carlo.
"""
from __future__ import annotations
import math
import platform
import random
import sys

SITIOS = {"S1": (-30.0, -70.0), "S2": (20.0, -156.0), "S3": (28.0, -17.0), "S4": (-32.0, 21.0), "S5": (-31.0, 149.0), "S6": (37.0, 138.0)}
JD0 = 2461000.5          # fecha fija (JD a 0 h UT)


def gmst_deg(jd):
    return (280.46061837 + 360.98564736629 * (jd - 2451545.0)) % 360.0


def altura(lat, lon, ra, dec, ut_h):
    lst = (gmst_deg(JD0 + ut_h / 24.0) + lon) % 360.0
    h = math.radians(lst - ra)
    phi, d = math.radians(lat), math.radians(dec)
    s = math.sin(phi) * math.sin(d) + math.cos(phi) * math.cos(d) * math.cos(h)
    return math.degrees(math.asin(max(-1.0, min(1.0, s))))


def es_noche(lon, ut_h):
    h = (ut_h + lon / 15.0) % 24.0
    return h >= 20.0 or h < 4.0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # fuente en el cenit
    lat, lon, ut = 10.0, 30.0, 5.0
    lst = (gmst_deg(JD0 + ut / 24) + lon) % 360
    assert abs(altura(lat, lon, lst, lat, ut) - 90.0) < 1e-5, "cenit"
    print(f"comprobacion: fuente en el cenit -> altura = {altura(lat, lon, lst, lat, ut):.6f} grados")
    rng = random.Random(20261109)
    n = 40000
    # fraccion del cielo sobre 30 grados
    cnt = 0
    for _ in range(n):
        ra, dec = rng.uniform(0, 360), math.degrees(math.asin(rng.uniform(-1, 1)))
        if altura(40.0, 0.0, ra, dec, 3.0) > 30.0:
            cnt += 1
    p30, esp30 = cnt / n, (1 - math.sin(math.radians(30.0))) / 2
    sd = math.sqrt(esp30 * (1 - esp30) / n)
    print(f"fraccion de fuentes a mas de 30 grados desde un sitio: MC = {p30:.4f} ; analitico (1 - sen 30)/2 = {esp30:.4f} (+/- {sd:.4f})")
    assert abs(p30 - esp30) < 5 * sd
    # probabilidad por sitio y de la red en un instante aleatorio
    contador = {k: 0 for k in SITIOS}
    union = 0
    union_disp = 0
    disp = 0.7
    for _ in range(n):
        ut = rng.uniform(0, 24)
        ra, dec = rng.uniform(0, 360), math.degrees(math.asin(rng.uniform(-1, 1)))
        alguno = False
        alguno_d = False
        for k, (la, lo) in SITIOS.items():
            ok = es_noche(lo, ut) and altura(la, lo, ra, dec, ut) > 30.0
            if ok:
                contador[k] += 1
                alguno = True
                if rng.random() < disp:
                    alguno_d = True
        union += alguno
        union_disp += alguno_d
    ps = {k: v / n for k, v in contador.items()}
    esp1 = esp30 * (8 / 24)
    print(f"{'sitio':>5} {'lat':>6} {'lon':>7} {'P(observar)':>12}")
    for k, (la, lo) in SITIOS.items():
        print(f"{k:>5} {la:6.1f} {lo:7.1f} {ps[k]:12.4f}")
        sdk = math.sqrt(esp1 * (1 - esp1) / n)
    print(f"esperado por sitio: 0.25 x 8/24 = {esp1:.4f}")
    for k in SITIOS:
        assert abs(ps[k] - esp1) < 5 * math.sqrt(esp1 * (1 - esp1) / n) * 1.5, f"sitio {k}"
    pu = union / n
    ing = 1 - math.prod(1 - p for p in ps.values())
    print(f"red de 6 sitios: P(al menos uno observa) = {pu:.4f} ; independencia ingenua 1 - Prod(1 - p) = {ing:.4f}")
    print(f"con disponibilidad {disp} por sitio: P(al menos uno observa y esta disponible) = {union_disp / n:.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
