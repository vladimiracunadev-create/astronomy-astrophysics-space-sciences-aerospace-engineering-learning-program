#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C18: tabla de decision de categorias de proteccion planetaria.

Datos: Tabla 1 de la politica COSPAR 2026 (Space Research Today n. 224, enero de 2026, texto
completo consultado el 2026-11-09 con PyMuPDF): categorias I a V segun cuerpo y tipo de mision.
Se codifica un SUBCONJUNTO (no la politica completa): no incluye misiones tripuladas, categorias
IIa/IIb de la Luna, subdivisiones IVa-IVc de Marte, Ceres ni la tabla 2 de cuerpos. Las
misiones de prueba son SINTETICAS. La politica vigente prevalece sobre este script.
Modelo: funcion categoria(cuerpo, tipo) con tipos "sobrevuelo/orbitador", "sonda/aterrizador"
y "retorno". Para mundos helados la categoria por defecto es III (orbitador) o IV (aterrizador);
II exige un analisis con probabilidad < 1e-4 de llevar nave a ambientes > LLT en 1000 anios.
Supuestos: cuerpo clasificado por su tipo. Validez: ejercicio de decision. Tolerancia:
exactitud (prueba por enumeracion).
"""
from __future__ import annotations
import itertools
import platform
import sys

I, II, III, IV = "I", "II", "III", "IV"
CUERPOS = {
    "asteroide no diferenciado": "I", "io": "I",
    "venus": "II", "luna": "II", "cometa": "II", "asteroide condritico carbonaceo": "II",
    "jupiter": "II", "saturno": "II", "urano": "II", "neptuno": "II",
    "marte": "marte", "europa": "helado", "encelado": "helado", "titan": "helado",
}
SOBREVUELO = "sobrevuelo/orbitador"
SONDA = "sonda/aterrizador"
RETORNO = "retorno"


def categoria(cuerpo, tipo, justificado_II=False):
    grupo = CUERPOS[cuerpo]
    if tipo == RETORNO:
        base = categoria(cuerpo, SONDA, justificado_II)
        restringido = grupo in ("marte", "helado")
        return base + " + V " + ("restringido" if restringido else "no restringido")
    if grupo in ("I", "II"):
        return grupo
    if grupo == "marte":
        return III if tipo == SOBREVUELO else IV
    # mundos helados
    if justificado_II:
        return II
    return III if tipo == SOBREVUELO else IV


ESPERADO = {
    ("io", SONDA): "I", ("venus", SOBREVUELO): "II", ("saturno", SONDA): "II",
    ("marte", SOBREVUELO): "III", ("marte", SONDA): "IV",
    ("europa", SOBREVUELO): "III", ("europa", SONDA): "IV",
    ("encelado", SOBREVUELO): "III", ("titan", SONDA): "IV",
    ("marte", RETORNO): "IV + V restringido", ("luna", RETORNO): "II + V no restringido",
}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for (cuerpo, tipo), esp in ESPERADO.items():
        obt = categoria(cuerpo, tipo)
        print(f"{cuerpo:10s} {tipo:22s} -> {obt}")
        assert obt == esp, f"{cuerpo}/{tipo}: esperado {esp}, obtenido {obt}"
    assert categoria("europa", SOBREVUELO, justificado_II=True) == "II"
    # Prueba por enumeracion: toda combinacion tiene una categoria valida
    for c, t in itertools.product(CUERPOS, (SOBREVUELO, SONDA, RETORNO)):
        assert categoria(c, t).split()[0] in (I, II, III, IV)
    print(f"Enumeradas {len(CUERPOS) * 3} combinaciones sin error.")
    # Presupuesto de probabilidad para mundos helados: 1e-4 en 1000 anios
    p_anual = 1e-4 / 1000
    print(f"Probabilidad anual media equivalente de acceso a ambientes > LLT: {p_anual:.1e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
