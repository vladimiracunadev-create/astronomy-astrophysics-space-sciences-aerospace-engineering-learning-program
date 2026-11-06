#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C21: direcciones en el ICRS, separaciones de milisegundos de arco y rotaciones de ejes.

Datos: oblicuidad de la eclíptica en J2000.0 eps0 = 84381.406 arcsec (IERS
Conventions 2010, TN36, Tabla 1.1, consultada 2026-11-05); 1 au = 1.495978707e11 m
(TN36); distancia lunar media 384 400 km (NASA/NSSDC, 2024). Cifras de calidad
de los marcos (TN36 y ICRF3, arXiv:2010.13625): ruido de ICRF2 ~0.04 mas,
estabilidad de ejes 0.01 mas, ICRF3 mediana 0.1 mas (AR) y 0.2 mas (dec),
suelo de ruido 0.03 mas. Las posiciones de las fuentes del laboratorio son
SINTETICAS.
Modelo: una direccion (alfa, delta) del ICRS es el vector unitario
(cos d cos a, cos d sin a, sin d). Una rotacion de los ejes del marco por un
angulo pequeno theta alrededor de z cambia alfa en theta. La separacion
angular se calcula con atan2(|u x v|, u . v), estable a mas; la forma
acos(u . v) pierde precision para separaciones de milisegundos de arco.
Supuestos: fuentes sin movimiento propio; sin aberracion ni paralaje.
Tolerancia: separacion de 1 mas recuperada a 1e-6 relativa con atan2.
"""
from __future__ import annotations
import math
import platform
import sys

MAS = math.pi / (180 * 3600 * 1000)       # rad por mas
EPS0 = 84381.406 / 3600.0                  # grados
AU, D_LUNA = 1.495978707e11, 3.844e8


def vec(ra_deg, dec_deg):
    a, d = math.radians(ra_deg), math.radians(dec_deg)
    return (math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d))


def sep_atan2(u, v):
    cx = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
    return math.atan2(math.sqrt(sum(c * c for c in cx)), sum(a * b for a, b in zip(u, v)))


def sep_acos(u, v):
    return math.acos(max(-1.0, min(1.0, sum(a * b for a, b in zip(u, v)))))


def rot_z(v, th):
    c, s = math.cos(th), math.sin(th)
    return (c * v[0] - s * v[1], s * v[0] + c * v[1], v[2])


def rot_x(v, th):
    c, s = math.cos(th), math.sin(th)
    return (v[0], c * v[1] - s * v[2], s * v[1] + c * v[2])


def a_radec(v):
    return math.degrees(math.atan2(v[1], v[0])) % 360.0, math.degrees(math.asin(v[2]))


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1) separacion de 1 mas a dec = 40 grados, en declinacion
    u = vec(150.0, 40.0)
    v = vec(150.0, 40.0 + 1 * MAS * 180 / math.pi)
    s_at, s_ac = sep_atan2(u, v), sep_acos(u, v)
    print(f"separacion verdadera = 1.000000 mas ; atan2 = {s_at/MAS:.6f} mas ; acos = {s_ac/MAS:.6f} mas")
    assert abs(s_at / MAS - 1.0) < 1e-6
    # 2) separacion en AR: delta alfa cos delta
    v2 = vec(150.0 + 1 * MAS * 180 / math.pi / math.cos(math.radians(40.0)), 40.0)
    assert abs(sep_atan2(u, v2) / MAS - 1.0) < 1e-6
    # 3) rotacion de ejes de 0.1 mas alrededor de z cambia alfa en 0.1 mas
    w = rot_z(u, 0.1 * MAS)
    a0, d0 = a_radec(u)
    a1, d1 = a_radec(w)
    print(f"rotacion de 0.1 mas: delta alfa = {(a1 - a0) * 3600e3:.6f} mas ; delta dec = {(d1 - d0) * 3600e3:.2e} mas")
    assert abs((a1 - a0) * 3600e3 - 0.1) < 1e-6 and abs(d1 - d0) < 1e-12
    # 4) ICRS -> ecliptica de J2000 (rotacion alrededor de x por eps0)
    ncp = rot_x(vec(0.0, 90.0), -math.radians(EPS0))
    lat = math.degrees(math.asin(ncp[2]))
    print(f"polo norte celeste: latitud ecliptica = {lat:.6f} grados (90 - eps0 = {90 - EPS0:.6f})")
    assert abs(lat - (90 - EPS0)) < 1e-9
    # 5) cuanto es 1 mas en metros a la distancia de la Luna y de Marte (2 au, ejemplo)
    for nombre, d in (("Luna", D_LUNA), ("2 au", 2 * AU)):
        print(f"1 mas a {nombre}: {d * MAS:.4g} m")
    assert abs(D_LUNA * MAS - 1.8636) < 1e-3
    # 6) marcos: 0.03 mas de suelo de ruido a la distancia lunar
    print(f"0.03 mas a la Luna = {0.03 * D_LUNA * MAS * 100:.2f} cm ; 0.1 mas = {0.1 * D_LUNA * MAS * 100:.1f} cm")
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
