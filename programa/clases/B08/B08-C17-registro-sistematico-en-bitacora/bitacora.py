#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C17: validar una bitácora de observación.

Datos: filas de EJEMPLO SINTÉTICAS (inventadas para practicar; NO son observaciones). Una de ellas incluye una altura de la Luna que se
contrasta con la altura CALCULADA por astrolib_b08 a partir de posiciones de NASA SVS 5415 (JPL DE421, mooninfo_2025.txt, consultada
2026-11-05). Modelo: reglas de validación (formato ISO 8601 en UT, rangos físicos, procedencia obligatoria) y coherencia con un cálculo.
Dominio: bitácoras tabulares CSV. Tolerancia de la coherencia: 5 grados en altura (estimación a mano).
Prueba independiente: filas válidas e inválidas construidas a propósito; el validador debe aceptar las primeras y rechazar cada
inválida con un mensaje concreto. No se importa ningún paquete.
"""
from __future__ import annotations

import csv
import io
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import altaz_j2000, jd_utc, pruebas_biblioteca  # noqa: E402

CAMPOS = ["fecha_hora_utc", "lat", "lon", "objeto", "metodo", "instrumento", "seeing_1a5", "nubosidad_pct",
          "luna_pct", "alt_estimada", "procedencia", "observador", "notas"]
METODOS = {"ojo", "binoculares", "telescopio", "datos"}
PROCEDENCIAS = {"observado", "estimado", "calculado", "sintetico", "simulado"}

# Luna (NASA SVS 5415, J2000): fecha UT -> (RA h, Dec grados)
LUNA = {"2025-11-05T00:00": (2.0630, 16.5927), "2025-11-05T04:00": (2.2260, 17.5864)}
LAT, LON = -30.0, -70.7

CSV_EJEMPLO = """fecha_hora_utc,lat,lon,objeto,metodo,instrumento,seeing_1a5,nubosidad_pct,luna_pct,alt_estimada,procedencia,observador,notas
2025-11-05T00:00,-30.0,-70.7,Luna,ojo,ninguno,3,10,99.4,20,sintetico,A,fila de ejemplo coherente
2025-11-05T04:00,-30.0,-70.7,Luna,ojo,ninguno,3,10,99.7,70,sintetico,A,altura estimada incoherente
2025-11-05T25:00,-30.0,-70.7,Luna,ojo,ninguno,3,10,99.4,20,sintetico,A,hora inexistente
2025-11-05T00:00,-130.0,-70.7,Luna,ojo,ninguno,3,10,99.4,20,sintetico,A,latitud imposible
2025-11-05T00:00,-30.0,-70.7,Luna,satelite,ninguno,3,10,99.4,20,sintetico,A,metodo no permitido
2025-11-05T00:00,-30.0,-70.7,Luna,ojo,ninguno,3,10,99.4,20,,A,sin procedencia
"""


def validar_fila(f: dict) -> list[str]:
    errores: list[str] = []
    try:
        t = datetime.strptime(f["fecha_hora_utc"], "%Y-%m-%dT%H:%M")
    except ValueError:
        errores.append("fecha_hora_utc no es ISO 8601 UT valido (AAAA-MM-DDTHH:MM)")
        t = None
    for campo, lo, hi in (("lat", -90.0, 90.0), ("lon", -180.0, 180.0), ("seeing_1a5", 1, 5), ("nubosidad_pct", 0, 100), ("luna_pct", 0, 100)):
        try:
            v = float(f[campo])
            if not lo <= v <= hi:
                errores.append(f"{campo} fuera de rango [{lo}, {hi}]")
        except (ValueError, KeyError):
            errores.append(f"{campo} no es numerico")
    if f.get("metodo") not in METODOS:
        errores.append(f"metodo debe ser uno de {sorted(METODOS)}")
    if f.get("procedencia") not in PROCEDENCIAS:
        errores.append(f"procedencia obligatoria, una de {sorted(PROCEDENCIAS)}")
    if t is not None and f.get("objeto") == "Luna" and not errores:
        clave = f["fecha_hora_utc"]
        if clave in LUNA:
            ra, dec = LUNA[clave]
            calc, _ = altaz_j2000(ra * 15, dec, LAT, LON, jd_utc(t.year, t.month, t.day, t.hour, t.minute))
            if abs(float(f["alt_estimada"]) - calc) > 5.0:
                errores.append(f"altura estimada {f['alt_estimada']} difiere de la calculada {calc:.1f} en mas de 5 grados")
    return errores


def pruebas() -> None:
    pruebas_biblioteca()
    filas = list(csv.DictReader(io.StringIO(CSV_EJEMPLO)))
    assert list(filas[0].keys()) == CAMPOS
    assert validar_fila(filas[0]) == []
    for i, esperado in zip(range(1, 6), ["difiere", "ISO 8601", "lat fuera", "metodo", "procedencia"]):
        e = validar_fila(filas[i])
        assert e and any(esperado in m for m in e), (i, e)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    for i, f in enumerate(csv.DictReader(io.StringIO(CSV_EJEMPLO)), 1):
        e = validar_fila(f)
        print(f"fila {i} ({f['notas']}): {'VALIDA' if not e else 'RECHAZADA: ' + '; '.join(e)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
