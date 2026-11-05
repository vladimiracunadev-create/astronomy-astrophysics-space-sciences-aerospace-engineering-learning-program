#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C03: leer, convertir y comparar coordenadas ecuatoriales.

Datos OBSERVADOS-CALCULADOS: posiciones de la Luna (RA en horas, Dec en grados, J2000) copiadas de
NASA SVS 5415 «Moon Phase and Libration, 2025» (efeméride JPL DE421), archivo mooninfo_2025.txt,
consultado el 2026-11-05. Los efectos de precesión se calculan (SIMULADOS) con astrolib_b08.
Modelo: esfera celeste, equinoccio medio J2000 y de la fecha. Dominio: 1950-2050.
Tolerancia: separación angular a 1e-9 grados en casos analíticos; precesión a 0,002 grados contra astropy.
Prueba independiente: casos analíticos (polo a polo; 1 h de AR = 15 grados) y valor de astropy copiado.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import grados_a_hms, hms_a_grados, precesion_j2000, pruebas_biblioteca, separacion  # noqa: E402

# (fecha UT, RA [h], Dec [grados]) copiados de mooninfo_2025.txt (columnas RA y Dec)
LUNA = [
    ("2025-11-04 20:00", 1.9020, 15.5725),
    ("2025-11-05 00:00", 2.0630, 16.5927),
    ("2025-11-05 04:00", 2.2260, 17.5864),
    ("2025-11-05 08:00", 2.3911, 18.5510),
]


def main() -> int:
    pruebas_biblioteca()
    assert abs(separacion(0, 0, 15, 0) - 15.0) < 1e-9
    assert abs(hms_a_grados(1) - 15.0) < 1e-12
    h, m, s = grados_a_hms(30.0)
    assert (h, m) == (2, 0) and abs(s) < 1e-9
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Luna, NASA SVS 5415 (J2000):")
    prev = None
    for fecha, ra_h, dec in LUNA:
        hh, mm, ss = grados_a_hms(ra_h * 15)
        linea = f"{fecha} UT  RA {hh:02d}h{mm:02d}m{ss:04.1f}s  Dec {dec:+.4f}"
        if prev:
            linea += f"  | desplazamiento en 4 h: {separacion(prev[0]*15, prev[1], ra_h*15, dec):.3f} grados"
        print(linea)
        prev = (ra_h, dec)
    ra, dec = LUNA[1][1] * 15, LUNA[1][2]
    ra_f, dec_f = precesion_j2000(ra, dec, 2460984.5)
    print(f"Precesion J2000 -> fecha para la Luna del 5-nov-2025 00 UT: dRA={ (ra_f-ra)*3600:.0f}\" dDec={(dec_f-dec)*3600:.0f}\" "
          f"(separacion {separacion(ra, dec, ra_f, dec_f):.3f} grados)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
