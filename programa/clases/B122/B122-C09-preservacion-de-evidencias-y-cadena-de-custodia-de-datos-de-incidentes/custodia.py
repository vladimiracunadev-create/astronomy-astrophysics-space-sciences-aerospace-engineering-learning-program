#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B122-C09: cadena de custodia de evidencias SINTETICAS con hashes SHA-256 encadenados.

CONTENIDO EDUCATIVO Y DEFENSIVO: no es asesoria legal ni forense; la admisibilidad de una prueba depende de cada jurisdiccion y de un perito.
Datos SINTETICOS (registros inventados). Marco conceptual (solo ficha y resumen consultados el 2026-11-11): NIST SP 800-86 (2006, integracion de tecnicas
forenses en la respuesta a incidentes; el resumen advierte que no es asesoria legal). Vector de prueba publico de SHA-256: SHA-256("abc") =
ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad (FIPS 180-4; el documento FIPS NO se consulto: el vector es el conocido y se verifica con hashlib).
Sistema de referencia: reloj UTC sintetico. Unidades: bits, entradas. Tolerancias: efecto avalancha: fraccion de bits distintos = 0.5 +- 0.02 (1000 pares, semilla 122).
"""
from __future__ import annotations
import hashlib, platform, random

VECTOR_ABC = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def construir(entradas):
    cadena, prev = [], "0" * 64
    for e in entradas:
        h = sha((prev + "|" + e).encode())
        cadena.append((e, prev, h))
        prev = h
    return cadena


def verificar(cadena):
    """Devuelve el indice de la primera entrada rota o None si es integra."""
    prev = "0" * 64
    for i, (e, p, h) in enumerate(cadena):
        if p != prev or sha((p + "|" + e).encode()) != h:
            return i
        prev = h
    return None


def bits_distintos(a: str, b: str) -> int:
    return bin(int(a, 16) ^ int(b, 16)).count("1")


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS: entradas de custodia inventadas; no es una cadena de custodia real ni valida legalmente.")
    assert sha(b"abc") == VECTOR_ABC
    print("Vector de prueba SHA-256('abc') verificado.")
    entradas = [
        "2026-03-05T22:31Z|captura|registro_telemetria.bin (copia de trabajo 1)|analista A",
        "2026-03-05T23:05Z|hash|registro_telemetria.bin|analista A",
        "2026-03-06T08:10Z|transferencia|de analista A a custodio B|custodio B",
        "2026-03-06T08:40Z|almacenamiento|volumen WORM sintetico|custodio B",
        "2026-03-07T10:00Z|acceso|lectura para analisis|analista C",
    ]
    cad = construir(entradas)
    for i, (e, p, h) in enumerate(cad):
        print(f"  #{i} hash={h[:16]}... prev={p[:8]}... {e[:48]}")
    print("Verificacion de la cadena original:", "integra" if verificar(cad) is None else "rota")
    assert verificar(cad) is None
    manip = list(cad)
    e, p, h = manip[2]
    manip[2] = (e.replace("custodio B", "custodio X"), p, h)
    print(f"Se altera el texto de la entrada #2 -> primera entrada rota: #{verificar(manip)}")
    assert verificar(manip) == 2
    manip2 = list(cad)
    e, p, h = manip2[1]
    nuevo = sha((p + "|" + e + " ").encode())
    manip2[1] = (e + " ", p, nuevo)
    print(f"Se altera #1 y se recalcula su hash -> primera entrada rota: #{verificar(manip2)} (la siguiente no encadena)")
    assert verificar(manip2) == 2
    rng = random.Random(122)
    tot = 0
    n = 1000
    for _ in range(n):
        m = bytearray(rng.randbytes(64))
        h1 = sha(bytes(m))
        m[rng.randrange(64)] ^= 1 << rng.randrange(8)
        tot += bits_distintos(h1, sha(bytes(m)))
    frac = tot / (n * 256)
    print(f"Efecto avalancha: fraccion media de bits distintos al cambiar 1 bit = {frac:.4f} (esperado 0.5)")
    assert abs(frac - 0.5) < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
