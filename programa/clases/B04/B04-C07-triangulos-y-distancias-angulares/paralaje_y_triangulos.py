#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C07: triángulos rectángulos, paralaje y distancia angular.

Datos (PUBLICADOS; estimados, NASA Exoplanet Archive, tabla pscomppars, consulta
TAP del 2026-11-05; el archivo es mutable): paralaje sy_plx ± sy_plxerr1 (mas) de
Proxima Cen 768,5 ± 0,2030; tau Cet 277,516 ± 0,5173; eps Eri 312,219 ± 0,4673;
GJ 1061 272,245 ± 0,0661; Teegarden's Star 261,015 ± 0,2690. Radio ecuatorial
terrestre nominal 6,3781e6 m (IAU 2015 B3); distancia lunar media 384 400 km
(NASA Moon Fact Sheet). 1 au = 149 597 870 700 m (SI); 1 pc = 648000/pi au.
Modelo: tan p = 1 au / d (triángulo rectángulo con base 1 au, Sol-Tierra a 90° de
la visual) y d = 1/p (d en pc, p en ″). Supuestos: órbita terrestre circular de
1 au, estrella en el polo de la eclíptica (base perpendicular); sin movimiento
propio. Validez: p << 1 rad. Tolerancia de pruebas: 1e-12 relativa en
identidades; 1e-6 en la aproximación 1/p.
"""
from __future__ import annotations
import math, platform, sys

AU = 149_597_870_700.0
PC = 648_000.0 / math.pi * AU
LY = 299_792_458.0 * 365.25 * 86_400.0
MAS_A_RAD = math.pi / (648_000.0 * 1000.0)

ESTRELLAS = {          # nombre: (paralaje mas, error mas)  [publicado, estimado]
    "Proxima Cen": (768.5, 0.2030210),
    "tau Cet": (277.516, 0.517309),
    "eps Eri": (312.219, 0.467348),
    "GJ 1061": (272.245, 0.0660788),
    "Teegarden": (261.015, 0.26896),
}


def distancia_exacta(p_mas):
    """d = 1 au / tan p, en metros."""
    return AU / math.tan(p_mas * MAS_A_RAD)


def resolver_rectangulo(cateto_a, cateto_b):
    h = math.hypot(cateto_a, cateto_b)
    return h, math.atan2(cateto_a, cateto_b)


def pruebas():
    h, ang = resolver_rectangulo(3.0, 4.0)
    assert abs(h - 5.0) < 1e-15 and abs(math.degrees(ang) - 36.8698976) < 1e-6
    assert abs(math.sin(math.radians(30)) - 0.5) < 1e-15
    for p in (1.0, 100.0, 768.5):                         # tan p * d = 1 au
        d = distancia_exacta(p)
        assert abs(math.tan(p * MAS_A_RAD) * d / AU - 1) < 1e-12
    assert abs(PC - 3.0856775814913673e16) / PC < 1e-12    # parsec en m
    # d = 1/p en pc: tolerancia 1e-6 porque tan p ≈ p
    assert abs(distancia_exacta(768.5) / PC - 1000 / 768.5) / (1000 / 768.5) < 1e-6
    assert abs(MAS_A_RAD * 206_264_806.2471 - 1.0) < 1e-9  # 1 mas en rad


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (3-4-5, 30°, tan p·d = 1 au, parsec, d = 1/p, mas→rad)")
    print(f"\n{'Estrella':<13}{'p (mas)':>10}{'± (mas)':>9}{'d (pc)':>10}{'± (pc)':>9}{'d (ly)':>9}{'error rel.':>11}")
    for n, (p, e) in ESTRELLAS.items():
        d_pc = distancia_exacta(p) / PC
        e_pc = d_pc * e / p
        print(f"{n:<13}{p:10.3f}{e:9.3f}{d_pc:10.4f}{e_pc:9.4f}{d_pc * PC / LY:9.3f}{e / p:11.2e}")
    print("\nProxima: 1000/p = %.5f pc; archivo (sy_dist) = 1,30119 pc" % (1000 / 768.5))
    # Paralaje horizontal lunar con la Tierra como base: sin(pi) = R / d
    R_t, d_l = 6.3781e6, 384_400e3
    pi_l = math.asin(R_t / d_l)
    print(f"\nParalaje horizontal lunar: sen π = R/d -> π = {math.degrees(pi_l):.4f}° = {math.degrees(pi_l)*60:.2f}′")
    print(f"  Con la base R y ángulo π se recupera d = R/sen π = {R_t / math.sin(pi_l) / 1e3:.0f} km")
    # Tamaño lineal a partir del tamaño angular
    delta = 0.5179 * math.pi / 180
    print(f"\nObjeto de diámetro angular 0,5179° a 384 400 km: D = 2 d tan(δ/2) = "
          f"{2 * d_l * math.tan(delta / 2) / 1e3:.0f} km (Luna: 3474,8 km de diámetro)")
    # Mínimo paralaje detectable: si el error fuera 1 mas, ¿a qué distancia llega 10 %?
    print(f"\nCon error de 0,2 mas y exigiendo error relativo del 10 %: p ≥ {0.2 / 0.10:.1f} mas -> "
          f"d ≤ {1000 / (0.2 / 0.10):.0f} pc")


if __name__ == "__main__":
    main()
