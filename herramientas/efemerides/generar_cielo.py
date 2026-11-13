# SPDX-License-Identifier: Apache-2.0
"""Genera simuladores/datos/cielo.json (estrellas, nombres y figuras de constelaciones) para los simuladores de cielo.

Fuente: d3-celestial de Olaf Frohn (licencia BSD de 3 cláusulas), https://github.com/ofrohn/d3-celestial — estrellas hasta magnitud 6
derivadas de Hipparcos/Tycho (ESA), nombres propios de las estrellas y figuras de las 88 constelaciones. Coordenadas ecuatoriales ICRS
(J2000) en grados, con el movimiento propio de Hipparcos (HYG, mas/año) que el simulador aplica desde J2000.
Uso: python herramientas/efemerides/generar_cielo.py
"""
import csv
import io
import json
import urllib.request
from pathlib import Path

BASE = "https://raw.githubusercontent.com/ofrohn/d3-celestial/master/data/"
SALIDA = Path(__file__).resolve().parents[2] / "simuladores" / "datos" / "cielo.json"


def bajar(n):
    with urllib.request.urlopen(BASE + n, timeout=90) as r:
        return json.load(r)


def movimientos_propios():
    """Movimiento propio (mas/año, pmRA* y pmDE) de Hipparcos por número HIP, vía HYG (Hipparcos de la ESA)."""
    url = "https://raw.githubusercontent.com/astronexus/HYG-Database/master/hyg/CURRENT/hygdata_v41.csv"
    with urllib.request.urlopen(url, timeout=180) as r:
        texto = r.read().decode("utf-8")
    pm = {}
    for fila in csv.DictReader(io.StringIO(texto)):
        if fila["hip"]:
            a, d = float(fila["pmra"]), float(fila["pmdec"])
            pm[fila["hip"]] = [a if abs(a) < 9999 else 0.0, d if abs(d) < 9999 else 0.0]
    return pm


def main():
    est = bajar("stars.6.json")["features"]
    nom = bajar("starnames.json")
    cons = bajar("constellations.json")["features"]
    lin = bajar("constellations.lines.json")["features"]
    pm_hip = movimientos_propios()
    estrellas, nombres, pm = [], {}, []
    for f in est:
        ra, dec = f["geometry"]["coordinates"]
        ra = ra % 360
        bv = f["properties"].get("bv") or ""
        try:
            bvf = float(bv)
        except ValueError:
            bvf = 0.6
        i = len(estrellas)
        estrellas.append([round(ra, 3), round(dec, 3), round(f["properties"]["mag"], 2), round(bvf, 2)])
        m = pm_hip.get(str(f["id"]), [0.0, 0.0])
        pm.append([round(m[0]), round(m[1])])
        n = nom.get(str(f["id"]))
        if n and n.get("name"):
            nombres[i] = n["name"].replace(" ", " ")
    figuras = []
    for f in lin:
        figuras.append({"id": f["id"], "lineas": [[[round(a % 360, 2), round(b, 2)] for a, b in seg] for seg in f["geometry"]["coordinates"]]})
    nombre_cons = {}
    for f in cons:
        p = f["properties"]
        nombre_cons[f["id"]] = (p.get("es") or p.get("la") or p.get("name")).replace(" ", " ")
    SALIDA.write_text(json.dumps({"fuente": "d3-celestial (Olaf Frohn, BSD-3-Clause); estrellas Hipparcos/Tycho (ESA); ICRS J2000, sin movimiento propio",
                                  "estrellas": estrellas, "pm_mas_ano": pm, "nombres": nombres, "figuras": figuras, "constelaciones": nombre_cons}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(len(estrellas), "estrellas;", len(nombres), "con nombre;", len(figuras), "figuras;", SALIDA.stat().st_size // 1024, "KB")


main()
