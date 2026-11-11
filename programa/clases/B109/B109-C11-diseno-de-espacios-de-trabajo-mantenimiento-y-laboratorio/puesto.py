#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C11: areas de trabajo frente a los minimos recomendados, paso de equipos por la pista y holguras de mantenimiento.

Datos consultados (2026-11-10; Burke, Howard y Kessler 2022): Tabla 4 (areas recomendadas y del trazado), Tabla 1 (volumen y area de funciones: estacion de mantenimiento 3.28 m3 / 1.37 m2,
reparacion de componentes 3.28 / 1.37, interfaz de ordenador 2.24 / 1.12, almacenamiento temporal de equipos EVA 0.25 / 0.25), altura estandar 2.4 m, pista de traslado de 1.00 m de ancho,
paletas ECLSS de 72 in de largo y seccion maxima de 30.19 in para pasar por una escotilla estandar de NASA (1 in = 0.0254 m, definicion), 10 paletas en el habitat.
ILUSTRATIVOS (no son requisitos): profundidad del cuerpo de quien trabaja (0.50 m), profundidad de extraccion de cada equipo (lista abajo) y su posicion frente a la pista.
Modelo: area del trazado - area minima recomendada = holgura (negativa = deficit); profundidad libre necesaria = 0.50 + extraccion; el equipo es accesible si la necesaria <= ancho de pista.
Segunda via: la razon volumen/area de la estacion de mantenimiento debe ser la altura estandar con 0.5 %; el conteo de equipos inaccesibles por bucle debe coincidir con el calculo por comprension (igualdad).
Unidades: area [m2], volumen [m3], longitud [m].
"""
from __future__ import annotations
import platform

PULG = 0.0254
TABLA4 = {  # funcion: (minimo recomendado m2, area del trazado m2)
    "Estiramiento": (1.40, 2.68), "Sueno": (1.82, 3.70), "Medico": (1.87, 3.43), "Ejercicio": (1.5, 2.09), "UWMS": (0.91, 1.04),
    "Higiene": (1.06, 1.04), "Mesa": (1.62, 2.23), "Trabajo (mantenimiento)": (1.37, 1.30), "Ordenador general": (1.82, 2.10),
    "Cocina trabajo": (0.56, 0.95), "Cocina preparacion": (0.56, 1.17),
}
PISTA = 1.00
CUERPO = 0.50  # m, ILUSTRATIVO
EQUIPOS = {  # extraccion necesaria frente al equipo [m], ILUSTRATIVA
    "filtro de aire": 0.30, "bomba de agua": 0.40, "ordenador": 0.30, "panel electrico": 0.45,
    "unidad sustituible (rack)": 0.80, "paleta ECLSS (extraccion)": 0.90, "ventilador": 0.35,
}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Areas de la Tabla 4 y dimensiones de las paletas de Burke et al. (2022); cuerpo y extraccion ILUSTRATIVOS")
    print(" funcion                    minimo [m2]   trazado [m2]   holgura [m2]")
    deficit = []
    for k, (mn, ar) in TABLA4.items():
        print(f"{k:26s} {mn:10.2f} {ar:13.2f} {ar - mn:13.2f}")
        if ar < mn:
            deficit.append(k)
    print("Funciones con area del trazado menor que el minimo recomendado:", ", ".join(deficit))
    assert abs(3.28 / 1.37 - 2.4) / 2.4 < 0.005
    ancho = 30.19 * PULG
    largo = 72 * PULG
    print(f"Paleta ECLSS: largo {largo:.3f} m ; seccion maxima {ancho:.3f} m ; margen lateral en una pista de {PISTA:.2f} m = {PISTA - ancho:.3f} m ({(PISTA - ancho) / 2:.3f} m por lado)")
    print(f"Estacion de mantenimiento: 3.28 m3 / 1.37 m2 = {3.28 / 1.37:.3f} m (altura estandar 2.4 m)")
    print(" equipo                      extraccion [m]   profundidad libre necesaria [m]   accesible desde una pista de 1.00 m")
    inacc = []
    for k, e in EQUIPOS.items():
        nec = CUERPO + e
        ok = nec <= PISTA + 1e-12
        print(f"{k:27s} {e:14.2f} {nec:33.2f}   {'si' if ok else 'no'}")
        if not ok:
            inacc.append(k)
    assert len(inacc) == sum(1 for e in EQUIPOS.values() if CUERPO + e > PISTA + 1e-12)
    print("Inaccesibles con pista de 1.00 m:", ", ".join(inacc))
    print(" ancho de pista [m]   equipos accesibles")
    for w in (1.00, 1.20, 1.30, 1.40):
        n = sum(1 for e in EQUIPOS.values() if CUERPO + e <= w + 1e-12)
        print(f"{w:18.2f} {n:12d} de {len(EQUIPOS)}")
    assert len(inacc) == 2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
