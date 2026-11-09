#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C18: colimacion instrumental: tolerancia de inclinacion del primario por coma y desviacion de un plano secundario inclinado.

Datos: ILUSTRATIVOS (reflector newtoniano D = 200 mm, f/5, distancia focal 1000 mm; lambda = 550 nm; plano secundario a 250 mm del plano focal). Sin datos de instrumentos reales.
Modelo: una inclinacion eps del paraboloide equivale a un angulo de campo eps respecto de su eje; el coma (desplazamiento del centroide de los rayos marginales respecto del rayo principal) sigue 3 eps/(16 N^2) F.
Criterio: coma igual al radio de Airy 1,22 lambda N; de ahi eps_max = 1,22 lambda N 16 N^2/(3 F). Un plano inclinado delta desvia el haz 2 delta.
Verificacion independiente: trazado exacto de rayos meridionales por un paraboloide (interseccion por Newton, reflexion vectorial) frente a la formula; reflexion vectorial en un plano inclinado frente a 2 delta.
Supuestos: geometria, sin difraccion, meridional. Validez: eps pequeno.
Tolerancia: coma trazada frente a formula, 2 % relativo; desviacion del plano, 1e-9 rad.
"""
from __future__ import annotations
import math, platform

D = 200.0; F = 1000.0; N = F / D; LAM = 550e-6  # mm

def sag(y):
    return y * y / (2 * 2 * F)

def hit(p, d):
    t = 0.0
    for _ in range(60):
        y = p[0] + t * d[0]; z = p[1] + t * d[1]
        f = z - sag(y)
        df = d[1] - y / (2 * F) * d[0]
        t -= f / df
    return (p[0] + t * d[0], p[1] + t * d[1])

def reflect(d, y):
    n = (-y / (2 * F), 1.0); nn = math.hypot(*n); n = (n[0] / nn, n[1] / nn)
    k = d[0] * n[0] + d[1] * n[1]
    return (d[0] - 2 * k * n[0], d[1] - 2 * k * n[1])

def y_foco(h, theta):
    d0 = (math.sin(theta), -math.cos(theta))
    p0 = (h - d0[0] / d0[1] * 3000.0, 3000.0)
    p = hit(p0, d0)
    d1 = reflect(d0, p[0])
    t = (F - p[1]) / d1[1]
    return p[0] + t * d1[0]

def coma(theta, h=D / 2):
    return ((y_foco(h, theta) + y_foco(-h, theta)) / 2 - y_foco(0.0, theta))

def plano(delta):
    d = (1.0, 0.0)
    ang = math.radians(45) + delta
    n = (math.cos(ang), math.sin(ang))
    k = d[0] * n[0] + d[1] * n[1]
    r = (d[0] - 2 * k * n[0], d[1] - 2 * k * n[1])
    return math.atan2(r[1], r[0])

def calc():
    r = {}
    airy = 1.22 * LAM * N
    r["airy_um"] = airy * 1e3
    r["eps_max_rad"] = airy * 16 * N ** 2 / (3 * F)
    r["eps_max_arcmin"] = math.degrees(r["eps_max_rad"]) * 60
    r["coma_en_eps_max_um"] = coma(r["eps_max_rad"]) * 1e3
    filas = []
    for arcmin in (0.5, 1.0, 2.0, 4.0):
        th = math.radians(arcmin / 60)
        filas.append((arcmin, coma(th) * 1e3, 3 * th / (16 * N ** 2) * F * 1e3))
    r["filas"] = filas
    d0 = plano(0.0)
    delta = math.radians(0.5)
    r["desv_plano_rad"] = abs(plano(delta) - d0); r["desv_esperada"] = 2 * delta
    r["desplazamiento_foco_mm"] = 2 * delta * 250.0
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k in ("airy_um", "eps_max_rad", "eps_max_arcmin", "coma_en_eps_max_um", "desv_plano_rad", "desv_esperada", "desplazamiento_foco_mm"):
        print(f"{k} = {r[k]:.6g}")
    print("eps (arcmin) | coma trazada (um) | formula (um)")
    for a, b, c in r["filas"]:
        print(f"{a} | {b:.4f} | {c:.4f}")
    for a, b, c in r["filas"]:
        assert abs(b / c - 1) < 0.02
    assert abs(r["coma_en_eps_max_um"] / r["airy_um"] - 1) < 0.02
    assert abs(r["desv_plano_rad"] - r["desv_esperada"]) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
