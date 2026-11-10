#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B63-C03: registro de custodia encadenado por hash, balance de masa y contaminacion por mezcla.

Datos: SINTETICOS. La muestra "S-0001", sus masas, los eventos y la contaminacion del blanco son inventados para
el ejemplo; no representan ninguna coleccion real ni el sistema de ningun repositorio.
Modelo: (1) cada evento lleva el SHA-256 del evento anterior (cadena); alterar un registro invalida todos los
posteriores; (2) balance de masa de subdivisiones: masa inicial = suma de alicuotas + residuo + perdidas
declaradas; (3) contaminacion por mezcla: fraccion de contaminante f = (c_medida - c_muestra) / (c_blanco -
c_muestra) y correccion de la concentracion.
Sistema de referencia: tiempo en ISO 8601 UTC como texto; masas en mg; concentraciones en ppm (sinteticas).
Tolerancias: balance de masa exacto en aritmetica de enteros (mg); mezcla < 1e-12 relativo.
Versiones: se imprimen al ejecutar (solo biblioteca estandar).
"""
from __future__ import annotations
import hashlib, json, platform

GENESIS = "0" * 64


def sello(prev: str, ev: dict) -> str:
    cuerpo = json.dumps(ev, sort_keys=True, ensure_ascii=True)
    return hashlib.sha256((prev + cuerpo).encode("utf-8")).hexdigest()


def construir(eventos: list) -> list:
    cadena, prev = [], GENESIS
    for ev in eventos:
        h = sello(prev, ev)
        cadena.append({"ev": ev, "hash": h})
        prev = h
    return cadena


def verificar(cadena: list):
    """Devuelve (True, None) o (False, indice del primer registro inconsistente)."""
    prev = GENESIS
    for i, r in enumerate(cadena):
        if sello(prev, r["ev"]) != r["hash"]:
            return False, i
        prev = r["hash"]
    return True, None


def balance(m0_mg: int, alicuotas_mg: list, residuo_mg: int, perdida_mg: int) -> int:
    return m0_mg - (sum(alicuotas_mg) + residuo_mg + perdida_mg)


def fraccion_contaminante(c_med: float, c_mue: float, c_bla: float) -> float:
    return (c_med - c_mue) / (c_bla - c_mue)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    eventos = [
        {"t": "2026-01-10T09:00:00Z", "accion": "recepcion", "quien": "curador-A", "masa_mg": 5000},
        {"t": "2026-01-10T09:30:00Z", "accion": "pesaje", "quien": "curador-A", "masa_mg": 5000},
        {"t": "2026-01-12T14:00:00Z", "accion": "subdivision", "quien": "curador-B", "alicuotas_mg": [1200, 800], "residuo_mg": 2990},
        {"t": "2026-01-12T14:20:00Z", "accion": "envio", "quien": "curador-B", "destino": "laboratorio-X"},
    ]
    cad = construir(eventos)
    ok, i = verificar(cad)
    print(f"Cadena sintetica de {len(cad)} registros: integra = {ok}")
    assert ok and i is None
    for r in cad:
        print(f"  {r['ev']['t']}  {r['ev']['accion']:12s} {r['hash'][:12]}")
    # prueba de manipulacion: alterar la masa del registro 1 invalida desde ese indice
    cad[1]["ev"]["masa_mg"] = 5100
    ok2, i2 = verificar(cad)
    print(f"Tras alterar el registro 1: integra = {ok2}, primer registro inconsistente = {i2}")
    assert (not ok2) and i2 == 1
    ev = eventos[2]
    sobrante = balance(5000, ev["alicuotas_mg"], ev["residuo_mg"], 10)
    print(f"Balance de masa (5000 mg; alicuotas {ev['alicuotas_mg']}; residuo {ev['residuo_mg']}; perdida declarada 10): sobrante = {sobrante} mg")
    assert sobrante == 0
    print("Balance de masa cerrado (0 mg sin explicar).")
    c_mue, c_bla, c_med = 2.0, 50.0, 3.2
    f = fraccion_contaminante(c_med, c_mue, c_bla)
    c_corr = (c_med - f * c_bla) / (1 - f)
    print(f"Mezcla sintetica: medida {c_med} ppm, blanco {c_bla} ppm, muestra verdadera {c_mue} ppm -> fraccion de contaminante = {f:.6f}; concentracion corregida = {c_corr:.6f} ppm")
    assert abs(c_corr - c_mue) < 1e-12
    print("Correccion por mezcla recupera el valor verdadero (< 1e-12). Pruebas superadas.")


if __name__ == "__main__":
    main()
