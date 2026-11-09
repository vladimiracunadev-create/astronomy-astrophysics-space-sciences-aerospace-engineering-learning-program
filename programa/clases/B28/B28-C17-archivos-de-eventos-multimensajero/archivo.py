#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C17: archivo de eventos multimensajero con identificador, version, huella SHA-256, validacion y cruce.

Datos: ninguna constante fisica. Contexto: GWTC-1 es un catalogo de fusiones de objetos compactos de las dos primeras campanas
(arXiv:1811.12907, resumen, consultado 2026-11-09). TODOS los registros de este laboratorio (identificadores, tiempos, posiciones,
significancias) son SINTETICOS; no corresponden a ningun evento real.
Modelo: cada registro es un diccionario con campos obligatorios y tipos; la huella es el SHA-256 de su serializacion JSON canonica
(claves ordenadas, separadores fijos, sin espacios); el validador comprueba: campos y tipos, ascension recta en [0, 360), declinacion en
[-90, 90], tiempo ISO 8601 en UTC con sufijo Z, identificador unico, version >= 1 y no decreciente por identificador, significancia >= 0;
el cruce agrupa registros de mensajeros distintos con |dt| < ventana y separacion angular < radio.
Supuestos: registros pequenos en memoria. Validez: ilustrativa.
Tolerancia: el validador debe detectar exactamente los errores inyectados; la huella no depende del orden de las claves y cambia si cambia un valor.
"""
from __future__ import annotations
import hashlib
import json
import math
import platform
import sys
from datetime import datetime, timezone

OBLIG = {"id": str, "mensajero": str, "tiempo_utc": str, "ra_deg": (int, float), "dec_deg": (int, float),
         "error_deg": (int, float), "significancia": (int, float), "version": int}
MENSAJEROS = {"fotones", "neutrinos", "rayos_cosmicos", "ondas_gravitacionales"}


def huella(reg):
    cuerpo = {k: v for k, v in reg.items() if k != "huella"}
    s = json.dumps(cuerpo, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def parsear_tiempo(t):
    if not t.endswith("Z"):
        raise ValueError("falta sufijo Z (UTC)")
    return datetime.strptime(t[:-1], "%Y-%m-%dT%H:%M:%S.%f" if "." in t else "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)


def validar(registros):
    errores = []
    vistos = {}
    for i, r in enumerate(registros):
        rid = r.get("id", f"#{i}")
        for campo, tipo in OBLIG.items():
            if campo not in r:
                errores.append((rid, f"falta {campo}"))
            elif not isinstance(r[campo], tipo) or isinstance(r[campo], bool):
                errores.append((rid, f"tipo de {campo}"))
        if errores and errores[-1][0] == rid and errores[-1][1].startswith(("falta", "tipo")):
            continue
        if r["mensajero"] not in MENSAJEROS:
            errores.append((rid, "mensajero desconocido"))
        if not (0 <= r["ra_deg"] < 360):
            errores.append((rid, "ra fuera de rango"))
        if not (-90 <= r["dec_deg"] <= 90):
            errores.append((rid, "dec fuera de rango"))
        if r["significancia"] < 0 or r["error_deg"] < 0:
            errores.append((rid, "valor negativo"))
        try:
            parsear_tiempo(r["tiempo_utc"])
        except ValueError as e:
            errores.append((rid, f"tiempo: {e}"))
        if r["version"] < 1:
            errores.append((rid, "version < 1"))
        previo = vistos.get(rid)
        if previo is not None:
            if r["version"] <= previo:
                errores.append((rid, "version no creciente"))
        vistos[rid] = r["version"]
        if "huella" in r and r["huella"] != huella(r):
            errores.append((rid, "huella no coincide"))
    return errores


def sep_ang(r1, r2):
    a1, d1, a2, d2 = (math.radians(x) for x in (r1["ra_deg"], r1["dec_deg"], r2["ra_deg"], r2["dec_deg"]))
    c = math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(a1 - a2)
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def cruzar(registros, ventana_s, radio_deg):
    pares = []
    for i in range(len(registros)):
        for j in range(i + 1, len(registros)):
            a, b = registros[i], registros[j]
            if a["mensajero"] == b["mensajero"]:
                continue
            dt = abs((parsear_tiempo(a["tiempo_utc"]) - parsear_tiempo(b["tiempo_utc"])).total_seconds())
            if dt <= ventana_s and sep_ang(a, b) <= radio_deg:
                pares.append((a["id"], b["id"], dt))
    return pares


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    base = [
        {"id": "SINT-0001", "mensajero": "ondas_gravitacionales", "tiempo_utc": "2030-01-05T10:00:00Z", "ra_deg": 197.5, "dec_deg": -23.4, "error_deg": 5.0, "significancia": 12.0, "version": 1},
        {"id": "SINT-0002", "mensajero": "fotones", "tiempo_utc": "2030-01-05T10:00:02Z", "ra_deg": 195.0, "dec_deg": -22.0, "error_deg": 3.0, "significancia": 5.4, "version": 1},
        {"id": "SINT-0003", "mensajero": "neutrinos", "tiempo_utc": "2030-02-11T03:20:00Z", "ra_deg": 77.3, "dec_deg": 5.7, "error_deg": 0.5, "significancia": 3.0, "version": 1},
        {"id": "SINT-0004", "mensajero": "fotones", "tiempo_utc": "2030-02-11T03:20:40Z", "ra_deg": 77.0, "dec_deg": 5.9, "error_deg": 0.1, "significancia": 6.1, "version": 1},
        {"id": "SINT-0005", "mensajero": "fotones", "tiempo_utc": "2030-03-01T12:00:00Z", "ra_deg": 10.0, "dec_deg": 40.0, "error_deg": 1.0, "significancia": 4.0, "version": 1},
    ]
    for r in base:
        r["huella"] = huella(r)
    assert validar(base) == [], "el archivo base debe ser valido"
    print(f"archivo base: {len(base)} registros, sin errores")
    # huella: independiente del orden de las claves, sensible al valor
    r0 = dict(base[0])
    reordenado = {k: r0[k] for k in sorted(r0, reverse=True)}
    assert huella(reordenado) == huella(r0), "orden de claves"
    r1 = dict(r0)
    r1["significancia"] = 12.0001
    assert huella(r1) != huella(r0), "sensibilidad al valor"
    print(f"huella SHA-256 de SINT-0001: {huella(r0)[:16]}... ({len(huella(r0))} hex) ; independiente del orden de claves y sensible a un cambio de 1e-4")
    # errores inyectados
    malo = [dict(r) for r in base]
    malo.append({"id": "SINT-0006", "mensajero": "fotones", "tiempo_utc": "2030-03-02T00:00:00Z", "ra_deg": 45.0, "dec_deg": 95.0, "error_deg": 1.0, "significancia": 4.0, "version": 1})
    malo.append({"id": "SINT-0007", "mensajero": "fotones", "tiempo_utc": "2030-03-02T01:00:00", "ra_deg": 45.0, "dec_deg": 10.0, "error_deg": 1.0, "significancia": 4.0, "version": 1})
    malo.append({"id": "SINT-0008", "mensajero": "neutrino", "tiempo_utc": "2030-03-02T02:00:00Z", "ra_deg": 45.0, "dec_deg": 10.0, "error_deg": 1.0, "significancia": 4.0, "version": 1})
    malo.append({"id": "SINT-0009", "mensajero": "fotones", "tiempo_utc": "2030-03-02T03:00:00Z", "ra_deg": 361.0, "dec_deg": 10.0, "error_deg": 1.0, "significancia": 4.0, "version": 1})
    malo.append({"id": "SINT-0010", "mensajero": "fotones", "tiempo_utc": "2030-03-02T04:00:00Z", "ra_deg": 45.0, "dec_deg": 10.0, "significancia": 4.0, "version": 1})
    dup = dict(base[2])
    dup["significancia"] = 3.5
    malo.append(dup)                                 # misma version -> no creciente
    manip = dict(base[3])
    manip["significancia"] = 99.0                    # huella antigua
    malo[3] = manip
    errs = validar(malo)
    esperados = {("SINT-0006", "dec fuera de rango"), ("SINT-0007", "tiempo: falta sufijo Z (UTC)"), ("SINT-0008", "mensajero desconocido"),
                 ("SINT-0009", "ra fuera de rango"), ("SINT-0010", "falta error_deg"), ("SINT-0003", "version no creciente"), ("SINT-0003", "huella no coincide"), ("SINT-0004", "huella no coincide")}
    print("errores detectados:")
    for e in errs:
        print(f"   {e[0]}: {e[1]}")
    assert set(errs) == esperados, "el validador debe detectar exactamente los errores inyectados"
    pares = cruzar(base, ventana_s=60.0, radio_deg=8.0)
    print("coincidencias (ventana 60 s, radio 8 grados):")
    for a, b, dt in pares:
        print(f"   {a} - {b}: dt = {dt:.0f} s")
    assert [(a, b) for a, b, _ in pares] == [("SINT-0001", "SINT-0002"), ("SINT-0003", "SINT-0004")]
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
