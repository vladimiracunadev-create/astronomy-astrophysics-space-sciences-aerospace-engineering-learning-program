#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C19: clasificacion TRL por evidencia y eslabon mas debil.

Datos CONSULTADOS (2026-11-10): escala TRL 1-9 de la NASA (pagina Technology Readiness Levels): 1 investigacion inicial; 2 principios estudiados y aplicaciones
consideradas; 3 investigacion y diseno activos con estudios analiticos y de laboratorio, prueba de concepto; 4 prueba de concepto lista, varios componentes probados juntos;
5 tecnologia de 'breadboard' probada en entornos simulados realistas; 6 prototipo funcional completo o modelo representativo; 7 modelo o prototipo demostrado en el espacio;
8 tecnologia probada y 'calificada para vuelo'; 9 tecnologia 'probada en vuelo' en una mision exitosa.
SINTETICOS (inventados para el ejercicio; NO describen ninguna tecnologia real): las tecnologias A-E y los hitos de evidencia que cada una declara.
Modelo: cada nivel L exige un hito de evidencia; TRL = mayor L tal que los hitos 1..L estan todos presentes (cadena contigua). Un sistema vale el minimo de sus componentes.
Segunda via: calculo por la funcion alternativa 'primer hito ausente - 1' y comparacion con el maximo nivel con evidencia y con la media.
Tolerancia: ambas vias de TRL coinciden exactamente (enteros).
"""
from __future__ import annotations
import platform

NIVELES = {
    1: "investigacion inicial", 2: "principios estudiados", 3: "estudios analiticos y de laboratorio; prueba de concepto",
    4: "componentes probados juntos", 5: "breadboard en entorno simulado realista", 6: "prototipo funcional o modelo representativo",
    7: "demostracion en el espacio", 8: "calificado para vuelo", 9: "probado en vuelo en una mision exitosa",
}

# tecnologias SINTETICAS: conjunto de hitos con evidencia
TECNOLOGIAS = {
    "A (sintetica)": {1, 2, 3, 4, 5, 6, 7, 8, 9},
    "B (sintetica)": {1, 2, 3, 4, 5, 6, 7},
    "C (sintetica)": {1, 2, 3, 5, 6},        # salta el hito 4
    "D (sintetica)": {1, 2, 3},
    "E (sintetica)": {1, 2, 3, 4, 6, 7, 8},   # salta el 5
}


def trl_cadena(hitos: set[int]) -> int:
    n = 0
    for lvl in range(1, 10):
        if lvl in hitos:
            n = lvl
        else:
            break
    return n


def trl_alt(hitos: set[int]) -> int:
    ausentes = [l for l in range(1, 10) if l not in hitos]
    return (min(ausentes) - 1) if ausentes else 9


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Escala TRL de la NASA (consultada; resumen propio):")
    for k, v in NIVELES.items():
        print(f"  TRL {k}: {v}")
    print("Tecnologias SINTETICAS (evidencia declarada -> TRL por cadena contigua):")
    print("  tecnologia       hitos con evidencia            TRL cadena  TRL maximo con evidencia  media de niveles con evidencia")
    for n, h in TECNOLOGIAS.items():
        a, b = trl_cadena(h), trl_alt(h)
        assert a == b
        mx = max(h)
        media = sum(h) / len(h)
        print(f"  {n:<15} {str(sorted(h)):<30} {a:>10} {mx:>25} {media:>19.2f}")
    # sistema: minimo de sus componentes
    sistema = ("A (sintetica)", "B (sintetica)", "C (sintetica)")
    trls = [trl_cadena(TECNOLOGIAS[x]) for x in sistema]
    print(f"Sistema formado por {', '.join(sistema)}: TRL de componentes = {trls} -> TRL del sistema = min = {min(trls)} (la media daria {sum(trls)/len(trls):.2f})")
    assert min(trls) == 3 and sum(trls) / len(trls) > min(trls)
    # sensibilidad: que hito falta para subir cada tecnologia
    print("Hito siguiente que falta para subir un nivel (cadena):")
    for n, h in TECNOLOGIAS.items():
        t = trl_cadena(h)
        print(f"  {n:<15} TRL {t} -> falta evidencia del hito {t+1}" if t < 9 else f"  {n:<15} TRL 9")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
