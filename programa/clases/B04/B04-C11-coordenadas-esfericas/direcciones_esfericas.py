#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C11: coordenadas esféricas y direcciones del cielo.

Datos (PUBLICADOS; estimados): NASA Exoplanet Archive, tabla pscomppars, columnas
ra y dec (grados decimales), consulta TAP del 2026-11-05 (archivo mutable; marco y
época de referencia NO declarados por la documentación del archivo (no se afirman);
solo con fines didácticos): Proxima Cen (217,3934657; -62,6761821), tau Cet
(26,0093029; -15,9337987), eps Eri (53,2284306; -9,4581715), GJ 1061
(54,0032486; -44,5143104), Teegarden (43,2691449; 16,8649024).
Modelo: ascensión recta α (sentido antihorario visto desde el polo norte) y
declinación δ (de -90° a +90°) -> vector unitario (cos δ cos α, cos δ sen α, sen δ).
Supuestos: dirección pura (sin distancia, sin paralaje ni movimiento propio).
Validez: ángulos en radianes internamente. Tolerancia: 1e-12 (ida y vuelta), 1e-9 (norma).
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


def a_vector(ra_deg, dec_deg):
    a, d = math.radians(ra_deg), math.radians(dec_deg)
    return (math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d))


def a_esfericas(v):
    x, y, z = v
    r = math.sqrt(x * x + y * y + z * z)
    ra = math.degrees(math.atan2(y, x)) % 360.0
    dec = math.degrees(math.asin(z / r))
    return ra, dec, r


def hms(ra_deg):
    h = ra_deg / 15.0
    hh = int(h)
    mm = int((h - hh) * 60)
    ss = ((h - hh) * 60 - mm) * 60
    return hh, mm, ss


def dms(dec_deg):
    s = -1 if dec_deg < 0 else 1
    a = abs(dec_deg)
    dd = int(a)
    mm = int((a - dd) * 60)
    ss = ((a - dd) * 60 - mm) * 60
    return s * dd, mm, ss


def pruebas():
    assert a_vector(0, 0) == (1.0, 0.0, 0.0)
    v = a_vector(90, 0)
    assert abs(v[0]) < 1e-15 and abs(v[1] - 1) < 1e-15
    assert a_vector(123, 90)[2] == 1.0
    assert abs(a_vector(10, -90)[2] + 1) < 1e-15
    n = 0
    for ra in (0.0, 45.0, 123.456, 270.0, 359.999):
        for dec in (-89.0, -45.0, 0.0, 30.0, 89.5):
            v = a_vector(ra, dec)
            assert abs(sum(c * c for c in v) - 1) < 1e-12
            ra2, dec2, r = a_esfericas(v)
            assert abs(((ra2 - ra + 180) % 360) - 180) < 1e-9 and abs(dec2 - dec) < 1e-9
            n += 1
    assert hms(217.3934657)[0] == 14
    return n


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    n = pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print(f"Pruebas: OK (ejes, polos, norma 1 e ida y vuelta en {n} direcciones)")
    print(f"\n{'Estrella':<13}{'α (°)':>10}{'α (h m s)':>16}{'δ (°)':>10}{'δ (° ′ ″)':>16}{'x':>9}{'y':>9}{'z':>9}")
    for nombre, (ra, dec) in ESTRELLAS.items():
        h, m, s = hms(ra)
        d, dm, ds = dms(dec)
        x, y, z = a_vector(ra, dec)
        print(f"{nombre:<13}{ra:10.4f}{h:5d}h{m:02d}m{s:05.2f}s{dec:10.4f}{d:6d}°{dm:02d}′{ds:04.1f}″{x:9.4f}{y:9.4f}{z:9.4f}")
    print("\nNota: α en horas = grados/15 (24 h = 360°).")
    print("Latitud −24,6° y longitud −70,4° (SINTÉTICAS) como vector:",
          " ".join(f"{c:.4f}" for c in a_vector(-70.4, -24.6)))


if __name__ == "__main__":
    main()
