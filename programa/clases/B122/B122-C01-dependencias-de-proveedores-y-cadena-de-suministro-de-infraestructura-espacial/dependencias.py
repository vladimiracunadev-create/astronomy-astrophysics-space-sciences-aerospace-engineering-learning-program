#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B122-C01: concentracion de proveedores y alcance de una caida en una cadena SINTETICA.

CONTENIDO EDUCATIVO Y DEFENSIVO: no es asesoria legal, regulatoria ni de seguridad. Todos los datos son SINTETICOS (inventados);
no representan a ningun operador ni proveedor real. Marco conceptual (solo ficha/resumen consultados el 2026-11-11):
NIST SP 800-161 Rev. 1 (gestion de riesgos de la cadena de suministro; retirada el 2024-11-01).
Definicion usada: HHI = suma de (cuota en %)^2, rango 0..10000. Probabilidad de caida por proveedor: 2 % (ilustrativa).
Sistema de referencia: ninguno espacial; el tiempo no interviene. Unidades: cuotas en %, probabilidades adimensionales.
Tolerancias: HHI de 4 cuotas iguales = 2500 exacto; Monte Carlo (200000 repeticiones, semilla 122) vs enumeracion exacta < 0.003.
"""
from __future__ import annotations
import itertools, platform, random

# Cuota de compra (%) de cada componente-tipo entre proveedores (sintetico)
CUOTAS = {"Antena": [70, 20, 10], "Modem": [40, 30, 30], "Software_C2": [90, 10], "Reloj": [100]}
# Servicios y componentes que necesitan (todos, AND); cada componente tiene proveedores (lista) en el mapa
PROVEEDORES = {  # componente -> proveedores que lo suministran (sinteticos P1..P5)
    "Antena": ["P1", "P2", "P3"], "Modem": ["P2", "P3", "P4"], "Software_C2": ["P4", "P5"], "Reloj": ["P5"],
}
SERVICIOS = {"Telemetria": ["Antena", "Modem"], "Telecomando": ["Antena", "Modem", "Software_C2"],
             "Cronometria": ["Reloj"], "Mision_completa": ["Antena", "Modem", "Software_C2", "Reloj"]}
P_FALLA = 0.02
PROV = ["P1", "P2", "P3", "P4", "P5"]


def hhi(cuotas):
    return sum(c * c for c in cuotas)


def servicio_activo(serv, caidos, modo):
    """modo 'unico': cada componente depende solo de su primer proveedor (monoabastecimiento);
    modo 'multi': basta que quede un proveedor del componente."""
    for comp in SERVICIOS[serv]:
        provs = PROVEEDORES[comp] if modo == "multi" else PROVEEDORES[comp][:1]
        if all(p in caidos for p in provs):
            return False
    return True


def indisponibilidad_exacta(serv, modo):
    total = 0.0
    for bits in itertools.product([0, 1], repeat=len(PROV)):
        caidos = {p for p, b in zip(PROV, bits) if b}
        pr = 1.0
        for b in bits:
            pr *= P_FALLA if b else 1 - P_FALLA
        if not servicio_activo(serv, caidos, modo):
            total += pr
    return total


def indisponibilidad_mc(serv, modo, n, seed):
    rng = random.Random(seed)
    malos = 0
    for _ in range(n):
        caidos = {p for p in PROV if rng.random() < P_FALLA}
        if not servicio_activo(serv, caidos, modo):
            malos += 1
    return malos / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS: cuotas, proveedores P1..P5 y probabilidad de caida del 2 % son inventados.")
    assert hhi([25, 25, 25, 25]) == 2500 and hhi([100]) == 10000
    print("HHI por componente (cuotas %):")
    for comp, cs in CUOTAS.items():
        print(f"  {comp:12s} cuotas={cs} HHI={hhi(cs):5d}")
    print("Alcance de la caida de UN proveedor (servicios que pierden alguna funcion, modo monoabastecimiento):")
    for p in PROV:
        afectados = [s for s in SERVICIOS if not servicio_activo(s, {p}, "unico")]
        print(f"  cae {p}: {len(afectados)} de {len(SERVICIOS)} servicios -> {afectados}")
    print("Indisponibilidad por servicio: exacta (enumeracion de 32 estados) y Monte Carlo [monoabastecimiento | multiproveedor]")
    maxdif = 0.0
    for s in SERVICIOS:
        ex_u, ex_m = indisponibilidad_exacta(s, "unico"), indisponibilidad_exacta(s, "multi")
        mc_u, mc_m = indisponibilidad_mc(s, "unico", 200000, 122), indisponibilidad_mc(s, "multi", 200000, 122)
        maxdif = max(maxdif, abs(ex_u - mc_u), abs(ex_m - mc_m))
        print(f"  {s:16s} exacta: {ex_u:.5f} | {ex_m:.5f}   MC: {mc_u:.5f} | {mc_m:.5f}")
    print(f"Diferencia maxima MC - exacta = {maxdif:.5f}")
    assert maxdif < 0.003
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
