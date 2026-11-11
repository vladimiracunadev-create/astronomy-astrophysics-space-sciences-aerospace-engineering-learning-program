#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B116-C03: registro de observaciones de misión SINTETICO, integridad por hash, volumen y sincronizacion con cortes.

Todo es sintetico (semilla 118): una tripulacion ficticia de 4 personas ("S1"-"S4"), sin datos de ninguna persona real. Cada
observacion tiene los campos que describe el recurso HL7 FHIR "Observation" (consultado 2026-11-10): code, value, effective (instante),
status, device, subject. NO se usa un servidor FHIR ni los codigos LOINC reales: los codigos son rotulos propios del laboratorio.
Unidades: tiempo en s, volumen en bytes, tasa en bit/s. Parametros del enlace ILUSTRATIVOS (no de una mision): ventana de contacto de
1 h/dia a 256 kbit/s. Se calcula: bytes por observacion en JSON, ratio de compresion zlib, ancho de banda necesario, y la sincronizacion
de dos copias (a bordo y en tierra) con cortes de enlace usando un registro de solo anadir con identificador unico: tras sincronizar,
el hash SHA-256 de ambas copias coincide. Verificacion: alterar una observacion cambia el hash; la sincronizacion es idempotente.
Solo biblioteca estandar y numpy.
"""
from __future__ import annotations
import hashlib
import json
import platform
import zlib
import numpy as np

CODIGOS = {"fc": ("lpm", 72.0, 4.0), "spo2": ("%", 97.0, 1.0), "temp": ("C", 36.8, 0.2)}
TRIP = ["S1", "S2", "S3", "S4"]


def generar(dias, intervalo_s, rng):
    obs, k = [], 0
    for d in range(dias):
        for t in range(0, 86400, intervalo_s):
            for s in TRIP:
                for code, (u, mu, sd) in CODIGOS.items():
                    k += 1
                    obs.append({"id": f"o{k:08d}", "subject": s, "code": code, "value": round(float(rng.normal(mu, sd)), 1), "unit": u,
                                "effective": d * 86400 + t, "status": "final", "device": "sensor-sintetico-01"})
    return obs


def hash_registro(obs):
    cuerpo = json.dumps(sorted(obs, key=lambda o: o["id"]), sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(cuerpo).hexdigest()


def sincronizar(a, b):
    """Union por identificador (solo anadir); devuelve (nuevo_a, nuevo_b)."""
    ia, ib = {o["id"]: o for o in a}, {o["id"]: o for o in b}
    u = {**ia, **ib}
    return list(u.values()), list(u.values())


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 118): tripulacion ficticia de 4 personas; ninguna observacion es de una persona real")
    rng = np.random.default_rng(118)
    ej = generar(1, 60, rng)
    one = len(json.dumps(ej[0], separators=(",", ":")).encode())
    print(f"Ejemplo de observacion: {json.dumps(ej[0], separators=(',', ':'))}")
    print(f"Bytes por observacion (JSON compacto) = {one}")
    print("Volumen por dia para 4 personas x 3 magnitudes segun el intervalo de muestreo:")
    print("  intervalo [s]   observaciones/dia   JSON [MB]   zlib [MB]   ratio   ancho de banda en 1 h de contacto [kbit/s]")
    for iv in (300, 60, 10):
        obs = generar(1, iv, rng)
        raw = json.dumps(obs, separators=(",", ":")).encode()
        z = zlib.compress(raw, 9)
        bw = len(z) * 8 / 3600 / 1000
        print(f"     {iv:5d}          {len(obs):7d}          {len(raw) / 1e6:6.3f}      {len(z) / 1e6:6.3f}   {len(raw) / len(z):5.1f}        {bw:7.3f}")
    print("Comparacion con el enlace ilustrativo de 256 kbit/s durante 1 h/dia (= 115.2 MB/dia utiles teoricos)")
    # integridad
    base = generar(1, 300, rng)
    h0 = hash_registro(base)
    alterada = [dict(o) for o in base]
    alterada[100]["value"] = alterada[100]["value"] + 0.1
    h1 = hash_registro(alterada)
    print(f"SHA-256 original   = {h0[:16]}...")
    print(f"SHA-256 con un valor alterado en 0.1 = {h1[:16]}... (distinto: {h0 != h1})")
    assert h0 != h1
    # sincronizacion con cortes
    bordo, tierra = [], []
    n_total = len(base)
    perdidos = 0
    registros = list(base)
    rng.shuffle(registros)
    hist = []
    for paso in range(10):
        lote = registros[paso * n_total // 10:(paso + 1) * n_total // 10]
        bordo.extend(lote)  # todo se registra a bordo
        contacto = paso % 3 != 1  # cortes en los pasos 1, 4, 7
        if contacto:
            tierra, bordo = sincronizar(tierra, bordo)
        hist.append((paso, contacto, len(bordo), len(tierra), hash_registro(bordo) == hash_registro(tierra)))
    print("Sincronizacion bordo-tierra con cortes (pasos 1, 4 y 7 sin enlace); observaciones y coincidencia de hash:")
    for p, c, nb, nt, ig in hist:
        print(f"  paso {p}: enlace={'si' if c else 'NO'}  bordo={nb:5d}  tierra={nt:5d}  hash igual={ig}")
    tierra, bordo = sincronizar(tierra, bordo)
    assert hash_registro(tierra) == hash_registro(bordo) == h0
    t2, b2 = sincronizar(tierra, bordo)
    assert hash_registro(t2) == h0
    print(f"Tras el ultimo contacto: {len(tierra)} observaciones en ambas copias; hash final = hash del original: {hash_registro(tierra) == h0}")
    print("Idempotencia: sincronizar otra vez no cambia el hash: True")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
