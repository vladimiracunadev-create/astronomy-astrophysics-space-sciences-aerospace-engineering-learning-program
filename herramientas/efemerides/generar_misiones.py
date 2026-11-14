# SPDX-License-Identifier: Apache-2.0
"""Genera las efemérides del simulador de misiones: trayectorias heliocéntricas de naves (JPL Horizons, SPICE) y de los planetas 1970-2050.

Salida: simuladores/datos/misiones.{json,bin} (naves) y simuladores/datos/planetas_hist.{json,bin} (planetas), en el mismo formato que
el resto de las efemérides (Lagrange de 10 puntos). Las trayectorias posteriores a la fecha de descarga son PREDICCIONES de JPL.
Uso: python -X utf8 herramientas/efemerides/generar_misiones.py
"""
from __future__ import annotations

import json
import math
import random
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generar_efemerides as G  # noqa: E402
import horizons as H  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "simuladores" / "datos"
JD_1970 = 2440587.5            # 1970-01-01
JD_2051 = 2470172.5            # 2051-01-01
# (id Horizons, nombre, lanzamiento aprox. (JD), paso en días)
NAVES = [
    ("-23", "Pioneer 10", 2441379.5, 3), ("-24", "Pioneer 11", 2441779.5, 3), ("-32", "Voyager 2", 2443375.5, 3), ("-31", "Voyager 1", 2443392.5, 3),
    ("-77", "Galileo", 2447817.5, 1), ("-82", "Cassini", 2450737.5, 1), ("-98", "New Horizons", 2453755.5, 1), ("-61", "Juno", 2455778.5, 1),
    ("-96", "Parker Solar Probe", 2458342.5, 1), ("-170", "James Webb", 2459573.5, 1), ("-159", "Europa Clipper", 2460597.5, 1),
    ("-55", "Ulysses", 2448170.5, 2), ("-236", "MESSENGER", 2453220.5, 1), ("-226", "Rosetta", 2453066.5, 1),
    ("-203", "Dawn", 2454370.5, 1), ("-121", "BepiColombo", 2458411.5, 1), ("-144", "Solar Orbiter", 2458889.5, 1), ("-64", "OSIRIS-REx", 2457639.5, 1),
    ("-49", "Lucy", 2459503.5, 1), ("-255", "Psyche", 2460230.5, 1), ("-37", "Hayabusa2", 2456994.5, 1), ("-202", "MAVEN", 2456615.5, 1),
]
PLANETAS = [("199", "Mercurio", 1), ("299", "Venus", 2), ("399", "Tierra", 1), ("499", "Marte", 2), ("599", "Júpiter", 4), ("699", "Saturno", 4), ("799", "Urano", 4), ("899", "Neptuno", 4), ("9", "Plutón (baricentro)", 4)]
NV = 80


MESES = {m: i + 1 for i, m in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split())}


def _jd_fecha(txt: str) -> float:
    """'2043-OCT-30' -> JD (0 h) mediante el calendario gregoriano proléptico."""
    import datetime
    a, m, d = txt.split("-")
    return datetime.date(int(a), MESES[m], int(d)).toordinal() + 1721424.5


def rango_valido(cid: str, jd0: float, jd1: float) -> tuple[float, float]:
    """Recorta [jd0, jd1] a la cobertura de las efemérides de la nave (los límites salen del mensaje de error de Horizons)."""
    import re
    for fecha, sentido in (("1960-01-01", "prior to"), ("2060-01-01", "after")):
        t = H.consulta({"COMMAND": cid, "OBJ_DATA": "NO", "MAKE_EPHEM": "YES", "EPHEM_TYPE": "VECTORS", "CENTER": "500@10", "START_TIME": fecha, "STOP_TIME": fecha[:-1] + "2",
                        "STEP_SIZE": "1d", "REF_PLANE": "ECLIPTIC", "REF_SYSTEM": "ICRF", "OUT_UNITS": "KM-S", "VEC_TABLE": "2", "CSV_FORMAT": "YES"})
        m = re.search(sentido + r" A\.D\. (\d{4}-[A-Z]{3}-\d{2})", t)
        if m:
            j = _jd_fecha(m.group(1))
            if sentido == "prior to":
                jd0 = max(jd0, j + 2)
            else:
                jd1 = min(jd1, j - 2)
    return jd0, jd1


