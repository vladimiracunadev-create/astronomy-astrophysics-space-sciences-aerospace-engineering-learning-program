#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C03: reflexion, imagen virtual de un espejo plano, espejo girado y espejos en angulo.

Datos: sin constantes fisicas; todas las distancias y angulos son ILUSTRATIVOS.
Modelo: reflexion vectorial d' = d - 2 (d.n) n. (1) Imagen: se reflejan varios rayos de un punto objeto y se intersectan sus prolongaciones hacia atras;
(2) espejo girado un angulo a: el rayo reflejado gira 2a; (3) dos espejos en angulo phi: desviacion total 2 phi (rayo en el plano) y numero de imagenes
360/phi - 1 (formula de libro, solo tabulada, no simulada).
Supuestos: espejos planos perfectos, rayos en un plano. Validez: optica geometrica.
Tolerancia: posicion de la imagen 1e-9 m; angulos 1e-9 rad.
"""
from __future__ import annotations
import math, platform, sys


def refl(d, n):
    k = d[0] * n[0] + d[1] * n[1]
    return (d[0] - 2 * k * n[0], d[1] - 2 * k * n[1])


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # (1) espejo en x = 0 (normal +x), objeto en (0,5 ; 0,2) metros
    obj = (0.50, 0.20)
    n = (1.0, 0.0)
    puntos = []
    for ang in (-20, -5, 10, 25):
        a = math.radians(180 + ang)               # rayos hacia el espejo
        d = (math.cos(a), math.sin(a))
        t = -obj[0] / d[0]
        hit = (obj[0] + t * d[0], obj[1] + t * d[1])
        r = refl(d, n)
        puntos.append((hit, r))
    # interseccion de la prolongacion hacia atras de los rayos 0 y 1
    (h0, r0), (h1, r1) = puntos[0], puntos[1]
    det = r0[0] * (-r1[1]) - r0[1] * (-r1[0])
    s = ((h1[0] - h0[0]) * (-r1[1]) - (h1[1] - h0[1]) * (-r1[0])) / det
    im = (h0[0] + s * r0[0], h0[1] + s * r0[1])
    print(f"imagen por prolongacion de rayos = ({im[0]:.6f} ; {im[1]:.6f}) m ; esperada (-0,500000 ; 0,200000) m")
    assert abs(im[0] + 0.50) < 1e-9 and abs(im[1] - 0.20) < 1e-9
    for hit, r in puntos[2:]:
        # los otros rayos tambien pasan por la imagen virtual
        t = (im[0] - hit[0]) / r[0]
        assert abs(hit[1] + t * r[1] - im[1]) < 1e-9
    # (2) espejo girado
    d = (1.0, 0.0)
    print("espejo girado: angulo a -> giro del rayo reflejado")
    for a_deg in (1.0, 5.0, 12.5):
        a = math.radians(a_deg)
        n0 = (-1.0, 0.0)
        n1 = (-math.cos(a), -math.sin(a))
        g = math.atan2(*refl(d, n1)[::-1]) - math.atan2(*refl(d, n0)[::-1])
        g = (g + math.pi) % (2 * math.pi) - math.pi
        print(f"  a = {a_deg:5.2f} deg : giro = {math.degrees(g):7.3f} deg ; 2a = {2*a_deg:7.3f} deg")
        assert abs(abs(g) - 2 * a) < 1e-9
    # (3) dos espejos en angulo phi: desviacion total
    for phi_deg in (30.0, 60.0, 75.0):
        phi = math.radians(phi_deg)
        m1 = (0.0, 1.0)                                    # espejo 1: normal +y (pared y = 0)
        m2 = (-math.sin(phi), math.cos(phi))               # espejo 2 girado phi
        d0 = (math.cos(math.radians(-20)), math.sin(math.radians(-20)))
        d1 = refl(refl(d0, m1), m2)
        dev = math.atan2(d1[1], d1[0]) - math.atan2(d0[1], d0[0])
        dev = (dev + math.pi) % (2 * math.pi) - math.pi
        print(f"  espejos a {phi_deg:5.1f} deg : desviacion = {abs(math.degrees(dev)):7.3f} deg ; 2 phi mod 360 = {(2*phi_deg)%360:7.3f} deg")
        assert abs(abs(dev) - abs(((2 * phi) + math.pi) % (2 * math.pi) - math.pi)) < 1e-9
    # numero de imagenes en un caleidoscopio de dos espejos: 360/phi - 1
    print("imagenes de un objeto entre dos espejos en angulo phi")
    for phi_deg in (90, 60, 45, 30):
        cuenta = 360 // phi_deg - 1
        print(f"  phi = {phi_deg:3d} deg : imagenes = {cuenta}")
    assert 360 // 60 - 1 == 5
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
