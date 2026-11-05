#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C18: de un conteo de meteoros a una tasa horaria comparable (ZHR simplificada).

Definición (IMO, glosario, consultada 2026-11-05): ZHR = meteoros por hora que vería un observador con magnitud límite 6,5 y el
radiante en el cenit. Modelo (SIMULADO, deducido aquí de esa definición; NO es la fórmula publicada completa de la IMO):
ZHR = N * r^(6,5 - lm) / (T * sen(h) * (1 - nubes)), con N meteoros contados en T horas, lm magnitud límite, r índice de población
(valor de EJEMPLO, 2,5) y h altura del radiante. Supuestos: radiante puntual; válido para h >= 25 grados; r constante.
Radiante de EJEMPLO SINTÉTICO (ar 7,5 h; dec +30): NO corresponde a una lluvia real, cuyos radiantes deben tomarse de una fuente
(la página del calendario de la IMO consultada no los lista). Datos de conteo: SINTÉTICOS. Sol y tiempo sidéreo: astrolib_b08.
Prueba independiente: casos analíticos (lm = 6,5 y h = 90 -> ZHR = N/T; lm 5,5 con r = 2,5 -> x 2,5; h = 30 -> x 2) y la altura
máxima del radiante, 90 - |lat - dec|, calculada por dos vías.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import D2R, altaz, altaz_j2000, jd_utc, lst_deg, pruebas_biblioteca, sun_radec  # noqa: E402

LAT, LON = -30.0, -70.7
RADIANTE_EJEMPLO = (7.5 * 15.0, 30.0)     # SINTÉTICO (ar grados, dec grados)
R_EJEMPLO = 2.5


def zhr(n: float, t_h: float, lm: float, h_deg: float, r: float = R_EJEMPLO, nubes: float = 0.0) -> float:
    if h_deg < 25.0:
        raise ValueError("altura del radiante < 25 grados: el modelo simplificado no es válido")
    return n * r ** (6.5 - lm) / (t_h * math.sin(h_deg * D2R) * (1.0 - nubes))


def altura_radiante(y: int, m: int, d: int, h_ut: float) -> float:
    return altaz_j2000(RADIANTE_EJEMPLO[0], RADIANTE_EJEMPLO[1], LAT, LON, jd_utc(y, m, d, h_ut))[0]


def altura_sol(y: int, m: int, d: int, h_ut: float) -> float:
    jd = jd_utc(y, m, d, h_ut)
    ra, dec, _ = sun_radec(jd)
    return altaz(ra, dec, LAT, lst_deg(jd, LON))[0]


def pruebas() -> None:
    pruebas_biblioteca()
    assert abs(zhr(10, 1.0, 6.5, 90.0) - 10.0) < 1e-12
    assert abs(zhr(10, 1.0, 5.5, 90.0) - 25.0) < 1e-9
    assert abs(zhr(10, 1.0, 6.5, 30.0) - 20.0) < 1e-9
    assert abs(zhr(10, 1.0, 6.5, 90.0, nubes=0.5) - 20.0) < 1e-9
    maxima = max(altura_radiante(2026, 12, 13, h / 4.0) for h in range(0, 24 * 4))
    assert abs(maxima - (90.0 - abs(LAT - RADIANTE_EJEMPLO[1]))) < 0.5, maxima        # 30 grados en el Elqui
    try:
        zhr(1, 1, 6.5, 10.0)
    except ValueError:
        pass
    else:
        raise AssertionError("debía rechazar radiante bajo")


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Altura del radiante SINTETICO (ar 7,5 h, dec +30) en lat -30, 14 de diciembre de 2026, horas UT (SIMULADO):")
    for t_ut in range(0, 10):
        a = altura_radiante(2026, 12, 14, t_ut)
        noche = altura_sol(2026, 12, 14, t_ut) < -18.0
        print(f"  {t_ut:02d}:00 UT (14-dic)  altura {a:6.1f}  sen h = {max(math.sin(a * D2R), 0):.2f}  noche astronomica: {'si' if noche else 'no'}")
    print("Ejemplo SINTETICO: 18 meteoros en 1,5 h con lm 5,8 y radiante a 30 grados, r = 2,5, sin nubes")
    print(f"  ZHR = {zhr(18, 1.5, 5.8, 30.0):.1f}; con 20 % de nubes: {zhr(18, 1.5, 5.8, 30.0, nubes=0.2):.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
