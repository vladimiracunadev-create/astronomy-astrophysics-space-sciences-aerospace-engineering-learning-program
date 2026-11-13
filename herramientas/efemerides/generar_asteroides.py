# SPDX-License-Identifier: Apache-2.0
"""Genera simuladores/datos/asteroides.json con los elementos orbitales osculadores de ~2 500 asteroides (JPL Small-Body Database)
y simuladores/pruebas/verificacion_asteroides.json con posiciones de Horizons para medir el error del modelo de dos cuerpos.

Selección: asteroides del cinturón principal (MBA, IMB, OMB, MCA) con H <= 10,3; troyanos de Júpiter (TJN) con H <= 10,6; Hildas (HYA)
con H <= 12; y asteroides cercanos a la Tierra (IEO, ATE, APO, AMO) con H <= 17,5 (aprox. 1 km o más).
Elementos: eclíptica y equinoccio J2000, época osculadora de JPL (JD TDB), UA y grados.
Uso: python herramientas/efemerides/generar_asteroides.py   (necesita red y numpy)
"""
from __future__ import annotations

import json
import math
import random
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import horizons as H  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
GRUPOS = [("MBA,IMB,OMB,MCA", 10.3), ("TJN", 10.6), ("HYA", 12.0), ("IEO,ATE,APO,AMO", 17.5)]
CAMPOS = "spkid,full_name,pdes,name,class,a,e,i,om,w,ma,epoch,H,diameter"
EPOCAS_VERIF = [2461406.5 + 365.25 * 3, 2461406.5 + 365.25 * 12, 2461406.5 + 365.25 * 23.9]  # 2030, 2039 y 2050


def consulta(clases: str, hmax: float) -> list[list]:
    p = {"fields": CAMPOS, "sb-kind": "a", "sb-class": clases, "sb-cdata": json.dumps({"AND": [f"H|LT|{hmax}"]}), "full-prec": "true"}
    with urllib.request.urlopen("https://ssd-api.jpl.nasa.gov/sbdb_query.api?" + urllib.parse.urlencode(p), timeout=180) as r:
        return json.load(r)["data"]


def num(x, d=6):
    return None if x in (None, "") else round(float(x), d)


def main() -> None:
    filas, vistos = [], set()
    for clases, hmax in GRUPOS:
        for r in consulta(clases, hmax):
            if r[0] in vistos or any(v in (None, "") for v in r[5:12]):
                continue
            vistos.add(r[0])
            nombre = (r[3] or r[2] or r[1]).strip()
            filas.append([r[0], r[2].strip(), nombre, r[4], num(r[5], 7), num(r[6], 7), num(r[7], 5), num(r[8], 5), num(r[9], 5), num(r[10], 5), num(r[11], 1), num(r[12], 2), num(r[13], 1)])
    filas.sort(key=lambda f: (f[11] if f[11] is not None else 99))
    (RAIZ / "simuladores" / "datos" / "asteroides.json").write_text(json.dumps({
        "fuente": "NASA/JPL Small-Body Database (SBDB Query API)", "marco": "Eclíptica y equinoccio J2000, heliocéntrico", "unidades": "UA y grados; época en JD TDB",
        "columnas": ["spkid", "designacion", "nombre", "clase", "a", "e", "i", "om", "w", "ma", "epoca", "H", "diametro_km"], "asteroides": filas},
        ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(len(filas), "asteroides")
    # verificación: Horizons (heliocéntrico) en tres épocas para una muestra con semilla fija
    rng = random.Random(2027)
    muestra = rng.sample(filas, 18)  # Horizons tarda ~1 min por cuerpo pequeño
    verif = []
    for f in muestra:
        try:
            pos = H.vectores_lista(str(f[0]), "500@10", EPOCAS_VERIF, tabla="1")
        except Exception as e:  # noqa: BLE001
            print("sin datos", f[2], str(e)[:80]); continue
        verif.append({"spkid": f[0], "nombre": f[2], "clase": f[3], "epocas": [[p[0], p[1], p[2], p[3]] for p in pos]})
    (RAIZ / "simuladores" / "pruebas" / "verificacion_asteroides.json").write_text(json.dumps({"fuente": "NASA/JPL Horizons, vectores heliocéntricos eclípticos J2000 [km]", "asteroides": verif}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(len(verif), "asteroides de verificación")


main()
