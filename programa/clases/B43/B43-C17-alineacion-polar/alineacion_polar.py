#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C17: alineacion polar: deriva en declinacion causada por un error de alineacion, con rotaciones exactas.

Datos: ILUSTRATIVOS (errores del eje de la montura de 10' en acimut y 6' en altura; exposicion de 300 s; deriva medida de 5" en 5 min para la parte inversa). Velocidad angular de la Tierra omega = 2 pi/86164,0905 s (dia sideral de C12).
No hay mediciones reales.
Modelo: marco ecuatorial (X hacia el ecuador en el meridiano, Y hacia el este, Z al polo). Una estrella s gira alrededor de Z; la montura gira alrededor de p = (Z + e_x X + e_y Y)/norma. Se aplican rotaciones de Rodrigues exactas y se mide la
separacion en la direccion de declinacion tras t. Prediccion lineal: ds_montura/dt - ds_estrella/dt = omega (p - Z) x s, de modo que (con el signo de la simulacion) en el meridiano dDec/dt = +omega e_y (error de acimut) y a seis horas del meridiano dDec/dt = -+omega e_x (error de altura); el caso de primer orden nulo conserva un residuo de segundo orden menor que 1e-3 "/s.
Supuestos: refraccion, flexion y error periodico ignorados; angulos pequenos. Validez: e << 1.
Tolerancia: simulacion exacta frente a la prediccion lineal, 1 % relativo (el termino cuadratico es del orden de e).
"""
from __future__ import annotations
import math, platform

OM = 2 * math.pi / 86164.0905
ARC = math.pi / 648000.0

def norm(v):
    n = math.sqrt(sum(x * x for x in v)); return tuple(x / n for x in v)

def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def rodrigues(v, k, ang):
    c = math.cos(ang); s = math.sin(ang)
    kv = cross(k, v); kd = dot(k, v)
    return tuple(v[i] * c + kv[i] * s + k[i] * kd * (1 - c) for i in range(3))

def deriva(H, dec, ex, ey, t):
    s0 = (math.cos(dec) * math.cos(H), -math.cos(dec) * math.sin(H), math.sin(dec))
    Z = (0.0, 0.0, 1.0)
    p = norm((ex, ey, 1.0))
    # la estrella gira con angulo -OM t alrededor de Z visto desde el norte (H crece hacia el oeste); la montura sigue con el mismo sentido alrededor de p
    est = rodrigues(s0, Z, -OM * t)
    tel = rodrigues(s0, p, -OM * t)
    # direccion de declinacion en la posicion de la estrella
    nd = (-math.sin(dec) * math.cos(H), math.sin(dec) * math.sin(H), math.cos(dec))
    d = tuple(tel[i] - est[i] for i in range(3))
    return dot(d, nd) / t

def lineal(H, dec, ex, ey):
    s0 = (math.cos(dec) * math.cos(H), -math.cos(dec) * math.sin(H), math.sin(dec))
    nd = (-math.sin(dec) * math.cos(H), math.sin(dec) * math.sin(H), math.cos(dec))
    e = (ex, ey, 0.0)
    return -OM * dot(cross(e, s0), nd)

def calc():
    r = {}
    ex = 6 * 60 * ARC; ey = 10 * 60 * ARC
    casos = [("meridiano, dec 0, error de acimut", 0.0, 0.0, 0.0, ey), ("meridiano, dec 60, error de acimut", 0.0, math.radians(60), 0.0, ey),
             ("6 h al este, dec 0, error de altura", math.radians(-90), 0.0, ex, 0.0), ("6 h al oeste, dec 0, error de altura", math.radians(90), 0.0, ex, 0.0),
             ("meridiano, dec 0, error de altura", 0.0, 0.0, ex, 0.0)]
    filas = []
    for n, H, d, a, b in casos:
        num = deriva(H, d, a, b, 300.0) / ARC
        lin = lineal(H, d, a, b) / ARC
        filas.append((n, num, lin))
    r["filas"] = filas
    r["omega_e_acimut"] = OM * ey / ARC
    # inverso
    deriva_medida = 5.0 / 300.0  # "/s
    r["e_estimado_arcmin"] = deriva_medida / OM / 60
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print("caso | deriva simulada (\"/s) | prediccion lineal (\"/s)")
    for n, a, b in r["filas"]:
        print(f"{n} | {a:.6f} | {b:.6f}")
    for k in ("omega_e_acimut", "e_estimado_arcmin"):
        print(f"{k} = {r[k]:.6g}")
    for n, a, b in r["filas"]:
        if abs(b) > 1e-9:
            assert abs(a / b - 1) < 0.01, n
        else:
            assert abs(a) < 1e-3, n
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
