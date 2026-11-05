#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C05: tiempo sidéreo, día sidéreo y ecuación del tiempo.

Datos: duración del día sidéreo de la NASA Earth Fact Sheet (23,9345 h; consultada 2026-11-05) y
tiempos de tránsito solar SIMULADOS (calculados) para lon -70,7 (redondeada). Modelo: GMST con
coeficientes IAU 1982 y Sol de baja precisión (astrolib_b08). Dominio: 1950-2050. Tolerancias:
0,0001 h en el día sidéreo; 0,5 min en el tránsito solar.
Prueba independiente: tránsitos solares calculados con astropy 8.0.2 (valores copiados) y el día
sidéreo publicado por la NASA.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import jd_utc, lst_deg, pruebas_biblioteca, sun_radec  # noqa: E402

LON = -70.7
DIA_SIDEREO_NASA_H = 23.9345                      # NASA Earth Fact Sheet (act. 15-nov-2024)
# (año, mes, día) -> hora UT del tránsito solar (astropy 8.0.2, lon -70,7)
REF_TRANSITO = {(2025, 2, 11): 16.9498, (2025, 5, 14): 16.6522, (2025, 7, 26): 16.8227, (2025, 11, 5): 16.4401}


def dia_sidereo_h() -> float:
    """Duración del día sidéreo a partir de la tasa del GMST (grados por día solar medio)."""
    tasa = (lst_deg(2451546.0, 0) - lst_deg(2451545.0, 0)) % 360.0   # exceso sobre 360 grados en un día
    return 24.0 * 360.0 / (360.0 + tasa)


def transito_solar_ut(y: int, m: int, d: int) -> float:
    """Hora UT (decimal) en que el ángulo horario del Sol cruza 0 en LON; barrido de 1 min y refinado lineal."""
    base = jd_utc(y, m, d, 12.0)
    prev = None
    for minuto in range(0, 12 * 60 + 1):
        jd = base + minuto / 1440.0
        ra, _, _ = sun_radec(jd)
        h = (lst_deg(jd, LON) - ra + 180.0) % 360.0 - 180.0
        if prev is not None and prev[0] < 0 <= h:
            frac = -prev[0] / (h - prev[0])
            return 12.0 + (prev[1] + frac) / 60.0
        prev = (h, minuto)
    raise RuntimeError("sin tránsito")


def pruebas() -> None:
    pruebas_biblioteca()
    assert abs(dia_sidereo_h() - DIA_SIDEREO_NASA_H) < 1e-4, dia_sidereo_h()
    for (y, m, d), ref in REF_TRANSITO.items():
        t = transito_solar_ut(y, m, d)
        assert abs(t - ref) * 60 < 0.5, (y, m, d, t, ref)


def hhmm(h: float) -> str:
    return f"{int(h):02d}:{int((h % 1) * 60):02d}:{int(((h * 60) % 1) * 60):02d}"


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    ds = dia_sidereo_h()
    print(f"Dia sidereo (modelo): {ds:.5f} h = {hhmm(ds)} | NASA: {DIA_SIDEREO_NASA_H} h")
    print(f"Dia solar - dia sidereo: {(24 - ds) * 60:.4f} min = {(24 - ds) * 3600:.1f} s")
    print(f"Adelanto del cielo en 30 dias solares: {(24 - ds) * 30:.3f} h")
    print("Transito solar en lon -70,7 (media = 16:42:48 UT). SIMULADO")
    for y, m, d in sorted(REF_TRANSITO):
        t = transito_solar_ut(y, m, d)
        print(f"{y}-{m:02d}-{d:02d}: {hhmm(t)} UT | ecuacion del tiempo {(16.7133333 - t) * 60:+.1f} min")
    jd = jd_utc(2025, 11, 5, 0)
    print(f"TSL en lon -70,7 el 2025-11-05 00:00 UT: {lst_deg(jd, LON) / 15:.3f} h")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
