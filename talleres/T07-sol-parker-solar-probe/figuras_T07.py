# SPDX-License-Identifier: Apache-2.0
"""Figuras SVG del taller T07 (Parker Solar Probe). Uso: python figuras_T07.py"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403
import laboratorio_T07 as lab  # noqa: E402

SALIDA = Path(__file__).resolve().parent / "figuras"


def elipse(rp: float, ra: float, rot: float) -> list[tuple[float, float]]:
    a, e = (rp + ra) / 2, (ra - rp) / (ra + rp)
    pts = []
    for k in range(0, 361, 4):
        th = math.radians(k)
        r = a * (1 - e * e) / (1 + e * math.cos(th))
        pts.append((th + rot, r))
    return pts


def mapa() -> str:
    rp1, ra1 = 0.166, 0.94           # primera órbita (UA)
    rp2, ra2 = lab.RP_FINAL / UA, lab.orbita_final()["ra_ua"]
    rot1, rot2 = math.radians(205), math.radians(205)
    orbitas = [("Mercurio", 0.387, GRIS), ("Venus", 0.723, ROJO), ("Tierra", 1.0, AZUL)]
    marcas = [(math.radians(25), 0.723, "Venus: freno gravitatorio", ROJO, 12, -10, "start"),
              (rot1, rp1, "", MORADO, 0, 0, "start"),
              (math.radians(5), 1.0, "Lanzamiento 2018", AZUL, 12, 20, "start")]
    return mapa_orbital("Parker: de la órbita de la Tierra a 6 millones de km del Sol", "Plano de la eclíptica visto desde el norte · escala lineal en UA (1 UA = 270 píxeles)",
                        orbitas, [(elipse(rp1, ra1, rot1), MORADO, 2.5), (elipse(rp2, ra2, rot2), VERDE, 3.5)], marcas, 270.0,
                        ["Verde: órbita final, período de 88 días, perihelio a 9,86 radios solares. Morado: primera órbita (perihelio a 35,7).",
                         "Siete pasos por Venus fueron acercando el perihelio al Sol sin gastar combustible."],
                        "Esquema de las órbitas de Mercurio, Venus y la Tierra con dos elipses: la primera y la final de Parker; la final llega casi al Sol.",
                        centro="Sol", rcentro=8, alto=700)


def tiempo() -> str:
    ev = [("12 ago 2018", "Lanzamiento", "Delta IV Heavy, C3 récord"), ("3 oct 2018", "Venus 1", "primer freno"),
          ("5 nov 2018", "Primer perihelio", "35,7 radios solares"), ("2018 a 2024", "Siete Venus", "perihelio cada vez menor"),
          ("29 abr 2021", "Entra en la corona", "cruza la superficie de Alfvén"), ("6 nov 2024", "Venus 7", "último freno"),
          ("24 dic 2024", "Perihelio récord", "9,86 radios solares"), ("2025", "Fin de la misión primaria", "órbitas de 88 días")]
    return linea_tiempo("Parker Solar Probe: 7 años acercándose al Sol", "Fechas de referencia pública, redondeadas: verifica en la fuente.", ev,
                        (6, "Perihelios dentro de la corona"), "En el perihelio la nave va a ≈ 690.000 km/h, el objeto más rápido construido por personas.",
                        "Línea de tiempo con ocho hitos del lanzamiento de 2018 al perihelio récord de 2024.")


def calor() -> str:
    pts = [("Tierra (1 UA)", S_1UA / 1000, AZUL), ("Venus (0,72 UA)", S_1UA / 0.723**2 / 1000, ROJO), ("Mercurio (0,39 UA)", S_1UA / 0.387**2 / 1000, AMBAR),
           ("Primer perihelio (0,166 UA)", lab.termica()["S_primero"] / 1000, MORADO), ("Perihelio récord (0,046 UA)", lab.termica()["flujo"] / 1000, VERDE)]
    return barras("Cuánta energía solar llega a cada lugar", "Flujo solar en kW por metro cuadrado", pts, "kW/m²",
                  "En el perihelio récord el flujo es 476 veces el de la Tierra: por eso el escudo y los paneles son el corazón del diseño.",
                  "Cinco barras: desde 1,4 kW/m² en la Tierra hasta 647 kW/m² en el perihelio récord.", 1)


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for n, f in (("trayectoria_parker", mapa), ("linea_de_tiempo", tiempo), ("flujo_de_calor", calor)):
        (SALIDA / f"{n}.svg").write_text(f(), encoding="utf-8")
        print("figuras/" + n + ".svg")


if __name__ == "__main__":
    main()
