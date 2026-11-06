#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C25: un catálogo de escenas con metadatos estilo STAC (simplificado) y su búsqueda.

AVISO: los «ítems» de este laboratorio imitan la IDEA de STAC (ítem = objeto
GeoJSON con geometría, caja envolvente, propiedades y activos) pero son una
SIMPLIFICACIÓN DIDÁCTICA: no se validaron contra el esquema STAC ni contra
ninguna extensión, y la propiedad de nubosidad se llama «nubosidad_pct» (nombre
inventado). No hay red ni servicio STAC.
Datos: SINTÉTICOS. 400 escenas ficticias de 1 grado x 1 grado, en una rejilla de
20 x 20 sobre lon [0, 20), lat [0, 20), con fecha 2026-01-01 + k días (k = 0..39,
cada fecha repetida en 10 escenas) y nubosidad = (indice * 7) % 100 (determinista).
Modelo: búsqueda por caja envolvente (intersección de rectángulos, bordes
excluidos: dos cajas que solo se tocan NO se intersecan), intervalo de fechas
[d0, d1) y filtro por nubosidad.
Supuestos: coordenadas planas lon/lat sin cruce del antimeridiano.
Validez: demostración; el catálogo real tiene colecciones, enlaces y extensiones.
Tolerancia: conteos exactos calculados analíticamente.
"""
from __future__ import annotations
import datetime as dt, json, platform, sys


def construir():
    items = []
    for i in range(400):
        fila, col = divmod(i, 20)
        lon0, lat0 = float(col), float(fila)
        k = i // 10                                   # 40 fechas, 10 escenas por fecha
        fecha = (dt.date(2026, 1, 1) + dt.timedelta(days=k)).isoformat()
        items.append({
            "type": "Feature",
            "id": f"escena-{i:03d}",
            "bbox": [lon0, lat0, lon0 + 1.0, lat0 + 1.0],
            "geometry": {"type": "Polygon", "coordinates": [[[lon0, lat0], [lon0 + 1, lat0], [lon0 + 1, lat0 + 1], [lon0, lat0 + 1], [lon0, lat0]]]},
            "properties": {"fecha": fecha, "nubosidad_pct": (i * 7) % 100},
            "assets": {"imagen": {"href": f"https://ejemplo.invalido/escena-{i:03d}.tif", "type": "image/tiff"}},
        })
    return items


def intersecta(a, b):
    return a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]


def buscar(items, bbox=None, d0=None, d1=None, max_nubosidad=None):
    out = []
    for it in items:
        if bbox is not None and not intersecta(it["bbox"], bbox):
            continue
        f = it["properties"]["fecha"]
        if d0 is not None and f < d0:
            continue
        if d1 is not None and f >= d1:
            continue
        if max_nubosidad is not None and it["properties"]["nubosidad_pct"] > max_nubosidad:
            continue
        out.append(it)
    return out


def revisar_item(it):
    faltan = [k for k in ("type", "id", "bbox", "geometry", "properties", "assets") if k not in it]
    if "fecha" not in it.get("properties", {}):
        faltan.append("properties.fecha")
    if it.get("type") != "Feature":
        faltan.append("type distinto de Feature")
    return faltan


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  (catálogo sintético; sin red; STAC simplificado)")
    items = construir()
    prueba(all(revisar_item(i) == [] for i in items), "todos los ítems tienen los campos mínimos")
    print(f"ítems: {len(items)}; todos con campos mínimos; tamaño de un ítem en JSON = {len(json.dumps(items[0]))} caracteres")

    r = buscar(items, bbox=[3.5, 3.5, 5.5, 5.5])
    print(f"caja [3.5, 3.5, 5.5, 5.5]: {len(r)} escenas (esperado 3 x 3 = 9)")
    prueba(len(r) == 9, "caja interior")
    r = buscar(items, bbox=[5.0, 5.0, 6.0, 6.0])
    print(f"caja [5, 5, 6, 6] (coincide con una escena): {len(r)} escena (esperado 1; las vecinas solo se tocan)")
    prueba(len(r) == 1 and r[0]["id"] == "escena-105", "bordes excluidos")
    r = buscar(items, bbox=[-5, -5, 0.5, 0.5])
    prueba(len(r) == 1 and r[0]["id"] == "escena-000", "caja parcialmente fuera")
    print("caja parcialmente fuera de la rejilla: 1 escena (la 000)")
    r = buscar(items, d0="2026-01-01", d1="2026-01-06")
    print(f"fechas [2026-01-01, 2026-01-06): {len(r)} escenas (esperado 5 fechas x 10 = 50)")
    prueba(len(r) == 50, "intervalo de fechas")
    r = buscar(items, max_nubosidad=20)
    esperado = sum(1 for i in range(400) if (i * 7) % 100 <= 20)
    print(f"nubosidad <= 20 %: {len(r)} escenas (conteo independiente: {esperado})")
    prueba(len(r) == esperado == 84, "filtro de nubosidad")
    r = buscar(items, bbox=[0, 0, 10, 10], d0="2026-01-01", d1="2026-01-21", max_nubosidad=50)
    print(f"combinada: caja [0,0,10,10] x fechas [01-01, 01-21) x nubosidad <= 50: {len(r)} escenas")
    comprobacion = [i for i in range(400)
                    if (i % 20) < 10 and (i // 20) < 10 and (i // 10) < 20 and (i * 7) % 100 <= 50]
    prueba(len(r) == len(comprobacion), "búsqueda combinada contra conteo independiente")
    print(f"conteo independiente de la combinada: {len(comprobacion)} (coincide)")
    # un ítem incompleto se detecta
    malo = dict(items[0]); del malo["bbox"]
    prueba(revisar_item(malo) == ["bbox"], "ítem sin bbox detectado")
    print("ítem sin bbox detectado por el revisor")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
