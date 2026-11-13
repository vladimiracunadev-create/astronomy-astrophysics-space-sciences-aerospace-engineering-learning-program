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
SALIDA_RST = SALIDA.with_name("referencia_usno_salidas.json")
LUGARES = [("Santiago", -33.45, -70.67), ("Greenwich", 51.4769, 0.0), ("Quito", -0.18, -78.5), ("Tokio", 35.68, 139.69), ("Reikiavik", 64.15, -21.94), ("Sídney", -33.87, 151.2)]
FECHAS = ["2027-03-20", "2027-06-21", "2028-12-21", "2030-09-23", "2035-01-15", "2040-07-04", "2045-05-10", "2049-11-30"]


def pedir(ruta: str) -> dict:
    for i in range(5):
        try:
            with urllib.request.urlopen("https://aa.usno.navy.mil/api/" + ruta, timeout=60) as r:
                return json.load(r)
        except Exception:  # noqa: BLE001
            time.sleep(2 * (i + 1))
    raise RuntimeError(ruta)


def salidas() -> None:
    out = []
    for nom, lat, lon in LUGARES:
        for f in FECHAS:
            d = pedir(f"rstt/oneday?date={f}&coords={lat},{lon}&tz=0")["properties"]["data"]
            ev = lambda lista: [[e["phen"], e["time"]] for e in (lista or []) if e["phen"] in ("Rise", "Set")]
            out.append({"lugar": nom, "lat": lat, "lon": lon, "fecha": f, "sol": ev(d.get("sundata")), "luna": ev(d.get("moondata"))})
            time.sleep(0.3)
    SALIDA_RST.write_text(json.dumps({"fuente": "U.S. Naval Observatory, Astronomical Applications API v4 (rstt/oneday, tz=0); horas UT en minutos", "dias": out}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(len(out), "días de salidas y puestas")


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
salidas()
