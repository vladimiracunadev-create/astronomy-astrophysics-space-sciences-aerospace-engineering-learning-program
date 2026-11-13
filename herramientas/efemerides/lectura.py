# SPDX-License-Identifier: Apache-2.0
"""Lee las tablas de `simuladores/datos/` y evalúa posiciones con la MISMA interpolación (Lagrange de 10 puntos) que el motor
JavaScript. Lo usan `generar_svg.py` (figuras del README) y las comprobaciones. Sólo biblioteca estándar.
"""
from __future__ import annotations

import json
import math
import struct
from array import array
from pathlib import Path

DATOS = Path(__file__).resolve().parents[2] / "simuladores" / "datos"
NODOS = 10
_DEN = [math.prod(a - b for b in range(NODOS) if b != a) for a in range(NODOS)]
FMT = {"f64": ("d", 8), "f32": ("f", 4), "i16": ("h", 2)}


class Cuerpo:
    def __init__(self, meta: dict, blob: bytes):
        self.meta = meta
        self.id, self.nombre = str(meta["id"]), meta["nombre"]
        self.t0, self.h, self.n = meta["t0"], meta["paso_min"] / 1440, meta["n"]
        cod, tam = FMT[meta["fmt"]]
        self.esc = meta.get("escala_i16", 1.0) if meta["fmt"] == "i16" else 1.0
        raw = blob[meta["offset"]: meta["offset"] + meta["longitud"]]
        self.d = array(cod)
        self.d.frombytes(raw)

    def pos(self, jd_tdb: float) -> tuple[float, float, float]:
        s = (jd_tdb - self.t0) / self.h
        i = int(math.floor(s)); u = s - i
        w = []
        for a in range(NODOS):
            num = 1.0
            for b in range(NODOS):
                if a != b:
                    num *= u - (b - (NODOS // 2 - 1))
            w.append(num / _DEN[a])
        x = y = z = 0.0
        for a in range(NODOS):
            k = (i + a - (NODOS // 2 - 1)) * 3
            x += w[a] * self.d[k]; y += w[a] * self.d[k + 1]; z += w[a] * self.d[k + 2]
        return x * self.esc, y * self.esc, z * self.esc


class Sistema:
    def __init__(self, nombre: str):
        self.meta = json.loads((DATOS / f"{nombre}.json").read_text(encoding="utf-8"))
        blob = (DATOS / f"{nombre}.bin").read_bytes()
        self.cuerpos = {str(c["id"]): Cuerpo(c, blob) for c in self.meta["cuerpos"]}

    def pos(self, id_: str, jd_tdb: float):
        return self.cuerpos[str(id_)].pos(jd_tdb)
