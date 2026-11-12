# SPDX-License-Identifier: Apache-2.0
"""Figuras SVG del taller T04 (telescopio James Webb). Uso: python figuras_T04.py"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403
import laboratorio_T04 as lab  # noqa: E402

SALIDA = Path(__file__).resolve().parent / "figuras"


def geometria() -> str:
    y = 260
    c = [encabezado("Dónde está el telescopio: el punto L2 Sol-Tierra", "Esquema fuera de escala visto desde arriba del plano de la eclíptica")]
    c.append(f'<line x1="60" y1="{y}" x2="920" y2="{y}" stroke="{GRIS}" stroke-dasharray="5 5"/>')
    c.append(f'<circle cx="110" cy="{y}" r="34" fill="{AMBAR}"/>' + t(110, y + 60, "Sol", 14, TINTA, "middle", "bold"))
    c.append(f'<circle cx="520" cy="{y}" r="14" fill="{AZUL}"/>' + t(520, y + 36, "Tierra", 14, AZUL, "middle", "bold"))
    c.append(f'<circle cx="640" cy="{y}" r="6" fill="{TINTA}"/>' + t(640, y + 28, "L2", 14, TINTA, "middle", "bold"))
    c.append(f'<ellipse cx="640" cy="{y}" rx="60" ry="96" fill="none" stroke="{VERDE}" stroke-width="3.5"/>')
    c.append(t(640, y - 112, "Órbita alrededor de L2", 13, VERDE, "middle", "bold"))
    c.append(t(640, y - 130, "≈ 800.000 km de ancho, ≈ 6 meses", 12, SUAVE, "middle"))
    c.append(f'<line x1="520" y1="{y + 52}" x2="640" y2="{y + 52}" stroke="{SUAVE}"/>' + t(580, y + 72, "≈ 1,5 millones de km · 5 s luz", 13, TINTA, "middle"))
    c.append(t(110, y - 60, "Luz solar →", 13, AMBAR, "start", "bold"))
    c.append(t(24, 440, "En L2 el Sol, la Tierra y la Luna quedan siempre del mismo lado: un solo escudo basta para taparlos a los tres.", 13, TINTA))
    return svg(980, 470, "Geometría del punto L2", "Sol, Tierra y L2 alineados; el telescopio describe una órbita amplia alrededor de L2, a 1,5 millones de km de la Tierra.", "".join(c))


def tiempo() -> str:
    ev = [("25 dic 2021", "Lanzamiento", "Ariane 5, Kourou"), ("+33 min", "Paneles solares", "se separan y se abren"),
          ("+2 días", "Antena y carga", "primeros despliegues"), ("Día 3 a 7", "Escudo solar", "5 capas, 21 m x 14 m"),
          ("Día 14", "Espejo secundario", "y alas del primario"), ("24 ene 2022", "Llegada a L2", "quema de inserción"),
          ("Feb a May", "Alineación", "18 segmentos como uno"), ("12 jul 2022", "Primeras imágenes", "ciencia comienza")]
    return linea_tiempo("James Webb: del lanzamiento a la primera imagen", "Fechas de referencia pública, redondeadas: verifica en la fuente.", ev,
                        (2, "≈ 2 semanas de despliegues sin posibilidad de reparación"),
                        "A 1,5 millones de km nadie puede ir a arreglar nada: todo debe funcionar la primera vez.",
                        "Línea de tiempo con ocho hitos desde el lanzamiento hasta las primeras imágenes científicas.")


def fiabilidad() -> str:
    datos = [("99,900 % por punto", lab.despliegues(0.999) * 100, ROJO), ("99,950 % por punto", lab.despliegues(0.9995) * 100, AMBAR),
             ("99,990 % por punto", lab.despliegues(0.9999) * 100, AZUL), ("99,999 % por punto", lab.despliegues(0.99999) * 100, VERDE)]
    return barras("Probabilidad de que los 344 despliegues salgan bien", "Cadena en serie de puntos únicos de fallo", datos, "%",
                  f"Para un 90 % global hace falta {lab.exigido() * 100:.3f} % por punto: por eso se probó durante años.",
                  "Cuatro barras: con 99,9 % por punto el éxito global es 71 %; con 99,999 %, 99,7 %.", 1)


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for n, f in (("geometria_l2", geometria), ("linea_de_tiempo", tiempo), ("fiabilidad_de_los_despliegues", fiabilidad)):
        (SALIDA / f"{n}.svg").write_text(f(), encoding="utf-8")
        print("figuras/" + n + ".svg")


if __name__ == "__main__":
    main()
