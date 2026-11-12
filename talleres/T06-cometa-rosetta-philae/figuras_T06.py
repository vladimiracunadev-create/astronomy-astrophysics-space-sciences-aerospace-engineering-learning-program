# SPDX-License-Identifier: Apache-2.0
"""Figuras SVG del taller T06 (Rosetta y Philae). Uso: python figuras_T06.py"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403
import laboratorio_T06 as lab  # noqa: E402

SALIDA = Path(__file__).resolve().parent / "figuras"


def comp(r: float) -> float:
    return math.sqrt(r)


def mapa() -> str:
    hitos = [(100, 1.0, "Lanzamiento 2004"), (150, 1.0, "Tierra 2005"), (250, 1.5, "Marte 2007"), (330, 1.0, "Tierra 2007"),
             (30, 2.1, "Šteins 2008"), (110, 1.0, "Tierra 2009"), (200, 2.5, "Lutetia 2010"), (290, 5.3, "Hibernación"), (20, 3.4, "Cometa 2014")]
    ruta = []
    for (a0, r0, _), (a1, r1, _) in zip(hitos[:-1], hitos[1:]):
        da = a1 - a0 if a1 > a0 else a1 + 360 - a0
        for k in range(0, 21):
            f = k / 20
            ruta.append((math.radians(a0 + da * f), comp(r0 + (r1 - r0) * f)))
    orbitas = [("Tierra", comp(1.0), AZUL), ("Marte", comp(1.52), ROJO), ("Cinturón", comp(2.8), GRIS), ("Júpiter", comp(5.2), AMBAR)]
    desp = [(14, -12, "start"), (-12, 22, "end"), (-12, 20, "end"), (12, 20, "start"), (12, -12, "start"), (12, 20, "start"),
            (-12, 4, "end"), (12, -10, "start"), (14, 22, "start")]
    marcas = [(math.radians(a), comp(r), n, [AZUL, AZUL, ROJO, AZUL, GRIS, AZUL, GRIS, MORADO, VERDE][i], desp[i][0], desp[i][1], desp[i][2])
              for i, (a, r, n) in enumerate(hitos)]
    return mapa_orbital("Rosetta: diez años para alcanzar un cometa", "Plano de la eclíptica visto desde el norte · esquema, escala radial comprimida (raíz cuadrada)",
                        orbitas, [(ruta, VERDE, 3.5)], marcas, 62.0,
                        ["Tres pasos por la Tierra y uno por Marte le dieron la energía; en el camino sobrevoló dos asteroides.",
                         "Los ángulos y radios de los hitos son aproximados."],
                        "Esquema de la trayectoria de Rosetta con sus asistencias gravitatorias hasta el cometa.", centro="Sol")


def tiempo() -> str:
    ev = [("Mar 2004", "Lanzamiento", "Ariane 5 desde Kourou"), ("2005 a 2009", "Cuatro asistencias", "tres Tierra y una Marte"),
          ("2008 y 2010", "Dos asteroides", "Šteins y Lutetia"), ("Jun 2011", "Hibernación", "≈ 957 días, a 5,3 UA"),
          ("20 ene 2014", "Despertar", "señal de la nave"), ("6 ago 2014", "Llegada al cometa", "tras 10 años"),
          ("12 nov 2014", "Philae baja", "con dos rebotes"), ("30 sep 2016", "Fin de misión", "descenso controlado")]
    return linea_tiempo("Rosetta y Philae: 12 años en ocho hitos", "Fechas de referencia pública, redondeadas: verifica en la fuente.", ev,
                        (5, "Dos años junto a un cuerpo de gravedad casi nula"),
                        "Un solo cohete, diez años de viaje y un aterrizaje en un cuerpo cuya fuerza de gravedad es una cienmilésima de la terrestre.",
                        "Línea de tiempo con ocho hitos del lanzamiento de 2004 al final de la misión en 2016.")


def flujo() -> str:
    pts = [(d / 10, flujo_solar(d / 10)) for d in range(10, 61, 2)]
    return lineas("Cuánta luz solar llega a los paneles", "Flujo solar en W/m² frente a la distancia al Sol (escala logarítmica en el eje vertical)",
                  [("Flujo solar", pts, AMBAR)], "Distancia al Sol (UA)", "W/m²", [1, 2, 3, 4, 5, 6], [30, 100, 300, 1000],
                  [(1.24, flujo_solar(1.24), "Perihelio"), (3.4, flujo_solar(3.4), "Llegada"), (5.3, flujo_solar(5.3), "Hibernación")], logy=True,
                  nota="A 5,3 UA llega 28 veces menos luz que a la Tierra: la nave se apagó casi por completo para sobrevivir.",
                  desc="Curva decreciente del flujo solar con tres marcas: 1,24 UA en el perihelio, 3,4 UA en la llegada y 5,3 UA en la hibernación.")


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for n, f in (("trayectoria_rosetta", mapa), ("linea_de_tiempo", tiempo), ("flujo_solar", flujo)):
        (SALIDA / f"{n}.svg").write_text(f(), encoding="utf-8")
        print("figuras/" + n + ".svg")


if __name__ == "__main__":
    main()
