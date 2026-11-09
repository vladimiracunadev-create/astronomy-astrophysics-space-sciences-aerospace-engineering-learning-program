#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C19: colimacion (tolerancia de inclinacion), profundidad de foco con Strehl y zonas de la prueba de Foucault.

Datos: sin constantes del NIST. Newton de D = 200 mm, F = 1000 mm (f/5), distancia del plano al foco q = 130 mm, lambda = 550 nm y sigma de descolimacion de 0,1 grado
son ILUSTRATIVOS.
Modelo: (1) Foucault: un punto fuente en el centro de curvatura R de un paraboloide; el rayo reflejado por la zona h corta el eje a una distancia R + h^2/R (trazado exacto
frente a la formula). (2) Enfoque: el defecto de enfoque dz produce W20 = dz/(8 N^2) en el borde; Strehl por integracion numerica sobre la pupila (regla del punto medio en rho)
frente a la forma cerrada sinc^2(a/2) con a = 2 pi W20/lambda; se busca el dz con Strehl 0,8. (3) Colimacion: inclinar el secundario un angulo alfa gira el eje 2 alfa y descentra el campo
un angulo equivalente theta = 2 alfa q/F; la coma 3 theta F/(16 N^2) (verificada en B41-C13) se compara con el radio del disco de Airy 1,22 lambda N. Simulacion con semilla 20261109: fraccion de
equipos con coma menor que ese radio frente a erf.
Supuestos: paraboloide perfecto, descolimacion solo del secundario, sin efecto de segundo orden. Validez: tercer orden, angulos pequeños.
Tolerancia: Foucault 1e-6 mm; Strehl numerico frente a cerrado 1e-6; fraccion Monte Carlo frente a erf 1,5 %.
"""
from __future__ import annotations
import math, platform, random, sys


def foucault(R, h):
    """Fuente en (0, R) (centro de curvatura) frente a un paraboloide z = x^2/(2R) con vertice en 0. Devuelve donde el rayo reflejado corta el eje."""
    z = h * h / (2 * R)
    d = (h - 0.0, z - R)
    nrm = math.hypot(*d)
    d = (d[0] / nrm, d[1] / nrm)
    n = (-h / R, 1.0)                    # gradiente de z - x^2/(2R)
    nn = math.hypot(*n)
    n = (n[0] / nn, n[1] / nn)
    kdn = d[0] * n[0] + d[1] * n[1]
    r = (d[0] - 2 * kdn * n[0], d[1] - 2 * kdn * n[1])
    t = -h / r[0]
    return z + t * r[1]


def strehl_num(a, n=20000):
    s = 0.0
    c = 0.0
    for i in range(n):
        rho = (i + 0.5) / n
        w = 2 * rho / n
        s += w * math.cos(a * rho * rho)
        c += w * math.sin(a * rho * rho)
    return s * s + c * c


def strehl_cerrado(a):
    return 1.0 if a == 0 else (math.sin(a / 2) / (a / 2)) ** 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = 2000.0
    print("Foucault: fuente en el centro de curvatura de un paraboloide, R = 2000 mm")
    print(f"{'h [mm]':>7} {'corte del eje [mm]':>19} {'R + h^2/R [mm]':>16} {'dif. con R [mm]':>16}")
    for h in (20.0, 50.0, 70.7, 100.0):
        z = foucault(R, h)
        print(f"{h:7.1f} {z:19.6f} {R + h*h/R:16.6f} {z-R:16.6f}")
        assert abs(z - (R + h * h / R)) < 1e-2
    # a mayor precision: la formula es de tercer orden; la diferencia exacta
    z = foucault(R, 100.0)
    print(f"  diferencia exacta - tercer orden en h = 100 mm: {z-(R+100.0**2/R):.6f} mm")
    # enfoque
    D, F, lam = 200.0, 1000.0, 550e-6
    N = F / D
    print(f"f/{N:.0f}: 2 lambda N^2 = {2*lam*N*N*1e3:.1f} micras")
    print(f"{'dz [micras]':>12} {'W20 [ondas]':>12} {'Strehl num.':>12} {'cerrado':>10}")
    for dz_um in (0.0, 13.75, 27.5, 55.0, 110.0):
        dz = dz_um * 1e-3
        w20 = dz / (8 * N * N) / lam
        a = 2 * math.pi * w20
        sn, sc = strehl_num(a), strehl_cerrado(a)
        print(f"{dz_um:12.2f} {w20:12.4f} {sn:12.5f} {sc:10.5f}")
        assert abs(sn - sc) < 1e-6
    lo, hi = 0.0, 4 * lam * N * N
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        a = 2 * math.pi * mid / (8 * N * N) / lam
        if strehl_cerrado(a) > 0.8:
            lo = mid
        else:
            hi = mid
    print(f"dz con Strehl 0,8 = +-{lo*1e3:.2f} micras = {lo/(lam*N*N):.3f} lambda N^2 (la regla de libro usa 2 lambda N^2)")
    assert 1.5 < lo / (lam * N * N) < 2.2
    # colimacion
    q = 130.0
    airy_r = 1.22 * lam * N * 1e3        # micras
    print(f"radio de Airy 1,22 lambda N = {airy_r:.2f} micras")
    print(f"{'alfa [deg]':>10} {'descentrado [mm]':>17} {'theta eq. [arcmin]':>19} {'coma [micras]':>14} {'coma/radio Airy':>16}")
    for ad in (0.02, 0.05, 0.1, 0.2, 0.5):
        al = math.radians(ad)
        dec = 2 * al * q
        th = dec / F
        coma = 3 * th * F / (16 * N * N) * 1e3
        print(f"{ad:10.2f} {dec:17.4f} {math.degrees(th)*60:19.3f} {coma:14.3f} {coma/airy_r:16.3f}")
    # alfa maximo con coma = radio de Airy
    al_max = airy_r * 1e-3 * 16 * N * N / (3 * F) * F / (2 * q)
    print(f"alfa maximo con coma igual al radio de Airy = {math.degrees(al_max):.4f} deg = {math.degrees(al_max)*60:.2f} arcmin")
    # simulacion
    rng = random.Random(20261109)
    sig = math.radians(0.1)
    n = 200_000
    ok = sum(1 for _ in range(n) if abs(rng.gauss(0, sig)) < al_max)
    frac = ok / n
    teor = math.erf(al_max / (sig * math.sqrt(2)))
    print(f"descolimacion normal de sigma = {math.degrees(sig):.1f} deg: fraccion con coma < radio de Airy = {frac:.4f} (Monte Carlo) frente a erf = {teor:.4f}")
    assert abs(frac - teor) < 0.015
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
