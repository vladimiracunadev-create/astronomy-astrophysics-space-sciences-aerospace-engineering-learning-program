#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C02: tipos de datos y variables con una ficha de la Tierra.

Datos PUBLICADOS: NASA NSSDC, fichas individuales de planetas (Earth Fact Sheet act. 15-nov-2024), consultada el 2026-11-05:
masa 5,9722e24 kg, radio ecuatorial 6378,137 km, período sidéreo 365,256 d.
Modelo: ninguno; se estudian los tipos de Python (int, float, str, bool, None).
Supuestos: aritmética de coma flotante binaria de 64 bits (float de CPython).
Dominio de validez: valores finitos. Tolerancia: math.isclose con rel_tol=1e-9.
"""

from __future__ import annotations

import math
import sys

nombre = "Tierra"            # str
masa_kg = 5.9722e24          # float en notación científica: 5,9722 × 10^24
posicion = 3                 # int: tercer planeta desde el Sol
radio_ecuatorial_km = 6378.137  # float
periodo_d = 365.256          # float: período sidéreo
es_gigante = False           # bool
satelite_mayor = None        # None: «sin valor»


def nombre_del_tipo(valor) -> str:
    """Devuelve el nombre del tipo de un valor."""
    return type(valor).__name__


def pruebas() -> None:
    assert nombre_del_tipo(nombre) == "str"
    assert nombre_del_tipo(masa_kg) == "float"
    assert nombre_del_tipo(posicion) == "int"
    assert nombre_del_tipo(radio_ecuatorial_km) == "float"
    assert nombre_del_tipo(es_gigante) == "bool"
    assert nombre_del_tipo(satelite_mayor) == "NoneType"
    assert 0.1 + 0.2 != 0.3                                # la igualdad exacta falla
    assert math.isclose(0.1 + 0.2, 0.3)                    # la comparación con tolerancia funciona
    assert 7 / 2 == 3.5 and 7 // 2 == 3 and 7 % 2 == 1     # división real, entera y resto
    assert int("3") + 1 == 4                                 # texto -> entero
    assert float("365.256") == periodo_d                     # texto -> decimal
    assert True + True == 2                                # bool es un tipo de entero
    assert math.isclose(masa_kg, 5.9722 * 10**24, rel_tol=1e-9)
    assert math.isclose(2 * radio_ecuatorial_km, 12756.274)   # diámetro = 2 × radio


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    for etiqueta, valor in [("nombre", nombre), ("masa_kg", masa_kg),
                            ("posicion", posicion), ("radio_ecuatorial_km", radio_ecuatorial_km), ("periodo_d", periodo_d),
                            ("es_gigante", es_gigante), ("satelite_mayor", satelite_mayor)]:
        print(f"{etiqueta:<20} = {valor!r:<10} tipo: {nombre_del_tipo(valor)}")
    print("0.1 + 0.2 =", 0.1 + 0.2, "| ¿igual a 0.3?", 0.1 + 0.2 == 0.3,
          "| isclose:", math.isclose(0.1 + 0.2, 0.3))
    print("7 / 2 =", 7 / 2, "| 7 // 2 =", 7 // 2, "| 7 % 2 =", 7 % 2)
    print("diámetro (km) =", 2 * radio_ecuatorial_km, "| tipo:", nombre_del_tipo(2 * radio_ecuatorial_km))
    print("masa en forma legible:", f"{masa_kg:.4e} kg", "| float.hex(0.1) =", float.hex(0.1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
