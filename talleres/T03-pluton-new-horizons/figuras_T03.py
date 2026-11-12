# SPDX-License-Identifier: Apache-2.0
"""Figuras SVG del taller T03 (New Horizons). Uso: python figuras_T03.py"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403
import laboratorio_T03 as lab  # noqa: E402

SALIDA = Path(__file__).resolve().parent / "figuras"


def comp(r: float) -> float:
    return math.sqrt(r)  # escala radial comprimida (raíz cuadrada)


def mapa() -> str:
    a_tierra, a_jup, a_plu = math.radians(120), math.radians(240), math.radians(287)
    ida = []
    for k in range(0, 41):
        f = k / 40
        ida.append((a_tierra + (a_jup - a_tierra) * f, comp(1.0 + 4.2 * f ** 1.3)))
    sal = []
    for k in range(0, 41):
        f = k / 40
        sal.append((a_jup + (a_plu - a_jup) * f ** 0.8, comp(5.2 + (31.9 - 5.2) * f)))
    orbitas = [("Tierra", comp(1.0), AZUL), ("Júpiter", comp(5.2), AMBAR), ("Plutón", comp(31.9), GRIS)]
    marcas = [(a_tierra, comp(1.0), "Lanzamiento · 2006", AZUL, 12, -10, "start"),
              (a_jup, comp(5.2), "Júpiter · 2007", AMBAR, -12, 20, "end"),
              (a_plu, comp(31.9), "Plutón · 2015", ROJO, -12, -10, "end")]
    return mapa_orbital("New Horizons: de la Tierra a Plutón", "Plano de la eclíptica visto desde el norte · escala radial comprimida (raíz cuadrada)",
                        orbitas, [(ida, VERDE, 3.5), (sal, MORADO, 3.5)], marcas, 50.0,
                        ["Sale a ≈ 16 km/s, el lanzamiento más rápido de su época; Júpiter la acelera ≈ 4 km/s y recorta ≈ 3 años.",
                         "Los ángulos son aproximados (esquema); el radio de las órbitas no está a escala lineal."],
                        "Esquema de la trayectoria: sale de la Tierra, pasa por Júpiter y llega a Plutón en nueve años y medio.",
                        centro="Sol")


def tiempo() -> str:
    ev = [("Ene 2006", "Lanzamiento", "Atlas V + tercera etapa"), ("Feb 2007", "Júpiter", "asistencia gravitatoria"),
          ("2007-2014", "Hibernación", "≈ 1.870 días en reposo"), ("Dic 2014", "Despertar", "fin de la hibernación"),
          ("4 jul 2015", "Modo seguro", "10 días antes del sobrevuelo"), ("14 jul 2015", "Sobrevuelo", "a ≈ 12.500 km"),
          ("Oct 2016", "Fin de la descarga", "≈ 16 meses de transmisión"), ("1 ene 2019", "Arrokoth", "segundo objetivo")]
    return linea_tiempo("New Horizons: 13 años en ocho hitos", "Fechas de referencia pública, redondeadas: verifica en la fuente.", ev,
                        (4, "10 días entre la anomalía y el sobrevuelo"), "El encuentro dura horas; el viaje, casi una década; recibir los datos, más de un año.",
                        "Línea de tiempo con ocho hitos desde el lanzamiento de 2006 hasta el sobrevuelo de Arrokoth.")


def velocidad() -> str:
    l = lab.lanzamiento()
    sin = lab.perfil_velocidad(l["exceso"], 0.0)
    con = lab.perfil_velocidad(l["exceso"], 4.0)
    return lineas("Velocidad frente a distancia al Sol", "Modelo radial con conservación de la energía; con y sin la asistencia de Júpiter (+4 km/s)",
                  [("Sin Júpiter", sin, GRIS), ("Con Júpiter", con, VERDE)], "Distancia al Sol (UA)", "km/s", [0, 5, 10, 15, 20, 25, 30, 35], [0, 10, 20, 30, 40],
                  [(5.2, con[[p[0] for p in con].index(5.2)][1] if 5.2 in [p[0] for p in con] else 20, "Júpiter")],
                  nota="El Sol frena a la nave durante todo el viaje; la asistencia de Júpiter es como volver a lanzarla a mitad de camino.",
                  desc="Dos curvas que bajan con la distancia; la de la asistencia de Júpiter queda siempre por encima de la otra.")


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for n, f in (("trayectoria_new_horizons", mapa), ("linea_de_tiempo", tiempo), ("velocidad_frente_a_distancia", velocidad)):
        (SALIDA / f"{n}.svg").write_text(f(), encoding="utf-8")
        print("figuras/" + n + ".svg")


if __name__ == "__main__":
    main()
