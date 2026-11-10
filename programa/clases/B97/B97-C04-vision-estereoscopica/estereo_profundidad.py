#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C04: profundidad por disparidad en un par estereo ideal.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): distancia focal f = 1000 px, base B = 0.42 m, ruido de disparidad sigma_d = 0.25 px,
profundidades de 2 a 30 m, 200000 muestras con semilla fija. Ninguna cifra corresponde a una camara real.
Modelo: camaras paralelas rectificadas (pinhole); Z = f B / d; error por propagacion sigma_Z = Z^2 sigma_d / (f B).
Segunda via: Monte Carlo de la disparidad con ruido gaussiano (tolerancia 2 % relativa para Z = 10 m).
Unidades: Z y B en m; f y d en px. Sin distorsion, sin error de calibracion ni de correspondencia.
"""
from __future__ import annotations
import math, platform, random

F, B, SD, N, SEMILLA = 1000.0, 0.42, 0.25, 200000, 20261110   # ILUSTRATIVOS / SINTETICOS


def disparidad(z):
    return F * B / z


def sigma_z(z):
    return z * z * SD / (F * B)


def calc():
    rng = random.Random(SEMILLA)
    z0 = 10.0
    d0 = disparidad(z0)
    zs = [F * B / (d0 + rng.gauss(0, SD)) for _ in range(N)]
    m = sum(zs) / N
    s = math.sqrt(sum((z - m) ** 2 for z in zs) / (N - 1))
    tabla = [(z, disparidad(z), sigma_z(z), 100 * sigma_z(z) / z) for z in (2.0, 5.0, 10.0, 20.0, 30.0)]
    z5 = 0.05 * F * B / SD                    # alcance con error relativo <= 5 %
    b20 = 20.0 * SD / (F * 0.05)              # base para 5 % a 20 m
    return dict(d10=d0, s10=sigma_z(z0), s_mc=s, rel=abs(s - sigma_z(z0)) / sigma_z(z0), sesgo=m - z0, tabla=tabla, z5=z5, b20=b20,
                s20=sigma_z(20.0), s5=sigma_z(5.0), razon=sigma_z(20.0) / sigma_z(10.0), s10_b2=sigma_z(10.0) * 0.5)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Par estereo SINTETICO: f = {F:.0f} px; B = {B} m; sigma_d = {SD} px")
    print("  Z [m]   d [px]   sigma_Z [m]   error relativo [%]")
    for z, d, s, p in r["tabla"]:
        print(f"{z:6.1f} {d:8.2f} {s:12.4f} {p:14.2f}")
    print(f"Z = 10 m: sigma_Z teorica = {r['s10']:.5f} m; Monte Carlo = {r['s_mc']:.5f} m (diferencia relativa {r['rel']:.2e}); sesgo MC = {r['sesgo']*1000:.3f} mm")
    print(f"Alcance con error relativo <= 5 %: Z = {r['z5']:.2f} m; base necesaria para 5 % a 20 m: B = {r['b20']:.3f} m")
    print(f"sigma_Z(20 m)/sigma_Z(10 m) = {r['razon']:.3f} (teoria 4)")
    assert r["rel"] < 0.02 and abs(r["razon"] - 4) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
