#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B20-C04: escribir una medida con su incertidumbre.

Datos: SINTÉTICOS (valores inventados para la clase). Modelo: convención
editorial de la clase (no una norma citada): la incertidumbre se redondea a
2 cifras significativas y el valor se redondea al mismo decimal. Se imprime
como "valor ± incertidumbre unidad". Supuestos: incertidumbre positiva y
finita. Validez: presentación de resultados; no calcula incertidumbres.
Tolerancia: coincidencia exacta de cadenas con los casos de referencia.
"""

from __future__ import annotations

import math
import sys
from decimal import ROUND_HALF_EVEN, Decimal


def formatea(valor: float, incert: float, unidad: str = "", cifras: int = 2) -> str:
    if not (incert > 0 and math.isfinite(incert) and math.isfinite(valor)):
        raise ValueError("la incertidumbre debe ser positiva y finita")
    exp = math.floor(math.log10(incert))
    decimales = cifras - 1 - exp              # decimales a conservar (pueden ser negativos)
    paso = Decimal(1).scaleb(-decimales)      # 10**(-decimales)
    inc_r = Decimal(repr(incert)).quantize(paso, rounding=ROUND_HALF_EVEN)
    val_r = Decimal(repr(valor)).quantize(paso, rounding=ROUND_HALF_EVEN)
    if inc_r >= Decimal(10) ** (exp + cifras):  # el redondeo subió una cifra (p. ej. 0,0996 -> 0,10)
        return formatea(valor, float(inc_r), unidad, cifras)
    sufijo = f" {unidad}" if unidad else ""
    if decimales > 0:
        return f"{val_r:.{decimales}f} ± {inc_r:.{decimales}f}{sufijo}"
    return f"{int(val_r)} ± {int(inc_r)}{sufijo}"


CASOS = [
    ((662.9317, 0.1234, "nm"), "662.93 ± 0.12 nm"),
    ((0.0101234, 0.000153, ""), "0.01012 ± 0.00015"),
    ((43.17, 3.82, "Mpc"), "43.2 ± 3.8 Mpc"),
    ((70.4, 1.27, "km/s/Mpc"), "70.4 ± 1.3 km/s/Mpc"),
    ((12345.0, 432.0, "m"), "12340 ± 430 m"),
]


def pruebas() -> None:
    for entrada, esperado in CASOS:
        obtenido = formatea(*entrada)
        assert obtenido == esperado, (entrada, obtenido, esperado)
    for malo in (0.0, -1.0, float("nan"), float("inf")):
        try:
            formatea(1.0, malo)
        except ValueError:
            continue
        raise AssertionError(f"debía rechazar {malo}")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK | datos SINTÉTICOS")
    for entrada, _ in CASOS:
        print(f"{entrada[0]!r:>12} , {entrada[1]!r:>9} {entrada[2]:<9} ->  {formatea(*entrada)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
