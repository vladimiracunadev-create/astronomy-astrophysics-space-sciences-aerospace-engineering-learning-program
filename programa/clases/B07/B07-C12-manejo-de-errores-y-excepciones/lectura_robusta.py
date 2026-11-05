#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C12: errores y excepciones en una lectura y un cálculo robustos.

Datos: planetas_nssdc.csv (PUBLICADO, NASA NSSDC, clase B07-C08, consultado el
2026-11-05) y datos_sinteticos_invalidos.csv (SINTÉTICO, inventado para esta clase).
Modelo: razón de Kepler T^2/a^3 con T en años terrestres y a en distancias terrestres.
Supuestos: a > 0 y T > 0; un dato inválido debe provocar un error claro, no un número.
Dominio de validez: planetas del sistema solar. Tolerancia: la razón de la Tierra es 1
dentro de 1e-12; los demás planetas dentro de ±2 %.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
C08 = AQUI.parent / "B07-C08-lectura-de-archivos-csv"
A_TIERRA, T_TIERRA = 149.598, 365.256


class DatoInvalido(ValueError):
    """Un dato de entrada no cumple lo que el cálculo necesita."""


def a_positivo(texto: str, nombre: str) -> float:
    """Convierte `texto` a float positivo o lanza DatoInvalido con un mensaje claro."""
    try:
        valor = float(texto)
    except ValueError:
        raise DatoInvalido(f"{nombre}: '{texto}' no es un número") from None
    if not valor > 0:                      # también rechaza NaN
        raise DatoInvalido(f"{nombre}: {valor} no es positivo")
    return valor


def razon_kepler(semieje_1e6km: float, periodo_d: float) -> float:
    """Razón T^2/a^3 (años y distancias terrestres); lanza DatoInvalido si a o T no son > 0."""
    if not (semieje_1e6km > 0 and periodo_d > 0):
        raise DatoInvalido("semieje y período deben ser positivos")
    return (periodo_d / T_TIERRA) ** 2 / (semieje_1e6km / A_TIERRA) ** 3


def razones_desde_csv(ruta: Path):
    """Devuelve (razones por nombre, lista de problemas) leyendo un CSV; no oculta errores."""
    razones, problemas = {}, []
    try:
        f = ruta.open(encoding="utf-8", newline="")
    except FileNotFoundError:
        raise FileNotFoundError(f"no existe el archivo de datos: {ruta.name}") from None
    try:
        lector = csv.DictReader(f)
        for fila in lector:
            try:
                a = a_positivo(fila["semieje_1e6km"], "semieje")
                t = a_positivo(fila["periodo_sidereo_d"], "período")
            except DatoInvalido as error:
                problemas.append((lector.line_num, str(error)))
            else:
                razones[fila["nombre"]] = razon_kepler(a, t)
    finally:
        f.close()                           # se cierra siempre
    return razones, problemas


def lanza(funcion, *args, esperado):
    """Comprueba que funcion(*args) lance `esperado`; devuelve el mensaje."""
    try:
        funcion(*args)
    except esperado as error:
        return str(error)
    raise AssertionError(f"debía lanzar {esperado.__name__}")


def pruebas() -> None:
    assert a_positivo("365.256", "T") == 365.256
    assert lanza(a_positivo, "abc", "T", esperado=DatoInvalido) == "T: 'abc' no es un número"
    assert lanza(a_positivo, "-1", "T", esperado=DatoInvalido) == "T: -1.0 no es positivo"
    assert lanza(a_positivo, "nan", "T", esperado=DatoInvalido) == "T: nan no es positivo"
    assert lanza(razon_kepler, 0.0, 1.0, esperado=ValueError)         # DatoInvalido es un ValueError
    assert abs(razon_kepler(A_TIERRA, T_TIERRA) - 1.0) < 1e-12
    razones, problemas = razones_desde_csv(C08 / "planetas_nssdc.csv")
    assert len(razones) == 8 and problemas == []
    assert all(abs(r - 1.0) < 0.02 for r in razones.values())
    assert lanza(razones_desde_csv, C08 / "no_existe.csv", esperado=FileNotFoundError)
    razones, problemas = razones_desde_csv(AQUI / "datos_sinteticos_invalidos.csv")
    assert list(razones) == ["Alfa"] and [n for n, _ in problemas] == [3, 4, 5, 6]
    try:
        1 / 0
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("1/0 debía fallar")


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    razones, problemas = razones_desde_csv(C08 / "planetas_nssdc.csv")
    print(f"planetas_nssdc.csv: {len(razones)} razones, {len(problemas)} problemas")
    for texto in ("abc", "-1", "nan"):
        try:
            a_positivo(texto, "semieje")
        except DatoInvalido as error:
            print(f"  entrada {texto!r:<6} -> DatoInvalido: {error}")
    razones, problemas = razones_desde_csv(AQUI / "datos_sinteticos_invalidos.csv")
    print(f"datos_sinteticos_invalidos.csv: {len(razones)} razón válida, {len(problemas)} problemas")
    for n, motivo in problemas:
        print(f"  línea {n}: {motivo}")
    try:
        razones_desde_csv(C08 / "no_existe.csv")
    except FileNotFoundError as error:
        print("  archivo inexistente ->", error)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
