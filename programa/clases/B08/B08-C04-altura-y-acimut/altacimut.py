#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C04: de RA/Dec a altura y acimut desde el valle del Elqui.

Datos: posiciones de la Luna (J2000) de NASA SVS 5415 (efeméride DE421), consultadas el
2026-11-05; el lugar (lat -30,0, lon -70,7) está redondeado, no medido. Altura y acimut son SIMULADOS
(calculados). Modelo: tiempo sidéreo medio + precesión; sin refracción, nutación ni paralaje lunar
(la paralaje horizontal de la Luna, ~1 grado, desplaza su altura aparente hasta ese valor: no se corrige).
Tolerancia: 0,03 grados en altura contra astropy (copiado). Prueba independiente: (1) valor de astropy
8.0.2 para la fila de las 03:00 UT; (2) el tránsito por el meridiano da altura 90-|lat-dec|.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import altaz, altaz_j2000, jd_utc, lst_deg, precesion_j2000, pruebas_biblioteca  # noqa: E402

LAT, LON = -30.0, -70.7
# (fecha UT, hora UT decimal, día, RA [h], Dec) copiados de mooninfo_2025.txt
LUNA = [
    (4, 20, 1.9020, 15.5725), (4, 22, 1.9822, 16.0858), (5, 0, 2.0630, 16.5927), (5, 2, 2.1443, 17.0931),
    (5, 4, 2.2260, 17.5864), (5, 6, 2.3083, 18.0725), (5, 8, 2.3911, 18.5510), (5, 10, 2.4744, 19.0216),
]


def pruebas() -> None:
    pruebas_biblioteca()
    alt, az = altaz_j2000(2.1851 * 15, 17.3406, LAT, LON, jd_utc(2025, 11, 5, 3))
    assert abs(alt - 40.59285) < 0.03 and abs(az - 17.99260) < 0.05, (alt, az)   # astropy 8.0.2
    ra_f, dec_f = precesion_j2000(100.0, -20.0, jd_utc(2025, 11, 5))
    lst = ra_f                                                # ángulo horario 0 -> en el meridiano
    alt_m, az_m = altaz(ra_f, dec_f, LAT, lst)
    assert abs(alt_m - (90.0 - abs(LAT - dec_f))) < 1e-9
    assert min(az_m, 360.0 - az_m) < 1e-6          # sobre el meridiano, al norte (dec > lat)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Luna vista desde lat -30,0 lon -70,7 (alt/az SIMULADOS; RA/Dec: NASA SVS 5415)")
    for dia, hora, ra_h, dec in LUNA:
        jd = jd_utc(2025, 11, dia, hora)
        alt, az = altaz_j2000(ra_h * 15, dec, LAT, LON, jd)
        lst = lst_deg(jd, LON) / 15
        print(f"2025-11-{dia:02d} {hora:02d}:00 UT  TSL {lst:5.2f} h  alt {alt:6.1f}  az {az:6.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
