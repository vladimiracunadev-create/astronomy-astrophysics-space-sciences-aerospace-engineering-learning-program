#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C19: validacion de un registro de calibracion.

Datos: SINTETICOS. Registro de calibracion de un fotodiodo (la calibracion de
C05: a = 46.55 DN, b = 2.5036 DN/(W/m2)) con patrones, condiciones,
incertidumbres y vigencia. Como ejemplo REAL de vigencia declarada se cita el
archivo Leap_Second.dat del IERS, cuya cabecera indica expiracion el
2027-06-28 (consultado 2026-11-05).
Modelo: un registro es valido si (1) contiene todos los campos obligatorios;
(2) las fechas son coherentes (calibracion <= vigencia) y no ha vencido en la
fecha de uso; (3) cada patron declara certificado, incertidumbre y
trazabilidad; (4) U = k * u dentro de 1e-9; (5) el hash SHA-256 del contenido
canonico coincide (integridad).
Supuestos: un solo mensurando y modelo lineal. Tolerancia: coherencia de
U = k u a 1e-9; hash exacto.
"""
from __future__ import annotations
import copy
import datetime
import hashlib
import json
import platform
import sys

OBLIGATORIOS = ["id", "instrumento", "mensurando", "fecha_calibracion", "vigente_hasta",
                "condiciones", "patrones", "resultado", "software", "operador"]


def hash_registro(r: dict) -> str:
    base = {k: v for k, v in r.items() if k != "sha256"}
    canon = json.dumps(base, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def validar(r: dict, fecha_uso: str) -> list[str]:
    errores = []
    for c in OBLIGATORIOS:
        if c not in r:
            errores.append(f"falta el campo obligatorio '{c}'")
    if errores:
        return errores
    try:
        f0 = datetime.date.fromisoformat(r["fecha_calibracion"])
        f1 = datetime.date.fromisoformat(r["vigente_hasta"])
        fu = datetime.date.fromisoformat(fecha_uso)
    except ValueError:
        return ["fecha con formato no ISO"]
    if f1 < f0:
        errores.append("vigencia anterior a la calibracion")
    if fu > f1:
        errores.append("registro vencido en la fecha de uso")
    if fu < f0:
        errores.append("uso anterior a la calibracion")
    if not r["patrones"]:
        errores.append("sin patrones declarados")
    for p in r["patrones"]:
        for c in ("id", "certificado", "u_k1", "trazable_a"):
            if c not in p:
                errores.append(f"patron sin '{c}'")
    res = r["resultado"]
    for c in ("modelo", "parametros", "k", "u_tipica", "U"):
        if c not in res:
            errores.append(f"resultado sin '{c}'")
    if "k" in res and "u_tipica" in res and "U" in res:
        if abs(res["k"] * res["u_tipica"] - res["U"]) > 1e-9:
            errores.append("U distinta de k * u")
    for c in ("python", "numpy_o_otras"):
        if c not in r["software"]:
            errores.append(f"software sin '{c}'")
    if "sha256" not in r:
        errores.append("sin hash de integridad")
    elif r["sha256"] != hash_registro(r):
        errores.append("el hash no coincide: registro alterado")
    return errores


def registro_ejemplo() -> dict:
    r = {
        "id": "CAL-FD-0001",
        "instrumento": {"id": "FD-01", "modelo": "fotodiodo (sintetico)", "serie": "SIN-0001"},
        "mensurando": {"nombre": "irradiancia", "unidad": "W/m2"},
        "fecha_calibracion": "2026-11-05",
        "vigente_hasta": "2027-11-05",
        "condiciones": {"temperatura_K": 293.15, "intervalo_W_m2": [100, 1000]},
        "patrones": [{"id": "LAMP-PAT-7", "certificado": "CERT-SIN-123", "u_k1": 0.5,
                      "trazable_a": "patron primario (sintetico)"}],
        "resultado": {"modelo": "DN = a + b x", "parametros": {"a": 46.55, "b": 2.5036},
                      "k": 2.0, "u_tipica": 0.0096, "U": 0.0192},
        "software": {"python": platform.python_version(), "numpy_o_otras": "ninguna"},
        "operador": "operador sintetico",
    }
    r["sha256"] = hash_registro(r)
    return r


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = registro_ejemplo()
    print(f"hash = {r['sha256'][:16]}... ; errores en el registro bueno: {validar(r, '2026-12-01')}")
    assert validar(r, "2026-12-01") == []
    casos = []
    x = copy.deepcopy(r); del x["vigente_hasta"]; casos.append(("sin vigencia", x, "2026-12-01"))
    x = copy.deepcopy(r); casos.append(("vencido", x, "2028-01-01"))
    x = copy.deepcopy(r); x["resultado"]["U"] = 0.05; x["sha256"] = hash_registro(x); casos.append(("U != k u", x, "2026-12-01"))
    x = copy.deepcopy(r); x["patrones"] = []; x["sha256"] = hash_registro(x); casos.append(("sin patrones", x, "2026-12-01"))
    x = copy.deepcopy(r); x["resultado"]["parametros"]["b"] = 2.6; casos.append(("alterado sin rehacer el hash", x, "2026-12-01"))
    x = copy.deepcopy(r); x["fecha_calibracion"] = "2026-13-45"; casos.append(("fecha no ISO", x, "2026-12-01"))
    for nombre, reg, fu in casos:
        e = validar(reg, fu)
        print(f"- {nombre}: {e}")
        assert e, nombre
    # Vigencia del archivo de segundos intercalares del IERS (ejemplo real)
    iers = {"id": "TABLA-IERS", "vigente_hasta": "2027-06-28"}
    d = (datetime.date.fromisoformat(iers["vigente_hasta"]) - datetime.date(2026, 11, 5)).days
    print(f"la tabla del IERS vence el {iers['vigente_hasta']}: faltan {d} dias desde 2026-11-05")
    assert d == 235
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
