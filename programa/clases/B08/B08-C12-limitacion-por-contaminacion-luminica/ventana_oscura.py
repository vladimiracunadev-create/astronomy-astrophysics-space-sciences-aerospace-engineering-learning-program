#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C12: cuántas horas de noche astronómica quedan sin Luna.

La luz de la Luna es una contaminación natural del cielo; esta clase la cuantifica como «horas de noche astronómica
con la Luna bajo el horizonte». Datos CALCULADOS por la NASA (SVS 5415, JPL DE421, mooninfo_2025.txt, consultada
2026-11-05): fase [%], AR [h] y Dec [grados] (J2000) cada 2 h para dos noches de 2025, copiadas fila a fila.
Lugar (redondeado): lat -30,0, lon -70,7. Modelo (SIMULADO): Sol de baja precisión (astrolib_b08); noche astronómica = Sol a
menos de -18 grados (definición USNO); Luna a su dirección geocéntrica con interpolación lineal entre filas, sin refracción
ni paralaje (error posible de ~1 grado en la altura). Dominio: estas dos noches. Tolerancia: 6 min en el crepúsculo (la referencia de astropy tiene paso de 5 min).
Prueba independiente: instantes del crepúsculo astronómico calculados con astropy 8.0.2 (copiados): 2025-11-06 00:35 y 08:15 UT;
2025-11-21 00:50 y 08:00 UT.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import altaz, altaz_j2000, jd_utc, lst_deg, pruebas_biblioteca, sun_radec  # noqa: E402

LAT, LON = -30.0, -70.7
# noche -> (año, mes, día de la fecha UT de la fila 0, filas (hora UT desde el inicio, fase %, AR h, Dec)), cada 2 h desde 22:00 UT
NOCHES = {
    "llena (5-6 nov 2025)": ((2025, 11, 5), [(99.64, 2.9849, 21.6610), (99.54, 3.0717, 22.0672), (99.41, 3.1590, 22.4631),
                                              (99.26, 3.2468, 22.8482), (99.09, 3.3351, 23.2222), (98.89, 3.4238, 23.5850),
                                              (98.68, 3.5130, 23.9363)]),
    "nueva (20-21 nov 2025)": ((2025, 11, 20), [(0.55, 16.1641, -26.0442), (0.65, 16.2359, -26.2362), (0.76, 16.3080, -26.4202),
                                                 (0.89, 16.3803, -26.5960), (1.03, 16.4529, -26.7636), (1.18, 16.5256, -26.9229),
                                                 (1.34, 16.5986, -27.0737)]),
}
REF_CREPUSCULO = {"llena (5-6 nov 2025)": (24.0 + 0.5833, 24.0 + 8.25), "nueva (20-21 nov 2025)": (24.0 + 0.8333, 24.0 + 8.0)}  # horas UT desde 00:00 del día de partida


def altura_sol(jd: float) -> float:
    ra, dec, _ = sun_radec(jd)
    return altaz(ra, dec, LAT, lst_deg(jd, LON))[0]


def crepusculos(y: int, m: int, d: int) -> tuple[float, float]:
    """(inicio, fin) de la noche astronómica en horas UT desde 00:00 del día (y,m,d); barrido de 1 min."""
    base = jd_utc(y, m, d, 18.0)
    dusk = dawn = None
    prev = altura_sol(base)
    for k in range(1, 16 * 60):
        a = altura_sol(base + k / 1440.0)
        if prev > -18.0 >= a and dusk is None:
            dusk = 18.0 + k / 60.0
        if prev < -18.0 <= a and dusk is not None and dawn is None:
            dawn = 18.0 + k / 60.0
        prev = a
    return dusk, dawn


def altura_luna(t_h: float, filas: list[tuple[float, float, float]], fecha: tuple[int, int, int]) -> float:
    """t_h = horas UT desde las 22:00 del día de partida; interpolación lineal de AR y Dec entre filas de 2 h."""
    i = max(0, min(int(t_h // 2), len(filas) - 2))
    f = (t_h - 2 * i) / 2.0
    ra = filas[i][1] + (filas[i + 1][1] - filas[i][1]) * f
    de = filas[i][2] + (filas[i + 1][2] - filas[i][2]) * f
    y, m, d = fecha
    return altaz_j2000(ra * 15.0, de, LAT, LON, jd_utc(y, m, d, 22.0) + t_h / 24.0)[0]


def analizar(nombre: str) -> dict:
    fecha, filas = NOCHES[nombre]
    dusk, dawn = crepusculos(*fecha)
    sin_luna = 0
    total = 0
    for minuto in range(int(dusk * 60), int(dawn * 60)):
        t = minuto / 60.0 - 22.0                      # horas desde las 22:00 UT
        if 0.0 <= t <= 12.0:
            total += 1
            if altura_luna(t, filas, fecha) < 0.0:
                sin_luna += 1
    ilum = sum(f[0] for f in filas) / len(filas)
    return {"dusk": dusk, "dawn": dawn, "noche_h": (dawn - dusk), "sin_luna_h": sin_luna / 60.0, "fase_media": ilum}


def pruebas() -> None:
    pruebas_biblioteca()
    for nombre, (ref_d, ref_a) in REF_CREPUSCULO.items():
        d, a = crepusculos(*NOCHES[nombre][0])
        assert abs(d - ref_d) * 60 < 6 and abs(a - ref_a) * 60 < 6, (nombre, d, a, ref_d, ref_a)
    ll, nu = analizar("llena (5-6 nov 2025)"), analizar("nueva (20-21 nov 2025)")
    assert nu["sin_luna_h"] > ll["sin_luna_h"]            # una noche de Luna nueva tiene más horas sin Luna


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    for nombre in NOCHES:
        r = analizar(nombre)
        print(f"{nombre}: noche astronomica {r['dusk'] % 24:05.2f}-{r['dawn'] % 24:05.2f} UT ({r['noche_h']:.2f} h) | "
              f"horas sin Luna sobre el horizonte {r['sin_luna_h']:.2f} h | fase media {r['fase_media']:.2f} %")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
