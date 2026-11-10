#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C19: comunicacion de una probabilidad de impacto en frecuencias naturales y comportamiento de la probabilidad al llegar nuevas observaciones.

Datos: SINTETICOS. La posicion transversal x del objeto en el plano B, en unidades del radio efectivo del blanco (impacto si |x| < 1), sigue a priori N(4, 3^2). Se simulan 200 000 objetos
(semilla 20261109): cada uno recibe dos observaciones sucesivas con errores de 2 y 0.3 unidades. El ejercicio de la Conferencia de Defensa Planetaria 2023 (CNEOS, consultado el 2026-11-09) describe un
asteroide FICTICIO cuya probabilidad de impacto crecio de ~1 en 10 000 a ~1 % y cuyo Torino era 1; aqui solo se usa esa trayectoria cualitativa, no sus cifras orbitales.
Modelo: actualizacion gaussiana de la posicion (media y varianza posteriores) y probabilidad P = Phi((1-m)/s) - Phi((-1-m)/s). Propiedad: la probabilidad es una martingala, de modo que la media de
las probabilidades posteriores es igual a la probabilidad inicial y la fraccion de impactos es igual a la probabilidad inicial.
Supuestos: gaussiana unidimensional, sin ojos de cerradura, errores independientes. Validez: ilustrativa.
Tolerancia: media de P1, media de P2 y fraccion de impactos iguales a P0 dentro de 3 errores tipicos.
"""
import math, platform, random

def Phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

def prob(m, s):
    return Phi((1 - m) / s) - Phi((-1 - m) / s)

def actualiza(m, v, y, s):
    vn = 1.0 / (1.0 / v + 1.0 / (s * s))
    return vn * (m / v + y / (s * s)), vn

def frecuencia(p):
    return "1 de cada %d" % round(1 / p) if p > 0 else "ninguno"

def calcular():
    mu0, s0 = 4.0, 3.0
    P0 = prob(mu0, s0)
    rng = random.Random(20261109)
    N = 200000
    P1s, P2s, imp = [], [], 0
    sube_baja = 0
    for _ in range(N):
        x = rng.gauss(mu0, s0)
        imp += abs(x) < 1
        m, v = mu0, s0 * s0
        y1 = x + rng.gauss(0, 2.0)
        m, v = actualiza(m, v, y1, 2.0)
        p1 = prob(m, math.sqrt(v))
        y2 = x + rng.gauss(0, 0.3)
        m, v = actualiza(m, v, y2, 0.3)
        p2 = prob(m, math.sqrt(v))
        P1s.append(p1); P2s.append(p2)
        if p1 > P0 and p2 < 0.01 * P0:
            sube_baja += 1
    def media_err(xs):
        mm = sum(xs) / len(xs)
        sd = math.sqrt(sum((x - mm) ** 2 for x in xs) / (len(xs) - 1))
        return mm, sd / math.sqrt(len(xs))
    m1, e1 = media_err(P1s); m2, e2 = media_err(P2s)
    fi = imp / N; efi = math.sqrt(P0 * (1 - P0) / N)
    return {"P0": P0, "m1": m1, "e1": e1, "m2": m2, "e2": e2, "fi": fi, "efi": efi, "N": N,
            "baja1": sum(1 for p in P1s if p < P0) / N, "baja2": sum(1 for p in P2s if p < 0.01 * P0) / N,
            "p2_alto": sum(1 for p in P2s if p > 0.5) / N, "sube_baja": sube_baja / N, "freq": frecuencia(P0)}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Probabilidad inicial P0 = %.5f ; en frecuencias naturales: %s" % (r["P0"], r["freq"]))
    print("Con %d objetos simulados:" % r["N"])
    print("  media de P tras la 1a observacion = %.5f +- %.5f (P0 = %.5f)" % (r["m1"], r["e1"], r["P0"]))
    print("  media de P tras la 2a observacion = %.5f +- %.5f" % (r["m2"], r["e2"]))
    print("  fraccion de impactos reales = %.5f +- %.5f" % (r["fi"], r["efi"]))
    print("  P1 < P0 en %.1f %% de los casos ; P2 < 0.01 P0 en %.1f %% ; P2 > 0.5 en %.1f %%" % (100 * r["baja1"], 100 * r["baja2"], 100 * r["p2_alto"]))
    print("  casos en que P sube tras la 1a observacion y termina por debajo de 0.01 P0: %.1f %%" % (100 * r["sube_baja"]))
    assert abs(r["m1"] - r["P0"]) < 3 * r["e1"] + 3 * r["efi"]
    assert abs(r["m2"] - r["P0"]) < 3 * r["e2"] + 3 * r["efi"]
    assert abs(r["fi"] - r["P0"]) < 3 * r["efi"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
