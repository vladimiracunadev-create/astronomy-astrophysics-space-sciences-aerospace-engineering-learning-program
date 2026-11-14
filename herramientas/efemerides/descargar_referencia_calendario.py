# SPDX-License-Identifier: Apache-2.0
"""Descarga de JPL Horizons (tabla OBSERVER, centro geocéntrico) la longitud y latitud eclípticas aparentes y la elongación al Sol de los
siete planetas en 24 épocas por planeta (semilla fija) entre 2027 y 2050, y las guarda en simuladores/pruebas/referencia_calendario.json.
Sirven de contraste independiente del cálculo propio (`pruebas/ejecutar.mjs`), que se ejecuta después sin red.
Uso: python herramientas/efemerides/descargar_referencia_calendario.py
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import horizons as H  # noqa: E402

SALIDA = Path(__file__).resolve().parents[2] / "simuladores" / "pruebas" / "referencia_calendario.json"
JD_UTC_2027, JD_UTC_2051 = 2461406.5, 2470172.5
PLANETAS = ["199", "299", "499", "599", "699", "799", "899"]


def tabla(cuerpo: str, jds: list[float]) -> list[list[float]]:
    t = H.consulta({
        "COMMAND": cuerpo, "OBJ_DATA": "NO", "MAKE_EPHEM": "YES", "EPHEM_TYPE": "OBSERVER", "CENTER": "500@399",
        "TLIST": "\n".join(f"{j:.9f}" for j in jds), "TLIST_TYPE": "JD", "TIME_TYPE": "UT", "QUANTITIES": "23,31", "CSV_FORMAT": "YES", "ANG_FORMAT": "DEG",
        "APPARENT": "AIRLESS",
    })
    if "$$SOE" not in t:
        raise RuntimeError(t[:400])
    filas = []
    for l in t.split("$$SOE")[1].split("$$EOE")[0].strip().splitlines():
        c = [x.strip() for x in l.split(",")]
        filas.append(c)
    return filas


def main() -> None:
    rng = random.Random(2027)
    out = []
    for pid in PLANETAS:
        jds = sorted(rng.uniform(JD_UTC_2027, JD_UTC_2051) for _ in range(24))
        fp = tabla(pid, jds)
        fs = tabla("10", jds)
        for j, rp, rs in zip(jds, fp, fs):
            # columnas: fecha, , , elongación S-O-T, /r, longitud, latitud
            lp, bp, el = float(rp[5]), float(rp[6]), float(rp[3])
            ls, bs = float(rs[5]), float(rs[6])
            out.append({"planeta": pid, "jdUtc": j, "lonP": lp, "latP": bp, "lonS": ls, "latS": bs, "elong": el})
    SALIDA.write_text(json.dumps({"fuente": "NASA/JPL Horizons (OBSERVER, geocéntrico 500@399, cantidades 23 y 31, posiciones aparentes), grados", "muestras": out}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(len(out), "muestras")


main()
