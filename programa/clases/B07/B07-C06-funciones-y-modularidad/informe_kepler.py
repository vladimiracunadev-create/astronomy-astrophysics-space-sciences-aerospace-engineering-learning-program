#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C06: usa el módulo kepler.py desde otro archivo.

Datos y modelo: los de kepler.py (NASA NSSDC publicados; regularidad de Kepler).
Supuestos y validez: los de kepler.py. Tolerancia: la del módulo (±2 %).
Este script solo IMPORTA funciones; no repite su código.
"""

from __future__ import annotations

import sys

import kepler


def main() -> int:
    kepler.pruebas()
    print(f"python {sys.version.split()[0]} | pruebas del módulo OK")
    print(f"{'planeta':<9}{'T real (años)':>15}{'T predicho':>12}{'desv. %':>9}")
    for nombre, (a, t) in kepler.DATOS.items():
        a_rel = kepler.normalizar(a, kepler.A_TIERRA_1E6KM)
        t_real = kepler.normalizar(t, kepler.T_TIERRA_D)
        t_pred = kepler.periodo_predicho(a_rel)
        print(f"{nombre:<9}{t_real:>15.3f}{t_pred:>12.3f}"
              f"{kepler.desviacion_porcentual(t_pred, t_real):>+9.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
