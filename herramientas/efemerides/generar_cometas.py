# SPDX-License-Identifier: Apache-2.0
"""Genera las efemérides del simulador de cometas: posiciones heliocéntricas (eclíptica J2000) de cometas periódicos de 2027 a 2050 desde
JPL Horizons (solución orbital vigente de cada cometa, con fuerzas no gravitatorias), en el mismo formato que el resto de las efemérides.

Salida: simuladores/datos/cometas.{json,bin}. Una predicción: cada cometa se ajusta a sus observaciones; la incertidumbre crece con el tiempo
y tras acercamientos a Júpiter. Uso: python -X utf8 herramientas/efemerides/generar_cometas.py
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generar_efemerides as G  # noqa: E402
import generar_misiones as M  # noqa: E402

JD_2027, JD_2051 = 2461406.5, 2470172.5
# (designación, nombre, paso en días)
COMETAS = [("1P", "1P/Halley", 2), ("2P", "2P/Encke", 1), ("8P", "8P/Tuttle", 1), ("9P", "9P/Tempel 1", 1), ("10P", "10P/Tempel 2", 1), ("12P", "12P/Pons–Brooks", 2),
           ("17P", "17P/Holmes", 1), ("19P", "19P/Borrelly", 1), ("21P", "21P/Giacobini–Zinner", 1), ("46P", "46P/Wirtanen", 1), ("55P", "55P/Tempel–Tuttle", 1),
           ("67P", "67P/Churyumov–Gerasimenko", 1), ("81P", "81P/Wild 2", 1), ("96P", "96P/Machholz 1", 1), ("103P", "103P/Hartley 2", 1), ("109P", "109P/Swift–Tuttle", 2)]


def main() -> None:
    rng = random.Random(1986)
    cuerpos = []
    for des, nombre, paso in COMETAS:
        cmd = f"DES={des};CAP"
        try:
            tab, t0, n = M.tramo(cmd, JD_2027, JD_2051, paso)
        except Exception as e:  # noqa: BLE001
            print("sin efemérides", nombre, str(e)[:120]); continue
        cuerpos.append({"id": des, "cmd": cmd, "nombre": nombre, "tab": tab, "t0": t0, "paso_d": paso, "fmt": "f64"})
    M.empaquetar("cometas", cuerpos, rng)


if __name__ == "__main__":
    main()
