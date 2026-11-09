#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C13: aberracion esferica de un espejo esferico frente a un paraboloide y coma fuera de eje.

Datos: sin constantes del NIST. D = 200 mm, F = 1000 mm (f/5), campo de 10 minutos de arco y lambda = 550 nm son ILUSTRATIVOS.
Modelo: espejo conico (c = 1/R, k = 0 esfera, k = -1 paraboloide); los rayos se trazan exactamente (interseccion con la conica + reflexion). (1) Aberracion
esferica: la diferencia de camino optico (OPD) del espejo esferico frente al paraboloide en la zona h se compara con h^4/(4 R^3) (tercer orden) y se halla la
relacion focal minima para que la esfera cumpla el criterio de Rayleigh con el mejor foco (P-V = W040/4 <= lambda/4). (2) Coma: abanico tangencial de rayos
inclinados un angulo theta sobre el paraboloide; la longitud de la coma tangencial en el plano focal paraxial se compara con 3 theta F /(16 N^2).
Supuestos: rayos meridionales, reflexion perfecta, sin difraccion. Validez: tercer orden para campos pequeños.
Tolerancia: OPD frente a h^4/(4R^3) 2 %; coma numerica frente a la formula de libro 5 %.
"""
from __future__ import annotations
import math, platform, sys


def sag(c, k, x):
    return c * x * x / (1 + math.sqrt(1 - (1 + k) * c * c * x * x))


def traza(c, k, x0, th, zplano):
    """Rayo que viaja hacia -z con inclinacion th (rad) respecto al eje, entra en z = zplano+... Devuelve x en el plano z = zplano tras reflejar."""
    d = (math.sin(th), -math.cos(th))
    p = (x0, 3000.0)
    # F(x,z) = c (x^2 + (1+k) z^2) - 2 z = 0
    A = c * (d[0] ** 2 + (1 + k) * d[1] ** 2)
    B = 2 * c * (p[0] * d[0] + (1 + k) * p[1] * d[1]) - 2 * d[1]
    C = c * (p[0] ** 2 + (1 + k) * p[1] ** 2) - 2 * p[1]
    if abs(A) < 1e-18:
        ts = [-C / B]
    else:
        disc = math.sqrt(B * B - 4 * A * C)
        ts = [(-B - disc) / (2 * A), (-B + disc) / (2 * A)]
    cand = []
    for t in ts:
        if t > 0:
            cand.append((p[1] + t * d[1], t))
    z, t = min(cand)
    x = p[0] + t * d[0]
    n = (2 * c * x, 2 * c * (1 + k) * z - 2)
    nn = math.hypot(*n)
    n = (n[0] / nn, n[1] / nn)
    kdn = d[0] * n[0] + d[1] * n[1]
    r = (d[0] - 2 * kdn * n[0], d[1] - 2 * kdn * n[1])
    s = (zplano - z) / r[1]
    return x + s * r[0]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    D, F, lam = 200.0, 1000.0, 550e-6          # lambda en mm
    R = 2 * F
    c = 1 / R
    print(f"espejo f/{F/D:.0f}: R = {R:.0f} mm, lambda = {lam*1e6:.0f} nm")
    print(f"{'h [mm]':>7} {'OPD esfera-parab. [nm]':>24} {'h^4/(4R^3) [nm]':>17} {'razon':>7}")
    for h in (25.0, 50.0, 75.0, 100.0):
        dz = sag(c, 0.0, h) - sag(c, -1.0, h)
        opd = 2 * dz
        terc = h ** 4 / (4 * R ** 3)
        print(f"{h:7.0f} {opd*1e6:24.2f} {terc*1e6:17.2f} {opd/terc:7.4f}")
        assert abs(opd / terc - 1) < 0.02
    W040 = (D / 2) ** 4 / (4 * R ** 3)
    print(f"W040 en el borde = {W040*1e6:.1f} nm = {W040/lam:.3f} ondas ; con mejor foco P-V = W040/4 = {W040/4/lam:.3f} ondas")
    # relacion focal minima para la esfera con Rayleigh (P-V <= lambda/4 con mejor foco, W040 <= lambda)
    lo, hi = 1.0, 40.0
    for _ in range(80):
        N = 0.5 * (lo + hi)
        Fm = N * D
        w = (D / 2) ** 4 / (4 * (2 * Fm) ** 3)
        if w <= lam:
            hi = N
        else:
            lo = N
    print(f"relacion focal minima de una esfera de D = 200 mm con W040 <= 1 onda: f/{hi:.2f} ; formula cerrada D <= 512 N^3 lambda -> N = {(D/(512*lam))**(1/3):.2f}")
    assert abs(hi - (D / (512 * lam)) ** (1 / 3)) < 1e-6
    # LSA y blur de la esfera frente a N
    for Nn in (5.0, 10.0):
        Fm = Nn * D
        Rr = 2 * Fm
        lsa = Rr * (1 / (2 * math.cos(math.asin(D / 2 / Rr))) - 1)           # |LSA| del rayo marginal respecto al foco paraxial
        lsa = abs(Rr * (1 - 1 / (2 * math.cos(math.asin(D / 2 / Rr)))) - Rr / 2)
        blur = lsa * (D / 2) / Fm * 2
        print(f"esfera f/{Nn:.0f}: LSA marginal = {lsa:.4f} mm ; disco de aberracion (aprox.) = {blur*1e3:.1f} micras")
    # coma
    th = math.radians(10.0 / 60.0)
    zf = F
    x_ch = traza(c, -1.0, 0.0, th, zf)
    print(f"campo de 10 arcmin ({th:.6e} rad): imagen del rayo principal x = {x_ch:.5f} mm (F tan th = {F*math.tan(th):.5f})")
    print(f"{'h [mm]':>7} {'x - x_principal [micras]':>26}")
    for h in (-100.0, -70.7, -50.0, 50.0, 70.7, 100.0):
        xh = traza(c, -1.0, h, th, zf)
        print(f"{h:7.1f} {(xh-x_ch)*1e3:26.3f}")
    xa, xb = traza(c, -1.0, 100.0, th, zf), traza(c, -1.0, -100.0, th, zf)
    coma_num = ((xa + xb) / 2 - x_ch)
    coma_form = 3 * th * F / (16 * (F / D) ** 2)
    print(f"coma tangencial (rayos marginales respecto al principal) = {coma_num*1e3:.3f} micras ; 3 theta F/(16 N^2) = {coma_form*1e3:.3f} micras ; razon = {coma_num/coma_form:.4f}")
    Airy = 2.44 * lam * (F / D)
    print(f"disco de Airy (2,44 lambda N) = {Airy*1e3:.2f} micras ; coma / diametro de Airy = {coma_num/Airy:.2f}")
    assert abs(coma_num / coma_form - 1) < 0.05
    # la coma crece linealmente con el campo
    c2 = (traza(c, -1.0, 100.0, 2 * th, zf) + traza(c, -1.0, -100.0, 2 * th, zf)) / 2 - traza(c, -1.0, 0.0, 2 * th, zf)
    print(f"campo doble: coma = {c2*1e3:.3f} micras ; razon con el campo simple = {c2/coma_num:.4f}")
    assert abs(c2 / coma_num - 2) < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
