# SPDX-License-Identifier: Apache-2.0
"""Cliente mínimo y con caché de la API de NASA/JPL Horizons (https://ssd-api.jpl.nasa.gov/doc/horizons.html).

Sólo biblioteca estándar. Cada respuesta se guarda en `_cache/` (ignorada por git) con la huella de la consulta,
de modo que regenerar las efemérides no repite descargas y cada dato es reproducible.
"""
from __future__ import annotations

import hashlib
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

CACHE = Path(__file__).resolve().parent / "_cache"
URL = "https://ssd.jpl.nasa.gov/api/horizons.api"
JD_TDB_MENOS_JD_UTC_S = 69.184  # TT-UTC = 32.184 + 37 s (TAI-UTC vigente desde 2017); TDB-TT < 2 ms


def consulta(params: dict[str, str], reintentos: int = 6) -> str:
    p = {"format": "text", **params}
    clave = hashlib.sha256(repr(sorted(p.items())).encode()).hexdigest()[:32]
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / f"{clave}.txt"
    if f.exists():
        return f.read_text(encoding="utf-8")
    q = urllib.parse.urlencode({k: (v if k == "format" else f"'{v}'") for k, v in p.items()})
    espera = 3.0
    for i in range(reintentos):
        try:
            with urllib.request.urlopen(f"{URL}?{q}", timeout=180) as r:
                t = r.read().decode("utf-8", "replace")
            if "$$SOE" in t or "OBJ_DATA" in str(params) and params.get("MAKE_EPHEM") == "NO":
                f.write_text(t, encoding="utf-8")
                return t
            if "Number of matches" in t or "No ephemeris for target" in t or "Cannot" in t or "No matches" in t or "prior to" in t:
                f.write_text(t, encoding="utf-8")
                return t
            raise RuntimeError(t[:300])
        except Exception as e:  # red o límite de tasa: espera creciente
            if i == reintentos - 1:
                raise
            time.sleep(espera)
            espera *= 2
    raise RuntimeError("inalcanzable")


def vectores(cuerpo: str, centro: str, inicio: str, fin: str, paso: str, tabla: str = "2", obj_data: bool = False) -> tuple[str, list[list[float]]]:
    """Devuelve (cabecera, filas[JD, x, y, z, (vx, vy, vz)]) en km, km/s, eclíptica J2000, TDB."""
    t = consulta({
        "COMMAND": cuerpo, "OBJ_DATA": "YES" if obj_data else "NO", "MAKE_EPHEM": "YES", "EPHEM_TYPE": "VECTORS",
        "CENTER": centro, "START_TIME": inicio, "STOP_TIME": fin, "STEP_SIZE": paso,
        "REF_PLANE": "ECLIPTIC", "REF_SYSTEM": "ICRF", "OUT_UNITS": "KM-S", "VEC_TABLE": tabla, "CSV_FORMAT": "YES",
    })
    return t.split("$$SOE")[0], _filas(t)


def vectores_lista(cuerpo: str, centro: str, jds: list[float], tabla: str = "2") -> list[list[float]]:
    t = consulta({
        "COMMAND": cuerpo, "OBJ_DATA": "NO", "MAKE_EPHEM": "YES", "EPHEM_TYPE": "VECTORS", "CENTER": centro,
        "TLIST": "\n".join(f"{j:.9f}" for j in jds), "TLIST_TYPE": "JD", "TIME_TYPE": "TDB",
        "REF_PLANE": "ECLIPTIC", "REF_SYSTEM": "ICRF", "OUT_UNITS": "KM-S", "VEC_TABLE": tabla, "CSV_FORMAT": "YES",
    })
    return _filas(t)


def _filas(t: str) -> list[list[float]]:
    if "$$SOE" not in t:
        raise RuntimeError("sin datos: " + t[:400])
    cuerpo = t.split("$$SOE")[1].split("$$EOE")[0].strip().splitlines()
    out = []
    for l in cuerpo:
        c = [x.strip() for x in l.split(",")]
        out.append([float(c[0])] + [float(x) for x in c[2:] if x != ""])
    return out


def radio_medio(cabecera: str) -> float | None:
    """Radio medio (km) del bloque de propiedades físicas de Horizons, si lo publica."""
    m = re.search(r"(?:Vol\. mean radius|Mean radius|Radius)\s*(?:\(km\))?\s*=\s*([0-9.]+)(?:\s*\+-\s*[0-9.]+)?(?:\s*x\s*([0-9.]+))?(?:\s*x\s*([0-9.]+))?", cabecera)
    if not m:
        return None
    v = [float(x) for x in m.groups() if x]
    return round(sum(v) / len(v), 3) if len(v) > 1 and False else (round((v[0] * (v[1] if len(v) > 1 else v[0]) * (v[2] if len(v) > 2 else v[0])) ** (1 / 3), 3) if len(v) == 3 else v[0])
