#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C17: planificacion de observaciones, oclusion terrestre por orbita y seleccion de blancos con presupuesto de tiempo.

Datos: GM_Tierra = 3,986004e14 m3/s2 y R_ecuatorial = 6,3781e6 m de la Resolucion B3 de la UAI de 2015 (arXiv:1510.07674, consultada el 2026-11-09).
ILUSTRATIVOS (no son una programacion real): orbita circular a 600 km, blancos con inclinacion respecto del plano orbital beta de 0 a 60 grados, 12 blancos sinteticos
(semilla 20261109) con duracion 5-30 min y valor 1-10, presupuesto de 150 min.
Modelo: (1) fraccion de la orbita ocultada por la Tierra f(beta) = acos(cos rho / cos beta)/pi con sin rho = R/(R+h) si |beta| < rho, 0 en otro caso; (2) comprobacion independiente por
muestreo de la orbita y prueba rayo-esfera (rayo r + t s con t > 0 corta la esfera de radio R); (3) seleccion de blancos como mochila 0/1: heuristica voraz por valor/duracion (que aqui coincide con el optimo; el caso clasico de tres blancos muestra cuando falla) frente
al optimo exacto por programacion dinamica y por enumeracion de los 2^12 subconjuntos.
Supuestos: orbita sin precesion, Tierra esferica, blanco fijo en direccion, sin tiempos de maniobra ni zona de anomalia, sin limite por Sol o Luna. Validez: ilustrativa.
Tolerancia: fraccion analitica frente a muestreo, 2e-4; programacion dinamica igual a enumeracion exacta.
"""
from __future__ import annotations
import math, platform, random

GM = 3.986004e14
RE = 6.3781e6
A = RE + 600e3
RHO = math.asin(RE / A)
PER = 2 * math.pi * math.sqrt(A ** 3 / GM)


def frac_analitica(beta):
    b = math.radians(beta)
    if abs(b) >= RHO:
        return 0.0
    return math.acos(math.cos(RHO) / math.cos(b)) / math.pi


def frac_muestreo(beta, n=200000):
    b = math.radians(beta)
    s = (math.cos(b), 0.0, math.sin(b))
    ocu = 0
    for i in range(n):
        ph = 2 * math.pi * (i + 0.5) / n
        r = (A * math.cos(ph), A * math.sin(ph), 0.0)
        bb = r[0] * s[0] + r[1] * s[1] + r[2] * s[2]
        d2 = A * A - bb * bb
        if bb < 0 and d2 < RE * RE:
            ocu += 1
    return ocu / n


def voraz(items, cap):
    orden = sorted(range(len(items)), key=lambda i: -items[i][1] / items[i][0])
    t = v = 0
    for i in orden:
        if t + items[i][0] <= cap:
            t += items[i][0]
            v += items[i][1]
    return v, t


def dp(items, cap):
    best = [0] * (cap + 1)
    for d, v in items:
        for c in range(cap, d - 1, -1):
            best[c] = max(best[c], best[c - d] + v)
    return best[cap]


def enumerar(items, cap):
    n = len(items)
    mejor = 0
    for m in range(1 << n):
        t = v = 0
        for i in range(n):
            if m >> i & 1:
                t += items[i][0]
                v += items[i][1]
        if t <= cap and v > mejor:
            mejor = v
    return mejor


def calc():
    r = {"rho": math.degrees(RHO), "per_min": PER / 60}
    r["ocu"] = {}
    for beta in (0, 30, 60, 65, 70):
        a = frac_analitica(beta)
        m = frac_muestreo(beta)
        r["ocu"][beta] = (a, m, (1 - a) * PER / 60)
    rng = random.Random(20261109)
    items = [(rng.randint(5, 30), rng.randint(1, 10)) for _ in range(12)]
    r["items"] = items
    cap = 150
    r["voraz"] = voraz(items, cap)
    r["dp"] = dp(items, cap)
    r["enum"] = enumerar(items, cap)
    cl = [(10, 60), (20, 100), (30, 120)]
    r["clasico"] = (voraz(cl, 50)[0], dp(cl, 50), enumerar(cl, 50))
    r["suma_dur"] = sum(d for d, _ in items)
    r["suma_val"] = sum(v for _, v in items)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"semiangulo de la Tierra rho = {r['rho']:.4f} grados ; periodo = {r['per_min']:.3f} min")
    print(f"{'beta':>5} {'f analitica':>12} {'f muestreo':>11} {'visible [min/orbita]':>21}")
    for b, (a, m, vis) in r["ocu"].items():
        print(f"{b:5d} {a:12.5f} {m:11.5f} {vis:21.3f}")
        assert abs(a - m) < 2e-4
    print("blancos (duracion min, valor):", r["items"])
    print(f"duracion total = {r['suma_dur']} min ; valor total = {r['suma_val']}")
    print(f"presupuesto 150 min: voraz = {r['voraz'][0]} (usa {r['voraz'][1]} min) ; optimo por programacion dinamica = {r['dp']} ; optimo por enumeracion = {r['enum']}")
    print(f"caso clasico (10,60) (20,100) (30,120) con presupuesto 50: voraz = {r['clasico'][0]} ; optimo DP = {r['clasico'][1]} ; enumeracion = {r['clasico'][2]}")
    assert r["dp"] == r["enum"] and r["clasico"][1] == r["clasico"][2] == 220 and r["clasico"][0] == 160
    assert r["voraz"][0] <= r["dp"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
