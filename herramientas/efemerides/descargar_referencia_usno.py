# SPDX-License-Identifier: Apache-2.0
"""Descarga del U.S. Naval Observatory (API pública de Astronomical Applications) las estaciones, ápsides y fases lunares
de 2027 a 2050 y las guarda en simuladores/pruebas/referencia_usno.json. Sirven como contraste independiente del cálculo propio
(`pruebas/ejecutar.mjs`), que se ejecuta después sin red. Uso: python herramientas/efemerides/descargar_referencia_usno.py
"""
import json
import time
import urllib.request
from pathlib import Path

SALIDA = Path(__file__).resolve().parents[2] / "simuladores" / "pruebas" / "referencia_usno.json"


def pedir(ruta: str) -> dict:
    for i in range(5):
        try:
            with urllib.request.urlopen("https://aa.usno.navy.mil/api/" + ruta, timeout=60) as r:
                return json.load(r)
        except Exception:  # noqa: BLE001
            time.sleep(2 * (i + 1))
    raise RuntimeError(ruta)


def main() -> None:
    est, fases = [], []
    for a in range(2027, 2051):
        for e in pedir(f"seasons?year={a}")["data"]:
            est.append([f"{e['year']:04d}-{e['month']:02d}-{e['day']:02d}", e["time"], e["phenom"]])
        for e in pedir(f"moon/phases/year?year={a}")["phasedata"]:
            fases.append([f"{e['year']:04d}-{e['month']:02d}-{e['day']:02d}", e["time"], e["phase"]])
        time.sleep(0.4)
    SALIDA.write_text(json.dumps({"fuente": "U.S. Naval Observatory, Astronomical Applications API v4 (seasons, moon/phases/year); horas UT1 ~ UTC en minutos",
                                  "estaciones": est, "fases": fases}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(len(est), "estaciones/ápsides;", len(fases), "fases")


main()
