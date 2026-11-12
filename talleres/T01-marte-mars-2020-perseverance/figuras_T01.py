# SPDX-License-Identifier: Apache-2.0
"""Genera las figuras SVG del taller T01 a partir del mismo modelo del laboratorio.

Salida: carpeta `figuras/` con SVG autónomos (fondo blanco, texto oscuro: se leen en pantalla, en PDF y en modo oscuro).
UNIDADES: UA (trayectoria), s (entrada), kg (masas), W y años (potencia).
SISTEMA DE REFERENCIA: plano de la eclíptica visto desde el norte, Sol en el origen, órbitas circulares y coplanares.
TOLERANCIA: esquemas de diseño preliminar; las posiciones angulares salen del modelo (±1°), no de efemérides.
Uso: python figuras_T01.py
"""
from __future__ import annotations

import math
from pathlib import Path

import laboratorio_T01 as lab

SALIDA = Path(__file__).resolve().parent / "figuras"
FONDO, TINTA, SUAVE = "#ffffff", "#1d2733", "#5b6b7c"
TIERRA, MARTE, RUTA, SOL = "#1f77b4", "#c1440e", "#2a7f62", "#e0a800"
FUENTE = "font-family=\"Segoe UI, Arial, sans-serif\""


def _svg(ancho: int, alto: int, titulo: str, descripcion: str, cuerpo: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}" '
            f'role="img" aria-labelledby="t d"><title id="t">{titulo}</title><desc id="d">{descripcion}</desc>'
            f'<rect width="{ancho}" height="{alto}" fill="{FONDO}"/>{cuerpo}</svg>')


def _t(x, y, s, tam=14, color=TINTA, anchor="start", peso="normal") -> str:
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{tam}" fill="{color}" text-anchor="{anchor}" font-weight="{peso}" {FUENTE}>{s}</text>'