def tramo(cid: str, jd0: float, jd1: float, paso_d: float):
    G.JD_INI, G.JD_FIN = jd0, jd1
    n = int(math.ceil((jd1 - jd0) / paso_d)) + 2 * G.NODOS + 2
    tab, t0, jmin, jmax = G.descargar(cid, "500@10", int(round(paso_d * 1440)), n)
    return tab, t0, n


def empaquetar(nombre: str, cuerpos: list[dict], rng: random.Random) -> None:
    meta = {"sistema": nombre, "centro_horizons": "500@10", "marco": "Eclíptica y equinoccio J2000 (ICRF), geométrico", "unidades": "km", "escala_tiempo": "TDB", "nodos_lagrange": G.NODOS, "cuerpos": []}
    trozos, off = [], 0
    verif = {}
    vf = SALIDA / "verificacion.json"
    todo = json.loads(vf.read_text(encoding="utf-8")) if vf.exists() else {}
    for c in cuerpos:
        tab, t0, h = c["tab"], c["t0"], c["paso_d"]
        q, esc = G.cuantizar(tab, c["fmt"])
        tabq = q.astype(np.float64)
        lo, hi = t0 + 6 * h, t0 + (len(tab) - 7) * h
        jds = sorted(rng.uniform(lo, hi) for _ in range(G.N_VERIF))
        ref = []
        for k in range(0, len(jds), 60):
            ref += H.vectores_lista(c.get("cmd", c["id"]), "500@10", jds[k:k + 60], tabla="1")
        errs, muestras = [], []
        for r in ref:
            p = G.lagrange(tabq, t0, h, r[0]); errs.append(float(np.linalg.norm(p - np.array(r[1:4])))); muestras.append([r[0], r[1], r[2], r[3]])
        b = q.tobytes(); pad = (-len(b)) % 8; b += b"\0" * pad
        meta["cuerpos"].append({"id": c["id"], "nombre": c["nombre"], "paso_min": int(round(h * 1440)), "fmt": c["fmt"], "n": len(tab), "t0": t0, "jd_valido_ini": t0 + 5 * h, "jd_valido_fin": t0 + (len(tab) - 6) * h,
                                "offset": off, "longitud": len(b) - pad, "escala_i16": esc, "error_max_km": round(max(errs), 3), "error_rms_km": round(float(np.sqrt(np.mean(np.square(errs)))), 3), "a_km": None})
        todo[f"{nombre}/{c['id']}"] = {"nombre": c["nombre"], "epocas": muestras[:12], "error_max_km": round(max(errs), 3)}
        trozos.append(b); off += len(b)
        print(f"  {c['nombre']}: {len(tab)} nodos, error máx {max(errs):.1f} km")
    (SALIDA / f"{nombre}.bin").write_bytes(b"".join(trozos))
    (SALIDA / f"{nombre}.json").write_text(json.dumps(meta, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    vf.write_text(json.dumps(todo, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def main() -> None:
    rng = random.Random(1977)
    planetas = []
    for cid, nom, paso in PLANETAS:
        tab, t0, n = tramo(cid, JD_1970, JD_2051, paso)
        planetas.append({"id": cid, "nombre": nom, "tab": tab, "t0": t0, "paso_d": paso, "fmt": "f64"})
    print("planetas descargados")
    naves = []
    for cid, nom, lanz, paso in NAVES:
        try:
            a, b = rango_valido(cid, lanz, JD_2051)
            tab, t0, n = tramo(cid, a, b, paso)
        except Exception as e:  # noqa: BLE001
            print("sin efemérides", nom, str(e)[:120]); continue
        naves.append({"id": cid, "nombre": nom, "tab": tab, "t0": t0, "paso_d": paso, "fmt": "f32"})
    print("naves descargadas")
    # los errores de verificación usan JD dentro del tramo válido de cada cuerpo
    empaquetar("planetas_hist", planetas, rng)
    empaquetar("misiones", naves, rng)


if __name__ == "__main__":
    main()
