#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C13: producto escalar y separación angular entre estrellas.

Datos (PUBLICADOS; estimados): NASA Exoplanet Archive, tabla pscomppars, columnas
ra y dec (grados decimales), consulta TAP del 2026-11-05 (archivo mutable; marco y
época no verificados, tratados como ICRS aproximado, solo con fines didácticos):
Proxima Cen (217,3934657; -62,6761821), tau Cet (26,0093029; -15,9337987),
eps Eri (53,2284306; -9,4581715), GJ 1061 (54,0032486; -44,5143104),
Teegarden (43,2691449; 16,8649024). Vectores de prueba: SINTÉTICOS.
Modelo: u·v = |u||v| cos γ; con vectores unitarios, γ = arccos(u·v). Variante
estable para ángulos pequeños: γ = 2·arcsen(|u − v|/2).
Supuestos: direcciones puras, sin paralaje ni movimiento propio. Validez: todo γ en [0, π].
Tolerancia de las pruebas: 1e-12 rad (casos exactos) y 1e-9 relativa (arccos frente a
cuerda para γ >= 1 grado).
"""
from __future__ import annotations
import math, platform, sys

ESTRELLAS = {
    "Proxima Cen": (217.3934657, -62.6761821),
    "tau Cet": (26.0093029, -15.9337987),
    "eps Eri": (53.2284306, -9.4581715),
    "GJ 1061": (54.0032486, -44.5143104),
    "Teegarden": (43.2691449, 16.8649024),
}


def a_vector(ra, dec):
    a, d = math.radians(ra), math.radians(dec)
    return (math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d))


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norma(u):
    return math.sqrt(dot(u, u))


def ang_arccos(u, v):
    c = dot(u, v) / (norma(u) * norma(v))
    return math.acos(max(-1.0, min(1.0, c)))


def ang_cuerda(u, v):
    un, vn = [a / norma(u) for a in u], [a / norma(v) for a in v]
    d = math.sqrt(sum((a - b) ** 2 for a, b in zip(un, vn)))
    return 2 * math.asin(min(1.0, d / 2))


def pruebas():
    x, y, z = (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)
    assert dot(x, y) == 0.0 and abs(ang_arccos(x, y) - math.pi / 2) < 1e-12
    assert ang_arccos(x, x) == 0.0 and abs(ang_arccos(x, (-1.0, 0.0, 0.0)) - math.pi) < 1e-12
    assert abs(ang_arccos((1.0, 0.0, 0.0), (0.5, math.sqrt(3) / 2, 0.0)) - math.pi / 3) < 1e-12
    assert abs(dot((1.0, 2.0, 3.0), (4.0, -5.0, 6.0)) - 12.0) < 1e-12        # 4 - 10 + 18
    # Simetría y escala
    u, v = (2.0, -1.0, 0.5), (0.3, 0.8, -1.2)
    assert dot(u, v) == dot(v, u) and abs(dot(tuple(3 * a for a in u), v) - 3 * dot(u, v)) < 1e-12
    # arccos y cuerda coinciden para separaciones >= 1 grado
    for deg in (1, 5, 30, 90, 150, 179):
        a = a_vector(10.0, 20.0)
        b = a_vector(10.0 + deg, 20.0)
        gam = math.degrees(ang_cuerda(a, b))
        assert abs(math.degrees(ang_arccos(a, b)) - gam) < 1e-9 * max(1, gam)
    # Para el ecuador, la separación es la diferencia de ascensión recta
    assert abs(math.degrees(ang_cuerda(a_vector(10, 0), a_vector(47.5, 0))) - 37.5) < 1e-9
    # Desigualdad triangular en la esfera
    A, B, C = (a_vector(*ESTRELLAS[k]) for k in ("Proxima Cen", "tau Cet", "eps Eri"))
    assert ang_cuerda(A, C) <= ang_cuerda(A, B) + ang_cuerda(B, C) + 1e-12


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (ortogonales, paralelos, 60°, producto 12, simetría, arccos=cuerda, ecuador, triangular)")
    nombres = list(ESTRELLAS)
    print(f"\n{'Par':<28}{'u·v':>10}{'γ arccos (°)':>14}{'γ cuerda (°)':>14}")
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            u, v = a_vector(*ESTRELLAS[nombres[i]]), a_vector(*ESTRELLAS[nombres[j]])
            print(f"{nombres[i] + ' – ' + nombres[j]:<28}{dot(u, v):10.5f}{math.degrees(ang_arccos(u, v)):14.4f}{math.degrees(ang_cuerda(u, v)):14.4f}")
    print("\nÁngulos pequeños (sintéticos): separación en el ecuador, arccos frente a cuerda")
    for arcsec in (1.0, 0.01, 0.001):
        g = math.radians(arcsec / 3600)
        u, v = a_vector(10.0, 0.0), a_vector(10.0 + arcsec / 3600, 0.0)
        print(f"  {arcsec:6.3f}″ exacto {arcsec:9.6f}″ | arccos {math.degrees(ang_arccos(u, v)) * 3600:10.6f}″ | cuerda {math.degrees(ang_cuerda(u, v)) * 3600:10.6f}″")
    w, e = (3.0, 4.0, 0.0), (1.0, 0.0, 0.0)
    print(f"\nProyección de w = (3, 4, 0) sobre ê = (1, 0, 0): w·ê = {dot(w, e):.1f}")


if __name__ == "__main__":
    main()
