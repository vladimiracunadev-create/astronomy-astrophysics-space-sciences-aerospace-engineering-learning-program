# SPDX-License-Identifier: Apache-2.0
"""Figuras SVG del taller T09 (Crew Dragon Demo-2). Uso: python figuras_T09.py"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403
import laboratorio_T09 as lab  # noqa: E402

SALIDA = Path(__file__).resolve().parent / "figuras"


def mapa() -> str:
    # Radios en radios terrestres; se exagera la altura para que se vea (la órbita real está a solo 6 % del radio).
    k = 4.0                      # factor de exageración de la altura sobre la superficie
    r_iss = 1 + 0.0659 * k
    r_ini = 1 + 0.0314 * k
    f = lab.fase()
    ang_fase = math.radians(75)  # la estación va adelantada
    espiral = []
    # vuelta 1 a 200 km, luego 2 vueltas de acercamiento a 200 km y finalmente transferencia
    for i in range(0, 361, 6):
        espiral.append((math.radians(-10 + i * 0.55), 1.0 + (r_ini - 1.0) * min(1.0, i / 60)))
    for i in range(0, 181, 6):
        espiral.append((math.radians(192 + i * 0.55), r_ini + (r_iss - r_ini) * (i / 180)))
    marcas = [(math.radians(-10), 1.0, "Lanzamiento", AZUL, 14, 22, "start"),
              (math.radians(192 + 99), r_iss, "Acoplamiento", VERDE, 12, -12, "start"),
              (math.radians(80), r_iss, "Estación", ROJO, 12, -12, "start")]
    return mapa_orbital("Crew Dragon: de la plataforma a la estación en 19 horas", "Vista desde el polo norte · la altura de las órbitas está exagerada 4 veces",
                        [("Órbita de la estación", r_iss, ROJO), ("Órbita de espera", r_ini, GRIS)], [(espiral, VERDE, 3.5)], marcas, 165.0,
                        [f"La nave sube a ≈ 200 km y, al ser más rápida, alcanza a la estación: gana ≈ {f['ganancia_por_vuelta']:.0f}° por vuelta.",
                         "Esquema: la geometría real exige un ángulo de fase y quemas precisas."],
                        "Esquema con la Tierra al centro, la órbita de la estación, una órbita más baja de espera y el recorrido de la nave hasta alcanzarla.",
                        centro="Tierra", color_centro=AZUL, rcentro=165, alto=700)


def tiempo() -> str:
    ev = [("30 may 2020", "Lanzamiento", "Falcon 9, plataforma 39A"), ("+12 min", "Separación", "en órbita baja"),
          ("≈ 19 h", "Acoplamiento", "31 mayo, a la estación"), ("62 días", "En la estación", "con cuatro paseos espaciales"),
          ("1 ago 2020", "Desacople", "regreso a la Tierra"), ("2 ago 2020", "Quema de salida", "≈ 100 m/s"),
          ("2 ago 2020", "Entrada", "≈ 7,8 km/s, hasta ≈ 4 g"), ("2 ago 2020", "Amerizaje", "Golfo de México")]
    return linea_tiempo("Demo-2: 64 días de misión", "Fechas de referencia pública, redondeadas: verifica en la fuente.", ev,
                        (6, "Entrada y amerizaje"), "Los dos tripulantes fueron los primeros en volar en un vehículo comercial para la NASA.",
                        "Línea de tiempo con ocho hitos del lanzamiento del 30 de mayo al amerizaje del 2 de agosto de 2020.")


def riesgo() -> str:
    q = lab.riesgo()
    datos = [("Transbordador (2 pérdidas en 135 vuelos)", q["diez_shuttle"] * 100, ROJO), ("Requisito actual (1 en 270)", q["diez_req"] * 100, AMBAR),
             ("Objetivo ambicioso (1 en 1.000)", q["diez_obj"] * 100, VERDE)]
    return barras("Probabilidad de que una tripulación vuelva sana en 10 vuelos", "Porcentaje con cada nivel de riesgo por vuelo (supuesto de vuelos independientes)",
                  datos, "%", "Un riesgo que parece pequeño por vuelo se acumula: tras diez vuelos, el transbordador implicaba un 14 % de perder una tripulación.",
                  "Tres barras: 86,1 % con el riesgo del transbordador, 96,4 % con el requisito de 1 en 270 y 99,0 % con 1 en 1.000.", 1)


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for n, f in (("ruta_a_la_estacion", mapa), ("linea_de_tiempo", tiempo), ("riesgo_acumulado", riesgo)):
        (SALIDA / f"{n}.svg").write_text(f(), encoding="utf-8")
        print("figuras/" + n + ".svg")


if __name__ == "__main__":
    main()
