#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C18: umbral de notificacion internacional aplicado a un catalogo sintetico y delta-v exigido segun el tiempo de aviso.

Datos: catalogo SINTETICO de 20 000 objetos: diametros con ley de potencias N(>D) ~ D^-2.7 desde 5 m (exponente ILUSTRATIVO), probabilidades de impacto con log10 uniforme entre -8 y -0.5 y
tiempos de aviso uniformes entre 0.1 y 30 anios (semilla 20261109). El umbral de notificacion (probabilidad de impacto mayor que 1 % para un objeto de mas de 10 m) procede de la pagina de IAWN
consultada el 2026-11-09. Radio terrestre 6378.137 km recordado, no consultado. Capacidad de desviacion de 1, 5 y 20 mm/s: ILUSTRATIVA.
Modelo: regla de notificacion P > 0.01 y D > 10 m; fraccion esperada = P(D > 10) P(P > 0.01) = (10/5)^-2.7 x (1.5/7.5); tiempo minimo de aviso para desplazar 1.5 radios terrestres con un impulso
dv: T = b / (3 dv) (C17) y fraccion de objetos notificados con aviso suficiente = (30 - T)/(29.9) para T entre 0.1 y 30.
Supuestos: variables independientes, catalogo sintetico, sin la politica real de ninguna agencia. Validez: ilustrativa.
Tolerancia: fraccion notificada dentro de 3 errores binomiales de la esperada; fraccion con aviso suficiente dentro de 3 errores binomiales.
"""
import math, platform, random

def notifica(D, P):
    return P > 0.01 and D > 10.0

def calcular():
    rng = random.Random(20261109)
    N = 20000
    objs = []
    for _ in range(N):
        D = 5.0 * rng.random() ** (-1 / 2.7)
        P = 10 ** rng.uniform(-8, -0.5)
        T = rng.uniform(0.1, 30.0)
        objs.append((D, P, T))
    notif = [o for o in objs if notifica(o[0], o[1])]
    esperado = (10 / 5) ** -2.7 * (math.log10(0.316227766) - math.log10(0.01)) / 7.5 if False else (10 / 5) ** -2.7 * (-0.5 + 2.0) / 7.5
    f = len(notif) / N
    err = math.sqrt(esperado * (1 - esperado) / N)
    b = 1.5 * 6378.137e3
    filas = []
    for dv_mm in (1.0, 5.0, 20.0):
        Tmin = b / (3 * dv_mm * 1e-3) / (365.25 * 86400.0)
        suf = sum(1 for o in notif if o[2] >= Tmin) / max(1, len(notif))
        ana = max(0.0, min(1.0, (30.0 - Tmin) / 29.9))
        e = math.sqrt(ana * (1 - ana) / len(notif)) if 0 < ana < 1 else 0.0
        filas.append((dv_mm, Tmin, suf, ana, e))
    return {"N": N, "n_notif": len(notif), "f": f, "esperado": esperado, "err": err, "filas": filas}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Catalogo sintetico de %d objetos ; regla de notificacion: P > 1 %% y D > 10 m" % r["N"])
    print("Notificados: %d (fraccion %.5f) ; esperado %.5f +- %.5f ; diferencia = %+.2f errores" % (r["n_notif"], r["f"], r["esperado"], r["err"], (r["f"] - r["esperado"]) / r["err"]))
    print("Objetos notificados con aviso suficiente para desplazar 1.5 radios terrestres:")
    for dv, T, suf, ana, e in r["filas"]:
        print("  dv = %4.1f mm/s -> T minimo = %6.2f anios ; fraccion con aviso suficiente = %.4f (analitica %.4f)" % (dv, T, suf, ana))
    assert abs(r["f"] - r["esperado"]) < 3 * r["err"]
    for dv, T, suf, ana, e in r["filas"]:
        assert abs(suf - ana) <= 3 * e + 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
