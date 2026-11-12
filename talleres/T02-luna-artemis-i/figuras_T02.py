# SPDX-License-Identifier: Apache-2.0
"""Figuras SVG del taller T02 (Artemis I). Uso: python figuras_T02.py"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403
import laboratorio_T02 as lab  # noqa: E402

SALIDA = Path(__file__).resolve().parent / "figuras"


def ruta_translunar() -> str:
    # Esquema (no a escala) en el plano orbital: la Tierra al centro y la Luna a 384.400 km (radio 1 en el mapa).
    ida = [(math.radians(a), 0.05 + 0.95 * (a / 175) ** 0.9) for a in range(0, 176, 5)]
    # lazo de la órbita retrógrada distante alrededor de la Luna (radio dibujado exagerado)
    cx, cy = math.cos(math.pi), math.sin(math.pi)
    lazo = []
    for k in range(0, 361, 10):
        ang = math.radians(k)
        x = cx + 0.22 * math.cos(ang)
        y = cy + 0.22 * math.sin(ang)
        lazo.append((math.atan2(y, x) % (2 * math.pi), math.hypot(x, y)))
    vuelta = [(math.radians(185 + a), 1.0 - 0.95 * (a / 175) ** 0.9) for a in range(0, 176, 5)]
    marcas = [(0, 0.05, "Lanzamiento y órbita baja", AZUL, 14, 22, "start"),
              (math.pi, 1.0, "Luna", GRIS, -24, -26, "end"),
              (math.radians(332), 0.34, "Inyección translunar", VERDE, 12, 20, "start"),
              (math.radians(188), 0.40, "Regreso", ROJO, -12, 22, "end")]
    return mapa_orbital("Trayectoria de Artemis I (esquema)", "Plano orbital visto desde el norte · no está a escala",
                        [("Órbita de la Luna", 1.0, GRIS)], [(ida, VERDE, 3.5), (lazo, MORADO, 3.5), (vuelta, ROJO, 3.5)], marcas, 240.0,
                        ["Ida ≈ 5 días · órbita retrógrada distante ≈ 6 días · retorno ≈ 6 días · total ≈ 25,5 días.",
                         "Distancia máxima ≈ 432.000 km de la Tierra, la mayor alcanzada por una nave diseñada para personas."],
                        "Esquema de la ruta de Artemis I: sale de la Tierra, pasa junto a la Luna, entra en una órbita retrógrada distante y regresa.",
                        centro="Tierra", color_centro=AZUL, rcentro=10)


def linea_de_tiempo() -> str:
    ev = [("Día 0", "Lanzamiento", "SLS, plataforma 39B"), ("Día 0 (≈ 1,5 h)", "Inyección translunar", "motor de la etapa superior"),
          ("Día 5", "Sobrevuelo lunar", "a ≈ 130 km"), ("Día 9", "Entrada en la DRO", "quema de inserción"),
          ("Día 12", "Distancia máxima", "≈ 432.000 km"), ("Día 15", "Salida de la DRO", "quema de salida"),
          ("Día 19", "Sobrevuelo de regreso", "con motor, ≈ 130 km"), ("Día 25,5", "Amerizaje", "Pacífico, Baja California")]
    return linea_tiempo("Artemis I: 25,5 días en ocho hitos", "Fechas relativas al lanzamiento del 16 de noviembre de 2022 (UTC). Cifras redondeadas: verifica en la fuente.",
                        ev, (6, "Reentrada con rebote: ≈ 11 km/s"), "El retorno desde la Luna es la prueba que no se podía hacer desde órbita baja: 2,8 veces más flujo de calor.",
                        "Línea de tiempo con ocho hitos de la misión Artemis I.")


def reentrada() -> str:
    r = lab.reentrada()
    datos = [("Entrada en Marte (Mars 2020)", 5.4, AZUL), ("Reentrada desde órbita baja", r["v_leo"], VERDE), ("Reentrada desde la Luna (Artemis I)", r["v_lunar"], ROJO)]
    return barras("Velocidad de entrada en la atmósfera", "Velocidad al llegar a la interfaz de entrada (km/s)", datos, "km/s",
                  f"La energía por kilo es {r['razon_e']:.1f} veces mayor que desde órbita baja ({r['e_lunar']:.0f} frente a {r['e_leo']:.0f} MJ/kg).",
                  "Tres barras con la velocidad de entrada: 5,4 km/s en Marte, 7,8 desde órbita baja y 11,1 desde la Luna.", 1)


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for n, f in (("trayectoria_artemis_i", ruta_translunar), ("linea_de_tiempo", linea_de_tiempo), ("velocidad_de_entrada", reentrada)):
        (SALIDA / f"{n}.svg").write_text(f(), encoding="utf-8")
        print("figuras/" + n + ".svg")


if __name__ == "__main__":
    main()
