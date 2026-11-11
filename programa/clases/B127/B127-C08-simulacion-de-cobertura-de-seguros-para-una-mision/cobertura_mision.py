#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B127-C08: cuatro estrategias de cobertura para una MISION SINTETICA (lanzamiento + 5 anios en orbita + tercero).

CONTENIDO EDUCATIVO: no es una recomendacion ni asesoria financiera, legal o de seguros; ninguna cifra es una cotizacion.
Consultado (2026-11-11): 14 CFR parte 440 (via resumen): MPL por probabilidad 1 en 10 millones, seguro de terceros hasta el menor
de 500 MUSD o el maximo del mercado, y pago publico adicional hasta 1500 MUSD. Convenio de 1972 Arts. II-III. Gallagher Q1 2026:
volatilidad del mercado (loss ratio 2025 de ~15 % a ~75 % por un siniestro). Ningun parametro sale de esas fuentes.
ILUSTRATIVOS (reutiliza C01-C03): resultados de lanzamiento, Weibull (beta 0.7, eta 120), depreciacion, severidad de tercero lognormal,
probabilidad de evento de tercero por mision, recargos.
Estrategias: A sin seguro; B lanzamiento; C lanzamiento + orbita (deducible 5); D lanzamiento + orbita + tercero (tope 500).
Prima = pago esperado analitico * (1 + recargo). Costo del operador = primas + perdidas retenidas.
Unidades: MUSD ficticios. Tolerancias: Monte Carlo (100000 misiones, semilla 127): pago esperado de lanzamiento y orbita frente al analitico < 3 %; el de tercero
(cola pesada, pocos eventos) < 12 %.
"""
from __future__ import annotations
import math, platform, random
from statistics import NormalDist

V = 200.0
LANZ = [(0.940, 0.0), (0.025, 0.25), (0.015, 0.60), (0.020, 1.0)]
BETA, ETA, DEP, ANIOS = 0.7, 120.0, 0.08, 5
D_ORB = 5.0
P_TERC, MU, S, TOPE_T = 0.02, 2.0, 1.6, 500.0
REC_L, REC_O, REC_T = 0.35, 0.30, 0.50
N = NormalDist()


def Sv(t):
    return math.exp(-((t / ETA) ** BETA))


def lev(u):
    z = (math.log(u) - MU) / S
    return math.exp(MU + S * S / 2) * N.cdf(z - S) + u * (1 - N.cdf(z))


def vk(k):
    return V * max(0.0, 1 - DEP * k)


def pago_lanz_esp():
    return sum(p * f for p, f in LANZ) * V


def pago_orb_esp():
    # solo si el lanzamiento fue exitoso (prob 0.94); fallo en el anio k con valor vk(k) y deducible
    exito = LANZ[0][0]
    tot = 0.0
    for k in range(ANIOS):
        q = Sv(k) - Sv(k + 1)  # probabilidad incondicional de fallar en [k, k+1)
        tot += q * max(vk(k) - D_ORB, 0.0)
    return exito * tot


def pago_terc_esp():
    return P_TERC * lev(TOPE_T)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Mision SINTETICA; consultados solo el contexto de 14 CFR 440 (via resumen), el Convenio de 1972 y Gallagher Q1 2026.")
    pl, po, pt = pago_lanz_esp(), pago_orb_esp(), pago_terc_esp()
    prim = {"L": pl * (1 + REC_L), "O": po * (1 + REC_O), "T": pt * (1 + REC_T)}
    print(f"Pagos esperados analiticos: lanzamiento = {pl:.3f} ; orbita = {po:.3f} ; tercero = {pt:.4f} MUSD")
    print(f"Primas: lanzamiento = {prim['L']:.3f} ; orbita = {prim['O']:.3f} ; tercero = {prim['T']:.4f} MUSD")
    rng = random.Random(127)
    n = 100000
    costos = {k: [] for k in "ABCD"}
    sp = {"L": 0.0, "O": 0.0, "T": 0.0}
    for _ in range(n):
        u, f = rng.random(), 0.0
        c = 0.0
        for p, ff in LANZ:
            c += p
            if u < c:
                f = ff
                break
        perd_l = f * V
        perd_o = 0.0
        if f == 0.0:
            t = ETA * (-math.log(1 - rng.random())) ** (1 / BETA)
            if t < ANIOS:
                perd_o = vk(int(t))
        perd_t = rng.lognormvariate(MU, S) if rng.random() < P_TERC else 0.0
        pag_o = max(perd_o - D_ORB, 0.0)
        pag_t = min(perd_t, TOPE_T)
        sp["L"] += perd_l
        sp["O"] += pag_o
        sp["T"] += pag_t
        costos["A"].append(perd_l + perd_o + perd_t)
        costos["B"].append(prim["L"] + perd_o + perd_t)
        costos["C"].append(prim["L"] + prim["O"] + min(perd_o, D_ORB) + perd_t)
        costos["D"].append(prim["L"] + prim["O"] + prim["T"] + min(perd_o, D_ORB) + max(perd_t - TOPE_T, 0.0))
    print("Pago esperado por cobertura: analitico frente a Monte Carlo")
    errmax = 0.0
    for key, an in (("L", pl), ("O", po), ("T", pt)):
        e = abs(sp[key] / n - an) / an
        errmax = max(errmax, e if key != "T" else e / 4)
        print(f"  {key}: analitico = {an:.4f} ; MC = {sp[key] / n:.4f} ; error relativo = {e:.2%}")
    print("Estrategia                         costo medio  desv. est.  cuantil 99 %  P(costo>60)")
    nombres = {"A": "A sin seguro", "B": "B lanzamiento", "C": "C lanzamiento + orbita", "D": "D lanz. + orbita + tercero"}
    for key in "ABCD":
        v = sorted(costos[key])
        m = sum(v) / n
        sd = math.sqrt(sum((x - m) ** 2 for x in v) / (n - 1))
        print(f"  {nombres[key]:30s} {m:9.3f} {sd:11.3f} {v[int(0.99 * n)]:12.3f} {sum(1 for x in v if x > 60) / n:11.4f}")
    assert errmax < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