def trayectoria() -> str:
    cx, cy, esc = 350.0, 330.0, 150.0  # px por UA
    a_t, a_m = 1.0, lab.A_MARTE / lab.UA
    h = lab.hohmann(lab.A_TIERRA, lab.A_MARTE)
    fase = math.pi - h["n2"] * h["t_vuelo_s"]  # Marte por delante de la Tierra al salir
    rp, ra = a_t, a_m
    a, e = (rp + ra) / 2, (ra - rp) / (ra + rp)

    def pto(r, ang):
        return cx + esc * r * math.cos(ang), cy - esc * r * math.sin(ang)

    pts = []
    for i in range(0, 181, 3):
        th = math.radians(i)
        r = a * (1 - e * e) / (1 + e * math.cos(th))
        pts.append(pto(r, th))
    ruta = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    t0x, t0y = pto(a_t, 0)
    m0x, m0y = pto(a_m, fase)
    m1x, m1y = pto(a_m, math.pi)
    t1x, t1y = pto(a_t, math.pi)  # Tierra a la llegada (a 180° del punto de salida + movimiento): se calcula abajo
    ang_t_llegada = h["n1"] * h["t_vuelo_s"]
    t1x, t1y = pto(a_t, ang_t_llegada)
    # arco de la órbita de Marte recorrido durante el vuelo
    arco = "M" + " L".join("%.1f,%.1f" % pto(a_m, fase + (math.pi - fase) * i / 40) for i in range(41))
    c = []
    c.append(f'<circle cx="{cx}" cy="{cy}" r="{esc * a_t:.1f}" fill="none" stroke="{TIERRA}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    c.append(f'<circle cx="{cx}" cy="{cy}" r="{esc * a_m:.1f}" fill="none" stroke="{MARTE}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    c.append(f'<path d="{arco}" fill="none" stroke="{MARTE}" stroke-width="3" opacity="0.55"/>')
    c.append(f'<path d="{ruta}" fill="none" stroke="{RUTA}" stroke-width="3.5"/>')
    c.append(f'<line x1="{cx}" y1="{cy}" x2="{t0x:.1f}" y2="{t0y:.1f}" stroke="{SUAVE}" stroke-width="1"/>')
    c.append(f'<line x1="{cx}" y1="{cy}" x2="{m0x:.1f}" y2="{m0y:.1f}" stroke="{SUAVE}" stroke-width="1"/>')
    # ángulo de fase
    r_arco = 48
    ax0, ay0 = cx + r_arco, cy
    ax1, ay1 = cx + r_arco * math.cos(fase), cy - r_arco * math.sin(fase)
    c.append(f'<path d="M{ax0:.1f},{ay0:.1f} A{r_arco},{r_arco} 0 0 0 {ax1:.1f},{ay1:.1f}" fill="none" stroke="{TINTA}" stroke-width="1.5"/>')
    c.append(_t(cx + 56, cy - 14, f"{math.degrees(fase):.0f}°", 14, TINTA, "start", "bold"))
    c.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="{SOL}"/>')
    c.append(_t(cx, cy + 34, "Sol", 14, TINTA, "middle"))
    for (x, y, col) in ((t0x, t0y, TIERRA), (t1x, t1y, TIERRA), (m0x, m0y, MARTE), (m1x, m1y, MARTE)):
        c.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{col}" stroke="#fff" stroke-width="1.5"/>')
    c.append(_t(t0x + 12, t0y + 22, "Tierra al partir (día 0)", 13, TIERRA, "start", "bold"))
    c.append(_t(m0x + 10, m0y - 10, "Marte al partir", 13, MARTE, "start", "bold"))
    c.append(_t(24, m1y - 16, f"Marte a la llegada (día {h['t_vuelo_s'] / 86400:.0f})", 13, MARTE, "start", "bold"))
    c.append(_t(t1x - 14, t1y + 22, "Tierra a la llegada", 13, TIERRA, "end", "bold"))
    c.append(_t(cx - 60, cy - esc * a * 1.1 + 4, "Órbita de transferencia", 14, RUTA, "end", "bold"))
    c.append(_t(cx + 6, cy + esc * a_m + 22, "Órbita de Marte (1,52 UA)", 13, MARTE, "middle"))
    ex, ey = pto(a_t, math.radians(-50))
    c.append(_t(ex + 12, ey + 14, "Órbita de la Tierra (1 UA)", 13, TIERRA, "start"))
    c.append(_t(24, 36, "Transferencia Tierra-Marte (Hohmann)", 20, TINTA, "start", "bold"))
    c.append(_t(24, 58, "Plano de la eclíptica visto desde el norte · órbitas circulares y coplanares", 13, SUAVE))
    caja = (f"v∞ salida {h['v_inf_salida']:.2f} km/s · C3 = {h['v_inf_salida'] ** 2:.1f} km²/s² · "
            f"vuelo {h['t_vuelo_s'] / 86400:.0f} días · ventana cada {lab.periodo_sinodico(lab.A_TIERRA, lab.A_MARTE) / 86400:.0f} días")
    c.append(_t(24, 626, caja, 13, TINTA))
    c.append(_t(24, 648, "La misión real voló ≈ 203 días con C3 mayor: ver capítulo 2.", 13, SUAVE))
    return _svg(700, 660, "Transferencia de Hohmann entre la Tierra y Marte",
                "Esquema del plano de la eclíptica con el Sol al centro, la órbita de la Tierra, la de Marte y la elipse de transferencia. "
                f"Marte va {math.degrees(fase):.0f} grados por delante de la Tierra al partir y se encuentran con la nave 259 días después.",
                "".join(c))


def entrada() -> str:
    # (t [s respecto a la interfaz de entrada], etiqueta corta, detalle) — tiempos redondeados, ⚠ verificar
    ev = [(-600, "Separación del crucero", "≈ 10 min antes"),
          (0, "Interfaz de entrada", "≈ 125 km · ≈ 5,4 km/s"),
          (80, "Calentamiento máximo", "escudo térmico de 4,5 m"),
          (240, "Paracaídas", "≈ 11 km · ≈ Mach 1,7"),
          (260, "Sale el escudo", "navegación por el terreno"),
          (330, "Descenso propulsado", "se suelta la cubierta"),
          (400, "Grúa aérea", "el rover baja con cables"),
          (415, "Contacto", "≈ 0,75 m/s")]
    n = len(ev)
    x0, x1, y = 90.0, 910.0, 250.0
    paso = (x1 - x0) / (n - 1)
    c = [_t(24, 36, "Entrada, descenso y aterrizaje de Mars 2020", 20, TINTA, "start", "bold"),
         _t(24, 58, "Eventos en orden, no a escala. Tiempos desde la interfaz de entrada. Cifras redondeadas: verifica.", 13, SUAVE),
         f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{TINTA}" stroke-width="3"/>']
    c.append(f'<rect x="{x0 + paso:.1f}" y="{y - 10}" width="{x1 - x0 - paso:.1f}" height="20" fill="{MARTE}" opacity="0.18"/>')
    c.append(_t((x0 + paso + x1) / 2, y + 150, "≈ 7 minutos de entrada, descenso y aterrizaje, sin control desde la Tierra", 14, MARTE, "middle", "bold"))
    for i, (t_, nombre, det) in enumerate(ev):
        x = x0 + i * paso
        arriba = i % 2 == 0
        y_txt = y - 70 if arriba else y + 62
        c.append(f'<line x1="{x:.1f}" y1="{y}" x2="{x:.1f}" y2="{y_txt + (6 if arriba else -16):.1f}" stroke="{SUAVE}" stroke-width="1"/>')
        c.append(f'<circle cx="{x:.1f}" cy="{y}" r="8" fill="{RUTA if i < n - 1 else MARTE}" stroke="#fff" stroke-width="2"/>')
        ancla = "start" if i == 0 else ("end" if i == n - 1 else "middle")
        etiqueta_t = f"T{t_:+d} s" if t_ else "T = 0"
        c.append(_t(x, y_txt - 20 if arriba else y_txt - 2, etiqueta_t, 12, SUAVE, ancla))
        c.append(_t(x, y_txt, nombre, 13, TINTA, ancla, "bold") if arriba else _t(x, y_txt + 16, nombre, 13, TINTA, ancla, "bold"))
        c.append(_t(x, y_txt + 17, det, 12, SUAVE, ancla) if arriba else _t(x, y_txt + 33, det, 12, SUAVE, ancla))
    c.append(_t(24, 430, "La señal tarda ≈ 11 min hasta la Tierra: cuando llega el aviso de «entrada», el vehículo ya terminó.", 13, TINTA))
    return _svg(980, 460, "Línea de tiempo de entrada, descenso y aterrizaje",
                "Línea de tiempo con ocho eventos desde la separación de la etapa de crucero hasta el contacto con el suelo de Marte, en unos siete minutos.",
                "".join(c))


def masas() -> str:
    datos = [("Rover (con instrumentos)", 1025, "#2a7f62"), ("Etapa de descenso (con combustible)", 2070, "#c1440e"),
             ("Etapa de crucero", 540, "#1f77b4"), ("Escudo y cápsula", 410, "#8a6d3b")]
    total = sum(d[1] for d in datos)
    x0, y0, w = 40, 110, 900
    c = [_t(24, 36, "Reparto aproximado de la masa al lanzamiento", 20, TINTA, "start", "bold"),
         _t(24, 58, f"Total ≈ {total:,} kg. Cifras redondeadas de referencia pública: verifica en la hoja de datos.".replace(",", "."), 13, SUAVE)]
    x = x0
    for i, (n, m, col) in enumerate(datos):
        ancho = w * m / total
        c.append(f'<rect x="{x:.1f}" y="{y0}" width="{ancho:.1f}" height="70" fill="{col}"/>')
        c.append(f'<line x1="{x + ancho / 2:.1f}" y1="{y0 + 70}" x2="{x + ancho / 2:.1f}" y2="{y0 + 90 + (i % 2) * 44}" stroke="{SUAVE}"/>')
        c.append(_t(x + ancho / 2, y0 + 106 + (i % 2) * 44, f"{n}", 13, TINTA, "middle", "bold"))
        c.append(_t(x + ancho / 2, y0 + 123 + (i % 2) * 44, f"{m} kg · {100 * m / total:.0f} %", 13, SUAVE, "middle"))
        x += ancho
    c.append(_t(24, 330, "Lo que llega a la superficie es solo ≈ 25 % de lo que sale de la Tierra hacia Marte: el resto se gasta o se descarta en el camino.", 13, TINTA))
    return _svg(980, 360, "Reparto de masas de Mars 2020",
                "Barra horizontal dividida en cuatro tramos: rover 1025 kilos, etapa de descenso 2070, etapa de crucero 540 y escudo con cápsula trasera 410.",
                "".join(c))


def potencia() -> str:
    x0, y0, w, h = 90.0, 90.0, 800.0, 300.0
    pmax = 120.0
    anios = 15

    def pt(a, p):
        return x0 + a / anios * w, y0 + h - p / pmax * h

    c = [_t(24, 36, "Potencia eléctrica del generador de radioisótopos (MMRTG)", 20, TINTA, "start", "bold"),
         _t(24, 58, "Modelo: 110 W al inicio y degradación exponencial de ≈ 4,8 % anual. Es un modelo simple, no un dato de vuelo.", 13, SUAVE),
         f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="none" stroke="{SUAVE}"/>']
    for p in (0, 30, 60, 90, 120):
        xx, yy = pt(0, p)
        c.append(f'<line x1="{x0}" y1="{yy:.1f}" x2="{x0 + w}" y2="{yy:.1f}" stroke="#e3e8ee"/>')
        c.append(_t(x0 - 10, yy + 4, f"{p}", 12, SUAVE, "end"))
    for a in range(0, anios + 1, 3):
        xx, yy = pt(a, 0)
        c.append(_t(xx, y0 + h + 20, f"{a}", 12, SUAVE, "middle"))
    pts = " ".join("%.1f,%.1f" % pt(a / 10, lab.mmrtg(a / 10)) for a in range(0, anios * 10 + 1))
    c.append(f'<polyline points="{pts}" fill="none" stroke="{RUTA}" stroke-width="3.5"/>')
    for a in (0, 2, 5, 10, 14):
        xx, yy = pt(a, lab.mmrtg(a))
        c.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="5" fill="{RUTA}" stroke="#fff" stroke-width="1.5"/>')
        c.append(_t(xx + (34 if a == 0 else 0), yy - 12, f"{lab.mmrtg(a):.0f} W", 13, TINTA, "middle", "bold"))
    c.append(_t(x0 + w / 2, y0 + h + 44, "Años desde el lanzamiento", 13, TINTA, "middle"))
    c.append(_t(26, y0 + h / 2, "W", 13, TINTA, "middle"))
    return _svg(980, 470, "Potencia del MMRTG en el tiempo",
                "Curva descendente que parte de 110 vatios y baja a unos 56 vatios a los 14 años.", "".join(c))


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for nombre, f in (("trayectoria_hohmann", trayectoria), ("entrada_descenso_aterrizaje", entrada),
                      ("reparto_de_masas", masas), ("potencia_mmrtg", potencia)):
        (SALIDA / f"{nombre}.svg").write_text(f(), encoding="utf-8")
        print("figuras/" + nombre + ".svg")


if __name__ == "__main__":
    main()
