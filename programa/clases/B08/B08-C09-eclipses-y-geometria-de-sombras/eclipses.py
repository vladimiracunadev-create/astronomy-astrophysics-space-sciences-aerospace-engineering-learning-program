#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C09: geometría de sombras y candidatos a eclipse en 2025.

Datos PUBLICADOS: radios medios del Sol (695 700 km), la Tierra (6371 km) y la Luna (1737,4 km) y la distancia media
al Sol (149,6e6 km), de las fichas de la NASA NSSDC (consultadas 2026-11-05). Posiciones lunares (RA h, Dec grados,
J2000) de NASA SVS 5415 (efeméride JPL DE421, mooninfo_2025.txt), copiadas de las filas horarias más cercanas a cada
Luna nueva y llena de 2025. Salidas SIMULADAS (calculadas): longitud del cono de sombra y separación Luna-Sol
(o Luna-antisolar). Modelo: Sol puntual a distancia media, conos de sombra rectos, sin atmósfera ni penumbra.
Límites derivados (no son valores publicados): solar parcial posible si sep < r_sol + r_luna + paralaje; lunar umbral si
sep < r_umbra + r_luna. Dominio: Luna nueva/llena; tolerancia de muestreo horario: +-0,3 grados.
Prueba independiente: la tabla de eclipses solares de la NASA (eclipse.gsfc.nasa.gov, década 2021-2030) lista para 2025
solo los eclipses parciales del 29-mar y el 21-sep; el modelo debe marcar como candidatas exactamente esas dos lunas nuevas.
"""
from __future__ import annotations

import math
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import D2R, jd_utc, precesion_j2000, pruebas_biblioteca, separacion, sun_radec  # noqa: E402

R_SOL, R_TIERRA, R_LUNA, UA = 695_700.0, 6_371.0, 1_737.4, 149.6e6   # km

# (fecha UT, distancia km, AR h, Dec grados) -- filas de mooninfo_2025.txt
NUEVAS = [
    ("2025-01-29 12:00", 374358, 20.8458, -21.6841), ("2025-02-28 00:00", 364784, 22.7401, -9.771),
    ("2025-03-29 10:00", 358751, 0.4659, 4.1156), ("2025-04-27 18:00", 357123, 2.1995, 16.809),
    ("2025-05-27 01:00", 359885, 4.1015, 25.6821), ("2025-06-25 10:00", 366718, 6.2605, 28.2914),
    ("2025-07-24 18:00", 376103, 8.2817, 23.6148), ("2025-08-23 05:00", 386876, 10.1426, 13.241),
    ("2025-09-21 18:00", 396872, 11.8385, 0.0765), ("2025-10-21 10:00", 404115, 13.5768, -13.3766),
    ("2025-11-20 04:00", 406689, 15.5295, -23.9697), ("2025-12-20 00:00", 403624, 17.7879, -28.2244),
]
LLENAS = [
    ("2025-01-13 22:00", 381343, 7.7408, 25.945), ("2025-02-12 14:00", 392642, 9.8076, 16.2927),
    ("2025-03-14 06:00", 401414, 11.5891, 3.0583), ("2025-04-12 23:00", 405970, 13.3184, -10.7612),
    ("2025-05-12 14:00", 405412, 15.118, -21.846), ("2025-06-11 06:00", 399930, 17.2022, -27.9839),
    ("2025-07-10 20:00", 390825, 19.3551, -26.6177), ("2025-08-09 07:00", 380209, 21.2968, -18.6408),
    ("2025-09-07 17:00", 369841, 23.0468, -6.4753), ("2025-10-07 02:00", 361640, 0.7194, 7.0269),
    ("2025-11-05 12:00", 357024, 2.5582, 19.484), ("2025-12-04 22:00", 357169, 4.6437, 27.1617),
]
ECLIPSES_SOLARES_2025_NASA = {"2025-03-29", "2025-09-21"}   # tabla de la década 2021-2030


def longitud_umbra_luna_km() -> float:
    """Distancia desde el centro de la Luna hasta el vértice de su cono de umbra."""
    return R_LUNA * UA / (R_SOL - R_LUNA)


def radio_umbra_tierra_a(distancia_km: float) -> float:
    """Radio de la umbra de la Tierra a una distancia dada del centro de la Tierra (km)."""
    return R_TIERRA - distancia_km * (R_SOL - R_TIERRA) / UA


def limite_solar_deg(dist_luna_km: float) -> float:
    paralaje = math.asin(R_TIERRA / dist_luna_km) / D2R
    return (math.atan(R_SOL / UA) + math.atan(R_LUNA / dist_luna_km)) / D2R + paralaje


def limite_lunar_umbra_deg(dist_luna_km: float) -> float:
    return (math.atan(radio_umbra_tierra_a(dist_luna_km) / dist_luna_km) + math.atan(R_LUNA / dist_luna_km)) / D2R


def separacion_luna_sol(fecha: str, ar_h: float, dec: float, opuesto: bool) -> float:
    t = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
    jd = jd_utc(t.year, t.month, t.day, t.hour)
    rl, dl = precesion_j2000(ar_h * 15.0, dec, jd)
    rs, ds, _ = sun_radec(jd)
    if opuesto:
        rs, ds = (rs + 180.0) % 360.0, -ds
    return separacion(rl, dl, rs, ds)


def candidatas_solares() -> list[str]:
    return [f[:10] for f, d, ar, dec in NUEVAS if separacion_luna_sol(f, ar, dec, False) < limite_solar_deg(d)]


def pruebas() -> None:
    pruebas_biblioteca()
    assert set(candidatas_solares()) == ECLIPSES_SOLARES_2025_NASA, candidatas_solares()
    assert longitud_umbra_luna_km() > 356_830 - R_TIERRA          # al perigeo, la umbra alcanza la superficie
    assert longitud_umbra_luna_km() < 406_690 - R_TIERRA          # al apogeo no llega: eclipse anular
    assert abs(radio_umbra_tierra_a(0.0) - R_TIERRA) < 1e-9


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    L = longitud_umbra_luna_km()
    print(f"Longitud de la umbra de la Luna: {L:,.0f} km (SIMULADO). Totalidad posible si distancia - R_Tierra < L, es decir distancia < {L + R_TIERRA:,.0f} km")
    ru = radio_umbra_tierra_a(384_400)
    print(f"Umbra de la Tierra a 384 400 km: radio {ru:,.0f} km = {ru / R_LUNA:.2f} radios lunares; radio angular {math.degrees(math.atan(ru / 384_400)):.3f} grados")
    print("Lunas nuevas 2025: fecha | distancia | separacion Luna-Sol | limite | candidata")
    for f, d, ar, dec in NUEVAS:
        s, lim = separacion_luna_sol(f, ar, dec, False), limite_solar_deg(d)
        print(f"{f} | {d:6d} | {s:5.2f} | {lim:4.2f} | {'SI' if s < lim else 'no'}")
    print("Lunas llenas 2025: fecha | separacion Luna-antisolar | limite umbra | candidata (eclipse lunar umbral)")
    for f, d, ar, dec in LLENAS:
        s, lim = separacion_luna_sol(f, ar, dec, True), limite_lunar_umbra_deg(d)
        print(f"{f} | {s:5.2f} | {lim:4.2f} | {'SI' if s < lim else 'no'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
