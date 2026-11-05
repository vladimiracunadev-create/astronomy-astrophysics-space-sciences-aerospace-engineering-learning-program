#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C16: leer, convertir y validar parámetros en YAML y JSON.

Datos PUBLICADOS: parametros_tierra.yaml (GM del Sol, semieje y período sidéreo de la
Tierra; NASA NSSDC, consultado el 2026-11-05). El paso de 3600 s es un valor ELEGIDO.
Modelo: un archivo de parámetros es un diccionario anidado que se guarda en texto.
Supuestos: PyYAML 6.0.3 con safe_load (implementa reglas de YAML 1.1, que difieren de
las de JSON); json de la biblioteca estándar.
Dominio de validez: datos simples (números, texto, listas, None, bool). Tolerancia:
igualdad exacta tras ida y vuelta; las magnitudes se validan como float positivos.
Requiere: pyyaml 6.0.3 (Python 3.12.9).
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

import yaml

AQUI = Path(__file__).resolve().parent
ARCHIVO = AQUI / "parametros_tierra.yaml"

CAMPOS_POSITIVOS = [("cuerpo_central", "gm_km3_s2"), ("planeta", "semieje_km"),
                    ("planeta", "periodo_sidereo_d"), ("simulacion", "paso_s"),
                    ("simulacion", "dias")]


def cargar_yaml(ruta: Path) -> dict:
    """Carga un YAML con safe_load (nunca yaml.load con datos que no controlas)."""
    return yaml.safe_load(ruta.read_text(encoding="utf-8"))


def validar(parametros: dict) -> None:
    """Exige que cada magnitud sea un número positivo; lanza ValueError con el campo."""
    for seccion, campo in CAMPOS_POSITIVOS:
        valor = parametros[seccion][campo]
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError(f"{seccion}.{campo}: se esperaba un número y llegó {valor!r} ({type(valor).__name__})")
        if not valor > 0:
            raise ValueError(f"{seccion}.{campo}: debe ser positivo, llegó {valor}")


def ida_y_vuelta_json(parametros: dict) -> dict:
    """Escribe a JSON en una carpeta temporal, lo lee de vuelta y devuelve el resultado."""
    with tempfile.TemporaryDirectory() as tmp:
        destino = Path(tmp) / "parametros.json"
        destino.write_text(json.dumps(parametros, indent=2, ensure_ascii=False, allow_nan=False), encoding="utf-8")
        return json.loads(destino.read_text(encoding="utf-8"))


def pruebas() -> None:
    p = cargar_yaml(ARCHIVO)
    validar(p)
    assert p["planeta"]["periodo_sidereo_d"] == 365.256 and p["simulacion"]["semilla"] is None
    assert isinstance(p["etiquetas"], list) and p["cuerpo_central"]["gm_km3_s2"] == 1.32712e11
    assert ida_y_vuelta_json(p) == p                                           # YAML -> JSON -> dict
    assert yaml.safe_load(yaml.safe_dump(p, allow_unicode=True)) == p          # dict -> YAML -> dict
    assert yaml.safe_load("pais: no\nactivo: yes") == {"pais": False, "activo": True}   # trampa de YAML 1.1
    assert yaml.safe_load("a: 1.0e+3\nb: 1.0e3") == {"a": 1000.0, "b": "1.0e3"}          # exponente sin signo = texto
    assert yaml.safe_load("z: 010") == {"z": 8}                                          # octal
    assert json.loads(json.dumps({1: "a"})) == {"1": "a"}                                # claves JSON son texto
    assert json.loads('{"a": 1, "a": 2}') == {"a": 2}                                    # clave repetida: gana la última
    for texto in ("{'a': 1}", '{"a": 1, // c\n"b": 2}'):
        try:
            json.loads(texto)
        except json.JSONDecodeError:
            pass
        else:
            raise AssertionError("JSON no admite comillas simples ni comentarios")
    try:
        json.dumps({"x": float("nan")}, allow_nan=False)
    except ValueError:
        pass
    else:
        raise AssertionError("allow_nan=False debía rechazar NaN")
    malo = cargar_yaml(ARCHIVO)
    malo["planeta"]["semieje_km"] = "1.49598e8"                                           # el texto se detecta
    try:
        validar(malo)
    except ValueError as error:
        assert "planeta.semieje_km" in str(error)
    else:
        raise AssertionError("validar debía rechazar un texto")


def main() -> int:
    pruebas()
    p = cargar_yaml(ARCHIVO)
    print(f"python {sys.version.split()[0]} | pyyaml {yaml.__version__} | pruebas OK")
    print("Claves de primer nivel:", list(p))
    print("GM del Sol:", p["cuerpo_central"]["gm_km3_s2"], "km³/s² | tipo:", type(p["cuerpo_central"]["gm_km3_s2"]).__name__)
    print("Ida y vuelta YAML→JSON→dict idéntica:", ida_y_vuelta_json(p) == p)
    print("JSON compacto:", json.dumps(p["planeta"], ensure_ascii=False))
    print("YAML 'pais: no' ->", yaml.safe_load("pais: no"))
    print("YAML 'b: 1.0e3' ->", yaml.safe_load("b: 1.0e3"), "(texto, no número)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
