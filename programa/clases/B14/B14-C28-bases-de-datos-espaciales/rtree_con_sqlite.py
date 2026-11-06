#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C28: índice espacial R-tree en SQLite (módulo estándar sqlite3).

Datos: SINTÉTICOS. 50 000 huellas rectangulares ficticias de escenas en el plano
lon [0, 360), lat [-90, 90): lon0 ~ U(0, 359), lat0 ~ U(-90, 89), tamaño 0.5 a 3
grados (semilla 20261105). No son escenas reales.
Modelo: tabla `escenas` + tabla virtual `idx` (rtree) con id, minX, maxX, minY,
maxY. Consulta por caja: candidatos del R-tree (solapamiento) frente a una
búsqueda por fuerza bruta con NumPy (conteo independiente).
Supuestos: coordenadas planas (sin antimeridiano ni esfera); el R-tree guarda
float de 32 bits, por lo que las cajas pueden crecer ligeramente (por redondeo
hacia afuera), nunca encoger.
Validez: demostración del principio de índice espacial; no es PostGIS ni SpatiaLite.
Tolerancia: los identificadores devueltos por el R-tree deben ser un SUPERCONJUNTO
exacto-o-casi de los de la fuerza bruta: nunca faltar; los sobrantes (por el
redondeo a float32) deben ser <= 0.1 % del total devuelto.
"""
from __future__ import annotations
import platform, sqlite3, sys, time
import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  SQLite {sqlite3.sqlite_version}")
    rng = np.random.default_rng(20261105)
    n = 50_000
    lon0 = rng.uniform(0, 359, n)
    lat0 = rng.uniform(-90, 89, n)
    w = rng.uniform(0.5, 3.0, n)
    h = rng.uniform(0.5, 3.0, n)
    cajas = np.column_stack([lon0, lon0 + w, lat0, np.minimum(lat0 + h, 90.0)])   # minX, maxX, minY, maxY

    con = sqlite3.connect(":memory:")
    try:
        con.execute("CREATE VIRTUAL TABLE idx USING rtree(id, minX, maxX, minY, maxY)")
    except sqlite3.OperationalError as e:
        print(f"OMITIDO: este SQLite no incluye el módulo R*Tree ({e})")
        raise SystemExit(2)
    con.execute("CREATE TABLE escenas(id INTEGER PRIMARY KEY, nombre TEXT)")
    con.executemany("INSERT INTO escenas VALUES(?, ?)", [(i, f"escena-{i:05d}") for i in range(n)])
    con.executemany("INSERT INTO idx VALUES(?, ?, ?, ?, ?)", [(i, *map(float, cajas[i])) for i in range(n)])
    con.commit()
    print(f"insertadas {n} huellas en tabla y en el R-tree")

    q = (100.0, 110.0, 20.0, 30.0)               # minX, maxX, minY, maxY
    t0 = time.perf_counter()
    ids_rt = {r[0] for r in con.execute(
        "SELECT id FROM idx WHERE maxX >= ? AND minX <= ? AND maxY >= ? AND minY <= ?", (q[0], q[1], q[2], q[3]))}
    t_rt = time.perf_counter() - t0
    t0 = time.perf_counter()
    m = (cajas[:, 1] >= q[0]) & (cajas[:, 0] <= q[1]) & (cajas[:, 3] >= q[2]) & (cajas[:, 2] <= q[3])
    ids_bf = set(np.flatnonzero(m).tolist())
    t_bf = time.perf_counter() - t0
    faltan = ids_bf - ids_rt
    sobran = ids_rt - ids_bf
    print(f"caja de consulta {q}: R-tree devuelve {len(ids_rt)}, fuerza bruta {len(ids_bf)}; faltan {len(faltan)}; sobran {len(sobran)}")
    prueba(len(faltan) == 0, "el R-tree nunca debe perder un solapamiento")
    prueba(len(sobran) <= max(1, int(0.001 * len(ids_rt))), "sobrantes por redondeo float32 <= 0.1 %")
    print(f"tiempos (una sola medición, sin repetir): R-tree = {t_rt*1e3:.2f} ms; NumPy sobre todas las cajas = {t_bf*1e3:.2f} ms")

    # consulta puntual con unión a la tabla de atributos
    punto = (180.0, 0.0)
    filas = con.execute(
        "SELECT e.nombre FROM idx i JOIN escenas e ON e.id = i.id WHERE i.minX <= ? AND i.maxX >= ? AND i.minY <= ? AND i.maxY >= ? ORDER BY e.id",
        (punto[0], punto[0], punto[1], punto[1])).fetchall()
    bf = np.flatnonzero((cajas[:, 0] <= punto[0]) & (cajas[:, 1] >= punto[0]) & (cajas[:, 2] <= punto[1]) & (cajas[:, 3] >= punto[1]))
    print(f"punto {punto}: {len(filas)} escenas lo contienen (fuerza bruta: {len(bf)})")
    prueba(len(filas) >= len(bf) and len(filas) - len(bf) <= 1, "consulta puntual coherente")

    # caso exacto: caja que no toca nada (fuera del dominio)
    vacio = con.execute("SELECT count(*) FROM idx WHERE maxX >= 400 AND minX <= 410 AND maxY >= 0 AND minY <= 10").fetchone()[0]
    prueba(vacio == 0, "caja fuera del dominio")
    print("caja fuera del dominio: 0 resultados (correcto)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
