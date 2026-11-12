# SPDX-License-Identifier: Apache-2.0
"""Figuras SVG del taller T05 (Cassini-Huygens). Uso: python figuras_T05.py"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403
import laboratorio_T05 as lab  # noqa: E402

SALIDA = Path(__file__).resolve().parent / "figuras"


def comp(r: float) -> float:
    return math.sqrt(r)


def mapa() -> str:
    # Esquema: puntos (ángulo°, radio UA) de los hitos; la nave pasa por Venus dos veces, la Tierra, Júpiter y llega a Saturno.
    hitos = [(10, 1.0, "Lanzamiento 1997"), (200, 0.72, "Venus 1"), (330, 1.3, "Maniobra"), (120, 0.72, "Venus 2"), (220, 1.0, "Tierra"),
             (250, 5.2, "Júpiter"), (320, 9.5, "Saturno 2004")]
    ruta = []
    for (a0, r0, _), (a1, r1, _) in zip(hitos[:-1], hitos[1:]):
        da = a1 - a0 if a1 > a0 else a1 + 360 - a0
        for k in range(0, 21):
            f = k / 20
            ruta.append((math.radians(a0 + da * f), comp(r0 + (r1 - r0) * f)))
    orbitas = [("Venus", comp(0.72), ROJO), ("Tierra", comp(1.0), AZUL), ("Júpiter", comp(5.2), AMBAR), ("Saturno", comp(9.54), GRIS)]
    marcas = []
    desp = {0: (12, 18, "start"), 1: (-12, -10, "end"), 2: (12, 20, "start"), 3: (-12, 18, "end"), 4: (-12, -10, "end"), 5: (-12, 20, "end"), 6: (12, -10, "start")}
    cols = [AZUL, ROJO, VERDE, ROJO, AZUL, AMBAR, MORADO]
    for i, (a, r, n) in enumerate(hitos):
        dx, dy, anc = desp[i]
        marcas.append((math.radians(a), comp(r), n, cols[i], dx, dy, anc))
    return mapa_orbital("Cassini: cuatro sobrevuelos para llegar a Saturno", "Plano de la eclíptica visto desde el norte · esquema, escala radial comprimida (raíz cuadrada)",
                        orbitas, [(ruta, VERDE, 3.5)], marcas, 62.0,
                        ["Lanzada con energía para llegar a Venus, ganó el resto con dos pasos por Venus, uno por la Tierra y uno por Júpiter.",
                         "Los ángulos y los radios de los hitos son aproximados."],
                        "Esquema de la trayectoria con sus cuatro sobrevuelos, desde la Tierra en 1997 hasta Saturno en 2004.", centro="Sol")


def tiempo() -> str:
    ev = [("Oct 1997", "Lanzamiento", "Titan IV y Centaur"), ("Abr 1998", "Venus 1", "primer sobrevuelo"),
          ("Jun a Ago 1999", "Venus 2 y Tierra", "dos asistencias"), ("Dic 2000", "Júpiter", "último impulso"),
          ("1 jul 2004", "Llegada a Saturno", "freno de ≈ 96 min"), ("14 ene 2005", "Huygens en Titán", "descenso de ≈ 2,5 h"),
          ("2004 a 2017", "Gira por Saturno", "≈ 290 órbitas"), ("15 sep 2017", "Entrada final", "en la atmósfera de Saturno")]
    return linea_tiempo("Cassini-Huygens: 20 años en ocho hitos", "Fechas de referencia pública, redondeadas: verifica en la fuente.", ev,
                        (4, "13 años de ciencia en torno a Saturno"), "Seis años y medio de viaje para trece de exploración; el final fue una zambullida planificada.",
                        "Línea de tiempo con ocho hitos del lanzamiento de 1997 a la entrada final de 2017.")


def energia() -> str:
    sv = lab.sobrevuelo
    datos = [("Energía necesaria al salir (v∞)", 10.29, GRIS), ("Aporte del cohete (v∞ ≈ 4,1)", 4.1, AZUL),
             ("Giro por la Tierra, 1999", sv(16.9, MU_TIERRA, R_TIERRA + 1166)["dv"], VERDE),
             ("Giro por Júpiter, 2000", sv(5.7, MU_JUPITER, 9.7e6)["dv"], AMBAR), ("Freno de inserción en Saturno", lab.insercion()["dv"], ROJO)]
    return barras("Cuánto aporta cada ayuda", "Velocidades en km/s del modelo de dos cuerpos (orden de magnitud)", datos, "km/s",
                  "Sin asistencias, el cohete no alcanzaba: la gravedad de los planetas completó lo que faltaba.",
                  "Cinco barras: la energía necesaria al salir es mayor que el aporte del cohete; los sobrevuelos cambian la velocidad en varios km/s.", 2)


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for n, f in (("trayectoria_cassini", mapa), ("linea_de_tiempo", tiempo), ("aportes_de_velocidad", energia)):
        (SALIDA / f"{n}.svg").write_text(f(), encoding="utf-8")
        print("figuras/" + n + ".svg")


if __name__ == "__main__":
    main()
