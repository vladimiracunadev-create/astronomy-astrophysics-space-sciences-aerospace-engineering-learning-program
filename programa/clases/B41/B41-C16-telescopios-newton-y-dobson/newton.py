#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C16: espejo plano secundario de un Newton (tamano, obstruccion) y tiempo de transito de un Dobson.

Datos: D = 200 mm, F = 1000 mm (f/5), campo plenamente iluminado de 20 mm, distancia del eje al plano focal q = 130 mm y ocular de 25 mm con campo aparente de
52 grados son ILUSTRATIVOS. El dia sideral, 86164,0905 s, es un valor de libro NO consultado en esta sesion (ilustrativo); 360 grados en arco son 1 296 000 segundos de arco.
Modelo: eje menor del plano: a = w + (D - w) q/F (derivable de la geometria del cono de rayos). Segunda via: simulacion Monte Carlo con semilla 20261109: se
sortean puntos de campo (disco de diametro w) y de pupila (disco de D), se lleva el rayo hasta el plano z = F - q y se mide el radio maximo cubierto.
Dobson: montura altazimutal sin motor; tiempo de transito t = campo real / (velocidad sideral cos dec).
Supuestos: primario parabolico perfecto, rayos sin aberracion, plano perpendicular al eje en la medicion. Validez: geometrica.
Tolerancia: radio maximo del Monte Carlo frente a la formula 2 % (el maximo de una muestra queda por debajo del valor teorico).
"""
from __future__ import annotations
import math, platform, random, sys


def punto_disco(rng, r):
    while True:
        x, y = rng.uniform(-r, r), rng.uniform(-r, r)
        if x * x + y * y <= r * r:
            return x, y


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    D, F, w, q = 200.0, 1000.0, 20.0, 130.0
    a = w + (D - w) * q / F
    rad = a / 2
    print(f"Newton f/{F/D:.0f}: D = {D:.0f} mm, F = {F:.0f} mm, campo plenamente iluminado w = {w:.0f} mm, q = {q:.0f} mm")
    print(f"eje menor del plano a = w + (D - w) q/F = {a:.2f} mm ; eje mayor (a por raiz de 2) = {a*math.sqrt(2):.2f} mm")
    print(f"obstruccion lineal = {a/D*100:.1f} % ; por area = {(a/D)**2*100:.2f} % ; perdida de luz = {-2.5*math.log10(1-(a/D)**2):.4f} mag")
    # Monte Carlo
    rng = random.Random(20261109)
    zs = F - q
    rmax = 0.0
    n = 400_000
    for _ in range(n):
        sx, sy = punto_disco(rng, w / 2)
        hx, hy = punto_disco(rng, D / 2)
        # rayo desde el punto (hx, hy) del primario (z=0) hacia el punto de imagen (sx, sy) en z = F; posicion en z = F - q
        t = (F - q) / F
        x = hx + (sx - hx) * t
        y = hy + (sy - hy) * t
        r = math.hypot(x, y)
        if r > rmax:
            rmax = r
    print(f"Monte Carlo ({n} rayos, semilla 20261109): radio maximo = {rmax:.4f} mm ; formula a/2 = {rad:.4f} mm ; razon = {rmax/rad:.4f}")
    assert 0.98 < rmax / rad <= 1.0 + 1e-9
    # el eje menor crece con q
    print(f"{'q [mm]':>7} {'a [mm]':>8} {'obstruccion lineal [%]':>24}")
    for qq in (100.0, 130.0, 160.0, 200.0):
        aa = w + (D - w) * qq / F
        print(f"{qq:7.0f} {aa:8.2f} {aa/D*100:24.1f}")
    # Dobson: transito
    sid = 360 * 3600 / 86164.0905
    print(f"velocidad sideral = {sid:.4f} arcsec/s")
    assert abs(sid - 15.0411) < 1e-3
    fe, afov = 25.0, 52.0
    M = F / fe
    tfov = afov / M
    print(f"ocular {fe:.0f} mm: aumento {M:.0f} ; campo real = {tfov:.4f} deg = {tfov*3600:.1f} arcsec")
    print(f"{'dec [deg]':>9} {'transito [s]':>13}")
    for dec in (0, 30, 60, 75):
        t = tfov * 3600 / (sid * math.cos(math.radians(dec)))
        print(f"{dec:9d} {t:13.1f}")
    t0 = tfov * 3600 / sid
    assert abs(t0 - 311.1) < 0.5
    print(f"con aumento doble el transito dura la mitad: {t0/2:.1f} s en dec 0")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
