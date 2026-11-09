#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C12: pixelizacion equiarea tipo HEALPix (orden anillo), ida y vuelta, uniformidad y fraccion de cielo de una mascara.

Datos: ninguna constante fisica. El esquema esta descrito en Gorski et al. (arXiv:astro-ph/0409513, solo resumen, consultado el 2026-11-09): pixeles de igual area en anillos de latitud
constante. Las formulas de ang2pix y pix2ang de este laboratorio son una implementacion PROPIA escrita de memoria (no copiada ni contrastada con la biblioteca oficial HEALPix, que no se
consulto); su validez se comprueba aqui por ida y vuelta y por area. Los puntos aleatorios (semilla 20261109) y el corte galactico de 20 grados son ILUSTRATIVOS.
Modelo: N_pix = 12 N_side^2 ; omega_pix = 4 pi / N_pix ; 4 N_side - 1 anillos ; casquete polar para |z| > 2/3.
Supuestos: orden anillo; N_side cualquier entero positivo (no se exige potencia de 2). Validez: educativa.
Tolerancia: ida y vuelta exacta para todos los pixeles de N_side = 4, 8 y 16; chi^2 por grado de libertad del recuento aleatorio entre 0,85 y 1,15; fraccion de cielo a 2e-3 del valor analitico con N_side = 256 (el error baja al subir N_side).
"""
from __future__ import annotations
import math, platform, random, sys

def npix(ns):
    return 12 * ns * ns

def ang2pix_ring(ns, z, phi):
    za = abs(z)
    tt = (phi % (2 * math.pi)) / (math.pi / 2)
    ncap = 2 * ns * (ns - 1)
    if za <= 2.0 / 3.0:
        t1 = ns * (0.5 + tt)
        t2 = ns * z * 0.75
        jp = int(t1 - t2); jm = int(t1 + t2)
        ir = ns + 1 + jp - jm
        kshift = 1 - (ir & 1)
        ip = (jp + jm - ns + kshift + 1) // 2
        ip %= 4 * ns
        return ncap + (ir - 1) * 4 * ns + ip
    tp = tt - int(tt)
    tmp = ns * math.sqrt(3 * (1 - za))
    jp = int(tp * tmp); jm = int((1 - tp) * tmp)
    ir = jp + jm + 1
    ip = int(tt * ir)
    ip %= 4 * ir
    if z > 0:
        return 2 * ir * (ir - 1) + ip
    return npix(ns) - 2 * ir * (ir + 1) + ip

def pix2ang_ring(ns, pix):
    ncap = 2 * ns * (ns - 1)
    n = npix(ns)
    if pix < ncap:
        ir = (1 + math.isqrt(1 + 2 * pix)) // 2
        iphi = pix + 1 - 2 * ir * (ir - 1)
        z = 1 - ir * ir / (3.0 * ns * ns)
        phi = (iphi - 0.5) * math.pi / (2 * ir)
    elif pix < n - ncap:
        ip = pix - ncap
        ir = ip // (4 * ns) + ns
        iphi = ip % (4 * ns) + 1
        fodd = 1.0 if (ir + ns) & 1 else 0.5
        z = (2 * ns - ir) * 2.0 / (3 * ns)
        phi = (iphi - fodd) * math.pi / (2 * ns)
    else:
        ip = n - pix
        ir = (1 + math.isqrt(2 * ip - 1)) // 2
        iphi = 4 * ir + 1 - (ip - 2 * ir * (ir - 1))
        z = -1 + ir * ir / (3.0 * ns * ns)
        phi = (iphi - 0.5) * math.pi / (2 * ir)
    return z, phi

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'N_side':>7} {'N_pix':>9} {'omega_pix [arcmin^2]':>22} {'resolucion [arcmin]':>20} {'anillos':>8} {'ida y vuelta':>13}")
    for ns in (1, 2, 4, 8, 16):
        fallos = 0
        for p in range(npix(ns)):
            z, ph = pix2ang_ring(ns, p)
            if ang2pix_ring(ns, z, ph) != p:
                fallos += 1
        om = 4 * math.pi / npix(ns) * (180 * 60 / math.pi) ** 2
        print(f"{ns:7d} {npix(ns):9d} {om:22.1f} {math.sqrt(om):20.2f} {4 * ns - 1:8d} {'exacta' if not fallos else str(fallos) + ' fallos':>13}")
        assert fallos == 0
    for ns in (64, 1024):
        om = 4 * math.pi / npix(ns) * (180 * 60 / math.pi) ** 2
        print(f"{ns:7d} {npix(ns):9d} {om:22.2f} {math.sqrt(om):20.3f}")
    # uniformidad con puntos aleatorios uniformes en la esfera
    ns = 8
    n = npix(ns)
    rng = random.Random(20261109)
    cuentas = [0] * n
    puntos = 200 * n
    for _ in range(puntos):
        z = rng.uniform(-1, 1); ph = rng.uniform(0, 2 * math.pi)
        cuentas[ang2pix_ring(ns, z, ph)] += 1
    esp = puntos / n
    chi2 = sum((c - esp) ** 2 / esp for c in cuentas)
    print(f"N_side = 8: {puntos} puntos, esperado {esp:.0f} por pixel, minimo {min(cuentas)}, maximo {max(cuentas)}, chi^2/gl = {chi2 / (n - 1):.3f}")
    assert 0.85 < chi2 / (n - 1) < 1.15
    # integral de z^2 y fraccion de cielo
    corte = math.sin(math.radians(20))
    errs = {}
    for ns in (64, 256):
        n = npix(ns)
        s2 = 0.0; fuera = 0
        for p in range(n):
            z, _ = pix2ang_ring(ns, p)
            s2 += z * z
            if abs(z) > corte:
                fuera += 1
        integral = 4 * math.pi / n * s2
        errs[ns] = abs(fuera / n - (1 - corte))
        print(f"N_side = {ns}: integral de z^2 = {integral:.6f} (4 pi/3 = {4 * math.pi / 3:.6f}) ; fraccion de cielo |b| > 20 grados = {fuera / n:.5f} (analitica 1 - sin 20 = {1 - corte:.5f}) ; error {errs[ns]:.1e}")
        assert abs(integral / (4 * math.pi / 3) - 1) < 1e-3
    assert errs[256] < 2e-3 and errs[256] < errs[64]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
