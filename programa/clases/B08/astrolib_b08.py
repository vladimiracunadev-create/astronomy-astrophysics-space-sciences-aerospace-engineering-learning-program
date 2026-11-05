#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Biblioteca mínima del bloque B08 (observación del cielo). Solo biblioteca estándar.

Procedencia: las fórmulas son aproximaciones de baja precisión de uso común
(tiempo sidéreo medio de Greenwich con coeficientes IAU 1982, posición aparente
del Sol con series de pocos términos, precesión rigurosa de J2000 a la fecha).
Dominio de validez: años 1950-2050; precisión objetivo ~0,02 grados en posiciones
y ~1 s en tiempo sidéreo. NO sustituye una efeméride oficial.
Referencia independiente de las pruebas: astropy 8.0.2 / pyerfa 2.0.1.5 con numpy 2.5.4,
ejecutado el 2026-11-05; los valores se copiaron como constantes (no se importa astropy).
Convenciones: ángulos en grados; longitud este positiva; latitud sur negativa;
acimut medido desde el norte hacia el este; tiempo UT1~UTC (error < 1 s, despreciable aquí).
"""
from __future__ import annotations

import math
import sys

D2R = math.pi / 180.0


def jd_utc(y: int, m: int, d: int, h: float = 0.0, mi: float = 0.0, s: float = 0.0) -> float:
    """Día juliano de una fecha gregoriana UTC."""
    if m <= 2:
        y, m = y - 1, m + 12
    a = y // 100
    b = 2 - a + a // 4
    jd0 = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + d + b - 1524.5
    return jd0 + (h + mi / 60.0 + s / 3600.0) / 24.0


def gmst_deg(jd: float) -> float:
    """Tiempo sidéreo medio de Greenwich, en grados."""
    t = (jd - 2451545.0) / 36525.0
    g = 280.46061837 + 360.98564736629 * (jd - 2451545.0) + 0.000387933 * t * t - t ** 3 / 38710000.0
    return g % 360.0


def lst_deg(jd: float, lon_este: float) -> float:
    return (gmst_deg(jd) + lon_este) % 360.0


def sun_radec(jd: float) -> tuple[float, float, float]:
    """Ascensión recta y declinación aparentes de la fecha (grados) y distancia (UA)."""
    t = (jd - 2451545.0) / 36525.0
    l0 = 280.46646 + 36000.76983 * t + 0.0003032 * t * t
    m = (357.52911 + 35999.05029 * t - 0.0001537 * t * t) * D2R
    e = 0.016708634 - 0.000042037 * t
    c = ((1.914602 - 0.004817 * t) * math.sin(m) + (0.019993 - 0.000101 * t) * math.sin(2 * m)
         + 0.000289 * math.sin(3 * m))
    nu = m + c * D2R
    r = 1.000001018 * (1 - e * e) / (1 + e * math.cos(nu))
    om = (125.04 - 1934.136 * t) * D2R
    lam = (l0 + c - 0.00569 - 0.00478 * math.sin(om)) * D2R
    eps = (23.439291 - 0.0130042 * t + 0.00256 * math.cos(om)) * D2R
    ra = math.atan2(math.cos(eps) * math.sin(lam), math.cos(lam)) / D2R % 360.0
    dec = math.asin(math.sin(eps) * math.sin(lam)) / D2R
    return ra, dec, r


def precesion_j2000(ra: float, dec: float, jd: float) -> tuple[float, float]:
    """Lleva coordenadas medias J2000 al equinoccio medio de la fecha (precesión rigurosa)."""
    t = (jd - 2451545.0) / 36525.0
    zeta = (2306.2181 * t + 0.30188 * t * t + 0.017998 * t ** 3) / 3600.0 * D2R
    z = (2306.2181 * t + 1.09468 * t * t + 0.018203 * t ** 3) / 3600.0 * D2R
    th = (2004.3109 * t - 0.42665 * t * t - 0.041833 * t ** 3) / 3600.0 * D2R
    a, d = ra * D2R, dec * D2R
    aa = math.cos(d) * math.sin(a + zeta)
    bb = math.cos(th) * math.cos(d) * math.cos(a + zeta) - math.sin(th) * math.sin(d)
    cc = math.sin(th) * math.cos(d) * math.cos(a + zeta) + math.cos(th) * math.sin(d)
    return (math.atan2(aa, bb) + z) / D2R % 360.0, math.asin(max(-1.0, min(1.0, cc))) / D2R


def altaz(ra: float, dec: float, lat: float, lst: float) -> tuple[float, float]:
    """Altura y acimut (desde el norte, hacia el este) de coordenadas DE LA FECHA."""
    h = (lst - ra) * D2R
    d, f = dec * D2R, lat * D2R
    sin_alt = math.sin(d) * math.sin(f) + math.cos(d) * math.cos(f) * math.cos(h)
    alt = math.asin(max(-1.0, min(1.0, sin_alt)))
    az = math.atan2(-math.cos(d) * math.sin(h), math.sin(d) * math.cos(f) - math.cos(d) * math.sin(f) * math.cos(h))
    return alt / D2R, az / D2R % 360.0


def altaz_j2000(ra: float, dec: float, lat: float, lon: float, jd: float) -> tuple[float, float]:
    ra_f, dec_f = precesion_j2000(ra, dec, jd)
    return altaz(ra_f, dec_f, lat, lst_deg(jd, lon))


def separacion(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    """Separación angular (grados) por la fórmula de Vincenty (estable a ángulos pequeños)."""
    a1, d1, a2, d2 = ra1 * D2R, dec1 * D2R, ra2 * D2R, dec2 * D2R
    dl = a2 - a1
    num = math.hypot(math.cos(d2) * math.sin(dl), math.cos(d1) * math.sin(d2) - math.sin(d1) * math.cos(d2) * math.cos(dl))
    den = math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(dl)
    return math.atan2(num, den) / D2R


def hms_a_grados(h: float, m: float = 0.0, s: float = 0.0) -> float:
    return (h + m / 60.0 + s / 3600.0) * 15.0


def grados_a_hms(g: float) -> tuple[int, int, float]:
    h = (g % 360.0) / 15.0
    hh = int(h)
    mm = int((h - hh) * 60)
    return hh, mm, ((h - hh) * 60 - mm) * 60


# --- Referencias independientes (astropy 8.0.2; copiadas) ---
REF_GMST = {  # (jd) -> GMST [deg]
    2460984.5: 44.47932, 2460984.625: 89.60252, 2460755.0: 358.27305,
    2461031.0: 270.31187, 2461213.25: 179.94583,
}
REF_SOL = {  # jd -> (ra, dec) aparentes de la fecha [deg]
    2460984.5: (220.3764, -15.687), 2460984.625: (220.5004, -15.725),
    2460755.0: (0.1131, 0.0488), 2461031.0: (269.8588, -23.4382), 2461213.25: (90.4157, 23.4374),
}
# (ra_J2000, dec_J2000, jd, alt, az) para lat -30,0 y lon -70,7
REF_ALTAZ = [
    (186.65, -63.10, 2460984.625, 3.7207, 174.6605),
    (186.65, -63.10, 2460984.8333333335, 25.2626, 150.1822),
    (279.23, 38.78, 2460984.625, -25.1039, 301.9112),
    (0.0, 0.0, 2460984.625, 55.0521, 326.2292),
    (101.287, -16.716, 2460984.625, 14.4614, 101.2189),
    (101.287, -16.716, 2460984.8333333335, 75.0823, 28.9261),
]

REF_PRECESION = [  # (ra, dec) J2000 -> (ra, dec) medios de 2025-11-05 00:00 UT
    ((0.0, 0.0), (0.33112768, 0.14386963)),
    ((186.65, -63.10), (187.01497235, -63.24284829)),
    ((101.287, -16.716), (101.57573915, -16.74451602)),
]


def pruebas_biblioteca() -> None:
    assert abs(jd_utc(2025, 11, 5) - 2460984.5) < 1e-9
    assert abs(jd_utc(2000, 1, 1, 12) - 2451545.0) < 1e-9
    for jd, ref in REF_GMST.items():
        d = abs((gmst_deg(jd) - ref + 180) % 360 - 180)
        assert d * 240 < 1.0, (jd, d * 240)          # < 1 s de tiempo (1 grado = 4 min)
    for jd, (ra, dec) in REF_SOL.items():
        r, dd, _ = sun_radec(jd)
        assert abs((r - ra + 180) % 360 - 180) < 0.02 and abs(dd - dec) < 0.02, (jd, r, dd)
    for ra, dec, jd, alt, az in REF_ALTAZ:
        a, z = altaz_j2000(ra, dec, -30.0, -70.7, jd)
        assert abs(a - alt) < 0.03, (ra, dec, jd, a, alt)
        if abs(alt) < 85:
            assert abs((z - az + 180) % 360 - 180) < 0.05, (ra, dec, jd, z, az)
    for (r0, d0), (r1, d1) in REF_PRECESION:
        r, d = precesion_j2000(r0, d0, 2460984.5)
        assert abs(r - r1) < 0.002 and abs(d - d1) < 0.002, (r0, d0, r, d)
    assert abs(separacion(0, 90, 123, -90) - 180) < 1e-9          # polo a polo
    assert abs(separacion(0, 0, 15, 0) - 15) < 1e-9               # 1 h de AR en el ecuador
    assert abs(hms_a_grados(6) - 90) < 1e-12


if __name__ == "__main__":
    pruebas_biblioteca()
    print(f"python {sys.version.split()[0]} | pruebas de la biblioteca OK")
