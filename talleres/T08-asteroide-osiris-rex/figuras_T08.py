# SPDX-License-Identifier: Apache-2.0
"""Figuras SVG del taller T08 (OSIRIS-REx). Uso: python figuras_T08.py"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403
import laboratorio_T08 as lab  # noqa: E402

SALIDA = Path(__file__).resolve().parent / "figuras"


def elipse(rp: float, ra: float, rot: float) -> list[tuple[float, float]]:
    a, e = (rp + ra) / 2, (ra - rp) / (ra + rp)
    return [(math.radians(k) + rot, a * (1 - e * e) / (1 + e * math.cos(math.radians(k)))) for k in range(0, 361, 4)]


def mapa() -> str:
    bennu = elipse(0.897, 1.356, math.radians(60))
    # ruta esquemática: Tierra -> vuelta de un año -> sobrevuelo de la Tierra -> Bennu -> regreso
    hitos = [(0, 1.0), (120, 1.18), (240, 1.0), (360, 1.0), (440, 1.1), (500, 1.2), (560, 1.15), (640, 1.0), (720, 1.0)]
    ruta = []
    for (a0, r0), (a1, r1) in zip(hitos[:-1], hitos[1:]):
        for k in range(0, 13):
            f = k / 12
            ruta.append((math.radians(a0 + (a1 - a0) * f), r0 + (r1 - r0) * f))
    marcas = [(0, 1.0, "Lanzamiento · sep 2016", AZUL, 14, 22, "start"),
              (math.radians(500), 1.2, "Bennu · dic 2018", ROJO, 12, -14, "start"),
              (math.radians(720), 1.0, "Retorno · sep 2023", VERDE, 14, -12, "start")]
    return mapa_orbital("OSIRIS-REx: ida a Bennu y regreso con la muestra", "Plano de la eclíptica visto desde el norte · esquema en UA (1 UA = 220 píxeles)",
                        [("Tierra", 1.0, AZUL)], [(bennu, GRIS, 2.0), (ruta, VERDE, 3.5)], marcas, 220.0,
                        ["Gris: órbita de Bennu (e = 0,20, inclinada 6°). Verde: recorrido esquemático de la nave (no está a escala).",
                         "Tras una vuelta al Sol y un paso por la Tierra, alcanzó a Bennu; el regreso duró 2,4 años."],
                        "Esquema con la órbita de la Tierra, la de Bennu y el recorrido de ida y vuelta de la nave.", centro="Sol", rcentro=10)


def tiempo() -> str:
    ev = [("8 sep 2016", "Lanzamiento", "Atlas V"), ("22 sep 2017", "Paso por la Tierra", "asistencia gravitatoria"),
          ("3 dic 2018", "Llegada a Bennu", "tras 2 años"), ("2019", "Órbitas cercanas", "a ≈ 1 km del cuerpo"),
          ("20 oct 2020", "Toma de muestra", "contacto de ≈ 5 s"), ("10 may 2021", "Salida de Bennu", "con la muestra"),
          ("24 sep 2023", "Cápsula en Utah", "entrada a 12,4 km/s"), ("2024", "Apertura y análisis", "≈ 121,6 g de muestra")]
    return linea_tiempo("OSIRIS-REx: 7 años de ida y vuelta", "Fechas de referencia pública, redondeadas: verifica en la fuente.", ev,
                        (4, "Del muestreo al laboratorio: 3 años"), "La parte más corta de la misión, ≈ 5 s de contacto, decide todo su resultado.",
                        "Línea de tiempo con ocho hitos del lanzamiento de 2016 a la apertura de la muestra en 2024.")


def orbita() -> str:
    pts = [(r / 1000, lab.periodo_orbita(r)) for r in range(300, 3001, 50)]
    return lineas("Cuánto dura una órbita alrededor de Bennu", "Período en horas según el radio de la órbita (modelo de cuerpo esférico)",
                  [("Período", pts, VERDE)], "Radio de la órbita desde el centro (km)", "horas", [0.5, 1.0, 1.5, 2.0, 2.5, 3.0], [0, 40, 80, 120],
                  [(0.7, lab.periodo_orbita(700), "0,7 km"), (1.75, lab.periodo_orbita(1750), "1,75 km")],
                  nota="Una vuelta tarda de horas a días: con una gravedad tan débil, orbitar es un ejercicio de paciencia y de precisión.",
                  desc="Curva creciente del período con el radio: 15 horas a 0,7 km y 58 horas a 1,75 km.")


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for n, f in (("trayectoria_osiris_rex", mapa), ("linea_de_tiempo", tiempo), ("periodo_orbital", orbita)):
        (SALIDA / f"{n}.svg").write_text(f(), encoding="utf-8")
        print("figuras/" + n + ".svg")


if __name__ == "__main__":
    main()
