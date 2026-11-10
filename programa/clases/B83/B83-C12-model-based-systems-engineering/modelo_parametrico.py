#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C12: modelo parametrico de sistema con unidades, una sola fuente de verdad y propagacion de cambios.

Datos: SINTETICOS (parametros de la mision de ejemplo ESTRELLA-S; los valores base siguen a B83-C01, C09 y C11). g0 = 9.80665 m/s2
(NASA/NSSDC, 2026-11-10). Modelo: cada parametro derivado es una ecuacion sobre otros parametros; el motor evalua en orden topologico,
comprueba las dimensiones fisicas con una clase minima de cantidades (m, kg, s, bit) y calcula el conjunto de parametros afectados por
un cambio. Segunda via: iteracion de punto fijo en orden arbitrario hasta que nada cambie. Tolerancia: 1e-9 relativo.
No es SysML: es un ejemplo minimo de la idea de modelo como fuente unica de verdad.
"""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

DIMS = ("m", "kg", "s", "bit")


class Q:
    def __init__(self, v, d=(0, 0, 0, 0)): self.v, self.d = float(v), tuple(d)
    def __mul__(s, o):
        o = o if isinstance(o, Q) else Q(o); return Q(s.v * o.v, [a + b for a, b in zip(s.d, o.d)])
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = o if isinstance(o, Q) else Q(o); return Q(s.v / o.v, [a - b for a, b in zip(s.d, o.d)])
    def __rtruediv__(s, o): return Q(o) / s
    def __pow__(s, p): return Q(s.v ** p, [a * p for a in s.d])
    def __add__(s, o):
        assert s.d == o.d, f"suma de dimensiones distintas {s.d} {o.d}"; return Q(s.v + o.v, s.d)
    def __sub__(s, o):
        assert s.d == o.d, f"resta de dimensiones distintas {s.d} {o.d}"; return Q(s.v - o.v, s.d)


def qexp(x):
    assert x.d == (0, 0, 0, 0), "exp de una magnitud con dimensiones"; return Q(math.exp(x.v))


M, KG, S, BIT = Q(1, (1, 0, 0, 0)), Q(1, (0, 1, 0, 0)), Q(1, (0, 0, 1, 0)), Q(1, (0, 0, 0, 1))
ADIM = (0, 0, 0, 0)

ENTRADAS = {
    "gsd": 5.0 * M, "lam": 550e-9 * M, "h": 550e3 * M, "gsd0": 5.0 * M, "v_suelo": 6983.0 * M / S, "franja": 30e3 * M,
    "bits": 12.0 * BIT, "bandas": Q(4), "t_toma": 40.0 * S, "orbitas": Q(15.055), "compresion": Q(3.0),
    "m_resto": 45.71 * KG, "m_cam0": 21.6 * KG, "dv": 150.0 * M / S, "isp": 220.0 * S, "g0": 9.80665 * M / S / S,
    "m_limite": 80.0 * KG, "cap_dia": 115.76e9 * BIT, "p_toma0": 110.0 * KG * M ** 2 / S ** 3, "p_pico_max": 150.0 * KG * M ** 2 / S ** 3,
}
# parametro: (funcion, dependencias, dimensiones esperadas)
ECUACIONES = {
    "D": (lambda p: 1.22 * p["lam"] * p["h"] / p["gsd"], ["lam", "h", "gsd"], (1, 0, 0, 0)),
    "D0": (lambda p: 1.22 * p["lam"] * p["h"] / p["gsd0"], ["lam", "h", "gsd0"], (1, 0, 0, 0)),
    "m_cam": (lambda p: p["m_cam0"] * (p["D"] / p["D0"]) ** 2, ["m_cam0", "D", "D0"], (0, 1, 0, 0)),
    "pix": (lambda p: p["franja"] / p["gsd"], ["franja", "gsd"], ADIM),
    "lineas": (lambda p: p["v_suelo"] / p["gsd"], ["v_suelo", "gsd"], (0, 0, -1, 0)),
    "tasa": (lambda p: p["pix"] * p["lineas"] * p["bits"] * p["bandas"], ["pix", "lineas", "bits", "bandas"], (0, 0, -1, 1)),
    "tasa0": (lambda p: (p["franja"] / p["gsd0"]) * (p["v_suelo"] / p["gsd0"]) * p["bits"] * p["bandas"], ["franja", "gsd0", "v_suelo", "bits", "bandas"], (0, 0, -1, 1)),
    "p_toma": (lambda p: p["p_toma0"] * (p["tasa"] / p["tasa0"]), ["p_toma0", "tasa", "tasa0"], (2, 1, -3, 0)),
    "prod_dia": (lambda p: p["tasa"] * p["t_toma"] * p["orbitas"] / p["compresion"], ["tasa", "t_toma", "orbitas", "compresion"], (0, 0, 0, 1)),
    "m_seco": (lambda p: p["m_resto"] + p["m_cam"], ["m_resto", "m_cam"], (0, 1, 0, 0)),
    "m_prop": (lambda p: p["m_seco"] * (qexp(p["dv"] / (p["g0"] * p["isp"])) - Q(1)), ["m_seco", "dv", "g0", "isp"], (0, 1, 0, 0)),
    "m_total": (lambda p: p["m_seco"] + p["m_prop"], ["m_seco", "m_prop"], (0, 1, 0, 0)),
    "margen_masa": (lambda p: (p["m_limite"] - p["m_total"]) / p["m_limite"], ["m_limite", "m_total"], ADIM),
    "margen_datos": (lambda p: (p["cap_dia"] - p["prod_dia"]) / p["prod_dia"], ["cap_dia", "prod_dia"], ADIM),
    "margen_pico": (lambda p: (p["p_pico_max"] - p["p_toma"]) / p["p_pico_max"], ["p_pico_max", "p_toma"], ADIM),
}


def orden():
    hechos, res = set(ENTRADAS), []
    pend = dict(ECUACIONES)
    while pend:
        lis = [k for k, (f, deps, d) in pend.items() if all(x in hechos for x in deps)]
        assert lis, "dependencia circular"
        for k in sorted(lis): res.append(k); hechos.add(k); pend.pop(k)
    return res


def evaluar(entradas):
    p = dict(entradas)
    for k in orden():
        f, deps, d = ECUACIONES[k]
        p[k] = f(p)
        assert p[k].d == d, f"{k}: dimensiones {p[k].d} distintas de las declaradas {d}"
    return p


def punto_fijo(entradas):
    p = dict(entradas)
    for k in ECUACIONES: p[k] = Q(0.0, ECUACIONES[k][2])
    for _ in range(100):
        previo = {k: p[k].v for k in ECUACIONES}
        for k in reversed(list(ECUACIONES)):   # orden inverso a proposito
            deps = ECUACIONES[k][1]
            if all(x in p for x in deps):
                try: p[k] = ECUACIONES[k][0](p)
                except ZeroDivisionError: pass
        if all(abs(p[k].v - previo[k]) <= 1e-12 * max(1.0, abs(previo[k])) for k in ECUACIONES): break
    return p


def afectados(raiz):
    afect, cambio = set(), True
    while cambio:
        cambio = False
        for k, (f, deps, d) in ECUACIONES.items():
            if k not in afect and (raiz in deps or afect & set(deps)):
                afect.add(k); cambio = True
    return afect


def calcular():
    V = {}
    for g in (5.0, 4.0, 3.0):
        e = dict(ENTRADAS); e["gsd"] = g * M
        p = evaluar(e)
        t = int(g)
        V[f"D_{t}"] = p["D"].v * 100; V[f"mcam_{t}"] = p["m_cam"].v; V[f"mtot_{t}"] = p["m_total"].v
        V[f"mm_{t}"] = p["margen_masa"].v * 100; V[f"prod_{t}"] = p["prod_dia"].v / 1e9; V[f"md_{t}"] = p["margen_datos"].v * 100
        V[f"ptoma_{t}"] = p["p_toma"].v; V[f"mp_{t}"] = p["margen_pico"].v * 100
        V[f"cumple_{t}"] = int(p["margen_masa"].v >= 0 and p["margen_datos"].v >= 0 and p["margen_pico"].v >= 0)
    e = dict(ENTRADAS); e["gsd"] = 4.0 * M
    a = evaluar(e); b = punto_fijo(e)
    V["dif_vias"] = max(abs(a[k].v - b[k].v) / max(1.0, abs(a[k].v)) for k in ECUACIONES)
    af = afectados("gsd")
    V["n_param"] = len(ENTRADAS) + len(ECUACIONES); V["n_ent"] = len(ENTRADAS); V["n_ec"] = len(ECUACIONES)
    V["n_afect"] = len(af); V["afect"] = sorted(af); V["orden"] = orden()
    V["n_afect_mlimite"] = len(afectados("m_limite")); V["n_afect_compresion"] = len(afectados("compresion"))
    return V


def main():
    V = calcular()
    print(cabecera())
    print(f"Datos SINTETICOS: {V['n_ent']} entradas y {V['n_ec']} ecuaciones con unidades (m, kg, s, bit); g0 = 9.80665 m/s2 (NASA/NSSDC)")
    print("Orden de evaluacion: " + " -> ".join(V["orden"]))
    print(f"{'GSD':>4s} {'D [cm]':>8s} {'m_cam':>7s} {'m_total':>8s} {'marg.masa':>10s} {'prod.[Gbit]':>12s} {'marg.datos':>11s} {'P_toma[W]':>10s} {'marg.pico':>10s}  veredicto")
    for t in (5, 4, 3):
        print(f"{t:4d} {V[f'D_{t}']:8.2f} {V[f'mcam_{t}']:7.2f} {V[f'mtot_{t}']:8.2f} {V[f'mm_{t}']:9.2f}% {V[f'prod_{t}']:12.2f} {V[f'md_{t}']:10.2f}% {V[f'ptoma_{t}']:10.2f} {V[f'mp_{t}']:9.2f}%  {'CUMPLE' if V[f'cumple_{t}'] else 'NO CUMPLE'}")
    print(f"Parametros afectados por cambiar gsd: {V['n_afect']} de {V['n_ec']} derivados -> {', '.join(V['afect'])}")
    print(f"Afectados por m_limite: {V['n_afect_mlimite']} ; por compresion: {V['n_afect_compresion']}")
    print(f"Diferencia maxima entre orden topologico y punto fijo = {V['dif_vias']:.2e}")
    comprobar(V["dif_vias"] < 1e-9, "orden topologico y punto fijo coinciden")
    comprobar(V["cumple_5"] == 1 and V["cumple_4"] == 0, "el caso base cumple y GSD 4 m rompe algun presupuesto")
    comprobar(abs(V["D_5"] - 7.3873) < 1e-3 or abs(V["D_5"] - 7.38) < 0.01, "apertura base coherente con C01")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
