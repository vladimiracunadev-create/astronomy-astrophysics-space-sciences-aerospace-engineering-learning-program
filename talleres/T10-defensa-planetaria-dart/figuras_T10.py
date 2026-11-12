# SPDX-License-Identifier: Apache-2.0
"""Figuras SVG del taller T10 (DART). Uso: python figuras_T10.py"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403
import laboratorio_T10 as lab  # noqa: E402

SALIDA = Path(__file__).resolve().parent / "figuras"


def geometria() -> str:
    cx, cy = 400.0, 300.0
    r_orb = 170.0
    ang = math.radians(35)
    dx, dy = cx + r_orb * math.cos(ang), cy - r_orb * math.sin(ang)
    c = [encabezado("El impacto de DART sobre Dimorphos", "Esquema fuera de escala visto desde el polo del sistema")]
    c.append(f'<circle cx="{cx}" cy="{cy}" r="{r_orb}" fill="none" stroke="{GRIS}" stroke-width="1.5" stroke-dasharray="5 5"/>')
    c.append(f'<circle cx="{cx}" cy="{cy}" r="52" fill="{AMBAR}" opacity="0.9"/>')
    c.append(t(cx, cy + 5, "Didymos", 14, TINTA, "middle", "bold"))
    c.append(t(cx, cy + 76, "≈ 780 m", 12, SUAVE, "middle"))
    c.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="14" fill="{AZUL}"/>')
    c.append(t(dx + 22, dy + 28, "Dimorphos ≈ 160 m", 13, AZUL, "start", "bold"))
    # velocidad orbital (tangente, sentido antihorario)
    tx, ty = -math.sin(ang), -math.cos(ang)
    c.append(f'<line x1="{dx:.1f}" y1="{dy:.1f}" x2="{dx + 70 * tx:.1f}" y2="{dy + 70 * ty:.1f}" stroke="{VERDE}" stroke-width="3.5"/>')
    c.append(f'<polygon points="{dx + 70 * tx:.1f},{dy + 70 * ty:.1f} {dx + 56 * tx - 7 * ty:.1f},{dy + 56 * ty + 7 * tx:.1f} {dx + 56 * tx + 7 * ty:.1f},{dy + 56 * ty - 7 * tx:.1f}" fill="{VERDE}"/>')
    c.append(t(dx + 70 * tx - 8, dy + 70 * ty - 12, "Su velocidad: ≈ 17 cm/s", 13, VERDE, "end", "bold"))
    # nave que llega de frente (sentido contrario al movimiento)
    sx, sy = dx - 260 * tx, dy - 260 * ty
    c.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{dx - 18 * tx:.1f}" y2="{dy - 18 * ty:.1f}" stroke="{ROJO}" stroke-width="3.5"/>')
    c.append(f'<polygon points="{dx - 18 * tx:.1f},{dy - 18 * ty:.1f} {dx - 34 * tx - 7 * ty:.1f},{dy - 34 * ty + 7 * tx:.1f} {dx - 34 * tx + 7 * ty:.1f},{dy - 34 * ty - 7 * tx:.1f}" fill="{ROJO}"/>')
    c.append(t(sx + 8, sy + 4, "Nave: 580 kg a 6,1 km/s", 13, ROJO, "start", "bold"))
    c.append(t(24, 540, "El golpe va de frente, contra el sentido del movimiento: frena a Dimorphos unos 3 mm/s y acorta su período.", 13, TINTA))
    c.append(t(24, 562, "Los restos expulsados empujan más que la nave sola; ese refuerzo se mide con el factor β.", 13, SUAVE))
    return svg(980, 590, "Geometría del impacto de DART",
               "Didymos al centro, la órbita de Dimorphos alrededor y la nave llegando de frente, en sentido contrario al movimiento de Dimorphos.", "".join(c))


def tiempo() -> str:
    ev = [("24 nov 2021", "Lanzamiento", "Falcon 9, Vandenberg"), ("27 jul 2022", "Primera imagen", "del sistema, a 32 millones de km"),
          ("11 sep 2022", "Sale LICIACube", "microsatélite italiano"), ("26 sep 2022", "Impacto", "23:14 UTC, a 6,1 km/s"),
          ("27 sep 2022", "Telescopios en tierra", "ven la cola de restos"), ("11 oct 2022", "Resultado", "32 min menos"),
          ("oct 2024", "Sale Hera", "misión europea de revisión"), ("2026", "Hera llega", "mide el cráter")]
    return linea_tiempo("DART: del lanzamiento al resultado en 10 meses", "Fechas de referencia pública, redondeadas: verifica en la fuente.", ev,
                        (3, "Del impacto al resultado: 15 días"), "La misión duró 10 meses y terminó en un evento de segundos: el impacto.",
                        "Línea de tiempo con ocho hitos desde el lanzamiento de 2021 hasta la llegada prevista de la misión Hera.")


def periodo() -> str:
    pts = [(b / 10, lab.cambio_periodo(lab.impacto(b / 10))["min"]) for b in range(0, 61, 2)]
    return lineas("Cuánto cambia el período con el factor β", "Minutos que se acorta el período de Dimorphos según el modelo (impacto frontal)",
                  [("Modelo", pts, VERDE)], "Factor de aumento β", "minutos", [0, 1, 2, 3, 4, 5, 6], [0, 20, 40, 60, 80],
                  [(3.3, lab.cambio_periodo(lab.impacto(3.3))["min"], "≈ 33 min")],
                  nota="Con β = 1 solo contaría la nave; lo observado exige β ≈ 3,3 a 3,6: los restos expulsados triplicaron el efecto.",
                  desc="Recta creciente: el acortamiento del período crece con β; la medición de ≈ 33 minutos corresponde a β cercano a 3,3.")


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for n, f in (("geometria_del_impacto", geometria), ("linea_de_tiempo", tiempo), ("efecto_del_impacto", periodo)):
        (SALIDA / f"{n}.svg").write_text(f(), encoding="utf-8")
        print("figuras/" + n + ".svg")


if __name__ == "__main__":
    main()
