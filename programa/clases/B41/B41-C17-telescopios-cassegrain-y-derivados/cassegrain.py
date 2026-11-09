#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C17: Cassegrain clasico, Dall-Kirkham y Ritchey-Chretien (trazado exacto de dos espejos conicos).

Datos: sin constantes del NIST. D = 200 mm, focal del primario f1 = 400 mm (f/2), aumento del secundario m = 5 (focal efectiva 2000 mm, f/10), foco 100 mm detras del vertice
del primario y campo de 10 minutos de arco son ILUSTRATIVOS.
Modelo: geometria de primer orden: separacion d = (m f1 - b)/(m + 1); radio del secundario R2 = 2 s s'/(s' - s) con s = f1 - d y s' = d + b. Cassegrain clasico: primario parabolico (k1 = -1) y
secundario hiperbolico k2 = -((m+1)/(m-1))^2 (formula analitica). Dall-Kirkham: secundario esferico (k2 = 0) y k1 que anula la aberracion esferica (biseccion). Ritchey-Chretien:
k1 y k2 que anulan simultaneamente la aberracion esferica y la coma (Newton 2D con jacobiano numerico). Todo con trazado exacto de rayos meridionales.
Segunda via: la aberracion esferica del clasico se verifica nula por el trazado y la focal efectiva se mide con un rayo de campo; la coma del clasico se compara con la del paraboloide f/10, 3 theta F/(16 N^2).
Supuestos: rayos meridionales, sin obstruccion modelada en el trazado (solo se registra la fraccion), reflexion perfecta. Validez: geometrica.
Tolerancia: aberracion esferica residual < 1e-6 mm; focal efectiva 2000 mm a 0,1 %; coma del clasico frente a la formula 10 %.
"""
from __future__ import annotations
import math, platform, sys

D, F1, M, BF = 200.0, 400.0, 5.0, 100.0
Dsep = (M * F1 - BF) / (M + 1)
S, SP = F1 - Dsep, Dsep + BF
R1 = 2 * F1
R2 = 2 * S * SP / (SP - S)
ZF = -BF


def interseca(p, d, zv, c, k):
    A = c * (d[0] ** 2 + (1 + k) * d[1] ** 2)
    B = 2 * c * (p[0] * d[0] + (1 + k) * (p[1] - zv) * d[1]) - 2 * d[1]
    C = c * (p[0] ** 2 + (1 + k) * (p[1] - zv) ** 2) - 2 * (p[1] - zv)
    if abs(A) < 1e-18:
        ts = [-C / B]
    else:
        disc = math.sqrt(B * B - 4 * A * C)
        ts = [(-B - disc) / (2 * A), (-B + disc) / (2 * A)]
    cand = [(abs(p[1] + t * d[1] - zv), t) for t in ts if t > 1e-9]
    t = min(cand)[1]
    return t


def refleja(p, d, zv, c, k):
    t = interseca(p, d, zv, c, k)
    q = (p[0] + t * d[0], p[1] + t * d[1])
    n = (2 * c * q[0], 2 * c * (1 + k) * (q[1] - zv) - 2)
    nn = math.hypot(*n)
    n = (n[0] / nn, n[1] / nn)
    kdn = d[0] * n[0] + d[1] * n[1]
    return q, (d[0] - 2 * kdn * n[0], d[1] - 2 * kdn * n[1])


def traza(h, th, k1, k2):
    d = (math.sin(th), -math.cos(th))
    p = (h, 3000.0)
    q, d = refleja(p, d, 0.0, 1 / R1, k1)
    q, d = refleja(q, d, Dsep, 1 / R2, k2)
    s = (ZF - q[1]) / d[1]
    return q[0] + s * d[0]


def esferica(k1, k2, h=100.0):
    return traza(h, 0.0, k1, k2) - traza(1e-3, 0.0, k1, k2)


def coma(k1, k2, th, h=100.0):
    return (traza(h, th, k1, k2) + traza(-h, th, k1, k2)) / 2 - traza(0.0, th, k1, k2)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"geometria de primer orden: separacion d = {Dsep:.3f} mm ; s = {S:.3f} ; s' = {SP:.3f} ; R1 = {R1:.1f} ; R2 = {R2:.3f} mm (convexo)")
    th = math.radians(10.0 / 60.0)
    k2c = -((M + 1) / (M - 1)) ** 2
    print(f"{'diseno':>14} {'k1':>10} {'k2':>10} {'esferica [mm]':>14} {'coma 10 arcmin [micras]':>25}")
    ec = esferica(-1.0, k2c)
    cc = coma(-1.0, k2c, th)
    print(f"{'Cassegrain':>14} {-1.0:10.5f} {k2c:10.5f} {ec:14.2e} {cc*1e3:25.3f}")
    assert abs(ec) < 1e-6
    # focal efectiva
    feff = (traza(1e-3, th, -1.0, k2c) - traza(1e-3, 0.0, -1.0, k2c)) / math.tan(th)
    print(f"focal efectiva medida = {abs(feff):.2f} mm (esperada {M*F1:.0f} mm)")
    assert abs(abs(feff) / (M * F1) - 1) < 1e-3
    # coma del paraboloide f/10 de comparacion
    comaf = 3 * th * (M * F1) / (16 * (M * F1 / D) ** 2)
    print(f"  coma del paraboloide f/10 con la misma focal: 3 theta F/(16 N^2) = {comaf*1e3:.3f} micras ; razon con el clasico = {abs(cc)/comaf:.3f}")
    assert abs(abs(cc) / comaf - 1) < 0.10
    # Dall-Kirkham: k2 = 0, k1 que anula la esferica
    lo, hi = -1.0, 0.0
    f_lo = esferica(lo, 0.0)
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if esferica(mid, 0.0) * f_lo > 0:
            lo = mid
        else:
            hi = mid
    k1dk = 0.5 * (lo + hi)
    print(f"{'Dall-Kirkham':>14} {k1dk:10.5f} {0.0:10.5f} {esferica(k1dk,0.0):14.2e} {coma(k1dk,0.0,th)*1e3:25.3f}")
    assert abs(esferica(k1dk, 0.0)) < 1e-6
    # Ritchey-Chretien: Newton 2D
    k1, k2 = -1.0, k2c
    for it in range(30):
        f1_, f2_ = esferica(k1, k2), coma(k1, k2, th)
        e = 1e-6
        a11 = (esferica(k1 + e, k2) - f1_) / e
        a12 = (esferica(k1, k2 + e) - f1_) / e
        a21 = (coma(k1 + e, k2, th) - f2_) / e
        a22 = (coma(k1, k2 + e, th) - f2_) / e
        det = a11 * a22 - a12 * a21
        dk1 = (a22 * f1_ - a12 * f2_) / det
        dk2 = (-a21 * f1_ + a11 * f2_) / det
        k1 -= dk1
        k2 -= dk2
        if abs(dk1) + abs(dk2) < 1e-13:
            break
    er, cr = esferica(k1, k2), coma(k1, k2, th)
    print(f"{'Ritchey-Chretien':>14} {k1:10.5f} {k2:10.5f} {er:14.2e} {cr*1e3:25.6f}")
    assert abs(er) < 1e-6 and abs(cr) < 1e-6
    # coma residual a 30 arcmin (orden superior) y astigmatismo no corregidos
    th3 = math.radians(0.5)
    print(f"a 30 arcmin la coma residual del RC = {coma(k1,k2,th3)*1e3:.3f} micras ; del clasico = {coma(-1.0,k2c,th3)*1e3:.3f} micras")
    # obstruccion del secundario: radio del cono en el secundario
    r_sec = (D / 2) * S / F1
    print(f"el secundario intercepta un cono de radio {r_sec:.2f} mm: obstruccion lineal minima = {r_sec*2/D*100:.1f} % (sin campo)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
